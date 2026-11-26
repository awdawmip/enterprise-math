# R816 — Soft-factor separator transport and paid re-splitting of large feedback cliques

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared CLAIM/RUN/Result. Researcher EM-DIRECT-82A007 / TASK_RESEARCH; own metadata recovery r3-20261126-r816-own-read confirms original registration, no own run, execution_authorized=false. RUNNING query r3-20261126-r816-running-read was still RUNNING during derivation; no empty-owner inference. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read. Predecessor b981236f0fa70e0cfdc4e86c9592db68f9f674e5:research_notes/portable_direct/R815_WEIGHTED_DEGREE_FEEDBACK_FPTAS.md; R813 c6a2b95f767b8cf8316c207ec103cb86130e78d1. Account entries read at d3c11e6f1333fbacb9ab2cfa5bb5edf9f5293d38. Only the auxiliary nonnegative occupancy/parity observer, at fixed feasible charge, is computed; original signed/native BRC, full road matrices, provenance, time order and common depth are retained. No native phase experiment.

## 1. Path transport through retained soft factors

Use R813 incidence forest H-D, with nonnegative block tables h_B (possibly zeros), binary interface bits and retained shared factors g_v=1-delta_v prod z_{Bv}, 0<=delta_v<1. For each deleted factor its original incident bits become leaf ports attached to their blocks, one distinct bit per incidence. Attach a unary leaf node if needed to mark a bit. Arbitrary nonnegative unary weights and feasible pinnings are allowed. The probability measure is normalized by positive Z0.

For two distinct port bits i,j let K(i,j)=0 if disconnected; otherwise K(i,j)=prod over retained shared-factor nodes v on the unique path of kappa_v, where
 kappa_v=(1-sqrt(1-delta_v))/(1+sqrt(1-delta_v))
 <= delta_v/(4-3delta_v).
Use K(i,i)=1; empty products are 1. Thus any intervening block, however large or internally correlated, pays at most 1. No independence approximation inside h_B.

**Lemma.** Under any common feasible pinning, if both conditions i=0 and i=1 have positive probability, the absolute difference in the conditional probability of j=1 is <=K(i,j). This also applies to internal interface bits by treating the bit as an edge separator (and counting only factors strictly traversed). If a pinned bit separates i and j the actual difference is zero.

Proof: sum all off-path subtrees into nonnegative incoming messages. For a retained shared factor with two path ports x,y the resulting 2x2 weight is [[A,A],[A,A-delta_v P]], A the product of sums of off-path messages, P the product of their 1-state values. Positive partition implies A>0; 0<=P<=A. Write a=1-delta_v P/A. After absorbing the remaining suffix into a nonnegative column likelihood, the two row probabilities of y=1 have difference (1-a)t/[(1+t)(1+a t)] for likelihood ratio t>=0 (including endpoints by continuity). Its maximum over t is (1-sqrt(a))/(1+sqrt(a)), by 1/t+a t>=2 sqrt(a). This is <=kappa_v; the rational bound follows from (1+sqrt(1-delta))^2 >=4-3delta. For an arbitrary block the effective 2x2 weight is nonnegative, and its conditional stochastic kernel has row-TV <=1. A zero row cannot carry mass and may be completed to a stochastic row without worsening the claimed block bound. For shared factors zero suffix states give zero TV. The forest marginal on the path is a Markov chain obtained by successive suffix normalization, valid in both source conditions. For a binary stochastic matrix the difference in output 1-mass is the input difference times the row difference; multiplication proves the claim. Other components factor exactly. Common pins have simply been absorbed into local messages; no change to the path coefficient is required.

For actual Port retained shared v, original degree d_v>=2, delta_v<=2^(-2d_v-1)<=1/32; hence kappa_v<=1/125. If the path traverses l such factors, K(i,j)<=125^(-l). This is uniform in block size, weights and feasible common boundary conditions. It is a stronger metric than the R814 dependency clique for the purpose of real conditional influence, not a complex zero-free theorem.

