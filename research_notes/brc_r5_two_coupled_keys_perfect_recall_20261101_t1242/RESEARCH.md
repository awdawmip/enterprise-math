# R5 — Perfect-recall obstruction and a full-rank nonconvex two-collision time–likelihood-ratio model

**Author-side portable mathematical research, 2026-11-01 (Asia/Shanghai).** Status: `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. The four-observer mother question remains OPEN. This note proves a structural prerequisite, realizes an actual full-rank nonconvex LR image, and eliminates that concrete candidate by a strict signed support certificate; it does not assert a hull-equal witness.

## Frozen inputs and typed scope

- `GLOBAL_KNOWLEDGE_V1` canonical `main@0192c9363f655febaf25285457bb73f200f61feb`, including its bootstrap/manual, EM TASK router, P000 startup projection, canonical original P000 (Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matching the projection), and ACTIVE worldview.
- Enterprise Math canonical control `main@85f90349600ef59f4cf9fcda5201d50be257772e`, including `AGENTS.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, and `control_plane/current_control_authority.json`.
- Immediate R5 frontier: `472593aa1b2a47ae7b1623255318e82b3b61d8a8`, `research_notes/brc_r5_single_root_convex_images_20261101_t1142/` on PR #1663.
- The present tree is an **external auxiliary finite decision model**. P000's six-dimensional native space, three-dimensional slice and discrete residual-faithfulness are untouched. Its four-dimensional observer chart is **not** four native spatial coordinates. In the BRC source/port discipline, the primitive quantities here are nonnegative separately labelled P/Q path masses. Only after terminal aggregation do signed support differences occur; those are not probability masses.

## Theorem 1 — perfect recall makes behavioral terminal-flow images convex

Let a finite rooted decision/nature tree have strictly positive exogenous nature-path weights under two fixed probability laws P and Q. At every behavioral information set I, the agent uses the same randomized action distribution under P and Q. Suppose the agent has **perfect recall**: every decision history in I carries the same sequence of the agent's earlier information sets and its own earlier actions. In particular no information set is revisited on a path. The laws of nature do not depend on the agent's randomization mechanism.

Then the set of **joint P/Q terminal-history flow vectors** attainable by real behavioral strategies is convex and equals the convex hull of deterministic-strategy flow vectors. Hence every fixed linear observer of these flows has a convex actual behavioral image. For a FULL perfect-history policy class containing this LR class, if their convex observer hulls are equal, their actual real observer images are equal. Consequently **a FULL/LR convex-hull-equal but actual-image-unequal witness necessarily has an LR information partition that fails perfect recall**, provided the stated finite-tree/fixed-law/shared-behavior premises hold.

**Constructive proof.** Take two behavioral strategies `b1,b2` and a real mixture weight `λ∈[0,1]`. For every information set I, let `h(I)=((I1,a1),...,(Ik,ak))` denote its unique remembered own information/action trace. Define `s_j(I)=∏_{m=1}^k b_j(am|Im)` for j=1,2; these are independent of the nature history inside I and of the law P/Q. Let `s(I)=λs_1(I)+(1−λ)s_2(I)`. For `s(I)>0` set

`b(a|I)=[λs_1(I)b1(a|I)+(1−λ)s_2(I)b2(a|I)]/s(I)`;

for `s(I)=0` choose any valid action distribution. Perfect recall makes this choice consistent at all histories in I. Induction along each remembered own-action trace gives its realization factor `s_b(trace)=λs_1(trace)+(1−λ)s_2(trace)`. The probability of any terminal history z under law L∈{P,Q} is its **fixed nature likelihood** `ν_L(z)` times this own-action realization factor. Therefore both P- and Q-terminal probabilities under b equal their coordinatewise λ-mixtures under b1,b2. This proves convexity **simultaneously under both laws**, not by choosing law-specific conditional policies. Because no key repeats on a path, the terminal probabilities are multiaffine in the independently assigned information-set behavioral probabilities and are mixtures of deterministic profiles. Their convex hull is therefore exactly the actual set. FULL has perfect recall too, so the stated implication follows. □

