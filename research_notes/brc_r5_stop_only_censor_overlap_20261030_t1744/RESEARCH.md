# R5 — Exact overlap obstruction for a strict-stopping route-memory compiler

Date: 2026-10-30, Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is a negative theorem for one defined strict STOP/CONTINUE family, not an impossibility theorem for all stopping-only models.

## Sources and model scope

Frozen GLOBAL_KNOWLEDGE_V1 canonical main@104a8e9dabd6198aeb9994305ea4fd4f4eea0d12; Enterprise Math canonical main@7a590c60e49a420b88518fec60818ac3b70a4b7d. Account bootstrap/manual, P000, ACTIVE worldview, joint-observer retention, BRC and portable research protocol read at these pins. Exact predecessor: Draft PR #1663 @66e9d11b112b048dbf9d067fa2a6d765b110ad72, research_notes/brc_r5_nonterminal_route_memory_20261030_t1640/PARAMETRIC_EXTENSION.md.

Previous R5 auxiliary example used a NONTERMINAL choice of route X and established full-rank convex-hull identity but differing real images. The strict original STOP/CONTINUE mother question remained OPEN. Here we test a natural literal stopping-only compilation rather than rename the nonterminal action. No native X6 physical embedding or P000 modification is claimed.

Nature chooses X in {0,1}. At time 2 the policy sees X and either STOPS forever at t=2 or CONTINUES. Only survivors sample U in {0,1}; at time 3, Y=1 STOPS at t=3 while Y=0 CONTINUES to compulsory stopping t=4. A fixed would-be joint continuation-path mass table, in order XU=00,01,10,11, is:

              00       01       10       11
P             7/40     9/40     3/40     21/40
Q             7/20     3/20     3/20     7/20
P/Q           1/2      3/2      1/2      3/2

Every P/Q mass is strictly positive, normalized, and induces strictly positive conditional U kernels given X and continuation. At time 2 the X likelihood ratios are 4/5 and 6/5, so seedless LR may choose two distinct survival probabilities s_0,s_1. At time 3 the two X histories COLLIDE exactly for each U: likelihood ratios 1/2 and 3/2. Thus LR must use shared stopping probabilities y_0,y_1 at time 3, whereas FULL may choose y_{00}, y_{01}, y_{10}, y_{11}. Both laws use identical behavioral decisions; LR has no persistent random seed.

Let c,a,b be real constants, b nonzero. Early stop has terminal error probability c+aX+d_X, later stop has terminal error probability c+aX+bXY, with ALL stated terminal probabilities strictly between 0 and 1. Both measures use the same error kernel. The four observation coordinates are O=(eP,eQ,TP,TQ), expected terminal error and actual stop time under each law. For law L with path weights w^L_{xu} and pi^L_x=sum_u w^L_{xu}:

 e_L = c+a*pi^L_1 + sum_x pi^L_x*(1-s_x)*d_x + b*sum_u w^L_{1u}*s_1*y_{1u}
 T_L = 2+2*sum_x pi^L_x*s_x - sum_{x,u} w^L_{xu}*s_x*y_{xu}.

For LR put y_{xu}=y_u. U is only actually sampled along surviving routes. Summing latent would-be U weights is a bookkeeping identity, not a claim that early-stopped paths remain alive.

## Theorem (all real parameters and behavioral strategies)

Assume strictly positive P/Q path weights, LR recognition of X at t=2, and collision of X histories indexed by U at t=3 as above. Suppose b != 0 and the legal early error shifts satisfy d_0/b <= 1/2 and d_1/b <= 1. For the signed functional

 H(O) = (2/b)*eP + TP,

the EXACT difference between FULL and seedless LR supports over all real behavioral strategies is

 Delta_H = max_FULL H - max_LR H
         = Gamma_P := sum_u min(w^P_{0u},w^P_{1u}) > 0.

Thus the two FOUR-coordinate convex hulls are strictly different throughout this entire legal, real, two-parameter wedge. If the time-2 LR ratios coincide, the same Gamma is still a lower bound against the formally larger policy class permitted separate s_0,s_1 (do not call it exact for the smaller LR class).

