# R5 — Two-law predictive lumpability and four-observer residual envelope

Date 2026-10-28 Asia/Shanghai. Author-side identity LOCAL_EMR5_20261028_1340_LUMP_Q_761B / TASK_RESEARCH (local provenance only). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. Inputs: GLOBAL_KNOWLEDGE_V1 main@4faffbe68584637f37d630e345543a8f7300f394 and Enterprise Math main@06980818839db31c9a2e4b01f41d0829bd0171da. Predecessor: research_notes/brc_r5_fiberwise_bellman_double_collision_20261028_t1243/RESEARCH.md and NEXT_TASK.md; its eight-leaf support gap 1/16 rules out that earlier model as a mother witness.

## Question and exact scope

The R5 mother problem asks for a strictly positive rational passive two-law sequential observation tree with equal four-dimensional convex hulls of full-history and no-persistent-seed likelihood-ratio (LR) behavioral policies, but unequal true four-images. Observation is O=(e_P,e_Q,T_P,T_Q) with e_P=P(declare Q), e_Q=Q(declare P), T_mu=E_mu stopping stage. This note derives a safe-compression gate for arbitrarily many interacting nonterminal LR collisions, and a quantitative signed-support bound for heterogeneous predictive fibers. It is an external finite auxiliary P/Q model with stages t=1,...,N, not a native Heartbeat World X6 dynamics; native lifting requires Cell embedding, readout and future-relation preservation.

Let each raw history h at time t have strictly positive p_h,q_h and r_h=p_h/q_h. LR fibers F=(t,r) group histories of the same time and ratio. Stop-P, stop-Q and continue are the three nonnegative behavioral probabilities summing to one (continue is zero at N). For each nonterminal history define K_h^Q(s)=sum_{child h' with r_h'=s} q_h'/q_h and K_h^P(s)=sum p_h'/p_h=(s/r) K_h^Q(s). These are finite probability kernels on next-step LR values. For mu in {P,Q}, set
delta_F^mu=max_{h,g in F} TV(K_h^mu,K_g^mu), TV(k,l)=sum_s|k(s)-l(s)|/2, with zero for singleton F;
delta_t^mu=max_{F at time t}delta_F^mu;
D_mu=min(1,sum_{t=1}^{N-1}delta_t^mu).

## Theorem A — real-policy Markovization and quantitative control

For every full-history behavioral policy pi there exists a *genuine* no-persistent-random-seed LR policy pi_bar such that
|e_P(pi)-e_P(pi_bar)|<=D_P, |T_P(pi)-T_P(pi_bar)|<=(N-1)D_P,
|e_Q(pi)-e_Q(pi_bar)|<=D_Q, |T_Q(pi)-T_Q(pi_bar)|<=(N-1)D_Q.
Under each law mu, the total-variation distance between the complete terminal (stopping stage, declaration) distributions is at most D_mu.

For every signed lambda in R^4, if V_C(lambda)=min_{pi in C} lambda·O(pi), then
0<=V_LR(lambda)-V_full(lambda)
<=(|lambda1|+(N-1)|lambda3|)D_P+(|lambda2|+(N-1)|lambda4|)D_Q.

Corollary B: if delta_F^Q=0 at all nonterminal LR fibers, then delta_F^P=0 too and the *actual four-images* are equal: O_LR=O_full for **all real behavioral strategies**. The constructed LR policy preserves each P/Q time-and-ratio occupation marginal and the terminal (stage,declaration) law, but need not preserve complete raw-path or hidden-source laws. A successful mother counterexample must have at least one predictive-heterogeneous nonterminal LR collision. This condition is necessary for the sought unequal true four-images, not sufficient; nonzero delta alone never proves any support gap.

At a fixed fiber ratio r, the exact two-law change-of-measure identity is:
TV(K_h^P,K_g^P)=(1/(2r))sum_s s|K_h^Q(s)-K_g^Q(s)|.
Thus P/Q diameters are separately typed, generally unequal, and Q-zero is equivalent to P-zero.

### Complete constructive proof

For pi let R_h be its conditional probability of reaching h before stopping, independent of which measure governs observations. Define Q reach weights w_h=q_h R_h. For each fiber F with W_F=sum_F w_h>0 average *all three* actions:
bar a_F^j=(sum_{h in F}w_h a_h^j)/W_F, j in {stop-P,stop-Q,continue}.
If W_F=0 choose any valid three-action probabilities. This defines a real LR behavior strategy using only (t,r) and fresh local randomness. Since P reach weight is p_h R_h=r w_h for every h in F, the full policy's action averages at F are exactly the same under P as under Q, including conditional terminal declarations.

For either law mu, conditional on being active at F the full process's next-fiber distribution after continue is a convex mixture of {K_h^mu:h in F}, with mixture weights its source-specific continuation masses. The new LR policy's conditional next-fiber distribution is another convex mixture of the very same set, with mixture weights determined by its own reached raw histories. Two such convex mixtures have TV distance at most delta_F^mu: expand their difference into pairwise source kernels and use TV convexity. Both processes assign the same probability to stopping and each terminal declaration at F.

