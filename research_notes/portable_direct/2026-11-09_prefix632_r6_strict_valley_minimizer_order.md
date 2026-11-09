# PREFIX-632-R6 — Strict leftward ordering of signed-BRC variance valleys

Date: 2026-11-09 Asia/Shanghai.
Researcher-ID: EM-DIRECT-23F213 / TASK_RESEARCH.
Research-Activity-ID: RA-C7D075E0C0D860ED02903F38.
Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Source premises: PREFIX-621 exact first-passage finite survivor law; PREFIX-622 Poissonized moments; PREFIX-625 strict coordinatewise mean monotonicity; PREFIX-631 uniform gradient reversal. This is the unchanged signed-observer statistical model, not a new execution of the original 96-port graph.

## Question and model

For p2 in B=[37/256,39/256], consider the interval I=[3/20,1/6] in the first signed-observer parameter. Let T_q(p1,p2) denote the native-action trial count until both directions reach the same frozen anytime-confidence stopping condition (beta=1/40, confidence diameter <=1/4). Native slots use q=12 and q=24; the independent-thinning model admits real q>=2. Denote V_q=Var(T_q), mu=E[Y], W=Var(Y) for the maximum Y of the two independent unit-rate informative Poisson waiting times. The established exact relation is

    V_q(p1,p2)=q^2 W(p1,p2)-q mu(p1,p2).

Both W and mu are finite differentiable polynomials in the parameters, induced by the 189-level first-passage survivor recurrence.

## Theorem A — universal strict ordering of *all* valley minimizers

Fix any p2 in B and any real 12<=q1<q2. For each q, define the nonempty compact set

    M(q,p2) = Argmin { V_q(p1,p2) : p1 in I }.

For EVERY a in M(q1,p2) and EVERY b in M(q2,p2), the following inequalities hold:

    3/20 < b < a < 1/6,
    mu(b,p2) < mu(a,p2),
    W(b,p2) < W(a,p2).

More precisely, setting dmu=mu(b,p2)-mu(a,p2)<0 and dW=W(b,p2)-W(a,p2)<0,

    dmu/q1 <= dW <= dmu/q2 < 0.                     (1)

This does not assume stationary-point uniqueness. It applies simultaneously to every choice of global minimizer within I. For actual slots, every q=24 valley minimizer in I lies strictly LEFT of every q=12 valley minimizer in I.

### Proof

1. PREFIX-631 proves for every p2 in B and q>=12 that dV_q/dp1 is negative at p1=3/20 and positive at p1=1/6. The compact-interval minimum therefore cannot occur at either endpoint: moving inward strictly decreases V_q. So all elements of M(q,p2) lie in the open interval I°, where the first-order condition applies.

2. PREFIX-625 proves that mu is strictly increasing in p1 on [0,1/2], and, stronger, mu'(p1,p2)>0 on (0,1/2). A direct proof: each surviving-direction probability s_n has nonnegative derivative on that interval; s_25'=25((1-p1)^24-p1^24)>0; and mu'=sum_n alpha_n(p2)s_n'(p1), where every alpha_n(p2)>0.

3. Since minimizing V_q is equivalent to minimizing F_q=W-mu/q, the optimality inequalities F_q1(a)<=F_q1(b) and F_q2(b)<=F_q2(a) yield exactly

    dW >= dmu/q1,       dW <= dmu/q2.

Because 1/q1>1/q2, dmu>0 would make these inequalities inconsistent. Hence dmu<=0.

4. Suppose dmu=0. The two bounds force dW=0, so both a and b minimize F_q1 and F_q2. In particular, a is an interior common minimizer. The two stationary equations at a give W'(a)=mu'(a)/q1=mu'(a)/q2, forcing mu'(a)=0, contrary to step 2. Thus dmu<0. Strict increase of mu implies b<a, and the sandwich (1) then implies dW<0. This completes the proof.

## Theorem B — disjoint rational local-valley windows at a fixed parameter

At the exact rational second parameter p2=19/128, there exists at least one local minimum of V_24 in

    4/25 < p1 < 401/2500,     i.e. 0.1600 < p1 < 0.1604,

and there exists at least one local minimum of V_12 in

    401/2500 < p1 < 161/1000, i.e. 0.1604 < p1 < 0.1610.

Proof: the companion standalone program uses exact Fraction sums from the PREFIX-621 survivor counts and the PREFIX-622 negative-binomial moment law to verify these four exact inequalities:

    (dV_24/dp1)(4/25,19/128) < 0,
    (dV_24/dp1)(401/2500,19/128) > 0,
    (dV_12/dp1)(401/2500,19/128) < 0,
    (dV_12/dp1)(161/1000,19/128) > 0.

For each interval, continuity and differentiability imply that the interval minimum is attained strictly in its interior, where it is a local minimum. The windows are disjoint. The statement is existential; neither uniqueness nor global optimality on the larger interval I is inferred from these four endpoint comparisons.

## Exact certificate details

For 0<=n<=188, let A[n,k] be the first-passage survivor word counts, and s_n(p)=sum_k A[n,k]p^k(1-p)^(n-k). Put

    w(n,m)=C(n+m,n)/2^(n+m+1),
    z(n,m)=(n+m+1)C(n+m,n)/2^(n+m+2),
    alpha_n(p2)=1-sum_m w(n,m)s_m(p2),
    beta_n(p2)=n+1-sum_m z(n,m)s_m(p2).

Then mu=sum_m s_m(p2)+sum_n alpha_n(p2)s_n(p1),
U=dmu/dp1=sum_n alpha_n(p2)s_n'(p1),
J=dH/dp1=sum_n beta_n(p2)s_n'(p1),
and

    (dV_q/dp1)/q^2 = 2(J-mu*U)-U/q.                 (2)

The supplied Python standard-library script checks 189 positive alpha and beta coefficients and the four exact rational derivative signs using (2). It independently reconstructs the PREFIX-621 189-level recurrence, which has first stop at 25. Executed output:

    ALL_CHECKS_PASS [('4/25', 24, 'NEGATIVE'), ('401/2500', 24, 'POSITIVE'), ('401/2500', 12, 'NEGATIVE'), ('161/1000', 12, 'POSITIVE')]

Approximate derivative values are displayed only after Fraction sign decisions, in PREFIX632_R6_RESULTS.json. The analytical theorem is conditional on the source-proved PREFIX-625 and PREFIX-631 statements; it is not an independent replay of every preceding model certificate.

## Reuse and next work

BRC reuse: COMPOSE_APPLIED (PREFIX-621/622/625/631); EXTEND_EXISTING_TOOL (exact joint-variance-gradient rational witnesses). The observer retains two signed directions, neutral outcomes, native-slot q, and the exact first-passage decision. Frozen science and P000 V5/ACTIVE world assumptions are unchanged.

Next discriminating unit: certify derivative-positive intervals or convexity to prove whether the valley is unique for every p2 in B, and whether the q-dependent local valley branches are continuous/monotone in p2. Separately pursue the full two-dimensional global MAXIMUM variance question; the present local MINIMUM theorem supplies a useful internal separating structure, not a replacement for that task.
