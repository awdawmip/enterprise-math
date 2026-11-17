# R5 — Uniform stop-only censor no-go over the ENTIRE legal early-error rectangle

Date: 2026-10-30 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This theorem strictly strengthens the earlier local-wedge support-gap result in RESEARCH.md at commit 423e9db4c1d7088aba2f9290644323b80ab55de9. It supersedes that note's suggested search over early-error offsets for this fixed topology. It does NOT solve the general original strict-stop mother problem.

Frozen knowledge inputs: GLOBAL_KNOWLEDGE_V1 main@104a8e9dabd6198aeb9994305ea4fd4f4eea0d12; Enterprise Math main@7a590c60e49a420b88518fec60818ac3b70a4b7d. Prior auxiliary route-memory theorem: PR #1663 @66e9d11b112b048dbf9d067fa2a6d765b110ad72. Current proof uses typed positive P/Q branch masses and does not assert an X6 physical embedding, Foundation admission, or any modification of P000 or the ACTIVE worldview.

## Entire legal strict-stopping model

Time 2: natural X=0/1 is observed; each policy chooses STOP at 2 or CONTINUE. Only surviving branches sample U=0/1; at time 3, Y=1 causes actual STOP at 3 while Y=0 leads to compulsory STOP at 4. There is no nonterminal routing policy action, no persistently remembered random seed, and STOP really terminates a path.

P and Q continuation-path masses, ordered (X,U)=(00,01,10,11), are

   P=(7/40,9/40,3/40,21/40),    Q=(7/20,3/20,3/20,7/20).

All four are strictly positive and sum to 1 in each law. Time-2 P/Q ratios are 4/5 for X=0 and 6/5 for X=1, hence LR can choose early survival probabilities s_0,s_1 separately. At time 3 the X branches collide at ratio 1/2 for U=0 and 3/2 for U=1; seedless LR uses one shared Y stopping probability y_u per U, whereas FULL may use distinct y_{x,u}. All behavioral choices are real numbers in [0,1].

Both laws have the common terminal error-probability kernel: after early STOP, k_early(X)=1/4+X/8+d_X; after survival, k_late(X,Y)=1/4+X/8+XY/8. The COMPLETE strict probability-legality domain of the two arbitrary real early-error increments is

   -1/4 < d_0 < 3/4,      -3/8 < d_1 < 5/8.

All late error values 1/4,3/8,1/2 are legal. Terminal Bernoulli errors realize the declared probabilities. Observe O=(eP,eQ,TP,TQ) with expected terminal errors and actual stopping times.

## Theorem: one fixed integer support inequality works for EVERY legal pair

Define the signed four-observer functional

   L(O) = 12 eP + 25 TP - 12 TQ.

Then for EVERY real pair (d_0,d_1) in the entire open legal rectangle and EVERY admissible real behavioral policy,

   sup_FULL L = 895/16,
   sup_seedless_LR L = 559/10,
   sup_FULL L - sup_LR L = 3/80 > 0.

Both suprema are attained by deterministic policies; the values are independent of d_0,d_1. Thus no early-error tuning in this entire rectangle can make the FULL and LR FOUR-dimensional convex hulls equal. In particular, the positive margin cannot be removed merely by changing the earlier STOP reward while keeping the stated late P error kernel, path masses, collisions and stopping times.

**Proof — forcing both routes to survive at the maximizer.** Write w^L_{xu} for the joint continuation-path masses and pi^L_x=sum_u w^L_{xu}. Relative to early STOP, the increment in L contributed by survival of route X=x with arbitrary late stop probabilities y_{x,u} is

   D_x = sum_u (2-y_{x,u})*(25 w^P_{xu}-12 w^Q_{xu})
         + 12 * [ (x/8)*sum_u w^P_{xu} y_{x,u} - d_x*pi^P_x ].

The same expression holds for LR after substituting y_{x,u}=y_u. The exact collision ratios imply

   25 w^P_{x0}-12 w^Q_{x0}=(1/2) w^Q_{x0},
   25 w^P_{x1}-12 w^Q_{x1}=(51/2) w^Q_{x1},

