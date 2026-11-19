# Q30 n=15: independent connected degree-sector targets (2026-11-19)

Task: RS-P000-Q30-N15-FIRST-COLLISION-FRONTIER / TP2-D26B7FC040AB70B8B136.
Scope: **exact finite count target only**. The n<=14 parent recovery RR-15457ACA568B33A04CE7 has a current ACCEPTED review DR-CC898FED6F444A808B06; do not redo that census.

## Sector classification

Fix 15 labeled vertices, exactly r with degree 3 and s=15-r with degree 2, and require connected simple graphs. The handshake parity rule forces even r. The frozen U_BR branching sectors are r in {2,4,6,8,10,12,14}; the r=0 pure cycle is not part of the branching sectors previously used in Q30. Suppressing degree-two paths yields a connected cubic multigraph kernel on r vertices, with 3r/2 edge instances and total s inserted degree-two vertices. Loops need at least two insertions and parallel kernel edges may not both remain unsubdivided if they would duplicate an edge. Quotient such valid subdivisions by exact graph isomorphism; kernel data are coverage coordinates, not the Q30 observable.

## Independent exact labeled count recurrence

Let H(a0,a1,a2,a3) count all simple labeled graphs on a fixed set of vertices having prescribed degrees 0,1,2,3. Choose a fixed vertex of maximum positive prescribed degree d and remove it. For choices t_k neighbors among remaining prescribed-degree-k vertices (k=1,2,3), with sum t_k=d, the neighbor-set multiplicity is product binom(a'_k,t_k), where a'_d=a_d-1 and all other a'_k=a_k. Decrement each selected neighbor's prescribed degree and recurse. Base case: all residual degrees 0 implies H=1. This counts each labeled graph once by its unique root neighbor set.

Let C(r,s) count **connected** simple labeled graphs on a fixed degree assignment (r cubic, s degree-two labels). Root at one specified cubic vertex. By partitioning its unique connected component:
C(r,s)=H(0,0,s,r)-sum_{(u,v)!=(r,s)} binom(r-1,u-1)*binom(s,v)*C(u,v)*H(0,0,s-v,r-u),
where u runs over positive even integers <=r, v=0..s, and infeasible small components contribute zero. This is an exact connected-component recurrence, independent of any 1-WL packet calculation.

## Exact computed sector counts

| r | s | Connected labeled target for fixed degree assignments |
|---:|---:|---:|
|2|13|191480889600|
|4|11|651681676800|
|6|9|2197681340400|
|8|7|7687127448000|
|10|5|28311322888800|
|12|3|110280358742400|
|14|1|454465199588400|

Sum of seven **fixed-degree-assignment sector targets** = 603784852574400. If instead every choice of the r cubic labels among 15 is counted, the corresponding sum of binom(15,r)C(r,15-r) is 203389155075506400. Do not confuse these totals.

Regression against the existing immutable n=14 certificate: all seven independent C(r,14-r) outputs exactly match 12414124800, 38690265600, 120607023600, 393165964800, 1358543793600, 4991840330400, 19491385914000; their sum is 26406647416800.

A proposed exhaustive representative list for each r must contain valid distinct isomorphism classes and satisfy sum_{[G]} r!s!/|Aut(G)| = C(r,s). Such equality plus verified disjointness and validity is an independent **coverage criterion**. These count targets alone certify neither full representative coverage nor absence/presence of equal Q30 stable packets.

## Remaining hard target

Build the actual persistent n=15 kernel/subdivision orbit representatives with checked automorphism order, verify the coverage identity, then compute exactly the *unchanged* primitive-return-profile initialized ordinary 1-WL stable packet and compare packet equality directly. For a repeated packet provide nonisomorphic pair; otherwise make no no-collision assertion before exhaustive evidence. The attached zero-dependency deterministic Python reproducer counts only degree sectors.
