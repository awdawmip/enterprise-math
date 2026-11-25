# R790 — General matching witnesses with bipartite boundary exchange admit linear-size bipartite witnesses

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779_R783_AND_GALLAI_EDMONDS / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R789. EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own metadata r3-20261125-1515-own-metadata-v1: registration exists, no own runs, execution_authorized=false. Owner inventory r3-20261125-1515-owner-read-v1 last observed RUNNING before publication; no shared Task, CLAIM or Result changed. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer contract blob 3923890d77a02d84b772f789e6912dd14f220d14 verified. Frozen generated foundation, Heartbeat and residual-position companion paths returned 404; direct canonical P000/joint and current ACTIVE worldview read. Current global entries verified at 8b3a47b65863c78ab2e8bdd409f8278a3b42054c. Scope: fixed-prefix unsigned Boolean boundary relation only; native signed BRC, weights, provenance, counts, order, X6 common depth remain distinct.

Dependencies:
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md
- c7b233960d24c33525572bd3c4d9b9663f2b830f:research_notes/portable_direct/R786_ASYMMETRIC_K33_DICTIONARY_AND_RANK_CAPACITIES.md
- 05e776b722640728801b1c9810a2cd4e22a4b87f:research_notes/portable_direct/R789_BIPARTITE_LINKAGE_AND_CANONICAL_DEFICIT_CORE.md
- Classical Gallai–Edmonds structure theorem (external): https://link.springer.com/article/10.1007/s00373-020-02266-6 (Theorem 2.1); Berge augmenting-path lemma. We use these standard graph-theory results, not claim novelty for them.

## 1. Statement
Let H be a finite loop-free graph with a perfect matching and labeled terminals T of size b. E={D subset T: H-D admits a perfect matching}. Let L be its pair-exchange graph, edge ij iff {i,j} in E. Suppose L is bipartite with a chosen partition T=A disjoint union B, including arbitrary choices for isolated vertices. Put a=|A|. There is a bipartite graph K with the same labeled terminals, all A on one side and B on the other, and a perfect matching, such that for EVERY D subset T,
    H-D has a perfect matching iff K-D has a perfect matching.
If H has n vertices and m edges, K can be constructed with at most n+2a+2b vertices and m+2a+2b edges. A polynomial preprocessing uses a general maximum matching routine (at most n+a+1 calls with the simple exposability algorithm below), then graph traversal and the indicated incidence construction. It suffices to find one perfect matching in K once. All subsequent rank, membership and canonical deficit-core queries of R789 can use bipartite flow on K, without general matching/blossom processing per query.

The assumption H has a perfect matching is harmless for a nonempty R783 relation normalized at a feasible u: the terminal leaf-twist below implements E XOR u using |u| additional vertices/edges. Thus for an unnormalized H and baseline u replace n,m in the bound by n+|u|,m+|u|. No claim of preservation of number/weight/identity of internal witnesses.

