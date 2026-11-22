<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P017-RH-LOCAL-CORRELATION-20261122",
  "title": "P017 平方窗相关余项中的 RH 输入压力测试",
  "priority": "P3",
  "leverage": "MEDIUM",
  "frontier": "旧capacity/analytic-mass任务已SUPERSEDED；G4四次根预筛已将目标集中为W2=3R3−3S1+2S2，Walsh-L2核只有表示定理；RH标准尺度尚未进入每个平方窗。",
  "next_action": "从冻结G4相关余项或Walsh精确核选择一个实际子问题，写明RH/Dirichlet-GRH输入能控制的算术项与目标平方窗之间仍缺的关系。",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P017-P018-ANALYTIC-MASS",
  "successor_gate": {
    "new_information_gap": "RH/Dirichlet-GRH作为新外部输入是否改善G4相关余项或Walsh核的指定局部目标。",
    "why_parent_result_does_not_close_it": "历史父任务已SUPERSEDED；最新已保存G4结构与Walsh表示仍没有所需局部估计，标准RH给O(n log n)而相邻平方端点距离为2n+1。",
    "discriminating_outcomes": [
      "明确子族或平均/异常窗范围的更强局部结论",
      "本体系观察量推出局部正性的可验证充分条件",
      "指定全局预算或观察机制不足以推出所需局部结论的精确障碍"
    ],
    "kill_condition": "重做旧capacity、generic Fourier norm或独立密度估计而没有改变已知缺口时，结束该候选；抽象信号反例只反驳对应推论机制。",
    "alternative_route_or_free_exploration_considered": "已比较继续原任务、直接引用外部定理、研究局部特例及不同内部方法；本单元由用户明确要求发布，方法可自主选择，结论按实际范围判断。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "新单元承接G4实际前沿并测试新外部输入，历史父任务仅保留谱系，不恢复其过时科学目标。"
  },
  "source_refs": [
    "c2f563200a46fd4bc70ac44453c749ccd0a37bd1:research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md",
    "16d003b7f927efc5ee96f6c47335ab54c8a4d945:research_tasks/LEGACY_CONTROL_MIGRATION_RS_P017_P018_ANALYTIC_MASS_20260902.md",
    "16d003b7f927efc5ee96f6c47335ab54c8a4d945:research_task_records/RS-P017-P018-ANALYTIC-MASS/TP2-6245EA3F6703EAFCB2FD.json",
    "90251d026b4d422a98de007f76de2a1e3de9337e:docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_WIP.md",
    "90251d026b4d422a98de007f76de2a1e3de9337e:docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_SUPPLEMENT_06_WIP.md",
    "90251d026b4d422a98de007f76de2a1e3de9337e:src/enterprise_math/p017_p018_walsh_even_l2_kernel.py"
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
  "registry_key": "RS-P017-RH-LOCAL-CORRELATION-20261122",
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

# P017 平方窗相关余项中的 RH 输入压力测试

## 精确起点

目标平方窗为 \(I_k=\{k^2+1,\ldots,k^2+2k\}\)。冻结的G4材料取四次根预筛，得到
\[
\mathcal W_2(k)=3R_3-3S_1+2S_2=3\pi(I_k)-N_2,
\quad \mathcal W_2(k)>0\Rightarrow\pi(I_k)>0.
\]
pair token单次使用和重复因子的真实范围按原稿保留。配套Walsh材料给 \(\sum_q A_q^2=\sum_{r,s}K_C(r,s)\) 及同/反向碰撞核的精确表示，目前未有sublinear能量估计。

上述科学输入来自PR #170的已保存分支90251d026b4d422a98de007f76de2a1e3de9337e，观察时尚未合并。历史父任务已SUPERSEDED；本任务以这里的真实相关前沿继续。

## 新问题

RH的标准供给尺度在 \(x=k^2\) 为 \(O(k\log k)\)，相邻平方的端点距离为 \(2k+1\)，目标整数窗含 \(2k\) 个整数。研究RH/Dirichlet-GRH的确切算术输入能否改善G4余项、Walsh核或其一个明确子族/平均问题。保留局部相位、联合残差和有限支持关系，不将标量全局误差直接当逐窗正性。

## 结果标准

可交付某个真实参数族、平均意义或异常窗口集合上的局部改进；一个有可验证本体系假设的充分条件；或指定预算/观察机制的能力边界。若使用保持全局预算的抽象信号反例，精确限定为推论机制的反例。

已有线性筛临界、generic Fourier norm及独立密度障碍作为来源中的已知边界使用。研究方法和先行子问题自由选择；整个勒让德猜想的解决不是局部研究成果成立的条件。

## 固定来源

- [research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/c2f563200a46fd4bc70ac44453c749ccd0a37bd1/research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md)（c2f563200a46）
- [research_tasks/LEGACY_CONTROL_MIGRATION_RS_P017_P018_ANALYTIC_MASS_20260902.md](https://github.com/awdawmip/enterprise-math/blob/16d003b7f927efc5ee96f6c47335ab54c8a4d945/research_tasks/LEGACY_CONTROL_MIGRATION_RS_P017_P018_ANALYTIC_MASS_20260902.md)（16d003b7f927）
- [research_task_records/RS-P017-P018-ANALYTIC-MASS/TP2-6245EA3F6703EAFCB2FD.json](https://github.com/awdawmip/enterprise-math/blob/16d003b7f927efc5ee96f6c47335ab54c8a4d945/research_task_records/RS-P017-P018-ANALYTIC-MASS/TP2-6245EA3F6703EAFCB2FD.json)（16d003b7f927）
- [docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_WIP.md](https://github.com/awdawmip/enterprise-math/blob/90251d026b4d422a98de007f76de2a1e3de9337e/docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_WIP.md)（90251d026b4d）
- [docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_SUPPLEMENT_06_WIP.md](https://github.com/awdawmip/enterprise-math/blob/90251d026b4d422a98de007f76de2a1e3de9337e/docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_SUPPLEMENT_06_WIP.md)（90251d026b4d）
- [src/enterprise_math/p017_p018_walsh_even_l2_kernel.py](https://github.com/awdawmip/enterprise-math/blob/90251d026b4d422a98de007f76de2a1e3de9337e/src/enterprise_math/p017_p018_walsh_even_l2_kernel.py)（90251d026b4d）
