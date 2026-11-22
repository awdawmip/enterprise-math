# T6 one-power p17 q13 (6,7), zero-q0: unique H0–H2 alias and H3 separation

2026-11-22 · portable TASK_RESEARCH author evidence · original Research logical lane \`chatgpt-research-onhour-enterprise-math-20260923\` · researcher \`EM-X6-FB6990\` · original SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`.

**Status:** \`AUTHOR_EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED\`. This note is a bounded new mathematical unit, not an authorized current T6 CLAIM, an accepted Result, or a global T6 proof.

## Frozen mathematical carrier and new subcase

The mother task is \`RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND\`, with target \`T_6=2332\` or a cheaper exact six-moment collision. Use the same one-power maximal-p17 named-cofactor carrier and signed side mass bound from the predecessor's [q14 split(7,7) preflight](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md).

An admissible vertical atom is the **named** pair (q,r), q≥1, 1≤r≤16, with 17-smooth cofactor a=17q+r, actual denominator d=17a, exponent mass d−1=289q+17r−1. Same-sign multiplicities count separately, and identical named atoms may not appear on opposite signs after cancellation.

Here the vertical orders are q+=6 and q−=7, the total order is 13, **no q0 atoms are permitted**, and both masses are ≤2331. This is a precisely scoped adjacent case, not a claim covering all q13 or all p17.

## Theorem: one and only one zero-q0 H0/H1/H2 alias (up to side swap)

For shapes with all the declared constraints, the number of signed pairs satisfying H0,H1,H2 equality is **exactly one**, up to global sign exchange:

| | q=6 side (+) | q=7 side (−) |
|---|---|---|
| Cofactors a | (21,30,84) | (20,35,70) |
| Actual denominators d=17a | (357,510,1428) | (340,595,1190) |
| Exponents e=d−1 | (356,509,1427) | (339,594,1189) |
| Vertical order | 6 | 7 |
| Exact side mass | 2292 | 2122 |
| Number of terms | 3 | 3 |

The cofactor identities are

\[
\sum_{a\in A}\frac1a=\sum_{b\in B}\frac1b=\frac{13}{140},\qquad
\sum_{a\in A}\frac1{a^2}=\sum_{b\in B}\frac1{b^2}=\frac{69}{19600}.
\]

For the original shape observer \`H_k = Σ (e/(e+1))^k\`, this proves H0,H1,H2 equality exactly. However

\[
\sum_{a\in A}a^{-3}-\sum_{b\in B}b^{-3}=-\frac1{220500},\qquad
\boxed{H_3(A)-H_3(B)=+\frac1{1\,083\,316\,500}}.
\]

The H3 difference is an exact positive rational, not numerical noise. This example **does not** satisfy the T6 H0–H6 collision requirement.

An algebraic explanation for the third-moment defect uses Newton's identities: for the three cofactor reciprocals x_i=1/a_i, equal p1 and p2 imply equal elementary symmetric e1 and e2=1/392. Their e3 differ, because the cofactor products are 52,920 and 49,000; therefore p3(A)−p3(B)=3(1/52920−1/49000)=−1/220500. The 17³ denominator scaling gives the displayed H3 defect.

## Why the finite classification is exhaustive

The two allowed vertical orders constrain every named atom to q≤6 and q≤7 respectively. Enumerate all admissible pairs (q,r) with 17-smooth 17q+r, then every nondecreasing repeated-atom roster whose q sum is exactly its side's order and mass is at most 2331. The first enumerator uses monotone atom-index DFS. A different integer-partition / combinations-with-replacement implementation generates identical full multiset keys; this is an independent **algorithmic crosscheck by the same author**, not an independent mathematical reviewer.

| Exhaustive stage | Exact count |
|---|---:|
| Allowed named atoms for q≤6 / q≤7 | 52 / 60 |
| Admissible full side rosters, q6 / q7 | 11,105 / 1,907 |
| Signed pairs with equal H0 and H1 before opposite support cancellation | 2,425 |
| Of those, disjoint opposing named support | 375 |
| Of those, additionally equal H2 | **1** |

Under equal H0, equality of H1 is equality of the first reciprocal sums. Under equal H0,H1, equality of H2 is equality of the second reciprocal sums. All tests use \`fractions.Fraction\` and exact integer masks. No cofactor support, same-side repetition, budget or observer moment was silently compressed away. The checker also recalculates H0 through H6 from the actual denominators.

Immutable artifacts:
- [Executable exact checker](https://github.com/awdawmip/enterprise-math/blob/40cedcd9a97236634e776e5e688c51c1cc5d0f96/research_checks/T6_P17_Q13_SPLIT6_7_ZERO_Q0_H012_CHECK_20261122.py)
- [Full integer/rational certificate](https://github.com/awdawmip/enterprise-math/blob/622eef23ca6a8d74619317ef651ba52bf31f6d3d/research_checks/T6_P17_Q13_SPLIT6_7_ZERO_Q0_H012_CERT_20261122.json)

## Implication and real next scientific action

The earlier q14 split(7,7) one-power H0/H1/H2 emptiness does **not** extend verbatim to q13(6,7): there is exactly one small zero-q0 three-moment alias, and the next observer H3 resolves it. This illustrates a residual preserved by the higher observer in the original discrete shape carrier.

The remaining q13 class with **nonempty q0**, other p17 valuation classes and mixed congruences still require their own analysis. A bounded next discrimination is to extend the q13 (6,7) exact H0/H1 keyed roster with all admissible q0 side multisets at the real per-side residual budgets, then check H2/H3 and named support. Use a finite resource cap and preserve any partial enumeration as partial; do not manufacture q13 EMPTY from the zero-q0 slice.

Control continuity: original receipt \`onhour-20261122-1959-t6-own-current-continuation-v1\` has succeeded as an as-of read. The newly requested T6 current Task read \`onhour-20261122-2100-t6-current-task-v1\` was still RUNNING at latest observation. The prior typed-prepare failures are terminal and were not replayed. A live winning T6 CLAIM/RUN and protected semantic PROGRESS were not verified in this research unit.
