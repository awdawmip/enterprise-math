# EC49GBZ — Difference-support dominance tests and low-deficit cut-network comparison

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRUTE_REPLAY / NOT_REVIEWED.
Predecessor: 26131f46a7f318d19bc158caeeac0ed0f60844fb:research_notes/portable_direct/EC49GBY_CUT_NETWORK_SPARSE_BUDGET_DP.md (blob 8b733c13a907f45134d3097e785ca5489640dc0c, actually read). BRC16943 inherited frozen science, raw archive not read/replayed this round. Auxiliary finite labeled strict-Hall model; no native physical interpretation or P000 change.

## 1. Exact dominance by difference-label unions

Let C be finite ports of positive integer capacities c_i, E_x nonempty neighborhoods of finite labeled targets. For any strictly independent selected set H (f_H(V)<=c(V)-1 on nonempty V), write
h_H(U)=min_{V superset U}(c(V)-f_H(V)), U subset C,
including h_H(empty)=0. For U nonempty, h_H=q_H+1 in GBX/GBY. It is monotone submodular: g_H(V)=c(V)-f_H(V) is submodular because each containment indicator is supermodular; union/intersection of minimizing supersets proves the claim (g_H(empty)=0, all other g_H>=1). GBX proves that h_T<=h_S pointwise on nonempty subsets of the allowed boundary is equivalent to every fresh labeled suffix feasible after T also feasible after S: necessity follows by taking h_S(U) identical fresh labels of neighborhood U whenever h_T(U)>h_S(U). Sufficiency follows directly from all strict-Hall inequalities. These are insertion-only future observers; identity-sensitive prefix operations are excluded.

Take two independent selected states S and T on the same capacities and labels (same label means same neighborhood). Let P=S intersect T, X=S minus T and Y=T minus S; E_K=union_{x in K} E_x. Then on the full boundary C:
   
  h_T(U)<=h_S(U) for all U subset C
  iff h_T(E_K)<=h_P(E_K)-|K| for all nonempty K subset X.   (1)

This can be reduced to one test per distinct nonempty union W=E_K:
   
  h_T(W)<=h_P(W)-f_X(W).                                   (2)

Indeed all labels of X with E_x subset W can be added to K without changing its union, so the largest relevant |K| is exactly f_X(W).

Proof: for any independent P+X, for nonempty U the GBX block-insertion identity has the equivalent expansion
  h_{P+X}(U)=min_{K subset X}[h_P(U union E_K)-|K|].
To see it directly, minimize over V containing U; f_X(V) is the largest cardinality of a subfamily K with E_K subset V. Interchange the two finite minima. Necessity of (1): take U=E_K, then h_S(E_K)<=h_P(E_K)-|K| by this expansion. Sufficiency: fix U and K. For K empty, h_T(U)<=h_P(U) holds since T contains P. Otherwise choose a subfamily L subset Y attaining the expansion at E_K for T. From (1),
  h_P(E_K union E_L)-h_P(E_K)-|L| <= -|K|.
Submodularity (diminishing returns under enlarging the base from E_K to U union E_K) gives
  h_P(U union E_K union E_L)-h_P(U union E_K)-|L| <= -|K|.
By the expansion of h_T at U, and monotonicity of h_P,
  h_T(U)<=h_P(U union E_L)-|L|
        <=h_P(U union E_K union E_L)-|L|
        <=h_P(U union E_K)-|K|.
Take the minimum over K. This proves (1), including X empty (then T contains S). A failed test at W gives h_T(W)>h_S(W) and an explicit separating suffix of h_S(W) fresh labels of neighborhood W. Reverse the roles for equality.

For a restricted future boundary B subset C, (2) remains sufficient. It is also necessary when union_{x in X}E_x subset B. Otherwise it may be conservative: two ports a,b of capacity 2; S={singleton a}, T={singleton b}; B={b}. h_T(b)=1<=h_S(b)=2 yet the full test fails at a. No claim of a complete restricted-boundary test outside this scope.

