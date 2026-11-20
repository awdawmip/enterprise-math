# EC49FUR — Two-endpoint total-variation dual, exact support classifier, and a new n=30 phase onset

Date: 2026-11-20 (Asia/Shanghai). Mode: independent portable research (TASK_RESEARCH scientific continuation). Evidence: **AUTHOR_PROVED / EXACT_FRACTION_INTERVAL_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Exact source scope

Frozen BRC16943 scientific pin: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\` (unchanged).
Predecessor: EC49FUQ at commit \`96ad7a2c22c274446e74906c48bc6e3234a39436\` (PR #2846). FUQ provides (i) reduction from full-bit randomized tests to upper-tail count rules and (ii) the theorem that their worst nuisance values occur at the two compactified endpoints. Those premises are explicitly reused, not independently re-proved here.

This concerns the *lossy binary clipped-price observer*, not a no-loss representation of native X6 branch/port/provenance state. The P000 six-dimensional native space, three-dimensional research slice and residue-fidelity constraints remain unchanged.

For integer \`n>=1\`, width \`0<x<1\` and the common nuisance \`theta in [0,theta_E]\` (0 a compactification limit), set

\[
\beta=\frac3{637},\quad\theta_E=\frac{31597745}{1653649},\quad
u_\theta=\frac{21829245984}{45529434409-456083905\theta},\quad
T_\theta(x)=(1-x)(1-\beta x+\beta x\theta).
\]
The two conditional Bernoulli probabilities are \`p_theta=1-T_theta\`, \`q_theta=1-u_theta*T_theta\`; \`0 <= p_theta < q_theta <= 1\`.

For endpoint \`t in {0,E}\`, define the signed binomial mass
\[
\Delta_t(k)=\binom nk\{q_t^k(1-q_t)^{n-k}-p_t^k(1-p_t)^{n-k}\},\qquad 0\le k\le n.
\]
Let \`d_k=Delta_E(k)-Delta_0(k)\` and \`Delta_lambda(k)=Delta_0(k)+lambda*d_k\` for \`0<=lambda<=1\`.

## Theorem 1: exact one-dimensional total-variation dual

Under the predecessor's endpoint-reduction and uniform threshold-dominance theorems, the full composite minimax advantage and risk are exactly
\[
\boxed{A_n(x)=1-2V_n(x)=\min_{0\le\lambda\le1}
 f_{n,x}(\lambda),\qquad
 f_{n,x}(\lambda)=\sum_{k=0}^{n}[\Delta_\lambda(k)]_+.}
\]
This is the total-variation distance of the two distributions formed by mixing the endpoint binomial laws with the **same** lambda under each hypothesis. Hence \`f\` is convex, continuous, piecewise affine with breakpoints only at
\[
\boxed{\lambda_k=-\frac{\Delta_0(k)}{\Delta_E(k)-\Delta_0(k)}
 \quad\text{when }d_k\ne0,\ 0<\lambda_k<1.}
\]
An exact minimizer is among \`{0,1} union {lambda_k}\`: at most \`n+3\` rational candidates, with no optimization over nuisance or randomization parameters. For rational width \`x\`, all of these and the resulting risk are exact rationals.

*Proof.* For a fixed endpoint-mixture weight lambda and arbitrary randomized full-bit test phi, the mixture advantage is linear in phi. Maximization independently chooses phi=1 at positive signed masses and phi=0 at negative masses, giving \`f(lambda)\`. The finite compact convex minimax theorem swaps max over tests with min over lambda. The predecessor's endpoint-only theorem identifies this finite two-endpoint game with the original nuisance continuum. Since the mixture masses have total zero, their sum of positive parts equals total variation. Each signed mass is affine in lambda, proving convexity, the breakpoints and rationality.

For completeness, the Bayes rule for *every* endpoint mixture is a single upper-tail threshold: its mixed Q and mixed P laws are mixtures of binomial laws. Their adjacent ratios obey
\[
\frac{Q_\lambda(k+1)}{Q_\lambda(k)}
 \ge \frac{n-k}{k+1}\frac{q_{\min}}{1-q_{\min}},
\quad
\frac{P_\lambda(k+1)}{P_\lambda(k)}
 \le \frac{n-k}{k+1}\frac{p_{\max}}{1-p_{\max}}.
\]
The predecessor's uniform strict gap \`q_min>p_max\` makes \`Q_lambda(k)/P_lambda(k)\` strictly increasing in k. Thus the maximizing rule has one threshold and randomizes at most at its boundary. This also independently confirms that the dual's Bayes optimizer is compatible with the primal threshold class.

## Theorem 2: necessary and sufficient endpoint-support criterion

Define \`s_0=f'_+(0)\` and \`s_E=f'_-(1)\`, where \`d_k=Delta_E(k)-Delta_0(k)\`. The exact formulas, including ties, are:
\[
s_0=\sum_{\Delta_0(k)>0}d_k+\sum_{\Delta_0(k)=0}[d_k]_+,
\]
\[
s_E=\sum_{\Delta_E(k)>0}d_k+\sum_{\Delta_E(k)=0}\min(d_k,0).
\]
Then:
- The pure nuisance endpoint \`theta=0\` is least favorable **iff** \`s_0>=0\`.
- The pure nuisance endpoint \`theta=theta_E\` is least favorable **iff** \`s_E<=0\`.
- **Both endpoints are necessary in every least-favorable mixture iff** \`s_0<0<s_E\`.

*Proof.* A convex function on \`[0,1]\` is minimized at 0 iff its right derivative is nonnegative, and at 1 iff its left derivative is nonpositive. Its minimizers are all interior iff both boundary derivative tests are strict. The displayed formulas follow termwise from directional derivatives of \`max(0,a+lambda*d)\`. This exactly classifies whether one or two endpoint supports are **necessary**, including degenerate endpoint ties without silently calling a merely possible two-point mixture compulsory.

For fixed n, \`Delta_0(k;x)\`, \`Delta_E(k;x)\` are rational-coefficient polynomials in x of degree at most \`2n\`. The support-pattern regions and their transition boundaries are therefore finite semialgebraic sets over the rationals; this gives a symbolic algorithm to isolate all switches without scanning real widths.

## Theorem 3: a newly isolated n=30 E-to-two-support transition

For \`n=30\` and every real width in the closed rational interval
\[
\boxed{I=[749/5000,\;1499/10000]=[0.1498,0.1499],}
\]
the pure \`theta=theta_E\` endpoint's Bayes rule is \`K>=9\`, and the pure \`theta=0\` endpoint's Bayes rule is \`K>=11\`. Put
\[
G(x)=D_E(\mathbf1_{\{K\ge9\}})-D_0(\mathbf1_{\{K\ge9\}})
=\sum_{k=9}^{30}(\Delta_E(k;x)-\Delta_0(k;x)).
\]
There is **exactly one** real algebraic number \`x_* in (749/5000,1499/10000)\` with \`G(x_*)=0\`. Its numerical location from exact rational bisection is approximately
\[
\boxed{x_*\approx0.1498008234431.}
\]

On \`[749/5000,x_*]\`, a pure \`theta_E\` least-favorable prior exists. On \`(x_*,1499/10000]\`, **every least-favorable prior assigns positive weight to both endpoints**. At \`x_*\`, the pure \`theta_E\` solution is allowed; mixed solutions may also be optimal.

*Exact certificate.* On all of \`I\`, elementary rational interval evaluation certifies:
\[
\Delta_E(8)<0<\Delta_E(9),\qquad
\Delta_0(10)<0<\Delta_0(11),\qquad
s_0(x)<-1/20.
\]
Since the endpoint mixtures are binomial MLR families, these adjacent signs certify the respective full Bayes thresholds, not just two isolated coefficients. The exact interval derivative of the displayed polynomial \`G\` satisfies
\[
\boxed{G'(x)>1/2\quad(x\in I).}
\]
Direct exact rational substitution gives \`G(749/5000)<0<G(1499/10000)\`. The intermediate value theorem and strict derivative bound establish existence and uniqueness. By Theorem 2, \`s_E=G(x)\`, and \`s_0<0\` throughout; hence the claimed support change is proved. All interval arithmetic uses outward enclosures constructed from exact \`fractions.Fraction\` endpoints, and the certified strict inequalities are evaluated as exact fraction comparisons.

## Reproducibility and limitations

Companion Python 3 standard-library verifier: \`EC49FUR_DUAL_TV_PHASE_CLASSIFIER.py\`. It independently compares the dual minimization and FUQ-style primal endpoint threshold enumeration for seven exact rational cases: \`(n,x)=(1,1/2),(2,1/2),(15,7/25000),(15,1/2),(30,3/20),(40,1/100),(60,7/20)\`. It checks the selected dual sign changes and derivative classification, plus the entire rational interval certificate for the new n=30 transition. Local execution: \`PASS\`. Floating-point displays are only summaries; all mathematical assertions use exact fractions. The continuum-\`theta\` reduction rests on the analytic predecessor FUQ proof, while the n=30 interval result has its own fully rational certificate.

Source/authorship: independent current automation research continuation; prior \`EM-DIRECT-8454C6\` and SID \`MCP-44cfc4e6f2094f96861854ebefc77e84\` are historical scientific provenance, not a claimed current session capability. This portable artifact is neither an official CLAIM, Result, mathematical Review nor a P000 change; Activity association waits for authenticated current ownership.

Next: isolate all remaining n=30 algebraic switch points and compare their support/threshold chamber topology with n=15; study any general monotonicity or scaling laws for the first two-support transition as n grows. An independent mathematical review of FUQ's analytic endpoint reduction and this new dual classification remains outstanding.
