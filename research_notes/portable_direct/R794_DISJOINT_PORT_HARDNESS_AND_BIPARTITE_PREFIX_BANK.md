# R794 — Disjoint Port hardness and optimal bipartite prefix banks

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779_R783_R792_R793 / EXACT_JS_CHECKED / NOT_REVIEWED.
Independent continuation, Researcher EM-DIRECT-82A007 / TASK_RESEARCH, Activity RA-708BCC309CE076D8BB599B91. Own recovery r3-20261125-1920-own-metadata-v1 confirms original registration, no own RUN, execution_authorized=false. Owner inventory r3-20261125-1920-owner-read-v1 last observed RUNNING (inventory job, not an inference of any active owner). No shared claim or task state changed.
Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer contract blob 3923890d77a02d84b772f789e6912dd14f220d14 read; generated foundation package unavailable (404). ACTIVE worldview and current continuation, portable, BRC and mathematical-evidence policies consulted. Global canonical entry blobs checked at main@8b8d686fad146d48eebfb971c45dcb980d1035b3.

Exact predecessors:
- R779 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md (even triples and fixed local gadgets).
- R783 236e6fea7374ac883a0fe12e2083cfcb31ada64b:research_notes/portable_direct/R783_MATCHING_REPRESENTATION_AND_SPARSE_BOUNDARY.md (matching-to-Port converse).
- R792 6dcc39ca328ee24ca8493100a27cc1bf209b7446:research_notes/portable_direct/R792_SHARED_PORT_PREFIX_VERTEX_COVER.md.
- R793 3be90c3aeb22a33abb3d1c57ec04ce423952b0f2:research_notes/portable_direct/R793_MIXED_RANK_AND_CUT_ORIENTATION_PRUNING.md.

## 1. Exact minimum bank for every bipartite source

Use the R793 typed, level-m mixed envelope and cut-cover criterion, with singleton orientations choosing an endpoint of each source edge. An orientation covers I iff all edges crossing I point outside I. Let C be ANY vertex cover. For each H subset C choose an orientation as follows. On an edge whose endpoints both lie in C with unequal H membership, direct from the member of H to the nonmember; otherwise orient arbitrarily if both in C. On an edge from c in C to v outside C, orient toward v if c in H, toward c otherwise. There is no edge with both endpoints outside C.

For any cut I choose H=I intersect C. On every crossing edge the orientation points outside I: for an edge internal to C the unequal memberships fix it; for an edge with exactly one endpoint in C the membership of that endpoint fixes it. The resulting 2^|C| orientations therefore cover all cuts and preserve the entire declared mixed envelope by R793. No enumeration of 2^n cuts or 3^m prefixes is required for bank construction. Duplicates may be removed. With a minimum cover this proves N_min(G)<=2^tau(G). Combined with R793's 2^nu(G) lower bound and classical Konig equality tau=nu for bipartite G:
    N_min(G)=2^nu(G) for every bipartite G.
This includes arbitrarily large forests, cycles of even length, complete bipartite graphs, and disconnected bipartite graphs. A minimum cover is computed from a maximum matching, and the bank can be streamed in O(m+n) per orientation. The bank length itself may be exponential. For general G this is a further upper bound, not equality. The actual scope is the R793 rank-m observation envelope and exterior family; full extra levels, counts and prefix provenance are not erased.

## 2. Hardness of robust composition with a disjoint interior

R792 put the source graph's vertex-cover difficulty in the shared public label slots of the interior. We show the same coNP-completeness with the interior reduced to m independent one-vertex Port components. Each fixed-prefix interior rank is a direct sum of rank-one slots on disjoint labels, and its complete mixed rank envelope has a linear-time formula. The difficulty is then entirely in exterior coupling across the independent choices.

Take ANY simple input graph G=(V,E), m>=1, n=|V|; threshold t with 0<=t<=min(m,n). Make a NEW source graph F of m disjoint edges, with distinct endpoint labels u_e,v_e for each e=uv, and private labels a_e. The two endpoint labels carry group names u and v respectively; labels themselves remain distinct. Reuse R792's exact local even-triple gadget p=t_local=1,w=0, normalized at private-only. Each prefix admits private-only, and one or both endpoint singletons; if exactly one endpoint singleton is admitted the triple may also be admitted. Each local prefix excludes precisely one of the three nonbaseline patterns. All 3^m prefixes are independently realized, with one fixed target and reserve. Here there are no shared label trees because all 3m labels are distinct. Write S=A xor D, A={a_e}. Full local states have 1 or 3 selected labels.

Construct a fixed exterior with these precise admissible S:
    S contains only public endpoint labels, |S|=m, and at least t distinct group names occur in S.
