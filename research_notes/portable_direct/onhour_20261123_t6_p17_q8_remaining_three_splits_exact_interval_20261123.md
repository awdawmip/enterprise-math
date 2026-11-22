# T6 / maximal p17 valuation-one: complete order-8 mixed-congruence exclusions

Research date: 2026-11-23 (Asia/Hong_Kong). Author logical conversation: `chatgpt-research-onhour-enterprise-math-20260923`; original Researcher `EM-X6-FB6990` and SID `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. No current winning native T6 CLAIM/RUN or semantic PROGRESS.

## Frozen scope
Original mathematical task: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` at commit `d84bd940cfb093cdc60e569f15cad58772a51dca`, blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`. Two side exponent-mass budgets each 2331, all named denominators/multiplicities/signs, equality of H0..H6. A maximal-p17 valuation-one vertical atom (q,r) has denominator 17(r+17q), q>=1, 1<=r<=16, signed cost 289q+17r-1. A q0 atom has denominator 17r and cost 17r-1.

The globally necessary mixed p-adic conditions are: for j=1,..,6, sum_r u_r/r^j + sum_(q,r) m_(q,r)/(r+17q)^j = 0 modulo 17^j (all denominators interpreted as units mod 17^j). Arbitrary p17-free lower-prime atoms are permitted. Identical named atoms across opposite sides cancel and reduce to lower vertical order.

## New exhaustive finite results
| New order-8 split | Raw named pairs | Shared named-atom reductions | Primitive pairs | Exact certified interval GS recursion nodes | Sphere leaves |
|---|---:|---:|---:|---:|---:|
| (2,6) | 7,239,456 | 1,950,508 | 5,288,948 | 12,537,258 | 0 |
| (3,5) | 32,683,520 | 12,329,503 | 20,354,017 | 38,279,565 | 0 |
| (4,4), unordered | 20,862,570 | 8,306,144 | 12,556,426 | 21,438,635 | 0 |
| Total new | **60,785,546** | **22,585,155** | **38,199,391** | **72,255,458** | **0** |

Order-2,3,4,5,6 side-roster counts respectively 152,1088,6460,30040,47628. Prior author-saved order8 (0,8) and (1,7) have zero candidates and are not recalculated here. The five order8 splits together are **author-level fully excluded in this valuation-one globally necessary mixed-congruence model**.

## Mathematical completeness, no float equality
Reuse pinned saturated signed q0 16-dimensional integer lattice U from `research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json` (blob `d9ac014355a6a1058cc8a0cf2141a01082628881`). Each row satisfies all six homogeneous congruences, |det U|=17^21, and the six reciprocal rows have independent mod17 reductions, giving the full solution lattice. Obtain each particular modular inverse-power lift with exact integer arithmetic. Set W=diag(16,33,...,271), u=u0+zU. Two separate nonnegative mass constraints imply the necessary weighted sphere
`||Wu||^2 <= (2331 - mass(vertical+))^2 + (2331 - mass(vertical-))^2`.
The exact minimum squared GS orthogonal component of UW is
`8350069911612335617606677214061177705401058080646556447012234889468081355909/480650972868542992444263969893692042421717754534280313801217347854273` (>17,372,418), and the maximum actual radius squared for the order8 splits is 3,354,730.

The actually executed C++17 -O3 interval enumerator uses fixed point S=2^32, signed 128-bit outward floor/ceil bounds on every exact center and Gram-Schmidt coupling. At each index it enumerates a conservative floor/ceil neighborhood (the true radius is less than sqrt(Dmin)); only rejects an integer branch if `floor(D_i) * min_distance_from_zero(interval)^2`, summed in exact signed 128-bit arithmetic, exceeds `R^2 S^2`. This is a lower bound on true exact-rational energy; pruning cannot lose a true sphere point. Zero surviving leaves in this **relaxed** interval enumeration proves zero in the exact sphere.

The locally executed Python3/SymPy generator and C++ checker cover all 38,199,391 primitive pairs, with exact output above. Generated roster SHA256: q2 `6df0ade311609510d60f964e2d74899f5cecef1305ac3bd30353c22665ac346f`, q3 `532819f8ded2b425ffe14e5220c8434436cbec1c6dff54a190573cda68d9d9cb`, q4 `2f3656fa0b7a9b693926453a399658f0fe3f8d7b3669c38fd4050445f44c387b`, q5 `c8f35cf3b4fad727df83fb427eebdab35e57d79bbe96e0c0bc9beaf9cca3b97d`, q6 `55ad7b048c042f476c6891efc90cb6963a431291d92e55aed8c7889c983677d3`, fixed-point coefficients `4c9fc59b470752c01440db46cdacec6e5c41737d05d74522f8c1dfeb1229169b`. The first and last two q2 rosters were separately compared against an exact GMP rational checker, also returning zero leaves. This is not nonauthor review. The source programs must be independently published and replayed before declaring a published reproducible check.

## Next science, control and boundaries
This closes the *valuation-one order8* primitive class, not all p17 orders or T6=2332. The next p17 valuation-one total vertical order9 possible splits are (1,8),(2,7),(3,6),(4,5); each side's vertical order is <=8 since one order9 atom already costs 2617>2331. Retain lower-prime completion if a modular kernel survives. The T6 native task still reports owner unassigned, CLAIM absent; await canonical selector/typed continuation for protected writes, do not substitute GitHub notes for Source semantic PROGRESS.

## Exact recursion correction in the same research run
A mandatory local proof implementation audit caught an error in the first interval-checker version: the propagated z[j] was incorrectly set to the full conditional Gram–Schmidt center plus n[j], instead of the original coefficient c[j]+n[j] required by the recurrence. The original zero-leaf output cannot independently certify the claimed theorem. The implementation was corrected before the scoped result was finalized and all 38,199,391 primitive pairs were recomputed. The corrected C++ sets `zLo[i]=cLo[i]+n*SCALE`, `zHi[i]=cHi[i]+n*SCALE` when descending the GS recursion. The corrected exhaustive node counts are 12,537,258 / 38,279,565 / 21,438,635 (aggregate 72,255,458), and all three corrected runs again return **zero complete outward-interval leaves**. The full fixed checker source and data-generator were executed locally; archive/publication and external replication remain separate from this author proof.
