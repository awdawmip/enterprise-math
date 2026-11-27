# X6 R281 — active-pair envelope sweep and sixth-pencil continuation

2026-11-28. Independent informed TASK_RESEARCH; author proof and author computation, NOT_REVIEWED. P000 Source V5, global V4, ACTIVE worldview, joint relation preservation and residual fidelity retained. Auxiliary coefficient algebra of the frozen BRC observer problem; no native spatial plane or dynamical interpretation. Native lookup r2-20261128-0014-x6-current SUCCEEDED at 2026-11-27T16:14:54.157175Z, Source 7b0f464423c95f80ffa204b1f39f8d370e0f182a, NO_CANONICAL_PUBLICATION_DIRECTORY, not a native owner projection. Own researcher binding unconfirmed; no CLAIM/Result/Review/shared-control mutation. Activity association pending.

## Frozen inputs
Paths under research_notes/portable_direct/2026-11-27_r2_x6_r:
- R247@7e54892a45579bdc497c27e061399339d1fb3512: 247_two_anchor_signed_primary_faces.md
- R275@001076e59298e45715cb58c87ab3395c53d005a8: 275_monic_block_compression_and_strict_prefix.md
- R276@33fba542db5f810e803d770b7046b5e26ac1ebb9: 276_strict_fifth_pencil_packed_frontier.md
- R277@a1df3c1aa315909d8c109ef8551f24a460a44b1f: 277_incremental_slope_projection_sixth_prefix.md
- R280@3366eecf953f9943f8a9d88b36279f221cb1e1c7: 280_joint_affine_envelope_sixth_prefix.md

Same frozen Port 10, 1935 directions, six-pair BRC, 47 support tags, 51 endpoints, 98 germs, 2225 linear suffix partitions. Capacity exclusion inherits R247 necessary-wall and complete pure-linear suffix premises. Only c=1 strict endpoint words on the six multipoint pencils; singleton words and zero cases still open. Prior classified 189600/667787; survivors 1389; next [2400,0].

## Lemma: simultaneous active-pair projection
For strict rows A e+B f+C>0, use R280 lower envelope maximum L(f)=max_{A>0}[-(Bf+C)/A] and sign-reversed upper envelope maximum H(f)=max_{A<0}[(Bf+C)/A]. Keep any preexisting projection interval I and all new A=0 restrictions. If either side empty, no pair constraints required. Otherwise existence of e is equivalent to L(f)+H(f)<0. Construct each exact affine max envelope on all real f, using only previously retained rows plus new rows (previous removed rows are implied on I by R280). Let p,m count active affine pieces. On each open interval of the merged activation events, one lower and one reversed-upper line are active. Sweep the two sorted event lists, advancing both at a tie; at most p+m-1 ordered pairs occur (zero if either side empty). For each visited pair use its ordinary global Fourier–Motzkin inequality (A_p B_m-A_m B_p) f+(A_p C_m-A_m C_p)>0, not just a restriction on its active subinterval.

Proof: every visited pair is an original necessary inequality wherever f is feasible, even outside its active subinterval. Conversely, for any f in I satisfying all visited-pair inequalities and flat rows, if f is in an open merged segment the active pair gives L+H<0. If f is an event, continuity of both envelopes gives their values from either adjacent open segment, and that visited pair's inequality at f is strict. Thus L+H<0 also at events; choose e strictly between bounds. Equal slopes, coincident events and unbounded first/last segments are handled by the exact hull and sweep. The intersection is exactly the original open projection, including empty and unbounded cases. The retained envelopes together with new exact I still represent the entire joint feasible set, not just the projection, so future intersections are exact. Original endpoint words, germ masks and branch identity retained. This uses strict inequalities; weak/equality row systems need separate endpoint/tie semantics before reuse.

Cost: at most p+m-1 projection pair cuts vs p*m if every full hull pair is taken; hull construction O(n log n) comparisons plus O(n) stack intersection comparisons, sweep O(p+m), flat rows O(n). This is not a claim of end-to-end runtime reduction: rational bit lengths, per-extension sorting, normalization, row generation, branch copying, capacity costs and repeated hull reconstruction must be charged. R280 incremental all-pair method can be cheaper in some small-update regimes. Future optimization: merge sorted old hull slopes and new rows, or choose algorithm adaptively.

