# R806 — Multi-charge cut certificate and finite nonbacktracking bounds

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable research, no shared claim or Result. Direct continuation of R805 at c2ea5b4c135fe69fd28a987a18fc7f828b31b5fc:research_notes/portable_direct/R805_BOUNDARY_CHARGE_AND_BRIDGE_TRANSPORT.md. Frozen foundation commit a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 directly read by blob (generated startup file returned 404). ACTIVE worldview, global entry blobs at e59a4f061d208f4f84dcbc86c37b903eb788e3de and current continuation/method/portable rules read. Own metadata r3-20261126-0720-own-metadata verified prior RESEARCHER session, no RUN, execution_authorized=false. Owner request r3-20261126-0720-owner-read last observed RUNNING before derivation; no shared task ownership inferred.

## 1. Model and multi-terminal pairing bound

Use the R805 exact nonnegative charge expansion on a finite simple loopless road kernel G=(V,E), n=|V|. Incidence occupancy r, active-edge set A(r), nonnegative W(r), eta_e in (0,1]. For J subset E, Q_T(J)=sum_r W(r) sum_{F subset A(r) intersect J, boundary(F)=T} prod_{e in F} eta_e. Q_T=Q_T(E), Q=Q_empty>0, q_T=Q_T/Q. Here q_T is the auxiliary sign character with independent fair empty signs. Hence 0<=q_T<=1. All odd charges vanish. For a path gamma write w(gamma)=prod eta_e; p(s,t) is the sum over all simple s-t paths. For nonempty even T and any s in T,

 q_T <= sum_{t in T minus {s}} p(s,t) q_{T minus {s,t}}. (1)

Proof: in each F with boundary T the component of s has another odd vertex t. Select deterministically a simple path gamma in F to such a t. Removing it leaves boundary T minus {s,t}. The map (r,F) to (r,t,gamma,F minus gamma) is injective and weights factor. Dropping disjointness and gamma occupancy gates only increases the nonnegative sum. Divide by Q. Induction gives q_T <= min(1, sum over perfect matchings M of T prod_{st in M} p(s,t)). This is a pairing upper bound using path weights, not a claim of Gaussian factorization or independent transport. On a tree where T admits edge-disjoint paths, the unique T-join gives its exact product times the joint activation probability, not a product of activation marginals.

## 2. Marked cycle/path loss with one shared cut

Let C=E minus J be the anti-channel deletion set. Define c_C=sum over undirected simple cycles gamma meeting C w(gamma), and p_C(s,t)=sum over simple s-t paths meeting C w(gamma). Then the unnormalized deletion loss obeys

 0 <= Q_T-Q_T(J) <= c_C Q_T + sum_{unordered {s,t} subset T} p_C(s,t) Q_{T minus {s,t}}. (2)

Proof: every edge set F with boundary T decomposes into edge-disjoint simple cycles and simple paths pairing the odd vertices (each odd vertex used once as an endpoint). To see existence, attach one new vertex to all odd vertices, take Euler circuits in the even graph, split at visits to the new vertex, then erase closed segments from the resulting trails, splitting these into simple cycles. Remaining components already even also decompose into cycles. If F meets C, a component of this decomposition meets C. Pick one deterministically. Removing that cycle preserves T; removing that path deletes its two endpoint charges. The map recording (r,removed component,remainder) is injective, weights factor, and relaxing disjointness and activation gates gives (2). For T empty only cycles contribute; if C consists of neutral bridges, both marked sums vanish (for relevant T after replacing path bound by paths with endpoints in T; individual paths between terminals on the same side cannot traverse that bridge). For a charged bridge R805 gives exact loss 100% for that charge even if small in absolute units. Bound (2) is absolute relative to Q, not a uniform relative guarantee for tiny nonzero Q_T.

Define b_T=min(1,c_C q_T + sum p_C q_{T minus pair}), b_0=min(1,c_C). One may replace the q's by (1), min(1,pairing bound), or simply 1. For q'_T=Q_T(J)/Q_empty(J), write a=(Q_T-Q_T(J))/Q and d=(Q-Q_empty(J))/Q. Then q_T-q'_T=a-d q'_T, and 0<=a<=b_T, 0<=d<=b_0, 0<=q'_T<=1 imply |q_T-q'_T|<=max(b_T,b_0). No denominator amplification is needed. This also gives a common cut budget for any prescribed finite charge family. A signed linear combination with coefficients alpha_T has normalized error at most sum |alpha_T| max(b_T,b_0). For a marginal of k specified auxiliary signs, Fourier inversion and Cauchy-Schwarz give total variation <= min(1, (1/2) sqrt(sum over nonempty T of max(b_T,b_0)^2)); use exact zero differences for odd charges. Proof: Parseval on the uniform sign cube gives sum_x (p(x)-p'(x))^2=2^-k sum_T (q_T-q'_T)^2, then bound the l1 norm. Empty character is exactly 1. This is a certificate for the declared auxiliary sign observer, not native signed BRC or full endpoint/occupancy reconstruction.

## 3. Finite polynomial heterogeneous certificate, no spectral threshold required

