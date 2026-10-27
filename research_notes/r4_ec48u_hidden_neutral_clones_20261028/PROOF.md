# EC48U — History-dependent source-neutral cloning: terminal LR descent and an eight-leaf predictive obstruction

Date: 2026-10-28. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. Author-side independent portable research; NOT a native CLAIM, Result, Driver review, Lean theorem or X6 dynamics result.

## Source and authority pins

Global GLOBAL_KNOWLEDGE_V1 current read snapshot: awdawmip/chatgpt-global-knowledge main@fc4f25deacc2f1d4fda13ddf18b93f23ebc7615a. The immutable global bootstrap/manual, project router, original P000, ACTIVE worldview, and mathematical/code/Research Activity/BRC policies were read at this one snapshot. Project source read: awdawmip/enterprise-math main@0927aadb568bb1152579f2c3102399cb00772723, including AGENTS, AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN, PORTABLE_RESEARCH_PROTOCOL, activity protocol, native X6/time and joint-observer-preservation constraints. Publication branch is based on refreshed project main b2ae357431fef548a065950ac2362310459bf4c7. Prior EC48T result is Draft PR #1595, commit 4cad523163f2698cd24d961c260e2ed0d7cf8125, not accepted canonical mathematics.

Native status read: enterprise_math 0.6.11, research_authority_granted=false and active_jobs=5/5. The native tasks/owner read returned CONTROL_QUOTA, so actual active owner and native CLAIM remain unverified. Historical local role label: EM-R004-K7E48K, TASK_RESEARCH; not a native session identity.

Only a finite, strictly positive, two-source auxiliary probability BRC observer model is studied. A time index is an ordered stop stage, NOT native X6 spatial geometry. No signed/phase cancellation, native dynamical transfer, or information loss outside an expressly defined observation/future-operation scope is claimed.

## Model

P and Q are strictly positive laws on the same finite branch tree. An m-state policy carries exactly m possible memory states and uses source-independent private randomization, with fresh coins not acting as hidden unlimited persistent memory. Stop/continue and terminal accept/reject actions are available at specified decision times. The original (not convexified) four-dimensional observation region is S_m = {(alpha,beta,E_P T,E_Q T)} over all such randomized policies.

A new visible clone label j of old terminal symbol i has positive kernel r(j|h,i) that may depend on physical hidden prefix h but is the SAME under P and Q conditional on h,i; summing over j returns the original path law. Distinguish a terminal-only clone with no future operations from a clone before another controllable transition.

## U1 — history-dependent terminal clones preserve the ENTIRE raw region when full joint LR is observable

Fix any number m >= 1, any finite positive P,Q laws, any source-independent history-dependent clone kernel and any legal preterminal randomized policy. Suppose the clone is generated ONLY at the final accept/reject decision and cannot change earlier stop times or later physical transitions. Suppose the old terminal decoder sees its original old observation z INCLUDING the complete physical path likelihood ratio L(h,i)=P(h,i)/Q(h,i). Then

  S_m(old) = S_m(refined)

as exact original four-coordinate sets, even if r(j|h,i) depends arbitrarily on forgotten h.

PROOF: Fix a fine m-policy and copy its preterminal controls and state-update rules in the old experiment. At a surviving physical old terminal path (h,i) and preclone controller state s, let w_Q(h,i,s) be Q(h,i) multiplied by its source-independent conditional probability of survival and state s. Let z contain all old visible terminal observations including L(h,i). Fold all fine terminal decisions (including a possible terminal state update) into an acceptance probability a(s,z,j) between 0 and 1.

For every nonzero-Q fiber F(s,z) of paths having the same s and z, define

  b(s,z) = (sum over (h,i) in F of w_Q(h,i,s) times sum_j r(j|h,i)a(s,z,j)) / (sum over (h,i) in F of w_Q(h,i,s)).

