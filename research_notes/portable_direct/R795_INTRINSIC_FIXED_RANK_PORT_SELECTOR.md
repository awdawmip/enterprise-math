# R795 — Intrinsically fixed-rank uncertain Port selector

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779_R792_R793_R794 / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation. Prior Researcher EM-DIRECT-82A007, Activity RA-708BCC309CE076D8BB599B91; own SID recovered by r3-20261125-2018-own-metadata, no own RUN, execution_authorized=false; owner inventory r3-20261125-2018-owner-read last observed RUNNING (job status, not active owner evidence). No shared state change. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14 read. ACTIVE worldview, canonical main entry files and portable/continuation/method rules consulted; common immutable global read snapshot not established. This is unsigned Boolean Port support, not native BRC dynamics.

Exact predecessors:
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 6dcc39ca328ee24ca8493100a27cc1bf209b7446:research_notes/portable_direct/R792_SHARED_PORT_PREFIX_VERTEX_COVER.md
- 3be90c3aeb22a33abb3d1c57ec04ce423952b0f2:research_notes/portable_direct/R793_MIXED_RANK_AND_CUT_ORIENTATION_PRUNING.md
- b38534886e5e6f19c5a2a4380cefb027b9776379:research_notes/portable_direct/R794_DISJOINT_PORT_HARDNESS_AND_BIPARTITE_PREFIX_BANK.md

## 1. Four-vertex switch and full support theorem

R792's one-vertex uncertain slot admitted additional triples, requiring a fixed cardinality observer. We construct a NEW local network, not an equivalence to the full old relation. It has four vertices X,U,V,M, internal edges X-U (s), X-V (t), U-M (j), V-M (k), boundary ports at U (u), V (v), M (a); X's third port is private with lift zero. All bits in this paragraph are lift bits z, with triple integer code first+2*second+4*third. The R779 local law is x XOR w XOR z in S(reserve), S(1)={3,5,6}; each local triple even. Set:
- X: ports (s,t,0), p=1, reserve=1, target w=5. Actual prefix x ranges over 3,5,6, independent of other slots.
- U: (s,u,j), p=0, reserve=1, w=3.
- V: (t,v,k), p=0, reserve=1, w=6.
- M: (j,k,a), p=0, reserve=1, w=6.
The three fixed vertices exclude one even triple each. Graph is loop-free subcubic with four internal edges.

Interpret selected labels S by u,v,1 XOR a; i.e. boundary D=A XOR S, A={a}. In raw selection-flow coordinates the switch routes exactly one unit: U parent 1 XOR s, V parent t, since s=t. Its two possible z triples are 0 and 3. At X, x=3 excludes 6 and permits both; x=5 excludes 0 and forces s=t=1 (V); x=6 excludes 3 and forces s=t=0 (U). At U, raw parent=1 XOR s, public child=u, private child=1 XOR j. The condition parent=public+private in integers with Boolean bits allows raw codes 0,3,5, which XOR 5 gives z codes 5,6,0, exactly exclusion 3. At V raw parent=t, children v,k, the same law gives codes 0,3,5, exactly exclusion 6. At M raw children 1 XOR j,k and parent 1 XOR a; parent=child1+child2 allows raw codes 0,5,6, XOR 5 gives z codes 5,0,3, exactly exclusion 6. Therefore exactly one unit reaches u,v or a. Either switch direction can send its unit through M to a. The entire projected support is:
 x=3: { {a},{u},{v} }; x=5: { {a},{v} }; x=6: { {a},{u} }.
No other boundary states exist, including triples. This holds for all prefixes with a single fixed target and reserve. Private-only A is a common feasible boundary basis (D empty), not necessarily a common internal lift: the two forced switch prefixes route it differently. The prefix x=3 has two distinct private lifts, so support equivalence does not preserve multiplicity. This is why one must not identify this construction with the old Port's full relation or with its counts.

## 2. Arbitrary source graph, no layer projection

Replace each R792 slot by this new switch. Reuse R792's binary count trees on common labels: parent=child1+child2 in {0,1}, normalize by the private-only baseline on boundary bits and internal tree bits; each such vertex excludes one even triple and is realized at p=0 with fixed target, reserve 1. Wire and isolated label gadgets as in R792. There is exactly one selected incidence per slot, and at most one per label. All 3^m prefixes remain independent and realized. For every prefix, the WHOLE boundary relation in the common A-twist is precisely the bases of its transversal matroid of rank m, with private labels proving nonemptiness and rank. No fixed-cardinality projection, no extra states to remove. Size O(n+m) for simple source graph, with four uncertain-slot gadget vertices per edge (one uncertain and three fixed). There is no change to an existing graph's full support: this is a new construction in the same Port class.

