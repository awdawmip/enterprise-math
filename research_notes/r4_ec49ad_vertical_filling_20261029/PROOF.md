# EC49AD — Exact vertical filling of the fixed-cost causal observation region

Date 2026-10-29. Status AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Scientific predecessor EC49AC PR #1686 at immutable 1b22692744f9d790200fa8b257f2d04fa6e42c5a.

## Exact model and theorem

Histories w=0,1,2 have prior 1/3. First actions are STOP, A0/A1 (cost 1), B0/B1 (cost 2). Conditional signal t_w(u)=1/2+(2u-1)(1-w)/200. Source masses P(w,u,z)=t_w(u)*(1/6 if w=z, else 1/12) and Q(w,u,z)=t_w(u)/9, for u=0,1 and z=0,1,2. Each source has 18 strictly positive leaves, normalized to 1; P and Q have identical (w,u) marginals. After forgetting w, optional sensor S is purchased according only to (c,u) and terminal acceptance depends only on observations available then. Behavioral coins are fresh, no persistent initial mixture seed. Set (C1,C2)=(43/48,7/8) in both sources and alpha=P(accept), beta=Q(accept), delta=alpha-beta.

Let D=59/576. Let L(d) on 0<=d<=D be EC49AC's exact piecewise-affine lower boundary through six knots (d,L(d)):
(0,0), (17/288,17/96), (3047/38400,3641/12800), (19/192,25/64), (1939/19200,3067/6400), (59/576,109/192).

THEOREM: The COMPLETE real behavioral feasible two-dimensional projection at the fixed costs is exactly:
- -D <= delta <= D, beta=alpha-delta.
- For 0<=delta<=D: L(delta) <= alpha <= 1-3delta.
- For -D<=delta<=0: -3delta <= alpha <= 1-L(-delta).

Every point is realizable using ONE FIXED initial sensor prefix and S always bought after any paid action, with local fresh terminal Bernoulli coins. Consequently the fixed-cost (alpha,beta) projection is a compact CONVEX POLYGON, even though variable-cost/full-policy regions need not be convex. All rational target pairs have rational policies.

## Necessity for ALL real causal policies

EC49AC's analytic convex-prefix reduction plus exact 288-vertex proof yields the sharp lower graph L(d) for every real d in [0,D] and the universal maximum discrimination D. Acceptance-complement symmetry implies delta>=-D.

On each raw leaf P/Q is 3/2 for w=z and 3/4 otherwise. Therefore pointwise 4P-3Q>=0. Every legal terminal observation and every rejection event is a nonnegative mixture of these source leaves with the SAME behavioral policy. On the rejection event this yields:
4(1-alpha)-3(1-beta)=1-alpha-3delta >= 0.
Thus alpha<=1-3delta. Complementing any admissible acceptance rule yields (1-alpha,1-beta,-delta), with unchanged costs and no extra memory, giving the stated negative-delta upper and lower bounds. All constraints are therefore necessary for arbitrary real strategies.

## Sufficiency through a single legal prefix (not initial strategy mixing)

Fix w=0 -> A0 with probability 1; w=1 -> A1 with probability 1; w=2 -> A0 with 9/16, B0 with 1/16, STOP with 3/8. Always buy S after every paid action. Under both sources C1=43/48 and C2=7/8 exactly, and unconditional STOP mass is 1/8.

For sensed atom j=(c,u,z), write p_j=P(j), q_j=Q(j), d_j=p_j-q_j. Explicit exact source calculation (VERIFY.py) gives 8 positive, 10 negative and 6 zero/empty atoms, and:
sum_(d_j>0) d_j = D,
sum_(d_j<0) d_j = -D,
for ALL d_j<0: p_j=-3*d_j,
sum_(d_j<0) p_j=3D.
The negative-atom identity also follows algebraically: every negative j in this prefix has no diagonal weight x_zc, so P/Q=3/4 on that atom and p_j=3(q_j-p_j).

For each 0<=d<=D, EC49AC's LOWER witness uses this SAME prefix. It rejects STOP and nonpositive-d atoms, accepts positive-d atoms in increasing p_j/d_j order until sum y_j*d_j=d. The eight positive atoms have successive p_j/d_j levels 3, 12369/2341, 1359/251, 567/13, 5097/83. The resulting alpha is exactly L(d), by the EC49AC universal supporting-line theorem.

For the UPPER witness, also use the SAME prefix and S-always decision. Accept STOP with probability 1; accept every positive/zero-d atom with probability 1; accept each negative-d atom with probability 1-d/D, independently at its observable terminal state. Relative to accepting everything, the rejected mass equals (d/D) sum_neg p_j=3d, and removed discrimination equals (d/D) sum_neg d_j=-d. Thus alpha=1-3d and delta=d, exactly.

For any desired alpha between these endpoints, define theta=(alpha-L(d))/(1-3d-L(d)), unless the denominator is 0 (endpoints then coincide). At EVERY observed terminal atom choose acceptance probability y_j=(1-theta)*y_j(LOW)+(theta)*y_j(UP); at STOP choose probability theta. These are ordinary single-policy local behavioral probabilities, not a retained seed selecting a strategy. The shared fixed prefix makes acceptance and discrimination affine in y_j: delta stays d, alpha is the desired convex combination, beta=alpha-d. Complement acceptance realizes every negative-delta point. This proves the entire region exactly.

Because all feasible points have been realized by this fixed prefix, the feasible region equals an affine image of the hypercube of terminal acceptance probabilities for that prefix; it is therefore convex. NO claim is made about the full cost-varying 4D achievable set.

## Concrete first open fiber

At delta=1/12, EC49AC's lower endpoint is (alpha,beta)=(1229/4016,2683/12048); the new upper endpoint is (3/4,2/3). Every intermediate alpha in [1229/4016,3/4] is achievable exactly with the same fixed sensor prefix and independent terminal accept coins.

## Evidence, limitations and next

VERIFY.py (actually run with Python 3 Fraction) confirms 18 positive normalized leaves per source, all 24 sensed observation atoms and their signs/mass identities, budgets, the five EC49AC slopes, knots and rational midpoint samples including vertical interpolation at delta=1/12. Arbitrary-real coverage comes from the analytic construction and the inherited all-real EC49AC proof, NOT from finite grid extrapolation. No independent formal/Lean proof or Driver review. This positive-probability auxiliary BRC observer is not signed/phase native BRC nor a typed X6/three-dimensional slice/heartbeat dynamics model. P000 and ACTIVE worldview unchanged. Next EC49AE varies fixed cost pairs or eta and asks whether universal-prefix convex projection persists.