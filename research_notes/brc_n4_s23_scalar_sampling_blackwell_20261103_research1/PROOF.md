# BRC N=4 / S23: exact cost of a single repaired Bernoulli event versus a full source draw

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: PR #1765, `f7203e1396879839dc29a045ddc1e519b30ff0da`, binary-erasure two-state witness.

## Model and target

Use the existing six provenance-labeled sources, four stopping outcomes and nonuniform mixing matrix specified in the predecessor. Fix scheme F=(3,31), delete source row j=0 in the N and E views, and restore only the indicator of the event E-row-0 outcome 2 (one scalar probability, estimated by repeated independent Bernoulli trials). The retained E-row-1 permits independently chosen full four-outcome trials. Original-view data are excluded. Other retained rows and N-view rows are sign-independent on this particular witness.

Consider the lawful states z+/z- from the predecessor: z2=1, every otherwise-unmentioned parameter is 1/2, z5+=1/2+21h, z5-=1/2-21h, z6+=1/2-19h, z6-=1/2+19h, with real 0<=h<=1/42. Their target-nine-coordinate infinity distance is 42h.

Write s=(1-beta_E)^2 in [0,1], p=1/2+h and q=1/2-h. Source row 0 has third-branch mean t0=p under + and q under -; retained row 1 has mean t1=q under + and p under -. Retain source/view identity when recoding outcomes.

A full row-1 draw, after recoding its outcome 3 as '+' and outcome 2 as '-', is a ternary experiment T with law
  under +: (+,0,-)=(sp,1-s,sq);
  under -: (+,0,-)=(sq,1-s,sp).
(The 0 tag combines first/second gate erasures, whose conditional split is hypothesis-independent.)
A repaired scalar event-2 draw from deleted row 0 is binary experiment B:
  under +: Bernoulli(sp); under -: Bernoulli(sq).
The experiment B is the deterministic coarsening of T that sends '+' to 1 and {0,'-'} to 0. This is an equivalence of the two *specified hypotheses*, not of the entire nine-dimensional parameter family.

## Theorem 1: exact mixed-allocation finite-sample Bayes error

For any integers f,r>=0 and independent f full T trials and r repaired-scalar B trials, under equal prior probability on the two states, the optimal testing error is

 e(f,r) = (1/2) SUM_{k=0}^f SUM_{t=0}^k SUM_{u=0}^r
  binom(f,k) binom(k,t) binom(r,u) (1-s)^(f-k) s^k
  min{ p^t q^(k-t) (sp)^u (1-sp)^(r-u),
       q^t p^(k-t) (sq)^u (1-sq)^(r-u) }.

Use 0^0=1 in the binomial expansion. This is exact for all real 0<=h<=1/42, 0<=s<=1 and all f,r. It counts each mutually exclusive four-outcome source trial once.

Proof: k is the number of non-erased full trials, t the number of '+' among these, and u the number of positive scalar indicators. Conditional independence gives the two terms in the braces, including the combinatorial multiplicity; the optimum equal-prior likelihood test contributes half the smaller joint probability for every sufficient-statistic cell. Summation gives the formula.

## Theorem 2: finite-sample Blackwell order and an exact one-trial equality

For every N>=1 and every real h,s in the above domain,

  e(N,0) <= e(f,N-f) for 0<=f<=N,
  and e(N,0) = e(N-1,1).

Proof of the inequality: replace each binary B sample by a ternary T sample, then apply the fixed coarsening map. T is Blackwell-more-informative for the pair, and Bayes risk cannot increase under a more informative observation.

For equality, first observe N-1 full T trials. If h>0 and s>0, the prior likelihood ratio equals (p/q)^d for an integer d=(number '+')-(number '-'). The final T trial has likelihood ratios p/q on '+', 1 on erasure, q/p on '-'. Under equal prior and 0-1 testing loss, the optimal decision after an erasure and after '-' may be chosen the same: if d<=0 choose '-' (erasure is a tie when d=0); if d>=1 choose '+' (the '-' event is a tie when d=1). Thus combining precisely these two events into B=0 loses no Bayes decision value for any possible prefix. B=1 remains the T='+' event. The cases h=0 and s=0 are uninformative; s=1 has no erasure and B retains the complete Bernoulli outcome. Therefore equality holds including endpoints.

