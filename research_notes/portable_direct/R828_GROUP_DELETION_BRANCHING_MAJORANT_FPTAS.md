# R828 — Group-deletion branching majorant and a three-quarter square-root load FPTAS

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_GAUSSIAN_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH: EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own recovery r3-20261127-r828-own-read verified metadata and no runs, execution_authorized=false. Prior request r3-20261127-r827-running-read resolved SUCCEEDED with empty RUNNING filter as of 2026-11-26T20:23:32.790409Z, Source drift recorded. New r3-20261127-r828-running-read RUNNING at derivation; no shared task acquisition or owner mutation. Source control snapshot 79d86b4cd6896ce3265febc2bee908bfd6698710; global canonical snapshot d5aa6f8967ab2672f39a8dfbcddcf446caee2ba1 verified both entry blobs. ACTIVE worldview, P000 V4 projection and canonical metadata, current portable, mathematical, residual and BRC-only policies read. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read; frozen Heartbeat companion 404; current companion read for method/terminology, not scientific repinning. Predecessor R827 63aad9407d05da2fcf5b822a01601f96a7a57d83:research_notes/portable_direct/R827_DECOUPLED_KRAFT_AND_ANALYTIC_LOAD_FPTAS.md; R825 current blob e0059e2bcd25f4706e8b31c6ce4ce5760c2fea0b and R820 section 2 at research_notes/portable_direct/R820_STEINER_OVERLAP_HOST_SUPPORT_FPTAS.md. Reuse R812/R813 observer scope through R825/R827. This is auxiliary fixed-charge combinatorial analysis, with no native BRC dynamics computation or native residual attribution. Preserve signed BRC, full road matrices, joint relations, branch identity/provenance, time order and common depth.

## 1. Group-deletion theorem

Let independent base groups be indexed by B in G, g=|G|. Each labeled factor f has a nonempty footprint F_f of s_f distinct groups. Let P_U(t)=E product_{f in U}(1+alpha_f I_f t^{c_f}) for subsets U of the finite explicit factor family. Integer costs c_f>=1, signed rational alpha_f, normalized nonnegative independent group law, exact polynomial-bit polynomial-time joint pinned moment oracles as in R825/R827. For any subset J assume |E product_{f in J} I_f|<=product_{f in J} lambda_f with moment factorization across disjoint group supports. Set b_f=|alpha_f|lambda_f, u_f=b_f R^{c_f} for fixed R>1. Positive exact baseline Z_base; original observer is Z=Z_base P_F(1); zero baseline treated exactly. If some b_f=0 it contributes zero to every term containing it for this fixed observer, without deleting original data.

For every group B choose rational 0<rho_B<1, and put A_B=(1+rho_B)/(1-rho_B). Sufficient certificate:

    product_{f: B in F_f} [1+u_f product_{D in F_f minus B} A_D] <= 1+rho_B.       (1)

Then for every subset U, |t|<=R, P_U(t) is nonzero and

    |P_U/P_{U minus F(B)} - 1| <= rho_B,    F(B)={f:B in F_f}.                    (2)

The normalized analytic log of the full P satisfies

    |log P(t)| <= sum_B rho_B/(1-rho_B).                                         (3)

Proof. Use connected polymers C of factors, where adjacency means intersecting footprints. The exact moment expansion is the hard-core polymer sum because disconnected moments factor. The polymer weight w(C) satisfies |w(C)|<=product_{f in C}u_f. In a compatible family at most one polymer touches group B. Thus the exact decomposition is

    P_U = P_{U minus F(B)} + sum_{C connected, C subset U, B in G(C)}
               w(C) P_{U minus N[C]},

where G(C)=union_{f in C}F_f and N[C] consists of all factors sharing any group in G(C), including C. Induct simultaneously on |U|. If U contains no factor at B, ratio is 1; for a nonempty U choose a group with a factor to prove nonvanishing first. For B with incident factors, remove from the smaller U minus F(B) the groups of G(C) other than B in succession. By the smaller-subset induction, the modulus of the last polynomial divided by the first is at most product_{D in G(C) minus B}(1-rho_D)^(-1). (A deletion that removes nothing has ratio 1.) Therefore the deviation in (2) is bounded by

    sum_{C connected, B in G(C)} product_{f in C}u_f
                                  product_{D in G(C) minus B}(1-rho_D)^(-1).   (4)

