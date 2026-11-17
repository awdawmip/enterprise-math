# R233 — Two independent rational source spectral collisions yield exact scalar order 230

Date 2026-11-17 (Asia/Shanghai). AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC EffectHistogram NOT_EXECUTED.

## Mathematical scope and provenance

Continue R229–R232; direct immutable predecessor R232@b7801c2e08e1ae3f857b6d5f14e26184caa1bf54 (twenty proper killed blocks sharing one eigenvalue, minimal scalar recurrence order 231). Frozen scientific input remains awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. P000 and ACTIVE Heartbeat World are unchanged: the complete native six-axis, twelve-signed-direction, port, branch, joint relation, source, exact positive weight, provenance and cross-moment carriers are preserved. This is a **derived scalar source-support ideal-cardinality observer**, not a physical BRC dynamical model or an authorization to quotient its native typed state.

Consider the stationary strictly positive sticky-reset Markov chain

\[
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\quad 0<\alpha_i<1,\quad\pi_i>0,\quad \sum_i\pi_i=1
\]

on seven source labels 0,...,6, with 0 neutral. The seven holding parameters are pairwise distinct. Select k=6, m=12 signed-direction labels and tail depth L=2. The exact rational parameters are

\[
\alpha=(1/5,\ 1/4,\ 3/10,\ 9/20,\ 2/5,\ 2/3,\ 1077/1385),
\]
\[
\pi=(13/48,\ 5/54,\ 5/63,\ 5/198,\ 5/108,\ 5/36,\ 3845/11088).
\]

All pi are strictly positive and sum exactly to one.

Write \(b_i=(1-\alpha_i)\pi_i\). For each proper nonneutral subset \(U\subsetneq[6]\), define \(D_U=\{0\}\cup U\) and the monic killed-block polynomial

\[
C_D(x)=\prod_{i\in D}(x-\alpha_i)-\sum_{i\in D}b_i\prod_{j\in D\setminus\{i\}}(x-\alpha_j).
\]

## Collision one: twenty blocks have the same root 1/2

For \(\lambda=1/2\) and \(c=5/18\), direct exact substitution gives

\[
\frac{b_0}{\lambda-\alpha_0}=1-c=13/18,\quad
\frac{b_i}{\lambda-\alpha_i}=
\begin{cases}+c&i=1,2,3,4,\\-c&i=5,6.\end{cases}
\]

Thus \(C_{D_U}(\lambda)=0\) exactly when

\[
|U\cap\{1,2,3,4\}|-|U\cap\{5,6\}|=1.
\]

The proper masks are precisely 1,2,4,8,19,21,22,25,26,28,35,37,38,41,42,44,55,59,61,62, where bit i−1 encodes source i. There are exactly \({6\choose3}=20\), attaining the R232 Sperner multiplicity upper bound for a fixed non-pole eigenvalue. One common mode reduces the generic degree count by 19.

## Collision two: an additional exact rational eigenvalue 5/12

For neutral-only \(D_\varnothing=\{0\}\), the unique killed-block root is

\[
r=\alpha_0+b_0=1/5+(4/5)(13/48)=5/12 .
\]

For proper source mask \(U=\{1,3\}\) (integer 5), the two **added** secular fractions cancel at r:

\[
\frac{b_1}{r-\alpha_1}
=\frac{5/72}{5/12-1/4}=5/12,\qquad
\frac{b_3}{r-\alpha_3}
=\frac{1/72}{5/12-9/20}=-5/12 .
\]

The secular condition \(S_{\{0\}}(r)=1\) therefore also holds on \(D_{\{1,3\}}\). The two killed-block polynomials share \(x-5/12\). These blocks 0 and 5 are outside the twenty-block family that shares 1/2, so this contributes a **second independent** degree collapse.

## Exhaustive exact certificate and proof of minimality

All 63 proper-block polynomials have total degree 249. The full non-killed source block contributes only the stationary eigenmode 1. Run the accompanying standalone Python 3 program R233_two_eigenvalue_collision_230_check.py; it uses only exact fractions.Fraction arithmetic. It checks all 63 polynomials squarefree, each avoiding eigenvalue 1, and explicitly computes all \({63\choose2}=1953\) pairwise polynomial gcds.

The complete rational result is: 191 nontrivial pairwise gcds, of which 190 are \(x-1/2\) between pairs of the twenty indicated blocks, and exactly one is \(x-5/12\) between masks 0 and 5. No other pair shares a root. Consequently the lcm polynomial has degree

\[
\boxed{d_{\min}=1+249-19-1=230}.
\]

This is the **minimal observable** scalar recurrence degree, not merely an upper bound, because the stationary chain is reversible with \(\rho_i\propto\pi_i/(1-\alpha_i)\). Every proper killed block is similar to the positive-definite symmetric matrix \(K_D=\mathrm{diag}(\alpha_i)+vv^\top\), \(v_i=\sqrt{(1-\alpha_i)\pi_i}\). At a secular eigenvalue \(0<\lambda<1\), the corresponding eigenvector has coordinates proportional to \(v_i/(\lambda-\alpha_i)\), and its overlap with the stationary observer vector \(\sqrt{\rho_D}\) is proportional to

\[
\sum_{i\in D}\frac{\pi_i}{\lambda-\alpha_i}
=\frac{1-q_D}{1-\lambda}>0,\quad q_D=\sum_{i\in D}\pi_i<1 .
\]

Every proper-block eigenmode thus has strictly positive scalar observation mass, and positive R215 source-fiber weights prevent cancellation when modes coincide. Hence the exact lcm is the minimal scalar recurrence polynomial. The stationary positive-spectrum source model also yields complete monotonicity of the scalar ideal-size sequence. QED.

## Verification and open questions

R233_verification.json holds the exact PASS certificate for this explicitly parameterized seven-source model, 63 squarefree blocks, 1953 pairwise gcds, and degree 230. Independent review NOT_REVIEWED. Native BRC EffectHistogram integration NOT_EXECUTED.

R233 establishes an **existence** statement at degree 230 in the pairwise-distinct holding-parameter class, not a universal optimum. The broader strictly positive class includes already studied low-order exchangeable cases (R223), so any global-minimum conjecture must specify whether repeated holdings and source symmetry are allowed. Open work: seek further multi-eigenvalue collisions with distinct holdings, or a sharp lower bound for a specified class; compare full exact-bit costs of 230/231/250 scalar realizations and 256-state source-mask propagation; integrate a read-only native typed BRC observer with complete preservation of signed, port, source, provenance, branching, weights, multiplicities and joint cross moments. No formal CLAIM, Result, Review or Foundation promotion is asserted.
