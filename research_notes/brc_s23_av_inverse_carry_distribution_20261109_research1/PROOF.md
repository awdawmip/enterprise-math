# S23/AV inverse-index carry law and exact asymptotic frequency

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Status: author-side mathematical derivation and a finite exact rational certificate; independent review pending. This is the frozen two-point S23/AV auxiliary likelihood observer, **not** a native-X6/full six-source capacity theorem.

## Source dependencies and interface

This note uses the definitions and **proved all-index two-candidate candidate-plateau inverse lemma** from
research_notes/brc_s23_av_plateaux401_410_two_candidate_inverse_20261109_r1/PROOF.md
at immutable commit 23547581b85db6212d89f466dfb3f85b33e852c3.
The frozen likelihood laws on labels (1,3,4) are P0=(1/2,1/4,1/4) and P1=(5/7,1/4,1/28).
Label-1/label-4 joint counts and neutral label-3 padding remain preserved for this specific likelihood-cell readout and future operations. BRC reuse resolution: REUSE_APPLIED (joint provenance-preserving observer); no new native spatial claim.

Set r=ln(7)/ln(10/7), epsilon=79r-431, alpha=(2074774-380295r)/epsilon.
The earlier exact certificates establish 1/2<alpha<2/3. Define A=380295, B=79,
Gamma=A+B*alpha, a_k=floor(k*alpha), V_k=A*k+B*a_k, H_k=V_k+510, and
I(h)=min{i>=1:H_i>=h} for integer h>=511. As in the earlier inverse lemma,
k(h)=ceil((h-510)/Gamma) gives I(h) in {k(h),k(h)+1}.

## New theorem 1: exact second-candidate carry count in each coarse bin

For every integer k>=1 the set of integer horizons with k(h)=k but I(h)=k+1 is exactly

    E_k={H_k+1, ..., 510+floor(Gamma*k)}

where the set is empty when its upper endpoint is below its lower endpoint. Its cardinality is

    C_k = floor(B*{k*alpha}) = floor(79*{k*alpha}) in {0,...,78}.

Proof: k(h)=k is equivalent to Gamma*(k-1)<h-510<=Gamma*k.
The earlier two-candidate inverse chooses k+1 precisely when h>H_k.
Because H_k-510=Gamma*k-B*{k*alpha}>Gamma*(k-1) (Gamma>B),
the intersection with the coarse bin is the stated integer interval.
Its integer cardinality equals
floor(Gamma*k)-(H_k-510)
= A*k+floor(B*k*alpha)-A*k-B*floor(k*alpha)
= floor(B*{k*alpha}). QED.

Thus the correction uses at most 78 integer horizons in any one coarse bin
of approximately 380,341 horizons. This is a structural optimization for the
candidate staircase; the exact capacity N(h) requires the separate plateau
coverage certificate at the requested horizon.

## New theorem 2: complete finite-prefix counting identity

For every integer K>=1, the number of integer horizons
511<=h<=510+floor(Gamma*K) for which the second candidate is selected is

    S(K) = sum_{k=1}^K C_k
         = sum_{k=1}^K floor(79*k*alpha)
           - 79*sum_{k=1}^K floor(k*alpha).

These K coarse bins partition that integer horizon interval, so the first
identity follows from Theorem 1; the second is the floor carry identity.
For any certified rational interval al<alpha<au whose endpoints give identical
floors for both k*alpha and 79*k*alpha at k=1,...,K, evaluate both sums
exactly using Euclidean integer floor_sum on either endpoint.
The floor_sum core has logarithmic recursion in its integer inputs; this
**does not** omit the cost of obtaining an adequate rational certificate and
representing the large integer arguments.

## New theorem 3: asymptotic frequency and uniform carry symbols

The real number alpha is irrational. Indeed, rational r=p/q>0 would imply
7^(p+q)=10^p, contradicting unique prime factorization. The displayed
fractional-linear formula relating alpha and r is invertible over the rationals
(its numerator/denominator coefficient determinant is nonzero); hence
r irrational implies alpha irrational.

By equidistribution of {k*alpha}, each C_k symbol c in {0,...,78}
has natural frequency exactly 1/79. In particular,

    lim_{K->infty} S(K)/K = (0+...+78)/79 = 39;
    lim_{K->infty} S(K)/floor(Gamma*K) = 39/Gamma.

Numerically, 39/Gamma is approximately 0.00010253949249, or 0.010253949249%.
This is an all-index asymptotic fact about the **candidate inverse branch**,
rather than a density theorem about independently certified exact capacities.

## Exact finite computational certificate

VERIFY_INVERSE_CARRY.py uses the rational positive arctanh expansion
ln(z)=2*sum_{j=0}^{n-1} x^(2j+1)/(2j+1)+R,
x=(z-1)/(z+1), 0<R<=2*x^(2n+1)/((2n+1)*(1-x*x)).
Apply to z=7 and z=10/7 at n=160; propagate signed rational
numerator/denominator bounds through alpha.
All 20,000 floors k*alpha and 79*k*alpha for 1<=k<=10,000
are certified by equality of their rational endpoint floors.
Check the derived C_k in each bin, the endpoint inequalities for every
nonempty carry set, and the independent Euclidean floor_sum identity.

Actual local output in RUN_EVIDENCE.txt:
PASS_S23_AV_INVERSE_CARRY_EXACT_RATIONAL;
S(10000)=390100; every one of the 79 symbols occurs.
The complete finite 10,000-bin computation is separate from the
irrational-rotation argument proving the unbounded theorem.

## Next scientific question

Can the full S23/AV critical-cell witness checker be given a uniform
translation/rotation certificate along this irrational mechanical index,
so that a full interval of exact capacity plateaux can be proved without
running an endpoint exhaustive check for each i?
A narrower next test is the exact i=412 critical-cell certificate using
the frozen checker and an explicit first uncovered cell, if any.
Independently inspect the inherited critical-cell reduction and first-entry
lower bound before promoting any unconditional exact-capacity claim.
