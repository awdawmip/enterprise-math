# EC49FZL — Complete third-level classification and tight full-row residual pruning

2026-11-25. Independent portable continuation of EC49FZK at f1f35e9a3dbaa0cb3ca5544f825d4b5ea4896fda, theorem report dc8b115308cd79803a939cda30e8db2388cd4bbb. Frozen BRC16943 family, h=14, m=25, unchanged. Historical provenance EM-DIRECT-23537B; current private writer binding unconfirmed. Topic read r4-20261125-0830-ec49as-read-v1 SUCCEEDED at e680d720f5f8a9de691f1b62e09805812b358f72: NO_CANONICAL_PUBLICATION_DIRECTORY (directory observation, no owner authority). No CLAIM, Result or Review mutation.

## Tight full-row certificate

Reuse exact fiber B_U subset H subset A_U, |H|<=h, normalized when saturated, and query W(r,j)=1_{r in U}1_{j not in H}. At x=(U,B_U), p=|A_U minus B_U|, let D be all nonempty U XOR V for active V!=U with B_V subset B_U subset A_V. Write R for union of D. Define L(U)=min over T subset R hitting every D of max(p,|T intersect U|)+|T minus U|. Empty D gives L=p. Each free column has a one-column hole-addition competitor requiring a separate positive probe on that column (normalization ensures an optional column really is free). Each same-hole competitor must be separated on a live column and a differing row. Along the actual path of x, select all informative positive/negative rows in R as T. The positive probe count is at least max(p,|T intersect U|); the negative count is at least |T minus U|. Thus k>=L(U) for any recovering decision tree. This reuses FZH's local certificate and extends FZK's directly computable negative-only bound to all same-hole competitors, not a new full-certificate equality claim.

If L(U)=k, let E be the union of T intersect U over minimizing T with |T intersect U|>p, and N the union of T minus U over all minimizing T. A necessary first-probe set is
 (U x (A_U minus B_U)) union ((E union N) x ([m] minus B_U)).
Indeed a length-k actual path must attain both resource inequalities for its own T. If |T intersect U|<=p, all its positive probes must cover distinct optional columns. Otherwise every positive probe accounts for a distinct row in T; extra probes can occur on any live column. Each negative probe accounts for a distinct negative row in T. Intersect these necessary sets over all tight U. Empty intersection proves impossibility. This is a conservative union, not a sufficient decision-tree criterion. Implementation evaluates the full-row bound only for k-p<=3 as a performance choice. Inherits exact column-permutation quotient, complete informative query enumeration and child counts, and physical-label replay. Caps yield UNKNOWN.

## Executed searches

Input hash parent cover.cpp 67e53e012c5ef53d7ae8c6cc99ff5971fcf86758c42d9d979213b5caa351cc0c; remaining.txt 176558da850d8d15e4343fde18fba647eaf4d0234a83b1aae1bcebb03d625334; cover_results.csv 02f26380b8988778ae1126fb27ad50a13d20f0b2754e520404b868b85e6b401d; cases.json fb8de4440701e40967edb587e915b933a6e26393e3241a5bb71908aea7530d30. These match the previous recorded frozen evidence.

Compile patched fullrow.cpp with g++ -O3 -std=c++17 (assertions enabled). Filter only the 72 prior status-0 IDs, retain labeled pairs and order, replace each header cap. At cap 12000 all 72 remained UNKNOWN (864072 calls, each 12001); this equal-cap trial provides no increased classification rate. At cap 50000, 35 YES, 29 exhausted NO, 8 UNKNOWN, 1972114 calls and 21816 replayed states. At cap 250000 on those 8 only, 3 YES, 5 exhausted NO, 449414 calls. No cap in the final classification. Total 38 new YES, 34 new NO; 23767 newly replayed labeled states. No speedup claim; no old closed keys rerun. All 348 canonical roots now 266 YES / 82 NO / 0 UNKNOWN, corresponding to 326 YES / 94 NO out of 420 ordered histories. This closes the entire third-level classification, not the full decision tree. M14 remains 25..27, finite exceptions exact 35/82.

### Reproduction patch

From parent cover.cpp replace the block beginning with ' // Minimum negative row cover' and ending immediately before ' struct O' by:

```cpp
 // Full same-hole row certificate for minimal fiber states.
 vector<tuple<int,int,int>> tightRows;
 for(int i=0;i<(int)ids.size();i++){int p=free[i],u=F[ids[i]],budget=k-p; if(budget>3)continue;
 vector<int> dif;int rows=0;for(int j=0;j<(int)ids.size();j++)if(i!=j&&(B[j]&~B[i])==0&&(B[i]&~A[j])==0){int z=F[ids[j]]^u;dif.push_back(z);rows|=z;}
 if(dif.empty())continue; int best=k+1,extra=0,neg=0;
 for(int z=rows;z;z=(z-1)&rows){int pos=pc(z&u),c=max(p,pos)+pc(z&~u);if(c>best||c>k)continue;bool ok=true;for(int q:dif)if(!(q&z)){ok=false;break;}if(ok){if(c<best){best=c;extra=neg=0;}if(pos>p)extra|=z&u;neg|=z&~u;}}
 if(best>k)return mem.emplace(key,-1).first->second;
 if(best==k)tightRows.push_back({i,extra,neg});}
```

