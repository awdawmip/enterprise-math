# RH fractional-node rough-BRC interpolation and canonical arm correction

Status: `RESEARCH FRONTIER / EXACT COEFFICIENT IDENTITY + CORRECTION OF PRIOR ABSOLUTE-MASS NO-GO / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Möbius / rough factor split / growing Heath-Brown depth / generalized divisor functions / Lagrange extrapolation / operation-safe absolute observer`

## 0. Correction to the same-day growing Heath-Brown note

This note corrects a load-bearing inference in

`RH_GROWING_HEATH_BROWN_BRC_CRITICAL_DEPTH_20260908.md`.

That note writes the integer j-th branch as

`zeta^(j-1) F_y^j`

and then treats `F_y^j` as a separate small-prime A-arm when taking an absolute Dirichlet mass. The algebraic factorization is exact, but it is **not operation-safe for the later absolute-value observer**, because the `zeta^(j-1)` factor contains the inverse small-prime Euler factors which cancel `j-1` copies of `F_y` before absolute values are taken.

The canonical Euler-reduced branch is instead

`B_(j,y)(s) = F_y(s) [zeta(s)F_y(s)]^(j-1)`.

Hence the earlier statement

`ABSOLUTE_SMALL-PRIME_BRANCH_CONTROL_IS_TRAPPED_AT_THE_P1_BOUNDARY sigma=1`

is withdrawn as an intrinsic branch obstruction. The computed mass of the artificial factor `F_y^j` was correct for that factor, but the inference from it to the exact branch after changing the observer to absolute value was not T6-safe.

The genuine difficulty remains signed critical cancellation, but it is not caused by a j-fold small-prime absolute mass.

---

## 1. Canonical small/rough factorization

Let

`F_y(s)=prod_(p<=y)(1-p^-s)`

and

`R_y(s)=zeta(s)F_y(s)`.

In the half-plane of absolute convergence,

`R_y(s)=prod_(p>y)(1-p^-s)^(-1)`

and its Dirichlet coefficient is exactly `1` on y-rough integers (including 1) and `0` otherwise.

Thus the j-th integer Heath-Brown branch is

`B_(j,y)=F_y R_y^(j-1)`.

Every integer n has a unique prime-cut factorization

`n=a b`,

where every prime divisor of a is `<=y` and every prime divisor of b is `>y`.

The coefficient of `F_y` at a is `mu(a)` (and is zero if the small-prime part is not squarefree), while the coefficient of `R_y^(j-1)` at b is the nonnegative restricted divisor coefficient `d_(j-1)(b)`.

Therefore exactly

`B_(j,y)(n)=mu(a) d_(j-1)(b)`.

The sign of every branch is carried by the **same single small-prime Möbius provenance arm**, independent of j. The rough arm is positive.

Freeze corrected typing:

`COMMON_SMALL_PRIME_MOBIUS_ARM + POSITIVE_ROUGH_MULTIPLICITY_ARM`.

For the absolute Dirichlet observer the small-prime mass is therefore

`prod_(p<=y)(1+p^-sigma)`,

not its j-th power.

At `y=(log X)^2` and `sigma=1/2`, prime summation gives

`log prod_(p<=y)(1+p^-1/2)=O(log X/loglog X)=o(log X)`,

so this common small-prime absolute mass is `X^o(1)`.

This does **not** prove branchwise RH bounds: for integer `j~K` the positive rough multiplicity `R_y^(j-1)` can itself be large. The location of the absolute-growth obstruction has changed from small-prime repetition to rough multiplicity.

---

## 2. Arbitrary-node coefficient-exact interpolation theorem

The integer exponents `0,1,...,K-1` are not forced.

Let `alpha_0,...,alpha_(K-1)` be any K distinct complex numbers. Let

`ell_j(alpha)`

be the Lagrange basis for these nodes, and set

`c_j=ell_j(-1)`.

Define the generalized branch

`B_(alpha,y)(s)=F_y(s) R_y(s)^alpha`.

All powers are understood coefficientwise in the Dirichlet-convolution algebra, equivalently through generalized divisor coefficients.

### Theorem (fractional-node rough interpolation)

For every integer `n<=y^K`, exactly

`mu(n)=sum_(j=0)^(K-1) c_j B_(alpha_j,y)(n)`.

Equivalently, coefficientwise through support `<=y^K`,

`zeta^-1 == sum_j c_j F_y (zeta F_y)^(alpha_j)`.

No equality of the full analytically continued Dirichlet functions is claimed.

### Proof 1: formal H-adic proof

Set

`T=R_y=zeta F_y`, `H=1-T`.

H has zero constant coefficient and is supported on integers `>y`. Hence `H^K` is supported on integers `>y^K`.

For every m<K, `binom(alpha,m)` is a polynomial of degree m, so Lagrange exactness gives

`sum_j c_j binom(alpha_j,m)=binom(-1,m)=(-1)^m`.

