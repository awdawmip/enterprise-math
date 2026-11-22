# T6 maximal p17, vertical order six, split (2,4): exact affine exclusion

2026-11-23 Asia/Hong_Kong · **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Exact proposition

Let two cancellation-normalized exponent shapes each have mass at most 2331, and suppose their full observers H0,...,H6 agree. Work in the original integral named-denominator carrier, after cancelling the shared v17 >=2 atoms as shown in the earlier p17 high-valuation lemma. For the residual v17=1 denominators a=17(17q+r) (1<=r<=16), assume total q-order six and opposite signs split (2,4). Retain signed multiplicity, every full named denominator, all q0=17r compensators (r=1,...,16), and both independent mass budgets.

The original full-observer equalities imply the six necessary congruences

\[
\sum_{q>=0,r}m_{q,r}(17q+r)^{-j}\equiv0\pmod{17^j},\quad j=1,\dots,6,
\]

where q=0 is interpreted as the q0 compensator r, and the sum runs over signed v17=1 occurrences. The search deliberately allows all r=1,...,16, a superset of the frozen 17-smooth restrictions. **There is no admissible signed pair in this split.** Lower-prime completion can be arbitrary; it cannot repair a failed globally necessary congruence.

## Exhaustive exact certificate

The saturated 16-dimensional q0 lattice is taken at original Git blob `d9ac014355a6a1058cc8a0cf2141a01082628881`, with row determinant magnitude `17^21`. Every row satisfies the six congruences, and a six-column inverse-power Vandermonde minor is invertible modulo 17; hence the kernel index is precisely `17^21` and no q0 solutions lie outside this lattice. All affine vertical shifts are obtained by exact successive modular lifting.

The complete vertical rosters, with per-side budget, contain 152 states of q-order 2 and 6460 of q-order 4. Ordered pairs: 981,920. Of these 262,720 share an identical named vertical atom across signs and cancel to a previously handled lower q-order; the remaining 719,200 primitive pairs are exhausted.

For a primitive pair with vertical masses c+, c-, let u be the signed 16-coordinate q0 vector and w_r=17r-1. If both side budgets hold then the necessary weighted sphere bound is

\[
\sum_{r=1}^{16}(w_r u_r)^2\le(2331-c_+)^2+(2331-c_-)^2.
\]

The maximum possible squared radius is `4,360,450`, using minimum vertical costs 594 and 1172. The **exact** minimum Gram-Schmidt diagonal squared of the weighted q0 lattice equals

`8350069911612335617606677214061177705401058080646556447012234889468081355909 / 480650972868542992444263969893692042421717754534280313801217347854273`,

which is approximately 17,372,418.62 and strictly exceeds the radius. Thus at every GS coordinate the only possible integer choices are the floor and ceiling around the exact affine center. Search prunes only with exact Fraction inequalities.

The locally executed exact computation reports **1,917,830 GS recursive nodes, zero complete sphere leaves, and zero mass-valid q0 completions**. Initial full prefix 128/152 roster states completed before runtime interruption; it had 579,976 primitive pairs and 1,537,763 nodes. The remaining 24/152 states were executed without replaying the completed prefix, and counters were accumulated exactly. Local certificate SHA256: `57be59d0010745f398ca89e7e02396e91b3d08badc66a163aea12e69cb52db5f`. The published complete checker is a directly adapted q5 reproducer and has **not separately been executed**; its code reproduces the same saturated lattice and entire q6 split enumeration without a continuation shortcut.

## Scope and next frontier

This proves only the globally necessary mixed-congruence exclusion for maximal p17 v17=1, q6 split(2,4). The earlier q6 splits (0,6) and (1,5) are preserved at their original source pins. The next exact unfinished q6 unit is split (3,3). No independent mathematical reviewer, official T6 CLAIM/RUN, Native semantic PROGRESS, terminal global T6 proof or promotion is asserted.

Authorship belongs to the ordinary Research lane `chatgpt-research-onhour-enterprise-math-20260923`, researcher `EM-X6-FB6990`, original Source session `MCP-082892eb480e45dea6d4b9fcc0491034` (not a maintenance-lane session). Frozen task scientific input commit `d84bd940cfb093cdc60e569f15cad58772a51dca` remains unchanged.
