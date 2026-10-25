# Auxiliary iid N=14 sequential testing — Stage 94 exact affine segment

2026-10-25. **Evidence class: author-side exact finite-model proof, not an independent Research Driver acceptance, native Task/CLAIM/Result, or native BRC/X6/Heartbeat theorem.**

## Question and theorem

Let observations on {0,1,2} be iid under P=(1/8,1/24,5/6) or Q=(1/12,1/12,5/6). All randomized stopping/decision policies dependent on the complete ordered history with stopping time T<=14 are allowed. Denote e_P=P(decide Q), e_Q=Q(decide P), t_P=E_P T, t_Q=E_Q T, and V14(alpha)=inf{max(t_P,t_Q):e_P,e_Q<=alpha}.

Inherited, author-verified Stage93 endpoint:
alpha93=5172463688734421243/14900301753911083008,
V93=24275119932147668699/1862537719238885376,
s93=27641630644888847/41779200000000000,
where s93 is the probability of immediate Q at balance state B=(12,0,1).
All earlier endpoint decisions are frozen, especially A93=(5,4,0) to immediate P. The new state A94=(10,5,1) permits continue/immediate P.

**Theorem.** Let eta94=2234496875/9700717287702528, Gamma94=13545864/4231. For EVERY REAL 0<=delta<=eta94:

  V14(alpha93+delta) = V93 - Gamma94 * delta.

The right endpoint is

  alpha94=5172467120921621243/14900301753911083008,
  V14(alpha94)=24273746381538068699/1862537719238885376.

The fixed supporting line is *strictly unattainable* for alpha>alpha94: this is right-end sharpness of Stage94, NOT proof of the Stage95 interval.

## Bellman support over all ordered-history policies

At count state (n,a,b), with a occurrences of 0, b occurrences of 1, the likelihood ratio of every ordered history reaching that count equals Q/P=2^(a+b)/3^a. Take lambda_Q=K94=7010064/4231 and lambda_P=72+(8/9)K94=6535800/4231, so Gamma94=lambda_P+lambda_Q=13545864/4231. With continue forbidden at n=14, define the exact rational Bellman minimum

  D(n,a,b)=min{lambda_Q*2^(a+b)/3^a, lambda_P, 1 + sum_i P_i D(child_i(n,a,b))}.

These correspond to decide P, decide Q, continue. Conditional-expectation induction gives D(root)<=t_P+lambda_P e_P+lambda_Q e_Q for ANY randomized ordered-history policy, even if the policy is not count-Markov. Hence V14(alpha)>=D(root)-Gamma94*alpha.

The inherited Stage93 endpoint selected-action table, with A93 frozen P, satisfies every Bellman inequality at K94, by 680 exact rational state evaluations and 1240 nonselected-action comparisons: 1238 gaps are strictly positive, none negative, exactly two zero ties, A94(C/P) and B(C/Q). Minimum strictly positive gap is 175345197055/116432163569664. A separately programmed minimizing Bellman recursion confirms

  D(root)=65153634128674757873633/57944096250733264896
         =V93+Gamma94*alpha93.

Thus the lower support line is exact at the starting point, with no unexamined count states.

## Exact first-hit carrier (word multiplicity is not probability mass)

Under the inherited deterministic policy, A94=(10,5,1) has 1260 nominal compatible ordered prefixes, but only 845 genuine first-hit histories. Their exact total first-hit weights are

  p_A=528125/1019215872, q_A=528125/3869835264.

The inherited continuation from A has 21 distinct terminal suffix words (12 terminal state/action classes). Stopping at A truncates 845*21=17745 complete ordered histories. Its conditional continuation vector, ordered as (P-error, Q-error, P-additional-time, Q-additional-time), is

  R_A=(635/165888,10201/10368,7711/6912,1069/864).

At B=(12,0,1), all 12 nominal prefixes are genuine first hits, with

  p_B=48828125/725594112, q_B=48828125/362797056,
  R_B=(63/64,1/144,9/8,13/12).

B's old continuation has 5 terminal suffix words. A includes 5 zero-symbols by time 10 whereas B requires zero zero-symbols by time 12. Counts do not decrease, so A and B have disjoint path cones. These are finite positive-rational ordered-history BRC-style weights and word counts; signed-amplitude or native geometric claims are excluded.

## Constructed optimal primal family for the FULL real interval

