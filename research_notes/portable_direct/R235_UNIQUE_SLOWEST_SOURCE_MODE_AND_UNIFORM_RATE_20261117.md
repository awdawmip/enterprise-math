# R235 — Unique slowest missing-source mode and certified uniform rate in the R234 230-mode family

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_INTERVAL_CERTIFIED / NOT_REVIEWED**. Native BRC integration: **NOT_EXECUTED**.

## Source and scientific scope

Immutable R234: \`awdawmip/enterprise-math@37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6:research_notes/portable_direct/R234_MAXIMAL_COLLISION_RIGIDITY_AND_230_FAMILY_20261117.md\`. Frozen scientific source \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. P000 and ACTIVE worldview unchanged. The current theorem concerns the **derived scalar source-support observer** of a finite stochastic chain; it does not identify the scalar with the native BRC signed, port, branch, provenance, weight, multiplicity, or cross-moment carrier.

Let s vary in I=(39/100,41/100). The R234 stationary strictly positive seven-source sticky-reset chain is
\[
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\quad b_i=(1-\alpha_i)\pi_i,
\]
with neutral source 0, and
\[
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\
t(s)=\frac{1691s-2615}{2615s-3539},\quad c=5/18,
\]
\[
b_0=13/60,\quad b_i=c|1/2-\alpha_i|\quad (1\le i\le6).
\]
For proper U⊊[6], let D_U={0}∪U. The reversible killed matrix is similar to
\[
K_D=\operatorname{diag}(\alpha_i)_{i\in D}+a_Da_D^T,\quad a_i=\sqrt{b_i}.
\]
The R220–R234 stationary expected-ideal-size sequence, for n≥L, is
\[
\mathbb E F_n-W_6=\sum_{U\subsetneq[6]}W_{|U|}v_{D_U}^T K_{D_U}^{n-1}v_{D_U},
\quad v_i=\sqrt{\rho_i},\quad
\rho_i=\frac{\pi_i/(1-\alpha_i)}{\sum_j\pi_j/(1-\alpha_j)}.
\]
The block weights W_r are strictly positive in the model.

## Theorem — Unique asymptotic bottleneck and rational rate certificate

For **every real s∈I**, including any exceptional parameter with an extra spectral collision, the **unique** proper source subset attaining the maximum killed Perron radius is
\[
D_*=\{0,1,2,4,5,6\}=\{0,\ldots,6\}\setminus\{3\}.
\]
Its radius r(s) is the unique root for x>max alpha_j of
\[
\boxed{\sum_{j\ne3}\frac{b_j(s)}{x-\alpha_j(s)}=1},
\quad\boxed{\frac{99}{100}<r(s)<\frac{991}{1000}}.
\]
Consequently there are A(s)>0 and 0≤sigma(s)<r(s) with
\[
\boxed{\mathbb E[F_n]-W_6=A(s)r(s)^{n-1}+O_s(\sigma(s)^{n-1})}
\]
as n→∞ through integers. Here
\[
A(s)=W_5(v_{D_*}\cdot u_*)^2>0
\]
for the unit Perron eigenvector u_* of K_{D_*}. This unique long-time mode is governed by **exclusion of source 3**, whose holding parameter is 9/20 and reset coefficient b_3=1/72.

### Proof 1: Exact uniform enclosure

Define f_3(x,s)=Σ_{j≠3}b_j(s)/(x−alpha_j(s))−1. For x>max alpha, f_3 is strictly decreasing in x. On I, 3/4<t(s)<4/5. Exact symbolic rational cancellation gives
\[
f_3(99/100,s)=\frac{-49Q_-(s)}{704291004(100s-99)(89785s-88861)}
\]
where
\[
Q_-(s)=1518850343500s^2-1968802891315s+455373749139,
\]
and
\[
f_3(991/1000,s)=\frac{-1964Q_+(s)}{24127412751(1000s-991)(300155s-297383)}
\]
where
\[
Q_+(s)=48471549398125s^2-69426833298695s+21080704373902.
\]
Each denominator is positive on I (product of two negative linear factors). Both Q_- and Q_+ decrease strictly on the closed interval [39/100,41/100]; indeed their derivatives at its right endpoint are negative and both have positive second derivative. Exact endpoint certificates:
\[
Q_-(39/100)=-162884482455/2<0,\quad
Q_+(41/100)=61101614020949/80>0.
\]
Hence f_3(99/100,s)>0>f_3(991/1000,s), giving the claimed unique radius root and strict interval for every real s∈I.

### Proof 2: Comparison with every proper block

Any proper D_U is contained in a single-deletion D_{-i}={0,...,6}\setminus{i}, i∈[6]. Perron–Frobenius strict monotonicity on positive killed transitions gives strict inequality upon proper containment. Compare the six single-deletion blocks at x=r(s)>0.99.

For i∈{1,2,4}, alpha_i<alpha_3=9/20<1/2. At fixed x>1/2 the function a↦(1/2−a)/(x−a) is strictly decreasing. Therefore b_i/(x−alpha_i)>b_3/(x−alpha_3).

For i∈{5,6}, alpha_i≥2/3. Since x<1,
\[
\frac{b_i}{x-\alpha_i}\ge c\frac{\alpha_i-1/2}{1-\alpha_i}\ge c/2,\quad
\frac{b_3}{x-\alpha_3}<c\frac{1/20}{54/100}=c\frac{5}{54}<c/2.
\]
Thus the same strict ratio inequality holds. Writing f_i(x)=Σ_{j≠i}b_j/(x−alpha_j)−1, the equation f_3(r)=0 implies f_i(r)<0 for every i≠3. The functions f_i strictly decrease above their retained holding parameters and each has its unique killed Perron root there. Hence every other single-deletion radius is strictly below r, and all remaining proper masks are smaller still.

Each symmetric K_D is positive definite since alpha_i>0. Its spectral contributions to v_D^T K_D^{n-1}v_D are nonnegative squares. For the unique maximal block D_*, both its Perron eigenvector and v_{D_*} have strictly positive components, so A(s)>0. Every other eigenvalue across the finite family is smaller than r, proving the asymptotic formula.

## Reproduction, evidence boundaries, and next frontier

The accompanying \`R235_unique_slowest_source_mode_check.py\` uses only Python standard-library exact Fraction arithmetic and checks the algebraic numerator identities, endpoint and derivative sign certificates, holding interval, positive stationary inputs and three independent rational substitutions s=39/100,2/5,41/100. The output \`R235_verification.json\` is PASS. The theorem's continuum assertion uses the explicit symbolic inequalities, not finite-sample extrapolation. Independent review: NOT_REVIEWED; proof assistant: NOT_EXECUTED; native BRC EffectHistogram integration: NOT_EXECUTED.

This identifies the asymptotic dominant mode even when the exact recurrence has 230 (or exceptionally fewer) distinct observable spectral modes. Next: certify a quantitative parameter Lipschitz bound and explicit tail error constants; compare few-mode approximation to exact 230-mode and 256-state propagation with actual bit-complexity; separately develop a read-only provenance-preserving native BRC EffectHistogram observer.
