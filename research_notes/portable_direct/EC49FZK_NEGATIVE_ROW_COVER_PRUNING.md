# EC49FZK — Negative row cover pruning in the exact support-fiber quotient

2026-11-25. Independent portable continuation of EC49FZJ at 267c54f47de90a327b77a82dd4695104d42aed64 (BRC16943 inherited frozen support family). Topic RS-EC49AS has no canonical task publication directory at current Source f3a8cfcb1bb8ae299920e3dd7d9e2abd69e8e08e per succeeded original request r4-20261125-0730-ec49as-read-v1. No shared CLAIM, Result or Review mutation. Historical author provenance EM-DIRECT-23537B; current private writer binding unconfirmed. Evidence status AUTHOR_PROVED / EXACT_FINITE_SEARCH_AND_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.

## Theorem and proof
The parent uses W(r,j)=1_{r in U}1_{j not in H}, with each active support V carrying the exact fiber B_V subset H subset A_V, |H|<=h. Normalize saturated fibers so their optional set is empty. Let p_U=|A_U minus B_U|. For the minimal state x=(U,B_U), define D_U={V minus U: V strictly contains U, B_V subset B_U subset A_V}. Define lambda_U as the minimum cardinality of a subset N of rows outside U meeting every member of D_U, with lambda_U=0 for empty D_U. Let K_U be the union of every minimum-cardinality such N.

Any decision tree recovering all current states in k additional binary probes has k>=p_U+lambda_U for every active U. Indeed, for every optional column j the state (U,B_U union {j}) is compatible; along the path of x it can only be separated by a probe of j at a row in U, with positive response. These p_U probes have distinct columns. Every same-hole strict superset V in D_U agrees with x on all those positive probes. To distinguish it, a probe must use a row in V minus U and a live column (outside B_U), giving negative response on x. Such probes are disjoint from the p_U positive ones. Their row set hits D_U, so at least lambda_U additional probes are needed. This proves the bound even when the tree is adaptive, since we examine one actual path.

If p_U+lambda_U=k, the first probe must lie in
(U x (A_U minus B_U)) union (K_U x (all columns minus B_U)).
Every probe on the path belongs to one of the two resource classes above, because their minimum costs exhaust the budget. Each negative probe uses one distinct row in a minimum hitting set; consequently its row is in K_U. Intersection of these necessary first-query sets over all tight supports is necessary. Empty intersection is an analytic impossibility certificate. This generalizes the parent's p=k and p=k-1 strict-superset checks to arbitrary negative row-cover costs. The implementation evaluates it for k-p<=3 only (a performance choice, not a hypothesis of the theorem); otherwise it uses the inherited weaker pruning. All non-pruned informative row/column classes are searched, with exact child counts and memoized canonical states. A capped search is UNKNOWN, not NO.

The result operates on the BRC-derived finite support family and retains the exact FZJ column-permutation quotient and reconstruction of physical labels. No assertion about native spatial dynamics or new BRC arithmetic. This is a lower bound on a single-state path, not a sufficient criterion for a global decision tree.

## Executed calculation
Starting with the 102 unknown canonical keys in EC49FZJ symbolic_results.csv, set per-key recursion cap 12000; retain the labeled states and original order. Compiled modified symbolic.cpp using g++ -O3 -std=c++17. All 102 searches returned: 21 YES (11167 labeled states replayed by direct W filtering), 9 exhausted NO, 72 UNKNOWN (cap). Total recursive calls 1122635, including cap-trigger calls. Combined third-level counts: 228 YES, 48 NO, 72 UNKNOWN out of 348 canonical roots. Restored ordered counts: 281 YES, 58 NO, 81 UNKNOWN out of 420. M14 still 25..27; 35/82 finite exceptions exact. No runtime speedup claim, since the cap and prior implementation differ.

Parent symbolic.cpp SHA256 045aa29b9dc5fb27e09db372cafed68ab4deb018d1aae70a0110c8a85fa8e6d4; modified cover.cpp SHA256 67e53e012c5ef53d7ae8c6cc99ff5971fcf86758c42d9d979213b5caa351cc0c. Parent input.txt SHA256 bd940d21570f128c7a64f2a65f27b4a632908f578bbe0cb4fd816f69fe7becbd; cases.json SHA256 fb8de4440701e40967edb587e915b933a6e26393e3241a5bb71908aea7530d30. Filtered remaining.txt SHA256 176558da850d8d15e4343fde18fba647eaf4d0234a83b1aae1bcebb03d625334. Raw cover_results.csv SHA256 02f26380b8988778ae1126fb27ad50a13d20f0b2754e520404b868b85e6b401d.

## Exact reproduction patch
From parent research_artifacts/portable_direct/EC49FZJ/symbolic.cpp replace the block beginning at ' for(int i=0;i<(int)ids.size();i++){int p=free[i]' and ending immediately before ' struct O' with:

