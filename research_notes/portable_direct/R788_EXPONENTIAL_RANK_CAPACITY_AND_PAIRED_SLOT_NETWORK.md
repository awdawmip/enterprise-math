# R788 — Exponential necessary rank-capacity dictionaries from a compact paired-slot network

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R783_R786_R787 / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R787. EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own session metadata r3-20261125-1320-own-metadata-v1 verified existing registration, no runs, execution_authorized=false. Owner read r3-20261125-1320-owner-read-v1 observed RUNNING before publication; no shared Task or CLAIM changed. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-relation contract 3923890d77a02d84b772f789e6912dd14f220d14 read; generated foundation startup package at pin returned 404. ACTIVE worldview and current portable/continuation rules read. Account entry snapshot main@93f1604658826d25b73ce1c3468de813e798b339. Scope: normalized fixed-prefix unsigned Boolean auxiliary Port relation; not native signed BRC, weights, counts, provenance, event order or X6 common depth.

Dependencies:
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md (matching deletion converse).
- c7b233960d24c33525572bd3c4d9b9663f2b830f:research_notes/portable_direct/R786_ASYMMETRIC_K33_DICTIONARY_AND_RANK_CAPACITIES.md (basis/rank representation).
- 683701d35e2da49c4aafe11839cee3110dfe7b1e:research_notes/portable_direct/R787_CYCLIC_FLAT_CAPACITY_AND_MATCHING_RANK.md (cyclic-flat reduction).

## 1. Question and theorem

R787 gives at most three rank inequalities for K3,3 and leaves higher-width growth open. For every even q=2k+2 >=4, construct a real matching-deletion/Port relation with b=2q terminal labels T grouped into q pairs P_i={a_i,b_i}, baseline A={a_1,...,a_q}, B=T\\A. In the basis coordinates S=A XOR D its feasible family is exactly

    |S|=q, f(S):=#{i:P_i subset S} <= k.

Equivalently every q-subset is a basis except the union of exactly q/2 pairs. Its pair-exchange graph is the complete bipartite K(q,q). Every exact representation by individual R786 rank inequalities |S intersect W|<=r(W), with |S|=q supplied, requires precisely binom(q,q/2) nontrivial inequalities. Yet the above pair-count formula is a single exact nonlinear cardinality constraint, with O(q) pair labels. This separates the size of a rank-inequality dictionary from compact structure-aware computation.

## 2. Explicit matching graph and proof

First make a graph G whose terminal element vertices are the 2q labels, whose q source vertices s_i are mandatory, and which has q private slots and k common slots. Split each slot into an in-vertex and out-vertex, joined by an edge. Connect every source to every slot in-vertex. Connect every slot out-vertex to the two elements of its own pair (private slot) or all 2q elements (common slot). Edges respect a bipartition (sources/slot-out on left, slot-in/elements on right). To normalize at A, append a leaf to each b_i, and regard those leaves, instead of their adjacent b_i, as the B-side deletion terminals; a_i remain deletion terminals. Call the resulting even-order graph H. For D subset T, set S=A XOR D. The mandatory leaf at each b_i not in S forces its b_i to match to that leaf; a_i outside S is deleted. Every selected element in S therefore needs a distinct slot out-vertex, while each source needs a distinct slot in-vertex. A slot unused by sources must match its in/out vertices together, and a slot used by a source must match its out-vertex to a selected element. Thus |S|=q is necessary, and feasibility is precisely assignment of its q elements to distinct slots. For each hit pair use its private slot for one chosen element; every fully selected pair needs one common slot. Necessity follows as each fully selected pair can use at most one private slot and shares the k common slots. Conversely this allocation suffices, and every q occupied slot in-vertex may match an arbitrary distinct source. Therefore H-D has a perfect matching exactly under the stated constraint. H has 6q+2k vertices and O(q^2) edges. H has a perfect matching at D=empty. R783 converse realizes this even-order matching relation by auxiliary trivalent Port gadgets with polynomial size. No unrestricted skew-matrix realizability assumption is used.

For any pair toggle of one a_i and one b_j, S has at most one full pair, feasible since k>=1. Two A-side or two B-side toggles violate size. Hence the complete K(q,q) graph is fixed. A set of size q can have at most q/2=k+1 full pairs; if it has k+1, it consists entirely of those pairs. All others are feasible.

## 3. Exact ranks and sharp exponential lower bound

For W subset T put h(W)=#{i:W intersects P_i}. For the untruncated assignment to private/common slots, maximum matching of elements of W to slots has size min(|W|,h(W)+k): first allocate one element of each hit pair to its private slot, then allocate up to k second elements. With q sources the maximum extendible independent set size is

    r(W)=min(q, |W|, h(W)+k).

Indeed any independent selection of <=q elements with <=k full pairs extends to size q by adding one element from each still unused pair until it reaches q (there are q pairs). This identifies the rank with the R786 basis rank, not merely a matching upper bound.

For |W|<q, h(W)+k>=|W| because floor(|W|/2)<=k. For |W|=q, rank drops to q-1 precisely when W is a union of k+1 full pairs. For |W|>q, h(W)>=ceil(|W|/2)>=k+2, hence rank q. Consequently the ONLY non-tautological individual rank inequalities on q-element candidates are

    |S intersect F| <= q-1,   F=union_{i in I} P_i, |I|=q/2.

