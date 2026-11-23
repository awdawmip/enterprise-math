# EC49FYA — A 15-query Farey–CRT Boolean observer and exact 14-site certificate complexity

Date: 2026-11-23. Frozen science: `BRC16943`. Continuation of EC49FXZ, exact source commit `80243d814de151f7a7a6d6f883881054b30e9223`, Draft PR #3018. Original C11/P10 auxiliary observer, not a native X6 dynamical assertion.

**Status: AUTHOR_PROVED / EXACT_FINITE_CONSTRUCTIVE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.** This continuation has not issued a shared CLAIM, Result, independent Review or Foundation promotion.

## The precise experiment

Use the original 50 nonzero ten-bit support masks `U`, and the twelve mod-11 column factors `z∈{-1,0,…,10}` (the value `-1` denotes all columns present). Each genuine Farey anchor yields one of 600 normalized observation words; EC49FXU proves that all 600 occur, at its frozen scientific pin.

At physical site `(t,j)∈(Z/10)×(Z/11)`, the noiseless Boolean readout is

```
W_(U,z)(t,j) = ((U >> t) & 1) AND (z != j).
```

Every query costs one unit. Query locations may be chosen from previous answers, but the indexed reflection spectrum is not supplied free. Let `Q` be the least worst-case number of physical reads among deterministic exact-identification decision trees.

## Theorem 1: improved adaptive interval

**14 ≤ Q ≤ 15.**

*Lower bound:* retain the exact EC49FXZ analytic witness `U=833, z=-1`. The eleven deletion variants `(833,j)` force eleven positive queries in eleven distinct columns. Three strict supermasks `857, 867, 965` have disjoint extra-row sets `{3,4}`, `{1,5}`, `{2,7}`; their full-factor variants force three additional negative queries on different extra-row sets. These cannot overlap any of the eleven positive queries, hence at least fourteen sites on the full state’s path.

*New upper construction:* Precompute the 600 known states. Query **`(t,j)=(0,0)` first**. Thereafter, for each non-singleton remaining candidate set, choose a site minimizing the larger of the two answer-class cardinalities. Break ties by ascending row `t`, then column `j`. Stop at a singleton.

The companion exact finite verifier reconstructs the original `P10` atlas from 72 primitive direction representatives, checks 50 distinct masks and 600 distinct words, generates the complete decision tree, and follows all 600 traces. Its certified tree has 599 internal nodes, 600 leaves, initial split `no=193, yes=407`, and **maximum depth 15**. Leaf depths are:

| depth | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 2 | 28 | 94 | 137 | 68 | 50 | 50 | 54 | 67 | 50 |

The uniform-state average is exactly `6413/600 = 10.688333…` physical reads. The construction is an upper-bound witness, not a globally optimality claim.

## Theorem 2: exact state-dependent certificate complexity

A *state-dependent isolating certificate* for word `s` is a set of positions whose values on `s` distinguish it from **every other** one of the 600 states. Unlike a decision tree, its positions can be selected with foreknowledge of `s`. Define `C(s)` as the minimum certificate size.

```
max_{s among all 600 normalized states} C(s) = 14.
```

The earlier `W_(833,-1)` eleven-positive plus three-negative argument proves the lower bound of fourteen for that state. For the upper bound, the new verification program embeds actual certificates for all 50 full-factor words and all 50 column-zero-deletion words. Column translation maps each column-zero certificate to one for any deletion column, and the program directly verifies **all 600 translated certificates against all competing states**, using only integer tests. Every certificate has at most fourteen sites; at least one has exactly fourteen. No MILP solver is required to verify the stored witnesses.

For transparency, the sizes of the *provided* full-factor witnesses are `11:22,12:17,13:8,14:3` across 50 masks. For all 550 provided one-hole witnesses the counts are `4:44,5:462,6:44`. These size histograms describe the witnesses, not a separately certified minimum for each individual state.

The distinction is mathematically relevant: individual full-information certificates never require more than 14 observations, while the *globally usable adaptive tree* is currently constructed with 15 observations. A `Q=14` decision tree remains possible but unproved.

## New structural observation

EC49FXZ's locally most balanced root `(8,0)` split candidates `303/297` and led to depth 16 (uniform-state average 10.95). Using the deliberately **unbalanced** first query `(0,0)` gives `193/407` and yields depth 15, also improving the uniform average to `6413/600`. Candidate-count balancing at the first step therefore does not order the true residual conditional decision complexity; support-mask/column coupling matters. No distributional assumption enters the worst-case statement.

## Independent validation, inputs and continuation

- Exact, reproducible JavaScript: `research_notes/portable_direct/EC49FYA_DEPTH15_CERT14_VERIFY.js`. It embeds the 100 base certificates as compact physical-site indexes and checks every translated word.
- Exact output: `research_notes/portable_direct/EC49FYA_DEPTH15_CERT14_OUTPUT.json`.
- The same depth-15 algorithm was independently reconstructed and executed in local Python using integer 600-bit query masks; that run returned the same root split, depths, 599/600 tree counts and 600 correct paths. The source-linked JavaScript construction is the published verification path.
- Fixed scientific parents: EC49FXZ `80243d814de151f7a7a6d6f883881054b30e9223` and the previously established EC49FXU genuine-anchor surjection `5e33d4576bb0c1ef09e9169f8e17df469b8b7692`.
- The state population, full 110-position observer, column factor, P10 formula and frozen input are unchanged. The exact Q is now confined to `{14,15}`; independent review is pending.

**Next discriminating question:** Build a depth-14 observer or prove that none exists. Candidate-count balance alone is insufficient, so one useful route is exact finite branching with adversarial certificate lower bounds after each first answer (up to cyclic equivalence of mod-11 columns). A completed impossibility claim needs all admissible first-query branches and valid lower-bound certificates; partial search is not a negative theorem.

**Scope:** Normalized original auxiliary C11 Boolean observation only, unit-cost noiseless point reads, all 600 states equally admissible for the worst-case domain. No claim is made about obtaining anchor/height/provenance information, physical noise, non-Boolean observations or native X6 dynamics.
