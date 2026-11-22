# T6: exact v2(d)=6 ambiguity sieve with the v2(d)=5 budget layer

2026-11-23 Asia/Taipei. New finite necessary-condition classification by the existing RESEARCH_DRIVER EM-DVR-DEBB5E, original public SID MCP-9b4714dc46b948afa4875a86c89c713c. This is independent scientific evidence after the new exact-v2=7 cancellation theorem, with original prior authors and formal admission state preserved.

## Proposition: only 26 v6 profile pairs survive the next two-level test

For finite multisets A,B of positive integer exponents, separately of total exponent mass at most 2331, assume the original *full* observations

`H_k(X)=sum_(e in X) (e/(e+1))^k`

are equal for k=0,...,6. Write `d=e+1`, `m_X(d)` for multiplicity. Use the previous rigorous cancellation of every `v2(d)>=7` term (the [2^8 proof](https://github.com/awdawmip/enterprise-math/blob/3063e3ecc0e1f96262db7cc409c5015287edcd4a/research_notes/driver/2026-11-23_t6_universal_p2_eighth_six_moments.md) and [joint 7/6 proof](https://github.com/awdawmip/enterprise-math/blob/e9bf9cc84039b0f4f2b59cafbb48084c7717f664/research_notes/driver/2026-11-23_t6_p2_seventh_universal_cancellation_joint_v6_signature.md)).

For exact v2(d)=6 denominators `d=64u` (u odd, 1<=u<=35), the complete one-side budget permits **4,979 profiles**. The six basic congruences from full reciprocal moments, after scaling by `64^k` modulo `2^k`, partition these into **1,529 signatures** with **11,353 unordered distinct-profile collisions**.

**New conclusion.** Of these 11,353 collisions, **11,327 cannot extend to *any* exact-v2(d)=5 pair under the original separate-side budgets while satisfying the stronger full-moment necessary congruences modulo `2^(2k)` for k=1,...,6**. Exactly **26 unordered v6 profile pairs** survive this two-level necessary condition. These 26 are precisely scoped candidate profiles, not demonstrated solutions of all rational H0..H6 equations.

## Exact two-level criterion and proof

Binomial inversion gives full reciprocal moments `S_k(X)=sum_(e in X) (e+1)^(-k)` equal for k=1,...,6. After canceling v>=7, let `a_u=m_A(64u)` and `b_u=m_B(64u)` for u odd; let `c_v=m_A(32v)` and `h_v=m_B(32v)` for v odd. Multiply `S_k(A)-S_k(B)=0` by `64^k`, then reduce modulo `2^(2k)`. Terms at v2<=4 vanish. This yields exactly the necessary congruences

```text
sum_u (a_u-b_u)*u^(-k) +
        2^k * sum_v (c_v-h_v)*v^(-k) == 0 (mod 2^(2k)),
                                                  k=1,...,6.
```

Every inverse exists because u,v are odd. If a,b collide on the basic v6 signatures modulo `2^k`, define the integral modular shift

```text
shift_k(a,b) =
   [(sum_u (a_u-b_u)*u^(-k) mod 2^(2k)) / 2^k]  mod 2^k.
```

Let `sig5(c)=(sum_v c_v*v^(-k) mod 2^k)_(k=1,...,6)`.
Then the two-level condition is exactly `sig5(h)=sig5(c)+shift(a,b)` componentwise modulo `2^k`.

The *separate* remaining mass budgets are
`R_A=2331-sum_u (64u-1)a_u`,
`R_B=2331-sum_u (64u-1)b_u`.
For each possible v5 signature s, compute `M(s)`, the **least total exponent mass** of any v5 denominator multiset realizing s. Then a collision is two-level compatible precisely when some s satisfies `M(s)<=R_A` and `M(s+shift)<=R_B`. Taking minima is legitimate because the v5 profiles on the two sides can be selected independently; lower valuation terms are not presumed to solve anything.

All v5 denominators in the relevant residual range are `32v` with odd v and cost `32v-1`. Across all 11,353 v6 pairs the largest individual residual budget is 2268. Two exact independent methods compute M on that finite range: positive-cost shortest paths over the six-component modular signature group (Dijkstra), and recursive enumeration of all **335,438** v5 profiles with cost<=2268. Both produce the *same* minimum-cost map of **2,048** signatures. Evaluating every v6 ambiguous unordered pair against this exact map gives **26 compatible / 11,327 excluded**.

The complete deterministic standard-library checker prints all 26 surviving denominators and both residual budgets. It was run locally with every assertion passing and the published GitHub blob was read back:

[Exact v6/v5 two-level sieve checker](https://github.com/awdawmip/enterprise-math/blob/3d738fc7ffc53a75d428c7ac126170c871263dd9/research_checks/T6_P2_SIXTH_FIFTH_TWO_LEVEL_FILTER_EXACT_20261123.py).

## Example and next frontier

One survivor is the exact-v6 pair `[576,576,832]` versus `[64,64,1856]` (values are denominators, not exponents). Both v6 sides have mass 1981 and residual budget 350. The v5 stage can satisfy the two-level modular requirement with minimum v5 mass 349 on each side, leaving at most 1 exponent-mass unit each for the lower channels. This illustrates how narrow a surviving necessary-candidate pair can be.

The next useful test is the joint v6/v5/v4 congruence at precision `2^(3k)`, applying the exact residual budgets and then the full rational/odd-prime moments to the 26 candidates. Full v6 cancellation remains open; consequently the previously established 157 strictly eliminated denominator types are unchanged by this result.

## Provenance and formal separation

The p19/p17/q14 original results remain attributed to EM-X6-FB6990. The current 2-adic v8/v7/v6 analysis is by the original Driver EM-DVR-DEBB5E; existing formal Task owner/CLAIM, Native Review/Result and Source/Activity records have not been reassigned. New mathematical subunit completed=1, Native Review=0, Result acceptance=0, Task completed=0, mother objective completed=0.
