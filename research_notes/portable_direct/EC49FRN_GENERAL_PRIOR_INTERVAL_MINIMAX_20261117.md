# EC49FRN — General uncertain-prior interval: exact minimax regret with two native trees

Date: 2026-11-17. Parent EC49FRM and inherited EC49FRJ/EC49FRL. Frozen original BRC pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Status AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / INHERITED_GLOBAL_ENVELOPE_NOT_REVIEWED. Research-only portable publication, no Task/CLAIM/Result/Review or Activity authorization.

## Exact proposition

Hold the same 141 complete named states, 310 original configuration multiplicities, all 228 original native physical observations, full signed/port provenance and exact BRC response semantics. Price ratio x=r/t is any fixed real x>=1 and the *unknown* prior mixing parameter lies in an arbitrary closed interval [a,b] within [0,1], with a<b. A prior-blind policy chooses an original complete exact native tree using a coin before any observation. No original physical observation changes.

For deterministic native tree Q, C_Q(x,lambda)/t=(1-lambda)(U_T+x U_R)/141+lambda(M_T+x M_R)/310. Let V(x,lambda) be the inherited author-checked *global original native Bellman* value min{A,B,C,D,E}. Define its endpoint chord

ell(lambda)=(b-lambda)V(x,a)/(b-a)+(lambda-a)V(x,b)/(b-a).

**Theorem.** Among ALL prior-blind randomized exact original native trees, the precise minimax expected regret over the unknown prior interval is

R*(x;[a,b])=max_{lambda in [a,b]} [V(x,lambda)-ell(lambda)].

A mixture of at most TWO of the five original fully named BRC trees attains it. Both trees have original worst-case observation depth three. It suffices to evaluate at most two native prior breakpoints plus the interval endpoints; exact fractional probability formulas below provide a constructive globally optimal randomized protocol.

## Finite explicit evaluator

In the order (U_R,U_T,M_R,M_T), the inherited exact source vectors are:
A=(6,290,6,751), B=(5,293,5,704), C=(5,295,5,685), D=(4,296,4,707), E=(4,298,4,688).

Source: EC49FRL_GLOBAL_FIVE_TREE_DEPTH3_CERTIFICATE.json, SHA256 2164b2a374c46bad29d5b669573fcafe87218f946e1bdd42e78dc78642ba0dfb, indexed by PR #2630. The predecessor global Bellman envelope PR #2624 remains author-proved, not independently reviewed.

Set beta=620/3299 and, for 1<=x<3,

alpha(x)=[(3-x)/141] / [(3-x)/141+(x+47)/310].

Exact comparison of the five original native cost vectors gives global winning sequence A, B, C as lambda increases on 1<=x<3, with prior switches alpha(x) then beta; 0<alpha(x)<beta. At x>=3 the only switch is beta, with winner D on its left and E on its right. Equal-cost boundary ties are harmless.

Compute exact V at a,b. Let s=[V(x,b)-V(x,a)]/(b-a). Evaluate phi(lambda)=V(x,lambda)-ell(lambda) at {a,b} and at any of {alpha(x), beta} strictly inside (a,b), omitting alpha when x>=3. Pick lambda* maximizing phi. If the maximum is zero, use a native tree that is optimal at both endpoints; no randomization is needed. Otherwise among the original native Bellman trees active at lambda*, select one of minimal slope s_L=dC_L/dlambda and one of maximal slope s_H=dC_H/dlambda. The maximizing-kink condition ensures s_L<=s<=s_H. Choose the higher-slope tree with probability

q_H=(s-s_L)/(s_H-s_L)

and the lower-slope tree otherwise. Their mixed expected-cost line touches V at lambda* with slope s, so the expected regrets at a and b both equal R*. The construction is exact for all real admissible x,a,b.

## Proof of *global* minimax (not only five-tree restricted)

Every original deterministic tree has cost affine in lambda; the same is true under a prior-blind lottery. V is concave, being the minimum of these affine values. Hence the regret is convex and reaches its maximum at the two prior interval endpoints.

For ANY policy P and ANY lambda in [a,b], put theta=(b-lambda)/(b-a). Then

max{G_P(a),G_P(b)}
>= theta G_P(a)+(1-theta)G_P(b)
 = E_P[C_Q(x,lambda)]/t - ell(lambda)
>= V(x,lambda)-ell(lambda).

Maximizing over lambda gives the universal lower bound, independent of the original native tree chosen by P.

The function phi=V-ell is concave piecewise affine and zero at both endpoints. At any interior maximizing kink lambda*, its left derivative is >=0 and right derivative <=0. The upper and lower slopes of the original Bellman lines active at lambda* therefore straddle the chord slope s. Mixing those two genuine native trees with q_H above yields an expected cost line passing through V(lambda*) with slope s. Its endpoint regrets are exactly phi(lambda*) and dominate all interior regrets by convexity. If phi is zero throughout, an active tree in an interior point is affine and globally optimal on the interval. Thus the universal lower bound is attained with at most two original native trees. QED.

## Closed forms

If exactly one prior kink c∈(a,b) occurs, and the slope drop between its adjacent active native trees is kappa>0, then

R* = kappa (c-a)(b-c)/(b-a),

and the left-optimal tree is sampled with probability (c-a)/(b-a).

For x>=3, c=beta and kappa=2/141+19/310=3299/43710. Thus if a<beta<b,

R*=(3299/43710)(beta-a)(b-beta)/(b-a);

otherwise the exact minimax regret is zero. On 1<=x<3, intervals meeting only alpha use A/B and kappa_A=(3-x)/141+(x+47)/310; intervals meeting only beta use B/C and kappa_B=3299/43710. Intervals meeting both use the finite two-knot evaluator.

EC49FRM for [a,b]=[0,1] follows as a special case with regret 19(5-x)/3299 (1<=x<=3) and 38/3299 (x>=3).

## Reproduction, limits, next problem

A separate exact Fraction verifier tested 84 (x,a,b) combinations (7 prices ×12 rational prior intervals), including zero-, one- and two-kink intervals. For each it constructed only original complete tree choices, verified both endpoint regrets equal the dual lower bound, and tested several interior fractions. The formula for all real parameters is proved by the affine/concavity argument rather than finite samples. An executable verification script is co-published.

The only load-bearing inherited mathematical input is the prior author-checked global five-tree Bellman envelope, still NOT_REVIEWED. No stronger future-X6 or native heartbeat dynamics claim follows from a static finite-observer result. Next: unrestricted deterministic minimax-regret Pareto frontier and genuinely multidimensional prior uncertainty, where a two-tree support bound may change.