## Actual calculations
Batch 1: R280 envelope method, start=2400,size=300, capacity ceiling 18000000, all complete.
```json
{"hist":{"direct":10486,"alg":12705,"recursive":411,"surv":98,"visits":23700,"checkedAgainstOld":100},"checks":1340735,"next":[2700,0],"stats":{"prefixes":300,"rawRows":16977,"hullRows":1594,"pairRows":1976,"hullIntersections":27475,"pairDominanceTests":122192,"compared":13214,"rawPairs":4054588,"hullPairs":1611568},"partial":false}
```
Batch 2: active-pair sweep, start=2700,size=1000, capacity ceiling 24000000, all complete. Triple comparison with R277 raw incremental projection and R280 compressed incremental projection for every algebra-tested extension, including exact rational endpoints when feasible. First 100 additionally compare R275 full elimination. First development attempt hit an assertion for both hulls empty (bound -1 instead of zero); fixed zero-side bound and reran the uncommitted batch, no earlier durable prefix reclassified. R276 support count checks repeated.
```json
{"hist":{"direct":35264,"alg":40341,"recursive":2778,"surv":617,"visits":79000,"checkedAgainstOld":100},"checks":7737042,"next":[3700,0],"stats":{"prefixes":1000,"rawRows":67337,"hullRows":4755,"pairRows":5658,"hullIntersections":113715,"pairDominanceTests":434947,"compared":0,"rawPairs":0,"hullPairs":0,"scanPairs":188992,"scanIntersections":11628871,"scanCompared":43736,"scanRawPairs":36397267,"scanHullPairs":16710571,"scanMaxPairs":272227},"partial":false}
```
All computation BigInt and exact cross-products. Total new visits 102700, direct 45750, algebra 53046, recursive 3189, survivors 715, capacity checks 9077777. Cumulative classified 292300/667787, survivors 2104, remaining 375487, next [3700,0]. Necessary-condition survivors only. Projection pair cuts reduced relative to R280 in batch 2, but scan adds 11628871 hull intersection comparisons; no wall-clock improvement claimed.

All new surviving words, first batch (prefix index: hex mask of sixth words):
```text
2405:fc
2407:60
2408:7c
2410:7c
2411:1c
2412:1e
2413:10
2414:1e
2416:38
2417:1c
2418:1c
2420:30
2421:18
2422:1c
2425:78
2434:200
2435:40
2436:40
2438:c0
2440:40
2441:7c
2443:60
2445:30
2447:30
2456:40
2458:40
2467:40
2468:20
2472:40
2473:70
2475:600
2482:600
2483:200
2484:40
2485:40
2486:200
2487:c0
2488:c0
2490:1c0
2499:200
2501:40
2506:80000
2507:80080
2508:80
2509:80
2651:2000000000000000
```
Second batch:
```text
2748:100000
2749:100000
2775:84000000000000000
2778:84000000000000000
2852:1c
2854:e
2855:6
2856:6
2857:6
2859:4
2861:18
2862:fc
2863:10
2864:1c
2865:1c
2866:c
2867:c
2874:f0
2882:f0
2887:40
2890:40000
2891:40000
2894:80
2921:180781c038010
2922:180180c018000
2924:781c038010
2925:80180c018000
2926:52210418180c0300600f
2927:52210008080000000001
2928:1
2929:6
2931:4
2932:181c0300e01f
2933:1
2934:201c
2935:18040100600f
2936:1
2937:200f
2939:2007
2940:1
2941:2007
2948:700e01f
2949:201f
2950:300e007
2951:e007
2953:1
2954:1
2959:300e01d
2960:e01f
2961:6001
2962:6001
2968:c008
2969:c008
2976:8000000
2978:180781c038000
2979:208180180c018000
2981:181c038000
2982:180c018000
2983:8180c00000001
2984:80000000001
2985:1
2986:10418381c01006001
2987:10008180c01000001
2988:8180000002001
2989:80000000001
2992:c38783c0f006001
2993:10c08181c07000001
2994:1
2995:418381c01002001
2996:10008180c01002001
2997:2001
2998:1
3001:10000
3004:438783c0f002001
3005:10c08181c07002001
3006:2001
3007:1
3011:10000
3015:180e000000
3016:806000000
3017:2000000
3018:2000000
3021:1000001
3022:1000001
3023:4000000
3026:40f000000
3027:c01000000
3028:c000000
3029:400000000
3033:800000000
3041:400000000000001
3043:400000000000001
3045:410000000000000
3047:800000000
3050:10000000000000
3059:12231c60c00000000001
3061:231c60c00000000001
3062:21040800000000000
3063:4000000000
3070:12220000000000000001
3071:220000000000000001
3076:8000000000000000000
3079:fc00000000000000000
3087:1
3088:9000000000000000000
3092:2000000000000000001
3093:1
3094:1
3095:1
3100:1
3101:1
3102:1
3103:1
3108:2c000000000000000000
3109:38000000000000000000
3119:40000
3120:40000
3162:8000000000
3163:808000000000
3165:c0c000000000
3206:c000000000000000000
3208:c000000000000000000
3256:40000000000
3283:8000000000000000
3284:8000000000000000
3288:8000000000000000
3310:1900000000000000000
3314:1900000000000000000
3327:fc
3328:3c
3330:20
3331:60
3332:7c
3333:3c
3335:7c
3336:3c
3337:1c
3338:1e
3339:c
3340:10
3341:1e
3342:c
3344:38
3345:1c
3346:1c
3348:30
3349:18
3350:1c
3351:200
3353:38
3354:38
3374:e0
3377:78
3378:30
3380:60
3381:20
3383:30
3386:30
3401:40
3417:40
3418:20
3423:20
3426:600
3433:600
3437:200
3438:40
3441:c0
3585:2000000000000000
```
Banks checked for strictly increasing prefix indices, range, 79-bit bound and popcount totals 98 and 617 respectively.

