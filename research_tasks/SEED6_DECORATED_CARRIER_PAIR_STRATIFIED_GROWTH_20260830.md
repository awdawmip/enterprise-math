<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEED6-DECORATED-CARRIER-PAIR-STRATIFIED-GROWTH",
  "title": "Seed-6 扩展的装饰载体对分层生长图谱",
  "kind": "RESEARCH",
  "owner": "research/seed6-decorated-carrier-pair-stratified-growth",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Starting from Seed-6 as the reference coordinate, replace the scalar seed by a decorated carrier pair Sigma=(a,b) and classify the positive-growth local and pairing structures across prime-pair, coprime-thick, coprime-multisupport, overlap and equality strata, preserving valuation/support data and separating standard matching identities from arithmetic decoration.",
  "next_action": "Build an exact stratum atlas for decorated pairs (a,b), derive local triangle and pairing-cell invariants as functions of gcd/support/valuations, classify transitions and minimal counterexamples between strata, and determine which data must be retained for operation-safe gluing without introducing a distance or factorization objective.",
  "dependencies": [
    "research_returns/SEED6_BRIDGE_TRIANGLE_LOCAL_GROWTH_RETURN_20260829.md@main",
    "research_returns/SEED6_THREE_PAIRING_ORBIT_BRIDGE_RECTANGLE_RETURN_20260829.md@main",
    "research_returns/SEED6_SEED_SPECIFICITY_TRANSFER_TEST_RETURN_20260829.md@main",
    "driver_reviews/SEED6_POSITIVE_MULTIPLICATIVE_GROWTH_DRIVER_REVIEW_20260830.md@main"
  ],
  "evidence_status": "SEED6_FIRST_WAVE_DRIVER_ACCEPTED / DECORATED_CARRIER_PAIR_REQUIRED / OBJECTIVE_OPEN",
  "hard_block": null,
  "tags": ["seed6","decorated-carrier","stratification","valuation","support","overlap","positive-growth"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEED6-DECORATED-CARRIER-PAIR-STRATIFIED-GROWTH",
  "parent_objective_id": "OBJ-SEED6-MULTIPLICATIVE-GROWTH-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "S6DCG",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEED6-SEED-SPECIFICITY-TRANSFER-TEST",
  "successor_gate": {
    "new_information_gap": "The transfer result proves that scalar seed values are insufficient and that the intrinsic state must retain a decorated carrier decomposition. It also isolates overlap defect, valuation thickness and seed strata, but no exact common state space or transition atlas for those strata has yet been constructed.",
    "why_parent_result_does_not_close_it": "RR-9F63DC1F42946346C130 classifies which Seed-6 signatures transfer, but it does not classify the full decorated pair state space, inter-stratum morphisms, or which valuation/support decorations are required for later gluing.",
    "discriminating_outcomes": [
      "construct an exact decorated-carrier stratified cell model with complete local invariants and operation-safe transition maps",
      "prove that some proposed strata collapse to the same typed structure and reduce the state data to a smaller exact interface",
      "prove that no single finite decorated-cell interface captures both support and valuation behavior without losing essential operation data"
    ],
    "kill_condition": "Do not replace the decorated pair by its scalar product; do not turn gcd or valuation data into an additive distance; do not use factor recovery or search performance as a success criterion; do not claim standard perfect-matching or rank-one identities as new mathematics.",
    "alternative_route_or_free_exploration_considered": "The first-wave isolated prime cells and raw global product complex are already classified. Enlarging the prime census would repeat a standard isomorphism type; the higher-value continuation is the newly exposed decorated-carrier stratification.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The proof obligation has changed from testing whether Seed-6 is special to constructing the actual generalized state space forced by the negative specificity result."
  }
}
-->

# Seed-6 扩展的装饰载体对分层生长图谱

Status: `READY / P1 / POSITIVE-GROWTH / NO-FACTORIZATION`

## Mother question

以 `6=(2,3)` 为参考坐标，但不再把标量 `6` 当作完整状态。令

