# R832 — Overlap-bundle contextual product certificate

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own recovery r3-20261127-r832-own-read verified metadata, no run, execution_authorized=false. Original owner read r3-20261127-r832-running-read was RUNNING at last observation before this proof. No shared claim, task or Result mutations. Current EM control/source read at 4235c202f63c4ffbbf399584ad9cf2c069de3e7e; current global entries read at main 52d15897eb3e5fae58ccc5d886db682ebb706c0f and ACTIVE worldview. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer 3923890d77a02d84b772f789e6912dd14f220d14 read by blob. Current portable, method, BRC-only and residual rules read. Predecessor R831: 3d5b384fc982488fa6de188dfd8fcd7c8fef2db0:research_notes/portable_direct/R831_CONTEXTUAL_DELETION_RESOURCE_FRONTIER.md. Enumeration from R825: 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md.
Auxiliary fixed-charge joint-moment model only; no native Heartbeat/BRC arithmetic, new classical physical comparison or native attribution. Preserve all original signed factors, full joint moments, road matrices, branch IDs, provenance, time order and common depth.

## 1. Exact overlap bundle and new certificate

Use R831's independent groups B, labeled factors f with footprints F_f of s_f>=2 distinct groups, signed rational alpha_f, joint indicators I_f, joint moment envelope |E prod I_f|<=prod lambda_f for every subset, and factorization over disjoint group supports. Exact polynomial-time polynomial-bit joint moment oracles, positive baseline (zero baseline handled exactly), explicit incidence. Let b_f=|alpha_f| lambda_f, and fix integer costs c_f=s_f+L_f with the original per-group Kraft inequalities sum 2^(-L_f)<=1. Let P_U(t)=E prod_{f in U}(1+alpha_f I_f t^c_f). Factors of zero envelope may vanish in this observer only.

Partition the original labels into bundles H of identical footprint F_H. Any refinement of that partition also works. For fixed rational R>1, u_f=b_f R^c_f. Define
    w_H(U)=prod_{f in H intersect U}(1+u_f)-1,
    w_H=w_H(all).
Drop w_H=0 from the certificate only. For each group-bundle incidence (B,H), choose a nonnegative rational d_{BH}. Define
    Q_B=prod_{H incident B}(1+d_{BH}),
    T_{B|H}=prod_{K incident B,K!=H}(1+d_{BK}).
New theorem: if Q_B<2 for every B and
    w_H prod_{D in F_H minus {B}} [ T_{D|H}/(2-T_{D|H}) ] <= d_{BH}       (1)
for every incidence, then for every subset U and |t|<=R, P_U(t) is nonzero and
    |P_U/P_{U minus F(B)} -1| <= Q_B(U)-1,                              (2)
    Q_B(U)=prod_{H incident B}(1+d_{BH} w_H(U)/w_H).
Here F(B) denotes the set of original labels incident to B. The numerator and denominator in (2) are the original polynomials. No original label is erased, and no aggregate envelope is substituted for a joint moment. In particular, a parent bundle absent after deleting one group releases all parallel label resources, not just the label that first entered that group. Set r_B=Q_B-1<1. Then |log P(t)|<=sum_B r_B/(1-r_B), and the Taylor log tail at t=1 obeys
    E_k <= R^(-k)/(R-1) sum_B r_B/(1-r_B).                            (3)
The fixed log branch equals zero at t=0.

## 2. Proof

For each H and U use the exact polynomial random variable G_H(U,t)=prod_{f in H intersect U}(1+alpha_f I_f t^c_f)-1. Identity P_U=E prod_H(1+G_H). For a set C of bundles, the expectation E prod_{H in C} G_H is the sum over a nonempty original-label subset of H intersect U for each H. The moment envelope and triangle inequality imply its absolute value is <=prod_{H in C}w_H(U). This is an exact regrouping followed by a bound, not independence between parallel factors. Bundle supports disjoint in groups give factorization by the original independent-group hypothesis. Therefore the connected-polymer expansion on bundle labels is exact. Deleting group B gives
    P_U=P_{U minus F(B)}+sum_C W_U(C) P_{U minus N[C]},
where C is a nonempty connected bundle support touching B, W_U(C)=E prod_{H in C}G_H, and N[C] means all original labels in bundles sharing any group with C (within U). At least one label in each selected bundle is present; zero terms may be ignored.

