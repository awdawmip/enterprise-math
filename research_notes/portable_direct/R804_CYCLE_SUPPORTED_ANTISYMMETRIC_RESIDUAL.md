# R804 — Cycle-supported antisymmetric residuals and certified bridge elimination

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R803, fixed source 6ef4949f9a48d3349766b474b5cef8105a6aafd4:research_notes/portable_direct/R803_TWO_CHANNEL_ROAD_CERTIFICATE.md and R802 at 0529f92c7063ba89115f344647451ac968f5a736:research_notes/portable_direct/R802_DEGREE_TWO_TRANSFER_AND_CERTIFIED_ROAD_CUT.md. Frozen scientific inputs a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json blob 3923890d77a02d84b772f789e6912dd14f220d14 directly read. ACTIVE worldview read; global entries verified at 0dac63cffda986816aeee70d8fd82378e270f9e7; applicable portable, continuation, research-method, BRC, residual, code and math policies consulted. Own metadata recovery r3-20261126-0515-own-metadata confirms prior line EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, registered RESEARCHER, managed custody not revoked, no RUN, metadata-only, execution_authorized=false. Owner inventory r3-20261126-0515-owner-read last observed RUNNING job, no final inventory inferred. No shared claim or task-state mutation. This is a positive unsigned auxiliary observer, not a native signed BRC or time-dynamics result.

## 1. Exact parity-resolved observer

Reuse the R802 closed road kernel multigraph K, with loops counted twice in vertex degree, and each road e carrying the R803 transfer matrix P_e. Include ell=0 via P_e=I and the ell=1 transfer as well. In the symmetric coordinates, write N product = [[A,2B],[C,D]], with A>0,D>=1 and determinant E. Define
S_e = [[A,B,B],[C,D/2,D/2],[C,D/2,D/2]],
J=jj^T/2, j=(0,1,-1)^T,
so P_e=S_e+J exactly. The symbol E for a road determinant is distinct from the kernel edge set F. All S entries are nonnegative, and D>=1 follows from the nonnegative N product and its bottom-right path staying at coordinate 2. The scalar observer Q is the contraction with the R802 vertex factors: zero on mixed signs, 1 on nonzero single-sign incidences, 2a_v on all-zero incidences. Preserve the original ordered road matrices and branch source.

For each incidence let occupancy r be 0 or 1 according as its label is 0 or nonzero. At a vertex all occupied incidences must have the same sign sigma_v in {+1,-1}. Introduce a sign even for an empty vertex, changing its local weight to a_v before summing its two signs; an occupied vertex has weight 1. In the S channel the edge factor depends only on its two occupancy bits, with entries [[A,B],[C,D/2]]. If both occupied the full edge factor is D/2 times (1+sigma_u sigma_v / D); otherwise it is just S. A loop uses two incidences at the same vertex and sigma_v^2=1.

