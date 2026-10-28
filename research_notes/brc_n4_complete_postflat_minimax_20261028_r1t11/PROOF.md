# BRC N4 — exact common-TV post-flat minimax diagram through λ=1

Research date: 2026-10-28 Asia/Shanghai. Classification: AUTHOR_PROVED / EXACT_FRACTION_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is author-side portable mathematical research, not a native session Result. Authentic GitHub user: awdawmip; native active-owner listing returned CONTROL_QUOTA, so no live owner or CLAIM is asserted.

Frozen GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@30a0b3ec845e08a9d5d2ea2bd179c27735398ee2. Frozen Enterprise Math input: awdawmip/enterprise-math@d2c0c9157cc89f1c08c9db7c321b4c4702278703. Predecessor: research_notes/brc_n4_post_switch_flat_tv_phase_20261028_r1t11/PROOF.md. Original author-side theorem covers λ≤27483/39215.

## Global theorem for remaining parameters

Fix the predecessor's strictly positive, depth-four, two-law P/Q tree and full-history stopping policy F_λ, for real λ∈[0,1]. Let S₂ require equal fresh instantaneous (P,Q,C) decisions only across time-2 histories having the same likelihood ratio P/Q. Let S₂₃ additionally impose the same rule at time 3. There is NO persistent common random seed. Compare both laws' complete eight-coordinate joint distributions of (T,D) by total variation. Let d₂ and d₂₃ be the infimum over the respective class of the maximum of the two TV values.

Put λold=27483/39215, λ*=11526/16445, λ**=89/125. Then for EVERY REAL λ∈[λold,1]:

 d₂(λ)=d₂₃(λ)=
  1/506                         if λold≤λ≤λ*,
  11/22855+39λ/18284            if λ*≤λ≤89/125,
  13λ/228−11/285                if 89/125≤λ≤1.

The boundary equalities hold in exact rational arithmetic. The true first switch is λ*=11526/16445, a distance 27/509795 to the RIGHT of the preceding particular upper-witness feasibility limit. At λ=89/125 the optimum is 1/500 and at λ=1 it is 7/380. The earlier separately established d₃(λ)=(1−λ)/2000 gives d₂+d₃−d₂₃=(1−λ)/2000, strictly positive for λ<1. This theorem is for the specified external model and F_λ family, not an arbitrary full-history F or native X6 dynamics.

## Model, BRC provenance, complete target

At time 1: A=(q,r)=(1/2,1/2), B=(1/2,3/2). At time 2: AU=(1/6,1), AV=(1/3,1/4), BU=(1/4,1), BV=(1/4,2), where q is Q mass and r=P/Q. Each parent has equal-Q-mass children with ratios r(1±epsilon). At time 3 the time-2 parent epsilons AU,AV,BU,BV are (1/10,0,4/5,0); at time 4 they are zero for AV0, 3/50 for AV1 and 1/20 otherwise. The resulting 2,4,8,16 leaf levels each conserve both Q and P mass; all probabilities are strictly positive.

F_λ continues at t1. At t2 it stops P at AU,BV and continues at AV,BU. At t3 AV0 stops Q with probability 1−λ, continues with λ; AV1 and BU0 continue; BU1 stops Q; other histories stop P. At t4 it stops Q if 100r<2501/100, else P. With event order (1P,1Q,2P,2Q,3P,3Q,4P,4Q):

 Q_F=(0,0,5/12,0,0,7/24−λ/6,1/12,5/24+λ/6)
 P_F=(0,0,2/3,0,0,4/15−λ/24,53/2400,107/2400+λ/24).

## Exact causal likelihood-fiber occupancy lemma

For this specific tree, given t1=C, all histories h having the same time-t likelihood ratio r have the SAME upstream survival probability. At t2 the collision AU/BU shares t1; at t3 AV0/AV1 and BV0/BV1 have a common parent; at t4 every collision either shares a parent or has parents with an identical time-3 (t,r) signature. This must be checked for this tree; it is NOT a general Markovian theorem for likelihood quotients.

Let x(t,r,d) be this common survival probability multiplied by the fresh local behavioral probability for d∈{P,Q,C} at t2/t3 and d∈{P,Q} at t4. They obey x≥0, sum_d x(2,r,d)=1, and sum_d x(t,r,d)=x(t−1,r_parent,C). There are 3,6,13 ratio-fibers at times 2,3,4 and 53 scalar occupancy variables. Every point obeying these linear constraints is attained by a genuine legal COMMON behavioral strategy: divide outgoing occupancy by incoming survival when positive, and choose any action on unreachable fibers. No correlated seed is needed. Both full joint law distributions are LINEAR in x:

 Q(t,d)=Σ_r [Σ_(h∈H_t(r)) q_h] x(t,r,d),
 P(t,d)=Σ_r [Σ_(h∈H_t(r)) q_h r] x(t,r,d).

