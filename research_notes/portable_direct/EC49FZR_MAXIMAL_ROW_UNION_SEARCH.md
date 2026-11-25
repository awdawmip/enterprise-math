# EC49FZR — Maximal affordable row sets and adaptive minimal-union obstruction search

2026-11-25. Parent FZQ at 029c47d9714f2124e7378c5c403828dc745b1444:research_notes/portable_direct/EC49FZQ_PROJECTED_UNSATURATED_OBSTRUCTION.md. Frozen BRC16943, h=14, m=25, fourth-level budget 15. Reused FZQ reproduction archive, checked SHA256SUMS locally. 2393 roots; parent 1737 YES, 10 NO, 646 open. Historical contributor EM-DIRECT-23537B; current private writer binding not established, no identity adoption. Exact task read r4-20261125-1432-ec49as-read SUCCEEDED, Source bca2d0951acf274c938b645a3c7879d179bad841, NO_CANONICAL_PUBLICATION_DIRECTORY (not an owner projection). Independent portable derivation and artifact, no shared CLAIM/Result/Review. P000 unchanged.

## Theorem: maximal affordable row reduction and exact adaptive union recurrence

Use FZQ assumptions: genuine observation history, common positive anchor, common possible-hole universe, fixed U and maximal unsaturated layer b. F free columns, p=|F|. Retain rivals V with D_V subset F, |D_V|<=b, R_V=U xor V. A = {T subset union R_V : max(p,b+|T intersect U|)+|T minus U|<=k}. Define M_T as the inclusion-minimal D_V for rivals missed by T, i.e. R_V intersect T empty. An obstruction exists iff some Z subset F of size <= b contains a member of every M_T (FZQ). Any such Z extends to the maximal layer.

The budget cost is monotone under row-set inclusion, so A is downward closed. It suffices to retain inclusion-maximal T in A: if T subset T', every rival missed by T' is missed by T. Each affordable T extends to a maximal affordable T' by finiteness. Hence the conjunction over maximal T is equivalent to the original conjunction. Maximality can be tested by checking every one-element extension within the union of R_V. If A is empty the conjunction is vacuous; if any retained M_T is empty there is no obstruction.

For a current union S, |S|<=b, define F(S) to be the predicate that an extension Z of S, |Z|<=b, meets all retained clauses. A clause is met exactly if some D in it is contained in S. If all clauses are met, F(S)=true. Otherwise choose any unmet clause M; let G be the inclusion-minimal members of {S union D : D in M, |S union D|<=b}. Then
F(S) = OR_{G' in G} F(G').
Proof: every feasible extension must contain some D of M and hence a candidate S union D; that candidate contains a minimal G' in the finite family. Conversely every successful child extends S and meets all clauses. Since M is unmet, each child strictly increases |S|; recursion terminates within b increases. A failed union is safe to memoize independent of which clause was chosen. An empty child family proves F(S)=false. Choosing the clause with fewest minimal children is an ordering heuristic, not a mathematical restriction. This proves exact equivalence to FZQ projected maximal-layer enumeration, for the path-certificate obstruction only.

Additional reusable rule (proved, not implemented separately): a clause M implies clause N on all Z of size <=b iff every D in M with |D|<=b contains some E in N. Necessity: take Z=D; sufficiency: inclusion. Thus entire conjunctive clause families can also be reduced by this implication, independently of maximal row reduction. When restricting to size exactly b, this criterion remains sufficient; necessity is stated only for size <=b.

## Implementation and computation

Replace the block in projected.cpp starting at "   int relevant=0;" and ending just before the closing brace followed by " struct O" with the following exact algorithm (same gate k<=8, q<=2, b>0). All other solver and independent labeled-state replay code is unchanged. C++17.

```cpp
   // Minimal-union search over maximal affordable row sets.
   vector<vector<int>> families;
   for(int t:allowed){
     bool maximal=true;
     for(int bits=rows&~t;bits;bits&=bits-1){int v=t|(bits&-bits);if(max(p,b+pc(v&u))+pc(v&~u)<=k){maximal=false;break;}}
     if(!maximal)continue;
     vector<int> f;
     for(auto[need,diff]:rivals)if(!(diff&t))f.push_back(need);
     sort(f.begin(),f.end(),[](int a,int b){return make_pair(pc(a),a)<make_pair(pc(b),b);});
     vector<int> g;for(int d:f){bool dominated=false;for(int e:g)if(!(e&~d)){dominated=true;break;}if(!dominated)g.push_back(d);}
     if(g.empty()){families.clear();families.push_back({});break;}
     families.push_back(move(g));
   }
   // No affordable T: empty conjunction, hence an obstruction.
   unordered_set<int> failed;
   auto obstruction=[&](auto&& self,int z)->bool{
     if(failed.count(z))return false;
     vector<int> best;bool pending=false;
     for(const auto& f:families){
       bool satisfied=false;for(int d:f)if(!(d&~z)){satisfied=true;break;}
       if(satisfied)continue;
       vector<int> opts;for(int d:f)if(pc(d|z)<=b)opts.push_back(d|z);
       if(opts.empty()){failed.insert(z);return false;}
       sort(opts.begin(),opts.end(),[](int a,int b){return make_pair(pc(a),a)<make_pair(pc(b),b);});
       vector<int> g;for(int d:opts){bool dominated=false;for(int e:g)if(!(e&~d)){dominated=true;break;}if(!dominated)g.push_back(d);}
       if(!pending||g.size()<best.size()){best=move(g);pending=true;}
     }
     if(!pending)return true;
     for(int v:best)if(self(self,v))return true;
     failed.insert(z);return false;
   };
   if(obstruction(obstruction,0)){++envelopePrunes;return mem.emplace(key,-1).first->second;}
```