Let directed arcs be both orientations of each original edge. B_ab=eta_b if head(a)=tail(b) and b is not the reversal of a, else 0. Let D_J be the diagonal 0/1 projector onto retained arcs, B_J=D_J B D_J; u_s(a)=eta_a 1_{tail(a)=s}, v_t(a)=1_{head(a)=t}. Write u_{s,J}=u_s D_J and v_{t,J}=D_J v_t. Then

 P_C(s,t)= sum_{l=1}^{n-1} [u_s B^{l-1} v_t - u_{s,J} B_J^{l-1} v_{t,J}] >= p_C(s,t).
 C_C= sum_{l=3}^{n} [tr(B^l)-tr(B_J^l)]/(2l) >= c_C. (3)

For C empty, P_C=C_C=0. For unrestricted p use u_s B^k v_t, not P_empty. Proof: simple paths are nonbacktracking, length <=n-1; difference counts all weighted walks with at least one marked arc exactly once as a walk. For cycles, each undirected simple l-cycle occurs exactly 2l times as a directed arc-rooted closed nonbacktracking walk in trace(B^l). All other marked walks have nonnegative weights. The difference counts only marked walks; 2l division gives each simple cycle unit multiplicity. This finite cutoff needs neither a homogeneous degree bound nor rho(B)<1. It may overestimate on dense graphs; one may take minimum with any independent certificate. For n=1 the sums are empty. Loops and parallel roads require appropriately defined orientations and l=1,2 terms; the stated implementation and theorem (3) use simple loopless kernels. (2) extends with the usual loop/digon cycle convention, not tested here.

Arithmetic cost: B has 2m states and O(sum_v deg(v)^2) nonzeros h. For one terminal s, sparse vector propagation to depth n-1 costs O(n(h+m)) operations and returns all t; trace propagation from each directed basis vector costs O(n m(h+m)), independently for full and retained matrices. No enumeration of simple paths/cycles is needed for (3). If rational eta have total bit length L0, take common denominator product D; each length-l weight has denominator D^l and integer numerator of bit length O(n(L0+log(2m))); trace denominators 2l can use a common product with O(n log n) extra bits. Exact rational certificates thus have polynomial bit length and can be computed in polynomial time in the explicit kernel and input weights. Full 2^k marginal output is still exponential in k. Pairing sums need not be expanded: use q<=1 or memoized subsets for small charge families. If a weighted nonbacktracking resolvent exists, it supplies another optional infinite-walk bound; no resolvent is necessary for the finite certificate.

## 4. Exact finite verification

The following JavaScript BigInt program was actually executed in this turn. It builds rational road matrices from M(b/16) with b=14,15,16 and road lengths 1..3; uses exact incidence-occupancy/charge DP (common scaled denominator), independently enumerates simple paths/cycles and finite nonbacktracking walks, verifies (1), (2), (3) and normalized bound by cross multiplication. Graph inputs: all labeled simple graphs on 2..4 vertices with all nonempty cuts, all 64 labeled K2,3 subgraphs with singleton/all/selected cut masks, and 8 specified K3,3 subgraphs with the same cuts. No native BRC run, performance comparison, or independent review is claimed.

Actual output: {"graphs":146,"cuts":1023,"chargeChecks":23116,"normalizedChecks":23116,"pathChecks":7663,"cycleChecks":1023,"pairRecursionChecks":1682,"mismatches":0}

