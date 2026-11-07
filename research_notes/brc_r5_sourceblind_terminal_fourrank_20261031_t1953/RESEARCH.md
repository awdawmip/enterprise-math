# R5 — a source-blind terminal observer detects hidden-source residual after exact time compensation

Date: 2026-10-31 (Asia/Shanghai).
Evidence status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**.
Scope: auxiliary finite two-law stochastic stopping model. Neither a native X6 theorem nor an accepted answer to the original four-observer mother problem.

## Frozen input and role boundary

GLOBAL_KNOWLEDGE_V1 canonical main 9c204606f700d04b93ca9cb1e422085a2420b183, including current bootstrap, manual, ACTIVE worldview and mathematical/BRC policies. Enterprise Math canonical main 3244d13af5ec26808eac8494504988f414cddc6e, including AGENTS, locked P000, X6/time and joint-relation preservation contracts, control and portable research protocols. Protected foundations have not changed.

Unreviewed predecessor: fe9bc384a1368e5eadd08ada606c8c4297770eb0 / research_notes/brc_r5_c_to_l_time_rigidity_20261031_t1840/SOURCE_SPECIFIC_EXTENSION.md. Earlier source-and-action-history-sensitive-error separator this same author run: c942af479f42327a1219879e2550f73b41943900 / research_notes/brc_r5_source_compensated_four_rank_separator_20261031_t1936/RESEARCH.md. The present result is stronger: the new terminal response uses ONLY final observed (time, likelihood ratio), not hidden source or prior action.

The connected native service at intake reported research_authority_granted=false, executor_binding_configured=false, control CODE_REVIEW_REQUIRED, and active job quota 5/5. Current Source owner/CLAIM, Result and independent Driver review were not established. This is an author-side portable proof and verified GitHub storage, not a state-machine admission or review.

BRC carrier: retain origin/path-labelled positive Q-cylinder masses and exact P=lambda*Q leaf transport up to the final observer O=(error_P,error_Q,T_P,T_Q); origin contrast is a typed lost-information witness when compressed to times. A signed support functional of O is a diagnostic readout, NOT signed positive-BRC branch mass. No independent 2D native space, no native six-axis X6 dynamics, no physical timing claim.

## Full stopping model and strategy classes

Two hidden origins i=0,1 each start with Q=P probability 1/2 at key A=(time1, LR1). A may STOP at time1 or CONTINUE. Conditional on CONTINUE, nature chooses D,C,Y at time2 with Q masses (alpha_i, 1-2alpha_i, alpha_i) and likelihoods (1/2,1,3/2); their P masses are (alpha_i/2,1-2alpha_i,3alpha_i/2).

D may STOP at (t2,LR1/2) or CONTINUE, splitting Q in proportions (2/3,1/3) to terminal (t3,LR1/4) and common L=(t3,LR1). Y may STOP at (t2,LR3/2), or CONTINUE with Q proportions (1/2,1/2) to (t3,LR2) and common L. C has no policy decision: nature STOPs at (t2,LR1) with probability 1-kappa_i, or enters that same L with probability kappa_i. At L, policy STOP ends at t3 and CONTINUE at t4, both at LR1. All nature probabilities are positive for 0<alpha_i<1/2, 0<kappa_i<1. Likelihoods and conditional Q weights imply each origin contributes Q=P total mass 1/2 under every strategy.

FULL policies may use origin and full path history: 12 independent binary deterministic decisions (origin A,D,Y and the three origin-specific L-entry routes). Seedless LR policies can decide only at common observed keys A,D,Y,L: 4 binary decisions without persistent random seed. Their behavioural variants choose independent real local stop/continue probabilities. No decision key is revisited on a single path. Expected linear scores are multi-affine in policy action probabilities, hence the FULL and LR maximum in any signed direction is attained at a deterministic policy.

Put theta_i=[1+kappa_i(1-2alpha_i)]/alpha_i. The preceding unreviewed author proof establishes equality of actual two-time behavioural images on theta_0=theta_1. This run independently checks every FULL deterministic time vector in the exact rational LR time hull for the concrete compensated pair; it does NOT claim an independent review of the predecessor's all-real assertion.

## Theorem 1 — exact all-real source-BLIND observer gap

