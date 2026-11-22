# T6 maximal-p17 valuation-one total vertical order10: four-split exact exclusion

Date 2026-11-23 (Hong Kong time). Author TASK_RESEARCH logical conversation chatgpt-research-onhour-enterprise-math-20260923, researcher EM-X6-FB6990, original public SID MCP-082892eb480e45dea6d4b9fcc0491034. State AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED, whole T6=2332 still OPEN.

Frozen task mathematical input is awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md (blob 87b3a6f38e9350f7a3f56624b27bff2a7778a439). Each side's exponent mass <=2331, preserve named full denominators, multiplicities, signs, p17 val1 and full H0..H6 observers. A p17 val1 vertical atom (q,r) costs 289q+17r-1 and q0 (r) costs 17r-1. Since the vertical order of either side cannot exceed 8, the four total-order10 splits are precisely (2,8),(3,7),(4,6),(5,5), up to sign exchange.

Six necessary GLOBAL mixed congruences (j=1..6) require sum_r u_r * inv(r^j,17^j) + sum_(q>=1,r) m_(q,r)*inv((r+17q)^j,17^j) == 0 mod17^j, while allowing unrestricted lower-prime atoms. Opposite-side equal named vertical atoms cancel and are referred to already completed smaller vertical order.

## New fully executed finite search
| Total order10 split | Raw pairs | Opposite shared support | Primitive pairs | Exact outward-interval recursion nodes | Complete sphere leaves |
|---|---:|---:|---:|---:|---:|
| (2,8) | 152 | 0 | 152 | 334 | 0 |
| (3,7) | 9,462,336 | 2,298,236 | 7,164,100 | 12,757,136 | 0 |
| (4,6) | 307,676,880 | 124,372,713 | 183,304,167 | 262,224,571 | 0 |
| (5,5) unordered | 451,185,780 | 217,665,508 | 233,520,272 | 300,725,452 | 0 |
| **Total** | **768,325,148** | **344,336,457** | **423,988,691** | **575,707,493** | **0** |

This is actual execution of all four finite cases by the corrected C++17 signed-integer outward interval checker in the present turn, using the exact previously generated q1..q8 roster files and the same 16-dimensional saturated signed q0 lattice. The largest (5,5) run examined all 451,185,780 unordered side pairs in approximately 34 seconds using about 11 MiB memory. No split was left half-executed; the completed terminal JSON for each of the four cases records zero leaves.

## Completeness
Reuse unchanged: 16x16 p17 q0 saturated integer basis from research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json (blob d9ac014355a6a1058cc8a0cf2141a01082628881); determinant magnitude 17^21, which is the full index of six mod17^j reciprocal constraints. After exact modular lift, any signed q0 completion is u0+zU. The two side-cost caps imply the necessary weighted squared ball:
norm(diag(16,33,...,271)*u)^2 <= (2331-Cpositive)^2 + (2331-Cnegative)^2.
The exact min Gram-Schmidt squared diagonal is 8350069911612335617606677214061177705401058080646556447012234889468081355909 / 480650972868542992444263969893692042421717754534280313801217347854273 (>17,372,418); this is larger than every q10 radius squared (maximum <=4,104,685). Therefore at each coefficient the search enumerates all possible nearest integer candidates from a rigorously conservative outward fixed-point S=2^32 interval. The corrected version propagates original affine coordinate c_j+n_j in GS recurrence; all possible exact spherical solutions are contained in the relaxed integer search. Zero relaxed leaves proves zero exact solutions, without any floating-point equality.

The executed source is local equivalent to currently published research_checks/T6_P17_Q9_INTERVAL_GENERATOR_20261123.py and research_checks/T6_P17_Q8_INTERVAL_EXHAUSTIVE_CHECK_20261123.cpp; original generated integer roster hashes are preserved in q9 certificate research_checks/T6_P17_Q9_ALL_FOUR_SPLITS_AUTHOR_CERT_20261123.json. The published reproducer was not independently rerun after GitHub publication, so this is an author-level completed finite proof awaiting independent audit.

Scope: no primitive maximal-p17 valuation-one vertical-order10 signed pair within both side budget caps survives all six globally necessary p-adic conditions, hence low-prime completion cannot rescue this subset. Other valuation layers, higher total vertical orders q11..16, and maximal p13/11/etc remain unclosed. Next candidate q11 possible splits (3,8),(4,7),(5,6), with complete existing side rosters and the same original 2331 budgets. No T6 winning native CLAIM or protected PROGRESS is reported; leave T6 OPEN.