Majorize (4) with rooted alternating incidence trees. Root is group B; at a group node choose any subset of its incident factor labels as children; each factor child f has as group children all its other groups, in fixed order. Each factor occurrence carries u_f, each nonroot group occurrence carries (1-rho_D)^(-1). Allow repeated labels in distinct tree nodes; this is a nonnegative majorant only. For each connected support C, deterministically traverse it from B by a queue. At the first processed occurrence of a group discover all as-yet-undiscovered incident factors of C, and add all their other groups; duplicate group occurrences are leaves. Mark factors globally, so every factor in C occurs once. Connectivity ensures all factors are discovered. This creates one tree per C, injective since its factor label set is C. Every distinct nonroot group of G(C) is paid at least once; repeated group occurrences only enlarge the weight. The empty tree has weight one.

The finite-height majorants T_B^(0)=1 and
    T_B^(h+1)=product_{f: B in F_f}(1+u_f product_{D in F_f minus B} T_D^(h)/(1-rho_D))
count all these trees up to h alternating layers. By (1), T_B^(h)<=1+rho_B for all h. Monotone limit bounds the sum of all finite trees; thus (4)<=rho_B. This proves the induction, including nonvanishing by rho_B<1. Successively remove all groups, telescoping analytic logs of the deletion ratios; each ratio stays within rho_B of one and is one at t=0. The power series log(1+z) has modulus <=|z|/(1-|z|), which yields (3). No pairwise independence assumption inside a group and no replacement of the actual connected moment by its envelope in evaluation.

## 2. Oriented incidence witness (optional stronger variant)

The queue injection never reuses the parent factor as a child. For each incidence (B,f) choose Y_{B|f}>=1 such that
    product_{h incident B,h!=f}(1+u_h product_{D in F_h minus B} Y_{D|h}/(1-rho_D)) <= Y_{B|f}.
At each root require
    product_{h incident B}(1+u_h product_{D in F_h minus B} Y_{D|h}/(1-rho_D)) <=1+rho_B.
The same finite-height induction, now with the parent label excluded, gives (2)-(3). A rational witness is directly checkable with the explicit incidence input. The uniform choice Y_{B|f}=1+rho_B recovers (1). This variant may exploit actual incidence overlaps and heterogeneous weights; no optimization-complexity or universal sharpness claim.

## 3. Decoupled entropy: uniform threshold 3/4

Use R827's resource coordinates s_f>=2, a_f=2^{s_f}b_f, p_f>0, sum_{f incident B}p_f<=1, q_f=a_f/p_f, sum_{f incident B}q_f<=beta. Costs c_f=s_f+L_f, L_f=ceil(log2(1/p_f)). R825's queue enumeration is unchanged. Fix 1<R<2 and common rho, A=(1+rho)/(1-rho). Since p_f R^{L_f}<=R p_f^{1-log2 R}<=R, if

    R A <= 2,                beta R^3 A/4 <= log(1+rho),                         (5)

then u_f A^{s_f-1} = q_f p_f R^{L_f}(R/2)^{s_f} A^{s_f-1}
<= q_f R^3 A/4. Hence sum over factors at B <= beta R^3 A/4; product(1+x)<=exp(sum x) proves (1).

For M=max_B sum_{f incident B}sqrt(a_f)<=sqrt(beta), take p_f=sqrt(a_f/beta), q_f=sqrt(beta a_f). This satisfies the budgets. The integer length L_f can be computed by exact doubling until 2^{2L_f}a_f>=beta, as in R827; no exact square-root sum decision is needed on promised inputs. With supplied rational p_f, the more general (1) can be checked directly.