Fix a single common terminal-error response for BOTH strategy classes, depending ONLY on terminal (time,LR), never on hidden origin, historical path, action or policy class:

r(t,lambda) = 1/2 + epsilon*I[(t,lambda)=(2,1)] + eta*I[(t,lambda)=(3,1/4)],

where 0<epsilon<1/2 and 0<=eta<1/2. The indicator (2,1) is the unique C_STOP terminal leaf; (3,1/4) is the unique D_HIGH leaf. These leaves are mutually exclusive; every r and 1-r is strictly positive. This is a legitimate error-probability response rather than a controllable strategy action.

For all real positive natural parameters in the declared domain with theta_0=theta_1=theta, let
b_i=(1-2alpha_i)(1-kappa_i)>0 and
t_star=theta-epsilon*(b_0+b_1)/(alpha_0+alpha_1).
Then t_star>0, and for the signed full four-observer direction

H_star=e_Q + 2(t_star+1)*T_P - (2t_star+3)*T_Q,

the exact support gap over ALL real behavioural strategies is

sup_FULL H_star - sup_LR H_star
= epsilon*|alpha_0-alpha_1|/(alpha_0+alpha_1).

Thus on the source-compensation surface the complete four-observer convex hulls match IF AND ONLY IF alpha_0=alpha_1. When alpha_0=alpha_1, compensation forces kappa_0=kappa_1 and even the ACTUAL real four-observer behavioural sets agree (proof below). For different source kernels this entire family can therefore NEVER yield the mother target: equal four-hulls with unequal actual real images.

### Proof — all signed controls and positivity of t_star

For arbitrary t>0 define u=2(t+1), v=-(2t+3), and w_lambda=u*lambda+v. Then w_1=-1, w_(1/2)=-(t+2), w_(3/2)=t. At L, STOP is strictly preferable to CONTINUE because w_1<0. At Y, CONTINUE is strictly preferable because w_(3/2)>0 and the continuation Q-weighted likelihood mean remains 3/2. At D, CONTINUE adds one time unit with mean-likelihood 1/2, giving a time-score loss t+2. It can collect only eta*(2/3) extra e_Q through D_HIGH, with eta*(2/3)<1/3<t+2. Thus D STOP is optimal. All these lower actions are common across origins, so they can simultaneously be implemented by FULL and by seedless LR, giving no source-policy gap below A.

Conditional on origin i, the A CONTINUE minus A STOP advantage for H_t equals

D_i(t) = alpha_i*(t-theta_i) + epsilon*b_i.

To verify directly, the time reward difference is
2alpha_i*w_(1/2) + (1-2alpha_i)(2+kappa_i)*w_1
+3alpha_i*w_(3/2) - w_1
=alpha_i*(t-theta_i).
The terminal base-error 1/2 cancels because Q is normalized under any policy. C_STOP contributes epsilon*(1-2alpha_i)*(1-kappa_i)=epsilon*b_i. D_HIGH is not reached with optimal D STOP. FULL chooses the sign of each D_i independently at A, while seedless LR must make the same A choice for both origins. With the Q prior 1/2 each and max(0,x)=(x+|x|)/2,

Delta(H_t) = [|D_0(t)|+|D_1(t)|-|D_0(t)+D_1(t)|]/4.

Under theta compensation,
b_i=(1-2alpha_i)(1-kappa_i)=2-alpha_i*(theta+2),
b_i/alpha_i=2/alpha_i-theta-2.
Because theta>1/alpha_i>2 and b_i>0, one has 0<b_i/alpha_i<theta-2. Their alpha-weighted average has the same bound. Consequently,
t_star > theta-epsilon*(theta-2)>0.

Substitute t=t_star. Then D_0+D_1=0 and

D_0=epsilon*(alpha_1*b_0-alpha_0*b_1)/(alpha_0+alpha_1)
=2epsilon*(alpha_1-alpha_0)/(alpha_0+alpha_1)=-D_1.

Therefore Delta(H_star)=|D_0|/2
=epsilon*|alpha_0-alpha_1|/(alpha_0+alpha_1).
This is an all-real strict four-hull separating direction whenever alpha values differ, even when the two-time projections have exactly matching actual images.