## 2. Fixed-parameter comparison near a common basis

For independent S,T contained in the same prefix basis J, let deficits d_S=|J|-|S| and d_T=|J|-|T|. Then |S minus T|<=d_T, |T minus S|<=d_S. Hence testing h_T<=h_S on full C uses at most 2(2^d_T-1) max-flow queries (two per distinct union), regardless of boundary width b. Equality uses at most 2(2^d_T+2^d_S-2) queries; for d_S,d_T<=d this is <=4(2^d-1). The same bounds apply to any pair with small actual symmetric label difference, without a common basis premise. Enumerate union masks iteratively from {empty} and scan X to compute f_X(W); with bitsets and binary capacities this is O(2^r poly(input)) for r=|X|. No claim of a uniform FPT algorithm solely in d for arbitrary states extending to different bases. For B restricted, use the scope of section 1.

This is a comparison algorithm, not a bound on number of observer-distinct states (GBX). Under the budget DP of GBY, a same-stage state S may replace T if h_S>=h_T on the remaining boundary, cost_S<=cost_T and reward_S>=reward_T, for the sole observer of maximum feasible final reward. Every suffix extension of T works after S with no greater cost and no smaller reward. If preserving all optimal label witnesses, keep provenance/backpointers separately; for a conservative implementation also retain the count condition for existing prefix rank pruning. Dynamic update preserves h-order by the GBX formula; boundary restriction preserves it as well. This provides an exact pairwise dominance certificate without building the dense signature; it is not yet integrated into the DP.

## 3. Direct max-flow implementation without a matching

For any H above, add source s, sink t, one vertex per H label and each port. Arc s->x capacity 1; x->i capacity M for i in E_x; i->t capacity c_i; force each i in query U to the source side by s->i capacity M. Choose M=1+sum c_i+|H|. Then
  h_H(U)=mincut(s,t)-|H|.
The all-ports/all-labels source side costs sum c_i, so a minimum cut crosses no M arc. For port source side V containing U, an optimal cut includes precisely (up to zero-cost ties) all labels whose neighborhoods lie in V, giving cost c(V)+|H|-f_H(V). Minimize over V. This is an alternative query realization of GBY; it does not require constructing a matching first. GBY's reference basis carrier retains its useful d-unit-arc perturbation mechanism. Edmonds-Karp integer maxflow is used below; general polynomial-time capacity-encoded flow algorithms also apply.

## 4. Singleton tests are insufficient

Let capacities (a,b,c,d)=(2,1,1,2), common P empty; S consists of distinct labels with E1={a,b}, E2={a,c}, T consists of singleton labels {a},{d}. Both independent and have size 2. The singleton tests pass: h_T({a,b})=2=h_P({a,b})-1, h_T({a,c})=2=h_P({a,c})-1. But W={a,b,c} has h_T(W)=3 and h_S(W)=2; h_P(W)-2=2. Two fresh labels supported on W are feasible after T and infeasible after S. This supplies a concrete joint-relation obstruction to replacing union tests by independent marginal tests, even when selected counts agree.

## 5. Executed replay

Deterministic xorshift32 seed 20261128. 500 synthetic models, 1..7 ports, capacities 1..4, 1..12 labels, nonempty arbitrary neighborhood masks. For each, compare two randomly ordered greedy independent subsets in both directions and two sub-bases (same greedy J, 0..3 deletions each) in both directions; add the two explicit cases above. Candidate union test uses actual integer max-flow, compared with direct enumeration of all port subsets. For each directed pair compare to exhaustive pointwise dominance on full boundary and three restricted boundaries; check every failed-test distinguishing fresh-label suffix against original strict Hall. All counts are actual executed checks; flow calls are not runtime comparison. This code uses small integer masks only in this synthetic test.

