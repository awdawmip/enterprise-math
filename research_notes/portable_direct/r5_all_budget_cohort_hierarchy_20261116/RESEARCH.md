# R5 — Exact 101-budget interaction-order hierarchy for the eight closure residues

Date: 2026-11-16. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Status: **AUTHOR_PROVED / EXACT_INTEGER_FINITE_RECOMPUTABLE / NOT_REVIEWED**.
This is independent author-side portable research on the derived radius-two 954-event indexed-center observer, not a native six-axis or BRC transfer claim.

## Question and input

The established all-closed path DAG has 4,383 unconditional and 16 conditional predecessor arcs, two for each of the eight effective closure bits
`U=(3,8,9,10,15,17,25,27)`.
The prior theorem in `../r5_single_sweep_cohort_zeta_20261116/RESEARCH.md` establishes a common finite minimum path cost across all closure masks at `K>=214`. For every `K` in `214..314`, extend its single-sweep cohort counts to all 101 budgets, and determine the *highest order of genuine joint dependency* among closure switches.

## General theorem: complete monotonicity of the closure-count observer

Fix any finite weighted DAG with conditional edges labeled by subsets of a `q`-bit switch set. Assume the allowed mask `b` retains precisely the conditional edges whose entire required label is included in `b`, costs and boundary conditions do not change with `b`, and the minimum complete-path cost `D_b(K)` is constant over masks for the specified `K`. Let `A_T(K)` count minimum-cost full-graph paths with exact union of required labels `T`.

For `b_i in {0,1}`, the exact number of minimum-cost paths is the unique multilinear polynomial

`N_b(K) = sum_{T subseteq [q]} A_T(K) * product_{i in T} b_i`, with `A_T(K) >= 0`.

For any disjoint `S,b`, writing `Delta_S` for the product of forward on/off differences in the coordinates of `S`,

`Delta_S N_b(K) = sum_{T: S subseteq T subseteq (supp(b) union S)} A_T(K) >= 0`.

In particular the function is coordinatewise nondecreasing and all square-free mixed discrete differences are nonnegative. If all nonzero `A_T(K)` have `|T|<=d`, every mixed difference of order greater than `d` is identically zero.

**Proof.** A path in the mask-`b` graph exists if and only if its exact requirement union is contained in `supp(b)`. Under the common-cost hypothesis this is optimal precisely when it is a full-graph optimum. Partition those paths by their exact requirement union `T`; this proves the multilinear expansion and nonnegative coefficients. Applying each forward difference kills every monomial not containing its differenced coordinate and leaves the product on the remaining coordinates. Evaluate at `b` and sum surviving coefficients, which proves the difference formula and degree bound. The polynomial is unique by inversion on the Boolean lattice. No independence assumption between the eight switches is used.

## New exact finite conclusion on the frozen 954-event model

The original 15-coefficient frozen generator and 28 length-three gaps were rebuilt without changing the scientific input pin. A single exact integer shortest-path cohort sweep ran through budget 314. Every one of the **101 budgets x 256 switch masks = 25,856** exact integer counts was recovered by subset-zeta expansion; all 24 selected mask-specific independent DP checks across all 101 budgets agreed (2,424 cost/count pairs, zero mismatches).

Across all 101 budgets, exactly **25 distinct requirement masks** occur with a positive coefficient, and there are only **9 distinct nonzero-cohort support patterns**. The maximum cohort requirement size is **4**, attained only by mask `139 = binary 10001011`, i.e. simultaneous requirements from cuts `{3,8,10,27}`. It occurs exactly at budgets **214–219**. Thus for every budget 214..314, every fifth-order or higher mixed closure difference vanishes identically. Fourth-order effects are strictly positive on 214–219 and vanish elsewhere in this interval.

The exact interaction-degree staircase is:

| K | Maximum degree | Positive requirement masks |
|---|---:|---:|
| 214–219 | 4 | 20 |
| 220 | 3 | 18 |
| 221 | 2 | 10 |
| 222 | 1 | 2 |
| 223–290 | 2 | 4 |
| 291 | 1 | 3 |
| 292 | 0 | 1 |
| 293 | 1 | 3 |
| 294–313 | 2 | 4 |
| 314 | 1 | 3 |

This refines the previously known five support *windows*: budget regions can have the same active singleton cuts while exhibiting different interaction orders. For example, all five cuts `{3,8,9,10,27}` individually affect optimal counts at K=221, but no optimal path simultaneously requires more than two of those cuts.

## Exact execution and evidence

Reproducer: `VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py`. It imports **the actual preserved predecessor source** `../r5_single_sweep_cohort_zeta_20261116/R5_PATH_REQUIREMENT_DP_20261116.py`, rebuilds the frozen event sequence, verifies the 4,383+16 kernel decomposition, computes all 101 cohort vectors, expands each to 256 masks and checks 24 masks independently with the predecessor's own mask-specific DP. It asserts the nine support patterns, exactly 25 active monomial masks, exact degree staircase and three published reference counts.

Run from the repository checkout:

`python research_notes/portable_direct/r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py > exact_coefficients.json`

The actual local run returned `PASS_R5_101_BUDGET_INTERACTION_HIERARCHY`. Exact compact coefficient stdout is 32,555 bytes, SHA256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`. This stdout contains all 101 exact coefficient dictionaries, not merely aggregate statistics. `RESULTS_SUMMARY.json` records the reproducible constraints, spot-check masks, nine patterns, nonzero monomial union and digests. The full 256-value-per-budget expansion was also generated locally (1,549,048 bytes; SHA256 `0ab5b0f229785118d80a758c8f9dd330f47dec9d16e595dd4e8f30c7991e0615`), but independent mask-specific DP checks in this run cover the specified 24 masks; the full direct 256-mask rerun did not complete. All 25,856 counts from the zeta expansion are exact by the proved transform and reproduced from the published script.

**Provenance:** prior frozen-source and cohort proof `enterprise-math@9ff2c06f3e64b79dc12c80044f392a53fd649491`; same immutable `435e77af0d180eac32bd1f9c4c464bc4010b7551` scientific input. New author-side script is verified at its Git Blob in the same Draft PR. No independent mathematical review is claimed.

## Next discriminating problem

Explain the degree-four obstruction and its disappearance at K=220 without enumerating all optimal paths: find a localized separation/cutset argument for why a minimum-cost path cannot require five switches, and why the four-cut set `{3,8,10,27}` cannot remain jointly required after budget 219. Separately, return to the unresolved **max-new/min-old** optimal-center replacement distance for K=214..291, preserving its quantifier order; aggregate mask counts alone do not determine the pairwise center-set recourse metric.
