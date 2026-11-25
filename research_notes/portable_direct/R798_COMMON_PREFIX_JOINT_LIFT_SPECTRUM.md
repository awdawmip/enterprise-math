# R798 — Common-prefix joint lift spectrum by overlap-factor contraction

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R797, own researcher metadata EM-DIRECT-82A007, Activity RA-708BCC309CE076D8BB599B91; own session recovery succeeded, no RUN, execution_authorized=false. Owner query r3-20261125-2315-owner-read last observed RUNNING (read job, not active-owner evidence). No shared Task/CLAIM/Result/Review changes. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer contract blob 3923890d77a02d84b772f789e6912dd14f220d14 read in enterprise-math. ACTIVE worldview and current account/project policy consulted, common immutable global-main snapshot not yet established. Scope: unsigned integer Port branch-count auxiliary observer, not native signed/amplitude BRC dynamics.

Exact predecessors:
- 1a2471a8b10ac6f0a8d7eadeb05f27def385aff3:research_notes/portable_direct/R795_INTRINSIC_FIXED_RANK_PORT_SELECTOR.md
- 3e7108d2ba1a0d36a83957d6c01f9e493029eedb:research_notes/portable_direct/R796_EXACT_LIFT_FIBER_AND_MINIMAL_SELECTOR.md
- 9f4937d3c38a41fd30103cfc49473a1970f2d591:research_notes/portable_direct/R797_ALL_PREFIX_LIFT_COUNT_SPECTRUM.md

## 1. Joint spectrum theorem

Use R795's source graph G=(V,E), m edges, independent prefix x_e in {F,U,V}, with local public endpoint counts (1,1),(1,0),(0,1), respectively; private count 2 at F and 1 otherwise. Fixed boundaries S_1,...,S_k use the common A-twist. Let L_i(x) be the full lift count for S_i at the SAME x. Take independent weights w_e(F),w_e(U),w_e(V) (nonnegative rational or integer; uniform weights 1). Define

H_J(z)=sum over x with L_i(x)>0 for every i in J of (product_e w_e(x_e)) product_{i in J} z_i^(log2 L_i(x)).

Empty J gives the total prefix weight. If a boundary in J fails the R797 all-flexible component test, H_J=0. Otherwise, for each i, take its all-flexible graph of R797. Its public components are uniquely oriented rooted trees (one stub) and unicyclic components (two orientations); attached tree directions are common to the two alternatives. Private slots are fixed. For each unicyclic component C of observation i introduce a three-state variable q_C in {+,-,*}. Plus and minus demand the indicated orientation, star demands BOTH; attach factor 1,1,z_i-2 respectively. For each edge e, let D_e(q) be the union of required public endpoints over all observations: trees/stubs and attached trees give fixed demands, cycle choices give the indicated endpoint or both. Let P_e be the set of observations selecting a_e privately. Define

K_e(D_e)=sum_{x_e admits every endpoint in D_e} w_e(x_e) product_{i in P_e} z_i^[x_e=F].

Then the exact contraction is

H_J(z)=sum_q (product_{C:q_C=*}(z_{i(C)}-2)) product_e K_e(D_e(q)).

Proof: for a single cycle, at any prefix its two orientation events have indicators I_+,I_-. The positive-count generating value is I_+ + I_- + (z_i-2)I_+ I_-. If neither holds it is 0; if exactly one holds it is 1; if both hold it is z_i. Multiply over cycles and deterministic public incidences, and by the private F exponent factors. By R796 this product is exactly zero for an infeasible boundary and otherwise z_i^log2 L_i. Multiplication across observations retains the SAME prefix. Expand the cycle products and sum over x; each summand splits by independent slot weights, giving K_e. The subtraction is inclusion-exclusion within an unsigned count polynomial, not native amplitude cancellation. Every coefficient of the final H_J is nonnegative for nonnegative weights. The formula handles repeated boundaries, empty private sets, empty cycles and zero weights. For fixed x, the pre-sum product also retains pointwise joint exponent/readout; summation is a quotient only for the specified weighted spectrum observer.

To recover the FULL joint distribution including zeros, for each subset J of observations and every specified positive exponent vector on J, use coefficients of

H_exact,J(z_J)=sum_{B subseteq [k]\J} (-1)^|B| H_{J union B}(z_J,z_B=1).

This inclusion-exclusion requires exactly J positive and every other coordinate zero, with no independence assumption between observations. Equivalently replace H_J's positive term by the moment evaluations: for all positive integer powers h_i, sum_x weight(x) product_i L_i(x)^h_i = H_J(2^h_i). An empty boundary list has weight product_e sum_x w_e(x). Arbitrary dependent prefix weights are not claimed to factor.

## 2. Overlap graph and exact algorithm

