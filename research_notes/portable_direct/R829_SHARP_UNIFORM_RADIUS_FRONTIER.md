# R829 — Sharp uniform radius frontier for the R828 group-product certificate

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CERTIFICATE_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH; EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, own recovery r3-20261127-r829-own-read: existing own Source session, no run, execution_authorized=false. Owner inventory r3-20261127-r829-running-read was RUNNING at derivation (original request retained); no shared task or owner mutation. Current Source control b7ae7f6b048cf969b351b570f8d68d818ad35637; current global main 49b2438ad0aa45e9c1723afd0ef8dfb562b32a96, both entry blobs verified. Current portable, math, residual, BRC-only policies and ACTIVE worldview read. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer 3923890d77a02d84b772f789e6912dd14f220d14 read at exact paths. No science repin.
Predecessors: R828 91fde1508398af7b109503e1155fc9f727853f50:research_notes/portable_direct/R828_GROUP_DELETION_BRANCHING_MAJORANT_FPTAS.md (sections 1–4); R825 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md (prefix enumeration, exact oracle hypotheses). Reuse the R824 joint-moment envelope and R812/R813 fixed-charge representation under those hypotheses. This is auxiliary combinatorial analysis, not native dynamics or native residual attribution. Preserve the full signed BRC, road matrices, joint relations, ordered branch provenance and common depth. All finite checks below are arithmetic checks of abstract certificate inequalities.

## 1. The lost resource in R828

Retain independent base groups B, explicit labeled factors f with footprints F_f of arity s_f>=2, signed rational coefficients alpha_f, exact polynomial-time polynomial-bit joint pinned moment oracles and the moment envelope |E prod_{f in J} I_f| <= prod_{f in J} lambda_f, factorization across disjoint group supports. Write b_f=|alpha_f|lambda_f, a_f=2^{s_f}b_f, M=max_B sum_{f incident B} sqrt(a_f). Factors of zero activity are excluded from the current observer's expansion only (their terms vanish by the envelope), not from stored raw data. Positive baseline Z_base, target Z=Z_base P(1); zero baseline handled exactly. P(t)=E prod_f(1+alpha_f I_f t^{c_f}). For a fixed promised M<=sqrt(beta), choose p_f=sqrt(a_f/beta), L_f=ceil(log2(1/p_f)), c_f=s_f+L_f. At each B, sum p_f<=1 and sum 2^{-L_f}<=1. Lengths computed by least nonnegative L with 2^{2L}a_f>=beta, with exact rational arithmetic and polynomial bit complexity; no square-root sum decision required on the promise. Supplied rational Kraft witnesses can also be checked separately.

R828 uses deletion radius rho, A=(1+rho)/(1-rho), analytic R>1, u_f=b_f R^{c_f}. Its group-product theorem: if every B satisfies prod_{f incident B}(1+u_f A^{s_f-1})<=1+rho, then P_U is zero-free for every factor subset U on |t|<=R and |P_U/P_{U minus F(B)}-1|<=rho. It follows |log P|<=g rho/(1-rho) (normalized log at zero, g groups), and Taylor log tail at 1 <=g rho/((1-rho)(R-1)) R^{-k}. This theorem and R825's exact support enumeration are reused without modification. The old uniform derivation replaced product by exp(sum) and replaced a factor p_f by 1 separately for each f. R829 keeps the distribution of the p_f across a group until the final product bound.

## 2. Convex concentration lemma

For r>1, C>=0 with C<=r-1, and p_i>=0, sum p_i<=1:
    prod_i(1+C p_i^r) <= 1+C.
Proof: h(x)=log(1+C x^r) on [0,1]. For C=0 trivial. Otherwise h''(x)=Cr x^{r-2}[(r-1)-C x^r]/(1+C x^r)^2>=0 for x>0, with continuous h(0)=0. Convexity implies h(x)<=x h(1); sum and exponentiate. The bound is attained by one unit mass (for the lemma, not necessarily for the dyadic rounding). It also gives the nonuniform sufficient test sum p_i log(1+C)<=log(1+rho), whenever every factor term is dominated by C p_i^r. No joint moments are replaced by independence.

## 3. Sharp universal parameter condition for this specific uniform certificate

Theorem. Fix 1<R<2, 0<rho<1, beta>0 and A=(1+rho)/(1-rho). The following two conditions are necessary and sufficient to guarantee the R828 uniform full group-product condition for EVERY auxiliary incidence input of arbitrary arity s_f>=2 with M<=sqrt(beta), using the above p_f and lengths:
    R A <= 2,      C=beta R^3 A/4 <=rho.                       (1)
