# R791 — Minimum-rank envelope: exact typed multiprefix dominance and an exponential information obstruction

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R783_R786_R790_AND_EDMONDS / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own session metadata r3-20261125-1624-own-metadata-v1: existing registration, no runs, execution_authorized=false. Owner inventory r3-20261125-1624-owner-read-v1 SUCCEEDED, snapshot INV-c2af691a4c0a7a05025fece2ffdbda79 as of 2026-11-25T08:27:14Z, filtered RUNNING list empty, execution_authorized=false. No formal Task/CLAIM/Result changed. Frozen pin a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer preservation blob 3923890d77a02d84b772f789e6912dd14f220d14 directly read. ACTIVE worldview and current portable/continuation/method rules read. Account canonical entry snapshot 0d9b8b33d82ca4f1264aa8d151a0ea6f93f8cafa both entries verified. Scope: unsigned Boolean auxiliary boundary relations, not native signed BRC, weights, source, temporal order, counts or X6 common depth.

Sources:
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md
- c7b233960d24c33525572bd3c4d9b9663f2b830f:research_notes/portable_direct/R786_ASYMMETRIC_K33_DICTIONARY_AND_RANK_CAPACITIES.md
- 05e776b722640728801b1c9810a2cd4e22a4b87f:research_notes/portable_direct/R789_BIPARTITE_LINKAGE_AND_CANONICAL_DEFICIT_CORE.md
- a3e96f54e9d060baf3a04cc227951f62e2bc7fea:research_notes/portable_direct/R790_GALLAI_EDMONDS_BIPARTITE_WITNESS.md
- Standard Edmonds matroid intersection min-max theorem: Goemans, MIT 18.997 lecture 11, 16 March 2004, https://studylib.net/doc/13660952/lecture--11 ; related external oracle research https://arxiv.org/abs/2209.14516 . Classical theorem is reused, not claimed novel.

## 1. Typed family of residual relations
Let T have b labeled terminals, fix a twist A subset T and an integer r in [0,b] with r congruent to |A| mod 2. Each nonempty fixed-prefix real Boolean relation E_i is required to satisfy: B_i={A symmetric-difference D:D in E_i} is the basis family of a rank-r matroid M_i. Sufficient structural condition: choose feasible u_i, the normalized exchange graph L_{u_i} is bipartite with sides P_i=A symmetric-difference u_i and its complement, and |P_i|=r. R786 gives this directly by using [I C] after normalization; R790 provides a bipartite witness. This permits different baselines; it does not require a common feasible deletion assignment. The original typed observation is T_F(E)=1 iff for EVERY prefix i, E_i intersects E. Families are nonempty finite lists of individually realizable fixed-prefix relations. Simultaneous realization of an arbitrary list as the complete prefix population of one network at one reserve is not assumed.

Define rho_F(W)=min_i rank(M_i,W), for every W subset T. Let G be another nonempty typed family with the same A and r. The exact worst pair common-independent size is
    min_{i,j} max{|I|: I independent in M_i and N_j}
      = min_{W subset T} [rho_F(W)+rho_G(T minus W)].
By Edmonds, the inner maximum equals min_W [r_i(W)+s_j(T minus W)]. All three minima are finite and commute; for fixed W the two prefix choices are independent. Thus universal compatibility (for every i,j there exists a common feasible deletion D, which may depend on both prefixes) is equivalent to every cut sum being at least r. The exact worst pair deficit is r minus the displayed minimum. A minimizing W and individually minimizing i,j are a certificate of a failing pair when the deficit is positive. A witness of compatibility is not a universal common D. Even two distinct singleton basis matroids can each meet a uniform exterior with different choices and have no common base across all prefixes.

## 2. Exact typed dominance and minimal sufficient coordinate
For a single real exterior of the same type, with rank function s, T_F(E)=1 iff rho_F(W)+s(T minus W)>=r for all W. Therefore rho_F>=rho_G pointwise implies T_F>=T_G for all typed exteriors.
Conversely assume rho_F(W)<rho_G(W), and put k=rho_G(W). Construct the test basis family of all r-subsets S with |S intersect W|>=k. It is the transversal matroid of r slots, k slots accepting only labels in W, r-k slots accepting any label. Because k<=min(|W|,r), this family is nonempty. A rank-r matroid M has a basis in this test family iff rank(M,W)>=k: a largest independent subset of W extends to a basis, and the reverse is immediate.
The test is a real Port exterior, not an abstract arbitrary subset. Build a bipartite graph with r slot vertices, b labeled vertices l_t and b sockets s_t. Join each l_t to s_t, and connect each slot to sockets of its allowed labels. Deletion of labels S forces all remaining l_t to their sockets, and leaves exactly the sockets of S to be matched to slots. Twist terminals by A using the private leaf gadget of R790, giving deletion relation {S symmetric-difference A}. Total vertices r+2b+|A| are even, by the parity condition, and R783 converse realizes it. Hence T_G(test)=1 but T_F(test)=0.
Consequently, exact dominance on ALL complete real exteriors of this type is equivalent to rho_F>=rho_G. Equality of the envelope is exactly observer equivalence on this class. Threshold tests recover every coordinate of rho_F; this is an observationally minimal quotient, not a minimal fixed-length encoding or a proof for arbitrary exterior types. It applies to multiprefix exterior families by conjunction. Partial compositions that leave the class require separate proof.

