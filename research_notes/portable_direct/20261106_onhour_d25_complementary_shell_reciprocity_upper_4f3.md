# D25 — complementary 216 valuation shells and finite upper 4F3 (author-side)

Date: 2026-11-06. TASK_RESEARCH, AUTHOR-PROVED / FINITE VERIFIED / UNREVIEWED / NOT_ADMITTED.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research lane: chatgpt-research-onhour-enterprise-math-20260923 (no maintenance-lane identity).
This note advances the original 216/2304 scalar interface, not the native p373 H0/B0 experiment.

## Original coefficients and precise open target

Let a_k=(2k)!(3k)!/[216^k(k!)^5] = C(2k,k)^2*C(3k,k)/216^k;
b_k=(4k)!/[2304^k(k!)^4]. For prime p=6m+1 put h=3m, s=3m+1,
L=4m and J=m-1. The already-proved valuation partition of original a_k
is 0..2m (v_p=0), 2m+1..3m (v_p=1), 3m+1..4m (v_p=2), k>L (v_p>=3).
Define B_p=sum_{k=0}^{2m}(6k+1)a_k,
M_p=sum_{k=2m+1}^{3m}(6k+1)a_k,
U_p=sum_{k=3m+1}^{4m}(6k+1)a_k/p^2,
V_h=sum_{k=0}^{h}(8k+1)b_k, and D_p=(B_p-V_h)/p mod p^2
under the previously established first-digit divisibility.
The outstanding uniform third-digit condition is
D_p + M_p/p + p*U_p = 0 (mod p^2).
The frozen scalar bridge to Delta_p-R_p=0 mod p retains its actual source scope.

## Theorem A — exact complementary-shell reciprocity (ALL primes p>3)

For every prime p>3 and integer p/3<k<p/2, set l=p-k (p/2<l<2p/3).
Then v_p(a_k)=1, v_p(a_l)=2 and, in F_p,

    (a_k/p)*(a_(p-k)/p^2) = 1/(36*k^3).                      (A)

Here division by p is first performed on the p-integral original rational
coefficient and only then reduced modulo p. All shown denominators are p-units.

Proof. Wilson gives r!*(p-r)!=(-1)^r*r mod p for 0<r<p.
For p<n<2p, n!/p=-(n-p)! mod p.
Exactly three numerator factorials in the product a_k*a_l have
one p-factor: (3k)!, (2l)! and (3l)!. Therefore

 (a_k/p)*(a_l/p^2)
  = -(2k)!*(3k-p)!*(p-2k)!*(2p-3k)! /
    [216^p*(k!*l!)^5]  (mod p).

Use (2k)!*(p-2k)!=2k; (3k-p)!*(2p-3k)!=
(-1)^(3k-p)*(3k-p); k!*l!=(-1)^k*k; and 216^p=216,
all modulo p. The total sign is positive because 2k-p is odd.
Thus the expression is (2k)*(3k-p)/(216*k^5)
=6k^2/(216*k^5)=1/(36*k^3) mod p. QED.

For p=6m+1 the entire middle band k=h-j, 0<=j<=J, is bijective
under k<->p-k with upper band l=s+j. Their original weights add EXACTLY
to (6k+1)+(6l+1)=6p+2. Keep the signed index and valuation provenance.

## Theorem B — terminating upper-shell hypergeometric kernel

For prime p=6m+1>=7, write eps=(6/p) in {+1,-1}. In F_p put Q_0=1 and

 Q_(j+1)/Q_j = (j+1)(6j+5)(6j+7)(6j+9) /
               [27(2j+3)^4],          0<=j<J.            (B0)

All denominators are units. Equivalently
 Q_j = 2^(-j)*j!*(5/6)_j*(7/6)_j / (3/2)_j^3.
Then for every 0<=j<=J,

    a_(s+j)/p^2 = (eps/9)*Q_j (mod p),                  (B1)

and, for H_U(z)=sum_{j=0}^J Q_j*z^j with theta=z*d/dz,

    U_p = (eps/9)*(6*theta+4)*H_U(1) (mod p).          (B2)

Proof. At s=(p+1)/2, (2s)!/p=-1 and (3s)!/p=-(s+1)! mod p.
Consequently a_s/p^2=(s+1)/[216^s(s!)^4].
Writing h=(p-1)/2, Wilson gives (h!)^4=1, s!=s*h!,
(s!)^4=1/16, and by Euler 216^s=216*eps, all mod p.
Hence a_s/p^2=eps/9. The exact original coefficient ratio is

 a_(k+1)/a_k =
 (2k+1)(2k+2)(3k+1)(3k+2)(3k+3)/(216(k+1)^5).