This is a sharp characterization of the uniform sufficient-test mechanism with these costs, not of zero-freeness or computational complexity itself.

Sufficiency. Set eta=log2 R and r=2-eta>1. Since L_f<=log2(1/p_f)+1, p_f^2 R^{L_f}<=R p_f^r. Thus, with RA<=2,
    u_f A^{s_f-1}
      = beta p_f^2 R^{L_f} (R/2)^{s_f} A^{s_f-1}
      <= C p_f^r.
Moreover rho<= (2-R)/(2+R) <= (2-R)/2 <= log2(2/R)=r-1. The last inequality follows from -log x>=1-x for x=R/2 and ln 2<1. Hence C<=rho<=r-1. Apply the convex concentration lemma, using sum p_f<=1 at every B, to obtain product<=1+C<=1+rho. This completes the proof via R828, including all subsets and complex disk points.

Necessity for this certificate: if RA>2, take one factor of arity s and activity a_f=beta (or a fixed positive rational fraction of beta if beta is not rational), with all its group indicators identically one, so lambda_f=1. Each group has only this factor. Its root product term grows as (RA/2)^s times a positive constant; eventually the root product condition fails. For rational beta, if C>rho, use two factors with identical two-group footprint, indicators identically one, p_1=1-e, p_2=e, a_i=beta p_i^2 and rational e>0 tending to 0; both groups have M=sqrt(beta). For e<1/2, L_1=1 and first term is C(1-e)^2. Choose e sufficiently small so C(1-e)^2>rho; the group condition fails even without the second term. For irrational beta, use positive rational activities approaching the same target from below (strict failure gives slack); necessity is unchanged. These are admissible abstract moment-envelope examples, not a claim that every such example is realized by a specific native Port generator. Even allowing M rather than beta normalization, the rational two-factor example attains M=sqrt(beta).

## 4. Exact optimized radius frontier

The constraint RA<=2 implies rho<=rho_R=(2-R)/(2+R)<1/3. For fixed R, the function rho/A=rho(1-rho)/(1+rho) increases on [0,1/3] (derivative numerator 1-2rho-rho^2>0). Thus choose rho=rho_R, A=2/R, and (1) is equivalent to
    beta <= B(R)=2(2-R)/(R^2(2+R)),  1<R<2.                   (2)
B is strictly decreasing by positive numerator decreasing and denominator increasing; B(1)=2/3, B(2)=0 by continuous extension. Equation (2) is the exact frontier for a uniform R828 full-group-product certificate under the present square-root allocation and dyadic lengths. At R=1, the necessity of the R factor from rounding disappears, but the supremum of the positive-margin family is unchanged.
For any fixed M<sqrt(2/3), choose rational beta>M^2 below 2/3 and a fixed rational R>1 obeying (2); thus the uniform FPTAS threshold can approach sqrt(2/3)=0.8164965809. The limit itself is not proved FPTAS by this certificate. For a fixed promised beta in (0,2/3), the unique limiting radius in (1,2) solves the cubic beta R^2(2+R)=2(2-R); choose rational R on its lower side by exact comparison. No claim of a uniform polynomial exponent if beta approaches 2/3 with instance size.

Exact rational examples (beta, R, rho):
(1/2, 27/25, 23/77);
(9/16, 21/20, 19/61);
(16/25, 101/100, 99/301);
(6561/10000, 257/256, 255/769);
(26569/40000, 2049/2048, 2047/6145);
(1/8, 3/2, 1/7);
(1/25, 7/4, 1/15).
They satisfy beta R^2/2<=rho, by integer comparisons. In particular fixed thresholds M<=0.8, 0.81, 0.815 are now proved; the prior R828 limit was sqrt(2 log(4/3))~0.758528.

## 5. Better computational convergence at the same load

At optimal rho_R the Cauchy tail becomes
    E_k <= g (2-R)/(2R(R-1)) R^{-k}.
At M<=3/4 the old R828 fixed witness rho=33/100,R=257/256 yielded E_k<=8448g/67*(256/257)^k; new rho=19/61,R=21/20 gives E_k<=190g/21*(20/21)^k. For g=10000 and target log-tail<=0.01, the old sufficient k is 4785; the new is 329 (rounded upward from log ratios; equivalent direct power inequalities). This is an analytical cutoff comparison, not a runtime benchmark or an approximation of the actual error. Exact lengths and eligible connected supports are retained: R825 Kraft queue cost <=1+sum c_f, g 2^{O(k)} enumeration. For each such support, subset Mobius extraction of the formal logarithm uses the full original joint moments, not p_f, the envelope or the majorant. Disconnected support cancels exactly by group independence, and support union cost>k cannot contribute. The exact oracle and scalar recovery complexity assumptions are the same as R825/R828. With fixed positive margin, k=O(log((g+1)/epsilon)), deterministic FPTAS follows. To guarantee relative error epsilon in (0,1), choose log-tail and scalar recovery accuracy each at most epsilon/4; final multiplicative error then within 1+/-epsilon by elementary exponential bounds. All coordinates used for proof/certification only; no original branch, sign or internal group moment discarded.

