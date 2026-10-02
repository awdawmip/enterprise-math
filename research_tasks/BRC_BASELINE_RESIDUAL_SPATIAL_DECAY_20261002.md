<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "title": "BRC 残差的尺度衰减与壳层平均：反平方候选及适用边界",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "用户明确继续授权的残差尺度/空间衰减扩展已完成：1728个生产矩检查、48个显式支路卷积、12个壳计数、20层实际局部CWM传播及17项生产模块回归通过；已归档统计ell^-2、壳均1/(24r²+2)、其绝对/相对模型残差r^-4/r^-2以及角点指数反例。保留首轮1024个矩核验；没有正式CLAIM、Driver裁定、引力发现或N0结论。",
  "next_action": "从本轮不可变报告恢复已完成前沿，评审标准化高阶律、壳均残差及局部outward Moore端点CWM反例的适用范围；不重复首轮或本轮已完成校准、枚举和传播。只有未来明确原生距离、源—探针耦合等新信息缺口时再立新研究。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/src/enterprise_math/brc_transport.py",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/native_semantics_admissibility.json",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/METHOD_AUDIT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/METHOD_AUDIT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/run_spatial_decay.py"
  ],
  "evidence_status": "SPATIAL_DECAY_DIRECT_RESEARCH_COMPLETE_SOURCE_VERIFIED_NO_CLAIM_DRIVER_VERDICT_GRAVITY_OR_N0",
  "last_progress_ref": "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/REPORT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "synthetic-benchmark",
    "residual",
    "spatial-decay",
    "cumulants",
    "shell-average",
    "local-outward-Moore-CWM",
    "completed-direct-research",
    "scope-revision"
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

# BRC 残差的尺度衰减与壳层平均：反平方候选及适用边界

Status: V2 task registration; execution authority is separate; the completed direct-research extension is tracked by its activity and verified report.

本修订沿用 `RS-BRC-BASELINE-RESIDUAL-20261002` 及 `DIRECT_USER_DIRECTION`，把用户明确“继续”的新指令纳入同一任务范围。修订前 publication 为 `TP2-C298C50695BD0B52E74D`；本代明确 supersede 该记录，原记录及其 taskbook 字节保持不变。本轮为已完成的 direct `TASK_RESEARCH` 扩展，不创建正式 CLAIM，不声称 Driver 裁定或 N0。以下问题、范围和硬目标保留为本轮协议及评审依据，执行接续从已完成前沿开始。

## 0. Mother question

承接用户“继续，考虑残差衰减可能像万有引力一样衰减等等”的明确扩展，检验 BRC 高阶残差在何种合成模型和观测尺度下呈现反平方形式；区分随时间累积的标准化残差经 RMS 宽度重参数化后的衰减，与源到探针距离上的壳层平均稀释。两者是否有共同指数、各需什么假设，以及哪些对照会破坏该指数，构成本轮检验问题，结果与反例已按下述不可变证据归档。指数形式相似不等同于已经构造吸引力或导出万有引力。

## 1. Frozen inputs and scope

### 继承的已验证前沿

首轮线性衰减、扩散和振荡三类合成基准已经完成精确校准、1024 个矩核验及高阶律/反例，活动为 `RA-BRC-BENCHMARK-20261002-FCA717`。首轮报告、结果和方法审计已由父执行在 commit `8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e` 逐字节远程读回；完整不可变链接保留于 frontmatter `source_refs`。恢复这些结果，不默认重跑已完成校准与枚举。

现有 BRC 模块与语义约束仍冻结于 commit `4ef1370c5dfa5fa20ade50906e1df1c544515cfc`：`src/enterprise_math/brc_transport.py`、`research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md`、`native_semantics_admissibility.json`。首轮已有工具复用证据继续保留；本扩展的实际复用、组合和局部端点 CWM 构造在本轮 `METHOD_AUDIT.md` 中列明。既有生产模块共 17 项回归通过；本轮执行证据来自归档代码和结果，不由任务登记文字代替。

