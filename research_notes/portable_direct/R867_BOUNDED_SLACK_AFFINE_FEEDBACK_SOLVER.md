# R867 — Bounded-slack signed affine observer and feedback-edge exact solver
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Predecessor: 144e22c24e8d6b51fc1264200455c5b42b496c48:research_notes/portable_direct/R866_ZERO_SLACK_DISCOVERY_OVERLAPPING_PAIR_RELATIONS.md (full relevant argument read). Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: root P000 V5 and joint observer companion read. Global P000 V4, ACTIVE worldview and current entries verified at 98d2710cde6202b573ff1f4a2045199458f7f89b; current portable and method rules read at 1938b6decf70be6c66bb003fe6297c020b393ec9. Existing RA-708BCC309CE076D8BB599B91 / EM-DIRECT-82A007 own session recovery metadata verified, execution_authorized=false. R866 original RUNNING read succeeded (2026-11-28T11:24:01.172431Z empty snapshot, Source changed before completion). R867 fresh owner read r3-20261128-r867-running-read queued at initiation. Independent auxiliary research, no claim or shared task mutation.

## 1. Signed affine residual coordinates with global integer slack
Let G be a connected finite undirected loopless multigraph; vertex v has a nonempty finite integer domain D_v and additive integer cost c_v(x). Each edge e=uv has integer target t_e; its signed defect is epsilon_e=x_u+x_v-t_e. Require total L1 slack sum_e |epsilon_e| <= K for a nonnegative integer K. Retain indexed option provenance; the algorithm below treats one option per value; repeated values may use multiplicities and per-value minimum cost/witness as R866, without deleting the original indexed language.
Select any spanning tree T and root o. Define s_o=1,b_o=0, s_v=-s_u,b_v=t_uv-b_u along tree edges. For a fixed root value r=x_o introduce y_v=s_v(x_v-b_v)-r, hence x_v=s_v(r+y_v)+b_v, y_o=0. For tree parent u and child v, epsilon_uv=s_u(y_u-y_v). Thus |y_v| <= sum along root path |epsilon_e| <= K, so every feasible assignment lies in the exact finite local window -K..K. Conversely any y assignment in this window whose x are in their domains and whose full edge slack meets K decodes uniquely to a feasible assignment. Off-tree edges have exact residual epsilon_uv=(s_u+s_v)r+b_u+b_v-t_uv+s_u y_u+s_v y_v. This is a bijection, not a marginal projection. All edge residual signs, costs and original value identities are recovered; arbitrary partial assignments are handled by restricting the corresponding domains and repeating the exact computation. No native BRC/Port correspondence asserted.
For a connected bipartite graph, a tree anchor can be chosen at a smallest-domain vertex, yielding at most min_v |D_v| root candidates. This root bound holds also in a nonbipartite graph. Additionally any odd cycle v0..v_(2l),v0 yields 2x_v0 = alternating sum of edge targets plus alternating sum of edge defects (start plus at first edge, end plus). Each edge occurs once; consequently |2x_v0-T_cycle|<=K. The integer interval contains at most K+1 integers, independently of raw domain magnitude. Choose an anchor on an odd cycle if this bound is preferable. A spanning tree plus a same-sign off-tree edge gives an odd fundamental cycle; reroot the same tree at one endpoint. Then |(s_u+s_v)r+b_u+b_v-t_uv|<=K for that edge: exactly the cycle inequality, not the weaker bound obtained when rooting outside the cycle. Candidate roots can be found by interval/domain intersection using sorted lists, or by scanning the explicit domain as in the reference script. Full preprocessing accounts for reading the input. This gives at most min(min_v |D_v|,K+1) root candidates in a nonbipartite component with the stated anchor choice.

