# X6 R262 — common-zero infinity-anchor closure with one finite zero

2026-11-27. Independent informed TASK_RESEARCH, author proof and exact integer computation, NOT_REVIEWED. P000 V5 and joint relation preservation retained. All (t,B,D) are auxiliary BRC weight coordinates. Native exact lookup r2-20261127-1106-x6-read SUCCEEDED at 2026-11-27T03:06:46.785076Z, Source c0ac0878ba868c6a66885a1e81e25ee446e073de; NO_CANONICAL_PUBLICATION_DIRECTORY, directory-only observation, native owner projection not evaluated, own researcher identity unconfirmed. No CLAIM, Result, Review or shared task mutation; Activity pending. No new registration or assumed authority.

## Inputs, theorem and scope

Frozen R247@7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (51 rays, 98 directed germs, 47 necessary labels, 2225 linear suffix partitions, exact can). Port 10, 1935 directions, weights (17t,B,22t,D), six-pair joint BRC strict 3/2. R258@b0960b0e767177f2b6bb7437275bf19aa662f7f0 closed internal quadratic positions at author-proof scope. R261@b091d79f5b7b493918b181750b2494c3688799a2:research_notes/portable_direct/2026-11-27_r2_x6_r261_all_pencil_circuit_helly.md proved all-pencil intercept criterion and excluded c=0 with all finite endpoints nonzero (already excluded by its first 13 directions). No new scientific input.

Let Q=a t²+b B²+c D²+d tB+e tD+f BD be full rank, and Q(p24)=c=0. In the pencil through p24 and direction t=0, the finite rays are p18=(0,1,0), p2=(0,1,11), p0=(0,1,12), p36=(0,1,18). Claim: under inherited necessary-wall and complete linear suffix capacity premises, if exactly one of the 50 finite endpoint rays is zero and belongs to these four, Q cannot be the unique quadratic root of a correct depth-six tree.

Proof: along this pencil Q/B²=b+f D/B. A finite zero forces f≠0: otherwise b=0 and t divides Q, contradicting full rank. Normalize f=1 by positive scaling or global sign reversal (branches interchangeable). The four possible zero words have a unique zero and signs sign(y-y0), with K∞=b=-y0. All other finite points are nonzero. Use the R261 exact all-pencil circuits for the full 17 directions, with the equality interval J∞={-y0}, other intervals open (possibly unbounded). Each quartet has at least three non-singleton open intervals and nonzero cofactor weights. Thus its Minkowski sum is open, and the same two strict bounds and slope interval update as R261 apply; equality is encoded by identical lower and upper affine forms. Any nonzero finite point fixes all outgoing signs. Leave the germs emanating from the zero finite point unassigned for now; a failure of can(mask,5) on either partial branch excludes every completion by monotonicity. The p24 germ is still assigned by R261's exact lexicographic rule. In all 12 existing slope sectors, including f=0 boundary (no zero word there), the one-zero relaxation yields exactly eight full finite-sign partial masks, all with the zero at p18 and f=1. No candidate at p2,p0,p36. Hence b=0 for remaining candidates.

For p18=(0,1,0), a germ toward q=(t_q,B_q,D_q) has first jet d t_q+D_q. Every one of its 12 neighbors has t_q>0 and nonzero Q(q) (assumption). At d=-D_q/t_q the second jet equals Q(q), since Q(p18)=0 and its polarization with q is zero. Thus the entire missing local word is exactly determined by d and the retained neighbor signs. Sweep the 12 rational events and 13 complementary intervals on the entire real d-axis (a mediant is an exact interior representative, outer probes one unit beyond extremes). This is a relaxation of joint feasibility with e,a, because d is allowed to range freely; absence of any capacity-feasible completion is a valid exclusion. All 104 distinct per-mask completions (8×13) fail: 31 direct count failures, 73 exact recursive failures. No remaining masks. The two-stage proof does not erase the zero germ residual; it is recovered completely at the end.

