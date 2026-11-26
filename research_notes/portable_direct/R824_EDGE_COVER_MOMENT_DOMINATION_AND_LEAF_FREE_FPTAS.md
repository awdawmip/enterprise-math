# R824 - Edge-cover moment domination and leaf-free Port FPTAS at degree four

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_MOMENT_CHECKED / NOT_REVIEWED.
Independent portable continuation, EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own metadata request r3-20261127-r824-own-read confirmed original registered SID, no runs, execution_authorized=false. Running inventory r3-20261127-r824-running-read was RUNNING during derivation; no shared claim or owner change. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 and joint-observer directly read as blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14. Frozen generated startup 404; current normative BRC-only companion read. Account entries immutable main snapshot 0250100c763e5ae6c3ada7545826879da3ae3d3d (matching both entry blobs); ACTIVE worldview and applicable policies read. Predecessor ee223a9580c3762b395c61fd753d64df0f4a07e7:research_notes/portable_direct/R823_EXACT_LEAF_ATTENUATION_AND_PORT_CORE_FPTAS.md, verified blob e11a7669534a39c2fd92403a5ca7258542818136. Reuse R812, R813, R820, R822 in same directory (read blobs 8ee90887417c0c09170b91f2ecd3a17dfcc9f3fb, a3511002437d4fd080f272fbea23c55fa9ff30b3, 7810b200b9af2c073209408595a2222431517e60, 60acefe69f50eeeb7dac38774f2d42db07421635). Scope: R812 auxiliary rational nonnegative fixed-charge occupancy/parity observer, not native Heartbeat evolution or native residual attribution. Full road matrices, signed BRC, branch source, time order and common depth remain preserved.

## 1. Joint moment domination directly from the road matrix

Use R812's exact block law. For each block B, local affine parity support F is a subset of retained edges, with fixed boundary charge t_B. The joint weight of (x,F) is proportional to prod_e S_e(x_e) eta(F) times prod_{w internal} g_w(x), with x_e=11 required on F and g_w=1-delta_w I(all w ports empty). Shared vertex v has interface z_Bv=1 iff all its B ports are empty. Assume feasible charge, S_e(11)>0, a_w=1-delta_w>0, and nonnegative rational road weights. There is no extra interface pinning in the base law. Each edge has ordered endpoint bits.

For e=uv with both endpoints shared, define W=sum_x S_e(x), m_u=(S00+S01)/W, m_v=(S00+S10)/W, m_uv=S00/W. Pick any rational theta_eu,theta_ev in [0,1] satisfying
theta_eu >= m_u, theta_ev >= m_v, theta_eu theta_ev >= m_uv.
They always exist (both 1). For example a symmetric rational dyadic upper approximation to max(m_u,m_v,sqrt(m_uv)) suffices; asymmetric allocations are also permitted. These are envelope coefficients, not replacement marginals.

For e=uw with only u shared, choose theta_eu equal to the larger of the two ratios
(S00+S01)/W,
(a_w S00+S01)/(a_w(S00+S10)+S01+S11),
where u is the first bit (transpose otherwise). Reason: after fixing all other edges, the internal endpoint factor is either identically 1 or multiplies the weight by a_w precisely when w's bit on e is 0. The denominator is positive. For an edge with no shared endpoint no payment is needed. Define p_Bv=prod_{e in B incident v} theta_ev.

Theorem: for every subset A of shared vertices of B,
m_B(A)=E_B prod_{v in A} z_Bv <= prod_{v in A} p_Bv.
The bound holds uniformly over all feasible local parity charges and positive eta, and allows zeros in S.

Proof: condition first on the entire parity support F, retaining its exact distribution; the event all selected interfaces are empty is the intersection of one event E_e per edge touching A. If e belongs to F, then E_e is impossible. Otherwise, conditional on all road states other than e (with positive conditional mass), its weight is exactly S_e times endpoint factors at the internal endpoints. For two shared endpoints neither endpoint contributes an internal factor, hence the one- or two-end emptiness probability is respectively m_u,m_v,m_uv and bounded by the product of its selected theta values. For one shared endpoint the preceding two ratios give the same bound. Thus each E_e has a uniform conditional bound even given every other road state. Iterating conditional expectations, since all remaining E_f depend only on other edges, removes one edge event at a time and multiplies the bounds. The result is uniform in F; average over F and regroup the product by selected vertex. This proves the claim without assuming independence within B. In particular it is not necessary to bound each port's conditional probability given all other interface pins: for a diagonal road that conditional probability may be 1.

Example of necessary distinction: one diagonal road S00=1, S11=M>0, S01=S10=0, F empty, both endpoints shared. Both marginal empty probabilities are p=1/(1+M), yet joint emptiness has probability p, strictly greater than p^2. Marginal multiplication is invalid. The envelope constraint theta_u theta_v>=p retains the cost of this full joint event and is necessary for this one-road case. Under a forced parity support on this edge, the event is instead identically zero.

