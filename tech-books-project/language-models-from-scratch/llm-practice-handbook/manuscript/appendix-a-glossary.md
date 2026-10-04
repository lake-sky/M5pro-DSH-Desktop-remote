# 附录 A · 术语表（中英对照）

全书出现的术语在此统一。首次出现时正文给出英文原词，此处汇总便于查阅。

## A.1 基础与数据

| 中文 | 英文 | 一句话说明 |
| --- | --- | --- |
| 语言模型 | Language Model (LM) | 对 token 序列概率分布建模的模型 |
| 大语言模型 | Large Language Model (LLM) | 参数量与训练数据规模较大的语言模型 |
| 小语言模型 | Small Language Model (SLM) | 可在个人设备训练/推理的语言模型（本书指 10M–1B 级） |
| 词元 | Token | 模型处理的最小文本单位 |
| 分词器 | Tokenizer | 文本 ↔ token 序列的转换器 |
| 词表 | Vocabulary | 全部 token 的集合，大小决定嵌入表规模 |
| 字节对编码 | Byte-Pair Encoding (BPE) | 常用的子词分词算法 |
| 语料 | Corpus | 用于训练/评测的文本集合 |
| 去重 | Deduplication | 删除重复文本（精确/近似）以防记忆与污染 |
| 打包 | Packing | 把多条短样本拼成定长序列以提高利用率 |
| 序列长度 / 上下文长度 | Sequence Length / Context Length | 单次前向能处理的 token 数 |
| 嵌入 | Embedding | 把 token 映射为向量的查表 |
| 位置编码 | Positional Encoding | 让模型感知 token 顺序 |
| 注意力机制 | Attention | 按相关性加权聚合信息的机制 |
| 自注意力 | Self-Attention | 序列内部元素互相注意 |
| 多头注意力 | Multi-Head Attention (MHA) | 多组注意力并行，捕捉不同子空间关系 |
| 因果掩码 | Causal Mask | 遮住未来位置，保证自回归性质 |
| 前馈网络 | Feed-Forward Network (FFN) | Transformer 块中的逐位置非线性变换 |
| 归一化 | Normalization（LayerNorm / RMSNorm） | 稳定训练、控制激活尺度 |
| 残差连接 | Residual Connection | 缓解深层网络的梯度问题 |
| 隐藏维度 / 宽度 | Hidden Dimension / Width | 表示空间的向量维度 |
| 深度 | Depth | Transformer 层的数量（nanochat 的 `--depth` 旋钮） |
| 参数量 | Parameter Count | 模型可训练权重总数，决定容量与成本 |
| 浮点精度 | Precision（fp32 / tf32 / fp16 / bf16 / fp8） | 数值格式，直接影响显存与速度 |

## A.2 训练

| 中文 | 英文 | 一句话说明 |
| --- | --- | --- |
| 预训练 | Pretraining | 在大规模通用语料上做下一 token 预测 |
| 继续预训练 / 领域自适应预训练 | Continued / Domain-Adaptive Pretraining (DAPT) | 用领域语料在已有模型上继续预训练 |
| 微调 | Fine-tuning | 在下游数据上继续训练 |
| 监督微调 | Supervised Fine-Tuning (SFT) | 用「指令—回答」样本教模型怎么答 |
| 指令微调 | Instruction Tuning | 同 SFT，强调遵循指令 |
| 低秩适配 | Low-Rank Adaptation (LoRA) | 只训练低秩旁路矩阵，显存友好 |
| 量化低秩适配 | QLoRA | 基座量化后再挂 LoRA |
| 全参微调 | Full Fine-tuning | 更新全部参数，成本最高 |
| 偏好对齐 | Preference Alignment | 让输出更符合人类偏好 |
| 直接偏好优化 | Direct Preference Optimization (DPO) | 用偏好对直接优化，无需奖励模型 |
| 基于人类反馈的强化学习 | RLHF | 训练奖励模型 + 强化学习对齐 |
| 批大小 | Batch Size | 一次参数更新用到的样本数 |
| 梯度累积 | Gradient Accumulation | 小批多次累积，等效大批量 |
| 学习率 | Learning Rate | 步长；最关键的超参之一 |
| 学习率预热 | Warmup | 训练初期逐步升高学习率 |
| 权重衰减 | Weight Decay | 正则化项，抑制权重过大 |
| 混合精度训练 | Mixed-Precision Training | bf16/fp16 前向反向 + fp32 主权重 |
| 梯度检查点 | Gradient Checkpointing | 用计算换显存，重算激活值 |
| 优化器 | Optimizer（如 AdamW） | 参数更新算法，AdamW 需额外优化器状态显存 |
| 分布式数据并行 | Distributed Data Parallel (DDP) | 每卡一份模型、切分数据、同步梯度 |
| 全分片数据并行 | Fully Sharded Data Parallel (FSDP) | 参数/梯度/优化器状态分片，省显存 |
| 检查点 | Checkpoint | 训练中间状态的存档 |
| 断点续训 | Resume | 从检查点继续训练 |
| 灾难性遗忘 | Catastrophic Forgetting | 学新领域后通用能力退化 |
| 过拟合 / 欠拟合 | Overfitting / Underfitting | 训练集太好/太差而泛化不行 |
| 随机种子 | Random Seed | 决定随机性，复现实验必须固定 |