The retained history labels, Q positive mass and P/Q ratios are the BRC carrier; discarding parent-provenance before this fiber check would be invalid.

## Four exact constructive endpoint certificates and real intervals

The companion standalone VERIFY.py includes complete sparse rational occupancy tables x at λold, λ*, 89/125,1. Unspecified coefficients are zero. Each one satisfies all 22 fiber constraints, and reconstructs actual shared (t,r) behavior. Their (TV_Q,TV_P) are respectively:

 λold: (1/506,1/506);
 λ*:   (1/506,1/506);
 89/125:(1/500,1/500);
 1:    (7/380,7/380).

For every real λ between adjacent endpoints a,b, set theta=(λ−a)/(b−a) and xλ=(1−theta)xa+theta xb. Exact flow equalities guarantee a legal shared instantaneous behavioral policy. The target Fλ is affine, so the signed residual is an affine combination of endpoint residuals; by triangle inequality, each law's TV is at most the matching affine interpolation of the endpoint bounds. These interpolate to exactly the three claimed upper affine pieces. This proves ALL real parameters, not merely finite sample values.

## Three independently checked global S₂ lower duals

For eight-event vectors wQ,wP, write L(σ)=E_Q[wQ]+E_P[wP]. For each of the following oscillation(wQ)+oscillation(wP)=1; hence L(σ)−L(Fλ)≤max(TV_Q,TV_P).

Flat dual w0:
 wQ=(0,0,25/253,0,3/2024,25/253,25/253,−25/253)
 wP=(0,0,−203/506,0,0,−197/506,−197/506,203/506)
 min_(σ∈S₂)L0(σ)=−153/506, L0(Fλ)=−154/506.
 First rising dual w1:
 wQ=(0,0,292/3265,961/9142,961/9142,961/9142,799/9142,−961/9142)
 wP=(0,0,−1805/4571,1805/4571,1805/4571,−1805/4571,−245/653,1805/4571)
 min_(σ∈S₂)L1(σ)=−6981/22855, L1(Fλ)=−6992/22855−39λ/18284.
 Second rising dual w2:
 wQ=(0,0,3/190,9/38,9/38,9/38,−9/38,−9/38)
 wP=(0,0,−29/190,5/19,5/19,−5/19,5/19,5/19)
 min_(σ∈S₂)L2(σ)=−85/456, L2(Fλ)=−337/2280−13λ/228.

Proof of global Bellman minima: For a FIXED linear objective the behavioral target is multi-affine in the independent action probabilities for each time-signature. Successively replacing each simplex variable by a minimizing vertex never increases the objective. The t1 choices at A,B have 3² possibilities, and the t2 grouped signatures U=AU/BU, AV, BV have 3³ possibilities. For each of the 243 deterministic prefixes optimize every unrestricted t3 decision independently over STOP P, STOP Q, or CONTINUE followed by its cheapest t4 decision. This exact finite grouped Bellman check is a global lower bound for all real randomized S₂ policies, and therefore the subset S₂₃. Three minima and both oscillations have been re-executed with standard-library Fraction.

The three bounds therefore imply

 d₂,d₂₃ ≥ max(1/506, 11/22855+39λ/18284, 13λ/228−11/285).

The pairwise switches of this MAX are precisely λ*,89/125. All four behavior endpoint upper witnesses and convex interpolation attain it, completing the global proof of each piece. This also establishes that the observed loss is not a convexified unattainable solution.

## Evidence, status and follow-up

The companion VERIFY.py reconstructs every labeled history and original full-history Fλ trajectory; checks both laws' mass conservation, true likelihood fiber groups, 53 flow variables, four explicit rational endpoint occupancy witnesses, endpoint full signed residuals and TV, all three duals' exact 243-prefix Bellman minima and score-affine identities, and six rational interval-interior probes. Output RESULT.json contains status PASS_EXACT_FRACTION_N4_COMPLETE_POST_FLAT_PHASES. Full-real interval strength rests on the occupancy lemma plus TV convexity and exact global lower duals.

All research is external finite BRC probability-tree analysis. P000 remains six native discrete spatial axes, 3D slice readouts inside native X6, separately typed time, and preserved structural residuals. No faithful native X6 state/update and future-observer bridge has yet been established.

Next: change F outside this one-parameter family on the SAME N4 tree and determine whether some exact F has d₂(F)+d₃(F)<d₂₃(F); alternatively prove general subadditivity for a specified family. Require explicit executable policies and matching full-class lower certificates. The equal-upstream-survival lemma used here must be rechecked for changed t1 histories or other trees.