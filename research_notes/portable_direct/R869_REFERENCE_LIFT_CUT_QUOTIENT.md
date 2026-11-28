# R869 — Reference-lift cut quotient and exact forest counting
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Predecessor: 37285cc9cb2e596413bf7f89919e331c7f687c26:research_notes/portable_direct/R868_THRESHOLD_CLAUSE_RESIDUAL_PARAMETER.md (full read). Existing lane RA-708BCC309CE076D8BB599B91 / EM-DIRECT-82A007 public recovery metadata checked; no execution authority asserted. Current normative Source efbea300651af51f8dd1f67086acbad10084b72c; global entry verified 114e5570f1ed7d653e9e6baf43fb9b4eb0cfa790, ACTIVE worldview, global P000 V4. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: root p000_reality_foundation.json V5 and mandatory joint relation observer read. Separate residual companion at this pin returned 404; no repin. R868 original RUNNING query SUCCEEDED with empty RUNNING slice as of 2026-11-28T13:24:01.222782Z; Source changed during query; current r3-20261128-r869-running-read last observed WAITING_RESOURCE / SOURCE_LOCK_BUSY. Independent portable auxiliary integer relationship work; no shared ownership mutation or native BRC attribution.

## 1. Reference difference and lifted coarea bound
Same finite explicit distinct-value integer domains D_v and additive integer unary costs c_v as R868; loopless undirected multigraph with indexed parallel edges allowed. For e=uv, target t_e, signed residual eps_e(x)=x_u+x_v-t_e, slack S(x)=sum_e |eps_e(x)|, cap K>=0 integer. Let X be any verified feasible witness with S(X)=k0<=K, obtainable by R868 decision/witness reduction (external Almost-2-SAT engine not implemented here). If infeasible, return zero count and no optimum. Define d_v=x_v-X_v and B=K+k0. Every feasible x satisfies sum_e |d_u+d_v| <= S(x)+S(X)<=B. This bound preserves signs through eps_e(x)=eps_e(X)+d_u+d_v; it is not a replacement budget.

Build the undirected two-sheeted graph H with nodes (v,+),(v,-) and for each original indexed edge two unit-capacity edges (u,+)(v,-) and (u,-)(v,+). Set z(v,+)=d_v, z(v,-)=-d_v. Lift total variation is twice sum_e |d_u+d_v| <=2B. The involution swaps sheets and edges. For a connected component C of H, if its involution image is disjoint, the two mirrored components have equal variation, hence TV_C<=B; otherwise TV_C<=2B. Set T_C accordingly. For a,b in C let lambda(a,b) denote unit edge mincut capacity, counting parallel copies. For integer z, coarea identity TV_C = sum_{h=min z+1}^{max z} |cut({v:z_v>=h})|. Each threshold strictly between z_a,z_b separates a,b and contributes at least lambda(a,b). Thus
 lambda(a,b)*|z_a-z_b| <= TV_C <= T_C.
Consequently |z_a-z_b|<=floor(T_C/lambda(a,b)). If lambda(a,b)>T_C, z_a=z_b for every feasible assignment. In addition if a=(v,+), b=(v,-) in the same C, 2lambda(a,b)|d_v|<=2B, so lambda(a,b)>B forces d_v=0 even without the full class merge. This latter strengthening is proved but not used by the implementation. The variation/cut identities are classical combinatorial tools; contribution here is their exact reference-relative application to the finite signed relation model and quotient.

## 2. Exact quotient and inexpensive class construction
Within C, define a~b when a=b or lambda(a,b)>T_C. This is an equivalence: every separating cut of a,c also separates a,b or b,c; hence lambda(a,c)>=min(lambda(a,b),lambda(b,c)). Different components are separate. Involution preserves class structure and thresholds. Any class invariant under involution has z=0; each unordered pair of distinct mirrored classes has one signed integer coordinate y_j. For each original v store j(v), s_v in {+1,-1}, or fixed d_v=0, such that x_v=X_v+s_v y_j. Each y_j lies in the intersection over its member vertices of s_v(D_v-X_v), including arbitrary holes. Set cost C_j(y)=sum of original c_v(X_v+s_v y) over members, plus fixed constant. For every original edge retain its exact identity, target, endpoints and signed affine formula eps_e(X)+s_u y_j(u)+s_v y_j(v) (fixed terms omitted). Edges with identical group endpoints become unary or constant, not silently erased. Between distinct group pairs keep the exact sum of absolute affine terms for budget evaluation, plus individually recoverable signed terms.