Let u in [0,1] be the chance of immediate P at A, and s in [0,1] the chance of immediate Q at B. Define

  X=p_A*R_A.Perr=335359375/169075682574336,
  Y=q_A*(1-R_A.Qerr)=88196875/40122452017152,
  E=p_B*(1-R_B.Perr)=48828125/46438023168,
  H=q_B*R_B.Qerr=48828125/52242776064.

Disjoint cones make the following exact, not approximations:

  e_P=alpha93-X*u+E*(s-s93),
  e_Q=alpha93+Y*u-H*(s-s93).

Setting e_P=e_Q gives

  s=s93+h94*u, h94=(X+Y)/(E+H)=54977897/26112000000,

and the common error is

  alpha93+eta94*u, eta94=-X+E*h94=Y-H*h94
                    =2234496875/9700717287702528>0.

The right-end B parameter is s94=27729595280088847/41779200000000000. Since 0<s93<s94<1, every real u in [0,1] gives a valid randomized policy.

The P and Q expected times are affine functions of u because the two randomized branch cones are disjoint. Exact endpoint forward recurrences yield

  (t_P-t_Q)(0)=775708071240140755/1241691812825923584>0,
  (t_P-t_Q)(1)=775383214032140755/1241691812825923584>0.

Therefore t_P>t_Q for all real u in [0,1]. The exact change is

  t_P(0)-t_P(1)=99359853125/134732184551424
               =Gamma94*eta94.

At both randomized states all available actions are Bellman minimizers; all other visited actions are the unique minimizers. Consequently

  t_P+lambda_P*e_P+lambda_Q*e_Q=D(root),

and equality holds in the universal dual bound with alpha=alpha93+eta94*u for every real u in [0,1]. This proves the full asserted continuum.

## Sharpness for arbitrary history-dependent randomization

Finite horizon implies a finite occupation-measure polytope and attainment. If for some alpha>alpha94 the same supporting line equaled V14(alpha), then equality in the universal lower-bound chain and positivity of both multipliers force BOTH errors equal alpha and every reached action to minimize the Bellman objective. All other states have a positive gap, so only A and B may randomize. At a fixed count state, Q/P is constant for all its ordered words and its conditional suffix law is identical. Arbitrary history-specific randomization can therefore be first-hit-mass averaged to one u at A and one s at B without changing errors/times. The first-hit masses remain fixed and the cones are disjoint. Error equality then forces s=s93+h94*u and alpha=alpha93+eta94*u<=alpha94, contradiction. Hence the fixed Stage94 support is right-sharp even for the full ordered-history policy class.

## Verified next dual candidate; limits

After freezing A94 to immediate P, Bellman gaps stay nonnegative for every K in [K95,K94], where

  K95=112428/71; A95=(10,1,2), continue/immediate Q.

At K95 only B and A95 tie, with 1238 strict gaps; at K95-1/10000 the A95 gap is negative. All gaps are affine in K, so the fixed policy is dual optimal over that exact K interval. **No Stage95 primal risk interval is established.**

Two exact rational programs passed: derive94.py evaluates the selected policy Bellman values and forward positive-weight histories, while crosscheck94.py independently enumerates ordered first-hit/suffix words and computes the minimizing root. Both reuse the inherited deterministic action table from stages 88-93 and are not an independent Driver audit. A reproduction bundle with ancestor modules is provided separately. All-real optimality follows from the displayed algebra and affine endpoints; eight internal sample-point assertions alone would not prove that statement.

Input pins: GLOBAL_KNOWLEDGE_V1 main@c8191daa0c167af40c86972ac9fe45dc3569e06c; Enterprise Math main@dc5ac35bec5b016609edeba64f298fcab1db9270; parent derive93.py blob c27cb008fe5c1a9b3b821a6496f8704f4a2d7064. Existing positive rational weighted BRC typed carrier was REUSE_APPLIED; inherited exact algorithm chain REUSE_EXECUTED; ordered positive-weight provenance with Bellman recursion COMPOSE_APPLIED.

Native control inventory failed CONTROL_QUOTA, and the authenticated read-only service refused session_start with STATIC_READONLY_SCOPE_DENIED (operation_sent=false). GitHub author-source storage DOES NOT create a Source Task CLAIM, verify an active owner, freeze a Result, grant independent review, or lift any authorization restrictions. P000 remains locked. No X6/six-axis or three-dimensional-slice/native transfer theorem is implied.