**Prior art boundary.** The perfect-recall mixed/behavioral realization equivalence is classical (Kuhn 1953); we do **not** claim this general result as new. The contribution here is its explicit two-law shared-randomization derivation, its application as an exact necessary filter for the `(eP,eQ,TP,TQ)` mother question, and the fully verified time–LR instance below. Public references: Harold W. Kuhn (1953), *Extensive Games and the Problem of Information*, in *Contributions to the Theory of Games II*; a current Lean blueprint explaining the realization argument: https://gametheoryinlean.github.io/blueprint/game_theory/extensive_game/game_theory_extensive_game_imperfect_information_perfect_recall_mixed_to_behavioral.html . No Lean check of this note has been performed.

## Theorem 2 — two *genuinely coupled* true time–LR collisions can have a full-rank nonconvex LR image

Nature initially chooses hidden source A1,A2,B,C with strictly positive masses:

| source | P(source) | Q(source) | initial P/Q |
|---|---:|---:|---:|
| A1 | 1/8 | 1/8 | 1 |
| A2 | 1/8 | 1/8 | 1 |
| B | 1/4 | 1/8 | 2 |
| C | 1/2 | 5/8 | 4/5 |

At **time 1**, A1/A2 meet common LR key `I=(1,1)`: STOP (probability p under LR) returns fixed terminal answer Q at time 1; CONTINUE runs an exogenous low/high split. For A1 the conditional (P(low),Q(low)) is `(1/2,1/4)`; for A2 it is `(3/4,3/8)`. High terminates at time 2 with answer P. Low arrives at **time 2** at shared LR key `J=(2,2)`; source B **bypasses key I** and also reaches J. At J, STOP (probability q under LR) answers Q at time 2. CONTINUE ends at time 3: A2 and B answer Q, while A1 gets an additional exogenous X/Y signal with conditional `(P(X),Q(X))=(3/5,1/2)`, `(P(Y),Q(Y))=(2/5,1/2)` and answers P for X, Q for Y. Source C has its own private time-1 key `(1,4/5)`: STOP probability r answers P at time 1, CONTINUE answers Q at time 3.

All declared nature-edge probabilities are strictly positive and sum to one under each law. The terminal answer is a single deterministic function of **terminal (time, exact P/Q likelihood ratio)**, including `(3,12/5)→P`, `(3,8/5)→Q`, `(3,2)→Q`; all nine distinct terminal keys and all 729 interior FULL strategy grids were checked for this consistency. Source-tagged events are kept separate in the computation. The likelihood ratio of a history is the ratio of its **exogenous P and Q probabilities**; common behavioral action factors cancel. Thus A1/A2 at I both have ratio 1; their low descendants reach J with ratios `1×(1/2)/(1/4)=2` and `1×(3/4)/(3/8)=2`, while B has ratio 2. Both collisions are genuine: A1 and A2 have different future nature kernels; J aggregates descendants of I with bypass B. No information key is revisited along a path. At J, paths from A1/A2 remember `(I,CONTINUE)` but B has no earlier I, so LR **violates perfect recall**.

LR has independent real parameters `p,q,r∈[0,1]`; FULL has `p1,p2,q1,q2,qB,r∈[0,1]`. The same behavioral randomization is used under P and Q. Define `eP=P(answer Q)`, `eQ=Q(answer P)`, `TP=E_P[terminal time]`, `TQ=E_Q[terminal time]` (time measured in integer ticks), and `O=(eP,eQ,TP,TQ)`.

By direct expansion of all 13 labelled terminal-event flows, for **every real** `p,q,r∈[0,1]`,

`O_LR(p,q,r)=O0+p B+q C+pq D+r E`, with

- `O0=(139/160, 3/16, 93/32, 181/64)`;
- `B=(21/160, −3/16, −13/32, −21/64)`;
- `C=(3/80, −1/64, −13/32, −13/64)`;
- `D=(−3/80, 1/64, 5/32, 5/64)`;
- `E=(−1/2, 5/8, −1, −5/4)`.

