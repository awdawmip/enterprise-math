# R284Y — Exact partial-matching coefficient certificate and two-terminal Schur reduction for Port numerators

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASSED / NOT_REVIEWED**.
Scientific pin retained: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Author provenance: **EM-DIRECT-E6B1DD**, original registered SID **MCP-8487128c846440d1952bfc6fa44aeb86** (read-only recovery in this continuation). No Task CLAIM, Result, Review or native-X6 correspondence asserted.

## Exact sources and boundary

Immediate frozen-frontier predecessor: R284X, [aligned pencil completeness and Hall boundary](https://github.com/awdawmip/enterprise-math/blob/f143c6895fab26d716a31a9b1680996e8e9fb863/research_notes/portable_direct/R284X_ALIGNED_EDIT_PENCIL_COMPLETENESS_AND_HALL_BOUNDARY_20261119.md); R284W [common-kernel criterion](https://github.com/awdawmip/enterprise-math/blob/89e04fea7a68eab91c406b37934ae0662540c150/research_notes/portable_direct/R284W_COMMON_KERNEL_MATCHING_PRESENT_DEGREE_CERTIFICATE_20261119.md); R284V [Hall cofactor criterion](https://github.com/awdawmip/enterprise-math/blob/851060e73f9915e78e463f738c1c144962752c49/research_notes/portable_direct/R284V_OFFDIAGONAL_COFACTOR_HALL_CERTIFICATE_20261118.md); R284T [bordered determinant comparator](https://github.com/awdawmip/enterprise-math/blob/88183c11a6ad8e3c27e26e6a46fe54037e73e4c0/research_notes/portable_direct/R284T_JOINT_BORDERED_DETERMINANT_QUADRATIC_CERTIFICATE_20261118.md).

This note concerns only the **finite, auxiliary BRC Port matrix model over exact rationals**, with separately named matrix-unit edits. In Heartbeat World the underlying native object remains P000/X6, and the present algebra is an observer-specific auxiliary calculation; no native dynamics, time step or joint-residual erasure is inferred.

## Theorem Y1 — Complete coefficient/minor certificate (arbitrary named edit geometry)

Let `K` be any field, `A0 in K^{k x k}`, and `e_t=(i_t,j_t)` for `t=1,...,m`, with coordinates indexed from 0. Distinct **names** can even occupy the same matrix cell. Let
```
A(z) = A0 + sum_{t=1}^m z_t E_(i_t,j_t),   P(z)=det A(z).
```
For a subset `S` of names, put `I_S={i_t:t in S}`, `J_S={j_t:t in S}`. If any two selected names hit the same row **or** column, then `[prod_{t in S} z_t]P=0`. Otherwise list selected edges in ascending row order and write `pi_S` for the permutation that reorders their selected columns increasingly. Then
```
[prod_{t in S} z_t] P
 = (-1)^(sum_{t in S}(i_t+j_t)) * sign(pi_S)
   * det A0[[0..k-1]\I_S, [0..k-1]\J_S].
```
For `S=empty`, the right side is `det A0`; for a full matching of size `k`, the remaining `0 x 0` determinant is 1. In Port applications with updates `-z_t E`, multiply the displayed coefficient by `(-1)^|S|`.

**Consequences.** `det A(z)` is identically zero in the independent names **if and only if** all complementary fixed-base minors associated with the variable-edge partial matchings (including the empty matching) vanish. This is a finite exact decision procedure for unrestricted multirow/multicol edit families, including families for which Hall failure or fixed common kernels are absent. The names and joint edit geometry are retained; no quotient of Port identities is used.

**Proof.** In the determinant Leibniz expansion, choosing a named variable contributes one entry from its row and column; no permutation term can choose two entries from a common row or column. If the selected entries have pairwise distinct rows/columns, every contributing permutation restricts to the fixed selected row-column bijection and a permutation of the untouched rows/columns. Sorting the selected rows/columns and applying the generalized Laplace sign yields precisely `(-1)^{sum i+sum j}sign(pi_S)` times the untouched determinant. Each named variable has degree at most 1. The coefficients of all squarefree monomials are therefore exhausted by the formula, and a polynomial over a field is zero exactly when every coefficient vanishes. QED.

**Algorithmic cost and scope.** Enumerate partial matchings of the *named-edit bipartite multigraph*, then evaluate their complementary base minors, using exact Gaussian elimination/rank over `K`. For `q` such matchings the naive field-operation bound is `O(sum_S (k-|S|)^3)` with at most `2^m` subsets; determinant-zero may be tested by rank without evaluating the determinant. Ordinary sparse-support matching on the complementary **baseline** may prune zero minors before arithmetic, since a missing baseline perfect matching forces its determinant to vanish. This avoids the degree-2 tensor grids of R284S/T in families with small variable-matching number, while preserving exactness. It is not a general polynomial-time algorithm in `m`; rational bit-complexity depends on fraction-size growth.

## Theorem Y2 — Two-terminal Schur normal form for a Port cofactor coefficient

Let `W(x,z)>=0` be a rational `n x n` Port transition matrix with spectral radius below 1 (strict row-substochasticity suffices). Set `M=I-W` and `F_ab=(M^-1)_(a,b)=N_ab/det M`, with named target edit `x:E_(u,v)` in `W`. Assume `u != b`, `v != a`. Define
```
R = V \ {b,u},   C = V \ {a,v},
S = R intersect C,   P = R \ C,   Q = C \ R,
r = |P| = |Q| <= 2.
```
If `r>0`, order rows of `M[R,C]` as `(S,P)` and columns as `(S,Q)`; denote the sign of these row/column reorderings by `epsilon`. Write
```
G=I-W_SS,   T=W_PQ+W_PS * G^-1 * W_SQ .
```
Then, with the indicated ordering,
```
det M[R,C] = epsilon * det(G) * (-1)^r * det(T).
```
For `r=0` the same formula holds with `det(T)=1`; the determinant is `det G>0`. In particular, since `G` is invertible on the stable nonnegative Port domain, **vanishing of the target-edit numerator coefficient** `[x]N_ab` is equivalent to the rational identity `det T(z)=0` for `r=1,2` (or to the corresponding nonvanishing principal-minor statement if `r=0`). For `r=2`, this is exactly the two-terminal cross-product equation
```
T_11(z) T_22(z) = T_12(z) T_21(z).
```
All four entries have a nonnegative path-sum interpretation, with possible paths through `S`; source/destination labels remain named.

**Proof.** By a simultaneous permutation of the selected row and column orders, the submatrix `M[R,C]` becomes
```
[ G       -W_SQ ]
[ -W_PS   -W_PQ ].
```
The Schur complement of `G` is `-W_PQ-W_PS G^-1 W_SQ=-T`. The block determinant identity gives the formula; restore the permutation sign `epsilon`. As `W_SS` is nonnegative with spectral radius less than 1, `G^-1=sum_{j>=0}W_SS^j` exists with nonnegative entries. Cofactor expansion in the single target edge gives `[x]N_ab = s * det M[R,C]` for a fixed sign `s in {+1,-1}` determined by ordered deletion, so the zero criteria follow. All are rational identities on an open stable parameter box; clearing their nonzero denominators gives equivalent polynomial identities. QED.

**Interpretation.** The complementary `(n-2)x(n-2)` determinant is reduced to an `r x r` terminal transfer determinant with `r<=2`, after computing the `(n-2-r)` internal resolvent once for each required evaluation. This gives a small observer-facing certificate and identifies where the cancellation lives, without suppressing paths through the internal vertices. Theorem Y1 supplies a finite global identity test; four sampled values in the example below are **verification of that example only**, not a proof of a universal `z` identity.

## Proposition Y3 — Matching-present singular pencil with no fixed kernel (abstract rational boundary)

The following **abstract** `4x4` rational matrix is strictly entrywise positive:
```
B = [[1,2,3,1],
     [1,3,1,1],
     [1,3,1,1],
     [2,1,2,2]] .
```
Take `A(z,t)=B+z E_(0,0)+t E_(1,1)`. All four Y1 coefficients for `1,z,t,zt` are zero. Indeed, `det B=0`; the `z` and `t` cofactors vanish; and the `zt` coefficient is `det B[{2,3},{2,3}]=det[[1,1],[2,2]]=0`. Thus `det A(z,t) == 0` for all `z,t`. Its baseline support has every possible perfect matching (all entries positive).

The `3x3` subdeterminant on rows `(0,1,3)` and columns `(0,1,2)` is `-10`, so `rank B=3`. The unique left kernel is spanned by `p=(0,1,-1,0)`; the unique right kernel is spanned by `q=(1,0,0,-1)`. But `p^T E_(1,1) != 0` and `E_(0,0) q != 0`, so the pencil has **neither a common nonzero left kernel nor a common nonzero right kernel**. This proves the logical need for criteria beyond the union of Hall deficiency and fixed-kernel tests in general rational unit-edit pencils, with only two independent edits.

**Port-model boundary.** This strictly positive `B` is an abstract complementary pencil, *not claimed to be a submatrix of `I-W` with nonnegative stable `W`*. The analogous matching-present/no-fixed-kernel example inside that **additional Port-sign/stability constraint** remains open. It would be unsound to label this `B` an actual Port example.

## Exact reproducible checks

Program: `research_notes/portable_direct/R284Y_exact_port_matching_minor_checker.py`. Machine-readable output: `R284Y_exact_verification.json`. Python standard-library `fractions.Fraction` throughout (no floating-point arithmetic). The deterministic seed is `28419`.

- 720 generated pencils with `k=2,3,4`, `m=1,2,3` independently named matrix-unit edits (80 cases at each `k,m`); binary-cube Möbius inversion was compared with Y1's base-minor formula for all **3,360** exact coefficients; **767** nonmatching subsets explicitly gave zero. As each determinant is multiaffine, binary-cube interpolation is exhaustive for each generated pencil, while the finite random suite does not prove Y1.
- The abstract `B` witness was checked at its four coefficient minors, with a nonzero `3x3` minor `-10` and explicitly given unique nonconstant kernels.
- Four exact parameter pairs `(z,t) in {0,1/64}^2` in a **six-Port** nonnegative strictly substochastic witness checked the ordered `4x4` cofactor determinant, the `2x2` Schur transfer and the coefficient of target edit `x:5->3` in `N_24`. The other edits are `z:0->5` and `t:2->0`, with all baseline transitions listed in the executable. At `z=t=0`,
```
det M[R,C] = 752849/16172956800,
det T       = 752849/15970794840,
[x]N_24     = -752849/16172956800.
```
The four cases have positive `det(I-W)` and `det(G)`; each checks `det M[R,C]=det(G)det(T)`, `[x]N_24=-det M[R,C]`.

## Remaining focused science

1. Decide whether a **stable nonnegative Port** complementary pencil can have full baseline-support matching, identically vanishing edit coefficient, *no constant left/right kernel*, and genuinely independent named matrix-unit edits. Y3 settles the ambient rational case, not this restricted case.
2. Use Y1's minors and Y2's terminal transfer to find a structural, low-bit-cost certificate for the `r=2` cross-product identity that avoids exponential matching enumeration on sparse Port graphs. Compare actual arithmetic/bit complexity against R284T, including cached internal resolvents, baseline edge multiplicities, and exact fraction growth.
3. Preserve the original `F_ab` observer and the named paths in any further quotient; no X6/native attribution should be asserted until independently constructed.