## 2. Moment-paid zero-free region and exact-coefficient FPTAS

Use independent original groups B in R812, factors f with I_f=prod_{B incident f} z_Bf and original coefficient delta_f. Define lambda_f=prod_{B incident f}p_Bf. For every factor set A, exact moment m(A) factorizes over dependency components and satisfies 0<=m(A)<=prod_{f in A}lambda_f by section 1. If lambda_f=0 the factor is inactive almost surely in this base law; omit it from this observer only. Otherwise R820 section 2 polymer weights satisfy
|w(C)|=|prod_{f in C}(-delta_f t^{c_f}) m(C)| <= prod_{f in C}(delta_f lambda_f R^{c_f})
for |t|<=R. One may directly reuse its rooted-tree induction: it only needs this absolute product envelope plus disconnected moment factorization, not a new probability law. Set c_f=s_f+max_{B incident f}ceil(log2 b_B) as in R822 and q_f=2^{c_f}delta_f lambda_f. If each group load beta_B=sum_{f incident B}q_f <=1/8, then
prod_{g adjacent f}(1-q_g)^2 >= (7/8)^{2s_f} >= (7/8)^{2c_f};
delta_f lambda_f (3/2)^{c_f} <= q_f (7/8)^{2c_f}, since 3/2<49/32.
R820 gives all deletion ratios within q_f of 1 on radius 3/2. Telescope log and use Cauchy as R822:
P(t) nonzero on |t|<=3/2, |log P(t)|<=g/7,
|log P(1)-sum_{j=1}^k [t^j]log P(t)| <= (2g/7)(2/3)^k.
Crucial: P(t)=E prod_f (1-delta_f t^{c_f} I_f) uses ORIGINAL delta and EXACT joint moments, not delta*lambda. The latter is an analytic budget only. R822 queue encoding, connected support Mobius difference, and R813 pinned oracle calculate the true coefficients; their complexity g 2^{O(k)} poly(N,k) remains valid. With k=O(log((g+1)/epsilon)), recover a certified relative 1+/-epsilon approximation to the original fixed-charge partition as R822. Infeasible charge is zero exactly. Rational envelope verification is polynomial-bit by direct products and comparisons, and exact moments retain R813's stated local-oracle hypotheses. This certificate applies to unpeeled groups; arbitrary imposed interface pins can invalidate an original envelope and need a separate proof. No factor independence approximation and no new native computation.

## 3. A leaf-free degree-four family with no long roads

Take g odd >=5 disjoint retained ladders (2 by b/2, b=g-1), with one outside-J connector between every pair of ladders, using each of a ladder's b vertices once. All vertices are shared, degree 3 at ladder corners and 4 otherwise; the incidence graph has no leaves, no pendant branches. Every retained block has width two, arbitrary cycle rank and b interfaces. The graph contains a K_g minor by contraction, hence unbounded treewidth. No road is subdivided.

On every retained ladder edge use diagonal rational S00=1, S11=b^2, S01=S10=0, with any allowed eta. For both shared endpoints, theta=1/b is valid since m_u=m_v=m_uv=1/(1+b^2) <=1/b^2. Consequently p_Bv<=b^(-2) at every ladder interface. On connector groups use envelope 1, allowing any admissible connector weight. A factor at a ladder vertex has s=2 and delta<=2^-7 (original d>=3), with 2^{c_f}<=8b. Thus q_f<=1/(16b), beta_ladder<=1/16 and beta_connector<=1/(8b), all below 1/8. R824 certifies an FPTAS for every feasible charge, with no leaf attenuation or long propagation. R822's raw certificate fails for the saturated examples: d<=4 gives delta>=2^-9, 2^{c_f}>=4b, so beta_ladder>=b^2/128>1/8 for b>=6. This compares sufficient certificates, not hardness. R823's leaf peeling does nothing on this incidence topology. The diagonal matrices are admissible in R812's auxiliary model; realization by a particular native road generator remains open.

## 4. Exact finite validation and next question

The appended JS BigInt code enumerates all road states and all eligible parity subsets on four small block shapes, with 12 deterministic weight cases each (diagonal, asymmetric and zero entries; retained or nonretained road sets; internal factors 7/8 or 1). It checks all shared-interface subsets for every charge with positive exact mass, using rational cross-products. Executed result:
{"shapes":4,"instances":48,"feasibleCharges":318,"zeroCharges":498,"momentChecks":3060,"localEnvelopeChecks":420,"diagonalStrictChecks":4}
All 3484 comparisons passed. This finite check is an auxiliary combinatorial identity/inequality validation, not a native BRC execution, independent review or FPTAS benchmark. Some tested shapes/charges serve as broader local-factor fixtures rather than canonical R812 retained block partitions.

Next: optimize asymmetric theta allocations under the local loads, and exploit conditional parity support/mandatory occupation to improve the edge-cover budget for weakly biased matrices, including S00~S11. Investigate whether a certified exact forest merge can combine this budget with R823 attenuation without enlarging the interface cost too much. General Port FPTAS and native realizability remain open.

