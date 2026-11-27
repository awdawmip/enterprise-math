# R851 — Scope-streaming live-anchor residual frontier, one exact capacity, single radius payment

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent informed portable continuation of R850, not shared Task execution. Existing own session MCP-ec17f2f30fb8409f8e664eb29ae6c08c recovered as metadata-only with no runs, execution_authorized=false; activity RA-708BCC309CE076D8BB599B91, researcher EM-DIRECT-82A007. Owner read observation {"status":"RUNNING","error":null,"phase":"NATIVE_RUNNER","request_id":"r3-20261128-r851-running-read","source":"6df86a3cfc7f0b73bd8a083f2c3f52c8122cdf34"}. No claim or Result mutation.
Source: R850 at f3df968a835da9b746c579af18418adb34229a04:research_notes/portable_direct/R850_FIXED_ANCHOR_GAP_RESIDUAL_FRONTIER.md; frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5 and joint observer read at pin, generated startup missing). Global entries verified by matching blobs at fcb414936bdd8b1dd889c172180b0f81c9f9c89d, ACTIVE worldview and P000 V4 read, current normative/portable routes consumed. This is a positive auxiliary certificate model; keep original joint/signed observations, paths, branch identities, common depth and source data, not a native BRC quotient or experiment.

## Theorem
Use R850's independent Kraft scopes and explicit finite edge lists of actual witnesses (integer k>=0, p(R)>=1). Each edge has a fixed capacity/identity and a product of factors 1+b R^(L+2), b>=0, integer L>=0; alternatively assume its residual p(R1)-1 <= alpha[p(R2)-1] for alpha=(R1/R2)^2. Each scope has fixed nonnegative integer base and capacity. Anchor base B_h(R)>=1 is nondecreasing in R and ceiling U_h<=2-eta, eta>0 fixed per instance. The target cost C=sum phi(Q_h), phi(q)=(q-1)/(2-q), Q_h=B_h prod p_e. No retained shared-bundle propagation or cross-scope grade coupling.

Supply an edge order in which each Kraft scope's edges are consecutive. Let E be the edge count, w the maximum number of anchors that have both a processed and an unprocessed incident edge immediately after a cut. The total anchor count and degrees may be unbounded; finding an order of minimum w is not included. For 0<eps<=1, rational R2>R1>1 with (R2/R1)^2>=1+eps, there is a deterministic algorithm that, for every feasible reference at R2, returns a true feasible witness at R1 of cost <= C_ref(R2), with exact Kraft capacities and original analytic ceilings. It can return failure when no retained witness is feasible; if R2 had a feasible reference that failure is impossible. It does not decide exact same-radius feasibility.

Let J bound the number of bins per live residual or closed incremental cost and D the maximum explicit edge list size. At most J^(w+1) states per edge cut, O(E D J^(w+1)) candidate transitions, up to polynomial bit/lookup/reconstruction factors. Unlike R850's n D^g J^(g-1) enumeration, no local D^degree term is needed, including scopes incident to many one-shot anchors. For fixed w the full search is polynomial in input bit length and 1/eps; finding a suitable order is separate. E=0 or empty scopes handled directly by checking bases. Empty edge list forces infeasibility.

## Algorithm
Use R850 exact dyadic bins, K=ceil(2 max(1,E)/eps), rho=1+1/K; zero separate. Same-bin positive ratios <=rho. Store a real prefix witness, exact products for currently live anchors (starting at 1), exact current scope capacity consumption k, and exact closed incremental cost c=sum of [phi(B_h(R1) P_h)-phi(B_h(R1))] over completed nonisolated anchors. Baseline sum phi(B_h(R1)) is constant. Reject base violations at R1. Process one edge at a time, extend by each actual edge option, add capacity and multiply its anchor product. Reject capacity overflow. At the anchor's last edge, check its exact analytic ceiling BEFORE compression, add its incremental cost and drop the resource coordinate from the search state (retain the witness). At scope end reset capacity to zero after the exact check. Bin live residuals P_h-1 and c. Within each cell keep a prefix with minimum exact current capacity k (ties arbitrary). Reconstruct the minimum exact final cost among retained witnesses and verify original constraints. Isolated anchors contribute only baseline. All pruning is confined to this observer and edge-order horizon.