Let W(r)=2^{|V|} prod_v [a_v if empty else 1] prod_e S_e(r_u,r_v), Q0=sum_r W(r)>0. Let A(r) be edges occupied at both ends, eta_e=1/D_e. For any subset K0 of edges retaining the antisymmetric channel, with all others replaced by S, we have the exact formula
 Q(K0)=sum_r W(r) sum_{F' subset A(r) intersect K0, every vertex even in F'} prod_{e in F'} eta_e.
Proof: expand the product of (1+eta_e sigma_u sigma_v) on retained, doubly occupied edges. Sum independent signs: an odd power sums to zero, an even power sums to 2. Empty vertices are already accounted for by a_v. The resulting coefficients are all nonnegative. This is an algebraic character cancellation within the auxiliary counting representation, not a cancellation of physical positive BRC mass. In particular the ratio Q(K0)/Q0 is the expectation of the even-subgraph polynomial over the positive occupancy measure W/Q0. One may insert any nonnegative function of all occupancy bits in W without changing the proof.

The scalar Q as a function of independent channel strengths x_e in [0,1] is multiaffine with nonnegative coefficients supported exactly on Eulerian edge sets, replacing eta_e by x_e eta_e. Every Eulerian edge set has strictly positive coefficient for the free scalar: all incidences occupied gives positive W and every eta>0. This is a direct refinement of the local absolute-error R803 certificate: the anti-channel can affect this scalar only collectively around cycles.

## 2. Exact bridge criterion

For cut set C, define Q_S=Q(F\C), full Q=Q(F). Then Q_S<=Q, and equality for the free scalar holds iff every cut edge is a graph bridge (not a loop). Indeed no bridge belongs to an even subgraph; any nonbridge belongs to a simple cycle and its strictly positive coefficient is removed. For the larger class of nonnegative occupancy observations, the bridge direction still holds, while strictness can fail on observations excluding all relevant active cycles.

Thus the antisymmetric channel can be deleted exactly on every bridge, independent of road length. If additionally any internal a_i=1, R803 gives E=0 and S=R, where R=P[:,0]P[0,:]/A. Such a bridge may be rank-one separated with **zero scalar error**, including short roads. More generally for ell>=2, replace S by R with the exact local determinant payment d_e=|E|/(2BC) (B,C>0). The original local anti-channel payment, of order lambda^{-ell}, disappears on bridges entirely. On a bridge of length 1 with E=0 the same exact rank-one claim holds since B,C>0. No assertion is made for R at ell=0, where B=C=0.

Scope counterexample: pin endpoint labels +,+ versus +,- on a single bridge. P_{++}-S_{++}=1/2 and P_{+-}-S_{+-}=-1/2. Thus the stronger signed endpoint observer fails the deletion; even an observer invariant under simultaneous global sign reversal can distinguish them. Preserve full P and its ordered source for such future operations. The certified deletion is for scalar/occupancy-only contraction at the present declared composition horizon.

## 3. Cycle-dependent multiplicative error certificate

Let mathcal C_C denote all simple cycles of the multigraph touching C (a loop is a length-1 cycle, two parallel roads form a length-2 cycle). Put w(gamma)=prod_{e in gamma} eta_e. Then
  Q_S <= Q <= Q_S * K_C,
  K_C = prod_{gamma in mathcal C_C}(1+w(gamma)).
Proof at fixed occupancy: each even subgraph decomposes into edge-disjoint simple cycles (remove cycles successively, using a deterministic order of edge IDs). Keep cycles not touching C as a union F0, which is an even subgraph using retained edges. Record each cycle touching C individually as a set T. The map F' -> (F0,T) is injective because union recovers F'. Its weight factors into the weight of F0 times the product of w(gamma) over T. Summing over all F0 and all subsets T of the touching simple cycles relaxes edge disjointness and only increases the nonnegative sum. It gives the claimed bound pointwise in occupancy, hence after summation. The certificate also holds for any nonnegative occupancy observation. In particular (Q-Q_S)/Q<=1-1/K_C. Also K_C<=exp(sum_{gamma touching C} w(gamma)).

A one-edge incremental form follows by the same injection with a single cycle through e: Q(K0)/Q(K0\e)<=1+sum_{gamma subset K0, gamma contains e} w(gamma). One may compute an ordered product of such bounds, recomputing the active graph after each deletion; deleting bridges costs zero. These are observer-level, not entrywise endpoint guarantees. They can be tighter than R803 local estimates by a product of the attenuation along an entire cycle. For a single simple cycle of a kernel (with attached trees allowed) the exact correction relative to Q0 is 1+w(gamma)*Pr_W(gamma subset A(r)). For a theta kernel there are three length-2 cycles and the exact correction has three corresponding terms, no higher even set.

Combine cycle and symmetric determinant budgets for rank-one separation on C, for ell>=2 (or any road with B,C>0 and d_e<1):
 define Q_R as full contraction with P replaced by R on C.
 (prod_C (1-d_e)) Q_R <= Q <= K_C (prod_C (1+d_e)) Q_R.
This follows from the exact S-R determinant identity and nonnegative contraction with the uncut P. For even ell the S-R term is nonnegative, for odd ell nonpositive, so the factor on the opposite side can be replaced by 1. This mixed budget preserves R803's fast determinant scale on bridges and uses cycle products rather than independent edge errors elsewhere.

## 4. Computable polynomial certificates and exact small-cycle coordinate

The all-cycle product may be exponential to compute; it is not claimed to be an efficient general algorithm. For a loopless simple kernel with maximum degree Delta>=2, girth g, uniform eta_e<=rho, and (Delta-1)rho<1, each edge lies on at most (Delta-1)^{l-1} cycles of length l (count oriented simple return paths in the graph with that edge removed). Therefore
 sum_{gamma touching C} w(gamma)
 <= |C| rho [(Delta-1)rho]^{g-1}/[1-(Delta-1)rho].
The union bound can count a cycle more than once, which is safe. For forests use zero directly. This gives a polynomial certificate using bridge detection, maximum degree, girth (e.g. BFS from each vertex), and rational powers/ratios. For heterogeneous weights one can bound each simple return path by all nonbacktracking walks in K\e; if the maximum weighted successor row sum is <1, the tail is geometric. This is a sufficient criterion, not a universal FPTAS.

For exact contraction with cycle rank r=|F|-|V|+number of components, enumerate 2^r even subgraphs via the GF(2) fundamental cycle basis of a spanning forest (including loop and parallel edges). Each even set specifies forced occupancies and a positive two-state endpoint contraction. The local binary occupancy tensor is 2a_v if all zero, 2 otherwise. This is an exact separation of the cycle-coordinate cost from the symmetric contraction cost, not a guarantee of a polynomial solver for general symmetric contractions. On a forest the remaining binary contraction is ordinary tree messages, O(|F|+|V|) arithmetic operations: at each vertex products of child sums give the weight for any occupied incidence; when the parent incidence is zero, adjust the all-zero child term by 2(a_v-1). Alternatively sum the two disjoint empty and nonempty cases. For a small cycle rank, the symmetric contraction can itself be evaluated by conditioning on the two endpoint occupancy bits of r non-tree edges followed by tree messages; a direct bound is O(poly(N) 8^r) arithmetic operations, with bit complexity from rational denominators and explicit road input counted separately. R802 already handles bounded structural width; the new value is the exact support of antisymmetric contributions and improved error payment. Exact bridge detection is linear graph work and does not depend on length or accuracy.

## 5. Actual finite checks

Executed BigInt exact arithmetic with vertex activities b/16, b in {14,15,16}. Matrices P scaled by 16^ell; doubled matrices used so S is integral. Compared direct original 3-label endpoint contraction to positive occupancy/even-set expansion; all cut masks tested with exact integer cross-products and the strict bridge characterization. Tested 602 labeled bipartite graphs from parts (1,1),(1,2),(2,1),(2,2),(2,3),(3,3), including empty graphs and isolated vertices, and 25 road kernels with loops, parallel roads, triangle, square-tail, and mixed road sequences of lengths 0,1,2,4,8,16. Counts: 1,325 direct contraction comparisons, 20,858 cut/cycle inequalities, 1,613 exact bridge deletions, 9 exact rank-one bridge checks, 400 nonempty positive Eulerian coefficient checks; zero mismatches. This is deterministic finite evidence, no performance benchmark, no new native XOR/BRC execution. General results above are analytic.

For the theta kernels, all three anti-channels removed, the exact relative scalar loss (Q-Q0)/Q and K_C-1 are respectively approximately:
ell=2: 0.00484184 and 0.371742;
ell=4: 0.0000672243 and 0.00461682;
ell=8: 1.28362e-8 and 8.79852e-7;
ell=16: 4.67947e-16 and 3.20858e-14.
Display decimals are only indicative; exact verification uses integers. The loop-bridge example's exact bridge deletion was individually checked; the all-edge cut including loops is not exact.

Reproducer (JavaScript, no external dependencies):

```javascript
function verify(){
 const A=(b)=>{if(!b)throw Error("exact check failed")},I=()=>[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]],M=b=>[[2n*BigInt(b),16n,16n],[16n,16n,0n],[16n,0n,16n]],mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0n)));
 const make=(u,v,seq)=>{let p=I();for(const b of seq)p=mul(p,M(b));return {u,v,p,s:16n**BigInt(seq.length),d:p[1][1]+p[1][2]}};
 const sym=e=>[[2n*e.p[0][0],2n*e.p[0][1],2n*e.p[0][2]],[2n*e.p[1][0],e.d,e.d],[2n*e.p[2][0],e.d,e.d]];
 function direct(n,E,b,cut=0,rank1=-1){
  let mask=Array(n).fill(0),den=1n;
  let mats=E.map((e,k)=>{let p=cut>>k&1?sym(e):e.p.map(r=>r.map(x=>2n*x));if(k===rank1){den=p[0][0];p=p.map((r,i)=>r.map((_,j)=>p[i][0]*p[0][j]));}return p;});
  function rec(k){if(k===E.length){let w=1n;for(let v=0;v<n;v++)w*=mask[v]?16n:2n*BigInt(b[v]);return w}let {u,v}=E[k],z=0n;for(let i=0;i<3;i++)for(let j=0;j<3;j++){let w=mats[k][i][j];if(!w)continue;let a=mask[u],c=mask[v];mask[u]|=i;mask[v]|=j;if(mask[u]!==3&&mask[v]!==3)z+=w*rec(k+1);mask[u]=a;mask[v]=c;}return z}
  return [rec(0),den];
 }
 function expansion(n,E,b){
  let m=E.length,coef=Array(2**m).fill(0n);
  function rec(k,active,odd,F,w){if(k===m){if(odd)return;for(let v=0;v<n;v++)w*=active>>v&1?32n:2n*BigInt(b[v]);coef[F]+=w;return}let e=E[k],{u,v,p,d,s}=e,U=1<<u,V=1<<v;let opts=[[0,0,2n*p[0][0]],[0,1,2n*p[0][1]],[1,0,2n*p[1][0]],[1,1,d]];
    for(const [x,y,f] of opts)if(f)rec(k+1,active|(x?U:0)|(y?V:0),odd,F,w*f);
    rec(k+1,active|U|V,odd^U^V,F|(1<<k),w*s);
  }
  rec(0,0,0,0,1n);return coef;
 }
 function cycles(n,E){
  let C=[];for(let f=1;f<2**E.length;f++){let deg=Array(n).fill(0),par=Array.from({length:n},(_,i)=>i),s=1n,d=1n;function root(x){while(par[x]!==x)x=par[x];return x}for(let j=0;j<E.length;j++)if(f>>j&1){let e=E[j];deg[e.u]++;deg[e.v]++;par[root(e.u)]=root(e.v);s*=e.s;d*=e.d}let V=deg.map((x,i)=>x?i:-1).filter(x=>x>=0);if(V.every(v=>deg[v]===2&&root(v)===root(V[0])))C.push({f,s,d});}return C;
 }
 let graphs=0,kernels=0,directChecks=0,cutChecks=0,bridgeChecks=0,positiveTerms=0,rank1Checks=0,examples=[];
 function check(n,E,b,kind,label){
  let m=E.length,all=2**m-1,c=expansion(n,E,b),C=cycles(n,E),z=c.slice();for(let j=0;j<m;j++)for(let f=0;f<=all;f++)if(f>>j&1)z[f]+=z[f^(1<<j)];let Q=z[all];A(direct(n,E,b)[0]===Q);directChecks++;
  for(let f=1;f<=all;f++)if(c[f]){let parity=0;for(let k=0;k<m;k++)if(f>>k&1)parity^=(1<<E[k].u)^(1<<E[k].v);A(parity===0);positiveTerms++;}
  for(let cut=0;cut<=all;cut++){let Z=z[all^cut],lo=1n,hi=1n;for(let q of C)if(q.f&cut){lo*=q.d;hi*=q.d+q.s;}A(Q>=Z&&Q*lo<=Z*hi);A((Q===Z)===!C.some(q=>q.f&cut));cutChecks++;}
  if(kind==="kernel"||m<=4){for(let cut of new Set([all,all&5])){A(direct(n,E,b,cut)[0]===z[all^cut]);directChecks++;}}
  for(let k=0;k<m;k++)if(!C.some(q=>q.f>>k&1)){A(z[all^(1<<k)]===Q);bridgeChecks++;let e=E[k],p=e.p;if(p[0][0]*e.d===2n*p[0][1]*p[1][0]){let [num,den]=direct(n,E,b,1<<k,k);A(num===den*Q);rank1Checks++;}}
  if(label){let lo=1n,hi=1n;for(let q of C){lo*=q.d;hi*=q.d+q.s;}examples.push({label,relativeLossNumerator:(Q-z[0]).toString(),relativeLossDenominator:Q.toString(),cycleFactorExcessNumerator:(hi-lo).toString(),cycleFactorExcessDenominator:lo.toString()});}
 }
 for(let [p,q] of [[1,1],[1,2],[2,1],[2,2],[2,3],[3,3]]){let all=[];for(let i=0;i<p;i++)for(let j=0;j<q;j++)all.push([i,p+j]);for(let f=0;f<2**all.length;f++){let E=all.filter((_,i)=>f>>i&1).map(([u,v])=>make(u,v,[]));check(p+q,E,Array.from({length:p+q},(_,i)=>14+(i+f)%3),"simple");graphs++;}}
 for(const [name,n,edges] of [["triangle",3,[[0,1],[1,2],[2,0]]],["theta",2,[[0,1],[0,1],[0,1]]],["loops-bridge",2,[[0,0],[0,1],[1,1]]],["square-tail",5,[[0,1],[1,2],[2,3],[3,0],[3,4]]]])for(let l of [0,1,2,4,8,16]){let E=edges.map(([u,v],j)=>make(u,v,Array.from({length:l},(_,i)=>14+(i+j)%3)));check(n,E,Array.from({length:n},(_,i)=>14+i%3),"kernel",name==="theta"&&l>=2?name+"-"+l:null);kernels++}
 let E=[make(0,0,[14,15]),make(0,1,[14,16,15]),make(1,1,[15,14])];check(2,E,[14,15],"kernel","exact-bridge");kernels++;
 return {graphs,kernels,directChecks,cutChecks,bridgeChecks,rank1Checks,positiveTerms,examples,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```


## 6. Next
Exploit the cycle support in the global resource allocation problem: choose bridge, cycle cut, rank-two and full channels with actual weighted cycle budgets, and seek efficient heterogeneous cycle certificates. Investigate direct positive binary-occupancy contraction and a general sampler for the tilted cluster model. General FPRAS remains open; no native signed BRC attribution or formal task closure. Preserve all full original road and prefix records for stronger observers.
