# R282 — Finite rational grids certify full Port-response equivalence

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED**.
Source: R281 at `a957ac339577bf794b46d25221f9e38a43c2128d`, which continues R280. Preserve frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scope: finite stable nonnegative-rational **named BRC Port** matrices, with `m` named additive single-edge update types and declared output pairs, all future additions constrained to keep the matrix stable. This result does not conflate the Port model with P000 X6-native history or the R269 auxiliary observation quotient.

## 1. An exact 3^m-grid observer-equivalence theorem

For each model `j=1,2`, let `W_j` be a finite strictly sub-stochastic nonnegative-rational matrix, and fix the same `m` named update coordinates `x=(x_1,...,x_m)`; their underlying Port endpoints may be model-specific but are part of the declared interface. For each matched declared readout `(a,b)`, write `F_ab^j(x)=[I-W_j-\sum_i x_i E_i^j]^{-1}_{a,b}`. Compare outputs by their declared matching, even if the matrices have different internal dimensions.

**Lemma (multiaffine quotient).** Each readout admits `F_ab^j(x)=N_ab^j(x)/D^j(x)`, with both numerator and denominator multiaffine rational polynomials and `D^j(0)=1`. In particular, for two models, the cross-product
`P_ab(x)=N_ab^1(x)D^2(x)-N_ab^2(x)D^1(x)`
has degree at most **2 in every individual x_i**.

**Theorem R282-A.** For each named edit coordinate choose **three distinct rational weights** `t_(i,0), t_(i,1), t_(i,2)` such that every point in their Cartesian product is admissible/stable for both models. The two models have identical complete rational response functions for all declared outputs and every admissible future edge-addition vector if and only if their readouts agree at all **3^m** grid points. Thus `3^m` exact point evaluations provide a finite, complete **full-horizon observer equivalence certificate** for this specified edit/output language.

A sufficiently small rational grid `{0,eps,2eps}^m` always exists because the two baseline systems have strictly positive row-sum margins and finitely many edit coordinates. Such a certificate can be applied without symbolic reconstruction of all numerator/denominator coefficients, albeit with exponential evaluation count.

**Proof.** The matrix determinant is separately affine in each rank-one edit parameter `x_i` (multilinearity in rows/columns, or the matrix determinant lemma with the other edits fixed). Every adjugate cofactor is separately affine for the same reason: deleting a row and a column restricts a rank-one update to a rank-one or zero update. After normalization by nonzero `det(I-W_j)`, this yields the stated multiaffine numerator and denominator. On a stable input, denominators cannot vanish. Equality of responses at every grid point therefore gives `P_ab=0` on the grid. Fix all but one coordinate: a polynomial of degree <=2 with three distinct roots vanishes identically; repeat for each coordinate (tensor-product polynomial interpolation) to prove `P_ab\equiv0` over the rationals. This establishes rational-function equality on all common admissible update vectors. The converse follows by evaluation. Repeating for the finite declared output family proves the theorem. QED.

The test includes intermediate observations after any prefix of nonnegative edit additions because every such prefix is another admissible update vector. No assertion is made for operation languages involving deletion, path-specific state changes, nonlinear Port rewrites or extra observers.

## 2. Modular finite-resolution extension

Write `Z_(p)` for rationals with denominator prime to `p`.

**Theorem R282-B.** Let `p>=3` be prime and `k>=1`. Suppose the two quotient presentations have `N,D,N',D'` with coefficients in `Z_(p)`. In each coordinate choose three admissible sampling points in `Z_(p)` whose pairwise differences are p-adic units. Assume the denominators of both models are p-adic units at every sampling point. If every declared output agrees modulo `p^k` on the **3^m** grid points, then all coefficients of the cross-product `P=N D'-N'D` are divisible by `p^k`. Consequently, the two responses agree modulo `p^k` for **every** p-integral edit vector at which both denominators are p-adic units and both physical updates are admissible.

**Proof.** Grid observations with unit denominators give `P(t)\equiv0\mod p^k`. Evaluation on polynomials of coordinate degree <=2 is the tensor product of the 3-by-3 Vandermonde maps `(1,t,t^2)`. Each determinant is a product of three pairwise sampling differences, all p-adic units. Hence the tensor-product evaluation map is invertible over `Z_(p)/p^k`, so every coefficient of `P` is zero modulo `p^k`. At any other p-integral point, evaluating the coefficientwise congruence gives `P(x)\equiv0`; invert unit denominators to conclude. QED.

**Domain precision.** This finite-resolution result uses coefficients integral at p and *unit* denominators at the relevant points. Near the resonant denominator strata of R270–R277, the corresponding valuations and additional digits must be retained; the theorem does not extrapolate a unit-denominator congruence through those strata. For `p=2`, three pairwise distinct residues are impossible, and a separate finite-ring certificate is required.

## 3. Two sampling values do not suffice even for one edit

Use Ports 0,1,2, observer (0,0), sole edit `1->2` of weight `x`, and baseline edges `0->1=a,\ 2->0=b,\ 2->1=gamma`. Then
`F(x)=(1-gamma*x)/(1-(gamma+a*b)*x)`.

Two strictly stable, nonnegative-rational systems are:
- `(a,b,gamma)=(1/4,1/4,0)` giving `F_1(x)=1/(1-x/16)`;
- `(a,b,gamma)=(1/4,15/64,1/4)` giving `F_2(x)=(1-x/4)/(1-79x/256)`.

They agree at `x=0` (value 1) and `x=1/4` (value 64/63), but at `x=1/2`:
```
F_1(1/2)=32/31,    F_2(1/2)=448/433.
```
Their numerator cross-product difference is exactly
```
D_2(x)-N_2(x)D_1(x)=x(1-4x)/256.
```
Thus a two-point test is insufficient for complete rational-function equality even when the two baseline outputs and a nonzero future readout coincide. The same counterexample remains distinguishable modulo 13 at `x=1/2` under unit denominators.

## 4. Typed observer scope and reproduction

The same finite-grid theorem applies simultaneously to any finite declared list of matched output Port pairs. A four-Port example with baseline `0->1=1/4,\ 2->0=1/4`, edits `A:1->2,\ B:3->3`, and two models differing only in their baseline `3->3` weight (0 versus 1/4) shows: the full nine-point `{0,1/16,1/8}^2` grid certifies equality at readout (0,0), but (3,3) distinguishes the states. Declared readout scope is part of the equivalence certificate.

Independent `R282_finite_grid_checker.py` validates both rational models at three sample points, the nine-point scoped two-edit grid, the mod-13 distinction, and exhausts all 2,197 quadratic polynomials over F_13 to establish that the `0,9,5` evaluation map has only the zero polynomial in its kernel. `R282_verification.json` is the exact saved finite output. The universal proofs are the determinant and interpolation arguments above; the computer check is limited to these examples.

**Next research.** Develop a stratified finite-grid certificate at resonant points with `v_p(D)>0`, including the minimum digits for normalized Port readouts. Investigate whether a small grid can be reduced for specific nonnegative Port transfer graphs, and under which extra source/Port provenance carriers such a reduction remains safe. Continue preserving the distinction between exact rational observation quotient and underlying P000 state.

GitHub persistence of this independent study does not create formal TASK/CLAIM/Result/review authority or independent scientific acceptance.