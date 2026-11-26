# R811 — Full scalar cactus anti-channel FPTAS by cycle-paid factor recursion

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Portable independent continuation, no shared CLAIM or Result. Fixed predecessor 4432797b505566a8172ccd2f8dbe2f2b3919e9d1:research_notes/portable_direct/R810_DEGREE_PAID_OCCUPANCY_FPTAS.md and f8e92e90a85ede6f922ebcda716adbb0528e4192:R809_PORT_OCCUPANCY_PAID_TRANSPORT_AND_PHYSICAL_REVERSAL.md (same portable_direct directory). Frozen P000 V5 and joint-observer contract directly read at a72226e2430ffa4786321ac86e7f0c599d5f0389, blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14; generated startup 404. ACTIVE worldview and current portable/method/account rules read, global canonical entry snapshot 251f97ea6b3bbd1fd51ceae8b1b238d9390860c5. Own verified metadata r3-20261126-1223-own-metadata: RESEARCHER EM-DIRECT-82A007, no RUN, execution_authorized=false. Owner query r3-20261126-1223-owner-read still RUNNING at derivation; no empty inventory inferred. Auxiliary positive combinatorial observer only: full matrices, native signed BRC, branch provenance, time ordering and common depth retained.

## 1. Exact cycle factorization with original occupancy competition intact

Let G=(V,E) be a finite simple road kernel with R809 physical symmetric occupancy weights S_e=(A,B,C,D/2), eta_e=1/D, road lengths ell>=0, internal a in [7/8,1], vertex a_v>=1-2^(-2d_v-1) for d_v>=1. Isolated factors any positive constant. Retain J subset E as anti-channels only. Suppose each edge of J belongs to at most one simple cycle (cactus, with arbitrary bridges and components). Let C be its simple cycles; distinct cycles are edge disjoint, possibly meet at vertices. Every even subgraph of J is uniquely a union of a subset of these cycles, since an even graph decomposes into edge-disjoint simple cycles and each edge has a unique cycle. With lambda_C=prod_{e in C} eta_e <=1, the exact R809 parity sum becomes
 Q_empty(J)=2^n sum_x prod_e S_e(x_e) prod_v (1-delta_v I(all incident bits zero)) prod_C (1+lambda_C I(all C edges 11)).
Proof: interchange the finite nonnegative sums over occupancy and even supports and distribute the independent cycle choices. The whole original G supplies the vertex factors and all road weights, including edges outside J. There is no independence assumption on occupancy and no deletion of its joint competition. Cactus J may have linear cycle rank; E itself need not be cactus or low-treewidth. Only the scalar observer is claimed; nonzero charges and native signed observations retain their exact inputs.

## 2. Conditional occupancy cap after removing one cycle factor

For ell=0, S=(1,0,0,1/2). For ell>=1 write N product as [[A,2B],[C,D]], N(a)=[[2a,2],[1,1]]. The first factor gives row0>=7/4 row1; the last gives column0>=7/8 column1, so A>=D and B,C>=7D/8. The identity road also has A=D. Condition on all other variables in any feasible subinstance with arbitrary unary restrictions, vertex-factor deletions/shrinking, and cycle-factor deletions/shrinking. If the unique cycle factor of e is absent, and the allowed support includes 11 and at least one other positive state, the relative conditional unnormalized weight of 11 is D/2; each other allowed positive state has weight at least 49D/64 relative to the common factor. Indeed endpoint empty/occupied ratios lie in [7/8,1] (or equal 1 if removed), and the above matrix inequalities apply. Hence P(X_e=11)<=rho=32/81. Averaging over other variables preserves the cap. The cap is not asserted if 11 is the only allowed state or if e's cycle factor remains. Infeasible domain event is zero; deterministic events are exact. When computing a cycle's all-11 probability after removing that factor, all nontrivial chain children meet the cap, because cycle factors have disjoint edge supports. This uniform pinning cap is stronger than an unconditioned two-point estimate.

## 3. Exact deletion recursion and cost-paid contraction

