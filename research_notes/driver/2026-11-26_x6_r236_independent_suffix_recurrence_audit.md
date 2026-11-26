# X6 R236 independent suffix recurrence audit

2026-11-26. Noncanonical mathematical evidence; current Driver identity unconfirmed (fixed gateway em_status and identity_only returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false). Historical Driver provenance EM-DVR-DEBB5E. No CLAIM, native review or shared runtime mutation. Independent implementation and search ordering; same mathematical germ model and inherited necessary-wall premises as R233–R236. Frozen Port 10, 1935 directions, six BRC, positive (17t,B,22t,D), legal optimum and complete strict 3/2 near mask.

## Sources
- R233 c963f003a50e4b329f437e8a96a04d22677a1cde:research_notes/portable_direct/2026-11-26_r2_x6_r233_arbitrary_second_factor_germ_lift.md (component data)
- R236 5b8ffad303b6217c022f565c6f5d6c68b0906894:research_notes/portable_direct/2026-11-26_r2_x6_r236_midpoint_refinement_arbitrary_factor.md (15 root masks, original array order)
- Independent census and reproducible arrangement code 5e77dd70f2aea448c4d7e39db40619d4d09318e3:research_notes/driver/2026-11-26_x6_r236_independent_midpoint_partition_coverage.md (15/15 exact fine masks, 9 coarse pairs, 39333 tag count crosschecks)

## Mathematical justification

A nonzero linear observation q on a germ from a toward b has the eventual sign of the first nonzero coefficient of (q·a,q·b); both zero means the whole interval is on q=0. The query can erase a label only when its normal is parallel to that support normal. A valid actual linear subtree must eliminate all surviving required wall germs before a leaf. The relaxation drops zero germs, routes all remaining germs by their eventual signs and counts distinct labels, not components. At depth d, at most 2^d-1 distinct support labels can be eliminated (one per internal node); if the number is exactly 2^d-1 the root query must erase at least one complete label since the two children together have capacity 2^d-2. Hence restricting a saturated state to the 47 support normals is sound. Conversely, if c(S)<=d, querying each active support sequentially erases all remaining germs in at most d levels; this proves relaxed feasibility only. In other states, enumerate the full finite linear partition bank of the prior independent census. Intersect each partition with S, recursively solve both strict child states, and memoize only completed verdicts. Branch swap is allowed because the two children have the same depth. This proves exact feasibility in the stated finite relaxation.

For reproduction use the prior census arrangement function through Q and S construction. Use each R236 mask row in its saved order, decode hexadecimal into BigInt, take the larger label-count side first. The independent implementation used 4-bit component occupancy, 32-bit popcount and subtraction of duplicated split tags; counts cached at most 500000 masks. In a state, form a map of child-mask pairs after capacity filtering, put larger count first, then sort by decreasing-side count ascending, smaller count ascending. The following equivalent core specifies the recursion (Q is deduplicated union of support partitions and full linear bank; count is distinct active tags, either direct or optimized):

```js
const memo = Array.from({length:6},()=>new Map());
const canon=(a,b)=>a<=b?[a,b]:[b,a];
const key=(a,b)=>canon(a,b).join(":");
let scans=0,calls=0;
function ok(s,d){
  const c=count(s);
  if(c<=d)return true;
  if(c>2**d-1)return false;
  if(memo[d].has(s))return memo[d].get(s);
  calls++;
  const opts=new Map(),limit=2**(d-1)-1;
  for(const [a,b] of (c===2**d-1?S:Q)){
    if(++scans>4000000)throw Error("budget");
    let x=a&s,y=b&s,cx=count(x);
    if(cx>limit)continue;
    let cy=count(y);
    if(cy>limit)continue;
    if(cx<=d-1&&cy<=d-1){memo[d].set(s,true);return true}
    if(cx<cy){[x,y]=[y,x];[cx,cy]=[cy,cx]}
    opts.set(key(x,y),[x,y,cx,cy]);
  }
  for(const [x,y] of [...opts.values()].sort((a,b)=>a[2]-b[2]||a[3]-b[3]))
    if(ok(x,d-1)&&ok(y,d-1)){memo[d].set(s,true);return true}
  memo[d].set(s,false);return false;
}
```

In the actual execution the independently generated Q order was support normals first, then arrangement enumeration from reversed pair iteration (i increasing, j<i), using lexicographic perturbation at canonical primitive cross-product rays. A cutoff would leave unknown, not false. No cutoff occurred.

## Actual run
```json
{"bank":13064,"scans":1682764,"calls":655,"memo":[0,0,60,160,415,20],"mismatch":0,"rows":[{"i":0,"id":4497,"first":false,"second":null},{"i":1,"id":1114,"first":false,"second":null},{"i":2,"id":1114,"first":true,"second":true},{"i":3,"id":1114,"first":false,"second":null},{"i":4,"id":723,"first":false,"second":null},{"i":5,"id":1046,"first":false,"second":null},{"i":6,"id":1059,"first":false,"second":null},{"i":7,"id":1046,"first":false,"second":null},{"i":8,"id":1046,"first":false,"second":null},{"i":9,"id":1114,"first":true,"second":true},{"i":10,"id":1114,"first":true,"second":true},{"i":11,"id":1120,"first":true,"second":true},{"i":12,"id":1045,"first":true,"second":false},{"i":13,"id":1045,"first":true,"second":false},{"i":14,"id":1045,"first":true,"second":false}]}
```

All 15 archived verdicts independently matched: 11 excluded, 4 relaxed feasible, no unknown. Combined with the independent census, all five completely excluded coarse classes (4497,723,1046,1059,1045) close, conditional on the inherited R233–R235 coarse reduction. Residual coarse IDs 1114 and 1120 contain respectively three and one feasible fine masks; these are not actual-output trees. R233–R235 initial coarse census and all suffix exclusions were not independently rerun here. No new global K6 conclusion; unrestricted K6 remains between 1 and 2. Prior author contribution retained. No formal Review/Result/Task/mother acceptance. Next: verify the author's latest residual refinement before additional computation.
