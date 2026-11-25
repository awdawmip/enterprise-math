# EC49FZQ — Projected unsaturated obstruction and union certificate

2026-11-25. Parent EC49FZP at 04c44cde802e0714b123fab47ef3a69a475d84df:research_notes/portable_direct/EC49FZP_MAXIMAL_UNSATURATED_FIBER_ENVELOPE.md. Frozen BRC16943, h=14, m=25; 2393 fourth-level roots. Parent EC49FZP_reproduction.zip: all 36 manifest entries verified (37 files including manifest). fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923, envelope.cpp b1047b0df52701a4fd0edcf7d7ba43bfb856a45f20ed6efa05585b458894792a. Historical researcher EM-DIRECT-23537B, current private binding unconfirmed. Task query r4-20261125-1331-ec49as-read SUCCEEDED, Source 314d551e8e603ed91bb21586358c6c86996c62ba, NO_CANONICAL_PUBLICATION_DIRECTORY; no formal owner projection. Unshared portable continuation, no CLAIM/Result/Review; P000 unchanged.

## Theorem 1: projected maximal layer

Use FZP's genuine binary observation history, common positive anchor and common potential-hole universe C. Fix U with |B_U|<h; F=C minus B_U, p=|F|, b=min(p,h-1-|B_U|). For each rival V let D_V=B_V minus B_U, R_V=U xor V. Retain only rivals with D_V subset F and |D_V|<=b. Define L=union of the retained D_V, l=min(b,|L|). For fixed maximal-layer cardinality b and budget k let A={T:max(p,b+|T intersect U|)+|T minus U|<=k}; T need only range over the union of rival row differences. Then an unsaturated target in this fiber has path certificate cost >k iff there exists Y subset L, |Y|=l, such that every T in A misses some R_V with D_V subset Y.

Proof. By FZP, it suffices to test Z subset F of size b. Rival activation D_V subset Z depends only on Y=Z intersect L. Importantly the cost of each T still uses b, not |Y|; deleting irrelevant coordinates is valid only with that resource retained. For any Z extend its projection to size l within L, which is possible since |Y|<=l. More activated constraints cannot restore feasibility. Conversely every Y of size l is realizable as a projection of a maximal Z: if b<=|L|, choose Z=Y, else extend Y=L by b-|L| columns of F minus L. This proves both directions. Empty L works (one candidate Y=empty); empty A makes the universal condition vacuous. This is exact for the worst unsaturated path certificate, not for the full adaptive strategy.

Candidate count decreases from binom(p,b) to binom(|L|,min(b,|L|)), never increases (each projected candidate has a distinct maximal-Z realization). The simple submask implementation visits at most 2^|L| rather than 2^p, and just one if |L|<=b. In particular if all required columns fit within b, activating all retained rivals is exact. This removes irrelevant free-column identities without removing their payment.

## Theorem 2: minimal union obstruction (proved, not integrated)

For every affordable row set T define the family M_T of inclusion-minimal D_V among retained rivals with T intersect R_V empty. If M_T is empty for any affordable T, no obstruction exists. Otherwise an obstruction exists iff one can choose D_T in M_T for every T in A with |union_T D_T|<=b. An empty A has the empty union as a witness. Proof: an obstructing maximal Z contains at least one missed D_V for each T; replace each by an inclusion-minimal missed requirement contained in it. Conversely extend the union of chosen requirements to a maximal Z of size b in F. Then every affordable T fails. Thus the exact minimum required union cardinality is computed by starting with family {empty}, then for each T taking all unions of current members with M_T, discarding sets of cardinality>b and removing strict supersets. Inclusion dominance is safe because future union is monotone and the sole constraint is an upper bound on cardinality. The final family is nonempty iff obstruction exists. One may keep predecessor pointers to recover actual missed rivals and a maximal target. A cheaper row set whose covered rival set is contained in another affordable row set can be dropped when testing obstruction: failing the larger coverage entails failing the smaller. This recurrence is an alternative to enumerating all maximal projections; no performance claim yet. It is scoped to the same FZP common-universe model.

## Executed experiment

All parent manifest hashes passed. Reused parent code, including exact normalized fiber transitions, necessary row constraints, and independent labeled replay of every successful root. Only the loop below changed. The 690 unresolved roots are reconstructed by loading the five fourth-level CSVs, then updating with retry.csv, next.csv, next2.csv; baseline_next.csv is not an additional result. Select the sorted unresolved IDs, positions [0,45). Node cap 100000 per root. Commands:
    g++ -O3 -std=c++17 projected.cpp -o projected
    g++ -O3 -std=c++17 envelope.cpp -o envelope
    python retry_q.py 0 15 100000 > q.in
    ./projected < q.in > q.csv
    ./envelope < q.in > qbase.csv
    python retry_q.py 15 45 100000 | ./projected > q2.csv
