# R847 - Group-separable Kraft capacity/residual witness lists

2026-11-28 (Asia/Shanghai). AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.

Independent informed portable continuation, not a formal Task execution. Existing lane's public metadata: EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 / MCP-ec17f2f30fb8409f8e664eb29ae6c08c, verified from current session/Activity records; current gateway identity read succeeded but no private execution authority established. R846 owner query SUCCEEDED (empty RUNNING projection as of 2026-11-27T15:23:06.162911Z, Source drift); current original request r3-20261128-r847-running-read observation {"status":"SUCCEEDED","error":null,"as_of":"2026-11-27T16:20:13.903215+00:00","running_count":0,"source":"eec7a9a75994f4bbf4c4ca0e95f1ac88b7c17ddb"}. No shared Task/owner/Result mutation.

Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; p000_reality_foundation.json V5 and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json read at pin; generated foundation, residual-position and Heartbeat companions returned 404 at pin. Global P000 V4, ACTIVE worldview, and applicable current normative/portable/research rules read; global main core snapshot 952fd46e07acf723460b7ee875de7dd6075744a2 verified. The result is confined to the auxiliary positive certificate resource layer, not native BRC dynamics. No external priority claim.

Sources: R845 7473e8488b5c789621b6d39a156dd7f61a5161ca:research_notes/portable_direct/R845_MULTIANCHOR_PENDANT_RESIDUAL_FRONTIER.md; R846 2e3617d86dfe2a7581fee2b6944a7295ed49f5ad:research_notes/portable_direct/R846_EXPONENTIAL_TWO_ANCHOR_EXACT_PARETO_FRONTIER.md; R844 a54e958db252ff8533224c99cd3326d9c840d7ed:research_notes/portable_direct/R844_PENDANT_BUNDLE_EXACT_MULTIANCHOR_ELIMINATION.md. R839 local caps and R837 retained payment grid as used in R845.

## 1. One-group capacity-preserving approximation theorem

For a group h of n positive rational weights b_i at rational R>1, allow each grade L_i in 0..C_i, with M>=max_i C_i. Define integer Kraft consumption k(L)=sum_i 2^(M-L_i), product P(L)=prod_i(1+b_i R^(L_i+2)), residual v=P-1. For rational 0<eps<=1, there is a list W_h of actual assignments such that for every allowed grade assignment L (whether or not globally feasible) a witness L' satisfies

    k(L') <= k(L),   v(L') <= (1+eps) v(L).

Importantly the Kraft comparison is exact and one-sided, so every residual approximation respects the original remaining capacity. No sorting or common private cap is required. Empty group: a single empty assignment k=0, P=1.

Construction. Let a=min_i b_i R^2>0, U=prod_i(1+b_i R^(C_i+2))-1, rho=1+eps/(2n). Partition [a,U] by exact half-open intervals [a rho^j,a rho^(j+1)), with separate zero state. Starting from k=0,P=1, process labels in any fixed order. From each state and each allowed length l add the integer 2^(M-l) to k and multiply P by F=1+b_i R^(l+2). In each residual bin retain a witness having the smallest k (break ties by smaller P if desired). Store exact product, k and reconstruction pointer. All retained states are actual assignments.

Proof. For any reference prefix after i labels, inductively a retained witness has k'<=k and v'<=rho^i v. Base i=0 exact. Append the reference next length to that witness: k inequality persists, and the residual update v -> F v + F-1, F>=1, preserves an upper multiplicative factor lambda>=1 because F lambda v+F-1 <= lambda(Fv+F-1). Bin replacement weakly reduces k, and increases residual by a factor strictly less than rho, or leaves zero exact. Thus the induction holds. At n, rho^n<=exp(eps/2)<=1+eps, since log(1+eps)>=eps/2 on [0,1]. Actual assignments verify each length, integer Kraft and exact product independently. This dominance proof is valid only for this label-local resource transition and its monotone residual observer; it does not claim original signed or joint state equivalence.

Complexity. Let J_h=1+ceil(log(U/a)/log(rho)) bound the positive bins, and C=max_i C_i. Each label has at most J_h prior states and C_i+1 choices; O(J_h sum_i(C_i+1)) candidate transitions, polynomial extra work for rational endpoint construction and binary search, integer addition/comparison, exact products and reconstruction. J_h=O(1+(n/eps)log(U/a)); for polynomially bounded M,C, rational input bit size B, J_h is polynomial in B,M,1/eps. Endpoint numerator/denominator bit lengths grow at most linearly in J_h times rational input/rho bit lengths. Products use at most n factors; Kraft integers have O(M+log n) bits. Keeping reconstruction pointers needs O(n J_h) states. A full copied witness per state is also polynomial. This is not an exact Pareto enumeration (R846 rules that out in general).

