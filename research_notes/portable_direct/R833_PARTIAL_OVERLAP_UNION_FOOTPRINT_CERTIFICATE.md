# R833 — Partial-overlap union-footprint certificate and exact deletion-history bound

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH. Own session metadata verified by r3-20261127-r833-own-read, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, execution_authorized=false; no claim or Result mutation. Owner query r3-20261127-r833-running-read was RUNNING at the last prepublication read; continue original receipt. Current normative entries read at global main@37b4077045d582784c58c2dd09e06a5fe1a34c6c and Source@b091d79f5b7b493918b181750b2494c3688799a2. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14, ACTIVE worldview and current portable/BRC-only/residual rules read. Generated frozen startup returned 404; original foundation files read. R832 predecessor d7b2f813b12780c30120efc98f0577cec21db0dc:research_notes/portable_direct/R832_OVERLAP_BUNDLE_CONTEXTUAL_PRODUCT_CERTIFICATE.md. R825 original-label enumeration 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md.
This is the existing auxiliary fixed-charge joint-moment model, not native Heartbeat/BRC arithmetic or an external physical comparison. Preserve original signed BRC, full road matrices, branches, provenance, time order and common depth.

## 1. Arbitrary union-footprint bundles
Use R832 assumptions: independent groups B, explicit original factors f with true footprint F_f of s_f>=2 groups, signed rational alpha_f, indicators I_f measurable in F_f, joint envelope |E prod I_f|<=prod lambda_f for all subsets and exact polynomial-time polynomial-bit moment oracles. Original costs c_f=s_f+L_f, original per-group Kraft inequalities. P_U(t)=E prod_{f in U}(1+alpha_f I_f t^c_f). Fixed R>1, u_f=|alpha_f|lambda_f R^c_f.
Partition labels into arbitrary nonempty bundles H, no identical-footprint hypothesis. Let V_H=union_{f in H}F_f (or any supplied superset, with explicit incidence), D(B)=union_{H:B in V_H}H (artificial deletion set), and w_H(U)=prod_{f in H intersect U}(1+u_f)-1, w_H=w_H(all). Zero-envelope bundles may be removed for this observer only.
Choose d_BH>=0, Q_B=prod_{H:B in V_H}(1+d_BH)<2, T_{B|H}=prod_{K:B in V_K,K!=H}(1+d_BK). The R832 certificate with union footprints is:
 w_H prod_{D in V_H minus {B}} T_{D|H}/(2-T_{D|H}) <= d_BH. (1)
Define Q_B(U)=prod_{H:B in V_H}(1+d_BH w_H(U)/w_H).
Then P_U(t) is nonzero for all U, |t|<=R, and
 |P_U/P_{U minus D(B)}-1|<=Q_B(U)-1. (2)
Proof: use G_H(U)=prod_{f in H intersect U}(1+alpha_f I_f t^c_f)-1. It is measurable on V_H, even if actual selected labels use fewer groups. Expanding products of G_H, the joint envelope bounds each selected bundle by w_H(U), and disjoint union footprints guarantee factorization. Connected components on the artificial graph give an exact polymer expansion (extra connectivity merely changes component grouping). R832's entire group-deletion induction and queue-tree majorant apply with V_H, D(B): after processing a group, every bundle incident to it is absent, so T excludes the parent bundle. No need to assume identical true footprints. This proves (2), nonvanishing and the R832 log tail E_k <= R^(-k)/(R-1) sum_B (Q_B-1)/(2-Q_B).
Original coefficients are unchanged. Artificial deletion and true deletion must be distinguished; treating all labels of an arbitrary bundle as actually touching each group would be incorrect. This construction is solely an analytic payment representation.

## 2. Partial deletion theorem
For ANY S subset U intersect D(B), put V=U minus S, P_0=P_{U minus D(B)}=P_{V minus D(B)}. Then the sharper bound is
 |(P_U-P_V)/P_0| <= Q_B(U)-Q_B(V), (3)
 |P_U/P_V-1| <= [Q_B(U)-Q_B(V)]/[2-Q_B(V)]. (4)