Two fixed rational parameter choices:
- rho=3/10, beta=1/2, R=33/32: M<=1/sqrt(2); tail <= (96g/7)(32/33)^k.
- rho=33/100, beta=9/16, R=257/256: M<=3/4; tail <= (8448g/67)(256/257)^k.
Both satisfy (5), verified exactly using log(1+rho)>=rho-rho^2/2+rho^3/3-rho^4/4, the alternating-series lower bound for 0<rho<1. R827's previous uniform family approached sqrt(1-1/sqrt(2))~0.541196. New fixed thresholds can approach sqrt(2 log(4/3))~0.7585276164: let rho approach 1/3 from below and R approach 1 from above while R A<=2, so the beta bound tends to 2 log(4/3). Every fixed M strictly below this limiting value admits a fixed rational beta>M^2 and rational rho,R with slack. No assertion at the limiting point, or of universal optimality. Close to the limit the smaller R leads to larger truncation degree.

## 4. Algorithmic implications and complexity

The Cauchy tail for the Taylor log at t=1 is
    E_k <= [sum_B rho_B/(1-rho_B)] R^{-k}/(R-1).
For a fixed rho,R use k=O(log((g+1)/epsilon)). Preserve R825's Kraft codes with c_f=s_f+L_f: connected factor supports of total cost <=k are enumerated by at most g 2^{k+O(1)} queue words. The analytic deletion grouping does not change these costs. For each support and its subsets compute exact truncated polynomial and formal log by summing exact pinned joint moments, then use R822/R825 support Mobius differences. Disconnected supports cancel by exact factorization; monomials whose union has cost greater than k cannot contribute. At most k factor labels and O(k) incidences per support; oracle, rational coefficients, and final certified scalar recovery have polynomial bit complexity as in R820/R825/R827. Input lengths are explicit; zero-activity labels are excluded only for the declared observer; only labels with cost <=k require constructing codewords, so large supplied lengths cause no exponential materialization. Result: deterministic FPTAS for the declared fixed-charge observer with fixed convergence margin. The actual coefficient uses complete joint moment, not the envelope or branching tree. No general Port representation or native realizability is inferred; no production benchmark.

## 5. Exact finite verification

Executed BigInt Gaussian-rational arithmetic below. {"parameter_checks":4,"rounding_term_checks":45760,"instances":42,"group_ratio_checks":23790,"oriented_witness_checks":52}. 69,606 exact comparisons, zero failures: two parameter pairs, all positive rational p=n/d with 1<=n<=d<=64 and arities 2..12; seven labeled incidence shapes including parallel factors, tetrahedron, star, mixed-arity and dense pair cycles, 42 group-probability/parameter fixtures. For each fixture and five rational complex points (zero, +/-R, iR and (3+4i)R/5), compare (2) by squared-modulus rational inequalities for every subset and incident group deletion. Within each group all ports share one bit (hard correlation), independent across groups, signs alternate; the moment of a factor subset is the product of group probabilities on its union. Full subset zeta transform yields P_U exactly. 'oriented_witness_checks' tests the uniform sufficient product (1), not a nonuniform optimization. No root solver, physical comparison, or native dynamics run; the general disk theorem is analytical.

