# EC49GCA — Monotone residual thresholds and exact restricted-boundary dominance

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRUTE_REPLAY / NOT_REVIEWED.
Predecessor: c23e1dccfd5d2b158da6ea5f65c38ad71049c4e6:research_notes/portable_direct/EC49GBZ_DIFFERENCE_SUPPORT_DOMINANCE.md (blob b2f9b2ba623e3a6dd927a4b840c3a152fad4fb14, read this turn).
Also read GBX at 80231aca033f53fffaa69d60ac1e290f0947c1fc:research_notes/portable_direct/EC49GBX_BOUNDED_DEFICIT_BOUNDARY_SIGNATURE.md (blob e668872ac8ffdbf95c95fcbceedf43fee2396edf).
Frozen scientific identifier BRC16943 inherited unchanged; no raw archive replay. Auxiliary finite labeled strict-Hall model only; no native physical calculation, no change of P000 or interpretation of ordinary integer synthetic tests as typed native BRC execution.

## 1. Monotone residual theorem, even for different extending bases
Finite ports C, positive integer capacities c_i, nonempty neighborhoods E_x of distinct labels, prefix A. For a strictly independent set H (f_H(V)<=c(V)-1 for all nonempty V), define h_H(U)=min_{V containing U}[c(V)-f_H(V)], including h_H(empty)=0. GBX and GBZ establish the insertion oracle and monotone submodularity of h_H. For a basis J of A, h_A=h_J is independent of J (fresh identical-neighborhood probe argument in GBX). For independent S subset A, extend to any J_S=S+Z of size r(A), with d_S=|Z|. Put delta_S=h_S-h_A.

GBZ's expansion, valid including U=empty by independence, gives
 h_A(U)=min_{K subset Z}[h_S(U union E_K)-|K|].
Thus
 delta_S(U)=max_{K subset Z}[|K|-(h_S(U union E_K)-h_S(U))].
Each fixed-K expression is monotone nondecreasing under inclusion of U by submodular diminishing returns (for a set E_K, including overlap). Hence delta_S is monotone nondecreasing, integer, 0<=delta_S<=d_S, delta_S(empty)=0. This is an extension of GBX's coordinate bounds; no common extending basis for S and T is required. For empty boundary all comparisons are vacuous.

Proof of diminishing returns for arbitrary E: if U subset V, submodularity applied to U union E and V gives h(U union E)+h(V)>=h(V union E)+h((U union E) intersect V)>=h(V union E)+h(U); rearrange.

## 2. Exact threshold-antichain certificate on any restricted boundary B subset C
For 1<=k<=d_S define the upward-closed family F_S,k={U subset B:delta_S(U)>=k}, with minimal members L_S,k. Then
 delta_S(U)=sum_{k=1}^{d_S} 1_{exists L in L_S,k:L subset U}.
For S,T independent in the same A, h_T<=h_S on B iff for every 1<=k<=d_T every minimal trigger L in L_T,k satisfies delta_S(L)>=k. Equalities of h_A cancel; empty trigger families cause no constraints. This criterion is necessary and sufficient even if the differing label supports extend outside B or S,T extend to different bases. GBX then gives exact inclusion of all arbitrary fresh insertion-only suffix feasibilities supported in B, with no bound on suffix length. A failed threshold at U yields h_T(U)>h_S(U); U is nonempty and h_S(U) fresh distinct labels with support U separate T from S.

If the threshold antichains were already materialized for a larger boundary, restriction simply retains members contained in B. This follows from upward closure and minimality. This representation is canonical for fixed reference prefix A and boundary B, but not necessarily small.

## 3. Adaptive two-sided cone certificate, with no precomputed antichains
For one threshold k maintain lists L (minimal true sets of delta_S>=k) and H (maximal false sets of delta_T>=k) discovered so far. The upward cones of L and downward cones of H are safe regions for the desired implication. Find any subset U of B outside their union. This is precisely the SAT instance with one clause OR_{i in l} not x_i for every l in L and one clause OR_{i in B\h} x_i for every h in H. Empty clause means no uncovered point. If no such subset exists, the threshold implication holds. Otherwise:
* If delta_S(U)>=k, greedily delete elements while preserving the inequality; record the resulting globally minimal true set.
* Else if delta_T(U)>=k, return the separating U.
* Else greedily add elements while preserving delta_T<k; record the resulting globally maximal false set.
One pass suffices in each greedy operation by monotonicity. Each new cone was not already recorded because the original U was uncovered. Thus at most |L_S,k|+|H_T,k| successful cone discoveries per threshold, plus at most one failing point overall. With b=|B|, at most b+2 delta-oracle requests per discovery and at most two for the failing point. Each delta evaluation can use at most two GBZ max-flow queries, with a cached common reference and direct h queries. A positive certificate consists of the cone lists, oracle checks at their generators, and Boolean coverage (unsatisfiability of the above formula); no dense h table is required. The replay uses exact DPLL with unit propagation, plus exhaustive independent verification of cover and comparisons. General Boolean coverage cost may be exponential; no FPT-in-deficit or runtime speedup claim. In particular this is output-sensitive in oracle evaluations, not a polynomial total-time guarantee.

