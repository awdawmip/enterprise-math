# R783 — Matching representation and exact sparse-pair boundary classification

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own recovery r3-20261125-0820-own-metadata-v1 confirms existing registration, no own run and no execution authorization. Owner inventory r3-20261125-0820-owner-read-v1 last observed RUNNING before publication. No shared Task, no CLAIM or Result. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-relation contract blob 3923890d77a02d84b772f789e6912dd14f220d14 read. ACTIVE worldview and current portable/continuation rules read. Exact predecessors:
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- be902aba663c144a6377895f6f0a7e9c9b850526:research_notes/portable_direct/R782_TABLE_FREE_BOOLEAN_QUOTIENT_GLUE.md

## 1. Scope and theorem

Use R779's unsigned auxiliary even-triple Port network: at each vertex a fixed prefix x and target w yield a local constraint x+w+z in S(t), S(0)={0}, S(1)={1,2,3} in two-bit local coordinates, S(2)=all four. In three-port bit notation all patterns have even parity. Internal ports agree, private ports have lift bit zero. R779 provides gadgets for arbitrary nonempty subsets of the four even triples, with p=0. Let E be the relation of extendible assignments at b labeled boundary ports for ONE fixed prefix and reserve. The theorem concerns this single relation, not the universal multiprefix reserve optimizer.

Theorem A (matching representation). For every such network there is an ordinary loop-free matching graph H of even order, with distinct labeled terminal vertices T, such that D subset T belongs to E iff H-D has a perfect matching. H has at most six vertices per original support. Conversely every such even-order matching deletion relation, allowing disconnected interiors, is realizable by an auxiliary trivalent Port network using R779's local gadgets, without requiring nonzero prefix.

Proof forward. Replace each support by three terminal vertices p0,p1,p2 and a center c. For every allowed pair of active ports {i,j}, connect the remaining terminal to c. A two-terminal deletion then leaves exactly that remaining terminal and c, so is feasible precisely for the declared pair. If the zero triple is allowed and at least one pair is allowed, add a terminal-terminal edge for one such pair; this makes the empty deletion feasible by matching its complement to c. If zero is not allowed, omit this edge, so no perfect matching on the four vertices. For the singleton {zero}, instead use three separate terminal-private-leaf edges (six vertices); any nonempty deletion leaves an isolated leaf. For the empty relation use an isolated center and no other edges. Odd deletions are impossible by parity. Thus the entire local truth table is preserved, including empty and infeasible cases.

For each original internal Port edge add the edge linking its two matching terminals. A global perfect matching selects some of these linking edges. Their endpoints are removed from their local gadgets, precisely implementing a common bit 1. Unselected linking edges implement bit 0. Private terminals have no linking edge and are never deleted. Boundary bit 1 deletes the indicated terminal. Hence any global matching restricts to accepted local lifts, and every accepted lift extends to a global matching by independently matching the remaining gadget vertices. The reduction is linear in the network size. A fixed-prefix feasibility query now admits an ordinary general-graph perfect-matching decision instead of enumerating every cycle lift. Recovering one lift follows by reading the selected linking edges.

Proof converse. For H of even order, if E is empty an inconsistent Port component realizes it. Otherwise choose one feasible deletion D0 and one perfect matching of H-D0. At each graph vertex impose exactly one of the incident matching-edge variables and, for a terminal, its deletion variable. Encode this using a binary tree of count bits: parent = sum of two children in {0,1}; the allowed triple is (000,101,110) in parent/children order up to permutation, and root is pinned to 1. The selected matching/deletion baseline determines every internal count bit. XOR each variable by its baseline (the same on both ends of every shared edge); the local ternary relation remains a subset of even triples and the root pin becomes zero. Unary cases use a singleton zero relation with private zero ports; a zero-degree nonterminal cannot occur in a nonempty deletion relation. The tree handles all degrees, with linear-size overhead in the incidence list. Any size-two local relation is realizable by R779's pin gadget. This yields boundary relation E XOR D0. Since |D0| is even, pair the coordinates in D0. To unshift them, append at each such port a vertex with old and new port bits opposite and third bit fixed 1; link the third ports in each pair, and use the R779 size-two gadget for the allowed even triples (011,101) in old/new/third order. Other ports remain unchanged. This exactly restores E. All graphs can be taken loop-free; the converse does not assert connectedness of every witness. This completes the equivalence.

## 2. Principal-minor representation of the entire boundary relation

