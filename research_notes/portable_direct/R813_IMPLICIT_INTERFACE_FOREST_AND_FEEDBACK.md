# R813 — Implicit interface contraction, feedback-factor correction and degree-paid pruning

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R812, no shared CLAIM/RUN/Result. Predecessor 3388232532a0199a3ce794fd8fde628a4d402c16:research_notes/portable_direct/R812_CHARGED_BLOCK_INTERFACE_FPTAS.md. Frozen scientific source a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read directly. Current account entries verified at 0a6c0ce6a3ac7990be16286749206cf333da25da; ACTIVE worldview and applicable policies read. Own metadata recovery r3-20261126-r813-own-metadata confirms original session registration, no own run, execution_authorized=false. Running inventory original request r3-20261126-r813-running-read was still RUNNING during derivation; do not infer an empty owner set. Researcher EM-DIRECT-82A007 / TASK_RESEARCH. All results are for the R812 auxiliary positive combinatorial occupancy/parity observer. Retain original matrices, signed/native BRC, branch provenance, time order, and common-depth coordinate.

## 1. Implicit interface oracle

Use all definitions of R812 section 1–2: explicit rational edge weights S_e(x), eta_e>0, original degree d_v and a_v>=1-2^(-2d_v-1), delta_v=1-a_v. For feasible T, its affine parity supports factor by retained biconnected blocks plus outside-J singletons. At each shared vertex v, z_{Bv}=1 iff all B ports at v are empty; h_B(z) is the nonnegative joint interface table defined in R812, but we do not materialize it. Define

 L_B(u)=sum_z h_B(z) prod_{v in U_B} u_v(z_v),    u_v(0),u_v(1)>=0.

This is an exact weighted joint observer, not a product of marginals. It includes any chosen interface pinnings by setting the unwanted weight to zero. At a tree-decomposition forget vertex, use the R812 state (parity,OR of occupied bits). Enforce local charge, multiply g_v for internal v, or u_v(1-OR) for shared v. The 5 edge alternatives and XOR/OR bag join are otherwise unchanged. Thus L_B costs O(16^(t_B+1) poly(input/decomposition size)) rational operations with a supplied width t_B decomposition. The alternative R812 affine support plus chord/tree DP gives O(8^r_B poly(input)) per call: at a shared vertex use u_v(0)(U-V)+u_v(1)V instead of fixing z. There is no factor 2^b_B in either construction. No assumption of independence within a block. No hidden exponential preprocessing of h_B. Local charge is fixed by the original forest parity solve.

## 2. Exact factor-incidence forest contraction

Build bipartite graph H with one node per group B, one per shared vertex v, and edge B-v for each interface. Normalized Q_T(J)/K_0 is the contraction of h_B and shared factors g_v=1-delta_v prod_B z_{Bv}. If H is a forest, root each component at a group. Message from shared factor v to parent block B is
 A=prod_{C != B}(m_C(0)+m_C(1)); P=prod_{C != B}m_C(1),
 m_{v->B}(0)=A, m_{v->B}(1)=A-delta_v P.
Both are nonnegative. Message from B to parent v at bit b is L_B with incoming child weights and u_v=indicator of b. Missing factors contribute unary weights (1,1); optional original pinnings are unary indicators. Root group uses one L_B. Induction on the rooted forest proves equality by summing disjoint descendant edge variables conditional on the single incident bit. Each message counts the exact original weighted assignments in its subtree. At most two oracle calls per nonroot group, one per root. Other work linear in H in arithmetic operations. The result is exact for every feasible T (infeasible T is exactly zero by R812 component parity). This removes any bound on b_B or A_B for this topology. H is constructible in polynomial time from the original G,J. With J=E the block-cut incidence graph is always a forest, hence exact with bounded/logarithmic internal width or cycle rank; the extension permits E\J edges that induce a forest of groups as well.

## 3. Exact feedback-factor contraction and approximation

Let D be any supplied subset of shared-vertex factor nodes such that H-D is a forest. Z_0 is the exact partition with those factors replaced by 1, and Z_A for A subset D is the same forest partition with all interface bits incident to every v in A pinned to 1. Pinning is done inside each L_B with unary indicators. Define I_v=prod_B z_{Bv}. Exact finite expansion gives

 Z= sum_{A subset D} (-1)^|A| (prod_{v in A} delta_v) Z_A.

The signs are inclusion-exclusion coefficients in an auxiliary rational computation; the original weights are nonnegative, not native phase cancellation. Exact rational arithmetic gives no rounding loss. The forest structure is independent of A. Cost O(2^|D| times the forest oracle cost). More generally a hybrid subset D can be removed, and only a selected subset K of D restored by the same expansion with remaining D\K omitted. This yields a controllable choice of exact feedback restoration and bounded residual removal.