Simultaneously induct (2) and nonvanishing on |U|. Empty U gives 1. If B has incident labels, denominator P_{U minus F(B)} is nonzero by induction. Fix C and use the deterministic queue tree of R831: at the first processing of a group discover each still undiscovered incident bundle of C, creating all its other groups as child occurrences; repeated groups are leaves. Each bundle discovered once; factor labels of C can be recovered from the bundle labels for this bound (original labels remain in W_U(C)). Delete all distinct groups of C in first-occurrence FIFO order, root B first. When a nonroot D is reached through H, every label of H has already been deleted by its parent group. For the smaller surviving subset V, Q_D(V)<=T_{D|H}, so the inverse deletion ratio has modulus <=1/(2-T_{D|H}) by the inductive (2). A repeated group occurrence need not be deleted again; paying this >=1 reciprocal again only enlarges the bound. Deleting these groups yields exactly U minus N[C].

To sum over C, enlarge the injected tree set to all alternating trees with distinct incident child-bundle labels at a group, excluding its parent label. Nonnegative subtree bound at nonroot (D,H) is T_{D|H}, by induction on depth from 1: each possible child K contributes at most w_K prod_{E in F_K minus D} T_{E|K}/(2-T_{E|K}) <= d_{DK} by (1). Thus the sum over child subsets is bounded by the product defining T_{D|H}. At the root use the actual w_K(U), giving contribution at most d_{BK}w_K(U)/w_K and tree total <=Q_B(U). Remove the empty tree to bound the sum of deviations by Q_B(U)-1. The finite-height majorants are monotone and bounded, so the limit is valid. This proves (2); since Q_B(U)-1<1, any U with an incident label is nonzero, closing induction. Groups with no incident labels have ratio 1. Telescoping group deletions, analytic logarithm series gives |log ratio|<=r_B/(1-r_B); Cauchy's coefficient estimate gives (3). No assumption on arity, overlap or group degree beyond the certificate.

## 3. Constructive witness search

Let Phi(d) be the right-to-left bound in (1), component by component. On the downward-closed domain Q_B<2 it is monotone in all d (each T/(2-T) is increasing). Starting at d=0, repeatedly compute d'=Phi(d) using rational arithmetic; the sequence is nondecreasing and bounded by any feasible witness. If a finite iterate violates Q_B<2, no such witness exists for this R and grouping, since every feasible witness would dominate that iterate. If there is a feasible witness, the limit is the least fixed point: finite dimension, monotone bounded convergence, denominators uniformly positive under the feasible upper bound. Conversely, a rational supersolution with Q_B<2 is a directly checkable certificate. Exact iteration is a discovery method, not a proven polynomial-time convergence algorithm; intermediate numerator/denominator bit lengths may grow. For FPTAS use supplied polynomial-bit rational supersolutions or a proven constructive family below. Partial remaining labels automatically yield the tighter Q_B(U); removing a bundle completely removes its cost from numerator and denominator. This includes R831's multi-removal history in a new multiplicative budget, and is nonuniform by incidence.

## 4. Unbounded square-root load at fixed radius, unbounded topology

Take any 4-regular simple graph, e.g. the Cartesian product of two cycles of equal length >=3, with g groups at vertices. For each graph edge make a bundle of m=2^j labeled factors, all with the two endpoint groups as footprint. No physical road realization claimed. Use L=2+j (original Kraft exact 4m*2^-L=1), c=4+j, R=4/3, lambda_f=1 and b_f=1/(32m R^c). Signs arbitrary. One concrete nontrivial hard-correlated local model uses a shared Bernoulli bit at each group, I_f=product of endpoint bits, arbitrary rational probabilities, satisfying the envelope. These moments are exact and polynomial-bit. More generally use any original oracles meeting the hypotheses.

For each bundle u_f=1/(32m), and
    w_H=(1+1/(32m))^m-1 <= 1/31
by binomial coefficient <=m^k and the geometric sum. Set all d_{BH}=1/16. Then T=(17/16)^3=4913/4096; T/(2-T)=4913/3279. Consequently
    w_H*T/(2-T)<=4913/(31*3279)<1/16,
