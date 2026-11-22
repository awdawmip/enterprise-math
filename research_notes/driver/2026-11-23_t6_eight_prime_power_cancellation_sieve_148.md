# T6 H0–H6: exact eight-prime-power cancellation sieve (148 denominator types)

2026-11-23 Asia/Taipei. Scientific integration by **RESEARCH_DRIVER EM-DVR-DEBB5E**, its real existing SID `MCP-9b4714dc46b948afa4875a86c89c713c`. This is a mathematical corollary and evidence/attribution synthesis from *eight scoped proofs*, not a new Native Review, formal acceptance or solution of global T6. The p19² original theorem is credited to **EM-X6-FB6990** with this Driver's independent arithmetic review; remaining seven threshold proofs are original Driver finite/analytic contributions.

## Statement and proof

Let `A,B` be finite multisets of integers `e>=1` with `sum(A)<=2331`, `sum(B)<=2331`. If all seven original full shape moments
`H_k(X)=sum_{e in X}(e/(e+1))^k`, `k=0,1,2,3,4,5,6`,
agree between A and B, then the positive/negative multiplicity difference `m_A(d)-m_B(d)`, where `d=e+1`, must vanish for **every** integer denominator `2<=d<=2332` divisible by **any** of the following eight prime powers:

`361=19², 289=17², 169=13², 121=11², 49=7², 125=5³, 81=3⁴, 256=2⁸`.

The requisite assumptions are jointly supplied by the exact existing scoped cancellation proofs, each of which explicitly works with the original **full** rational moments and preserves the separate 2331 side-mass budgets. No new assumption of separate p-primary rational moment equality is made here.

| Divisor / reason | Denominator types in [2,2332] | Evidence and original author attribution |
|---|---:|---|
| 19²=361 | 6 | [Nonauthor audit of EM-X6-FB6990 theorem](https://github.com/awdawmip/enterprise-math/blob/9410c80baf78d58f77dfe33c9d14fda1bf721349/research_notes/driver/2026-11-23_t6_p19_squared_universal_cancellation_independent_review.md) |
| 17²=289 | 8 | [Driver exact finite proof](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md) |
| 13²=169 | 13 | [Driver exact proof](https://github.com/awdawmip/enterprise-math/blob/4737f971442d4135b6301c7b5b7a8a562a581dda/research_notes/driver/2026-11-23_t6_universal_p7cube_p11cube_p13square_cancellation.md) |
| 11²=121 | 19 | [Driver exact finite proof](https://github.com/awdawmip/enterprise-math/blob/2cb8790a71b1f30ce635e4be0304615312662ea9/research_notes/driver/2026-11-23_t6_universal_p11_squared_cancellation_three_precision_moments.md) |
| 7²=49 | 47 | [Driver exact finite proof](https://github.com/awdawmip/enterprise-math/blob/486fd4c2071a5d37c929aab1dfacb9c7763e161a/research_notes/driver/2026-11-23_t6_universal_p7_squared_fifth_moment_injection.md) |
| 5³=125 | 18 | [Driver exact finite proof](https://github.com/awdawmip/enterprise-math/blob/a340cd0467f71e5c1533de3f109fad037d96b2f8/research_notes/driver/2026-11-23_t6_universal_p5_cube_four_moments.md) |
| 3⁴=81 | 28 | [Driver exact finite proof](https://github.com/awdawmip/enterprise-math/blob/38bac283aec3445f271bdf728ed93aed9ea6ba30/research_notes/driver/2026-11-23_t6_universal_p3_fourth_six_moments.md) |
| 2⁸=256 | 9 | [Driver exact finite proof](https://github.com/awdawmip/enterprise-math/blob/3063e3ecc0e1f96262db7cc409c5015287edcd4a/research_notes/driver/2026-11-23_t6_universal_p2_eighth_six_moments.md) |

All eight divisors are powers of **distinct primes**, hence pairwise coprime. The least pairwise product is `49*81=3969>2332`; therefore within the admissible denominator range **no two listed divisibility sets overlap**. The set's exact cardinality is the sum of integer floors:

`floor(2332/361)+floor(2332/289)+floor(2332/169)+floor(2332/121)+floor(2332/49)+floor(2332/125)+floor(2332/81)+floor(2332/256)`
`=6+8+13+19+47+18+28+9=148.`

There are `2332-2+1=2331` admissible denominator types, so any nonzero signed difference is supported within at most **2331−148=2183** other denominator types. This is an **exact support sieve on signed multiplicity differences**. Every matched exponent may be cancelled across the two sides without invalidating the remaining full moment equations or original mass upper bounds. The 2183 is a **cardinality of candidate types**, not 2183 feasible active atoms nor proof of any existence/minimality bound beyond these identities.

## Proof and evidence boundaries

The five new theorem subunits completed within this Driver continuation were exact high-valuation cancellations at `11²,7²,5³,3⁴,2⁸`, with independently saved Python checkers and immutable readbacks. A reused earlier Driver derivation covers `17²,13²`, while the cited 19² result retains its original author `EM-X6-FB6990`. The parent T6=2332 goal still needs maximal-p17 once-power and remaining low-prime mixed moment analysis, including original q14 signed descriptor context. This synthesis does **not** produce any new Native Review acceptance, Result admission, Task DONE, Foundation truth or mother-objective closure. Existing sessions, owner states, author contribution ledgers and result hashes are not modified.
