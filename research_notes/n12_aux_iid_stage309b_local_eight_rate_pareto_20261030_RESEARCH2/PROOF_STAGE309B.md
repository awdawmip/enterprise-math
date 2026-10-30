# Stage309-B — sharp, nonzero, FULL eight-rate local Pareto interval

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Author: current local research2 portable writer, not an authenticated native Researcher. Frozen account knowledge main f20e408007833bc0518fdb16c4919a705d7b8a77 and Enterprise Math main a406972cef38811f58b5afe38c277037415ef81e; original P000 V5 and ACTIVE worldview preserved. This is a finite positive-weight BRC *auxiliary* probability model, NOT a P000 X6 or heartbeat dynamics theorem. Source owner lookup returned CONTROL_QUOTA; Sites research_authority_granted=false.

Predecessors: Stage307-B.1 (505192696012143fbbbc8a4cbd690bd59112568d), Stage307-B.2 (128d2ce6aeb0299cdf842d0ad65082a64ba9d475), and Stage308-B (273b50a6355e98c96bcc1e44ef11160d19325333). Stage308 proved only an endpoint slope and a restricted symmetry-breaking comparison. The new result proves a sharp law on an explicit **nonzero interval** of the original eight-real-parameter optimization, not merely a candidate curve.

## Frozen source / observer / future-operation types

S is fair. Given S=s, independent J matches s with fidelity 7/8, W matches s with fidelity 3/4, and Y is Bernoulli(p_s), p_0=1/4, p_1=3/4. Public initial G=(W,Y), private h=(J,W,Y). For h in order 000,001,010,011,100,101,110,111, the strictly positive integer source pairs (256 Pr(S=0,h),256 Pr(S=1,h)) are
(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63).

The original future F port emits conditionally IID Bernoulli(p_S), while the compressed port uses one locked real t_h in [0,1] per private h for all three F visits. H emits independent fair bits. Policies choose F/H adaptively using public history only. Let P(t) be worst total variation keeping public G and trace, and T(t) be worst TV retaining terminal original S,J,G and trace. The all-F policy maximizes both over all adaptive policies: presample three F bits and enough independent H bits; every adaptive trace is a common stochastic image of the all-F observation augmented by common independent randomness. This is the previously proved Stage307-B.1 reduction, here reused with unchanged observer scopes.

The unique joint-optimal MAP table chooses t_h=p_0 if a_h>b_h, otherwise p_1; its P_0=11/256 and T_*=77/1024. Define the full Pareto envelope F_P(p)=min{T(t): t in [0,1]^8, P(t)<=p}, with all eight real rates unconstrained apart from being locked within each private fiber.

## Theorem — exact full eight-rate Pareto law

For real 0<=epsilon<=1/10000 put
q(u)=9u/128+3u^2/32-u^3/8 and
g(u)=117u/4096-123u^2/1024+23u^3/256.
There is a unique u_epsilon in [0,1/100] satisfying q(u_epsilon)=epsilon, and

    F_P(11/256-epsilon)=77/1024+g(u_epsilon).

For epsilon>0, precisely TWO global minimizing eight-rate tables exist: change only h=100 from 1/4 to 1/4+u_epsilon, OR change only h=011 from 3/4 to 3/4-u_epsilon; leave the other seven rates at MAP. At epsilon=0 the unique minimum is MAP. No assertion is made beyond epsilon=1/10000.

### 1. Globally localize EVERY potential minimizer

Let D(t,p) be TV between the three-bit Bernoulli product laws. For each h, the triangle inequality implies

 a D(p0,t)+b D(p1,t) >= min(a,b)D(p0,p1)+|a-b|D(t,p_MAP).

A projection onto one bit yields D(t,p_MAP)>=|t-p_MAP|. Because min_h |a_h-b_h|=2 for the integer /256 masses,

 T(t)-T_* >= sum_h |a_h-b_h||t_h-t_MAP,h|/256
          >= max_h |t_h-t_MAP,h|/128.                       (1)

