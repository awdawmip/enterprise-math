<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RH-METHOD-TRANSFER-20261121",
  "title": "RH 新证明方法提取：相位保真、提升代价与整数道路能量接口",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "上一轮已定位外部正式代码与独立核验资料，证明并复算双线性秩/Smith 相位计数和端点—相位递推；尚需展开承重提升接口，并判定哪些保真、代价与统一性结构可用于 B_{a,N} 的固定原点能量。",
  "next_action": "读取已定位承重引理的精确源依赖，形成可核验的对象/假设/结论/常数映射，并在整数道路观察量上推进可证明命题或精确障碍。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/c3acb4d86c52f432a2697d8e035e4078ef2a4dab/research_notes/portable_direct/rh_method_harvest_20261121_b5750a/README.md",
    "https://github.com/awdawmip/enterprise-math/blob/c3acb4d86c52f432a2697d8e035e4078ef2a4dab/research_notes/portable_direct/rh_method_harvest_20261121_b5750a/verify_finite_models.py",
    "https://github.com/CocoSgt/riemann-hypothesis-lean/tree/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4",
    "https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/RH_MOBIUS_FLUX_RENYI_GRAM_HIERARCHY_20260908.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/definitions/ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md"
  ],
  "evidence_status": "EXISTING_PORTABLE_RESEARCH_PLUS_OPEN_TRANSFER_FRONTIER",
  "last_progress_ref": "c3acb4d86c52f432a2697d8e035e4078ef2a4dab:research_notes/portable_direct/rh_method_harvest_20261121_b5750a/README.md",
  "last_progress_at": "2026-11-21T00:39:05+00:00",
  "hard_block": null,
  "tags": [
    "RH",
    "METHOD_EXTRACTION",
    "ANCHORED_PHASE",
    "INTEGER_ROAD_ENERGY",
    "BRC"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RH-METHOD-TRANSFER-20261121",
  "parent_objective_id": "OBJ-RH-METHOD-HARVEST-20261121",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-METHOD",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# RH 新证明方法提取：相位保真、提升代价与整数道路能量接口

## 研究目标与实际谱系

本任务响应用户 2026-11-21 的直接指令“出任务，然后继续提取”。母目标是理解新公布 RH 形式证明中对进取数论有用的数学结构，给出能核验、能复用、能由他人接续的结果。

这是本轮直接研究的首次正式任务出版，谱系为 INTEGRATION：整合外部证明材料、先前 portable 方法提取，以及项目既有整数道路能量与 BRC 定义。上一轮材料没有正式 Task / Result / Review 父记录；其真实来源由 source_refs 与 last_progress_ref 保留。现有 RH 道路任务的所有权与状态按各自记录继续成立，本任务只承担此次方法提取和接口研究。

方法由执行者根据证据选择。需要交付的是数学对象、可复算证据和迁移判断；工具数量、阅读顺序和预定中间结论均不作为验收门槛。

## 当前已完成内容

固定输入报告为 enterprise-math@c3acb4d86c52f432a2697d8e035e4078ef2a4dab 的 research_notes/portable_direct/rh_method_harvest_20261121_b5750a/README.md；同目录 verify_finite_models.py 与 finite_model_results.json 保存精确整数复算。

已完成：
- 定位作者说明、实际 Lean 代码主定理与独立核验者报告，分开记录外部报告和本地实际执行。
- 从角色正交性证明 qN=M^k+R。
- 对全有限域双线性形式 aᵀBb，得到秩控制的完整相位计数；对整数模数得到 Smith 不变量与 gcd 的精确角色和公式。
- 证明保留端点和累计相位可支持既定追加操作；展示相同权重直方图仍有不同算术相位读出的例子。
- 核验 F_2、F_3、F_5 上全部 2×2 矩阵及报告所列路径、递推和合数模数案例。
- 识别本项目固定原点交叉相位与逃逸尺度尾项的真实未闭合接口。

这些是实际研究输入，其 Project Review 状态保留为未审查。它们提供可复用证据，不自带 Foundation 或 Working Truth 晋升。

## 输入与对象

### 外部来源

源码镜像固定为 CocoSgt/riemann-hypothesis-lean@7cbf7a0c32fca1badf05931879a37c3f8a2b03b4。已定位入口：

- src/Main.lean
- src/Statements.lean
- src/Supplements/Kernels/MainTheorems.lean
- src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean
- src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean

作者说明 https://alpo.ge/remark.pdf 和核验页 https://math.mit.edu/~drew/grh/ 为来源入口。新的页面状态依其实际观察时间记录；源码结论依固定字节与已读依赖说明。本任务提取有用接口，所需的依赖展开由证明责任决定。

### 项目来源

科学输入固定为 enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7：

- research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md
- research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md
- research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md
- research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md
- research_notes/RH_MOBIUS_FLUX_RENYI_GRAM_HIERARCHY_20260908.md
- definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md
- definitions/ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md

在这些输入的符号下：

R_a(n)=∏_{p|n}(1−p^(−a)), c_a=1/ζ(1+a),
S_a(x)=Σ_{n≤x}R_a(n), E_a(x)=S_a(x)−c_ax,
Q_a=∫_0^∞|E_a(x)−1_[1,∞)(x)|² dx/x²,
B_(a,N)=S_a(N)−1−c_a(N+1/2).

项目已有 RH⇔Q_a=O(a) 及离散能量接口保持其原来源状态；新增证明应清楚说明实际使用的前提。P000/X6 原生对象和外部线性代数/解析工具各保留类型，辅助记忆字段按观察用途解释。

## 所需交付与验收

1. **源证明承重接口的准确转译。** 把实际读到的关键提升、秩/退化、整除或斜率—范数引理整理成明确的对象、假设、结论和参数依赖，附固定提交、文件、定理名及必要依赖；说明何处使用了更强的上游数学。引用来源、我们自行推导的命题和待证明迁移分别可辨。

2. **对项目对象有实质内容的迁移结果。** 交付可检查的恒等式、有限定理、条件估计或精确障碍，说明它怎样作用于保留算术标签的 BRC 状态或固定原点的 B_(a,N) 观察。计算使用确定的输入、精度规则和可复算脚本；证明陈述覆盖实验以外范围时给出证明。

3. **保真、代价与统一性核算。** 说明转换前后哪些观察量相等，残差怎样保留，增益与代价分别来自何处。对随 a、N 或提升深度变化的界，明确常数和适用范围。若只得到固定窗口、平移平均或有限截断结果，给出它与固定原点无限能量之间仍需补齐的条件。

4. **可接手的完成状态。** 结果中保留已经完成的证明和实验、没有关闭的数学接口、可直接使用的材料位置以及继续研究所需条件。后续执行者无需隐藏对话即可复核。

本任务完成以准确的方法提取和上述迁移判定为准，RH 本身的自主证明不属于本次验收条件。一个证据充分的不可直接迁移结论同样是有效结果：需给出失效假设、反例或未满足的明确必要接口，并保存仍可复用的结构。

## 要回答的具体缺口

核心缺口是：外部提升链的收益是否能落到我们真实算术观察量上，而其代价和相位损失又是否可统一控制。

当前可用的探针包括但不限于：

- 退化部分的秩/质量与有效提升收益之间的定量关系；
- 保留原点相位的 Gram / Parseval 恒等式与近频交叉项；
- 提升深度与 a、N 的联动；
- 全尺度能量对有限窗口结论的额外统一性要求。
- 窗口型替代路线：核对源代码中 HasWindows / ChebyshevInequalityOnWindows 与 Landau 强迫坏点的量词，判定“任意远存在完整幂窗口”怎样与本项目正能量的全尾界关联。全尺度统一估计只是候选路线之一，不能预先当作外部证明实际使用的唯一机制。

例如定义 H_j(a)=Σ_{2^j≤N<2^(j+1)}B_(a,N)^2，估计
4^(−j)H_j(a)≤Ca·2^(−η(j−J(a)))
在 j≥J(a) 上具有统一常数时可求和得到尾界。它只是可研究的充分条件，执行者可选择等价或更合适的界；其成立与否由数学证据决定。

## 研究价值与返回条件

将“提升会带来抵消”细化为有明确定义、守恒信息和净代价的可复用结构，可防止在只剩权重直方图、逐点稳定或平移平均时误判已经控制原始能量。

完整返回包含源绑定提取稿、证明或精确反例、实际计算记录、迁移判断和尚未闭合接口。若某条具体桥接被反例或成本障碍否定，记录它适用的精确范围，并在当前母问题内评估仍有信息增量的其他路线。任务结果的实际数学范围决定完成状态，单次提交或阶段摘要不单独决定终止。
