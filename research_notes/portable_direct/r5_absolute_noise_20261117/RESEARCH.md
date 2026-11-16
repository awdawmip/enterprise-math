# R5 — Sharp absolute-noise saturation and four-query necessity (2026-11-17)

**Frozen science:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
**Status:** AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED. **Role:** independently preserved portable research, not Task CLAIM/Result/Review. The object is the derived radius-2, 954-event indexed-center **integer count observer**, not a promoted native X6 dynamical quotient.

## Model

Let `U=(3,8,9,10,15,17,25,27)` be the eight effective closure cuts. For each switch mask `b∈{0,...,255}` and integer budget `K∈{214,...,314}`, let the positive integer `N_b(K)` be the number of optimal paths. By the established common-optimum-cost/cohort theorem,

`N_b(K)=Σ_{T⊆b} A_T(K)`, with nonnegative integer `A_T(K)`.

An absolute-error observation returns a real number `y` obeying `|y-N_b(K)|≤η`. The same bound applies to all budgets and all calls. Errors may be adversarial and selected independently, and queries may be repeated or chosen adaptively. The objective is certain recovery of all eight bits. This differs from the preceding *relative-error* count-observer theorem.

## Theorem A — Universal sharp absolute-error saturation

Define

`D(b,c)=max_{214≤K≤314}|N_b(K)-N_c(K)|`,
`D_*=min_{b≠c}D(b,c)`.

For the pinned frozen 101×256 table the exact integer value is

`D_* = 1882951873548292168718745600000`.

The sharp uniform absolute-error bound is therefore

`η_* = D_*/2 = 941475936774146084359372800000`.

At any `0≤η<η_*`, the **four fixed queries** `K=(217,218,224,305)` identify all 256 states. At `η≥η_*`, **no finite number of adaptive or repeated scalar queries** using budgets 214–314 guarantees identification.

**Proof.** Two possible counts `u,v` have overlapping absolute-error intervals precisely when `|u-v|≤2η`. Exact integer enumeration over all `C(256,2)=32640` pairs and all 101 budgets establishes the displayed `D_*`. Exactly eight mask pairs realize this minimum: `(11+16j,14+16j)` for `j=0,...,7`. For `b=11,c=14`, the gap has its **unique** maximum `D_*` at `K=217`, and is strictly smaller at all other budgets. An adversary at `η≥D_*/2` may therefore return an intersecting value at *every* requested budget, keeping identical transcripts for the pair under an arbitrary adaptive protocol. In the opposite direction, a complete 32640-pair integer check gives

`min_{b<c} max_{K∈{217,218,224,305}} |N_b(K)-N_c(K)| = D_*`.

Thus the four-dimensional error boxes are disjoint for `η<D_*/2`, giving a unique decoder. Both directions include the equality boundary.

## Theorem B — Four calls are necessary near the sharp threshold

For every `η` satisfying

`1752576979999614335377735680000/2 ≤ η < η_*`,

**any guarantee of full eight-bit recovery needs at least four queries, even adaptively**.

**Proof.** The exact positive-cohort support partitions useful budget queries into early `214..221` (cuts 3/8/9/10/27), middle `223..291` (cuts 25/27), and late `294..313` (cuts 15/17) windows. Other budgets cannot replace an omitted group: in particular 222 cannot observe cut 25, and neither 293 nor 314 separates the singleton late masks 16 and 32. Any valid three-call protocol must therefore use one query in each window on every full-identification transcript.

The four masks `4,10,11,14` have identical outputs at every middle and late budget. Until the first early query their observation transcripts may be identical. For the two pairs `(4,10)` and `(11,14)`, the smaller of the two count gaps at a given early budget is *at most* `1752576979999614335377735680000` (the exact maximum over early budgets, attained at 218). At 217 the pair 4/10 has gap `1744659037213380157479321600000`; at 218 the pair 11/14 has gap `1752576979999614335377735680000`. Hence any single early query leaves at least one pair's error intervals intersecting at the stated `η`. With only one early query available, the identical middle/late counts cannot split that pair. This proves the adaptive lower bound.

As an additional complete finite optimization, a **fixed three-query** decoder must take one budget from each window. The first/middle observations depend on the same six bits `(0,1,2,3,6,7)` and the late observation only on bits `(4,5)`. Splitting all mask pairs into these product factors gives a sharp three-query absolute margin `min(P_abs(K1,K2),T_abs(K3))`. Exhaustive testing of `8×69=552` early/middle budget pairs and their 2016 unordered 64-state pairs gives

`max P_abs = 1744659037213380157479321600000` (e.g. `K1=217,K2=290`).

The late four-state factor gives

`max T_abs = 2653627577676347634246872444436480` (at `K3=305`).

Thus the **best fixed three-query margin** is `1744659037213380157479321600000`, strictly below the sharp four-query margin. The exact optimum over *adaptive* three-query protocols further below the proven four-query-necessary interval is open.

## Exact executed certificate and scope

Executed Python standard-library **integer-only** postprocessing of the previously saved cohort file `compact_stdout.json`, SHA-256

`a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`.

Source generator: `research_notes/portable_direct/r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py`. The companion exact-count table was also checked entry-by-entry for all **25,856** values. Its earlier independent mask-specific DP checks retain their original scope; this turn verifies exact cohort postprocessing and pairwise integer calculations, not a second 256-mask direct DP rerun.

The local executed verifier returned `PASS_R5_ABSOLUTE_NOISE_FOUR_QUERIES_SHARP`. Exact checked coverage: **3,296,640** full-state pair/budget differences, **32,640** pair comparisons for the four-query certificate, **552** first/middle budget pairs × **2016** six-bit state pairs, and all 20 late budgets × six two-bit state pairs. The full executable, proof and precise JSON results are in this same research directory.

The result compares absolute-error versus previously studied relative-error instruments. Under the relative model the persistent bottleneck is the late pair `(16,32)` at K302. Here the persistent bottleneck is the early pair `(11,14)` at K217, and a fourth query is necessary near the sharp threshold. This demonstrates mathematically that which provenance residue dominates identification depends on **observation-error geometry**.

**Next unresolved units:** exact adaptive three-query absolute margin below the four-query-necessary interval; local path-exchange explanation of the 217/218 early-cut bottlenecks; independently the original indexed-center `max-new/min-old` recourse distance, requiring center-set rather than aggregate count evidence.
