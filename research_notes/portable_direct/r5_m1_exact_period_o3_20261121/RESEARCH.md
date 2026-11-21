# R5 — Exact least cost-quasipolynomial period at threshold m=1, remainder O(N^3)

Scientific date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_EXACT_DERIVATION / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED. This is a new independent *scalar cost observer* unit; no native X6/BRC physical-transfer claim. P000, ACTIVE worldview and frozen R5 scientific prices/event incidences remain unchanged. Predecessor correction: [real overlapping-event intersections @75d986aa](https://github.com/awdawmip/enterprise-math/blob/75d986aa23b68a7ecf9b29dc1006f0e322b35a15/research_notes/portable_direct/r5_true_intersection_audit_20261121/RESEARCH.md). Previous verified m=1 error O(N^4) period: 12,252,240. The m>=2 collapsed-union-cap proof is not reused.

## Exact statement and new factor

Let P={214,...,314}, with one nonnegative integer multiplicity a_p for each price p and cost N=sum(p a_p). Original failure events are E_i={sum_{p in S_i}a_p<m}:

- S0={214,215,216,217,218};
- S1={214,216,217,218,219,220,221};
- S2={215,216,217,218,219,220,221};
- S3={223,...,290};
- S4={296,...,312}.

Let f_m(N) count cost-N multiplicity vectors in the union of the five failure events. Let M_m(O(N^a)) be the least positive period of polynomial-in-N quasipolynomial coefficients representing f_m(N) up to an O(N^a) error as N tends to infinity with fixed m.

**Theorem, for the exact original model at m=1:**

```
M_1(O(N^3)) = 232,792,560 = 19 * 12,252,240.
```

In particular, a primitive nineteenth-root contribution of degree N^4 is present, while the only order-24 candidate at the fivefold denominator boundary cancels to degree N^3.

## Rational-function identity: genuine intersections

At m=1, an event E_i requires every a_p with p in S_i to be zero. Therefore, for a nonempty event mask I, the intersection uses *all* individual constraints exactly and its generating function is the unrestricted Euler product with the prices in U_I=union_{i in I} S_i removed.

Writing D(q)=product_{p=214}^{314}(1-q^p), inclusion-exclusion yields the exact identity

```
F_1(q) = R_1(q)/D(q),
R_1(q) = sum_{empty != I subset {0,...,4}} (-1)^(|I|+1)
                   product_{p in U_I}(1-q^p).
```

This avoids the known m>=2 erroneous replacement of multiple upper bounds by a single union-cardinality bound. Let R_A be the same seven-mask numerator for {E0,E1,E2}; let W3=product_{p in S3}(1-q^p), W4=product_{p in S4}(1-q^p). The support of the first three events is disjoint from both S3 and S4, so an independent identity is

```
R_1 = R_A + W3 + W4 - R_A*W3 - R_A*W4 - W3*W4
      + R_A*W3*W4.
```

Both identities are recomputed exactly and checked for equal truncated expansions in the attached script.

## Pole-order certificate and finite completeness

At a primitive d-th root z, D has a zero of exact order

```
k(d) = floor(314/d)-floor(213/d).
```

Let nu_d be the multiplicity of z as a root of R_1. Every primitive d-th root has the same nu_d because R_1 is an integer polynomial and Phi_d is irreducible over Q. Thus the reduced rational function F_1 has pole order p(d)=k(d)-nu_d, and a nonzero Fourier term of degree p(d)-1 if p(d)>0.

There cannot be five multiples of d in the 101 consecutive prices for d>=26: five multiples would span at least 4d>=104 > 100. Therefore only d<=25 can contribute a term of degree at least N^4.

For each d with k(d)>=5, compute R_1(z(1+t)) in the exact ring Z[z,t]/(Phi_d(z),t^6). Use binomial expansions (1-(z(1+t))^p), integer cyclic convolution modulo z^d-1, and exact remainder modulo Phi_d. The smallest t-degree with a nonzero cyclotomic coefficient gives nu_d. Every listed value is <=5, so the truncation is sufficient to determine the valuation exactly. Results:

| d | k(d) | nu_d | p(d) |
|---:|---:|---:|---:|
|1|101|5|96|
|2|51|3|48|
|3|33|1|32|
|4|25|1|24|
|5|20|1|19|
|6|17|1|16|
|7|14|1|13|
|8|13|1|12|
|9|11|1|10|
|10|10|0|10|
|11|9|0|9|
|12|9|1|8|
|13|8|0|8|
|14|7|0|7|
|15|6|0|6|
|16|6|0|6|
|17|6|0|6|
|18|6|1|5|
|19|5|0|5|
|20|5|0|5|
|22|5|0|5|
|24|5|1|4|

The other d<=25 are 21,23,25, each with k(d)<5. Thus the *complete* set with p(d)>=5 is d=1,...,20 and d=22 (not 21). Its least common multiple is 232,792,560.

For the new primitive-19 factor, the exact nonzero R_1(z) reduced to the basis (1,z,...,z^17) of Z[z]/Phi_19(z) is

```
(6,7,10,12,13,10,11,2,0,-6,-8,-18,-14,-17,-14,-14,-10,-8).
```

Because k(19)=5, its fivefold pole contributes a nonzero N^4 periodic term. For d=24, R_1(z)=0 and the first nonzero t coefficient is

```
(0,-3312,-3744,-4176,-7056,-4608,-3528,-3312)
```

in the degree-8 basis. Hence p(24)=4, so its Fourier term is absorbed by O(N^3). Recombining the exact poles of order >=6 reproduces the earlier period M_1(O(N^4))=12,252,240, an independent regression check.

Any rational generating function with these root-of-unity poles has, up to finitely supported terms, an exponential-polynomial coefficient expansion. Terms from poles of order <=4 are O(N^3). The primitive conjugate contributions of order >=5 are linearly independent exponential-polynomial sequences: a periodic-coefficient quasipolynomial that approximates f_1 to O(N^3) must carry each of their exact character orders. Conversely, the lcm of those orders permits a representation using every retained term. The displayed least common multiple is therefore both necessary and sufficient.

## Validation, provenance and next unit

The companion `VERIFY_R5_M1_O3.py` implements two distinct exact numerator constructions (31 genuine event intersections and the disjoint-group factorization), tests coefficientwise equality before cyclotomic reduction for all 22 eligible d, computes all valuations without floating point or external packages, verifies the primitive-19 and primitive-24 full vectors and reproduces the O(N^4) predecessor period. Local execution: PASS, 22/22 eligible root orders, all 22 independent-algorithm crosschecks. The companion `RESULT_R5_M1_O3.json` stores the full first nonzero cyclotomic vector for each d.

This is an author-side exact finite proof/certificate with a transparent, executable checker; independent mathematical review is NOT_REVIEWED. No official Source CLAIM/RUN/Result acceptance is claimed. The frozen scientific input remains as defined by the prior R5 commit and overlapping-event audit.

Next: classify primitive-19 coefficients for all positive integer thresholds under the *genuine* three-load intersections. At m>=2 the simple all-zero intersection identity no longer holds, so use the exact event-specific max-load kernels and derive whether nineteenth-root N^4 coefficients persist, vanish periodically or require the next Laurent order. Subsequently combine all root orders 1..25 for O_m(N^3) and make the all-threshold minimal-period statement. Preserve P000 and the scalar-observer scope.
