# R784 — Chordless long even cycles are forced; exact cactus boundary classification

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779_R783 / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own metadata r3-20261125-0920-own-metadata-v1 confirmed the existing research registration and no runs or execution authorization; owner inventory r3-20261125-0920-owner-read-v1 was RUNNING before the science. No shared Task/CLAIM/Result. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14, weighted BRC substrate f375a059fa4af8c6eefaddb4d4a8689a0c063674. Frozen generated foundation package returned 404; exact relevant canonical inputs were read instead. Global V4, ACTIVE worldview and current portable and research policies consulted. Sources:
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md

## 1. Scope and long-cycle obstruction

Let E be the feasible boundary assignments of one fixed prefix/reserve in the unsigned even-triple auxiliary Port network of R779/R783. Normalize by a feasible u, so 0 belongs to E' = E XOR u. Define the simple pair graph L by ij in L iff {i,j} belongs to E'. R779 proves simultaneous disjoint paired exchange between any two feasible assignments. R783 proves the matching-deletion representation and the characteristic-zero skew principal-minor representation of E', and shows that any subset with exactly one perfect matching in its induced pair graph is feasible.

Theorem 1. If an induced subgraph L[C] is a chordless even cycle of length 2k >= 6, then C belongs to E'. This holds regardless of other vertices or edges outside C.

Proof. Number the cycle 0,...,2k-1 in cyclic order. Let U={0,2k-1} and V=C minus U. U is feasible by definition. V induces an even path, with exactly one perfect matching, hence is feasible by R783. Assume C is infeasible. Apply R779 paired exchange to U and V, whose symmetric difference is C. The two vertices of U cannot be paired together: toggling that pair starting from V would produce C (all subset toggles are possible starting from either endpoint). They must be paired to two distinct vertices in V. Toggling either of these pairs starting from U yields a feasible two-element set; hence the partner of 0 must be 2k-2 (the only other neighbor of 2k-1 inside C), and the partner of 2k-1 must be 1. Toggling both pairs produces {1,2k-2}. These are not adjacent for 2k>=6 in an induced cycle. Contradiction. The result fails for a four-cycle, where 1 and 2 are adjacent and R779 gives both possible full-cycle outcomes. Thus a putative zero full-cycle Pfaffian on a chordless C6 or longer is an obstruction to realization by this Port/matching network, even though abstract skew matrices with such a cancellation exist (choose nonzero edge weights to cancel the two matching monomials). This distinguishes general skew representability from matching representability.

## 2. Cactus theorem: exact classification and minimal extra bits

A cactus here is a finite simple graph, possibly disconnected, in which no edge belongs to two distinct simple cycles. Fix a normalized relation E' whose pair graph L is a cactus. For each four-cycle C in L record one bit f(C)=1 if C belongs to E', else 0. Then for EVERY even subset J of labels:

- if L[J] has no perfect matching, J is infeasible;
- otherwise choose ANY perfect matching M of L[J]. J is feasible iff no four-cycle with f(C)=0 has all its vertices matched to each other by M using edges of that cycle.

The empty matching is allowed. This rule and the pair graph determine E' completely. The criterion is independent of the selected perfect matching. Every assignment of the four-cycle bits is realizable; thus a fixed labeled cactus L gives exactly 2^(number of four-cycles) distinct normalized relations, and exactly that many bits are necessary in a fixed-length exact extra code. In particular, for cactus graphs without four-cycles the pair graph alone determines all higher-order feasibility, even if there are arbitrarily many long even cycles.

Proof of necessity and exactness. Apply the R783 skew matrix representation M0, with nonzero entries precisely on L. Fix any perfect matching M of L[J]. A second perfect matching differs from M in a vertex-disjoint union of M-alternating simple even cycles. In a cactus any two distinct M-alternating cycles are vertex-disjoint: if they shared a vertex they would share the unique matching edge at that vertex, violating the cactus hypothesis. Conversely any collection of these alternating cycles can be flipped independently to produce a matching. The alternating cycles are exactly the even cycle blocks with all their vertices matched internally along the cycle by M. Each cycle is chordless, since a chord would place an edge in two distinct cycles. Reorder J by these disjoint cycles and the remaining fixed matching edges. In the Pfaffian expansion every matching term factors into its cycle-local term and the same product of remaining nonzero entries; the sign of the reordering is common. Therefore Pf(M0[J]) is, up to sign, the product of the fixed entries and the Pfaffians Pf(M0[C]) over all active cycles. Theorem 1 shows that each long even cycle factor is nonzero. The four-cycle factors are nonzero exactly when f(C)=1. Since the coefficient field has no zero divisors, the claimed criterion follows. If one active cycle is flipped, its vertices remain matched internally; all other active cycles are disjoint. Any matching is a sequence of these flips, so the criterion is independent of M. This proof covers arbitrary finite size and includes odd cycles, which cannot be alternating.

