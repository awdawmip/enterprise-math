# X6 R282 — exact sorted-hull merge and sixth-pencil continuation

2026-11-28. Independent informed TASK_RESEARCH; author proof and author computation, NOT_REVIEWED. P000 V5 / global V4, ACTIVE worldview, native joint relation and residual fidelity retained. This is auxiliary coefficient algebra for a frozen BRC observer, not a native spatial plane or native dynamics. Exact native lookup r2-20261128-0113-x6-read SUCCEEDED 2026-11-27T17:13:09.362576Z Source ba127542afbf1a083d5c75ed9ad2ff69e11305c0, NO_CANONICAL_PUBLICATION_DIRECTORY, not a live owner projection. Own researcher binding unconfirmed. No CLAIM/Result/Review/shared state mutation; Activity association pending.

## Frozen sources and scope
- R247: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md
- R275: 001076e59298e45715cb58c87ab3395c53d005a8:research_notes/portable_direct/2026-11-27_r2_x6_r275_monic_block_compression_and_strict_prefix.md
- R276: 33fba542db5f810e803d770b7046b5e26ac1ebb9:research_notes/portable_direct/2026-11-27_r2_x6_r276_strict_fifth_pencil_packed_frontier.md
- R277: a1df3c1aa315909d8c109ef8551f24a460a44b1f:research_notes/portable_direct/2026-11-27_r2_x6_r277_incremental_slope_projection_sixth_prefix.md
- R280: 3366eecf953f9943f8a9d88b36279f221cb1e1c7:research_notes/portable_direct/2026-11-27_r2_x6_r280_joint_affine_envelope_sixth_prefix.md
- R281: eec7a9a75994f4bbf4c4ca0e95f1ac88b7c17ddb:research_notes/portable_direct/2026-11-28_r2_x6_r281_active_pair_sweep_sixth_prefix.md
Same Port 10, 1935 integer directions, six-pair BRC, 47 support labels, 51 endpoints, 98 oriented germs, 2225 suffix partitions. Inherits necessary wall and complete linear suffix assumptions of R247. Strict c=1 six multipoint pencil words only. Prior R281: 292300/667787 visits, 2104 survivors, next [3700,0].

## Lemma — sorted hull update without sorting old lines
Let I be the exact open projection of a strict affine system and let O be the retained slope-sorted lower max envelope rows (or reversed upper max envelope rows), after safe restriction to I by R280. For any finite new rows N, sort only N by slope ascending and intercept descending at equal slope. Merge O and sorted N in that same order; retain the highest intercept for each equal slope. Apply the ordinary max-envelope monotone stack, using exact rational switch events, popping a row when its new intersection is at or before its own activation. The resulting max equals max(old envelope,new rows) at each f in I. Proof: O equals the previous envelope on I, so taking max with new functions preserves equality; merging is simply the same sorted order as a fresh joint sort, except irrelevant order among exactly identical functions. Equal slope lower intercept is never maximal; the stack removes a line only when its activation interval is empty, including single-point ties where adjacent retained functions have the same value. By R281 sweep, intersect the two merged envelopes and flat rows with the retained I; this exactly recovers the new projection. Keep the new envelopes as well as I, not merely I. Consequently all later strict or arbitrary additional intersections of this represented joint feasible set remain exact. Original endpoint words, germ masks, and different branches remain distinct. This lemma covers strict systems; retaining merely value envelopes in mixed strict/weak systems may lose active strict flags at ties and needs a separate proof.

For p retained rows and k new rows, comparison count O(k log(k+1)+p+k) for one hull update, plus pair sweep O(p'+m'). Old sorted rows need not be sorted again. Exact rational bit cost, row generation, prior prefix reconstruction, branch copying, and capacity recursion remain charged; no total runtime speedup claimed. If hull rows were truncated on old I, the merged envelope outside I need not equal the original; the stored I must never be discarded.