Proof: Put pi_1=P(X=1). Relative to time-2 stopping, survival at route x followed by late stopping probability y has H-increment

 G_x(y) = 2 + (2x-1)*y - 2*d_x/b.

At the stated inequalities, G_0(y)>=0 and G_1(y)>=0 for every y in [0,1]. Hence both classes have an H-optimum with s_0=s_1=1, and early shifts disappear from the optimum. In FULL, independently maximize every late decision: y_{0u}=0, y_{1u}=1, giving

 max_FULL H = (2/b)*(c+a*pi_1) + 4 + pi_1.

For LR at all-continue, the common y_u has marginal H coefficient w^P_{1u}-w^P_{0u}. Therefore

 max_LR H = (2/b)*(c+a*pi_1) + 4
            + sum_u max(0,w^P_{1u}-w^P_{0u}).

Subtract; pi_1=sum_u w^P_{1u} yields Gamma_P by min(A,B)=B-max(0,B-A). Positivity gives Gamma_P>0. Every optimization is over actual real seedless behavioral probabilities; the pointwise argument is universal. This proves exact signed support separation and hence strict convex-hull inequality. Q-error perturbations preserving the same P law and LR filtration cannot remove this P-only signed separation. QED.

Gamma_P=(1-sum_u abs(w^P_{1u}-w^P_{0u}))/2 is a typed positive-branch source-overlap statistic, not signed-branch cancellation. Its positivity directly measures the hidden-route decision coupling under LR. The BRC positive labelled branch carrier and its observer-specific quotient are preserved.

## Explicit full-affine-rank certificate

Choose c=1/4, a=b=1/8, and d_0=d_1=0. All actual error probabilities are among 1/4,3/8,1/2. The same theorem holds at every legal real (d_0,d_1) with d_0<=1/16 and d_1<=1/8.

The P overlap is min(7/40,3/40)+min(9/40,21/40)=3/10. H=16*eP+TP. The FULL deterministic policy s_0=s_1=1 and y_{xu}=x produces

 O* = (2/5, 3/8, 17/5, 7/2),    H(O*)=49/5.

ALL real seedless LR policies and ALL mixtures of them satisfy

 16*eP+TP <= 19/2.

Exact support gap 49/5 - 19/2 = 3/10. Thus distance in the UNSCALED four-coordinate infinity norm from O* to the entire LR image is at least (3/10)/17 = 3/170. No claim of optimal metric distance. Crucially the LR convex hull itself already has affine dimension FOUR: the difference determinant of LR observation indices (0,4,5,6,8) in VERIFY.py's lexicographic enumeration is exactly 21/64000, nonzero.

## Executed evidence and exclusions

VERIFY.py (Python standard library Fraction) actually executed and enumerated 64 deterministic FULL and 16 LR strategies, verified the two genuine exact LR collisions, strictly positive normalized P/Q kernels, exact signed support maxima, explicit witness, 4D determinant and four legal rational early-error pairs including wedge boundaries. Original stdout is EXACT_OUTPUT.txt, ending PASS_EXACT_R5_STOP_ONLY_CENSOR_COMPILER_NO_GO. The finite computation checks the displayed rational instances and deterministic extremal structure, while the proof covers the entire stated real family.

This eliminates the specific natural compiler that turns the auxiliary nonterminal route into an exogenous X with optional literal early STOP/censor and late additive bXY error. It DOES NOT eliminate different stop/continue topologies, early error offsets outside the wedge, richer lawful law-specific errors, or a genuinely different observation kernel. The original strict-stopping mother question remains OPEN. This is author-side portable research, not a source-native CLAIM, Result, Driver review or mathematical admission.

Next problem: leave the certified wedge, vary legal early-stop d_0,d_1 or P/Q-specific early error kernels while retaining both collisions and real stop semantics; derive exact full signed Bellman envelopes and test all-direction FOUR-dimensional hull equality by rational vertex combinations or Farkas certificates before asking about actual real-image separation.