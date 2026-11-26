# R810 — Deterministic occupancy FPTAS by degree-paid deletion recursion

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R809, no shared CLAIM or Result. Exact predecessor: f8e92e90a85ede6f922ebcda716adbb0528e4192:research_notes/portable_direct/R809_PORT_OCCUPANCY_PAID_TRANSPORT_AND_PHYSICAL_REVERSAL.md. Reuse R809 physical incidence model and cycle cut theorem. Frozen P000 V5 and joint-observer files at a72226e2430ffa4786321ac86e7f0c599d5f0389, respective Git blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14 directly read; generated startup and Heartbeat companion at this pin returned 404. ACTIVE worldview, portable and current continuation/research method, account math, output, code, BRC and residual rules consulted; global entry snapshot 288dc9e62fd8c54ad6c0a3358bbd9d407abe0c80 with both entry blobs matching. Own session recovery r3-20261126-1124-own-metadata confirmed RESEARCHER, no RUN, execution_authorized=false. Owner query r3-20261126-1124-running-read pending at derivation. This is an auxiliary positive combinatorial observer, not native signed BRC execution. Preserve full matrices, branch provenance, time ordering and common depth.

## 1. Exact subinstance closure

For a simple finite road graph G=(V,E), use R809 incidence variables X_e in {00,01,10,11} and nonnegative rational edge weights S_e(x), with at least one positive state per edge. Let a_v in (0,1] and delta_v=1-a_v. Each vertex factor is g_v=1-delta_v I(all its incident bits are zero). The occupancy partition W(F) is 2^n times the sum of product edge weights and vertex factors with both bits of all e in F forced to 1. Assume these forced states have positive weight; otherwise W(F)=0 exactly. Allow arbitrary unary restrictions to positive states, deletion of factors, and deletion of variables with remaining factors tracking only their surviving incidences. The original degree d_v is retained as a bound; a factor with no remaining incidences is constant a_v. All feasible subinstances have positive partition because remaining vertex factors are strictly positive. Constant factors can be kept. The unconditioned edge weights may include zeros, including identity roads.

For a query edge e=uv and each admissible state x, remove e and both active endpoint factors to obtain a common base H. Reinsert the factors for endpoints whose bit in x is 0, one at a time; a factor whose bit is 1 is exactly the constant 1. Each reinsertion changes the partition by 1-delta_v p_v, where p_v is the probability under the then-current H that all remaining incidences of that vertex are zero. Compute p_v by the probability chain rule over those at most d_v-1 edge variables: each call queries the appropriate incidence-zero event under the previous unary restrictions. Impossible events give zero without querying an infeasible conditional. Thus the exact marginal of X_e is obtained by normalizing the nonnegative weights
 w_x=S_e(x) prod_{v: bit_v(x)=0, factor active} (1-delta_v p_{v,x}).
There are at most 4 states, 2 endpoints and d_v-1 children per endpoint per state. Every recursive child has one fewer variable. This is an exact deletion recursion on arbitrary graphs; it is not a tree approximation or an independence assumption. In particular it preserves all joint occupancy competition from R809.

## 2. Uniform contraction on degree-three graphs

Truncate the recursion at depth L; at L=0 use the normalized base edge weights alone. Every returned event probability belongs to [0,1], including under feasible unary restrictions. If child probabilities have absolute errors at most h, a chain product of k factors in [0,1] has absolute error at most k h by telescoping. Since 1-delta p >= a_v, the absolute log error of each reinsertion is <= (delta_v/a_v) k h by the mean value theorem. Hence the log error of each positive w_x is at most B=h sum_{v in {u,v}} (d_v-1)delta_v/a_v. The positive support is unchanged. For normalized weights with per-state log errors bounded by B, interpolate logarithmically; for an event H, derivative of its probability is P(H)(1-P(H)) times the difference of conditional mean log increments inside and outside H, so its absolute value is <=B/2. Integrate, including trivial events. Thus the event error is at most theta h, theta=(1/2) max_e sum_{v in e}(d_v-1)delta_v/a_v. For d_v<=3 and a_v>=7/8, theta<=2/7. Induction yields absolute event error <=(2/7)^L uniformly over all feasible pinnings and factor deletions. At most 16 children per node, so work is polynomial for L=O(log(m/epsilon)). In particular the truncation depends only on the local line-graph ball of radius L (factor and domain data within it); two boundary restrictions agreeing there change the exact local event probability by at most 2(2/7)^L. This is strong spatial mixing for the symmetric occupancy measure, not yet for the full occupation/sign measure.

