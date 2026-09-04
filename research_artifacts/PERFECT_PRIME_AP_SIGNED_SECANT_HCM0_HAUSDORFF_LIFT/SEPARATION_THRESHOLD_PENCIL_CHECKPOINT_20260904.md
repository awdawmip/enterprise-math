# Perfect Prime AP HCM0 — separation-threshold quotient-pencil checkpoint

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL STRUCTURAL / EXACT-BOUNDARY CHECKPOINT — HCM0 REMAINS OPEN**

## 1. Frozen quotient family

Put `n=m-1` and

\[
\mu_r=\frac{n!}{\prod_{a=1}^{m}(mr+a)}
      =\int_0^1 v^r\,d\nu_m(v),
\]

with

\[
d\nu_m(v)=\frac1m v^{1/m-1}(1-v^{1/m})^n\,dv>0.
\]

Let

\[
D_r=\operatorname{diag}\left((-1)^j\binom nj\mu_{r+j}\right)_{j=0}^{n},
\]

let `P` be the Pascal value-to-Newton matrix on `0,1,...,n`, and let `H_r` be the leading `n x n` block of `P^T D_r P`.

For an integer translation distance `M>=1`, let

\[
T_M[k,a-1]=\binom{M}{a-k}\quad(0\le k<a\le n),
\]

with all other entries zero.  For integers `r0<r`, set

\[
M=r-r_0,
\qquad
Q_{r_0,r}=T_M^T H_rT_M.
\tag{1.1}
\]

For actual Perfect-Prime layers `s_e<s_d`,

\[
r_0=ms_e,\qquad r=ms_d,
\]

so `M=m(s_d-s_e)`.

The base-`m` three-support cell with a third layer `s_f` is controlled, up to the already frozen nonzero scalar, by

\[
\det\left(uQ_{ms_e,ms_d}+vQ_{ms_e,ms_f}\right).
\tag{1.2}
\]

## 2. Exact Mellin–Euler operator normal form

For `a=1,...,n` define

\[
g_{M,a}(j)=\binom{j+M}{a}-\binom ja
\]

and the polynomial in the Euler operator `Theta=x d/dx`

\[
\mathcal G_{M,a}(\Theta)
=\binom{\Theta+M}{a}-\binom{\Theta}{a}.
\]

Because `(1-x)^n=sum_j (-1)^j binom(n,j)x^j`, equation (1.1) gives the exact entry formula

\[
\boxed{
Q_{r_0,r}[a,b]
=\int_0^1 x^r
\mathcal G_{M,a}(\Theta)\mathcal G_{M,b}(\Theta)(1-x)^n
\,d\nu_m(x),
\qquad M=r-r_0.
}
\tag{2.1}
\]

Equivalently,

\[
Q_{r_0,r}[a,b]
=\sum_{j=0}^{n}(-1)^j\binom nj\mu_{r+j}
 g_{M,a}(j)g_{M,b}(j).
\tag{2.2}
\]

The corresponding bivariate generating kernel is

\[
\boxed{
\sum_{a,b\ge1}Q_{r_0,r}[a,b]z^aw^b
=((1+z)^M-1)((1+w)^M-1)
\int_0^1 x^r\left(1-x(1+z)(1+w)\right)^n d\nu_m(x),
}
\tag{2.3}
\]

where the matrix uses only `1<=a,b<=n`.

This normal form isolates the load-bearing coupling: the same `M` occurs both in the translation difference and in the moment shift `r=r0+M`.

A useful conjugation identity is

\[
\binom{\Theta+M}{a}=x^{-M}\binom{\Theta}{a}x^M,
\qquad
\binom{\Theta}{a}=\frac{x^a}{a!}\frac{d^a}{dx^a}.
\tag{2.4}
\]

Thus the candidate threshold `M>=n+1=m` is exactly the range in which integration by parts through every order `a<=n` can kill the `x^M` boundary jet at `x=0`.  This observation is a proof interface, not yet a completed positivity proof.

## 3. Correction: the moment weight is not classical two-parameter Hahn

An intermediate hypothesis attempted to identify

\[
(-1)^j\binom nj\mu_{r+j}
\]

with an ordinary Hahn weight.  Exact substitution rejects that identification: the factor

