# R814 — Connected feedback supports and a weighted zero-free certificate

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared CLAIM, RUN or Result. Researcher EM-DIRECT-82A007, existing own session metadata recovered (r3-20261126-r814-own-metadata, no runs, execution_authorized=false). Running inventory request r3-20261126-r814-running-read was RUNNING at the last observation during derivation; no inference of empty inventory. Predecessor c6a2b95f767b8cf8316c207ec103cb86130e78d1:research_notes/portable_direct/R813_IMPLICIT_INTERFACE_FOREST_AND_FEEDBACK.md. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer 3923890d77a02d84b772f789e6912dd14f220d14 verified at that pin. Global entries at 12df830ee96a5b0829df86e0ae36f0ebf80c6947. Scope: R813 auxiliary positive combinatorial occupancy/parity observer; no native phase attribution. Keep original signed/native BRC, complete road matrices, provenance, time and common depth.

## 1. Dependency graph of feedback factors

Use R813's H, D with H-D a forest, Z0 the partition with D factors removed, and Z_A the forest partition with A's incident bits pinned to 1. A feasible positive base Z0 is assumed; if Z0=0, positivity of the original factors implies Z=0 exactly. Let n=|D|, I_v the all-empty indicator, delta_v=1-a_v in [0,1). Under normalized base measure E0, m(A)=Z_A/Z0=E0 prod_{v in A} I_v. Define G_D on D: join two factors if they touch the same connected component of H-D. The base assignment distribution factors over these components, including arbitrary correlations inside each component. Thus for A with components C_i in G_D[A], m(A)=prod_i m(C_i). This is exact even for a nonzero feasible charge, as its local block charges have already been fixed by R812. No interface table is needed: every m(A) is one R813 forest contraction with pinnings. A feedback factor with no incident component is deterministic (empty product=1).

For any S subset D set P_S(t)=E0 prod_{v in S}(1-t delta_v I_v). It has constant coefficient 1 and P_D(1)=Z/Z0. It is an abstract polymer partition polynomial on G_D: nonempty connected sets C have activity w(C)=(-t)^|C| delta(C)m(C); two are compatible iff disjoint and nonadjacent. This follows by splitting the exact subset expansion by connected components, with no sign reinterpretation as physical cancellation.

## 2. Weighted zero-free theorem (proved)

Suppose R>1 and rational 0<q_v<1 satisfy for every v

 R delta_v <= q_v prod_{u adjacent v}(1-q_u)^2.             (1)

Then for all S subset D, v in S and complex |t|<=R,

 P_S(t) != 0,  |P_S(t)/P_{S-v}(t)-1| <= q_v.             (2)

Proof by induction on |S|. Polymer recurrence at v:
 P_S=P_{S-v}+sum_{C connected, v in C subset S} w(C) P_{S\N[C]}.
All smaller polynomials are nonzero. Delete the vertices of (N[C] intersect S)\{v} successively from S-v and apply the induction lower ratio bound 1-q_u. Consequently
 |P_S/P_{S-v}-1|
 <= sum_C prod_{x in C}(R delta_x) prod_{u in (N[C] intersect S)\{v}} (1-q_u)^(-1)
 <= (1-q_v) sum_C prod_{x in C} b_x,
 where b_x=R delta_x prod_{u in N[x]}(1-q_u)^(-1).
The last inequality counts each closed-neighborhood inverse at least once, including the root before compensating by 1-q_v.

To majorize the connected-set sum, choose a deterministic rooted spanning tree for each C, root v, whose children at each node have distinct neighboring labels. Distinct C give distinct labeled trees (the vertex set recovers C). Allow labels to repeat at different nodes, increasing the nonnegative sum. The total weight of these trees up to height h satisfies T_x^(0)=b_x, T_x^(h+1)=b_x prod_{u adjacent x}(1+T_u^(h)). Set L_x=q_x/(1-q_x). By (1), b_x prod_{u adjacent x}(1+L_u)<=L_x. Induction gives T_x^(h)<=L_x, and monotone convergence gives the same for all finite trees. Hence the connected-set sum at v <= L_v. The ratio bound is <=(1-q_v)L_v=q_v<1, proving nonvanishing and completing the induction.

