# R5: Global optimizer-family inertness from full-budget interval factorization

Date: 2026-11-14. Scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Status: **author-side finite theorem, reproducible exact calculation; NOT_REVIEWED**.
Observer: 954 labeled integer event coordinates, event-index candidate centers, covering radius 2, sum of distances to nearest selected center. Gap indices start at 0. This is an auxiliary one-dimensional observer, not a native X6 or physical-dynamics theorem.

## Result: eleven gaps globally preserve the *entire optimizer index-set family*

For a subset `B` of the 28 length-3 gaps, close each gap in `B` from length 3 to length 2, translating subsequent event coordinates and preserving all 954 event labels. Let `Opt_B(K)` be the family of all feasible exactly-`K` center **index subsets** attaining minimum nearest-center total cost. Thus `Opt_B(K)` is empty for infeasible budgets.

Define

`I_0 = {0,1,7,14,18,19,20,21,22,23,24}`.

**Theorem (complete arbitrary-background optimizer invariance).** For every `i in I_0`, every subset `B ⊆ {0,...,27}\{i}`, and every integer `K`,

`Opt_B(K) = Opt_{B ∪ {i}}(K).`

In particular, the full optimal-center-index-family readout factors through the other **17** closure bits; every one of its distinguishable states is represented by at least `2^11 = 2048` original closure patterns. This theorem is exact for all `2^28 = 268435456` closure patterns and all budgets, by structural factorization rather than individual enumeration.

Within the 13 gaps previously proved **globally inert for the optimum-cost spectrum**, the remaining gaps `15` and `17` are not optimizer-family inert. Earlier immutable, explicit 293-center witnesses for each gap establish a strict family expansion for the empty background at `K=293`. This yields the complete classification of the 13 cost-inert gaps by whether they ever change the optimizer family.

## Why local full-budget factorization proves this universal statement

The 28 original gaps of length 3 partition the event sequence into 29 nonempty ordered blocks `0,...,28`. For every `0 ≤ a ≤ b ≤ 28`, let `L[a,b](k)=(j_{a,b}(k),n_{a,b}(k))` be the **entire** feasible budget profile of the subinstance containing blocks `a,...,b`, with all gaps internal to that run closed. Here `j` is the minimum total cost, `n` is the number of optimal center-index subsets, and infeasible budgets are absent. There are 435 such local profiles.

For two independent profiles, define their min-plus convolution with tie counting by

`(P ★ Q)_k.c = min_{r+s=k}(P_r.c+Q_s.c)`,

`(P ★ Q)_k.n = sum_{r+s=k, P_r.c+Q_s.c=(P ★ Q)_k.c} P_r.n Q_s.n.`

An unclosed gap is length 3, larger than the radius 2. Every feasible center set must cover events on each side internally, and every nearest-center distance within either side is at most 2. Consequently the feasible optimizer profile of independent runs is their exact `★` convolution; selected-center labels combine bijectively, so ties are counted without duplication.

For each potential split gap `i`, every `a≤i<b` gives the candidate identity

`L[a,b] = L[a,i] ★ L[i+1,b]` **at every feasible budget, for both cost and optimizer multiplicity**.

The included exact checker constructs all 435 profiles from the immutable frozen generator using the center-index path-DP recurrence in the earlier PR #2379, and checks all straddling pairs. For each `i in I_0` this identity holds for every straddling pair and every budget. In an arbitrary closure background `B`, toggling `i` only merges the two neighboring maximal runs `[a,i]` and `[i+1,b]`. The recorded identity preserves the joined/split profile. Every other maximal run remains unchanged. Associativity of `★` preserves the **global** minimum cost and optimizer count at each budget.

Finally, the gap-shortening feasibility lemma already established on this exact derived observer shows `Opt_B(K) ⊆ Opt_{B∪{i}}(K)`: any previously feasible index set stays feasible with unchanged cost (cross-gap candidate distances were at least 3). Since the exact global optimum costs and integer cardinalities coincide, inclusion between finite families is equality. This establishes equality of the full index-set families, not only their numerical multiplicities.

## Exact calculated certificate

The verifier checks **1,916** straddling-run combinations for all 13 cost-inert candidate gaps, comprising **490,974** full-budget join/split comparisons.

* All **1,510** straddling runs for the eleven indices in `I_0` match exactly, for all feasible budgets, both minimum cost and optimizer multiplicity, with no newly feasible budgets.
* Gap `15`: 208 straddling runs, 2,198 budget comparisons with a strict optimizer-count difference; all minimum costs and feasible-budget domains agree. First witness: local run `[0,16]`, `K=68`, cost `191`, optimizer counts `457450241040` (unclosed) versus `519720954480` (closed).
* Gap `17`: 198 straddling runs, 2,183 budget comparisons with a strict optimizer-count difference; again the cost and feasible-budget domains agree. First witness: run `[0,18]`, `K=77`, cost `223`, counts `12717595706400` versus `13838468548320`.

The checker also compares the selected-center path-DP routine with exhaustive enumeration for 144 seeded small integer-coordinate inputs. Exact arithmetic only; the main certificate is the complete finite run/budget comparison, not randomized extrapolation. All 954 original event labels remain distinguishable.

Companion materials: `VERIFY_R5_OPTIMIZER_FIBER_FACTORIZATION.py`, `EXACT_GLOBAL_OPTIMIZER_FIBER_FACTORIZATION.json`. The verifier imports the two prior immutable PR #2379 routines from `research_notes/brc_r5_exact_cost_spectrum_20261114`; scientific input stays on the same frozen pin. Earlier endpoint witness and theorem: `research_notes/brc_r5_cost_inert_optimizer_residual_20261114/INERT_GAP_OPTIMIZER_RESIDUAL.md` at `a558dd36a3238b66872b5c162ec8e8c2751d3af3`.

## Validation and remaining research

This run executed an equivalent locally reconstructed version of the complete-profile recurrence and exhaustive small-case checks; all assertions passed. Code, proof and numerical output are authored evidence pending independent mathematical review. The posted script's **exact remote bytes** should be run separately in a repository checkout to close the reproduction gap.

Next: determine the **exact circumstances and optimizer-set edit-distance effects** of the two still optimizer-active but cost-inert gaps `15,17` under all intermediate closure backgrounds. For that, the 17-bit family quotient is sufficient, while full center identities and route/provenance evidence must be retained. The native 2,520-byte / 28-coordinate / 8,192-prefix-query experiment remains a distinct unfinished task. No formal R5 Task CLAIM or Result/Review is asserted by this research note.
