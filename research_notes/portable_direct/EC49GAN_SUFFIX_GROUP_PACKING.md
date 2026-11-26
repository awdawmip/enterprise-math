# EC49GAN — Exact suffix-group packing hierarchy and common-root obstruction

2026-11-26. Independent informed continuation of EC49GAM at cc80d9e8ab55adcc36ebb73df2a6ab86469ff6b7:research_notes/portable_direct/EC49GAM_LAST_SIBLING_PACKING.md. Parent reproduction manifest checked. Unchanged frozen BRC16943: fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. The observer is fixed binary unit-cost physical row-column query on full labeled joint states (u,h), positive iff r in u and j not in h. This is an exact finite observer relaxation; no new native dynamics or P000 change.

## Theorem

Let S be a finite distinguishable set under fixed binary queries Q; k>=1. For 1<=h<=k put d=k-h. Let R_{d,j} be the set of nonempty residuals attainable from S by a single common path of at most d-j positive and j negative informative queries. Padding to exactly d bits is symbolic and may use either bit; not a new physical query. Define A_h(R) as the downward-closed family of target subsets identifiable with an actual depth<=h decision tree on R. Keep all competitors, including non-target rivals. Let G_j=union_{R in R_{d,j}} A_h(R). There are binom(d,j) slots of class j, each independently allowing a group in G_j. Define F_h as the family of unions of pairwise disjoint groups assigned to all slots. Empty groups are allowed. For any T subset S define B_{k,h}(T)=max{|T intersect U|:U in F_h}. Then

A_k(S)=F_k subseteq F_{k-1} subseteq ... subseteq F_1 subseteq the individual word-matching feasible family.

Consequently V_k(T)=B_{k,k}(T)<=...<=B_{k,1}(T)<=U_0(T), with all inequalities also holding for any nonnegative state weights (replace cardinality by weight). F_1 is exactly GAM last-sibling packing: the two-state group must be isolated before the final separating query, whereas a singleton is equivalent to having an allowed full-word weight in j,j+1.

Proof: Each real decision tree splits at depth d into groups identified by depth-h suffix trees on the actual residuals; extend a shorter identifying leaf by virtual padding to one slot. Distinct prefixes have disjoint identified target groups. Thus A_k(S) subseteq F_h. For h=k there is one slot, R=S, giving equality. For h+1 to h, each occupied prefix slot may be given a fixed distinct abstract word of length k-h-1 with its required number of negative bits. Choose its witnessing common path and actual suffix tree. If its first suffix query is informative, partition its identified group into the positive and negative child groups and attach each to the corresponding extended word; the child residuals belong to the required reachable classes. If the suffix tree already stops, its identified group is empty or a singleton, and assign it to one extended word using virtual padding. Every new slot is unique and the two children of every group are disjoint. This proves F_{h+1} subseteq F_h, preserving complete target membership rather than just the full-set capacity. Finally F_1 embeds into individual word matching by GAM. Downward closure is retained by removing targets inside each assigned group. Nonnegative weighted inequalities follow from inclusion. The full residuals, not their sizes, determine G_j. No claim of equality between independent abstract slots and a common physical prefix tree before h=k.

Algorithm: compute R_{d,j} by forward sets of exact residual masks, with symbolic padding and informative splits. Compute A_h(R) by the union of child attainable groups across each real split; only maximal elements are needed internally by downward closure. Expand their subsets for disjoint slot packing. With a bitset whose bit index is target mask M, each eligible group g updates dp by dp OR ((dp AND allowed[g]) << g), all groups in one slot reading the old dp. Allowed[g] marks disjoint masks; this is the inherited GAM bitset recurrence. Class capacities are binomial. Cost includes reachability, suffix recursion, and packing of up to 2^n target masks; no end-to-end complexity or speed advantage claimed. The counts of generated groups in output are actual groups constructed until early full-universe saturation, not a full catalog when early exit occurs.

## Executed verification

Code suffix_pack.py at 9219e465e7776e4dc1b5627eed2dd3a540827cb4 (blob d65d59431cdcf0edb7ff9bce07c09348b6cee7ee, matching local Git blob). Independent explicit-set implementation suffix_verify.py at 952877a2137d29e2c6bc1df848bc4a83a316ab31. From GAM archive run python suffix_pack.py 0 180 > gan_pack.json; python suffix_verify.py > gan_verify.json. Raw gan_pack.json SHA256 6acffddd6781ae7ad6d4a5e64376ec7d4b40dc73805312561914e8f8e6a8e69e.

