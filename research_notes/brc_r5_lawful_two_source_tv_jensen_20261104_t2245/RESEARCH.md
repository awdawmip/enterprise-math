# R5: two-source lawful stopping and a total-variation Jensen separator

Date: 2026-11-04. Author-side research, analytic proof plus exhaustive rational instance. Research status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Research connection and scope

Continuation of the Fréchet joint-occupancy source at enterprise-math@475b308c09eeaa3cd6c3332bf7eeb8797d2e46ea, research_notes/brc_r5_frechet_joint_occupancy_20261104_t2147/RESEARCH.md. That model established a nonconvex seedless independent-action surface with matching convex hull under an auxiliary four-coordinate observer. This note tests the causal stopping-and-declaration vocabulary of original R5 and isolates a measurable obstruction: variation in the conditional value of terminal information across histories sharing the same time/likelihood-ratio key.

Scientific input pins retained: global a01383f825ef9d43b4b754254303298c64041568; enterprise-math 86149263e38c22292c9def1e0f69092efa1be77e. P000, ACTIVE Heartbeat World, and joint-relation observer policy retained as starting constraints. The finite probability experiment below is an explicitly typed statistical observer; it makes no independent native spatial-dimension claim.

## Positive finite BRC construction

At time 1, chance reveals a finite source h in H with P(h)=Q(h)=w_h>0, sum_h w_h=1. Hence every source shares the likelihood-ratio key (t=1,R=1), though FULL remembers h. Available time-1 actions are STOP_P, STOP_Q and CONTINUE. A continuation reveals at time 2 a terminal signal s from a finite set S_h with strictly positive conditional probabilities P_h(s), Q_h(s); then the controller stops and freely declares P or Q. The terminal likelihood ratio is R(h,s)=P_h(s)/Q_h(s). A seedless LR strategy uses only (t,R), with independent behavioral randomization at each key; FULL may use the full observed path. All observations use O4=(eP,eQ,TP,TQ), where eP=P(declare Q), eQ=Q(declare P), and TP,TQ are expected stopping times.

Write delta_h=TV(P_h,Q_h)=(1/2) sum_s |P_h(s)-Q_h(s)| and delta_bar=sum_h w_h delta_h. Set n_lambda=(-1,-1,-lambda,0) for lambda>=0.

### Theorem: signed stopping support and information-heterogeneity residual

For every such finite positive experiment, and for all real lambda>=0,

h_FULL(n_lambda)=-(1+lambda)+sum_h w_h (delta_h-lambda)_+,

h_LR(n_lambda)=-(1+lambda)+(delta_bar-lambda)_+.

Consequently the exact support difference is

D(lambda)=sum_h w_h (delta_h-lambda)_+ -(delta_bar-lambda)_+ >= 0.

At lambda=delta_bar,

D(delta_bar)=(1/2) sum_h w_h |delta_h-delta_bar|.

Thus any unequal pair of conditional total-variation values produces a strictly positive gap in the four-coordinate convex hull, witnessed by n_{delta_bar}. The residual is half the mean absolute variation of terminal information value across merged source histories.

Proof. An immediate stop gives eP+eQ=1 per unit source mass regardless of the P/Q declaration because P(h)=Q(h). Its time contribution to lambda*TP is lambda. At terminal time 2, minimization of eP+eQ selects declaration P where R>1 and Q where R<1, with either choice permitted for R=1. This selector uses only the terminal LR key and attains conditional total error sum_s min(P_h(s),Q_h(s))=1-delta_h. Continuing from source h improves total error by delta_h and increases TP by one. FULL chooses continuation independently for each h and therefore selects the positive part (delta_h-lambda)_+, giving the first support formula.

Seedless LR must use one common time-1 continuation probability c for all h since their keys equal (1,1). Conditional on continuation, the same terminal LR threshold R>1 attains sum_h w_h(1-delta_h)=1-delta_bar. The objective is affine in c; its optimal value adds (delta_bar-lambda)_+. This proves the second formula. Convexity of v -> (v-lambda)_+ yields nonnegativity. Since sum_h w_h(delta_h-delta_bar)=0, positive and negative deviations have the same total magnitude, establishing the formula at lambda=delta_bar. If the delta_h are unequal, that positive total is nonzero. QED.

The formula measures variation of the future experiment, not a mere source-label difference. It gives a direct topology filter before attempting the R5 mother question's equal-hull requirement.

## Exact rational two-source certificate

Let H={A,B}, w_A=w_B=1/2, S={+,-}, and Q_A(+)=Q_A(-)=Q_B(+)=Q_B(-)=1/2. Set
P_A(+)=3/4, P_A(-)=1/4;
P_B(+)=5/8, P_B(-)=3/8.

Every transition has positive P and Q probability. Terminal LR keys are respectively 3/2, 1/2, 5/4, 3/4; they are all distinct. The two time-1 histories collide at R=1.

delta_A=1/4, delta_B=1/8, delta_bar=lambda=3/16, so D=1/32. In the FULL witness choose CONTINUE on A, STOP_Q on B, and at time 2 declare P for + and Q for -. This is a legal deterministic history strategy. Its full observation vector is

W=(eP,eQ,TP,TQ)=(5/8,1/4,3/2,3/2).

For n=(-1,-1,-3/16,0), exact support values are
h_FULL(n)=-37/32,
h_LR(n)=-19/16,
h_FULL(n)-h_LR(n)=1/32.

Since ||n||_1=35/16, dual-norm separation gives

dist_infty(W,conv O4(LR)) >= (1/32)/(35/16)=1/70.

The support values use the complete real behavioral policy classes. The first-stage dependence is affine in each behavioral continuation choice, while terminal Bayes declarations optimize linearly; therefore deterministic policies attain these maxima.

## Exhaustive executable rational witness check

VERIFY.py enumerates all 3^2 * 2^4 = 144 deterministic FULL settings (two time-1 source actions, four terminal declaration actions) and all 2+2^4=18 effective deterministic LR settings. It computes the exact O4 vector under P and Q with Fraction, checks support at seven rational penalties, independently checks the formula, W and the infinity-distance lower bound. The saved output includes the PASS marker. The analytic theorem covers arbitrary finite H and positive conditional P/Q distributions; verification exhaustively covers the stated rational example.

## Relation to verified external theory

Anderson and Montúfar, "The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes", ICML 2026, PMLR 306:2677-2715, https://proceedings.mlr.press/v306/anderson26a.html, characterizes feasible value-function sets for infinite-horizon POMDPs with memoryless stochastic policies as semi-algebraic. It is context for the nonlinear seedless-image program; the theorem here is a self-contained finite-horizon likelihood-ratio calculation.

## Scientific return and exact next question

We obtained a lawful stop/continue/free-declaration positive-P/Q example with a strict hull gap and a sharp general formula for the source-heterogeneity obstruction. To pursue a true R5 hull-equal but image-unequal construction, couple at least two stopping resources or branches and test whether their signed support residuals cancel simultaneously in all four observation directions, retaining the seedless polynomial dependence. Compute all FULL deterministic O4 vertices and LR deterministic O4 vertices, then obtain exact convex certificates before semialgebraic nonmembership analysis. No mathematical-admission or formal CLAIM inference is made by this author-side note.