## 3. Degree-paid recursion: arbitrary degree at actual Port activities

The original uncontracted R799/R809 construction has a_v=1-2^(-2d_v-1) for nonisolated vertices. Allow any a_v >= this value; isolated factors may be any positive constant. Keep original d_v even after subinstance restrictions or deletions. Charge each recursive call belonging to endpoint v a budget c_v=d_v-1 (only if it has at least one child, so c_v>=1). With integer remaining budget L, call children at L-c_v when c_v<=L; otherwise use p_v=0 for that factor. At L=0 use normalized base weights. If no child remains, use the exact p=1. Inductively all child event errors are <=2^(-(L-c_v)); when c_v>L the skipped product error <=1<=2^(c_v-L). Therefore log weight error <= 2^(-L) sum_v (d_v-1) 2^(d_v-1) delta_v/a_v. For d>=2,
 (d-1)2^(d-1)/(2^(2d+1)-1) <= (d-1)/2^(d+1) <= 1/8.
For degree 1 the term vanishes. The normalized event error is at most (1/8)2^(-L), and in particular <=2^(-L). This induction is uniform in original graph size, degree, domains and factor deletions. Degree payment avoids an exponential branching penalty at large degree: at most 4c children at cost c from each endpoint; 4c/16^c<=1/4 for c>=1. By induction the number of nodes is <=2*16^L (the two endpoint sums are <=1/2, plus one root). Per-node nonrecursive work is polynomial in input size. L=O(log(m/epsilon)) gives a polynomial bound even for unbounded degrees. Arbitrary rational positive weights are allowed: zeros are tracked by unary support. No use of transcendental arithmetic is necessary for evaluation; logarithms are solely a proof of error propagation. Exact rational formula sizes are polynomial: each node uses bounded arithmetic per child, and the bit lengths of sums, products and divisions are bounded by a constant times the sum of operand bit lengths; a constant-factor replication per depth O(L) is polynomial. The original graph is the input, not a precomputed list of occupation patterns.

## 4. Deterministic FPTAS for every forced occupancy partition W(F)

For each edge in any feasible subinstance choose a positive state of maximal base weight among its admissible states. Its exact marginal probability is >= (7/8)^2/4=49/256 in both cases above: comparing the conditional weights after fixing all other edges, at most two factors vary, each lies in [7/8,1], and the chosen base weight is at least one fourth of their sum. The same bound survives averaging and arbitrary pinnings. Choose these reference states sequentially and pin them. If p_i are their conditional probabilities and w(x*) the exact known weight of the resulting full assignment (including 2^n), then W(F)=w(x*)/prod p_i. With 0<epsilon<=1, approximate each p_i to absolute error <=(49/256)epsilon/(8 max(1,m)). The relative probability errors are <=epsilon/(8m) for m>0. Since |log(1+t)|<=2|t| for |t|<=1/2, the total log error is <=epsilon/4. Exponentiating gives relative error <=epsilon (including lower side). Empty edge set is exact. In degree-three use L chosen by (2/7)^L bound; in actual degree-paid case use L chosen by 2^(-L) bound. All arithmetic/bit lengths and recursion sizes are polynomial in rational input length, m and 1/epsilon, hence this is a deterministic FPTAS for W(F). No claim of practical performance benchmark.

## 5. Transfer back to the full residual observer under a certified cut

The R809 full coefficients are Q_T(J)=sum_{F subset J, boundary F=T} eta(F)W(F), where all original edge weights in W are kept, including the symmetric part of deleted anti-channels. For any feasible T the affine cycle space of J has 2^r candidate supports, r=|J|-|V|+components(J). Use the above FPTAS on each W(F) with the same relative error; positive weighted summation preserves that relative error, while structural zero is exact. This is O(2^r poly(input,1/epsilon)) for Q_T(J), even when the original E has large cycle rank. Unlike the earlier full-graph cycle rank algorithm, it is parameterized by the retained anti-channel graph, without deleting the original symmetric occupation competition. For the scalar observer let C=E minus J. R809 proves 0<=Q_empty(E)-Q_empty(J)<=c_C^+ Q_empty(E), where c_C^+ sums products of kappa^+ over simple cycles meeting C. Use any certified upper bound b>=c_C^+ (R806 finite nonbacktracking bound with R809 weights, for example). If b<=epsilon/2, approximate Q_empty(J) to relative epsilon/2; the result approximates Q_empty(E) to relative epsilon, since (1-epsilon/2)(1-b)>=1-epsilon and the upper side is immediate. If r=O(log(input,1/epsilon)), the resulting algorithm is polynomial. In particular deleting all anti-channels is certified whenever the cycle bound is small enough; for max degree 3 and minimum cycle length g, c_E^+ <= n*3*rho*((2*rho)^(g-1))/(2*g*(1-2*rho)), rho=32/81, by counting oriented nonbacktracking walks and dividing by 2l at length l. This is an instance- and tolerance-dependent condition, not an unrestricted full Q FPTAS on every subcubic graph. For nonzero boundary charges the R809 path/cycle cut inequalities give additive budgets; relative full-charge approximation requires a positive lower certificate. General full occupancy/sign strong mixing and general tilted-cluster FPRAS remain open.