Put k=m-t, q=n+k>=m. Make n group-specific slots, each adjacent to endpoint labels with that group name, and k wildcard slots adjacent to all endpoint labels. Require S to be injectively assigned to slots, filling unused slots by q-m universal filler labels. A set of m distinct public labels is assignable iff it contains at least t distinct group names: at most one per group can use a group slot, and the others must use at most k wildcard slots; conversely use one group slot for each present group and assign all remaining labels to wildcard slots, then fill unused slots. This is exact, including t=0 and isolated original graph vertices.

The fixed exterior is REAL in the R783 Port class, not an abstract set oracle. Explicit deletion graph H has each a_e as an isolated terminal (it must be deleted); for each of the 2m public labels j make terminal j and copy j' joined by an edge; all q slot vertices are on the same side as j, with the stated slot adjacencies to j'; q-m universal filler vertices on the copy side are adjacent to every slot. No other edges. For D=A xor S, the private terminals force S to avoid A. Undeleted public terminals force their copy edges; deleted public terminals free the corresponding copies. The remaining bipartite graph admits a perfect matching iff |S|=m and those free copies can be assigned to the slots, with all filler vertices matched. H has 4m+2q vertices, O(m+n) vertices, and at most 2m+2m(k+1)+q(q-m) edges (the middle bound safely counts specific and wildcard adjacencies), polynomial in G. For a nonempty exterior relation R783 gives the fixed p=0 subcubic Port realization in linear size in H. An empty relation can be implemented by an inconsistent fixed component as in R783. In fact the exterior is nonempty iff at least t nonisolated group names exist; for hardness restrict to G without isolated vertices (delete them initially). The formula and construction also work for isolated vertices; threshold exceeding nonisolated group count simply yields empty exterior. No uncertain exterior prefix or additional quantifier is introduced.

Now each compatible interior state must use precisely one public label per local slot: the exterior rejects the private-only and triple states (both contain a_e), and accepts only the fixed-size layer. A singleton-endpoint prefix chooses a unique S. Its group set is exactly a vertex cover of G, since each original edge has one chosen endpoint. Conversely any cover C can direct each original edge toward a member of C; a minimum cover can be realized exactly (otherwise the smaller selected set contradicts minimality). Thus the minimum group count over singleton prefixes is tau(G). Two-endpoint prefixes admit a singleton refinement, so if every singleton prefix is compatible then every actual prefix is compatible. If some singleton fails, it is itself an actual prefix. Consequently:
    forall actual prefixes x exists compatible lift  <=>  tau(G)>=t.
The worst-prefix maximum achievable group count is exactly tau(G).

Complement Vertex Cover decision is coNP-complete (use t=l+1 for threshold l; handle trivial out-of-range inputs). Reduction is polynomial, using no exponential input table. Noncompatibility for this constructed class has a certificate consisting of one failing prefix, with polynomial fixed-prefix perfect-matching check by R783, so robust compatibility is coNP-complete for the constructed class. This extends R792: the interior F is a matching (treewidth one), the exterior has no uncertain prefixes and has a bipartite matching witness; its couplings carry the arbitrary input graph. The statement is not a hardness claim for fixed arbitrary exterior or for bounded treewidth of the *glued* network. This proof operates on the entire actual local Port population; the specific exterior isolates the public-only layer without deleting other states in storage.

In particular F has nu(F)=m; by section 1 its optimal explicit level-m bank is 2^m and its mixed rank envelope can be computed by R793 in O(m) (each surviving internal edge contributes one). Hence fast single-query rank evaluation, trivial interior components and a fixed exterior do not imply a fast robust gluing decision. A sufficient hypothesis for future algorithms must control cross-interface group coupling or the joint graph, not just the interior treewidth.

## 3. Exact computational replay

The dependency-free JS below was executed twice (once separately, once to generate this source). All nonempty simple labeled input graphs on 2--4 vertices: enumerate all ternary prefixes and all three allowed local patterns per slot, INCLUDING triples. For each graph, independently run bipartite augmenting-path perfect matching on the actual deletion graph for every potentially admissible local-state union and every public m-subset (including those not choosing one endpoint per slot), at each t from 0 to min(m,n); test all resulting robust thresholds against exhaustive minimum vertex cover. For every nonempty bipartite labeled graph on 2--5 vertices, compare brute minimum vertex cover to brute maximum matching, and independently check that the explicit cover bank hits every cut. Finite validation only on these domains. General-size conclusions use the proofs. No native signed BRC/amplitude or dynamics calculation is asserted.

