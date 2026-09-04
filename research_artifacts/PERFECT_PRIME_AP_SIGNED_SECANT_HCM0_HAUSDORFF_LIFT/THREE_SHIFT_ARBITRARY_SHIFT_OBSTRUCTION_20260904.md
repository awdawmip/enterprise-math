# Perfect Prime AP HCM0 — three-shift arbitrary-shift obstruction

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL CHECKPOINT — HCM0 AND PARENT NONVANISHING REMAIN OPEN**

## 1. What is refuted

Let `L(c)` denote the pure Cauchy-shift signed bipartite Laplacian from the preceding checkpoint,

\[
C(c)_{ij}=\frac1{i+1+mj+c},\qquad
L(c)=\begin{bmatrix}I\\-P_c^T\end{bmatrix}A_c\begin{bmatrix}I&-P_c\end{bmatrix}.
\]

The preceding all-`m` theorem proves that every mixed tree-cofactor coefficient supported on exactly two distinct shifts has sign `(-1)^n`, `n=m-1`. A natural attempted continuation was:

> **Auxiliary arbitrary-shift conjecture.** For arbitrary nonnegative shifts `c_1,...,c_r`, every nonzero polarized mixed coefficient of `det'(sum z_s L(c_s))` has sign `(-1)^n`.

This conjecture is false.

Take

\[
m=7,\qquad n=6,\qquad D=13,
\]

three shifts

\[
(c_0,c_1,c_2)=(0,2,5),
\]

and multiplicities

\[
\alpha=(1,5,7).
\]

Then the exact coefficient

\[
[z_0z_1^5z_2^7]\,\det'\bigl(z_0L(0)+z_1L(2)+z_2L(5)\bigr)
\]

is

\[
\boxed{
-\frac{9124563710159060296133331257733323921803}
{214894420165177617520129597749664857553591871024974545851844728742741899728650240000}
}<0.
}
\]

Since `n=6`, the proposed uniform sign `(-1)^n` is positive. Thus the arbitrary-nonnegative-shift all-support extension of the two-shift theorem is **exactly refuted**.

This is **not** an HCM0 counterexample and is **not** a zero or sign obstruction for the actual Perfect-Prime polynomial.

## 2. Two independent exact certifications

The paired exact script

`research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/three_shift_arbitrary_shift_obstruction_check_20260904.py`

uses only `fractions.Fraction` and certifies the same rational number by two independent coefficient extractions.

### 2.1 Multivariate finite-difference extraction

For the homogeneous degree-`D` polynomial

\[
p(z)=\det'\left(\sum_sz_sL(c_s)\right),
\]

coefficient extraction is performed exactly by

\[
[z^\alpha]p
=\frac1{\prod_s\alpha_s!}
\sum_{0\le k_s\le\alpha_s}
(-1)^{\sum_s(\alpha_s-k_s)}
\left(\prod_s\binom{\alpha_s}{k_s}\right)
p(k_0,\ldots,k_r).
\]

### 2.2 Jacobi derivative + exact univariate interpolation

Independently put

\[
q(t)=\left.\frac{\partial}{\partial z}
\det'\bigl(zL(0)+tL(2)+L(5)\bigr)\right|_{z=0}.
\]

For nonsingular

\[
A(t)=tL(2)+L(5),
\]

Jacobi's identity gives

\[
q(t)=\det A(t)\,\operatorname{tr}\bigl(A(t)^{-1}L(0)\bigr).
\]

The script evaluates this exactly at 13 rational points, Lagrange-interpolates the degree-at-most-12 polynomial `q(t)`, and recovers its `t^5` coefficient. It is exactly the same negative rational displayed above.

Hence the obstruction is not an artifact of one coefficient-extraction implementation.

## 3. The actual Perfect-Prime spacing survives the same cell

The actual layers are not arbitrary shifts. They are

\[
c_s=bs,\qquad b=m^2.
\]

For `m=7`, `b=49`. Repeating the *same* multiplicity cell `alpha=(1,5,7)` at the consecutive actual shifts

\[
(0,49,98)
\]

gives the exact positive coefficient

\[
\boxed{
\frac{2020508893605078901068867942380512448517816669066168908718740610593813}
{1705478180555715554493070132258456452246159299927111039765299907113833208874517899074841695344312605748184696287356534903432480176558433107968000000}
>0.
}
\]

Thus the counterexample kills an over-strong auxiliary theorem but leaves the actual `m^2`-spaced target alive.

An exact finite AP-spacing scan for the same `m=7`, `alpha=(1,5,7)`, shifts `(0,B,2B)` gives:

- negative at `B=1,2,5,10`;
- positive at `B=20,30,40,49`.

This scan is discovery evidence only; it is not promoted to a threshold theorem.

## 4. Why `b=m^2` is structurally special

For every atom denominator before the layer shift,

\[
A_{ij}=i+1+mj,\qquad 0\le i,j\le m-1,
\]

one has the exact range

\[
1\le A_{ij}\le m^2=b.
\]

Therefore the actual layer-`s` denominators lie in the disjoint integer block

\[
bs+A_{ij}\in[bs+1,(s+1)b],
\]

while layer `s+1` starts at `(s+1)b+1`.

Hence consecutive actual Cauchy layers occupy strictly ordered, nonoverlapping denominator blocks. The false arbitrary-shift conjecture discards precisely this spacing information.

Freeze the new research boundary:

\[
\boxed{
\text{ARBITRARY SHIFT SIGN REGULARITY IS FALSE; ACTUAL }m^2\text{-BLOCK-SEPARATED SIGN REGULARITY REMAINS OPEN.}
}
\]

## 5. Sharper three-shift reduction

Fix a base shift `e` occurring with multiplicity `m`. In coordinates adapted to `ker L(e)`, the remaining `n=m-1` degrees are governed by the quotient forms

\[
Q_{e,d}=(P_e-P_d)^TA_d(P_e-P_d)
\quad\text{on }\mathbb P_n/\mathbf1.
\]

For two further shifts `d,f`, the `m+r+(n-r)` three-shift cells reduce, up to the already controlled nonzero scalar `det A_e` and a positive square coordinate factor, to the coefficients of

\[
\det\bigl(uQ_{e,d}+vQ_{e,f}\bigr).
\]

Thus a sufficient next theorem is:

> for the actual block-separated shifts, prove that the generalized eigenvalues of the pencil `(Q_{e,d},Q_{e,f})` are positive real numbers (with the already known determinant sign normalization).

Then every coefficient of the quotient determinant has the required common sign, giving the whole three-shift slice with one multiplicity `m` at once.

Finite numerical discovery (not a proof) shows this positive-real generalized-eigenvalue pattern for consecutive actual blocks in the tested range, while the false small-shift triple `(0,2,5)` at `m=7` develops negative/complex generalized eigenvalues. This matches the exact coefficient obstruction and makes the block-separated pencil the next load-bearing object.

## 6. Scope boundary

This checkpoint proves only:

1. the explicit exact `m=7` arbitrary-shift three-support counterexample;
2. its independent exact re-verification;
3. positivity of the same cell at actual spacing `(0,49,98)`;
4. the exact disjoint-block property of the actual shifts.

It does **not** prove all-support actual-layer sign regularity, HCM0, full shifted HCM for all `m`, or parent determinant nonvanishing. No Result-ID is frozen.

Recommended scheduler state: `ACTIVE / CONTINUE`, with next target `M2_BLOCK_SEPARATED_THREE_SHIFT_PENCIL_POSITIVE_SPECTRUM`.
