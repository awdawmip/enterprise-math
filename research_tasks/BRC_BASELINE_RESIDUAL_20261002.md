<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "title": "已有数学模型基准下的 BRC 残差拟合与原生规律检验",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "在三个已确认的合成线性系统基准中，区分可跨时间与初值复现的 BRC 残差结构、二阶闭包恒等式和高阶失配；尚无真实数据或通用原生性结论。",
  "next_action": "固定线性衰减、扩散、振荡三组离散系统及正态 iid 创新，复用 brc_transport 的 Affine/EffectHistogram/MomentState，以前 8 步和多个初始条件校准固定正有理权分支，并冻结留出检验。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/src/enterprise_math/brc_transport.py",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/native_semantics_admissibility.json"
  ],
  "evidence_status": "SYNTHETIC_FIRST_ROUND_PROTOCOL_FROZEN_NO_EMPIRICAL_OR_N0_CLAIM",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "synthetic-benchmark",
    "residual",
    "held-out",
    "REUSE_EXECUTED"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "parent_objective_id": "BRC-BASELINE-RESIDUAL-LAWS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "BRC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 已有数学模型基准下的 BRC 残差拟合与原生规律检验

Status: `LOCAL V2 PUBLICATION CANDIDATE / CANONICAL MAIN INTEGRATION PENDING / NO CLAIM`

## 0. Mother question

以用户确认的线性衰减、扩散、振荡三类已有数学模型为基准，使用现有 BRC 残差模式拟合后，哪些残差结构能在留出时间与新初始条件下复现，哪些只是已有二阶闭包、拟合方式或合成基准的结果？本任务完成首轮可复现实验与代数解释，不以拟合优度直接判定原生规律。

## 1. Frozen inputs and scope

来源冻结于 `awdawmip/enterprise-math` main commit `4ef1370c5dfa5fa20ade50906e1df1c544515cfc`：

- `src/enterprise_math/brc_transport.py`：复用 `Affine`、`EffectHistogram`、`MomentState`。
- `research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md`：保留既有 BRC 残差与数学闭包的来源，既有结论不重命名为新发现。
- `native_semantics_admissibility.json`：约束外部基准比较与原生语义主张的层级。

三类基准均为合成离散线性系统，以正态 iid 创新建立精确均值和协方差递推。分别覆盖线性衰减、扩散和振荡；报告须明确写出各模型的矩阵/系数、噪声协方差、初值和时间步，不把模拟样本或期望量当作实测数据。基准的精确均值与协方差是参考对象；如用 Monte Carlo，只作额外核对并披露随机种子、样本量和抽样误差。

BRC 路线限定为现有 `Affine`/`EffectHistogram`/`MomentState` 的正有理权、固定、与状态无关的分支模型。训练仅使用前 8 步及多个初始条件；校准完即冻结参数，再测试第 9 至 64 步和未用于校准的新初始条件。冻结训练/留出划分、拟合目标、误差量和必要数值容差，禁止用留出结果回调参数而仍称其留出。

工具复用状态为 `REUSE_EXECUTED`：当前父研究直接调用现有模块完成实验；具体运行证据由研究报告与脚本保存。已有一阶/二阶数学闭包作为已有结果使用，不构成方法新颖性。外部高斯模型与其 BRC 表示的拟合比较只作 N1/N2 比较，不因拟合成功提升为 N0 原生结论，不赋予 Working Truth 或 正典晋升。

必须保留协方差及四阶累积量的分层证据；包括相同二阶而不同四阶的反例、非线性观测 `X^2` 的闭包边界、时变噪声对固定齐次分支假设的负对照。范围限这三类模型；不外推任意非线性系统、任意噪声、任意观测或真实系统。

## 2. Hard target and required outputs

提交一套可从冻结输入重跑的首轮结果，包含：

1. 明确三类离散线性基准及正态 iid 创新的定义，推导其精确均值、协方差递推；标注既有定理/闭包与本轮推导的区别。
2. 校准和留出实验脚本，记录分支、正有理权、参数、多个训练初值、新留出初值、前 8 步训练和第 9 至 64 步留出划分、误差度量、容差及软件依赖。参数冻结后保存逐模型/逐时间的均值和协方差残差。
3. 三类结果和对应代数解释，判别残差是否为精确闭包恒等式、校准误差或真正未解释的稳定结构。报告不得以训练误差小代替留出证据。
4. 四阶累积量计算与“同二阶、不同四阶”的明确可核对反例，证明一二阶匹配不决定完整分布；报告 `X^2` 观测何时需要四阶信息及现有状态闭包的适用边界。
5. 时变噪声负对照：固定齐次分支若不能表达逐时创新方差，应显示相应留出失配；不得临时改成时变分支后称原模型通过。
6. 汇总报告、机器可读结果、精确/数值核验与文件清单。清楚标识 synthetic、N1/N2、三类范围、非新闭包及未解决问题；任何负结果同等保留。

研究代码、报告和结果是可继续研究的证据。本地 V2 文件准备完成不等于 main 可见或正式执行授权；本轮实验由已登记 activity 的 direct `TASK_RESEARCH` 进行，直到正式 main 集成和 CLAIM 另行成立。

## 3. Research value to preserve

把“残差有没有原生规律”拆成可检验的层级：二阶矩输运是否跨时间/初值成立、四阶信息是否区分二阶等价模型、非线性观测与非齐次噪声何时突破表示边界。由合成真值、严格留出和反例同时界定 BRC 拟合能力，避免将已有闭包或漂亮曲线误认成普遍原生规律。即使得到的是完全解释的零二阶残差或明确失配，也应保留其精确适用条件和反例。

## 4. Success, kill, and return criteria

成功条件：三类模型的训练/留出均完成且可重跑；均值、协方差和四阶诊断都有明确结果；同二阶不同四阶反例、`X^2` 边界和时变噪声负对照均完成；每个结论标注其代数证明、精确计算或有限数值证据级别；源代码及结果足以独立复核。

Kill/no-go 条件：只有拟合优度、只看训练集、把既有闭包当新发现、把一二阶相等当作完整分布相等，或从本三类 N1/N2 比较直接宣称通用 N0 原生性，均不得作为通过或晋升理由。若某模型不能由固定正有理权且与状态无关的分支表达，返回明确差异与失败证据，不隐式扩充模型类。数值容差不足、训练/留出污染或不可复现结果须先修正或如实标记失败。

返回条件：完成上述首轮输出与证据核验后返回，包括通过、负对照预期失配及剩余限制；明确结论仅覆盖线性衰减、扩散、振荡三类的冻结设置。首轮通过不自动开启第二轮、其他模型或新理论任务。任务登记、拟合成功和有限计算均不授予数学接受、Working Truth、N0 或 正典晋升。
