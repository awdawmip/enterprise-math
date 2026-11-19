# EC49FTV — Full positive-price-prior domain and unique interior maximum of the sharp stochastic-order threshold

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_RATIONAL_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Provenance, scope and frozen input

This is external-price-prior postprocessing of an inherited BRC16943 optimal-q140 Bellman outcome, **not** new native dynamics, geometry or a claim about physical reality. Frozen native scientific source: \`awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Inherited native Bellman author result: EC49FTH [PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774) @ \`999bf1069403306b3813e0e390dae4435d7b4b8c\`, NOT_REVIEWED. Immediate parent: EC49FTU [PR #2801](https://github.com/awdawmip/enterprise-math/pull/2801) @ \`f8857e1d6e22f47bb7fc397316df9e8650e6701d\`, specifically \`EC49FTU_TWO_PARAMETER_PHASE_THEOREM.md\` and its exact mass formulas. No source pin is rebased. The continuum price prior is an external effective observer, not a new P000 native coordinate.

External box: \((a,b)\in[3/4,49/64]\times[7/16,57/128]\), clipping curve \(a_c(b)=(77+6b)/105\). Condition on inherited high-gap \(m=M\in I=(1469/64,187/8)\), \(t=187/8-m\in(0,27/64)\), \(U=3/4\), \(L(m)=(8m+173)/480\). The inherited optimal discount is \(Z\). For real \(\theta\), take the baseline price prior

\[
h_\theta(a,b)=(1+a+b)\,[1+\theta(a-a_c(b))].
\]

Retain the parent's smooth clipped-only nonnegative bump with parameter \(\lambda\ge0\), whose mass added to the atom at \(Z=U\) is exactly \(\lambda t A_\theta(t)\). On the nonclipped fiber the normalized-irrelevant continuous kernel is

\[
K_\theta(m,z)=\frac{16}{945}\,[1+a(m,z)+b(m,z)]\left[1+\frac{8\theta(4z-3)}{35}\right],\quad L(m)<z<U.
\]

The continuous mass \(A_\theta\), clipped mass \(B_\theta\), and atom ratio \(r_{\theta,\lambda}\) are

\[
A_\theta(t)=\frac{tQ_\theta(t)}{421954312500},\quad Q_\theta(t)=3296t^2\theta-1992060t\theta+258300t+261457875,
\]

\[
B_\theta(t)=\frac{(64t-441)(109568t^2\theta+12022416t\theta-209018880t-88044327\theta-24135965280)}{35838544379904000},
\]

\[
r_{\theta,\lambda}(m)=\frac{B_\theta(t)}{A_\theta(t)}+\lambda t.
\]

## New exact theorems

**Theorem 1: maximal strict-positive prior domain.** The baseline \(h_\theta\) is strictly positive throughout the *closed* price box if and only if

\[
\boxed{-960/7<\theta<6720/59.}
\]

The nonnegative bump leaves the full prior strictly positive on that interval. At the interval endpoints \(h_\theta\) is nonnegative but zero at a corner, so whole-box strict positivity does not extend to them.

**Theorem 2: all-admissible-theta sharp stochastic order.** For every \(\theta\) in the maximal strict-positive interval, and every \(\lambda\ge0\), the inherited conditional law \(Z\mid M=m\) is first-order stochastically nondecreasing for *all* real \(m<m'\) in \(I\) if and only if

\[
\boxed{0\le\lambda\le\Lambda(\theta)},\qquad
\boxed{\Lambda(\theta)=\frac{3500(862686243742176000-2239375169798320\theta-18989094173841\theta^2)}{6561(413340200-1327113\theta)^2}}.
\]

This extends the two-parameter phase classification of EC49FTU from \([0,1]\) to the full admissible open interval, with **no native Bellman rerun**.

**Theorem 3: unique interior peak, breaking global monotonicity.** The exact threshold \(\Lambda(\theta)\) strictly increases until

\[
\boxed{\theta_*=\frac{2131469495973983261425}{29171587292164226979}\approx73.0666272845}
\]

and strictly decreases afterward. This is its unique global maximum on the admissible interval. \(\Lambda(\theta_*)\approx3.18546477639\); the limiting endpoint thresholds, in increasing theta order, are approximately \(1.22310994254\) and \(2.80370476252\). The monotonicity on \(\theta\in[0,1]\) proved in EC49FTU was correct in its scope but is **not** a global monotonicity statement.

## Proof

1. \(q=a-a_c(b)\) has exact min/max on the price box \(-59/6720\) and \(7/960\). Since \(1+a+b>0\), the requirement \(1+\theta q>0\) for every \(q\) in that range gives exactly \(-960/7<\theta<6720/59\). The bump only adds nonnegative clipped mass.

2. On the nonclipped fibers \(K_\theta=K_0\,w_\theta(z)\), where \(K_0=(16/945)(1+a(m,z)+b(m,z))\) is strictly TP2 and \(w_\theta(z)=1+8\theta(4z-3)/35>0\). The factor \(w_\theta\) depends on \(z\) alone; strict TP2 and stochastic growth of the normalized continuous law under increasing lower endpoint \(L(m)\) are preserved. The full law mixes this continuous component with an atom at the *fixed highest endpoint* \(U\), with probability \(r/(1+r)\). A nondecreasing top-atom weight is sufficient for first-order stochastic order via monotone mixture coupling and is also necessary by the upper-tail event \(\{Z=U\}\). Thus the full order is **equivalent** to monotonicity of \(r_{\theta,\lambda}\).

3. Put \(r_\theta=B_\theta/A_\theta\). Exact polynomial differentiation yields
\[
r_\theta''(m)=\frac{875P(t,\theta)}{589824\,t^3Q_\theta(t)^3},
\]
where \(P\) is integer polynomial of bidegree \((6,3)\), with its full 20 nonzero integer coefficients listed in EC49FTU. The companion \`EC49FTV_FULL_THETA_VERIFY.py\` reconstructs \(P\) independently by the quotient rule from the stated rational \(A_\theta,B_\theta\), and checks the entire bivariate identity coefficient by coefficient.

4. **All-theta sign certificate.** Set \(s=64t/27\in[0,1]\), \(u=(\theta+960/7)/(6720/59+960/7)\in[0,1]\). Write \(P((27/64)s,-960/7+(6720/59+960/7)u)\) in the tensor Bernstein basis of bidegree \((6,3)\). **All 28 Bernstein coefficients are strictly positive**, and the exact smallest coefficient is
\[
\boxed{\min\beta_{ij}=\frac{15814420445330980080708334710364875}{3286064}>0}
\]
at \((i,j)=(6,3)\). Tensor Bernstein basis functions are nonnegative and sum to one, proving \(P>0\) *over the entire rectangle*, not a grid. Also
\[
Q_\theta(t)\ge261457875-1992060(27/64)(6720/59)=9778524525/59>0.
\]
Indeed \(3296t^2-1992060t<0\) for \(0<t\le27/64\), so a negative theta only increases Q and positive theta has the displayed bound. Hence \(r_\theta''(m)>0\) for every admissible theta throughout \(I\).

5. Strict convexity gives \(\inf_{m\in I}r_\theta'(m)=\lim_{m\downarrow1469/64}r_\theta'(m)=\Lambda(\theta)\). Because \(d(\lambda t)/dm=-\lambda\), the ratio \(r_{\theta,\lambda}\) is nondecreasing for all \(m\) precisely when \(\lambda\le\Lambda(\theta)\); if greater it decreases on a left interior neighborhood. This proves both directions including equality. The threshold is positive over the admissible theta interval (the quadratic numerator has negative leading coefficient, and positive endpoint values).

6. Differentiating the exact threshold yields
\[
\Lambda'(\theta)=\frac{2240000(2131469495973983261425-29171587292164226979\theta)}{6561(413340200-1327113\theta)^3}.
\]
The denominator stays positive throughout the admissible range and the numerator changes sign exactly once at the stated interior \(\theta_*\). QED.

## Verification and next research

The standard-library \`Fraction\` checker independently rederives the quotient-rule polynomial identity, evaluates all 28 Bernstein coefficients *exactly* including their minimum, establishes Q's positive rational bound, and checks endpoint/critical phase identities. The polynomial test is an exact finite algebraic certificate; the conditional stochastic-order argument remains analytic. No native 228-observer Bellman optimum was recomputed or independently reviewed. Source GitHub publication is not an Activity checkpoint, Task CLAIM, Result, Review or Foundation admission.

Next: allow a **nonaffine** \(z\)-dependent continuous-kernel perturbation, and determine possible multiple turning points of the atom-compatibility phase boundary; separately retain the frozen native \(z<11/16\) Bellman phase expansion.