Theorem B. If E is nonempty, fix u in E. There exists a b by b skew-symmetric matrix M over a rational function field of characteristic zero such that
    v in E iff det M[support(v XOR u)] != 0,
with the empty principal determinant equal to 1.

Proof. Give each edge of H an independent indeterminate and form its skew adjacency A (opposite signs on opposite orientations). For any even vertex subset W, the Pfaffian expansion of A[W] is a signed sum of distinct monomials indexed by perfect matchings, so is nonzero exactly when H[W] has a perfect matching. Its square is det A[W]; odd subsets have zero determinant. Put I=V(H) minus u; A[I] is invertible. Perform principal pivot on I: for A=[P Q; C R], the transformation B=[P^-1, -P^-1 Q; C P^-1, R-C P^-1 Q], C=-Q^T, is skew-symmetric. To see the relevant nonsingularity relation directly, write y=A x and swap x_i and y_i for i in I. The resulting relation is y'=B x'. For any J, B[J] singular iff a nonzero pair (x',y') exists with x' supported on J and y' zero on J. Undoing the swap gives exactly x supported on I symmetric-difference J and y zero there, with a nonzero pair (and thus nonzero x). Therefore B[J] nonsingular iff A[I symmetric-difference J] nonsingular. Restrict B to the b labeled boundary terminals to obtain M. For J=v XOR u, I symmetric-difference J=V(H) minus v. This proves the claim.

No claim is made that an arbitrary skew matrix support is realizable by the original Port graph; the necessary representation has a matching-graph origin. In particular, all entries and larger minors may be correlated. It is essential not to infer independence of the effective boundary matrix entries.

## 3. Exact sparse-pair classification at arbitrary boundary width

For baseline u define the pair graph L_u on the boundary labels, where ij is an edge iff u XOR {i,j} is feasible. By Theorem B this is exactly the nonzero entry graph of M. For an even subset J, the Pfaffian expansion of M[J] yields:
- if L_u[J] has no perfect matching, u XOR J is excluded;
- if L_u[J] has exactly one perfect matching, u XOR J is feasible;
- when there are multiple perfect matchings, the conclusion may depend on the actual joint coefficients. Retain this as unresolved by the pair graph alone.

If L_u has no even simple cycle, any two distinct perfect matchings would have an even alternating cycle in their symmetric difference. Thus every induced subset has at most one perfect matching. In this case the complete relation is precisely
    E = {u XOR J : J is the vertex coverage of a matching in L_u}.
Conversely any graph L with no even cycle gives such a relation: attach one private terminal leaf to every vertex of L. Deleting exactly the terminal set J forces the core vertices of J to match internally, with all other cores forced to match their leaves. Apply Theorem A converse; an arbitrary even baseline shift is available by the same paired shift gadget. In fact the coverage construction works for every L, although the pair graph need not determine all relations if even cycles exist.

For six terminals with L=P6 (path), the complete normalized dictionary is exactly the 13 masks 0,3,6,12,15,24,27,30,48,51,54,60,63 (binary coordinate numbering 0..5). This is a complete unbounded-interior classification under the stated sparse-pair hypothesis, not a count over all six-cut networks. On four terminals with a C4 pair graph, R779 gives two real relations with the same pair graph, with and without the all-four toggle, since the first has two full antipodal pairs and the second has three. Thus even-cycle joint information is genuinely needed beyond pair readouts. The result provides a structural exact test at arbitrary cut width and a restricted dictionary reconstruction theorem. It does not replace the R780/R782 multiprefix quotient, which still needs the complete set of per-prefix relations.

## 4. Actual finite replay

Exact JS integer and BigInt execution: 433 network configurations; 12,616 even boundary label decisions compared between direct Port assignment enumeration and an independent perfect-matching recursion on the gadget graph. Included all 16 local masks (including empty sentinel), all 225 nonempty two-vertex mask combinations, and 64 deterministic local configurations each on 4-, 6-, and 8-cycles; zero discrepancies. All odd deletions are excluded analytically by even gadget order. Path/cycle coverage masks independently enumerated. This checks the forward gadget implementation; the converse, principal pivot and sparse theorem use the analytic proof, not a finite experimental generalization.