As a consequence, among all equal-cost nonadaptive allocations of N trials between the repaired scalar and retained full row 1, sampling only the retained full row 1 achieves the smallest equal-prior error; replacing its last trial by one repaired scalar retains the same error. Because the all-T pair experiment is symmetric on exchanging the hypotheses and '+'/'-', its equal-prior error is also its frequentist minimax testing error. Thus the optimum *over these allocations* for maximum hypothesis-testing error is e(N,0). The corresponding two-point infinity-norm estimation minimax risk after optimization over allocations is 42h e(N,0), by the metric triangle lower bound and the symmetric endpoint decision. This is a two-state statistical decision result, not the minimax estimator over [0,1]^9.

## Theorem 3: strict information loss at three scalar draws and local pricing

For h=1/42 and beta_E=1/2 (s=1/4), exact values include:
  e(1,0)=e(0,1)=83/168;
  e(2,0)=e(0,2)=47/96;
  e(3,0)=576167/1185408;
  e(0,3)=576497/1185408;
  e(0,3)-e(3,0)=55/197568 > 0.
Thus three binary repair trials lose information relative to three retained full-row trials, even though one or two trials tie for this fixed pair.

For the smooth one-dimensional family indexed by h around h=0 at fixed 0<s<=1, Fisher information per independent trial is I_T(0)=4s and I_B(0)=4s/(2-s). Therefore I_T(0)/I_B(0)=2-s; for s=1/4 the exact factor is 7/4. With positive per-trial prices c_T,c_B, the local Fisher-information-per-cost criterion prefers T precisely when c_T/c_B<2-s (equality is a tie); it prefers B when the reverse strict inequality holds. This price statement is a local-in-h criterion, not an exact finite-budget Bayes ordering under unequal costs.

Proof: T has two non-erasure atom probabilities s/2 with derivatives +s and -s at h=0, giving 2s^2/(s/2)=4s. B has event and non-event probabilities s/2 and 1-s/2 with derivatives s and -s, giving s^2/(s/2)+s^2/(1-s/2)=4s/(2-s). The displayed rational three-sample comparisons follow by substituting into Theorem 1 and evaluating exact fractions.

## Independent downstream-intervention contrast on this witness

An added intervention setting the N-view middle gate z2 to gamma<1, in addition to its original overwrites of z0,z1 to beta_N, changes the N-view row-1 non-erasure probability on this witness from zero (because z2=1) to s_I=(1-beta_N)(1-gamma). Row 1 then becomes the same signed ternary experiment with s replaced by s_I. At beta_N=0, gamma=0, beta_E=1/2, it has s_I=1, whereas the original E-view has s=1/4. For the two witness states, total-variation contrast per full row-1 draw rises from 2sh=h/2 to 2h (a factor of exactly 4); the ratio of target infinity distance to the full-event sup contrast for this pair decreases from 84 to 21. This is a concrete witness-level operator test; global nine-parameter minimax and intervention pricing remain open.

## Evidence, BRC scope and continuation

`VERIFY.py` uses Python standard-library Fraction to check 700 exact mixed-allocation rational inequalities/equalities over 4 values of h, 5 values of s and N=1,...,7, and the explicit sample and intervention contrasts. `RUN_EVIDENCE.txt` records the actual execution. The universal statements follow from the analytic arguments above, not the finite grid.

These conclusions retain the BRC stopping branch, labeled source, event tag, observer and intervention provenance. They do not assert a native Heartbeat X6 time/space lift or update P000; the original ten-label S23 minimax interval [1/2,2/3] remains open. Research output is author-side, unreviewed and not admitted; the present GitHub author identity is not a native EM Researcher-ID/CLAIM.

Next: optimize a finite cost budget over mixed T/B designs with actual positive prices; analyze whether added z2-gate interventions improve the *global* repaired-nine-parameter risk, rather than only this sharply chosen pair.
