# 近期研究综合：跨机制边界、可组合信息与完整成本

日期：2026-10-02。状态：`BOUNDED_PORTFOLIO_SYNTHESIS / NO_FORMAL_MATHEMATICAL_DISPOSITION`。

本文件保存委派只读研究核查的综合判断，供当前父执行者作组合决策。它不创建研究身份、CLAIM、正式 Review、数学接受或新任务。当前 live/native 状态及最终 main 由父执行者另行绑定；此处采用固定 Source `3920cc33ca6fa586dc1d9b13b4292ab11ddd4cf7`，不把静态出版字段当作当前 owner 或执行权限。

## 最新实质增量

相比前次组合核查，新增的数学材料主要是 BRC 跨模型类型扩展。它把“某些例子出现反平方”推进为一组明确的适用条件、闭包反例与不同长期行为。Source 在该扩展之后的三个提交主要修复验证和保存控制状态；没有据此认定其他研究线新增了已完成数学结果。

最新出版为 `RS-BRC-BASELINE-RESIDUAL-20261002 / TP2-C8ACA99CAEFA8E281E3E`，generation 5，supersede `TP2-3DE3CA9E9F75E8F5D084`。固定 Source 的 publication 与 taskbook Git blob 绑定实际核验一致。其下一步是消费已完成报告并审核范围，不是默认重跑或继续无限扩展模型。

归档为官方仓库 commit `46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c` 下 `experiments/brc_expanded_types_20261002_fca717/`。本次通过现有 official origin 取得精确 commit，实际读取完整报告、summary、相关机制推导、图边界和动力学交叉检查；summary 所列七个源码/结果文件的 SHA-256 全部与真实 Git 字节一致。详细字节证据、读取范围与未执行范围见 [BRC_EXPANDED_EVIDENCE_READBACK_20261002.json](BRC_EXPANDED_EVIDENCE_READBACK_20261002.json)。

主要原件：

- [REPORT.md](https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/REPORT.md)，SHA-256 `2595d65a0b88af982ba438b41806e14270caf737ebed14293e6820a66fdc12e0`。
- [summary.json](https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/summary.json)，SHA-256 `cd3cdbd90225e3b99313bcaf236981e138f4ee5f5464fb70e8b3c92744142b48`。
- [RELATED_BRANCHES.md](https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/RELATED_BRANCHES.md)、[GRAPH_BOUNDARIES.md](https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/GRAPH_BOUNDARIES.md)、[DYNAMICS_REVIEW.md](https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/DYNAMICS_REVIEW.md)。

## BRC 结果应以机制与观察者分类

报告包含十一类机制，其中保留控制；积分噪声与线性响应权重属于同一机制。它们不构成十一个独立盲实验，核验计数也不能相加成独立样本数。实际归档出现幂律、指数行为、非零平台、周期、最终增长以及标准化量未定义，反平方不是这组模型中残差的统一规律。

| 结构 | 最值得保留的有界结果 | 对后续研究的约束 |
| --- | --- | --- |
| 独立对称加权符号和 | `gamma4=-2/N_eff`，其中 `N_eff=(sum a_j²)²/sum a_j⁴`。`j` 权重按时间约 `1/n`，按 RMS 宽度却为 `ell^(-2/3)`；几何权重可有非零平台。 | 时间、RMS 宽度和物体间距离不能互换；公式依赖声明的独立性与权重。 |
| 相关创新 | `rho=-1/2` 的前十六步拟合系数约 `-0.8890`，长期推导系数为 `+2`；`rho=-1` 的偶数正时点方差为零，标准化量记为 `null`。 | 保留隐藏控制态、混合假设、有限时修正与未定义原因；早期拟合不能代替渐近证明。 |
| 非线性与状态依赖 | logistic 两初态具有同均值方差而下一步方差不同；lazy Ehrenfest 在状态依赖下仍有精确二阶闭包。 | 问题是具体转移是否保持观察量的充分性；不能概括为“状态依赖总会/总不会破坏闭包”。 |
| 随机乘子 | 标准化四阶量最终按 `(353/289)^n` 增长，早期负值与 `n=3` 变号保留。 | 均值正确不保证高阶形状趋于高斯；最终增长不自动等于逐时单调。 |
| 图、吸收与尾部 | 无停留吸收模型质量衰减但条件形状保持两周期；图谱、割权和归一化改变速率；无限重尾所需矩可不存在。 | 无条件质量与条件形状分别报告；有限截断不能替代原分布矩存在性，也不能推出无限图或真实空间力律。 |

