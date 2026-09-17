<!-- ENTERPRISE_MATH_TASK_V1
{"task_id":"X6CM-LOCAL-BAD-SEED-DECAY-20260917","title":"X6 局部坏种子衰减与 epsilon-zero 几何前沿","kind":"RESEARCH","owner":"taskbook/unassigned","base_state":"READY","priority":"P1","leverage":"HIGH","frontier":"The tunable local geometry theorem can make the bad-seed fraction arbitrarily small only by paying an epsilon-dependent positive geometry constant; no p- or layer-decay law is known at a fixed positive uniform constant.","next_action":"Fix one positive prime-power geometry threshold independent of p and layer, count bad dual-seed lines across local blocks, and prove a decay law, a nondecay obstruction, or a quantified intermediate rate; then propagate the exact conditioning factor to the global gamma/alpha frontier.","created_by_role":"RESEARCH_DRIVER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"X6CM-LOCAL-BAD-SEED-DECAY-20260917","parent_objective_id":"OBJ-X6CM-ALL-INDEX-GEOMETRY-20260917","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","identity_lane":"X6CM","origin_kind":"DRIVER_ROADMAP","task_lineage":"CONTINUATION","parent_task_id":"X6CM-DRIVER-ALL-INDEX-GEOMETRY-20260917","successor_gate":{"new_information_gap":"The tunable good-seed construction approaches epsilon zero but does not show that the bad-seed fraction decays with prime size or block layer while a positive uniform prime-power geometry constant is retained.","why_parent_result_does_not_close_it":"Checkpoint 12 provides an arbitrarily small positive epsilon construction and an epsilon-dependent geometry constant; it does not establish decay of bad-seed density or attain the epsilon-zero critical frontier.","discriminating_outcomes":["A quantitative decay law in p or layer makes the conditioning factor summable/bounded enough to reach or improve the epsilon-zero frontier.","An infinite family has a nonvanishing bad-seed fraction for every fixed positive geometry constant, giving a strict obstruction.","An intermediate decay rate yields a new explicit gamma/alpha frontier without full epsilon-zero closure."],"kill_condition":"If a nondecaying lower bound for bad-seed fraction is proved on an infinite local-block family under any fixed positive uniform geometry constant, record the obstruction and stop attempts to reach epsilon zero by this mechanism.","alternative_route_or_free_exploration_considered":"The independent actual-overlap-growth route is published in parallel; weakening the geometry constant to zero or changing the observer is not accepted as closure.","why_new_stage_or_task_is_better_than_same_task_or_closure":"This is a distinct local finite-field/lattice-counting question whose outcome can be translated globally and assessed independently of mixed-index witness-overlap counting."},"source_refs":["awdawmip/enterprise-math@50eb9a8f720e46aa973e54d1e8e38b61fc9dfcb4:research_notes/x6_witness_overlap_checkpoint_20260911.json","awdawmip/enterprise-math@7abd6f9523e1f6edc4c714b93c9e81dde588633e:research_notes/x6_tunable_geometry_checkpoint_20260911.json","awdawmip/enterprise-math@b89e6628783609f5f883353ddb6f7339e600d8f6:research_activity_records/RA-X6CM-F01144F76207.json"],"dependencies":[],"evidence_status":"TASK_DEFINED_NOT_EXECUTED","tags":["X6CM","bad-seed","prime-power","epsilon-zero","geometry","BRC"],"claim_lease_minutes":120,"policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf","review_state":"PASS","temporary_overrides":[]}}
-->

# X6 局部坏种子衰减与 epsilon-zero 几何前沿

Status: `READY / PUBLISHED_REGISTERED`

## Mother question

能否在保持一个与素数 p 和层级 r 无关的正 prime-power 几何常数时，证明局部 bad-seed 比例随 p、层级或块复杂度衰减，从而消除当前全局条件化中必须支付的固定 epsilon，并真正达到或逼近 epsilon-zero 的临界几何/乘数窗口前沿？

## Frozen inputs and scope

冻结 `X6CM-TUNABLE-GEOMETRY-20260911-12` 的局部 ideal block、信息最优 cyclic flag、对偶 seed line 与原生 Q 长度定义。其 epsilon>0 定理作为已有输入，不重做。

冻结 P000、四个已有种子锁定、全部正整数中间格关系、未来信息尖锐下界以及 U 的非原生非等距身份。

不得把“让几何阈值趋于 0”作为 bad-seed 比例趋于 0 的证明；目标要求存在一个固定正的、全块一致的 prime-power 几何尺度常数。不得仅用随机大素数样本外推无穷衰减。

## Hard target and required outputs

Hard target: `LOCAL_BAD_SEED_DECAY_LAW_OR_NONDECAY_OBSTRUCTION_AT_FIXED_POSITIVE_GEOMETRY`.

必须交付：

1. 一个固定正几何阈值/常数的精确定义，与父 checkpoint 的 λ1/λ6/短向量条件兼容。
2. 对每个局部块 `(p,r)` 的 bad dual-seed 比例的可证明公式或上下界，显式显示 p、residue degree、层级或其他真实参数。
3. 至少一条无穷方向的结论：比例衰减率、非衰减下界，或分情形分类；有限枚举不能代替该结论。
4. 将局部比例翻译成冻结全整数种子乘积测度下的条件化算术主项，并重新计算单目标 `gamma`、乘数窗口 `alpha` 与例外强度之间的可证前沿。
5. 明确是否达到 epsilon=0 临界关系，若不能，指出阻碍该等号的精确局部项。
6. 精确回归验证器覆盖已有 p=2,3,13 块与若干新块，四个锁定必须继续通过。
7. 若发现坏比例不衰减的块族，保留其完整局部结构和合数组合影响，不用平均值抹去。

第一步：选择一个固定正阈值，重写父笔记的 packing/counting 证明，使 bad seed 计数暴露其 p 与层级依赖；先对可完全枚举的小块核验公式，再证明无穷族行为。

## Research value to preserve

这条路线不依赖混合合数事件之间的独立性。如果 local bad mass 本身衰减，就可能直接减少全局条件化成本；若它不衰减，则会给 epsilon-zero 路线一个干净障碍，防止以后反复靠“再把 epsilon 调小”制造表面进展。

## Success, kill, and return criteria

Success：证明足够强的局部衰减并严格改善/闭合全局前沿；或证明一个无限块族的非衰减下界，形成明确 no-go；中间速率也可成功，只要它导出新的精确全局参数关系。

Kill：若在固定正几何常数下已经证明 bad-seed 比例存在不趋零的统一下界，则停止同机制的 epsilon-zero 尝试，返回反例族与全局后果。

Return：提供局部定理或反例、全局翻译公式、精确有限回归、四锁定兼容性、未完成项和一个可执行后续动作。不得把 epsilon-dependent 常数趋零与固定正常数下的衰减混为一谈。