Uniform sufficient criterion with max degree Delta>=1: q=1/(2Delta+1), R delta_max <= q(1-q)^(2Delta). For Delta=0 choose q=1/2; factors then separate exactly. For actual Port delta_v<=2^(-2d_v-1), d_v is ORIGINAL degree, not G_D degree. E.g. Delta=2, d_v>=2, R=2: 2/32=1/16 <=256/3125. Delta=3, d_v>=3, R=2: 1/64 <= (1/7)(6/7)^6. These are sufficient, not optimal thresholds. The weighted criterion can be checked directly with rational arithmetic; large max dependency degree may still satisfy it when delta varies, but does not by itself give efficient connected-set enumeration.

## 3. Connected-support log reconstruction and FPTAS

Let ell_j(S)=[t^j]log P_S(t) as a formal series at zero; let c_j(C)=sum_{A subset C}(-1)^(|C|-|A|)ell_j(A). If C disconnected, c_j(C)=0: P_A factors over the partition of C into components, log adds, and the alternating sum cancels. Also c_j(C)=0 for |C|>j. Proof of the latter: introduce separate formal variables t_v; P has coefficients only on squarefree monomials; log's degree-j part contains monomials of support size <=j, and restricting to A sets all other variables to zero. The subset alternating sum extracts precisely full-support terms. Thus
 ell_j(D)=sum_{C connected, |C|<=j} c_j(C).
For every C of size <=k, obtain m(A) for A subset C from R813, form P_A coefficients p_i, and compute ell_j by j ell_j = j p_j - sum_{i=1}^{j-1} i ell_i p_{j-i}. All calculations are rational. The algorithm need not enumerate subsets of D globally. Enumerate connected sets by rooted plane-tree shapes of size <=k and neighbor labels (at most n*(4 max(1,Delta))^(k-1) at each size, discard repeated labels, deduplicate vertex sets). Each C uses <=2^k forest moment calls and O(3^k poly(k)) coefficient operations. This is an explicit construction; full production implementation not yet executed.

Since P_D has degree <=n, all its complex roots have modulus >R by section 2. Factoring by roots and taking the analytic log with value 0 at the origin proves
 |log P_D(1)-sum_{j=1}^k ell_j(D)| <= n R^(-k)/((k+1)(R-1)).