This is a legal source-independent randomized old acceptance rule because 0 <= b <= 1 and the denominator is positive. Choose b arbitrarily on zero-Q-mass fibers. Its Q accepted mass equals that of the fine controller fiber by construction. On every member of the fiber P(h,i)=L(z)Q(h,i), and survival/state coins are source-independent given the physical path, so w_P=L(z)w_Q. Multiplication by that SAME L(z) proves exact equality of P accepted mass as well. Sum fibers. Stopping-time moments were fixed before the terminal clone and hence are unchanged. Conversely lift every old controller by ignoring j. Both inclusions yield equality. QED.

This strengthens EC48T's terminal-only theorem by REMOVING the assumption that the clone kernel is independent of hidden history, but ONLY with the explicitly observable complete physical joint LR. The simulated old rule reproduces the declared P/Q accept masses; it need not recreate individual clone-label histories or future updates.

## U2 — four-leaf counterexample if full joint LR readout is removed

Hidden past h in {A,B} was observed previously but is forgotten by the one-state register at the last decision. P(A)=3/4, P(B)=1/4, Q(A)=1/4, Q(B)=3/4. The old terminal symbol i is constant and the last decoder CANNOT see L(h). Any old one-state accept rule has alpha=beta, so max(alpha-beta)=0.

Refine i to j in {1,0} with r(1|A)=3/4 and r(1|B)=1/4; complements are positive, and the kernel is identical under both sources conditional on h. All FOUR physical (h,j) leaves are strictly positive. Accept iff j=1 yields (alpha,beta)=(5/8,3/8), optimal fine alpha-beta=1/4. With full old joint LR readout L(A)=3 and L(B)=1/3, the old randomized rule b(3)=3/4,b(1/3)=1/4 exactly reproduces (5/8,3/8). Thus U2 is NOT a counterexample to U1.

## U3 — strictly positive eight-leaf preterminal predictive-information counterexample WITH joint LR readout

The finite tree has:

Stage t=1: h in {A,B}, P(h)=Q(h)=1/2; advance to t=2 is MANDATORY. A one-state register cannot retain h.
Stage t=2: old observation i is constant, refined observation j in {1,0} is sampled conditionally on h with r(1|A)=3/4, r(1|B)=1/4 (positive complements), independent of the source. The controller STOPs with T=2 or CONTINUEs to t=3. Every current full physical LR L(h,j)=1. Even marginally P(j=1)=Q(j=1)=1/2, so j has zero immediate source-discrimination value.
Stage t=3 after CONTINUE: y in {1,0} is independent of j conditional on h. At A, P(y=1|A)=3/4, Q(y=1|A)=1/4; at B, P(y=1|B)=Q(y=1|B)=1/2. All eight refined (h,j,y) leaves are strictly positive. At the final decision FULL joint LR is observable: L(A,y=1)=3, L(A,y=0)=1/3, L(B,y)=1. No additional register state or persistent random tape is available. Acceptance at a stop at t=2 also sees LR=1.

Consider the linear support objective J_c=alpha-beta-c(E_P T+E_Q T), c>=0. Remove the common mandatory t=2 time cost by W_c=J_c+4c. Exact one-state optimal supports are

  W_old(c) = max(0, 1/4-2c),
  W_fine(c)= max(0, 3/16-c)+max(0, 1/16-c).

PROOF: Stopping at t=2 yields no alpha-beta payoff because LR=1. At t=3, optimal terminal accept is the sign decision 1{L>1}, independently of j. Only the A,y=1 branch contributes positive source discrimination. In old m=1, with current i and LR constant, the continuation probability t cannot depend on h. Always continuing yields a source-discrimination advantage P(A)(3/4-1/4)=1/4 and an extra P+Q stop-time cost of 2c. Random t therefore yields t(1/4-2c), optimized at an endpoint. In fine m=1, j IS currently visible at the stop/continue decision, so there are two separate continuation probabilities t_1,t_0. Their discrimination gains are P(A)r(1|A)(1/2)=3/16 and P(A)r(0|A)(1/2)=1/16; each j has P+Q mass 1 and so costs c if continued. Optimizing independently over t_1,t_0 yields W_fine above. The LR-sign accept policy attains these bounds and randomization cannot beat them. QED.

