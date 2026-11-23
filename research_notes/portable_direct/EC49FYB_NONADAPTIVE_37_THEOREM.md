# EC49FYB — Exact 37-site nonadaptive Farey–CRT Boolean observer

Date: 2026-11-23. Frozen scientific input: `BRC16943`. Direct continuation of EC49FYA, source commit `19a04cf3410c979ceb6502eae1fdbaba84ec5b68` (Draft PR #3020). Inherits the EC49FXU genuine-anchor 600-state surjection at `5e33d4576bb0c1ef09e9169f8e17df469b8b7692`.

**Research status:** AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. Auxiliary P10/C11 Farey–CRT observer, not native X6 dynamics or a claim about actual acquisition costs of an anchor.

## Exact observation problem

Let `U` range over the frozen 50 nonzero ten-bit support masks obtained from the original 72 primitive P10 direction representatives; let `z ∈ {-1,0,...,10}` be the 12 column factors, where `-1` means no missing column. There are 600 distinct normalized states. A site `(t,j)`, `0 ≤ t < 10`, `0 ≤ j < 11`, returns

```
W_(U,z)(t,j) = ((U >> t) & 1) AND (z != j).
```

Each physical Boolean site costs one unit. A *nonadaptive observer* chooses one fixed subset `E` of the 110 sites before seeing any answers, and must give distinct restricted binary words for all 600 states. Denote the minimum size by `N_nonadaptive`. The reflection spectrum and anchor identity are **not** supplied for free.

## Theorem: exact optimum

**N_nonadaptive = 37.**

### Lower bound: a column hitting invariant and two row residuals

For each column `j`, let `T_j = {t:(t,j) ∈ E}`. The full-factor state `(U,-1)` and its one-hole counterpart `(U,j)` differ only at that column, and there precisely on rows whose bit is present in `U`. Therefore `T_j` must intersect each of the 50 masks.

An exhaustive finite 10-bit check of the **frozen** atlas gives the following exact hitting facts (verified by independently enumerating all `2^10=1024` row subsets in the companion program):

1. There is no hitting subset with fewer than 3 rows; the **only** hitting triples, encoded as bitmasks, are `7, 13, 145, 259`.
2. A hitting subset that contains row 5 has at least 4 rows. The same holds for row 9.
3. A hitting subset containing **both** rows 5 and 9 has at least 5 rows.

Write `n_5` and `n_9` for the number of different physical columns where row 5 or row 9 is queried. The three facts imply for every column

```
|T_j| ≥ 3 + 1{5 ∈ T_j} + 1{9 ∈ T_j},
```

hence `|E| ≥ 33+n_5+n_9`.

Now masks `91` and `123` in the frozen atlas differ **only at row 5** (`91 XOR 123 = 32`); masks `101` and `613` differ **only at row 9** (`101 XOR 613 = 512`). For a fixed one-hole column `z=j`, each such pair of states differs only in the indicated row and in columns *other than* `j`. If a row is queried in at most one column, choose `j` equal to that column (or any column if the row is never queried): the pair has identical responses on all `E`, contradicting exact identification. Thus `n_5 ≥ 2`, `n_9 ≥ 2`, and

```
|E| ≥ 11·3 + 2 + 2 = 37.
```

This is an analytic reduction to two finite atlas facts and two explicit singleton-difference pairs. No MILP/solver optimality certificate is used for the lower-bound proof.

### Upper bound: explicit 37-site layout

In column order `j=0,...,10`, take these row subsets:

| j | T_j |
|---:|:---|
| 0 | 0,4,7 |
| 1 | 0,2,3 |
| 2 | 0,4,7 |
| 3 | 0,1,2 |
| 4 | 0,1,8 |
| 5 | 0,1,2 |
| 6 | 0,4,7 |
| 7 | 0,4,7 |
| 8 | 2,5,6,8 |
| 9 | 0,3,5,6,9 |
| 10 | 0,3,6,9 |

Column sizes are `3,3,3,3,3,3,3,3,4,5,4`, totalling **37**. The companion script reconstructs all 50 masks directly from the frozen P10 formula, constructs all 600 normalized words, and verifies that the 37-bit signatures are pairwise distinct by exhaustive exact-integer checking of `600 choose 2 = 179700` pairs. Thus this is a finite constructive upper-bound certificate; combined with the lower bound, equality holds.

## Cost comparison, assumptions and significance

EC49FYA proves `14 ≤ Q_adaptive ≤ 15` for the same 600-state, noiseless, unit-cost Boolean-only experiment with adaptive query choice. Therefore **adaptivity saves at least `37-15=22` physical reads in the worst case**, and the nonadaptive/adaptive optimal-cost ratio is at least `37/15` (about 2.47). This is a strict comparison under the *same* raw observation interface without free reflection spectrum.

The hitting-set count captures a structural residual that the mere support count does not retain: same-support full-vs-hole comparisons constrain every physical column; singleton mask differences force repeated coverage of rows 5 and 9 in distinct columns. A globally optimized nonadaptive choice achieves all constraints simultaneously.

Discovery of the 37-site layout used a finite 0–1 hitting-set search; the published mathematical verification **does not depend** on trusting the solver. It verifies the displayed layout exhaustively, and separately proves its optimality by the preceding lower bound. An independently reconstructed Python check also verified all 600 signatures.

**Verification files:** `EC49FYB_NONADAPTIVE_37_VERIFY.js` (Node.js, no packages), `EC49FYB_NONADAPTIVE_37_OUTPUT.json` (reproducible exact output). No floating-point operations are involved in the mathematical checks.

**Open frontier:** determine whether the optimal unrestricted adaptive decision-tree depth `Q` is 14 or 15. Useful next experiment: exploit the 37-site nonadaptive layout and the row-5/9 forcing pairs to construct adversarial depth-14 branch constraints or a depth-14 tree. The nonadaptive theorem itself does not settle that minimax question.

**Scope:** Original normalized auxiliary C11/P10 Boolean readout for the frozen 600-state image. All states are legitimate realized anchors only by the cited EC49FXU source. No transfer is claimed to native X6 evolution, noise, weighted read costs, or hidden anchor-height acquisition. No formal CLAIM, Result, independent Review or Foundation promotion is claimed by this science note.