An envelope need not be a matroid rank: on T={1,2}, r=1, take matroids with unique bases {1} and {2}. The envelope vanishes on either singleton, equals 1 on T and 0 on empty, violating submodularity. Thus treating the worst-prefix envelope as one ordinary R789 rank oracle is invalid. R789 nevertheless evaluates each constituent rank via flow after the R790 preprocessing; an envelope query uses at most the number of constituent oracles and may terminate at a known lower bound.

## 3. Exponential information lower bound for arbitrary typed lists
For 1<=r<b, let U be the uniform rank-r matroid. For every r-subset Q, construct M_Q with every r-subset except Q a basis. It has r-1 unrestricted slots and one slot accepting only T minus Q. These are individually real fixed-prefix relations by the graph construction above, size O(br) edges and O(b+r) vertices.
Its rank coincides with U on every W except W=Q, where it is r-1. Proof: smaller subsets extend to an r-set different from Q (since b>r), larger subsets contain an r-set different from Q, and at size r only Q is excluded. For each collection X of r-subsets let F_X contain U and M_Q for Q in X. Then rho_FX(W)=min(r,|W|) except on members of X, where it is r-1. Hence there are exactly 2^C(b,r) distinct envelopes in this constructed family, and the same number of typed observational equivalence classes: a test with the unique basis Q (all r slots restricted to Q) distinguishes membership of Q in X. Every M_Q included has its own independent coordinate and cannot be deleted from that list without changing the observer.
Any uniform exact fixed-length encoding for all such arbitrary lists needs at least C(b,r) bits. Taking b even, r=b/2, and |A|=r yields C(b,b/2)>=2^b/(b+1). This lower bound is for arbitrary finite lists of individually real relations; it does not establish that exponentially many independent prefixes are generated by a single small Port network, nor rule out compact encodings for structured prefix populations. There are at most 2^b envelope coordinates, each an integer in [0,r]; the actual family may be given as a list of polynomial-size witnesses and evaluated lazily. No universal polynomial bound in b alone for exact typed family observation.

## 4. Different bipartitions and direct pair compatibility
For arbitrary two fixed-prefix matching deletion witnesses H,K on the same seam labels, take disjoint graphs and connect corresponding terminal pairs by one edge per label. A perfect matching selects a subset D of seam edges; both local graphs must then match after deleting D. Conversely any common D extends to a perfect matching. For partial gluing, retain other labels as terminals; prescribed external deletions commute with this construction. This preserves exact Boolean relation with no enumeration of D, even when the witness graphs have incompatible bipartitions. Thus explicit families of sizes p,q can be checked by at most pq general matching decisions (with early failure), with graph size linear in their pair input size; no claim of polynomial cost in a compact encoding of exponentially many prefixes. If both witnesses are bipartite, orient each connected component independently; seam edges remain bipartite iff the resulting component flip XOR equations are consistent. One can test consistency by traversal. Given a spanning forest in the component seam multigraph, satisfy all its equations; enumerate subsets of the inconsistent nonforest seams as forced matching edges, delete their endpoints, and remove all remaining inconsistent seams. Each surviving graph is bipartite; perfect matching existence is the disjunction over these branches. At most 2^k bipartite decisions with k the number of inconsistent seams after this orientation, at most the cycle rank of the multigraph. General matching remains polynomial for arbitrary k; no measured speed advantage claimed. Empty fixed relations are immediate failure. This gives an exact fallback for mixed types, not a single mixed-type rank envelope.