and Q_B=(17/16)^4=83521/65536<2. All parameters are explicit rational and construction costs polynomial in the original label/incidence input length. In contrast, the original R831 square-root load M=max_B sum sqrt(2^s_f b_f) satisfies
    M^2=64m^2 b_f=2m/R^(4+j)=(81/128)*(3/2)^j -> infinity.
Already j=2 gives M^2>4/3, above R831's best universal contextual witness. Thus for this family the new certificate handles simultaneously unbounded original square-root load, label incidence degree, network size and treewidth, with a fixed R=4/3. The graph family has unbounded treewidth by square-grid subgraphs. This is a separation from the old *uniform square-root guarantee*, not a necessity lower bound on all previous algorithms or all R831 nonuniform certificates. No claim that every input with large M is tractable. Positive/negative signs and all correlated moments are retained. In the stated hard-correlated example, lambda=1 is a valid (not necessarily optimal) envelope.

R825's exact original-label Kraft queue and connected-support Mobius extraction still apply without change. The analytic grouping is not used to compress or delete original coefficients. Enumerate connected supports of original cost <=k in g*2^O(k) poly(N,k), evaluate exact pinned original joint moments and truncate log P. For fixed R>1 and Q_B<=2-eta with fixed eta>0, (3) yields k=O(log((g+1)/epsilon)); polynomial input/oracle precision and rational arithmetic follow R825. Certificate verification is polynomial in the supplied rational bit lengths and incidence count when costs c_f are polynomially bounded in N (as here); for arbitrary supplied exponential binary costs, exact powers require separate bit-complexity control. Original enumeration can restrict to labels eligible at cost <=k. Positive baseline and real coefficients give P(1)>0 by nonvanishing and P(0)=1. Certified scalar recovery then yields FPTAS. For the family, r=17985/65536; g=10000, epsilon_log=1/100, exact minimal sufficient k=49 from (3).

## 5. Executed evidence

