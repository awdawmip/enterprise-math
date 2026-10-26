# Stage178 portable exact primal task — DUAL_ONLY

Mother problem: external ternary IID length N14; P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Full ordered-history randomized stopping/decision policies; minimize V14(alpha)=max(E_P tau,E_Q tau) under errors eP,eQ<=alpha.

Last proved author frontier: Stage177 (this directory), alpha177=5148172029061283786075/14750257906470044565504 and V177=338725183820868439620725/29500515812940089131008. Its right-end coins: T=(8,2,0) chooses P with t=1870960582929997/3860125696000000, U=(12,5,2) continues with probability 1. Stage177 already proved T/U cones disjoint, because reaching U from T requires 5 non-symbol-2 observations in 4 new slots.

New exact dual-only candidate: along T=P/C tie-preserving ray dK=-1 and dL=-169640/99621, first closure step epsilon=182297148377844/615294196448617. Candidate

K178=64228036011/290873926,
L178=93785824168/436310889,
H178=977402749984215798412630525/5975334471155518248321024.

New tie states T=(8,2,0) P/C and S=(9,0,1) Q/C. All remaining 1238 action gaps strictly positive; min 67271053/31414384008; 758 negative-derivative candidates scanned. See SCAN_STAGE178.py and dual178.json. Stage178 primal is **not** proved by this scan.

First discrimination: independently evaluate all four T/S deterministic corners with Fraction suffix DP and unmerged integer-numerator ordered DFS. Their first-hit cones are disjoint (S has zero symbol-0 counts, T already has 2), but explicitly check. Solve eP=eQ for legal coin interval, match Stage177 endpoint, evaluate tP-tQ, exact dual equality and monotonicity, determine early saturation, prove the entire next real interval plus strict support boundary or provide a rational obstruction. Do not extrapolate from the dual scan.

Keep separate P/Q positive rational branch masses and ordered-path sources (BRC reuse); no X6/P000 transfer, Source CLAIM or Driver admission without independent typed evidence.
