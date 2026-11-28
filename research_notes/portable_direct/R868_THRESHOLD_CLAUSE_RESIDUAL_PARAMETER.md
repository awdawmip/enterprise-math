# R868 — Threshold-clause residual parameterization and exact signed-profile solver
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Predecessor: f2261539af16f94cb47c4bf837f8e12b7a701d3e:research_notes/portable_direct/R867_BOUNDED_SLACK_AFFINE_FEEDBACK_SOLVER.md (full read). Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json V5 and joint observer companion read; generated startup path 404, no repin. Global P000 V4 and ACTIVE worldview read; current entry pair verified at 447638447e9d7fbb31a287710bae27dba3afd51d; current protocol/method/portable read at 754afa4ef9c5b2ff42d0af1e3ded4209e4d66905. Existing own RA-708BCC309CE076D8BB599B91 / EM-DIRECT-82A007 public session recovery metadata verified; no execution authority. R867 original RUNNING query SUCCEEDED, snapshot 2026-11-28T12:20:48.215347Z empty, Source changed before completion. Current r3-20261128-r868-running-read last observed WAITING_RESOURCE / SOURCE_LOCK_BUSY; no shared claim or task mutation. Independent auxiliary integer relation model, not a native BRC computation or physical attribution.

## 1. Exact ordered Boolean coordinate system
Use the R867 finite loopless undirected multigraph model, possibly disconnected: each vertex v has a nonempty explicit finite integer domain D_v={d_v0<...<d_vq}, one option per distinct value, arbitrary additive integer cost c_v. Edge e=uv has target t_e and signed residual eps_e=x_u+x_v-t_e. Budget K is a nonnegative integer, sum_e |eps_e|<=K. Duplicate indexed choices can be carried as multiplicities/cost lists per value for the profile solver, not silently collapsed. All integers including gaps are binary encoded.
For each vertex keep q Boolean threshold indicators Y_vj=[x_v>=d_vj], j=1..q, with hard implications Y_v,j+1 => Y_vj. Exactly the prefix-one strings are legal. They correspond bijectively to the original distinct values (including singleton domains); an arbitrary integer threshold [x_v>=h] is a constant or the indicator for the first domain value >=h. A hard true bit can represent constants. Thus no expansion proportional to the numeric range or gaps is needed. Original costs telescope: c_v(x_v)=c_v(d_v0)+sum_j (c_v(d_vj)-c_v(d_v,j-1))*Y_vj. Cost coefficients may be signed.

For edge e=uv write a=x_u and b=t_e-x_v. Sort the distinct union D_u union (t_e-D_v) as z_0<...<z_l. For j=1..l set w_j=z_j-z_(j-1)>0, P_j=[a>=z_j], Q_j=[b>=z_j]=NOT [x_v>=t_e-z_j+1]. Every threshold is a literal or constant. By telescoping, sum_j w_j P_j=a-z_0 and sum_j w_j Q_j=b-z_0. All nonzero P_j-Q_j have the same sign for a fixed a,b, so the two identities hold exactly:
 eps_e=sum_j w_j(P_j-Q_j), |eps_e|=sum_j w_j [P_j != Q_j].
The pair of 2-clauses (NOT P_j OR Q_j),(P_j OR NOT Q_j) violates exactly one iff P_j!=Q_j. Give each weight w_j. Retain edge and block labels and both original literals: the full signed defect and its magnitude recover exactly, not just the unsigned total. The original assignment, arbitrary domain restrictions, costs and all edge signs can be reconstructed. There is no generalization to native X6 or BRC until a matching map is proved.