### A. 累积量与 RMS 宽度路线

检验标准化四阶残差的候选时间率 `1/t`，在明示 `ell^2 ~ t` 的扩散尺度条件下是否转写为 `ell^-2`。同时检验一般标准化累积量候选 `ell^(2-p)`：明确 `p`、所用投影或分量、中心化、方差归一化、矩存在性、相关性及非零系数条件，区分精确等式、渐近率和有限区间数值拟合。各公式的本轮证据与适用条件以已归档报告为准；任务登记本身不构成证明。

包含 `d` 维 toy 轴步进与同协方差、不同高阶累积量的分支反例。必须报告常数、符号或抵消项，不能只比较 log-log 斜率。对 persistent/持续相关、均值漂移和有限记忆分别明示模型、状态扩展与观测定义，检验其对方差尺度和标准化残差率的影响。中心 RMS 宽度、非中心 RMS 位移和均值运动须分别定义，不能互换。

持续相关或有限记忆模型如超出首轮固定、与状态无关分支的表示范围，应明确标记扩展条件；不得把记忆状态或相关创新隐式塞进原 iid 假设后宣称原模型普遍成立。

### B. 源—探针距离与壳层平均路线

另行使用 `Z^d` 的 Moore 图及整数 `r >= 1` 的 `L_infinity` 壳，核验壳计数 `N(r) = (2r+1)^d - (2r-1)^d`。在明确 BRC 守恒输运、壳总量与归一化约定后检验壳平均质量 `1/N(r)` 的意义及适用条件，比较 `d=3` 的反平方候选、吸收情形以及三叉树的指数情形。

必须写明单位壳总量或守恒通量等归一化假设是否实际由指定模型满足；总质量守恒本身不能省略壳总量和分配规则的定义。壳层平均不自动保证每个点的值相等，须保留各向异性或不均匀分配的可能性。

此处 `r` 是图上的源—探针壳半径；路线 A 的 `ell` 是分布 RMS 宽度。二者不因指数相同就成为同一物理距离。Moore 图、维数、距离度量、分支权和守恒假设都是明确输入，不能作为 BRC 自动导出这些结构的证据。

### 已完成的局部端点 CWM 与衰减前沿

本轮新增构造并实际传播的是局部 outward Moore 邻接端点 CWM：在端点上按局部 outward 邻接规则分配质量，逐层保留端点质量及壳总量，不以预先指定的 shell histogram 或逐壳均匀重分配代替局部过程。20 层实际局部传播已保存；局部立方对称与总量守恒仍允许角点质量 `1/[26*19^(r-1)]` 呈指数形式，故壳平均与点值传播须分开评审。

已完成证据包括 1728 个生产矩检查、48 个显式支路卷积、12 个壳计数、20 层上述局部 CWM 传播和 17 项生产模块回归。统计路线记录了标准化四阶残差 `ell^-2`，同一过程的 `p=3,4,6` 分别给出 `ell^-1, ell^-2, ell^-4`；其观测、归一化和适用假设见报告。壳平均路线在 `d=3` 给出 `1/(24r^2+2)`，与报告定义的反平方渐近模型比较时，绝对与相对模型残差分别呈 `r^-4`、`r^-2`。这些是不同对象的衰减，不能混成单一力律。

这些结果承接并保留首轮已验证的三个基准与 1024 个矩核验，不将既有单元重新计算为新发现。本轮没有发现或验证万有引力，没有建立点值吸引力或 N0；用户继续授权给出扩展研究范围，不代替正式 CLAIM 或 Driver 裁定。

### 输出位置与证据边界

本扩展的 `REPORT.md`、`results.json`、`METHOD_AUDIT.md`、`run_spatial_decay.py` 已保存在 commit `b7bec0be19987620eb77e7e72122c79e557aeb1a` 的 `experiments/brc_residual_spatial_decay_20261002_fca717/`，并由父执行逐字节远程读回核验。四个完整不可变链接保留于 frontmatter `source_refs`；报告是当前恢复与评审入口。

