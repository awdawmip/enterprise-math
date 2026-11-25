# R789 - Exact directed linkage and canonical deficit core for bipartite matching residuals

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R783_R786 / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R788, EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own session metadata r3-20261125-1420-own-metadata-v1: existing registration, no own runs, execution_authorized=false. Owner query r3-20261125-1420-owner-read-v1 last observed RUNNING; no shared Task or CLAIM changed. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer preservation blob 3923890d77a02d84b772f789e6912dd14f220d14 read. Generated foundation and residual-position companion at that pin returned 404; ACTIVE worldview and P000 read directly. Canonical global entries verified at a83688d16ced6c8c32039e36b18fd02b2f2728c6. Scope: fixed-prefix unsigned Boolean boundary support, not native signed BRC, counts, weights, provenance, event order or X6 common depth.

Dependencies:
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md
- c7b233960d24c33525572bd3c4d9b9663f2b830f:research_notes/portable_direct/R786_ASYMMETRIC_K33_DICTIONARY_AND_RANK_CAPACITIES.md
- 55850201b21b431ada5439749a96a5c3fc50630f:research_notes/portable_direct/R788_EXPONENTIAL_RANK_CAPACITY_AND_PAIRED_SLOT_NETWORK.md

## 1. Directed linkage construction

Let H be any finite bipartite matching-deletion witness with equal left and right sizes n, a fixed perfect matching M0, and distinct boundary labels A on the left and B on the right. No assumption that all vertices are terminals. The normalized deletion relation is E={D:H-D has a perfect matching}. Set S=A symmetric-difference D. All feasible S have size a=|A|. By R783 these relations are auxiliary Port realizable; by R786 the feasible S are bases of a rank-a matroid (or use the linkage construction below).

Index matched pairs as (l_i,r_i). Contract each matching edge to vertex i; every nonmatching edge l_i r_j gives directed arc i->j. Write U=D intersect A, V=D intersect B. Then H-D has a perfect matching iff |U|=|V| and there are vertex-disjoint directed paths from the matched-pair indices of V to those of U, allowing zero-length paths.

Proof: superpose a matching of H-D on M0. After omitting common edges the components are alternating cycles and paths with endpoints the deleted vertices. Since both endpoints have a baseline edge, each such path has odd length and endpoints on opposite sides. Traverse from deleted right to deleted left: nonbaseline edges are l_i r_j, hence orientation i->j. Distinct paths cannot use the same matched pair. If both endpoints of a baseline edge are deleted its path has length zero in the contracted graph. Conversely expand paths, remove their baseline edges, add their nonmatching edges, and retain untouched baseline edges. This matches exactly all undeleted vertices. Cycles are unnecessary for Boolean feasibility.

## 2. Exact basis and rank oracle with independent sink gates

Build a directed integral flow network. Each matched-pair vertex i has in/out nodes and a unit capacity arc. Each nonmatching arc has capacity M=b+1 with b=|A|+|B|. For every a_i in A create a separate gate g_i with a unit arc to the sink and an M-capacity arc from i_out to g_i. For a query W subset A union B, each label in W has its own label node and a unit arc from the source. The label a_i connects directly to g_i with capacity M; the label b_i connects to i_in with capacity M. All other label nodes have no source arc. The gates must be separate from the matched-pair vertices.

Claim: the maximum flow f(W) equals r(W)=max_{basis S}|S intersect W|. In particular a size-a candidate S is feasible iff f(S)=a.

Proof: a full flow for a size-a S sends each selected A label directly to its gate (these are their only outgoing arcs), leaving precisely the gates of A minus S for the selected B labels. Integral path decomposition gives exactly the disjoint contracted paths of section 1, and conversely. For arbitrary W, a basis supplies a flow of size |S intersect W| by deleting the other source paths. Conversely an integral maximum flow chooses some subset I of W. Complete its paths by sending the A labels of unused gates directly to those gates. These labels are not already used, and these paths consume no pair-vertex capacity. Thus I extends to a feasible basis; f(W)<=r(W). This also gives a constructive completion and a matching witness for accepted basis queries.

A failed first construction merged each A gate with its pair vertex. Counterexample actually found in the first exact replay: n=3, row masks [3,2,4], A left indices {0,1}, B right index {0}, W={a0,b0}. Direct deletion matching accepts W (delete l1 and r0; match l0 to r1 and l2 to r2), rank 2, but the merged network returned flow 1. A retained A label must not consume a pair vertex that can be used by an alternating path. The separate-gate construction fixes this issue. No claim that the original incorrect model is a valid compression.

