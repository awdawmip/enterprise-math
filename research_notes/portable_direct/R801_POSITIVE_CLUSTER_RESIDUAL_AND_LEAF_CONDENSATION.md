# R801 — Positive cluster residual, exact leaf condensation and certified approximation

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R800, original own session metadata verified, Researcher EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; no own RUN and execution_authorized=false. Owner inventory request r3-20261126-0224-owners last observed RUNNING before this computation; no inference of absent owners. No shared Task/CLAIM/Result/Review change. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer 3923890d77a02d84b772f789e6912dd14f220d14 read; generated foundation package and Heartbeat companion absent at this pin (404). ACTIVE worldview and global main entries at 8ec14e35593c0dfb76fc17e3d1cbff0d26380e3e, current method/portable/continuation rules consulted. Auxiliary unsigned Boolean/integer branch observer; not a claim about signed native BRC or dynamics.

Predecessors: R795 1a2471a8b10ac6f0a8d7eadeb05f27def385aff3:research_notes/portable_direct/R795_INTRINSIC_FIXED_RANK_PORT_SELECTOR.md; R799 9b0c500f0972f718ee7a2ba3e674448f53f40188:research_notes/portable_direct/R799_UNIVERSAL_CYCLE_OVERLAP_AND_MIXED_MOMENT_HARDNESS.md; R800 9900c89f1c8783e6f5b9bd9eaa3b528c75c286a4:research_notes/portable_direct/R800_BOOLEAN_PREFIX_COUNT_HARDNESS_BY_STRETCHING.md.

## 1. Exact positive cluster representation
Use R799's aligned two-boundary realization of any finite simple bipartite overlap B=(V,F), n vertices, q edges, c_v exclusive connectors of cycle v (unpadded c_v=2d_v for d_v>0, else 3). H=H12(1,1) counts each feasible common prefix once. Set D=2^(sum c_v), delta_v=2^(-c_v-1), a_v=1-delta_v. T=D Z_B(2) is R800 orientation mass, NOT R799 full mixed moment (which includes private multiplicities).

For a shared prefix, let A subset F contain exactly the nonflexible slots. Each such edge forces both endpoint cycles to the same specified sign; feasibility requires a uniform sign on each nontrivial connected component of (V,A). Each component with >=1 edge has precisely two sign assignments; an isolated vertex has both directions still available. Exclusive connectors contribute 2^c_v for forced direction or 2^(c_v+1)-1 for an isolated vertex. This is exactly R800's nonnegative mask algorithm grouped by the full set A, not a guess of independent cycles. Writing k(A) for number of connected components including isolated vertices and I(A) for the isolated vertex set, we obtain
 H/D = Q_B(a) = sum_{A subset F} 2^k(A) product_{v in I(A)} a_v.
With a=1 this is Z_B(2), by expansion of product over edges of (1+1_{equal spins}). Every A's exact correction is retained. In particular H/T=E_RC[product_{v in I(A)} a_v], where RC is the finite probability measure proportional to 2^k(A). This is positive, unlike the alternating ternary contraction. It gives an exact O(2^q(n+q)) elementary arithmetic algorithm with DSU (or graph traversal) versus O(3^q(n+q)) in R800; input lengths, integer operations and bit costs are separate. It applies to the specified aligned, single-shared-slot family, not arbitrary sign-frustrated or dependent weights.

## 2. Multiplicative residual certificate
For arbitrary a in [7/8,1]^V consider the tilted measure proportional to 2^k(A) product of a_v for isolated v. This includes the actual R799 c_v>=2 (even isolated c_v>=3), and all leaf updates below. Conditional on all other edge choices, opening an absent edge has weight ratio 1 if its endpoints are already connected, otherwise (1/2) times the inverse product of a_v for endpoints currently isolated. This ratio lies in [1/2,1], since (7/8)^2>1/2. Thus every conditional probability of an absent edge lies in [1/2,2/3], including conditioning on a subset of other edges by averaging. For any vertex v, chain rule gives
 2^(-d_v) <= Pr(v isolated) <= (2/3)^d_v.