全部模型与计算须标识为合成 toy/代数模型；与经典衰减律的比较保持 N1/N2 层次。本任务不声称实测引力，不从壳均量推点值、从标量质量推向量吸引力、从反平方指数推引力机制，也不将 N1/N2 升为 N0。

## 2. Hard target and required outputs

以下为本轮已执行协议与交付验收标准；对应完成证据在上述不可变归档中。后续评审不默认重跑已完成单元。

1. 给出路线 A 每种模型的累积量、标准化方式、RMS 定义、时间与宽度关系；检验四阶候选和一般 `p` 候选，区分适用条件、常数、符号、抵消和失败情形。
2. 可复现地比较 `d` 维轴步进、同协方差不同高阶分支、persistent、均值漂移及有限记忆模型；已有首轮实验只作恢复来源，新增运行必须对应本扩展的具体信息缺口。
3. 给出路线 B 的精确壳计数核验、指定守恒/归一化模型的壳均量、`d=3` 的渐近或有限半径差异，以及吸收和三叉树对照；加入实际局部 outward Moore 邻接端点 CWM 的 20 层传播与角点指数反例，分开壳平均与点值行为。
4. 编写一份显式比较表或报告段，逐项区分 `t`、`ell`、`r`、标准化残差、壳平均质量、点值场、方向/吸引性和物理量纲；没有建模或证明的栏位明确写“未建立”。
5. 在预定目录保存代码、可机器读取的结果、报告及方法审计，附重跑命令、必要依赖、随机种子/容差（若用）、精确算术或数学推导的证据级别。保留负结果，不用新命名替代已知数学来源。
6. 最终归档明确完成单元、未完成问题和边界；给出被证据支持的最强结论，同时说明为何该结论尚不足以建立点值力律、吸引力、引力或 N0 原生性。

## 3. Research value to preserve

将“像万有引力一样衰减”的类比拆成可反驳的具体命题：标准化高阶信息随有效扩散宽度的衰减，和守恒量在给定图壳上的平均稀释。保留二者可能出现的共同指数及各自独立的来源、条件与反例，防止只因幂指数吻合便混同距离、观测量或物理机制。即使结果只是已知加和律、壳计数或明确反例，也应保存其对 BRC 表示和残差解释的约束。

## 4. Success, kill, and return criteria

成功条件：两条路线及指定对照均完成或有明确且可复核的失败原因；每个幂律主张都绑定模型、观测、归一化、适用尺度和证据级别；精确结果与数值拟合分开，已完成首轮不被重复登记为新成果；报告、代码、结果和方法审计可独立复核。

Kill/no-go 条件：只靠斜率拟合宣称规律、忽略零高阶系数/符号或有限尺度修正、把 persistent/有限记忆当作 iid、把漂移距离等同于中心 RMS 宽度、把 `ell` 与 `r` 混用、把守恒总量自动当作每个壳的单位总量、把壳均量推成点值各向同性、把无方向标量衰减推成吸引力或万有引力，均不足以支持对应强结论。反平方候选被对照破坏时返回确切条件，不隐式变更模型以保住指数。

返回条件：完成本次用户明确扩展的有限检验集合并归档后，返回最强被验证结果和边界。若仍需额外数据、实际物理动力学、更多模型或独立原生推导，具体列出真实信息缺口；不因一次幂律吻合自动开启无限实验或授予 N0、Working Truth、数学接受或正典晋升。本代任务登记不追溯授予正式 CLAIM、Driver 审查或结果接受。当前下一步是基于已归档报告评审这些结论及其范围；不重复已完成的校准、枚举或传播。只有未来明确原生距离、源—探针耦合等新信息缺口，再另立有界研究。
