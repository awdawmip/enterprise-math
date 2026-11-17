# R5 — Repeated coarse LR key: a curved-hull theorem and an exact Markovization boundary

Date: 2026-11-01, Asia/Shanghai.
Author-side scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
This is an auxiliary finite two-law stopping process, NOT native Enterprise Math X6 or the mother four-observer result.

## Frozen input and scope

GLOBAL_KNOWLEDGE_V1 canonical main: dfd8e064388b9ff875ce2780b657ca80be5630eb. Canonical Enterprise Math main: 1fde72896593e8b10c9abb356983a265d2a4600f. Applied current 00_BOOTSTRAP, OPERATING_MANUAL, P000 and ACTIVE worldview, task role, math/code/BRC policy and portable protocol. Predecessor research at PR #1663 immutable commit d5db79195a9d0cdda4f51a07dcecb3fc9d0bb8bd proves a no-go for fourth linear readings of 24 fixed source-labelled terminal atoms, under policy keys visited once per trajectory. This note tests the smallest *new mechanism* that breaks that finite-corner argument. All protected worldviews remain unmodified.

Native em_status v0.6.11: research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED, five of five control jobs active; a bounded live-owner inventory call returned CONTROL_QUOTA. This author-side preservation grants no formal CLAIM, Result, review or theorem admission.

BRC methodological reuse is the positive source/route-labelled P,Q carrier and preservation of hidden phase/branch provenance. Arithmetic here is standard exact rational algebra, NOT an invocation of a native BRC operation or X6 coordinate update.

## Model and the exact policy-key distinction

Two hidden origins i=0,1 each have Q(i)=P(i)=1/2. A trajectory can visit a coarse observation key L twice, first in physical phase 1 and later in physical phase 2. The agent controlling the coarse key cannot see origin, phase, visit number or chronological time; its likelihood ratio is exactly 1 at both decision points. This coarse observation convention is explicit: an actual LR key that includes time would distinguish the two visits, and the present theorem must not be transferred to it without proof.

At the first visit, the policy either stops in class S1 or continues. On continuation the environment returns to L in phase 2 with chance rho, or exits at E with chance 1-rho, where rho is any real number in (0,1). At the second visit it stops at S2 or continues to F. Every terminal class k∈{S1,E,S2,F} is then decorated by an independent *late* binary signal s: Q(s=0|i,k)=Q(s=1|i,k)=1/2, while P(s=0|i,k)=1/4 and P(s=1|i,k)=3/4. Thus P and Q are genuinely distinct, both normalized, and every environmental branch is strictly positive. Ratios at terminal signals are 1/2 and 3/2; all earlier likelihood ratios equal 1. Deterministic actions are allowed to make a policy-selected event unreachable; this does not violate strictly positive environment kernels.

Full history chooses origin-and-phase-specific stop probabilities p_{j,i}. Seedless LR-FRESH-STATIONARY chooses one stop probability p for *both* visits, drawing independent fresh Bernoulli actions conditional on each visit. It reuses the **parameter**, not a realized action or a persistent random seed. LR-PERSISTENT-BIT instead samples one Bernoulli action before the first visit and reuses the outcome; it is a different policy class. LR-PHASE-REFINED can choose different parameters on the two visits.

The observation is the four aggregated Q terminal class masses Z=(q_S1,q_E,q_S2,q_F), after summing both hidden origins and late signal labels. These coordinates sum to 1: they are NOT the mother tuple (e_P,e_Q,T_P,T_Q), and the affine rank is below 4. This is a method-scope lemma, not a purported mother-solution.

## THEOREM A — Complete curved stationary hull (all real 0<rho<1)

Under fresh independent resampling at the repeated coarse key,

Z_LR(p) = (p, (1-rho)(1-p), rho*p*(1-p), rho*(1-p)^2),  0<=p<=1.

Write t=q_S1 and r=q_F. The exact **actual** LR image is the parabola r=rho*(1-t)^2. Its complete convex hull is the closed semialgebraic strip

0<=t<=1;  q_E=(1-rho)*(1-t);  q_S2=rho*(1-t)-r;
rho*(1-t)^2 <= r <= rho*(1-t).

Proof: For any convex mixture, t=E[p] and r=rho*E[(1-p)^2]. Jensen gives the lower bound and (1-p)^2<=(1-p) gives the upper. Conversely p=t attains the lower bound; the mixture of p=0 and p=1 with weights (1-t,t) attains the upper. Mixtures of these two representations at fixed t achieve every intervening r, with the remaining coordinates fixed by conservation.

Furthermore, for every p0 in (0,1), the *linear* functional

ell_p0(Z) = -q_F - 2*rho*(1-p0)*q_S1

obeys the exact identity

ell_p0(Z_LR(p0)) - ell_p0(Z_LR(p)) = rho*(p-p0)^2.

Hence Z_LR(p0) is a uniquely exposed extreme point of the entire convex hull. There are uncountably many such points; this compact convex hull is NOT a polytope. In particular the two deterministic stationary-key policies p=0 and p=1 do not generate the hull. QED.

## THEOREM B — FULL triangle and strict support gap

The FULL **actual** image equals the convex triangle

0<=t<=1; q_E=(1-rho)*(1-t);
q_S2+r=rho*(1-t), 0<=r<=rho*(1-t).

Proof: For origin-specific controls, put t=(p_{1,0}+p_{1,1})/2 and
h=[(1-p_{1,0})p_{2,0}+(1-p_{1,1})p_{2,1}]/2.
Then q_S2=rho*h and q_F=rho*(1-t-h), with 0<=h<=1-t, and q_E=(1-rho)(1-t). Conversely choose the same first-phase stop probability t in both origins and second-phase stop probability h/(1-t), for t<1. This realizes every point of the triangle, including its boundary; t=1 is the single first-stop vertex.

