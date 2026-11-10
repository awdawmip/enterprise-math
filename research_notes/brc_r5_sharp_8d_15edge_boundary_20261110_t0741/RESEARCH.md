# R5: sharp eight-dimensional 15-to-14 edge support transition

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_DERIVATION / INDEPENDENT_EXACT_RATIONAL_LOCAL_CHECK / SCIENTIFIC_REVIEW_PENDING.
Frozen scientific inputs preserved from predecessor PR #1923: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.
Model and exact input: PR #1902 (original lawful rational `g=b` source and seedless-F matched-time target); PR #1913 (physical map and tangent rank); PR #1923 (the explicit 8D parameter map and ten full-carrier forced-edge dual certificates). This is an author-side scientific artifact, not a formal R5 CLAIM, Result, Review or mathematical admission.

## Theorem: the exact symmetric-cube threshold

Let the allowed carrier be
`D = {(0,0),(6,6)} union {(i,j): 0<=i<=6, j in {1,2,3,5}}`;
the likelihood ratios are
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`.
The Blackwell mass/moment matrix `C` has 21 rows and columns
`C_(i,j)=(e_i,e_j,r_i e_j)`.
Let `p_0` and the eight rational physical directions `P=(n_0,n_1,n_2,n_4,n_5,n_6,n_7,n_8)` be **exactly** those defined in PR #1923's `VERIFY_8D.py`; they are reproduced byte-for-byte at the beginning of the new `VERIFY_SHARP.py`. Let `p(t)=p_0+Pt`, `B_8=J_bP`, where `J_b` is the 21-coordinate marginal/moment Jacobian.

Define the exact rational constant
```
rho_* = 23/17050000 = 0.000001348973607038123... .
```

**(A)** For every real `0 <= rho < rho_*` and every real `t in [-rho,rho]^8`, `p(t)` satisfies all original physical capacity constraints, `g(X)=b(X)`, `g(Y)=1`, `z(Y)=a(Y)/10` and the two matched stopping-time equalities. It admits a strictly positive coupling on the fixed 15-edge support
```
SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),
    (1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6)).
```
Every allowed nonnegative Blackwell coupling of the same margins has at least 15 positive edges. Hence **every point in each of these eight-dimensional real cubes has minimum support exactly 15**. `rank(B_8)=8`, so the statistical marginal image is genuinely eight-dimensional.

**(B)** At `rho=rho_*`, the explicit corner
```
t_*=(0,0,0,-rho_*,+rho_*,0,0,-rho_*)
```
is still physically lawful and Blackwell feasible, but has **minimum support exactly 14**. The fixed basis `SB` realizes it with the weight of edge `(1,3)` exactly zero and the other 14 weights strictly positive. All 21 Blackwell equalities hold. Its additional zero physical slack has index 19 (zero-based, among 26; the pre-existing zeros 4,15,23 remain). Thus `rho_*` is the **sharp supremum** of symmetric `L_infinity` cube radii for which *every point of the closed cube* is lawful and requires precisely 15 edges. The threshold is relative to the **specified frozen physical basis P**, not a coordinate-free distance to the full 14-edge set.

## Exact proof and finite certificates

**Physical equality and existence.** The 5x14 equality Jacobian `J_c` has rank five and `J_c P=0`; the original center satisfies the equalities. Every capacity slack is affine in `t`; its three structurally zero components have zero derivatives. For every other slack with positive center value `s_i(0)`, compute the exact row-specific symmetric-cube positivity threshold `s_i(0)/sum_k |d s_i/d t_k|` (ignore zero-denominator rows). The **minimum** over those rows is precisely `23/17050000`, achieved at zero-based slack index 19. Consequently all slacks remain strictly positive except structural zeros when `||t||_infty<rho_*`.

The original 15-column `CB=C[:,SB]` has full column rank. Its exact affine coupling rule is `E_B(t)=E_B(0)+Delta_B t`, where `Delta_B` is computed by the 15 pivot rows `I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)`. Verify `CB E_B(0)=b_0` and `CB Delta_B=B_8` on **all 21 rows**. The minimum row-specific positivity radius `E_{B,e}(0)/sum_k|Delta_{B,e,k}|` is again `rho_*`, achieved by edge `(1,3)`, whose center weight is `23/4000000` and absolute derivative row sum is `341/80`.

**Ten unavoidable edges.** Reuse the ten exact full-30-carrier dual vectors of PR #1902/#1923, with forced set
```
F=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),
   (4,5),(5,5),(6,5),(6,6)).
