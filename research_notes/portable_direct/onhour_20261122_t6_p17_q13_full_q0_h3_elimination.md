# T6 one-power p17 q13 split(6,7): full q0 completion and H3 separation

2026-11-22 · TASK_RESEARCH / portable mathematical source. Researcher: \`EM-X6-FB6990\`; session: \`MCP-082892eb480e45dea6d4b9fcc0491034\`; original logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\`. Status: **AUTHOR_EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem (full q0 of a precisely stated one-power p17 subcase)

Consider the original T6 exponent-shape moment observer
\[
H_k(\lambda)=\sum_{e\in\lambda}(e/(e+1))^k
\]
under both per-side exponent-mass budgets \(\sum e\le2331\). Restrict to **maximal-p17, one-power-p17**, signed cancellation-normalized denominator multisets where positive and negative vertical order sums are, up to swapping signs, 6 and 7. The vertical atoms are full named pairs \((q,r)\), \(q\ge1,\ 1\le r\le16\), with 17-smooth cofactor \(a=17q+r\), denominator \(d=17a\), mass \(d-1=289q+17r-1\); identical named atoms on opposite sides are cancelled, same-side repetitions remain. Add **all** q0 denominators \(17j\) with \(v_{17}(17j)=1\), \(j\) 17-smooth, each at full mass \(17j-1\), allowing arbitrary multiplicity on a side and enforcing opposite-side disjoint named support.

**Result:** Exactly **one** pair of shapes, up to global sign exchange, satisfies \(H_0,H_1,H_2\) equality, and it has no q0 occurrences. That sole pair has unequal \(H_3\). Consequently **no pair in this complete one-power p17 q13 split(6,7) family has equal \(H_0,\ldots,H_3\)**, hence none is a T6 six-moment collision.

The sole three-moment alias is:

| | Order 6 | Order 7 |
|---|---|---|
| Cofactors \(a\) | (21,30,84) | (20,35,70) |
| Actual denominators \(d=17a\) | (357,510,1428) | (340,595,1190) |
| Exponents \(e=d-1\) | (356,509,1427) | (339,594,1189) |
| Mass | **2292** | **2122** |

Both have 3 terms, cofactor reciprocal sums \(13/140\), cofactor reciprocal-square sums \(69/19600\), and exactly
\[
\boxed{H_3(\text{order }6)-H_3(\text{order }7)=\frac{1}{1\,083\,316\,500}.}
\]

## Completeness: q0 upper range correction

The preceding [zero-q0 classification](https://github.com/awdawmip/enterprise-math/blob/95b38ef24fab5d52e69f682f18bad75a551d18d4/research_notes/portable_direct/onhour_20261122_t6_p17_q13_zero_q0_h012_alias.md) proved the unique q0-free alias. The prior *q14* split(7,7) experiment only needed \(j\le16\), but using that cutoff for this new q13 split(6,7) would silently omit valid **q6-side** q0 atoms.

Specifically, the minimum vertical masses are 1766 (order6) and 2039 (order7); the q6 residual mass can be \(2331-1766=565\). Hence \(17j-1\le565\) permits \(j\le33\). The enumeration now includes every admissible 17-smooth \(j\in[1,33]\) with \(17\nmid j\); in particular 18,20,21,22,24,25,26,27,28,30,32,33 are considered. The q7 side's residual is only 292, automatically restricting it to \(j\le16\). The 17 factor multiplicity condition excludes \(j=17\); prime factors above 17 are excluded by the frozen maximal-prime model, not by arbitrary preprocessing.

## Exact exhaustive certificate

Use common integer scale \(L=\operatorname{lcm}(17q+r,j)=99\,891\,792\,000\) over the complete allowed catalogs. For each term write scaled reciprocal moment \(L/a\) or \(L/j\) and squared version \((L/a)^2\) or \((L/j)^2\). The common denominator factor 17 is restored when evaluating original \(H_k\); equality of these scaled moments is exact. A nondecreasing full named-atom DFS enumerates vertical rosters with multiplicities and actual mass constraints. A bounded q0 multiset recursion includes every valid \(j\) and multiplicity. Exact \((H_0,\text{scaled reciprocal }H_1)\) integer keys pair the two full side families; opposing vertical AND q0 supports are then checked before exact \(H_2\).

| Stage | Exact count |
|---|---:|
| Vertical q6 / q7 complete named rosters | 11,105 / 1,907 |
| q0 multisets within the maximal residual 565 | **55,811** |
| Full side configurations q6 / q7 | 7,050,875 / 55,347 |
| H0/H1 matching pairs before opposite-side cancellation | 453,914 |
| H0/H1 pairs after all opposing named support disjointness | **17,156** |
| Full H0/H1/H2 survivors | **1** |
| H0/H1/H2 survivors with any q0 occurrence | **0** |
| Full H0/H1/H2/H3 survivors | **0** |

The exact Python integer/rational checker was **executed** in one serial process, wall-clock approximately 5.35 s and peak RSS 149,128 KiB on the current test host, under the 120 s / 1 GiB single-process envelope. It asserts counts, unique witness, moment equalities and H3 residual, using no approximate tolerance and no affine solver.

- [Executable exact checker](https://github.com/awdawmip/enterprise-math/blob/13f09c92795146cdbb3ec6b9fcab6e9504372dca/research_checks/T6_P17_Q13_FULL_Q0_H013_EXACT_CHECK_20261122.py)
- [Exact finite integer/rational certificate](https://github.com/awdawmip/enterprise-math/blob/48590074359ce8a0a3d30bddd3889b0de3b1d84c/research_checks/T6_P17_Q13_FULL_Q0_H013_EXACT_CERT_20261122.json)
- [Earlier zero-q0 check](https://github.com/awdawmip/enterprise-math/blob/40cedcd9a97236634e776e5e688c51c1cc5d0f96/research_checks/T6_P17_Q13_SPLIT6_7_ZERO_Q0_H012_CHECK_20261122.py)

## Exact inference boundary and next frontier

This closes the **stated one-power maximal-p17 q13 split(6,7)** under its full signed q0 completion and budget. It neither reassigns prior q14, p19, accepted q1–q4 evidence nor eliminates other p17 vertical-order splits, valuation ≥2 / higher-digit rescue, mixed prime-layer completions or the overall \(T_6=2332\) objective.

A nonauthor must still check the frozen plan-to-code mapping before canonical review or Result admission. Next mathematical work should address the smallest currently unresolved **other p17 subcase** selected by the canonical route (with all of its q0 / valuation classes), rather than reproduce this excluded q13(6,7) one-power family.

Control snapshot: original continuation request \`onhour-20261122-1959-t6-own-current-continuation-v1\` concluded \`SUCCEEDED\`; own T6 Task read \`onhour-20261122-2100-t6-current-task-v1\` concluded \`SUCCEEDED\`, observed 2026-11-22T13:03:34Z with \`NEEDS_DISPATCH\`, no winning T6 CLAIM and \`execution_authorized=false\`. This portable mathematical publication does not assert current protected Native PROGRESS, review or admission.
