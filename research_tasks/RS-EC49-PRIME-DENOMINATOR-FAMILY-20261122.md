<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-EC49-PRIME-DENOMINATOR-FAMILY-20261122",
  "title": "EC49 真实锚点族的素数分母密度与统一供给",
  "priority": "P0",
  "leverage": "VERY_HIGH",
  "frontier": "锚1/2的54/80单位类计数及平方根误差已保存；真实锚a/b的允许单位类分类、变动模数下主项占优范围及可改进短窗尚未确定。",
  "next_action": "从冻结EC49FWS的实际锚点、规范基点和单孔观察器出发，确定合格单位分母类随a、b及相位变化的结构，并选择可统一处理的锚点族。",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "source_refs": [
    "c2f563200a46fd4bc70ac44453c749ccd0a37bd1:research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md",
    "95507f064ee46910b32e26d1c49e6df4a05b84fc:research_notes/portable_direct/EC49FWS_FAREY_ONE_HOLE_FIBER_OBSERVER_THEOREM.md",
    "95507f064ee46910b32e26d1c49e6df4a05b84fc:research_notes/portable_direct/EC49FWS_FAREY_FACTOR_PROBE_OUTPUT.json",
    "https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/17.0_pp_419_451_Conditional_estimates.pdf"
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
  "registry_key": "RS-EC49-PRIME-DENOMINATOR-FAMILY-20261122",
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

# EC49 真实锚点族的素数分母密度与统一供给

## 研究问题

对实际约分锚 \(a/b\)，保留 determinant-one 分支、规范基点与相位，研究原 \(C_{11}\) 观察器允许的素数分母：哪些锚点有正主项，允许单位类怎样分类，当分母上限 \(H\) 与 \(b\) 同时增长时，在什么范围能保证合格素数供给及靠近上限的逼近？

冻结分支为
\[
(h_t,n_t)=(H_1,N_1)+t(a,b-a),\qquad d_t=H_1+N_1+bt,
\]
以及原稿 \(U(t\bmod10)\mathbf1_V(t\bmod11)\)。采用模数 \(Q=110b\) 时，保留与Q互素的实际分母类，并单列整除Q的有限素数例外。原始rephase与规范基点只转换一次。

## 已有结论

本轮报告的锚 \(1/2\) 已有 \(h=t,n=t+1,d=2t+1\)，54个模220单位类与 \(\varphi(220)=80\)，故
\[
N(H)=\tfrac{27}{40}\operatorname{Li}(H)+O(\sqrt H\log H).
\]
其密度主项来自固定模素数定理；Dirichlet-GRH提供误差和末端窗口。一般有限特征展开及 \(\mathcal F(1_S)\le\sqrt{|S|}\) 也已给出。EC49FWS母材料是已保存分支上的作者证明/有限精确核对，尚未独立Review。

## 新产出与判断

目标包括实际锚点族的允许类精确分类或正性判据，保留 \(b,H\) 和谱成本的统一误差/主项占优域，或利用真实相关结构改善某类锚点的短窗与逼近误差。精确说明某参数区间不能由所用估计保证供给，也可形成范围明确的结果。

仅重复一般周期计数公式、1/2的27/40或至多110个参数类的通用界，不构成新增推进。若候选族出现结构性空支持，给出真实锚点和完整原因。与既有有限6/9/12观察预算相区别，本任务的新观察是素数分母及模数增长。

## 固定来源

- [research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/c2f563200a46fd4bc70ac44453c749ccd0a37bd1/research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md)（c2f563200a46）
- [research_notes/portable_direct/EC49FWS_FAREY_ONE_HOLE_FIBER_OBSERVER_THEOREM.md](https://github.com/awdawmip/enterprise-math/blob/95507f064ee46910b32e26d1c49e6df4a05b84fc/research_notes/portable_direct/EC49FWS_FAREY_ONE_HOLE_FIBER_OBSERVER_THEOREM.md)（95507f064ee4）
- [research_notes/portable_direct/EC49FWS_FAREY_FACTOR_PROBE_OUTPUT.json](https://github.com/awdawmip/enterprise-math/blob/95507f064ee46910b32e26d1c49e6df4a05b84fc/research_notes/portable_direct/EC49FWS_FAREY_FACTOR_PROBE_OUTPUT.json)（95507f064ee4）
- <https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/17.0_pp_419_451_Conditional_estimates.pdf>