## 3. Realization of all bit choices

Construct a matching-deletion graph, then apply R783 Theorem A converse (p=0 Port gadgets). Partition cactus edges into cycle blocks and the remaining bridges. For an unmarked block B (bridge, odd cycle, long even cycle, or four-cycle with bit 1), make a core graph B with a labeled terminal leaf at each core vertex. Deleting a subset of leaves is feasible precisely when that subset admits an internal perfect matching in B. For a four-cycle with bit 0 use four terminals t0,t1,t2,t3 and two internal vertices a,b; edges a-t0,a-t2,b-t1,b-t3,t0-t1. The empty deletion is feasible (match t0-t1, a-t2,b-t3), an adjacent pair deletion is feasible (one remaining terminal from each parity class), an opposite pair is infeasible, and deletion of all four leaves a,b unmatched. Odd deletions are excluded by parity.

For every global label v, add a new global terminal leaf and its center c_v. Join c_v to the local terminal of v in each incident block. A nondeleted global leaf forces its center to match it and no block terminal of v is deleted. A deleted global leaf forces the center to match exactly one block terminal of v. Thus global deletion sets are disjoint unions of feasible block-local deletions, with at most one chosen block at each label; the construction also handles isolated labels. All graph orders are even, and the graphs are loop-free. A feasible decomposition is equivalent to a perfect matching of L[J] that does not saturate a marked four-cycle internally: within an unmarked block choose an internal perfect matching, within a marked block choose zero or one edge. Because the necessity criterion is independent of the matching, this is exactly the asserted relation. The realized pair graph is L, since two-element feasible deletions must belong to one block and form an edge there. The full four-cycle label set has no alternative matching using edges outside that induced cycle, so its bit is exactly prescribed. This proves both independent realization and the minimum bit count. An arbitrary feasible even baseline shift uses R783's paired shift gadget. The construction does not require connected witness interiors.

## 4. Exact replay

Enumerated all labeled simple graphs on 1..6 vertices, retained precisely the cactus graphs by simple-cycle edge-disjointness, enumerated every assignment of four-cycle bits, and checked every even subset against two implementations: (a) first perfect matching of the pair graph with marked-cycle test; (b) perfect matching of the independently constructed deletion graph, using recursive exact BigInt bit sets. Additional fixtures include two squares sharing an articulation, two squares joined by a bridge, a length-ten cycle, and a length-six cycle joined to a square and tail. These finite experiments check the construction and algorithm; the general statements follow from the analytic proofs. No performance benchmark or native BRC execution is claimed.

Actual output:
```json
{
  "counts": [
    {
      "n": 1,
      "graphs": 1,
      "relations": 1,
      "labels": 1
    },
    {
      "n": 2,
      "graphs": 2,
      "relations": 2,
      "labels": 4
    },
    {
      "n": 3,
      "graphs": 8,
      "relations": 8,
      "labels": 32
    },
    {
      "n": 4,
      "graphs": 57,
      "relations": 60,
      "labels": 480
    },
    {
      "n": 5,
      "graphs": 623,
      "relations": 698,
      "labels": 11168
    },
    {
      "n": 6,
      "graphs": 9334,
      "relations": 11044,
      "labels": 353408
    }
  ],
  "extras": [
    {
      "n": 7,
      "labels": 256,
      "relations": 4
    },
    {
      "n": 8,
      "labels": 512,
      "relations": 4
    },
    {
      "n": 10,
      "labels": 512,
      "relations": 1
    },
    {
      "n": 12,
      "labels": 4096,
      "relations": 2
    }
  ],
  "failures": 0
}
```