## 2. Multi-port feedback-event certificate

For disjoint port sets A,B, compare the joint distribution on B before and after conditioning all bits in A to 1 (assume positive event probability). Then
 TV(mu_B | A=1, mu_B) <= min(1, sum_{i in A,j in B} K(i,j)).
The notation is TV(mu_B conditioned on A=1, mu_B unconditioned). First compare the distributions on B under i=0 and i=1 with all previously applied common pins. Generate the bits of B in a fixed order and use maximal coupling of each conditional binary distribution as long as their prefixes agree. Both prefix probabilities are then positive; the lemma bounds each mismatch by K(i,j), uniformly in the common prefix. The first-disagreement union bound gives TV <=sum_j K(i,j). If only one state of i is feasible conditioning to it does not change anything. The unconditional law is a mixture of the feasible i-conditional laws. Telescope pinning each i in A, using the triangle inequality. Each conditioning is feasible because the final event is feasible. This also proves the bound under any prior common pinning with positive partition.

For feedback factors u let S_u denote its distinct leaf ports and I_u=prod_{i in S_u}z_i. For disjoint sets of factors U,V define S_U union of their ports, and m(U)=E0 prod_{u in U} I_u. With B=S_V, the TV bound controls its all-one event, giving
 |m(U union V)-m(U)m(V)| <= m(U) min(1,sum_{i in S_U,j in S_V}K(i,j)).
If m(U)=0 both terms vanish. Also the same bound with U,V swapped; use min(m(U),m(V)) as prefactor. This is a directly computable, weighted approximate factorization certificate even when all feedback factors touch a single connected forest and the R814 dependency graph is complete. Paths inside a single block may give K=1 and are explicitly retained. Computing all needed K products is polynomial in the explicit forest size and number of ports. For a partition into several groups, telescoping the moment-factorization estimate gives an additive sum of cut pair bounds (with each factor <=1). These are real moment certificates only; errors in a signed inclusion-exclusion sum need separate conditioning/cancellation analysis.

## 3. Exact re-splitting with additional paid soft factors

A second way around the large-component clique is to choose an expanded feedback set D'=D union C, where C consists of retained shared-factor nodes. Since H-D is a forest, H-D' is a forest as well. Re-expand all factors in D' using the exact R813 identity, not by dropping them. Apply the R815 weighted-degree FPTAS to the new exact forest moment oracle. In particular if every component of H-D' touches at most three distinct D' vertices, the new dependency degree h_v<=2d_v (each component contributes at most two neighbors and a vertex meets at most d_v components). Therefore R815's c_v=max(1,ceil(h_v/4)), R=5/4, q_v=1/9 certificate is valid. Local oracle cost is as in R813; total input/bit complexity remains polynomial when local cycle rank or supplied treewidth is logarithmic. The number of cut factors can be linear; their cost is paid by R815 weighted connected expansion. This is a reparameterization of the exact same Q_T for every feasible fixed charge, not a deletion of physical relations. A supplied D' is verified by graph search. No assertion of a general polynomial search for a suitable cut.

