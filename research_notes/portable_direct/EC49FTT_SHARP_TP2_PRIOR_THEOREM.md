# EC49FTT — Sharp C-infinity prior threshold with an unchanged strictly TP2 continuous fiber

**Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.  
**Date:** 2026-11-19. **Independent portable research.**

## Scientific scope and provenance

Frozen native BRC16943 input: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Native 228-observer / 141-profile Bellman optimum is inherited from EC49FTH PR #2774@999bf1069403306b3813e0e390dae4435d7b4b8c (author-proved; not independently reviewed). External high-gap pricing coordinates and prior-score theorem: EC49FTS PR #2797@7dcff5e1e3713ac34f57484563ab6cdc57b9dd9a; mixed TP2 atom criterion: EC49FTR PR #2795@6e6da57541f965b0c02c27ceed97daddff2e1417. This note proves a new external *prior-dependent* result conditional on the inherited native optimizer. It does not alter P000 or assert heartbeat physics.

## 1. Inherited exact high-gap fibers

Let prices (a,b) range over [3/4,49/64] × [7/16,57/128]. Set M=max_z(D-S) and Z=optimal discount in the inherited [11/16,3/4] regime. On the open high-gap sector

\[
m\in I=(m_2,m_3)=\left(\frac{1469}{64},\frac{187}{8}\right),
\quad U=\frac34,\quad L(m)=\frac{8m+173}{480},
\]

the continuous conditional (unnormalized) density associated with a positive price prior h is

\[
K_h(m,z)=\frac{16}{945}h(a(m,z),b(m,z)),\quad
a(m,z)=\frac{47-m}{945}+\frac{44z}{45},\quad
b(m,z)=\frac1{27}-\frac m{54}+\frac{10z}{9},
\quad L(m)<z<U.
\]

The clipped atom at Z=U has unnormalized mass

\[
B_h(m)=\frac1{54}\int_{a_c(b_m)}^{49/64}h(a,b_m)\,da,\quad
b_m=\frac{47-m}{54},\quad a_c(b)=\frac{77+6b}{105}.
\]

Write A_h(m)=∫_{L(m)}^U K_h(m,z) dz and r_h=B_h/A_h. Common positive normalization of h cancels.

## 2. Strictly TP2 baseline and its exact atom ratio

Take h_0(a,b)=1+a+b. Its continuous kernel is

\[
K_0(m,z)=\frac{16}{945}(1+a(m,z)+b(m,z)),
\qquad
\partial_m\partial_z\log K_0=
\frac{(37/1890)(94/45)}{(1+a(m,z)+b(m,z))^2}>0.
\]

Thus K_0 is strictly TP2 on every interior fiber rectangle. Put t=m_3-m, 0<t<27/64. Exact rational integration yields

\[
A_0(m)=\frac{t(164t+166005)}{267907500},\qquad
B_0(m)=-\frac{(64t-441)(256t+29561)}{43893964800},
\]

and the partial fractions

\[
r_0(m)=-\frac{25}{41}
 +\frac{1997623522965}{22125568(164t+166005)}
 +\frac{1034635}{2158592t}.
\]

Write c_1=1997623522965/22125568>0 and c_2=1034635/2158592>0. Differentiation with t=m_3-m gives

\[
r_0'(m)=\frac{164c_1}{(164t+166005)^2}+\frac{c_2}{t^2}>0,\qquad
r_0''(m)=\frac{2(164)^2c_1}{(164t+166005)^3}+\frac{2c_2}{t^3}>0.
\]

Hence r_0' is strictly increasing on I. Its infimum is the exact left-endpoint value

\[
\lambda_*=\lim_{m\downarrow m_2}r_0'(m)
=\boxed{\frac{171167905504400}{63545784776721}}
\approx2.693615416126.
\]

## 3. Atom-profile realization with a fixed strict-TP2 continuous kernel

Define δ(b)=49/64-a_c(b)>0, m(b)=47-54b and \(\mathcal J=\int_0^1e^{-1/s^2}\,ds>0\). Let the normalized flat bump be

\[
\psi(s)=\begin{cases}0&s\le0,\\e^{-1/s^2}/\mathcal J&s>0.\end{cases}
\]

It is C-infinity on the real line; ∫_0^1 ψ(s) ds=1. For **any** nonnegative C-infinity function g on the closed interval [m_2,m_3], set