The one-h=100 candidate has exactly P=P_0-q(u), T=T_*+g(u) for 0<=u<=1/100 (the source's fixed residual signs prove these polynomial identities). Note q'(u)>0, q(1/100)>1/10000 and

 (13/32)q(u)-g(u) = 9u^2(9-8u)/512 >=0.                   (2)

Fix epsilon in (0,1/10000]. Since the candidate is feasible, any minimizing t must have T(t)-T_* <= (13/32)epsilon. By (1), every one of its eight coordinates differs from MAP by at most 52epsilon <=52/10000<1/100. This excludes ALL remote points of the original [0,1]^8 cube without a grid, numerical optimizer or missing compactness argument.

### 2. Fix the TV signs simultaneously in the eight-dimensional box

Let B_k(z)=z^k(1-z)^(3-k), k=0,1,2,3, and A(z)=B_0(z)+3B_1(z)=1-3z^2+2z^3. At MAP, the compressed-minus-original G=00 per-word residuals are (13,3,-3,-13)/1024. The combined mass of its two private rates is 5/16; both rates in the localized box lie in [24/100,26/100]. Throughout that interval the exact bounds on |B'_k| are respectively 2,1/3,1/3,1/3. Therefore perturbations cannot exceed (5/16)(1/100) times these bounds, strictly smaller than the corresponding residual margins (13,3,3,13)/1024. Signs remain (+,+,-,-), everywhere in the full box. The reflected G=11 signs are fixed analogously. At G=01,10 baseline public TV is zero and new public TV is always nonnegative.

For each G=00,11 outer rate that moves TOWARD the minority source, let u>=0 be the amount and q_h(u) its decrease of outer public TV. It is m_h [A(1/4)-A(1/4+u)] by reflection, where m_h=(a_h+b_h)/256. In h=100,011 the mass is 1/16, so q_h=q(u); in h=000,111 the mass is 1/4, so q_h=4q(u). All four moves AWAY from the minority source contribute nonnegative public changes, as do both middle public fibers. Therefore every localized table satisfies

 P_0-P(t) <= sum_{outer h moving toward minority} q_h(u_h). (3)

This does NOT discard provenance or pretend middle fibers vanish: their exact nonnegative TV remains on the right side of the comparison.

### 3. Compare the exact joint cost per unit of public gain

For an outer h with majority source mass a>b (or the reflected b>a fiber), moving toward the minority source by u in [0,1/100] has joint excess

 C_{a,b}(u) =
 [a((3/4)^3-(3/4-u)^3) + b(A(1/4+u)-A(1/4))]/256.     (4)

This uses the explicit local signs of each of the two three-bit product TVs; it is exact, not a linearization. For h=100,011 it equals g(u). For h=000,111 it equals H(u)=C_{63,1}(u).

Write C(v)=g(q^{-1}(v)) on 0<=v<=q(1/100), and M(v)=H(q^{-1}(v/4)) on 0<=v<=4q(1/100). Exact derivatives on 0<=u<=1/100 give

 q'>0, q''=3/16-3u/4>0,
 g'>0, g''=-123/512+69u/128<0.

Hence C is strictly increasing AND strictly concave with C(0)=0, while

 0 < C'(v) <= C'(0)=g'(0)/q'(0)=13/32 < 1.             (5)

For the majority outer source pair,

 H'(u)=[189(3/4-u)^2-6z(1-z)]/256,
 (4q)'(u)=6z(1-z)/4, z=1/4+u.

The strict inequality H'(u)>(4q)'(u) is equivalent to

 189(3/4-u) > 390(1/4+u),

valid for every 0<=u<=1/100. Consequently M'(v)>1 and M(v)>v for v>0. (6)

In particular a majority-label outer gain is more costly than the same gain in either minority-label fiber. All other rate departures have strictly positive joint cost by (1).

### 4. Exact global constrained exchange

For any minimizing t, (3) implies total positive outer gains >=epsilon. Choose retained gains 0<=v_h<=q_h(u_h) summing exactly epsilon (trim excess if necessary). Their joint costs are increasing with gains, so the original cost is at least the cost of these retained values. Since each v_h<=epsilon<=1/10000<q(1/100), all inverse functions are in their proved domains.

Let v1,v2 be retained gains of h100,011 and v3,v4 those of h000,111. By separability of the full source-tagged joint TV, strict concavity, and (5)-(6),

 T(t)-T_* >= C(v1)+C(v2)+M(v3)+M(v4)
          >= C(v1+v2)+(v3+v4)
          >= C(v1+v2+v3+v4)=C(epsilon).                 (7)

The single-h100 or single-h011 candidate meets this bound exactly, so it is the **true full continuous minimizer**, proving the boxed parametrization. Strictness shows equality is impossible with any majority gain, two nonzero minority gains, surplus gain, an away move, or a middle-fiber move. Thus there are precisely the two stated tables for epsilon>0; MAP is unique at epsilon=0. QED.

## Executed exact-rational verification and research boundary

The locally executed REPRO_STAGE309B.py checks all 16 strictly positive source/h branches, exact public and joint path totals, polynomial formulas, the explicit rational sign-margin/derivative bounds, the epsilon localization and three rational interior Pareto candidates. Execution prints STAGE309B_LOCAL_EIGHT_RATE_PARETO_EXACT_PASS. Independently executed VERIFY_STAGE309B.py recomputes the conditional source probabilities from scratch and enumerates every one of the 128 S,J,W,Y,X^3 atoms for rational witnesses, printing INDEPENDENT_128_ATOM_SOURCE_PUBLIC_JOINT_EXACT_PASS. Continuum optimality is established by the four-step analytic proof, not by these finite checks.

BRC resolution: REUSE_APPLIED to the existing positive-weight branch carrier (definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json), retaining source S, label J, public G, future-operation scope, and the distinct public versus source-tagged observers. No signed-amplitude cancellation, P000 X6 coordinates, triadic native force closure, time dynamics or registered six-field Cell address is inferred from this probability example. Existing source and task status are UNREVIEWED/NOT_ADMITTED. Further mathematical work: locate or isolate the first breakpoint after the certified epsilon=1/10000 sharp interval; preserve native X6/Cell/time embedding as an independent proof obligation.