## 4. A complete polynomial special case: unit-capacity graph forests
For capacities all 1 and two-port labels, independence is forest independence (GBX). If H is a forest, h_H(U) equals the number of connected components of H touched by U, including isolated vertices. Indeed c(V)-f_H(V) counts components of the induced forest on V; this is at least the number of whole-forest components touched by U, and taking their whole union attains equality. For two forests S,T, restricted dominance h_T<=h_S on B is equivalent to the S partition restricted to B refining the T partition restricted to B. Necessity: if one S block meets two T blocks, choose the two boundary vertices, giving h_S=1 and h_T=2. Sufficiency: every S block meets only one T block, so the number of T blocks touched cannot exceed S blocks touched. Compute component identifiers using union-find and scan B to check that each S component maps to one T component; near-linear graph construction/scan cost, independent of deficits and without shared basis. Failed dominance has a two-port witness and one fresh edge. This supplies a compact exact comparator in the very family where GBX proved exponentially many distinct states.

## 5. Two obstructions to general small-threshold interfaces
(a) Arbitrarily high witness arity even with deficit one and common extending basis: take b>=2 unit ports B, one external unit port a, C=B+a. Prefix J={x,y}, E_x=B, E_y=C, is independent. S={x}, T={y}. Both deficits are 1. For proper U subset B, h_S(U)=h_T(U)=|U|. At U=B, h_S=b-1 and h_T=b. Thus all restricted observers using fewer than b ports agree, yet b-1 fresh labels on B distinguish the states. This is an arity lower bound, not a query lower bound for an algorithm exploiting labels.
(b) Exponential minimal triggers at deficit one: for n>=3, 2<=k<=n, unit ports C of size n, J contains n-k+1 distinct labels all supported on C, S=J minus one label. Then J independent, h_A(U)=min(|U|,k-1), h_S(U)=min(|U|,k), delta_S(U)=1_{|U|>=k}. Hence exactly binomial(n,k) minimal threshold triggers, exponentially many for central k. If S=T, any coverage proof using only safe monotone cones for that threshold must include every minimal true and every maximal false generator: a minimal true point can only be covered by its own upward cone; similarly for a maximal false point. This is a lower bound for that explicit certificate language only; equality can have other much smaller proofs. The cut network remains polynomial-size.

## 6. Executed verification
Deterministic xorshift32 seed 20261128. 400 random finite labeled models (2..8 ports, capacities 1..4, 2..13 labels), two independently ordered greedy bases, up to 3 labels removed from each. Checked basis invariance and residual monotonicity on every Boolean cover, four directed comparisons per model (one random boundary and full boundary, each direction). Adaptive algorithm uses integer Edmonds-Karp max-flow, separately compared with dense direct strict-Hall minima via min-zeta transform. Every failed comparison has direct fresh-label witness, every successful threshold cover is checked exhaustively. 200 random unit-capacity graph models tested in both directions; arity cases b=2..10; binomial family n=3..12. No timing or general distribution guarantee. Counts of oracle queries and dense coordinates are different operations and not a performance ratio.

Actual executed output:
```json
{
  "seed": 20261128,
  "models": 400,
  "comparisons": 1600,
  "restrictedComparisons": 732,
  "differentExtendingBases": 85,
  "basisCoordinates": 30152,
  "residualCoverChecks": 212792,
  "denseComparisonCoordinates": 67604,
  "adaptiveDeltaRequests": 30620,
  "adaptiveDistinctDeltaQueries": 21641,
  "flowCalls": 34012,
  "satNodes": 20415,
  "coverBlocks": 5576,
  "coverVerificationCoordinates": 20638,
  "dominanceTrue": 977,
  "dominanceFalse": 623,
  "separatorChecks": 623,
  "graphModels": 200,
  "graphComparisons": 400,
  "graphCoordinates": 3256,
  "arityCases": 9,
  "antichainCases": 10,
  "antichainCounts": [
    [
      3,
      2,
      3
    ],
    [
      4,
      2,
      6
    ],
    [
      5,
      2,
      10
    ],
    [
      6,
      3,
      20
    ],
    [
      7,
      3,
      35
    ],
    [
      8,
      4,
      70
    ],
    [
      9,
      4,
      126
    ],
    [
      10,
      5,
      252
    ],
    [
      11,
      5,
      462
    ],
    [
      12,
      6,
      924
    ]
  ],
  "disagreements": 0
}
```

