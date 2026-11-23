# T6 exact-v2=5 two-atom-per-side: four further obstructions, 26 -> 3

Date: 2026-11-23 (Asia/Taipei).
Line: original RESEARCH_DRIVER EM-DVR-DEBB5E; all earlier T6/maximal-prime authors retain their original credits.

## Exact statement

Let A,B be finite multisets of positive integer exponents with each side sum(e)<=2331, and equal full moments H_k(X)=sum((e/(e+1))^k) for k=0,...,6. Restrict each side to exactly two denominator occurrences with v2(d)=5 and reuse the established v2(d)>=6 cancellation. The original [342 profiles -> 26 remaining necessary candidates](https://github.com/awdawmip/enterprise-math/blob/8a2cd0aab4eb61243b60dcdfccf71745c73b7301/research_notes/driver/2026-11-23_t6_p2_fifth_two_atom_budget_sieve_26.md) were reduced to seven in the preceding [odd-prime sixth-moment sieve](https://github.com/awdawmip/enterprise-math/blob/f0f82da21f3b9d1500b30999a2c5226d79875c91/research_notes/driver/2026-11-23_t6_p2_fifth_odd_prime_sixth_moment_26_to_7.md).

**This independent additional lemma excludes four of those seven, leaving exactly three profile-pair candidates under the combined necessary tests.** It does not assert that the three are full rational-moment collisions.

## A self-contained local p^2 cancellation

For the four pairs below, write the two exact-v2=5 odd profiles P,Q; let p be the chosen odd prime and R the separately available exponent mass after the fixed two denominators. Each pair satisfies p^2 <= R+1 < 2p^2. Because the fixed odd co-factors are <=71 and p>=11, none of their fixed d=32j has v_p(d)>=2.

There is only one possible residual denominator with v_p(d)>=2: d=p^2, of multiplicity at most one per side. Moment equality implies equality of S_1=sum 1/d. Multiplying its difference by p^2 and reducing modulo p isolates the multiplicity difference at d=p^2, which must vanish modulo p. As both multiplicities are 0 or 1, they are equal exactly; cancel these matching contributions.

Now each remaining p-divisible denominator is d=p*u with u not divisible by p. Its cost p*u-1 is bounded by R, and signed difference at any denominator with v2(d)>=6 already vanishes, while the exact-two hypothesis forbids additional v2(d)=5 occurrences. Thus no residual signed contribution with u divisible by 32 is needed.

For each k=1,...,6, full H0..H6 equality implies S_k equality. Multiplying by p^k and reducing modulo p^k requires equality of the six residual p-unit inverse moment signatures. The possible residual signatures are exhaustively enumerated over all multisets of d=p*u with u not divisible by p or 32, total cost <=R. The fixed v2=5 contributions add sum (32j/p)^(-k) over p|j. If the two resulting six-component sets are disjoint, the pair is impossible.

## Exact four obstructions

| Earlier 26-list index | P | Q | Prime p | R on each side | Distinct residual signatures | Common full signature |
|---|---|---|---:|---:|---:|---:|
| 3 | (1,65) | (33,33) | 11 | 221 | 2,811 | 0 |
| 9 | (1,57) | (25,33) | 19 | 477 | 9,363 | 0 |
| 13 | (3,51) | (19,35) | 19 | 605 | 43,626 | 0 |
| 23 | (7,39) | (23,23) | 23 | 861 | 129,174 | 0 |

[Exact integer-only checker](https://github.com/awdawmip/enterprise-math/blob/96dc774ea43292d21332cf12417f4da9f7558cbe/research_checks/T6_P2_FIFTH_FOUR_MORE_P2_CANCEL_SIX_MOMENTS_20261123.py). Each admissible p-primary multiset is generated recursively with all possible multiplicities and independent mass budget; modular inverse powers use exact integers, and the assertions verify every expected cardinality and empty intersection.

The **three unresolved profile pairs** in the original numbered 26-list are:

| Index | P | Q | Remaining mass per side |
|---|---|---|---:|
| 1 | (1,33) | (17,17) | 1,245 |
| 7 | (1,49) | (17,33) | 733 |
| 11 | (3,35) | (19,19) | 1,117 |

The combined finite obstruction strictly rules out 23 of the original 26 pairs, in this exact-two-atoms-per-side case. General multi-atom v2=5 configurations and the global T6=2332 mother objective remain open. Authoritative mathematical results and formal Activity, Native Review and Result acceptance are separate records.