## 2. Factorized multi-group frontiers

In a private Kraft scope S with retained boundary labels and groups G_h by anchor, build each W_h independently, once for fixed R, weights, and caps. Let M cover boundary and private caps. Choose one witness z_h from each W_h and impose the single exact condition

    sum_h k(z_h) + sum_(v in boundary) 2^(M-L_v) <= 2^M.

Any such choice lifts to an original feasible private assignment with exactly its recorded group products. Conversely any original feasible private assignment admits a choice with each k no larger and each residual at most (1+eps) times the original. In particular this is a factored R845 approximate frontier. Neither lists nor their construction depend on the retained boundary lengths; those appear only in the exact capacity inequality, so the lists are reusable across all boundary tuples. Empty scopes and infeasible boundary are handled by the same inequality.

Total list construction across scopes is the sum of the one-group costs, with no exponent in the number of groups; explicit combined frontiers may still have product size prod_h |W_h|, and solving their coupled choices need not be polynomial. In contrast, R845 enumerates simultaneous count/slot/bin states and builds each conditional list for each boundary tuple. R847 avoids both within the list-building phase; the new global factorization uses one selection variable per group and a separate exact capacity factor per scope. For a supplied reduced primal elimination order of width t, with all factor scopes explicit, domain max D=max(grade caps+1, retained payment grid cardinality, max J_h+1), standard finite-domain elimination gives poly(input, precision) D^(t+1) operations and witness recovery. The capacity factor may have high arity and increase t; no bound by original incidence width is asserted. If using an explicit factor table, its construction is included in that width bound.

## 3. End-to-end R845 radius gap with these smaller lists

Keep R844 whole pendant bundles, each incident to exactly one anchor, and every eliminated label in at most one nontrivial Kraft scope. Free pendant labels take grade zero. Retain all original non-eliminated Kraft constraints, retained grades, and retained incidence payments. Original definitions: w_H=prod_f(1+b_f R^(L_f+2))-1; Q_A=prod_H(1+d_AH); T_AH=Q_A/(1+d_AH); r(T)=T/(2-T); safety Q_A<=2-eta and d_AH>=w_H prod_(D != A) r(T_DH); cost C=sum_A (Q_A-1)/(2-Q_A). For eliminated H recover exact d_AH=w_H; hence each selected group multiplier contributes exactly to the anchor product, even if pendant bundles cross private scopes at the same anchor.

Soundness: check all original Kraft, all retained payments, and safety after exact witness reconstruction, setting the pendant payments as above. The group list is only a restriction of feasible assignments.

Completeness with gap: suppose a capped real reference certificate at R2>R1>1 exists with Q<=2-eta. R839 supplies caps without increasing activity. Set pendant payments to w_H and condition on retained grades. If max(q,1+eps)<=(R2/R1)^2, choose the R847 witnesses at R1 for each private group. Every nonconstant positive monomial in v has degree at least 2, so its new residual <=(1+eps)v(R1)<=v(R2), and each capacity weakly decreases; all free factors also decrease. For retained H use the grade-independent base a_H=prod_f(1+b_f)-1 and ratio q, grid capped at 1-eta. Round reference d down to the largest grid point <=d*, which exists since d*>=w_H(R2)>=q a_H and d*<=1-eta. Then d>=d*/q. All relevant anchor factor products and excluded-factor T decrease; r(T) is increasing for 1<=T<2. Retained activity w_H(R1)<=w_H(R2)/q. Consequently the retained inequalities still hold, all Q<=reference Q, and C<=reference C. Thus the R845 max-gap guarantee and original safety are retained. This is an algorithmic certificate-search statement; the full native Port observer/FPTAS remains open.

## 4. Actual exact computations

The code below uses exact BigInt rational arithmetic. Local tests enumerate all permitted grade vectors for 1..5 labels, four deterministic weight/cap profiles, two radii and two eps values. End-to-end tests: two anchors, two Kraft scopes sharing one retained singleton bundle H with a grade common to both; each private group consists of singleton pendant bundles. First 24 networks have four singleton groups; next 8 have group sizes (2,1,1,2), exercising within-group compression and repeated group contributions to anchors. Each scope cap is its size minus one; shared cap is their max. R1=4/3, R2=5/3, q=5/4, eta=1/2; eps=1/4 or 1/2. At R2 every capped assignment is enumerated; because there is one retained incidence per anchor, the two minimal real payments are explicitly w*r(P_other), independent of the other payment. Exact tests for each feasible reference assignment find a capacity-nonincreasing list choice and payment grid floor with no larger objective. At R1 enumerate all list combinations and retained grades; for each, use the grid ceiling of those explicit minima. Reconstruct products, check exact original constraints and compare reduced optimum to reference optimum whenever the reference exists. This exercises a specific two-anchor/two-scope family, not a generic reduced-width implementation or performance benchmark.

