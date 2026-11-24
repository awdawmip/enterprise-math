# R779 — Four-cut graphic exterior classification and paired residual exchange

2026-11-25. AUTHOR_PROOF_WITH_EXACT_FINITE_CERTIFICATE / NOT_REVIEWED. Independent portable continuation of R778 (b570d0d6a824b2693a9680ecff1ba5ade8377294:research_notes/portable_direct/R778_EXACT_CONTINUATION_DOMINANCE.md), frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint-relation contract blob 3923890d77a02d84b772f789e6912dd14f220d14. Frozen Heartbeat companion returned 404. ACTIVE worldview and current portable/continuation rules consulted. Own public SID MCP-ec17f2f30fb8409f8e664eb29ae6c08c recovery metadata r3-20261125-0420-own-metadata-v1 confirms existing registration and no runs; owner inventory r3-20261125-0420-owner-read-v1 last observed RUNNING before publication. No shared task claim.

## Model and paired exchange theorem

Use R778's auxiliary Boolean observer: loop-free subcubic graph with three ports at each vertex (private unused ports), local even binary triples, equal bits on each internal joint edge and zero lift bits on private ports. For one fixed prefix x, target w and reserve t, local allowed lift patterns are those satisfying x+w+z in S(t), where S(0)={0}, S(1)=three nonzero even triples, S(2)=all four even triples. Boundary edges are dangling ports, distinguished and labeled; let E be their extendible assignments, for this one prefix. Any such assignment has even total parity. A fixed prefix can equivalently be absorbed into the target.

Theorem: for any two assignments u,v in E with Hamming distance 2k, the differing boundary coordinates admit a pairing into k disjoint pairs such that toggling any union of these pairs in u produces another assignment in E. In particular E contains the entire corresponding 2^k point binary subcube (in paired coordinates). This applies even to disconnected interiors, with pairings inside components.

Proof: choose complete internal lifts U,V of u,v. Their XOR has even degree at every vertex, because both local triples are even; private ports do not differ. Since degree is at most three, the XOR support consists of vertex-disjoint paths joining differing boundary ports, and cycles. There are k such paths, each with two distinct boundary endpoints. Independently replace U by V on any selection of these paths, keeping all other edge bits fixed. At each vertex the resulting triple is exactly the U or V triple, hence retains its original local acceptance, including all fixed prefix and reserve constraints. Internal equality and private bits remain valid. The boundary toggles precisely the selected endpoint pairs. This is a structural residual exchange certificate; no counts/weights/provenance of lift histories are collapsed into a stronger observer.

## Complete connected four-edge cut exterior catalog

Let Q be the eight even four-bit labels, in integer order 0,3,5,6,9,10,12,15. Partition Q into four antipodal pairs {q,q XOR 15}. A nonempty E subset Q is attainable by a connected graphic exterior with zero prefix and fixed reserve if and only if the number of complete antipodal pairs in E is NOT exactly one.

Necessity: if E contains u and its antipode v, all four boundary coordinates differ. The paired-exchange theorem yields two additional complementary intermediates, so a second full antipodal pair must occur. This necessity holds even if the exterior is disconnected.

Sufficiency: use a four-cycle with one external boundary port per vertex. Each local ternary constraint may be any of the 15 nonempty subsets of even triples by the explicit R778 three-port gadgets: full set via t=2, three via t=1 excluding w, singleton via t=0, pair by fixing their shared bit using a degree-two subdivision vertex and private port. All use p=0 and connected gadgets. Replacing the four-cycle vertices by these gadgets preserves the graph class and labels. Enumerate the 15^4 local choices, each on all 16 assignments to the four internal cycle edges. At vertex j, if outgoing bit is u and incoming bit is v, the boundary bit is u XOR v and local choice mask uses index u+2v. Enumerate boundary label permutations. Exact finite computation below finds precisely all 147 sets satisfying the necessary criterion and independently replays each witness; the finite domain and gadget construction establish sufficiency for unbounded graph class (not an empirical absence claim). For a fixed cyclic boundary order the cycle realizes 129 sets; allowing relabelings gives all 147.

Count analytically: 3^4-1=80 nonempty choices with no full pair. At least two full pairs give C(4,2)*3^2+C(4,3)*3+1=67. Exactly one full pair gives 4*3^3=108 forbidden nonempty sets. Total 147 out of 255. Smallest obstruction {0000,1111}. It has the same ambient even parity as any legal pair but no permitted paired exchange. Therefore arbitrary-set distinguishing contexts of R778 do not extend unchanged to width four.

## Exact graphic continuation dominance on a connected four-cut

For a fixed interior reserve let A and B be feasible minimal antichains as in R777–R778. T_A(E)=1 iff all a in A meet E. Define real-context dominance A >=g B iff T_A(E)>=T_B(E) for all actual exterior assignments E. At width four the above catalog is both necessary and sufficient; empty E never distinguishes feasible A,B. For arbitrary exterior prefixes its full family amounts to the conjunction of those tests. Thus the restricted predicate is exactly the invariant for fixed-reserve continuation through arbitrary graphic exterior, including a disconnected exterior, at this labeled interface. If A dominates B and costs no more, replacing B is safe for a whole completion of this interface with any fixed exterior reserve. The abstract R778 dominance remains sufficient across arbitrary intermediate joins; this new result concerns complete graphic exteriors, and any intermediate use must retain the same allowed class of future contexts.

