# EC49FZS — Tight unsaturated layer first-query intersection

2026-11-25. Parent FZR @91053cc7a187af277860a02b653e372ff6834135:research_notes/portable_direct/EC49FZR_MAXIMAL_ROW_UNION_SEARCH.md. Frozen BRC16943, m=25, h=14, fourth-level budget 15. Parent reproduction archive SHA256SUMS checked; 2393 roots, 1802 YES, 13 NO, 578 open. Task read r4-20261125-1535-ec49as-read SUCCEEDED at e82191f37b71ccb83c8c1f85ac6a95497b6f2f9b, NO_CANONICAL_PUBLICATION_DIRECTORY, not an owner projection. Historical researcher EM-DIRECT-23537B, current private binding unconfirmed; no new identity or shared CLAIM/Result/Review. Independent portable work. P000 unchanged.

## Theorem and proof

Under FZP/FZQ genuine anchored observation-history assumptions, let U be a compatible support, B its forced holes, F its free columns, p=|F|. Fix any unsaturated target H=B union Z, Z subset F, b=|Z|, |H|<h. Same-H competing supports V are precisely those compatible with H; in the common possible-hole universe these are identified by D_V=B_V minus B subset Z. Let T range over row covers of every active difference U xor V. The FZP exact path certificate cost is
C(Z)=min_T [max(p,b+|T intersect U|)+|T minus U|].
For C(Z)=k, let N be the union of T minus U over minimizing row covers and E the union of T intersect U over minimizing covers with |T intersect U|>p-b. Then the first query of any depth-k identifying strategy belongs to
P(Z) = U x F union (E union N) x ([m] minus H).
Consequently the intersection of P(Z) over any collection of tight witnesses must contain the first query; an empty intersection excludes the node.

Proof: Along the target path, every free column has a one-column competing state, because H is unsaturated. Distinguishing each requires a query on that column in a row of U. This forces b missing-column queries and p-b positive queries, all on distinct columns. Same-H competitors can only be distinguished on normal columns, so the rows T queried there hit all active row differences. Writing positive-row count a and negative-row count c, the path length is at least b+max(p-b,a)+c = max(p,b+a)+c. If C(Z)=k and the path has length at most k, all inequalities are equalities, and T minimizes the formula. A query on a missing column must be one of the b required queries. A negative-row query on a normal column belongs to a row in N. A positive-row query on a nonfree normal column consumes an additional positive observation beyond p-b, so equality forces a>p-b and its row is in E. All other allowed queries are in U x F. Rows outside the union of active differences cannot participate in an optimal cover's N or E: removing a negative such row lowers cost, as does removing a positive such row when a>p-b. This also justifies enumerating only relevant rows. Intersecting over witnesses is sound because a decision tree has one common first query. This extends the FZL minimal-fiber tight-row rule to the entire unsaturated layer, including b>0. It is a necessary first-query condition, not an adaptive feasibility equivalence. Maximal-layer witnesses suffice for detecting any path-cost excess by FZP; we do not claim they capture every tight-query restriction from lower layers.

## Actual implementation

Starting with union.cpp in the FZR reproduction, add `array<int,M> allowR;allowR.fill(1023);` immediately before the maximal unsaturated fiber envelope comment. Immediately after the existing obstruction(obstruction,0) exclusion line, insert the following code (including the blank line before the original closing brace). Add `if(!(allowR[j]>>r&1))continue;` immediately after `if(tight&~R[r])continue;` in query enumeration. All remaining search and independent physical-label replay code is unchanged. The existing gate k<=8,q=k-p<=2,b>0 bounds free-set enumeration by 2^8. Skipping other nodes or rival-empty fibers just weakens the necessary condition.

```cpp
   // Tight maximal-layer witnesses: retain the intersection of necessary first queries.
   for(int z=freeMask;;z=(z-1)&freeMask){
     if(pc(z)==b){
       int best=k+1,posExtra=0,neg=0;
       for(int t:allowed){
         int pos=pc(t&u),cost=max(p,b+pos)+pc(t&~u);
         if(cost>best)continue;
         bool ok=true;for(auto[d,r]:rivals)if(!(d&~z)&&!(r&t)){ok=false;break;}
         if(!ok)continue;
         if(cost<best){best=cost;posExtra=neg=0;}
         if(pos>p-b)posExtra|=t&u;
         neg|=t&~u;
       }
       assert(best<=k);
       if(best==k){
         for(int j=0;j<M;j++){
           int permit=(freeMask>>j&1)?u:0;
           if(!((B[i]|z)>>j&1))permit|=posExtra|neg;
           allowR[j]&=permit;
         }
       }
     }
     if(!z)break;
   }

```

Save as tight.cpp (SHA256 08477f6be462fed3217d82e5732968dccbbcf46775a23b50bf9ba810562978e2). In retry_r.py append 'r.csv','r2.csv','r3.csv' to the files list and change len(ids)==646 to len(ids)==578; save retry_s.py (SHA256 7b334a1a20b1d516985d2dab5d94097852bb1b1fb25049a5940c935e47cd732a). Compile both union.cpp and tight.cpp with g++ -O3 -std=c++17. Generate batches with python retry_s.py 0 12 100000, 12 42 100000, 42 72 100000. Run tight on all batches and union on first two; separately generate root 1814 from fourth.json using gen.physical([mask,*other],14,r,0) and budget 15, cap 250000, run union. Root 1814 is excluded by both solvers. CSV format root,n,status,calls,envelopePrunes (1 replayed YES, -1 exhausted NO, 0 cap).

