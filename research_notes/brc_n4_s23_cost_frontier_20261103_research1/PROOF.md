# BRC N=4 / S23: finite-budget exact pricing frontier for the repaired scalar versus full-source sampling

Date: 2026-11-03. Status: AUTHOR_EXACT_FINITE_CERTIFICATE / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: PR #1765@efb0044b414b80704aeb4ad3b4d2b171475161b9, research_notes/brc_n4_s23_scalar_sampling_blackwell_20261103_research1/PROOF.md.

## Experiment and observer scope
Fix S23 scheme (3,31), delete source row 0 in the two overwrite views, retain a full labeled E-row-1 sample T and a Bernoulli E-row-0 event-2 repair sample B. Original observation is excluded. The lawful two-state witness has z2=1, z5^±=1/2 ± 21h, z6^±=1/2 ∓ 19h; all other coordinates 1/2. Set h=1/42, beta_E=1/2, beta_N=0, s=(1-beta_E)^2=1/4, p=1/2+h=11/21, q=1/2-h=10/21. Both states are legal and their nine-coordinate infinity distance is 1. Their future-operator/source/stopping-branch provenance is preserved.

The full retained-row ternary sufficient-statistic T has laws (+,0,-):
  P_+=(sp,1-s,sq), P_-=(sq,1-s,sp).
The repaired indicator B has laws (1,0):
  P_+=(sp,1-sp), P_-=(sq,1-sq).
The two erasure stopping outcomes in T are aggregated ONLY because their conditional split is sign-independent for this fixed pair and terminal binary test. The ternary and binary reductions do not establish sufficiency for all [0,1]^9 or new interventions.

Samples are independent given the state. Each T costs 7/4 and each B costs 1 abstract unit (stipulated, not externally measured). An allocation has nonnegative integers f full and r scalar trials. Equal-prior Bayes hypothesis-testing error is optimized over fixed nonadaptive allocations; no sequential stopping/other source rows/estimator for all nine parameters is included.

## Exact finite theorem
For integer 0<=n<=56 let E_n=min{e(f,r):7f+4r<=n}, budget L=n/4, where e is the exact equal-prior error below. All optimal integer pairs, including ties, and exact rational E_n appear in COST_FRONTIER.tsv (59 data rows for 57 budgets; two budgets are tied).

In particular:
- Budget L=7: unique optimum (f,r)=(1,5), exact e=328039051/682795008.
- Budget L=11: unique optimum (f,r)=(0,11), exact e=698447749741624227953/1469170321634239709184.
- Budget L=14: unique optimum (f,r)=(1,12), exact e=90726161986642043016697/191971588693540655333376.
- L=7/4 has two tied optima (0,1) and (1,0), e=83/168; L=11/4 has two tied optima (0,2) and (1,1), e=47/96.

Strict certified differences:
  e(0,7)-e(1,5)=50769489581/59018069311488 > 0;
  e(4,4)-e(0,11)=368056034177868079/1469170321634239709184 > 0;
  e(0,14)-e(1,12)=10806609854872949405567/82931726315609563104018432 > 0.
At L=11 the (4,4) allocation is the closest competitor among all maximal-r choices; all other allocations are checked exactly.

Thus the sequence of exact optimal designs at budgets 7, 11 and 14 is mixed, all-scalar, mixed, despite equal local Fisher information per stipulated cost at h=0. The precise statement is finite-grid and pair-specific, not an all-budgets or nine-state sampling theorem.

## Proof / reproducible exact certificate
The predecessor's exact likelihood-overlap identity, with binomial C(a,b), is

  e(f,r) = (1/2) Σ_{k=0}^f Σ_{t=0}^k Σ_{u=0}^r
    C(f,k) C(k,t) C(r,u) (1-s)^(f-k) s^k
    min{p^t q^(k-t) (sp)^u (1-sp)^(r-u),
        q^t p^(k-t) (sq)^u (1-sq)^(r-u)}.

Here k is the number of unerased T trials, t its + signs and u the positive B trials. Each term is half the minimum of the two joint cell probabilities. Summing produces the optimum equal-prior likelihood test error for every nonnegative f,r.

Adding an independent observation cannot worsen optimal Bayes error, because a test can ignore it. For fixed f and budget quarter index n, a minimum therefore exists with r=floor((n-7f)/4). To establish UNIQUE and ALL tied optima without assuming strict monotonicity, the attached program checks *every* feasible pair, including smaller r and budget slack.

The executable VERIFY.py evaluates the formula as exact Python Fraction arithmetic for EVERY integer n=0..56 and EVERY f,r with 7f+4r<=n, writes ALL winners to COST_FRONTIER.tsv, and asserts the above exact values/differences. At n=56 there are 69 distinct feasible allocation pairs. A separate direct implementation enumerates each ordered T outcome in {+,0,-}^f and B outcome in {1,0}^r; it multiplies its two separate hypothesis probabilities and sums half their minimum. Direct and grouped evaluations coincide for ALL 45 distinct allocation pairs with total cost<=11. This is an exhaustive finite rational certificate for the declared grid, not a universal statement about arbitrary real budgets.

At budget 7 the exact maximal-r candidate values in f=0,1,2,3,4 order are:
  (0,7) 28405152901817/59018069311488
  (1,5) 328039051/682795008
  (2,3) 4024178113/8364238848
  (3,1) 2290781/4741632
  (4,0) 2290781/4741632.
At budget 11 the exact maximal-r candidates in f=0,...,6 order are:
  (0,11) 698447749741624227953/1469170321634239709184
  (1,9) 794551989016538099/1665725988247437312
  (2,7) 198792565915194953/416431497061859328
  (3,5) 112495678891231/236072277245952
  (4,4) 112288572819421/236072277245952
  (5,2) 28123990891237/59018069311488
  (6,0) 5334982963/11152318464.
L=14 has nine maximal-r candidates; their exact values are in RUN_EVIDENCE.txt. All exact comparisons use rational cross-multiplication.

## Fisher threshold / next scientific question
For this pair and s=1/4, the previously proved local Fisher informations are I_T(0)=4s=1 and I_B(0)=4s/(2-s)=4/7, giving I_T/c_T=I_B/c_B=4/7. This equality is a LOCAL differential criterion, whereas the exact finite-budget designs depend on likelihood shape, discrete cost constraints, and optimal finite-sample decision regions. The reported switches are precise new finite counterexamples to inferring an allocation from that local equality alone.

This model maintains the BRC source branch/observer provenance and excludes any claimed native X6/time interpretation; P000 is unchanged. The full S23 ten-label minimax [1/2,2/3] remains a distinct open parent target. Program result: PASS_BRC_S23_FINITE_BUDGET_EXACT_FRONTIER_20261103; 57 budgets, 69 feasible pairs at max budget, 45 independent ordered-sequence crosschecks. Mathematical status AUTHOR_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

Next: identify an analytic switching law for arbitrary budgets h,s, or a counterexample to eventual cost-normalized dominance; separately test new z2 interventions against the entire nine-parameter map with operator costs.