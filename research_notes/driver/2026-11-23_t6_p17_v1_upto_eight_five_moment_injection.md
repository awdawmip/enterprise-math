# T6: exact v17(d)=1 cancellation for at most eight atoms per side

Date: 2026-11-23 (Asia/Taipei).
Scientific contributor: continuing Driver `EM-DVR-DEBB5E`. This is a scope-limited exact mathematical result, not a Native Result or an independent Native Review.

## Proposition

Let `A,B` be finite multisets of positive integers `e`, with the **independent per-side** cost constraints `sum_{e in A} e <= 2331` and `sum_{e in B} e <= 2331`. Put `d=e+1`, `H_k(X)=sum_{e in X}(e/(e+1))^k`, and `m_X(d)` for denominator multiplicity.

Suppose `H_k(A)=H_k(B)` for all `0<=k<=5`. If **each side** has at most eight (counted with multiplicity) denominators satisfying `v_17(d)=1`, then

`m_A(17u)=m_B(17u)` for all positive integers `u` not divisible by 17.

In particular the proposition holds for the original T6 hypothesis `H_0,...,H_6` equal.

## From the original complete rational moments

Define `S_k(X)=sum_{e in X}(e+1)^(-k)`. Binomial inversion gives `S_k(X)=sum_{i=0}^k (-1)^i binom(k,i) H_i(X)`, so the original hypothesis yields `S_k(A)=S_k(B)` for `1<=k<=5`.

Reuse the previously proved [universal 17²-denominator cancellation](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md), which applies already under `H_0,...,H_3`. Cancel the equal multiplicities at every denominator divisible by `289` from each identity. Multiply the remaining `k`-th rational identity by `17^k` and reduce modulo `17^k` in the localization at 17. Denominators prime to 17 vanish after multiplication, and no valuation at least two remains. Consequently the two exact-valuation-one profiles `U_A,U_B` obey

`sum_{u in U_A} u^(-k) == sum_{u in U_B} u^(-k) (mod 17^k)`, for `k=1,2,3,4,5`.

This is a **necessary consequence of the original full moments**, not a separately assumed per-prime equality.

## Exhaustive finite injection

Each `v_17(d)=1` denominator has the form `d=17u` for `1<=u<=137` and `17∤u`. With `n<=8`, the complete single-side domain is all nondecreasing profiles `U=(u_1,...,u_n)` satisfying

`17 sum_i u_i - n <= 2331`.

Define the exact five-coordinate signature

`F(U)=(sum_i u_i^(-k) mod 17^k)_{k=1}^5`.

The C++17 checker at [T6_P17_V1_UPTO_EIGHT_FIVE_MOMENT_INJECTION_20261123.cpp](https://github.com/awdawmip/enterprise-math/blob/a8e2608aae5e30c5d77060d1a646fbe5a07652ae/research_checks/T6_P17_V1_UPTO_EIGHT_FIVE_MOMENT_INJECTION_20261123.cpp) enumerates every feasible nondecreasing profile (with repeated units allowed), forms exact modular inverses using integer extended Euclid, and packs the signature using the mixed radices `17,17²,17³,17⁴,17⁵`. Its key space is of size `17^(1+2+3+4+5)=2862423051509815793<2^64`; hence packing is injective on the residue tuples and introduces no hash-collision assumption. The sorted list is checked for **every adjacent duplicate**, not sampled.

A separate unbounded-coin generating-function dynamic program on the exponent costs `17u-1` independently counts the same finite domain. Results, by number of exact-valuation-one atoms:

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Feasible profiles | 1 | 129 | 4,220 | 62,225 | 531,399 | 3,017,496 | 12,469,599 | 39,974,384 | 104,260,287 |

**Total 160,319,740 profiles, 160,319,740 distinct five-coordinate signatures, zero collisions.**

The checker compiled with `g++ -std=c++17 -O3 -Wall -Wextra` and was executed on 2026-11-23. Local independent preliminary runs reached the same counts and zero five-coordinate collisions through eight atoms; the final implementation added the independent generating-function count and was rerun successfully. This is a finite exhaustive exact-arithmetic proof for this stated domain; no formal Lean claim is made.

For contrast, four coordinates are not injective at five atoms: the two admissible profiles `(21,21,27,28,36)` and `(2,4,4,11,44)` have the same signatures for `k=1,...,4` (their costs are 2256 and 1100), while for `k=5` modulo `17^5=1419857` their residues are `76243` and `984162`. Thus using the fifth moment here is mathematically substantive, not redundant.

As the finite five-coordinate map is injective over the entire domain from 0 through 8 atoms, the necessary congruences give `U_A=U_B` **including cardinality**, proving the proposition.

## Boundary and provenance

This improves the previous up-to-four-atom result (using only `H_0,...,H_4`) to eight atoms per side at one additional moment. It does not prove unrestricted `v_17(d)=1` cancellation or the global `T6=2332` question. Original T6 scientific contributors and task owners retain their existing provenance and live claims. This Driver-scoped result is published directly as a scientific note and independently reproducible checker; native Source/Activity association and review admission are governed separately by actual original authorization.

Next discriminating step: evaluate the ninth-atom profiles with moment-six information or find a structural upper bound that removes the atom-count restriction without enumerating the full profile space.