Dependency-free JavaScript replay:
```js
function verify(){
 const counts=[],bit=i=>1<<i;
 function cycles(n,edges){
  let adj=Array.from({length:n},()=>[]);edges.forEach(([u,v],i)=>{adj[u].push([v,i]);adj[v].push([u,i])});
  const cs=[],used=new Set();let cactus=true;
  function dfs(s,path,ei,mask){let u=path[path.length-1];for(const [v,k] of adj[u]){
   if(v===s&&path.length>=3&&path[1]<u){let ids=[...ei,k];if(ids.some(i=>used.has(i)))cactus=false;ids.forEach(i=>used.add(i));cs.push({vs:[...path],ids,mask});}
   else if(v>s&&!(mask&bit(v)))dfs(s,[...path,v],[...ei,k],mask|bit(v));
  }}
  for(let s=0;s<n;s++)dfs(s,[s],[],bit(s));return {cactus,cs,used}
 }
 function check(n,edges,cs,used,marks){
  const adj=Array(n).fill(0);for(const [u,v] of edges){adj[u]|=bit(v);adj[v]|=bit(u)}
  const memo=new Map([[0,[]]]);
  function first(s){if(memo.has(s))return memo.get(s);let x=s&-s,u=31-Math.clz32(x),a=adj[u]&s,ans=null;while(a){let y=a&-a;a^=y;let r=first(s^x^y);if(r!==null){ans=[x|y,...r];break}}memo.set(s,ans);return ans}
  function predicted(s){let m=first(s);return m!==null&&!marks.some(c=>m.filter(e=>(e&c.mask)===e).reduce((a,e)=>a|e,0)===c.mask)}
  // Independently build a matching-deletion graph; vertices 0..n-1 are global terminals.
  let N=n,he=[],ports=Array.from({length:n},()=>[]),alloc=()=>N++;
  function ordinary(vs,es){let t=new Map(),core=new Map();for(const v of vs){t.set(v,alloc());core.set(v,alloc());he.push([t.get(v),core.get(v)]);ports[v].push(t.get(v))}for(const [u,v] of es)he.push([core.get(u),core.get(v)])}
  for(const c of cs){if(marks.includes(c)){let t=c.vs.map(v=>{let k=alloc();ports[v].push(k);return k});let a=alloc(),b=alloc();he.push([a,t[0]],[a,t[2]],[b,t[1]],[b,t[3]],[t[0],t[1]])}
   else ordinary(c.vs,c.ids.map(i=>edges[i]))}
  edges.forEach((e,i)=>{if(!used.has(i))ordinary(e,[e])});
  for(let v=0;v<n;v++){let c=alloc();he.push([v,c]);for(const t of ports[v])he.push([c,t])}
  let h=Array(N).fill(0n);const B=i=>1n<<BigInt(i);for(const [u,v] of he){h[u]|=B(v);h[v]|=B(u)}
  const pm=new Map([[0n,true]]);
  function perfect(s){if(pm.has(s))return pm.get(s);let a=s,best=0n,degree=Infinity,chosen=0n;
   while(a){let x=a&-a;a^=x;let i=x.toString(2).length-1,q=h[i]&s,d=0;for(let t=q;t;t&=t-1n)d++;if(d<degree){degree=d;chosen=x;best=q;if(d<=1)break}}
   let ok=false;while(best){let y=best&-best;best^=y;if(perfect(s^chosen^y)){ok=true;break}}pm.set(s,ok);return ok}
  let labels=0,feasible=0;for(let s=0;s<1<<n;s++){if(s.toString(2).replace(/0/g,"").length%2)continue;let p=predicted(s),q=perfect(((1n<<BigInt(N))-1n)^BigInt(s));if(p!==q)throw Error(JSON.stringify({n,edges,s,marks:marks.map(c=>c.vs),p,q}));labels++;if(p)feasible++}
  return {labels,feasible}
 }
 function graph(n,edges,c){let {cs,used,cactus}=c;if(!cactus)throw Error("not cactus");let squares=cs.filter(x=>x.vs.length===4),labels=0,relations=0;for(let j=0;j<1<<squares.length;j++){let marks=squares.filter((_,i)=>j&bit(i));labels+=check(n,edges,cs,used,marks).labels;relations++}return {labels,relations}}
 for(let n=1;n<=6;n++){let es=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)es.push([i,j]);let graphs=0,labels=0,relations=0;for(let a=0;a<1<<es.length;a++){let edges=es.filter((_,i)=>a&bit(i)),c=cycles(n,edges);if(!c.cactus)continue;graphs++;let r=graph(n,edges,c);labels+=r.labels;relations+=r.relations}counts.push({n,graphs,relations,labels})}
 const extras=[
  [7,[[0,1],[1,2],[2,3],[3,0],[0,4],[4,5],[5,6],[6,0]]],
  [8,[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[3,4]]],
  [10,Array.from({length:10},(_,i)=>[i,(i+1)%10])],
  [12,[...Array.from({length:6},(_,i)=>[i,(i+1)%6]),[5,6],[6,7],[7,8],[8,9],[9,6],[9,10],[10,11]]]
 ].map(([n,edges])=>({n,...graph(n,edges,cycles(n,edges))}));
 return {counts,extras,failures:0}
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next

Extend the obstruction to non-cactus pair graphs. Identify the first genuinely overlapping even-cycle pattern requiring higher joint bits, and characterize which skew cancellation relations remain matching-realizable at six labels. The six-cycle all-toggle exclusion is already impossible, not an open case. The unrestricted six-cut dictionary and universal multi-prefix optimization remain open. Retain signed BRC, exact weights, branch histories, source, native slice common depth and time order as distinct observers. The present certificate is only for fixed-prefix Boolean boundary feasibility and its existing exact glue; it removes no required signed or provenance data. R782 end-to-end DP benchmark remains open.
