#!/usr/bin/env python3
"""第 1 章试跑脚本：环境自检 + 最小训练步压测。

不依赖任何上游项目，只用 PyTorch，用来回答三个问题：
  1. 我的设备能不能用来训练语言模型？（CUDA / Apple MPS / CPU）
  2. 训一个 N 参数量的模型，单步要多久、吃多少显存？
  3. 按这个速度，跑完 X 亿 token 大概要多少小时、多少钱？

用法：
    python smoke_test.py                       # 默认按 64M 参数压测
    python smoke_test.py --target-m 350        # 按 350M 参数压测
    python smoke_test.py --seq 1024 --batch 4  # 调序列长度与批大小
    python smoke_test.py --price 24            # 按 $24/小时（8×H100 节点口径）算钱

依赖：PyTorch >= 2.0
说明：本脚本用合成随机数据压测「吞吐与显存」，**不反映真实训练的收敛情况**。
"""
from __future__ import annotations

import argparse
import math
import platform
import time

import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------- 1. 设备自检 ----------

def pick_device() -> "tuple[str, str]":
    if torch.cuda.is_available():
        return "cuda", torch.cuda.get_device_name(0)
    mps = getattr(torch.backends, "mps", None)
    if mps is not None and mps.is_available():
        return "mps", "Apple Silicon (MPS)"
    return "cpu", platform.processor() or "CPU"


def report_device(device: str, name: str) -> None:
    print("=" * 62)
    print("环境自检")
    print("=" * 62)
    print(f"  Python   : {platform.python_version()}")
    print(f"  PyTorch  : {torch.__version__}")
    print(f"  设备     : {device}  ({name})")
    if device == "cuda":
        props = torch.cuda.get_device_properties(0)
        print(f"  显存     : {props.total_memory / 1024 ** 3:.1f} GB")
        print(f"  算力版本 : sm_{props.major}{props.minor}")
        print(f"  可见卡数 : {torch.cuda.device_count()}")
    elif device == "mps":
        print("  显存     : 统一内存（与系统共享）")
    else:
        print("  提示     : 无可用 GPU，只能验证流程，不适合真正训练")


# ---------- 2. 迷你 GPT：结构与真实模型同构，规模可调 ----------

class Block(nn.Module):
    def __init__(self, d_model: int, n_head: int):
        super().__init__()
        self.n_head = n_head
        self.ln1 = nn.LayerNorm(d_model)
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, 4 * d_model, bias=False),
            nn.GELU(),
            nn.Linear(4 * d_model, d_model, bias=False),
        )

    def forward(self, x):
        B, T, C = x.shape
        h = self.ln1(x)
        q, k, v = self.qkv(h).chunk(3, dim=-1)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2)
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        x = x + self.proj(y)
        x = x + self.mlp(self.ln2(x))
        return x


