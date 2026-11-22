# R5: the sharp O(N) period persists through threshold m=4

Date: 2026-11-22. Status: **AUTHOR_EXACT_PROOF / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED**. Independent GitHub portable work, with no current authenticated Task CLAIM/RUN, Result or Review.

## Frozen model and result

For the **same true five-event scalar partition model** frozen at enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15, with 101 prices 214,...,314 and five supports

S0={214,...,218}, S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}, S3={223,...,290}, S4={296,...,312},

count nonnegative integer price multiplicities a_p of cost N=sum p a_p such that **at least one** failure event E_i : sum_{p in S_i}a_p<m holds. Let M_m(O_m(N)) denote the least common quasipolynomial coefficient period for terms of degree >=2, modulo remainder O_m(N). The new exact theorem is

\[
\boxed{M_4(O_4(N))=229\,746\,052\,653\,717\,600.}
\]

Together with the separately certified m=1,2,3 cases, the same sharp maximum holds at every **m=1,2,3,4**.

## Exact numerator with all joint constraints retained

For nonempty I subset of {0,...,4}, put U_I=union_{i in I} S_i and let the exact membership signature \sigma_I(p)={i in I:p in S_i}. Set C_B={p in U_I:\sigma_I(p)=B} for each nonempty signature B. For 0<=r<=3 define

\[
H_{B,r}(q)=[u^r]\prod_{p\in C_B}(1-uq^p)^{-1}.
\]

Every price in U_I has multiplicity <=3 under the intersection of E_i, i in I. Each selected class B has aggregate count r_B, with simultaneous constraints \sum_{B\ni i}r_B<=3 for each i in I. Hence the intersection polynomial is the exact identity

\[
Q_{I,4}(q)=\sum_{\substack{0\le r_B\le3\\
 \sum_{B\ni i}r_B\le3\ (i\in I)}}\prod_{B}H_{B,r_B}(q).
\]

Proof is a bijection: restrict a valid assignment to each disjoint exact-signature class; conversely each tuple of class multiplicities satisfying the incidence counts defines a unique assignment. This preserves the joint E0/E1/E2 overlap.

For D(q)=prod_{p=214}^{314}(1-q^p), inclusion-exclusion gives F_4(q)=R_4(q)/D(q) with

\[
R_4(q)=\sum_{\emptyset\ne I\subseteq\{0,\ldots,4\}}
(-1)^{|I|+1}Q_{I,4}(q)\prod_{p\in U_I}(1-q^p).
\]

## Exact cyclotomic period proof

At a primitive d-th root zeta_d, the denominator vanishes to order n_d=# {214<=p<=314:d divides p}. To contribute an N^2 or higher quasipolynomial term, pole order at least 3 is necessary. Precisely 39 d>=2 have n_d>=3:

2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,43,44.

Their lcm L=229746052653717600 is the universal upper bound for M_4(O(N)).

For every d in the table below, the integral power-basis coefficient of the first nonzero term of R_4(zeta_d(1+t)) is as displayed. All checks use integer arithmetic modulo Phi_d and identical full vectors from **two separately implemented** exact formulas: (A) per-price five-capacity DP over a_p=0,...,3, (B) per-signature group convolution with complete homogeneous polynomial H_{B,r}, r=0,...,3. The implementations agree on the full zero and first jets for every listed root, not merely on the first coordinate.

| d | denominator zero n_d | first nonzero jet j | remaining pole | coordinate (zero-based) | coefficient |
|---:|---:|---:|---:|---:|---:|
| 7 | 14 | 1 | 13 | 2 | -1519 |
| 9 | 11 | 1 | 10 | 0 | -7776 |
| 11 | 9 | 0 | 9 | 0 | 7 |
| 13 | 8 | 0 | 8 | 0 | 11 |
| 17 | 6 | 0 | 6 | 0 | -2 |
| 19 | 5 | 0 | 5 | 0 | -34 |
| 23 | 4 | 0 | 4 | 0 | -21 |
| 25 | 4 | 0 | 4 | 0 | 101 |
| 27 | 4 | 1 | 3 | 0 | 6021 |
| 29 | 3 | 0 | 3 | 0 | 1269989 |
| 31 | 4 | 1 | 3 | 0 | 744 |
| 32 | 3 | 0 | 3 | 0 | 52487392 |
| 37 | 3 | 0 | 3 | 0 | -4 |
| 43 | 3 | 0 | 3 | 0 | 1 |

Every table row has a pole of order n_d-j>=3 and hence forces d to divide any O(N)-coefficient period (distinct primitive-root frequencies cannot disappear into the O(N) remainder). The 14 witness d have lcm L, so L divides the period, matching the upper bound.

## Validation and scope

The checked Python 3 standard-library verifier is VERIFY_R5_M4_O1.py, which imports the already-verified m2 ring arithmetic from its sibling directory. Locally executed at the same author code version on 2026-11-22: **ALL CHECKS PASS**. Code SHA256 328b39a6b3ea845f774d17b44746b8c0aa659ed30f1ac484a5c2e43d81fdd9ba. The full root vectors are recomputed, compared and reduced to the shown certificate rows on every run. Independent mathematical review: **NOT_REVIEWED**.

Signed cyclotomic jet information is retained, rather than replaced by positive-only BRC totals, because the exact unit-root cancellation is the decisive observer. This is the frozen scalar model and does not alter P000 or claim full native X6 dynamics.

## Next open problem and control

Investigate m>=5 through the same exact signature-capacity construction and attempt general m symbolic closure or locate a genuine shrinking primitive-root factor. The four verified cases establish a finite family, not a proof for all m.

Native owner inventory request r5-20261122-0843-owner-onebounded-v1 returned FAILED/SOURCE_TREE_TRUNCATED. Current Researcher session/Activity CAS and live owner were not authenticated. This file is an independently published research note under the existing portable GitHub scope; it is not a formal CLAIM/RUN or adopted Result/Review.