Use R810's common-base deletion on any query edge: remove it and all factors involving it (at most two vertex factors, one cycle factor). For each allowed state x, restore the factors for which its condition is satisfied, shrinking the support by that edge. Restore vertex factors first, cycle factor last. Each restoration multiplies the base partition by 1+c p, where c=-delta_v or c=lambda_C, and p is the probability of the conjunction of the remaining conditions in the then-current subinstance. Calculate p by the conditional probability chain rule, with no independence assumption. Unary restrictions to positive support, removal and shrinking preserve the subinstance class, and constant factors cancel in marginals. No infeasible child is queried. Each recursive call reduces the variable count. Cycle restoration occurs only for state 11. All its nontrivial chain children are queried with that cycle factor absent.

Take integer budget L, base L=0 normalized base weights, output event errors <=1. For each vertex factor with nontrivial children charge c_v=d_v-1>=1 (original degree). For each cycle factor with k nontrivial children charge k>=1. If cost>L skip conjunction with p=0, otherwise recurse at L-cost. Deterministic conjunctions evaluated exactly (unless at base L=0, where the trivial error bound suffices). Clamp each approximate cycle child probability to [0,rho] before multiplication; the cap in section 2 makes this nonexpansive. Keep other probabilities in [0,1].

Inductive target absolute error h_L=(3/4)^L for any event in the query edge state space, uniformly over all feasible subinstances. For a vertex factor, chain telescoping and log Lipschitz delta_v/a_v bound the log-weight error in each state by h_L (d_v-1)(4/3)^(d_v-1) delta_v/a_v, including skipped terms since 1<= (4/3)^(c_v-L) when c_v>L. This is <=h_L/8 by R810's stronger 2^c bound; degree-one has no nontrivial child. Each vertex factor therefore has log-error oscillation across states <=h_L/4.

For a cycle factor with k>=1, telescoping the products of capped children gives error <= k rho^(k-1) h_(L-k). Since log(1+lambda p) has derivative <=1, the same bounds log-weight error. For k<=L the multiplier relative to h_L is (4/3) k (128/243)^(k-1) <= 3/2: the maximum over k>=1 occurs at k=2 because subsequent ratios (k+1)/k *128/243<1, and the k=2 value is 1024/729<3/2. For k>L, true p<=rho^k<=h_L, so skipped log error <=h_L. The cycle log-error oscillation is at most 3h_L/2, not twice this: it affects only state 11. This observation is essential for clean payment. The common-base partition cancels, and all positive supports remain unchanged.

For an event under normalized positive weights interpolate linearly between exact and approximate log weights. Derivative of event probability is P(H)(1-P(H)) times the difference of conditional mean log increments; its magnitude is bounded by one quarter of their oscillation. Thus the total absolute error is <=(1/4)(2/4+3/2)h_L=h_L/2<=h_L. Base and induction give the claimed uniform bound. Degree paid and cycle paid costs allow long cycles and arbitrary original degrees.

Each vertex produces <=4c children at cost c, each cycle <=k children at cost k (only state 11). For integer c,k>=1, 4c/16^c<=1/4, k/16^k<=1/16. The sum over two endpoints and one cycle is <=9/16. The recursion tree has <=3*16^L nodes by induction (1+3*(9/16)*16^L<=3*16^L). Nonrecursive work polynomial in explicit input. The rational formula has polynomial bit cost for L=O(log(m/epsilon)): elementary operation bit lengths bounded by constant multiples of operand lengths, with at most constant replication per recursion level and polynomial total child count. In particular positive denominators are retained and probabilities normalized exactly as rationals. This is a worst-case polynomial bound, not a practical speed benchmark.

## 4. Full scalar FPTAS on retained cactus

In any subinstance choose an admissible maximal base weight state. Conditioning on other variables changes its weight relative to base by at most two vertex factors in [7/8,1] and one cycle factor in [1,2]. Thus its probability is >= (7/8)^2/(4*2)=49/512, surviving averaging and sequential pinnings. The exact partition identity is Q_empty(J)=2^n w(x*)/prod_i p_i, where w includes all factors and x* is the sequential reference configuration. Empty graph exact. For 0<epsilon<=1 approximate every p_i to absolute error <=(49/512)epsilon/(8 max(1,m)) using L=O(log(m/epsilon)). As in R810, log-product error <=epsilon/4 and relative partition error <=epsilon. All-occupied assignment is feasible and positive. Cycle extraction is polynomial (DFS biconnected components, verify blocks are bridges or simple cycles). Road matrix construction from explicit sequences uses linear matrix multiplications with polynomial bit lengths; binary compressed road lengths are not claimed. Overall deterministic FPTAS in explicit rational input size and 1/epsilon for Q_empty(J), independent of cycle rank. In particular full scalar Q_empty(E) on cactus E, and arbitrary G with retained cactus J and R809-certified cut loss <=epsilon/2 (run FPTAS at epsilon/2). The latter goes beyond treewidth-2 exact counting because E can be arbitrarily dense. This replaces R810's 2^r enumeration on this retained family. No universal full-Q FPTAS for arbitrary overlapping cycles is established.