P_D(1)>0 by positive original factors. With R>=1+c for a fixed c>0, choose k=O(log((n+1)/epsilon)) so that the bound <=epsilon/4, 0<epsilon<=1. Approximate exp of the exact rational log truncation to relative error epsilon/4, then multiply Z0 (and R813's K0 for Q_T). For example approximate exp of its absolute value by the positive Taylor sum with a rigorous geometric tail after the terms decrease by a factor <=1/2; invert when negative. The argument is O(n+1) because P_D(1)>=prod_v(1-delta_v), and (1) bounds delta_v<=1/R. Thus polynomial bit cost for the exponential and rational coefficients. Relative output lies in [1-epsilon,1+epsilon]. Empty D is exact. A common denominator for all normalized moments is a product of explicit physical input denominators and the same base numerator; products through order k and integer divisions introduce only polynomial bit length. Enumeration cost is polynomial in N and 1/epsilon when Delta is uniformly bounded, R separated from 1, and the forest oracle costs polynomial time for every pinned event (e.g. R813 supplied bounded/logarithmic width or cycle rank). The factor count |D| can be linear, and there is no bound on all interfaces b_B. For uniform FPTAS the chosen D and certificate must be provided or polynomially constructible, with fixed constants. This uses an analytic generating polynomial of positive auxiliary branch weights, not native BRC phase arithmetic.

## 4. Coverage, separation, next question

If J empty, choose D all shared factors: each component of H-D is a single edge group, so G_D is a subgraph of the original road graph. On a cubic circular ladder with even n>=4 columns there are n/2 disjoint plaquette cycles, so every shared-vertex feedback deletion set has at least n/2 vertices. With equality-only edge states S00=2,S11=1 and a_v=1-1/128, R=2 passes (1). This illustrates why logarithmic exact feedback correction and global first-order deletion budgets need not be the applicable mechanism. R810 already covers J empty, so this example is not a novelty claim over R810. More generally, when local groups have arbitrarily many tree-side interfaces but only a bounded number of feedback neighbors per surviving forest component, the same criterion uses the latter dependency graph instead of total interface count. A large forest component touching many feedback factors creates a clique; that is an actual remaining limitation. Seek conditional-moment factorization or a finer separator that exploits sparse correlations inside a large surviving component rather than using the entire clique. General overlapping Port network FPTAS remains open. No independence of individual interface bits is assumed.

## 5. Actual exact verification

Executed the JavaScript BigInt rational verifier below. 48 deterministic abstract cases, six incidence shapes including cycles, overlapping cliques, disconnected components, singleton groups, eight random nonnegative tables per shape. Exact comparisons: 1536 moment factorizations; 5864 disconnected/support-degree cancellations; 328 connected log reconstructions; 7936 real endpoint ratio checks at t=+/-2; 6 ring transfer checks. Total 15670 comparisons, zero mismatch. The real endpoint checks do not verify complex nonvanishing; section 2 supplies the proof. Ring model J empty, equality-only S00=2,S11=1, delta=1/32, scalar observer: normalized P(1) is trace([[62,32],[64,32]]^n)/96^n. At n=128 reduced numerator/denominator bits 713/715; n=512 2850/2860. Small rings n=3,4,5,6,8,16 independently enumerated. These are transfer checks, not runtime benchmarks of the new full FPTAS. The connected coefficient algorithm is proved and tested on small abstract data; general large-scale implementation and performance, independent review and native correspondence remain open.

```javascript
function verify(){
 const abs=x=>x<0n?-x:x;
 function gcd(a,b){a=abs(a);b=abs(b);while(b){let c=a%b;a=b;b=c;}return a;}
 function f(a,b=1n){if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];}
 const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]), neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b)), mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]), div=(a,b)=>f(a[0]*b[1],a[1]*b[0]), eq=(a,b)=>a[0]*b[1]===b[0]*a[1], zero=()=>f(0n), one=()=>f(1n);
 const pop=m=>{let k=0;for(;m;m&=m-1)k++;return k;};
 const sum=a=>a.reduce((s,x)=>s+x,0n);
 const subsets=m=>{let a=[];for(let s=m;;s=(s-1)&m){a.push(s);if(!s)return a;}};
 let stats={cases:0,momentFactorChecks:0,logSupportChecks:0,logReconstructionChecks:0,realRatioChecks:0,transferChecks:0};
 function check(x,label){if(!x)throw Error(label);}
 function logcoeff(p,k){let b=Array.from({length:k+1},zero);for(let j=1;j<=k;j++){let t=mul(f(BigInt(j)),p[j]??zero());for(let i=1;i<j;i++)t=sub(t,mul(mul(f(BigInt(i)),b[i]),p[j-i]??zero()));b[j]=div(t,f(BigInt(j)));}return b;}
 let seed=814;const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
 const patterns=[[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[2,3],[3,4],[4,0]],[[0,1],[2,3],[3,4]],[[0,1,2],[0,2,3],[1,4],[3,4]],[[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]],[[0],[1],[2],[3]]];
 for(const groups of patterns)for(let rep=0;rep<8;rep++){
  const n=1+Math.max(...groups.flat()), full=(1<<n)-1,k=n+2;
  const data=groups.map(v=>({v,w:Array.from({length:1<<v.length},()=>BigInt(rand()%9))}));
  for(const g of data)if(sum(g.w)===0n)g.w[0]=1n;
  const adj=Array(n).fill(0);for(const g of groups)for(const v of g)for(const u of g)if(u!==v)adj[v]|=1<<u;
  const comps=m=>{let a=[];while(m){let c=m&-m;for(;;){let d=c;for(let i=0;i<n;i++)if(c>>i&1)d|=adj[i]&m;if(c===d)break;c=d;}a.push(c);m^=c;}return a;};
  const deg=Math.max(...adj.map(pop)),D=BigInt(32*(deg+1)),q=f(1n,BigInt(2*deg+1||1));
  const qq=deg===0?f(1n,2n):q;
  const M=Array.from({length:full+1},(_,m)=>data.reduce((p,g)=>mul(p,f(sum(g.w.filter((_,i)=>g.v.every((v,j)=>!(m>>v&1)||(i>>j&1)))),sum(g.w))),one()));
  for(let m=0;m<=full;m++){const c=comps(m).reduce((p,x)=>mul(p,M[x]),one());check(eq(c,M[m]),"moment factoring");stats.momentFactorChecks++;}
  const P=Array.from({length:full+1},(_,m)=>{let p=Array.from({length:k+1},zero);for(const a of subsets(m)){let j=pop(a);p[j]=add(p[j],mul(M[a],f(j%2?-1n:1n,D**BigInt(j))));}return p;});
  const L=P.map(p=>logcoeff(p,k));
  const accum=Array.from({length:k+1},zero);
  for(let m=1;m<=full;m++){
   const c=Array.from({length:k+1},zero);
   for(const a of subsets(m))for(let j=1;j<=k;j++)c[j]=add(c[j],(pop(m^a)%2?neg(L[a][j]):L[a][j]));
   for(let j=1;j<=k;j++){if(comps(m).length>1||j<pop(m)){check(eq(c[j],zero()),"support cancellation");stats.logSupportChecks++;}if(comps(m).length===1)accum[j]=add(accum[j],c[j]);}
  }
  for(let j=1;j<=k;j++){check(eq(accum[j],L[full][j]),"connected reconstruction");stats.logReconstructionChecks++;}
  const val=(p,t)=>p.reduceRight((s,x)=>add(x,mul(s,f(t))),zero());
  for(const t of [-2n,2n])for(let m=1;m<=full;m++)for(let v=0;v<n;v++)if(m>>v&1){
   const d=sub(div(val(P[m],t),val(P[m^(1<<v)],t)),one());
   check(abs(d[0])*qq[1]<=qq[0]*d[1],"real ratio");stats.realRatioChecks++;
  }
  stats.cases++;
 }
 function mm(A,B){return A.map((r,i)=>B[0].map((_,j)=>r.reduce((s,x,h)=>s+x*B[h][j],0n)));}
 function pow(A,n){let I=[[1n,0n],[0n,1n]];while(n){if(n%2)I=mm(I,A);A=mm(A,A);n=Math.floor(n/2);}return I;}
 function trace(A){return A[0][0]+A[1][1];}
 const ring=[];
 for(const n of [3,4,5,6,8,16,128,512]){
  const num=trace(pow([[62n,32n],[64n,32n]],n)),den=96n**BigInt(n);
  if(n<=16){let direct=0n;for(let a=0;a<2**n;a++){let w=2n**BigInt(n-pop(a));for(let i=0;i<n;i++)w*=(!(a>>i&1)&&!(a>>((i+1)%n)&1))?31n:32n;direct+=w;}check(num===direct,"ring direct");stats.transferChecks++;}
  const r=f(num,den);ring.push({n,degree:2,feedbackNumberAtLeast:1,normalizedNumeratorBits:r[0].toString(2).length,normalizedDenominatorBits:r[1].toString(2).length,positive:r[0]>0n});
 }
 return {stats,ring};
}
console.log(JSON.stringify(verify(),null,2));
```