\[
f_g(b)=\frac{54A_0(m(b))g(m(b))}{\delta(b)},\qquad
h_g(a,b)=1+a+b+f_g(b)\,
\psi\left(\frac{a-a_c(b)}{\delta(b)}\right).
\]

These define a strictly positive C-infinity, generally nonproduct joint density on the full price box, after normalizing by its finite positive integral. On every nonclipped fiber a<a_c(b), the added term vanishes identically: K_{h_g}=K_0, **including all strict TP2 determinants**. At the clipped atom,

\[
B_{h_g}(m)=B_0(m)+\frac{f_g(b_m)\delta(b_m)}{54}\int_0^1\psi(s)\,ds
=B_0(m)+A_0(m)g(m).
\]

Therefore the exact ratio realizes an *arbitrary nonnegative smooth added profile*:

\[
\boxed{r_{h_g}(m)=r_0(m)+g(m).}
\]

This construction shows that a continuous kernel, even a fixed strictly TP2 one, leaves the atom/order relationship undetermined unless the atom profile is controlled.

## 4. Sharp all-parameter phase transition

Choose the explicit one-parameter family \(g_\lambda(m)=\lambda(m_3-m)\), for \(\lambda\ge0\). Thus

\[
h_\lambda(a,b)=1+a+b+\lambda f(b)
\psi\left(\frac{a-a_c(b)}{\delta(b)}\right),\quad
f(b)=\frac{54A_0(m(b))(m_3-m(b))}{\delta(b)}\ge0,
\]

and

\[
r_\lambda(m)=r_0(m)+\lambda(m_3-m),\qquad
r_\lambda'(m)=r_0'(m)-\lambda.
\]

**Sharp theorem.** Under the inherited high-gap optimizer, for *all* real m<m' in I,

\[
Z\mid M=m\preceq_{\rm st}Z\mid M=m'
\quad\Longleftrightarrow\quad
\boxed{0\le\lambda\le\lambda_*}.
\]

**Proof.** The normalized continuous laws are stochastically increasing: their support lower endpoint L(m) increases, and the positive strictly TP2 kernel K_0 has monotone likelihood ratios on shared support. The mixture adds a top atom at fixed U of probability p_\lambda(m)=r_\lambda(m)/(1+r_\lambda(m)). The mixed law increases in first-order stochastic order if r_\lambda is nondecreasing. Necessity follows by testing the event {Z=U}: stochastic increase requires p_\lambda nondecreasing. Sufficiency follows by monotone mixing with the top endpoint. Since r_0' strictly increases and inf_I r_0'=\lambda_*, r_\lambda is nondecreasing throughout I exactly when \(\lambda\le\lambda_*\). For larger \lambda it is strictly decreasing on an interior left neighborhood, so the top-atom probability moves in the wrong direction. At \(\lambda=\lambda_*\), the derivative is positive at every interior m, so inclusion of the threshold is exact. QED.

## 5. Rational witness on the failure side

Take λ=3>λ_* and the two **interior** points

\[
p=\frac{2939}{128}=\frac{1469}{64}+\frac1{128},\quad
q=\frac{735}{32}=\frac{1469}{64}+\frac1{64}.
\]

Exact rational evaluation gives

\[
r_3(p)-r_3(q)=\frac{729882893080403}{622677793671859328}>0,
\]

and the *actual top-atom probabilities* satisfy

\[
\boxed{\Pr(Z=U\mid M=p)-\Pr(Z=U\mid M=q)
=\frac{23356252578572896}{221362331083011774627}>0.}
\]

Since p<q, this strictly reverses the expected stochastic order. No transcendental integration is needed for the witness because the normalized bump has unit mass; the C-infinity proof establishes the density itself.

## 6. Reproducibility and exact scope

EC49FTT_SHARP_TP2_PRIOR_VERIFY.py uses Python standard-library Fraction arithmetic to check the exact decompositions, endpoint threshold, parameter-domain inequalities, 64 interior samples, four strict TP2 minors, and both explicit rational gaps. The continuous all-real theorem follows from the algebra, TP2 proof and normalized smooth-bump construction, not from finite samples. The original frozen native Bellman theorem remains AUTHOR_PROVED/NOT_REVIEWED and was not rerun.

**Next question:** characterize sharp order conditions when the *continuous* prior kernel also varies with the parameter; or extend native 228-observer Bellman cells to z<11/16. Preserve separate Researcher Activity and formal Task/CLAIM/Result/Review status; this independent portable note does not itself establish any formal control authority.
