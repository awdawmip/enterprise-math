<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RH-ROAD-CERTIFIED-NET-COST-20261122",
  "title": "已知 RH 下完整道路实际输出的净成本与短证书",
  "priority": "P0",
  "leverage": "VERY_HIGH",
  "frontier": "已知规定匹配族的平方根包络、全窗O(log A)和逐层核预算；尚无针对同一实际道路输出、同一误差要求且计入全部预处理与位成本的已证净收益。",
  "next_action": "从冻结F_Z匹配族和一个明确窗口/精度输入出发，固定实际待求量及直接计算基线，分析可复用残差/骨架信息对总成本的真实影响。",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RH-METHOD-TRANSFER-20261121",
  "successor_gate": {
    "new_information_gap": "RH作为已知输入后，实际输出的区间包络或计算能否更便宜。",
    "why_parent_result_does_not_close_it": "原任务主要提取外部证明结构并研究不以RH为前提的相位/能量机制；本轮O(log A)只控制大小，未计算实际能量或支付同精度全部成本。",
    "discriminating_outcomes": [
      "明确非空参数域上的总成本优势及正确性",
      "指定压缩/证书方案的精度—成本关系",
      "对实际候选族的净收益失败机制或成本下界"
    ],
    "kill_condition": "若候选只重新证明现有O(log A)，或成本节省来自更换待求量/放宽误差而未核算，结束该候选并保留精确比较。",
    "alternative_route_or_free_exploration_considered": "已比较继续原任务、直接引用外部定理、研究局部特例及不同内部方法；本单元由用户明确要求发布，方法可自主选择，结论按实际范围判断。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "采用已知RH后的同输出成本是独立可验收对象；保留原任务内部无条件抵消研究与原作者归属。"
  },
  "source_refs": [
    "c2f563200a46fd4bc70ac44453c749ccd0a37bd1:research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md",
    "b2664a273150536823c6c3217732adf4cd84e784:research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/README.md",
    "b2664a273150536823c6c3217732adf4cd84e784:research_notes/portable_direct/rh_triangle_correlation_20261122_b5750a/REPORT.md",
    "16d003b7f927efc5ee96f6c47335ab54c8a4d945:research_task_records/RS-RH-METHOD-TRANSFER-20261121/TP2-677F61D1BCF81D4E4FE3.json"
  ],
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "dependencies": [],
  "evidence_status": "SOURCE_BOUND_OPEN_RESEARCH",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "RH_APPLICATIONS",
    "USER_WEIGHTED_TASKSET"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RH-ROAD-CERTIFIED-NET-COST-20261122",
  "parent_objective_id": "OBJ-RH-APPLICATIONS-WEIGHTED-20261122",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-APPS",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "taskset_id": "TS-RH-APPLICATIONS-20261122",
  "priority_basis": "按当前用户授权，以数学接口成熟度、可独立推进程度及预期研究价值分档。",
  "priority_weight_reference": "research_runtime_policy_v2.json#/selection_policy/priority_weights"
}
-->

# 已知 RH 下完整道路实际输出的净成本与短证书

## 问题与起点

对既有稳定匹配族 \(F_Z\)，研究残差道路能否在同一数学输出、同一精度要求下减少总计算量、峰值存储或证书长度。已有 \(|F_Z(y)|\le K\sqrt y\)、固定幂窗正部能量 \(O(\log A)\) 和逐层精确 Green 核预算，作为已保存应用推导使用。

核心目标量取实际窗口能量
\[
S_Z(A,B)=\sum_{n=A}^B(F_Z(n))_+^2/n^2.
\]
声明输入 \(A,B,Z\)、匹配参数和所需误差，比较包含真实 \(S_Z\) 的区间包络或其它明确的同一输出。单点道路值、局部相关量可形成有用先行结果，并保留其实际范围。

## 数学与成本范围

使用来源列出的原匹配族、真实骨架、相位和完整整数人口。若使用参考曲线 \(G\)，将 \(F_Z-G\) 的实际误差计入输出。成本包括匹配节点/权重的构造、输入位长、除数与素数幂处理、参考筛法、对数/幂值精度、预处理和验证；共享预处理说明摊销范围。

既有有限证书的12次道路读取之外，还涉及筛至32768、3392个素数幂事件及3488个对数；这些是定位比较基线的历史数据，不代表新算法已经有收益。本任务固定RH为外部输入；原任务的不依赖RH的相位相关和内生统一估计保持其原问题。

## 有价值的交付

可交付明确参数族或有限实用范围中的总成本收益、严格误差—成本关系、可复算的比较，或对一个实际候选方案的成本下界/失败原因。程序仅在选择计算方法时提供相应复算材料，书面数学结论依其论证验收。

直接引用RH上界即可完成的“存在一个小上界”不是本任务的实际输出。方法、观察量压缩和证书设计可自由调整；压缩须保留所声明观察与未来操作需要的联合关系。

## 固定来源

- [research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/c2f563200a46fd4bc70ac44453c749ccd0a37bd1/research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md)（c2f563200a46）
- [research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/README.md](https://github.com/awdawmip/enterprise-math/blob/b2664a273150536823c6c3217732adf4cd84e784/research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/README.md)（b2664a273150）
- [research_notes/portable_direct/rh_triangle_correlation_20261122_b5750a/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/b2664a273150536823c6c3217732adf4cd84e784/research_notes/portable_direct/rh_triangle_correlation_20261122_b5750a/REPORT.md)（b2664a273150）
- [research_task_records/RS-RH-METHOD-TRANSFER-20261121/TP2-677F61D1BCF81D4E4FE3.json](https://github.com/awdawmip/enterprise-math/blob/16d003b7f927efc5ee96f6c47335ab54c8a4d945/research_task_records/RS-RH-METHOD-TRANSFER-20261121/TP2-677F61D1BCF81D4E4FE3.json)（16d003b7f927）