Hence the exact support deficit W_fine-W_old is STRICTLY POSITIVE if and only if 1/16<c<3/16. At c=1/8,

  W_old=0,   W_fine=1/16,
  J_old=-1/2,   J_fine=-7/16,
  gap = 1/16.

One achieving fine one-state policy CONTINUEs only when current j=1; at t=3 it accepts exactly when current physical LR>1. Its exact observation vector is

  (alpha,beta,E_PT,E_QT)=(9/32,3/32,5/2,5/2).

At that stop-time pair old one-state controllers can achieve at most alpha-beta=1/8, versus 3/16 in the fine region. Therefore BOTH the raw four-coordinate region and its convex hull change, despite source-neutral clones, full path LR access and zero instantaneous discrimination at the cloned stage. The mechanism is prediction of which hidden h will yield useful FUTURE source information, not discrimination by the current j itself.

This eight-leaf tree is a strictly positive rational certificate, not a proof of global minimum leaf count; the obligatory t=1 advance and exact memory/decision interface are essential.

## U4 — sufficient causal simulator when clone is born before future operations

Let o be the old controller's currently available observation at clone-birth time. If the clone kernel is policy-independent, source-independent and factors pointwise as r(j|h,o)=kappa(j|o) for every compatible hidden h, AND j has no direct causal effect on future physical transitions conditional on hidden history and controller actions, any fine m-policy can be simulated old-side: sample a virtual j from kappa upon observing o, then execute the fine controller's decision/register update. Induction on stages couples all physical transitions, future signals, actions and stop times under both P and Q. Ignoring j gives the reverse inclusion. Therefore S_m equality holds at all declared horizons. A policy-specific factorization through (o,state) also suffices if its sampling and update are implementable with that same register.

This is a SUFFICIENT causal factorization criterion, NOT a necessary one or an X6 bisimulation theorem. Conditioning only on a marginal P/Q law after hidden-history mixing is not pointwise causal factorization.

## U5 — memory repair for this particular eight-leaf tree

For U3 with TWO states, old can encode h in the register after mandatory t=1, then at t=2 privately sample a virtual j with its correct r(j|h), sample any fine policy's hypothetical preclone memory if necessary, and execute the fine t=2 and t=3 rules with the same two-state register. There was no discretionary t=1 action to preserve. This emulates every refined two-state policy. Ignoring j gives the converse inclusion, hence S_2(old)=S_2(refined) for THIS exact tree, whereas U3 shows S_1(old)!=S_1(refined).

## Executed exact evidence and limits

The published VERIFY.py is the executed author-side Python Fraction verifier; EXACT_REPORT.json is its exact-rational output. It checks positive mass and normalization on four/eight leaves, source-neutral kernels, 16 terminal decoder extremes, exact eight-leaf support/gap and policy vector, 21 rational c checks with 2 old and 4 fine deterministic continuation rules, and 83 positive rational policies (166 exact P and Q reconstructions) on a three-history/two-state LR-collision test. The universally quantified fiber and causal theorems rely on the complete proofs above, not extrapolation from finite tests. No independent mathematical review, Lean build, native BRC–Shor run, native Source Result/CLAIM, or typed X6 embedding has been performed.

Prior art: Blackwell/garbling and decision-relative value of information are classical (bibliography in SOURCES.md). The author's line-specific increment is the exact terminal LR descent despite hidden-history clone dependence, a strict preterminal stop-cost certificate over a continuous rational interval, and the future-operation/simulator distinction. Next proposed portable unit is EC48V in NEXT_TASK.md.
