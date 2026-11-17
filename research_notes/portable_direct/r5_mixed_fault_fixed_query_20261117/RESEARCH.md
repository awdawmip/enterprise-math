# R5 — Exact fixed-budget mixed erasure / Byzantine corruption theorem

Date: 2026-11-17. Scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Scope: the frozen 954-event derived indexed-center optimal-count observer `N_b(K)`, 256 effective closure masks, integer budgets 214–314. Evidence: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.

## Exact theorem (all fault counts)

A fixed **nonadaptive multiset** `Q=(k_1,...,k_n)` of budgets may contain independent repeated queries. A clean query returns the exact integer `N_b(k_i)`. Up to `e` positions may be erased (locations declared), and up to `f` other positions arbitrarily replaced. For every possible hidden mask `b` and every such adversarial fault pattern, the remaining record must uniquely identify `b`. The objective is the numeric budget sum `C(Q)=Σ k_i`.

For **every pair of integers e,f ≥ 0**, put `r=e+2f+1`. The exact optimum is

`C_fixed*(e,f) = 731r = (214+223+294)(e+2f+1)`.

The **unique** minimum-cost multiset, modulo ordering, consists of `r` copies each of 214, 223, and 294. Its minimum code Hamming distance is exactly `r`.

Examples: one erasure -> cost 1462, six readings; one arbitrary corrupted reading -> 2193, nine readings; one erasure plus one corruption -> 2924, twelve readings.

## Proof

**Coding criterion.** For distinct states `a,b`, let `d_Q(a,b)` count the query positions on which `N_a(k_i)≠N_b(k_i)`. Correcting `e` known erasures and `f` arbitrary symbol substitutions is possible iff `min_(a≠b) d_Q(a,b) ≥ e+2f+1`. Sufficiency follows because after removing at most `e` coordinates the remaining codewords differ on more than `2f` positions, so their corruption-radius-`f` balls are disjoint. For necessity, erase up to `e` differing coordinates and partition the at most `2f` remaining differences between the two candidate corruption sets to create an identical received record.

**Three disjoint exact witnesses.** Across *all* 101 allowed budgets, integer-count comparison produces these complete supports:
- `(a,b)=(16,17)`: disagreements **exactly** at 214–221 (8 budgets);
- `(a,b)=(16,80)`: disagreements **exactly** at 223–291 (69 budgets);
- `(a,b)=(16,32)`: disagreements **exactly** at 294–313 (20 budgets).

The support sets are disjoint. In particular the late witness is equal at budget 293, so 293 cannot replace 294 in this lower bound. Any robust fixed multiset must include at least `r` query positions in *each* support. Their unit budget costs are at least 214, 223, and 294 respectively, proving `C(Q)≥r(214+223+294)=731r`.

**Attainment and uniqueness.** All 256 signatures `(N_b(214),N_b(223),N_b(294))` are distinct by exhaustive exact integer reconstruction. Repeating each of these three budgets `r` times gives pairwise Hamming distance at least `r`. Each of the three witness pairs differs at exactly one of the three base budgets, so the minimum distance is exactly `r`. Equality in the lower bound forces exactly `r` coordinates from each disjoint support, all chosen at that support's **unique** minimum budget. This proves the theorem and uniqueness for arbitrarily large `e,f`.

## Source, recomputation and typing

The exact integer observer derives from the previously validated source-requirement cohort subset-zeta transform `N_b(K)=Σ_(T⊆b) A_T(K)`, which retains requirement-mask/provenance information within this positive-count branch carrier. This is not a theorem of native X6 six-axis dynamics, a physical fault-channel claim or a statement about signed/phase carriers.

The companion Python verifier reads the original 101-budget coefficient output and performs an eight-bit exact subset-zeta reconstruction of 25,856 integers, checks the three entire witness-support sets, the unique 256 signatures and five exact Hamming-distance cases. It optionally cross-checks the independently stored full table. Verified input hashes:
- `compact_stdout.json`: SHA-256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`.
- `EXACT_R5_ALL_101_BUDGETS.json`: SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

The coefficient input can be regenerated from the previously saved `research_notes/portable_direct/r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py` and the frozen source. Run `python VERIFY_R5_FIXED_ERASURE_CORRUPTION.py compact_stdout.json [EXACT_R5_ALL_101_BUDGETS.json]`. `RESULTS_EXACT.json` records the actual two-input validation output. Source lineage: `r5_single_sweep_cohort_zeta_20261116/RESEARCH.md`, `r5_all_budget_cohort_hierarchy_20261116/RESEARCH.md`, and `r5_complete_adaptive_cost_diagram_20261117/RESEARCH.md`.

## Next scientific questions

Find the optimal **feedback-adaptive** cost when erasure locations become visible, and when arbitrary corruptions require robust interactive decoding; the fixed-budget theorem does not determine adaptive cost. Next combine bounded absolute count error with erasures/corruptions using exact pairwise margins, and retain the original `K=214..291` max-new/min-old optimal-center replacement-distance frontier.

Author-side portable research only. An authenticated task CLAIM, protected Activity update, Result and independent Review are separate state transitions.