## Actual exact calculations
Batch A [3700,4200): R281 scan directly, no triple diagnostic, first 100 algebra checks compared with R275 complete elimination. Full result (except serialized survivors):
```json
{"hist":{"direct":19019,"alg":18711,"recursive":1240,"surv":530,"visits":39500,"checkedAgainstOld":100},"checks":3479294,"next":[4200,0],"stats":{"prefixes":500,"rawRows":38252,"hullRows":2262,"pairRows":2633,"hullIntersections":66994,"pairDominanceTests":258431,"scanPairs":99368,"scanIntersections":5717514,"scanMaxPairs":142473},"partial":false}
```
Batch B [4200,4700), plus any explicitly reported partial prefix: sorted-merge implementation compared against ordinary R281 scan on every algebra-tested extension; compare existence, exact projected endpoints, and retained ordered row lists (as implemented). First 100 also compared to R275 complete elimination. Exact BigInt.
```json
{"hist":{"direct":19773,"alg":17756,"recursive":1841,"surv":130,"visits":39500,"checkedAgainstOld":100},"checks":5634011,"next":[4700,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":500,"rawRows":26937,"hullRows":2035,"pairRows":2350,"hullIntersections":45970,"pairDominanceTests":178818,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":146196,"scanIntersections":4907330,"scanCompared":0,"scanRawPairs":0,"scanHullPairs":0,"scanMaxPairs":240478,"mergeCompared":19727,"mergeSort":13402389,"mergeComparisons":1772569,"mergeIntersections":4907330},"partial":false}
```
Bank verification: strict index order, bounds, positive <=79-bit masks, popcounts 530 and 130 respectively. The classification is a necessary-condition filter, not a feasible depth-six tree certificate.

Batch A bank:
```text
3704:100000
3705:100000
3748:84000000000000000
3751:84000000000000000
3819:1100000000000000000
3821:1100000000000000000
3846:40000000000
3872:1c
3873:1c
3874:10
3875:10
3876:e
3877:c
3878:e
3879:c
3881:6
3882:4
3883:6
3884:4
3892:fc
3893:10
3894:70
3895:10
3896:1c
3897:10
3898:1c
3899:10
3900:c
3902:c
3914:f0
3915:40
3929:f0
3930:40
3939:40
3940:40
3945:40000
3979:29100000000000000000
3984:180781c038010
3985:180180c018010
3986:d800000000000000000
3987:381c038010
3988:80180c018010
3992:52210418180c0300600f
3993:52210008080401002007
3994:1
3995:e
3996:6
4001:4
4004:4
4005:40300e01f
4006:40300e007
4007:1c
4008:4
4009:40100600f
4010:401006007
4011:f
4012:7
4016:2007
4017:1
4018:2007
4019:1
4021:2000
4029:e01f
4030:600f
4031:201f
4032:f
4033:e007
4034:6003
4035:6007
4036:2003
4050:e01f
4051:600f
4052:601f
4053:600f
4054:6000
4056:6000
4066:c008
4067:c008
4068:c008
4069:c008
4082:381c038000
4083:208180180c018000
4085:38000
4086:180c018000
4087:8180c00000001
4088:80000000003
4089:1
4090:81c01006001
4091:10008180c01006001
4093:2001
4094:80000002001
4095:1
4099:f006001
4100:10c08181c07002007
4101:1
4102:7
4104:1002001
4105:10008180c01002003
4106:2001
4107:2003
4111:10000
4116:3002001
4117:c08181c07002007
4118:2001
4119:2007
4124:10000
4131:806000000
4133:2000000
4147:800000000
4150:400000000000001
4151:400000000000001
4152:410000000000000
4153:800000000
4166:12231c70e00000000001
4167:231c78f00000000001
4168:21040800000000000
4169:4020000000
4177:2220000000000000001
4178:230000000000000001
4183:8000000000000000000
4184:28000000000000000000
4187:fee7000000000000000
4188:fec0000000000000000
4189:221000000000000000
4195:1
4196:fc00000000000000000
4197:d000000000000000000
```
Batch B bank:
```text
4203:800000000000000
4204:2010800000000000001
4205:2000000000000000001
4206:10c00000000000001
4207:1
4215:10000000000000001
4216:10000000000000001
4217:10000000000000001
4218:10000000000000001
4220:1
4223:2c000000000000000000
4224:7c000000000000000001
4225:1
4230:10
4260:40000
4262:40
4300:808000000000
4301:c0c000000000
4329:1000000000000000
4352:1dc0000000000000000
4354:cc0000000000000000
4357:3e000000000000000000
4359:3e000000000000000000
4361:c000000000000000000
4364:9900000000000000000
4431:8c6000000000000000
4433:ce6000000000000000
4437:8000000000000000
4438:8000000000000000
4442:8000000000000000
4447:180000000000000000
4466:dd80000000000000000
4470:dd80000000000000000
4475:1980000000000000000
4477:1980000000000000000
4486:4
4491:1c
4492:c
4498:20
4499:1c
4500:4
4502:1c
4503:4
4507:c
4508:e
4510:c
4518:18
```