This includes true group deletion S=U intersect {f:B in F_f}, and even individual label deletion. It provides a quantitative residual for artificial incidence rather than silently equating true and artificial deletion.
Proof of (3): in the polymer deletion expansion for the common root B, only connected selected bundle sets C touching B occur. For any such C, D(B) subset N[C] (closed bundle neighborhood expressed in original labels). Thus the complement P_{U minus N[C]} equals P_{V minus N[C]}. The difference of W_U(C) and W_V(C) is the sum over original choices with at least one label in S, hence its modulus is bounded by prod_{H in C}w_H(U)-prod_{H in C}w_H(V). Only root-incident bundle weights can change. In the deterministic R832 queue tree all selected root-incident bundles are discovered at the root. Factor the difference into the product of full (unchanged) descendant weights times the difference of products of root weights. The common complement ratio to P_0 has the same inverse deletion bounds as R832 for U (all later groups have their parent bundle already absent). Repeated group occurrences may be paid again as in R832. Enlarge the injected trees to all alternating trees; for each child root bundle H the descendant sum times inverse deletion factors is bounded by d_BH/w_H via (1) and the T majorant, independent of its root weight. Because each root product difference is nonnegative, summing over root subsets gives exactly the difference Q_B(U)-Q_B(V). This proves (3). By (2), |P_V/P_0|>=2-Q_B(V)>0, proving (4). The bound can vanish for an empty S and uses no artificial independence of factors inside H. The exact polynomial and signed joint moments are retained.

## 3. Leaf-free nonparallel separating family
Let G be a 4-regular simple graph from even-side square tori (unbounded treewidth, even vertex count). For each vertex v create a bundle H_v of m=2^j, j>=1, original labels f_{v,i}. Their common true core has h=256 private groups plus 4 groups x_e, one for each edge of G incident to v; x_e is shared by its endpoint bundles. Label f_{v,i} additionally contains its own fringe group y_{v,i}. Thus true footprints all differ, arity s=261, union arity 260+m. Pair vertices in any perfect pairing of the vertex set (not necessarily edges); for every pair (v,w), join y_{v,i},y_{w,i} by one weak two-group connector label, its own singleton bundle. All true and union group incidences have degree >=2 in their respective graphs except private core groups in the union graph, whose original incidence degree is m>=2; no original degree-one group or factor. Original incidence graph contains a subdivision of G by choosing f_{v,1} and shared x_e, so treewidth unbounded.
Take lambda=1, original L=j+1 for large labels, L=1 for weak connectors, so c=262+j and c=3 respectively. Original Kraft: private core m/(2m)=1/2, shared x_e 2m/(2m)=1, fringe 1/(2m)+1/2<=1. Set R=4/3, |alpha_f|=u_f/R^c with u_f=1/(32m) on H_v, u_f=1/(128m) on connector. A concrete joint model uses independent rational Bernoulli bits per group, with I_f product of endpoint/group bits; signs may be arbitrary. These exact joint moments require only the union of true footprints. No physical/native generator assumed.
For H_v, w_H=(1+1/(32m))^m-1<=1/31 by binomial/geometric majorization. Choose d_BH=1/8 on its entire union, and d_BK=1/(64m) for weak connectors. At private core, T excluding H is 1. At shared x_e, T excluding H is 9/8 so T/(2-T)=9/7. At fringe T excluding H is 1+x with x=1/(64m). Its ratio (1+x)/(1-x)<=1+1/(31m), hence product over m fringe groups <=31/30 by binomial/geometric majorization. Consequently every H incidence obeys
 w_H prod T/(2-T) <= (9/7)^4/30 < 1/8.