```cpp
 // Minimum negative row cover of same-hole strict supersets at each minimal fiber state.
 vector<pair<int,int>> tightNeg;
 for(int i=0;i<(int)ids.size();i++){int p=free[i],u=F[ids[i]],budget=k-p; if(budget>3)continue;
 vector<int> dif;for(int j=0;j<(int)ids.size();j++)if(i!=j&&(B[j]&~B[i])==0&&(B[i]&~A[j])==0&&(F[ids[j]]&u)==u)dif.push_back(F[ids[j]]^u);
 if(dif.empty())continue; int rows=0;for(int z:dif)rows|=z;int best=budget+1,uni=0;
 for(int z=rows;z;z=(z-1)&rows){int c=pc(z);if(c>best||c>budget)continue;bool ok=true;for(int q:dif)if(!(q&z)){ok=false;break;}if(ok){if(c<best){best=c;uni=0;}uni|=z;}}
 if(best>budget)return mem.emplace(key,-1).first->second;
 if(best==budget)tightNeg.push_back({i,uni});}
```

Replace 'if(tight&~R[r])continue;W Y=' with:
```cpp
if(tight&~R[r])continue;bool ok=true;for(auto[i,rows]:tightNeg){int u=F[ids[i]];if(!(((u>>r&1)&&((A[i]^B[i])>>j&1))||((rows>>r&1)&&!(B[i]>>j&1)))){ok=false;break;}}if(!ok)continue;W Y=
```

Generate remaining.txt from the parent symbolic_input.txt by selecting exactly the IDs with result 0 in parent symbolic_results.csv, replacing header cap by 12000, preserving input order and labeled pairs. Alternatively filter parent FZI input.txt directly by the IDs in the CSV below. Both use the parent input generation and immutable support family. First line 102; each header id n m k 12000 followed by n lines u h. Compile and run with assertions enabled. Replay performed by inherited direct physical-label filter. In the raw result rows status 1=YES, -1=exhausted NO, 0=UNKNOWN.

```csv
153,426,1,6704
156,435,0,12001
158,438,1,6922
161,451,1,5500
162,456,1,8753
163,456,1,8753
164,456,1,8753
165,456,1,8753
180,492,1,6786
195,513,0,12001
200,523,1,8264
201,526,1,10315
202,528,0,12001
203,531,1,9367
204,536,1,10867
205,538,0,12001
206,548,1,11773
207,558,0,12001
208,558,0,12001
209,560,1,9721
210,561,1,9878
213,563,0,12001
219,567,1,9185
221,570,1,8392
223,575,0,12001
224,579,0,12001
225,579,0,12001
230,586,0,12001
231,586,1,9946
233,587,0,12001
234,587,0,12001
235,587,0,12001
236,589,0,12001
237,599,0,12001
238,611,0,12001
239,614,0,12001
240,615,0,12001
241,616,0,12001
243,618,0,12001
244,624,0,12001
245,625,0,12001
246,627,0,12001
247,628,0,12001
248,628,0,12001
250,634,1,4115
251,636,0,12001
252,639,0,12001
253,648,0,12001
256,652,1,9530
259,654,0,12001
260,655,0,12001
261,661,0,12001
262,666,-1,11136
264,681,0,12001
265,693,0,12001
266,694,0,12001
269,695,0,12001
270,706,0,12001
272,712,0,12001
273,713,0,12001
274,714,0,12001
278,732,0,12001
279,742,1,11251
280,743,0,12001
281,749,0,12001
282,757,-1,8157
283,759,0,12001
284,759,0,12001
289,787,-1,9675
290,790,0,12001
291,791,0,12001
292,793,0,12001
293,803,0,12001
294,805,0,12001
295,809,-1,6899
296,816,0,12001
297,836,0,12001
298,836,0,12001
299,838,0,12001
300,841,0,12001
301,853,-1,9882
305,878,0,12001
306,879,0,12001
307,879,0,12001
308,880,0,12001
309,888,0,12001
310,890,0,12001
311,892,0,12001
319,956,-1,6420
320,959,0,12001
323,983,0,12001
327,1007,0,12001
329,1039,0,12001
331,1066,-1,9330
336,1112,0,12001
340,1181,0,12001
341,1188,-1,7479
342,1192,-1,6057
343,1223,0,12001
345,1279,0,12001
346,1279,0,12001
347,1453,0,12001
```

## Next
Only the 72 UNKNOWN keys require continuation at this depth. Generalize the hitting-set certificate to all same-hole competitors by allowing positive rows to be paid by mandatory optional-column probes, and use full mixed-state certificates on saturated fibers. Compare actual pruning at equal caps before claiming efficiency. No full 25-column strategy or exclusion established. Preserve existing verified keys; no repeated full run required.