Input selection: extend retry_q.py's files list by 'q.csv','q2.csv' and change assertion len(ids)==690 to len(ids)==646; save retry_r.py. Compile projected.cpp and union.cpp with g++ -O3 -std=c++17. Run python retry_r.py 0 12 100000 > r.in, 12 42 100000 > r2.in, 42 72 100000 > r3.in. Run union on all three and projected on first two. Both comparison CSV pairs were byte-identical (42 roots: 38 YES, 3 NO, 1 capped; 1,243,390 calls and 38,049 envelope prunes). Runtime seconds union/projected: 6.67/6.67, 9.64/9.64. No speedup demonstrated. Third run 17.49 s. All 65 new YES roots replayed against physical labels (90,418 target states); 3 NO from exhaustive solver termination; 4 capped remain open. Total new unique roots 72, calls 2,511,169, envelope prunes 78,058. Prior solved roots not recomputed. New totals YES 1802, NO 13, open 578; ordered histories YES 3623, NO 25, open 1047. Inventory still 25<=M14<=27. No full adaptive root closure yet. New result is an exact local obstruction algorithm and finite branch evidence, author-proved/not independently reviewed.

Raw CSV below, fields root,n,status,calls,envelopePrunes; status 1 verified feasible, -1 exhaustive exclusion, 0 cap. r.csv and r2.csv also equal their baseline CSVs.

r.csv:
```csv
1529,1237,0,100001,1241
1670,1360,1,41409,2053
1671,1360,1,49234,1577
1672,1369,1,55323,2200
1673,1371,1,21671,940
1674,1371,1,21671,940
1675,1371,1,45691,1802
1676,1371,1,48216,868
1677,1372,1,27202,1356
1678,1372,1,44127,435
1679,1372,1,12731,270
1682,1373,1,27399,837
```
r2.csv:
```csv
1683,1373,1,22317,1488
1684,1373,-1,35288,1865
1685,1373,-1,35288,1865
1690,1373,1,12779,261
1691,1373,1,12779,261
1693,1373,1,12779,261
1696,1373,1,12779,261
1698,1373,1,12779,261
1700,1373,1,12779,261
1701,1377,1,33159,747
1702,1379,1,49161,1682
1703,1382,1,28760,503
1704,1382,1,81372,1348
1705,1383,1,82968,2348
1709,1384,-1,42182,3134
1710,1384,1,24947,460
1711,1384,1,11839,363
1712,1384,1,11839,363
1713,1384,1,13347,607
1714,1384,1,22319,346
1715,1384,1,22319,346
1716,1384,1,13347,607
1717,1384,1,13347,607
1718,1384,1,22319,346
1719,1384,1,13347,607
1720,1386,1,12184,340
1721,1393,1,25018,0
1722,1395,1,17990,627
1723,1395,1,19394,738
1724,1395,1,17990,627
```
r3.csv:
```csv
1725,1397,1,12883,0
1726,1397,1,12883,0
1727,1397,1,12883,0
1728,1397,1,12122,374
1729,1398,1,19412,482
1730,1399,1,29335,1685
1731,1399,1,29335,1685
1732,1401,0,100001,6285
1733,1401,1,46881,2817
1734,1404,1,37104,1041
1736,1407,1,23352,178
1737,1408,1,67494,534
1738,1408,1,38715,409
1739,1408,1,18944,340
1740,1408,1,38715,409
1741,1408,1,28853,1262
1742,1410,1,47160,2476
1743,1410,1,47160,2476
1744,1410,0,100001,4865
1745,1411,0,100001,1813
1746,1412,1,20863,0
1747,1412,1,20863,0
1748,1413,1,13973,739
1749,1416,1,84466,767
1750,1416,1,49899,127
1751,1421,1,95756,3924
1752,1422,1,31236,804
1753,1423,1,39396,2736
1754,1423,1,50201,1708
1755,1424,1,37892,73
```

## Continuation

Do not recompute 1815 classified fourth-level roots. Remaining 578: use r.csv,r2.csv,r3.csv in cumulative status map. Next: test clause implication reduction and cheaper selection of tight saturated certificate witnesses; benchmark before claiming acceleration. Reuse FZO coverage quotient and FZQ projected enumeration, which remains an equal-cost baseline. Preserve original branch histories and physical replay. Activity association remains pending private session binding; do not adopt a historical SID or replay rejected recovery.