\[
\Sigma=(a,b),\qquad a,b>1,
\]

并对 fresh 乘法原子 \(r,p,q\) 形成

\[
T_r^{a,b}=\{ab,ar,br\},
\]

以及三配对态

\[
\{ab,pq\},\quad \{ap,bq\},\quad \{aq,bp\}.
\]

问题是：**装饰载体对 `(a,b)` 的正向乘法生长究竟具有怎样的精确分层结构？**

目标不是把所有种子强行统一，而是找出哪些结构只依赖互素性、哪些依赖素支撑、哪些依赖 valuation thickness、哪些在 overlap/equality 边界发生真正退化。

## Frozen inputs and scope

1. 接受 Seed-6 第一轮 Driver review 的五项边界。
2. `6=(2,3)` 只是 canonical reference，不是唯一公理。
3. 接受 `Delta_T=gcd(a,b)^2` 作为已发现的 exact overlap detector，但必须重新嵌入更完整的结构图谱。
4. 接受四原子三配对、`J(4,2)`、rank-one rectangle 为标准对象。
5. 接受 raw support-faithful 全局矩形拼接为 `K_k x I` 且自然 transport flat。
6. 允许 gcd、lcm、prime support、valuation vector、Smith normal form、typed incidence、finite cell/poset/groupoid language。
7. 禁止 additive-distance、Fermat/square-shell、因子恢复、endpoint、分解成功率和性能收益作为目标。
8. 必须区分 decorated pair `(a,b)` 与 scalar `ab`；同一 scalar 的不同 carrier decomposition 不得静默识别。

## Hard target and required outputs

Hard target: `DECORATED_CARRIER_PAIR_STRATIFIED_GROWTH_ATLAS_CLASSIFIED`

A. 定义最小合法状态 `DECORATED_CARRIER_CELL_V1`，明确哪些字段是 identity、support、valuation、incidence 与可选 presentation。

B. 精确分类至少五类 seed strata：
- distinct prime pair；
- coprime prime-power/thick pair；
- coprime multisupport pair；
- overlapping distinct pair；
- equality pair。

C. 对每类推导 \(T_r^{a,b}\) 的 gcd/lcm、support、valuation matrix、SNF 或等价 integral signature，并说明哪些不变量跨 strata 保持、哪些断裂。

D. 系统分析 overlap defect。判断 `Delta_T=d^2` 是否已经完备刻画局部 overlap 类型；若不完备，给出最小补充量和反例。

E. 分类 scalar decomposition ambiguity：什么时候同一标量对应不同结构 stratum；给出 operation-safe 的 carrier-partition 表示。

F. 把三配对 cell 放入 decorated setting，分类 equality、overlap、valuation thickness 对 pairing state、rectangle incidence、gcd decoration 的影响。

G. 构造 inter-stratum degeneration/forgetful maps，并证明哪些 quotient 安全、哪些会制造伪结构或丢失操作所需信息。

H. 给出 exact finite checker。有限 census 只作回归，必须有符号证明或 exact classification 支撑核心结论。

## Research value to preserve

保留“从 6 正向生长”的研究语义，同时把 6 从唯一对象降为参考坐标。真正要保存的是乘法 carrier 的支撑、厚度、重叠与退化结构，而不是整数大小、普通数轴位置或分解收益。

如果最终发现大部分结构都是标准 divisor/valuation incidence，也应精确冻结其标准边界，并保留不能被这些标准对象消去的最小装饰层。

## Success, kill, and return criteria

成功可以是：
- 完整 stratified atlas；
- 更小的等价 state interface；
- 精确证明某些候选装饰冗余；
- 精确反例证明不存在预期的统一模型。

Kill：
- scalar `ab` 代替 `(a,b)`；
- 把 gcd/valuation 解释成加法距离；
- 用隐藏因子或分解性能选择模型；
- 只扩大样本而不分类结构；
- 把标准 perfect matching / outer-product identity 当作新发现。

Return 必须包含：定义、定理/反例、strata 表、退化/forgetful maps、exact checker、边界与下一问题。