## 5. Executed exact verification
All calculations are JS integer/BigInt. Enumerate all 225 ordered pairs of nonempty slot neighborhoods on four labels, compare independent matching-witness augmenting path implementation against slot assignment recursion on all 16 deletion masks, deduplicate nonempty basis families. Then form all unordered pairs with repetition of the 36 distinct relations (includes singletons), compare dominance by full actual exterior signature versus coordinatewise envelope, and universal compatibility by direct basis intersection versus rank cuts. Count non-submodular envelopes over these family instances, not unique profiles. Finally verify all 64 constructed lower-bound families. Finite tests support implementation; general claims follow the analytic proofs above.
```json
{
  "b": 4,
  "r": 2,
  "slotConfigurations": 225,
  "graphChecks": 3600,
  "matroids": 36,
  "matroidPairChecks": 1296,
  "families": 666,
  "dominanceChecks": 443556,
  "universalChecks": 443556,
  "nonSubmodular": 376,
  "distinctEnvelopes": 280,
  "distinctSignatures": 280,
  "lowerBoundFamilies": 64,
  "lowerBoundDistinctProfiles": 64,
  "lowerBoundDistinctSingletonSignatures": 64
}
```
```js
function replay(){
 const b=4,r=2,T=(1<<b)-1,A=3,pop=x=>{let n=0;while(x){x&=x-1;n++}return n};
 const bs=Array.from({length:T+1},(_,x)=>x).filter(x=>pop(x)===r);
 const masks=new Map();
 function slotAccept(S,slots){const a=[];for(let i=0;i<b;i++)if(S>>i&1)a.push(i);if(a.length!==slots.length)return false;function rec(j,used){if(j===a.length)return true;return slots.some((w,k)=>!(used>>k&1)&&(w>>a[j]&1)&&rec(j+1,used|1<<k))}return rec(0,0)}
 function graphAccept(D,slots){const rows=Array.from({length:r+b},()=>[]);for(let j=0;j<r;j++)for(let t=0;t<b;t++)if(slots[j]>>t&1)rows[j].push(t);let delL=new Set(),delR=new Set(),next=b;for(let t=0;t<b;t++){rows[r+t].push(t);if(A>>t&1){rows[r+t].push(next);if(D>>t&1)delR.add(next);next++}else if(D>>t&1)delL.add(r+t)}if(rows.length-delL.size!==next-delR.size)return false;let mate=Array(next).fill(-1);function aug(i,seen){for(let j of rows[i])if(!delR.has(j)&&!seen[j]){seen[j]=1;if(mate[j]<0||aug(mate[j],seen)){mate[j]=i;return true}}return false}for(let i=0;i<rows.length;i++)if(!delL.has(i)&&!aug(i,Array(next).fill(0)))return false;return true}
 let graphChecks=0;
 for(let x=1;x<=T;x++)for(let y=1;y<=T;y++){let slots=[x,y],m=0;for(let j=0;j<bs.length;j++)if(slotAccept(bs[j],slots))m|=1<<j;if(m&&!masks.has(m))masks.set(m,slots);for(let d=0;d<=T;d++){if(graphAccept(d,slots)!==slotAccept(A^d,slots))throw Error("graph");graphChecks++}}
 const ms=[...masks.keys()].sort((a,b)=>a-b),rank=m=>Array.from({length:T+1},(_,w)=>Math.max(...bs.filter((_,j)=>m>>j&1).map(s=>pop(s&w))));
 const rr=ms.map(rank);let matroidPairChecks=0;for(let i=0;i<ms.length;i++)for(let j=0;j<ms.length;j++){let k=Math.min(...rr[i].map((v,w)=>v+rr[j][T^w]));if((k===r)!==Boolean(ms[i]&ms[j]))throw Error("minmax");matroidPairChecks++}
 const fs=[];for(let i=0;i<ms.length;i++)for(let j=i;j<ms.length;j++){const rho=rr[i].map((v,w)=>Math.min(v,rr[j][w]));let sig=0n;for(let k=0;k<ms.length;k++)if((ms[i]&ms[k])&&(ms[j]&ms[k]))sig|=1n<<BigInt(k);fs.push({i,j,rho,sig})}
 let dominanceChecks=0,universalChecks=0,nonSubmodular=0;
 for(let f of fs){let bad=false;for(let x=0;x<=T;x++)for(let y=0;y<=T;y++)if(f.rho[x]+f.rho[y]<f.rho[x&y]+f.rho[x|y])bad=true;if(bad)nonSubmodular++}
 for(let f of fs)for(let g of fs){if(((f.sig|g.sig)===f.sig)!==f.rho.every((v,w)=>v>=g.rho[w]))throw Error("dominance");dominanceChecks++;let direct=[f.i,f.j].every(i=>[g.i,g.j].every(j=>ms[i]&ms[j]));let cut=Math.min(...f.rho.map((v,w)=>v+g.rho[T^w]));if(direct!==(cut===r))throw Error("family cut");universalChecks++}
 const all=(1<<bs.length)-1,profiles=new Set(),lowerTests=new Set();for(let z=0;z<=all;z++){let family=[all];for(let j=0;j<bs.length;j++)if(z>>j&1){let m=all^(1<<j);if(!masks.has(m))throw Error("missing witness");family.push(m)}let rho=Array.from({length:T+1},(_,w)=>Math.min(...family.map(m=>rank(m)[w])));profiles.add(rho.join(","));let s=0;for(let j=0;j<bs.length;j++)if(family.every(m=>m>>j&1))s|=1<<j;lowerTests.add(s)}
 return {b,r,slotConfigurations:T*T,graphChecks,matroids:ms.length,matroidPairChecks,families:fs.length,dominanceChecks,universalChecks,nonSubmodular,distinctEnvelopes:new Set(fs.map(f=>f.rho.join(","))).size,distinctSignatures:new Set(fs.map(f=>String(f.sig))).size,lowerBoundFamilies:all+1,lowerBoundDistinctProfiles:profiles.size,lowerBoundDistinctSingletonSignatures:lowerTests.size}
}
console.log(JSON.stringify(replay(),null,2));
```

## 6. Next unresolved problem
Find source-level conditions under which a single Port network's implicitly generated prefix population has a tractably evaluable envelope or a small structured generating family. Determine whether different types can be covered by a small number of common twists without losing real distinguishing exteriors. Develop joint cut optimization only with proof or counterexample; the minimum envelope is not generally submodular. The arbitrary-list lower bound above is not a lower bound on compact shared-network input. Preserve native signed BRC and all previously excluded observer data independently.
