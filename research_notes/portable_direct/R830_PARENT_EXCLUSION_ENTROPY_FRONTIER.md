# R830 — Parent-exclusion entropy frontier for oriented group deletion

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CERTIFICATE_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Existing own session metadata recovered via r3-20261127-r830-own-read (no runs; execution_authorized=false). Owner inventory r3-20261127-r830-running-read was RUNNING during derivation; no shared claim, owner or Result mutation. Current control Source b0960b0e767177f2b6bb7437275bf19aa662f7f0; global entries at immutable main 46139b0a5f0e5ba7b5528541a21da41ddda2c747 verified, current method/portable/ACTIVE worldview/BRC and residual constraints read. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer 3923890d77a02d84b772f789e6912dd14f220d14; generated startup at frozen pin 404, actual foundation sources read directly. R829 970005915b9a3d1c827077730c2310a891736602:research_notes/portable_direct/R829_SHARP_UNIFORM_RADIUS_FRONTIER.md; R828 91fde1508398af7b109503e1155fc9f727853f50:research_notes/portable_direct/R828_GROUP_DELETION_BRANCHING_MAJORANT_FPTAS.md sections 1–2; R825 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md section 1. R812/R813 representation and R824 moment envelope retain their declared scope. Auxiliary combinatorial theorem, not native BRC dynamics or native residual attribution. Preserve signed BRC, joint relations, all road matrices, ordered branch provenance and common depth.

## 1. Statement and resource coordinates

Use R829's independent base groups B (g groups), explicit labeled residual factors f with footprints F_f of cardinality s_f>=2, coefficients alpha_f (signed rational), exact polynomial-time polynomial-bit pinned joint moment oracles, moment bound |E prod_{f in J} I_f|<=prod_{f in J} lambda_f, and factorization across disjoint group supports. Define b_f=|alpha_f|lambda_f, a_f=2^s_f b_f, M=max_B sum_{f incident B} sqrt(a_f). Zero-activity labels vanish only in this observer's expansion. The target is Z=Z_base P(1), P(t)=E prod_f(1+alpha_f I_f t^{c_f}); positive exact baseline, zero baseline handled exactly. For a fixed promise M<=sqrt(beta), use p_f=sqrt(a_f/beta)>0, L_f=ceil(log2(1/p_f)), c_f=s_f+L_f, so sum p_f<=1 per group, Kraft holds. L_f is computed by exact integer/rational comparisons, not numerical logarithms.

Theorem: for fixed 1<R<2, 0<rho<1, set A=(1+rho)/(1-rho). The explicit parent-exclusion witness Y_{B|f}=1+rho(1-p_f) satisfies R828's oriented incidence and root conditions for all such auxiliary inputs if and only if
    R A <= 2,       beta R^3/[4(1-rho)] <= rho.                      (1)
Thus with rho=(2-R)/(2+R), the sharp frontier of this specific witness template is
    beta <= B_or(R)=8(2-R)/[R^2(2+R)^2].                            (2)
Its limiting square-root threshold at R down to 1 is sqrt(8/9)=2sqrt(2)/3. For every fixed M below it there is a fixed positive radius margin and deterministic FPTAS; the limit itself is open. This is optimality for this explicit witness and allocation, not a complexity lower bound or sharp zero-freeness for all methods.

## 2. Proof of sufficiency

Recall the R828 oriented tree majorant. Put u_f=b_f R^{c_f}. For each incidence (B,f), require
    product_{h incident B,h!=f}(1+u_h product_{D in F_h minus B} Y_{D|h}/(1-rho)) <= Y_{B|f},
and at root B the same product over all h <=1+rho.
R828's queue injection excludes the parent factor; each selected connected support is represented once with its full factor labels, and all nonroot group deletions are paid. Nonnegative tree sums bound the exact connected-polymer deletion deviation; they do not replace joint moments when computing coefficients.

Let eta=log2 R, r=2-eta>1, kappa=rho/(1+rho). For the proposed witness, the contribution x_f to each root product is exactly
    x_f = beta p_f^2 R^{L_f} (R/2)^{s_f} A^{s_f-1}(1-kappa p_f)^{s_f-1}.
Since R A<=2, s_f>=2 and R^{L_f}<=R p_f^{-eta},
    x_f <= C p_f^r (1-kappa p_f),  C=beta R^3 A/4.
By (1), C(1-kappa)<=rho. Let F(x)=x^r(1-kappa x), h(x)=log(1+C F(x)), x in [0,1]. Observe that
    x F'(x)/F(x)=r-kappa x/(1-kappa x)>=r-rho.