## Actual results and interpretation

42-root paired comparison at cap 100000: both 28 YES and 14 open. Tight calls 2698461 vs baseline 2713477 (15016 fewer, 0.5534%); 23 roots fewer calls and 19 equal; 0 more. Runtime 11.02+18.38=29.40 s vs 10.86+18.23=29.09 s; no demonstrated runtime acceleration. Envelope-prune counters 56872 vs 94695, because earlier first-query exclusions alter visited nodes; counters do not measure total logical pruning. Third batch 22.01 s. 72 distinct previously open roots: 46 YES, 1 NO, 25 open; 4749095 calls, 104097 envelope prunes, 67533 physical-label target replays. NO 1814: new calls 79665, baseline calls 81077 (cap 250000). No old classified root recomputed. Totals 1848 YES, 14 NO, 531 open of 2393; ordered 3730 YES, 28 NO, 937 open of 4695. Inventory remains 25<=M14<=27. Author-proved, finite search/replay, not independently reviewed.

## Raw results

s.csv
```csv
1529,1237,0,100001,669
1732,1401,0,100001,3607
1744,1410,0,100001,2612
1745,1411,0,100001,1067
1756,1424,1,33889,297
1757,1426,1,38338,14
1758,1427,0,100001,1823
1759,1427,1,17806,351
1760,1427,0,100001,3581
1761,1432,0,100001,3865
1762,1432,0,100001,3865
1763,1432,0,100001,2775
```
s2.csv
```csv
1764,1433,1,51485,249
1765,1434,1,21795,0
1766,1435,1,92640,1758
1767,1437,1,54101,343
1768,1444,1,15476,128
1769,1445,1,75678,2654
1770,1449,1,56337,14
1771,1449,1,36335,898
1772,1450,1,53770,1794
1773,1451,0,100001,2773
1775,1451,1,43783,937
1776,1451,1,29123,807
1777,1452,1,11867,100
1778,1453,0,100001,3167
1779,1456,1,57432,831
1780,1456,1,45886,983
1781,1457,0,100001,2673
1782,1458,0,100001,1211
1783,1458,1,61082,0
1784,1462,1,95372,1656
1785,1462,1,30415,323
1786,1462,1,38909,840
1787,1462,0,100001,2336
1788,1464,1,13294,0
1789,1465,1,38602,1136
1792,1475,1,35215,112
1793,1475,1,35215,112
1794,1475,1,62984,850
1795,1476,1,84573,1646
1796,1476,1,67045,2015
```
s3.csv
```csv
1797,1476,1,49523,1366
1798,1477,1,14451,368
1799,1480,1,33332,952
1800,1480,1,37932,4
1801,1487,1,65915,2025
1802,1488,1,52317,802
1803,1488,1,52317,802
1804,1488,1,52317,802
1805,1488,1,52317,802
1806,1488,1,23292,376
1807,1488,1,41613,867
1808,1489,1,81034,1521
1809,1491,0,100001,795
1810,1492,0,100001,710
1811,1492,1,56700,280
1812,1493,1,42543,451
1813,1495,0,100001,1930
1814,1499,-1,79665,1864
1815,1499,0,100001,2488
1816,1507,1,74486,1491
1818,1511,0,100001,3661
1819,1511,0,100001,895
1820,1513,1,75883,2810
1821,1514,0,100001,2768
1822,1519,1,32882,524
1824,1523,1,32104,477
1825,1524,0,100001,2054
1826,1524,0,100001,5325
1827,1525,0,100001,4642
1828,1526,0,100001,3373
```
sbase.csv
```csv
1529,1237,0,100001,1241
1732,1401,0,100001,6285
1744,1410,0,100001,4865
1745,1411,0,100001,1813
1756,1424,1,34043,451
1757,1426,1,38338,14
1758,1427,0,100001,3242
1759,1427,1,18004,549
1760,1427,0,100001,5721
1761,1432,0,100001,6218
1762,1432,0,100001,6218
1763,1432,0,100001,3968
```
s2base.csv
```csv
1764,1433,1,51650,404
1765,1434,1,21795,0
1766,1435,1,94044,3161
1767,1437,1,54365,606
1768,1444,1,15671,304
1769,1445,1,77441,4350
1770,1449,1,56337,14
1771,1449,1,36869,1413
1772,1450,1,55392,3318
1773,1451,0,100001,4562
1775,1451,1,44502,1653
1776,1451,1,29475,1156
1777,1452,1,11973,206
1778,1453,0,100001,5535
1779,1456,1,58071,1417
1780,1456,1,46142,1223
1781,1457,0,100001,4328
1782,1458,0,100001,1852
1783,1458,1,61082,0
1784,1462,1,96963,3110
1785,1462,1,30608,516
1786,1462,1,39603,1507
1787,1462,0,100001,3521
1788,1464,1,13294,0
1789,1465,1,39515,2021
1792,1475,1,35330,227
1793,1475,1,35330,227
1794,1475,1,63558,1409
1795,1476,1,85680,2744
1796,1476,1,68388,3326
```
s_no_baseline.csv
```csv
1814,1499,-1,81077,3275
```

Next: preserve 1862 classified roots; use s.csv,s2.csv,s3.csv in cumulative status map. 531 open. Explore tight-query restrictions for saturated targets (FZO coverage quotient) and avoid expensive whole-layer enumeration by deriving query-specific witnesses; consider the FZR clause implication compression separately. Activity association requires actual own private binding.
