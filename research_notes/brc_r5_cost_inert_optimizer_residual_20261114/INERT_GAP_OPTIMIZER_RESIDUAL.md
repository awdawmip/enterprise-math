# R5: cost-inert gap closures with nontrivial optimal-index-set residuals

**Date:** 2026-11-14. **Evidence:** author-side exact finite theorem, independent mathematical review NOT_REVIEWED. **Frozen scientific input:** `435e77af0d180eac32bd1f9c4c464bc4010b7551`. **Scope:** the 954-event, one-dimensional integer-coordinate, radius-two indexed-center cover observer. Source branch is a continuation of Draft PR #2379. All event and gap indices are zero-based.

## Exact problem

Let `x_0 < ... < x_953` be the immutable frozen coordinates reconstructed by `VERIFY_R5_COST_SPECTRA.py`; let `C={0,...,27}` index the 28 original gaps of length three. For a subset `B ⊆ C`, shorten exactly these gaps from three to two and retain all original event labels. For each center-index subset `S` of size `K`, define its covering radius as the maximum nearest-center distance and its cost as the sum of nearest-center distances in the modified coordinates. `Opt_B(K)` is the family of feasible size-`K` index subsets with minimum cost.

The preceding cost spectrum result in Draft PR #2379 establishes that each of the 13 gaps

`I={0,1,7,14,15,17,18,19,20,21,22,23,24}`

is **globally inert for feasible-budget / optimum-cost readout**, i.e. adjoining a cut `i∈I` does not change `J_B(K)` for any other gap set `B` and any common feasible budget. This note resolves a stronger readout for two of them.

## New exact finite theorem

For each `i∈I`, compare the optimizer families along both chains

`Opt_empty(K) ⊆ Opt_{ {i} }(K)`

and

`Opt_{C\{i}}(K) ⊆ Opt_C(K)`.

For **i=15 and i=17**, both inclusions are **strict for exactly K=293,294,...,314** and are equal for every other feasible budget. The empty/single comparison has 742 common budgets `213≤K≤954`. The all-except/all comparison has 748 common budgets `207≤K≤954`. For each of the other eleven cost-inert cuts, both endpoint-context inclusions are equal for all these budgets.

In particular, **globally cost-inert does not imply optimizer-index-family inert** even for a single closure, and the information loss occurs in a 22-budget interval where optimum cost is unchanged.

For K=293, all four compared instances have cost 741. Their optimizer counts (event-index sets, exact integers) are:

| Case | count |
| --- | ---: |
| no cuts | 12606779601463240519046922240 |
| only cut 15 (equally: only cut 17) | 13102659259476980304288153600 |
| all except cut 15 (equally: all except cut 17) | 13102659259476980304288153600 |
| all cuts | 13598538917490720089529384960 |

At K=314, no-cut count is `34372089438980233382036766720000`, single-15 and single-17 counts are each `34461624376467130391986176000000`, and the fully closed count is `34551159313954027401935585280000`. At K=292 and every K≥315 all four counts agree, consistent with the universal full-family invariance theorem in this PR.

## Concrete new optimizers

For each i∈{15,17}, the companion certificate gives the exact 954-bit selected-center indicator in **hexadecimal** (`hex_mask`; bit j=1 means event index j is chosen). Decoding produces exactly 293 distinct center indices.

- With only gap 15 closed: the center set has modified maximum nearest-center distance 2, total distance 741 and old, unclosed maximum distance 3; event index **194** is left uncovered under the unclosed coordinates.
- With only gap 17 closed: the analogous values are 2, 741 and 3; old event index **245** is uncovered.

Thus the displayed sets are exact new optimal witnesses, because the previously established fixed-budget theorem yields `J_{ {i} }(293)=741`, while these center sets were not feasible before closure. The short verification program decodes and checks both entire center sets directly.

## Proof of the finite classifier

For any `B⊆B'` differing by closure of a cost-inert gap, the previous exact gap-closure lemma establishes that an already feasible center-index set remains feasible with the **same cost**. Since the global minimum costs agree, `Opt_B(K)⊆Opt_{B'}(K)` at every jointly feasible K. Hence equality of *integer optimizer counts* is equivalent to equality of the actual finite index-set families, and unequal counts prove strict containment.

The exact path-count recurrence has one state per last center and number of centers:

`F_1(j)=sum_{t<j}(x_j-x_t)` if `x_j-x_0≤2`, otherwise infinity; `N_1(j)=1` in feasible states. For successive centers `i<j`, require every intervening event `t` to have `min(x_t-x_i,x_j-x_t)≤2`; assign edge weight `e(i,j)=sum_{i<t<j} min(x_t-x_i,x_j-x_t)`. Update `F_{k+1}(j)=min_i(F_k(i)+e(i,j))` and sum `N_k(i)` over ties. A feasible right suffix contributes `sum_{t>j}(x_t-x_j)`. Every selected center-index set corresponds to a unique increasing path; interior nearest-center choices are determined by the two neighboring selected centers. Therefore this recurrence counts each optimal center-index set exactly once, including distance ties.

The companion verifier calls the exact existing `optimum_counts_spectrum` for each of 28 closure masks: empty, full, 13 singleton cuts, and the 13 full-minus-one cases. It checks known K=214,292,315,954 endpoint values as regression pins, all per-budget cost equalities, monotonicity of each count, and the complete sets of budgets with strict optimizer-count increase. The verifier also checks both exact bitmask witnesses against the full 954-event inputs and checks small-instance enumeration. Existing source scripts are inherited from the same PR branch, not regenerated from a changed scientific input.

## Source, reproducibility and remaining question

Run from this directory's parent `research_notes/brc_r5_exact_cost_spectrum_20261114` source folder using `PYTHONPATH` or install the two source scripts side-by-side. `VERIFY_R5_INERT_OPTIMIZER_RESIDUAL.py` imports the exact existing frozen-coordinate and path-DP routines and validates the provided result JSON. The original author-side expanded two-flag construction was also locally executed (old-infeasibility flag carried along a chosen-center path); the standalone verifier checks its explicit outputs.

**Unresolved:** Classify these 13 gaps for arbitrary intermediate closure backgrounds, rather than only the empty/single and all-except/full endpoints. In particular, determine whether any of the other eleven gaps can affect optimizer sets only under intermediate backgrounds; also determine the resulting exact minimum-reconfiguration-distance effects. A scalar cost spectrum is an insufficient carrier for those future readouts. Preserve event labels, optimizer multiplicity, branch/path provenance and the selected objective when compressing this observer. This is a derived one-dimensional readout, not a full native-X6 theorem or a performance claim.