**Unbounded-clique, unbounded-interface physical topology.** Take n>=4 disjoint retained cycles B_i of length m>=3. Each cycle vertex has one outside-J private leaf road. Join vertex 1 of B_i to vertex 0 of B_{i+1} by one outside-J road (i<n-1). Connect vertex 2 of B_i to a new vertex x_i by an outside-J spoke; the x_i form a cycle of outside-J roads. Each outside-J road is its own group; each retained cycle is a block of rank one. D={x_i}. H-D consists of a connected top-chain forest and isolated bottom-road groups, so every x_i touches the top component and G_D=K_n. The original degrees are <=4. In particular the R815 h<=2d sufficient test fails for this D when n>9. Instead choose D'=D union {vertex 0 of B_i: i=1,...,n-1}. Cutting these factors separates the top chain into components each touching at most the left cut, the right cut, and its own x_i. Bottom-road groups touch at most two. Private leaf groups at cut vertices touch only that vertex; otherwise they remain in the respective forest. Thus every component touches at most three D' factors. The oracle is polynomial because each B_i has cycle rank one, independently of m; all m interfaces can be retained implicitly. R815 proves deterministic FPTAS for every feasible charge on this entire family. The same topology has floor(n/2) vertex-disjoint incidence cycles, using disjoint consecutive pairs of top blocks and bottom edges, so any feedback vertex set must have at least floor(n/2) nodes. Consequently simply enumerating all feedback assignments cannot exploit a logarithmic exact feedback set here. This is an explicit certificate family, not a claim of novelty over every prior possible compression or algorithm.

## 4. Verification and next problem

Executed exact JS BigInt comparisons below: arbitrary nonnegative block tables with zeros on a five-block tree with a 3-ary and two 2-ary shared factors, all feasible common terminal pinnings, pair-source joint-target TV and all-one moment factorization, plus exact kernel grid checks. Equality-chain examples use matrix [[32,32],[32,31]] between consecutive blocks with perfectly correlated local ports; det=-32. All endpoint differences are exact via the determinant of its power; the chain is an abstract interface example (not claimed realizable by a native Port matrix). The n,m topology verification constructs original edge groups and tests both forest cuts and the dependency bound. No full FPTAS runtime benchmark or native BRC phase computation; no independent review.

```json
{
  "stats": {
    "kernel": 6300,
    "forestCases": 16,
    "conditionalTV": 13354,
    "jointMoment": 20732,
    "chain": 5,
    "resplitting": 4
  },
  "checks": 40395,
  "chain": [
    {
      "blocks": 2,
      "softDistance": 1,
      "exactDenominatorBits": 12,
      "bound": "125^-1"
    },
    {
      "blocks": 8,
      "softDistance": 7,
      "exactDenominatorBits": 84,
      "bound": "125^-7"
    },
    {
      "blocks": 32,
      "softDistance": 31,
      "exactDenominatorBits": 372,
      "bound": "125^-31"
    },
    {
      "blocks": 128,
      "softDistance": 127,
      "exactDenominatorBits": 1522,
      "bound": "125^-127"
    },
    {
      "blocks": 512,
      "softDistance": 511,
      "exactDenominatorBits": 6121,
      "bound": "125^-511"
    }
  ],
  "networks": [
    {
      "cycles": 4,
      "interfacesPerCycle": 4,
      "oldFeedbackCount": 4,
      "oldDependencyMax": 3,
      "newFeedbackCount": 7,
      "newComponentArity": 3,
      "newDependencyMax": 4
    },
    {
      "cycles": 16,
      "interfacesPerCycle": 32,
      "oldFeedbackCount": 16,
      "oldDependencyMax": 15,
      "newFeedbackCount": 31,
      "newComponentArity": 3,
      "newDependencyMax": 4
    },
    {
      "cycles": 32,
      "interfacesPerCycle": 128,
      "oldFeedbackCount": 32,
      "oldDependencyMax": 31,
      "newFeedbackCount": 63,
      "newComponentArity": 3,
      "newDependencyMax": 4
    },
    {
      "cycles": 128,
      "interfacesPerCycle": 32,
      "oldFeedbackCount": 128,
      "oldDependencyMax": 127,
      "newFeedbackCount": 255,
      "newComponentArity": 3,
      "newDependencyMax": 4
    }
  ]
}
```