All 180 frozen records, original and +1 budgets: 360 comparisons. h=1 agrees with GAM full capacity and attainable family cardinality. h=2 and h=3 full families checked for nesting as bitsets on each case; true full capacity <= h3 <= h2 <= h1. Exact full-capacity cases 211/236/284 respectively; at original budgets 32/57/105 of 180. h2 strictly improves h1 in 46 cases; h3 strictly improves h2 in 50. Among 2706 known inclusion-minimal obstacles, detected by h1/h2/h3: 234/328/1706; combining h2 with GAL U2 yields 340. h3 rank-wise counts: rank2 182/183, rank4 54/56, rank5 159/371, rank6 133/254, rank7 334/398, rank8 327/568, rank9 218/545, rank10 299/325, rank11 0/6. h2 newly detects rank4 42 and rank7 38. All checks against actual capacities and prior obstacles pass. Separate explicit-set implementation checks all 17,572 target memberships across 239 suffix families in 100 seeded small models; additionally h=k is compared bit-for-bit with GAG's complete recoverable families on all 180 original frozen budgets (2,879,232 membership positions). Zero mismatches. These are author computations, not independent research review.

Node125, n=16,k=4: B1=16, B2=16, B3=14, B4=13. The explicit witness of B3=14 uses positive query mask 48059 with recovered mask 37049 (seven targets) and negative query mask 45232 with recovered mask 20038 (seven disjoint targets). These are different physical query signatures. All 14 unordered root splits with their exact 3-budget capacities are:
[[187,6,7],[221,6,7],[224,3,7],[238,6,7],[255,6,6],[3855,6,6],[4607,7,6],[8191,7,3],[8738,4,7],[8959,7,6],[12079,7,6],[17476,4,7],[17663,7,6],[20303,7,6]].
None permits 7+7; the maximum is 13. Thus the remaining one-unit gap is an explicit shared-root-query compatibility obstruction. All six rank11 obstacles still pass h3, not an exact exclusion. This witness pinpoints where to retain joint query labels instead of independent slot marginals.

Compact complete capacity readouts: base64 then zlib decode. 9198 bytes SHA256 904c6deae380770da855e7f8c23cc2d3aac1baffd1f3d5f7048e28f56b9985fc. First 360 triples (B1,B2,B3) in frozen row/original-plus-one order; next 2706 triples in GAL obstacle order:
eNrtGY3SgiDsKkQxpd7/ab/pEicwBJvUd9dux9GEjf3BIK1113XGmL7vjemgHcfx8XhA536/Q//5fCIF+zimJbM06dt5JOVjl7nQakYWR8f+izL086oMrIq24zBM/ElL10b71q56YWvHATTCltKBk6NjC8RhGOD73E79Zfy0BlwhXRWOtCPyGR3/UFNrrSc9tHBMi0kKzkVKaEk7+vpSPuAZmEvHP8hKsL9d4SqR44Yttc9it31KaM/F2qvNl5GpMZzd8CtYy9Ma6ciN0kcStzQmUVY6/rFNezCcRWMYY2ZL8aMU+dhkBrV7UpyOSOH4hPl1uVzU7QbYNA30mxmQ3jQKEPpKqbbVG5zmth6CIIog2UPKH3jqFRqH7QqaRa1TX4tQvzBURxw9+0QxNFoOTg4KbHLAQWVO0awxpbzzr51CM8hlmQ6yLJp9ohknnMWCwSbCJ3cHqylL2ndeHwEpFGnO/jCG3wXdAuYHP6gIib0lts/44OI2NkZhmxwT4aPUDZA7H/Xu+dhyhztC5y53XEXq9Tm95m3WB1cedQwkfNETOCw3Kn03DFBi1AKkFKQVoN6WgrQg9L56UFr7eeo4n7qf3fZrlJ75qYDuRZRIoYhxyOVI2unHPH5MliexZKvxyyS3PyQSMDZyf8sKZ3HKhgbMTEM6JaeY3y1EMxNE7qZjcm7onAof3as3zo1W2omSexFkci59InkdufIEvj5gCsErBnv9FLouceHEh4qAfapcq8+wVeoK+WW7RJCJmn1he+ftxctWqUysGY0VitXz+/tnMXM4Jj59RhZ7eDH06IUF4Hq9qhnyS6YE5JRSPQP3AJKlCHOmn7lhVtsk339n+8g7reT7ZHFtdvKBK6TXoXeG15iil7ei4v9siYIrr/x6IHLknV3onvofga6UC87FiXe5dUxRREnub0J+FNGr8v84h95RU2+kf89rCtM=