## 3. One min-cut yields an exact canonical maximum-deficit constraint

For each W, let Z be the vertices reachable from the source in the residual graph of any maximum flow. Let R be the labels of W whose label nodes are in Z. Let X be the unit pair-vertex arcs and unit gate-to-sink arcs crossing Z to its complement. Since the minimum cut capacity is at most |W|<M, no M-capacity arc crosses. The min-cut identity is

    r(W)=|W minus R|+|X|.

All paths from R to the sink must cross X. By section 2, r(R)<=|X|. On the other hand r(W)<=|W minus R|+r(R), by restricting any basis. Equality follows:

    r(R)=|X|,   |R|-r(R)=|W|-r(W).

Thus if W is dependent, the ONE max-flow computation supplies a genuinely violated original rank inequality |S intersect R|<=r(R) for S=W (and a concrete bottleneck cut). No enumeration of cyclic flats or rank inequalities is required.

More strongly, R is the unique inclusion-minimal subset of W of the same deficiency |W|-r(W). For any Q subset W with that deficiency, use a min-cut for query Q and place the omitted W-label nodes outside its source side. The cut extends to W with extra capacity |W minus Q| (label nodes have no incoming arcs except source arcs). Its total capacity is r(W). Residual reachability Z is contained in the source side of EVERY minimum cut: any such cut has no positive residual outgoing arc. Therefore R subset Q. The previous equality shows R itself achieves full deficiency. This proves canonicity even if the maximum flow is not unique.

Equivalently R={e in W:r(W minus {e})=r(W)}, the union of all circuits contained in W (the cyclic part of the restriction, not necessarily a flat of the ambient matroid). Indeed if deleting e leaves rank unchanged then it reduces deficiency by one, so every full-deficiency subset contains e. If deleting e lowers rank, W minus {e} already attains full deficiency, so minimal R omits it. An element is in a circuit within W iff deletion leaves rank unchanged: if a circuit contains e then e is in the closure of the rest of W; if deletion leaves rank unchanged, add e to a basis of W minus e and take a minimal dependent subset. This identifies the canonical cut output without a second rank query per label.

Cost: construct O(n+b) vertices and O(|edges(H)|+n+b) arcs. At most min(a,|W|) integral augmentations suffice even with a simple BFS augmenting-path implementation on adjacency lists. Each augmentation and final reachability costs O(|edges(H)|+n+b). Thus a rank query, exact deficiency, canonical core and a cut certificate can be obtained in O((min(a,|W|)+1)(|edges(H)|+n+b)) operations, in addition to finding one baseline matching when not supplied. Integer capacities at most b+1 use O(log(b+2)) bits. This is an implicit representation, not a bound on the minimum possible witness graph size. The proof uses all alternating-path interactions; no independent pair-readout assumption is made. It applies to R788's explicit bipartite family including its exponentially many indispensable individual constraints.

## 4. Exact replay

All 64 simple bipartite graphs on 3+3 labeled vertices containing the fixed diagonal matching, and all 64 choices of terminal subsets A,B per graph; 128 deterministic distinct graphs on 4+4 (off-diagonal mask (4051*c+173) mod 4096, c=0..127), all terminals. Direct deletion matching by bipartite augmentation, independent full basis enumeration and intersection ranks compared with the directed network. For every query W checked rank, tight cut, full deficiency, canonical core against all single-label rank deletions, and candidate basis membership. Zero discrepancies after separate-gate repair. The direct matching and flow algorithms are separate implementations.

[
  {
    "n": 3,
    "cases": 4096,
    "queries": 46656,
    "failed": 18944,
    "nontrivial": 6048,
    "bases": 12608
  },
  {
    "n": 4,
    "cases": 128,
    "queries": 32768,
    "failed": 15207,
    "nontrivial": 7977,
    "bases": 6320
  }
]

Replay code (Node/JS, exact small integers, no packages):