```js
function verify(){
 const even=[0,3,5,6], ix=x=>even.indexOf(x), pop=x=>x.toString(2).replace(/0/g,"").length;
 function gadget(mask,edges,alloc){
  const p=[alloc(),alloc(),alloc()];
  if(mask===1){for(const v of p)edges.push([v,alloc()]);return p}
  const c=alloc();let witness=-1;
  for(let i=1;i<4;i++)if(mask>>i&1){let q=even[i],j=[0,1,2].find(j=>!(q>>j&1));edges.push([p[j],c]);witness=q}
  if((mask&1)&&witness>=0){let a=[0,1,2].filter(j=>witness>>j&1);edges.push([p[a[0]],p[a[1]]])}
  return p
 }
 function matchingRelation(masks,links,ports){
  let n=0,edges=[],alloc=()=>n++,p=masks.map(m=>gadget(m,edges,alloc));
  for(const [i,a,j,b] of links)edges.push([p[i][a],p[j][b]]);
  let adj=Array(n).fill(0n),bit=i=>1n<<BigInt(i);
  for(const [i,j] of edges){adj[i]|=bit(j);adj[j]|=bit(i)}
  const memo=new Map([[0n,true]]);
  function can(s){if(memo.has(s))return memo.get(s);let v=0;while(!(s&bit(v)))v++;let t=s^bit(v),a=t&adj[v],ok=false;while(a){let q=a&-a;a^=q;if(can(t^q)){ok=true;break}}memo.set(s,ok);return ok}
  let out=[];for(let b=0;b<1<<ports.length;b++){if(pop(b)%2)continue;let s=(1n<<BigInt(n))-1n;ports.forEach(([i,j],k)=>{if(b>>k&1)s^=bit(p[i][j])});if(can(s))out.push(b)}return out
 }
 function direct(masks,links,ports){
  let out=[];for(let b=0;b<1<<ports.length;b++){if(pop(b)%2)continue;let ok=false;
   for(let z=0;z<1<<links.length;z++){let a=masks.map(()=>0);links.forEach(([i,x,j,y],k)=>{if(z>>k&1){a[i]|=1<<x;a[j]|=1<<y}});ports.forEach(([i,j],k)=>{if(b>>k&1)a[i]|=1<<j});if(a.every((v,i)=>ix(v)>=0&&(masks[i]>>ix(v)&1))){ok=true;break}}
   if(ok)out.push(b)
  }return out
 }
 let cases=0,labels=0,seed=783;
 function check(m,l,p){let a=matchingRelation(m,l,p),b=direct(m,l,p);if(a.join()!=b.join())throw Error(JSON.stringify({m,l,p,a,b}));cases++;labels+=1<<(p.length-1)}
 for(let m=0;m<16;m++)check([m],[],[[0,0],[0,1],[0,2]]);
 for(let a=1;a<16;a++)for(let b=1;b<16;b++)check([a,b],[[0,2,1,2]],[[0,0],[0,1],[1,0],[1,1]]);
 function rand(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return 1+(seed>>>8)%15}
 for(let n of [4,6,8]){let l=Array.from({length:n},(_,i)=>[i,1,(i+1)%n,0]),p=Array.from({length:n},(_,i)=>[i,2]);for(let k=0;k<64;k++)check(Array.from({length:n},rand),l,p)}
 function covered(n,cycle){let es=Array.from({length:cycle?n:n-1},(_,i)=>(1<<i)|(1<<((i+1)%n))),s=new Set();for(let m=0;m<1<<es.length;m++){let a=0,ok=true;for(let j=0;j<es.length;j++)if(m>>j&1){if(a&es[j]){ok=false;break}a|=es[j]}if(ok)s.add(a)}return [...s].sort((a,b)=>a-b)}
 return {cases,evenBoundaryLabels:labels,localMasks:16,twoVertexCases:225,cycleCases:192,path6:covered(6,false),cycle6:covered(6,true),failures:0}
}
console.log(JSON.stringify(verify(),null,2));
```

Actual output: {"cases":433,"evenBoundaryLabels":12616,"localMasks":16,"twoVertexCases":225,"cycleCases":192,"path6":[0,3,6,12,15,24,27,30,48,51,54,60,63],"cycle6":[0,3,6,12,15,24,27,30,33,39,45,48,51,54,57,60,63],"failures":0}.

## 5. Continuation

Study six-cut relations with even cycles: characterize which principal-minor cancellation patterns can arise from a matching graph; seek a constructive finite dictionary or certified forbidden examples. Investigate weighted matching for a fixed prefix and whether matching representation provides an efficient universal-reserve optimizer (not implied by single-prefix polynomial feasibility). R782's end-to-end DP benchmark remains open. Preserve all signed BRC, event order, provenance, multiplicities and native three-dimensional slice/common-depth observers separately. Matching and skew matrices are auxiliary finite structural representations, not native spatial dimensions or a replacement for typed BRC.