## 2. Exact bounded-slack tree dynamic programming and feedback-edge conditioning
Let f=|E|-|V|+1; let H be the endpoints of the f off-tree edges except the root. For each fixed r enumerate only the permitted y values of H (at most (2K+1)^|H|; |H|<=2f). Each assignment to H fixes all off-tree defects and their total absolute cost B. Reject B>K; run tree DP with cap K-B and H fixed. At a vertex u define A_u(y,k) = count and minimal additive cost among assignments of its rooted subtree with fixed y_u=y and total internal tree slack exactly k, excluding the edge to its parent. Initialize at each admissible local y with count 1 and cost c_u(x_u), k=0. Merge one child v: combine (y,k) and (z,l) into (y,k+l+|y-z|), multiplying counts, adding costs and retaining one min-cost witness; sum counts and minimize costs across alternatives. Cap at K-B. Induction by independent child subtrees proves correctness. At root y=0 sum counts and minimize over k<=K-B. Enumerated roots and H profiles partition all original assignments; hence no double counting. Off-tree edges are checked exactly once, and all tree edge defects are checked exactly once. Counts use arbitrary precision integers; costs may be negative. Store backpointers for one optimal assignment; the original domains and relation constraints, together with the recurrence, preserve the complete feasible language, not only the optimum.
Write L=2K+1, R=number of root candidates. With dictionary lookups, constructing windows takes O(n L) operations per root after O(sum |D_v|+n+m) input processing. At most O(R L^|H| [m+n L^2 (K+1)^2]) arithmetic/dictionary operations, with integer bit costs separate. For trees f=0, this is polynomial in n,K and R, independent of the full product of domain sizes. Sorted lookups add logarithmic factors; boundary profiles can be streamed. A tree DP uses O(n L(K+1)) records including backpointers; the reference script retains persistent merge nodes and counts, not full assignments per record. Counts can have O(sum log |D_v|) bits. Disconnected components can be combined by exact budget convolution; treating each independently with the full K without convolution would be incorrect.
More generally given a tree decomposition of G of width w, standard variable/edge-introduction and forget/join recurrences with one bag assignment and a slack index k use O(R * (number of nice bags) * L^(w+1)*(K+1)^2) arithmetic operations (allow polynomial bag bookkeeping; each edge assigned exactly once, each vertex cost counted at its unique forget or designated node). At joins agree on the same bag and split slack; count multiplication and min-plus convolution apply. This is a conditional bound given the decomposition, not a claimed decomposition algorithm. For unbounded width and arbitrary K, binary domains {0,1} with t=1 reduce minimum slack exactly to |E|-MaxCut(G); thus the original general optimization includes MaxCut. This does not rule out an algorithm parameterized by K alone.

## 3. Exact structured check
For binary path n vertices, t=1, a root bit and the set of equal-adjacent edges uniquely determine all values. There are exactly 2*sum_{j=0}^{min(K,n-1)} binom(n-1,j) feasible assignments. At n=1000,K=2, costs c_v(x)=x, optimum 499: splitting into at most three alternating blocks gives at most two more zeros than ones since n is even (each block imbalance at most one, total even). Attain with two odd blocks favoring zero, e.g. lengths 1 and 999 joined by a 00 edge. The recurrence checks both count and optimum. This is an auxiliary signed-residual model and no physical interpretation or BRC native attribution is claimed.