```js
function replay(){
 const pop=x=>{let n=0;while(x){x&=x-1;n++}return n};
 function run(n,rows,A,B){
  const labels=[];for(let i=0;i<n;i++)if(A>>i&1)labels.push([0,i]);for(let i=0;i<n;i++)if(B>>i&1)labels.push([1,i]);
  const m=labels.length,N=1<<m,a=pop(A),base=(1<<a)-1;
  function match(S){
   let U=0,V=0;for(let t=0;t<m;t++)if((S^base)>>t&1){const [side,i]=labels[t];if(side)V|=1<<i;else U|=1<<i}
   if(pop(U)!==pop(V))return false;let used=Array(n).fill(-1);
   function aug(i,seen){for(let j=0;j<n;j++)if(rows[i]>>j&1&&!(V>>j&1)&&!seen[j]){seen[j]=1;if(used[j]<0||aug(used[j],seen)){used[j]=i;return true}}return false}
   for(let i=0;i<n;i++)if(!(U>>i&1)&&!aug(i,Array(n).fill(0)))return false;return true;
  }
  const bases=[];for(let S=0;S<N;S++)if(match(S))bases.push(S);
  const rank=Array.from({length:N},(_,W)=>Math.max(...bases.map(S=>pop(S&W))));
  function flow(W){
   const s=3*n+m,t=s+1,L=t+1,cap=Array.from({length:L},()=>Array(L).fill(0)),INF=m+1;
   for(let i=0;i<n;i++){cap[2*i][2*i+1]=1;if(A>>i&1){cap[2*i+1][2*n+i]=INF;cap[2*n+i][t]=1}for(let j=0;j<n;j++)if(i!==j&&(rows[i]>>j&1))cap[2*i+1][2*j]=INF}
   for(let l=0;l<m;l++)if(W>>l&1){const [side,i]=labels[l];cap[s][3*n+l]=1;cap[3*n+l][side?2*i:2*n+i]=INF}
   let value=0,seen;
   while(true){const p=Array(L).fill(-1),q=[s];p[s]=s;for(let k=0;k<q.length;k++){let u=q[k];for(let v=0;v<L;v++)if(p[v]<0&&cap[u][v]>0){p[v]=u;q.push(v)}}if(p[t]<0){seen=p.map(x=>x>=0);break}for(let v=t;v!==s;v=p[v]){cap[p[v]][v]--;cap[v][p[v]]++}value++}
   let R=0,X=0;for(let l=0;l<m;l++)if(seen[3*n+l])R|=1<<l;for(let i=0;i<n;i++){if(seen[2*i]&&!seen[2*i+1])X++;if((A>>i&1)&&seen[2*n+i])X++}
   return {value,R,X};
  }
  let failed=0,nontrivial=0;
  for(let W=0;W<N;W++){const {value,R,X}=flow(W);let core=0;for(let l=0;l<m;l++)if(W>>l&1&&rank[W^(1<<l)]===rank[W])core|=1<<l;
   if(value!==rank[W]||R!==core||rank[R]!==X||pop(R)-rank[R]!==pop(W)-rank[W])throw Error(JSON.stringify({n,rows,A,B,W,value,R,X,core,rank:rank[W]}));
   if(value<pop(W))failed++;
   if(pop(W)===a&&((value===a)!==match(W)))throw Error("membership");
   if(R&&R!==W)nontrivial++;
  }
  return {queries:N,failed,nontrivial,bases:bases.length};
 }
 let totals=[];
 for(const n of [3,4]){let cases=0,queries=0,failed=0,nontrivial=0,bases=0;const edges=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j)edges.push([i,j]);let limit=n===3?64:128;
 for(let c=0;c<limit;c++){const mask=n===3?c:((c*4051+173)&4095),rows=Array.from({length:n},(_,i)=>1<<i);edges.forEach(([i,j],k)=>{if(mask>>k&1)rows[i]|=1<<j});let full=(1<<n)-1;for(let A=0;A<=full;A++)for(let B=0;B<=full;B++){if(n===4&&(A!==full||B!==full))continue;const r=run(n,rows,A,B);cases++;queries+=r.queries;failed+=r.failed;nontrivial+=r.nontrivial;bases+=r.bases;}}
 totals.push({n,cases,queries,failed,nontrivial,bases});}
 return totals;
}
console.log(JSON.stringify(replay(),null,2));
```

## 5. Next frontier

The theorem completes the directed linkage question for a supplied BIPARTITE matching witness H; it does not prove that every Port relation whose pair graph is bipartite has a polynomial-size bipartite witness. The general R783 witness can be nonbipartite. Study whether its bipartite boundary relation has a directed representation, or whether blossom-type constraints genuinely survive. Also investigate multiprefix universal compatibility with implicit witnesses rather than expanding all bases or constraints. The canonical core is not a replacement for the full relation or signed/native state. The mathematical flow/gammoid ideas are classical; the concrete contribution is the scoped Port-to-linkage map, gate correction, and one-cut canonical deficiency interface for this research line. No external novelty or independent review claimed.