The first 15 roots produced byte-identical CSV (including calls and prune counts) on both algorithms. Control: 14 feasible, 1 capped, 837503 calls, 15790 envelope prunes, 17170 labeled replays; measured elapsed 8.43s projected and 8.54s baseline, single measurement only; no demonstrated general speed improvement. Across 45 distinct roots: 44 feasible, 1 capped (1529), 0 new impossible, 2121420 calls, 54011 envelope prunes, 57277 labeled replays. 77 additional ordered histories. Cumulative 1737 feasible, 10 impossible, 646 unresolved among 2393; ordered histories 3498 feasible, 18 impossible, 1179 unresolved among 4695. M14 remains 25..27. Do not repeat completed roots. Saturated optimizer FZO not yet integrated. Next: integrate/test minimal union obstruction on hard nodes, compare its full cost to the projected loop; continue remaining 646. AUTHOR_PROVED / EXACT_FINITE_REPLAY / NOT_REVIEWED.

## Reproduction delta

Replace the exact parent block starting with '   for(int z=freeMask;' through its closing brace immediately before the enclosing support loop's closing brace with:
```cpp
   int relevant=0;for(auto[need,diff]:rivals)relevant|=need;
   int layer=min(b,pc(relevant));
   for(int z=relevant;;z=(z-1)&relevant){
     if(pc(z)==layer){
       bool feasible=false;
       for(int t:allowed){bool ok=true;for(auto[need,diff]:rivals)
         if(!(need&~z)&&!(diff&t)){ok=false;break;}
         if(ok){feasible=true;break;}}
       if(!feasible){++envelopePrunes;return mem.emplace(key,-1).first->second;}
     }
     if(!z||layer==pc(relevant))break;
   }
```
projected.cpp SHA256 3374be1dfba92e57d6c7df9e5a5d6c2bd014a11a760c581e4f862c54a3343f5f.
retry_q.py:
```python
import csv,json,sys
from gen import physical
files=['fourth_partial.csv','fourth_new.csv','fourth_tail.csv','fourth_tail2.csv','fourth_tail3.csv','retry.csv','next.csv','next2.csv']
d={}
for file in files:
 for row in csv.reader(open(file)):
  i,n,s,c=map(int,row[:4]);assert i not in d or d[i][1]==0;d[i]=(n,s,c)
assert len(d)==2393
roots=json.load(open('fourth.json'))
ids=[i for i,(n,s,c) in sorted(d.items()) if s==0];assert len(ids)==690
lo,hi,cap=map(int,sys.argv[1:]);ids=ids[lo:hi];print(len(ids))
for i in ids:
 n,(r,mask,other),paths,status=roots[i];st=physical([mask,*other],14,r,0);assert len(st)==n
 print(i,n,25,15,cap)
 for u,h in st:print(u,h)
```
retry_q.py SHA256 199ff5a93e5ca3ee04d2226fdf6ac76cba87a7c8298c6dd9c1683e520534ffb8. CSV columns id,n,status,calls,envelopePrunes. q.csv and qbase.csv identical SHA256 b4cb0db3bbd9da53264500054af9ec472dba7cf9b037772cd525bf2571c1fde6:
```csv
1322,1061,1,59785,1198
1326,1064,1,54969,1312
1385,1105,1,81494,644
1417,1140,1,60580,768
1521,1228,1,51429,2306
1529,1237,0,100001,1241
1553,1246,1,68731,2611
1554,1250,1,51176,882
1575,1269,1,60264,1064
1586,1282,1,69710,814
1589,1287,1,74160,1108
1601,1298,1,62037,925
1621,1309,1,15577,558
1622,1315,1,15927,106
1624,1316,1,11663,253
```
q2.csv SHA256 68e0bbe23d2f352ca54658f8e7955d7d07203539fd9669e2ed695d22b360cc37:
```csv
1628,1316,1,11663,253
1630,1317,1,64680,2480
1632,1317,1,17430,282
1636,1318,1,54769,1036
1637,1319,1,39104,1995
1638,1320,1,50852,940
1639,1320,1,50852,940
1640,1323,1,25496,953
1641,1323,1,42038,1380
1642,1325,1,18102,0
1643,1329,1,62108,2760
1647,1331,1,46917,545
1648,1331,1,29791,956
1649,1332,1,53346,1329
1650,1333,1,35588,2347
1652,1334,1,89553,2875
1653,1335,1,55572,2251
1657,1342,1,25822,659
1658,1343,1,27930,268
1659,1347,1,26491,508
1660,1348,1,44508,10
1661,1348,1,12835,471
1662,1354,1,90115,3572
1663,1354,1,90115,3572
1664,1357,1,28601,953
1665,1357,1,31965,1047
1666,1357,1,22648,892
1667,1358,1,69188,1552
1668,1359,1,36940,1395
1669,1360,1,28898,0
```