For a connector, its other fringe has T=9/8; u_K*(9/7)<=1/(64m). All Q_B<=81/64<2 (shared x_e maximal). R825 original-label Kraft enumeration remains valid and does not expand a whole bundle in one oracle query. Fixed R and fixed gap give deterministic FPTAS, k=O(log((g+1)/epsilon)); all explicit incidences and rational parameters have polynomial bit length and construction cost in original input N. Original moments are evaluated exactly on connected supports; artificial edges are only for convergence, not enumeration. R825 complexity g*2^{O(k)} poly(N,k) applies on the original graph. Positive baseline, real coefficients, nonvanishing along [0,1] and P(0)=1 imply positive scalar P(1); use R825 certified recovery.
R831 square-root load at shared x_e has M^2 >= (2m)^2 2^261/(32m R^(262+j)), diverging like (3/2)^j. Stronger separation: R832 identical-footprint grouping is forced to singleton labels. For any feasible R832 d, each d_Bf>=u_f since all ratios>=1. At a private core B of H_v, each of the other 255 private core groups D has T_{D|f}>=(1+u_f)^(m-1)>=1+1/64, hence T/(2-T)>=65/63. Thus every d_Bf >= u_f*(65/63)^255 and Q_B>=1+m*u_f*(65/63)^255>2; indeed the quadratic binomial terms in (1+2/63)^255 alone with the constant/linear terms give >32. Contradiction. This excludes ALL nonnegative R832 singleton witnesses for this original input and fixed R=4/3 (also any larger radius), not just uniform choices. R833 union grouping certifies it. It is an auxiliary-model separation, not a native Port realization or lower bound on arbitrary algorithms.
The family uses true and artificial group graphs separately. Private groups of original degree m become degree one analytically; the gain is resource release without erasing original observations. The next problem is overlapping bundles that share many peripheral groups of nonnegligible load: design a nonuniform partition/cover selection with certified complexity and compare actual original-label truncation cost. Native Port realizability and general FPTAS remain open.