## 5. Verification

Actually executed JS BigInt rational verifier below. Five explicit kernels (triangle, K4 with retained square, two triangles sharing vertex plus extra edge, six-cycle plus chord, forest), two weight modes (identity and heterogeneous lengths 0,1,2 at a=7/8), actual degree-paid vertex factors. For each, compare parity expansion and cycle-factor partition; compare exact recursive and brute marginal probabilities under four domain/factor configurations, check reference state and occupancy cap, and all 14 nontrivial events at budgets 0..3. Test counts: {"instances":10,"parityChecks":10,"conditionalInstances":40,"marginalChecks":832,"truncationChecks":11648,"capChecks":188,"referenceChecks":208,"recursionNodes":5112}. All checks passed. Exact recursion cap also checked within calls. This is finite author validation of the implementation, not independent review or native BRC experiment.

```javascript
function verify(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a},f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}let g=gcd(a,b);return[a/g,b/g]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sub=(a,b)=>add(a,[-b[0],b[1]]),cmp=(a,b)=>a[0]*b[1]-b[0]*a[1],abs=a=>[a[0]<0n?-a[0]:a[0],a[1]],pow=(a,n)=>f(a[0]**BigInt(n),a[1]**BigInt(n)),one=f(1),zero=f(0),rho=f(32,81),base=f(3,4),sum=a=>a.reduce(add,zero),states=m=>[0,1,2,3].filter(s=>m>>s&1);
 const stats={instances:0,parityChecks:0,conditionalInstances:0,marginalChecks:0,truncationChecks:0,capChecks:0,referenceChecks:0,recursionNodes:0};
 const ck=(b,msg)=>{if(!b)throw Error(msg+" "+JSON.stringify(stats))};
 const cases=[
 [3,[[0,1],[1,2],[2,0]],[[0,1,2]]],
 [4,[[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]],[[0,1,2,3]]],
 [5,[[0,1],[1,2],[2,0],[0,3],[3,4],[4,0],[1,3]],[[0,1,2],[3,4,5]]],
 [6,[[0,1],[1,2],[2,3],[3,4],[4,5],[5,0],[0,3]],[[0,1,2,3,4,5]]],
 [4,[[0,1],[1,2],[2,3]],[]]
 ];
 for(const [n,E,cycles] of cases)for(let mode=0;mode<2;mode++){
  let m=E.length,deg=Array(n).fill(0);E.forEach(([u,v])=>{deg[u]++;deg[v]++});
  const ws=E.map((_,i)=>(mode===0?[2,0,0,1]:[[2,0,0,1],[7,4,4,2],[81,44,44,24]][i%3]).map(x=>f(x))),eta=E.map((_,i)=>mode===1&&i%3===2?f(1,3):one),dom=ws.map(w=>w.reduce((a,x,i)=>a|(x[0]>0n?1<<i:0),0));
  const vf=deg.map((d,v)=>({id:v,c:f(-1,2n**BigInt(2*d+1)),cost:Math.max(1,d-1),t:E.flatMap(([u,w],i)=>u===v?[[i,3]]:w===v?[[i,5]]:[])}));
  const cf=cycles.map((C,i)=>({id:n+i,c:C.reduce((a,e)=>mul(a,eta[e]),one),cost:0,t:C.map(e=>[e,8])}));
  const fs=[...vf,...cf];
  const memo=new Map();
  function dist(d,fs,e,L){
   let key=JSON.stringify([d,fs.map(g=>[g.id,g.t]),e,L]);if(memo.has(key))return memo.get(key);
   stats.recursionNodes++;
   let incident=fs.filter(g=>g.t.some(([i])=>i===e)),rest=fs.filter(g=>!incident.includes(g)),out=Array(4).fill(zero);
   for(let s of states(d[e])){
    let w=ws[e][s],live=rest.slice(),dd=d.slice();dd[e]=0;
    if(L!==0)for(const g of incident){
     let t=g.t.filter(([i])=>i!==e);
     if(!(g.t.find(([i])=>i===e)[1]>>s&1))continue;
     let p=one,free=t.filter(([i,mask])=>(dd[i]&mask)!==dd[i]);
     if(free.some(([i,mask])=>!(dd[i]&mask)))p=zero;
     else{
      let cost=g.c[0]>0n?free.length:g.cost;
      if(free.length&&L>=0&&cost>L)p=zero;
      else{
       let d2=dd.slice();
       for(let [i,mask] of free){
        let q=dist(d2,live,i,L<0?-1:L-cost),a=sum(states(d2[i]&mask).map(x=>q[x]));
        if(g.c[0]>0n){if(L<0)ck(cmp(a,rho)<=0n,"cap exact recursion");if(cmp(a,rho)>0n)a=rho;}
        p=mul(p,a);d2[i]&=mask;
       }
      }
     }
     w=mul(w,add(one,mul(g.c,p)));live.push({...g,t});
    }
    out[s]=w;
   }
   let z=sum(out);let result=out.map(x=>div(x,z));memo.set(key,result);return result;
  }
  function brute(d,fs,e=-1){
   let z=zero,out=Array(4).fill(zero),x=Array(m).fill(0);
   function rec(i,w){if(i===m){for(let g of fs)if(g.t.every(([j,mask])=>mask>>x[j]&1))w=mul(w,add(one,g.c));z=add(z,w);if(e>=0)out[x[e]]=add(out[x[e]],w);return;}if(!d[i]){rec(i+1,w);return;}for(let s of states(d[i])){x[i]=s;rec(i+1,mul(w,ws[i][s]));}}
   rec(0,one);return {z,p:e<0?null:out.map(w=>div(w,z))};
  }
  let J=cycles.flat(),z=zero;
  for(let b=0;b<1<<J.length;b++){let T=0,d=dom.slice(),w=one;for(let i=0;i<J.length;i++)if(b>>i&1){let e=J[i],[u,v]=E[e];T^=(1<<u)|(1<<v);d[e]=8;w=mul(w,eta[e]);}if(!T)z=add(z,mul(w,brute(d,vf).z));}
  ck(cmp(z,brute(dom,fs).z)===0n,"parity");stats.parityChecks++;
  let configs=[[dom,fs],[dom.map((x,i)=>i===0?8:x),fs],[dom.map((x,i)=>i===1?(x&7):x),fs],[dom,fs.filter(g=>g.id!==0)]];
  for(let [d,active] of configs){stats.conditionalInstances++;
   for(let e=0;e<m;e++){
    let p=brute(d,active,e).p,q=dist(d,active,e,-1);
    for(let s=0;s<4;s++){ck(cmp(p[s],q[s])===0n,"exact");stats.marginalChecks++;}
    let best=states(d[e]).reduce((i,j)=>cmp(ws[e][i],ws[e][j])>=0n?i:j);ck(cmp(p[best],f(49,512))>=0n,"ref");stats.referenceChecks++;
    if((d[e]&8)&&states(d[e]).length>1){let q0=brute(d,active.filter(g=>g.c[0]<0n||!g.t.some(([i])=>i===e)),e).p[3];ck(cmp(q0,rho)<=0n,"cap");stats.capChecks++;}
    for(let L=0;L<=3;L++){let a=dist(d,active,e,L);for(let mask=1;mask<15;mask++){let h=abs(sub(sum(states(mask).map(s=>a[s])),sum(states(mask).map(s=>p[s]))));ck(cmp(h,pow(base,L))<=0n,"truncation");stats.truncationChecks++;}}
   }
  }
  stats.instances++;
 }
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 6. Next

Extend the cycle-paid factor method to edge-overlapping biconnected blocks, using independent block parity polynomials rather than a separate factor for every overlapping cycle; bound conditional product perturbations with an explicit cost paid by support size. Nonzero T on cactus yields complementary forced subsets per cycle and mandatory bridges, so the current positive 1+lambda I factor proof does not automatically transfer. Investigate that separately. Benchmark exact rational recursion against R810 2^r enumeration. Preserve R809 reversal and R805 observation-specific bridge conditions.
