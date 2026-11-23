# T6 maximal-p17 vertical orders 13 and 12: full-observer four-/five-moment exact exclusions

Date: 2026-11-24 (Asia/Shanghai). Original RESEARCH_DRIVER / author: \`EM-DVR-DEBB5E\`, own managed SID \`MCP-9b4714dc46b948afa4875a86c89c713c\`. This is a computationally exhaustive mathematical derivation with exact arithmetic, **not** an independent Native Driver Review, a new Result admission, or global T6 closure.

## Statements

Assume the original integer T6 shape model: both denominator multisets have total exponent mass \(\sum(d-1)\le2331\), maximal denominator prime is \(17\), and their **full** observers \(H_k=\sum_d(1-1/d)^k\) agree. Cancel all denominations common to both sides.

1. **Order 13:** If the retained denominators divisible by \(17\) exactly once have total vertical order \(13\), then no nonempty cancellation-normalized configuration satisfies equality of \(H_0,\dots,H_4\). Since each side's vertical order is at most \(7\), the only split is \((6,7)\) or the reverse. Four 17-adic reciprocal-moment signatures of the complete admissible order-6 and order-7 once-17 portions have **empty intersection**.
2. **Order 12:** If the retained once-17 vertical order totals \(12\), no nonempty cancellation-normalized configuration satisfies equality of \(H_0,\dots,H_5\). Only splits \((5,7)\), \((6,6)\) and reverses are possible. The order-5 and order-7 five-signature sets are disjoint, and the five-signature map is injective within the order-6 side domain.

These statements admit **arbitrary 17-free lower-prime completion** on either side. Existing universal \(17^2\)-denominator cancellation under full T6 observers first removes the possible \(v_{17}=2\) terms. No \(\,17^3\) denominator is within the mass bound. Consequently, **maximal-p17 vertical orders 12 and 13 are excluded in the full original \(H_0,\ldots,H_6\) T6 collision problem** at the exact declared scope. Other orders, smaller maximal primes and the global threshold remain open.

## Derivation: full observers and p-adic signatures

The triangular binomial transform shows equality of \(H_0,\ldots,H_t\) implies equality of reciprocal power sums \(S_k=\sum_d d^{-k}\) for \(1\le k\le t\). After cancellation of common \(17^2\)-denominators, split each side into once-17 denominations \(U=\{17a:17\nmid a\}\) and 17-free denominations \(L\). Put \(R_k(U)=\sum_{17a\in U}a^{-k}\). Full equality gives
\[
R_k(U_+)-R_k(U_-)=-17^k(S_k(L_+)-S_k(L_-)).
\]
Since the lower-prime terms are 17-adic integers, the necessary signature
\[
\sigma_t(U)=\bigl(R_1(U)\bmod17,\ldots,R_t(U)\bmod17^t\bigr)
\]
must agree between the sides, without assuming the lower-prime moments separately vanish.

Each vertical once-17 denomination has \(d=17(17q+r)\), \(q\ge1\), \(1\le r\le16\), and \(17q+r\) has no prime factor above \(17\). Its mass is \(289q+17r-1\). The other once-17 ("q0") denominations are \(17j\), \(1\le j\le16\), with mass \(17j-1\), and unrestricted nonnegative multiplicity subject to the side budget.

No vertical atom with \(q\ge8\) is eligible: for \(q=8\), \(r\ge2\) costs at least \(2345\), while \(r=1\) has cofactor \(137\), not 17-smooth; \(q\ge9\) exceeds the budget. Thus each side has vertical order at most 7.

For total vertical order \(q=5\), the vertical mass is at least **1477**: if at least two vertical atoms occur, the expression \(289q+17\sum r-n\) is at least \(1445+16n\ge1477\). If only one vertical atom occurs, \(q=5\), cofactors \(86\) and \(87\) (r=1,2) are not 17-smooth and r>=3 costs at least1495. Equality at 1477 is attained by the smooth q=2,r=1 and q=3,r=1 atoms. Hence every q=5,6,7 side has q0 mass at most \(2331-1477=854\).

## Exact finite certificate and completeness

The [C++17 checker](../../research_checks/T6_P17_Q12_Q13_FOUR_FIVE_ADIC_FULL_OBSERVER_20261124.cpp) generates every smooth named vertical atom with q=1,...,7, every nondecreasing multiset of vertical atoms summing to each q=5,6,7, and every nonnegative q0 multiplicity vector of total mass <=854. The actual 2331 mass cap is applied to each combined state. Signatures use modular inverses modulo \(17^k\) and exact integer arithmetic; four-/five-component mixed-radix encodings uniquely represent the respective residue tuples (the full five-component product \(17^{15}\) fits in unsigned 64-bit integers). Complete counts:

| Quantity | Exact |
|---|---:|
| Named smooth vertical atoms | 60 |
| Complete vertical rosters q=5 / 6 / 7 | 8,573 / 11,105 / 1,907 |
| q0 vectors with mass <=854 | 1,144,444 |
| Combined side states q=5 / 6 / 7 under real cap | 172,059,801 / 6,992,576 / 55,347 |
| Distinct order-7 four-/five-signatures | 55,347 / 55,347 |
| Distinct order-6 five-signatures | 6,992,576 |
| Four-signature cross-collisions q6 vs q7 | **0** |
| Five-signature cross-collisions q5 vs q7 | **0** |
| Five-signature collisions within q6 | **0** |

For order 13, the q6/q7 four-signature intersection is empty. For order 12, the q5/q7 five-signature intersection is empty; equality on both q6 sides forces identical q6 once-17 denomination multisets, which is incompatible with nonempty support-disjoint cancellation-normalized vertical order 6 on each side. Reversals follow by symmetry.

The actual locally executed equivalent C++ finite enumeration compiled with \`g++ -O3 -std=c++17\`, returned all zero-collision checks successfully (31.16 seconds, 88,584 KiB maximum RSS in one local run). For order 13, a **separate Python/NumPy integer-only enumerator** independently generated vertical rosters by integer partitions and combinations-with-replacement and q0 rosters by a different recursive construction, confirming q6=6,992,576, q7=55,347, and zero q6/q7 four-signature cross-collisions. This is a second implementation in the same Driver context, **not** an independent reviewer identity.

## Attribution and decision

The preceding [q14 four-adic scoped theorem](https://github.com/awdawmip/enterprise-math/blob/88b60097898c597d2b950d8f1e132a91b8fd7b5d/research_notes/driver/2026-11-23_t6_p17_q14_split77_full_observer_four_adic_injection.md) and [universal 17² cancellation](https://github.com/awdawmip/enterprise-math/blob/325747d5661105943c2001abf32057e83ccf5fa5/research_checks/T6_P17_SQUARED_CANCELLATION_67_PROFILE_EXACT_CHECK_20261123.cpp) are reused at their original scopes and authorship. The original q14 side-roster contribution belongs to \`EM-EMF6D046-5A2844\`; the older pure-support H012 researcher \`EM-X6-FB6990\` keeps that distinct prior contribution. **New order-12/13 exclusions** derive from this Driver continuation; the same logical author's prior work means this is not a new independent Native review.

Scientific follow-up: preserve the current independent researcher frontiers. A qualified independent proof reviewer should audit the finite domain/completeness and re-execute the exact program before formal Result acceptance. Other p17 orders, including q11, remain open. This note creates no CLAIM, no formal Review or Result, no Task DONE and no mother Objective DONE.
