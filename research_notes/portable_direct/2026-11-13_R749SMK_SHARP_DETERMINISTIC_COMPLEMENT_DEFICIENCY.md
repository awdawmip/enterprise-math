# R749SMK — Sharp two-way Blackwell deficiency at deterministic A-complement

2026-11-13 (Asia/Shanghai). Continuation of R749SMG–R749SMJ on unchanged frozen scientific input awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is an eight-source conditional signed-Port observer theorem, not a native V29/V39 event. Author-side proof and exact checks; independent scientific review pending.

## Statement

Let z=(x,y,t) and output o=(u,v,w) range over {±1}³; put z₊=y,z₋=t. Retain the prior observer channels

\[
F_{uvw,z}={(2+\alpha ux)(2+\beta v z_u)(2+\gamma wyt)\over64},\qquad
P_{uvw,z}={2+\gamma wyt\over128}
\sum_{i=\pm1}(2+ix)(1+\alpha ui)(2+\beta v z_i).
\]

For column-stochastic source-independent output garblings G, set

\[
\delta(K\to L)=\inf_G\max_z\operatorname{TV}\big(L(\cdot\mid z),GK(\cdot\mid z)\big).
\]

**Theorem.** For every real \(\beta\in[-1,1]\), at \(\alpha=-1,\gamma=0\), writing \(b=|\beta|\),

\[
\boxed{\delta(F\to P)=\delta(P\to F)
={b(2+b)\over 2(4+3b)}.}
\]

The optimum is attained, vanishes exactly when b=0 and equals 3/14 for b=1. This sharpens R749SMJ's lower bound b/16 on the same stratum.

## Exact reduction and symmetry

At the stated parameters w is an independent fair coin in both channels. Deleting and independently reattaching it are source-independent stochastic operations; therefore either deficiency equals that of the four-output marginal on (u,v):

\[
F_{uv,z}={(2-ux)(2+\beta v z_u)\over16},\qquad
P_{uv,z}={(2-ux)(2+\beta v z_{-u})\over16}.
\]

A simultaneous change of the signs of v,y,t reduces negative beta to b≥0. Both kernels are equivariant under the commuting transformations (x,y,t;u,v) ↦ (-x,t,y;-u,v) and ↦ (x,-y,-t;u,-v). Average any stochastic G over this four-element symmetry group. Convexity of TV and the corresponding source permutations show that worst-source error cannot increase.

Every equivariant 4×4 G is specified by four nonnegative probabilities A,B,C,D summing to one, respectively taking input (u,v) to (u,v),(u,-v),(-u,v),(-u,-v). Write

\[
q=C+D,\quad d=A-B,\quad e=C-D,\quad
\lambda_u=1-2q,\quad \lambda_v=d+e,\quad
\lambda_{uv}=d-e.
\]

G multiplies Walsh expectations of U,V,UV by the three lambdas. In particular 0≤q≤1, e≤q, and both |\lambda_v|,|\lambda_{uv}|≤1.

## Lower bound

The symmetry makes two source states representative:
\(z_\parallel=(-1,1,1)\) and \(z_\times=(-1,1,-1)\).
The target-minus-garbled expectation difference for U is q for each. At the parallel source the absolute differences of the V and UV expectations are

\[
a_\parallel={b\over2}(1-\lambda_v),\qquad
c_\parallel={b\over4}(1-\lambda_{uv}),
\]

and at the cross source they are

\[
a_\times={b\over4}(1+\lambda_v),\qquad
c_\times={b\over2}(1+\lambda_{uv}).
\]

For either source its four-output signed probability difference, with nonconstant Walsh coefficient magnitudes q,a,c, has the exact total variation

\[
\operatorname{TV}
={\max(q,a+c)+\max(q,|a-c|)\over4}. \tag{1}
\]

This is immediate by Fourier inversion and |r+s|+|r-s|=2max(|r|,|s|); the V,UV coefficients have the same sign at each representative source.

Let η denote the maximum-source error. From (1), TV≥a/2 and TV≥c/2. Applying those inequalities respectively to a_parallel and c_cross gives

\[
\eta\ge\max\left\{{b(1-\lambda_v)\over4},
{b(1+\lambda_{uv})\over4}\right\}
\ge{b(1-e)\over4}\ge\boxed{{b(1-q)\over4}}. \tag{2}
\]

Also (1) gives TV≥(q+a+c)/4. Set S_parallel=a_parallel+c_parallel and S_cross=a_cross+c_cross. Their average is

\[
{S_\parallel+S_\times\over2}
={b(3-e)\over4}\ge{b(3-q)\over4}.
\]

Consequently

\[
\eta\ge{q+\max(S_\parallel,S_\times)\over4}
\ge\boxed{{4q+b(3-q)\over16}}. \tag{3}
\]

The bound (2) decreases with q while (3) increases for 0≤b≤1. They intersect at \(q_*=b/(4+3b)\), yielding the universal lower bound

\[
\eta\ge {b(2+b)\over2(4+3b)}. \tag{4}
\]

## Achieving randomizer

Set

\[
\boxed{A=B={2+b\over4+3b},\quad C={b\over4+3b},\quad D=0.} \tag{5}
\]

All entries are nonnegative and 2A+C=1. For (5), q=e=q*, d=0, \(\lambda_v=q_*\), \(\lambda_{uv}=-q_*\). On both representative sources,

\[
a+c={b(3-q_*)\over4},\quad
|a-c|={b(1-3q_*)\over4}=q_*.
\]

The first quantity is at least q*, so (1) equals exactly the right side of (4). The symmetry covers all eight source states. Add an independent fair w to the randomized output for an attaining 8-output G.

Exchanging source coordinates y and t interchanges F and P; a common permutation of their source columns preserves the minimax deficiency. Therefore the two directed optima agree. The simultaneous v,y,t sign change extends the formula to negative beta. QED.

## Executed verification and continuation

The companion standard-library Python Fraction checker reconstructs both full eight-output channels and an explicit 8×8 attaining garbling, verifies normalization and all source-column TV identities for the rational grid beta=k/8, k=-8,…,8, and checks equality of the two lower-bound expressions at q*. It returned PASS: 17 parameter values, 136 source-column checks, and 136 stochastic-G column checks. The theorem on all real beta in [-1,1] follows from the preceding algebra, not the finite grid. Companion files: R749SMK_SHARP_DEFICIENCY_EXACT_CHECK.py and R749SMK_SHARP_DEFICIENCY_RESULTS.json.

Remaining scientific question: compute the exact minimal predictive Walsh carrier for genuinely finite-memory feedback controllers, then establish the separately authorized Cell/Link/Port correspondence for actual V29/V39 events. Preserve P000, named-source/BRC branches and source firewall.