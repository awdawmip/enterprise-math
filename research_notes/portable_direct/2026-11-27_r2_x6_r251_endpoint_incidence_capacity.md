# X6 R251 — endpoint-incidence capacity obstruction for the unique internal quadratic

2026-11-27. Author proof and exact BigInt experiments, NOT_REVIEWED. Independent informed TASK_RESEARCH. Native read r2-20261127-0511-x6-read SUCCEEDED at 2026-11-26T21:12:07.474349Z, Source 8d69fb4742cd97bca2d88a6ff486fc92fb93f6a0: NO_CANONICAL_PUBLICATION_DIRECTORY, native operational/owner projection not evaluated. No own Researcher-ID verified, no CLAIM, Result or Review mutation. P000 V5 and ACTIVE worldview unchanged. Auxiliary weight-coefficient computation, not native geometry or dynamics.

## Frozen inputs and inherited premises

R250: 2d25eecb9bc4101bebc4c27a24522e8f5b351515:research_notes/portable_direct/2026-11-27_r2_x6_r250_internal_quadratic_location_and_product_closure.md.
R247 executable input: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md.
Port 10, 1935 integer directions, six-pair BRC, weights (17t,B,22t,D), strict 3/2 output, 47 labelled supports, 49 connected components, 51 endpoint rays, 98 directed germs, 2225 linear masks. Inherit R250's necessary-wall and complete linear-germ capacity premises; R238 zero-germ factor lemma and R242/R250 real-product exclusion. All source proofs retain their original review status.

## 1. Incidence capacity lemma

Let T be one of R250's 34 forced internal target germ masks, and c(T) the number of represented support labels. A candidate full-rank indefinite Q has no zero interval germ (R238); thus T=X disjoint union Y, its two strict sign branches. Each child has only four linear levels remaining. G(X,4) and G(Y,4) require c(X),c(Y)<=15. If D is the set of support labels appearing in both X and Y, the exact double-counting identity is
  |D| = c(X)+c(Y)-c(T) <= 30-c(T).
Call an endpoint mixed when two germs of T starting there have opposite Q signs. This implies Q(p)=0, by continuity of Q(p+epsilon v) and lexicographic jet evaluation. Nonmixed endpoints need not have nonzero Q(p); they may have zero with all incident signs equal. Hence the obstruction concerns mixed endpoints, not merely sampled zeros.

Construct a graph on the individual directed germs of T, adding equality edges between germs with the same label outside a selected exception set D' of size 30-c(T), and between germs starting at the same endpoint outside a selected endpoint exception set M. Every actual successful partition with mixed endpoints contained in M is constant on the graph components for some D': extend its actual split labels D to D' (there are enough labels). Enumerating all D' and all permitted M, then all binary component signs modulo global reversal, covers every such successful partition, even when some exceptions are not truly mixed/split. This is a relaxation: it allows arbitrary signs at exceptional endpoints and does not assume a feasible quadratic. Each complete partition is checked by the inherited exact G on both children. Partial sign assignments exceeding 15 distinct labels are safely pruned because c is monotone. Deduplication by canonical sign mask is safe within the same T because its complement and both child capacities are determined exactly. Label identity and individual germ identity are retained throughout. This uses the BRC support-label structure without conflating equal scalar counts with equal continuation states.

## 2. Executed exact experiment

First recomputed the common 2225-root classification: 3,275,335 inherited can() observation checks, 34 forced targets with counts 27:2, 28:4, 29:14, 30:14 (as R250). For every one of the 34, take M empty. All 7,782 choices of D' across targets were enumerated (sum of binomial(c,30-c)). Only 232 distinct complete masks per-target summed passed both direct label bounds: 215 and 17 in the two c=27 targets, zero in all other targets. All 232 failed the exact depth4 suffix test. Total can checks including common prefix 3,315,391; incremental 40,056. No cutoff.

Then take M to be one endpoint with at least two target germs (only these can be mixed). For the 28 targets with c>=29, enumerate every such M and D'. All completed, zero relaxed survivors. Total can checks including independently recomputed common prefix 10,260,814; incremental 6,985,479. The full 34-target one-exception run hit the tool execution timeout; no claims from that attempt. The completed restricted run is the evidence. The remaining six lower-label targets (c=27,28) are NOT tested for one mixed endpoint.

