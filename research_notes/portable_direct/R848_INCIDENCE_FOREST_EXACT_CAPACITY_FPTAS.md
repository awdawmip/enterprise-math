# R848 — Exact-capacity incidence-forest certificate optimization

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable continuation of R847, not a claimed Task. Own public session metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 / MCP-ec17f2f30fb8409f8e664eb29ae6c08c verified by Source and em_site_control recovery_status (no runs, execution_authorized=false). Current owner read r3-20261128-r848-running-read was RUNNING on last observation; no Task/owner mutation. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint observer read; global P000 V4 and ACTIVE worldview read at 123ece7250ae03e9b550f3bc0a2b903c9b61361d. Source R847 1e96cadf2804d95507f8ab0551b1e67cf15a080b:research_notes/portable_direct/R847_GROUP_SEPARABLE_KRAFT_CAPACITY_RESIDUAL_FRONTIER.md. Current continuation/portable/method rules read. Auxiliary positive certificate resource layer only, no native BRC calculation or observer deletion.

## 1. Model and theorem

Let the bipartite graph of private Kraft scopes S and analytic anchors A be a forest. Each edge e=(S,A) has a finite nonempty list of actual witnesses z, with exact nonnegative integer consumption k_e(z), positive rational multiplier p_e(z)>=1. These may be R847 group lists; all original label identities and grades remain in the witness. Each scope has fixed boundary consumption b_S>=0 and integer budget B_S. Each anchor has fixed multiplier P_A^0>=1 and rational ceiling U_A<=2-eta, 0<eta<=1. Require
  b_S + sum_e k_e(z_e)<=B_S;
  Q_A=P_A^0 prod_e p_e(z_e)<=U_A.
Minimize C=sum_A phi(Q_A), phi(Q)=(Q-1)/(2-Q). This is the pendant-only certificate model (or an independently established set of local anchor ceilings and fixed base factors); arbitrary retained shared-bundle propagation is not assumed separable. Costs of fixed anchors are included. For rational 0<eps<=1 there is a polynomial-time algorithm in explicit list lengths, input bit size and 1/eta,1/eps (indeed logarithmic dependence on the magnitude 1/eta in bin count) which decides feasibility exactly, and returns an original feasible witness with C<= (1+eps) OPT. No capacity or safety relaxation. The degree of any vertex is unrestricted; there is no exponent in it.

## 2. Algorithm and proof

Root each tree. A message from v to its parent is a table indexed by the single parent edge's list option. For each index either return infeasible or an actual subtree assignment and its exact cost. At v, initialize resource r to fixed boundary plus parent consumption (scope) or fixed multiplier times parent multiplier (anchor); initialize accumulated cost c=0. Reject resource above its ceiling. Process child edges in arbitrary order. For each partial state and each child option with a feasible child message, combine resource by addition at scope, multiplication at anchor, and add child message cost to c. Reject excessive resource. Bin c geometrically (zero separately), keeping minimum r per bin (ties by smaller c), with reconstruction pointer. When all children are processed, add phi(r) at an anchor, nothing at scope, and choose smallest exact total. Roots have no parent option. Recover all witnesses; sum root costs for forest.

Let E be total edges and rho=1+eps/(2 max(1,E)). Choose a lower bound a>0 on positive c: minimum of 1 and all positive (P_A^0-1),(p_e(z)-1), or 1 if none. Any positive safe anchor cost is >=a, since Q>=1 and phi(Q)>=Q-1. All intermediate accumulated costs contain only finalized feasible anchors, so are <= number of anchors times (1-eta)/eta; use max(1, that bound). Exact half-open bins [a rho^j,a rho^(j+1)) plus zero. Precompute rational endpoints and use binary search.

Induction: for a reference assignment of a subtree conditioned on its parent option, child messages can replace child assignments while retaining that option and increasing cost by at most rho to the power of their number of child-edge merges. Start with the reference parent resource; combine the same child options. Additive/multiplicative resource transitions are monotone, so the retained partial resource is never larger than the reference. Addition of nonnegative costs preserves the largest previous multiplicative factor; each bin replacement increases cost by strictly less than rho and weakly reduces resource. A valid upper bound on the exponent after processing a vertex is the sum of all child exponents plus its number of child merges. At closure phi is increasing for 1<=Q<2, so adding local cost at no larger resource preserves the factor. Minimizing among final states can only improve. The exponent is at most E, and rho^E<=exp(eps/2)<=1+eps. Zero cost remains exact. Every stored state is an actual witness, so soundness and exact feasibility (including equality at capacity or safety) follow. Isolated nodes use their base and are checked directly. Root cost summation preserves the same global factor.

