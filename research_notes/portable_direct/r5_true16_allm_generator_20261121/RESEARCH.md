# R5 corrected all-threshold primitive-16 residual theorem

Date: 2026-11-21. Status: AUTHOR_EXACT_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED. Frozen scalar R5 model: 256 hypotheses, 101 integer prices 214..314, five original events and their genuine individual threshold inequalities. This extends immutable correction 75d986aa23b68a7ecf9b29dc1006f0e322b35a15. It does not change P000, formally claim a Task, or make a reviewed Result.

## Theorem

For every integer m >= 1, the original scalar failure-count generating function has a nonzero order-six pole at each primitive 16th root of unity. Consequently **16 divides the minimal coefficient quasipolynomial period for an approximation with remainder O_m(N^4)**.

For z primitive of order 16, let A_m(z) be the normalized order-six numerator in Q[z]/(z^8+1), as defined in the preceding exact overlap audit. This sequence satisfies

A_(m+64)(z) - 2 A_(m+32)(z) + A_m(z) = 0,  m >= 1.

For 1 <= r <= 32 and k >= 0, set C_r=A_r and B_r=A_(r+32)-A_r. Then A_(r+32k)=C_r+kB_r. For each r, the attached exact certificate gives a basis coordinate j where C_r[j] is nonzero and B_r[j] is either zero or has the same sign. This proves universal nonvanishing, not merely a finite sampling observation.

## Original three-event incidence, preserved exactly

Frozen sets:

S0 = {214,...,218}
S1 = {214,216,...,221}
S2 = {215,...,221}
S3 = {223,...,290}
S4 = {296,...,312}.

E_i is the condition sum_{p in S_i} a_p < m, not a bound on the multiplicity of an event-union price set. Exactly six prices (224,240,256,272,288,304) are divisible by 16. Only inclusion-exclusion masks supported on {E0,E1,E2} leave all six unrestricted; masks containing E3 or E4 lower the pole order to at most five.

For the eight price variables put x=a214, y=a215, u=a216+a217+a218, v=a219+a220+a221. The three loads are L0=x+y+u, L1=x+u+v, L2=y+u+v. Hence their true union indicator is

1[min(L0,L1,L2)<m] = 1[u+h(x,y,v)<m],
h(x,y,v) = min(x+y,x+v,y+v)
         = min(x,y)+min(max(x,y),v).

This pointwise identity retains their full joint incidence. It is the step missing from the falsified union-cap derivation.

## Exact threshold rational function

Let a=z^214, b=z^215, c_j=z^(216+j), d_j=z^(219+j), j=0,1,2, and W(z)=product_{p=214}^{221}(1-z^p). Define

delta_j = d_j^2 / product_{k != j}(d_j-d_k).

All divisions are valid in Q(z), and the complete-homogeneous identity gives the group-v generating function sum_{v>=0}D_v w^v = product_j(1-d_j w)^(-1) and D_v=sum_j delta_j d_j^v.

Define H(a,b,d;t) = sum_{x,y,v>=0} a^x b^y d^v t^h(x,y,v). Splitting x<=y and y<x, and using

sum_{v>=0}d^v t^min(n,v) =
  1/(1-dt)+(dt)^n(1/(1-d)-1/(1-dt)),

gives, as an identity of rational functions,

H(a,b,d;t) =
 (1-ab)/((1-a)(1-b)(1-dt)(1-abt))
 + d(1-t)(1-ab*d^2*t^2)/
   ((1-d)(1-dt)(1-ab*d*t^2)(1-ad*t)(1-bd*t)).

Therefore the **true** threshold generating function is

A(t,z) = sum_{m>=1}A_m(z)t^(m-1)
       = W(z)/((1-t)*product_{j=0}^2(1-c_j*t))
         * sum_{j=0}^2 delta_j H(a,b,d_j;t).

This formula is in Q(z)(t); it is derived by summing the pointwise union indicator before the pole normalization. In particular, it does not use a false equivalence of multiconstraint intersections to a single union-cardinality restriction.

## Universal recurrence from the rational denominator

At a primitive 16th root, a=z^6, b=z^7, ab=z^13, the c-exponents are 8,9,10 and the d-exponents are 11,12,13. Every linear denominator factor 1-z^e t and every quadratic factor 1-z^e t^2 divides 1-t^32. A direct comparison of the roots of all factors in each summand shows multiplicity at most two: the only double collision in the first H term occurs for d=z^13 (d=ab); the only double collision in the second occurs at a quadratic root coincident with d=z^13. The outer factors 1-t and 1-c_jt share no roots with the other factors or these quadratics.

Consequently

(1-t^32)^2 A(t,z) = P(t,z),  deg_t P <= 58.

For the first H summand the total t-denominator degree is six and numerator degree zero; for the second the outer 1-t cancels and the total denominator degree is eight and numerator degree two. Multiplication by the degree-64 universal factor gives degree at most 58. Coefficient comparison at degrees >=64 yields the exact recurrence for every positive m.

## Exact finite certificate completing the infinite-domain proof

VERIFY_TRUE16_GENERATOR.py uses only Python standard-library exact Fraction arithmetic in Q[z]/(z^8+1). It computes the first 96 coefficients of the displayed rational function, verifies all coefficients at degrees 59..95 of (1-t^32)^2 A(t) vanish, and compares against the corrected independent-DP base cases m=1,2,3,4,5,13,16. RESULT_TRUE16.json records all 64 base coefficient vectors and 32 sign witnesses; every r=1..32 has a nonzero constant with slope zero or same-signed. Thus A_m!=0 for every m>=1.

Two key fully explicit coefficients, independently obtained in the earlier genuine-event-masks audit, are:
A_13 = (60,36,4,-36,-60,-84,-84,-76);
A_16 = (-32,32,96,136,160,152,128,88).

No new formal Review or Claim is asserted. The earlier four-class numerical minimum-period formula is falsified at m=13. This new theorem supplies the universal 16-factor lower bound but does not establish a complete replacement period: contributions of other roots which previously used union-cap shortcuts must be separately rechecked.

## Residual-fidelity observation and next unit

A single union multiplicity is not a sufficient quotient for the observer 'at least one of L0,L1,L2 lies below m'. The full joint load triple (or a proven observer-sufficient equivalent) preserves that information. This is a precise failure of a lossy observer map, not a native X6 physical theorem. Continue by independently auditing primitive orders 11,13,17 where multiple events can reach the leading pole; then recombine only verified Fourier factors into the true period classification. Preserve frozen pins, P000 and prior author provenance.