Also r-1=log2(2/R)>=2(2-R)/(2+R)>=2rho.
Indeed for 0<z<=1, -ln z>=2(1-z)/(1+z) by differentiating the difference, and ln2<1; use z=R/2. Hence xF'/F>=1+rho. F is increasing, and y=C F(x)<=C(1-kappa)<=rho. Therefore
    x h'(x)>= y(1+rho)/(1+y)>=y>=log(1+y)=h(x).
It follows that h(x)/x is increasing on (0,1], so h(x)<=x h(1)<=x log(1+rho). The root product is bounded by (1+rho)^{sum p_h}<=1+rho. Excluding parent f reduces the available sum to <=1-p_f; convexity of z->(1+rho)^z on [0,1] gives
    product_{h!=f}(1+x_h)<=(1+rho)^{1-p_f}<=1+rho(1-p_f)=Y_{B|f}.
This proves both conditions simultaneously. No independence among ports of a group is assumed. The R828 deletion theorem now implies nonvanishing on |t|<=R for every factor subset U and deviation <=rho for every group deletion. Its normalized logarithm satisfies |log P(t)|<=g rho/(1-rho), with Cauchy tail
    E_k<=g rho/[(1-rho)(R-1)] R^{-k}.

## 3. Sharpness of this witness template

If R A>2, choose a fixed small positive rational p with R A(1-kappa p)>2, a single factor of arbitrarily large arity s, activity a=beta p^2 and all indicators 1 (lambda=1). This input meets the promised M<=sqrt(beta), and the root contribution x grows geometrically with s, violating the template's root condition. If beta is irrational, approximate the activity from below with rational values retaining the strict growth inequality. This demonstrates failure of the proposed template, not of the best possible oriented witness (a lone factor could be handled exactly).

If beta R^3/[4(1-rho)]>rho, choose two factors of arity 2 sharing both groups, all indicators 1, p_1=1-e, p_2=e, a_i=beta p_i^2 with rational e>0 sufficiently small. L_1=1 and its root contribution is beta(1-e)^2 R^3[1+rho e]/[4(1-rho)], which tends to a number greater than rho. The root test fails even without the second factor. Strict violation permits rational approximations for irrational beta. Thus (1) is necessary for universal validity of the stated template. For fixed R, rho<=rho_R=(2-R)/(2+R)<1/3 and rho(1-rho) increases on [0,1/3]; setting rho=rho_R maximizes beta=4rho(1-rho)/R^3 and yields (2). B_or strictly decreases on (1,2), with limit 8/9 at 1. Compare R829 B_full(R)=2(2-R)/[R^2(2+R)]: B_or/B_full=4/(2+R)=1+rho_R>1.

## 4. Explicit separation and algorithmic gain

At beta=9/16, R=9/8, rho=7/25, choose one pair factor (p=99/100) and one arity-64 factor (p=1/100) sharing the two pair groups, the other 62 groups touching only the high-arity factor. All indicators may be 1 and coefficients rational, chosen to realize a=beta p^2. The R829 full group test fails at a shared group (strong pair contribution alone >rho). The new oriented witness passes at every group, even though the hyperedge arity is 64; the general theorem allows unbounded arity. This is an auxiliary envelope separation, not a native Port construction. Seven rational parameter tuples are in the replay below, including M<=0.942, R=4097/4096. The fixed M=3/4 certificate changes R from 21/20 to 9/8. With g=10000 and target log-tail 0.01, the exact minimum sufficient truncation degrees for the stated tail formulas are 329 and 127, respectively. No empirical runtime gain asserted.

The R825 Kraft queue enumerates all connected support sets of cost <=k in g*2^{O(k)} poly(N,k). For each support and its subsets, use exact original pinned joint moments for the formal logarithm and support Mobius extraction; disconnected support cancels by factorization and cost beyond k cannot occur. The new witness is analytical only: costs and original signed coefficients are unchanged. With fixed R>1, rho<1, k=O(log((g+1)/epsilon)); the same input, oracle, bit-complexity and certified scalar recovery hypotheses yield deterministic FPTAS. No numerical square-root evaluation required on promised inputs; choose L as least nonnegative integer with 2^{2L}a_f>=beta. For general explicit rational p witnesses the products are rational and directly checkable.

## 5. Exact reproducible validation

