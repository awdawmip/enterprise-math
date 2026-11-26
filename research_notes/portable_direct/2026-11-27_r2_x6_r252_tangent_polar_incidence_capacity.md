# X6 R252 — tangent-jet incidence and polar compatibility force further internal quadratic descent

2026-11-27. Author proof and exact BigInt computation; NOT_REVIEWED. Independent informed TASK_RESEARCH. Native request r2-20261127-0607-x6-read SUCCEEDED, observed 2026-11-26T22:07:43.203648Z, Source 673771a11b75db41a98bbaaebba8305fe8f28e30; NO_CANONICAL_PUBLICATION_DIRECTORY, directory absence only; live owner projection and own researcher identity not established. No CLAIM, Result, Review or shared task-state mutation. P000 V5, ACTIVE worldview and joint-observer/residual fidelity constraints retained. Auxiliary weight-coefficient arithmetic, not native spatial geometry/dynamics.

## Inputs and scope

R251: 79d86b4cd6896ce3265febc2bee908bfd6698710:research_notes/portable_direct/2026-11-27_r2_x6_r251_endpoint_incidence_capacity.md (blob 92dbdb465dff3063a8be604f3b03b3f82b695689).
R250: 2d25eecb9bc4101bebc4c27a24522e8f5b351515:research_notes/portable_direct/2026-11-27_r2_x6_r250_internal_quadratic_location_and_product_closure.md.
R247 executable input: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md.
Reuse exactly the frozen Port 10, 1935 integer directions, six-pair BRC, weights (17t,B,22t,D), strict 3/2 target, 47 necessary labelled supports, 49 components, 51 endpoint rays, 98 directed germs, 2225 linear masks. Inherit R250/R251 necessary-wall, full linear-germ bank and pure-linear capacity relaxation G, and R238 zero-germ factor lemma. R242/R250 product closure leaves full-rank indefinite quadratics. All original proof/review statuses are retained. The computations below exclude relaxed partitions, not a claim that a relaxed survivor would be an actual decision tree.

## 1. Tangent local sign lemma

Let Q(x)=x^T A x, A a real nonsingular symmetric 3 by 3 matrix, and let a directed germ have start p and other endpoint q, independent projective rays. When Q(p)=0 put g=Ap. Then g!=0, g·p=0 and
Q(p+epsilon(q-p))=2 epsilon g·q+epsilon^2 Q(q-p).
If g·q!=0, the strict infinitesimal sign is its sign. Otherwise Q(q-p)=Q(q), which is nonzero: if it vanished, the entire projective line span(p,q) would be in Q=0, giving a real linear factor (contradicts nonsingularity). Moreover all q with g·q=0 belong to the same two-dimensional auxiliary linear subspace g^perp containing p; if q'=alpha p+beta q (beta!=0), Q(q')=beta^2 Q(q). Thus the quadratic tangent residual is identical in sign for all tied germs at a given mixed endpoint. No zero germ is possible.