## Reproduction
Use R277 reconstruction exactly as R280, including R276 support-label bit count and R275 dirs extension. In R277 tail insert R280 first JS block before function grow; increment pairCalls before return cut in grow's pair; replace base construction with let raw=grow(empty,R);if(!raw)throw Error("old bank infeasible");let st=prune(raw);. Replace let good=!!grow(st,N); with let good=both(st,raw,N); for batch 1, let good=triple(st,raw,N); for batch 2. Add stats to both return objects. Set start,size,ceiling as above. In batch 2 additionally insert the following code after R280 block and before grow:
```javascript

stats.scanPairs=0;stats.scanIntersections=0;stats.scanCompared=0;stats.scanRawPairs=0;stats.scanHullPairs=0;stats.scanMaxPairs=0;
function scanHull(rows){
 let lines=rows.map(r=>({r,m:-r[1],c:-r[2],d:abs(r[0])}));
 lines.sort((a,b)=>cmp([a.m,a.d],[b.m,b.d])||cmp([b.c,b.d],[a.c,a.d]));
 let H=[];
 for(let l of lines){
  if(H.length&&cmp([H[H.length-1].m,H[H.length-1].d],[l.m,l.d])===0)continue;
  let at=null;
  while(H.length){let a=H[H.length-1];at=[a.c*l.d-l.c*a.d,l.m*a.d-a.m*l.d];stats.scanIntersections++;if(at[1]<=0n)throw Error("scan slope order");if(a.at===null||cmp(at,a.at)>0)break;H.pop()}
  H.push({...l,at:H.length?at:null});
 }
 return H;
}
function scan(st,rows){
 let o={pos:st.pos.slice(),neg:st.neg.slice(),seen:new Set(st.seen),lo:st.lo,hi:st.hi};
 function cut(b,c){if(!b)return c>0n;let q=b>0n?[-c,b]:[c,-b];if(b>0n){if(!o.lo||cmp(q,o.lo)>0)o.lo=q}else if(!o.hi||cmp(q,o.hi)<0)o.hi=q;return !o.lo||!o.hi||cmp(o.lo,o.hi)<0}
 for(let r of rows){let a=norm(r.slice(0,3)),key=a.join();if(o.seen.has(key))continue;o.seen.add(key);if(a[0]>0n)o.pos.push(a);else if(a[0]<0n)o.neg.push(a);else if(!cut(a[1],a[2]))return null}
 let P=scanHull(o.pos),M=scanHull(o.neg),i=0,j=0,k=0,bound=P.length&&M.length?P.length+M.length-1:0;stats.scanMaxPairs+=bound;
 while(i<P.length&&j<M.length){let p=P[i].r,m=M[j].r;stats.scanPairs++;k++;if(!cut(p[0]*m[1]-m[0]*p[1],p[0]*m[2]-m[0]*p[2]))return null;
  let a=P[i+1]?.at??null,b=M[j+1]?.at??null;if(!a&&!b)break;
  if(!b||a&&cmp(a,b)<0)i++;else if(!a||cmp(a,b)>0)j++;else{i++;j++}
 }
 if(k>bound)throw Error("scan pair bound");
 o.pos=P.map(x=>x.r);o.neg=M.map(x=>x.r);return o;
}
function triple(st,raw,N){
 let a=scan(st,N),before=pairCalls,b=grow(raw,N);stats.scanRawPairs+=pairCalls-before;before=pairCalls;let c=grow(st,N);stats.scanHullPairs+=pairCalls-before;stats.scanCompared++;
 if(!!a!==!!b||!!a!==!!c||a&&(!same(a.lo,b.lo)||!same(a.hi,b.hi)||!same(a.lo,c.lo)||!same(a.hi,c.hi)))throw Error("scan mismatch");return !!a
}

```
For subsequent production runs the triple diagnostic may be disabled only with preserved proof and evidence scope; use scan(st,N) directly for the strict feasibility predicate. Do not repeat classified prefix. Keep earlier R277–R280 banks and these two banks. Next [3700,0]; after sixth pencil, extend singleton words and mixed zero words. K6 remains 1–2; independent review and Activity association pending.
