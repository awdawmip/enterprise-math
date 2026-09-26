# Shor 模拟新路线：单活动控制位、完整残差、精确终端抽样

Progress-Event-ID: sep26-shor-streaming-closure-0c08f0
Researcher-ID: EM-DIRECT-0C08F0 / TASK_RESEARCH
Activity: RA-40F334CAC4876C16B82B0215
Status: AUTHOR_EXECUTED / DIRECTED_SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED

本轮按用户“从原对话不同角度试图闭合 Shor 模拟算法”的指令，完成了一条终端算法路线。它直接给出完整测量历史、抽样与因数/失败输出，不再通过增加 39/58/146 个局部统计量推进。

## 已完成的闭合

对原 Stage80 实际固定 BRC 字和相同输入 `(N,a,t)`，证明并实现：每轮只准备一位活动控制位，执行输入驱动的模乘、按先前测量记录执行有序相位字、读出并回收该控制位。工作寄存器与全部 61 个内部模式连续保留；同一个 spectator 通过两次 H4 精确回到零，没有重置或删除残差。

完整递归为 `v_(h r)=(I+(-1)^r (M_i ⊗ T_(i,h)))v_h/2`。`T` 必须按原相位字顺序组成，不假设不同残差相位可交换。所有终端工作/内部幅度与原全控制执行逐项相等。因此新表示误差严格为零，原相位编译误差仍按原证书保留。

- 三组全叶核验：`(15,2,4)`、`(21,2,6)`、`(15,14,4)`，共 24,400 个完整幅度坐标比较；联合概率、所有控制输出、后处理因数和失败分布完全相同。两条等价实现分别核验，数字没有把两次重复计为不同坐标。
- N21/t6：流式每个前缀的单轨迹状态峰值 12 端点 / 732 个实标量槽；原全控制宏步骤峰值 380 端点。验证时枚举全部叶仍承担 64 叶的额外存储，不能把验证程序冒称单轨迹内存。
- 实际接通外部均匀随机整数接口、CF/gcd、零相位重试、有限尝试停止、底数策略与非互素底数预检查。12 组驱动检查通过；含 15→3,5 和 21→3,7 的可能历史重放。指定历史与种子是测试，不是无偏随机性或成功频率的证据。随机源耗尽与底数列表耗尽分开返回；前者保留实际历史及完整原始状态，不把未完成结果悄悄剔除。
- 标准 N21/a2/t10 的一条 k171 轨迹，无完整直方图输入即可执行；其精确概率与冻结 Stage80 全分布中对应项完全相等，后处理返回 3、7。此项不是新跑全部 t10 叶。
- 额外修复一处真实深相位接口：固定 32 位网格在 m33 首次出现合法零下端点，原严格正断言失败。零根端点扩展用相同实际 BRC 观察器验证到 m34，没有提高精度或生成新相位 bank。34 位完整 Shor 尚未运行。

主证明：[STREAMING_SHOR_PROOF.md](math_route/STREAMING_SHOR_PROOF.md)。执行器：[terminal_instrument.py](algorithm_intake/terminal_instrument.py)。驱动：[shor_driver.py](driver/shor_driver.py)。完整原生执行与分支证据见 `algorithm_intake/terminal_output/`、`driver/DRIVER_RESULTS.json`；深相位失败和修补见 `adversarial/ADVERSARIAL_AUDIT.md`。

## 结论的边界

闭合的是已认证固定门库上的终端模拟和因数寻找程序：不依赖未知阶或因数输入，保留失败，并精确保留原完整算法的输出语义。已测控制位以后不能被再次相干访问；允许此类未来的 Stage87 压缩问题仍是另一合同。

这不是一般多项式时间经典分解：工作寄存器仍约有 N 个标签，原 `modular_columns` 冷认证还构造 N² 稠密图并做 N³ 级有理运算。也未证明物理 Born 定律或自主六轴接线。外部精确随机接口是数学假设；从公平位实现条件有理抽样时，拒绝采样几乎必然终止，但不保证固定最坏位数。有限重试仍可能返回 RETRY_LIMIT，不输出伪因数。

## 输入来源与复现

输入仓库冻结 HEAD `0852cad130c1d877174d235687cf60c19f318c58`，Drive bundle `1ox9qTtXGbN0p6Zma29uXtBXM6FcOOXhV`，61,398,315 bytes，SHA256 `a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c`。恢复副本后设置 `BRC_STAGE87_SOURCE` 为其路径；所有新文件位于本交付目录，未修改冻结输入。

```
python algorithm_intake/terminal_instrument.py
python driver/run_driver_checks.py
python math_route/check_shared_spectator.py
```

执行器具体参数以其 README 和 `--help` 为准。源码、证明和逐项证书都是接续输入；没有执行工具的网页/客户端对话可以直接进行证明核验、错误界分析或下述接口推导，工具可用者再产生新实算证据。不可把未执行写成执行成功。

## 下一对话直接可做的研究

优先核验并改进剩余真实成本：在相同 BRC 类型合同下，把模乘置换的稠密图认证改为保留来源的稀疏置换证书。输入只允许 N、a 与已知控制指数；不得先求阶，再伪造 Shor 测量。先证明串接/控制直和/反向与原核逐列相同，然后给有限输入的完整列证书和资源账；纯证明也形成可发布进展，不以工具缺失当作数学阻断。

第二条可续接：审阅零端点扩展如何接入完整 bank 编译器，证明每个请求位宽的实际总误差界；固定主 bank 和历史结果保留。m34 的端点验证不等于 34 位整机已验收。

本文件是科研交付与续接包，不创建正式 Task/CLAIM/Result，不借用其他驾驶员或研究员身份；后续评审必须如实声明共享上下文。原生会话登记只授予本轮持久化/执行身份，不授予数学准入。

## 复用与先行工作

当前 `enterprise_toolbox_registry.json`（Source c412dcb62f4b27189afd8e5748ff5f8dbb3c17dd）T0_BRC 覆盖带来源的支路/合流与组合语义；其固定 degree-two affine 子工具不自动覆盖本完整工作×61 模式历史。分类为已有 BRC 固定字、Stage56/58 有理抽样与 Stage78 后处理的 REUSE/COMPOSITION，新增有边界的调度等价证明与 Shor 接口，未擅自登记为通用工具。

总体方法有先行研究：[Griffiths–Niu 半经典 Fourier 变换](https://arxiv.org/abs/quant-ph/9511007)、[单控制位 Shor 模拟](https://arxiv.org/abs/0809.4416)。本轮贡献是它们在真实残差 BRC 固定字上的严格适配与可复验实现，不宣称半经典方法首创。仅读取官方摘要，不冒称全文新颖性审查。

Global-Knowledge-Sync: main@6dff66c / GLOBAL_KNOWLEDGE_V1