Enumerate the full local sign bank as follows. In the two-dimensional auxiliary gradient space p^perp, the hyperplanes g·q=0 are distinct lines through the origin after deduplication. Every nonzero gradient lies on one boundary ray or in an open angular sector adjacent to such a ray. For each q use g=±(p cross q), h=p cross g; both lie in p^perp, h independent of g. Boundary rays use sign(g·q') for nonzero values and either common +/- for all ties (an allowed relaxation of the actual uniform tangent residual). Adjacent sectors use lexicographic signs of (g·q', ±h·q'), with no unresolved tie because q' is independent of p. Every possible full-rank local pattern is included. If k distinct event lines occur, at most 2k open sectors and 2k rays with two residual options give at most 6k oriented patterns, hence at most 3k modulo simultaneous reversal; constant patterns can be omitted when the endpoint is required truly mixed. Unlike the R251 arbitrary exception signs, this is linear-size local enumeration. On the actual low-label targets p18 has 12 target germs but only 11 distinct nonconstant local masks modulo reversal. Retain exact bit identities, not only local counts.

## 2. Two-null-point polar compatibility

If Q(p)=Q(r)=0 at different projective endpoints, then B(p,r)=p^T A r is nonzero, by the same line-factor argument. Symmetry gives (Ap)·r=(Ar)·p. Multiplying Q by -1 exchanges both strict branches without changing the inherited G test; fix the common polar sign positive. To generate local masks at p add the constraint direction r to the list of gradient event lines, and at r add p. For a boundary ray require the actual polar value strictly positive (zero polar is impossible, even if a tangent residual can be assigned to an actual germ). For an adjacent sector use its lexicographic polar sign. Keep oriented local masks (do not canonically reverse each independently). Every full-rank quadratic with these mixed endpoints is represented by a pair in these two local banks. Independent local choices can allow some globally unrealizable pairs; rejecting all such relaxed choices is safe. Tangent signs at different endpoints are allowed independently, also a relaxation.

## 3. Complete incidence search on the declared ranges

R251 gives |D|<=30-c(T) for labels split between the two strict branches of target T. For a specified set M of truly mixed endpoints, enumerate all label exception supersets D' of exactly that budget. Build the graph of individual germs as in R251: equal signs at every endpoint outside M and every label outside D'. Components intersecting a prescribed positive and negative local mask simultaneously are contradictory; other components intersecting a mask are forced, and all free components are assigned both ways. Prune any partial branch with >15 labels. At completion, test G(X,4) AND G(Y,4), deduplicating only the whole target partition up to global exchange. All possible actual Q partitions with exactly M mixed endpoints are covered. In a singleton M fix its local orientation by global exchange; in a pair fix the nonzero polar positive as above. This does not discard any relevant joint observation; the bit masks keep all labels and full directed germ assignments. Only proven equality constraints are compressed in the relaxation. A CUT/timeout is not a rejection.

### Executed one-mixed search (six previously untested targets)

Common initial root classification: 3,275,335 checks, exactly 34 targets with counts 27:2, 28:4, 29:14, 30:14. Run all six c<29 with the tangent local banks; all complete and zero survivors. Table: target hex, c, label-exception/endpoint sets, branch visits, distinct direct-capacity passing masks, forced-component conflicts, incremental can checks.
```
3cc35cfff0003f3dff0000fcf 27 43875 360916 7461 32420 2031070
33cf3202fffc0c300ffffe30 27 40950 776487 11325 18370 2740139
2cb3010fffe7d304fffc030 28 4536 10748 98 1518 8597
2cb3010fffefd304fffc030 28 4536 10780 104 1518 4058
2cb3010fffefd30cfffc030 28 4536 10812 110 1518 4199
32cb3010fffe7c304fffc030 28 4536 16514 276 1518 26104
```
Total checks 8,089,502 including common prefix, incremental 4,814,167. Together with R251, all 34 targets require >=2 mixed endpoints.

### Executed exactly-two-mixed search (32 targets with c>=28)

Each of c=28,29,30 was run separately with common prefix and fresh caches. Every distinct candidate endpoint pair was included, all local banks nonempty, all branch assignments exhausted, zero relaxed survivors and zero unknown. Table: target hex, c, endpoint pairs, label-exception/endpoint sets, branch visits, direct-capacity passing masks, forced-component conflicts, oriented local pattern pairs (before label exceptions), incremental checks.
```
2cb3010fffe7d304fffc030 28 66 24948 143437 2237 80777 448 449907
2cb3010fffefd304fffc030 28 66 24948 145831 2405 80777 448 170391
2cb3010fffefd30cfffc030 28 66 24948 148295 2583 80777 448 178695
32cb3010fffe7c304fffc030 28 66 24948 232383 5369 74857 408 817571
33cf3010fffe7f304fffc030 29 78 2262 7789 233 9381 492 25658
33cf3303fffc0f300ffffff0 29 120 3480 6468 227 16402 690 16592
3fd3fcfef0003a3dfb0003fcf 29 120 3480 132339 8181 15167 672 907878
32cb3010fffe7d304fffc030 29 66 1914 9659 290 6901 448 25534
12cb3010fffefd304fffc030 29 66 1914 9701 297 6901 448 14816
32cf3010fffe7f304fffc030 29 78 2262 7727 223 9381 492 5187
12cf3010fffeff30cfffc030 29 78 2262 7825 239 9381 492 13631
12cf3010fffeff304fffc030 29 78 2262 7757 228 9381 492 11187
12cf3010fffe7f304fffc030 29 78 2262 7689 217 9381 492 0
20f3018fffeffb0cfffc030 29 78 2262 6280 121 10053 535 11435
33cb3010fffc7d304ffff030 29 66 1914 10077 326 6573 432 35892
3cc35dfff0003f3dffc000fcf 29 120 3480 13887 821 16748 751 91141
33cf3202fffc0f300ffffeb0 29 91 2639 14445 779 13334 589 80577
12cb3010fffefd30cfffc030 29 66 1914 9785 310 6901 448 13782
33cb3010fffe7d304ffff030 30 78 78 235 5 284 495 235
32cb3010fffe7d304fffe030 30 66 66 289 17 261 448 778
2cb3018fffefdb0cfffc030 30 78 78 238 1 315 549 94
3cd3fffef0003a3dfb8001fcf 30 136 136 961 98 630 783 4940
3fdf4cfef004183cfb0033fcf 30 91 91 23475 3174 300 551 160155
24f3018fffeffb0cfffc030 30 91 91 193 1 407 596 94
2cf3018fffeffb0cfffc030 30 91 91 193 1 407 596 94
3fdffcfef004183dfb0003fcf 30 120 120 3834 490 561 683 17766
3cd35dfff0003f3dffc001fcf 30 136 136 288 25 663 817 1175
3cd3fffff0003f3dffc001fcf 30 153 153 80 0 839 919 0
3fd3fffef0003a3dfb0003fcf 30 120 120 1799 218 581 710 8742
33cb3012fffc5c304ffffa30 30 78 78 263 13 271 474 966
3fdffcfef004383dfb0003fcf 30 120 120 3834 490 561 683 10672
3fdffcfef0003a3dfb0003fcf 30 120 120 3789 491 557 672 14602
```
c=28 total checks 4,891,899 incl. prefix (increment 1,616,564); c=29 total 4,528,645 (increment 1,253,310); c=30 total 3,495,648 (increment 220,313). Across four completed runs incremental can checks 7,904,354, plus four common prefixes. Exact two-mixed search for c=27 is not included in this artifact. All counts are summed across target masks, not deduplicated across targets.

## 4. Consequence and continuation

All 34 internal targets now require at least two actual mixed endpoints; 32 of them require at least three. Every such endpoint is a zero of Q, so all 34 descend to a finite union of coefficient kernels of dimension <=4; 32 descend to dimension <=3. Three distinct collinear zero points would force a line factor; for a full-rank candidate the mixed triples must be noncollinear. Their evaluation rows are independent (choose a linear form vanishing on the other two but not the selected one and square it). Hence the rank-three coefficient arrangement can be examined with existing R244/R246 exact techniques restricted to the actual target. For further combinatorial pruning a triple of independent null points has 2 B(p,r) B(r,s) B(s,p)=det(A) det[p,r,s]^2; the sign of this product fixes the common tangent residual sign to -sign(product), by R246 inertia lemma. This suggests a stronger multi-endpoint compatibility bank, not yet executed here. Preserve the two c=27 pair searches and all >=3 mixed cases as open; unique quadratic root and K6=1–2 remain open. No independent acceptance claimed.

## 5. Reproduction

Read the first JavaScript block of pinned R247 as src. The following consolidated patch reproduces the four completed variants (one-mixed mode c<29 and pair mode separately c=28,29,30). Only the reporting fields have been consolidated; the exact search and ordering match the runs above. Integer cross/dot, signs and bitmasks are BigInt; counters are exact JS integers within safe range. The inherited ceiling throws, and an interrupted run must not be interpreted as complete.

```javascript
function run(src,mode,c0){
 const patch=`ceiling=100000000;let roots=[];
for(let [a,b] of ordered){let ca=can(a,5),cb=can(b,5);if(ca&&cb)throw Error("linear");if(ca===cb)continue;let t=ca?b:a;if(count(t)<=30)roots.push(t)}
let initialChecks=checks,result=[];
function localPatterns(i,bits,j){
 const p=P[i],out=new Map(),rays=G.filter(([u,v,b])=>u===i&&(b&bits)),dirs=[...rays.map(x=>x[1]),...(j<0?[]:[j])];
 for(let v of dirs){let g=cross(p,P[v]);if(!nz(g))throw Error("parallel germ");
 for(let e of [-1n,1n]){let w=scale(g,e),h=cross(p,w);
 for(let mode of [-2,-1,1,2]){
  if(j>=0){let polar=sg(dot(w,P[j]));if(!polar&&Math.abs(mode)===1)polar=mode*sg(dot(h,P[j]));if(polar!==1)continue;}
  let a=0n,b=0n;
  for(let [u,k,z] of rays){let s=sg(dot(w,P[k]));if(!s)s=Math.abs(mode)===2?Math.sign(mode):mode*sg(dot(h,P[k]));if(!s)throw Error("zero local");if(s>0)a|=z;else b|=z}
  if(a&&b){if(j<0)[a,b]=canon(a,b);out.set(a+","+b,[a,b])}
 }}}
 return [...out.values()];
}
for(let t of roots.filter(t=>${mode}===1?count(t)<29:count(t)===${c0})){
 let L=tag.map((v,i)=>[v&t,i]).filter(([v])=>v),E=P.map((_,i)=>({i,bits:G.filter(([u,v,b])=>u===i&&(b&t)).map(([u,v,b])=>b)})).filter(x=>x.bits.length);
 let c=L.length,budget=30-c,visited=new Set(),survivors=[],sets=0,branches=0,direct=0,conflicts=0,pairs=[],before=checks;
 function test(skip,i,j,patterns){
  sets++;let comps=E.flatMap(({i:k,bits})=>k===i||k===j?bits:[bits.reduce((a,b)=>a|b,0n)]);
  for(let [v,k] of L)if(!skip.has(k)){let x=v,rest=[];for(let y of comps){if(x&y)x|=y;else rest.push(y)}rest.push(x);comps=rest;}
  comps.sort((a,b)=>count(b)-count(a));
  for(let [pa,pb] of patterns){let a=0n,b=0n,free=[],bad=false;
   for(let x of comps){if((x&pa)&&(x&pb)){bad=true;break}if(x&pa)a|=x;else if(x&pb)b|=x;else free.push(x)}
   if(bad){conflicts++;continue}
   function rec(k,a,b){branches++;if(count(a)>15||count(b)>15)return;
    if(k===free.length){let [x,y]=canon(a,b);if(visited.has(x))return;visited.add(x);direct++;if(can(x,4)&&can(y,4))survivors.push([x.toString(16),y.toString(16),i,j]);return}
    rec(k+1,a|free[k],b);rec(k+1,a,b|free[k]);
   }rec(0,a,b);
  }
 }
 function choose(start,need,skip,i,j,patterns){if(!need){test(skip,i,j,patterns);return}for(let k=start;k<=L.length-need;k++){skip.add(L[k][1]);choose(k+1,need-1,skip,i,j,patterns);skip.delete(L[k][1])}}
 const M=E.filter(x=>x.bits.length>1);
 if(${mode}===1){
  for(let {i,bits} of M){let A=localPatterns(i,bits.reduce((a,b)=>a|b,0n),-1);pairs.push([i,-1,A.length]);if(A.length)choose(0,budget,new Set(),i,-1,A)}
 }else for(let k=0;k<M.length;k++)for(let l=k+1;l<M.length;l++){
  let {i,bits}=M[k],{i:j,bits:bb}=M[l],A=localPatterns(i,bits.reduce((a,b)=>a|b,0n),j),B=localPatterns(j,bb.reduce((a,b)=>a|b,0n),i);
  let pats=A.flatMap(([a,b])=>B.map(([x,y])=>[a|x,b|y]));pairs.push([i,j,pats.length]);if(pats.length)choose(0,budget,new Set(),i,j,pats);
 }
 result.push({t:t.toString(16),c,sets,branches,direct,conflicts,pairs:pairs.length,nonempty:pairs.filter(x=>x[2]).length,localPatternPairs:pairs.reduce((s,x)=>s+x[2],0),survivors,checks:checks-before});
}
return {initialChecks,checks,result};`;
 const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
 if(!src.includes(old))throw Error("pin mismatch");
 return Function(src.replace(old,patch).replace(/experiment\(data\)\s*$/,"return experiment(data)"))();
}
// run(src,1,0); run(src,2,28); run(src,2,29); run(src,2,30);
```

Activity association and independent review pending; directory absence does not establish an active owner.