\[
\prod_{a=1}^{m}(m(r+j)+a)
=m^m\prod_{a=1}^{m}\left(r+j+\frac am\right)
\]

has `m` fractional-offset factors and is not the ordinary one-step Pochhammer that would produce classical Hahn.

The correct hypergeometric ratio is

\[
\boxed{
\frac{\mu_{r+j}}{\mu_r}
=\prod_{a=1}^{m}
\frac{(r+a/m)_j}{(r+a/m+1)_j}.
}
\tag{3.1}
\]

Hence the finite signed weight is a terminating higher hypergeometric / generalized-Hahn-type weight with `m` paired numerator/denominator parameters, not the classical two-parameter Hahn family.  No classical-Hahn orthogonality result is used below.

## 4. Positive-real generalized spectrum is too strong

A numerically attractive sufficient condition was

\[
\operatorname{spec}(Q_{r_0,r}^{-1}Q_{r_0,s})\subset\mathbb R_{>0}.
\]

It is false.

### 4.1 Non-actual integer-aligned spectral counterexample

At

\[
m=9,\qquad(r_0,r,s)=(0,1,4),
\]

the exact rational characteristic polynomial of `Q_{0,1}^{-1}Q_{0,4}` has a genuine nonreal conjugate pair

\[
0.0010291333225049004\ldots
\pm0.0004367967450661592\ldots i.
\]

High-precision roots are obtained from the exact rational polynomial, so this is not a floating-point conditioning artifact.

Nevertheless every coefficient of

\[
\det(Q_{0,1}+tQ_{0,4})
\]

has the correct common sign.  Thus real spectrum is stronger than the coefficient theorem actually needed.

### 4.2 Actual-layer spectral counterexample

Even the actual-layer spectrum eventually ceases to be real.  At

\[
m=10,\qquad(s_e,s_d,s_f)=(0,3,4),
\]
so

\[
(r_0,r,s)=(0,30,40),
\]
`Q_{0,30}^{-1}Q_{0,40}` has a stable nonreal pair approximately

\[
1.31612534101399\ldots\pm0.02454359756182\ldots i.
\]

Yet the ten coefficients of

\[
\det(Q_{0,30}+tQ_{0,40})
\]

are all strictly positive.  Therefore generalized-real-rootedness is decisively rejected as the all-`m` mechanism.

## 5. Exact coefficient frontier advances through every actual triple at m=10

Using exact `fractions.Fraction` arithmetic and determinant interpolation, all

\[
\binom{10}{3}=120
\]
actual layer triples `0<=s_e<s_d<s_f<=9` were checked.

For every triple, every coefficient of

\[
\det\left(Q_{10s_e,10s_d}+tQ_{10s_e,10s_f}\right)
\]

is nonzero and has one common sign.

This extends the earlier full three-support coefficient evidence (`m<=7`) in a different direction: it proves the complete **base-`m` slice** at `m=10`, including the actual spectral counterexample above.  It remains finite evidence, not an all-`m` theorem.

## 6. Integer alignment alone is also false: exact m=10 coefficient counterexample

The stronger conjecture allowing arbitrary integer synchronized shifts fails at

\[
\boxed{m=10,\qquad(r_0,r,s)=(0,1,5).}
\]

For

\[
p(t)=\det(Q_{0,1}+tQ_{0,5})
\]
all coefficients are positive except the coefficient of `t^8`, which is exactly

\[
\boxed{
[t^8]p(t)=
-\frac{
10612824961174951202027648577503279651182772104969959464262239715
}{
1779190353785266854363656648348425662886396623357055484212781139453940884444359455084001552607701836246656138519424941793415894301254772509798569513296767514860060672
}<0.
}
\tag{6.1}
\]

Thus neither `integer translation` nor `translation/moment synchronization` by itself is sufficient.

The actual scaled comparison `(r_0,r,s)=(0,10,50)` has all coefficients with the correct common sign.

## 7. New minimal candidate: separation threshold M>=m

The surviving structural conjecture is

### `M5_BLOCK_SEPARATED_MELLIN_EULER_PENCIL`

For every `m>=2`, `n=m-1`, integers