Actual output:
```json
{
  "groupInstances": 208,
  "groupAssignments": 9504,
  "groupWitnesses": 2235,
  "groupTransitions": 7708,
  "groupReplacements": 1893,
  "groupCoverageChecks": 87056,
  "networkInstances": 32,
  "multiLabelNetworks": 8,
  "multiLabelNetworkReplacements": 84,
  "referenceFeasible": 3541,
  "referenceAssignments": 136904,
  "reducedCandidates": 1764,
  "reducedFeasible": 1764,
  "networkGapChecks": 3541,
  "networkFeasible": 27,
  "failures": 0
}
```

Reproduction (JavaScript BigInt, no dependencies):
```javascript
function replay(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a},F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<=0n)throw Error("denom");const g=gcd(a<0n?-a:a,b);return[a/g,b/g]},add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a),pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k)),one=F(1),two=F(2),eps=F(1,4),q=F(5,4),R1=F(4,3),R2=F(5,3),margin=F(3,2),factor=(b,R,l)=>add(one,mul(b,pow(R,l+2))),prod=a=>a.reduce(mul,one),res=p=>sub(p,one),r=p=>div(p,sub(two,p)),cost=p=>div(res(p),sub(two,p));
 const stats={groupInstances:0,groupAssignments:0,groupWitnesses:0,groupTransitions:0,groupReplacements:0,groupCoverageChecks:0,networkInstances:0,multiLabelNetworks:0,multiLabelNetworkReplacements:0,referenceFeasible:0,referenceAssignments:0,reducedCandidates:0,reducedFeasible:0,networkGapChecks:0,networkFeasible:0,failures:0};
 function list(B,Cs,R,M,e=eps){
  if(!B.length)return [{k:0n,p:one,L:[]}];
  const a=B.map(b=>mul(b,pow(R,2))).reduce((a,b)=>le(a,b)?a:b),U=res(prod(B.map((b,i)=>factor(b,R,Cs[i])))),rho=add(one,div(e,F(2*B.length))),edges=[a];
  while(le(edges.at(-1),U))edges.push(mul(edges.at(-1),rho));
  function bin(v){let lo=0,hi=edges.length-1;while(hi-lo>1){let m=(lo+hi)>>1;if(le(edges[m],v))lo=m;else hi=m}return lo}
  let st=[{k:0n,p:one,L:[]}];
  for(let i=0;i<B.length;i++){let mp=new Map();for(const x of st)for(let l=0;l<=Cs[i];l++){const k=x.k+(1n<<BigInt(M-l)),p=mul(x.p,factor(B[i],R,l)),key=bin(res(p)),o=mp.get(key);stats.groupTransitions++;if(!o||k<o.k||(k===o.k&&le(p,o.p))){if(o)stats.groupReplacements++;mp.set(key,{k,p,L:[...x.L,l]})}}st=[...mp.values()]}
  for(const x of st){if(x.k!==x.L.reduce((s,l)=>s+(1n<<BigInt(M-l)),0n)||!eq(x.p,prod(B.map((b,i)=>factor(b,R,x.L[i]))))||x.L.some((l,i)=>l<0||l>Cs[i]))throw Error("bad witness")}
  stats.groupInstances++;stats.groupWitnesses+=st.length;return st
 }
 function enumerate(Cs,cb,L=[]){if(L.length===Cs.length){cb(L);return}for(let l=0;l<=Cs[L.length];l++)enumerate(Cs,cb,[...L,l])}
 for(let n=1;n<=5;n++)for(let mode=0;mode<4;mode++)for(const R of [R1,F(2)])for(const e of [eps,F(1,2)]){
  const B=Array.from({length:n},(_,i)=>F(1+(i*3+mode)%7,2**(5+((i+mode)%4)))),Cs=B.map((_,i)=>1+(i+mode)%4),M=Math.max(...Cs),out=list(B,Cs,R,M,e);
  enumerate(Cs,L=>{let p=prod(B.map((b,i)=>factor(b,R,L[i]))),k=L.reduce((s,l)=>s+(1n<<BigInt(M-l)),0n);stats.groupAssignments++;if(!out.some(x=>{stats.groupCoverageChecks++;return x.k<=k&&le(res(x.p),mul(add(one,e),res(p))) }))throw Error("group gap")})
 }
 // Two Kraft scopes sharing a boundary H; H is a singleton retained bundle
 // in both anchors. Each group consists of singleton pendant bundles.
 for(let mode=0;mode<32;mode++){
  const big=mode>=24,ns=big?[2,1,1,2]:[1,1,1,1],cs=[ns[0]+ns[1],ns[2]+ns[3]],M=Math.max(...cs),cap=1n<<BigInt(M),b=F(1+mode%3,big?512:128),B=ns.map((n,h)=>Array.from({length:n},(_,i)=>F(1+(mode*3+h*5+i)%7,big?1024:256))),Cs=ns.map((n,h)=>Array(n).fill(cs[h>>1])),grid=[b];
  while(le(mul(grid.at(-1),q),F(1,2)))grid.push(mul(grid.at(-1),q));
  const before=stats.groupReplacements,lists=B.map((v,h)=>list(v,Cs[h],R1,M,big?F(1,2):eps)),minK=L=>1n<<BigInt(M-L),K=ls=>ls.reduce((s,l)=>s+minK(l),0n),P=(h,R,ls)=>prod(B[h].map((b,i)=>factor(b,R,ls[i])));
  if(big){stats.multiLabelNetworks++;stats.multiLabelNetworkReplacements+=stats.groupReplacements-before}
  let bestRef=null,bestRed=null;
  function cert(R,L,pp,d){let w=res(factor(b,R,L));let Q=pp.map((p,i)=>mul(p,add(one,d[i])));if(Q.some(v=>!le(v,margin)))return null;if(!le(mul(w,r(pp[1])),d[0])||!le(mul(w,r(pp[0])),d[1]))return null;return add(cost(Q[0]),cost(Q[1]))}
  for(let L=0;L<=M;L++){
   const boundary=minK(L);
   enumerate(Cs.flat(),flat=>{stats.referenceAssignments++;let pos=0;const ls=ns.map(n=>{let a=flat.slice(pos,pos+n);pos+=n;return a});
    if(boundary+K(ls[0])+K(ls[1])>cap||boundary+K(ls[2])+K(ls[3])>cap)return;
    const ps=ls.map((l,h)=>P(h,R2,l)),pp=[mul(ps[0],ps[2]),mul(ps[1],ps[3])];if(pp.some(v=>!le(v,margin)))return;
    const w=res(factor(b,R2,L)),ds=[mul(w,r(pp[1])),mul(w,r(pp[0]))],c=cert(R2,L,pp,ds);if(c===null)return;stats.referenceFeasible++;if(bestRef===null||le(c,bestRef))bestRef=c;
    const reps=ls.map((l,h)=>lists[h].find(x=>x.k<=K(l)&&le(x.p,ps[h])));if(reps.some(x=>!x))throw Error("lift local");
    const floor=d=>grid.filter(x=>le(x,d)).at(-1),d=ds.map(floor);if(d.some(x=>!x))throw Error("floor");const p=[mul(reps[0].p,reps[2].p),mul(reps[1].p,reps[3].p)],c1=cert(R1,L,p,d);if(c1===null||!le(c1,c))throw Error("network gap");stats.networkGapChecks++;
   });
   for(const x of lists[0])for(const y of lists[1])for(const z of lists[2])for(const t of lists[3]){
    if(boundary+x.k+y.k>cap||boundary+z.k+t.k>cap)continue;
    let pp=[mul(x.p,z.p),mul(y.p,t.p)];if(pp.some(v=>!le(v,margin)))continue;
    const w=res(factor(b,R1,L)),ceil=d=>grid.find(x=>le(d,x)),d=[ceil(mul(w,r(pp[1]))),ceil(mul(w,r(pp[0])))];stats.reducedCandidates++;if(d.some(x=>!x))continue;let c=cert(R1,L,pp,d);if(c===null)continue;stats.reducedFeasible++;if(bestRed===null||le(c,bestRed))bestRed=c;
    const actual=[x,y,z,t].map((v,h)=>P(h,R1,v.L));if(!eq(pp[0],mul(actual[0],actual[2]))||!eq(pp[1],mul(actual[1],actual[3])))throw Error("reconstruction");
   }
  }
  if(bestRef!==null){stats.networkFeasible++;if(bestRed===null||!le(bestRed,bestRef))throw Error("opt gap")}stats.networkInstances++;
 }
 return stats
}
console.log(JSON.stringify(replay(),null,2));
```

## 5. Continuation

Retain original signed joint moments, composite roads, branch identities, ordered steps, multiplicities, provenance and common depth; this compression is solely of auxiliary certificate witnesses. Next: test and implement generic factorized list selection with multiple retained bundles per anchor and width-aware exact capacity factors; investigate an approximate capacity accumulator that preserves feasibility and can use analytical radius slack, or exact structured selection on bounded separators. R846 lower bound remains intact; full Port observer and native realization remain open. No independent review or native BRC run.
