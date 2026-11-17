# EC49FRM — Global minimax-regret policy for the frozen native BRC identification class

Date: 2026-11-17. Parent: EC49FRL (PR #2630), EC49FRJ (PR #2624). Immutable scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Status: AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / INHERITED_GLOBAL_ENVELOPE_NOT_REVIEWED. This is independent portable science, not a Task CLAIM, Result or Review.

## Original model and precise additional policy layer

Use all 141 original full-named states, their 310 original configuration multiplicities, and all 228 original physical BRC observations. No states, response paths, port labels, observer provenance, future operations or X6 native components are identified or discarded. For real x=r/t >=1 and real lambda in [0,1], the state prior is p_i(lambda)=(1-lambda)/141+lambda*m_i/310. The terminal observation costs t>0, the root observation costs xt. An exact deterministic native tree Q has normalized cost

C_Q(x,lambda)/t=(1-lambda)(U_T(Q)+x U_R(Q))/141 + lambda(M_T(Q)+x M_R(Q))/310.

V(x,lambda) denotes the exact *global* Bellman minimum over all original deterministic native trees. The inherited EC49FRJ author-checked theorem supplies V=min{A,B,C,D,E} on the entire stated domain; EC49FRL replays all five exact original full-named native trees and shows maximum query depth three. That inherited global-envelope proof is load-bearing and is still pending independent review.

The added policy layer chooses one of the complete original trees with an external random coin *before* observations start, without knowing lambda, and then executes it unchanged. The sampling does not alter the original BRC observation algebra, physical costs, original multiplicities or a query response.

## Theorem: global minimax expected regret for an unknown prior

Let P be any probability distribution on exact original native identification trees (not necessarily drawn from the five named candidates) with finite expected cost. Define G_P(x,lambda)=E_P[C_Q(x,lambda)]/t - V(x,lambda). Then for every fixed real x>=1:

R*(x) := inf_P sup_{lambda in [0,1]} G_P(x,lambda)
       = 19(5-x)/3299  if 1<=x<=3,
       = 38/3299       if x>=3.

A globally optimal protocol uses only two original trees:
* If 1<=x<=3: choose B with probability 310(5-x)/3299, and C otherwise.
* If x>=3: choose D with probability 620/3299, and E otherwise.

All realized trees have native worst-case query depth exactly three. Both protocols give identical expected costs at x=3 (the individual response/path distributions need not match). For comparison, the best deterministic tree within the certified five has worst-case regret (5-x)/141 on [1,3] (C), and 2/141 above 3 (E). This randomized protocol lowers that five-tree deterministic upper bound by exactly 620/3299, approximately 18.79%. The unrestricted deterministic minimax problem is separately open.

## Exact inherited integer vectors

Each row lists (U_R,U_T,M_R,M_T), where U counts named paths and M counts paths with the *original* multiplicity:

A=(6,290,6,751)
B=(5,293,5,704)
C=(5,295,5,685)
D=(4,296,4,707)
E=(4,298,4,688).

Source: EC49FRL_GLOBAL_FIVE_TREE_DEPTH3_CERTIFICATE.json, SHA256 2164b2a374c46bad29d5b669573fcafe87218f946e1bdd42e78dc78642ba0dfb, preserved in the verified original EC49FRL complete archive, indexed by PR #2630. This is a finite original BRC static-observer problem, not an assertion about arbitrary later six-axis heartbeat dynamics.

Set beta=620/3299. Exact affine comparisons and the inherited global envelope give
* lambda=0, x in [1,3]: V=(290+6x)/141 (tree A);
* lambda=0, x>=3: V=(296+4x)/141 (tree D);
* lambda=1, x in [1,3]: V=(685+5x)/310 (tree C);
* lambda=1, x>=3: V=(688+4x)/310 (tree E);
* lambda=beta, x in [1,3]: B and C both attain V;
* lambda=beta, x>=3: D and E both attain V.

The equality at beta follows from 2(1-beta)/141 = 19 beta/310, i.e. beta=620/3299. B/D and C/E tie in total cost at x=3 for every prior.

## Full proof

**Endpoint reduction.** For each fixed native tree, cost is affine in lambda. A policy independent of lambda retains that affinity under expectation. V is a minimum of affine costs and thus concave. Therefore G_P is convex and its maximum over lambda in [0,1] occurs at lambda=0 or 1.

**Universal dual lower bound.** For every P and beta=620/3299,

max{G_P(x,0), G_P(x,1)}
>= (1-beta)G_P(x,0)+beta G_P(x,1)
 = E_P[C_Q(x,beta)]/t - [(1-beta)V(x,0)+beta V(x,1)]
>= V(x,beta) - [(1-beta)V(x,0)+beta V(x,1)]
 = L(x).

The last inequality is true for *every* exact native tree (and any mixture), not just the five examples, because V is the global Bellman infimum. Substitute the three displayed exact global Bellman values: L(x)=19(5-x)/3299 for 1<=x<=3, and L(x)=38/3299 for x>=3.

**Attainment for 1<=x<=3.** The lambda=0,1 regret vectors are B: ((3-x)/141,19/310) and C: ((5-x)/141,0). Put q=310(5-x)/3299, which is a probability in [620/3299,1240/3299]. The mixture (q B)+(1-q C) gives the same endpoint regret on both priors:

(5-x-2q)/141 = 19q/310 = 19(5-x)/3299.

Since the regret is convex in lambda, the endpoint maximum controls every real interior prior. This achieves the universal L(x).

**Attainment for x>=3.** The lambda=0,1 regret vectors are D: (0,19/310) and E: (2/141,0). Sample D with probability q=beta. Both endpoint regrets equal

(1-beta)*2/141 = beta*19/310 = 38/3299.

This again achieves the universal lower bound for every real prior. Hence the stated formula and global optimality among all prior-blind randomized exact native tree policies. QED.

## Verification and scope

Exact rational/symbolic recomputation checked the original five cost vectors, lambda=0,beta,1 Bellman affine domination over both entire x intervals, the dual lower-bound identities and both endpoint-equalizing mixtures. A runnable verifier and execution log accompany this note. The algebraic proof (rather than finite samples) covers all real x>=1 and lambda in [0,1]. No expensive original native Bellman calculation was rerun; the analysis relies explicitly on the inherited all-prices theorem at its existing author-verified, not-independent-review status.

Next questions: exact global deterministic minimax regret over *all* native trees; minimax policy on an arbitrary proper mixture interval [lambda_minus,lambda_plus] and the resulting parameter-cell decomposition; observer-root versus expected regret Pareto tradeoff with explicit constraints on using randomness.