Let R=D\K and Z_K the partition restoring K. Pointwise product of the R factors lies in [prod_R a_v,1]. Thus for every feasible T and every nonnegative restriction on the original assignments,

 (prod_R a_v) Z_K <= Z <= Z_K,
 0<= (Z_K-Z)/Z_K <= 1-prod_R a_v <= sum_R delta_v.

The inequality is uniform across charges. To obtain relative error <=epsilon with respect to Z, require sum_R delta_v<=epsilon/(1+epsilon), or equivalently use the exact product threshold. For fixed supplied D, minimizing |K| under the sum certificate is achieved by restoring the largest delta_v first (exchange argument); finding an optimal D globally is not claimed.

A sharper a posteriori certificate uses forest event partitions. For K empty,
 S_j=sum_{A subset D, |A|=j} (prod delta_v) Z_A.
Then S_0-S_1 <= Z <= S_0-S_1+S_2, and more generally even and odd truncated alternating sums bracket Z (ordinary Bonferroni: conditional on each assignment, introduce independent Bernoulli events of probabilities delta_v I_v, then integrate). Computing through fixed order j costs O(|D|^j) forest contractions. In particular error upper bound S_1/Z_0 = sum delta_v Pr_0(I_v=1), often much smaller than sum delta_v. For a certified interval [L,U], L>0 and U/L<=1+epsilon, U gives a valid relative approximation. The same proof with Z_K instead of Z_0 uses the exact hybrid oracle. No claim that low-order truncation always suffices. Original factors and correction coordinates are retained.

## 4. Polynomial-time families with unbounded interfaces

If local t_B or r_B are O(log N) with supplied decompositions where needed, and a supplied D is split as K,R with |K|=O(log(N/epsilon)), sum_R delta_v<=epsilon/(1+epsilon), the algorithm is deterministic polynomial in explicit input size N and 1/epsilon. More precisely a uniform FPTAS for a family requires this certificate to be available or constructible in polynomial time for every epsilon, with uniform constants. This is an alternative to R812's fixed b and A_B constraints, not a general arbitrary-incidence FPTAS.

An explicit degree pruning rule: choose R as all shared vertices of original degree >=d_* where n*2^(-2d_*-1)<=epsilon/(1+epsilon), n=|V|. If H-R is a forest, no feedback expansion is needed. If H-R has a supplied feedback set K of logarithmic size, apply section 3. A feedback set can also be constructed by repeatedly choosing the shared-factor endpoint of a non-tree edge in a spanning forest, at most the cycle rank of H-R; deleting these factors removes all non-tree edges. Verify the resulting forest directly. This yields a polynomial certificate when the remaining incidence cycle rank is logarithmic. The high-degree error uses the original degree, not the degree after removal.

A scalable example: take J a long cycle of length n and outside-J spokes from each cycle vertex to a common hub. All n cycle vertices are interfaces, and H has cycle rank n-1, but removal of just the hub factor yields a forest. Exact correction needs two contractions, independent of n. With S(00)=2,S(11)=1, mixed states zero, eta=1, a_v=1-2^(-2d_v-1), every even cycle charge is feasible; the cycle oracle is a constant-width transfer of two occupancy bits and two affine support patterns. The uniform deletion certificate is 2^(-2n-1) relative to the deleted-factor partition. This example permits b=n, including n>127, without constructing 2^n interface values. Analogous multiple hub groups with large original degrees can be removed and paid by the sum bound.

Bit complexity: each oracle/message is a sum of products of explicit input rationals over assignments on a disjoint set of physical edges and vertex factors. Denominators divide products of input denominators, numerators have polynomial bit size (at most exponential number of assignments with polynomial log count). Each feedback expansion term contains each factor coefficient at most once, all terms share a polynomial-size common denominator, and the number of terms adds at most |D| counting bits. Use reduced rational arithmetic. Thus the claimed polynomial regimes include exact rational bit cost; no succinct binary-compressed road length assumption. Q_T=K_0 Z_T with K_0=2^n prod isolated a_v; K_0 cancels in relative certificates.

## 5. Exact finite verification and limits

