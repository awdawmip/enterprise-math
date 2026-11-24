# R5 — Uniform cut-27 factor and sign-changing closure coupling

Date: 2026-11-17 (Asia/Shanghai). Scientific input pinned to `435e77af0d180eac32bd1f9c4c464bc4010b7551` (unchanged). Claim status: **AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED**. The object is the derived 954-event, radius-two indexed-center observer, **not** a native X6 or BRC dynamical transfer.

## Input and question

Use the previously verified eight effective closure cuts `U=(3,8,9,10,15,17,25,27)`. At budget `K=214..314` the optimal cost is invariant across the 256 closure masks; the prior exact shortest-path cohort recurrence establishes

\[
N_b(K)=\sum_{T\subseteq b} A_T(K),\qquad A_T(K)\in\mathbb Z_{\ge0}.
\]

Here bits of `b` identify enabled cuts, and `A_T(K)` counts optimum paths whose exact required-cut union is `T`. The frozen generator and original cohort reproducer are at `r5_single_sweep_cohort_zeta_20261116/R5_PATH_REQUIREMENT_DP_20261116.py` and `r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py` under `research_notes/portable_direct` in this branch.

We ask whether the closure-cut dependence merely has low interaction *degree*, or actually factors into independent contributions, and whether the sign of multiplicative interaction can change while all additive mixed differences stay positive.

## Theorem 1: exact cut-27 multiplicative factor on nine consecutive budgets

For every integer `K` in `214..222`, every mask `s` using any subset of cuts other than cut 27, and `s` not containing its bit `128`, the count identity is

\[
\boxed{9 N_{s\cup\{27\}}(K)=13 N_s(K).}
\]

Equivalently, with the cut-27 on/off indicator `z`, the entire eight-variable multilinear counting polynomial factors as

\[
P_K(x_0,\ldots,x_7)=\bigl(1+\tfrac49 x_7\bigr)Q_K(x_0,\ldots,x_6),\quad 214\le K\le222.
\]

**Exact finite proof.** Let `h=128`. The independently regenerated frozen integer recurrence returns a complete coefficient dictionary for each of the nine budgets. For each `T` not containing `h`, it satisfies `9 A_{T|h}(K)=4 A_T(K)`, including the case where both entries vanish. All 75 positive coefficient pairs were checked; the full support on each side is also verified identical. Partition the optimal paths by exact requirement and apply the preceding Zeta relation:

\[
N_{s|h}=\sum_{T\subseteq s}(A_T+A_{T|h})
=\sum_{T\subseteq s}(1+\tfrac49)A_T=\tfrac{13}{9}N_s.
\]

This establishes 9×128=**1,152 exact count equalities**, uniformly over all other switch assignments. In the all-closed optimum-path population, the count share with cut 27 required is exactly **4/13** throughout these nine budgets (the 9:4 split is invariant under filtering by all other closure-mask permissions).

This is an exact factorization of the *count observer*. A local edge-gadget bijection explaining `9:4` without the finite coefficient calculation remains an open structural problem.

## Theorem 2: two-cutter multiplicative coupling changes sign

For a region with only two relevant closure bits `i,j`, write the four exact requirement coefficients as

\[
A=A_\varnothing>0,\quad B=A_{\{i\}},\quad C=A_{\{j\}},\quad D=A_{\{i,j\}}>0.
\]

The four observed counts are `N00=A`, `N10=A+B`, `N01=A+C`, `N11=A+B+C+D`. Hence the multiplicative-dependence determinant is

\[
\boxed{\mathcal D=N_{00}N_{11}-N_{10}N_{01}=AD-BC.}
\]

`\mathcal D=0` holds **if and only if** the two-bit count table is multiplicatively separable. `\mathcal D>0` means positive log interaction; `\mathcal D<0` means negative log interaction. The additive mixed difference is always `N11-N10-N01+N00=D>0`, so its positivity does not fix the sign of `\mathcal D`.

The complete exact-integer recurrence yields the following sign chart (each listed integer budget, no gaps):

| Effective cuts | Budgets | Sign of `\mathcal D` |
|---|---|---|
| `{25,27}` | `223..256` | positive (34 cases) |
| `{25,27}` | `257..290` | negative (34 cases) |
| `{15,17}` | `294..298` | negative (5 cases) |
| `{15,17}` | `299..301` | positive (3 cases) |
| `{15,17}` | `302..313` | negative (12 cases) |

There are **no zero determinants** in either full-support two-cut window. These are genuine sign transitions at `256→257`, `298→299`, and `301→302`. Each of the 88 two-cut budgets retains a strictly positive additive mixed difference (`D>0`).

One small exact witness is `K=223` with common positive factor removed:

`(A,B,C,D)=(39254391766431,72411120,17446323929516,32182720)`;

`AD-BC=5243370299654400 > 0`.

At `K=294` for cuts `{15,17}`, the normalized quadruple is

`(81050014519,6052584544,6073419616,270855936)`;

`AD-BC=-14807008151670680320 < 0`.

The attached JSON provides the complete normalized integer witnesses at the transition budgets and the precise common factors removed. The complete sign classification checks every budget, not just samples. This is also an exact counterexample to the implication “positive Boolean mixed differences imply positive multiplicative association” within this particular count model.

## Execution, verification and limits

The verifier `VERIFY_R5_FACTOR_AND_COUPLING.py` regenerates the complete 101-budget exact coefficients by invoking the prior source verifier, unless supplied the already preserved coefficient output with `--coefficients`. It checks the frozen pin, all 75 coefficient pair identities, both full-support pair regions, determinant signs for every budget, and the exact breakpoints. Standard-library Python integer arithmetic only. No sampling or floating-point decision is used.

Run from the checkout:

`python research_notes/portable_direct/r5_factorization_and_coupling_20261117/VERIFY_R5_FACTOR_AND_COUPLING.py > result.json`

Local independent post-processing of the previously verified 32,555-byte predecessor output (`SHA256 a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`) returned `PASS_R5_101_BUDGET_FACTOR_AND_COUPLING`. A separate check against the previously generated full 256-count-per-budget JSON confirmed all 1,152 count equalities; that file is an independent **Zeta reconstruction**, not a full 256-mask direct DP rerun. The preceding 101-budget source computation itself contains 24 independently mask-specific DP checks (2,424 cost/count pairs). This turn directly verifies **coefficient postprocessing**, not a new independent full DP execution of all 256 masks.

## Next research frontier

1. Explain the constant `4/9` as a finite predecessor-graph gadget or weight-preserving path correspondence, ideally removing reliance on coefficient enumeration.
2. Explain the first `\mathcal D` sign crossing at `K=257` via a small determinant recurrence or localized path competition; classify the later double reversal at `K=299/302`.
3. Return to `max-new/min-old` optimal-center replacement distance on `K=214..291` using actual center sets rather than aggregate count observers, retaining the stated order of the maximum and minimum.

Prior source is the same draft PR and frozen input, with the 2026-11-16 results at commit `cb5249695a7dce70f102d0ae426423a18facd12a`. This result is independent author-side research, not a formal claimed Task Result or independent review.