## 2. K-only FPT feasibility and minimum slack up to K
Let C=sum_e (|D_u|+|D_v|-1), Q=sum_v (|D_v|-1). The weighted hard/soft 2-CNF uses Q+1 variables, O(Q+1) hard clauses and at most 2C soft clauses. Sort and merge the two domain lists for each edge in polynomial time in explicit input length; after sorting domains, merge costs O(sum_e(|D_u|+|D_v|)) arithmetic comparisons; lookup threshold literals by binary search or monotone scanning. Bit operations depend polynomially on original integer bit lengths. Keep original weights and signs for reconstruction. For decision alone replace soft weight w by min(w,K+1). For any assignment respecting hard clauses, truncating the TOTAL at K+1 gives exactly the same result before and after clipping, since a single clipped positive mismatch already exhausts the budget; other weights are unchanged. In particular the <=K predicate is exact. Replace each weight by that many clause occurrences, and each hard clause by K+1 copies. At most O((K+1)(Q+C+1)) clauses. A <=K-violations assignment cannot violate a hard clause. Conversely every original feasible assignment extends to a <=K-violations assignment. If a solver assumes distinct clauses, replace each occurrence (A OR B) by (A OR z),(NOT z OR B) with a fresh auxiliary z per occurrence (including units A=B); the minimum violations over z is exactly one if both A,B false and zero otherwise. Use these gadgets only for decision, not count bijection. Deleting <=K indexed clauses is equivalent to satisfying all but <=K clauses; recover an assignment by 2-SAT on the remaining formula.
Apply Igor Razgon and Barry O'Sullivan, Almost 2-SAT is fixed-parameter tractable, JCSS 75(8), 435-450 (2009), DOI 10.1016/j.jcss.2009.04.002, preprint https://arxiv.org/abs/0801.1300, author institution https://research.ucc.ie/en/publications/almost-2-sat-is-fixed-parameter-tractable/ (abstract verified 2026-11-28). Their O(15^K K M^3) bound for M clauses (use ordinary 2-SAT at K=0) supplies deterministic FPT in K alone: O(15^K max(1,K) ((K+1)(Q+C+1))^3), plus polynomial preprocessing, integer bit costs and witness recovery. No f=m-n+1 or treewidth in exponential parameter; explicit domains and integer slack are essential. This is a reduction to an existing theorem, not a claim to have implemented or improved the external solver. Recover and recheck signed defects and costs from decoded thresholds. Minimum achievable slack up to K follows by monotone binary search using O(log(K+2)) decision calls, or one decision algorithm with optimal deletion size. Arbitrary pins are hard clauses; finite-domain restrictions can instead rebuild the encoding. The result is for feasibility and one witness (and minimum slack), not FPT exact counting or minimum arbitrary unary cost under slack cap. The exact weighted formula represents those objectives without solving them.

## 3. Exact signed-profile partition and XP optimization/count
For each residual profile r in Z^m with sum |r_e|<=K, replace all targets by t_e+r_e. The residual profile is unique for any original assignment. The exact-target graph retains all original edges, including nonzero-defect edges, so the profile classes are disjoint and cover precisely all feasible assignments. Number of profiles:
 P(m,K)=sum_(j=0..min(m,K)) binom(m,j) 2^j binom(K,j).
Choose j nonzero edge identities, signs, and j positive magnitudes with sum<=K; the latter count is binom(K,j) by stars and bars (including j=0). Enumerate in increasing edge index with a remaining budget; every prefix is one complete profile with all later edges zero. For each profile reuse R866 strict affine propagation with modified targets, not merely delete defective edges. In each connected component, choose smallest domain root and propagate x_v=s_v r+b_v using the spanning tree. Off-tree residual closure equations (s_u+s_v)r=t_e+r_e-b_u-b_v either reject or force an integer root. Check root candidates against all original domains; calculate exact count and min additive cost with original witness. Across components multiply counts and add minima; across disjoint profiles sum counts and take the min. For repeated indexed values use per-value multiplicities and minimum indexed costs within each component, with original indexed identities retained. No global feedback-boundary enumeration required. With explicit domain dictionary lookups, time O(P(m,K)*(m+n+sum_components n_c min_v_in_c |D_v|)) arithmetic/dictionary operations, plus input and bit costs; profile generation overhead O(P(m,K)*poly(m,K)), and depth <=K. Memory polynomial in explicit input, graph and K, streaming profiles. This is XP in K, not FPT: P grows as m^K at fixed K. It supplies exact costs/counts and a separate practical route when K very small but feedback count large.