Therefore the R792 vertex-cover theorem now holds for the entire relation:
 min_x max_{D in E_x} |(A XOR D) intersect V| = tau(G).
Proof: choose an admitted public endpoint per edge, its distinct endpoint set is a cover, and a choosing slot for each endpoint gives a matching of that size; fill remaining slots privately. For the converse orient every edge toward a minimum cover, take forced endpoint prefixes, then no public label outside the cover is available. R793's mixed rank formula rho(U union A(P))=|P|+tau(G[U]-P) also applies without level restriction because the full basis families are identical to the old level-m families. Likewise R793/R794 prefix-bank conclusions apply to the complete common-type support for these NEW networks. R794's disjoint interior hardness extends to full fixed-rank common-base interior by using the same fixed exterior. Its private-label exclusion is still used to demand public choices, not to exclude spurious cardinality levels. These consequences use exact predecessor theorems, not new independent complexity reductions. R791 common-type hypotheses are now satisfied directly for the interior, including common reference basis. Fixed exteriors and all remaining native observers remain separately scoped.

## 3. Exact replay

Executed dependency-free JS: enumerate all 128 lift configurations (four internal and three boundary bits) per prefix, independently compute raw selected support from literal local XOR constraints; then compose those computed supports with the label uniqueness condition for all nonempty labeled simple graphs of 2--4 vertices. Compare every prefix's cardinality, common basis and minimum maximal public count to exhaustive vertex cover. This latter computation uses the proved count-tree semantics, not a direct enumeration of every expanded tree vertex. No native numerical or dynamics verification claimed.
Actual output:
{"table":{"3":[1,2,4],"5":[2,4],"6":[1,4]},"raw":{"3":4,"5":2,"6":2},"graphs":71,"prefixes":4161,"rankChecks":4161,"uniqueAssignments":122100,"extra":0}
Here uniqueAssignments counts distinct projected support states per configuration, summed over configurations, not distinct global states. raw counts full local lifts. General-size results follow from analytic argument.

```javascript
function replay(){
const even=[0,3,5,6], table={}, raw={};
for(const x of [3,5,6]){
 let out=new Set(),n=0;
 for(let b=0;b<128;b++){
  let [s,t,j,k,u,v,a]=Array.from({length:7},(_,i)=>(b>>i)&1);
  let z=[s+2*t,s+2*u+4*j,t+2*v+4*k,j+2*k+4*a];
  if(z.every(y=>even.includes(y))&&z[0]!=(x^5)&&z[1]!=3&&z[2]!=6&&z[3]!=6){out.add(u+2*v+4*(a^1));n++}
 }
 table[x]=[...out].sort();raw[x]=n;
}
if(JSON.stringify(table)!==JSON.stringify({3:[1,2,4],5:[2,4],6:[1,4]}))throw Error(JSON.stringify(table));
let graphs=0,prefixes=0,rankChecks=0,uniqueAssignments=0,extra=0;
const pc=x=>{let c=0;while(x){x&=x-1;c++}return c};
for(let n=2;n<=4;n++){
 const pairs=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)pairs.push([i,j]);
 for(let g=1;g<1<<pairs.length;g++){
  const E=pairs.filter((_,i)=>g>>i&1),m=E.length,all=(1<<(n+m))-1;
  let tau=n,rho=n;graphs++;
  for(let I=0;I<1<<n;I++)if(E.every(([u,v])=>I>>u&1||I>>v&1))tau=Math.min(tau,pc(I));
  for(let p=0;p<3**m;p++){
   prefixes++;let z=p,sets=new Set([0]);
   for(let i=0;i<m;i++){let x=[3,5,6][z%3];z=Math.floor(z/3);let [u,v]=E[i];let next=new Set();for(let s of sets)for(let a of table[x]){let t=1<<(a===1?u:a===2?v:n+i);if(!(s&t))next.add(s|t)}sets=next}
   for(let s of sets){uniqueAssignments++;if(pc(s)!==m)extra++}
   if(!sets.has(all^((1<<n)-1)))throw Error("common basis");
   const r=Math.max(...[...sets].map(s=>pc(s&((1<<n)-1))));rho=Math.min(rho,r);rankChecks++;
  }
  if(rho!==tau)throw Error("cover");
 }
}
if(extra)throw Error("extra");return {table,raw,graphs,prefixes,rankChecks,uniqueAssignments,extra};
}
console.log(JSON.stringify(replay()));
```

## 4. Next

Now that the common-rank barrier is removed, investigate exact robust compatibility with structured external slot capacities, including combined graph separator/treewidth algorithms; test whether the local switch admits a smaller witness and whether internal private-path multiplicity can be separately encoded. Preserve full old relation and old evidence, signed/weighted BRC, branch source, temporal order and X6 common-depth coordinates independently. No Task/Result/Review or Foundation admission.