Replace the exact substring
`for(auto[i,rows]:tightNeg){int u=F[ids[i]];if(!(((u>>r&1)&&((A[i]^B[i])>>j&1))||((rows>>r&1)&&!(B[i]>>j&1))))`
with
`for(auto[i,extra,neg]:tightRows){int u=F[ids[i]];if(!(((u>>r&1)&&((A[i]^B[i])>>j&1))||(((extra|neg)>>r&1)&&!(B[i]>>j&1))))`.

fullrow.cpp SHA256 3d1ae2d75991d5b6cd9a131f38068f27d04a1e2fc2abccf6e6673893e00f9d0b.
Input unknown_12000.txt e256571c62eb320fee3c953bb25d46d09fbcbf1140c445b62d4de6b3a778d189; output all 72 lines id,n,0,12001, hash 45f3f8f0a1c327a0a222887b556c5382ba3f52502155358a086794ccddef50cc.
Input unknown_50000.txt 9e81c6bdcd35259fbe5ca69212628a4bf543a255a683a3d8e928405a1fd85c90. Output fullrow_50000.csv hash 53569e52b653fed647661252791726c4c6eaaefb709401ba4e1bce82fd4f3cfe:

```csv
156,435,1,13397
195,513,1,20729
202,528,-1,27433
205,538,1,30501
207,558,1,14273
208,558,1,13848
213,563,1,17960
223,575,1,14764
224,579,1,14781
225,579,1,21526
230,586,1,14780
233,587,1,16459
234,587,1,20273
235,587,1,14325
236,589,1,22473
237,599,1,16445
238,611,1,21902
239,614,1,26748
240,615,1,40203
241,616,1,35922
243,618,0,50001
244,624,1,14908
245,625,1,29194
246,627,1,26930
247,628,-1,42323
248,628,1,41919
251,636,1,12196
252,639,0,50001
253,648,1,20123
259,654,1,14731
260,655,1,15954
261,661,1,40520
264,681,1,28461
265,693,0,50001
266,694,0,50001
269,695,1,28917
270,706,1,46539
272,712,1,28064
273,713,-1,15779
274,714,-1,25854
278,732,-1,15716
280,743,-1,14222
281,749,1,43322
283,759,-1,38226
284,759,-1,23746
290,790,1,22533
291,791,-1,22099
292,793,-1,45809
293,803,-1,42926
294,805,0,50001
296,816,0,50001
297,836,1,34748
298,836,-1,21142
299,838,-1,34134
300,841,0,50001
305,878,-1,18109
306,879,-1,22012
307,879,-1,20333
308,880,-1,27942
309,888,-1,13848
310,890,-1,20290
311,892,-1,19036
320,959,-1,28677
323,983,-1,41168
327,1007,0,50001
329,1039,-1,31724
336,1112,-1,15389
340,1181,-1,17854
343,1223,-1,13328
345,1279,-1,16903
346,1279,-1,16323
347,1453,-1,39393
```

Input last8.txt cdb450bc2d7c7e96e1281f9f5782b35b7f527b644988200d70df1aea86d15bcf (filter status 0 from 50000 and change cap to 250000); output last8.csv 623ad7f3cb3148e502842f45416cb612cd6a7cdbfc3c9cc8e5f22187dbd060f6:
```csv
243,618,1,52074
252,639,1,54258
265,693,-1,51960
266,694,1,55508
294,805,-1,53875
296,816,-1,63436
300,841,-1,66605
327,1007,-1,51698
```

## Fourth level initial census

Use FZI gen.py, cases.json and FZI results.csv/results2.csv/results3.csv, FZJ symbolic_results.csv, FZK cover_results.csv, and the two new result CSVs above. Union nonzero statuses, asserting no contradictions and 348 keys. For each of the 326 ordered YES paths (case record paths), start with MS in gen.py and remove each of its 3 observation bits in sequence by selecting first equal mask, as in FZI generator. Enumerate types(p) for the fourth deletion, form canonical key (r,z[j],sorted remaining masks). For each key generate the exact support fibers: active U iff r in U, mask disjoint U, required holes B={j:mask_j intersects U} with |B|<=14. A=all columns except distinguished positive column, or A=B if |B|=14. Compute exact counts by binomial sums. Apply capacity 2^15 and the above certificate at k=15 including tight-set intersection. Executed result: 4695 ordered extensions, 2393 distinct keys; all counts in 118..3794, none rejected by capacity or full-row root certificate, all 2393 OPEN. This is an exact input census, not a feasibility result. Next: classify the fourth-level roots, exploit compressed full mixed-state certificate on saturated fibers instead of assuming root row bound suffices. No prior closed root needs recomputation.

Evidence grade AUTHOR_PROVED / EXACT_FINITE_SEARCH_AND_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED. P000 unchanged; finite BRC-derived support/query scope only.