The map from feasible originals to quotient coordinates is injective because each nonfixed pair has original vertices supplying its value; it is surjective onto quotient assignments satisfying the ORIGINAL slack cap since inverse reconstruction satisfies every domain and computes every original residual. Hence full feasible assignment counts, arbitrary additive costs, exact slack histogram, signed residual vector and original witness are preserved. The result is conditional on the fixed cap/reference; no claim for increased cap or different graph without a new certificate. All future observers of feasible assignments factor through this explicit lossless inverse map; only independent variables are compressed, original relation identities stay in the decoder.

Class discovery without all-pairs flows: partition each C initially as one candidate group, use representatives of merged blocks. Choose two representatives a,b in a group. Run undirected integer maxflow until flow>T_C or exhausted. High flow merges the blocks. A completed flow<=T_C supplies a separating cut; split the current representative group by its sides, which cannot split any already high-connected block. Always use the original H for flows, not induced subgraphs of current groups. Repeat until each group has one representative. Each merge or split decreases sum_groups (number_of_representatives-1) by exactly one, so at most |V(H)|-number_components flows, not quadratic. Threshold-capped augmenting-path flow uses at most T_C+1 augmentations (unit capacities aggregate safely), each O(|V(H)|+|E(H)|), with additional grouping overhead O(|V(H)|^2) in this simple implementation. Thus polynomial/FPT-in-K preprocessing O(n(B+1)(n+m)+n^2), plus explicit domain intersection, integer bit costs and reference acquisition. Graph and quotient storage polynomial. Could use Gomory-Hu or sparse-cut certificates in later engineering, not required here.

## 3. Exact count and optimization on quotient forests
Let Q be the simple interaction graph of free quotient coordinates; all parallel residual terms between one pair aggregate to their exact sum for budget arithmetic. Constant slack b0, unary residual u_j(y) and pair cost g_ij(y,z) are nonnegative integers. Each coordinate has arbitrary additive cost C_j(y). If Q is a forest, root components. For each vertex v, y in its domain, k<=K store exact count N_v(y,k), minimum additive cost M_v(y,k), and witness backpointer for feasible states. Initialize at k=u_v(y) with count 1 and cost C_v(y). Merge child w with z,l by k_new=k+l+g_vw(y,z); multiply counts then sum over alternatives, and add costs then minimize. Distinct alternatives split by unique child assignment and exact slack. At component roots sum/min over root values; convolve disconnected components and add fixed cost and constant slack. Discard k>K since all residual contributions are nonnegative. Exact slack histogram, total count, min arbitrary unary cost and one optimum witness follow from induction. For q vertices, maximum domain size Dmax, time O(q Dmax^2(K+1)^2) arithmetic/dictionary operations after evaluating unary/pair tables (O(m Dmax^2) safe bound); polynomial bit costs, backpointer space O(q Dmax(K+1)), plus pair tables, if using stage backpointers. Test code uses explicit witness lists and may cost extra polynomial copying. Thus K-only FPT counting and arbitrary cost optimization on the class whose certified quotient is a forest, even when the original graph has unbounded feedback count and treewidth. General quotient graphs remain open; contraction does not imply bounded treewidth in terms of K. For instance, binary-domain square-grid equality-gauged examples at sufficiently large fixed K have singleton/limited classes and unbounded treewidth. R868 general feasibility remains FPT; no general counting/optimization FPT is asserted. For a connected original graph and supplied quotient tree decomposition of width w, R867 root-domain conditioning gives at most 2K+1 possible values per original vertex once a root value is fixed, hence at most 2K+1 per quotient pair by intersecting these windows; ordinary tree-decomposition DP yields FPT in K+w with polynomial explicit root-domain enumeration. This extension is not implemented.