In the linear support direction selecting q_S2,
max_FULL q_S2 = rho,
max_LR-FRESH q_S2 = rho/4,
because p(1-p)=1/4-(p-1/2)^2.
The exact full-minus-LR support gap is 3*rho/4>0, for EVERY real rho∈(0,1). This separates their complete convex hulls; the example cannot satisfy the mother hull-equality prerequisite. QED.

## THEOREM C — Exact irrational infinity-norm distance

At rho=1/2, a legal FULL policy p1=0,p2=1 gives
W=(0,1/2,1/2,0).

In these four aggregated Q coordinates,
dist_infinity(W,conv Z_LR)=(3-sqrt(5))/2.

Proof: Let delta be the unique root of z^2-3z+1=0 in (3/8,2/5), i.e. delta=(3-sqrt(5))/2<1/2. Every LR mixture with first-coordinate t has q_S2 <= t*(1-t)/2 by Jensen, as in Theorem A. If t>=delta, the first-coordinate distance to W is >=delta. If 0<=t<delta, monotonicity of t*(1-t) on [0,1/2] gives the third-coordinate deviation
1/2-q_S2 >=1/2-t*(1-t)/2 >1/2-delta*(1-delta)/2=delta,
where the final equality is delta^2-3*delta+1=0. At the actual LR policy p=delta, the four absolute coordinate differences are exactly (delta,delta/2,delta,delta/2), using (1-delta)^2=delta. Both lower bound and attainment follow. QED.

The simpler q_S2-only support certificate yields 3/8; the exact L-infinity distance is strictly stronger.

## THEOREM D — Seed semantics and refined-key Markovization

A once-sampled persistent Bernoulli action B~Bernoulli(p), reused as the *same realized bit* on both visits, yields
Z_PERSIST(p)=(p,(1-rho)*(1-p),0,rho*(1-p)).
It never stops at S2. A persistent random choice of the *number p* followed by fresh Bernoulli samples instead yields mixtures of Theorem A's curve, not this segment.

If the LR information key distinguishes physical phases, allowing independent parameters p1 and p2, its **actual** aggregate terminal observation image is precisely the FULL triangle. Given any FULL aggregate t and q_S2, choose p1=t and p2=q_S2/[rho*(1-t)] for t<1 (arbitrary p2 if t=1). This reproduces all four class masses and therefore both P and Q origin-aggregated terminal signal masses, since the late signal kernel is common to origins. Thus the coarse-key failure is an information-loss issue; it is NOT an obstruction for the time-aware (time,LR) key class in this toy model. QED.

## Consequence for the ongoing R5 search

The earlier deterministic-corner/Farkas reduction is complete only if every policy parameter enters multi-affinely (in particular, the same decision key is not used twice along one path). Reusing p produces p(1-p) and (1-p)^2, which are quadratic, have interior support optima and an infinite exposed hull. For a repeated-key extension, do not replace real behavioral optimization by a finite deterministic strategy list without proving a new reduction. First pin the actual observation sigma-field, chronological-key convention and fresh-vs-persistent randomization. For recurrent keys use exact semialgebraic or certified support methods instead of a false finite-corner proof.

The typed two-law carrier has 2 origins × 4 terminal classes × 2 late signals=16 Q atoms and 16 P atoms, plus hidden phase. The aggregated four-coordinate readout loses phase/source residual. No native three-dimensional slice embedding, third-coordinate meaning or preserved X6 update is supplied, so native transfer is explicitly unproved.

## Executed exact validation and literature context

The standalone standard-library Fraction VERIFY.py actually checked: 39 two-law normalization/ratio cases; 243 two-origin source aggregation and phase-refined Markovization cases; 507 exact rational quadratic exposure identities; 195 explicit rational mixtures spanning the curved hull; the rho=1/2 witness, support extrema and rational isolation interval for the irrational root. Its last line is PASS_EXACT_R5_REVISITED_KEY_NONPOLYHEDRAL_HULL_AND_FLOW. The all-real theorems above are analytic; the finite checks are consistency tests and do not constitute an independent proof of continuum claims. No Lean, independent Driver assessment, mathematical admission or novelty-priority determination occurred.

Background contrast, not direct prior-art equivalence: Laroche and Tachet des Combes (ICML/PMLR 2023), "On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs", https://proceedings.mlr.press/v202/laroche23a.html, treats occupancy Markovization with an adequate state representation. Piunovskiy and Zhang (SIAM J. Control Optim. 62(1), 2024), "Extreme Occupation Measures in Markov Decision Processes with an Absorbing State", https://doi.org/10.1137/23M1572398, studies stationary extreme points under its distinct MDP assumptions. A hidden physical phase is NOT a complete Markov state for our coarse observation key, so neither source may simply be invoked to remove the above obstruction.

## Next exact task

Find a time-aware, source-sensitive two-law reconvergent or recurrent model with genuine (e_P,e_Q,T_P,T_Q) observations and strictly positive kernels. Freeze what LR can actually observe, compute the exact terminal carrier, rank and polynomial degree in each **actual** key parameter. If multi-affinity holds, use finite signed supports / exact LR convex certificates. If it fails, derive a valid semialgebraic support or membership certificate. Require rank4 AND entire FULL/LR convex hull equality before testing actual real image nonmembership. Original mother problem remains OPEN.