## Reproduce
Follow R281 reproduction and pinned R247/R275/R276/R277/R280/R281 blocks. For batch A use scan(st,N) directly, start=3700,size=500, ceiling=18000000. For batch B insert below after R281 block before grow, replace good predicate with compareMerge(st,N), start=4200,size=500, ceiling=18000000. Retain stats in both result paths. Batch B deliberately runs both algorithms, so scan counters include both, not a benchmark. Existing count checks and first-100 full elimination checks remain active.
```javascript

stats.mergeCompared=0;stats.mergeSort=0;stats.mergeComparisons=0;stats.mergeIntersections=0;
function mergedHull(old,rows){
 const line=r=>({r,m:-r[1],c:-r[2],d:abs(r[0])});
 const order=(a,b)=>cmp([a.m,a.d],[b.m,b.d])||cmp([b.c,b.d],[a.c,a.d]);
 let O=old.map(line),N=rows.map(line);
 for(let i=1;i<O.length;i++)if(order(O[i-1],O[i])>=0)throw Error("old hull order");
 N.sort((a,b)=>{stats.mergeSort++;return order(a,b)});
 let i=0,j=0,H=[];
 while(i<O.length||j<N.length){
  let take;
  if(i===O.length)take=false;else if(j===N.length)take=true;else{stats.mergeComparisons++;take=order(O[i],N[j])<=0}
  let l=take?O[i++]:N[j++];
  if(H.length&&cmp([H[H.length-1].m,H[H.length-1].d],[l.m,l.d])===0)continue;
  let at=null;
  while(H.length){let a=H[H.length-1];at=[a.c*l.d-l.c*a.d,l.m*a.d-a.m*l.d];stats.mergeIntersections++;if(at[1]<=0n)throw Error("merge slope");if(a.at===null||cmp(at,a.at)>0)break;H.pop()}
  H.push({...l,at:H.length?at:null});
 }
 return H;
}
function scanMerge(st,rows){
 let o={pos:[],neg:[],seen:new Set(st.seen),lo:st.lo,hi:st.hi};
 function cut(b,c){if(!b)return c>0n;let q=b>0n?[-c,b]:[c,-b];if(b>0n){if(!o.lo||cmp(q,o.lo)>0)o.lo=q}else if(!o.hi||cmp(q,o.hi)<0)o.hi=q;return !o.lo||!o.hi||cmp(o.lo,o.hi)<0}
 for(let r of rows){let a=norm(r.slice(0,3)),key=a.join();if(o.seen.has(key))continue;o.seen.add(key);if(a[0]>0n)o.pos.push(a);else if(a[0]<0n)o.neg.push(a);else if(!cut(a[1],a[2]))return null}
 let P=mergedHull(st.pos,o.pos),M=mergedHull(st.neg,o.neg),i=0,j=0,k=0,bound=P.length&&M.length?P.length+M.length-1:0;stats.scanMaxPairs+=bound;
 while(i<P.length&&j<M.length){let p=P[i].r,m=M[j].r;stats.scanPairs++;k++;if(!cut(p[0]*m[1]-m[0]*p[1],p[0]*m[2]-m[0]*p[2]))return null;
  let a=P[i+1]?.at??null,b=M[j+1]?.at??null;if(!a&&!b)break;
  if(!b||a&&cmp(a,b)<0)i++;else if(!a||cmp(a,b)>0)j++;else{i++;j++}
 }
 if(k>bound)throw Error("scan pair bound");
 o.pos=P.map(x=>x.r);o.neg=M.map(x=>x.r);return o;
}

function compareMerge(st,N){let a=scanMerge(st,N),b=scan(st,N);stats.mergeCompared++;if(!!a!==!!b||a&&(!same(a.lo,b.lo)||!same(a.hi,b.hi)||a.pos.map(r=>r.join()).join(";")!==b.pos.map(r=>r.join()).join(";")||a.neg.map(r=>r.join()).join(";")!==b.neg.map(r=>r.join()).join(";")))throw Error("merge mismatch");return !!a}

```

## Next
Cumulative classified 371300/667787, survivors 2764, remaining 296487, next [4700,0]. Preserve R277–R281 and these two banks; do not repeat completed prefix. Finish sixth strict words, then singleton and mixed zero words. K6 remains 1–2. Independent review and Activity association pending.