```javascript
function verify(){
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0n)));
 const road=(u,v,l,seed)=>{let p=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]];for(let i=0;i<l;i++){let b=BigInt(14+(seed+i)%3);p=mul(p,[[2n*b,16n,16n],[16n,16n,0n],[16n,0n,16n]])}return {u,v,p,s:16n**BigInt(l),d:p[1][1]+p[1][2]};};
 const stats={graphs:0,cuts:0,chargeChecks:0,normalizedChecks:0,pathChecks:0,cycleChecks:0,pairRecursionChecks:0,mismatches:0};const check=(x)=>{if(!x)throw Error("exact mismatch "+JSON.stringify(stats))};
 function test(n,E,seed,allCuts){
  const N=1<<n,m=E.length, D=E.reduce((p,e)=>p*e.d,1n),H=D**BigInt(n);
  let L=2n;for(let i=2;i<=n;i++)L*=BigInt(i);const den=H*L;
  function q(cut){let a=Array(N*N).fill(0n);a[0]=1n;E.forEach(({u,v,p,s,d},k)=>{let b=Array(N*N).fill(0n),U=1<<u,V=1<<v,opts=[[0,0,2n*p[0][0]],[V,0,2n*p[0][1]],[U,0,2n*p[1][0]],[U|V,0,d]];if(!(cut>>k&1))opts.push([U|V,U^V,s]);for(let i=0;i<a.length;i++)if(a[i])for(let [act,t,w] of opts)if(w)b[((i>>n)|act)*N+((i&(N-1))^t)]+=a[i]*w;a=b;});let z=Array(N).fill(0n);for(let act=0;act<N;act++){let w=1n;for(let v=0;v<n;v++)w*=act>>v&1?32n:2n*BigInt(14+(seed+v)%3);for(let t=0;t<N;t++)z[t]+=w*a[act*N+t];}return z;}
  function walks(cut){let A=[];E.forEach(({u,v,s,d},k)=>{if(!(cut>>k&1)){let i=A.length,w=D*s/d;A.push({u,v,w,rev:i+1},{u:v,v:u,w,rev:i})}});let adj=A.map(a=>A.map((b,i)=>b.u===a.v&&i!==a.rev?i:-1).filter(i=>i>=0));
   let P=Array.from({length:n},()=>Array(n).fill(0n)),Ps=P.map(r=>r.slice()),C=0n,Cs=0n;
   for(let s=0;s<n;s++){
    function dfs(v,mask,l,w){for(let a of A)if(a.u===v){if(a.v===s&&l>=2)Cs+=w*a.w*D**BigInt(n-l-1)*(L/BigInt(2*(l+1)));else if(!(mask>>a.v&1)){let z=w*a.w;Ps[s][a.v]+=z*D**BigInt(n-l-1)*L;dfs(a.v,mask|1<<a.v,l+1,z);}}}
    dfs(s,1<<s,0,1n);
    let z=A.map(a=>a.u===s?a.w:0n);for(let l=1;l<n;l++){A.forEach((a,i)=>{P[s][a.v]+=z[i]*D**BigInt(n-l)*L});let t=A.map(()=>0n);adj.forEach((js,i)=>{for(let j of js)t[j]+=z[i]*A[j].w});z=t;}
   }
   for(let s=0;s<A.length;s++){let z=A.map((_,i)=>i===s?1n:0n);for(let l=1;l<=n;l++){let t=A.map(()=>0n);adj.forEach((js,i)=>{for(let j of js)t[j]+=z[i]*A[j].w});z=t;if(l>=3)C+=z[s]*D**BigInt(n-l)*(L/BigInt(2*l));}}
   return {P,Ps,C,Cs};
  }
  const Q=q(0),W=walks(0);let cuts=allCuts?Array.from({length:(1<<m)-1},(_,i)=>i+1):[...new Set([...E.map((_,i)=>1<<i),(1<<m)-1,(1<<m)-1&0x155].filter(Boolean))]; 
  for(let t=1;t<N;t++){let vs=Array.from({length:n},(_,i)=>i).filter(i=>t>>i&1);if(vs.length%2)continue;let s=vs[0],sum=0n;for(let v of vs.slice(1))sum+=W.Ps[s][v]*Q[t^(1<<s)^(1<<v)];check(Q[t]*den<=sum);stats.pairRecursionChecks++;}
  for(let cut of cuts){const R=q(cut),U=walks(cut),cs=W.Cs-U.Cs,c=W.C-U.C;check(cs>=0n&&cs<=c);stats.cycleChecks++;let p=W.P.map((r,s)=>r.map((x,v)=>x-U.P[s][v])),ps=W.Ps.map((r,s)=>r.map((x,v)=>x-U.Ps[s][v]));for(let s=0;s<n;s++)for(let v=s+1;v<n;v++){check(ps[s][v]>=0n&&ps[s][v]<=p[s][v]);stats.pathChecks++;}
   for(let t=0;t<N;t++){let b=cs*Q[t],b2=c*Q[t];for(let s=0;s<n;s++)if(t>>s&1)for(let v=s+1;v<n;v++)if(t>>v&1){let rest=Q[t^(1<<s)^(1<<v)];b+=ps[s][v]*rest;b2+=p[s][v]*rest;}
    let loss=Q[t]-R[t];check(loss>=0n&&loss*den<=b&&b<=b2);stats.chargeChecks++;
    let diff=Q[t]*R[0]-R[t]*Q[0];if(diff<0n)diff=-diff;let mx=b2>c*Q[0]?b2:c*Q[0];check(diff*den<=mx*R[0]);stats.normalizedChecks++;
   }stats.cuts++;
  }stats.graphs++;
 }
 for(let n=2;n<=4;n++){let e=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)e.push([u,v]);for(let f=0;f<1<<e.length;f++)test(n,e.filter((_,i)=>f>>i&1).map(([u,v],i)=>road(u,v,1+(f+i)%3,f+i)),f,true);}
 let e=[];for(let u=0;u<2;u++)for(let v=2;v<5;v++)e.push([u,v]);for(let f=0;f<64;f++)test(5,e.filter((_,i)=>f>>i&1).map(([u,v],i)=>road(u,v,1+(f+i)%3,f+i)),f,false);
 let e6=[];for(let u=0;u<3;u++)for(let v=3;v<6;v++)e6.push([u,v]);for(let f of [0,7,85,170,273,341,426,511])test(6,e6.filter((_,i)=>f>>i&1).map(([u,v],i)=>road(u,v,1+(f+i)%3,f+i)),f,false);
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 5. Next

Use weighted walk cut scores and exact bridge/charge parity to design a multi-observer cut allocation algorithm, improve overcount using block decomposition or signed cancellation only with a separate proof, and compare certified cuts against exact small-kernel optimization. General tilted-cluster FPRAS remains open. Preserve exact P matrices, original prefix/branch relation, native signed BRC provenance, time order and common depth. No shared Task mutation.
