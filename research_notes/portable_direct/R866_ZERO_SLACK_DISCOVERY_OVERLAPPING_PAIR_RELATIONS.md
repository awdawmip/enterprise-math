# R866 — Complete zero-slack certificate discovery and overlapping pair-relation solver
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Predecessor: 88e6249c6eb4fe84dfc374c799f0b6c0013af9bc:research_notes/portable_direct/R865_BUDGET_CONDITIONED_SUPPORT_ZERO_SLACK.md. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: root p000_reality_foundation.json V5 and joint relation observer companion read; generated foundation startup returned 404; no repinning. Global V4 and ACTIVE worldview read; canonical global entries verified at 27b278a791bcec9b4e8cb41006e0a55991fa8ec6. Own RA-708BCC309CE076D8BB599B91 / EM-DIRECT-82A007 recovery metadata verified, execution_authorized=false. R865 original owner read succeeded (2026-11-28T10:23:39.291664Z empty RUNNING snapshot); R866 original r3-20261128-r866-running-read queued. Independent portable auxiliary integer-capacity research; no shared Task mutation.

## 1. Automatic discovery: complete zero-slack certificate for the continuous relaxation
Let finite nonempty indexed option lists E_i contain integer nonnegative resource vectors z, and integer upper budget h. The continuous option-mixture LP P uses variables t_iz>=0, sum_z t_iz=1 per group, sum_i,z t_iz z<=h. Assume P nonempty. Define m_i(lambda)=min_z lambda·z, Delta(lambda)=lambda·h-sum_i m_i(lambda), lambda>=0. All feasible mixtures give Delta>=0. R865 shows Delta=0 implies all positive-weight resources saturated and only local minimizing options used. We prove a converse simultaneously for ALL constraints and options that are universally tight/zero in P.

For every resource j universally tight in P, maximize -F_j over P. Its value is -h_j. The LP dual is min lambda·h+sum_i alpha_i subject to alpha_i+lambda·z>=-z_j, lambda>=0, alpha_i free. An optimal rational dual exists because the rational primal is nonempty bounded. Put mu=lambda+e_j. Each alpha_i>=-m_i(mu); hence 0>=Delta(mu)>=0 and mu_j>=1. Thus every universally tight resource has a zero-slack witness with positive weight.

For every indexed option (k,z0) with t_k,z0=0 throughout P, maximize t_k,z0. Value 0. The dual has alpha_i+lambda·z>=indicator[(i,z)=(k,z0)] with objective lambda·h+sum alpha_i=0. Since alpha_i>=-m_i(lambda), feasibility forces Delta(lambda)=0 and equality alpha_i=-m_i(lambda) individually. Consequently lambda·z0-m_k(lambda)>=1, so this option is excluded by the zero-slack face.

Sum these rational witnesses (use zero vector for empty list). For any two nonnegative weights, m_i(lambda+mu)>=m_i(lambda)+m_i(mu); Delta is subadditive and nonnegative on the feasible LP. Therefore sum of zero-slack witnesses is zero-slack. Moreover at any feasible mixture the R865 identity forces local minimization for each summand, so m_i(sum)=sum m_i(summands): choose any locally positive coefficient of that mixture to obtain equality. Hence every excluded option retains positive excess under the sum (all other summand excesses nonnegative). Every universally tight resource retains positive weight. Conversely the R865 identity proves that no non-forced resource or option is incorrectly classified. Clear denominators to obtain a nonnegative integer witness. This single certificate exposes the entire forced-zero option set and entire forced-tight resource set of P. It is not a certificate for all integer-only implications. If P empty, rational LP infeasibility gives a separating nonnegative weight with Delta<0: the compact Minkowski sum of local convex hulls plus the closed nonnegative orthant is closed convex, does not contain h, and a strict separating lower functional must be nonnegative on the orthant; rational Farkas yields a rational certificate.

Construction: solve at most r+N rational LPs after feasibility (N=sum |E_i|); test maximum deficit or individual option mass, retain exact dual witnesses, sum and clear denominators. Standard rational LP algorithms yield polynomial bit complexity in input size; independent certificate verification only needs O(Nr) integer arithmetic plus bit costs. No numerical LP output was used in this round; theorem is analytic. It covers overlapping resource incidence without assuming disjoint groups.