Executed result:
```json
{
  "graphs": 71,
  "prefixes": 4161,
  "localStates": 1001007,
  "exteriorChecks": 92786,
  "robustChecks": 268,
  "bipartiteGraphs": 422,
  "bankCutChecks": 12692,
  "bankOrientations": 1500,
  "discrepancies": 0
}
```
```javascript
function replay(){
 const pc=x=>{let a=0;while(x){x&=x-1;a++}return a};
 const check=(p,s)=>{if(!p)throw Error(s)};
 let graphs=0,prefixes=0,localStates=0,exteriorChecks=0,robustChecks=0,bipartiteGraphs=0,bankCutChecks=0,bankOrientations=0;
 function cover(n,E){let best=(1<<n)-1;for(let s=0;s<1<<n;s++)if(pc(s)<pc(best)&&E.every(([u,v])=>(s>>u&1)||(s>>v&1)))best=s;return best}
 function perfect(n,E){let best=0;function f(j,s,k){if(j===E.length){best=Math.max(best,k);return}f(j+1,s,k);let [u,v]=E[j],d=(1<<u)|(1<<v);if(!(s&d))f(j+1,s|d,k+1)}f(0,0,0);return best}
 for(let n=2;n<=5;n++){
  const pairs=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)pairs.push([u,v]);
  for(let g=1;g<1<<pairs.length;g++){
   let E=pairs.filter((_,j)=>g>>j&1),m=E.length,C=cover(n,E),tau=pc(C);
   let bip=false;for(let s=0;s<1<<n;s++)if(E.every(([u,v])=>((s>>u)^(s>>v))&1)){bip=true;break}
   if(bip){bipartiteGraphs++;check(perfect(n,E)===tau,"Konig");let bank=[];for(let h=C;;h=(h-1)&C){let o=E.map(([u,v])=>{if(C>>u&1)return h>>u&1?v:u;return h>>v&1?u:v});bank.push(o);if(!h)break}check(bank.length===2**tau,"bank size");bankOrientations+=bank.length;
    for(let s=0;s<1<<n;s++){check(bank.some(o=>E.every(([u,v],j)=>!(((s>>u)^(s>>v))&1)||!(s>>o[j]&1))),"cut");bankCutChecks++}
   }
   if(n>4)continue;
   graphs++;const B=3*m,publicMask=(1<<(2*m))-1,grp=E.flat(),ts=Math.min(m,n);
   const states=new Set();function all(j,s){if(j===m){states.add(s);return}let u=1<<(2*j),v=1<<(2*j+1),a=1<<(2*m+j);for(let x of [a,u,v,a|u|v])all(j+1,s|x)}all(0,0);
   for(let s=0;s<=publicMask;s++)if(pc(s)===m)states.add(s);
   const signatures=new Map();
   for(let s of states){
    let labels=0;for(let j=0;j<2*m;j++)if(s>>j&1)labels|=1<<grp[j];
    let sig=0;
    for(let t=0;t<=ts;t++){
     let k=m-t,q=n+k,d=q-m;
     // Direct deletion graph: isolated private terminals, public terminal-copy edges,
     // q slot vertices and d universal filler vertices on the right.
     let L=[],R=2*m+d;
     for(let j=0;j<2*m;j++)if(!(s>>j&1))L.push([j]);
     for(let j=0;j<q;j++){let a=[];for(let i=0;i<2*m;i++)if(j>=n||grp[i]===j)a.push(i);for(let f=0;f<d;f++)a.push(2*m+f);L.push(a)}
     let ok=false;
     if(!(s&~publicMask)&&L.length===R){
      let match=new Int32Array(R).fill(-1);
      function aug(i,seen){for(let v of L[i])if(!seen[v]){seen[v]=1;if(match[v]<0||aug(match[v],seen)){match[v]=i;return true}}return false}
      ok=L.every((_,i)=>aug(i,new Uint8Array(R)));
     }
     check(ok===(!(s&~publicMask)&&pc(s)===m&&pc(labels)>=t),"exterior");
     if(ok)sig|=1<<t;exteriorChecks++;
    }
    signatures.set(s,sig);
   }
   let robust=(1<<(ts+1))-1;
   for(let p=0;p<3**m;p++){
    prefixes++;let a=[],z=p;
    for(let j=0;j<m;j++){let u=1<<(2*j),v=1<<(2*j+1),h=1<<(2*m+j),c=z%3;z=Math.floor(z/3);let opts=[h,u,v,h|u|v];opts.splice(c===0?2:c===1?1:3,1);a.push(opts)}
    let sig=0;function f(j,s){if(j===m){sig|=signatures.get(s);localStates++;return}for(let x of a[j])f(j+1,s|x)}f(0,0);robust&=sig;
   }
   for(let t=0;t<=ts;t++){check(Boolean(robust>>t&1)===(tau>=t),"robust");robustChecks++}
  }
 }
 return {graphs,prefixes,localStates,exteriorChecks,robustChecks,bipartiteGraphs,bankCutChecks,bankOrientations,discrepancies:0};
}
console.log(JSON.stringify(replay(),null,2));
```

## 4. Next question

Seek a parameterized algorithm based on treewidth of the *combined* interior/exterior witness (not interior alone), with quantified local state transitions for forall prefix/exists lift. Separately seek fixed-rank local uncertain Port construction that removes triples for every prefix without deleting their effects by an observer choice; not solved here. Preserve signed/weighted BRC, provenance, multiplicity, temporal order, and native X6/three-axis common depth outside the auxiliary Boolean observer. No shared task closure, Result, Review, Working Truth or Foundation promotion.