Actual JS BigInt verifier output:
{
  "abstractCases": 100,
  "physicalCases": 60,
  "exactChecks": 1043,
  "certificateChecks": 4172,
  "large": [
    {
      "cycleInterfaces": 32,
      "feedbackFactors": 1,
      "exactNumeratorBits": 389,
      "uniformRelativeBound": "2^-65",
      "interfaceTableEntries": "2^32"
    },
    {
      "cycleInterfaces": 128,
      "feedbackFactors": 1,
      "exactNumeratorBits": 1557,
      "uniformRelativeBound": "2^-257",
      "interfaceTableEntries": "2^128"
    },
    {
      "cycleInterfaces": 512,
      "feedbackFactors": 1,
      "exactNumeratorBits": 6229,
      "uniformRelativeBound": "2^-1025",
      "interfaceTableEntries": "2^512"
    }
  ]
}

Abstract tests cover five small incidence patterns with twenty deterministic nonnegative tables each, including zeros, all feedback-factor subsets that leave forests, comparison to direct contraction, Bonferroni and pointwise product certificates. Physical tests independently compare all even cycle charges for n=3..6 against original edge-occupancy and parity enumeration, with hub feedback and integer-scaled factors. Large cycle/spoke instances n=32,128,512 use implicit transfer oracle with nonzero boundary charge and exact feedback correction, no exponential table. The generic tree-decomposition implementation is proved analytically, not executed here. The verifier is not an independent review. Next: extend the implicit oracle beyond incidence forests by structured separators or a convergent weighted feedback expansion with polynomial term enumeration; seek uniform guarantees for low-degree overlapping external coupling without assuming a small feedback set.