\[
r_0<r<s,
\qquad
M=r-r_0\ge m,
\]

all coefficients of

\[
\det(Q_{r_0,r}+tQ_{r_0,s})
\]

are nonzero and have the same sign as `det Q_{r_0,r}`.

This theorem would immediately cover every actual Perfect-Prime base-`m` three-support slice, because actual gaps are positive multiples of `m`.

### Exact finite stress evidence

Near the proposed threshold, exact rational tests gave:

- for every `m=3,...,10`: 100 pencils per `m`, with `r_0=0,...,3`, `M=m,...,m+4`, and `N=s-r_0` ranging immediately above `M`; all 800 pencils had every coefficient strictly of the target common sign;
- `m=11`: 30 additional random exact large-gap pencils, all strict;
- `m=12`: 30 additional random exact large-gap pencils, all strict.

The condition is not being inferred from these finite checks; they only isolate the first still-unrefuted theorem.

## 8. Failure geometry below threshold

A base-`r0=0` exact census illustrates that the failure region first enters only near the top mixed coefficient.

- `m=9`, `1<=M<N<=15`: no coefficient failures.
- `m=10`, `1<=M<N<=18`: five failures, exactly `(M,N)=(1,5),(1,6),(1,7),(1,8),(1,9)`; in each case only degree `n-1=8` has the wrong sign.
- `m=11`, `1<=M<N<=18`: twelve failures; the first are `(1,4),...,(1,12)` and `(2,6),(2,7),(2,8)`; again the detected wrong degree is `n-1=9`.
- `m=12`, `1<=M<N<=18`: eighteen failures; the first are `(1,4),...,(1,14)` and `(2,5),...,(2,11)`; again the detected wrong degree is `n-1=10`.

This makes the `M>=m` threshold a natural sufficient boundary, not a claim of sharp necessity.

## 9. Pointwise mixed-discriminant positivity is false

A second tempting overstrengthening was to expand (2.1) into separate pointwise matrices and demand the mixed discriminant be of one sign before Hausdorff integration.

Exact rational counterexamples occur already for `m=3,4,5,6`, even with both translation distances at least `m`.  Therefore the proof cannot proceed by pointwise positivity of the integrand.

The positivity, if `M5` is true, is genuinely produced after the coupled Hausdorff/Mellin integration.  The synchronization `r=r0+M` must remain intact.

## 10. Next proof interface

Equation (2.4) suggests the next deterministic attack.

Because

\[
\binom{\Theta}{a}=\frac{x^a}{a!}\partial_x^a
\]

and

\[
\binom{\Theta+M}{a}=x^{-M}\binom{\Theta}{a}x^M,
\]
all translation differences can be converted into ordinary derivatives of `x^M f(x)` minus `x^M f^{(a)}(x)`.

For `M>=m=n+1`, every boundary jet of `x^M` through the maximal required order `n` vanishes at `x=0`.  The remaining task is to perform the required multi-column integration by parts without destroying determinant structure, and to identify the resulting coefficient as a positive multiple integral / divided-difference determinant.

This is the current smallest noncircular all-`m` target.  It is strictly narrower than the false arbitrary-shift, positive-real-spectrum, arbitrary-integer, and pointwise-discriminant conjectures.

## 11. Boundary

Proved all-`m` in this checkpoint:

1. exact Mellin–Euler entry normal form (2.1)–(2.4);
2. correct higher-hypergeometric weight identity (3.1).

Proved exact finite boundaries:

1. positive-real generalized spectrum is false (`m=9` integer, `m=10` actual);
2. all actual base-`m` triple pencils at `m=10` have coefficientwise common sign (`120/120`);
3. arbitrary synchronized integer shifts are false (`m=10,(0,1,5)`, exact negative `t^8` coefficient);
4. pointwise mixed-discriminant sign is false;
5. no `M>=m` coefficient counterexample was found in the stated exact stress range.

Still open:

- `M5_BLOCK_SEPARATED_MELLIN_EULER_PENCIL`;
- full three-support all-m sign regularity;
- all-support layer sign regularity;
- HCM0;
- full shifted HCM for all `m`;
- parent determinant nonvanishing.

Paired exact checker:

`research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/separation_threshold_pencil_check_20260904.py`.