```
For each `e in F`, the published dual vector `y_e` satisfies `y_e C_f <= 1_(e=f)` for **all 30 carrier edges**, so any nonnegative coupling must satisfy `E_e >= y_e b(t)`. The center minima of `beta_e=y_e b_0` and its eight-coordinate absolute derivative row-sum bound are respectively `18052765669/88328232000000` and `585227/46800`. They give a strictly positive lower bound at `rho_*`; thus the ten edges remain mandatory on the whole threshold cube.

**Exclusion of all <=14 support sets, uniformly in real t.** If a coupling had at most 14 positive edges, it would be contained in `S=F union T` for some four-element subset `T` of the remaining 20 edges. There are exactly `binom(20,4)=4845` such supports. Scale the moment rows of the selected 15 pivot rows `I` by 20, giving an **integer** coefficient matrix `A_S`. For each S, exact fraction row elimination constructs an annihilator `w_S` with `w_S A_S=0` and `c_S=w_S b_I(0) != 0`. Let `d_{S,k}=w_S (B_8)_I[:,k]` with the identical moment scaling. Then for every real t,
```
w_S b_I(t) = c_S + sum_{k=1}^8 d_{S,k} t_k .
```
The verifier enumerates all 4,845 cases (ranks: 3,669 of rank 14; 1,143 of rank 13; 33 of rank 12), selects among constructed independent annihilators the strongest available nonzero-center certificate for each case, and computes the exact threshold
```
min_S max_{enumerated nonzero-center w}
    |w b_I(0)| / sum_k |w (B_8)_I[:,k]| = 23/17050000.
```
An annihilator with zero derivative norm gives an infinite exclusion radius. Every S is excluded whenever `||t||_infty<rho_*`, proving the 15-edge lower bound. This replaces PR #1923's very conservative universal `15!*38^14` determinant bound with a complete **case-by-case rational annihilator** computation. It also independently reproduces the original 4,845 center exclusions rather than assuming them solely from a previous stdout file.

**Boundary and exact 14-edge minimum.** With `t_*` as above, all original constraints and the 21 Blackwell equalities hold, `E_B(t_*)_(1,3)=0`, and all other 14 basis weights are positive. Because the ten dual bounds remain strictly positive, any hypothetical support of <=13 edges must lie inside `F union U` for a three-element subset `U` of the remaining 20 edges. Exact fraction annihilator checks on all `binom(20,3)=1140` cases show that the **boundary right-hand-side vector is outside every such column span**, proving the 14-edge lower bound.

## Independent local computation and limits

A newly assembled local `Fraction`/SymPy reproducer was executed with all 4,845 cases in about 7 seconds, independently confirming the exact radius, the physical and 15-edge basis minima, the full 21-row boundary coupling, and the explicit 14-edge boundary. A separate exact local pass covered all 1,140 thirteen-edge candidates, with zero column-span matches; `INDEPENDENT_LOCAL_OUTPUT.txt` records those observed outputs.

`VERIFY_SHARP.py` is a self-contained source verifier assembled from the pinned predecessor's original physical formulas and dual dictionary plus the new finite exact scan; it has been published for byte-specific independent reruns. The local reproducer was not a byte-for-byte execution of this newly assembled published verifier, so no such execution claim is made. Mathematical independent review and formal task/Result admission remain open.

## Next concrete question

The threshold is attained by a simultaneous physical capacity and transport-support degeneration. Classify the adjacent low-support faces: find a rational half-space/chamber description for the local 14-edge region beyond the boundary, then determine whether the 14-edge locus has positive relative dimension and how its BRC observer-fiber residual direction acts on that stratification. Preserve the exact frozen `p_0,P,C` and the independent control/claim boundary.

## Publication/authority scope

An author-side GitHub branch and Draft PR preserve the research. Source materials may be reviewed independently; a branch and its contents confer no active R5 Owner/CLAIM and do not change P000, the task's immutable source pins, or an accepted mathematical Result.