Standalone replay source (actual executed function):
```javascript
function replay(){
 let z=20261128; const rnd=n=>{z^=z<<13;z^=z>>>17;z^=z<<5;return(z>>>0)%n};
 const st={seed:20261128,models:0,comparisons:0,restrictedComparisons:0,differentExtendingBases:0,basisCoordinates:0,residualCoverChecks:0,denseComparisonCoordinates:0,adaptiveDeltaRequests:0,adaptiveDistinctDeltaQueries:0,flowCalls:0,satNodes:0,coverBlocks:0,coverVerificationCoordinates:0,dominanceTrue:0,dominanceFalse:0,separatorChecks:0,graphModels:0,graphComparisons:0,graphCoordinates:0,arityCases:0,antichainCases:0,antichainCounts:[],disagreements:0};
 const check=(x,m)=>{if(!x){st.disagreements++;throw Error(m)}};
 const sub=(a,b)=>(a&b)===a, pop=v=>{let k=0;while(v){v&=v-1;k++}return k};
 function masks(c){return Array.from({length:1<<c.length},(_,u)=>c.reduce((s,v,i)=>s+((u>>i&1)*v),0))}
 function count(A,v){return A.reduce((n,x)=>n+Number(sub(x.e,v)),0)}
 function ok(cc,A){for(let v=1;v<cc.length;v++)if(count(A,v)>=cc[v])return false;return true}
 function dense(cc,A){let a=cc.map((c,v)=>c-count(A,v));for(let bit=1;bit<cc.length;bit*=2)for(let v=0;v<cc.length;v++)if(!(v&bit))a[v]=Math.min(a[v],a[v|bit]);return a}
 function shuffle(A){let a=[...A];for(let i=a.length-1;i>0;i--){let j=rnd(i+1);[a[i],a[j]]=[a[j],a[i]]}return a}
 function greedy(cc,A){let j=[];for(let x of A)if(ok(cc,[...j,x]))j.push(x);return j}
 function flow(c,A,u){
  if(!u)return 0;
  st.flowCalls++;
  let n=c.length,s=n+A.length,t=s+1,N=t+1,M=1+c.reduce((a,b)=>a+b,0)+A.length;
  let g=Array.from({length:N},()=>Array(N).fill(0));
  for(let j=0;j<A.length;j++){g[s][n+j]=1;for(let i=0;i<n;i++)if(A[j].e&(1<<i))g[n+j][i]=M}
  for(let i=0;i<n;i++){g[i][t]=c[i];if(u&(1<<i))g[s][i]=M}
  let f=0;
  while(true){let p=Array(N).fill(-1),Q=[s];p[s]=s;
   for(let k=0;k<Q.length;k++)for(let j=0;j<N;j++)if(p[j]<0&&g[Q[k]][j]>0){p[j]=Q[k];Q.push(j)}
   if(p[t]<0)return f-A.length;
   let d=M;for(let j=t;j!==s;j=p[j])d=Math.min(d,g[p[j]][j]);
   for(let j=t;j!==s;j=p[j]){g[p[j]][j]-=d;g[j][p[j]]+=d}f+=d
  }
 }
 // Return a subset of B not in any upward L or downward H cone, or null.
 function uncovered(B,L,H){
  let clauses=[...L.map(l=>[0,l]),...H.map(h=>[B&~h,0])];
  function dfs(on,off){
   st.satNodes++;
   while(true){
    let unit=false,choice=0;
    for(let [p,n] of clauses){
     if((p&on)||(n&off))continue;
     let rem=(p|n)&~(on|off);
     if(!rem)return null;
     if((rem&(rem-1))===0){if(rem&p)on|=rem;else off|=rem;unit=true;break}
     if(!choice)choice=rem&-rem;
    }
    if(unit)continue;
    if(!choice)return on;
    let a=dfs(on,off|choice);return a===null?dfs(on|choice,off):a;
   }
  }
  return dfs(0,0)
 }
 function compare(c,cc,J,S,T,B){
  let ref=dense(cc,J),hs=dense(cc,S),ht=dense(cc,T),ds=J.length-S.length,dt=J.length-T.length;
  let caches=[new Map(),new Map(),new Map()],sets=[J,S,T],truths=[ref,hs,ht];
  function h(i,u){if(caches[i].has(u))return caches[i].get(u);let v=flow(c,sets[i],u);check(v===truths[i][u],"flow");caches[i].set(u,v);return v}
  let dc=[new Map(),new Map()];
  function delta(i,u){st.adaptiveDeltaRequests++;if(dc[i].has(u))return dc[i].get(u);st.adaptiveDistinctDeltaQueries++;let a=h(i+1,u)-h(0,u);dc[i].set(u,a);return a}
  let expected=true;for(let u=B;u;u=(u-1)&B){st.denseComparisonCoordinates++;if(ht[u]>hs[u])expected=false}
  let witness=null,cert=[];
  for(let k=1;k<=dt;k++){
   let L=[],H=[];
   while(true){
    let u=uncovered(B,L,H);
    if(u===null)break;
    if(delta(0,u)>=k){
     for(let bit=1;bit<=B;bit*=2)if((u&bit)&&delta(0,u^bit)>=k)u^=bit;
     L.push(u);st.coverBlocks++;
    }else if(delta(1,u)>=k){witness=u;break}
    else{
     for(let bit=1;bit<=B;bit*=2)if((B&bit)&&!(u&bit)&&delta(1,u|bit)<k)u|=bit;
     H.push(u);st.coverBlocks++;
    }
   }
   if(witness!==null)break;
   cert.push([k,L,H]);
  }
  check((witness===null)===expected,"dominance");
  if(witness!==null){
   st.dominanceFalse++;check(witness!==0&&ht[witness]>hs[witness],"witness");
   let probes=Array.from({length:hs[witness]},(_,i)=>({id:10000+i,e:witness}));
   check(ok(cc,[...T,...probes])&&!ok(cc,[...S,...probes]),"separating suffix");st.separatorChecks++;
  }else{
   st.dominanceTrue++;
   for(let [k,L,H] of cert){
    for(let l of L){check(hs[l]-ref[l]>=k,"up cone");for(let bit=1;bit<=B;bit*=2)if(l&bit)check(hs[l^bit]-ref[l^bit]<k,"minimal trigger")}
    for(let h of H){check(ht[h]-ref[h]<k,"down cone");for(let bit=1;bit<=B;bit*=2)if((B&bit)&&!(h&bit))check(ht[h|bit]-ref[h|bit]>=k,"max false")}
    for(let u=B;;u=(u-1)&B){check(L.some(l=>sub(l,u))||H.some(h=>sub(u,h)),"cover");st.coverVerificationCoordinates++;if(!u)break}
   }
  }
  st.comparisons++;if(B!==cc.length-1)st.restrictedComparisons++;
 }
 for(let it=0;it<400;it++){
  let n=2+rnd(7),c=Array.from({length:n},()=>1+rnd(4)),cc=masks(c),N=cc.length;
  let A=Array.from({length:2+rnd(12)},(_,id)=>({id,e:1+rnd(N-1)})),J=greedy(cc,shuffle(A)),K=greedy(cc,shuffle(A));
  check(J.length===K.length,"basis rank");
  if(J.some(x=>!K.some(y=>x.id===y.id)))st.differentExtendingBases++;
  let S=shuffle(J).slice(rnd(Math.min(3,J.length)+1)),T=shuffle(K).slice(rnd(Math.min(3,K.length)+1));
  let h=dense(cc,J),h2=dense(cc,K),a=dense(cc,S),b=dense(cc,T);
  for(let u=0;u<N;u++){
   check(h[u]===h2[u],"basis invariance");st.basisCoordinates++;
   for(let [v,d] of [[a,J.length-S.length],[b,K.length-T.length]]){
    check(v[u]-h[u]>=0&&v[u]-h[u]<=d,"bounded residual");
    for(let bit=1;bit<N;bit*=2)if(!(u&bit)){check(v[u]-h[u]<=v[u|bit]-h[u|bit],"monotone residual");st.residualCoverChecks++}
   }
  }
  let B=1+rnd(N-1);compare(c,cc,J,S,T,B);compare(c,cc,J,T,S,B);compare(c,cc,J,S,T,N-1);compare(c,cc,J,T,S,N-1);st.models++;
 }
 // Unit-capacity graph specialization. Independent forests on a common complete graph.
 for(let it=0;it<200;it++){
  let n=2+rnd(7),c=Array(n).fill(1),cc=masks(c),N=cc.length,A=[];
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)A.push({id:A.length,e:(1<<i)|(1<<j)});
  let J=greedy(cc,shuffle(A)),K=greedy(cc,shuffle(A)),S=shuffle(J).slice(rnd(J.length+1)),T=shuffle(K).slice(rnd(K.length+1));
  function parts(F){let p=Array.from({length:n},(_,i)=>1<<i);for(let e of F){let w=0;for(let i=0;i<n;i++)if(e.e&(1<<i))w|=p[i];for(let i=0;i<n;i++)if(w&(1<<i))p[i]=w}return [...new Set(p)]}
  let B=1+rnd(N-1);
  for(let [s,t] of [[S,T],[T,S]]){
   let ps=parts(s),pt=parts(t),hs=dense(cc,s),ht=dense(cc,t);
   let pred=ps.every(p=>!(p&B)||pt.some(q=>sub(p&B,q))),actual=true;
   for(let u=B;u;u=(u-1)&B){check(hs[u]===ps.filter(p=>p&u).length&&ht[u]===pt.filter(p=>p&u).length,"partition formula");if(ht[u]>hs[u])actual=false;st.graphCoordinates++}
   check(pred===actual,"partition dominance");st.graphComparisons++;
  }
  st.graphModels++;
 }
 // Arity obstruction: same extending basis, deficit one, proper boundary.
 for(let b=2;b<=10;b++){
  let B=(1<<b)-1,C=(1<<(b+1))-1,c=Array(b+1).fill(1),cc=masks(c),x={id:0,e:B},y={id:1,e:C},J=[x,y],S=[x],T=[y];
  check(ok(cc,J),"arity independent");
  let hs=dense(cc,S),ht=dense(cc,T);
  for(let u=B;;u=(u-1)&B){check(ht[u]-hs[u]===Number(u===B),"arity");if(!u)break}
  st.arityCases++;
 }
 // Uniform residual threshold with exponentially many minimal triggers.
 for(let n=3;n<=12;n++){
  let k=Math.max(2,Math.floor(n/2)),C=(1<<n)-1,c=Array(n).fill(1),cc=masks(c),J=Array.from({length:n-k+1},(_,id)=>({id,e:C})),S=J.slice(1);
  check(ok(cc,J),"uniform independent");let h=dense(cc,J),a=dense(cc,S),m=0;
  for(let u=0;u<=C;u++){check(a[u]-h[u]===Number(pop(u)>=k),"uniform threshold");if(pop(u)===k)m++}
  let choose=1;for(let j=1;j<=k;j++)choose=choose*(n-j+1)/j;check(m===choose,"binomial");st.antichainCounts.push([n,k,m]);st.antichainCases++;
 }
 return st
}
console.log(JSON.stringify(replay()));

```

