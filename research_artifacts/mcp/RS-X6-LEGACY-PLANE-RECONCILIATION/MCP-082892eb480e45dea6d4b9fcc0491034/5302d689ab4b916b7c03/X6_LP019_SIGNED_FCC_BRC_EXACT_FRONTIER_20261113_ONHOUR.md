# On-hour signed-X6 FCC carrier BRC exact continuation — 2026-11-13

Parent Task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2.
Researcher EM-X6-FB6990; own session MCP-082892eb480e45dea6d4b9fcc0491034.
Winning claim MCP-9ce362c91287345702dd387d; own RUN RUN-1e81bbcb1938961eb41db249 generation 1, revision 2.
Frozen scientific P000/X6 @59538f585d037d09ef687b28715c4bc1a3f9fe03 and historical @fd2bcff10ca6e147348b6c1236027fc0d2877df3.

New theorem: primitive signed X6 carrier steps are ±v_i, v_i={(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)}.
Let S=(X+X^-1)(Y+Y^-1)+(X+X^-1)(Z+Z^-1)+(Y+Y^-1)(Z+Z^-1).
For all integers p,q,r and N>=0, the exact ordered length-N signed-X6 paths with FCC carrier terminal (p,q,r) have count C_N=[X^p Y^q Z^r]S^N = Σ_{a+b+c=N} N!/(a!b!c!) B(a+b,p)B(a+c,q)B(b+c,r), with B(k,t)=binom(k,(k+t)/2) under parity and bounds, else 0. This is an exact polynomial proof by disjoint step-family partition and independent signs, not finite extrapolation.
Exact actual checker: N=0..8, 50,445 native endpoint DP terms and 5,480 carrier coefficient tests, all PASS; 12^N mass for every N.
Minimal carrier-only return: N=1 no zero; N=2 has 12 opposite-pair carrier/native returns; N=3 has 8 sign-compatible XY/XZ/YZ triples times 3!=6 orderings => 48 carrier returns but 0 native signed-Z6 odd-length returns. Exhausted all 12^3=1728 words: 48 exactly.

Current consumer 'experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py' git blob 2a8c8c804c6d4b0a4e0919f62235e58ccb583e4e lines 8–16/72–85 is correctly typed carrier observer and keeps different native lifts. Disposition KEEP; no erroneous native cancellation historical caller proved there.

Exact published evidence:
- awdawmip/enterprise-math@b408775b7cf6031646031aec64a07301f59d8d3c:research_checks/X6_LP019_FCC_SIGNED_BRC_PUSHFORWARD_20261113_ONHOUR.py, blob a82b8cfb6039531aec2266e283a5277ab20f7c4c
- awdawmip/enterprise-math@bc6b7e10b30a29b07169ab87b4780c17c3ff3008:research_notes/X6_LP019_FCC_SIGNED_BRC_PUSHFORWARD_CONSUMER_20261113_ONHOUR.md, blob 3da2ce6301b725046998b8298c5f31c56fa5a4c9
- awdawmip/enterprise-math@b0069a4a9a1d9d2ea0b5e8d118a0350cced2fbe8:research_notes/X6_LP28_SOURCE_CONSUMER_ACTION_CROSSWALK_20261112_ONHOUR_1400.md, blob ea9696d4a9f901fcaf0bab4e43beee54f49f546e
Eight complete frozen historical files additionally audited, no erroneous LP011 native dominant-axis or LP019 positive-count cancellation call sites confirmed. Their historical provenance remains UNRESOLVED_PROVENANCE, not zero historical inventory.

Remaining mother target: full 28 LP downstream dependency closure, actual original LP011/LP019 historical provenance and Driver REQUEST_REVISION evidence, activity legacy receipt migration #2187. Current math AUTHOR_PROVED/LOCAL_EXACT_CHECK_EXECUTED/UNREVIEWED/NOT_ADMITTED, no benchmark or Result claimed.
Do not repeat prior LP026/LP028, coordinate 50771 regression, signed shell 30/846, V12 gauge repair or previous original PathSqrt tests.
Next action: inspect current executable native vs carrier BRC, can3/Coord6 calls, obtain exact wrong input/output and apply minimal correction only on evidence; then fulfill Driver revision and canonical result process. Preserve own session/claim/run; no maintenance lane.