Construct a factor graph on cycle variables. An edge-slot factor depends only on cycle variables whose actual cycle edges include that slot (attached tree demands are fixed). At most one variable per observation occurs in a slot. For two observations the variable interaction graph is bipartite after merging parallel factors (one part for each observation); constant/unary factors can be absorbed. This graph, not the raw source graph alone, identifies the coupling. For fixed numerical z_i, the three-state contraction on a forest is evaluated by ordinary leaf elimination: sum the three values of the leaf variable against its unary and pair factor, leaving a unary message on its neighbor. Each edge has at most 9 table entries. O(k(n+m)) construction operations to find all-flexible components/peel cycles and build tables for k=2, then O(m+n) arithmetic for forest contraction. For general k, given a tree decomposition of the cycle-variable primal graph with width w and B bags, place each factor on a bag containing its scope (a clique), perform separator-conditioned summation, and use at most O((B+m) 3^(w+1) poly(k)) arithmetic operations for bounded bag bookkeeping and precomputed factor tables; alternatively fix a feedback vertex set of h variables and use 3^h forest contractions for pair observations. Decomposition construction cost is separate. Expanded multivariate coefficient computation uses polynomial arithmetic instead of numerical scalars; degree in coordinate i is <=m, naive storage <=(m+1)^k coefficients, each with actual integer/rational bit cost. For numerical values, exact integer/rational arithmetic cost includes input weights and resulting bit lengths. For k=2 and fixed z, no decomposition search is needed if the graph is a forest. General unbounded-overlap tractability is open; no benchmark speedup claimed.

As a simple genuine counterexample to marginal product, one slot with S1={u}, S2={v} gives joint support polynomial H_{12}=1 (uniform counting), marginals H_1=H_2=2, total prefixes=3. The normalized covariance of feasibility indicators is -1/9. For S1=S2={u}, joint support is 2; the marginal polynomials are the same but covariance is +2/9. Thus scalar marginal histograms cannot identify even the sign of correlation. Source, observation labels, cycle overlap and common prefix identity remain retained. No signed, time-order, native X6 common-depth or provenance erasure follows.

## 3. Exact verification and scope

Dependency-free JS below derives the local table independently from all 384 literal local XOR configurations, computes direct full integer lift counts by prefix/assignment DP on the proved R795 capacity-tree semantics, then compares exact bivariate coefficients from the contraction to direct prefix histograms for both uniform and independently varying weights. The finite verifier enumerates component orientations directly rather than implementing leaf elimination; general-size contraction and forest algorithm follow from the proof. Coverage: all 71 nonempty labeled simple graphs on 2--4 vertices, all all-flexible feasible unordered pairs with repetition, plus four boundaries on two disjoint triangles (includes two-cycle cases); weights are 1+(edge index+2*prefix code index) mod 3. Arithmetic is exact JS integer arithmetic in these small ranges (degree <=6, weights <=3, all intermediate counts bounded well below 2^53). Zero-prefix mass for a pair follows from the total and marginal/joint positive masses; exact general zero strata follow from inclusion-exclusion above. Does not enumerate expanded capacity-tree bits separately, use native signed BRC, or independently review the proof.

Actual output:
```json
{
  "table": [
    [
      1,
      1,
      2
    ],
    [
      0,
      1,
      1
    ],
    [
      1,
      0,
      1
    ]
  ],
  "graphs": 72,
  "prefixes": 4890,
  "boundaries": 1876,
  "pairs": 50059,
  "jointQueries": 13844457,
  "weightedPairs": 50059,
  "zeroJoint": 0,
  "twoCyclePairs": 4,
  "mismatches": 0
}
```