These bounds hold with any subset of penalties applied. Insert penalties one by one, from all a=1. Each new vertex factor changes the partition by exactly 1-delta_v Pr_current(v isolated). Multiplication proves
 product_v (1-delta_v (2/3)^d_v) <= Q_B(a)/Z_B(2) <= product_v (1-delta_v 2^(-d_v)).
The degree-zero factors are exact. This is valid without the small-sum assumption and corrects R800's uniform union bound. In particular 1-H/T <= sum_v delta_v(2/3)^d_v. At an unpadded nonisolated vertex this payment is (1/2)6^(-d_v), instead of 4^(-d_v) in R800. Dropping only a subset of penalties admits the same product error certificate relative to the retained model (start with retained penalties, insert the omitted ones). No removal of the underlying common-prefix or source objects is implied.

## 3. Exact leaf condensation and 2-core reduction
A degree-zero vertex u can be removed with scalar factor 2a_u. If u is a leaf incident to v, put b=2a_u. For a fixed subset A of the remaining edges, when v is nonisolated the two choices of leaf edge yield common factor b+1. When v is isolated, the leaf absent contributes b*(2a_v) and present contributes 2. Therefore
 Q_B(a)=(1+2a_u) Q_{B-u}(a'), a'_v=(1+2a_u a_v)/(1+2a_u), a'_w=a_w otherwise.
 Equivalently delta'_v=(2a_u/(1+2a_u))delta_v <= (2/3)delta_v.
This proves equality for every remaining edge subset, a scoped port replacement with an isolated/nonisolated interface. Repeated leaf and isolated elimination gives exact Q=K Q_core(a') on the 2-core, with scalar K and updated rational activities. Every update preserves a>=7/8. Forests are solved exactly, and a tree attached by a single edge can never increase the residual at the attachment vertex. For each removed neighbor the deficit at that vertex is reduced by at least a factor 2/3. Queue-based implementation uses O(n+q) graph/arithmetic operations; the simple verification script scans vertices and is not that implementation. Exact rational sizes stay polynomial: leaf messages are ratios of partial sums of the original finite edge-subset weights, whose common denominator divides the original product of denominators, and integer numerator length O(n+q+sum c_v). Multiplying final D gives exact integer H. Isolated vertex and leaf rules preserve the partition for all remaining edge subsets, but not the original lift provenance; keep the original graph and elimination trace if those are needed.

## 4. A restricted FPRAS by ordinary ferromagnetic sampling
Let C be the 2-core, n' its order, q' its edge count, and L=product_{v in C}(1-delta'_v(2/3)^d_C(v)). The above exact reduction and certificate imply H=D K Z_C(2) mu, where mu=E_RC[X], X=product_{v in I(A)}a'_v in [0,1] and mu>=L. If S=sum delta'_v(2/3)^d_C(v)=O(log N), where N is input length, then L>=exp(-2S)=N^(-O(1)), since each summand <=1/8 and -log(1-x)<=2x. This includes all forests and cores whose remaining total defect has logarithmic growth; a sufficient unpadded degree condition is n' 6^(-d_min(original))=O(log N) for vertices remaining in C, using leaf attenuation to compensate for degree loss (each removed incident edge multiplies delta by <=2/3, so delta'_v(2/3)^d_C(v)<=delta_v(2/3)^d_B(v)).

Use Jerrum and Sinclair, Polynomial-Time Approximation Algorithms for the Ising Model, SIAM J Comput 22(5), 1087–1116 (1993), doi:10.1137/0222066, for an FPRAS of the zero-field ferromagnetic partition function. To obtain approximate independent RC samples, sequentially condition each edge. For any remaining graph (contract already-open edges, delete already-closed edges), opening e contributes Z(G/e), closing contributes Z(G-e); this follows directly by partitioning the edge-subset sum. Loops are removable with exact factor 2 (and open probability 1/2 if sampling them), parallel edges are standard ferromagnetic couplings. No native phase interpretation is used. Approximate both branch weights to relative eta; their ratio probability changes by at most 2eta for eta<=1/2. By coupling over q' choices the distribution's total variation is <=2q' eta plus the sum of oracle failure probabilities. Choose these errors O(epsilon L/(q'+1)) per call to bound the sampling expectation bias by epsilon L/8. Independent approximate samples with X in [0,1] and mean >=(1-epsilon/8)mu require O((epsilon^2 L)^(-1) log(1/beta)) samples by multiplicative concentration. Relative approximation to Z_C(2) and mu with adjusted epsilon and union-bounded failures yields a relative epsilon estimate of H with failure <=beta in polynomial time whenever L inverse polynomial. This is a proved oracle-based restricted FPRAS, not an implementation or an all-graphs approximation result. For a large unpadded bounded-degree cyclic core, S may grow linearly and this certificate may become exponentially weak. Its failure says nothing about the existence of other algorithms. Next: develop a sampler for the tilted positive cluster measure itself, or a locally controlled expansion that avoids the extensive global correction; also consider frustrated signs separately.

## 5. Exact finite validation
Executed the dependency-free BigInt rational code below, on all labeled bipartite graphs with part sizes (1,1),(1,2),(2,1),(2,2),(2,3),(3,3), including empty graphs, three connector-length vectors each (base, +1, heterogeneous +v mod 3). Direct R800 mask enumeration was compared to exact positive cluster summation, exact leaf pruning, and both multiplicative inequalities before and after pruning. The numerical example ratios printed are display-only; all equalities and inequalities tested by exact integer cross-products. No new full XOR simulation, sampler execution, proof review or runtime performance claim. Actual output:
```json
{
  "graphs": 602,
  "cases": 1806,
  "shared": 799596,
  "subsets": 61542,
  "coreSubsets": 29061,
  "peelSteps": 7833,
  "emptyCore": 1221,
  "examples": [
    {
      "graph": "K1,1",
      "H": "81",
      "ratio": 0.84375,
      "lower": 0.8402777777777778,
      "upper": 0.87890625,
      "core": 0,
      "coreLower": 1
    },
    {
      "graph": "K1,2",
      "H": "3823",
      "ratio": 0.8296440972222222,
      "lower": 0.8286072530864198,
      "upper": 0.872039794921875,
      "core": 0,
      "coreLower": 1
    },
    {
      "graph": "K2,1",
      "H": "3823",
      "ratio": 0.8296440972222222,
      "lower": 0.8286072530864198,
      "upper": 0.872039794921875,
      "core": 0,
      "coreLower": 1
    },
    {
      "graph": "K2,2",
      "H": "5087105",
      "ratio": 0.9466227089486471,
      "lower": 0.9455911723274844,
      "upper": 0.9691143073141575,
      "core": 4,
      "coreLower": 0.9455911723274844
    },
    {
      "graph": "K2,3",
      "H": "6060811615",
      "ratio": 0.9556945062503612,
      "lower": 0.9544751008668374,
      "upper": 0.9748383547989761,
      "core": 5,
      "coreLower": 0.9544751008668374
    },
    {
      "graph": "K3,3",
      "H": "186835921067265",
      "ratio": 0.9872260294062021,
      "lower": 0.986191238983222,
      "upper": 0.9941549115019317,
      "core": 6,
      "coreLower": 0.986191238983222
    }
  ],
  "mismatches": 0
}
```
```javascript
function verify(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
 const R=(a,b=1n)=>{let g=gcd(a,b);return [a/g,b/g]};
 const add=(x,y)=>R(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),mul=(x,y)=>R(x[0]*y[0],x[1]*y[1]),div=(x,y)=>R(x[0]*y[1],x[1]*y[0]),sub=(x,y)=>add(x,[-y[0],y[1]]),le=(x,y)=>x[0]*y[1]<=y[0]*x[1],eq=(x,y)=>le(x,y)&&le(y,x),P=(b,k)=>BigInt(b)**BigInt(k);
 const one=R(1n),two=R(2n);
 function cluster(n,F,a,active=Array.from({length:n},(_,i)=>i)){
  let z=R(0n),raw=0n;
  for(let s=0;s<2**F.length;s++){
   let parent=Array.from({length:n},(_,i)=>i),used=Array(n).fill(false),k=active.length;
   const find=x=>{while(x!==parent[x])x=parent[x];return x};
   for(let j=0;j<F.length;j++)if(s>>j&1){let [u,v]=F[j];used[u]=used[v]=true;let x=find(u),y=find(v);if(x!==y){parent[x]=y;k--}}
   let base=P(2,k),w=R(base);raw+=base;
   for(let v of active)if(!used[v])w=mul(w,a[v]);z=add(z,w);
  }return [z,raw];
 }
 function peel(n,F,a){
  let A=a.slice(),active=Array.from({length:n},(_,i)=>i),E=F.slice(),factor=one,steps=0;
  while(true){let d=Array(n).fill(0);for(let [u,v] of E){d[u]++;d[v]++}
   let u=active.find(v=>d[v]<=1);if(u===undefined)break;
   if(d[u]===0)factor=mul(factor,mul(two,A[u]));
   else{let e=E.find(e=>e.includes(u)),v=e[0]===u?e[1]:e[0],b=mul(two,A[u]),f=add(b,one);
    A[v]=div(add(mul(b,A[v]),one),f);factor=mul(factor,f);E=E.filter(x=>x!==e)}
   active=active.filter(v=>v!==u);steps++;
  }return {A,active,E,factor,steps};
 }
 function bounds(n,F,a,active){let d=Array(n).fill(0);for(let [u,v] of F){d[u]++;d[v]++}let lo=one,hi=one;
  for(let v of active){let delta=sub(one,a[v]);lo=mul(lo,sub(one,mul(delta,R(P(2,d[v]),P(3,d[v])))));hi=mul(hi,sub(one,mul(delta,R(1n,P(2,d[v])))))}return [lo,hi];
 }
 function direct(n,F,c){let H=0n;
  for(let s=0;s<3**F.length;s++){let t=s,M=Array(n).fill(3);for(let [u,v] of F){let a=[3,1,2][t%3];t=Math.floor(t/3);M[u]&=a;M[v]&=a}
   let w=1n;for(let v=0;v<n;v++){let D=P(2,c[v]);w*=M[v]===0?0n:M[v]===3?2n*D-1n:D}H+=w;
  }return H;
 }
 let graphs=0,cases=0,shared=0,subsets=0,peelSteps=0,emptyCore=0,coreSubsets=0,examples=[];
 for(let [l,r] of [[1,1],[1,2],[2,1],[2,2],[2,3],[3,3]]){
  let n=l+r,all=[];for(let u=0;u<l;u++)for(let v=0;v<r;v++)all.push([u,l+v]);
  for(let mask=0;mask<2**all.length;mask++){let F=all.filter((_,j)=>mask>>j&1),d=Array(n).fill(0);for(let [u,v] of F){d[u]++;d[v]++}graphs++;
   for(let pad of [0,1,2]){let c=d.map((x,v)=>(x?2*x:3)+(pad===2?v%3:pad)),D=P(2,c.reduce((x,y)=>x+y,0)),a=c.map(x=>sub(one,R(1n,P(2,x+1)))),A=Array.from({length:n},(_,i)=>i);
    let H=direct(n,F,c),[Z,z0]=cluster(n,F,a),[lo,hi]=bounds(n,F,a,A);
    if(!eq(R(H,D),Z)||!le(mul(R(z0),lo),Z)||!le(Z,mul(R(z0),hi)))throw Error("cluster or bound");
    let p=peel(n,F,a),[z,zbase]=cluster(n,p.E,p.A,p.active),[cl,ch]=bounds(n,p.E,p.A,p.active);
    if(!eq(Z,mul(p.factor,z))||!le(mul(R(zbase),cl),z)||!le(z,mul(R(zbase),ch)))throw Error("peel or core bound");
    cases++;shared+=3**F.length;subsets+=2**F.length;coreSubsets+=2**p.E.length;peelSteps+=p.steps;if(!p.active.length)emptyCore++;
    if(pad===0&&mask===2**all.length-1){const f=x=>Number(x[0])/Number(x[1]);examples.push({graph:`K${l},${r}`,H:String(H),ratio:f(div(Z,R(z0))),lower:f(lo),upper:f(hi),core:p.active.length,coreLower:f(cl)})}
   }
  }
 }
 return {graphs,cases,shared,subsets,coreSubsets,peelSteps,emptyCore,examples,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```