## 7. Continuation and provenance
Global canonical main e0fa7404b8b44cdb12918d61e52c7d059759960c; entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613 verified at that immutable ref. P000 V4/V5, ACTIVE worldview, joint and residual constraints, current normative continuation, portable protocol and role rules consulted. Control source dc4440436ec5f786af0c2a3eeb9359d10858bb53, exact read r4-20261128-0330-ec49as-read SUCCEEDED: NO_CANONICAL_PUBLICATION_DIRECTORY for RS-EC49AS; native owner projection not evaluated; execution_authorized=false. Current private identity unconfirmed; historical predecessor provenance EM-DIRECT-23537B only. Independent portable research; no claim, new session or task mutation. Activity association pending. No frozen archive replay; no physical root progress; inherited GBT historical frontier 1991 feasible, 68 excluded, 334 other, next root 2046, M14 in [25,27].
Next: integrate optional restricted dominance into GBY DP with cached basis queries and label witness backtracking; compare total computation (including SAT coverage, flows, and preprocessing) on identical synthetic and original frozen inputs when available. First try graph partition shortcut or cheap GBZ sufficient condition; fall back to adaptive threshold comparator if useful. Explore more compact certificate languages that avoid the explicit threshold antichain obstruction. Preserve all labels/provenance for observers beyond insertion-only maximum reward.
