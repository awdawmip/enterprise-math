<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id":"RS-ADDMUL-SUM-PRODUCT-OBSTRUCTION-STRESS-TEST","title":"加乘桥 A7：Sum–Product 与同时线性化阻碍压力测试","kind":"RESEARCH","owner":"research/addmul-sum-product-obstruction-stress-test","base_state":"READY","priority":"P1","leverage":"HIGH",
  "frontier":"Build an exact obstruction and stress framework for any proposed addition–multiplication bridge: detect unavoidable information loss, exceptional substructures, domain restrictions, hidden coordinates, or approximation when a representation appears to linearize both operations.",
  "next_action":"Formalize bridge-strength levels and elementary impossibility witnesses first, then add finite-set sum–product growth as a scoped external stress theorem and construct exact finite counterexample suites for injective or approximately structure-preserving candidates.",
  "dependencies":[],"source_refs":["classical: sum–product estimates in fields and integers","research_method_inventory.json@main"],
  "evidence_status":"DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["addmul","sum-product","obstruction","stress-test","information-loss","injectivity","expansion"],"claim_lease_minutes":240,
  "created_by_role":"RESEARCH_DRIVER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RS-ADDMUL-SUM-PRODUCT-OBSTRUCTION-STRESS-TEST","parent_objective_id":"OBJ-ADDMUL-BRIDGE-STRUCTURE","parent_objective_generation_id":"OG-9D6617146723B8E72C6F","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","identity_lane":"AMOBSTR","origin_kind":"DRIVER_ROADMAP","task_lineage":"NEW_DIRECTION","parent_task_id":null,"successor_gate":null,
  "policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 加乘桥 A7：Sum–Product 与同时线性化阻碍压力测试

Status: `READY / P1 / NEGATIVE-CONTROL`

## Mother question

任何“同时简化加法与乘法”的表示都可能把代价藏在非单射、缩域、额外坐标、例外子结构或近似误差中。怎样建立 exact stress suite，让未来所有加乘桥必须公开这些代价？

## Frozen inputs and scope

先做初等有限 obstruction；深 sum–product 定理仅作第二层外部压力。任一候选 `T` 必须记录 domain/codomain、injectivity、两种 transport law、exceptional set、hidden coordinates。允许 `Z`、有限整数盒、`F_p` 反例。不得把“不能同时线性化”偷换成“没有任何桥”。

## Hard target and required outputs

Hard target: `SIMULTANEOUS_ADD_MUL_LINEARIZATION_OBSTRUCTION_STRESS_SUITE_CLASSIFIED`

1. 定义 bridge strength hierarchy：exact injective conjugacy / homomorphic image / finite typed embedding / lossy invariant / approximate probe。
2. 用 identity、idempotent、cancellation、distributivity、growth 等给最小 elementary impossibility witnesses。
3. 把 finite-set sum–product growth 转成 scoped stress template，逐项核对适用假设。
4. 分类合法 escape：subring/subfield、log domain、valuation quotient、ghost coordinates、noninjective collapse、local/formal neighborhood。
5. 构造 exact finite bridge-table checker，检测 collision、operation law 与 set-growth distortion。
6. 定义最小 `BRIDGE_AUDIT_PACKET`，并给至少三类漂亮但错误的伪桥反例。

## Research value to preserve

建立统一负控，使后续桥梁必须类型化“保留/丢失/限制/附加”信息；可防止低阶吻合或漂亮坐标被误当全局统一。

## Success, kill, and return criteria

有效终态：`BRIDGE_STRENGTH_HIERARCHY_AND_STRESS_SUITE_CONSTRUCTED` / `ELEMENTARY_OBSTRUCTIONS_SUFFICIENT` / `SUM_PRODUCT_USEFUL_ONLY_UNDER_RESTRICTED_HYPOTHESES`。不得把 sum–product 口号当万能 no-go，不得把非单射 bridge 一律判错，不得用数值增长实验代替一般定理。