## 4. Executed exact verification
The following deterministic JavaScript BigInt replay was actually executed. Four small shapes, three signed/rational Bernoulli fixtures each, all label subsets, all artificial-root partial deletions, three boundary points R,iR,(3+4i)R/5. Check (1), (2), (4) with exact squared moduli. Also sweep family j=1..8. It is a model-internal auxiliary combinatorial check, not a native physical reference run. General theorem uses the proof. Actual counts: {"fixtures":12,"local":153,"ratios":3888,"partial":14661,"family":64}. No failed assertions. No production FPTAS performance test.
```js
function replay(){
 const Q=(n,d=1n)=>[BigInt(n),BigInt(d)], add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]), neg=a=>Q(-a[0],a[1]), sub=(a,b)=>add(a,neg(b)), mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]), le=(a,b)=>a[0]*b[1]<=b[0]*a[1], pow=(a,n)=>Q(a[0]**BigInt(n),a[1]**BigInt(n)), one=Q(1), two=Q(2), zero=Q(0);
 const stats={fixtures:0,local:0,ratios:0,partial:0,family:0};const ok=(x)=>{if(!x)throw Error("failed "+JSON.stringify(stats));};
 const shapes=[
 {F:[[0,1,2],[0,1,3],[2,3]],H:[[0,1],[2]]},
 {F:[[0,1],[0,2],[1,3],[2,3],[0,3]],H:[[0,1],[2,3],[4]]},
 {F:[[0,1,2],[1,2,3],[2,3,4],[0,4]],H:[[0,1],[2,3]]},
 {F:[[0,1],[1,2],[3,4],[4,5],[0,5]],H:[[0,2],[1,3],[4]]}
 ];
 const ga=(a,b)=>[a[0]+b[0],a[1]+b[1]], gs=(a,b)=>[a[0]-b[0],a[1]-b[1]], gm=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]], scale=(a,b)=>[a[0]*b,a[1]*b], norm=a=>a[0]*a[0]+a[1]*a[1];
 const R=Q(4,3), d=Q(1,16);
 for(const {F,H} of shapes)for(let fix=0;fix<3;fix++){
   stats.fixtures++;const n=F.length,g=1+Math.max(...F.flat()),all=(1<<n)-1, signs=F.map((_,i)=>BigInt(((fix+i)%2?-1:1)*(1+(fix+i)%2)));
   const masks=F.map(a=>a.reduce((m,b)=>m|(1<<b),0)), hm=H.map(a=>a.reduce((m,b)=>m|(1<<b),0)), unions=H.map(a=>a.reduce((m,b)=>m|masks[b],0)), inc=Array.from({length:g},(_,b)=>H.map((_,h)=>h).filter(h=>unions[h]&(1<<b)));
   const u=signs.map(a=>mul(Q(a<0n?-a:a,8192),pow(R,8)));
   const w=(h,U)=>sub(H[h].filter(f=>U&(1<<f)).reduce((v,f)=>mul(v,add(one,u[f])),one),one), full=H.map((_,h)=>w(h,all));
   const T=(b,h)=>pow(add(one,d),inc[b].filter(k=>k!==h).length);
   const qb=(b,U)=>inc[b].reduce((q,h)=>mul(q,add(one,mul(d,div(w(h,U),full[h])))),one);
   for(let b=0;b<g;b++){
     ok(!le(two,qb(b,all)));stats.local++;
     for(const h of inc[b]){let v=full[h];for(let z=0;z<g;z++)if(z!==b&&(unions[h]&(1<<z))){const t=T(z,h);v=mul(v,div(t,sub(two,t)))}ok(le(v,d));stats.local++}
   }
   for(const [a,b,z] of [[4n,0n,3n],[0n,4n,3n],[12n,16n,15n]]){
     let t=[1n,0n];for(let i=0;i<8;i++)t=gm(t,[a,b]);const den=8192n*z**8n;
     const P=Array.from({length:all+1},()=>[0n,0n]);
     for(let state=0;state<(1<<g);state++){
       let weight=1n;for(let v=0;v<g;v++)if(state&(1<<v))weight*=BigInt(1+((v+fix)%3));
       const terms=masks.map((m,i)=>(state&m)===m?ga([den,0n],scale(t,signs[i])):[den,0n]);
       for(let U=0;U<=all;U++){let p=[weight,0n];for(let i=0;i<n;i++)p=gm(p,U&(1<<i)?terms[i]:[den,0n]);P[U]=ga(P[U],p)}
     }
     for(let U=0;U<=all;U++)for(let v=0;v<g;v++){
       const D=inc[v].reduce((x,h)=>x|hm[h],0), live=U&D, base=U&~D;
       const check=(V,bound)=>{const nn=norm(gs(P[U],P[V])),dd=norm(P[V]);ok(dd>0n&&le(Q(nn,dd),pow(bound,2)))};
       check(base,sub(qb(v,U),one));stats.ratios++;
       for(let S=live;;S=(S-1)&live){const V=U&~S;check(V,div(sub(qb(v,U),qb(v,V)),sub(two,qb(v,V))));stats.partial++;if(!S)break}
     }
   }
 }
 // All family inequalities are symbolic except this exact parameter sweep.
 for(let j=1;j<=8;j++){
   let m=2**j, x=Q(1,64*m), u=Q(1,32*m);
   const fringe=pow(div(add(one,x),sub(one,x)),m);
   ok(le(fringe,Q(31,30)));stats.family++;
   ok(le(mul(mul(Q(1,31),pow(Q(9,7),4)),fringe),Q(1,8)));stats.family++;
   ok(le(mul(Q(1,128*m),Q(9,7)),x));stats.family++;
   ok(le(mul(Q(9,8),add(one,x)),Q(81,64)));stats.family++;
   ok(!le(mul(Q(1,32),pow(Q(65,63),255)),one));stats.family++;
   ok(le(mul(Q(m-1),u),Q(1,32)));stats.family++;
   ok(le(Q(1,64),mul(Q(m-1),u)));stats.family++;
   ok(le(add(Q(1,2*m),Q(1,2)),one));stats.family++;
 }
 return stats;
}
console.log(replay());
```
