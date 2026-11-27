# X6 R263 — common-zero single finite anchor closure on the remaining multi-point pencils

2026-11-27. Independent informed TASK_RESEARCH, author proof and exact BigInt computation, NOT_REVIEWED. P000 V5 and joint relation preservation retained. Coordinates (t,B,D) are auxiliary BRC weight coordinates. Native request r2-20261127-1211-x6-read SUCCEEDED at 2026-11-27T04:12:05.458267Z, Source dbacafdae2f5f74d93557c0e4e050d3fdcacc7b8, NO_CANONICAL_PUBLICATION_DIRECTORY; directory-only observation, not native owner projection. Own researcher identity unconfirmed; no CLAIM, formal Result/Review or shared task mutation. Activity association pending.

## Frozen inputs and exact scope

R247@7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (51 rays, 98 directed germs, 47 necessary support labels, 2225 linear suffix partitions). Port 10, 1935 directions, weights (17t,B,22t,D), six-pair joint BRC strict 3/2. R261@b091d79f5b7b493918b181750b2494c3688799a2:research_notes/portable_direct/2026-11-27_r2_x6_r261_all_pencil_circuit_helly.md gives the exact intercept circuit criterion and strict finite prefix exclusion. R262@cdd1ec936c0b5c10261a9c61e25620c15f43f999:research_notes/portable_direct/2026-11-27_r2_x6_r262_common_zero_infinity_anchor_closure.md closes exactly one finite zero on t=0. R258@b0960b0e767177f2b6bb7437275bf19aa662f7f0 closes internal quadratic positions at author-proof scope. No new scientific inputs; inherit necessary-wall and linear-suffix capacity premises.

## Theorem: all multi-point pencils now closed for exactly one finite zero

Let Q=a t^2+b B^2+c D^2+d tB+e tD+f BD be full rank, Q(p24)=c=0, and exactly one of the other 50 endpoints z be zero. If z belongs to any of the six multi-point pencils through p24, Q cannot be the sole quadratic root of a correct depth-six tree.

Proof: the pencil direction is (T,U), with p=(rT,rU,D), r>0, y=D/r. Its restriction is K+(eT+fU)y, K=aT^2+dTU+bU^2. If its slope vanishes and it has a zero, the entire pencil is zero and its linear equation divides Q, incompatible with full rank. Otherwise a zero at y0 forces K=-(eT+fU)y0, and every other sign is sign((eT+fU)(y-y0)). This yields exactly one singleton intercept interval on the target pencil. All other finite points have strict sign constraints, open intercept intervals. Each four-direction cofactor circuit contains at most one singleton, so its Minkowski sum is open and membership of zero is exactly the two strict endpoint inequalities (with infinite bounds handled as in R261). The same shared slope interval is intersected with all circuit constraints. R261's 12 projective slope sectors cover the six multi-point directions; one-point directions allow both signs independently of slope. Normalize f>0 or f=0,e>0 by global branch exchange; (e,f)=0 makes c=0 rank-deficient. The germ at p24 is sign(e+17f) unless that slope is zero, when its sign is the nonzero constant K17. If the target is B=17t and that slope is zero, the target word is impossible and is omitted.

Retain all nonzero-point outgoing germ signs; leave the zero finite point's outgoing germs unassigned (not assumed zero). At each prefix a partial branch mask is a subset of the eventual branch; count<=31 and can(mask,5) are necessary by the inherited monotone suffix capacity test. Failure on either partial branch excludes all completions, regardless of the still unknown germ residuals. Exact search below exhausts every target word in all 12 sectors. No partial masks survive for any of the five new pencils, so no tangent refinement is needed for them. Combine R262 for the sixth pencil. This does not exclude any whole two-anchor kernel when additional finite zeros are allowed.

## Exact executed evidence

Group indices are zero-based, in the frozen R261 order. Each row is a separately completed run; the number of capacity checks includes repeated prefixes and is computational workload, not number of different candidates. A combined attempt for groups 2–5 timed out without a usable output; it is not counted. Individual reruns returned the following exact output, without CUT or incomplete sector.

| group | (T,U) | finite anchor IDs | checks | sectors | final partial masks |
|---|---|---|---:|---:|---:|
| 1 | (1,17) | 26,19,34,20,25,28,39,1,37 | 20551433 | 12 | 0 |
| 2 | (1,0) | 10,15,11,45,49,9,38,42,40,44,47,50 | 18783079 | 12 | 0 |
| 3 | (1,4) | 48,21,29,23,46 | 13584099 | 12 | 0 |
| 4 | (2,5) | 4,14,16,12,3,8 | 14651867 | 12 | 0 |
| 5 | (1,9) | 6,5,43 | 17422876 | 12 | 0 |

