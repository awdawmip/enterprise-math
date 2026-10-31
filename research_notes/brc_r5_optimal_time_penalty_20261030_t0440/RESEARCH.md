# Enterprise Math R5 — optimized residual/time support envelope at two LR collisions

Date: 2026-10-30 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_BIGINT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is auxiliary finite two-law stochastic mathematics, not native X6/BRC-Shor execution or formal Source Result.

## Source pins, mother question and prior frontier

Frozen GLOBAL_KNOWLEDGE_V1 main@651dca136b89db6a39ec71a5c0d95d762a09ed7c; Enterprise Math canonical main@f4ca1284608113e2ec2faaa66ce6360834cb1578. Source predecessor: Enterprise Math Draft PR #1663, immutable author proof commit f17ac8064a2bf6b4f3965ece76ba436a0da36b38, research_notes/brc_r5_full_rank_collision_perturb_20261030_t0340/RESEARCH.md. Preserve P000 and ACTIVE residual-fidelity worldview. The mother question seeks equality of FULL and seedless exact-LR convex hulls but inequality of their actual real four-observer images; this question remains open.

This note **sharpens the separation certificate** within the previous doubly colliding, full-four-dimensional rational example. The prior exact lambda=1/10 witness gave distance lower bound 1/10598. Here the best lambda within the entire nonnegative time-penalty family is 1/22, giving a strictly stronger rational lower bound. It is a stronger exclusion of the same model, not the mother counterexample.

## Exact model

At t=1: P(A)=1/3, P(B)=2/3; Q(A)=2/3, Q(B)=1/3. At t=2, Y=1 conditionals (P,Q) are A:(1/2,1/4), B:(1/4,1/2). At t=3, Z=1 conditionals on A1:(1/2,1/4), B1:(2/3,1/3), A0:(1/2,2/5), B0:(1/2,3/5). All complement transition probabilities are positive. Stop decisions at t=1,2,3; t=4 forced stop with no new nature observation. L(h)=P(h)/Q(h) has exact collisions L(A1)=L(B1)=1 at t=2 and L(A11)=L(B11)=2 at t=3. The source-labelled paths and source-sensitive kernels stay intact.

At a stopped cylinder (t,h), Bernoulli error rates are

    p0(t,h) = 1/5 + t/20 + (t+1)/(100 L(h))
    q0(t,h) = 2/5 - t/30 + (t+2)L(h)/200.

Modify only p(2,A1)=p0+epsilon, p(2,B1)=p0-epsilon and q(3,A11)=q0+eta, q(3,B11)=q0-eta. Assume 0<epsilon<33/100 and |eta|<7/20; all error rates remain in (0,1). The executed exact instance has epsilon=eta=1/1000.

For O=(e_P,e_Q,T_P,T_Q), define

    R = e_P - 21/100 - T_P/20 - T_Q/100,
    D = 8 - T_P - T_Q.

Let alpha,beta be continue hazards at root A,B, and a,b the conditional stop hazards at A1,B1. FULL allows independent alpha,beta,a,b in [0,1]. Seedless exact LR forces a=b=y because of the t=2 LR collision. For all real policies, source-labelled BRC positive cylinder measures and the change-of-measure identity P(h)=L(h)Q(h) give

    R = epsilon (alpha*a-beta*b)/6,                     (1a)
    D >= 3(2-alpha-beta)+(2/3)(alpha*a+beta*b).         (1b)

Indeed, roots A/B each have P+Q cylinder mass 1 and forfeit 3 time units if stopped; A1/B1 each have P+Q mass 1/3 and forfeit 2 time units if stopped. Other early stops contribute further nonnegative time loss. For fixed alpha,beta,a,b, equality in (1b) is attained by letting all other nodes continue to t=4. Q-error eta does not affect either equation.

## Theorem — all-real exact optimal time penalty

For every real lambda >= 0, set Phi_lambda(O)=R-lambda*epsilon*D. Exact maxima over all REAL FULL and seedless-LR behavioral strategies are

    max_FULL Phi_lambda / epsilon = max(0,1/6 - 2lambda/3),
    max_LR   Phi_lambda / epsilon = max(0,1/6 - 11lambda/3).     (2)

Consequently the signed support gap of the four-dimensional observation convex hulls, for this family of directions, is

    Delta(lambda)/epsilon =
       3lambda              if 0 <= lambda <= 1/22;
       1/6 - 2lambda/3      if 1/22 <= lambda <= 1/4;
       0                    if lambda >= 1/4.             (3)

The unique maximizing lambda >=0 is 1/22; Delta_max=3epsilon/22. This is optimality **within this particular one-parameter family**, not over all signed four-dimensional directions.