## 4. Structured check
For the complete bipartite graph K_{8,8}, binary domains, t=1, K=2, compare any assignment with one proper coloring; equal-adjacent edges are exactly the cut of the set of flipped bits. Every nontrivial cut of K_{8,8} has size >=8: with a,b flipped vertices on each side, cut=8(a+b)-2ab, minimize this affine expression in b at b=0 or 8 for 0<a<8, and handle a=0,8 directly. Thus only the two proper colorings meet budget, with cost sum x=8. Feedback count 49. R867 boundary exponent does not enter the profile bound. A separate example uses a 101-digit domain value 10^100 with a constant-size threshold formula. No FPT external solver run; the verification tests the reduction's exact Boolean language, signed residual, capped budget and arbitrary costs, plus independently brute-checks the implemented profile solver.

## 5. Actual computation
Fixed JS seed 8682026; BigInt integer arithmetic for targets, domains, costs, counts and weights; small mask indices exact. The code constructs weighted clauses, not the FPT library; each Boolean assignment is checked against hard constraints and compared to original-domain enumeration. Dense instance compared to analytic count and cost. Actual output:
```json
{
  "random": 240,
  "boolean_patterns": 11836,
  "legal_encodings": 2905,
  "signed_edge_checks": 9640,
  "profiles": 11267,
  "feasible_instances": 124,
  "failures": 0,
  "huge": {
    "count": "2",
    "best": "2",
    "vars": 4,
    "hard": 2,
    "weightedSoft": 4,
    "profiles": 3
  },
  "dense": {
    "vertices": 16,
    "edges": 64,
    "feedback": 49,
    "K": 2,
    "count": "2",
    "best": "8",
    "profiles": 8321,
    "expectedProfiles": 8321
  }
}
```
Reproduction:
```javascript
function encode(D,E,K) {
 const cmp=(a,b)=>a<b?-1:a>b?1:0, T=1;
 let nv=1; const hard=[[T,T]], soft=[], blocks=[];
 const vals=D.map(d=>[...d.keys()].sort(cmp));
 const ids=vals.map(a=>a.slice(1).map(()=>++nv));
 for(const a of ids)for(let j=1;j<a.length;j++)hard.push([-a[j],a[j-1]]);
 function ge(v,t){let a=vals[v],l=0,r=a.length;while(l<r){let mid=(l+r)>>1;if(a[mid]<t)l=mid+1;else r=mid;}return l===0?T:l===a.length?-T:ids[v][l-1];}
 const clip=w=>w>BigInt(K)+1n?BigInt(K)+1n:w;
 for(const [u,v,t] of E){
  const z=[...new Set([...vals[u],...vals[v].map(x=>t-x)])].sort(cmp), row=[];
  for(let j=1;j<z.length;j++){
   const w=z[j]-z[j-1], a=ge(u,z[j]), b=-ge(v,t-z[j]+1n);
   row.push([a,b,w]); soft.push([-a,b,clip(w)],[a,-b,clip(w)]);
  }
  blocks.push(row);
 }
 const decode=bits=>vals.map((a,v)=>a[ids[v].filter(i=>bits[i]).length]);
 const cost0=vals.reduce((s,a,v)=>s+D[v].get(a[0]),0n), objective=[];
 for(let v=0;v<vals.length;v++)for(let j=1;j<vals[v].length;j++)objective.push([ids[v][j-1],D[v].get(vals[v][j])-D[v].get(vals[v][j-1])]);
 return {nv,hard,soft,blocks,decode,cost0,objective};
}
function profilesSolve(D,E,K){
 let count=0n,best=null,witness=null,profiles=0;
 const n=D.length, m=E.length,adj=Array.from({length:n},()=>[]),res=Array(m).fill(0n);
 E.forEach(([u,v],i)=>{adj[u].push([v,i]);adj[v].push([u,i]);});
 const seen=new Set(), comps=[];
 for(let u=0;u<n;u++)if(!seen.has(u)){
  const q=[u];seen.add(u);
  for(let j=0;j<q.length;j++)for(const [v] of adj[q[j]])if(!seen.has(v)){seen.add(v);q.push(v);}
  const root=q.reduce((a,v)=>D[v].size<D[a].size?v:a,u);
  const order=[root],parents=new Map([[root,null]]);
  for(let j=0;j<order.length;j++)for(const [v,i] of adj[order[j]])if(!parents.has(v)){parents.set(v,[order[j],i]);order.push(v);}
  comps.push({root,order,parents,edges:[...new Set(q.flatMap(v=>adj[v].map(a=>a[1])))]});
 }
 function evaluate(){
  profiles++;
  let ways=1n,value=0n,w=Array(n);
  for(const {root,order,parents,edges} of comps){
   const s=[],b=[];s[root]=1n;b[root]=0n;
   for(const v of order.slice(1)){const [u,i]=parents.get(v);s[v]=-s[u];b[v]=E[i][2]+res[i]-b[u];}
   let forced=null;
   for(const i of edges){
    const [u,v,t]=E[i], a=s[u]+s[v],c=t+res[i]-b[u]-b[v];
    if(a===0n){if(c!==0n)return;}
    else {if(c%a!==0n)return;const r=c/a;if(forced!==null&&r!==forced)return;forced=r;}
   }
   let localCount=0n,localBest=null,localWitness=null;
   for(const r of (forced===null?D[root].keys():[forced])){
    let c=0n,ok=true,xs=[];
    for(const v of order){const x=s[v]*r+b[v];if(!D[v].has(x)){ok=false;break;}xs.push(x);c+=D[v].get(x);}
    if(ok){localCount++;if(localBest===null||c<localBest){localBest=c;localWitness=xs;}}
   }
   if(localCount===0n)return;
   ways*=localCount;value+=localBest;order.forEach((v,j)=>w[v]=localWitness[j]);
  }
  count+=ways;if(best===null||value<best){best=value;witness=w;}
 }
 function visit(start,left){evaluate();for(let i=start;i<m;i++)for(let a=1;a<=left;a++)for(const s of [-1n,1n]){res[i]=BigInt(a)*s;visit(i+1,left-a);res[i]=0n;}}
 visit(0,K);return {count,best,witness,profiles};
}
function verify(){
 let seed=8682026;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n;};
 const out={random:0,boolean_patterns:0,legal_encodings:0,signed_edge_checks:0,profiles:0,feasible_instances:0,failures:0};
 const ck=(a,msg)=>{if(!a)throw Error(msg);};
 const slack=(E,x)=>E.reduce((s,[u,v,t])=>{let z=x[u]+x[v]-t;return s+(z<0n?-z:z);},0n);
 const min=(a,b)=>a<b?a:b;
 function check(D,E,K){
  const f=encode(D,E,K),limit=BigInt(K)+1n;
  let bruteCount=0n,bruteBest=null,hardValid=0n,lang=new Set();
  for(let mask=0;mask<2**f.nv;mask++){
   out.boolean_patterns++;
   const bits=Array.from({length:f.nv+1},(_,j)=>j>0&&Boolean(mask&(1<<(j-1))));
   const lit=i=>i>0?bits[i]:!bits[-i];
   if(!f.hard.every(([a,b])=>lit(a)||lit(b)))continue;
   hardValid++;out.legal_encodings++;
   const x=f.decode(bits),key=x.join(",");ck(!lang.has(key),"non-injective");lang.add(key);
   ck(x.every((a,i)=>D[i].has(a)),"domain");
   const c=x.reduce((s,a,i)=>s+D[i].get(a),0n),obj=f.objective.reduce((s,[a,w])=>s+(lit(a)?w:0n),f.cost0);
   ck(c===obj,"objective");
   const cost=f.soft.reduce((s,[a,b,w])=>s+(!lit(a)&&!lit(b)?w:0n),0n);
   const orig=slack(E,x);ck(min(cost,limit)===min(orig,limit),"clipped slack");
   f.blocks.forEach((row,i)=>{const z=row.reduce((s,[a,b,w])=>s+w*(BigInt(lit(a))-BigInt(lit(b))),0n);const [u,v,t]=E[i];ck(z===x[u]+x[v]-t,"signed defect");out.signed_edge_checks++;});
   if(orig<=BigInt(K)){bruteCount++;if(bruteBest===null||c<bruteBest)bruteBest=c;}
  }
  ck(hardValid===D.reduce((s,d)=>s*BigInt(d.size),1n),"bijection size");
  const a=profilesSolve(D,E,K);
  ck(a.count===bruteCount&&a.best===bruteBest,"profiles vs encoding");
  // Independent original-domain enumeration.
  let count=0n,best=null;const x=[];
  function brute(i,c){if(i===D.length){if(slack(E,x)<=BigInt(K)){count++;if(best===null||c<best)best=c;}return;}for(const [z,w] of D[i]){x[i]=z;brute(i+1,c+w);}}
  brute(0,0n);ck(count===a.count&&best===a.best,"profiles vs original");
  if(a.witness){ck(slack(E,a.witness)<=BigInt(K),"witness slack");ck(a.witness.reduce((s,x,i)=>s+D[i].get(x),0n)===best,"witness cost");}
  out.profiles+=a.profiles;if(count)out.feasible_instances++;
  return {count:String(count),best:best===null?null:String(best),vars:f.nv,hard:f.hard.length,weightedSoft:f.soft.length,profiles:a.profiles};
 }
 for(let i=0;i<240;i++){
  const n=1+rnd(5),K=rnd(4),D=Array.from({length:n},()=>{const d=new Map(),q=1+rnd(3);while(d.size<q)d.set(BigInt(rnd(11)-5),BigInt(rnd(15)-7));return d;});
  const E=[],x=D.map(d=>[...d.keys()][rnd(d.size)]);
  if(n>1)for(let j=0,m=rnd(8);j<m;j++){let u=rnd(n),v=rnd(n-1);if(v>=u)v++;E.push([u,v,i%2?x[u]+x[v]+BigInt(rnd(3)-1):BigInt(rnd(11)-5)]);}
  check(D,E,K);out.random++;
 }
 const M=10n**100n;
 out.huge=check([new Map([[-M,4n],[0n,0n],[M,2n]]),new Map([[-M,0n],[M,1n]])],[[0,1,0n]],1);
 const p=8,D=Array.from({length:2*p},()=>new Map([[0n,0n],[1n,1n]])),E=[];
 for(let u=0;u<p;u++)for(let v=p;v<2*p;v++)E.push([u,v,1n]);
 const a=profilesSolve(D,E,2);
 ck(a.count===2n&&a.best===BigInt(p),"dense analytical");
 ck(a.witness&&slack(E,a.witness)===0n,"dense witness");
 out.dense={vertices:2*p,edges:E.length,feedback:E.length-2*p+1,K:2,count:String(a.count),best:String(a.best),profiles:a.profiles,expectedProfiles:1+4*E.length+4*E.length*(E.length-1)/2};
 ck(out.dense.profiles===out.dense.expectedProfiles,"profile formula");
 return out;
}
console.log(JSON.stringify(verify(),null,2));
```

## 6. Next
K-only FPT feasibility is established using an external theorem; implement the actual Almost-2-SAT engine and end-to-end witness recovery when useful. Main mathematical gap is K-only FPT for exact counting or arbitrary unary-cost optimum under the cap. Explore whether the residual-profile partition admits a cut-based implicit weighted counting/optimization computation; distinguish fixed-parameter lower bounds from explicit profile enumeration and from the decision theorem. Keep native BRC/Port transfer open and separate.