Expand

`T^alpha=(1-H)^alpha=sum_(m>=0)(-1)^m binom(alpha,m)H^m`.

Therefore the coefficients of `H^m`, `m<K`, in `sum_j c_j T^(alpha_j)` are all 1, exactly as in

`T^-1=(1-H)^-1=sum_(m>=0)H^m`.

The difference is supported in `H^K`, hence above `y^K`. Multiplication by `F_y` cannot decrease integer support. Since `F_y T^-1=zeta^-1`, the claim follows.

### Proof 2: direct Factor-BRC / Cell proof

For the unique split `n=a b` above, the branch coefficient is

`B_(alpha,y)(n)=mu(a)d_alpha(b)`.

For `p^e || b`,

`d_alpha(p^e)=binom(alpha+e-1,e)`,

a polynomial of degree e. Hence `d_alpha(b)` is a polynomial in alpha of degree `Omega(b)`.

Every prime divisor of b exceeds y, so

`b>y^(Omega(b))`.

If `n<=y^K`, then `Omega(b)<K`. Therefore `alpha -> d_alpha(b)` has degree `<K`, and Lagrange interpolation gives

`sum_j c_j d_(alpha_j)(b)=d_(-1)(b)=mu(b)`.

Because the small and rough prime supports are disjoint,

`mu(a)mu(b)=mu(n)`

(with both sides zero when the small part is not squarefree). This proves the identity Cell by Cell.

Freeze interface:

`FRACTIONAL_NODE_ROUGH_BRC_INTERPOLATION`.

This is a provenance-preserving finite coefficient identity, not an RH proof.

---

## 3. Positive bounded branches on alpha in [0,1]

For real `0<=alpha<=1`, the generalized divisor coefficients satisfy

`0<=d_alpha(m)<=1`.

This is standard generalized-divisor/Newton-binomial structure and is also used explicitly in Robles 2026 (`arXiv:2608.07198`) for fractional zeta powers.

Therefore, for every integer n and every `alpha in [0,1]`,

`B_(alpha,y)(n)=mu(a)d_alpha(b)`

satisfies

`|B_(alpha,y)(n)|<=1`.

Thus the Möbius coefficient below `y^K` can be reconstructed from K branches that simultaneously have:

1. a common exact small-prime signed provenance arm `mu(a)`;
2. a positive rough arm;
3. pointwise coefficient magnitude at most 1.

This is strictly cleaner than the integer-node basis at large j, where the rough coefficient is `d_(j-1)(b)` and can grow rapidly.

The outer interpolation remains signed. Positivity of the individual rough branches does not imply parity cancellation of their extrapolation.

---

## 4. Interpolation conditioning is exponential in K but subpolynomial at RH depth

Take the explicit equispaced nodes

`alpha_j=j/(K-1)`, `j=0,...,K-1`.

At the evaluation point `alpha=-1`,

`|c_j| = prod_(m!=j) (K-1+m)/|j-m|`.

Using `K-1+m<=2(K-1)` and

`sum_j 1/[j!(K-1-j)!]=2^(K-1)/(K-1)!`,

one gets

`Lambda_K:=sum_j|c_j|`

`<= [4(K-1)]^(K-1)/(K-1)!`

`<= (4e)^(K-1)`.

At

`K~(1/2)log X/loglog X`,

this is

`Lambda_K=X^o(1)`.

There is also an unavoidable exponential cost for **any** node choice confined to `[0,1]`. Let

`q(alpha)=T_(K-1)(2alpha-1)`,

where `T_m` is the Chebyshev polynomial. Then `|q(alpha)|<=1` on `[0,1]`, while

`|q(-1)|=T_(K-1)(3)`.

For any exact evaluation weights at nodes in `[0,1]`,

`T_(K-1)(3)=|sum_j c_j q(alpha_j)|<=sum_j|c_j|`.

Hence

`Lambda_K >= T_(K-1)(3)`

`~ (1/2)(3+2sqrt(2))^(K-1)`.

So exponential-in-K sign mass is intrinsic to extrapolating from positive fractional-divisor parameters to the parity point `-1`; nevertheless it remains only `X^o(1)` at the RH-critical depth.

Freeze complexity law:

`POSITIVE_ALPHA_TO_PARITY_EXTRAPOLATION_COST = exp(Theta(K)) = X^o(1) AT K_RH`.

---

## 5. Relation to the integer Heath-Brown stencil

For integer nodes

`alpha_j=j-1`, `j=1,...,K`,

Lagrange evaluation at `-1` gives exactly

`c_j=(-1)^(j-1) C(K,j)`.

Hence the growing prime-cutoff Heath-Brown identity is precisely the special case of the fractional-node theorem obtained by extrapolating the rough generalized-divisor polynomial from the integer nodes

`0,1,...,K-1`

to the parity node `-1`.

For a squarefree rough part with r prime factors,