Augment the fiber state space with absorbing outcomes (t,declare-P) and (t,declare-Q), preserving stopping time. Although the full policy may be history-dependent, its one-time marginal active-fiber flow admits the conditional mixture kernel just described. The resulting two time-indexed stochastic kernels differ by at most delta_t^mu in TV on each active fiber, and agree on absorbing states. Stochastic-kernel TV contraction and the triangle inequality yield
TV(rho_{t+1}^pi,rho_{t+1}^barpi)<=TV(rho_t^pi,rho_t^barpi)+delta_t^mu.
Their t=1 fiber marginals coincide. Induction to forced stopping at N proves TV of the terminal (t,label) law at most D_mu. Each error coordinate is a terminal event probability; each expected stopping stage lies in [1,N] and thus changes by at most (N-1)D_mu. A full objective minimum exists by compactness of the finite behavioral parameter cube, and LR policies are a subset of full ones; apply this constructed LR approximation to a full minimizer to obtain the uniform signed support bound. For delta=0 the recursion is equality at each stage and every terminal joint distribution agrees. For all h,g at ratio r, K_h^P(s)-K_g^P(s)=(s/r)(K_h^Q(s)-K_g^Q(s)), proving the stated ratio identity. QED.

This argument does not infer universal results from numerical enumeration. It also does not assert historical novelty of strong Markov lumpability or general occupation Markovization.

## 20-history double-level collision example and exact test

At t=1 the distinct observed tags A,B have P=Q=1/2 each, thus a nonterminal ratio-1 collision. At t=2 each tag has three children with LR (1/2,1,3/2) and Q conditional row (1/4,1/2,1/4), hence P conditional row (1/8,1/2,3/8). Each of the three t=2 LR fibers contains A/B histories; all admit stop/continue, and their reach depends on the t=1 decision. From each t=2 history, t=3 has Q binary row (1/2,1/2) and child LR multipliers (3/4,5/4), so P row (3/8,5/8). There are 20 observed histories, 12 positive leaves, and 10 LR fibers. All P/Q masses normalize. The P/Q predictive diameters are zero on every nonterminal fiber, giving exact true-image equality despite several interacting collisions.

The independently implemented full policy in VERIFY.py uses different rational stop/continue actions on each A/B source and descendant and different rational terminal declarations. The exact fiber-averaged LR construction reproduces all per-time P/Q occupation and stopped (time,label) distributions, with
O_full=O_LR=(73189/143360,8691/17920,3473/1920,863/480).

An exact perturbation changes the tag B conditional t=2 Q row to (1/8,3/4,1/8), retaining child ratios and therefore the P row (1/16,3/4,3/16). t=2-to-t=3 transitions remain unchanged. Now delta_1^P=delta_1^Q=1/4, delta_2^P=delta_2^Q=0. The bound for all signed lambda is
V_LR(lambda)-V_full(lambda)<=|lambda1|/4+|lambda2|/4+|lambda3|/2+|lambda4|/2.
For the displayed full policy and its constructed LR approximation the four absolute observation errors are exactly
(56509/88309760,295/602112,431/394240,177/197120).
They are nonzero and within the certified per-coordinate envelope (1/4,1/4,1/2,1/2). This is **not** a claim of a positive optimal support gap.

Executed Python Fraction verification covers normalization, four nonterminal collision fibers, precise occupation and stop tables for both laws, kernel diameters, the two explicit policies, and 128 additional deterministic rational full-policy inputs (64 for each family). Full run output is in EXACT_OUTPUT.txt and ends ALL EXACT TWO-LAW FIBER MARKOVIZATION CHECKS PASSED. The real-policy theorem is established symbolically above; the 128 tests are finite regression evidence.

## BRC and literature provenance

BRC REUSE_APPLIED: positive rational labeled P/Q branch masses, explicit source tags and time, exact LR ratio, occupied Q mass for averaging, and a residual carrier of *differences of positive predictive kernels*. Information is reduced only with an exact observer/future-operations certificate or the quantified TV bound. This is not BRC–Shor or native X6 computation.

General strong lumpability is classical Kemeny–Snell territory; compare the exposition in https://link.springer.com/article/10.1007/s10959-026-01500-w , §4. Occupancy equivalence of non-Markovian and randomized Markov policies is an established topic; see Laroche and Tachet des Combes, PMLR ICML 2023 https://proceedings.mlr.press/v202/laroche23a.html . The task-specific derivation here specializes these themes to simultaneous P/Q likelihood-ratio fibers and an explicit quantitative bound for O; absence of prior publication of this exact specialization is not asserted.

## Live authority and next research step

On the 2026-10-28 13:40 Asia/Shanghai read, em_status had research_authority_granted=false and em_control_tasks returned CONTROL_QUOTA, preventing a trustworthy current Source owner determination. Authenticated GitHub login was awdawmip. GitHub notes do not create CLAIM, Result, or independent Driver review; preserve the author-side provenance and UNREVIEWED / NOT_ADMITTED status.

Next build predictive-heterogeneous **interacting** collision fibers (delta_F^Q>0), preferably heterogeneity at two nonterminal time levels. Compute sourcewise Bellman D_h for each candidate full exposed normal and check global optimality and terminal declarations. Establish equality of all signed four-dimensional support functions before investigating true-image nonmembership. Use the TV residual bound as a screening envelope, not as a zero-gap proof. See NEXT_TASK.md.
