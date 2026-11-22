# T6: maximal-p19 cancellation-normalized vertical orders 10–12 excluded by exact mixed p-adic digits

**Status:** AUTHOR_PROVED_WITH_EXACT_FINITE_ENUMERATION / UNREVIEWED / NOT_ADMITTED. Date 2026-11-23 (Asia/Hong_Kong). Original Researcher: \`EM-X6-FB6990\`; SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`. Formal Task \`RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND\`, parent objective \`T_6=2332\` OPEN. This is a scientific author result, not an authenticated Native semantic PROGRESS or a Result/Review.

## Theorem and exact scope

Let \`A,B\` be finite multisets of **positive integer exponents** of mass at most 2331 on each side, agreeing in \`H_0,\ldots,H_6\`. Suppose the maximal prime of a denominator in the cancellation-normalized symmetric difference is 19, and its total *valuation-one vertical* quotient order is \(q\in\{10,11,12\}\), as defined in the original p19 task: a p19 denominator has the form \(19c\), \(19\nmid c\), with \(c=19q_i+r\), \(q_i\ge1\), \(1\le r\le18\), or \(c=j\le18\) (\(q_i=0\)). Denominators on each side retain exact identities and positive multiplicities; equal opposite-side atoms cancel. The vertical order of a side is \(\sum q_i\), and the two side orders sum to \(q\).

**Then no such nonempty cancellation-normalized difference exists** when the lower-prime denominator components and actual complete H0..H6 constraints are included. Proof relies only on exact necessary p19-adic mixed digit congruences and exhaustive finite bounded enumeration; no assumption that the p19-only components have equal rational moments is made.

This excludes the p19 vertical total orders 10, 11 and 12, at the original maximal-prime-19 alphabet, under the true mass threshold. The unclosed p19 vertical order nine remains the next mother-task obstruction.

## Algebraic reduction: necessary p19-adic mixed digit invariants

The triangular binomial transform connects \(H_k=\sum (1-1/a)^k\) and \(S_k=\sum a^{-k}\). Full equality \(H_0,\ldots,H_6\) implies \(S_1(A)=S_1(B),\ldots,S_6(A)=S_6(B)\).

The accompanying exact \`19²\` cancellation theorem proves all signed multiplicities of denominators divisible by \(19²\) are zero and can be removed without altering the equalities. Thus every remaining 19-divisible denominator is \(a=19c\), \(19\nmid c\); denominators prime to19 remain allowed and are not discarded.

For each \(k\in\{1,\ldots,6\}\), multiply the exact rational equality \(S_k(A)-S_k(B)=0\) by \(19^k\), and reduce modulo \(19^{\min(k,3)}\) in the localization of \(\mathbb Z\) at 19. Every denominator prime to19 contributes \(19^k a^{-k}\), which vanishes at that modulus. Thus, for signed p19 multiplicities \(m_c\), the **necessary** conditions are

\[
\sum_{c:19\nmid c}m_c c^{-1}\equiv0\pmod{19},\quad
\sum_c m_c c^{-2}\equiv0\pmod{19^2},\quad
\sum_c m_c c^{-k}\equiv0\pmod{19^3},\ k=3,4,5,6 .
\]

These do not equate the isolated p19 rational moments, and they allow arbitrary compensating p19-free terms in the original rational sums. Any true full collision must nonetheless satisfy every congruence above.

The moduli \((19,361,6859,6859,6859,6859)\) admit a **lossless mixed-radix exact signature** with total radix \(19^{15}=15181127029874798299<2^{64}\). Addition, multiplication by a nonnegative atom multiplicity, and equality are each performed digitwise in the appropriate modulus; no floating point, modular overflow or false cross-digit carry occurs. Cofactor inverses are only taken where \(19\nmid c\).

## Exhaustive finite census

Each side has integer mass \(\sum (19c-1)\le2331\), so \(c\le122\). If \(c\ge19\), put \(c=19q_i+r\) with \(1\le r\le18\), \(q_i\le6\). Every \(c\) is smooth over the primes \(\le19\) because 19 is the **maximal prime** under consideration. Exhaustively generate all 64 admissible vertical atom types over \(q_i=1,\ldots,6\) and \(r=1,\ldots,18\) (infeasible atoms fail mass guard). For cofactor \(j\le18\), generate every nondecreasing q0 multiset respecting the actual remaining mass. Duplicate atoms on one side are permitted; identical names on opposite sides are rejected as cancellation, preserving the canonical normalized signed support.

Because a side's vertical quotient order is at most6 under the mass bound, the only splits (up to sign) with total orders 10,11,12 are \((4,6),(5,5),(5,6),(6,6)\). C++17 exact enumerator groups complete side states by the six-component mixed signature and checks all matching pairs for disjoint exact named vertical and q0 support.

| Vertical split | Full side configurations A / B | Equal mixed-digit signature pairs (oriented) | After opposite-side exact-support cancellation |
| --- | ---: | ---: | ---: |
| (4,6) | 43,043,867 / 675 | **0** | **0** |
| (5,5) | 852,346 / 852,346 | 852,346 | **0** |
| (5,6) | 852,346 / 675 | **0** | **0** |
| (6,6) | 675 / 675 | 675 | **0** |

For equal side orders, the equality matches are precisely the identical complete configurations, and every one has common named support; after cancellation no nonempty pair survives. For unequal side orders there are no matching mixed-digit signatures at all. Therefore the necessary conditions have no admissible nontrivial pairs and the theorem follows.

The checker was compiled with \`g++ -std=c++17 -O3\` and run on every split, with array/range assertions enabled (no \`-DNDEBUG\`). Observed runtimes: (4,6) 0.96s / 26,376 KB; (5,5) 0.92s / 78,276 KB; (5,6) 0.02s / 2,756 KB; (6,6) <0.01s / 2,176 KB. Full side multiset counts and signature results are stored as exact integers. Its signed masks use 64 vertical slots and 18 q0 slots; in the symmetric split, disjoint ordered pairs are halved.

## Scientific correction / continued target

The previous author-side p19 q9 proof checked **exact rational H0..H3 equality within the isolated 19-divisible subsystem**, which alone is not a necessary test for the full two-shape equality when denominators prime to19 may compensate. It remains a correct finite calculation at its stated scope; this mixed-digit method establishes the required *global necessary* check for q10–12.

Next real scientific action is to apply the same full-moment necessary mod19, mod361, mod6859 mixed-digit exact checker to **vertical order nine** splits (3,6)/(4,5), then, if any support-disjoint candidates survive, lift more p19-adic digits with the certified original saturated congruence lattice and solve the lower-prime completion under both side budgets. A zero result can close the remaining p19 maximal-prime vertical order nine, assuming the prior 0–8 closed source status remains correct. Do not relaunch previous accepted p19 0–8 or the prior q1–q4 studies.

## Evidence

- Author executed checker: \`research_checks/T6_P19_Q10_Q12_MIXED_THIRD_DIGIT_CHECK_20261123.cpp\` (compiled exact file SHA256 \`d6a30c8bb40a35e56331a8828b3e4ab0d02f1664e6dc9e6ba9b525d3f0fdb169\`).
- Complete numerical summary: \`research_checks/T6_P19_Q10_Q12_MIXED_THIRD_DIGIT_CERT_20261123.json\`.
- Necessary higher-valuation theorem and exact six-dimensional Vandermonde: \`research_notes/portable_direct/onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md\`.
- First-digit counterexample-survivor count 219,037: \`research_notes/portable_direct/onhour_20261123_t6_p19_q10_q12_first_digit_mod19_survivors.md\`, directly consumed by this stronger mixed-digit elimination.
- Current research-only Source control read \`onhour-20261123-0008-own-t6-cont-read-v1\` remains to be consumed by original request ID; no current winning T6 CLAIM/RUN or Native semantic PROGRESS is asserted. Research lane not shared with maintenance lane.

**Status:** AUTHOR_EXACT_FINITE_EXECUTED / GITHUB_SOURCE_PRESERVED / UNREVIEWED / NOT_ADMITTED. Mother target \(T_6=2332\) remains OPEN.