Result:
```json
{"seed":20261128,"models":500,"pairs":2002,"commonBasisPairs":1001,"fullCoordinatesCompared":67602,"distinctUnionTests":2327,"flowCalls":4654,"flowReferenceChecks":4654,"fullDominanceTrue":1217,"fullDominanceFalse":785,"failedWitnesses":785,"restrictedChecks":6006,"restrictedExactScope":4313,"restrictedConservativeMisses":815,"commonBasisSmallDeficitPairs":1001,"commonBasisTestCoordinates":994,"commonBasisFullCoordinates":33795,"disagreements":0}
```

Executed JavaScript:
```javascript
function replay(){
 let seed=20261128,z=seed;const rnd=n=>{z^=z<<13;z^=z>>>17;z^=z<<5;return(z>>>0)%n};
 const st={seed,models:0,pairs:0,commonBasisPairs:0,fullCoordinatesCompared:0,distinctUnionTests:0,flowCalls:0,flowReferenceChecks:0,fullDominanceTrue:0,fullDominanceFalse:0,failedWitnesses:0,restrictedChecks:0,restrictedExactScope:0,restrictedConservativeMisses:0,commonBasisSmallDeficitPairs:0,commonBasisTestCoordinates:0,commonBasisFullCoordinates:0,disagreements:0};
 const check=(x,m)=>{if(!x){st.disagreements++;throw Error(m)}};
 const sub=(x,y)=>(x&y)===x;
 const pop=x=>{let a=0;while(x){x&=x-1;a++}return a};
 function cs(c){return Array.from({length:1<<c.length},(_,v)=>c.reduce((a,b,i)=>a+((v>>i&1)*b),0))}
 const count=(A,v)=>A.reduce((n,x)=>n+Number(sub(x.e,v)),0);
 function ok(c,A){for(let v=1;v<c.length;v++)if(count(A,v)>=c[v])return false;return true}
 function direct(c,A,u){let h=Infinity;for(let v=1;v<c.length;v++)if(sub(u,v))h=Math.min(h,c[v]-count(A,v));return h}
 function flow(c,A,u){
  st.flowCalls++;
  const n=c.length,s=n+A.length,t=s+1,N=t+1,M=1+c.reduce((a,b)=>a+b,0)+A.length;
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
 function unions(X){let V=new Set([0]);for(let x of X)for(let v of [...V])V.add(v|x.e);V.delete(0);return [...V].sort((a,b)=>a-b)}
 function pair(c,S,T,isCommon,def){
  const cc=cs(c),N=cc.length,ids=new Set(T.map(x=>x.id)),P=S.filter(x=>ids.has(x.id)),X=S.filter(x=>!ids.has(x.id));
  let W=unions(X),pass=true,fail=0;
  check(ok(cc,S)&&ok(cc,T),"independent states");
  for(let w of W){
   let a=flow(c,P,w),b=flow(c,T,w);
   check(a===direct(cc,P,w)&&b===direct(cc,T,w),"flow reference");st.flowReferenceChecks+=2;st.distinctUnionTests++;
   if(b>a-count(X,w)){pass=false;if(!fail)fail=w}
  }
  let hS=Array(N),hT=Array(N),truth=true;
  for(let u=1;u<N;u++){hS[u]=direct(cc,S,u);hT[u]=direct(cc,T,u);if(hT[u]>hS[u])truth=false;st.fullCoordinatesCompared++}
  check(pass===truth,"full dominance");
  if(pass)st.fullDominanceTrue++;else{
   st.fullDominanceFalse++;
   check(hT[fail]>hS[fail],"failure witness");
   const n=hS[fail],probes=Array.from({length:n},(_,i)=>({e:fail,id:1000+i}));
   check(ok(cc,[...T,...probes])&&!ok(cc,[...S,...probes]),"fresh label witness");st.failedWitnesses++;
  }
  for(let j=0;j<3;j++){
   let B=j===0?N-1:1+rnd(N-1);
   let good=true;for(let u=B;u;u=(u-1)&B)if(hT[u]>hS[u])good=false;
   check(!pass||good,"restricted soundness");st.restrictedChecks++;
   let support=X.reduce((a,x)=>a|x.e,0);
   if(sub(support,B)){check(pass===good,"restricted exactness");st.restrictedExactScope++}
   else if(!pass&&good)st.restrictedConservativeMisses++;
  }
  st.pairs++;
  if(isCommon){st.commonBasisPairs++;check(X.length<=def,"common-basis bound");if(def<=3){st.commonBasisSmallDeficitPairs++;st.commonBasisTestCoordinates+=W.length;st.commonBasisFullCoordinates+=N-1}}
 }
 for(let it=0;it<500;it++){
  let n=1+rnd(7),c=Array.from({length:n},()=>1+rnd(4)),cc=cs(c),A=Array.from({length:1+rnd(12)},(_,id)=>({id,e:1+rnd((1<<n)-1)}));
  function greedy(a){let S=[];for(let x of a)if(ok(cc,[...S,x]))S.push(x);return S}
  function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){let j=rnd(i+1);[a[i],a[j]]=[a[j],a[i]]}return a}
  let S=greedy(shuffle(A).filter(()=>rnd(4)!==0)),T=greedy(shuffle(A).filter(()=>rnd(4)!==0));
  pair(c,S,T,false,0);pair(c,T,S,false,0);
  let J=greedy(A),d1=rnd(Math.min(3,J.length)+1),d2=rnd(Math.min(3,J.length)+1),a=shuffle(J).slice(d1),b=shuffle(J).slice(d2);
  pair(c,a,b,true,d2);pair(c,b,a,true,d1);
  st.models++;
 }
 // Singleton-only failure, equal selected counts; n=4, a=1,b=2,c=4,d=8.
 let c=[2,1,1,2],cc=cs(c),S=[{id:0,e:3},{id:1,e:5}],T=[{id:2,e:1},{id:3,e:8}];
 check(ok(cc,S)&&ok(cc,T),"singleton example independent");
 check(S.every(x=>direct(cc,T,x.e)<=direct(cc,[],x.e)-1),"singleton example tests");
 check(direct(cc,T,7)>direct(cc,S,7),"singleton example failure");pair(c,S,T,false,0);
 // Restricted-boundary full criterion may reject a true dominance.
 c=[2,2];cc=cs(c);S=[{id:0,e:1}];T=[{id:1,e:2}];
 check(direct(cc,T,2)<=direct(cc,S,2)&&direct(cc,T,1)>direct(cc,S,1),"restricted example");
 pair(c,S,T,true,1);
 return st
}
console.log(JSON.stringify(replay()));

```

## 6. Provenance and continuation

Global canonical main a89bbffa4f9f7544df78b3687019e0f88b0eed76; entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613 rechecked at immutable snapshot. Current control ac16605fb53ff73ea634295c843cefbc6ee94525; P000 V4/V5, ACTIVE worldview, joint/residual constraints, method and portable protocol consulted. Native original receipt r4-20261128-0230-ec49as-read SUCCEEDED with NO_CANONICAL_PUBLICATION_DIRECTORY at that Source; native owner projection not executed, no execution authorization. Historical provenance EM-DIRECT-23537B; current private research identity unconfirmed. Independent portable science, no shared claim or new identity. Activity association pending. No new physical root computations; inherited GBT historical frontier 1991 feasible, 68 excluded, 334 other; next root 2046, M14 in [25,27]. No frozen replay.

Next: implement union-test dominance as an optional DP state-pair filter with witness backpointers; measure pair count, union count, flow cost, actual pruning and total time against GBY on identical synthetic inputs and original pinned archive when accessible. Investigate exact restricted-boundary dominance without a support inclusion premise, and whether differing extending bases can be related at cost bounded in deficits rather than label differences. Keep failed comparisons as witnesses, not state equivalence.