```javascript
function verify(){
 const pc=x=>{let c=0;while(x){x&=x-1;c++}return c};
 const table=[];
 for(const x of [3,5,6]){const row=[0,0,0];for(let b=0;b<128;b++){let [s,t,j,k,u,v,a]=Array.from({length:7},(_,i)=>b>>i&1);let z=[s+2*t,s+2*u+4*j,t+2*v+4*k,j+2*k+4*a];if(z.every(y=>[0,3,5,6].includes(y))&&z[0]!=(x^5)&&z[1]!=3&&z[2]!=6&&z[3]!=6){let a1=u+2*v+4*(a^1);if(![1,2,4].includes(a1))throw Error("local support");row[[1,2,4].indexOf(a1)]++}}table.push(row)}
 if(JSON.stringify(table)!=="[[1,1,2],[0,1,1],[1,0,1]]")throw Error("local");
 const add=(a,k,v)=>{let w=(a.get(k)||0)+v;if(w)a.set(k,w);else a.delete(k)};
 const mul=(a,b)=>{const c=new Map;for(const [i,v] of a)for(const [j,w] of b)add(c,i+j,v*w);return c};
 const one=()=>new Map([[0,1]]);
 const same=(a,b)=>a.size===b.size&&[...a].every(([k,v])=>b.get(k)===v);
 const log=x=>{let k=0;while(x>1&&x%2===0){x/=2;k++}if(x!==1)throw Error("power");return k};
 const weights=(i,x)=>1+(i+2*x)%3;
 let graphs=0,prefixes=0,boundaries=0,pairs=0,jointQueries=0,weightedPairs=0,zeroJoint=0,twoCyclePairs=0;
 function terms(n,E,S,stride){
  const m=E.length, P=E.map((_,i)=>!!(S>>(n+i)&1)), U=Array.from({length:n},(_,i)=>i).filter(v=>S>>v&1);
  const adj=Array.from({length:n},()=>[]), allowed=E.map(([u,v],i)=>P[i]?0:((S>>u&1)?1:0)|((S>>v&1)?2:0));
  if(allowed.some((a,i)=>!P[i]&&!a))return [];
  E.forEach(([u,v],i)=>{if(allowed[i]===3){adj[u].push(v);adj[v].push(u)}});
  const seen=new Set, comps=[];
  for(const root of U){if(seen.has(root))continue;let Q=[root];seen.add(root);for(let k=0;k<Q.length;k++)for(const v of adj[Q[k]])if(!seen.has(v)){seen.add(v);Q.push(v)}const vs=new Set(Q), ix=E.map((_,i)=>i).filter(i=>{let [u,v]=E[i];return !P[i]&&((allowed[i]&1)&&vs.has(u)||(allowed[i]&2)&&vs.has(v))});if(ix.length!==Q.length)return [];
   const os=[];function dfs(j,used,arr){if(j===ix.length){os.push(arr.slice());return}let i=ix[j];for(let d=1;d<=2;d++)if(allowed[i]&d){let v=E[i][d-1],bit=1<<v;if(!(used&bit)){arr.push(d);dfs(j+1,used|bit,arr);arr.pop()}}}dfs(0,0,[]);
   if(os.length<1||os.length>2)throw Error("component");comps.push({ix,os});
  }
  let ts=[{d:Array(m).fill(0),poly:one()}];
  for(const {ix,os} of comps){let next=[];for(const t of ts){let opts=os.map(o=>({o,poly:one()}));if(os.length===2)opts.push({o:os[0].map((a,i)=>a|os[1][i]),poly:new Map([[0,-2],[stride,1]])});for(const q of opts){let d=t.d.slice();ix.forEach((i,j)=>d[i]=q.o[j]);next.push({d,poly:mul(t.poly,q.poly)})}}ts=next}
  return ts;
 }
 function predicted(E,a,b,weighted){let out=new Map;
  for(const A of a)for(const B of b){let p=mul(A.poly,B.poly);
   for(let i=0;i<E.length&&p.size;i++){let d=A.d[i]|B.d[i], exp=(A.d[i]===0?16:0)+(B.d[i]===0?1:0),q=new Map;
    for(let x=0;x<3;x++){let mask=x===0?3:x===1?2:1;if((mask&d)!==d)continue;add(q,x===0?exp:0,weighted?weights(i,x):1)}p=mul(p,q)}
   for(const [k,v] of p)add(out,k,v)}
  return out;
 }
 function run(n,E,subset=null){
  const m=E.length,N=3**m, maps=[], wts=[];graphs++;prefixes+=N;
  const all=new Set;
  for(let p=0;p<N;p++){let z=p,w=1,M=new Map([[0,1]]);for(let i=0;i<m;i++){let x=z%3;z=Math.floor(z/3);w*=weights(i,x);let next=new Map;let labels=[E[i][0],E[i][1],n+i];for(const [s,c] of M)for(let j=0;j<3;j++){let bit=1<<labels[j],v=table[x][j];if(v&&!(s&bit))add(next,s|bit,c*v)}M=next}maps.push(M);wts.push(w);for(const s of M.keys())all.add(s)}
  const ss=subset??[...all].sort((a,b)=>a-b);boundaries+=ss.length;
  const ts=ss.map(S=>terms(n,E,S,16)), us=ss.map(S=>terms(n,E,S,1));
  for(let j=0;j<ss.length;j++)for(let k=j;k<ss.length;k++){
   let a=new Map,b=new Map;for(let p=0;p<N;p++){let l=maps[p].get(ss[j])||0,r=maps[p].get(ss[k])||0;if(l&&r){let code=16*log(l)+log(r);add(a,code,1);add(b,code,wts[p])}}
   let A=predicted(E,ts[j],us[k],false),B=predicted(E,ts[j],us[k],true);
   if(!same(a,A)||!same(b,B))throw Error(JSON.stringify({n,E,j,k,a:[...a],A:[...A],b:[...b],B:[...B]}));
   pairs++;weightedPairs++;jointQueries+=N;if(!a.size)zeroJoint++;if(ts[j].length>=9||us[k].length>=9)twoCyclePairs++;
  }
 }
 for(let n=2;n<=4;n++){let p=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)p.push([u,v]);for(let g=1;g<1<<p.length;g++)run(n,p.filter((_,i)=>g>>i&1))}
 const E=[[0,1],[1,2],[0,2],[3,4],[4,5],[3,5]];run(6,E,[63,4032,7+(7<<9),56+(7<<6)]);
 return {table,graphs,prefixes,boundaries,pairs,jointQueries,weightedPairs,zeroJoint,twoCyclePairs,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```

## 4. Next

Determine structural restrictions on cycle overlap graphs realized by two R795 boundaries, especially whether cyclic overlap instances admit additional exact compression or encode difficult partition functions. Test the forest contraction implementation against explicit overlap cycles, then extend to shared-prefix universal compatibility / more general weights. Keep the original source and branch reconstruction coordinates; no shared Task completion or mathematical acceptance is asserted.