The **exact determinant** of the four coefficient columns `det[B C D E]=233/163840>0`. The LR affine hull therefore has **full rank four**, and the observer map is an injective affine image of the abstract graph `G(p,q,r)=(p,q,pq,r)` (with the monomial `pq` interpreted as a coordinate, not an independent policy parameter).

The LR actual image is **nonconvex over all real behavioral parameters**. Its two legal points `O_LR(0,0,0)=O0` and `O_LR(1,1,0)=(1,0,9/4,19/8)` have midpoint

`M=(299/320, 3/32, 165/64, 333/128)`.

Injectivity would require for an LR policy realizing M the coefficient tuple `(p,q,pq,r)=(1/2,1/2,1/2,0)`. But `p=q=1/2` implies `pq=1/4≠1/2`. Therefore M lies in the LR convex hull and **outside its entire actual real image**. This supplies the previously missing **typed time–likelihood-ratio realization** of the bilinear nonconvex mechanism (not merely the earlier abstract chart). □

## Theorem 3 — exact signed separator kills this candidate for hull equality

Take the signed observer direction `H=eP+TQ` in integer-tick time units. From the expansion,

`H_LR(p,q,r)=1183/320+(−63p−53q+13pq)/320−(7/4)r`.

For all real parameters in the cube, `−63p−53q+13pq ≤ −50p−53q ≤ 0`. Therefore **`max_LR H=1183/320`**, attained at `(p,q,r)=(0,0,0)`. For the legal FULL deterministic source policy `(p1,p2,q1,q2,qB,r)=(0,0,1,0,0,0)`, direct terminal-flow evaluation gives

`O_FULL=(29/32,11/64,91/32,179/64)`, hence `H_FULL=237/64=1185/320`.

Thus `max_FULL H−max_LR H≥1/160>0`. Exhaustive exact enumeration of all 64 FULL vertices proves equality here: `max_FULL H=237/64`. Multiaffinity of every full-policy parameter implies the enumeration computes the real continuous FULL maximum, not merely a sampled bound. Consequently

`conv(O_FULL) ≠ conv(O_LR)`, and `dist_∞(O_FULL,conv(O_LR)) ≥ (1/160)/(|1|+|1|)=1/320`.

This two-collision model **achieves rank four and nonconvex LR actual image**, but does **not** solve the mother question because its convex hulls are strictly separated. □

## Exact computation, verification scope, and limitations

`VERIFY.py` is a runnable, source-labelled P/Q exact-flow checker using only Python standard-library `Fraction`. It calculates 13 event masses per strategy, checks P/Q normalization, all 729 strictly interior FULL parameter tuples and terminal LR-measurable response consistency, 192 full-policy multiaffinity midpoint identities, 125 LR rational cube points against the displayed polynomial identity, all 64 FULL and eight LR deterministic vertices, the exact determinant, the nonconvex midpoint, the signed support extremum and witness. Recorded output: `PASS_EXACT_R5_TWO_COUPLED_KEYS_PERFECT_RECALL_OBSTRUCTION` in `EXACT_OUTPUT.txt`. Universal real-parameter conclusions rely on the explicit polynomial derivation and the perfect-recall constructive proof; finite rational tests separately check the concrete arithmetic and enumeration.

**Actual native authority observed during this study:** gateway `em_status` version `0.6.11` returned `research_authority_granted=false`, `executor_binding_configured=false`, current control `CODE_REVIEW_REQUIRED`, authenticated-subject active quota `5/5`. A bounded read-only `em_control_tasks` request returned `CONTROL_QUOTA`, so the active formal owner could not be established. No native CLAIM, Result, review, Driver promotion or independent replication was executed. Publication to an author-side research/PR frontier is evidence persistence only.

**Scope boundaries:** terminal decisions here are a predeclared function of terminal `(time,P/Q)`; the optimization concerns stopping/continuation at earlier keys. This is a finite strictly positive auxiliary dual-law decision model, not a native X6 theorem. No novelty priority is asserted for perfect-recall realization equivalence. The project still needs a coupled collision that preserves rank four **and** eliminates every signed FULL/LR support gap, then an all-real LR nonmembership certificate.
