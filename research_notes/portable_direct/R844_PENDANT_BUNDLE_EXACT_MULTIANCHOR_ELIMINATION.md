# R844 — Exact pendant-bundle elimination in multi-anchor grading/payment certificates

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent informed portable TASK_RESEARCH, own metadata verified for EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, session MCP-ec17f2f30fb8409f8e664eb29ae6c08c, no runs and execution_authorized=false. R843 owner query succeeded with empty RUNNING projection as of 2026-11-27T12:24:29.090002Z, Source drift recorded. R844 query r3-20261127-r844-running-read queued at initial observation; no shared Task, ownership or Result mutation. Global canonical entry blobs verified at dbe50ca11792c0468bb4956f3b2a51efa4191316, applicable research/portable/residual rules read. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read; generated foundation and residual-position companion at frozen pin returned 404. Global P000 V4 and ACTIVE worldview read. Auxiliary certificate optimization, not a native Heartbeat computation. All original signed joint moments, branch identity, road matrices, ordered steps, provenance and common depth retained.

Sources: R843 321f9d8c48366bb1385ede42a6269db1be67ef5c:research_notes/portable_direct/R843_BOUNDARY_CONDITIONED_KRAFT_OVERLAP_KERNEL.md; R837 9d062156808e49e28ff18098f507ddd7c409bc1a:research_notes/portable_direct/R837_RATIONAL_GRID_PAYMENT_SEARCH_AND_SHARP_ROUNDING.md; R841 894f3d61c542a2a9c363c8c94c56cb151e05713a:research_notes/portable_direct/R841_DYADIC_PARTIAL_PRODUCT_GAP_SOLVER.md. R834/R839 prerequisites as used there. No external priority or independent review asserted.

## 1. Exact pendant bundle quotient

Fix the R834 cover A and original partition H, positive rational b_f, rational R>1 and safety margin 0<eta<1. Define u_f=b_f R^(L_f+2), w_H=prod_(f in H)(1+u_f)-1, Q_A=prod_(H in A)(1+d_AH), r(T)=T/(2-T), T_AH=Q_A/(1+d_AH). Require Q_A<=2-eta and d_AH>=w_H prod_(D in A_H minus A) r(T_DH); require all original neighborhood Kraft inequalities. The cost C is sum_A (Q_A-1)/(2-Q_A).

Select any collection of *whole bundles* E, each occurring in exactly one anchor. Call their labels eliminated and all other labels/bundles retained. After discarding trivial Kraft scopes (sizes 0,1), assume (i) each eliminated label occurs in at most one nontrivial scope; (ii) all eliminated labels of each such scope belong to bundles attached to a single common anchor. Retained lengths are boundary parameters. Labels in a retained bundle cannot be partially eliminated by this theorem. Eliminated labels with no nontrivial scope optimally have length 0. R839 gives the common private cap |S|-1 for an eliminated label of scope S, and finite retained caps M_v. Bundle partition may cut across multiple private scopes attached to the same anchor.

For each private scope S define F_S as R843's minimum product prod_(f in S intersect eliminated)(1+b_f R^(L_f+2)) conditioned on the retained labels of S; use +infinity if infeasible. Let P_A be the product of F_S over scopes assigned to A, times prod_(free eliminated f attached to A)(1+b_f R^2). Set
    Q'_A=P_A prod_(retained H in A)(1+d_AH).
