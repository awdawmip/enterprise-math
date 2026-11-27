# EC49GBY — Cut-network boundary carrier and exact sparse-prefix budget DP

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRUTE_REPLAY / NOT_REVIEWED.
Predecessor: 80231aca033f53fffaa69d60ac1e290f0947c1fc:research_notes/portable_direct/EC49GBX_BOUNDED_DEFICIT_BOUNDARY_SIGNATURE.md (blob e668872ac8ffdbf95c95fcbceedf43fee2396edf, read this turn). Frozen BRC16943 inherited unchanged; raw archive not replayed. Auxiliary finite labeled strict-Hall combinatorial model, not a native physical simulation.

## 1. Polynomial-size cut-network carrier with d unit-arc updates

Let C be ports of positive integer capacities c_i, A a prefix of labeled nonempty neighborhoods E_x, S independent in the strict-Hall sense f_S(V)<=c(V)-1 for every nonempty V. As in GBX choose any basis J of A extending S, write Z=J\S, d=|Z|. Fix an ordinary full capacity matching a:J->C, a(x) in E_x, load_i<=c_i (exists by Hall, implied by strict Hall). Let B be the permitted future boundary. For nonempty U subset B put q_S(U)=min_{V superset U}(c(V)-1-f_S(V)).

Construct a directed network with ports, one vertex per label of J, and sink t. Port i -> t has capacity c_i-load_i. For every x in J add a(x)->x of capacity 1, and x->i of capacity M for every i in E_x, where M=1+sum c_i. For each x in Z add one arc x->t of capacity 1. Attach source s to every i in U by capacity M. Then

  q_S(U)+1 = mincut(s,t).

Proof: the all-ports, all-labels source side is a cut of capacity sum c_i-|J|+d <= sum c_i, so no minimum cut crosses a capacity-M arc. For any port source side V containing U, optimize label sides individually. If a(x) is outside V, placing x outside costs zero. If a(x) is inside V but E_x not contained in V, x must be outside, costing one. If E_x contained in V, keeping x inside costs zero for x in J\Z and one for x in Z; outside costs one. Summing the minimum contribution over labels and the free-port arcs gives c(V)-f_J(V)+f_Z(V)=c(V)-f_S(V). Minimizing over V proves the identity. The graph has |C|+|J|+2 vertices and at most |C|+|J|+sum_{x in J}|E_x|+d+|U| arcs (zero arcs may be omitted), with binary-encoded capacities. Thus a polynomial-size generative carrier for the full GBX signature exists, with exactly d extra unit arcs relative to an extending basis network. Matching construction can use ordinary capacity-level augmentations, query uses integer max-flow; no expansion of capacity slots or all boundary subsets is needed for a single q query. Different S may require different extending J and matching; this is not a common d-bit encoding, not a bound on observer-distinct states, and not a polynomial-time equality test between two carriers.

### Single-deletion certificate
Let d=1 with deleted label z. In the basis network (before adding z->t), let K_U be the inclusion-minimal source side of a minimum cut. Then
  q_S(U)-q_A(U) = 1 iff z in K_U; otherwise 0.
Indeed integer mincut changes by at most one; if some old minimum cut excludes z, it is unchanged. If all old minima include z, each gains one and every other cut already costs at least one more. The intersection of minimum source sides is the minimal minimum source side, given by reachability from s in any maximum-flow residual graph. This gives an exact deficit-one query without recomputing perturbed flow after the reference flow is found. For general Z the change is min over cuts of (old cut excess + number of Z vertices on source side); cuts of excess >d cannot improve the minimum. This makes explicit why the scalar d does not identify the retained relations.

## 2. Canonical sparse envelope and its update

For any monotone q=q_S on nonempty subsets of B define P(q)={(W,q(W)): q(W)<q(T) for every strict superset T in B}. Then q(U)=min_{(W,v) in P(q), W superset U} v. This follows by following a chain of equal values to a maximal set. More generally among weighted masks, remove any (W,v) having a strict superset with value <=v, and merge duplicates by min. The resulting envelope is canonical for q. Proof: each strict record W of q must be present with value q(W), since no strict superset can realize that value; the others are dominated by a larger record. Each strict record is independently necessary for the fixed mask inequality representation f_T(W)<=q(W): take q(W)+1 fresh identical labels with neighborhood W. Proper subsets do not count them, strict supersets have integer q>=q(W)+1, so only the omitted inequality rejects them. Scope is arbitrary fresh labeled suffix targets, not prefix deletion, and the minimality is for fixed-mask inequalities, not arbitrary encodings (section 1 is a counterexample to a universal exponential representation lower bound).

