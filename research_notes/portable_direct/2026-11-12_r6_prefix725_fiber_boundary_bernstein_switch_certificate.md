# PREFIX-725-R6 — Fiber-to-edge Bernstein certificate with finite witness switches

Date: 2026-11-12 (Asia/Shanghai). Mother question: PREFIX-675. Immediate predecessor: PREFIX-724-R6.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.

Status: AUTHOR_PROVED_CONDITIONAL_COMPOSITION / EXACT_FRACTION_TOY_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a reusable *conditional* exact certificate for the original Gamma observer, with an independently executed rational-polynomial example. No additional actual Gamma grid cells are claimed; the inherited count remains 139018/147456.

## 1. Setup and origin

For the auxiliary two-parameter conditional-Gamma maximum observer, let
\[
\mu=E[Y],\quad M_2=E[Y^2],\quad W=M_2-\mu^2,\quad
f_t=W-t\mu,\quad V_q=q^2 f_{1/q},\quad 0\le t\le 1/2.
\]
This combines the equal-mean dominance observation of PREFIX-724 with the finite affine-witness switching method of PREFIX-715/717 and explicit one-dimensional rational Bernstein bounds. It does not reprove the inherited native Gamma K-positivity certificates.

## 2. Rectangle fiber-to-boundary lemma

**Lemma 1.** On any compact axis-aligned rectangle R=[a,b]×[c,d], suppose mu,M2 are C1 on a neighborhood, mu_p>0, mu_z>0 and
\[
J=\mu_p(M_2)_z-\mu_z(M_2)_p=(z-p)K,\qquad K>0
\]
throughout R. Every interior x in R has a boundary competitor y with mu(y)=mu(x) and M2(y)>M2(x). Therefore
\[
\max_R f_t=\max_{\partial R}f_t,\qquad
\max_R V_q=\max_{\partial R}V_q
\]
for all real t and all real q>0.

*Proof.* Fix c0=mu(x). Since mu_p>0, the level set is a graph p=p(z), with p'=-mu_z/mu_p<0. Its allowed z values form an interval from mu(a,z)<=c0<=mu(b,z), because both endpoint functions strictly increase. This compact fiber has both endpoints on the rectangle boundary. Let v=z-p. Since dv/dz=1+mu_z/mu_p>0,
\[
\left.\frac{dM_2}{dv}\right|_{\mu=c_0}
=\frac{J}{\mu_p+\mu_z}
=\frac{vK}{\mu_p+\mu_z}.
\]
The derivative is strictly negative on v<0 and strictly positive on v>0. Thus an interior point has a strictly better endpoint, on the appropriate side (either endpoint if v=0). Along one fiber f_t and V_q/q² differ from M2 only by constants, proving the result. QED.

## 3. Edge Bernstein upper bound

Suppose mu,M2 have exact rational-polynomial coefficients. On any of the four rectangle edges, let s in [0,1] parametrize the edge and write
\[
f_t(s)=\sum_{k=0}^{d}c_k(t)s^k.
\]
The rational Bernstein coefficients are
\[
b_i(t)=\sum_{k=0}^i c_k(t)\frac{\binom{i}{k}}{\binom d k}\quad(0\le i\le d).
\]
The Bernstein basis is nonnegative and its sum is 1, so f_t(s)<=max_i b_i(t). Define U_R(t) as the maximum over all four edge coefficients. By Lemma 1, max_R f_t <= U_R(t). Each coefficient is affine in t, so U_R is convex and piecewise affine.

For the frozen 189-level Gamma construction, survivor rows n=0,...,188 give each mu and M2 separate polynomial degree <=188 in p and z. An edge restriction of W=M2-mu² has degree <=376. Four degree-376 edge arrays contain at most 4×377=1508 coefficients versus 377²=142129 for one full tensor degree-376 array. This is only certificate coefficient accounting; no runtime advantage is claimed without benchmarking.

## 4. Exact finite certification for every real q>=2

Let e1,...,em be feasible comparison points, and set P(t)=max_j f_t(ej), G(t)=P(t)-U_R(t). Let T be the endpoints {0,1/2} plus every intersection of pairwise affine witness lines in that interval. Between consecutive T nodes the maximizing witness is one affine line; G is that line minus convex U_R, hence concave, and its minimum occurs at one of the interval endpoints. Therefore
\[
\min_{0\le t\le1/2}G(t)=\min_{t\in T}G(t).
\]
If all exact node gaps are >=delta>0, then for every real q>=2 and every x in R,
\[
\max_j V_q(e_j)-V_q(x)\ge \delta q^2>0.
\]
This covers the entire continuous real parameter range using finitely many exact rational evaluations. Without K>0 on the rectangle, the same witness-switch argument can instead use a proven two-dimensional tensor Bernstein upper majorant; the edge-only reduction then is not invoked.

## 5. Independently executed exact-polynomial example

Take D=[0,1/2]² and the moment pair
\[
\mu=1+p+z,\quad W=\frac34+\frac{p+z}{4}-4pz,\quad M_2=\mu^2+W.
\]
Here mu_p=mu_z=1, J=4(z-p), and K=4>0 throughout D. The variance W is nonnegative on D (it is bilinear and its minimum is attained at a corner, where the smallest value is zero).

Let R=[1/5,3/10]² and compare with e1=(0,1/2), e2=(0,2/5). Their witness lines cross exactly at t*=1/4. On all four edges of R, f_t is affine in the edge coordinate, so its Bernstein majorant is exact:
\[
U_R(t)=\frac{69}{100}-\frac75t.
\]

| t | U_R(t) | P(t) | certified gap |
|---|---:|---:|---:|
| 0 | 69/100 | 7/8 | 37/200 |
| 1/4 | 17/50 | 1/2 | 4/25 |
| 1/2 | -1/100 | 3/20 | 4/25 |

Thus the exact minimum gap over all real t in [0,1/2] is 4/25, yielding for all real q>=2:
\[
\max_{e\in\{e_1,e_2\}}V_q(e)-\max_{x\in R}V_q(x)\ge \frac4{25}q^2.
\]
The companion Python Fraction code performs exact polynomial substitution, power-to-Bernstein conversion, the three switch-node checks and 21 grid samples on every boundary edge at each node, and returns ALL_CHECKS_PASS PREFIX725-R6. Finite regressions are supplementary: the continuous assertion follows from the two proved structural lemmas and exact node values. This example does not evaluate the frozen Gamma 189-level coefficients.

## 6. Next test in the actual frozen Gamma observer

Select a surviving PREFIX-718 rectangle. Obtain exact positive bounds for mu_p, mu_z and K from its frozen Gamma moment polynomials. Construct the four exact edge restrictions and Bernstein arrays; reuse actual feasible comparison points and their affine switch nodes, and test exact gaps. Record new exclusions only after intersecting with the inherited 139018/147456 certificate set. Where K is not certified positive, either partition or use the original two-dimensional Bernstein path. This conditional reduction is a tool for the PREFIX-675 global optimizer question, not a result about native X6 slice dynamics.