## Proof: one radius payment, including cost
Let alpha=(R1/R2)^2, so alpha rho^E<=1 (rho^E<=exp(eps/2)<=1+eps). For any reference feasible at R2, after j steps maintain a retained prefix whose live residuals are <=alpha rho^j times the corresponding reference prefix residual at R2, whose current scope used capacity is <= reference's, and whose closed incremental cost is <=alpha rho^j times the sum of corresponding completed reference increments at R2. Base case is zero. Extend the retained prefix by the SAME next identity as the reference, so capacity dominance is preserved. At R1 each new factor residual is <=alpha times its R2 counterpart. For beta=alpha rho^j<=1 and x,u>=0, T_(1+beta u)(beta x)=beta x+beta u+beta^2 xu<=beta(x+u+xu). Thus extending maintains the residual bound prior to trim. An anchor closing now is feasible because its product and base are <= reference's. Define f_B(v)=phi(B(1+v))-phi(B)=B v/[(2-B)(2-B-Bv)]. On the feasible domain, f_B is increasing in B and convex in v, vanishes at zero, so f_B(beta v)<=beta f_B(v) for beta<=1. Therefore the newly closed increment, as well as the previously closed sum, is at most beta times the corresponding R2 reference increments. Summing preserves the same beta. Trim within the cell may multiply each live residual and the closed cost by at most rho, while decreasing the current exact capacity; zero stays zero. At a scope boundary, capacity reset is identical for both. Induction gives the claimed bounds. The key is that each anchor contribution spends error first as a residual and subsequently as closed cost, never both in the same trim. At E the closed cost <= reference's increments; baseline at R1 <= baseline at R2, proving C_alg<=C_ref without a second objective error or additional radius payment. The proof also works for base ceilings varying with radius provided the R2 reference ceiling implies the R1 target ceiling; here ceilings are fixed.

## Bit complexity
Each retained value is the exact value of a real prefix. Rational products have bit length polynomial in total explicit list input, and sums of at most the number of anchors of rational cost increments have polynomial bit length as well (sum of denominator bit lengths). Positive residuals are bounded below by the minimum positive edge residual and above by the product of maximal factors minus one. Positive closed increments are at least the same minimum positive edge residual, since B>=1 and f_B(v)>=v, and total closed cost <= g/eta. If all factors are 1, every incremental coordinate is zero. Thus octave ranges are polynomial in input bit length, and J=O(1+K times the maximum octave range). Use exact integer bin computation as in R850. Each edge generates at most D candidates per state, retaining one per cell; copying witnesses adds at most a polynomial factor, or use backpointers. No claim of FPT in w alone. Scope order supplied as input. If using R847 local approximate lists of error delta with capacity nonincrease and the coverage property at R1, replace alpha by alpha(1+delta); the same proof gives sufficient (R2/R1)^2 >= (1+delta)(1+eps). That extension is analytic; experiment below uses uncompressed explicit lists.

## Exact checks
Deterministic JS BigInt rational arithmetic. Cases generated by the complete loops below; brute force at R2 over every binary edge assignment for up to 12 edges; verify reconstructed R1 optimum among retained states by original capacity, ceiling and exact cost recomputation. Non-reference-feasible instances do not assert R1 infeasibility. High-degree example with one scope and distinct one-shot anchors checks a returned witness, not a brute optimum. Fixed R2=2, R1=3/2, eps=1/2. Actual counters: {"cases":180,"reference_feasible":111,"reference_infeasible":69,"full_assignments":19260,"capacity_valid":2715,"transitions":9696,"merges":2124,"max_states":72,"max_width":4,"returned":180,"large_edges":27,"large_returned":1,"failures":0}. These are auxiliary arithmetic checks, not native BRC or independent review.