Update and shrink in a single operation: for insertion of a feasible label E (or E=empty sentinel for skip), and new boundary B' subset B, form records
  (W intersect B', v - 1_{E nonempty and E subset W})
for every old (W,v), discard empty masks, merge duplicates by min, and remove dominated records. The result is exactly P(q_new restricted B'). Proof: GBX update is the min over old supersets with the indicator subtraction, since if E subset W then every dominating superset also contains E. Hence omitted coordinates never become necessary on insertion. Restricting queries to B' replaces W by its intersection without changing which queried subsets it contains. Taking minima then pruning proves the assertion. This is GBO's dominance principle specialized to the GBX boundary observer, with exact shrinking. Naive implementation costs O(p^2) subset comparisons for p records and O(p) mask updates; query costs O(p). It may cost more than dense bitmask transforms. Worst case p=2^b-1 (empty prefix, all capacities 1), so no general sparse-size guarantee.

Additionally h(U)=q(U)+1 for U nonempty and h(empty)=0 is a monotone submodular function: the cut graph proves this by taking union/intersection of optimal source sides (include source, exclude sink), using cut submodularity. Source constraints may be expressed as forced port inclusion in a common graph. This gives equal-value closure: if h(U)=h(U union V)=h(U union W), then h(U union V union W)=h(U), by submodularity and monotonicity. Maximal equal-value extensions are unique; the sparse records are precisely closed nonempty subsets. No claim that their number is small.

## 3. Exact budget DP implementation and proof scope

Reuse GBW prefix gap g_j and rank r(A_j), and GBX signature states. Auxiliary capacity labels are retained or excluded (exclusion incurs release cost), actual target inclusion earns value, both types enter the same strict-Hall constraint at maximum capacity. All costs and rewards nonnegative integers in the experiment. Sort by score v_x or lambda*a_e (lambda positive integer in replay). Compute greedy Lagrangian upper U and a feasible baseline L by first including all dummy labels and greedily adding real targets. Each state stores canonical sparse envelope, selected count, accumulated cost, maximum reward; suffix boundary is union of neighborhoods of unprocessed labels. Include iff q(E)>=1; update as section 2, or skip; discard over-budget and g_j*(r(A_j)-count)>U-L. The latter cannot discard any solution at least as good as L, by GBW. Merge equal envelope/count/cost by maximum reward; future feasibility and objective increments agree by GBX. End returns max of L and all surviving terminal rewards. The same algorithm with dense signatures is an independent representation comparator; exhaustive subsets with direct strict Hall are the independent reference. This proves exactness for any finite input satisfying hypotheses; integer budget and state-space dependence remain. The test stores values only, not witness backpointers; these can be added, but not tested. Cross-state dominance and end-to-end speed not claimed.

## 4. Actual replay

Executed deterministic JS in tool runtime, xorshift32 seed 20261128. 300 synthetic instances: 1..5 ports, base capacities 1..3, per-port maximum increment 0 or 1, 1..7 actual labels, dummy costs 1..5, rewards 1..9, lambda 1..3. Enumerate all label subsets for the reference and all integer budgets from 0 to total dummy cost. For each model also verify every nonempty port query against an actual Edmonds-Karp integer max-flow on the cut carrier for random deleted subset of a greedy basis; test single-deletion mincut reachability when basis nonempty. Dense and sparse DP use identical prune rule and merge keys except representation. Counts below include retained states after each processed label for each budget; coordinate entries exclude key overhead, reference construction and computation; not memory bytes or runtime comparison.

Result:
```json
{"seed":20261128,"models":300,"bruteSubsets":36884,"budgets":1619,"flowQueries":3184,"singleDeletionQueries":3172,"sparseCoordinateChecks":3184,"dpDenseStates":93506,"dpSparseStates":93506,"denseEntries":967576,"sparseEntries":888115,"prunedTransitions":10375,"disagreements":0}
```

Executed standalone JavaScript:
```javascript
function replay(){
 let z=20261128;const rnd=n=>{z^=z<<13;z^=z>>>17;z^=z<<5;return (z>>>0)%n};
 const stats={seed:20261128,models:0,bruteSubsets:0,budgets:0,flowQueries:0,singleDeletionQueries:0,sparseCoordinateChecks:0,dpDenseStates:0,dpSparseStates:0,denseEntries:0,sparseEntries:0,prunedTransitions:0,disagreements:0};
 const assert=(a,m)=>{if(!a){stats.disagreements++;throw Error(m)}};
 const masks=b=>{let a=[];for(let u=b;u;u=(u-1)&b)a.push(u);return a.sort((x,y)=>x-y)};
 const subset=(a,b)=>(a&b)===a;
 function capsums(c){return Array.from({length:1<<c.length},(_,u)=>c.reduce((s,v,i)=>s+((u>>i)&1)*v,0))}
 function ok(c,S){for(let u=1;u<c.length;u++)if(S.filter(x=>subset(x.e,u)).length>=c[u])return false;return true}
 function sig(c,S,B){return masks(B).map(u=>[u,Math.min(...masks(c.length-1).filter(v=>subset(u,v)).map(v=>c[v]-1-S.filter(x=>subset(x.e,v)).length))])}
 function prune(a){let m=new Map();for(const [u,v] of a)if(u)m.set(u,Math.min(m.get(u)??Infinity,v));let t=[...m].sort((a,b)=>a[0]-b[0]);return t.filter(([u,v])=>!t.some(([w,h])=>w!==u&&subset(u,w)&&h<=v))}
 const query=(a,u)=>Math.min(...a.filter(([w])=>subset(u,w)).map(([,v])=>v));
 function sparseStep(a,e,B){return prune(a.map(([u,v])=>[u&B,v-(e&&subset(e,u)?1:0)]))}
 function denseStep(a,e,B){let m=new Map(a);return masks(B).map(u=>[u,e?Math.min(m.get(u),m.get(u|e)-1):m.get(u)])}
 function greedy(c,A){let J=[];for(let x of A)if(ok(c,[...J,x]))J.push(x);return J}
 function assign(c,J){let a=[],load=c.map(()=>0);function f(j){if(j===J.length)return true;for(let i=0;i<c.length;i++)if((J[j].e&(1<<i))&&load[i]<c[i]){load[i]++;a[j]=i;if(f(j+1))return true;load[i]--}return false}assert(f(0),"matching");return a}
 function flow(c,J,a,removed,U){let n=c.length,t=n+J.length,s=t+1,N=s+1,g=Array.from({length:N},()=>Array(N).fill(0)),inf=c.reduce((x,y)=>x+y,0)+1,load=c.map(()=>0);
 for(let j=0;j<J.length;j++){load[a[j]]++;g[a[j]][n+j]=1;for(let i=0;i<n;i++)if(J[j].e&(1<<i))g[n+j][i]=inf;if(removed.has(j))g[n+j][t]=1}
 for(let i=0;i<n;i++){g[i][t]=c[i]-load[i];if(U&(1<<i))g[s][i]=inf}
 let val=0;
 while(true){let p=Array(N).fill(-1),Q=[s];p[s]=s;for(let k=0;k<Q.length;k++)for(let j=0;j<N;j++)if(p[j]<0&&g[Q[k]][j]>0){p[j]=Q[k];Q.push(j)}
 if(p[t]<0)return [val,new Set(Q)];let f=inf;for(let j=t;j!==s;j=p[j])f=Math.min(f,g[p[j]][j]);for(let j=t;j!==s;j=p[j]){g[p[j]][j]-=f;g[j][p[j]]+=f}val+=f}
 }
 function dp(c,A,Budget,lambda,L,upper,sparse){
 let r=0,J=[],boundaries=Array(A.length+1).fill(0);for(let i=A.length-1;i>=0;i--)boundaries[i]=boundaries[i+1]|A[i].e;
 let a=sig(c,[],boundaries[0]);if(sparse)a=prune(a);
 let states=new Map([["initial",{a,k:0,cost:0,p:0}]]);let gap=upper-L;
 for(let j=0;j<A.length;j++){let x=A[j];if(ok(c,[...J,x]))J.push(x);r=J.length;let g=x.score-(A[j+1]?.score??0),next=new Map();
 for(let v of states.values())for(let take=0;take<=1;take++){if(take&&query(v.a,x.e)<1)continue;let k=v.k+take,cost=v.cost+(!take&&x.d?x.w:0),p=v.p+(take&&!x.d?x.w:0);if(cost>Budget||g*(r-k)>gap){if(sparse)stats.prunedTransitions++;continue}
 let q=sparse?sparseStep(v.a,take?x.e:0,boundaries[j+1]):denseStep(v.a,take?x.e:0,boundaries[j+1]);let key=JSON.stringify([k,cost,q]),old=next.get(key);if(!old||old.p<p)next.set(key,{a:q,k,cost,p})}
 states=next;for(let v of states.values()){if(sparse){stats.dpSparseStates++;stats.sparseEntries+=v.a.length}else{stats.dpDenseStates++;stats.denseEntries+=v.a.length}}
 }
 return Math.max(L,...[...states.values()].map(v=>v.p))
 }
 for(let it=0;it<300;it++){
 let n=1+rnd(5),N=1<<n,base=Array.from({length:n},()=>1+rnd(3)),h=Array.from({length:n},()=>rnd(2)),caps=base.map((x,i)=>x+h[i]),c=capsums(caps),D=[],X=[];
 for(let i=0;i<n;i++)if(h[i])D.push({e:1<<i,d:true,w:1+rnd(5)});
 for(let i=0,m=1+rnd(7);i<m;i++)X.push({e:1+rnd(N-1),d:false,w:1+rnd(9)});
 let A=[...D,...X],lambda=1+rnd(3);A=A.map((x,i)=>({...x,id:i,score:x.d?lambda*x.w:x.w})).sort((a,b)=>b.score-a.score||a.id-b.id);
 let J=greedy(c,A),assignment=assign(caps,J),Z=new Set(J.map((_,j)=>j).filter(()=>rnd(2)===0)),S=J.filter((_,j)=>!Z.has(j)),q=sig(c,S,N-1),q0=sig(c,J,N-1),sp=prune(q);
 for(let [u,v] of q){assert(query(sp,u)===v,"sparse query");stats.sparseCoordinateChecks++;let [f]=flow(caps,J,assignment,Z,u);assert(f===v+1,"cut");stats.flowQueries++;
 if(J.length){let i=rnd(J.length),[f0,reach]=flow(caps,J,assignment,new Set(),u),[f1]=flow(caps,J,assignment,new Set([i]),u);assert(f0===query(q0,u)+1&&f1-f0===Number(reach.has(n+i)),"single deleted arc");stats.singleDeletionQueries++}}
 let total=D.reduce((s,x)=>s+x.w,0),best=Array(total+1).fill(0);
 for(let bits=0;bits<(1<<A.length);bits++){stats.bruteSubsets++;let T=A.filter((_,i)=>bits&(1<<i));if(!ok(c,T))continue;let co=total-T.filter(x=>x.d).reduce((s,x)=>s+x.w,0),p=T.filter(x=>!x.d).reduce((s,x)=>s+x.w,0);best[co]=Math.max(best[co],p)}
 for(let b=1;b<=total;b++)best[b]=Math.max(best[b],best[b-1]);
 let low=greedy(c,[...A.filter(x=>x.d),...A.filter(x=>!x.d)]).filter(x=>!x.d).reduce((s,x)=>s+x.w,0),H=J.reduce((s,x)=>s+x.score,0)-lambda*total;
 for(let b=0;b<=total;b++){let p=dp(c,A,b,lambda,low,H+lambda*b,true),r=dp(c,A,b,lambda,low,H+lambda*b,false);assert(p===best[b]&&r===best[b],"budget optimum");stats.budgets++}
 stats.models++;
 }
 return stats
}
console.log(JSON.stringify(replay()));
```

## 5. Source and continuation

Global canonical main 3af8b88765316dd700ffa0bbc178a27c51d01bb7, entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613 checked at that commit. Current EM source a1b377769f23296ae8397b1370a4aa1a8bc49538. P000 V4/V5, ACTIVE worldview, joint/residual contracts, research method, portable rules used. Native original receipt r4-20261128-0130-ec49as-read SUCCEEDED; directory absence only for RS-EC49AS, native owner projection not executed. Historical researcher EM-DIRECT-23537B, current private identity unconfirmed. Independent portable work, no shared claim, no identity substitution, no acceptance. Activity association pending. No new root computations; inherited GBT frontier 1991 feasible, 68 excluded, 334 other; next root 2046. No frozen replay or runtime benchmark.

Next: implement witness backpointers and compare actual DP memory/time with GBW and brute references on the original pinned archive where available; investigate cut-network equivalence or observer-safe dominance without enumerating all subsets, and shared-basis reuse across prefix states. Preserve distinction between polynomial-size query carrier and exponential number of distinct states.