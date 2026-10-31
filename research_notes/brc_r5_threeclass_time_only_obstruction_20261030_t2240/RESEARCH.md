# R5 — Time-only support separator excludes all terminal-error compensation on the fixed three-class STOP tree

Date: 2026-10-30 Asia/Shanghai. Author-side research: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is a portable proof, not a formal Source CLAIM, native Result, or independent review.

## Sources and frozen assumptions

Verified GLOBAL_KNOWLEDGE_V1 main snapshot c74665ab9a707af30b7836313b50ccabb305abac; Enterprise Math canonical-main input dcdc00698333555b11e175150cf0ca6118dddef8. Global P000 startup projection matched the canonical P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Scientific predecessor: research_notes/brc_r5_binary_lr_markovization_threeclass_20261030_t2138/RESEARCH.md at commit f68cf18321962f2502c0de505879722ee27d2e9a (Draft PR #1663). The predecessor showed a 1/1024 signed gap involving the error coordinate, and proposed searching error-kernel compensation on the same twelve masses.

Use three genuine STOP/CONTINUE decisions at times 2,3,4. STOP absorbs immediately; CONTINUE from time 4 absorbs at time 5. Natural source X and intermediate state U are binary. Under Q,

Q(X=0,U=0)=3/8, Q(0,1)=1/8, Q(1,0)=1/8, Q(1,1)=3/8.

The stage-3 likelihood ratios are r_0=3/4, r_1=5/4. The three stage-4 ratios are R_0=1/2,R_1=1,R_2=3/2. Put t_0=1/16,t_1=1/8, and define conditional Q transition triples

K_(x,0)=(1/2+t_x,1/2-2t_x,t_x);
K_(x,1)=(t_x,1/2-2t_x,1/2+t_x).

Set Q(x,u,v)=Q(x,u)K_(x,u)(v) and P(x,u,v)=R_v Q(x,u,v). All 12 P and Q masses are positive, normalize to 1, and satisfy sum_v K_(x,u)(v)R_v=r_u. The time-2 ratios for X=0,1 are respectively 7/8 and 9/8. FULL knows X,U,V history at decision; LR knows only (time, likelihood ratio) and has no persistent random seed. In particular LR at time 3 cannot distinguish the two X values with the same U.

Four observations are (e_P,e_Q,T_P,T_Q). Error kernels can be ANY legal terminal-only probabilities, possibly law-, source-, path- and stop-time-sensitive. They must not alter the natural P/Q masses, available actions, stopping times or reveal additional data before stopping. All error compensation on this fixed stopping tree is included; altered natural kernels, new feedback observations or changed timing are not.

## Theorem (universal terminal-error-independent no-go)

For EVERY legal terminal error assignment, the signed time-only observer functional

H = 7 T_P - 6 T_Q

has exact global behavioral-policy support extrema

sup_FULL H = 1509/256,
sup_LR H = 1507/256,
FULL minus LR = 1/128 > 0.

Thus the time-observer convex hulls already differ, and therefore the four-observer FULL and LR convex hulls cannot be equal for ANY terminal-error compensation. This is an all-real-behavior theorem, not a finite parameter sweep.

An exact FULL maximizing witness continues at both time-2 sources, stops at time 3 only at (X,U)=(0,0), continues at time 3 everywhere else, and at time 4 stops on V=0 and continues on V=1 or 2. It yields

(T_P,T_Q) = (1119/256,527/128), H=1509/256.

For any error coordinates of the witness, every LR observation has H<=1507/256, giving the 4D sup-norm separation

d_infinity(O_witness,O_LR) >= (1/128)/(7+6) = 1/1664.

## Full analytic proof

Every realized trajectory visits each (time, LR) control key at most once. Hence holding all other behavioral probabilities fixed, the expected H is affine in a given control probability, including one LR probability shared across histories. The total map is multiaffine on the compact FULL or LR action cube: a maximum of a linear support is attained at deterministic vertices. A persistent mixture seed cannot improve this support. We may optimize binary STOP/CONTINUE choices below, with the result applying to ALL real behavioral policies.

The all-stop-at-time-2 baseline is H=2(7-6)=2. Continuing a Q mass at current likelihood ratio r for one additional time unit has gain 7r-6 per Q mass. Thus the optimal time-4 CONTINUE gain for each terminal V is

L_v=max(0,7R_v-6)=(0,1,9/2).

Continuing at time 3 rather than stopping, after optimizing time 4, yields per unit Q(X,U) the signed gain

G_xu = 7r_u-6 + sum_v K_xu(v) L_v.

Direct exact substitution gives (G_00,G_01,G_10,G_11)=(-3/32,181/32,1/16,93/16).

FULL can independently continue at each time-3 history if its G is positive. Its time-2 continuation gains at the two sources are

E_x^FULL = sum_u Q(x,u)[(7r_u-6)+max(0,G_xu)].

They equal (E_0^FULL,E_1^FULL)=(197/256,25/8). Both are positive, so the FULL support is 2+197/256+25/8=1509/256.

For LR, the time-3 continuation choice h_u in {0,1} is shared between the two sources at fixed U. At time 2 the sources remain distinguishable and may each stop or continue optimally:

E_x(h)=sum_u Q(x,u)[(7r_u-6)+h_u G_xu];
H_LR(h)=2+sum_x max(0,E_x(h)).

Exactly four pairs exist. Their complete values are

h=(0,0): H=3;
h=(0,1): H=1507/256;
h=(1,0): H=761/256;
h=(1,1): H=375/64.

The largest is 1507/256, achieved by deterministic LR behavior. All-real behavioral extrema are therefore as stated. The two suprema are different, establishing both convex-hull inequality and strict real-image separation. For any four-vectors z,w, |H(z)-H(w)| <= 13 ||z-w||_infinity, which gives 1/1664. QED.

The terminal error probabilities do not occur in any of these formulas. In contrast with the predecessor's mixed error/time separator, no adjustment of terminal error can close this gap. The previous fixed-twelve-mass compensation subproblem is now excluded as a whole. Preserve the quantifier: other P/Q path weights, LR information partitions, stopping topologies or feedback models are NOT excluded.

## Exact execution and literature boundary

VERIFY.py, run with Python standard-library Fraction and integers, independently checks both law normalizations, twelve positive paths, the two LR collisions and conditional martingale identities, all Bellman support values, and completely enumerates 262144 FULL and 128 LR deterministic policies with mass units 1/256. It checks the explicit witness. EXACT_OUTPUT.txt is captured actual stdout ending PASS_EXACT_R5_THREECLASS_TIME_ONLY_ALL_ERROR_NO_GO. Exhaustion checks the finite combinatorial certificate; the displayed proof gives all-real scope. This is not a Lean formalization, an empirical claim or an accepted project theorem.

R. Laroche and R. Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, ICML/PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html, is a general occupancy-Markovization context, not evidence of priority for this fixed-tree calculation. P/Q are nonnegative and source-tagged branch masses, not signed amplitudes; exact LR collisions preserve hidden X as BRC-relevant provenance until observation. This is an auxiliary finite probability model, with no claimed transfer to native X6/Heartbeat physics. P000 and protected ACTIVE worldview remain unmodified.

## Actual authority and next question

At this run, native em_status reported research_authority_granted=false, source control CODE_REVIEW_REQUIRED, 5/5 active jobs, and executor_binding_configured=false. No current Source owner, own CLAIM, Result, or independent Driver acceptance was obtained. GitHub saving is neutral author-side preservation, not native admission.

NEXT_TASK.md: change something that affects time behavior, not merely error kernels. First screen the two-dimensional (T_P,T_Q) convex hull by exact all-signed support; only time-hull-equal candidates deserve 4D exact rational primal/Farkas certificates, and only 4D-hull-equal candidates deserve real-image semialgebraic separation.