```js
function experiment(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);let d=gcd(a<0n?-a:a,b);return [a/d,b/d]};
 const Z=F(0),O=F(1),add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a),pow=(a,n)=>F(a[0]**BigInt(n),a[1]**BigInt(n)),phi=q=>div(sub(q,O),sub(F(2),q));
 const stats={cases:0,reference_feasible:0,reference_infeasible:0,full_assignments:0,capacity_valid:0,transitions:0,merges:0,max_states:0,max_width:0,returned:0,large_edges:0,large_returned:0,failures:0};
 const check=(x,m)=>{if(!x)throw Error(m)};
 function bin(v,K){let [a,b]=v;if(a===0n)return "z";let e=a.toString(2).length-b.toString(2).length;if(e>=0?a<(b<<BigInt(e)):(a<<BigInt(-e))<b)e--;if(e>=0)b<<=BigInt(e);else a<<=BigInt(-e);return e+":"+K*(a-b)/b}
 function factors(e,R){return [1,2].map(l=>({k:2**(2-l),p:add(O,mul(e.b,pow(R,l+2)))}))}
 function evaluate(net,R,w){let p=net.base.slice(),k=net.cap.map(()=>0);for(let i=0;i<net.edges.length;i++){let e=net.edges[i],z=factors(e,R)[w[i]];k[e.s]+=z.k;p[e.a]=mul(p[e.a],z.p)}if(k.some((v,s)=>v>net.cap[s]))return null;stats.capacity_valid++;if(p.some((v,h)=>!le(v,net.u[h])))return null;return p.reduce((s,q)=>add(s,phi(q)),Z)}
 function brute(net,R){let best=null;for(let m=0;m<2**net.edges.length;m++){let w=net.edges.map((_,i)=>(m>>i)&1);stats.full_assignments++;let c=evaluate(net,R,w);if(c&&(!best||le(c,best)))best=c}return best}
 function solve(net,R,eps){
  const E=net.edges.length,K=(2n*BigInt(Math.max(1,E))*eps[1]+eps[0]-1n)/eps[0],last=net.base.map(()=>-1),first=net.base.map(()=>E);
  net.edges.forEach((e,i)=>{last[e.a]=i;first[e.a]=Math.min(first[e.a],i)});
  if(net.base.some((b,h)=>!le(b,net.u[h])))return null;
  let states=[{p:net.base.map(()=>O),c:Z,k:0,w:[]}];
  for(let i=0;i<E;i++){
   let e=net.edges[i],active=last.map((l,h)=>first[h]<=i&&i<l?h:-1).filter(h=>h>=0),end=i+1===E||net.edges[i+1].s!==e.s,next=new Map(),options=factors(e,R);
   stats.max_width=Math.max(stats.max_width,active.length);
   for(let s of states)for(let j=0;j<options.length;j++){
    let z=options[j],k=s.k+z.k;stats.transitions++;if(k>net.cap[e.s])continue;
    let p=s.p.slice(),c=s.c;p[e.a]=mul(p[e.a],z.p);
    if(last[e.a]===i){let q=mul(net.base[e.a],p[e.a]);if(!le(q,net.u[e.a]))continue;c=add(c,sub(phi(q),phi(net.base[e.a])));p[e.a]=O}
    if(end)k=0;
    let key=active.map(h=>bin(sub(p[h],O),K)).concat(bin(c,K)).join("|"),old=next.get(key);
    if(old)stats.merges++;
    if(!old||k<old.k)next.set(key,{p,c,k,w:s.w.concat(j)});
   }
   states=[...next.values()];stats.max_states=Math.max(stats.max_states,states.length)
  }
  if(!states.length)return null;
  let best=states.reduce((a,b)=>le(a.c,b.c)?a:b),cost=add(best.c,net.base.reduce((s,b)=>add(s,phi(b)),Z));
  let actual=evaluate(net,R,best.w);check(actual&&eq(actual,cost),"recovery");stats.returned++;return cost
 }
 function make(n,g,seed,kind){
  let edges=[],cap=[],base=Array.from({length:g},(_,h)=>F(16+((seed+h)%3),16)),u=Array.from({length:g},(_,h)=>F(20+(seed+3*h)%8,16));
  for(let s=0;s<n;s++){let anchors=kind===0?[s%g,(s+1)%g]:kind===1?Array.from({length:g},(_,h)=>h).filter(h=>(s+h+seed)%3!==0):[s%g];anchors=[...new Set(anchors)];if(!anchors.length)anchors=[s%g];cap.push(anchors.length+(s+seed)%(anchors.length+1));for(let a of anchors)edges.push({s,a,b:F((seed+7*s+3*a)%11,512)})}
  return {edges,cap,base,u}
 }
 const R2=F(2),R1=F(3,2),eps=F(1,2);
 for(let seed=0;seed<60;seed++)for(let kind=0;kind<3;kind++){
  let net=make(1+seed%4,2+seed%3,seed,kind);if(net.edges.length>12)continue;stats.cases++;let ref=brute(net,R2),got=solve(net,R1,eps);
  if(ref){stats.reference_feasible++;check(got&&le(got,ref),"cross radius bound")}else stats.reference_infeasible++;
 }
 // One high-degree scope, 40 distinct one-shot anchors (width 0), no full enumeration.
 let net=make(1,40,11,1);stats.large_edges=net.edges.length;let got=solve(net,R1,eps);check(got,"large witness");stats.large_returned=1;
 return stats
}
console.log(JSON.stringify(experiment()));
```

## Next
Optimize the edge order to minimize live anchors, and investigate multiple simultaneously live exact capacity coordinates: one-dimensional min-k is insufficient for incomparable capacity vectors. Derive a precise tractable structure or gap bound preserving hard Kraft constraints; examine whether shared bundles can be included as explicitly live propagation resources. General native Port/joint observer remains open.