Each excludes exactly its own candidate F. They are all indispensable, even allowing all W, not just cyclic flats. Each F is a circuit (all proper subsets independent) and a hyperplane (adding any outside element increases rank), thus a cyclic flat. The exact minimum is binom(q,q/2). It is at least 2^q/(q+1)=2^(b/2)/(b/2+1) by the binomial sum and maximal central term. This is an exponential lower bound for the NUMBER OF INDIVIDUAL RANK INEQUALITIES in this real network family, not a lower bound for arbitrary encodings or runtime. In fact f(S)<=k is a polynomial-size exact alternative with O(q) membership work. R787 compression is still exact but cannot be uniformly polynomial-size as an explicit list of its inequalities. The compact pair-count formula preserves the entire single-prefix relation and therefore every Boolean gluing operation that uses it as input; no weights or multiprefix information are discarded.

## 4. Exact finite replay

Independent bipartite augmenting-path matching on explicit H (all 2^(2q) normalized boundary possibilities, enumerated equivalently as S), independent ranks from all feasible bases via downward submask marking and max-subset propagation, compared against closed formula for every W; all cross-pair toggles checked. The relevant rank sets were compared exactly with the list of forbidden bases. No floating-point arithmetic. q=4,6,8:

```json
[
  {
    "q": 4,
    "k": 1,
    "b": 8,
    "allMasks": 256,
    "bases": 64,
    "nonbases": 6,
    "nontrivialRankConstraints": 6,
    "rankChecks": 256,
    "pairChecks": 16
  },
  {
    "q": 6,
    "k": 2,
    "b": 12,
    "allMasks": 4096,
    "bases": 904,
    "nonbases": 20,
    "nontrivialRankConstraints": 20,
    "rankChecks": 4096,
    "pairChecks": 36
  },
  {
    "q": 8,
    "k": 3,
    "b": 16,
    "allMasks": 65536,
    "bases": 12800,
    "nonbases": 70,
    "nontrivialRankConstraints": 70,
    "rankChecks": 65536,
    "pairChecks": 64
  }
]
```

Reproduction (Node/JS, no packages):
```js
function verify(){
 const pop=x=>{let n=0;while(x){x&=x-1;n++}return n};
 let rows=[];
 for(const q of [4,6,8]){
  const k=q/2-1,b=2*q,N=1<<b,A=Array.from({length:q},(_,i)=>1<<(2*i)).reduce((x,y)=>x|y,0),s=q+k;
  // Left: q source nodes, s slot-out nodes, q leaf nodes. Right: s slot-in nodes, 2q element nodes.
  const adj=Array.from({length:q+s+q},()=>[]);
  for(let i=0;i<q;i++)for(let j=0;j<s;j++)adj[i].push(j);
  for(let j=0;j<s;j++){adj[q+j].push(j);for(let t=0;t<b;t++)if(j===Math.floor(t/2)||j>=q)adj[q+j].push(s+t)}
  for(let i=0;i<q;i++)adj[q+s+i].push(s+2*i+1);
  function match(S){
   let left=adj.map((_,i)=>i).filter(i=>i<q+s||!(S>>(2*(i-q-s)+1)&1));
   let rightOn=Array.from({length:s+b},(_,j)=>j<s||((j-s)%2===1)||Boolean(S>>(j-s)&1));
   if(left.length!==rightOn.filter(Boolean).length)return false;
   let own=Array(s+b).fill(-1);
   function aug(i,seen){for(const j of adj[i])if(rightOn[j]&&!seen[j]){seen[j]=true;if(own[j]<0||aug(own[j],seen)){own[j]=i;return true}}return false}
   return left.every(i=>aug(i,Array(s+b).fill(false)));
  }
  let bases=[],bad=[],pairChecks=0,rank=new Uint8Array(N);
  for(let S=0;S<N;S++){
   let full=0;for(let i=0;i<q;i++)if((S>>(2*i)&3)===3)full++;
   let expected=pop(S)===q&&full<=k;
   if(match(S)!==expected)throw Error(`match ${q} ${S}`);
   if(expected){bases.push(S);for(let T=S;;T=(T-1)&S){rank[T]=pop(T);if(!T)break}}
   else if(pop(S)===q)bad.push(S);
  }
  for(let i=0;i<b;i++)if(A>>i&1)for(let j=0;j<b;j++)if(!(A>>j&1)){if(!match(A^(1<<i)^(1<<j)))throw Error("pair");pairChecks++}
  for(let i=0;i<b;i++)for(let W=0;W<N;W++)if(W>>i&1)rank[W]=Math.max(rank[W],rank[W^(1<<i)]);
  let relevant=[];for(let W=0;W<N;W++){let hit=0;for(let i=0;i<q;i++)if(W>>(2*i)&3)hit++;let r=Math.min(q,pop(W),hit+k);if(rank[W]!==r)throw Error(`rank ${q} ${W}`);if(r<Math.min(q,pop(W)))relevant.push(W)}
  if(relevant.join()!==bad.join())throw Error("constraints");
  rows.push({q,k,b,allMasks:N,bases:bases.length,nonbases:bad.length,nontrivialRankConstraints:relevant.length,rankChecks:N,pairChecks});
 }
 return rows;
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next

Investigate a circuit/rank oracle representation for general asymmetric slot networks, where a family of capacity inequalities may be exponential but a polynomial-size matching/flow network can separate violations; compare compressed circuit families, laminar capacities and the actual R780 multi-prefix quotient. Investigate whether every bipartite normalized Port relation admits a polynomial-size directed linkage certificate relative to its original H (not established here). Preserve the distinction between output-size bounds, computation cost, and exact residual preservation. No independent review or formal acceptance claimed.