Retain all nontrivial Kraft scopes with no eliminated labels. For retained bundles impose exactly the original inequalities using Q'_A in T'_AH=Q'_A/(1+d_AH). Minimize sum_A (Q'_A-1)/(2-Q'_A) subject to Q'_A<=2-eta.

Theorem. For arbitrary fixed retained lengths and retained payments (real or from any specified finite rational domains), the reduced problem is feasible iff an original extension exists with unrestricted nonnegative real eliminated payments. Its cost is the exact minimum original extension cost. Furthermore all eliminated payments in an attaining extension are rational whenever R,b are rational, irrespective of whether retained payments are real. Recover an optimal eliminated grading by independent R843 DP backtracking and set d_AH=w_H for every eliminated bundle.

Proof. Because an eliminated bundle occurs in one anchor, its own constraint is just d_AH>=w_H. Replacing its payment by w_H leaves that constraint satisfied and decreases Q_A, hence decreases every propagation ratio of retained bundles (for fixed retained payments), preserves margin, and cannot increase C. Multiple such replacements commute; no constraint for another eliminated bundle involves that ratio. After this substitution the eliminated contribution to Q_A is exactly prod_(f eliminated at A)(1+u_f), even when a bundle crosses private scopes, since 1+w_H=prod_(f in H)(1+u_f). Conditioning on all retained lengths, private scopes are disjoint in eliminated labels by (i); (ii) means each local minimum reduces precisely one anchor multiplier, not a tradeoff between different anchors. Free eliminated lengths are minimized at zero. R843 gives an attainable minimum for every local product. The combined minima weakly decrease all Q_A simultaneously; therefore all retained payment inequalities and C weakly improve. Conversely any reduced feasible point lifts via the local witnesses, with exact Q'_A=Q_A and exactly the reduced cost. This proves the extension optimum, including infeasible and empty-scope cases. No original observation is erased: the quotient concerns only the certificate cost/feasibility and a recoverable witness, not arbitrary original payment vectors or signed joint moments. Arbitrary other observations continue to use their original inputs.

## 2. Complexity and gap completeness

Let D=max(1,Delta,K), where K is the largest retained incidence grid cardinality; let F_S have boundary size h_S. Its full table is built in O(D^h_S (M+1)(|S|+1)^3) exact rational operations using R843, with M<=max(0,Delta-1). For each retained constraint and each anchor cost create a factor over the retained variables (lengths, individual payments) that its expression actually uses, including the boundary variables of its P_A dependencies. The retained payment inequality for (A,H) involves w_H and Q'_D,d_DH for D in A_H minus A. Margin and objective factors use Q'_A. Include all retained Kraft scopes. Let t be the width of a supplied elimination order of this reduced primal graph; all original factor scopes are cliques, hence at most t+1 variables each, and h_S<=t+1 if the corresponding nonconstant multiplier is included in its anchor factor. Constant or isolated factors are handled directly. Build exact factor tables and use min-sum variable elimination with +infinity for violations. The complexity is poly(N,B') D^(t+1), with polynomial-bit rational arithmetic for explicit domains and R839 caps; backtracking and original certificate verification are polynomial in the constructed table size. No exponent in the number of private labels or private payments occurs when t is bounded. This is not a claim that t is bounded for every original network; high-degree *retained* scopes may still cause large width. This algorithm is exact on the hybrid domain, not an exact general real-payments solver.

For a real certificate at R2>R1>1 with margin eta, use R839 cap, and grid base a_H=w_H(1), ratio 1<q<=2, cap 1-eta only on retained incidences. If q<=(R2/R1)^2, round each retained d* down to its grid: d>=d*/q, d<=d*, existence follows d*>=w_H(R2)>=q a_H. At R1 set each eliminated d=w_H(R1) (<=d*) using the original capped grading, then perform exact pendant minimization at those retained lengths. For all retained inequalities monotonicity gives w_H(R1) prod r(T_new)<=d*_AH/q<=d_AH; margins remain eta. Eliminated inequalities are exact by construction. Cost does not exceed the reference C at R2. Thus exact pendant elimination contributes *no* extra radius loss, safety-margin loss, or objective inflation; the remaining grid gap is R1<=R2/sqrt(q), unlike the additional generic R841 rounding loss where its local product compression is used. This is conditional on a reference real certificate, fixed cover/partition and the stated pendant structure; no full native Port theorem.

## 3. Unbounded-degree multi-anchor example and sharp boundary

Take two adjacent hubs 0,1, with k,j>=1 leaves, respectively. Use singleton bundles and three anchors: hub 0 plus its leaves, hub 1 plus its leaves, bridge {0,1}. This covers the exact dependency graph. Each leaf occurs in one anchor and one nontrivial Kraft scope, with the other hub as its fixed boundary. Retain just L0,L1 and four hub payments. For p0,p1 the conditional leaf products, let a,b be the hub payments at their own leaf anchors and c,e at the bridge. Then Q0=(1+a)p0,Q1=(1+b)p1,Qbridge=(1+c)(1+e). The four retained conditions are a>=w0 r(1+e), b>=w1 r(1+c), c>=w0 r(p0), e>=w1 r(p1). The number of retained variables is six regardless of k,j; a direct exact hybrid search is O((k+1)(j+1) K^4) evaluations after the local DP tables. This avoids enumerating a private payment grid K^(k+j) and private grade Cartesian products; cost accounting includes R843 local DP and full recovery. More generally a fixed bounded-degree backbone with leaf anchors and separate backbone edge anchors meets the pendant conditions; each hub's leaf scope uses only its backbone neighbors as retained boundary. The resulting retained constraint graph has scopes within bounded distance of the involved hubs, so a bounded-width backbone decomposition can be expanded by bounded-radius neighborhoods (and attach each hub's bounded number of payment variables) to bound retained width independently of leaf counts. Explicit scope construction above determines the exact width. In this extension assume each hub has at least one leaf and original nontrivial hub scopes may include all its backbone neighbors; singleton leaf scopes are trivial.

Restriction (ii) matters: a Kraft scope with fixed boundary length 2 and two eliminated labels attached to different anchors allows (L1,L2)=(1,2) and (2,1), but not (1,1). Separate scalar anchor minima would choose both lengths 1, which cannot lift. Positive b and R>1 strictly prefer shorter lengths. Such cross-anchor scopes require joint conditional frontier rather than independent scalar minima. Also a bundle with two anchors need not have d=w: if the opposite anchor contains another positive payment then r(T)>1. These are obstructions to the stated reduction rule, not general complexity lower bounds.

## 4. Executed exact checks

Double-star family k,j in 1..3, R in {4/3,2}, two weight profiles, margin 3/4 (Q<=5/4), retained grid {1/32,1/16,1/8} (arbitrary specified finite domains, not claimed to be R837 bases). Exhaustively compare R843 private DP to all private capped grade vectors for every boundary; for k,j<=2 also compare each fixed retained payment vector and each pair of feasible private products directly, and compare global optimal cost. For larger k,j the local minima and reduced payment search are executed; no complete cross-product comparison there. The proof gives general scope. All arithmetic is BigInt rational, not a BRC native experiment. No production timing or actual large Port observer test performed. Exact output:
```json
{
  "cases": 36,
  "boundaryCases": 648,
  "privateVectors": 20664,
  "slotTransitions": 4824,
  "paymentVectors": 11664,
  "feasiblePaymentVectors": 4013,
  "fullComparisons": 8100,
  "fullFeasibleCases": 12,
  "splitScopeWitness": 1
}
```

```javascript
function replay(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);const g=gcd(a<0n?-a:a,b);return[a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a),pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k)),one=F(1),two=F(2),zero=F(0),prod=a=>a.reduce(mul,one);
 const stats={cases:0,boundaryCases:0,privateVectors:0,slotTransitions:0,paymentVectors:0,feasiblePaymentVectors:0,fullComparisons:0,fullFeasibleCases:0,splitScopeWitness:0};
 const each=(caps,fn)=>{let a=[];function rec(i){if(i===caps.length){fn(a.slice());return}for(let l=0;l<=caps[i];l++){a[i]=l;rec(i+1)}}rec(0)};
 function kraft(L,M){return L.reduce((s,l)=>s+(1n<<BigInt(M-l)),0n)<=1n<<BigInt(M)}
 function slot(b,fixed,C,R){
  const k=b.length,d=k+fixed.length,M=Math.max(C,0,...fixed),c=Array(M+1).fill(0),tail=Array(M+2).fill(0);for(const l of fixed)c[l]++;for(let l=M;l>=0;l--)tail[l]=tail[l+1]+c[l];
  let map=new Map([["0,"+Math.min(1,d),{v:one,L:[]}]]);
  for(let l=0;l<=M;l++){let next=new Map();for(const [key,o] of map){const[i,s]=key.split(",").map(Number);let seg=one;
   for(let x=0;x<=Math.min(k-i,s-c[l],l<=C?k:0);x++){if(x)seg=mul(seg,add(one,mul(b[i+x-1],pow(R,l+2))));let j=i+x,rem=k-j+tail[l+1],t=Math.min(rem,2*(s-c[l]-x));if(l===M&&rem)continue;let q=j+","+t,v=mul(o.v,seg);stats.slotTransitions++;if(!next.has(q)||le(v,next.get(q).v))next.set(q,{v,L:o.L.concat(Array(x).fill(l))})}
  }map=next}return map.get(k+",0")??null;
 }
 const r=t=>div(t,sub(two,t)),cost=q=>div(sub(q,one),sub(two,q)),grid=[F(1,32),F(1,16),F(1,8)];
 function evalCase(w,p,d,margin){
  const [a,b,c,e]=d,Q=[mul(add(one,a),p[0]),mul(add(one,b),p[1]),mul(add(one,c),add(one,e))];
  if(Q.some(x=>!le(x,margin)))return null;
  if(!le(mul(w[0],r(add(one,e))),a)||!le(mul(w[1],r(add(one,c))),b)||!le(mul(w[0],r(p[0])),c)||!le(mul(w[1],r(p[1])),e))return null;
  return Q.map(cost).reduce(add,zero);
 }
 for(let k=1;k<=3;k++)for(let j=1;j<=3;j++)for(const R of [F(4,3),F(2)])for(let profile=0;profile<2;profile++){
  const b0=F(profile?3:1,256),b1=F(profile?2:1,256);
  const bs=[Array.from({length:k},(_,i)=>F(1+(profile?i%3:0),512)).reverse(),Array.from({length:j},(_,i)=>F(1+(profile?i%3:0),512)).reverse()];
  const margin=F(5,4);let best=null,bruteBest=null;
  for(let L0=0;L0<=j;L0++)for(let L1=0;L1<=k;L1++){
   const L=[L0,L1],w=[mul(b0,pow(R,L0+2)),mul(b1,pow(R,L1+2))],P=[],opts=[];
   for(let a=0;a<2;a++){let C=bs[a].length,fix=L[1-a],all=[],o=slot(bs[a],[fix],C,R),min=null;
    each(Array(C).fill(C),ls=>{stats.privateVectors++;if(kraft([...ls,fix],C)){let v=prod(ls.map((l,i)=>add(one,mul(bs[a][i],pow(R,l+2)))));all.push(v);if(min===null||le(v,min))min=v}});
    if((o===null)!==(min===null)||o&&!eq(o.v,min))throw Error("local optimum");
    if(o&&!kraft([...o.L,fix],C))throw Error("local recovery");P.push(o?.v??null);opts.push(all);stats.boundaryCases++;
   }
   if(P.some(x=>x===null))continue;
   each([2,2,2,2],inds=>{let d=inds.map(i=>grid[i]),v=evalCase(w,P,d,margin);stats.paymentVectors++;if(v){stats.feasiblePaymentVectors++;if(best===null||le(v,best))best=v}
    if(k<=2&&j<=2){let v2=null;for(const p0 of opts[0])for(const p1 of opts[1]){let z=evalCase(w,[p0,p1],d,margin);stats.fullComparisons++;if(z&&(v2===null||le(z,v2)))v2=z}
     if((v===null)!==(v2===null)||v&&!eq(v,v2))throw Error("conditioned optimum");if(v2&&(bruteBest===null||le(v2,bruteBest)))bruteBest=v2}
   });
  }
  if(k<=2&&j<=2){if((best===null)!==(bruteBest===null)||best&&!eq(best,bruteBest))throw Error("global optimum");if(best)stats.fullFeasibleCases++}
  stats.cases++;
 }
 if(!kraft([1,2,2],2)||!kraft([2,1,2],2)||kraft([1,1,2],2))throw Error("split scope");stats.splitScopeWitness++;
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
```

Next: replace independent scalar minima by a multiobjective conditional frontier when a private Kraft scope spans two or more anchors; seek a controlled gap and polynomial-size frontier for fixed anchor count while retaining simultaneous feasibility and reconstruction. Full original Port observer, native realization and general FPTAS remain open.
