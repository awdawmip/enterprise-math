# R823 — Exact leaf attenuation and Port-core FPTAS at bounded original degree

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_PEELING_CHECKED / NOT_REVIEWED.
Independent portable continuation, EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own metadata receipt r3-20261127-r823-own-read confirms existing session, no run, execution_authorized=false. Running inventory r3-20261127-r823-running-read was RUNNING during derivation; no claim or owner change. No formal Result or admission. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 and joint observer blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14. Frozen Heartbeat companion returned 404, current normative companion read. Current account entries verified together at 392a0cb678f43a7d4bc0be6ce3653b5708a74d3e; ACTIVE worldview and applicable rules read. Source snapshot 685a53de549d4d0affe7ace42a26e1fc68af6f30: R812_CHARGED_BLOCK_INTERFACE_FPTAS.md (blob 8ee90887417c0c09170b91f2ecd3a17dfcc9f3fb), R813_IMPLICIT_INTERFACE_FOREST_AND_FEEDBACK.md (a3511002437d4fd080f272fbea23c55fa9ff30b3), R822_DIRECT_PORT_HYPEREDGE_ENTROPY_PAYMENT.md (60acefe69f50eeeb7dac38774f2d42db07421635), all in research_notes/portable_direct/. R822 immutable original b94082079b66ce4832bc43007a1c20565a34607f. The present result is in the R812 auxiliary rational nonnegative fixed-charge occupancy/parity model, not a new native Heartbeat evolution or native residual attribution. Preserve original road matrices, signed BRC, branch provenance, time order and common depth.

## 1. Exact unary leaf transfer and coefficient attenuation

Use R812's exact affine block factorization and R813's implicit observer. At feasible charge T, divide out the known 2^|V| and isolated-vertex constants. Write
Z=sum_z product_B h_B(z_B) product_f (1-delta_f product_{B in F_f} z_{Bf}),
0<=delta_f<1. h_B is a nonnegative rational joint mass, with exact polynomial-bit polynomial-time unary-weighted observer L_B; the incidence labels are retained even for coincident footprints. Original degree d_f bounds delta_f<=2^(-2d_f-1).

Maintain a bipartite incidence graph of surviving groups and factors, unary weights on original group bits, and an accumulated scalar. More generally let a factor be a-b I, a>b>=0, I=product of surviving incidence bits (empty product 1). All group unary weights include pinnings, if specified in the original query. The following identities hold with arbitrary nonnegative external factors on the other surviving variables.

(A) A group B of current incidence degree one, attached to f, has weighted mass H=sum_z h_B(z) product u(z), and H1=sum of the same weight over z_Bf=1. Both are computed by R813's observer (one total and one pinned query). Integrate the entire group exactly:
sum_{z_B} weight_B(z_B)(a-b z_Bf I_rest)=a H-b H1 I_rest.
For H>0 the normalized new coefficient is
delta_f'=(b/a)(H1/H)=delta_f p_B,  0<=p_B<=1.
If H=0 the full restricted partition is zero. Remove B and its incidence, keeping the new scalar aH or equivalently the scaled factor pair (aH,bH1). Multiple independent leaf branches multiply their activation probabilities exactly; no independence assumption is made on the bits within B.

(B) A factor f of degree one has a-b z_Bf and becomes an exact unary weight on the surviving group's original bit. Remove the factor from the incidence graph, retaining this weight in that group's observer. Degree zero factors are constants a-b; degree zero groups contribute their weighted mass H. In the normalized representation all scalar factors are accumulated without approximation.

Iterating these operations to exhaustion removes the incidence graph outside its ordinary bipartite 2-core; if there is no core, the answer is exact. The unweighted topology of the 2-core is independent of removal order (zero coefficients may optionally be removed, giving a smaller support). The identity for each leaf applies pointwise on all remaining variables. Induction proves exact equality for the whole partition and all restrictions or future nonnegative compositions on the surviving incidence bits. For a new pin on an eliminated bit, retain the original source and rerun the affected messages; no lossless recovery of arbitrary erased bits from the scalar alone is claimed. All original parity constraints are already inside the group laws; leaf transfer never modifies their charges.