Further corollary independent of this computation: if c=0, two distinct finite zeros on any one pencil through p24 imply its affine restriction vanishes identically, hence that linear pencil equation divides Q. Therefore full rank allows at most one finite zero on each pencil. Combined with R261/R262, a possible c=0 root either has exactly one finite zero outside the four infinity-pencil rays (and, by R261's 13-line prefix, in its 46-endpoint set), or at least two finite zeros on distinct pencils. The latter remains open; no blanket exclusion of the four full kernels is claimed.

## Exact executed reproduction

Take first JavaScript block from pinned R247 and first JavaScript block from pinned R261. Modify R261 patch using the following exact replacements, then replace R247's original return statement with the modified patch; convert final experiment(data) to return experiment(data) and execute in BigInt-capable JS. These are the actual edits and refinement used; the 28,717,446-check prefix was first run separately, then reproduced with refinement. Do not double count the prefix.

```javascript
let edits=[
["ceiling=50000000;","ceiling=100000000;"],
["if(v[i]>0)a|=E[ids[i]];else b|=E[ids[i]]","if(v[i]>0)a|=E[ids[i]];else if(v[i]<0)b|=E[ids[i]]"],
["out.push({a,b,l:pos.length?row(pos[s<0?pos.length-1:0]):null,u:neg.length?row(neg[s<0?0:neg.length-1]):null})","let z=v.indexOf(0);out.push({a,b,l:z>=0?row(ids[z]):pos.length?row(pos[s<0?pos.length-1:0]):null,u:z>=0?row(ids[z]):neg.length?row(neg[s<0?0:neg.length-1]):null,zero:z>=0?ids[z]:null})"],
["if(!s){emit(Array(n).fill(1));","if(k===0){if(s)for(let j=0;j<n;j++)emit(ids.map((_,i)=>i===j?0:i<j?-s:s));return out}if(!s){emit(Array(n).fill(1));"],
["if((a|b)!==ALL||(a&b))throw Error(\"full mask\");","if(a&b)throw Error(\"overlap\");"]
];
for(let [a,b] of edits){if(!patch.includes(a))throw Error("missing "+a);patch=patch.replace(a,b)}
```

Replace the final return in R261 patch (the return containing groups,points,germs,linear,checks,completed,unique,totals,final,hist) by:

```javascript
let before=checks, out=[], stats={visits:0,direct:0,recursive:0,surv:0}, gs=G.filter(g=>g[0]===18);
let events=[...new Map(gs.map(([u,v])=>{let p=P[v],g=gcd(p[2],p[0]);if(p[0]<=0n)throw Error("nonpositive t");let r=[-p[2]/g,p[0]/g];return [r.join(),r]})).values()].sort(cmp);
let probes=[ [events[0][0]-events[0][1],events[0][1]] ];
for(let i=0;i<events.length;i++){probes.push(events[i]);if(i+1<events.length)probes.push([events[i][0]+events[i+1][0],events[i][1]+events[i+1][1]])}
let last=events.at(-1);probes.push([last[0]+last[1],last[1]]);
for(let item of final){let A=BigInt("0x"+item.a),B=BigInt("0x"+item.b);if((ALL^(A|B))!==E[18]||item.f!=="1")throw Error("unexpected zero");let local=new Set();
for(let [n,d] of probes){let a=A,b=B;for(let [u,v,bit] of gs){let s=sg(n*P[v][0]+d*P[v][2]);if(!s){s=A&E[v]?1:B&E[v]?-1:0;if(!s)throw Error("missing neighbor sign")}if(s>0)a|=bit;else b|=bit}if((a|b)!==ALL||(a&b))throw Error("coverage");let key=a+","+b;if(local.has(key))continue;local.add(key);stats.visits++;if(count(a)>31||count(b)>31){stats.direct++;continue}if(!can(a,5)||!can(b,5)){stats.recursive++;continue}stats.surv++;out.push({a:a.toString(16),b:b.toString(16),d:[String(n),String(d)],input:item})}}
return {groups,checks,completed,unique:unique.map(s=>s.size),partial:final.length,refineChecks:checks-before,events:events.map(r=>r.map(String)),stats,out};
```

## Actual final exact output

```json
{"groups":[[18,2,0,36],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50],[48,21,29,23,46],[4,14,16,12,3,8],[6,5,43],[7],[13],[17],[22],[27],[30],[31],[32],[33],[35],[41]],"checks":28892380,"completed":12,"unique":[4,80,1319,2966,2985,1288,1249,1273,1306,675,425,286,132,91,29,18,8],"partial":8,"refineChecks":174934,"events":[["-395","2"],["-126","1"],["-87","1"],["-235","3"],["-61","1"],["-83","2"],["-22","1"],["-40","3"],["-38","3"],["-9","1"],["-25","3"],["-5","2"]],"stats":{"visits":104,"direct":31,"recursive":73,"surv":0},"out":[]}
```

Prefix candidate masks in hex (positive,negative; orientation f=1), all missing exactly E[18]:
```
3cc3ffcec0003a3dd980005cf 33c00303aee8082222fffa30
3cc3f7cec0003a3dd980005cf 33c08303aee8082222fffa30
3cc3f74ec0003a3dd980005cf 33c08b03aee8082222fffa30
3fdb0cfef000180cfb0003b4f 24f3000aeea2b300affc4b0
3fd30cfef000180cfb0003b4f 2cf3000aeea2b300affc4b0
3cd34cfef000182cfb0003fcf 32cb3000aeea29300affc030
3fd34cfef000102cfb0003fcf 2cb3000aeeaa9300affc030
3ed34cfef000102cfb0003fcf 12cb3000aeeaa9300affc030
```

## Next actual question

Extend singleton intercept constraints to other anchor groups, retaining tangent events for all zero germs. With at least two finite zero points on distinct pencils, reduce to 3-dimensional homogeneous kernel using the existing three-anchor polar representation (R253/R254). For a general one-zero finite anchor p=(rT,rU,D), after Q(p)=0 its germ's first jet is 2 p^T A q and at a zero first jet the second sign is sign Q(q); the latter remains known when q is nonzero. For multiple zeros, a distinct neighbor may also be zero, so recover both polar and second jets without using strict-neighbor shortcut. A possible improvement is to intersect residual word feasibility with the shared slope interval before expensive can calls. The c≠0 chart remains open; no new claim about K6 beyond 1..2. Author computation, no independent review.