## 2. Exact overlapping pair-sum network
Extend R865's disjoint complement blocks: a graph G=(V,E) (undirected, parallel edges allowed, no self-loops needed) has each vertex i choosing x_i from a nonempty finite integer domain D_i, with additive cost c_i(x_i). Every edge uv has constraint x_u+x_v=t_uv. To realize as the previous upper-budget model, shift each domain to nonnegative, choose M_i>=max D_i and put contributions x_i and M_i-x_i into that edge's pair of resources with budgets t_uv and M_u+M_v-t_uv (shift t consistently). A negative budget immediately gives infeasibility; otherwise the all-ones weight has zero slack and forces the exact pair equations. Retain all edge relations and original option identities.

In a connected component pick root x. Traverse any spanning tree to express x_i=s_i x+b_i with s_i in {+1,-1}, b_i integers, root (1,0), child (−s_parent,t_edge−b_parent). Each remaining edge demands (s_u+s_v)x=t_uv-b_u-b_v. If coefficient zero, a nonzero RHS refutes feasibility. If coefficient ±2, it either fixes an integer root or refutes feasibility by odd RHS; inconsistent fixed values also refute. Thus candidate roots are either one fixed integer or intersection of the inverse affine domains. Enumerate the inverse domain of a vertex with minimum domain size, then test all vertex domains. Every surviving root gives exactly one complete value assignment, and every feasible assignment arises this way, by tree propagation and all edge tests. For each component count survivors, minimize sum of original costs over survivors; multiply counts and sum optima across disconnected components. Recover witnesses by the affine equations. For repeated indexed options at the same value, keep multiplicities and min-cost option/witness per value; multiply multiplicities within each root assignment and sum across roots for exact indexed-word count; full indexed language is the original domains and edge constraints. Do not merge different root values unless the declared observation permits it.

With hash maps and explicit domains, O(N+|V|+|E|+sum_C |C| min_{i in C}|D_i|) expected dictionary/arithmetic operations (fixed roots need one check), plus integer bit lengths and count arithmetic. Sorted maps yield deterministic logarithmic lookup factors. Input incidence expansion to resource vectors is sparse O(sum_i deg(i)|D_i|); not free when starting from dense input. This exact solver covers arbitrary cycle overlap and retains original witnesses and constraints, not just a constant terminal resource label. Under fixed budgets, the residual pair equations after any chosen prefix are obtained by substitution; retaining surviving root candidates or the fixed root preserves all remaining completions. Costs do not authorize deletion of nonoptimal feasible words from the relation representation.

## 3. Sharp continuous/integer gap on overlapping relations
Uniform domain {0,...,p−1}, p>=2 integer, t=p−1 on every edge. Every connected bipartite component admits p roots (alternate x and p−1−x). Every connected nonbipartite component forces x=(p−1)/2: one root when p odd, no root when p even. Isolated vertices are bipartite. For even p an odd cycle has a continuous feasible mixture: assign each vertex half mass on 0 and p−1 (or symmetric uniform), so all resource totals equal budget. Indeed the symmetric uniform choice gives strictly positive mass to EVERY indexed option; no zero-slack LP certificate can remove any such option. But the integer problem is infeasible. This locates a genuine parity obstruction beyond every R865 nonnegative zero-slack certificate, and the tree/edge residual detects it without high-rank global tables. For a connected 10000-vertex path with p=7, there are 7 feasible words among 7^10000 unrestricted words, with seven candidate root evaluations; individual domain/edge operations are linear in path size for fixed p. This is an auxiliary relational model, not a native BRC or Port correspondence.