Let D=max list size (at least 1), J=1+ceil(log(U/a)/log(rho)) positive bins where U=max(1, number of anchors*(1-eta)/eta). The number of candidate transitions is O(E D^2 (J+1)); initialization/closing adds O((|V|+E)D(J+1)). Bin lookup adds O(log(J+1)) comparisons; exact rational endpoint bits O(J times input/rho bit lengths). Resource products and costs have polynomial bit length: each complete witness uses each edge once, each anchor rational product uses its own factors once, and sums of anchor fractions have total denominator bit length at most sum of their bit lengths. Capacities use input bit length plus log E; witness pointers polynomial, even copying whole witness adds only polynomial overhead. Thus explicit list input yields FPTAS on forest with no degree exponent. This is not an exact objective algorithm.

## 3. Combine with R847

At R1, R847 group lists preserve Kraft consumption exactly one-sided and approximate each group residual by 1+delta. If a pendant-only real certificate exists at R2 with fixed grades allowed and (R2/R1)^2>=1+delta, each group replacement has multiplier no larger than its R2 reference (all positive nonconstant terms have degree at least 2). Fixed base factors at R1 must also not exceed their reference values, boundary consumption unchanged; anchor ceilings must be the same or at least the reference products. Thus list feasibility follows and OPT_list(R1)<=C_ref(R2). Our forest solver returns exact feasible certificate with C<= (1+eps) C_ref(R2), with no further radius loss for the objective approximation. To guarantee no increase of C itself would need additional slack; no such guarantee is asserted. When R1=R2, only list feasibility is exact, not unrestricted grade feasibility. Original bundle payments d=w recover directly for pendant bundles. All original labels, signed observer data, roads and provenance are retained; only resource search states are pruned. Scope is auxiliary, not general Port FPTAS.

## 4. Reproducible exact calculation

The self-contained JavaScript below uses BigInt rational arithmetic. It uses U=number of vertices as a safe cost upper bound because every tested ceiling is 3/2, and test graph is a connected tree. Edge options are explicit synthetic resource lists, not a native Port experiment or test of R847 list construction. Four tree shapes, twelve deterministic profiles, two error levels and two roots: 192 solver calls plus one 48-edge high-degree scope star; independent complete enumeration for all 48 small instances. Exact check of feasibility, recovered witness, and approximation bound. Large instance checked for feasibility and witness cost only, not brute optimum. Counters: {"instances":48,"feasible":28,"infeasible":20,"brute_assignments":13608,"transitions":33066,"replacements":6591,"max_bins_used":218,"large":{"edges":48,"choices":"3^48","cost":["76071916674912283912182370542992","32434325728933401567365254156197"],"verified":true}}.

