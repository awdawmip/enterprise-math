<!-- ENTERPRISE_MATH_TASK_V1
{"task_id":"X6CM-SHORT-BALL-OVERLAP-GROWTH-20260917","title":"X6 混合指数实际短球见证重叠增长界","kind":"RESEARCH","owner":"taskbook/unassigned","base_state":"READY","priority":"P1","leverage":"HIGH","frontier":"Checkpoint 13 shows exact finite/scoped overlap gains, but the growth rate of the actual sign-quotiented short-ball ratio/annihilator overlap population over mixed indices remains unknown.","next_action":"Freeze the checkpoint-13 observer and witness deduplication, select a growing mixed-index family, count actual short-ball overlap multiplicities by local Krylov/annihilator type, and derive either a summable factorial-moment gain or a counterexample family.","created_by_role":"RESEARCH_DRIVER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"X6CM-SHORT-BALL-OVERLAP-GROWTH-20260917","parent_objective_id":"OBJ-X6CM-ALL-INDEX-GEOMETRY-20260917","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","identity_lane":"X6CM","origin_kind":"DRIVER_ROADMAP","task_lineage":"CONTINUATION","parent_task_id":"X6CM-DRIVER-ALL-INDEX-GEOMETRY-20260917","successor_gate":{"new_information_gap":"The actual short-ball ratio/annihilator overlap population is not bounded across growing mixed indices; existing exact overlap gains are finite or stratum-scoped.","why_parent_result_does_not_close_it":"Checkpoint 13 gives exact finite ensembles, a product-stratum limitation, and critical-window consequences, but it does not prove a growing mixed-index overlap theorem for the actual geometric short-ball witnesses.","discriminating_outcomes":["A uniform or summable overlap theorem yields a strict improvement of the current log-power or multiplier-window frontier.","Overlap can be bounded only strongly enough for a constant-factor or finite-scale improvement, leaving the exponent frontier unchanged.","An explicit clustering family or counterexample prevents the proposed overlap gain on infinitely many mixed indices."],"kill_condition":"If a rigorous upper/lower overlap analysis proves that the actual short-ball overlap cannot improve the current exponent frontier under the frozen observer semantics, return the no-go with exact witness families and stop this route.","alternative_route_or_free_exploration_considered":"The independent local bad-seed-decay route is published in parallel; changing the observer, deleting composite indices, or reselecting the four locked seeds is not an acceptable substitute.","why_new_stage_or_task_is_better_than_same_task_or_closure":"The remaining problem is a bounded asymptotic incidence/counting question with its own falsifiable outputs and can be executed independently while the Driver compares it with the local-decay route."},"source_refs":["awdawmip/enterprise-math@50eb9a8f720e46aa973e54d1e8e38b61fc9dfcb4:research_notes/x6_witness_overlap_checkpoint_20260911.json","awdawmip/enterprise-math@7abd6f9523e1f6edc4c714b93c9e81dde588633e:research_notes/x6_tunable_geometry_checkpoint_20260911.json","awdawmip/enterprise-math@b89e6628783609f5f883353ddb6f7339e600d8f6:research_activity_records/RA-X6CM-F01144F76207.json"],"dependencies":[],"evidence_status":"TASK_DEFINED_NOT_EXECUTED","tags":["X6CM","short-ball","overlap","mixed-index","factorial-moment","BRC"],"claim_lease_minutes":120,"policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4","review_state":"PASS","temporary_overrides":[]}}
-->

# X6 混合指数实际短球见证重叠增长界

Status: `READY / PUBLISHED_REGISTERED`

## Mother question

在保持当前 X6 全整数格族、四个冻结种子、全部合数与联合关系观察不变的前提下，实际几何短球中的 sign-quotiented 见证，其 ratio/annihilator/Krylov 重叠人口随混合指数增长到什么量级？这种真实重叠能否把现有一阶矩/窗口前沿推进到更强的对数指数，而不只是改善常数？

## Frozen inputs and scope

冻结 `X6CM-WITNESS-OVERLAP-20260911-13` 的对象和观察：原生六轴整数向量、当前格 M(N)、短向量存在事件、observer-safe 的符号/事件支持去重、局部 Krylov/annihilator 数据及全部来源 provenance。

冻结 P000、四个种子锁定、普通自然数算术与 U 的非原生非等距身份。合数和混合素数关系是研究人口的一部分，不允许只研究素数后把结果无证书外推到全部整数。

父结果的有限目录、N=55/N=605 等精确概率以及 product-stratum 树界可以作为回归，但不能被重新包装成增长混合指数的证明。

## Hard target and required outputs

Hard target: `GROWING_MIXED_INDEX_SHORT_BALL_OVERLAP_THEOREM_OR_COUNTEREXAMPLE`.

必须交付：

1. 一个明确的增长混合指数族或覆盖方案，以及与当前渐近坏事件阈值相容的真实短球半径。
2. observer-safe 去重后的见证类定义，保留足以重建局部素数块、ratio/annihilator 与 CRT 交互的 provenance。
3. 对不同见证类之间的重叠 multiplicity / Krylov-span / annihilator intersection 的精确或可证明上界，不能用全有限域均匀 ratio 统计替代实际短球人口。
4. 把局部重叠求和成 factorial moment、严格并集界或等价证书，并与现有一阶矩界同尺度比较。
5. 明确结论属于：指数前沿改善、仅常数级改善、或严格障碍/反例。
6. 至少一个可重复的精确整数验证器，有限计算只作证书/回归，不替代无穷结论。
7. 保留发现的高重叠合数族，即使它杀死目标上界；不得因其可分解为素数而删除。

第一步：消费 checkpoint 13 的 overlap 类型和事件去重接口，在一个可增长的两素数/三素数混合族上建立短球 witness catalog，并先比较实际 overlap degree 与全-field surrogate 的差异。

## Research value to preserve

这是判断“联合关系的重叠结构是否真的提供超越一阶矩的全局信息”的最直接试验。成功可改善全整数几何门槛；失败则给出一个重要 no-go，说明高阶联合概率的有限收益不会自动变成渐近指数收益。

## Success, kill, and return criteria

Success：得到可证明的增长重叠定理，并把它转成当前全局几何/窗口估计中的严格改进；或得到一个无限/可增长反例族，严格排除预期改进。

Kill：若证明最优可用 overlap 修正仅为与一阶矩同阶的常数因子，或高重叠族使二阶/高阶求和不可形成更强可求和指数，则记录精确障碍并结束此路线，不继续仅靠放大有限样本。

Return：提供 theorem/counterexample statement、证明草稿、精确验证器、与父界的定量比较、保留的 provenance schema，以及一个最小后继问题。不得把有限概率改善宣称为全局指数改善。
