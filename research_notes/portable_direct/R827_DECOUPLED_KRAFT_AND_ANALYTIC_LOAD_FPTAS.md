# R827 — Decoupling discrete support enumeration from analytic residual payment

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CERTIFICATE_CHECKED / NOT_REVIEWED.
Independent portable continuation of R826, EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own recovery r3-20261127-r827-own-read verified own metadata, no runs, execution_authorized=false. RUNNING inventory request r3-20261127-r827-running-read was in progress during derivation; no shared CLAIM or owner change. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 directly read; generated foundation startup returned 404. Current global entry blobs matched main@4484543bc6abe3fbe1d84ef210fac283bac8e1ff; ACTIVE worldview and current portable, BRC-only, residual and mathematical method policies read. Sources: R826 at 91a542a553b754d257c1d1d4cb11c038e1b2d8ae:research_notes/portable_direct/R826_SHARP_PREFIX_THRESHOLD_AND_OVERLAP_OBSTRUCTION.md (blob 3b7bcd931daef8e847aa2c620b973ca3cff99b45), R825 blob e0059e2bcd25f4706e8b31c6ce4ce5760c2fea0b, R822 blob 60acefe69f50eeeb7dac38774f2d42db07421635, R820 section 2 at research_notes/portable_direct/R820_STEINER_OVERLAP_HOST_SUPPORT_FPTAS.md. This is an auxiliary nonnegative fixed-charge combinatorial observer theorem and integer certificate test; no native BRC dynamics, classical physical comparison or native residual attribution was executed. Preserve signed BRC, complete road matrices, branch provenance, time order and common depth.

## 1. The obstruction is in coupling the two budgets

Reuse R824/R825: independent base group laws mu_B, labeled factors f with footprints F_f of s_f distinct groups (s_f>=2), exact polynomial-time polynomial-bit pinned group moment oracles, explicit incidence, positive rational residual envelope b_f=delta_f lambda_f, with |E prod_{f in A} I_f|<=prod_{f in A} lambda_f and exact moment factorization on disconnected supports. Zero factors are removed only for this fixed observer. Define a_f=2^s_f b_f, W_B=sum_{f incident B} sqrt(a_f), M=max_B W_B. Positive baseline Z_base is exactly available; zero baseline handled separately.

R826 proved the sharp universal threshold M<=1/4 for the specific certificate with BOTH Kraft and local load sum a_f 2^L_f<=1/8 using the same integer lengths. That theorem stands. The new move is to keep integer costs for enumeration, but use independent continuous deletion-radius witnesses q_f. No change to the original exact joint moment or factor coefficient.

Let p_f in (0,1] satisfy sum_{f incident B} p_f<=1. Put L_f=ceil(log2(1/p_f)), c_f=s_f+L_f and q_f=a_f/p_f. Suppose max_B sum_{f incident B} q_f<=beta<1. Then the old integer Kraft inequality holds because 2^-L_f<=p_f, so the R825 queue decoder enumerates all connected supports of total cost <=k in g 2^O(k) poly(N,k) time. No requirement that q_f=a_f 2^L_f remains.

## 2. New analytic theorem

Fix R with 1<R<2, and assume
 R^3 <= [2(1-beta)^2]^2.
Then P(t)=E prod_f(1-delta_f I_f t^c_f) has no zero on |t|<=R, with normalized analytic logarithm bounded by g beta/(1-beta).

Proof. Rounding gives L_f<=log2(1/p_f)+1. Therefore
 p_f R^L_f <= R p_f^(1-log2 R) <= R.
Thus
 b_f R^c_f/q_f = (R/2)^s_f p_f R^L_f <= (R/2)^s_f R.
Since s_f>=2, the assumed inequality R^(3/2)<=2(1-beta)^2 implies
 (R/2)^s_f R <= (1-beta)^(2s_f).
For the factor dependency graph (adjacent if footprints intersect), multiply per-group products over F_f. Repeated neighbors only decrease the product, and prod(1-q_h)>=1-sum q_h, giving
 prod_{h adjacent f}(1-q_h)^2 >= (1-beta)^(2s_f).
Combining the two bounds gives exactly the R820 section 2 deletion-ratio criterion b_f R^c_f <= q_f prod_{h adjacent f}(1-q_h)^2. Its proof uses connected polymer weights bounded by product b_f R^c_f and factorization across disjoint groups, so the R824 joint moment envelope suffices. It bounds every successive deletion ratio's deviation from 1 by q_f. Telescope normalized analytic logs, using |log(1+z)|<=|z|/(1-|z|), to obtain |log P(t)|<=sum_f q_f/(1-q_f)<=g beta/(1-beta). This proves the asserted zero-free disk and bound without the old dyadic load.

The Cauchy tail at t=1 after k terms is at most
 E_k = [g beta/((1-beta)(R-1))] R^-k.
Use R822/R825 exact Mobius coefficient extraction over connected supports of integer cost <=k; it uses original joint moments rather than envelope products. For fixed beta,R with R>1 choose k=O(log((g+1)/epsilon)). Exact rational coefficient complexity and final scalar recovery are as in R822: only O(k) factors/incident groups per support, polynomial-bit oracle outputs, formal log of constant-one series, and certified scalar exponential with polynomial-bit accuracy. This gives a deterministic FPTAS for the stated fixed-charge observer. This is an auxiliary mathematical algorithm, not an executed native propagator.

