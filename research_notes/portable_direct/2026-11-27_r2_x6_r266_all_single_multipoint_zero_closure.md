# X6 R266 — all single multipoint zero pencils closed

2026-11-27. Independent informed TASK_RESEARCH, author proof and exact BigInt calculation, NOT_REVIEWED. Coordinates (t,B,D) are auxiliary BRC weight coordinates, not native spatial addresses. Native task observation r2-20261127-1413-x6-owner-observe SUCCEEDED at 2026-11-27T06:14:11.610693Z, Source d63ab5abd4a6125320da63b9854d98f0bf2290a7: NO_CANONICAL_PUBLICATION_DIRECTORY, not a native owner projection. Own researcher identity unconfirmed, no CLAIM or shared Task/Result/Review change, Activity association pending.

## Frozen inputs and result

Reuse R247@7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md, R261@b091d79f5b7b493918b181750b2494c3688799a2:research_notes/portable_direct/2026-11-27_r2_x6_r261_all_pencil_circuit_helly.md, R264@3c6fcee204ed134a241ec8de3f2d7ccb571732e0:research_notes/portable_direct/2026-11-27_r2_x6_r264_singleton_pencil_all_zero_words_closure.md and R265@dc686c247bdc0dab857eca322648ec2231e30cb3:research_notes/portable_direct/2026-11-27_r2_x6_r265_infinity_only_multipoint_zero_closure.md. Frozen Port 10, 1935 directions, 47 labels, 51 endpoint rays, 98 directed germs, 2225 linear partitions. Inherit necessary-wall and monotone linear-suffix capacity premises; retain joint observation signs, zero anchors and unassigned germ masks.

Theorem: let Q=a t^2+b B^2+c D^2+d tB+e tD+f BD be full rank with Q(p24)=c=0. If exactly one of the five finite multipoint pencils B=17t, B=0, B=4t, 2B=5t, B=9t contains a finite zero, while every other multipoint pencil (including infinity t=0) is strict, then Q cannot be the sole quadratic root of a correct depth-six tree, irrespective of the zero/sign status of all singleton pencils. Combined with R264 and R265, any successful common-zero root must have zeros on at least TWO distinct multipoint pencils.

Proof: on each pencil (T,U) a finite point p=(rT,rU,D), r>0, has normalized readout K+s y with y=D/r, K=aT^2+dTU+bU^2, s=eT+fU. A full-rank Q with common zero cannot vanish on a whole line (linear factor), hence a finite zero requires s!=0 and determines a unique anchor z and K=-s y_z. All other finite signs on that line are sign(s) sign(y-y_z). For target pencil k, replace the strict sign patterns in R264 by exactly these n_k zero words if s!=0; no pattern if s=0. All other multipoint pencils remain strict; singleton pencils allow arbitrary zero words. R264's shared slope sector constraints and open/singleton four-direction circuit tests are retained. At p24 the sole germ towards the B=17t pencil has leading sign(e+17f) whenever this slope is nonzero; if zero the pencil is necessarily strict in the permitted cases, and the constant term sign gives the second jet. Thus the existing p24 recovery remains valid even for target k=1, where the zero slope sector yields no patterns. Nonzero anchor germs are fully assigned; finite zero anchor germs remain unassigned. Every true Q contributes a partial mask at each prefix; each strict branch must satisfy count<=31 and can(mask,5) by monotonicity. All five finite target runs exhaust 12 slope sectors and have no surviving partial mask, so every residual completion is excluded without computing individual tangent residuals. This is a relaxation proof and does not require sufficiency of partial words. Together with earlier exclusions of zero multipoint pencils and infinity-only zero multipoint pencil, the claimed necessary condition follows.

## Executed evidence

BigInt arithmetic, inherited exact runner, no CUT or incomplete sector. Five independently executed target runs; shared prefix costs counted in each, not distinct work. k=1..5 denotes the zero-based frozen group index. All other multipoint groups strict and arbitrary singleton zero words permitted.

| k | pencil | anchor count | checks | sectors | first empty prefix (1-based) | final |
|---|---|---:|---:|---:|---:|---:|
|1|B=17t|9|20991475|12|15|0|
|2|B=0|12|18986981|12|13|0|
|3|B=4t|5|13829328|12|13|0|
|4|2B=5t|6|14959061|12|15|0|
|5|B=9t|3|17630213|12|15|0|

Total 86,397,058 capacity checks (with repeated prefix cost). Unique partial masks up to branch exchange by prefix:
k1 [4,72,1225,2648,2359,387,369,360,368,145,51,48,8,8,0,0,0]
k2 [4,80,1290,2775,2152,303,276,292,318,93,21,15,0,0,0,0,0]
k3 [4,80,1278,2457,1637,258,188,188,188,62,16,11,0,0,0,0,0]
k4 [4,80,1278,2789,1753,319,322,336,359,97,35,32,9,9,0,0,0]
k5 [4,80,1278,2789,1997,403,298,406,510,214,81,70,28,28,0,0,0]

## Reproduction

Extract first JavaScript fenced blocks from frozen R247 as src, R261 as patch, R264 as runner. For each k independently execute the following wrapper (same actual edits executed):

```javascript
for (const k of [1,2,3,4,5]) {
 let run=runner.replace('let result=new Function(src)();','return new Function(src)();')
 .replace('if(k>=6)emit([0]);if(!s){emit(Array(n).fill(1));',
 'if(k>=6)emit([0]);if(k==='+k+'){if(s)for(let j=0;j<n;j++)emit(ids.map((_,i)=>i===j?0:i<j?-s:s));return out}if(!s){emit(Array(n).fill(1));');
 let result=new Function("src","patch",run)(src,patch);
 if(result.completed!==12||result.final.length!==0)throw Error("incomplete target "+k);
 console.log({target:k,checks:result.checks,completed:result.completed,unique:result.unique,final:result.final});
}
```

## Next

Only common-zero families with at least two distinct multipoint zero pencils remain. Choose any pair of multipoint zero anchors and use three noncollinear zero coordinates (p24 plus those anchors) to obtain a homogeneous 3-coefficient kernel, normalize a nonzero polar coefficient, and search the two remaining affine coefficients with exact endpoint and first/second-jet constraints. Pair candidates count before further geometric pruning is sum_{i<j} n_i n_j with n=(4,9,12,5,6,3), namely 605 (39 total; sum squares 311; (1521-311)/2=605). No need to choose singleton anchor pairs. Alternatively permit multiple multipoint zero words within the prefix circuit search. Do not redo the closed zero/single multipoint families. General c!=0 and K6 in {1,2} remain open. Independent review pending.