This extends R813's forest oracle to forest appendages of an arbitrary cyclic core, and extends R822 by using exact attenuated coefficients instead of original worst-case delta. It does not assert a weak coupling or independence approximation inside any retained block.

## 2. Resource bound and residual core FPTAS

A queue of current degree <=1 nodes gives O(total incidences) graph operations, at most two original observer calls per removed group, and one unary multiplication per removed factor. At a surviving group all removed factors give unary weights on its original interface coordinates. For a core joint moment pin exactly the selected remaining bits, jointly, in that same observer. The normalized group mass is positive for feasible T and no inconsistent pin; if a queried joint moment has zero mass, return zero. If an original pin forces zero total, the exact peeling/baseline test handles it.

Bit complexity: orient each removed group or factor toward its sole surviving neighbor when such a neighbor exists. Its scalar or unary messages represent sums of products on disjoint attached branches; use unnormalized rational pairs or weights and reduce fractions. Each intermediate quantity is a conditional partial partition of a subgraph, with denominator dividing the product of explicit input denominators and numerator log bounded by total input bit length plus assignment-count log. Normalization ratios use two such numbers. This avoids recursive repeated duplication of denominator factors; message storage, pinning calls and rational arithmetic are polynomial-bit under R813 hypotheses. Baseline for the core is the product of its weighted masses times all removed scalar factors. The same argument covers the all-peeled case.

