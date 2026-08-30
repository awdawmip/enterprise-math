<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id":"RS-ADDMUL-VALUATION-TROPICAL-COLLAPSE-GEOMETRY","title":"加乘桥 A5：估值 / Tropical 加法坍塌几何","kind":"RESEARCH","owner":"research/addmul-valuation-tropical-collapse-geometry","base_state":"READY","priority":"P1","leverage":"HIGH",
  "frontier":"Turn integer prime valuations into an exact bridge where multiplication becomes vector addition and ordinary addition produces min-plus behavior plus a cancellation depth kappa; classify the lost unit data and any path/coherence invariants.",
  "next_action":"Classify kappa_p(x,y)=v_p(x+y)-min(v_p(x),v_p(y)) including unequal/tied valuations and units, then build finite-support valuation-vector laws and compare local cancellation accumulation against existing valuation/holonomy tools.",
  "dependencies":[],"source_refs":["classical: non-Archimedean valuation inequality and tropical min-plus convention","research_method_inventory.json@main","src/enterprise_math/precision_holonomy.py@main","src/enterprise_math/weighted_relation_field.py@main"],
  "evidence_status":"DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["addmul","valuation","tropical","cancellation","collapse","holonomy","prime-support"],"claim_lease_minutes":240,
  "created_by_role":"RESEARCH_DRIVER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RS-ADDMUL-VALUATION-TROPICAL-COLLAPSE-GEOMETRY","parent_objective_id":"OBJ-ADDMUL-BRIDGE-STRUCTURE","parent_objective_generation_id":"OG-9D6617146723B8E72C6F","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","identity_lane":"AMTROP","origin_kind":"DRIVER_ROADMAP","task_lineage":"NEW_DIRECTION","parent_task_id":null,"successor_gate":null,
  "policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 加乘桥 A5：估值 / Tropical 加法坍塌几何

Status: `READY / P1 / DISCRETE-VALUATION`

## Mother question

\[v_p(xy)=v_p(x)+v_p(y),\qquad v_p(x+y)\ge\min(v_p(x),v_p(y)).\]
定义 \(\kappa_p(x,y)=v_p(x+y)-\min(v_p(x),v_p(y))\)。能否把“乘法→尺度位移加法”和“普通加法→min + cancellation defect”组成 exact discrete geometry，并完整记录 unit/sign/residue 信息损失？

## Frozen inputs and scope

先用整数 valuation，不要求 p-adic completion。`v_p(0)` 必须显式 infinity typed。若两 valuation 不等，检查何时取等；相等时由 unit residue 分类 cancellation。Tropical `min-plus` 只是 skeleton，不自动是普通加法同构。优先复用 valuation/holonomy 工具。

## Hard target and required outputs

Hard target: `VALUATION_TROPICAL_COLLAPSE_ADD_MUL_GEOMETRY_CLASSIFIED`

1. 完全分类单 `p` 的 `kappa_p`：不等/equal valuation、精确 cancellation、零值、符号与 unit residue。
2. 定义 finite-support valuation vector `V(n)`，证明 `V(xy)=V(x)+V(y)` 并给出信息损失表。
3. 建立 ordinary addition 的 tropical skeleton 与 excess vector `K(x,y)`。
4. 比较多项和不同括号路径的局部 `K`，分类 conservation/coherence 与纯 presentation 路径依赖。
5. 给出现有 precision-holonomy 的复用/缺口结论。
6. 分类有限素数窗口的 projection defect；exact checker 覆盖构造性 cancellation 与零值。

## Research value to preserve

保留 prime-support 厚度的线性位移与加法抵消深度；即便 tropical skeleton 有损，损失类型和 `kappa` 也可能是可用局部几何量。

## Success, kill, and return criteria

有效终态：`VALUATION_PLUS_CANCELLATION_GEOMETRY_CLASSIFIED` / `UNIT_DATA_REQUIRED_FOR_OPERATION_SAFETY` / `EXISTING_TOOLING_ALREADY_COVERS_ROUTE`。不得把 valuation vector 当整数单射，不得把不等式无条件改成等号，不得删除 `x+y=0`。