## Reproducible exact test
```javascript
function verify(){
 let seed=824;const rnd=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed};
 const shapes=[{n:4,E:[[0,1],[1,2],[2,3],[3,0]],U:[0,1,2,3]},
 {n:4,E:[[0,1],[1,2],[2,0],[2,3]],U:[0,1,3]},
 {n:5,E:[[0,1],[1,2],[2,3],[3,4],[4,0]],U:[0,2,4]},
 {n:2,E:[[0,1]],U:[0,1]}];
 const mul=(x,y)=>[x[0]*y[0],x[1]*y[1]];
 const le=(x,y)=>x[0]*y[1]<=y[0]*x[1];
 const max=(x,y)=>le(x,y)?y:x;
 const counts={shapes:shapes.length,instances:0,feasibleCharges:0,zeroCharges:0,momentChecks:0,localEnvelopeChecks:0,diagonalStrictChecks:0};
 for(const {n,E,U} of shapes)for(let trial=0;trial<12;trial++){
  counts.instances++; const b=U.length,m=E.length;const S=E.map(()=>trial%3===0?[1n,0n,0n,BigInt(2+rnd()%50)]:[BigInt(rnd()%7),BigInt(rnd()%8),BigInt(rnd()%8),BigInt(1+rnd()%20)]);
  const J=trial%4===0?0:(1<<m)-1;const g=Array.from({length:n},(_,v)=>U.includes(v)?[1n,1n]:[BigInt(7+rnd()%2),8n]);
  const p=U.map(()=>[1n,1n]);
  for(let j=0;j<m;j++){
   const [u,v]=E[j],ui=U.indexOf(u),vi=U.indexOf(v);if(ui<0&&vi<0)continue;
   const T=S[j],marg=(which,mask)=>{let den=0n,num=0n;for(let x=0;x<4;x++){let a=x>>1,c=x&1;let w=T[x]*(mask&1&&!a?g[u][0]:g[u][1])*(mask&2&&!c?g[v][0]:g[v][1]);den+=w;if((which===0&&!a)||(which===1&&!c)||(which===2&&!a&&!c))num+=w;}return [num,den]};
   if(ui>=0&&vi>=0){let a=marg(0,0),c=marg(1,0),d=marg(2,0),t=[1n,1n];while(t[1]<1024n){let h=[1n,t[1]*2n];if(!le(a,h)||!le(c,h)||!le(d,mul(h,h)))break;t=h;}
    if(!le(a,t)||!le(c,t)||!le(d,mul(t,t)))throw Error("bad pair");counts.localEnvelopeChecks+=3;p[ui]=mul(p[ui],t);p[vi]=mul(p[vi],t);
   }else{let i=ui>=0?ui:vi,which=ui>=0?0:1,mask=ui>=0?2:1;let a=marg(which,0),c=marg(which,mask),t=max(a,c);if(!le(a,t)||!le(c,t))throw Error("bad single");counts.localEnvelopeChecks+=2;p[i]=mul(p[i],t);}
  }
  const mass=Array.from({length:1<<n},()=>Array(1<<b).fill(0n));
  for(let x=0;x<4**m;x++){let code=x,occ=0,avail=0,wt=1n;for(let j=0;j<m;j++){let k=code%4;code=Math.floor(code/4);wt*=S[j][k];let [u,v]=E[j];if(k>>1)occ|=1<<u;if(k&1)occ|=1<<v;if(k===3)avail|=1<<j;}if(!wt)continue;for(let v=0;v<n;v++)wt*=occ&(1<<v)?g[v][1]:g[v][0];let z=0;for(let i=0;i<b;i++)if(!(occ&(1<<U[i])))z|=1<<i;
   let allowed=avail&J;for(let F=allowed;;F=(F-1)&allowed){let charge=0,k=0;for(let j=0;j<m;j++)if(F&(1<<j)){let[u,v]=E[j];charge^=(1<<u)|(1<<v);k++;}mass[charge][z]+=wt*(1n<<BigInt(m-k));if(!F)break;}
  }
  for(let ch=0;ch<(1<<n);ch++){let H=mass[ch].reduce((s,x)=>s+x,0n);if(!H){counts.zeroCharges++;continue}counts.feasibleCharges++;for(let A=0;A<(1<<b);A++){let z=0n,t=[1n,1n];for(let i=0;i<b;i++)if(A&(1<<i))t=mul(t,p[i]);for(let j=0;j<(1<<b);j++)if((j&A)===A)z+=mass[ch][j];if(!le([z,H],t))throw Error("moment failure");counts.momentChecks++;}}
  if(n===2&&trial%3===0){let H=S[0][0]+S[0][3];if(!(S[0][0]*H>S[0][0]**2n))throw Error("diagonal correlation");counts.diagonalStrictChecks++;}
 }
 return counts;
}
console.log(verify());
```