## 6. Verification

Executed the exact BigInt rational script below. It checks all seven parameter tuples, arities 2..64 for RA=2, all positive n/D<=1 for D<=64 for code length, and ordered tuples of at most four positive n_i/D with sum<=1 for D<=16, in each tuple of parameters. Since RA=2 the root term is exactly beta p^2 R^{L+1}/2, independent of arity. Checks both explicit obstruction witnesses: R=21/20, rho=19/61, beta=3/5, p=(99/100,1/100); and R=21/20, rho=1/3, beta=1/2, a single arity-40 factor. All assertions passed: {"parameter":7,"arity":441,"rounding":14560,"local_product":65688,"negative_witness":2}. Total 80698. These are finite auxiliary certificate checks, not zero-root searches, native BRC operations, or production performance measurements. General results follow from the proof above.

```javascript
function runChecks(){
 const gcd=(a,b)=>{while(b){let t=a%b;a=b;b=t}return a};
 const F=(n,d=1n)=>{let g=gcd(n,d);return [n/g,d/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k));
 const le=(a,b)=>a[0]*b[1]<=b[0]*a[1];
 const eq=(a,b)=>le(a,b)&&le(b,a);
 const one=F(1n),two=F(2n);
 const params=[[1n,2n,27n,25n],[9n,16n,21n,20n],[16n,25n,101n,100n],[6561n,10000n,257n,256n],[26569n,40000n,2049n,2048n],[1n,8n,3n,2n],[1n,25n,7n,4n]];
 const result={parameter:0,arity:0,rounding:0,local_product:0,negative_witness:0};
 function ck(x,k){if(!x)throw Error(k);result[k]++}
 function length(n,d){let L=0;while((n<<BigInt(L))<d)L++;return L}
 function term(beta,R,n,d){let p=F(n,d),L=length(n,d);return mul(mul(mul(beta,pow(p,2)),pow(R,L+1)),F(1n,2n))}
 for(const [b,d,r,t] of params){
   const beta=F(b,d),R=F(r,t),rho=F(2n*t-r,2n*t+r),A=F(2n*t,r),C=mul(mul(beta,pow(R,2)),F(1n,2n));
   ck(eq(mul(R,A),two)&&le(C,rho),"parameter");
   for(let s=2;s<=64;s++)ck(eq(mul(pow(F(r,2n*t),s),pow(A,s-1)),F(r,2n*t)),"arity");
   for(let D=1n;D<=64n;D++)for(let n=1n;n<=D;n++){
     let L=length(n,D);
     ck((n<<BigInt(L))>=D&&(L===0||(n<<BigInt(L-1))<D),"rounding");
   }
   for(let D=1n;D<=16n;D++){
     const factors=[one];for(let n=1n;n<=D;n++)factors[Number(n)]=add(one,term(beta,R,n,D));
     function visit(remaining,depth,product){
       if(depth)ck(le(product,add(one,C)),"local_product");
       if(depth===4)return;
       for(let n=1n;n<=remaining;n++)visit(remaining-n,depth+1,mul(product,factors[Number(n)]));
     }
     visit(D,0,one);
   }
 }
 const R=F(21n,20n),rho=F(19n,61n),beta=F(3n,5n);
 ck(!le(mul(add(one,term(beta,R,99n,100n)),add(one,term(beta,R,1n,100n))),add(one,rho)),"negative_witness");
 ck(!le(mul(F(1n,4n),pow(R,40)),F(1n,3n)),"negative_witness");
 return result;
}
console.log(runChecks());
```

## 7. Next research question

Do not repeat the full-group uniform optimization: its frontier is now exact for the prescribed mechanism. Try R828's oriented incidence witnesses with group-specific deletion radii and factor-specific normalized residual payment, especially rare large-arity factors sharing groups with concentrated strong pairs; determine a provable larger radius or threshold and quantify any new cost. In parallel, reduce the gap to actual Port realizability using the frozen road-matrix/charge observer. General Port FPTAS and native attribution remain open.