```js
function experiment(){
const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
const Q=(a,b=1)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a,b);return [a/g,b/g]};
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),cmp=(a,b)=>a[0]*b[1]<b[0]*a[1]?-1:a[0]*b[1]>b[0]*a[1]?1:0;
const zero=Q(0),one=Q(1),sub=(a,b)=>add(a,Q(-b[0],b[1])),phi=p=>{let v=sub(p,one);return Q(v[0]*p[1],v[1]*(2n*p[1]-p[0]))};
const check=(ok,msg)=>{if(!ok)throw Error(msg)};
let stats={instances:0,feasible:0,infeasible:0,brute_assignments:0,transitions:0,replacements:0,max_bins_used:0,large:null};
function solve(nodes,edges,eps,root){
 let E=edges.length,adj=nodes.map(()=>[]);edges.forEach((e,i)=>{adj[e.a].push(i);adj[e.b].push(i)});
 let positives=[];for(let n of nodes)if(n.t==="A"&&cmp(n.base,one)>0)positives.push(sub(n.base,one));for(let e of edges)for(let o of e.opts)if(cmp(o.p,one)>0)positives.push(sub(o.p,one));
 let lo=positives.reduce((a,b)=>cmp(a,b)<=0?a:b,one),hi=Q(nodes.length),rho=add(one,mul(eps,Q(1,2*Math.max(1,E)))),bounds=[lo];
 while(cmp(bounds[bounds.length-1],hi)<=0)bounds.push(mul(bounds[bounds.length-1],rho));
 const bin=c=>{if(!c[0])return -1;let l=0,r=bounds.length;while(l+1<r){let m=(l+r)>>1;if(cmp(bounds[m],c)<=0)l=m;else r=m}return l};
 function dfs(v,parent){
  let n=nodes[v],kids=adj[v].filter(i=>i!==parent).map(i=>{let e=edges[i];return [i,dfs(e.a===v?e.b:e.a,i)]});
  let opts=parent<0?[null]:edges[parent].opts;
  let resource=(o)=>n.t==="A"?o.p:Q(o.k),combine=n.t==="A"?mul:add,base=n.t==="A"?n.base:Q(n.base);
  return opts.map((o,oi)=>{
   let init=o?combine(base,resource(o)):base;
   if(cmp(init,n.cap)>0)return null;
   let table=[{r:init,c:zero,w:o?[[parent,oi]]:[]}];
   for(let [i,msg] of kids){
    let next=new Map();
    for(let s of table)for(let j=0;j<msg.length;j++)if(msg[j]){
     stats.transitions++;let r=combine(s.r,resource(edges[i].opts[j]));if(cmp(r,n.cap)>0)continue;
     let c=add(s.c,msg[j].c),b=bin(c),old=next.get(b);
     if(!old||cmp(r,old.r)<0||(cmp(r,old.r)===0&&cmp(c,old.c)<0)){if(old)stats.replacements++;next.set(b,{r,c,w:s.w.concat(msg[j].w)})}
    }
    table=[...next.values()];stats.max_bins_used=Math.max(stats.max_bins_used,table.length);
   }
   let best=null;for(let s of table){let c=n.t==="A"?add(s.c,phi(s.r)):s.c;if(!best||cmp(c,best.c)<0)best={c,w:s.w}}return best;
  })
 }
 return dfs(root,-1)[0];
}
function evaluate(nodes,edges,w){
 let m=new Map(w),r=nodes.map(n=>n.t==="A"?n.base:Q(n.base));check(m.size===edges.length,"missing edges");
 edges.forEach((e,i)=>{let o=e.opts[m.get(i)];check(!!o,"invalid option");r[e.a]=add(r[e.a],Q(o.k));r[e.b]=mul(r[e.b],o.p)});
 if(r.some((x,i)=>cmp(x,nodes[i].cap)>0))return null;
 return r.reduce((s,x,i)=>nodes[i].t==="A"?add(s,phi(x)):s,zero)
}
function brute(nodes,edges){let best=null;function rec(i,w){if(i===edges.length){stats.brute_assignments++;let c=evaluate(nodes,edges,w);if(c&&(!best||cmp(c,best)<0))best=c;return}edges[i].opts.forEach((_,j)=>rec(i+1,w.concat([[i,j]])))}rec(0,[]);return best}
function gen(pairs,seed){
 let ns=1+Math.max(...pairs.map(p=>p[0])),na=1+Math.max(...pairs.map(p=>p[1])),degS=Array(ns).fill(0),degA=Array(na).fill(0);for(let [a,b] of pairs){degS[a]++;degA[b]++}
 let nodes=degS.map((d,i)=>({t:"S",base:seed%3===0?1:0,cap:Q(seed%7===0?d-1:d*(1+((seed+i)%3)))})).concat(degA.map((d,i)=>({t:"A",base:Q(64+(seed+i)%3,64),cap:Q(3,2)})));
 let edges=pairs.map(([a,b],i)=>({a,b:b+ns,opts:[0,1,2].map(j=>({k:4>>j,p:Q(128+((seed+i*3)%5+1)*(1<<j),128)}))}));
 return [nodes,edges]
}
const shapes=[[[0,0],[0,1],[0,2],[0,3]],[[0,0],[1,0],[2,0],[3,0]],[[0,0],[0,1],[1,1],[1,2],[2,2]],[[0,0],[0,1],[0,2],[1,0],[2,0],[2,3]]];
for(let pairs of shapes)for(let seed=0;seed<12;seed++){
 let [n,e]=gen(pairs,seed),opt=brute(n,e);stats.instances++;if(opt)stats.feasible++;else stats.infeasible++;
 for(let eps of [Q(1,4),Q(1,2)])for(let root of [0,n.length-1]){
 let got=solve(n,e,eps,root);check(!!opt===!!got,"feasibility mismatch");if(got){let c=evaluate(n,e,got.w);check(c&&cmp(c,got.c)===0,"witness mismatch");check(cmp(c,opt)>=0&&cmp(c,mul(add(one,eps),opt))<=0,"approximation mismatch")}
 }
}
let [n,e]=gen(Array.from({length:48},(_,i)=>[0,i]),2);let got=solve(n,e,Q(1,2),0);check(got&&cmp(evaluate(n,e,got.w),got.c)===0,"large witness");stats.large={edges:e.length,choices:"3^48",cost:got.c.map(String),verified:true};
return stats;
}
console.log(JSON.stringify(experiment()));
```

## Next

Extend to cyclic incidence graphs with a bounded separator of edge choices or a bounded feedback edge set; then handle actual retained shared-bundle propagation with local ceilings or multi-resource separator states. Native Port realizability and full joint-moment observer remain open. No external novelty claim or independent review.