## 4. Actual author computation
Exact safe-integer graph arithmetic and BigInt counts. Fixed seed; random graphs and domains with signed costs compared against full original word enumeration; cycles tested by analytic classification; 10000-vertex path uses analytic reference, not exhaustive enumeration. Assertions verify every returned original witness and cost. Results:
```json
{
  "random_graphs": 500,
  "brute_words": 463075,
  "feasible_graphs": 300,
  "graph_candidate_checks": 2640,
  "structured_cycles": 108,
  "structured_candidates": 288,
  "large_path_candidates": 7,
  "failures": 0
}
```
Reproduction: run the following JavaScript in an ordinary JS runtime. 
```javascript
function verify(){
let seed=8662026;const rng=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return(seed>>>8)%n};
const out={random_graphs:0,brute_words:0,feasible_graphs:0,graph_candidate_checks:0,structured_cycles:0,structured_candidates:0,large_path_candidates:0,failures:0};
const ck=x=>{if(!x)throw Error("assertion")};
function solve(D,E){
 const n=D.length,adj=Array.from({length:n},()=>[]),s=Array(n).fill(0),b=Array(n).fill(0),w=Array(n).fill(null);let count=1n,cost=0,candidates=0;
 for(const [u,v,t] of E){adj[u].push([v,t]);adj[v].push([u,t])}
 for(let root=0;root<n;root++){if(s[root])continue;s[root]=1;const Q=[root];let fixed=null,dead=false;
 for(let q=0;q<Q.length;q++){const u=Q[q];for(const[v,t]of adj[u]){if(!s[v]){s[v]=-s[u];b[v]=t-b[u];Q.push(v)}else{const a=s[u]+s[v],d=t-b[u]-b[v];if(a===0){if(d!==0)dead=true}else if(d%a!==0)dead=true;else{const z=d/a;if(fixed!==null&&fixed!==z)dead=true;fixed=z}}}}
 if(dead)return {count:0n,cost:null,w:null,candidates};
 const k=Q.reduce((u,v)=>D[u].size<=D[v].size?u:v);const X=fixed===null?[...D[k].keys()].map(x=>s[k]*(x-b[k])):[fixed];let local=0n,best=null,bestX=null;
 for(const x of X){candidates++;let val=0,ok=true;for(const u of Q){const a=s[u]*x+b[u];if(!D[u].has(a)){ok=false;break}val+=D[u].get(a)}if(ok){local++;if(best===null||val<best){best=val;bestX=x}}}
 if(!local)return{count:0n,cost:null,w:null,candidates};count*=local;cost+=best;for(const u of Q)w[u]=s[u]*bestX+b[u];
 }return{count,cost,w,candidates};
}
function brute(D,E){let count=0n,cost=null;const a=[];function go(i,c){if(i===D.length){out.brute_words++;if(E.every(([u,v,t])=>a[u]+a[v]===t)){count++;if(cost===null||c<cost)cost=c}return}for(const[x,y]of D[i]){a[i]=x;go(i+1,c+y)}}go(0,0);return{count,cost}}
function check(D,E,ref){const s=solve(D,E);ck(s.count===ref.count&&s.cost===ref.cost);if(s.count){ck(s.w.every((x,i)=>D[i].has(x)));ck(E.every(([u,v,t])=>s.w[u]+s.w[v]===t));ck(s.w.reduce((v,x,i)=>v+D[i].get(x),0)===s.cost)}return s}
for(let k=0;k<500;k++){const n=1+rng(7),D=Array.from({length:n},()=>{let a=new Map();for(let x=0;x<5;x++)if(rng(3))a.set(x,rng(15)-7);if(!a.size)a.set(rng(5),0);return a}),E=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)if(rng(4)===0)E.push([u,v,rng(9)]);const r=brute(D,E),s=check(D,E,r);out.random_graphs++;out.feasible_graphs+=Number(s.count>0n);out.graph_candidate_checks+=s.candidates}
for(const p of [2,3,4,5,7,8])for(let n=3;n<=20;n++){const D=Array.from({length:n},()=>new Map(Array.from({length:p},(_,x)=>[x,0]))),E=Array.from({length:n},(_,i)=>[i,(i+1)%n,p-1]);const count=BigInt(n%2===0?p:p%2===1?1:0);const s=check(D,E,{count,cost:count?0:null});out.structured_cycles++;out.structured_candidates+=s.candidates}
const n=10000,p=7,D=Array.from({length:n},()=>new Map(Array.from({length:p},(_,x)=>[x,x]))),E=Array.from({length:n-1},(_,i)=>[i,i+1,p-1]);const s=check(D,E,{count:7n,cost:30000});out.large_path_candidates=s.candidates;
return out
}
console.log(verify());
```

## 5. Next
Extend the affine residual solver to low positive slack (bounded defective edge set), and to general small separator tables for overlapping higher-arity relations. Investigate exact LP dual discovery implementation with rational verification and integer-only residual certificates. No general novelty claim against classical LP duality, graph propagation or constraint satisfaction; native BRC/Port transfer and independent review remain open.