## Fourth-layer exact root progress (inherited GAK C++ only)

g++ -O3 -std=c++17 gak_solver.cpp; python retry_gai.py 56 64 250000 > gan_fresh.in; EM_DENSE=1 EM_FAST=1 EM_WORD=1 solver. Baseline python retry_gai.py 56 64 1200000 > gan_fresh_base.in; EM_DENSE=1 EM_FAST=1 solver with Hall disabled. These eight original OPEN indices were untouched in GAM. Inputs SHA256 fa41f1b1f71cb4b3266e2119a389fb87109b55e7156630a57b3a1c88a3555b3d and f8fdaed9e4d1cfc256350a5fa191c7418f81e4788c3872c9ec0e6e33350a4a5d. Actual raw outputs:
```
1938,1671,-1,25312,0,0,0,149,67,0,67,76,25072,22099
1939,1671,-1,25312,0,0,0,256,67,0,67,76,25072,22099
1940,1672,1,15680,0,0,0,373,92,0,92,139,15467,13116
1946,1682,1,20378,0,0,0,774,201,0,201,334,20087,16716
1947,1684,1,17777,0,0,0,827,202,0,202,335,17580,14817
1948,1684,1,17777,0,0,0,879,202,0,202,335,17580,14817
1949,1684,1,17777,0,0,0,931,202,0,202,335,17580,14817
1950,1687,-1,69556,0,0,0,2855,642,0,642,1823,68889,55858
```
Baseline:
```
1938,1671,-1,35455,1236,0,0,2264,512,0,512,2157,0,0
1939,1671,-1,35455,1236,0,0,2747,512,0,512,2157,0,0
1940,1672,1,24910,218,0,0,3446,631,0,631,2705,0,0
1946,1682,1,30915,838,0,0,7733,1395,0,1395,6474,0,0
1947,1684,1,28826,277,0,0,7942,1404,0,1404,6494,0,0
1948,1684,1,28826,277,0,0,8135,1404,0,1404,6494,0,0
1949,1684,1,28826,277,0,0,8328,1404,0,1404,6494,0,0
1950,1687,-1,116770,1722,0,0,12460,2118,0,2118,9493,0,0
```
Both modes agree on all eight, five YES and three exhaustive NO; positive roots replay all 8406 labeled states per configuration under the inherited solver's replay assertion. Calls 209569 vs 329983. No cap exhaustion. New frontier 1941 YES /40 NO /412 OPEN of 2393. Ordered histories add 12 YES (2+1+5+3+1), 4 NO (2+1+1), hence 3937 YES /67 NO /691 OPEN of 4695. 25<=M14<=27 unchanged. New suffix packing was not integrated into C++.

## Control and continuation

Canonical global snapshot dfc872ec280239a598cd43a1a8f0d636968e7991; project current source 88738ab6d9204eddc193ebcd537b1678ba40752f; applicable policy blobs re-read and unchanged; P000 V5 and ACTIVE worldview maintained. Topic query r4-20261126-1231-ec49as-read SUCCEEDED at 2026-11-26T04:31:56.305411Z on 88738ab6d9204eddc193ebcd537b1678ba40752f, NO_CANONICAL_PUBLICATION_DIRECTORY, no live owner projection. Historical EM-DIRECT-23537B only; current private identity/Activity unconfirmed. No shared CLAIM or substitute identity. Next: retain common query compatibility within selected prefix-slot families, use sharp late suffix bounds only on difficult nodes where their construction cost is justified, and continue fresh roots at original OPEN indices 64 onward. Earlier unresolved cases remain. AUTHOR_PROVED / EXACT_FINITE_SUFFIX_FAMILY_CHECK / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