**Proof.** Since lambda>=0, (1b) upper bounds Phi and its equality can always be realized by continuing at every other node. In FULL, the resulting expression divided by epsilon is

    alpha*a(1/6-2lambda/3) +
    beta*b(-1/6-2lambda/3) -
    3lambda(2-alpha-beta).

The B contribution is never positive, so choose beta=1,b=0. The A portion is maximized either by continuing to t=4, or by alpha=a=1; this gives max(0,1/6-2lambda/3).

In LR, the expression is

    y(alpha-beta)/6 -
    lambda*[3(2-alpha-beta)+(2/3)y(alpha+beta)].

The coefficient of alpha is y/6+3lambda-(2lambda/3)y >=0, so alpha=1 is optimal. The remaining expression is separately affine in beta,y and attains its maximum at the four corners: 0, 1/6-11lambda/3, -4lambda/3, and -3lambda. The maximum is max(0,1/6-11lambda/3). The positive LR branch is attained by continuing at root A, stopping at root B and using y=1; the zero branch is attained by never stopping before t=4. Thus (2) holds for all real behavior probabilities, including 0 and 1 and arbitrary unreachable-node actions. Elementary subtraction yields (3). QED.

## Sharper integer inequality and distance lower bound

For lambda=1/22 and epsilon=eta=1/1000, every real LR policy and every convex mixture of them satisfies the exact integer linear inequality

    22000 e_P - 1099 T_P - 219 T_Q <= 4628.             (4)

The legal FULL policy continuing everywhere except stopping at time 2 on A1 gives

    Ostar=(2581/6000, 551/1800, 11/3, 11/3),
    R=epsilon/6, D=2/3.

It has left-hand side 4631 in (4): the strict integer gap is 3. The coefficient l1 norm is 22000+1099+219=23318. By Holder duality,

    dist_infinity(Ostar, conv(O_LR)) >= 3/23318 > 1/10598.     (5)

The lower bound improves the previous exact certificate 1/10598; it is not asserted to be the exact nearest-point distance.

For epsilon=1/1000, directions Phi_lambda have l1 norm 53/50-2epsilon*lambda on 0<=lambda<=1/4. On [0,1/22], the normalized support gap 3epsilon*lambda/(53/50-2epsilon*lambda) is strictly increasing. On [1/22,1/4], differentiating epsilon*(1/6-2lambda/3)/(53/50-2epsilon*lambda) yields a derivative with numerator epsilon*(-53/75+epsilon/3)<0. For lambda>=1/4 the gap vanishes. Thus lambda=1/22 also gives the optimal normalized L-infinity lower bound among this direction family.

## Executed verification, reuse and limitations

VERIFY.js ran in V8 using exact BigInt fractions (Node 20+ compatible, no packages). It reconstructed 14 positive-labelled natural prefixes; checked every parent/child measure normalization, both exact LR collisions, positive Bernoulli kernels, the full four-observer witness, R and D, 16 FULL and 8 LR reduced binary corners, and exact corner-envelope endpoint domination at both breakpoints. The latter verifies the affine envelope for the continuum lambda>=0, not merely a finite lambda sample. EXACT_OUTPUT.txt is the actual output ending PASS_EXACT_R5_OPTIMAL_TIME_PENALTY_ENVELOPE. The all-real theorem is the proof above supported by the complete finite multi-affine reduction; numerical samples were not used.

BRC reuse is the exact positive-rational path/source measure prior to LR-key projection. The two time-2 collision fibers have identical LR but opposite epsilon residuals, so total LR-key mass alone loses the signed residual observer. This remains a finite positive-weight provenance calculation, not native heartbeat BRC-Shor arithmetic or a physical law.

Native Enterprise Math gateway version 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, and active-job quota 5/5. A bounded live owner-inventory request returned CONTROL_QUOTA. Therefore no current Owner, native CLAIM, Result or independent Driver review was authenticated. GitHub publication is author-side noncanonical mathematical preservation only.

## Next discriminating problem

On the same positive two-collision nature tree, introduce compensating strictly positive **P-error** perturbations at additional times/histories, retaining full four-dimensional affine span. First check (4) and the complete time/residual envelope; Q-only modifications cannot alter this specific signed gap. Surviving candidates must pass ALL signed support directions: for every FULL deterministic four-vector provide a nonnegative rational combination of at most five LR vectors, or an exact Farkas separator. Only for an all-signed hull-equal model seek actual real LR-image nonmembership with certified semialgebraic methods. Preserve P000 and original theorem scopes.