```javascript
function verify(){
 const prod=a=>a.reduce((x,y)=>x*y,1n),sum=a=>a.reduce((x,y)=>x+y,0n);
 const stats={abstractCases:0,physicalCases:0,exactChecks:0,certificateChecks:0,large:[]};
 const check=(x,k)=>{if(!x)throw Error(k);};
 // Integer scaled shared factors: D_v - I(all bits 1). Deleted factors replaced by D_v.
 function forest(groups,vertices,den,removed,pinned){
  const adj=groups.map(g=>g.v.filter(v=>!removed.has(v)));
  const inc=vertices.map(v=>groups.map((g,i)=>g.v.includes(v)?i:-1).filter(i=>i>=0));
  const seenG=new Set(),seenV=new Set();
  function gm(i,parent){
   if(seenG.has(i))throw Error("not a forest");
   seenG.add(i);
   const u=new Map(groups[i].v.map(v=>[v,pinned.has(v)?[0n,1n]:[1n,1n]]));
   for(const v of adj[i])if(v!==parent)u.set(v,vm(v,i));
   if(parent===-1)return groups[i].oracle(u);
   return [0,1].map(b=>{const w=new Map(u);w.set(parent,b?[0n,1n]:[1n,0n]);return groups[i].oracle(w);});
  }
  function vm(v,parent){
   if(seenV.has(v))throw Error("not a forest");
   seenV.add(v);
   const m=inc[v].filter(i=>i!==parent).map(i=>gm(i,v));
   const a=den[v]*prod(m.map(x=>x[0]+x[1]));
   return [a,a-prod(m.map(x=>x[1]))];
  }
  let total=1n;
  for(let i=0;i<groups.length;i++)if(!seenG.has(i))total*=gm(i,-1);
  return total;
 }
 function evaluate(groups,den,D){
  const V=den.map((_,i)=>i),R=new Set(D);
  const base=forest(groups,V,den,R,new Set()),scale=prod(D.map(v=>den[v]));
  let exact=0n,first=0n,second=0n;
  for(let m=0;m<2**D.length;m++){
   const A=D.filter((_,i)=>m>>i&1),P=new Set(A);
   const term=forest(groups,V,den,R,P)*prod(D.filter(v=>!P.has(v)).map(v=>den[v]));
   exact+=(A.length%2?-term:term);
   if(A.length===1)first+=term;
   if(A.length===2)second+=term;
  }
  const upper=base*scale;
  check(exact<=upper&&exact>=upper-first&&exact<=upper-first+second,"Bonferroni");stats.certificateChecks+=3;
  check(exact*scale>=upper*prod(D.map(v=>den[v]-1n)),"uniform certificate");stats.certificateChecks++;
  return {exact,upper,first,second};
 }
 function table(v,w){
  return {v,w,oracle:u=>sum(w.map((a,m)=>a*prod(v.map((x,i)=>u.get(x)[m>>i&1]))))};
 }
 function bruteGroups(G,den){
  let ans=0n;const flags=den.map(()=>1);
  function go(i,w,fl){
   if(i===G.length){ans+=w*prod(den.map((d,v)=>d-BigInt(fl[v])));return;}
   G[i].w.forEach((a,m)=>{let f=fl.slice();G[i].v.forEach((v,j)=>f[v]&=m>>j&1);go(i+1,w*a,f);});
  }
  go(0,1n,flags);return ans;
 }
 let seed=1701;const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
 const shapes=[[[0,1],[0,2],[1,2]],[[0,1,2],[0,1,3],[2,3]],[[0,1,2,3],[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[0],[1],[2]]];
 for(const shape of shapes)for(let j=0;j<20;j++){
  const n=Math.max(...shape.flat())+1,den=Array.from({length:n},(_,i)=>BigInt(8+2*((i+j)%7)));
  const G=shape.map(v=>table(v,Array.from({length:2**v.length},()=>BigInt(rand()%9))));
  // Deleting all vertices always yields a forest, plus test each minimal single or pair deletion that works.
  const Ds=[den.map((_,i)=>i)];
  for(let m=0;m<2**n;m++)if(m!==2**n-1){
   let D=den.map((_,i)=>i).filter(i=>m>>i&1);
   try{forest(G,den.map((_,i)=>i),den,new Set(D),new Set());Ds.push(D);}catch(e){if(e.message!=="not a forest")throw e;}
  }
  const truth=bruteGroups(G,den);
  for(const D of Ds){const q=evaluate(G,den,D);check(q.exact===truth,"abstract exact");stats.exactChecks++;}
  stats.abstractCases++;
 }
 // Physical identity roads: S(00)=2, S(11)=1, eta=1. J is cycle, spokes are outside J.
 // A fixed even charge induces precisely two complementary cycle supports.
 function cycle(n,T){
  const v=Array.from({length:n},(_,i)=>i),f=[0];
  for(let i=1;i<n;i++)f.push(f[i-1]^T[i]);
  check((f[n-1]^f[0])===T[0],"charge");
  const supports=[f,f.map(x=>1-x)];
  return {v,oracle:u=>{
   let total=0n;
   for(const F of supports)for(const first of [0,1]){
    if(F[0]&&!first)continue;
    let dp=[0n,0n];dp[first]=first?1n:2n;
    for(let i=1;i<n;i++){
     const nd=[0n,0n];
     for(const a of [0,1])for(const b of [0,1]){
      if(F[i]&&!b)continue;
      nd[b]+=dp[a]*(b?1n:2n)*u.get(i)[a||b?0:1];
     }dp=nd;
    }
    total+=dp[0]*u.get(0)[first?0:1]+dp[1]*u.get(0)[0];
   }return total;
  }};
 }
 function physical(n,T){
  const G=[cycle(n,T)];
  for(let i=0;i<n;i++)G.push(table([i,n],[1n,0n,0n,2n])); // index 0=both occupied, index 3=both empty
  const den=Array.from({length:n},()=>128n);den.push(2n**BigInt(2*n+1));
  return {G,den};
 }
 function brutePhysical(n,T,den){
  let ans=0n;
  for(let m=0;m<2**(2*n);m++){
   const x=Array.from({length:2*n},(_,i)=>m>>i&1);
   let w=2n**BigInt(x.filter(y=>!y).length);
   for(let i=0;i<n;i++)w*=den[i]-BigInt(!(x[(i+n-1)%n]||x[i]||x[n+i]));
   w*=den[n]-BigInt(!x.slice(n).some(Boolean));
   for(let f=0;f<2**n;f++){
    if(Array.from({length:n},(_,i)=>i).every(i=>((f>>i&1)^(f>>((i+n-1)%n)&1))===T[i]&&(!(f>>i&1)||x[i])))ans+=w;
   }
  }return ans;
 }
 for(let n=3;n<=6;n++)for(let t=0;t<2**n;t++){
  const T=Array.from({length:n},(_,i)=>t>>i&1);
  if(T.reduce((a,b)=>a^b,0))continue;
  const {G,den}=physical(n,T),q=evaluate(G,den,[n]);
  check(q.exact===brutePhysical(n,T,den),"physical exact");stats.exactChecks++;stats.physicalCases++;
 }
 for(const n of [32,128,512]){
  const T=Array.from({length:n},(_,i)=>+(i===0||i===n-1));
  const {G,den}=physical(n,T),q=evaluate(G,den,[n]);
  check(q.exact>0n&&q.upper-q.exact===q.first,"large one-factor exact");
  stats.exactChecks++;
  stats.large.push({cycleInterfaces:n,feedbackFactors:1,exactNumeratorBits:q.exact.toString(2).length,uniformRelativeBound:"2^-"+(2*n+1),interfaceTableEntries:"2^"+n});
 }
 return stats;
}
console.log(JSON.stringify(verify()));
```
