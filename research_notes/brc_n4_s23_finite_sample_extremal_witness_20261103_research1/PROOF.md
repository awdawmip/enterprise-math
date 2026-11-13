# BRC N=4/S23: exact finite-sample statistical experiment at the sharp inverse witness

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_BIGINT_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: PR #1765, immutable 7e8b9024523f55f3e93a3067b425d6209c9f3a4c (complete-bank inverse for unequal overwrites).

## Setting and precise sampling model

Retain the previous S23 model: z in [0,1]^11; the six source stopping laws R(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)); source triples A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10); prepared-source mixing rows M/20 where M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].

For any F in {(3,31),(7,27),(11,23),(15,19)}, N overwrites 0,1 but not 2 at beta_N, and E overwrites 0,1,2 at beta_E, with any further mask bits as prescribed by F. Retain both views, delete a common source row j in {2,3,4,5}, and retain the minimal repair scalars for that row. The original (un-overwritten) observation is absent. Our statistical design samples independent draws from any chosen labeled source/view's four-outcome distribution; a trial yields exactly one of the four mutually exclusive outcome tags. All samples are conditionally independent given z. The repair probabilities for deleted rows and any extra measurements on those rows are sign-independent in the specific witness below. No correlations between jointly sampled views, adaptive intervention costs, or original-observation samples are assumed.

## Theorem: exact binary-erasure reduction and finite-n minimax

For real 0<=h<=1/42, define two lawful states z^+,z^- by z_2^+=z_2^-=1, all other entries equal 1/2 except
  z_5^+=1/2+21h, z_5^-=1/2-21h;
  z_6^+=1/2-19h, z_6^-=1/2+19h.
Let b=1-beta_E and s=b^2 (0<=beta_E<=1). Put p=1/2+h, q=1/2-h. The target x=z_{2:10} obeys ||x^+-x^-||_infinity=42h.

For each of the four F masks and every beta_N, the N-view distributions and all E rows other than 0 and 1 are identical under +/-; the two informative E rows are
  E row 0: (beta_E,b beta_E,s p,s q) for + and (beta_E,b beta_E,s q,s p) for -;
  E row 1: (beta_E,b beta_E,s q,s p) for + and (beta_E,b beta_E,s p,s q) for -.

A row-0 trial with outcome 2, or row-1 trial with outcome 3, is recoded as success; a row-0 outcome 3 or row-1 outcome 2 as failure; outcomes 0 and 1 as erasure. Under +/- each recoded trial has respectively probability vector (1-s,s p,s q) and (1-s,s q,s p). Its erasure subtag (0 versus 1) has a sign-independent conditional distribution. Thus the original four-outcome experiment and this ternary experiment are exactly statistically equivalent for testing the two states (there are deterministic forward and sign-independent randomized reverse kernels).

For any nonadaptive sample allocation with N total E-row-0/1 draws (any split), and any number of further draws from the other views/rows, the optimal equal-prior testing error equals

  e_N(h,s) = sum_{k=0}^N Binom(N,k) s^k(1-s)^(N-k) e_k(h),

  e_k(h) = sum_{t=0}^k Binom(k,t) min(p^t q^(k-t),q^t p^(k-t))/2
         = P_{B~Binom(k,p)}(B<k/2)+ 1/2 P(B=k/2).

At k=0 set e_0=1/2. Equivalently, conditional on the K~Binom(N,s) non-erased trials, the success count is Binom(K,p) under + and Binom(K,q) under -; the sign of 2T-K is an optimal test, randomizing on a tie.

For the two-state estimation problem with loss ||xhat-x||_infinity and full target x=(z2,...,z10), the exact frequentist minimax *expected* loss over this pair is
  R_N^pair = 42h e_N(h,s).
This does not assert an exact minimax risk over the full nine-parameter cube.

## Proof

Row 0 third-branch parameter is (z5+z6)/2 and row 1 is (9z5+11z6)/20. The witness substitutes to r0^+=1/2+h, r0^-=1/2-h, r1^+=1/2-h, r1^-=1/2+h. The N-view original second gate z2=1 blocks every r branch from groups 0 and 1; every other group uses z7,...,z10 and hence is unchanged. In E, the first two gates of groups 0 and 1 are overwritten to beta_E, giving the four probabilities displayed.

The erasure split has conditional weights beta_E/(1-s) and b beta_E/(1-s), independent of sign (for s=1 no erasures occur). This yields exact experiment equivalence including source and view tags. For independent draws the count of non-erasures K is Binom(N,s), and the conditional likelihood ratio is (p/q)^(2T-K). The Neyman-Pearson/equal-prior likelihood decision gives the displayed exact finite binomial sums. Additional samples from sign-independent rows multiply both likelihoods by the same factor and cannot improve the pair test. Any E-row allocation is equivalent after source-aware recoding.

For any estimator output y and posterior pair weights (lambda,1-lambda), the triangle inequality gives lambda||y-x+|| + (1-lambda)||y-x-|| >= min(lambda,1-lambda)||x+-x-||. Equality is attained by choosing the more likely endpoint. Averaging yields the Bayes risk 42h e_N, and symmetry under swapping success/failure makes the endpoint maximum risk equal to its equal-prior Bayes risk, hence the pair minimax equality.

## Exact affinity and sample-size bounds

The Hellinger/Bhattacharyya *affinity*, not squared Hellinger distance, of one informative E-row trial is
  c = (1-s) + s*sqrt(1-4h^2).
For N independent useful trials, rho_N=c^N. For 0<h<=1/42 and s>0:

  [1-sqrt(1-c^(2N))]/2 <= e_N(h,s) <= c^N/2.

The upper bound follows from min(P,Q)<=sqrt(PQ); the lower bound from TV(P,Q)<=sqrt(1-rho_N^2). Therefore, for any 0<alpha<1/2, sufficient and necessary respective bounds on N for testing error <=alpha are

  N >= log(2alpha)/log(c)                 (sufficient),
  N >= log(4alpha(1-alpha))/(2 log(c))  (necessary).

Both quantities are positive. At h=0 or s=0, e_N=1/2 for all N. At fixed s>0, the small-h Chernoff exponent obeys -log(c)=2s h^2+O(h^4); fixed-confidence sample counts scale as 1/(s h^2) in this witness. Each E-row trial is counted once: four outcome probabilities from the same trial are not four independent measurements. In terms of the prior event sup-distance D_full=2s h, the surviving-outcome tags offer a branch-aware sample advantage compared with an analysis treating every event probability as a generic independent noisy scalar, although the prior sharp deterministic inverse coefficient remains unchanged.

At h=1/42 and beta_E in {0,1/4,1/2}, the exact finite-n Bayes errors and raw-four-outcome equivalence checks appear in RUN_EVIDENCE.json. The analytic theorem covers every real h,beta_E and every integer N>=0. The finite verifier is additional evidence, not the continuum proof.

## Scope, identity and research frontier

This is a typed statistical-observer calculation based on the preserved S23 stopping branches, source identity, preparation weights, and mask provenance; no physical Heartbeat-time evolution, phase residual or native 6D-to-slice lift is inferred. P000's six primitive axes, typed time, three-dimensional slice and triadic stability remain unchanged. Scientific inputs are frozen; current behavioral rules were read separately. Native Researcher-ID/Owner/CLAIM was not established: service currently reports CONTROL_QUOTA and research_authority_granted=false; this is author-side research only.

The main ten-label decoder minimax remains in the prior [1/2,2/3] bracket. The next precise question is to compute the exact sampling costs for j=0 or1 when the scalar repair is measured as a binary event rather than a full four-outcome row, and compare priced downstream interventions that break this witness.
