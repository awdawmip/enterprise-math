# R5 — Corrected martingale marginal dimension; full-dimensional 11- and 12-edge Blackwell chambers

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING.

## Frozen provenance and scope

Frozen scientific input pins are GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Exact predecessors: PR #1889, commit `b269751faa1996a1e1a6c8342817e1d00571d560` (26-edge carrier / rank 14); PR #1894, commit `b4d0594d3f9705dbe403b607741871ec9ff97842` (30-edge carrier / rank 15). Seven labels here are *statistical likelihood-ratio nodes*, not the six native P000 spatial axes. The method is nonnegative labelled branch mass plus an exact source-conditional moment observer. No heartbeat native dynamics or claim of physically lawful g=b flows is made for the new witnesses.

Let `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, `E_{ij}>=0`, `mu_i=sum_j E_{ij}`, `nu_j=sum_i E_{ij}`, and require
`H_j(E)=sum_i (r_i-r_j) E_{ij}=0` for each source column j. Normalize `sum E=1`. On `nu_4=0`, columns j=0 and j=6 have only their diagonal edge; source j=4 has none. Thus the full carrier consists of 30 edges, and with `mu_1=0` the reduced carrier has 26 edges.

## Theorem A — Correct affine marginal dimensions

The affine hull of normalized feasible `(mu,nu)` with `nu_4=0` has dimension **10**. With both `mu_1=0` and `nu_4=0`, it has dimension **9**.

Proof: After excluding `nu_4`, there are 13 marginal coordinates (`mu` seven, `nu` six). They satisfy the independent identities
`sum_i mu_i=sum_j nu_j` and `sum_i r_i mu_i=sum_j r_j nu_j`; normalization removes one more degree of freedom. Therefore dimensions are at most 10 and 9 respectively. The explicit full-column-rank 12- and 11-edge charts in Theorem B attain these dimensions through the martingale equations with strictly positive weights, proving equality for the affine hull of the feasible sets.

In particular `rank(A_D)=15` and `rank(A_D')=14` from the previous notes are ranks of **augmented** (target row masses, source column masses, independently recorded source moments) maps. The admissible right side has the four additional equalities `moment_j=r_j nu_j`, j=1,2,3,5. Those four coordinates are NOT independent statistical margins. Their omission explains the earlier ambient dimension overcounts (14 instead of 10, and 13 instead of 9 after normalization).

## Theorem B — Explicit full-dimensional 12-edge and 11-edge chambers

**Full `nu_4=0` face.** Define `S12={(0,0),(1,1),(2,2),(3,3),(6,6)} union {(i,5): 0<=i<=6}`. Set `E_(6,5)=39/83` and every other listed edge `E=4/83`, all other entries zero. Then all 21 augmented equalities hold and all six source masses and all seven target masses not structurally forbidden are strictly positive. The exact marginals are

`mu=(8,8,8,8,4,4,43)/83`,
`nu=(4,4,4,4,0,63,4)/83`.

**Double-zero `mu_1=nu_4=0` face.** Define `S11={(0,0),(2,2),(3,3),(5,5),(6,6)} union {(i,1): i in {0,2,3,4,5,6}}`. Set `E_(0,1)=39/79` and every other listed edge `E=4/79`, all other entries zero. Then

`mu=(43,0,8,8,4,8,8)/79`,
`nu=(4,59,4,4,0,4,4)/79`.

Every weight on the respective carrier is strictly positive. The moment equalities can be read directly: in S12, source column 5 balances `(r_6-r_5)*39/83 + sum_{i=0}^5 (r_i-r_5)*4/83=0`; in S11 source column 1 balances `(r_0-r_1)*39/79 + sum_{i=2}^6 (r_i-r_1)*4/79=0`. All other columns are diagonal.

For any support S, define `Psi_S(E)=(mu,nu)` and `H_S(E)` as the internal four source-moment *defects*. The stacked matrix `[Psi_S; H_S]` is row-equivalent to the predecessor's 21-row augmented Blackwell matrix `A_S`. Hence
`dim Psi_S(ker H_S) = rank(A_S)-rank(H_S)`.
In S12, the exact 12x12 minor with row indices
`(0,1,2,3,4,5,6,7,8,9,10,12)` is **+1**, and `rank(H_S12)=1`; the unnormalized marginal image has rank 11. In S11, the exact 11x11 minor on
`(0,2,3,4,5,6,7,8,9,10,12)` is **+1**, and `rank(H_S11)=1`; its marginal image has rank 10. Normalization yields dimensions **10** and **9**.

Because the above witnesses have every chosen edge strictly positive, the corresponding feasible positive parts of `ker H` are relatively open. The linear observation map is surjective onto the entire compatible marginal affine hull by the computed rank. Therefore the witnesses sit inside **nonempty relative-open sets of feasible marginal pairs with at most 12 edges and at most 11 edges**, respectively. Both sets have positive relative Lebesgue measure in their stated faces.

## Theorem C — Almost-everywhere lower bounds, and correction of earlier genericity claims

In the full normalized 10D face `nu_4=0`, almost every feasible marginal pair requires **at least 12** positive edges. Indeed points with `mu_4=0` belong to a proper hyperplane. If `mu_4>0`, at least one positive edge enters target row 4 from a non-4 source column, so its source-column moment-defect row is nonzero. For any support S realizing this pair, `rank(H_S)>=1`. When `|S|<=11`, the normalized image of `ker H_S` has dimension at most `|S|-rank(H_S)-1<=9`. There are finitely many supports, each with a measure-zero image in the 10D affine face.

Similarly in the normalized 9D double-zero face, almost every feasible marginal pair requires **at least 11** positive edges. On the relative interior `nu_1>0` and `mu_1=0` force positive non-diagonal edges in source column 1, hence `rank(H_S)>=1`. Supports with `|S|<=10` have normalized image dimension at most 8. Their finite union has relative measure zero.

Combining these lower bounds with Theorem B: on a relative-open positive-measure subset of the full face, the **exact** minimum is 12 (apart from a finite union of lower-dimensional exceptional charts); on such a subset of the double-zero face, it is 11. Thus the prior assertions that almost all feasible statistical marginals require exactly 15 edges (PR #1894) or exactly 14 edges (PR #1889) are **refuted**. The vertex upper bounds 15 and 14 respectively remain valid. The original finite-union argument used the 15/14-dimensional *augmented* image rather than the 11/10-dimensional martingale-compatible image; this correction changes the associated genericity conclusions but not the frozen physical task or previous explicit numerical couplings.

## Verification and continuation

`VERIFY.py` is a standalone standard-library `Fraction` checker for the two full-rank minor determinants, 21 exact Blackwell equations, strict positivity, all marginal identities, structural zeros and defect-row ranks. `EXACT_OUTPUT.txt` contains actual execution output. The exact algebraic rank argument, open mapping of finite-dimensional linear maps and finite-union measure proof establish the continuous statements.

Next: for the exact lawful `g=b` seedless-F physical witness in PR #1894, decide whether any 14-edge support is feasible, using an exact support/matroid certificate. Numerical sparse optimization alone is a candidate guide, not an exact 15-edge-necessity proof. Also map where the 11/12-edge chambers intersect the lower-dimensional legal physical affine family. Preserve the original Owner/CLAIM, independent review, mathematical admission and frozen inputs.

Research provenance: live native Researcher-ID `EM-DIRECT-0EC9F2`, Activity-ID `RA-8AA2E7FBB53A108D79AF32EE`, registration published to Source canonical main at `4adfe1e69506373b755b9f7a732b09a356201c2d`; formal R5 CLAIM remains subject to current control confirmation.