## 6. Actual exact computation

The following JavaScript BigInt rational verifier was actually executed. Graphs: all labeled simple graphs on 2 and 3 vertices, 11 explicitly selected masks on 4 vertices, and a six-vertex degree-five star. For the first 21 graphs use uniform degree-three activity and original degree-paid activity; for the star use degree-paid only. Edge base weights alternate among a scaled identity, a scaled R803 length-one transfer, and an arbitrary nonnegative test vector to check the broader W theorem. Domain and factor tests include forcing one road to 11 and deleting one factor. Every nontrivial state subset event is compared to exact enumeration; truncation depth/budget 0..3, reference probability bound, and exact partition self-reduction tested. Counts: {"graphs":22,"configurations":43,"conditionedInstances":117,"exactMarginalChecks":4242,"truncationChecks":16968,"referenceProbabilityChecks":303,"partitionChecks":117,"uniformDepthChecks":8064,"weightedDepthChecks":8904,"recursiveCalls":5147}. General conclusions follow from the proof, not extrapolation from these finite checks. No formal Lean check, independent review, runtime benchmark or native BRC execution. Code:

```javascript
function verify(){
 const stats={graphs:0,configurations:0,conditionedInstances:0,exactMarginalChecks:0,truncationChecks:0,referenceProbabilityChecks:0,partitionChecks:0,uniformDepthChecks:0,weightedDepthChecks:0,recursiveCalls:0};
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
 const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");let g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sub=(a,b)=>add(a,[-b[0],b[1]]),cmp=(a,b)=>a[0]*b[1]-b[0]*a[1],abs=a=>[a[0]<0n?-a[0]:a[0],a[1]],pow=(a,n)=>f(a[0]**BigInt(n),a[1]**BigInt(n));
 const one=f(1),zero=f(0),sum=a=>a.reduce(add,zero);
 const ck=(b,msg)=>{if(!b)throw Error(msg+" "+JSON.stringify(stats))};
 function instance(n,E,mode,seed){
  const m=E.length,deg=Array(n).fill(0),inc=Array.from({length:n},()=>[]);
  E.forEach(([u,v],i)=>{deg[u]++;deg[v]++;inc[u].push([i,2]);inc[v].push([i,1])});
  const a=deg.map((d,v)=>mode===0?f((1n<<BigInt(2*d+1))-1n,1n<<BigInt(2*d+1)):f(7+(v+seed)%2,8));
  const cost=deg.map(d=>mode===0?Math.max(1,d-1):1);
  const weights=E.map((_,i)=>[[2,0,0,1],[14,8,8,4],[3,1,5,4]][(i+seed)%3].map(x=>f(x)));
  const full=weights.map(w=>w.reduce((M,x,i)=>M|(x[0]>0n?1<<i:0),0)),all=(1<<n)-1;
  const states=mask=>[0,1,2,3].filter(s=>mask>>s&1);
  const memo=new Map();
  function dist(dom,active,x,L){
   let key=[dom.join(","),active,x,L].join(":");if(memo.has(key))return memo.get(key);
   stats.recursiveCalls++;
   const [u,v]=E[x],base=dom.slice();base[x]=0;
   const active0=active&~((1<<u)|(1<<v));
   const out=Array.from({length:4},()=>zero);
   for(const s of states(dom[x])){
    let w=weights[x][s],live=active0;
    if(L>0)for(const [z,bit] of [[u,2],[v,1]])if((active>>z&1)&&!(s&bit)){
     const children=inc[z].filter(([i])=>base[i]);
     let p=one;
     if(children.length&&cost[z]>L)p=zero;
     else{
      const d=base.slice();
      for(const [i,b] of children){
       const allowed=d[i]& (b===2?3:5);
       if(!allowed){p=zero;break}
       if(allowed!==d[i]){
        const q=dist(d,live,i,L-cost[z]);p=mul(p,sum(states(allowed).map(t=>q[t])));d[i]=allowed;
       }
      }
     }
     w=mul(w,sub(one,mul(sub(one,a[z]),p)));live|=1<<z;
    }
    out[s]=w;
   }
   let den=sum(out);const ans=out.map(w=>div(w,den));memo.set(key,ans);return ans;
  }
  function brute(dom,active,x=-1){
   let ans=Array.from({length:4},()=>zero),Z=zero;
   function rec(i,occ,w,sx){
    if(i===m){for(let v=0;v<n;v++)if((active>>v&1)&&!(occ>>v&1))w=mul(w,a[v]);Z=add(Z,w);if(x>=0)ans[sx]=add(ans[sx],w);return}
    if(!dom[i]){rec(i+1,occ,w,sx);return}
    const [u,v]=E[i];for(const s of states(dom[i]))rec(i+1,occ|(s&2?1<<u:0)|(s&1?1<<v:0),mul(w,weights[i][s]),i===x?s:sx);
   }rec(0,0,one,0);return {Z,p:x<0?null:ans.map(w=>div(w,Z))};
  }
  const configs=[{dom:full.slice(),active:all}];
  if(m){const d=full.slice();d[seed%m]=8;configs.push({dom:d,active:all});configs.push({dom:full.slice(),active:all&~(1<<(seed%n))});}
  for(const {dom,active} of configs){
   stats.conditionedInstances++;
   for(let x=0;x<m;x++){
    const p=brute(dom,active,x).p;
    const exact=dist(dom,active,x,1+m*Math.max(...cost));
    const ref=states(dom[x]).reduce((b,s)=>cmp(weights[x][s],weights[x][b])>0n?s:b,states(dom[x])[0]);
    ck(cmp(p[ref],f(49,256))>=0n,"reference mass");stats.referenceProbabilityChecks++;
    for(let mask=1;mask<15;mask++){
     const event=states(mask),truth=sum(event.map(s=>p[s]));
     ck(cmp(truth,sum(event.map(s=>exact[s])))===0n,"exact recursion");stats.exactMarginalChecks++;
     for(let L=0;L<=3;L++){
      const q=dist(dom,active,x,L),err=abs(sub(truth,sum(event.map(s=>q[s])))),bound=mode===0?pow(f(1,2),L):pow(f(2,7),L);
      ck(cmp(err,bound)<=0n,"truncation");stats.truncationChecks++;if(mode===0)stats.weightedDepthChecks++;else stats.uniformDepthChecks++;
     }
    }
   }
   let d=dom.slice(),p=one,occ=0,weight=one;
   for(let i=0;i<m;i++){
    const s=states(d[i])[0],q=dist(d,active,i,1+m*Math.max(...cost));p=mul(p,q[s]);d[i]=1<<s;weight=mul(weight,weights[i][s]);const [u,v]=E[i];occ|=(s&2?1<<u:0)|(s&1?1<<v:0);
   }
   for(let v=0;v<n;v++)if((active>>v&1)&&!(occ>>v&1))weight=mul(weight,a[v]);
   ck(cmp(div(weight,p),brute(dom,active).Z)===0n,"partition");stats.partitionChecks++;
  }
  stats.configurations++;
 }
 for(let n=2;n<=4;n++){
  const E=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)E.push([u,v]);
  for(let mask=0;mask<1<<E.length;mask++){
   if(n===4&&![0,1,3,7,11,13,15,23,31,45,63].includes(mask))continue;
   const e=E.filter((_,i)=>mask>>i&1);
   for(let mode=0;mode<2;mode++)instance(n,e,mode,mask);stats.graphs++;
  }
 }
 instance(6,[[0,1],[0,2],[0,3],[0,4],[0,5]],0,1);stats.graphs++;
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 7. Next

The full sign/occupancy model still needs a robust recursion or sampling method whose conditional error includes parity-cycle residuals, not just symmetric occupancy. Examine whether cycle-induced perturbations can be controlled by a second contraction or a polynomially computable local conditional partition ratio; keep the R809 normalization-reversal witness as an obstruction to naive monotone coupling. For actual Port graph families with a sparse retained anti-channel graph, implement the two-stage certified approximation and benchmark the degree-paid recursion. Do not conflate symmetric occupancy FPTAS with general full Q FPTAS.
