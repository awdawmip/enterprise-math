# X6 R238 — exact zero-germ factor recovery and closure of the one-support-factor root family

2026-11-26. AUTHOR PROOF + EXACT INTEGER CERTIFICATE / NOT_REVIEWED. Frozen R233/R236/R237 science (Port 10, 1935 directions, six-pair BRC, weights (17t,B,22t,D)>0, strict 3/2 near set and legal optimum, 47 necessary supports and 49 components); static auxiliary weight chart only. Informed unclaimed research. No new whole-direction scoring or formal task mutation. P000 V5 unchanged.

Theorem (zero-germ factor recovery). Let Q be a nonzero homogeneous polynomial of degree at most two on the three-dimensional auxiliary weight coefficient space. If its eventual sign is zero along a nondegenerate directed projective interval germ on support L=0, Q vanishes identically on that interval. The one-variable polynomial in the germ parameter has all coefficients zero. By homogeneity the zero extends to the open cone of rays in that two-dimensional linear subspace, and hence to the entire subspace by polynomial identity. After a linear coordinate change making L a coordinate, the constant-in-L term vanishes identically. Thus L divides Q. Two nonproportional zero-germ support normals imply Q=c L1 L2, c nonzero. A nonzero linear query cannot have two such supports. This is exact for zero-germ states, not for isolated point zeros. Positive and negative c give the same unordered pair of strict branch partitions, so a strict-capacity exclusion transfers to both; no assumption about assigning Q=0 to a strict branch is needed.

Application: R237 at e1aac4ac173c9f792108fdd7fe5212c0248374e9:research_notes/portable_direct/2026-11-26_r2_x6_r237_targeted_two_component_germ_refinement.md excluded 13 of 14 refined partitions at level 3, with no cutoffs; all original four R236 parents had their factor multiplicities checked. The sole surviving strict mask pair has every germ of exactly two nonproportional supports missing from both strict branches. Exact zero certificate below establishes supports 13 and 26, normals (74,0,-1) and (40,0,-3). Therefore any actual quadratic attaining this mask is proportional to (74t-D)(40t-3D). The earlier clipped-germ proof R231 at 0ade3820bee4afd0585225eac2b764bccbd196a5:research_notes/portable_direct/2026-11-26_r2_x6_r231_interior_split_germ_final_roots.md explicitly excludes pair (13,26): 100 directed germs, 54 points, 3524 distinct query partitions, 298927 checks, false. This is an earlier stronger witness bank conditioned on actual root clipping; no need to rerun the old proof. The coarser mask's relaxed feasibility is not actual feasibility. Independent corroboration from exact second-factor cone enumeration in this turn found only ray (-74,0,1) for support 26 and (-40,0,3) for support 13; the zero-germ certificate alone suffices.

Combining exhaustive R233-R237 coverage with this exact transfer closes the entire family Q=L_i M with any one of the 47 necessary support factors L_i and any real homogeneous linear M, followed by five arbitrary linear queries, conditional on the inherited necessary-wall premise and complete rank-three enumeration proof. By normalization the same applies to affine factors in the positive normalized chart. A depth-six correct tree cannot start with this family as its sole quadratic. Arbitrary quadratic roots with no necessary support factor and a first quadratic below linear ancestors remain open. In particular unrestricted K6 remains in [1,2].

Exact certificate:
```json
{"germs":220,"zero":[{"component":14,"support":13,"germStart":68,"germEnd":71,"normal":["74","0","-1"],"endpoints":[["1","9","74"],["1","4","74"]]},{"component":28,"support":26,"germStart":124,"germEnd":127,"normal":["40","0","-3"],"endpoints":[["0","1","0"],["3","38","40"]]}],"labels":[13,26],"prior":{"i":13,"j":26,"results":[{"pass":false,"points":54,"germs":100,"vertices":1238,"signPatterns":5195,"queries":3524,"calls":88,"checks":298927},null]},"remaining":1}
```
Reproduction using the immutable R237 source's embedded data and level-3 second JSON block, and R231 first JSON block (all three were read this turn):
```javascript
function zeroCertificate(data,res,old){
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],add=(a,b)=>a.map((x,i)=>x+b[i]);
const parts=data.flatMap((e,k)=>(e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]).map(p=>({k,a:p[0].map(BigInt),b:p[1].map(BigInt)})));
const remaining=res.rows.filter(r=>r.status!=="excluded");if(remaining.length!==1||remaining[0].status!=="relaxedFeasible")throw Error("remaining");
const r=remaining[0],A=BigInt("0x"+r.a),B=BigInt("0x"+r.b);
if(A&B)throw Error("overlap");
let pos=0,zero=[],normalByLabel={};for(let [c,{k,a,b}] of parts.entries()){let n=c===2||c===29?16:4,mask=((1n<<BigInt(n))-1n)<<BigInt(pos),hits=(A|B)&mask;if(hits===0n){let L=data[k].normal.map(BigInt);if(dot(L,a)||dot(L,b)||!cross(a,b).some(Boolean))throw Error("bad wall");zero.push({component:c,support:k,germStart:pos,germEnd:pos+n-1,normal:data[k].normal,endpoints:[a.map(String),b.map(String)]});normalByLabel[k]=L;}else if(hits!==mask)throw Error("partial zero");pos+=n}
if(pos!==res.summary.germs||((A|B)>>BigInt(pos)))throw Error("dimension");
let labels=Object.keys(normalByLabel).map(Number);if(labels.length!==2||!cross(normalByLabel[labels[0]],normalByLabel[labels[1]]).some(Boolean))throw Error("not two independent supports");
const prior=old.out.find(x=>x.i===labels[0]&&x.j===labels[1]&&x.results.some(y=>y?.pass===false));if(!prior)throw Error("no prior exclusion");
return {germs:pos,zero,labels,prior,remaining:remaining.length};
}
```

Next: for a quadratic root with no necessary support factor, every directed germ on each necessary support has nonzero eventual sign. Exploit this exact restriction in the six-coefficient lifted arrangement or a lazy linear-feasibility/capacity exclusion; do not repeat the closed factor family. Interior first-joint queries remain a separate task.