## 4. Actual exact computation
JavaScript fixed seed 8672026, safe small integer costs/defects and BigInt exact counts. Random connected signed-domain graphs with 0–3 added edges, cycles, signed costs, budgets 0–4, full original assignment enumeration against the solver. Large path checked against analytic count/optimum; no full enumeration. The tree-decomposition extension is analytic only. Results:
```json
{
  "random": 450,
  "brute": 417493,
  "feasible": 197,
  "root_candidates": 998,
  "boundary_profiles": 3756,
  "joins": 16705,
  "odd_cases": 27,
  "structured": 54,
  "failures": 0,
  "large": {
    "n": 1000,
    "K": 2,
    "count": "999002",
    "best": 499,
    "roots": 2,
    "profiles": 2,
    "joins": 23940
  }
}
```
Reproduction (ordinary JS runtime):
```javascript
function solve(D,E,K) {
 const n=D.length,adj=Array.from({length:n},()=>[]), tree=new Set(), q=[0], seen=new Set(q), sign0=[1];
 for(let i=0;i<E.length;i++){const [u,v,t]=E[i];adj[u].push([v,t,i]);adj[v].push([u,t,i]);}
 for(let k=0;k<q.length;k++)for(const [v,t,i] of adj[q[k]])if(!seen.has(v)){seen.add(v);q.push(v);tree.add(i);sign0[v]=-sign0[q[k]];}
 if(q.length!==n)throw Error("connected required");
 const extra=E.filter((e,i)=>!tree.has(i)), odd=extra.find(([u,v])=>sign0[u]===sign0[v]);
 let root=D.reduce((a,d,i)=>d.size<D[a].size?i:a,0);
 if(odd && K+1<D[root].size)root=odd[0];
 const s=[],b=[],children=Array.from({length:n},()=>[]),order=[root];s[root]=1;b[root]=0;
 for(let k=0;k<order.length;k++){let u=order[k];for(const [v,t,i] of adj[u])if(tree.has(i)&&s[v]===undefined){s[v]=-s[u];b[v]=t-b[u];children[u].push(v);order.push(v);}}
 const filter=odd&&root===odd[0]?odd:null;
 let total=0n,best=Infinity,witness=null,roots=0,profiles=0,joins=0;
 const boundary=[...new Set(extra.flatMap(([u,v])=>[u,v]))].filter(v=>v!==root);
 for(const r of D[root].keys()){
  if(filter){const [u,v,t]=filter;if(Math.abs((s[u]+s[v])*r+b[u]+b[v]-t)>K)continue;}
  roots++;
  const vals=D.map((d,v)=>{let a=[];for(let y=-K;y<=K;y++){if(v===root&&y!==0)continue;const x=s[v]*(r+y)+b[v];if(d.has(x))a.push([y,x,d.get(x)]);}return a;});
  if(vals.some(a=>!a.length))continue;
  const fixed=new Map();
  function evaluate(){
   profiles++;
   const y=v=>v===root?0:fixed.get(v);
   let extraCost=0;
   for(const [u,v,t] of extra)extraCost+=Math.abs(s[u]*(r+y(u))+b[u]+s[v]*(r+y(v))+b[v]-t);
   const cap=K-extraCost;if(cap<0)return;
   const tables=[];
   function add(map,k,count,cost,node){const old=map.get(k);if(old){old.count+=count;if(cost<old.cost){old.cost=cost;old.node=node;}}else map.set(k,{count,cost,node});}
   for(let i=order.length-1;i>=0;i--){
    const u=order[i], tab=new Map();
    for(const [yu,x,cost] of vals[u]) {
     if(fixed.has(u)&&fixed.get(u)!==yu)continue;
     let a=new Map([[0,{count:1n,cost,node:{u,x,parts:null}}]]);
     for(const v of children[u]){
      const next=new Map();
      for(const [yv,child] of tables[v]){
       const edge=Math.abs(yu-yv);
       for(const [k,A] of a)for(const [l,B] of child){joins++;if(k+l+edge<=cap)add(next,k+l+edge,A.count*B.count,A.cost+B.cost,{left:A.node,right:B.node});}
      }
      a=next;if(!a.size)break;
     }
     if(a.size)tab.set(yu,a);
    }
    tables[u]=tab;
   }
   for(const A of (tables[root].get(0)||new Map()).values()){
    total+=A.count;
    if(A.cost<best){best=A.cost;witness=Array(n);const stack=[A.node];while(stack.length){const w=stack.pop();if(w.u!==undefined)witness[w.u]=w.x;else stack.push(w.left,w.right);}}
   }
  }
  function enumerate(i){if(i===boundary.length){evaluate();return;}const v=boundary[i];for(const [y] of vals[v]){fixed.set(v,y);enumerate(i+1);}fixed.delete(v);}
  enumerate(0);
 }
 return {total,best,witness,roots,profiles,joins};
}
function verify(){
 let seed=8672026;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n;};
 const out={random:0,brute:0,feasible:0,root_candidates:0,boundary_profiles:0,joins:0,odd_cases:0,structured:0,failures:0};
 function ck(x){if(!x)throw Error("assertion");}
 function check(D,E,K){
  const a=solve(D,E,K);let count=0n,best=Infinity;const w=[];
  function visit(i,c){if(i===D.length){out.brute++;if(E.reduce((z,[u,v,t])=>z+Math.abs(w[u]+w[v]-t),0)<=K){count++;best=Math.min(best,c);}return;}for(const [x,cost] of D[i]){w[i]=x;visit(i+1,c+cost);}}
  visit(0,0);ck(count===a.total&&best===a.best);
  if(a.witness){ck(a.witness.every((x,i)=>D[i].has(x)));ck(E.reduce((z,[u,v,t])=>z+Math.abs(a.witness[u]+a.witness[v]-t),0)<=K);ck(a.witness.reduce((z,x,i)=>z+D[i].get(x),0)===best);}
  if(count)out.feasible++;out.root_candidates+=a.roots;out.boundary_profiles+=a.profiles;out.joins+=a.joins;
 }
 for(let t=0;t<450;t++){
  const n=2+rnd(6),K=rnd(5),D=Array.from({length:n},()=>{const d=new Map();while(d.size<2+rnd(3))d.set(rnd(7)-3,rnd(17)-8);return d;});
  const planted=D.map(d=>[...d.keys()][rnd(d.size)]);
  const E=[];for(let i=1;i<n;i++){const j=rnd(i);E.push([j,i,t%2?planted[j]+planted[i]+rnd(3)-1:rnd(9)-4]);}
  for(let i=0,m=rnd(4);i<m;i++){let u=rnd(n),v=rnd(n-1);if(v>=u)v++;E.push([u,v,t%2?planted[u]+planted[v]+rnd(3)-1:rnd(9)-4]);}
  check(D,E,K);out.random++;
 }
 for(let n=3;n<=8;n++)for(let p=2;p<=4;p++)for(let K=0;K<=2;K++){
  const D=Array.from({length:n},()=>new Map(Array.from({length:p},(_,i)=>[i,0])));
  const E=Array.from({length:n},(_,i)=>[i,(i+1)%n,p-1]);check(D,E,K);out.structured++;if(n%2)out.odd_cases++;
 }
 // Binary path: total slack counts adjacent equal bits; choose defect positions.
 const n=1000,K=2,D=Array.from({length:n},()=>new Map([[0,0],[1,1]])),E=Array.from({length:n-1},(_,i)=>[i,i+1,1]);
 const a=solve(D,E,K),N=BigInt(n-1),expected=2n*(1n+N+N*(N-1n)/2n);
 ck(a.total===expected&&a.best===499);ck(a.witness.reduce((z,x)=>z+x,0)===a.best);ck(E.reduce((z,[u,v,t])=>z+Math.abs(a.witness[u]+a.witness[v]-t),0)<=K);
 out.large={n,K,count:String(a.total),best:a.best,roots:a.roots,profiles:a.profiles,joins:a.joins};
 return out;
}
console.log(JSON.stringify(verify(),null,2));

```

## 5. Next
Study K-only tractability without bounded feedback-edge count/width: low slack permits at most K nonzero edges. Investigate whether deletion of these edges followed by R866 affine propagation and exact residual repair admits a bounded branching or cut-based algorithm; preserve signed cycle syndromes and root-domain intersections. Distinguish any parameterized lower bounds from representation-specific state bounds. Native BRC/Port transfer remains open. No formal Result, review, Task claim or admission.