There is a compact test requiring at most two exterior sets per a in A. Put C=Q minus a. If C is empty no separating test exists. If C has zero or at least two full antipodal pairs, C itself is the unique maximal attainable subset of C. If C has exactly one full pair {u,v}, its maximal attainable subsets are precisely C minus {u} and C minus {v}: no subset can create a second full pair, and removing either element eliminates the sole complete pair. Monotonicity of T_B implies a separator exists iff at least one of these maximal attainable sets hits every member of B. This proves the exact criterion, with at most 2|A| tests and ordinary eight-bit masks. Compared to unrestricted R778 it can be strictly weaker on abstract antichains: take a={0000,0011,0101}, C=Q minus a, with sole full pair {0110,1001}. A={a}, B={{0110},{1001}}. Every attainable E hitting B contains that pair and hence another full pair, which forces a hit on a; however E={0110,1001} separates in the unrestricted observer. Each member of A,B is separately realizable. Simultaneous reachability of B as an actual prefix family is not established; do not claim a strict reduction of the actual interior catalog from this example alone.

## Exact calculation

Python independently found 129 fixed-order and 147 relabeled relations. The following dependency-free JS enumeration and exact witness replay were also executed. Integers are at most 16-bit masks. The code computes an explicit local-mask tuple and permutation for each of the 147 relations and replays it. All 256 complement maximal-test classifications were independently compared against enumeration of valid subsets.

```json
{
  "assignments": 50625,
  "fixedOrder": 129,
  "relabels": 3096,
  "realizable": 147,
  "excluded": 108,
  "witnessReplays": 147,
  "maximalChecks": 256,
  "sizes": [
    8,
    24,
    32,
    22,
    24,
    28,
    8,
    1
  ]
}
```

```javascript
function verify(){
 const Q=[0,3,5,6,9,10,12,15],idx=new Map(Q.map((x,i)=>[x,i]));
 const pairs=Q.filter(x=>x<8).map(x=>[idx.get(x),idx.get(x^15)]);
 const pairCount=m=>pairs.filter(([i,j])=>(m&(1<<i))&&(m&(1<<j))).length;
 const valid=m=>m!==0&&pairCount(m)!==1;
 const expect=new Set(Array.from({length:255},(_,i)=>i+1).filter(valid));
 const loc=Array.from({length:4},(_,j)=>Array.from({length:16},(_,a)=>{
  let m=0;for(let z=0;z<16;z++){let x=((z>>j)&1)|(((z>>((j+3)%4))&1)<<1);if(a&(1<<x))m|=1<<z}return m;
 }));
 const out=Array.from({length:16},(_,z)=>{let b=0;for(let j=0;j<4;j++)b|=(((z>>j)^(z>>((j+3)%4)))&1)<<j;return 1<<idx.get(b)});
 const proj=new Uint8Array(65536);for(let m=1;m<65536;m++){let l=m&-m;proj[m]=proj[m^l]|out[31-Math.clz32(l)]}
 const found=new Map();let assignments=0;
 for(let a=1;a<16;a++)for(let b=1;b<16;b++)for(let c=1;c<16;c++)for(let d=1;d<16;d++){
  assignments++;let m=proj[loc[0][a]&loc[1][b]&loc[2][c]&loc[3][d]];if(m&&!found.has(m))found.set(m,[a,b,c,d]);
 }
 const perms=a=>a.length?a.flatMap(x=>perms(a.filter(y=>x!==y)).map(p=>[x,...p])):[[]];
 const all=new Map();let relabels=0;
 for(const p of perms([0,1,2,3]))for(const [m,a] of found){let r=0;for(let i=0;i<8;i++)if(m&(1<<i)){let y=0;for(let j=0;j<4;j++)y|=((Q[i]>>j)&1)<<p[j];r|=1<<idx.get(y)}relabels++;if(!all.has(r))all.set(r,{p,a})}
 if(all.size!==expect.size||[...all.keys()].some(m=>!expect.has(m)))throw Error("classification");
 // Independently replay each returned witness using direct edge-state enumeration.
 for(const [m,{p,a}] of all){let result=0;for(let z=0;z<16;z++){let b=0,ok=true;for(let j=0;j<4;j++){let u=(z>>j)&1,v=(z>>((j+3)%4))&1;if(!(a[j]&(1<<(u|2*v))))ok=false;b|=(u^v)<<p[j]}if(ok)result|=1<<idx.get(b)}if(result!==m)throw Error("witness")}
 const maximal=C=>{if(!C)return [];if(valid(C))return [C];let [i,j]=pairs.find(([i,j])=>(C&(1<<i))&&(C&(1<<j)));return [C^(1<<i),C^(1<<j)]};
 let maximalChecks=0;for(let C=0;C<256;C++){let exact=[...expect].filter(m=>(m&C)===m);let mx=exact.filter(m=>!exact.some(n=>n!==m&&(n&m)===m)).sort((a,b)=>a-b);let pred=maximal(C).sort((a,b)=>a-b);if(mx.join()!=pred.join())throw Error("maximal");maximalChecks++}
 const pop=m=>m.toString(2).replace(/0/g,"").length;
 const sizes=Array.from({length:8},(_,i)=>[...all.keys()].filter(m=>pop(m)===i+1).length);
 return {assignments,fixedOrder:found.size,relabels,realizable:all.size,excluded:255-all.size,witnessReplays:all.size,maximalChecks,sizes};
}
console.log(JSON.stringify(verify(),null,2));
```

## Next

Determine the actual reachable multi-prefix antichain catalog at width three/four and whether the weaker graphic dominance removes a reachable pair. Extend paired-exchange obstructions to six or more boundary ports, where simultaneous exchange cubes can impose stronger restrictions than pairwise local readouts. The scope remains the Boolean auxiliary Port observer. Native signed amplitude, weights as physical amplitudes, time, provenance and three-dimensional-slice common depth remain distinct observers. No formal task completion or mathematical admission claimed.