If alpha values are equal, theta equality algebraically implies kappa equality. At every observed key A,D,Y,L, nature's downstream transition law is then source-independent. For ANY FULL behavioural policy, aggregate the exact Q STOP flux over origins and incoming histories at each observed key and set a seedless LR local STOP probability equal to this flux divided by its total Q key occupancy (arbitrary on zero occupancy). Since P key occupancy is always the key LR times Q occupancy and the same Markov transition weights apply, this reproduces recursively all terminal Q and P masses grouped by (t,LR). Because BOTH terminal errors are functions of (t,LR), it reproduces e_P,e_Q and T_P,T_Q exactly. LR is itself a subset of FULL, so actual four-observer images coincide. QED.

## Theorem 2 — strictly positive exact rank-four rational separator

Choose
(alpha_0,kappa_0)=(1/4,3/4);
(alpha_1,kappa_1)=(1/5,1/6);
epsilon=1/4, eta=1/64.

Both theta_i=11/2, but source transition kernels are different.
b_0=1/8, b_1=1/2, t_star=371/72.
Multiplying H_star by 36 gives the INTEGER direction

J=36*e_Q+443*T_P-479*T_Q.

The analytic formula and complete exact-rational enumeration give
sup_FULL J=-17; sup_LR J=-18; signed support gap EXACTLY 1.

A legal FULL deterministic policy (A0=STOP,A1=CONTINUE,D0=D1=STOP,Y0=STOP,Y1=CONTINUE, all L=STOP) yields the four-observer vector
x=(9/16,9/16,17/10,33/20).
It satisfies J(x)=-17, while all LR four-hull y satisfy J(y)<=-18. By the dual norm inequality,

distance_infinity(x,conv(O_LR))>=1/(36+443+479)=1/958.

This separates the WHOLE LR convex hull, not only its actual behavioural set. Strict terminal error probability is in [1/2,3/4], with complementary probability in [1/4,1/2]. The extra source-BLIND D_HIGH error at (t3,LR1/4) does not alter the optimized J (D STOP remains strict), but makes LR's four-observer image FULL AFFINE RANK 4.

Using lexicographic LR bits (A,D,Y,L), the five exact vectors of policy indices 0,8,9,10,12 are:

0:  (1/2,1/2,1,1)
8:  (37/64,37/64,179/80,179/80)
9:  (37/64,37/64,99/40,99/40)
10: (37/64,37/64,103/40,197/80)
12: (2963/5120,743/1280,47/20,197/80)

The determinant of the four row differences relative to index0 is

det=-1539/419430400 !=0.

Thus this is a strict-positive, time-compensated, four-rank but still FOUR-HULL-SEPARATED model, where not even the error observer sees the hidden source or the decisions. This is the substantive negative discovery. No mother-theorem equality is claimed.

## Execution evidence and precise limits

The accompanying standard-library VERIFY.py was ACTUALLY EXECUTED locally with arbitrary-precision Fraction arithmetic; its unchanged stdout is EXACT_OUTPUT.txt. It checks exactly 4096 FULL and 16 LR deterministic policies; for each, P/Q terminal total=1 and per-origin mass=1/2, each terminal response is in (0,1). All 4096 FULL time points lie inside the exact six-vertex LR time polygon at the stated rational pair. The checker verifies J maxima (-17,-18), the exact FULL witness, the five LR rank vectors and the 4x4 nonzero rational determinant, and ends with PASS_EXACT_R5_COMPENSATED_SOURCEBLIND_TERMINAL_RANK4_SEPARATOR.

Theorem 1 holds for the stated continuum of real source-compensated parameters and response amplitudes by analytic Bellman proof. Theorem 2 is a fully enumerated exact rational example. The predecessor's all-real actual two-time equality is an unreviewed author proof; the present finite exact two-time hull containment is an independent check only of the displayed rational example. No native X6 realization, universal statement for arbitrary error kernels, accepted Source Result, independent Driver review or Foundation promotion.

NEXT_TASK.md gives one exact remaining question: seek source-blind terminal response families where all signed four-hull directions match while retaining rank four, with rational 5-vertex certificates or Farkas separators. Only after complete four-hull equality may the actual real seedless-LR nonmembership be investigated.