```javascript
function verify(){
 const stats={kernel:0,forestCases:0,conditionalTV:0,jointMoment:0,chain:0,resplitting:0};
 const check=(ok,k)=>{if(!ok)throw Error(k);stats[k]++};
 const abs=x=>x<0n?-x:x;
 const subm=m=>{const a=[];for(let s=m;;s=(s-1)&m){a.push(s);if(!s)return a}};
 const bit=(m,i)=>(m>>i)&1;
 for(const D of [2,4,32,128,1024])for(const P of [0,1,2])for(let p=0;p<=20;p++)for(let q=1;q<=20;q++){
  const d=BigInt(2*D),a=d-BigInt(P),x=BigInt(p),y=BigInt(q);
  // Row TV for effective residual P/(2D), likelihood ratio t=p/q.
  check(BigInt(P)*x*y*BigInt(4*D-3)<= (x+y)*(a*x+d*y),"kernel");
 }
 let seed=816;const rnd=()=>seed=(Math.imul(seed,1664525)+1013904223)>>>0;
 const factors=[[0,1,2],[2,3],[3,4]],Ds=[128,32,32],G=5,full=31;
 const ports=Array.from({length:G},(_,i)=>[i]),fp=[];let count=G;
 const adj=Array.from({length:G+factors.length},()=>[]);
 factors.forEach((vs,j)=>{fp[j]=[];for(const i of vs){ports[i].push(count);fp[j].push(count++);adj[i].push(G+j);adj[G+j].push(i)}});
 function denPath(a,b){const walk=(v,parent,d)=>{if(v===b)return d;for(const u of adj[v])if(u!==parent){const t=walk(u,v,u>=G?d*BigInt(4*Ds[u-G]-3):d);if(t!==null)return t}return null};return walk(a,-1,1n)}
 function sumBound(A,B){let num=0n,den=1n;for(let i=0;i<G;i++)if(bit(A,i))for(let j=0;j<G;j++)if(bit(B,j)){let d=denPath(i,j);num=num*d+den;den*=d}return [num,den]}
 for(let rep=0;rep<16;rep++){
  const tables=ports.map(v=>Array.from({length:1<<v.length},()=>BigInt(rnd()%11)));
  for(const t of tables)if(t.every(x=>!x))t[0]=1n;
  const hist=Array(32).fill(0n);
  for(let m=0;m<(1<<count);m++){
   let w=1n;for(let i=0;i<G;i++){let ix=ports[i].reduce((s,v,j)=>s+(bit(m,v)<<j),0);w*=tables[i][ix]}
   for(let j=0;j<fp.length;j++)w*=BigInt(Ds[j]-(fp[j].every(v=>bit(m,v))?1:0));
   hist[m&full]+=w;
  }
  function mass(mask,val){return hist.reduce((s,w,m)=>s+((m&mask)===val?w:0n),0n)}
  for(let C=0;C<=full;C++)for(const val of subm(C)){
   const rem=full^C,base=mass(C,val);if(!base)continue;
   for(let i=0;i<G;i++)if(bit(rem,i)){
    const a=mass(C|(1<<i),val),b=mass(C|(1<<i),val|(1<<i));if(!a||!b)continue;
    for(const B of subm(rem^(1<<i)))if(B){
     let tv=0n;
     for(const z of subm(B)){
      const x=mass(C|(1<<i)|B,val|z),y=mass(C|(1<<i)|B,val|z|(1<<i));tv+=abs(x*b-y*a);
     }
     const [num,den]=sumBound(1<<i,B);check(tv*den<=2n*a*b*num,"conditionalTV");
    }
   }
   for(const A of subm(rem))if(A)for(const B of subm(rem^A))if(B){
    const a=mass(C|A,val|A),b=mass(C|B,val|B),ab=mass(C|A|B,val|A|B);
    const [num,den]=sumBound(A,B);check(abs(ab*base-a*b)*den<=a*base*num,"jointMoment");
   }
  }
  stats.forestCases++;
 }
 const chain=[];
 for(const n of [2,8,32,128,512]){
  let a=1n,b=0n,c=0n,d=1n;
  for(let j=1;j<n;j++)[a,b,c,d]=[32n*(a+b),32n*a+31n*b,32n*(c+d),32n*c+31n*d];
  const num=abs(a*d-b*c),den=(a+b)*(c+d);
  check(num===32n**BigInt(n-1)&&num*125n**BigInt(n-1)<=den,"chain");
  chain.push({blocks:n,softDistance:n-1,exactDenominatorBits:den.toString(2).length,bound:"125^-"+(n-1)});
 }
 const networks=[];
 for(const [n,m] of [[4,4],[16,32],[32,128],[128,32]]){
  // n disjoint retained m-cycles; private leaf at each cycle vertex;
  // top chain joins cycle positions 1 to next position 0; spoke at 2 to x_i;
  // bottom x_i form a cycle. Original groups partition roads.
  const gs=[],degrees=new Map();const inc=new Map();
  const add=(vs,ds)=>{const j=gs.length;gs.push(vs);vs.forEach((v,k)=>{if(!inc.has(v))inc.set(v,[]);inc.get(v).push(j);degrees.set(v,(degrees.get(v)||0)+ds[k])})};
  const v=(i,j)=>"v"+i+":"+j,x=i=>"x"+i;
  for(let i=0;i<n;i++){
   const vs=Array.from({length:m},(_,j)=>v(i,j));add(vs,vs.map(()=>2));
   for(let j=0;j<m;j++)add([v(i,j),"leaf"+i+":"+j],[1,1]);
   if(i+1<n)add([v(i,1),v(i+1,0)],[1,1]);
   add([v(i,2),x(i)],[1,1]);add([x(i),x((i+1)%n)],[1,1]);
  }
  const D=new Set(Array.from({length:n},(_,i)=>x(i))),Dp=new Set([...D,...Array.from({length:n-1},(_,i)=>v(i+1,0))]);
  function inspect(cut){
   const seen=new Set(),dep=new Map([...cut].map(v=>[v,new Set()]));let max=0,forest=true;
   for(let g=0;g<gs.length;g++)if(!seen.has("g"+g)){
    let q=["g"+g],s=new Set(),edgeCount=0;seen.add(q[0]);
    for(let k=0;k<q.length;k++){
     const z=q[k];if(z[0]==="g"){for(const u of gs[Number(z.slice(1))])if(cut.has(u))s.add(u);else if(inc.get(u).length>1){edgeCount++;const t="s"+u;if(!seen.has(t)){seen.add(t);q.push(t)}}}
     else for(const j of inc.get(z.slice(1))){edgeCount++;const t="g"+j;if(!seen.has(t)){seen.add(t);q.push(t)}}
    }
    forest&&=(edgeCount/2===q.length-1);max=Math.max(max,s.size);
    for(const u of s)for(const w of s)if(u!==w)dep.get(u).add(w)
   }
   return {forest,max,deg:Math.max(...[...dep.values()].map(s=>s.size)),paid:[...dep].every(([u,s])=>s.size<=2*degrees.get(u))};
  }
  const old=inspect(D),fresh=inspect(Dp);
  check(old.forest&&old.max===n&&old.deg===n-1&&fresh.forest&&fresh.max<=3&&fresh.paid,"resplitting");
  networks.push({cycles:n,interfacesPerCycle:m,oldFeedbackCount:D.size,oldDependencyMax:old.deg,newFeedbackCount:Dp.size,newComponentArity:fresh.max,newDependencyMax:fresh.deg});
 }
 return {stats,checks:Object.entries(stats).filter(([k])=>k!=="forestCases").reduce((s,[,v])=>s+v,0),chain,networks};
}
console.log(JSON.stringify(verify(),null,2));
```

Next: use the conditional path bounds to control higher joint cumulants in a weighted forest metric, or develop a complex-message analogue with certified zero-free disks. The real two-set bound alone does not justify truncating signed feedback series; large internal blocks can still have arbitrary joint interface correlations. Seek a tractable cut or internal decomposition for those cases. General complete Port FPTAS remains open.