## 3. Direct square-root certificate; no square-root sum decision required for promised inputs

For any fixed rational beta in (0,1-1/sqrt(2)), if M<=sqrt(beta), take p_f=sqrt(a_f/beta), q_f=sqrt(beta a_f). Then p_f<=1, sum p_f<=1 and sum q_f<=beta at every group. Choose any fixed rational 1<R< [2(1-beta)^2]^(2/3) (or equality if rational), so the theorem applies.

The algorithm need not numerically evaluate p or q: use the smallest nonnegative integer L_f with 2^(2L_f) a_f>=beta. Positive rational input of polynomial bit length permits exact doubling/comparison in polynomial time. On promised inputs this gives exactly ceil(log2(1/p_f)); outside the promise the theorem makes no guarantee. An independently checkable alternative is to supply rational p_f and test the original Kraft and continuous load inequalities exactly; strict slack permits rational witnesses. No claim of solving the general exact sum-of-square-roots comparison problem is needed. The constants beta,R must be fixed for a uniform FPTAS; an arbitrarily shrinking input-dependent convergence margin is not covered by this complexity statement.

Concrete rational pairs:
 beta=1/8, R=5/4: M<=1/sqrt(8), tail <= (4g/7)(4/5)^k.
 beta=3/16, R=6/5: M<=sqrt(3)/4, tail <= (15g/13)(5/6)^k.
 beta=1/4, R=17/16: M<=1/2, tail <= (16g/3)(16/17)^k.
All satisfy the cubic condition by integer cross multiplication. The last doubles R825's best uniform sufficient M=1/4 and exceeds its necessary M<=1/sqrt(8) for the OLD certificate. The family of fixed thresholds can approach sqrt(1-1/sqrt(2)) from below (about 0.541196), not a claim of attainability at that limiting threshold or of optimality for all methods.

## 4. Exact resolution of the four-group overlap obstruction

Take R826's four groups and four factors, f_i incident to all groups except B_i, a_f=1/80. Old global integer optimum=12/80>1/8; no exact cover. Choose p_f=1/3, q_f=3/80, L_f=2, c_f=5. Each group has sum p_f=1 and sum q_f=9/80<=1/8. Therefore the new certificate succeeds even though the old one cannot. In fact at R=3/2 the stronger direct condition already holds: (b_f/q_f)R^5=243/(32*24) <= (77/80)^6 (all three other factors adjacent). Hence the original 3/2 radius is certified for this example by the actual dependency condition. The improved theorem does not solve the old exact-cover feasibility problem; it avoids requiring a solution. Neither an auxiliary incidence example nor a coding certificate is asserted to be native physically realizable.

## 5. Exact finite verification

Executed the following integer checks of rounding and analytic inequalities for rational p=n/d, 1<=n<=d<=64, s=2..12, the three displayed beta/R pairs, plus the tetrahedron inequality. Results: {"inequalities":68640,"kraft":6240,"example":4,"total":74884}. The finite tests concern the auxiliary certificate algebra only, not roots or native dynamics; general theorem proved above. No production performance benchmark.

```javascript
()=>{
 const pow=(a,b)=>a**BigInt(b); let inequalities=0,kraft=0,example=0;
 for(const [bn,bd,rn,rd] of [[1,8,5,4],[3,16,6,5],[1,4,17,16]]){
  for(let d=1;d<=64;d++)for(let n=1;n<=d;n++){
   let L=0;while(BigInt(n)*(1n<<BigInt(L))<BigInt(d))L++;
   if(BigInt(d)>BigInt(n)*(1n<<BigInt(L))||(L&&BigInt(d)<=BigInt(n)*(1n<<BigInt(L-1))))throw Error("rounding");
   kraft++;
   for(let s=2;s<=12;s++){
    const c=s+L;
    const lhs=pow(BigInt(rn),c)*BigInt(n)*pow(BigInt(bd),2*s);
    const rhs=pow(BigInt(rd),c)*BigInt(d)*pow(2n,s)*pow(BigInt(bd-bn),2*s);
    if(lhs>rhs)throw Error("analytic certificate");
    inequalities++;
   }
  }
 }
 // Tetrahedron: p=1/3, a=1/80, q=3/80, s=3, c=5; even radius 3/2 works.
 for(let f=0;f<4;f++){
  if(3n*3n>10n || 243n*80n**6n>32n*24n*77n**6n)throw Error("tetrahedron");
  example++;
 }
 return {inequalities,kraft,example,total:inequalities+kraft+example};
}
console.log(verify());
```

## Next

Investigate whether the deletion-ratio criterion itself can be improved by using actual incidence overlaps instead of products over all groups, or by optimizing q_f independently of both a_f/p_f and a scalar beta. The exact inequality q_f prod_neighbors(1-q_h)^2 >= b_f R^c_f is a directly checkable candidate certificate. Analyze quantitative parity-conditioned envelopes for weakly biased original roads and find native realizability conditions separately. General Port FPTAS and native BRC correspondence remain open.