`d_alpha(b)=alpha^r`,

so the familiar finite-difference identity becomes

`sum_(j=1)^K (-1)^(j-1) C(K,j)(j-1)^r=(-1)^r`, `r<K`.

This is not merely a formal analogy: it is the Cellwise content of the Heath-Brown circuit.

Freeze interpretation:

`GROWING_HEATH_BROWN = LAGRANGE EXTRAPOLATION OF ROUGH FACTOR MULTIPLICITY TO alpha=-1`.

---

## 6. Why the correction does not prove RH

The corrected/fractional representation removes one artificial obstruction but does not supply the needed global cancellation.

For `alpha in [0,1]` every branch coefficient is bounded by 1, so branchwise absolute summation gives at best order X. Multiplying by interpolation total variation `X^o(1)` still gives only

`X^(1+o(1))`,

not the required square-root scale for the first Brownian/cosine observer.

Thus

`BOUNDED POSITIVE ROUGH BRANCHES + SUBPOLYNOMIAL EXTRAPOLATION COST != RH`.

Cross-node signed cancellation remains essential.

The improvement is architectural: the search for a signed/PSD cross-branch mechanism can now be carried out in a basis whose individual coefficients are uniformly bounded and whose small-prime signs are common across branches, instead of a basis with large rough divisor multiplicities.

---

## 7. Analytic-continuation boundary: the omitted tail retains every zeta singularity

For the integer-node geometric identity,

`1/zeta = F_y sum_(r=0)^(K-1) H_y^r + H_y^K/zeta`,

where `H_y=1-zeta F_y`.

The finite branch part is analytic at every zero of zeta. Consequently the remainder

`H_y^K/zeta`

has exactly the same principal part as `1/zeta` at every zeta zero, for every K.

Indeed,

`H_y^K/zeta - 1/zeta = -F_y sum_(r=0)^(K-1)H_y^r`,

which is analytic at zeta zeros.

Thus growing coefficient depth does **not** attenuate off-critical zero singularities under analytic continuation. The fact that the remainder has no Dirichlet coefficients below `y^K` is a coefficient-support statement; it does not make the analytically continued remainder harmless in a contour shift.

Freeze observer boundary:

`HIGH COEFFICIENT SUPPORT != ANALYTIC SINGULARITY REMOVAL`.

This is another reason the coefficient identity is not itself an RH proof.

---

## 8. Prime-adapted connection route closed as a coordinate tautology

A previous conversation-local candidate introduced a vector field intended to annihilate the primitive prime channel `zP(s,y)`.

First, the sign must be corrected. If `P_s=dP/ds`, then at `z=-1` the null direction is

`V_z = partial_z + (P/P_s) partial_s`,

not `partial_z-(P/P_s)partial_s`.

More fundamentally, wherever a finite/regularized `P(s,y)` is nonzero and `P_s!=0`, define

`Phi(z,s,y)=log P(s,y)-z`.

Then

`V_z Phi=0`.

The y-adapted tangent direction is

`V_y = partial_y - (P_y/P_s) partial_s`,

and also `V_y Phi=0`.

Using `(z,y,Phi)` as local coordinates, `V_z` and `V_y` are just the coordinate derivatives at fixed Phi. Hence

`[V_z,V_y]=0`.

Any nonzero commutator obtained by comparing `V_z` with the **unadapted** `partial_y` is a coordinate mismatch, not an intrinsic curvature/holonomy invariant.

Moreover the infinite prime sum `P(s,y)` is directly convergent only to the right of 1; continuing/regularizing it in the critical strip imports the same zeta-zero singularity structure one is trying to control.

Freeze negative result:

`PRIME_ADAPTED_CONNECTION_HOLONOMY = COORDINATE TAUTOLOGY / NO INDEPENDENT RH LEVER`.

Do not continue this route unless a connection is defined independently of the actual prime channel and has a nontrivial arithmetic invariant.

---

## 9. Current admissible frontier

The best current multiplicative architecture is now:

`COMMON SMALL-PRIME MOBIUS PROVENANCE`

`x`

`K POSITIVE BOUNDED ROUGH FRACTIONAL-DIVISOR BRANCHES`

`x`

`LAGRANGE EXTRAPOLATION TO alpha=-1 WITH X^o(1) TOTAL VARIATION`.

At the canonical

`y=(log X)^2`, `K~(1/2)log X/loglog X`,

this exactly matches the independently identified RH-critical provenance depth.

The remaining question is no longer whether one can construct enough finite-depth branches or keep their pointwise coefficients bounded. One can.

The remaining question is:

Can the first Brownian/cosine RH-equivalent observer, or an equivalent Pair-BRC collision observer, exploit **cross-alpha cancellation** of these bounded branches by a PSD/provenance-preserving transform that is stronger than branchwise triangle inequality and does not hide `1/zeta` or an RH-equivalent inverse?

That is the next admissible target.