Executed the following JavaScript BigInt arithmetic in the current research run. {"stats":{"parameter":7,"arity":114576,"root":16562,"directed":55601,"separation":4,"cutoff":4},"old":329,"current":127,"total":186754}. Checks seven rational parameter tuples; all n/D with 1<=n<=D<=32 and arities 2..32; ordered positive resource tuples of at most four entries with sum<=1 and common denominator <=12, every root and every parent exclusion; a mixed arity-2/64 separation; and both cutoff minimalities. The finite arithmetic checks validate the stated certificate inequalities on these domains. The general theorem rests on the analytic proof, not a finite root search or native dynamics.

```javascript
function verify(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
 const F=(n,d=1n)=>{const g=gcd(n,d);return [n/g,d/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k));
 const le=(a,b)=>a[0]*b[1]<=b[0]*a[1];
 const one=F(1n),two=F(2n);
 const params=[[1,2,23,20],[9,16,9,8],[81,100,51,50],[2209,2500,1001,1000],[221841,250000,4097,4096],[1,8,3,2],[1,25,7,4]];
 const stats={parameter:0,arity:0,root:0,directed:0,separation:0,cutoff:0};
 function ck(x,k){if(!x)throw Error(k);stats[k]++}
 function L(p){let l=0;while((p[0]<<BigInt(l))<p[1])l++;return l}
 function term(beta,R,rho,p,s,oriented=true){
   const Y=oriented?add(one,mul(rho,sub(one,p))):add(one,rho);
   return mul(mul(mul(beta,pow(p,2)),pow(div(R,two),s)),mul(pow(R,L(p)),pow(div(Y,sub(one,rho)),s-1)));
 }
 for(const [bn,bd,rn,rd] of params){
   const beta=F(BigInt(bn),BigInt(bd)),R=F(BigInt(rn),BigInt(rd)),rho=div(sub(two,R),add(two,R));
   ck(le(beta,div(mul(two,mul(rho,add(one,rho))),pow(R,2))),"parameter");
   for(let D=1;D<=32;D++)for(let n=1;n<=D;n++){
     const p=F(BigInt(n),BigInt(D)),t2=term(beta,R,rho,p,2);
     for(let s=2;s<=32;s++)ck(le(term(beta,R,rho,p,s),t2),"arity");
   }
   for(let D=1;D<=12;D++){
     const ts=[one],ps=[F(0n)];for(let n=1;n<=D;n++){ps[n]=F(BigInt(n),BigInt(D));ts[n]=add(one,term(beta,R,rho,ps[n],2));}
     function visit(rem,arr,product){
       if(arr.length){
         ck(le(product,add(one,rho)),"root");
         for(const n of arr)ck(le(div(product,ts[n]),add(one,mul(rho,sub(one,ps[n])))),"directed");
       }
       if(arr.length===4)return;
       for(let n=1;n<=rem;n++)visit(rem-n,[...arr,n],mul(product,ts[n]));
     }
     visit(D,[],one);
   }
 }
 const beta=F(9n,16n),R=F(9n,8n),rho=F(7n,25n),p=F(99n,100n),q=F(1n,100n);
 const t=term(beta,R,rho,p,2),v=term(beta,R,rho,q,64);
 ck(!le(term(beta,R,rho,p,2,false),rho),"separation");
 ck(le(mul(add(one,t),add(one,v)),add(one,rho)),"separation");
 ck(le(add(one,t),add(one,mul(rho,sub(one,q)))),"separation");
 ck(le(add(one,v),add(one,mul(rho,sub(one,p)))),"separation");
 const g=F(10000n),eps=F(1n,100n);
 function cutoff(R,rho){
   const C=div(mul(g,rho),mul(sub(one,rho),sub(R,one)));
   let k=0;while(!le(C,mul(eps,pow(R,k))))k++;
   ck(le(C,mul(eps,pow(R,k))),"cutoff");ck(k===0||!le(C,mul(eps,pow(R,k-1))),"cutoff");
   return k;
 }
 const old=cutoff(F(21n,20n),F(19n,61n)),current=cutoff(R,rho);
 return {stats,old,current,total:Object.values(stats).reduce((a,b)=>a+b,0)};
}
console.log(verify());
```

## 6. Next question

The linear parent-exclusion witness is now sharply classified. Do not repeat its universal parameter optimization. Study factor-specific or nonlinear oriented witnesses exploiting the actual remaining children rather than just the remaining total p-mass, and whether adaptive block radii can improve the 8/9 limiting beta or radius at moderate load. In parallel, check actual fixed-charge road-matrix realizability and weak-bias moment bounds; general complete Port FPTAS and native attribution remain open.
