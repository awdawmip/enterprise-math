# Enterprise Math C269 / Research2 — seven four-free positive hulls by 5,666 exact leaves

> **AUTHOR_EXACT_AUXILIARY / UNMERGED RESEARCH EVIDENCE ONLY**. No service-issued RESEARCHER identity, no CLAIM, no native Source Result, no independent Research Driver acceptance. These are exact inequalities for the C195/H168 positive-rational 79-node *auxiliary*; not a native GF(2)-BRC or X6 Cell theorem.

## Frozen provenance, authority and frontier reconciliation

- GLOBAL_KNOWLEDGE_V1 canonical `main@0d1a36da02cbd766d83a625e62c9a47076edd4e5`, entry `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, current P000, ACTIVE worldview, mathematical research and BRC policy.
- Enterprise Math source snapshot `main@88e7583805cf84fa13de7805165103a29d3f6cf0`; current `docs/PORTABLE_RESEARCH_PROTOCOL.md`, researcher role and activity registration rules. Publication branch based on later observed repository main `6c6e3f37d66d64b793ed58c4dbbf4f5d166c9744`; **research inputs and exact arithmetic did not change**.
- C265 author archive SHA256 `dcf541ec1158d872eec5559548296197908e496da209a539f172955cbc73ff31`. Reconciled *unmerged author* descendants: C266 21-pair branch `research/c266-author-fourfree-21-pairs-20261023`, C266 complementary branches, and C268 `research/c268-r2-24-pairs-20261023`. Deduplicated pre-C269 frontier among 363 eligible pairs: 213 strict-negative witnesses, 136 whole-hull strict-positive certificates, **14 unclassified**. None is asserted admitted as canonical Source mathematics.
- Native calls `em_status` and `em_control_tasks` failed with `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false`. Active owner, service-issued Researcher-ID, research session and legitimate CLAIM were **not verifiable**. This file is an isolated author handoff, not a task registration or claim.

## Model, exact statement

Let `I=(5,50,55,56)`, `J={0,…,78}\\I`, `Q=2^128`, `H=2^166`, `Z=141421356237309504880/10^20`, `A=6912*50000^2/17^2`; the original 79 strictly increasing rational nodes `u[0:79]` are embedded in the standalone replay. For each `j∈J`, define positive integer

`B_j = floor((Q*A/H)/(((2-u_j²)*(3-u_j²))³) * PRODUCT_(r!=j) (Z-u_r)/abs(u_j-u_r)) > 0`.

Define the exactly specified positive-rational auxiliary function (on admissible, pole-free, order-preserving inputs)

`F(v) = SUM_(j∈J) B_j * PRODUCT_(p∈I) [(Z-v_p)/(Z-u_p)*abs(u_j-u_p)/abs(u_j-v_p)] + SUM_(k∈I) [ Q*A/(H*((2-v_k²)*(3-v_k²))³) * PRODUCT_(j∈J) [(Z-u_j)/abs(v_k-u_j)] * PRODUCT_(p∈I,p!=k) [(Z-v_p)/abs(v_k-v_p)] ]`.

**C269 exact theorem.** Every real four-tuple in the union of the six closed rational boxes below satisfies

`F(v) ≥ 2^128 + 37182935124052974981749991256406 > 2^128.`

Each of the four interval columns describes `v5; v50; v55; v56`. The strict integer margin is `min_leaf(floor(LB_leaf)-Q)`, not a floating point gap.

| Root hull | Four exact coordinate intervals | Exact positive leaves | Exact splits | Minimum integer margin | New previously unresolved pairs |
|---|---|---:|---:|---:|---|
| (8,28) | [1/135,2/137]; [16/23,7/10]; [18/23,27/34]; [4/5,9/11] | 623 | 622 | 4960982668873717258996227450137455 | (8,28) |
| (13,28) | [1/123,2/137]; [34/49,7/10]; [18/23,59/74]; [4/5,9/11] | 755 | 754 | 3046191377545063607211587604835111 | (13,28) |
| (9,28) | [1/135,2/137]; [16/23,7/10]; [18/23,4/5]; [49/61,9/11] | 868 | 867 | 215022374969642592997642504667492 | (9,28) |
| (16,27) | [1/119,3/205]; [7/10,12/17]; [32/41,37/47]; [4/5,9/11] | 2058 | 2057 | 90075347811762162781930272439461 | (16,27), (26,27) |
| (24,28) | [1/104,2/137]; [34/49,7/10]; [18/23,4/5]; [41/51,9/11] | 502 | 501 | 501373498366947830264906619737683 | (24,28) |
| (21,28) | [1/105,3/205]; [16/23,18/25]; [53/68,53/67]; [13/16,23/28] | 860 | 859 | 37182935124052974981749991256406 | (21,28) |
| **Total** | **six entire pole-free closed roots** | **5666** | **5660** | **37182935124052974981749991256406** | **seven distinct new pairs** |

### Why this covers continuous regions

The 75 fixed positive branches contain factors `(Z-t)/abs(u_j-t)`, monotone and convex on each pole-free, order-preserving coordinate interval; independent coordinates admit valid rational-endpoint lower bounds. A positive moving branch has strictly positive log-second derivative in its own coordinate:

`6*(2+t²)/(2-t²)² + 6*(3+t²)/(3-t²)² + SUM_(j∈J) 1/(t-u_j)² + SUM_(p∈I,p!=k) 1/(t-e_p)² > 0`.

A convex tangent gives a *global* lower bound. Keeping a common coordinate in a fixed-branch sum plus the corresponding moving branch and using one joint tangent gives a stronger `SHARED_k` lower bound; every discarded coordinate is bounded using valid positive endpoints. `BASE` is the all-unshared variant. Each internal tree symbol `0/1/2/3` bisects the indicated interval at its **exact rational midpoint**; terminal `B/A/C/D/E` invokes `BASE/SHARED_5/SHARED_50/SHARED_55/SHARED_56`. Two closed children cover their parent, hence all terminal lower bounds cover *all real points*, not just sampled vertices. Each of the 5666 terminal `floor(LB)-Q` is strictly positive, computed with Python `Fraction` using exactly the same 79 raw nodes and original integer floor weights.

## Verification and new classification

Primary builder reused the prior C257 exact bound implementation and produced the full six-tree JSON certificate with every rational leaf and margin. **A second separately coded executable checker** reconstructs the weights independently from the raw nodes, decompresses six trees with checked SHA256, recomputes all exact rational inequalities and verifies tree coverage, and is written to `C269_STANDALONE_REPLAY.py`. Its complete validation was performed in three independent root partitions, rather than asserting one timed-out monolithic process passed:

- `python C269_STANDALONE_REPLAY.py 0 1 2`: exact **PASS**, 2246 leaves, 2243 splits.
- `python C269_STANDALONE_REPLAY.py 3`: exact **PASS**, 2058 leaves, 2057 splits.
- `python C269_STANDALONE_REPLAY.py 4 5`: exact **PASS**, 1362 leaves, 1360 splits.

Combined: **5666/5666 exact positive leaves, 5660/5660 bisections**; author arithmetic cross-check **PASS**, formal proof assistant and independent Driver review **NOT DONE**. All seven new pair-box containment comparisons were made with exact fractions against the C254 35-box data.

New deduplicated **unmerged author evidence** frontier: **213 negative + 143 whole-box positive + seven unknown = 363 eligible**. The seven still open are `(4,18), (12,18), (14,18), (18,23), (18,27), (18,33), (21,22)`. The 232 combinations excluded from the historic method's domain remain excluded; original 35 base rectangles and historical 15685 candidate inputs were not rerun.

## Boundaries and next discriminating question

The positive rational branches provide **no proved map** of original GF(2)-BRC phase/sign, ordered branches, labels, provenance, ports or future observer operations. P000, six native axes, separate time, three-axis slice and native angles are unchanged. The four active numbers of this auxiliary are *not* four native spatial dimensions. This is not native physics, Shor gain, mathematical admission or formal task completion.

Next: attack the **seven remaining full four-coordinate hulls** with exact shared-coordinate joint bounds, or use the separate C267 coordinatewise-convex 16-vertex upper-bound method to find and prove a nonzero-volume `F<Q` region in one of them. The relatively costly (4,18) and (18,33) boxes were explored but **not certified** here. Reconcile the genuine active Owner/CLAIM before formal Source Result publication; author-level GitHub preservation must not be mistaken for native state-machine progress.

**Research status:** `C269_AUTHOR_EXACT_AUXILIARY / 7_NEW_POSITIVE_PAIRS / 5666_STRICT_LEAVES / 143_AUTHOR_POSITIVE_TOTAL / 7_UNRESOLVED / THREE_PARTITION_REPLAY_PASS / NO_NATIVE_CLAIM / NO_INDEPENDENT_REVIEW / NOT_ADMITTED`.

Global-Knowledge-Sync: main@0d1a36d / GLOBAL_KNOWLEDGE_V1