Per-target completed one-exception results (target hex, c, D'/M choices, distinct capacity-passing masks; all survivors zero):
33cf3010fffe7f304fffc030 29 377 11186
33cf3303fffc0f300ffffff0 29 464 31
3fd3fcfef0003a3dfb0003fcf 29 464 285
32cb3010fffe7d304fffc030 29 348 11670
33cb3010fffe7d304ffff030 30 13 434
32cb3010fffe7d304fffe030 30 12 862
12cb3010fffefd304fffc030 29 348 11670
2cb3018fffefdb0cfffc030 30 13 220
3cd3fffef0003a3dfb8001fcf 30 17 0
3fdf4cfef004183cfb0033fcf 30 14 305
32cf3010fffe7f304fffc030 29 377 10758
12cf3010fffeff30cfffc030 29 377 11186
12cf3010fffeff304fffc030 29 377 10758
12cf3010fffe7f304fffc030 29 377 10330
20f3018fffeffb0cfffc030 29 377 6212
24f3018fffeffb0cfffc030 30 14 220
2cf3018fffeffb0cfffc030 30 14 220
33cb3010fffc7d304ffff030 29 348 12471
3cc35dfff0003f3dffc000fcf 29 464 43
3fdffcfef004183dfb0003fcf 30 16 0
33cf3202fffc0f300ffffeb0 29 406 233
3cd35dfff0003f3dffc001fcf 30 17 0
3cd3fffff0003f3dffc001fcf 30 18 0
3fd3fffef0003a3dfb0003fcf 30 16 0
12cb3010fffefd30cfffc030 29 348 12098
33cb3012fffc5c304ffffa30 30 13 496
3fdffcfef004383dfb0003fcf 30 16 0
3fdffcfef0003a3dfb0003fcf 30 16 0

## 3. Consequence and next

Conditional on inherited capacity premises, every successful full-rank indefinite internal quadratic must have at least one mixed endpoint of its actual target T, and for 28 of 34 targets must have at least two distinct mixed endpoints. Thus instead of searching all of R^6, search a finite union of five-dimensional linear kernels Q(p)=0; for the 28 targets use four-dimensional kernels Q(p)=Q(r)=0. Distinct projective rays give independent quadratic evaluation rows: choose a linear form vanishing on one but not the other and square it, proving independence. Mixed endpoints have at least two incident target germs. For a full-rank conic no three distinct collinear endpoints can be zeros (restriction to the projective line is a binary quadratic; three zeros force a real factor). These facts offer a tighter next step: enumerate permitted pairs of mixed endpoints, derive their exact kernels, and apply the R245/R247 signed primary-face pruning restricted to T, or extend the graph search to two endpoint exceptions with exact conflict certificates. For the six low-label targets, partition the one-exception search to avoid the observed timeout. General root case, all internal targets with more mixed endpoints, and K6=1–2 remain open; no complete internal exclusion or feasible tree claimed.

## 4. Reproduction

Read first JavaScript code block of pinned R247 into src. Replace the final return by the following patch, replace final experiment(data) by return experiment(data), run Function(patched)(). For mode=0 run on all targets; for mode=1 run on c>=29. This consolidated reproduction is equivalent to the two completed runs: the actual mode0 variant used endpoint masks directly and recorded component histograms; mode1 used individual bits and recorded mixed candidate endpoint indices. These differences do not change enumeration or suffix checks. No floating-point geometry used; BigInt masks, exact counts and inherited exact G. The inherited CUT throws and must not be treated as an exclusion.

```javascript
const patch = (mode) => `ceiling=100000000;let roots=[];
for(let [a,b] of ordered){let ca=can(a,5),cb=can(b,5);if(ca&&cb)throw Error("linear");if(ca===cb)continue;let t=ca?b:a;if(count(t)<=30)roots.push(t)}
let initialChecks=checks,result=[];
for(let t of roots.filter(t=>${mode}===0||count(t)>=29)){
 let L=tag.map((v,i)=>[v&t,i]).filter(([v])=>v);
 let E=P.map((_,i)=>({i,bits:G.filter(([u,v,b])=>u===i&&(b&t)).map(([u,v,b])=>b)})).filter(x=>x.bits.length);
 let c=L.length,budget=30-c,visited=new Set(),survivors=[],sets=0,branches=0,direct=0;
 function test(skip,mixed){
  sets++;let comps=E.flatMap(({i,bits})=>i===mixed?bits:[bits.reduce((a,b)=>a|b,0n)]);
  for(let [v,i] of L)if(!skip.has(i)){
   let x=v,rest=[];for(let y of comps){if(x&y)x|=y;else rest.push(y)}rest.push(x);comps=rest;
  }
  comps.sort((a,b)=>count(b)-count(a));
  function rec(j,a,b){
   branches++;if(count(a)>15||count(b)>15)return;
   if(j===comps.length){let [x,y]=canon(a,b);if(visited.has(x))return;visited.add(x);direct++;
    if(can(x,4)&&can(y,4))survivors.push([x.toString(16),y.toString(16)]);return}
   rec(j+1,a|comps[j],b);rec(j+1,a,b|comps[j]);
  }rec(1,comps[0],0n)
 }
 function choose(start,need,skip,mixed){if(!need){test(skip,mixed);return}for(let j=start;j<=L.length-need;j++){skip.add(L[j][1]);choose(j+1,need-1,skip,mixed);skip.delete(L[j][1])}}
 if(${mode}===0)choose(0,budget,new Set(),-1);
 else for(let {i,bits} of E)if(bits.length>1)choose(0,budget,new Set(),i);
 result.push({t:t.toString(16),c,sets,branches,direct,survivors});
}
return {initialChecks,checks,result};`;
function run(src,mode){
 const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
 if(!src.includes(old))throw Error("pin mismatch");
 return Function(src.replace(old,patch(mode)).replace(/experiment\(data\)\s*$/,"return experiment(data)"))()
}
// run(src,0), run(src,1)
```

Activity association and independent review pending. No shared task ownership inferred from the topic lookup.