## A.3 评测

| 中文 | 英文 | 一句话说明 |
| --- | --- | --- |
| 困惑度 | Perplexity | 交叉熵的指数形式；越低越好，但不可跨词表直接比较 |
| 交叉熵损失 | Cross-Entropy Loss | 语言模型的训练目标 |
| 比特每字节 | Bits Per Byte (BPB)，训练中常看 `val_bpb` | 与词表无关的损失口径，便于跨分词器比较 |
| CORE 分数 | DCLM CORE | nanochat 采用的能力综合分；GPT-2 基线约 0.2565【源】 |
| 基准 | Benchmark | 标准化评测集 |
| 评测集污染 | Benchmark Contamination | 训练数据混入评测内容，分数虚高 |
| 消融实验 | Ablation Study | 控制变量，验证某项改动是否真的有效 |
| 基线 | Baseline | 对比参照（如未微调的原模型） |
| 回归集 | Regression Set | 每次迭代都要重跑的固定测试集 |
| 人工评估 | Human Evaluation | 主观质量（讲解是否清楚）只能靠人来评 |

## A.4 推理与部署

| 中文 | 英文 | 一句话说明 |
| --- | --- | --- |
| 推理 | Inference | 用训练好的模型生成输出 |
| 自回归生成 | Autoregressive Generation | 一个 token 接一个 token 地生成 |
| 键值缓存 | KV Cache | 缓存历史 K/V 免重复计算；显存随序列长度线性增长 |
| 采样 | Sampling | 从概率分布中挑下一个 token |
| 温度 | Temperature | 控制随机性，越高越发散 |
| 核采样 | Nucleus Sampling (top-p) | 只在累积概率前 p 的候选里采样 |
| 贪心解码 | Greedy Decoding | 每步取最大概率；稳定但易复读 |
| 束搜索 | Beam Search | 同时保留多条候选路径 |
| 重复惩罚 | Repetition Penalty | 抑制复读 |
| 首词元时延 | Time to First Token (TTFT) | 用户感知到的「反应速度」 |
| 吞吐量 | Throughput | 每秒生成/处理的 token 数 |
| 量化 | Quantization | 用低比特表示权重（8-bit / 4-bit），省显存、可能掉点 |
| 知识蒸馏 | Knowledge Distillation | 用大模型教小模型 |
| 服务化 | Serving | 把模型封装成 API / 服务 |
| 提示工程 | Prompt Engineering | 不改权重，只改输入来引导输出 |
| 系统提示 | System Prompt | 设定角色与规则的固定前缀 |
| 上下文窗口 | Context Window | 单次能容纳的 token 上限 |
| 检索增强生成 | Retrieval-Augmented Generation (RAG) | 先检索资料再生成，事实由外部提供 |
| 工具调用 | Tool / Function Calling | 让模型调用外部函数获取事实 |
| 幻觉 | Hallucination | 一本正经地编造 |
| 拒答 | Refusal | 明确表示不会或不确定 |

## A.5 垂直领域（第二部分：小学语文教学辅导）

| 中文 | 英文 | 说明 |
| --- | --- | --- |
| 笔画 | Stroke | 构成汉字的最小书写单位 |
| 笔顺 | Stroke Order | 书写顺序，有国家标准 |
| 部首 | Radical | 字典检索用的部件 |
| 偏旁 | Component | 合体字的构成部件 |
| 汉字结构 | Character Structure | 左右 / 上下 / 包围 / 独体 等 |
| 多音字 | Polyphonic Character | 一字多音 |
| 声调 | Tone | 普通话四声 |
| 拼音 | Pinyin | 拉丁字母注音 |
| 形近字 | Visually Similar Characters | 字形相近易混（如「己 / 已 / 巳」） |
| 音近字 | Phonetically Similar Characters | 读音相近易混 |
| 易错字 | Commonly Misspelled Character | 学生高频写错的字 |
| 通用规范汉字表 | Table of General Standard Chinese Characters | 汉字规范依据 |
| 国家语委 | National Language Commission | 语言文字规范发布机构 |