class TinyGPT(nn.Module):
    def __init__(self, vocab: int, d_model: int, n_head: int, n_layer: int, seq: int):
        super().__init__()
        self.tok = nn.Embedding(vocab, d_model)
        self.pos = nn.Embedding(seq, d_model)
        self.blocks = nn.ModuleList([Block(d_model, n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab, bias=False)

    def forward(self, idx):
        B, T = idx.shape
        pos = torch.arange(T, device=idx.device)
        x = self.tok(idx) + self.pos(pos)[None, :, :]
        for blk in self.blocks:
            x = blk(x)
        return self.head(self.ln_f(x))


def solve_width(target_params: int, vocab: int, n_layer: int, seq: int) -> int:
    """由目标参数量反解隐藏维度。

    参数量 ≈ 2*vocab*d（词嵌入+输出头） + 12*n_layer*d^2（Transformer 块） + seq*d + 2*d
    解 12*n_layer*d^2 + (2*vocab + seq + 2)*d - target = 0，再向上取 64 的整数倍。
    """
    b = 2 * vocab + seq + 2
    a = 12 * n_layer
    d = (-b + math.sqrt(b * b + 4 * a * target_params)) / (2 * a)
    return max(64, int(round(d / 64.0)) * 64)


def n_params(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters())


def peak_mem_gb(device: str):
    if device == "cuda":
        return torch.cuda.max_memory_allocated() / 1024 ** 3
    mps = getattr(torch, "mps", None)
    if device == "mps" and mps is not None and hasattr(mps, "current_allocated_memory"):
        return mps.current_allocated_memory() / 1024 ** 3
    return None


# ---------- 3. 压测主流程 ----------

def run(args) -> None:
    device, dev_name = pick_device()
    report_device(device, dev_name)

    vocab, depth, seq, batch = args.vocab, args.depth, args.seq, args.batch
    d_model = solve_width(int(args.target_m * 1e6), vocab, depth, seq)
    n_head = max(1, d_model // 64)
    model = TinyGPT(vocab, d_model, n_head, depth, seq).to(device)
    total = n_params(model)

    print("-" * 62)
    print("测试模型（与真实模型同构，仅规模缩小）")
    print(f"  目标参数量 : {args.target_m:.0f}M")
    print(f"  实际参数量 : {total / 1e6:.1f}M")
    print(f"  层数 / 宽度: {depth} / {d_model}（{n_head} 头，每头 64 维）")
    print(f"  序列长度   : {seq}    批大小: {batch}")
    print(f"  词表大小   : {vocab}（词嵌入+输出头约占 {2 * vocab * d_model / total * 100:.0f}% 参数）")
    print("-" * 62)

    opt = torch.optim.AdamW(model.parameters(), lr=3e-4)
    x = torch.randint(0, vocab, (batch, seq), device=device)
    y = torch.randint(0, vocab, (batch, seq), device=device)

    if device == "cuda":
        torch.cuda.reset_peak_memory_stats()

    model.train()
    timed = []
    for step in range(args.warmup + args.steps):
        t0 = time.perf_counter()
        logits = model(x)
        loss = F.cross_entropy(logits.view(-1, logits.size(-1)), y.view(-1))
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()
        if device == "cuda":
            torch.cuda.synchronize()
        elif device == "mps":
            torch.mps.synchronize()
        dt = time.perf_counter() - t0
        if step >= args.warmup:
            timed.append(dt)
        mem = peak_mem_gb(device)
        mem_s = f"{mem:.2f} GB" if mem else "n/a"
        tag = "预热" if step < args.warmup else "计时"
        print(f"  [{tag}] step {step + 1:>2}  loss={loss.item():.3f}  {dt * 1000:>7.0f} ms  峰值显存={mem_s}")

    step_time = sum(timed) / len(timed)
    tps = (batch * seq) / step_time
    mem = peak_mem_gb(device)

    print("=" * 62)
    print("结果")
    print("=" * 62)
    print(f"  单步耗时 : {step_time * 1000:.0f} ms（{len(timed)} 步均值，已排除预热）")
    print(f"  训练吞吐 : {tps:,.0f} tokens/s")
    print(f"  峰值显存 : {mem:.2f} GB" if mem else "  峰值显存 : 该后端不提供统计")
    for n_tokens, label in ((1e9, "10 亿 token"), (args.budget_b * 1e9, f"{args.budget_b:g} 亿 token")):
        hours = n_tokens / tps / 3600
        print(f"  {label:<11}: 约 {hours:.2f} 小时，按 ${args.price:.0f}/小时 约 ${hours * args.price:.2f}")

    print("-" * 62)
    if device == "cpu":
        print("  判断：当前只能用 CPU 跑通流程。要真正训练，请换有独显的机器或按小时租云卡。")
    elif device == "mps":
        print("  判断：可走小模型路线（MiniMind 级，64M 起步）。注意个别算子需回退 CPU。")
    else:
        vram = torch.cuda.get_device_properties(0).total_memory / 1024 ** 3
        if vram < 16:
            print(f"  判断：{vram:.0f}GB 显存，适合小模型全参预训练（配合梯度累积）。")
        elif vram < 40:
            print(f"  判断：{vram:.0f}GB 显存，小模型全参或 1–3B 级 LoRA 都可行。")
        else:
            print(f"  判断：{vram:.0f}GB 显存，可支撑十亿级模型；多卡可考虑 nanochat 路线。")
    print("  提醒：本结果为合成数据压测，仅用于估算吞吐与显存，不代表真实收敛表现。")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="环境自检 + 最小训练步压测（第 1 章试跑脚本）")
    p.add_argument("--target-m", type=float, default=64, help="目标参数量（百万），默认 64")
    p.add_argument("--depth", type=int, default=8, help="Transformer 层数，默认 8")
    p.add_argument("--seq", type=int, default=512, help="序列长度，默认 512")
    p.add_argument("--batch", type=int, default=8, help="批大小，默认 8")
    p.add_argument("--vocab", type=int, default=32000, help="词表大小，默认 32000")
    p.add_argument("--steps", type=int, default=5, help="计时步数，默认 5")
    p.add_argument("--warmup", type=int, default=2, help="预热步数，默认 2")
    p.add_argument("--budget-b", type=float, default=2.0, help="按多少亿 token 估算总时长，默认 2")
    p.add_argument("--price", type=float, default=3.0, help="每小时算力单价（美元），默认 3")
    return p


if __name__ == "__main__":
    run(build_parser().parse_args())