For a surviving factor f let s'_f be its remaining arity, b'_B the number of surviving incidences at B, L'_f=max_{B in F'_f} ceil(log2 b'_B), c'_f=s'_f+L'_f. The core factors are still exactly of R822's form, on independent weighted original group laws before reintroducing the surviving factors. Apply R822 sections 2-4 with
beta'_B=sum_{f incident B} 2^{c'_f} delta'_f.
If max_B beta'_B<=1/8, there is a deterministic FPTAS on the original input for each fixed feasible charge. In detail P(t)=E product_f(1-delta'_f t^{c'_f} I_f) has no zeros on |t|<=3/2, |log P(t)|<=g'/7 with g' surviving groups; truncation error <=(2g'/7)(2/3)^k. Connected labeled support enumeration costs g' 2^{O(k)} poly(N,k), using R822's queue encoding and implicit pinned group moments; k=O(log((g'+1)/epsilon)). Original preprocessing, exact leaf scalars, rational bit cost and certified output recovery are included. The theorem is for the same auxiliary fixed-charge partition; there is no new native arithmetic execution.

The exact inequality delta'_f=delta_f product_leaf p_B and c'_f<=c_f show that surviving original-group loads cannot increase in this procedure: every surviving incidence has smaller or equal cost and coefficient, and removed terms are absent. Thus it covers all original R822-certified inputs and potentially additional ones. This is a sufficient certificate, not a necessary boundary.

## 3. A family with bounded original degree, arbitrarily high interfaces AND no long separator paths

Let there be g odd >=5 disjoint retained biconnected ladders, each with b=g-1 vertices (a 2 by b/2 ladder). For every pair of ladders add one nonretained connector edge, with the b distinct vertices of each ladder used once. At every ladder vertex add one nonretained pendant edge to its own new degree-one vertex. J consists exactly of ladder edges. The full graph has maximum original degree 5; each ladder vertex has d=4 or 5, s=3, b_B=b. Contracting the connected ladders exhibits K_g as a minor, so treewidth grows unboundedly. There are no lengthened connector paths. Each retained block has width 2, arbitrary cycle rank and b interfaces; R813 supplies the exact implicit oracle. Every outside-J edge is a singleton group.

Choose on each pendant edge S(00)=1, S(11)=b^2, S(01)=S(10)=0. Its internal leaf-vertex factor is a_leaf when both ports are empty, and 1 when occupied. Thus in its singleton group p_B=Pr(z_Bf=1)=a_leaf/(a_leaf+b^2)<=1/b^2. This statement is independent of feasible T since pendant edges lie outside J. All other road weights and eta satisfying R812's hypotheses are arbitrary. Choose original shared-vertex deltas at their allowed maximum for the following comparison, though the new certificate holds for all smaller ones.

R822's unpeeled cost at each ladder vertex is 3+ceil(log2 b) and delta>=2^-11 in the saturated example. Its original ladder load >=b^2/256, which exceeds 1/8 for b>=6. Therefore the unpeeled local-load sufficient condition fails for these growing instances; this is a comparison of certificates, not hardness.

Peel the pendant singleton groups. Exactly one factor incidence disappears at each ladder vertex, leaving arity two (ladder plus connector singleton), with delta'_f<=2^-9/b^2. The ladder still has b surviving interfaces, connector singleton has two. Hence 2^{c'_f}=2^{2+ceil(log2 b)}<=8b and
q'_f<=1/(64b),
beta'_ladder<=1/64,
beta'_connector<=1/(32b).
Both are below 1/8 uniformly in b and g. No long-road residual transport, no full joint interface table and no bounded maximum original or residual interface number is required. This supplies an explicit new family with degree <=5, arbitrarily many low-degree shared vertices, unbounded core treewidth, and arbitrary feasible charge. The example uses explicit rational weights admissible in R812; whether a particular constrained native road generator realizes these weight ratios remains open. It does not add pendant edges to a given input while pretending its original partition is unchanged.

For general a pendant mass ratio bounded below by b^2, the same proof works. This demonstrates a second way of paying the entropy cost: local occupation suppression, rather than degree-dependent bare residual or separator length. The ratio is an exact joint observation of the integrated branch.

## 4. Optional exact forest-component contraction

A useful generalization for the next selection problem is to choose any supplied subset K of whole factors such that its incidence graph is a forest. Its components become independent base groups under the measure with K restored and D=all other factors temporarily removed. R813 computes their exact total and joint pinned masses. A factor in D may meet the same component several times: its new component-local indicator is the product of ALL corresponding original bits, not a single arbitrary bit. Pinning a set of factors pins their union of original incidences, so the moment oracle remains exactly the R813 forest oracle; this is enough for the R822 expansion and does not require a general unary oracle on those composite indicators. Include factors with just one distinct component (their arity is one, not zero); the proof of R822's local-load lemma and queue code remains valid with s'=1. Compute b' as the number of labeled residual factors incident on the component, not the number of raw incidences. The coefficient remains the original delta unless an independent leaf integration has supplied an exact attenuation. If the quotient load passes 1/8, apply the same weighted support proof. Cost of finding an optimal K is not claimed; the supplied forest is verified by graph traversal and its calls have polynomial rational bit cost by R813. In particular, do not absorb arbitrarily many internal residual loops into a merged block without an actual joint observer algorithm.

## 5. Finite verification actually executed

The following JavaScript BigInt test compares complete integer-scaled partitions of seven abstract labeled incidence patterns (trees, cyclic cores, coincident factors, higher arity, singleton and isolated components), with 16 deterministic tables/weight configurations each. It includes zero table entries, all single incidence pins and one joint pin pattern per configuration, and tests exact monotonic attenuation at each leaf step. A factor a-b I is an unnormalized rational-coordinate representative, so no rounding occurs. Direct exhaustive enumeration uses original factors; the alternative peels, then exhaustively contracts the remaining core, not the FPTAS. This is an auxiliary combinatorial identity test, not a native BRC experiment or a production FPTAS benchmark. Results:
{
  "shapes": 7,
  "instances": 112,
  "exactComparisons": 2112,
  "zeroPinCases": 87,
  "attenuationChecks": 5603,
  "eliminatedGroups": 6298,
  "eliminatedFactors": 4558
}

```javascript
function verify(){
 const shapes=[
 {n:4,F:[[0,1],[1,2],[2,0],[0,3]]},
 {n:5,F:[[0,1,2],[1,2],[0,3],[3,4]]},
 {n:6,F:[[0,1,2],[0,1,3],[2,4],[3,5]]},
 {n:5,F:[[0,1],[0,1],[1,2],[2,3],[3,4]]},
 {n:5,F:[[0,1,2,3],[0,4]]},
 {n:4,F:[[0,1],[1],[2,3],[2]]},
 {n:5,F:[[0,1],[1,2],[2,0],[0,3],[0,4]]}
 ];
 let seed=823; const rnd=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed};
 const sum=a=>a.reduce((s,x)=>s+x,0n);
 const counts={shapes:shapes.length,instances:0,exactComparisons:0,zeroPinCases:0,attenuationChecks:0,eliminatedGroups:0,eliminatedFactors:0};
 function brute(G,F){
  let result=0n;
  const masks=G.map(()=>0);
  function rec(i,w){
   if(i===G.length){for(const f of F){let I=true;for(const v of f.V){if(!((masks[v]>>G[v].ids.indexOf(f.id))&1)){I=false;break}}w*=f.a-(I?f.b:0n)}result+=w;return}
   const g=G[i];for(let j=0;j<g.w.length;j++)if(g.w[j]){masks[i]=j;rec(i+1,w*g.w[j])}
  }
  rec(0,1n);return result
 }
 function peel(G0,F0){
  const G=G0.map(g=>({ids:[...g.ids],w:[...g.w],active:true})),F=F0.map(f=>({...f,V:[...f.V],active:true}));let scale=1n;
  while(true){
   let changed=false;
   for(let v=0;v<G.length;v++)if(G[v].active){
    let g=G[v],A=g.ids.filter(i=>F[i].active);
    if(A.length>1)continue;
    let S=sum(g.w);g.active=false;counts.eliminatedGroups++;changed=true;
    if(S===0n)return 0n;
    if(A.length===0)scale*=S;
    else{
     let f=F[A[0]],bit=g.ids.indexOf(f.id),T=sum(g.w.filter((_,m)=>(m>>bit)&1));
     let a=f.a,b=f.b;f.a*=S;f.b*=T;f.V=f.V.filter(u=>u!==v);
     if(f.b*a>b*f.a)throw Error("attenuation");
     counts.attenuationChecks++;
    }
   }
   for(const f of F)if(f.active&&f.V.length<=1){
    f.active=false;counts.eliminatedFactors++;changed=true;
    if(!f.V.length)scale*=f.a-f.b;
    else {let g=G[f.V[0]],bit=g.ids.indexOf(f.id);g.w=g.w.map((x,m)=>x*(f.a-(((m>>bit)&1)?f.b:0n)))}
   }
   if(!changed)break;
  }
  // Retain original bit indices, including absorbed ones, in each surviving table.
  let rem=G.map(g=>g.active?g:{ids:[],w:[1n]});
  return scale*brute(rem,F.filter(f=>f.active))
 }
 for(const sh of shapes)for(let trial=0;trial<16;trial++){
  const F=sh.F.map((V,id)=>({id,V,a:BigInt(9+(rnd()%13)),b:BigInt(rnd()%7)}));
  const G=Array.from({length:sh.n},(_,v)=>{
   const ids=F.filter(f=>f.V.includes(v)).map(f=>f.id),w=Array.from({length:2**ids.length},()=>BigInt(rnd()%9));
   if(sum(w)===0n)w[0]=1n;return{ids,w};
  });
  counts.instances++;
  const pins=[[],...G.flatMap((g,v)=>g.ids.flatMap((id,k)=>[[[v,k,0]],[[v,k,1]]])),G.flatMap((g,v)=>g.ids.length?[[v,0,(v+trial)&1]]:[])];
  for(const pin of pins){
   const P=G.map(g=>({ids:g.ids,w:[...g.w]}));
   for(const [v,k,b] of pin)P[v].w=P[v].w.map((w,m)=>((m>>k)&1)===b?w:0n);
   const exact=brute(P,F),reduced=peel(P,F);
   if(exact!==reduced)throw Error("partition disagreement");
   counts.exactComparisons++;if(exact===0n)counts.zeroPinCases++;
  }
 }
 return counts;
}
console.log(verify());
```

## 6. Next problem

Find an efficiently constructible forest/core split or a finer retained-block interface decomposition whose *conditional* activation probabilities pay entropy even when no pendant branches exist. In the worst case large groups can have many parallel residual factors, and a forest contraction can merge their endpoints while leaving a large number of one-component residual factors; exact pinned forest moments do not by themselves make the load certificate pass. Seek a sharper conditional activation bound from actual R812 local road matrices and charge constraints, or a low-cost alternative expansion. General full Port FPTAS, native realization of special weight ratios, and native residual attribution are open. No task state or worldview changes.