## 4. Structured dense block chain
d blocks of K_{p,p} binary domains, target 1, bridge from previous block's right vertex to next block's left vertex; K=2, p=5. Reference proper within each block but flip first block, so k0=1, B=3. Original graph bipartite; each lifted component has T=3. Every internal pair in each block has edge-connectivity at least p=5 (cut proof: for a,b vertices on each side of a cut, size p(a+b)-2ab, nontrivial minimum p by affine endpoint minimization); bridge cuts have capacity 1. Thus each block is exactly one free quotient coordinate, interaction graph a path. Original feasible assignments are precisely block orientations with at most 2 bridge violations, count 2 sum_{j=0}^2 binom(d-1,j). Costs are x on left vertices, zero right; all left zero yields optimum 0. Test d=40 (400 vertices, 1039 edges, feedback 640 for connected graph); actual result below. Also test nonbipartite K6 target zero, domains {-1,0,1}, reference zero, cap2: lift is K6,6 minus perfect matching, computed class fixed (full cut class checked by flows); brute original assignments confirm unique zero. A 101-digit domain test confirms arithmetic independent of value scale. 

## 5. Actual reproducible computation
JavaScript BigInt values, signed residuals, costs, budgets, counts; bounded unit flow capacities and indices exact safe integers. Fixed seed 8692026. Random reference is constructed and verified, not solved by external FPT engine. For random small networks independently exhaust all lifted cuts for each same-component pair, and all original assignments; compare exact quotient feasible set, signed formula and costs, and forest histogram/optimum/witness whenever quotient forest. Large block chain uses independent analytic formula, not exhaustive original assignments. Actual output:
```json
{
  "random": 240,
  "original_assignments": 9056,
  "quotient_assignments": 7422,
  "feasible_assignments": 1326,
  "signed_checks": 47002,
  "cut_pair_checks": 2541,
  "forest_instances": 172,
  "flow_calls": 1637,
  "failures": 0,
  "huge": {
    "vars": 1,
    "classes": 2,
    "count": "2",
    "best": "0",
    "forest": true
  },
  "odd": {
    "vars": 0,
    "classes": 1,
    "count": "1",
    "best": "0",
    "forest": true
  },
  "dense_chain": {
    "vertices": 400,
    "edges": 1039,
    "K": 2,
    "reference_slack": "1",
    "B": "3",
    "quotient_variables": 40,
    "quotient_pairs": 39,
    "flow_calls": 798,
    "count": "1562",
    "best": "0",
    "hist": [
      [
        "0",
        "2"
      ],
      [
        "1",
        "78"
      ],
      [
        "2",
        "1482"
      ]
    ],
    "expected": "1562"
  }
}
```
```javascript
function verify869(){
 const ck=(x,m)=>{if(!x)throw Error(m)}, abs=x=>x<0n?-x:x, sum=a=>a.reduce((x,y)=>x+y,0n);
 const out={random:0,original_assignments:0,quotient_assignments:0,feasible_assignments:0,signed_checks:0,cut_pair_checks:0,forest_instances:0,flow_calls:0,failures:0};
 const slack=(E,x)=>sum(E.map(([u,v,t])=>abs(x[u]+x[v]-t)));
 function make(D,E,X,K){
  const n=D.length,N=2*n, B=K+slack(E,X);ck(slack(E,X)<=K,"reference");
  ck(X.every((x,i)=>D[i].has(x)),"reference domain");
  const adj=Array.from({length:N},()=>new Map()), le=[];
  function edge(a,b){le.push([a,b]);adj[a].set(b,(adj[a].get(b)||0)+1);adj[b].set(a,(adj[b].get(a)||0)+1);}
  for(const [u,v] of E){edge(2*u,2*v+1);edge(2*u+1,2*v);}
  const comps=[],cid=Array(N).fill(-1);
  for(let a=0;a<N;a++)if(cid[a]<0){let q=[a];cid[a]=comps.length;for(let j=0;j<q.length;j++)for(const b of adj[q[j]].keys())if(cid[b]<0){cid[b]=cid[a];q.push(b);}comps.push(q);}
  const lim=comps.map(q=>cid[q[0]^1]===cid[q[0]]?2n*B:B);
  const parent=Array.from({length:N},(_,i)=>i);
  function find(a){while(parent[a]!==a){parent[a]=parent[parent[a]];a=parent[a];}return a;}
  function flow(a,b,T){
   out.flow_calls++;
   const cap=adj.map(m=>new Map(m));let f=0n;
   for(;;){
    const pre=Array(N).fill(-1);pre[a]=a;let q=[a];
    for(let j=0;j<q.length&&pre[b]<0;j++)for(const [v,c] of cap[q[j]])if(c>0&&pre[v]<0){pre[v]=q[j];q.push(v);}
    if(pre[b]<0)return {high:false,side:new Set(q),value:f};
    let d=Infinity;for(let v=b;v!==a;v=pre[v])d=Math.min(d,cap[pre[v]].get(v));
    for(let v=b;v!==a;v=pre[v]){let u=pre[v];cap[u].set(v,cap[u].get(v)-d);cap[v].set(u,(cap[v].get(u)||0)+d);}
    f+=BigInt(d);if(f>T)return {high:true};
   }
  }
  for(let c=0;c<comps.length;c++){
   const work=[comps[c].slice()];while(work.length){let q=work.pop();if(q.length<2)continue;let a=q[0],b=q[1],f=flow(a,b,lim[c]);if(f.high){parent[find(b)]=find(a);q.splice(1,1);work.push(q);}else{work.push(q.filter(v=>f.side.has(v)),q.filter(v=>!f.side.has(v)));}}
  }
  const cls=Array.from({length:N},(_,i)=>find(i));
  const invol=new Map();for(let i=0;i<N;i++){if(invol.has(cls[i]))ck(invol.get(cls[i])===cls[i^1],"involution");invol.set(cls[i],cls[i^1]);}
  const ids=new Map(),map=[],dom=[],costFixed={value:0n};
  for(let v=0;v<n;v++){
   let a=cls[2*v],b=cls[2*v+1];
   if(a===b){map.push([-1,0n]);costFixed.value+=D[v].get(X[v]);continue;}
   let key=Math.min(a,b),s=a===key?1n:-1n;
   if(!ids.has(key)){ids.set(key,dom.length);dom.push(null);}
   let i=ids.get(key);map.push([i,s]);
   const d=new Map([...D[v]].map(([x,c])=>[s*(x-X[v]),c]));
   dom[i]=dom[i]===null?d:new Map([...dom[i]].filter(([y])=>d.has(y)).map(([y,c])=>[y,c+d.get(y)]));
  }
  const terms=E.map(([u,v,t])=>[...map[u],...map[v],X[u]+X[v]-t]);
  let base=0n;const unary=dom.map(()=>[]),pairs=new Map(),qa=dom.map(()=>[]);
  for(const [i,s,j,t,a] of terms){
   if(i<0&&j<0)base+=abs(a);
   else if(i<0||j<0||i===j){let k=Math.max(i,j);unary[k].push([s+t,a]);}
   else {let u=Math.min(i,j),v=Math.max(i,j),key=u+","+v;
    if(!pairs.has(key)){pairs.set(key,[]);qa[u].push(v);qa[v].push(u);}
    pairs.get(key).push(i===u?[s,t,a]:[t,s,a]);}
  }
  const decode=y=>X.map((x,v)=>{let [i,s]=map[v];return i<0?x:x+s*y[i];});
  const signed=y=>terms.map(([i,s,j,t,a])=>a+(i<0?0n:s*y[i])+(j<0?0n:t*y[j]));
  const qcost=y=>costFixed.value+sum(y.map((x,i)=>dom[i].get(x)));
  const un=(i,y)=>sum(unary[i].map(([s,a])=>abs(a+s*y)));
  const ed=(i,j,y,z)=>{let a=Math.min(i,j),b=Math.max(i,j);return sum(pairs.get(a+","+b).map(([s,t,c])=>abs(c+s*(i===a?y:z)+t*(i===a?z:y))));};
  return {cls,comps,lim,cid,le,dom,map,base,qa,pairs,decode,signed,qcost,un,ed,costFixed:costFixed.value,B,flow};
 }
 function forestSolve(q,K){
  const n=q.dom.length,seen=new Set(),components=[];let isForest=true;
  for(let v=0;v<n;v++)if(!seen.has(v)){let order=[v],pa=new Map([[v,-1]]);seen.add(v);for(let j=0;j<order.length;j++)for(const u of q.qa[order[j]]){if(u===pa.get(order[j]))continue;if(seen.has(u)){isForest=false;continue;}seen.add(u);pa.set(u,order[j]);order.push(u);}components.push({order,pa});}
  if(!isForest)return null;
  function add(a,k,count,c,w){if(k>K)return;let z=a.get(k);if(!z)a.set(k,{count,c,w});else{z.count+=count;if(c<z.c){z.c=c;z.w=w;}}}
  function combine(a,b,extra=0n){let r=new Map();for(const [k,x] of a)for(const [l,y] of b)add(r,k+l+extra,x.count*y.count,x.c+y.c,x.w.concat(y.w));return r;}
  let all=new Map();add(all,q.base,1n,q.costFixed,[]);
  for(const {order,pa} of components){
   const tab=new Map(),children=new Map(order.map(i=>[i,[]]));for(const i of order.slice(1))children.get(pa.get(i)).push(i);
   for(const i of order.slice().reverse()){
    let a=new Map();
    for(const [y,c] of q.dom[i]){let row=new Map();add(row,q.un(i,y),1n,c,[[i,y]]);
     for(const j of children.get(i)){let next=new Map();for(const [z,b] of tab.get(j)){const r=combine(row,b,q.ed(i,j,y,z));for(const [k,x] of r)add(next,k,x.count,x.c,x.w);}row=next;}
     a.set(y,row);
    }tab.set(i,a);
   }
   let local=new Map();for(const row of tab.get(order[0]).values())for(const [k,x] of row)add(local,k,x.count,x.c,x.w);all=combine(all,local);
  }
  let count=0n,best=null,witness=null;for(const x of all.values()){count+=x.count;if(best===null||x.c<best){best=x.c;let y=Array(n);for(const [i,z] of x.w)y[i]=z;witness=q.decode(y);}}
  return {count,best,witness,hist:new Map([...all].map(([k,x])=>[k,x.count]))};
 }
 function check(D,E,X,K,doCuts=true){
  const q=make(D,E,X,K);
  if(doCuts)for(let c=0;c<q.comps.length;c++){
   const V=q.comps[c],pos=new Map(V.map((v,i)=>[v,i])),m=V.length;
   for(let a=0;a<m;a++)for(let b=a+1;b<m;b++){
    let best=Infinity;for(let mask=0;mask<2**m;mask++)if(((mask>>a)&1)!==((mask>>b)&1)){
     let value=0;for(const [u,v] of q.le)if(pos.has(u)&&(((mask>>pos.get(u))&1)!==((mask>>pos.get(v))&1)))value++;
     best=Math.min(best,value);}
    ck((q.cls[V[a]]===q.cls[V[b]])===(BigInt(best)>q.lim[c]),"cut class");out.cut_pair_checks++;
   }
  }
  const orig=new Map(),hist=new Map(),x=[],y=[];let best=null;
  function brute(i,c){if(i===D.length){out.original_assignments++;let k=slack(E,x);if(k<=K){orig.set(x.join(","),c);hist.set(k,(hist.get(k)||0n)+1n);if(best===null||c<best)best=c;out.feasible_assignments++;}return;}for(const [v,w] of D[i]){x[i]=v;brute(i+1,c+w);}}
  brute(0,0n);
  const observed=new Set();
  function qb(i){if(i===q.dom.length){out.quotient_assignments++;let z=q.decode(y),c=q.qcost(y),s=q.signed(y);for(let j=0;j<E.length;j++){let [u,v,t]=E[j];ck(s[j]===z[u]+z[v]-t,"signed");out.signed_checks++;}
   ck(z.every((v,j)=>D[j].has(v)),"domain");ck(c===sum(z.map((v,j)=>D[j].get(v))),"cost");if(sum(s.map(abs))<=K){let key=z.join(",");ck(orig.has(key)&&orig.get(key)===c&&!observed.has(key),"bijection");observed.add(key);}return;}for(const v of q.dom[i].keys()){y[i]=v;qb(i+1);}}
  qb(0);ck(observed.size===orig.size,"complete");
  const f=forestSolve(q,K);if(f){out.forest_instances++;ck(f.count===BigInt(orig.size)&&f.best===best,"forest result");ck(f.hist.size===hist.size&&[...hist].every(([k,v])=>f.hist.get(k)===v),"forest histogram");ck(f.witness&&slack(E,f.witness)<=K&&sum(f.witness.map((v,i)=>D[i].get(v)))===best,"witness");}
  return {vars:q.dom.length,classes:new Set(q.cls).size,count:String(orig.size),best:String(best),forest:!!f};
 }
 let seed=8692026;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n;};
 for(let a=0;a<240;a++){
  let n=1+rnd(5),D=Array.from({length:n},()=>{let d=new Map(),q=1+rnd(4);while(d.size<q)d.set(BigInt(rnd(9)-4),BigInt(rnd(17)-8));return d;}),X=D.map(d=>[...d.keys()][rnd(d.size)]),E=[];
  let k0=0n;if(n>1)for(let j=0,m=rnd(14);j<m;j++){let u=rnd(n),v=rnd(n-1);if(v>=u)v++;let r=k0<2n&&rnd(4)===0?BigInt(rnd(2)*2-1):0n;k0+=abs(r);E.push([u,v,X[u]+X[v]-r]);}
  check(D,E,X,k0+BigInt(rnd(3)));out.random++;
 }
 const M=10n**100n;
 out.huge=check([new Map([[-M,5n],[M,-1n]]),new Map([[-M,1n],[M,2n]])],Array.from({length:5},()=>[0,1,0n]),[-M,M],1n);
 const n=6,D0=Array.from({length:n},()=>new Map([[-1n,1n],[0n,0n],[1n,-1n]])),E0=[];
 for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)E0.push([i,j,0n]);
 out.odd=check(D0,E0,Array(n).fill(0n),2n,false);ck(out.odd.vars===0&&out.odd.count==="1","odd anchor");
 const p=5,d=40,D=[],E=[],X=[];for(let b=0;b<d;b++){
  const start=2*p*b;
  for(let j=0;j<2*p;j++){D.push(new Map([[0n,0n],[1n,j<p?1n:0n]]));let v=j<p?0n:1n;X.push(b===0?1n-v:v);}
  for(let i=0;i<p;i++)for(let j=0;j<p;j++)E.push([start+i,start+p+j,1n]);
  if(b>0)E.push([start-1,start,1n]);
 }
 let f0=out.flow_calls,q=make(D,E,X,2n),f=forestSolve(q,2n),expected=2n*(1n+BigInt(d-1)+BigInt((d-1)*(d-2)/2));
 ck(q.dom.length===d&&q.pairs.size===d-1&&f.count===expected&&f.best===0n,"dense chain");
 ck(f.witness&&slack(E,f.witness)<=2n&&sum(f.witness.map((x,i)=>D[i].get(x)))===0n,"dense witness");
 out.dense_chain={vertices:D.length,edges:E.length,K:2,reference_slack:String(slack(E,X)),B:String(q.B),quotient_variables:q.dom.length,quotient_pairs:q.pairs.size,flow_calls:out.flow_calls-f0,count:String(f.count),best:String(f.best),hist:[...f.hist].sort((a,b)=>Number(a[0]-b[0])).map(([k,v])=>[String(k),String(v)]),expected:String(expected)};
 return out;
}
console.log(JSON.stringify(verify869(),null,2));
```

## 6. Next
Explore whether the low-cut quotient can be decomposed into bounded-adhesion pieces with unbreakability and local connected minority certificates, allowing exact counting and arbitrary unary optimization with K alone on arbitrary graphs. Related literature verified at abstract level: Cygan et al., Minimum Bisection Is Fixed-Parameter Tractable, DOI 10.1137/140988553 (small-separator decomposition); Bergé et al., On the Parameterized Complexity of Counting Small-Sized Minimum (S,T)-Cuts, DOI 10.1137/21M1398203 (FPT counting minimum cuts, not arbitrary signed finite-domain slack solutions). No general reduction from those counting statements yet. Keep original signed identities and hard domain restrictions; do not confuse cut count with original assignment count or optimize by dropping nonzero reference edges. Native BRC/Port transfer still open.