Substituting k=s+j and reducing modulo p gives (B0) with only p-units
for 0<=j<J. Finally the original weight 6(s+j)+1=3p+6j+4
reduces to 6j+4. QED.

This is the finite p-reduction of
 _4F_3(1,1,5/6,7/6;3/2,3/2,3/2;z/2).
The following FOURTH-ORDER polynomial equation holds in F_p[z]:

 [9*theta*(2*theta+1)^3
   -z*(theta+1)^2*(6*theta+5)*(6*theta+7)] H_U(z)=0.   (B3)

Indeed B0 cancels every coefficient at degrees 1..J; the remaining
degree J+1 coefficient is
 -(J+1)^2*(6J+5)*(6J+7)*Q_J, zero because 6J+7=p.
Degree zero is zero from the theta factor. No higher coefficients occur.

## Theorem C — exact middle/upper duality and new third-digit interface

Reuse the proven middle-shell mod-p kernel P_0=1,
 P_(j+1)/P_j=9(2j+1)^3/[(j+1)(6j+5)(6j+7)].
It satisfies a_(h-j)/p = -2*eps*P_j mod p.
Multiplying the rational consecutive ratios gives
 (P_(j+1)Q_(j+1))/(P_j Q_j)=((2j+1)/(2j+3))^3.
As P_0 Q_0=1,

    P_j Q_j = 1/(2j+1)^3 (mod p), 0<=j<=J.           (C)

This is precisely (A) for k=h-j; the middle and upper shells are
reciprocal under a source-preserving involution, not separate zero terms.
By (B2) the exact unresolved third-digit test now reads

    D_p + M_p/p + p*(eps/9)*(6theta+4)H_U(1)
      = 0 (mod p^2).                                  (D)

The upper port in (D) is now an explicit terminating 4F3 polynomial with
an exact homogeneous finite-field differential operator and indexwise
dual to the previously known middle 4F3. Equality (D) as a CONDITION is
equivalent to the inherited target; uniform vanishing is still OPEN.
Retain bottom D_p and the middle's second p-adic digit in any adjoint.

## Independently executed exact checks / BRC

Program: d25_upper_shell_finite_4f3_20261106.py. It reconstructs the
original binomial coefficients in Z/p^3, tests upper units, both kernels,
weighted U_p, every coefficient of (B3), and normalized paired products.
All 80 primes 7<=p<=997 with p=1 mod6 passed.
An independent p-free-factorial-unit implementation checks (A) for
all 166 primes 5<=p<=997: 12,688 distinct complementary index pairs,
zero failed assertions. Data:
20261106_d25_upper_shell_finite_4f3_results.json.

Samples (p,eps,a_s/p^2 mod p,U_p mod p):
(7,-1,3,5); (13,-1,10,10); (19,+1,17,9); (67,+1,15,58);
(139,+1,31,13); (373,-1,290,266); (997,-1,443,27).
For p=13,19 the new upper U values match prior original-source
third-digit witnesses. The p373 value here is only portable 216 arithmetic.

BRC use: COMPOSE_APPLIED to actual original model indices k and p-k with
valuation pair (1,2), original signed weights summing 6p+2, p-unit
normalization and the dual first-digit kernels. Algebraic operations are
explicitly mod p on the stated observer; no native Frobenius identification.

## Control status and next exact action

Source read-only continuation request
onhour11-20261106-0357-d25-exact-continuation was QUEUED at last receipt;
retain original request for read/reconcile, never replay its side effects.
Earlier onhour11-20261106-0302-exact-lift-continue was SUCCEEDED with
execution_authorized=false. Historical researcher record EM-ENTERPRISE-946A26
is not a current private session key. No own CLAIM/open/run/Result exists
in this author-side work.

Next: try a paired finite adjoint/creative-telescoping certificate using
(C) and the respective middle and upper 4F3 endpoints, retaining
the bottom p-adic correction D_p and the middle first-order p-deformation.
Test the nonzero p13/p19 signed boundary contributions, then aim for
the all-prime cancellation; preserve source pin, signed index mapping.
Native fixed H0/B0 [X]U mod139129, rank, semilinear eta/kappa and
odd Green/Hesse observer still require an authorized native p373 executor:
support Issue #1559, OPEN/PENDING_OWNER, NOT_EXECUTED.
Author-side mathematics is not a native experiment, Result or review.