both positive. Since 0<=y<=1, hence 2-y>=1, and the positive xY term is nonnegative, for EVERY possible real late behavior

   D_0 > (1/2)*(7/20)+(51/2)*(3/20)-12*(2/5)*(3/4) = 2/5 > 0,
   D_1 > (1/2)*(3/20)+(51/2)*(7/20)-12*(3/5)*(5/8) = 9/2 > 0.

The strict signs use only the two upper endpoints of the legal rectangle; its lower endpoints cause no problem. Thus EVERY L-maximizing FULL or LR policy necessarily continues both branches at time 2: s_0=s_1=1. All d-dependent error terms vanish from both support optima.

**Proof — exact late collision split.** At full survival, changing one late decision y_{xu} from 0 to 1 changes L by the signed mass

   g_{xu}=12*(1/8)*x*w^P_{xu}-25*w^P_{xu}+12*w^Q_{xu}.

The four exact gains in order 00,01,10,11 are

   g_00=-7/40,    g_01=-153/40,    g_10=3/80,    g_11=-651/80.

FULL independently maximizes the four variables: its unique maximizing late choice is y_10=1, with the other three y's zero. LR must share the late decision across X, so its gain for U=0 is g_00+g_10=-11/80<0 and for U=1 is g_01+g_11=-957/80<0. The unique LR maximizing late choice is y_0=y_1=0.

Under LR all paths continue to time 4, yielding

   O_LR^max=(13/40,5/16,4,4),       L=559/10.

Under FULL all paths survive time 2 but only the X=1,U=0 branch stops at time 3, yielding

   O*=(107/320,53/160,157/40,77/20),   L=895/16.

Therefore L(O*)-sup_LR L = 895/16-559/10 = 3/80. This is an exact all-real proof, not a grid experiment. QED.

As |12|+|0|+|25|+|-12|=49, the unscaled coordinate L-infinity distance from this fixed FULL O* to the ENTIRE seedless LR real image is at least

   (3/80)/49 = 3/3920.

This is a valid uniform lower bound, not a claim that the metric distance is optimal. The earlier note independently certified full affine dimension four for the LR convex hull at d_0=d_1=0, using a nonzero 21/64000 determinant; loss of convex-hull equality here is not an artifact of a low-rank baseline.

## Independent exact checker and validation boundary

VERIFY_UNIFORM.py uses Python standard-library Fraction and independently recomputes the four-coordinate observations. It checks the full/ LR support values by exhaustive enumeration of 64 FULL and 16 LR deterministic policies at SIXTEEN exact rational pairs distributed across the legal rectangle, including points near each boundary; checks the exact global route survival lower bounds 2/5 and 9/2, witness coordinates, coefficients and gap. The actually executed stdout is EXACT_UNIFORM_OUTPUT.txt and ends PASS_EXACT_R5_ALL_LEGAL_EARLY_ERROR_OFFSETS_NO_GO. Universal quantification over the entire open real rectangle follows from the displayed inequalities and signed-gain proof, not from those 16 tests. No independent Driver review, formal Lean checking or native Source admission is claimed.

## Boundaries and discriminating next problem

This closes the complete two-parameter early-error search in the FIXED natural censor/STOP diamond. The narrower wedge from RESEARCH.md remains a true stronger-margin subcase (its different signed direction yields a gap 3/10), but its NEXT_TASK.md is superseded by this theorem. Q-error changes alone, if they preserve P path masses/decisions and the P/Q likelihood-key filtration, cannot repair this particular P/T separation, because the functional ignores eQ. Other strictly stopping models, path kernels, late P-error interactions, stopping epochs or observer designs are NOT ruled out.

Next: vary a terminal P-error interaction at the late collision itself (for example independent coefficients for X*Y*1_{U=0} and X*Y*1_{U=1}) and/or modify the positive P/Q diamond path weights while retaining two exact LR collisions, then derive full signed FULL/LR Bellman envelopes. First establish exact four-dimensional convex-hull equality or a certified separator; only a hull-equal candidate advances to actual real-image separation. Preserve stop-as-absorption and source-labelled BRC paths.