Replay below is auxiliary BigInt exact rational/Gaussian-rational computation, not native BRC dynamics or physical comparison. Five incidence shapes, three sign/weight/probability fixtures each, all original-label subsets, every group deletion, three complex boundary points R,iR,(3+4i)R/5. Verify the sharper partial-bundle bound (2) by squared moduli, and exact local certificate checks. Family parameters j=0..8; check separation for j>=2 and the minimality of k. First draft of verification had an inverted Boolean in the Q<2 assertion; corrected to !le(2,Q), then the full run passed. No mathematical counterexample was inferred from the script mistake. Results: {"stats":{"family":18,"local":290,"ratios":9360,"instances":15,"exact_separation":7,"cutoff":2},"k":49,"total":9677}.
```javascript
function verify(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]};
 const a=(x,y)=>F(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),s=(x,y)=>a(x,[-y[0],y[1]]),m=(x,y)=>F(x[0]*y[0],x[1]*y[1]),v=(x,y)=>F(x[0]*y[1],x[1]*y[0]),p=(x,k)=>F(x[0]**BigInt(k),x[1]**BigInt(k)),le=(x,y)=>x[0]*y[1]<=y[0]*x[1];
 const O=F(1),Z=F(0),T=F(2),R=F(4,3),d=F(1,16),A=v(p(a(O,d),3),s(T,p(a(O,d),3)));
 const G=(x,y=Z)=>[x,y],ga=(x,y)=>G(a(x[0],y[0]),a(x[1],y[1])),gs=(x,y)=>G(s(x[0],y[0]),s(x[1],y[1])),gm=(x,y)=>G(s(m(x[0],y[0]),m(x[1],y[1])),a(m(x[0],y[1]),m(x[1],y[0]))),gn=x=>a(p(x[0],2),p(x[1],2)),gp=(x,k)=>{let z=G(O);while(k--)z=gm(z,x);return z};
 const stats={family:0,local:0,ratios:0,instances:0,exact_separation:0,cutoff:0};const ck=(b,key)=>{if(!b)throw Error(key);stats[key]++};
 ck(le(m(F(1,31),A),d),"local");ck(!le(T,p(a(O,d),4)),"local");
 for(let j=0;j<=8;j++){let n=2n**BigInt(j),c=4+j,b=v(F(1,32n*n),p(R,c)),u=m(b,p(R,c));ck(le(s(p(a(O,u),Number(n)),O),F(1,31)),"family");let M2=m(F(64n*n*n),b);ck(le(M2,m(F(81,128),p(F(3,2),j)))&&le(m(F(81,128),p(F(3,2),j)),M2),"family");if(j>=2)ck(!le(M2,F(4,3)),"exact_separation")}
 const shapes=[[[[0,1],3]],[[[0,1],2],[[1,2],2],[[0,2],2]],[[[0,1,2],2],[[1,2,3],2],[[0,3],2]],[[[0,1],2],[[0,2],1],[[0,3],1],[[0,4],2]],[[[0,1,2,3],3],[[0,1],2],[[2,3],1]]];
 for(const shape of shapes)for(let trial=0;trial<3;trial++){
  const groups=1+Math.max(...shape.flatMap(x=>x[0])),fs=[],bundles=shape.map(([foot,n],h)=>{let ids=[];for(let i=0;i<n;i++){ids.push(fs.length);fs.push({foot,h,u:F(1+(i+trial)%3,96*n)})}return {foot,ids}}),n=fs.length,adj=Array.from({length:groups},(_,b)=>bundles.map((h,i)=>h.foot.includes(b)?i:-1).filter(i=>i>=0)),maxDeg=Math.max(...adj.map(H=>H.reduce((z,h)=>z+bundles[h].ids.length,0))),L=Math.ceil(Math.log2(maxDeg)),prob=Array.from({length:groups},(_,b)=>F(1+(b+trial)%4,4));
  const U=(h,mask)=>s(bundles[h].ids.reduce((z,i)=>mask>>i&1?m(z,a(O,fs[i].u)):z,O),O),full=(1<<n)-1,W=bundles.map((_,h)=>U(h,full));
  const Tmsg=(b,h)=>adj[b].filter(k=>k!==h).reduce(z=>m(z,a(O,d)),O);
  for(let h=0;h<bundles.length;h++)for(const b of bundles[h].foot){let z=W[h];for(const e of bundles[h].foot)if(e!==b){let t=Tmsg(e,h);ck(!le(T,t),"local");z=m(z,v(t,s(T,t)))}ck(le(z,d),"local")}
  for(const H of adj)ck(!le(T,H.reduce(z=>m(z,a(O,d)),O)),"local");
  for(const t of [G(R),G(Z,R),G(m(R,F(3,5)),m(R,F(4,5)))]){
   const zf=fs.map((f,i)=>gm(G(m(F(i%2?1:-1),v(f.u,p(R,f.foot.length+L)))),gp(t,f.foot.length+L)));
   const P=Array.from({length:full+1},(_,mask)=>{let z=G(O),seen=new Set();for(let i=0;i<n;i++)if(mask>>i&1){z=gm(z,zf[i]);fs[i].foot.forEach(b=>seen.add(b))}for(const b of seen)z=gm(z,G(prob[b]));return z});
   for(let i=0;i<n;i++)for(let mask=0;mask<=full;mask++)if(mask>>i&1)P[mask]=ga(P[mask],P[mask^(1<<i)]);
   for(let mask=0;mask<=full;mask++)for(let b=0;b<groups;b++){let V=mask,Q=O;for(const h of adj[b]){for(const i of bundles[h].ids)V&=~(1<<i);Q=m(Q,a(O,m(d,v(U(h,mask),W[h]))))}ck(gn(P[V])[0]>0n&&le(gn(gs(P[mask],P[V])),m(p(s(Q,O),2),gn(P[V]))),"ratios")}
  }stats.instances++;
 }
 const rho=s(p(a(O,d),4),O),C=v(m(F(10000),rho),m(s(O,rho),s(R,O))),eps=F(1,100);let k=0;while(!le(C,m(eps,p(R,k))))k++;ck(le(C,m(eps,p(R,k))),"cutoff");ck(!le(C,m(eps,p(R,k-1))),"cutoff");
 return {stats,k,total:stats.family+stats.local+stats.ratios+stats.exact_separation+stats.cutoff};
}
console.log(verify());
```

## 6. Next question

Study bundles with near-identical (rather than identical) footprints, using explicit common-core deletion and retaining exceptional groups, and develop efficient nonuniform witness optimization with bit-complexity control. The bundle family demonstrates that original-label square-root load alone is not a necessary complexity coordinate. Weak-bias parity moment bounds and realization by the original native Port/BRC road generator remain open; no native experimental result or general Port FPTAS claimed.