## 2. Balance and terminal twist
Superpose a perfect matching of H with one of H-D. Components of their symmetric difference are alternating cycles and paths ending at the vertices of D. Each path separately gives a feasible pair deletion by exchanging the baseline along that path, so each pair crosses A,B. Therefore |D intersect A|=|D intersect B| for all D in E (also immediate from R779's paired exchange). Consequently S=A XOR D has exactly a elements.

Terminal twist lemma: for each label t in X append a private leaf t' adjacent only to t, and move the label from t to t'. Leaving t' present forces its edge to t, simulating deletion of old t; deleting t' leaves old t as an ordinary unlabelled vertex. For all S, the new deletion relation is exactly the old relation twisted by X, including simultaneous flips, by independent forced leaf edges.

Apply this lemma to H with X=A. Call the resulting graph G, with labels still T. Its feasible terminal deletion sets are exactly the S=A XOR D and all have size a. In particular G has a matching covering all vertices except the a labels in A (D=empty). This is a maximum matching: if it were not maximum, Berge's lemma gives an augmenting path. Its endpoints must both be exposed terminal labels; augmenting covers both and exposes no new vertex, yielding a feasible deletion set of size a-2, impossible. (If a<2 the same conclusion follows since no two exposed endpoints exist.) Hence G has deficiency a, and a set S of terminals is a feasible deletion iff it is the exact exposed vertex set of a maximum matching.

## 3. Canonical component reduction
Use Gallai–Edmonds on G. Let X be vertices exposable by some maximum matching, Y=N(X) minus X, Z=V(G) minus (X union Y), and Q_1,...,Q_c the components of G[X]. The theorem says each Q_i is factor-critical, G[Z] has a perfect matching, and every maximum matching matches each Y vertex into a different Q_i, with exactly one exposed vertex in each unassigned component. Conversely such a choice extends by perfect matching of Z and factor-criticality. In particular c-|Y|=a.

For a label t let p(t) be its component index if its vertex lies in X, or undefined otherwise. The precise terminal-exposure criterion is:
- |S|=a, p(t) exists for every t in S and the p(t) are distinct;
- there is a matching of all Y vertices to the c-a components not occupied by S, using adjacency from G.
Necessity is the decomposition; sufficiency follows by selecting an actual edge from each Y vertex to its assigned component and matching the component minus that endpoint; in an unassigned component delete the specified terminal and match the remainder. Components with no terminal are forced to receive a Y vertex. Labels outside X are never exposed. The criterion does not assume independent pair exchanges.

## 4. Explicit bipartite deletion graph and re-normalization
Build K0 with left vertices q_i (one per component), plus one labeled vertex l_t per terminal; right vertices y for Y plus one socket s_t per terminal. Put edges q_i-y iff the component touches y in G; put l_t-s_t for each label; put q_{p(t)}-s_t iff p(t) exists. These are all edges. If S is deleted from the labeled l_t vertices, every surviving l_t forces its socket. The remaining matching must cover all components using every y and exactly the sockets of S. This is exactly the criterion in section 3. Side cardinalities also force |S|=a. Thus K0 has the exact same terminal deletion relation as G.

Twist K0 again by A using the same private leaf gadget. K is bipartite: the A labels now lie on the right and the B labels on the left (swap side names for R789). It is balanced since c-|Y|=a, and has a perfect matching because D=empty is feasible. For each D,
    K-D perfect <=> K0-(A XOR D) perfect <=> G-(A XOR D) perfect <=> H-D perfect.
This is a full Boolean observer factorization, hence safe for every future legal Boolean boundary composition, including per-prefix usage inside a family. It does not equate families, weighted observations or internal lifts. Individual witnesses can be recovered by undoing the two twists, reading component assignments and choosing the requisite factor-critical matchings and a perfect matching on Z, then undoing R783 if desired.

Size: |V(K)|=c+|Y|+2b+a <= (n+a)+2b+a. The distinct component-to-Y edges are at most |E(G)|=m+a; the socket edges are at most 2b; the last twist adds a edges. Thus |E(K)|<=m+2a+2b. Compute X by testing nu(G-v)=nu(G) for each v, a polynomial (n+a+1)-call implementation; Y, components, adjacency follow by linear traversal. One may instead implement a standard Gallai–Edmonds algorithm. This preprocessing can be more expensive than a single original perfect-matching query; the conclusion is amortized and structural, not a measured speedup or minimum witness bound. With fixed K and its baseline perfect matching, R789 gives per-query O((min(a,|W|)+1)(m+n+b)) rank, exact deficit and canonical core (using the size bounds). The component labels provide a reversible graph-level witness interface. This closes R789's bipartite-pair/nonbipartite-witness question positively.

## 5. Exact replay and scope
The independent original deletion decision is a memoized perfect-matching recursion; GE exposability uses a separate maximum-cardinality recursion; reconstructed bipartite graphs use augmenting-path matching. All integers exact. Enumerated all 16 graphs on four labeled vertices containing the fixed baseline matching and all terminal subsets and valid bipartitions; all 4096 such six-vertex graphs with full terminal set, plus all terminal subsets for the first 256; 128 deterministic distinct eight-vertex graphs with full terminal set and a deterministic secondary subset; every valid oriented partition in each. All terminal deletion assignments checked for each admitted case. Odd factor-critical components and nonbipartite original graphs were included; finite tests verify implementation, the general theorem uses the proof and the classical structure theorem.

```json
[
  {
    "n": 4,
    "graphs": 16,
    "admitted": 544,
    "checks": 2576,
    "nonbip": 261,
    "oddComp": 80,
    "maxVertices": 16,
    "maxEdges": 16,
    "example": null
  },
  {
    "n": 6,
    "graphs": 4096,
    "admitted": 37380,
    "checks": 360256,
    "nonbip": 26053,
    "oddComp": 9416,
    "maxVertices": 24,
    "maxEdges": 27,
    "example": {
      "edges": [
        [
          0,
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ],
        [
          0,
          2
        ],
        [
          0,
          3
        ]
      ],
      "T": 23,
      "A": 18,
      "vertices": 16,
      "edges2": 14
    }
  },
  {
    "n": 8,
    "graphs": 128,
    "admitted": 82,
    "checks": 1272,
    "nonbip": 78,
    "oddComp": 38,
    "maxVertices": 32,
    "maxEdges": 38,
    "example": {
      "edges": [
        [
          0,
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ],
        [
          6,
          7
        ],
        [
          0,
          7
        ],
        [
          1,
          2
        ],
        [
          1,
          6
        ],
        [
          1,
          7
        ],
        [
          2,
          7
        ],
        [
          3,
          4
        ],
        [
          3,
          5
        ]
      ],
      "T": 92,
      "A": 68,
      "vertices": 16,
      "edges2": 15
    }
  }
]
```

Replay (Node/JS, no dependencies):
```js
function replay(){
 const pop=x=>{let k=0;while(x){x&=x-1;k++}return k}, idx=x=>31-Math.clz32(x), each=function*(s){while(s){let q=s&-s;s^=q;yield idx(q)}};
 function adj(n,edges){let r=Array(n).fill(0);for(let [i,j] of edges){r[i]|=1<<j;r[j]|=1<<i}return r}
 function pmOracle(r){let memo=new Map([[0,true]]);return function pm(s){if(memo.has(s))return memo.get(s);if(pop(s)%2)return false;let v=idx(s&-s),t=s^(1<<v),ok=false;for(let j of each(t&r[v]))if(pm(t^(1<<j))){ok=true;break}memo.set(s,ok);return ok}}
 function maxOracle(r){let memo=new Map([[0,0]]);return function mm(s){if(memo.has(s))return memo.get(s);let v=idx(s&-s),t=s^(1<<v),k=mm(t);for(let j of each(t&r[v]))k=Math.max(k,1+mm(t^(1<<j)));memo.set(s,k);return k}}
 function bipartite(r){let color=Array(r.length).fill(-1);for(let v=0;v<r.length;v++)if(color[v]<0){color[v]=0;let q=[v];for(let i of q)for(let j of each(r[i])){if(color[j]<0){color[j]=1-color[i];q.push(j)}else if(color[j]===color[i])return false}}return true}
 function convert(n,edges,T,A){
  let labels=[...each(T)],a=pop(A),gEdges=edges.map(x=>x.slice()),term=labels.slice(),ng=n;
  for(let t=0;t<labels.length;t++)if(A>>labels[t]&1){gEdges.push([labels[t],ng]);term[t]=ng++}
  let g=adj(ng,gEdges),full=(1<<ng)-1,mm=maxOracle(g),nu=mm(full);
  if(ng-2*nu!==a)throw Error("deficiency");
  let X=0;for(let i=0;i<ng;i++)if(mm(full^(1<<i))===nu)X|=1<<i;
  let Y=0;for(let i of each(X))Y|=g[i];Y&=~X;
  let comp=[],which=Array(ng).fill(-1),todo=X;
  while(todo){let seed=todo&-todo,seen=seed,queue=[idx(seed)];for(let i of queue){let add=g[i]&X&~seen;seen|=add;for(let j of each(add))queue.push(j)}for(let i of queue)which[i]=comp.length;comp.push(seen);todo&=~seen}
  let ys=[...each(Y)],c=comp.length,b=labels.length;
  if(c-ys.length!==a)throw Error("GE count");
  let L=c+b,R=ys.length+b+a,rows=Array.from({length:L},()=>[]),tl=[],tr=[],extra=ys.length+b;
  if(L!==R)throw Error("unbalanced witness");
  for(let j=0;j<ys.length;j++)for(let i=0;i<c;i++)if(g[ys[j]]&comp[i])rows[i].push(j);
  for(let t=0;t<b;t++){
    let socket=ys.length+t;rows[c+t].push(socket);
    if(which[term[t]]>=0)rows[which[term[t]]].push(socket);
    if(A>>labels[t]&1){rows[c+t].push(extra);tl[t]=-1;tr[t]=extra++}else{tl[t]=c+t;tr[t]=-1}
  }
  function accepts(D){
   let dl=new Set(),dr=new Set();
   for(let t=0;t<b;t++)if(D>>labels[t]&1){if(tl[t]>=0)dl.add(tl[t]);else dr.add(tr[t])}
   if(dl.size!==dr.size)return false;
   let mate=Array(R).fill(-1);
   function aug(i,seen){for(let j of rows[i])if(!dr.has(j)&&!seen[j]){seen[j]=1;if(mate[j]<0||aug(mate[j],seen)){mate[j]=i;return true}}return false}
   for(let i=0;i<L;i++)if(!dl.has(i)&&!aug(i,Array(R).fill(0)))return false;
   return true
  }
  return {accepts,nontrivial:comp.some(s=>pop(s)>1),vertices:L+R,edges:rows.reduce((s,r)=>s+r.length,0)}
 }
 let out=[];
 for(let n of [4,6,8]){
  let fixed=[],optional=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)(i%2===0&&j===i+1?fixed:optional).push([i,j]);
  let full=(1<<n)-1,limit=n===4?16:n===6?4096:128;
  let graphs=0,admitted=0,checks=0,nonbip=0,oddComp=0,maxVertices=0,maxEdges=0,example=null;
  for(let z=0;z<limit;z++){
   let mask=n===8?((z*104729+127815)&((1<<optional.length)-1)):z;
   let edges=fixed.concat(optional.filter((_,i)=>mask>>i&1)),r=adj(n,edges),pm=pmOracle(r),isBip=bipartite(r);graphs++;
   let pair=Array(n).fill(0);for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(pm(full^(1<<i)^(1<<j))){pair[i]|=1<<j;pair[j]|=1<<i}
   for(let T=0;T<=full;T++){
    if(n===6&&z>=256&&T!==full)continue;
    if(n===8&&T!==full&&T!==((z*73+19)&full))continue;
    for(let A=T;;A=(A-1)&T){
     let B=T^A,ok=true;for(let i of each(T))if(pair[i]&((A>>i&1)?A:B)){ok=false;break}
     if(ok){
      let h=convert(n,edges,T,A);admitted++;if(!isBip)nonbip++;if(h.nontrivial)oddComp++;
      maxVertices=Math.max(maxVertices,h.vertices);maxEdges=Math.max(maxEdges,h.edges);
      for(let D=T;;D=(D-1)&T){let expected=pm(full^D);if(expected&&pop(D&A)!==pop(D&B))throw Error("balance");if(h.accepts(D)!==expected)throw Error(JSON.stringify({n,edges,T,A,D,expected}));checks++;if(D===0)break}
      if(!example&&!isBip&&h.nontrivial&&pop(T)>=4)example={edges,T,A,vertices:h.vertices,edges2:h.edges};
     }
     if(A===0)break;
    }
   }
  }
  out.push({n,graphs,admitted,checks,nonbip,oddComp,maxVertices,maxEdges,example});
 }
 return out
}
console.log(JSON.stringify(replay(),null,2));
```

## 6. Continuation
For general pair graphs (nonbipartite), no fixed-size twist need exist; the preceding reduction does not apply. For multiprefix families, combine two fixed relations by adding labeled interface edges between their matching witnesses (as in R783), then test perfect matching; for full universal compatibility require a witness for every prefix pair. The next question is an implicit multiprefix quotient/dominance algorithm without listing all per-prefix relations, especially when different prefixes induce different bipartitions; seek a precise parameter or obstruction rather than assume flow alone decides the universal quantifier. No external novelty or independent review claimed.