```javascript
function verify(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
 const F=(x,y=0n,d=1n)=>{const g=gcd(gcd(x,y),d);return [x/g,y/g,d/g]};
 const add=(a,b)=>F(a[0]*b[2]+b[0]*a[2],a[1]*b[2]+b[1]*a[2],a[2]*b[2]);
 const neg=a=>[-a[0],-a[1],a[2]];
 const mul=(a,b)=>F(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0],a[2]*b[2]);
 const pow=(a,n)=>{let b=F(1n);while(n--)b=mul(b,a);return b};
 const le=(a,b)=>a[0]*b[2]<=b[0]*a[2];
 const norm=a=>F(a[0]*a[0]+a[1]*a[1],0n,a[2]*a[2]);
 const rat=(n,d)=>F(BigInt(n),0n,BigInt(d));
 const zero=F(0n),one=F(1n), stats={parameter_checks:0,rounding_term_checks:0,instances:0,group_ratio_checks:0,oriented_witness_checks:0};
 const ck=(v,k)=>{if(!v)throw Error(k);stats[k]++};
 const params=[[3,10,1,2,33,32],[33,100,9,16,257,256]];
 for(const [hn,hd,bn,bd,rn,rd] of params){
  const h=rat(hn,hd),beta=rat(bn,bd),R=rat(rn,rd),A=rat(hd+hn,hd-hn);
  const lower=add(add(h,neg(mul(pow(h,2),rat(1,2)))),add(mul(pow(h,3),rat(1,3)),neg(mul(pow(h,4),rat(1,4)))));
  ck(le(mul(mul(R,A),rat(1,2)),one),"parameter_checks");
  ck(le(mul(mul(mul(beta,pow(R,3)),A),rat(1,4)),lower),"parameter_checks");
  for(let d=1;d<=64;d++)for(let n=1;n<=d;n++){
   let L=0;while(BigInt(n)*(1n<<BigInt(L))<BigInt(d))L++;
   for(let s=2;s<=12;s++){
    const lhs=mul(mul(rat(n,d),pow(R,s+L)),mul(rat(1,2**s),pow(A,s-1)));
    const rhs=mul(mul(pow(R,3),A),rat(1,4));
    ck(le(lhs,rhs),"rounding_term_checks");
   }
  }
  const shapes=[[[0,1]],[[0,1],[0,1]],[[0,1],[1,2],[0,2]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1],[0,2],[0,3],[0,4],[0,5]],[[0,1,2,3],[0,2,4],[1,3,4],[2,4],[0,1]],[[0,1],[0,1],[1,2],[2,3],[3,0],[1,3],[0,2]]];
  for(const fs of shapes){
   const g=1+Math.max(...fs.flat()),m=fs.length,D=Array.from({length:g},(_,v)=>fs.filter(f=>f.includes(v)).length),d=Math.max(...D);
   let L=0;while(2**L<d)L++;
   const p=rat(1,2**L),q=mul(beta,rat(1,d));
   const b=fs.map((f,i)=>mul(mul(q,p),rat((i%3)+1,3*2**f.length)));
   const c=fs.map(f=>f.length+L),u=b.map((x,i)=>mul(x,pow(R,c[i])));
   for(let v=0;v<g;v++){
    let z=one;
    for(let i=0;i<m;i++)if(fs[i].includes(v))z=mul(z,add(one,mul(u[i],pow(A,fs[i].length-1))));
    ck(le(z,add(one,h)),"oriented_witness_checks");
   }
   for(let rep=0;rep<3;rep++){
    stats.instances++;
    const prob=Array.from({length:g},(_,v)=>rat((v+rep)%5+1,6));
    const points=[zero,R,neg(R),mul(R,F(0n,1n)),mul(R,F(3n,4n,5n))];
    for(const t of points){
     const terms=b.map((x,i)=>mul(i%2?x:neg(x),pow(t,c[i])));
     const P=Array.from({length:1<<m},(_,mask)=>{
      let z=one,vs=new Set();
      for(let i=0;i<m;i++)if(mask&(1<<i)){z=mul(z,terms[i]);fs[i].forEach(v=>vs.add(v))}
      for(const v of vs)z=mul(z,prob[v]);
      return z;
     });
     for(let i=0;i<m;i++)for(let mask=0;mask<(1<<m);mask++)if(mask&(1<<i))P[mask]=add(P[mask],P[mask^(1<<i)]);
     for(let mask=0;mask<(1<<m);mask++)for(let v=0;v<g;v++){
      let sub=mask;for(let i=0;i<m;i++)if(fs[i].includes(v))sub&=~(1<<i);
      if(sub===mask)continue;
      const base=norm(P[sub]);
      ck(base[0]>0n&&le(norm(add(P[mask],neg(P[sub]))),mul(pow(h,2),base)),"group_ratio_checks");
     }
    }
   }
  }
 }
 return stats;
}
console.log(verify());
```

## Next

Optimize the oriented incidence witness with actual exclusion of already deleted groups, especially a dominant factor adjacent to many weak ones; compare with R827 direct factor deletion certificates on separating rational families. A better uniform threshold may use actual p_f distribution instead of p_f R^{L_f}<=R, but global optimality is open. Also continue quantitative parity-conditioned envelopes and native realization separately. General Port FPTAS remains open.