Total 84,993,354 checks across the five completed runs; 35 new anchor positions excluded, 39/50 including R262. Distinct partial mask counts (up to global branch exchange) by the 17 prefix stages:
- group 1: [4,72,1225,2648,2359,387,325,298,287,85,27,25,0,0,0,0,0]
- group 2: [4,80,1290,2775,2152,303,232,220,219,41,7,5,0,0,0,0,0]
- group 3: [4,80,1278,2457,1637,258,149,149,149,29,7,5,0,0,0,0,0]
- group 4: [4,80,1278,2789,1753,319,284,256,250,43,8,8,1,1,0,0,0]
- group 5: [4,80,1278,2789,1997,403,268,299,328,114,38,34,12,12,0,0,0]

The R261 groups returned in all runs:
[[18,2,0,36],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50],[48,21,29,23,46],[4,14,16,12,3,8],[6,5,43],[7],[13],[17],[22],[27],[30],[31],[32],[33],[35],[41]].

## Reproduction

Extract the first JavaScript block from pinned R247 as src, first JavaScript block from pinned R261 as patch. Apply these exact edits (TARGET=1,2,3,4,5 separately), replace R261's final return, then replace the original R247 return statement and final expression. This is the common prefix of all five executed scripts; group 1 also ran an empty residual loop (zero input, zero checks). All arithmetic in the inherited BRC auxiliary coefficient/capacity calculation is exact BigInt. This is not a native time-dynamics experiment.

```javascript
let edits=[
["ceiling=50000000;","ceiling=100000000;"],
["if(v[i]>0)a|=E[ids[i]];else b|=E[ids[i]]","if(v[i]>0)a|=E[ids[i]];else if(v[i]<0)b|=E[ids[i]]"],
["out.push({a,b,l:pos.length?row(pos[s<0?pos.length-1:0]):null,u:neg.length?row(neg[s<0?0:neg.length-1]):null})","let z=v.indexOf(0);out.push({a,b,l:z>=0?row(ids[z]):pos.length?row(pos[s<0?pos.length-1:0]):null,u:z>=0?row(ids[z]):neg.length?row(neg[s<0?0:neg.length-1]):null,zero:z>=0?ids[z]:null})"],
["if(!s){emit(Array(n).fill(1));","if(k==="+TARGET+"){if(s)for(let j=0;j<n;j++)emit(ids.map((_,i)=>i===j?0:i<j?-s:s));return out}if(!s){emit(Array(n).fill(1));"],
["if((a|b)!==ALL||(a&b))throw Error(\"full mask\");","if(a&b)throw Error(\"overlap\");"],
["for(let {a,b,I} of states)","for(let {a,b,I,ps} of states)"],
["f:String(f),positive:","zero:ps["+TARGET+"].zero,f:String(f),positive:"]
];
for(let [a,b] of edits){if(!patch.includes(a))throw Error(a);patch=patch.replace(a,b)}
patch=patch.replace(/return \{groups,points:[\s\S]*?\};\s*$/,"return {groups,checks,completed,unique:unique.map(s=>s.size),partial:final.length,final};");
src=src.replace('return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};',patch).replace(/experiment\(data\)\s*$/,"return experiment(data);");
let result=new Function(src)();
```

## Sharpened remaining finite-anchor set

R261 already has zero strict-finite masks at prefix 13 (indices 0..12) covering 46 finite endpoints. For an exactly-one-finite-zero candidate, its zero must be in that prefix; otherwise its strict prefix would have been excluded by the same monotonicity argument. R263/R262 exclude all 39 multi-point anchors. Consequently the remaining possible exactly-one-finite-zero anchor set is exactly bounded by {7,13,17,22,27,30,31} (necessary candidate set, not an existence assertion). Four later singleton directions {32,33,35,41} need no separate single-zero calculation. This reduction is independent of any future full kernel closure.

## Reusable next step: singleton and tangent residual

For one-point target pencils, emit the single zero word even if the representative slope is zero; this is a safe relaxation, since a true zero-slope zero would contradict full rank. The singleton intercept row remains exact and does not need new slope sectors. Once the partial branch passes, restore the local residual. For p=z, g=A p lies in p-perp and g!=0 (full rank); its germ toward q has sign lexsgn(2g·q,Q(q)) at a zero first jet. For distinct zero neighbor p24, g·p24 cannot vanish (otherwise the line through them is a factor); its sign equals the opposite endpoint's polar sign if the corresponding germ exists. On the auxiliary 2D coefficient space p-perp, all linear event lines are generated by p×q; enumerate both rays of each event and their two adjacent sectors by infinitesimal perturbation, preserving the second jet using Q(q) for nonzero q. This covers a relaxation of gradient feasibility even without imposing global coupling; any remaining candidates need exact coupled feasibility. No singleton run is claimed here. Multiple finite zeros on distinct pencils still require joint polar/three-anchor treatment, and c!=0 remains open. K6 remains 1..2. Author proof/computation only; independent review pending.
