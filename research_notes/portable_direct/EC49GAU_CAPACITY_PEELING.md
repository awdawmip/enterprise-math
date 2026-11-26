# EC49GAU — Exact two-sided capacity peeling

2026-11-26. Informed independent continuation of EC49GAT and EC49GAQ (frozen BRC16943). No shared CLAIM, no formal Result. Historical provenance EM-DIRECT-23537B; current private identity not confirmed.

## Theorem (unit target credit, arbitrary finite capacity graph)

Let G be a bipartite graph of labeled targets and resource classes, each target at most one credit and class j having nonnegative integer capacity c_j. Write H(G) for maximum number of distinct matched targets. Delete zero-capacity classes. The following reductions preserve H after adding the specified paid credit:

1. A target with no remaining neighbors is deleted, with zero credit.
2. If D_j is the set of targets whose only remaining neighbor is j, let g=|D_j| and p=min(g,c_j). Delete all D_j, lower c_j by p, remove class j if its remaining capacity is zero, and add p credits. Then H(G)=p+H(G'). Proof: take an optimal matching. If fewer than p of D_j are matched, fill unused j slots or exchange occupants outside D_j for targets of D_j; exchanges cannot decrease cardinality. Thus there is an optimum matching p of D_j. Restrict this optimum to the other targets for the upper bound; lift any optimum of G' by matching p members of D_j to reserved slots for the lower bound. If g>c_j the g-p remaining singleton targets necessarily receive no credit in that normalized optimum (other optimal matchings may select different identities). Groups for distinct j may be processed simultaneously since their target sets and reserved resource slots are disjoint.
3. For any collection R of classes with c_j>=|N(j)|, delete P=union_{j in R} N(j) and remove classes R, add |P| credits. Assign each member of P to an arbitrary neighboring class in R, no capacity can be exceeded. Targets outside P have no neighbors in R. This gives a lower bound by lifting an optimum of the residual, and the corresponding upper bound by restricting any optimum to targets outside P. This extends GAT's global-rich test to local actual demand.

Repeat to a fixed point. The residual core has target degree >=2, and every non-isolated resource has 0<c_j<|N(j)|. Writing P for total paid credit, L for total targets deleted without credit, G_* for residual, n for original target count, we have n=P+L+|T_*| and H(G)=P+H(G_*). In particular n-H(G)=L+(|T_*|-H(G_*)). No prescribed order is needed for the scalar identity. The algorithm must maintain original target labels and allowed relation for subsequent physical decision/target queries; the peel is scoped to one fixed unit-weight abstract Hall capacity query. It does not preserve all feasible target subsets, or weighted optima for arbitrary target weights: with capacity one, a singleton target of weight 1 and a target of weight 2 eligible only for the same class, arbitrary singleton credit need not select the heavier target. Use original inputs for changed goals or weights. The physical decision capacity is still bounded above by the exact abstract H, not identified with H.

## Executed verification

Frozen inputs inherited from GAT reproduction archive, all 335 SHA256 manifest entries checked. ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0; gap_target.json SHA256 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5. Predecessor GAT proof 7644a824347bc5edf7be39fc14f1f0394b5473ee, GAT code/evidence 8e4f5b8a3017876ed84a2c938c028c9cb70d715c. Reuse GAQ HallOracle, GAT category-capacity matching, and physical frozen state masks. No new BRC arithmetic or physical state generation apart from the inherited exact root generator.

Executed peel_hall.py, blob cd57b54be1b14f30c10576ccb135c2aeb59adb0d, at e53affb85c7c4b03b6b1c935a6f96f7fc28771ad. Run python peel_hall.py > peel_hall.json inside extracted GAT archive. Seed 49261127, 3000 arbitrary (not just interval) graphs, 1..8 classes, 0..32 targets, capacities 0..6. Independent exact exhaustive capacitated Hall-cut formula agreed in every case. 47700 targets: dead 10722, singleton paid 11865, singleton lost 7127, rich paid 4162, residual 13824. Edges 91084 -> 43287.

All 180 frozen nodes, two budgets each, 366 goals, 87058 directed graph checks per mode; old and new exact graph adjacency and every per-case search counter agreed. 14498 paired calls, 8680 prunes; 41334 allocation nodes, 358275 scalar cache misses. Across paired calls: 167894 target records, 19502 dead, 11369 singleton paid, 3292 singleton lost, 27900 locally rich paid, 105831 residual. Edges 560786 -> 414394. Local-rich reduction succeeded despite GAT finding zero globally rich targets in the same cases. 181 cases had singleton payments and local-rich payments; 133 had singleton loss. Old word mode time 1.328670242 sec, peel mode 1.505812858 sec in one sequential run; new preprocessing/core reduction did not yield overall speedup. No C++ integration of GAU. Compact evidence at e23c7078874d110ec00817f4fb40e9069d59601d: research_artifacts/portable_direct/EC49GAU/peel_compact.zlib.b64; base64 decode then zlib decompress, SHA256 0a0a63701a21712a3575cdc8184bfe868573b8b87ec50d0a219fff9df787a34b. Row fields and exact summary are embedded; raw JSON is retained in local reproduction package. Timings nondeterministic.

## Additional fourth-layer physical root calculations

New IDs 1992 and 1993, not among GAR's eight historically reported roots. Frozen fourth.json, gen.py, fourth_input.py and gak_solver.cpp reused from GAT/GAQ archive. Generate python fourth_input.py 1992 1994 600000 > gau_roots.in. Input SHA256 c9cb2b4a723ceea7565d881abbfa84f662c14ab7b21522b98e95ae78933bbed5. Compile g++ -O3 -std=c++17 gak_solver.cpp -o gau_solver. Run with EM_DENSE=1 EM_FAST=1 EM_WORD=1 and with EM_DENSE=1 EM_FAST=1, respectively. GAK's actual full state replay checks all labels for YES, no search budget reached for NO. These are old GAK solver results, not GAU accelerated.

Word mode raw CSV:
1992,1750,1,18518,0,0,0,114,48,0,48,59,18295,15082
1993,1755,-1,105113,0,0,0,1316,334,0,334,957,104602,90510

Baseline raw CSV:
1992,1750,1,28262,763,0,0,730,188,0,188,681,0,0
1993,1755,-1,175281,3556,0,0,5430,1088,0,1088,4640,0,0

Both modes agree, 1750 YES states replayed per mode; 1993 exhaustive NO. From the GAQ durable 1960 YES/45 NO/388 OPEN, these two new verified roots yield at least 1961 YES/46 NO/386 other structures without counting the eight GAR historical decisions whose raw records remain missing. Adding those historical reports conditionally would give 1967 YES/48 NO/378 OPEN, not a fully verified total. Original M14 bound unchanged: 25<=M14<=27. Next fresh IDs at/after 1994 after reconciling other writers and the saved status list. GAR/GAS missing raw evidence remains an actual debt, not a claim of recovery.

## Control and next problem

Current topic query r4-20261126-1926-rs-ec49as-read SUCCEEDED, Source 1ac5847724c87d8690a4a2a67160071363edd6f1, directory absence only; native owner projection not evaluated. No shared task writes or ownership change, no replacement identity. Activity association pending. Next: seek inexpensive component splitting or bitset cut/core computation and compare to GAQ without defaulting to slow peeling. Recover GAR/GAS original artifacts if available; keep verified vs historical totals separate. AUTHOR_PROVED / EXACT_FINITE_ARBITRARY_CAPACITY_CUT_CHECK / EXACT_FINITE_FROZEN_CONFLICT_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
