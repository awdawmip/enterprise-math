# R5 — Universal adaptive-query noise saturation on the 101-budget count observer

Date: 2026-11-17 (Asia/Shanghai). Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Frozen science pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

## Object and question

This is the *derived* radius-two, 954-event, 28-candidate-cut indexed-center integer observer, with eight effective closure bits. For every effective mask `b` in `{0,...,255}` and budget `K` in `{214,...,314}`, the preceding frozen-source integer dynamic program gives a **positive integer** optimal-count readout `N_b(K)`. The current work is about those specified scalar readouts, not a claim of native Heartbeat-X6/BRC physical dynamics or a new full-state quotient.

An experimenter may make **any finite number** of budget queries, sequentially and adaptively. Each budget can be any integer `214 <= K <= 314`, can be repeated, and can depend on preceding reported values. Query response `y` obeys `|y-N_b(K)| <= epsilon*N_b(K)`. Errors may be chosen adversarially and independently on each response. The experimenter knows the exact count table and seeks a decoder guaranteed to recover `b` for *every* allowed error transcript. This strictly contains the prior family of fixed triples as a subclass.

## Theorem — no number of additional adaptive scalar reads improves the sharp worst-case radius

Let `rho_all` be the supremum relative observation-error level for guaranteed exact eight-bit recovery by any such finite adaptive query/decoder protocol. Then

`rho_all = rho_* = 535905744549271 / 298161762794076854 ≈ 0.001797365763897063`.

For every `0 <= epsilon < rho_*`, three nonadaptive queries `(214,230,302)` identify all 256 masks. For every `epsilon >= rho_*`, **no finite number of adaptive or repeated count queries** from the entire 101-budget set guarantees recovery. Equality is included in the obstruction because admissible closed error intervals touch. A randomized protocol cannot give an error-free, all-random-seeds guarantee above this threshold either.

### Proof: universal obstruction from one persistent residual pair

Choose `b_-=16` and `b_+=32` (the two distinct singleton-cut configurations corresponding to effective cuts 15 and 17). For every allowed `K`, let

`delta_K = |N_16(K)-N_32(K)| / (N_16(K)+N_32(K))`.

The exact source coefficients, independently recombined into all 256 count values, satisfy the following **complete finite certificate**:

* `delta_K = 0` for every `K=214,...,293` and for `K=314`.
* `delta_K` rises strictly in each of the nine comparisons `293->294, ..., 301->302` and falls strictly in each of the twelve comparisons `302->303, ..., 313->314`.
* Its unique global maximum is `delta_302 = 535905744549271 / 298161762794076854`.

All 101 comparisons with this rational upper bound use integer cross multiplication; 21 strict adjacent comparisons identify its unique maximizer. In the 20 budgets 294..313, the four single/double-cut counts are ordered `N_0<N_16<N_32<N_48`, and among their three consecutive positive symmetric relative gaps the central gap `delta_K` is always strictly smallest. The general nearest-neighbor fact follows since `(v-u)/(v+u)` is strictly increasing with the ratio `v/u` for positive `v>u`; a nonadjacent pair cannot be the closest pair in an ordered scalar list. The 20 scalar ordering and local gap statements are also directly checked using exact integers.

For `epsilon>=rho_*`, at any admissible budget `K` the relative-error intervals

`I_b(K) = [N_b(K)*(1-epsilon), N_b(K)*(1+epsilon)]`

of the two masks 16 and 32 intersect, because `epsilon>=delta_K`. Start any adaptive protocol with the same empty transcript in the two worlds. Whenever the protocol requests a `K`, return the same real value chosen in `I_16(K) intersect I_32(K)` in both worlds. The replies are individually admissible, and the next choices remain identical. Induction produces exactly the same full transcript for the two different masks, however many finite queries or repeats are made. The decoder cannot be correct for both. For randomized strategies, apply the same argument conditioned on a fixed random seed for any all-seed zero-error guarantee.

### Proof: attainability with three queries

A direct exhaustive independent check of `(214,230,302)` enumerates all `C(256,2)=32640` distinct mask pairs and computes the **exact** minimum of the maximum per-coordinate relative gaps. It equals `rho_*`, with minimizing pair `(16,32)`. The separate 64-state first/middle and four-state final-factor calculations check 2,016 and 6 unordered pairs, respectively, and give

`P(214,230) = 42558322421502812432044399936244961288 / 21096940239853073548183472853256642264015 > rho_*`,

`T(302) = rho_*`.

For `epsilon<rho_*`, each pair of masks has at least one query coordinate with disjoint admissible intervals; consequently the three-dimensional observation boxes of distinct masks are disjoint. The unique box containing the three reported values recovers the correct mask. Combined with the universal obstruction, this proves sharpness.

## Proof scope, checked data, provenance

`VERIFY_R5_ADAPTIVE_SATURATION.py` uses **only Python standard-library exact integers/Fraction** and the earlier source `compact_stdout.json`, whose SHA-256 is `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`. The stored source is generated by `r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py`; it declares status `PASS_R5_101_BUDGET_INTERACTION_HIERARCHY` and the unchanged science pin. The verifier checks this digest, scope and status before reconstructing the 101×256 table as `N_b(K)=sum_{T subset b} A_T(K)`. It then checks the 101 persistent-pair distances, the 21 strict steps, all 20 four-count order/gap conditions, and 34,662 pairwise checks (2,016+6+32,640). All pass; exact results and witness counts are in `RESULTS_EXACT.json`.

Reproduction:

`python VERIFY_R5_ADAPTIVE_SATURATION.py /path/to/compact_stdout.json > RESULTS_EXACT.json`

The proof applies to the declared finite count observer and *independently adversarial bounded real relative errors*. It does not claim that repeated queries are useless under an iid, unbiased, or otherwise stochastic noise model, nor does it cover other count observables, budgets outside `214..314`, or joint source-aware observations. Its exact finite checks are evidence at the stated frozen data/model, not a model-uniform symbolic recurrence theorem.

## Research significance and next question

The two closure masks 16 and 32 form a persistent indistinguishability residual under the full allowed scalar-query family once the error level reaches `rho_*`; retaining more repeated scalar observations does not repair this residual. The observable limitation is now attributed to the *available query alphabet*, not to the choice of a three-query schedule. The structural follow-up is to produce a local path-exchange/transfer certificate explaining the strict `293..302..314` gap peak and test a distinct provenance-preserving/joint observable capable of separating the cut-15/cut-17 residual beyond this sharp bound. This work stays distinct from the still-open center-set `max-new/min-old` recourse problem.

Formal claim/Result/Review acceptance and Activity association are governed by existing current Owner/CLAIM contracts. This is an independently preserved author result.
