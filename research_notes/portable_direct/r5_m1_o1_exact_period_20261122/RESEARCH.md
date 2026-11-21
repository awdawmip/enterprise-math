# R5: exact m=1 period at O(N) precision

Date: 2026-11-22. Status: AUTHOR_EXACT_PROOF / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED. This is independent portable R5 mathematics, without an authenticated current Task CLAIM or Result. Frozen scientific model is unchanged.

Scientific lineage: true-event correction at enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15; latest prior unit at enterprise-math@7ace9700b88780e043a41d703d313ddb863f74d7:research_notes/portable_direct/r5_root27_31_allm_20261122/RESEARCH.md. The new theorem is self-contained for the m=1 scalar instance, rather than depending on the previous author-side all-threshold period classification.

## Exact theorem

For each price p=214,...,314, let a_p be a nonnegative integer and define total cost N = sum(p*a_p). Let f_1(N) count solutions satisfying at least one of the five frozen failure events

- E0: sum_{p=214..218} a_p = 0;
- E1: sum_{p in {214,216,217,218,219,220,221}} a_p = 0;
- E2: sum_{p in {215,216,217,218,219,220,221}} a_p = 0;
- E3: sum_{p=223..290} a_p = 0;
- E4: sum_{p=296..312} a_p = 0.

These are exactly the original threshold events sum_{p in S_i} a_p < m at m=1; simultaneous events use their actual union of supports. Define M_1(O(N)) to be the least quasipolynomial coefficient period for the degree >=2 part of f_1(N), allowing an O(N) remainder as N tends to infinity through nonnegative integers. Then

$$
\boxed{M_1(O(N))=229\,746\,052\,653\,717\,600.}
$$

Prime-power factorization: 2^5 * 3^3 * 5^2 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 43.

## Proof: universal upper bound

With q an indeterminate and D(q)=prod_{p=214}^{314}(1-q^p), exact finite inclusion/exclusion gives

$$
F_1(q)=\sum_{N\ge0}f_1(N)q^N=\frac{R_1(q)}{D(q)},\qquad
R_1(q)=\sum_{\emptyset\ne I\subseteq\{0,\ldots,4\}}(-1)^{|I|+1}
\prod_{p\in U_I}(1-q^p),\quad U_I=\bigcup_{i\in I} S_i.
$$

At any primitive d-th root zeta_d (d>=2), the denominator has a zero of order n_d = floor(314/d)-floor(213/d). Thus a pole of order >=3 can occur only for n_d>=3. Exact integer enumeration for d=2,...,314 gives the 39 candidates

2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,43,44.

Their least common multiple is L=229746052653717600. Partial fractions of F_1 at roots of unity express f_1(N) as exponential polynomials; poles of order at most two contribute only O(N). Therefore M_1(O(N)) divides L.

## Proof: matching lower bound from exact residue/jet witnesses

For each d in the following table, evaluate R_1 at q=zeta_d(1+t). Denote the coefficient of t^j, reduced to the integral power basis 1,zeta_d,...,zeta_d^{phi(d)-1} of Z[zeta_d], by C_{d,j}. Each listed coefficient is nonzero; the displayed entry is the first nonzero coordinate in the chosen basis. Thus R_1 has vanishing order at most j at each primitive d-root, leaving a pole of order at least n_d-j >=3.

| d | n_d | j | surviving pole order | coordinate (zero-based) | exact integer coefficient |
|---:|---:|---:|---:|---:|---:|
| 7 | 14 | 1 | 13 | 0 | 1085 |
| 9 | 11 | 1 | 10 | 1 | 1080 |
| 11 | 9 | 0 | 9 | 0 | 2 |
| 13 | 8 | 0 | 8 | 0 | 3 |
| 17 | 6 | 0 | 6 | 1 | -2 |
| 19 | 5 | 0 | 5 | 0 | 6 |
| 23 | 4 | 0 | 4 | 0 | 5 |
| 25 | 4 | 0 | 4 | 0 | 9 |
| 27 | 4 | 1 | 3 | 0 | -1323 |
| 29 | 3 | 0 | 3 | 0 | -22143 |
| 31 | 4 | 1 | 3 | 0 | 1302 |
| 32 | 3 | 0 | 3 | 0 | 7794 |
| 37 | 3 | 0 | 3 | 0 | 1 |
| 43 | 3 | 0 | 3 | 0 | 3 |

Every entry arises from the exact 31-mask polynomial above, with integer cyclic group ring Z[q]/(q^d-1) and Euclidean reduction modulo Phi_d. The coefficient at j=1 is d/dt at t=0, equivalently the logarithmic q derivative q*dR/dq at zeta_d. No floating approximations are used. The attached VERIFY_R5_M1_O1.py reconstructs all witnesses and independently checks each zero-order coefficient by a separate cyclic-factor-product algorithm and each first derivative by a product-rule prefix/suffix algorithm. Its exact output is transcribed into CERTIFICATE.json.

For rational generating functions, a primitive d-th root pole of order >=3 forces d to divide any period of the degree >=2 quasipolynomial coefficients: distinct root-of-unity exponential polynomials with such leading orders cannot be canceled by an O(N) remainder, and a period-T quasipolynomial has frequencies only at T-th roots. The lcm of the 14 listed witness orders is exactly L, giving L | M_1(O(N)). Combining with the upper bound proves equality.

## Relation to previous frontiers and observer typing

This independently proves the m=1, O(N) equality without assuming the previously reported all-m O(N^3), m=1 O(N^2) or 27/31 all-m theorems. It is a frozen scalar partition-counting result, not a native X6 dynamical theorem. The integer cyclotomic residue/first-jet carrier retains exact signed algebraic information; positive-weight BRC mass cannot substitute for cancellation in this calculation. P000 and the ACTIVE worldview are not modified.

## Validation and next question

Local Python 3 standard-library execution: PASS; all 14 root witnesses passed the separate zero-order and derivative implementations, and candidate-order enumeration/lcm assertions passed. The proof is an exact finite certificate plus a general partial-fraction argument. Independent project review: NOT_REVIEWED.

Next: classify M_m(O_m(N)) for all m>=1. This m=1 result gives the sharp possible maximum L for all fixed m, because the denominator D is common to every threshold. Determine which of the 14 primitive-root witnesses survive or vanish for different m, respecting the full three-load joint constraints.

Control at this source writing: owner request r5-20261122-0744-inventory-once-v1 has final FAILED / SOURCE_TREE_TRUNCATED. No current own authenticated Researcher/Activity binding or formal CLAIM/RUN was asserted; Activity association remains pending. The GitHub independent portable artifact records actual research provenance, not native execution authorization.