归档 summary 的 `PASS` 和检查计数属于作者完成的有限实现证据。本次没有复跑这些程序，也没有重做 S15。全时间陈述依赖相应代数或谱推导；字节一致性不等于证明正确。动力学材料如实披露研究内交叉检查与共享工作来源，不构成盲审或正式 Driver 接受。

## 研究线之间应合成合同，不混合对象

当前可复用的共同问题是：压缩后是否保留允许的未来观察所需信息，以及证明和维护这个压缩是否比完整计算便宜。T6 的纤维常值/未来观察合同与完整成本记账可作为共同审查框架，但不能把一种对象的结论搬成另一种对象的定理。

BRC 的正质量 Markov/端点基准不证明 signed-amplitude QFT 干涉、p-adic 模谱或 CFD 复系数状态的充分性。logistic 同低阶矩而未来可区分的反例可帮助明确 R004 的问题结构，但不能代替其有限模上的同谱碰撞证书。壳平均与条件形状的区分也不能直接作为真实引力或外部物理机制。

本次没有取得真实观测数据、一般非线性或波动 PDE 分类、一般无限图定理、普遍残差衰减律、N0 或引力结论。上述缺口不能仅因未覆盖就自动变成新任务；必须先有具体模型、允许观察、可区分结果和停止条件。

## 优先消费的已有任务

以下是基于现有出版与已读取证据的组合建议，不是实时 claimability、owner 或正式优先级变更。正式派发仍用当前规范入口。

| 建议动作 | 既有任务/范围 | 最小有信息增量的单元 |
| --- | --- | --- |
| 审核最新 BRC 范围 | `RS-BRC-BASELINE-RESIDUAL-20261002`，最新 `TP2-C8ACA99CAEFA8E281E3E` | 消费归档，核对闭包、相关谱、边界归一化与证据强度；不再发布泛“扩大类型”或默认重跑。 |
| 推进可组合充分性 | `RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930` | 冻结未来语言，证明受限充分性或给出同谱而未来可区分的模；不把坐标单调误写成次模性。 |
| 合成算法分支 | `RS-BRC-SHOR-PROJECTED-ALLOCATION-CERTIFICATE-20261002` | 在共同容量、真实扩展见证、费用纤维与全部中间资源的同一合同中接合 S11/S12；保留 S11-S14 负成本证据与 S13 的实际科学计数改善。 |
| 保持 QFT 理论分工 | `RS-QFT-DIRECT-BOUNDED-READOUT-20261002`、`RS-QFT-ORDERED-LANDING-COMPRESSION-20261002`、`RS-QFT-NATIVE-MULTISAMPLE-DECODING-20261002` | 分别闭合可构造读出、表示/收缩宽度、实际联合样本到解码的桥梁；接口交付前不合并为整体高效求阶结论。 |
| 检验真正的扰动后行为 | `RS-R11-ONE-TICK-DELAY-ATLAS-LOCAL-REPAIR-20260930` | 保留已有周期与前沿，核查延迟后完整状态、累计观察及修复总成本；不把线性基准衰减率直接套在带反馈系统上。 |
| 接续实际宿主缺口 | `RS-CFD-SPECTRAL-HYBRID-20260910` 与 `RS-CFD-TRAJECTORY-VERIFY-20260910` | 从现成 static-carrier adapter 与 R23 前沿恢复，补匹配 native 总成本/正确性证据；不重复旧 detector 接入。 |

上述 QFT、BRC-Shor、R004、R11 和 CFD 边界与上一份精确源核查一致；本次没有将重复阅读记为新的科学进展。主报告应另绑定其最新实际 Source/frontier 和 native 状态。

当前更高价值的动作是消费成熟的有限证据与现成任务，明确哪些信息必须保留、哪些费用尚未支付。是否需要新的研究方向，应由这些有界单元揭示的真实余量决定，不能由一次 `PASS`、新的简称或某个环境缺项触发同义续集。
