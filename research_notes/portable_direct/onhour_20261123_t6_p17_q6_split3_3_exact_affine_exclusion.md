# T6 p17 vertical order 6, split (3,3): exact symmetric affine exclusion

2026-11-23 Asia/Hong_Kong. **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Statement

For the frozen integer/exponent T6 carrier (source commit `d84bd940cfb093cdc60e569f15cad58772a51dca`), let the maximum denominator prime be 17. Cancel any 17²-or-higher valuation matched across signs, preserve the full original denominators and each side exponent-mass <=2331, and let the residual v17=1 vertical total order be six with signed split (3,3). For every q0=17r (1<=r<=16) allow all signed multiplicities, before any extra 17-smooth filter. Opposite shared named atoms are cancelled to the already studied lower order.

The complete equalities H0,...,H6 imply six globally necessary mixed congruences

\[
\sum m_{q,r}(17q+r)^{-j}\equiv0\pmod{17^j},\quad j=1,\dots,6.
\]

**There are no admissible cancellation-normalized solutions for split (3,3), even allowing arbitrary lower-prime completions.**

## Exact complete search

The 16-dimensional q0 lattice has original pinned Git blob `d9ac014355a6a1058cc8a0cf2141a01082628881`. Its determinant is 17²¹ and it satisfies the six congruences. A six-column inverse-power Vandermonde minor is invertible mod17, so the congruence kernel has index 17²¹; the lattice is saturated, and each vertical roster shift has a complete integral affine representative.

Enumerate all q=3 vertical rosters of named integer atoms (q,r) with q>=1, 1<=r<=16, mass 289q+17r−1 and repetitions allowed. Each side admits exactly **1,088** budget-valid rosters. Because swapping sides changes only the global sign, enumerate unordered distinct pairs i<j; equal pairs are identical supports and cannot be primitive.

| Exact quantity | Count |
| --- | ---: |
| Unordered distinct raw roster pairs | 591,328 |
| Opposite shared named atoms (cancel to lower q order) | 171,136 |
| Primitive support-disjoint pairs | **420,192** |
| Fraction-exact Gram–Schmidt recursion nodes | **1,035,941** |
| Complete necessary weighted sphere leaves | **0** |
| Actual legal two-side q0 completions | **0** |

The necessary weighted Euclidean bound on the q0 signed vector u is
\[
\sum_{r=1}^{16}((17r-1)u_r)^2 \le (2331-c_+)^2+(2331-c_-)^2.
\]
Both sides have minimum vertical mass 883, yielding maximum squared radius **4,193,408**. Exact minimum squared GS diagonal of the weighted saturated lattice is

`8350069911612335617606677214061177705401058080646556447012234889468081355909 / 480650972868542992444263969893692042421717754534280313801217347854273`,

approximately 17,372,418.62. It strictly exceeds every radius, so exact floor/ceiling enumeration at each GS coordinate covers all possible q0 corrections. The actual Python Fraction execution completed all 420,192 primitive pairs in one run, reached no sphere leaves and no valid solution. Local original certificate SHA256 `5728e05a0ccca663e5a526d2f738c01d6b2056dfdde577c510099d564e68d9c3`. The GitHub complete reproducer is a direct q5 adaptation; separate execution of that published variant is not asserted.

## Scientific conclusion and boundary

Together with the previously preserved same-frozen-input author results for q6 splits (0,6), (1,5), and (2,4), this supplies an **author-level complete p17 vertical-order-6 exclusion**, conditioned on the previous high-valuation cancellation and earlier lower vertical-order cases. It is not a globally complete maximal-p17 exclusion: orders >=7, lower maximal primes, Source Result and independent review remain open.

Next precise unit: first unclosed p17 vertical order 7, once current Source and preexisting work have been checked. Do not recompute q6. Provenance: ordinary Research lane `chatgpt-research-onhour-enterprise-math-20260923`, `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`; no maintenance lane authority or Native T6 CLAIM/PROGRESS.
