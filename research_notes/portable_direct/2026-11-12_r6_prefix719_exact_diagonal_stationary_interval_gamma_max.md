# PREFIX-719-R6 — uniform diagonal stationary-maximizer interval in the frozen BRC Gamma-clock observer

Date: 2026-11-12 (Asia/Shanghai). Parent: PREFIX-675. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Dependencies: PREFIX-705 survivor monotonicity; PREFIX-710 corrected Gamma-clock kernel; PREFIX-716/718 exact integer recurrence. Evidence: AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Precise new theorem and scope

In the auxiliary statistical parameter domain D=[0,1/2]^2, use the original first-stop count 25<=N_p<=189, independent conditional Gamma(N_p,1) completion clocks T_p,T_z, and Y(p,z)=max(T_p,T_z). Write

\[
\mu(p,z)=E[Y(p,z)],\quad M_2(p,z)=E[Y(p,z)^2],\quad W=M_2-\mu^2,\quad V_q=q^2 W-q\mu.
\]

**Theorem (diagonal stationary maximum).** For each real q>=2 there is at least one p_q in the *open* interval

\[
\boxed{\frac{43}{384}<p_q<\frac{91}{768}}
\]

that maximizes the restricted function p -> V_q(p,p) over the closed interval with these endpoints. In particular the diagonal derivative vanishes at p_q, and p_q is a local maximizer for the diagonal restriction. Neither uniqueness nor global optimality on the full two-parameter square is asserted. The statistical square is not a native two-dimensional Enterprise Math spatial plane.

## Exact Gamma-moment derivative kernel

For 0<=n<=188 set s_n(p)=Pr(N_p>n). The original survivor polynomials are finite, hence smooth. Their monotonicity on [0,1/2] was certified in PREFIX-705 with 17,766 rational Bernstein derivative coefficients. Let

\[
C_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}},\quad 0\le n,m\le188.
\]

The conditional Gamma survivor expansion reads

\[
S_p(u)=e^{-u}\sum_{n=0}^{188}s_n(p)\frac{u^n}{n!}.
\]

Independence gives Pr(Y>u)=S_p(u)+S_z(u)-S_p(u)S_z(u). Integrating the first two tail moments exactly yields

\[
\mu(p,z)=\sum_n(s_n(p)+s_n(z))-\sum_{n,m} C_{nm}s_n(p)s_m(z),
\]

\[
M_2(p,z)=2\sum_n(n+1)(s_n(p)+s_n(z))
-\sum_{n,m}(n+m+1)C_{nm}s_n(p)s_m(z).
\]

Define

\[
A_n(z)=1-\sum_m C_{nm}s_m(z),\qquad
H_n(z)=2(n+1)-\sum_m(n+m+1)C_{nm}s_m(z).
\]

All A_n,H_n are strictly positive: the finite sums are strictly less than their corresponding infinite sums over m with s_m=1, whose values are 1 and 2(n+1). Therefore, by differentiating the finite moments,

\[
\mu_p=\sum_n s'_n(p)A_n(z),\qquad
(M_2)_p=\sum_n s'_n(p)H_n(z).
\]

PREFIX-705 proves s'_n(p)>=0 on the full bias interval. The explicit survivor at stage 25 is s_25(p)=1-p^{25}-(1-p)^{25}, so s'_25(p)=25((1-p)^{24}-p^{24})>0 for 0<p<1/2. It follows that mu_p>0 in the interior.

Put

\[
R_p=\frac{(M_2)_p}{\mu_p},\qquad
\Theta_p=R_p-2\mu,\qquad f_t=W-t\mu,\quad t=\frac1q.
\]

Then the **exact gradient factorization** is

\[
\boxed{\partial_p f_t=\mu_p(\Theta_p-t).}
\]

By exchange symmetry the z derivative has the matching expression. Along p=z=x define \Theta(x)=\Theta_p(x,x); the chain rule gives

\[
\boxed{\frac{d}{dx}f_t(x,x)=2\mu_p(x,x)(\Theta(x)-t).}
\]

This is the load-bearing reduction from a two-clock variance optimization to a scalar, exactly computable diagonal endpoint test.

## Frozen exact endpoint certificate and proof

The accompanying self-contained Python checker reconstructs the original 189-level integer survivor recurrence with the frozen width predicate. It verifies 9,529 nonzero survivor coefficient cells, computes Gamma moments and their bias derivatives entirely with integers/Fraction, and proves strict rational enclosures at

\[
a=\frac{86}{768}=\frac{43}{384},\qquad b=\frac{91}{768}:
\]

\[
\boxed{\frac{566}{1000}<\Theta(a)<\frac{567}{1000}},\qquad
\boxed{-\frac{109}{1000}<\Theta(b)<-\frac{108}{1000}}.
\]

For any t in [0,1/2] (and hence every finite real q>=2), the diagonal derivative is strictly positive at a and strictly negative at b since mu_p>0. The continuous diagonal function attains its maximum on [a,b]. It cannot maximize at a because its derivative there is strictly positive, and cannot maximize at b because its derivative there is strictly negative. Thus a maximizing point p_q lies strictly between a and b and has derivative zero. Multiplying by the positive q^2 preserves it. This proves existence, stationarity and localization uniformly for all q>=2; the proof even covers the limiting t=0 case.

The argument does **not** prove that p_q is the only diagonal stationary point or that a point (p_q,p_q) is a maximizer in D.

## An off-diagonal, q-independent stationary eliminant

For an interior stationary point of f_t with 0<p,z<1/2, mu_p,mu_z>0 and the two gradient equations imply

\[
\Theta_p(p,z)=\Theta_z(p,z)=t.
\]

Eliminating t and the shared term -2mu yields the necessary condition

\[
\boxed{J(p,z):=\mu_p(M_2)_z-\mu_z(M_2)_p=0}.
\]

Equivalently J=mu_p mu_z(R_z-R_p). Exchange symmetry implies J(p,p)=0. A finite exact probe uses 16 predeclared rational grid indices

1, 20, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 380

on the 768 denominator grid. At all 120 ordered pairs i<j the checker finds R_p<R_z and therefore J>0. These 120 pointwise Fraction comparisons are **finite exact evidence only**; they do not establish positivity on the open off-diagonal continuum. This condition nevertheless creates a concrete next mathematical route: prove the sign on continuous rectangles using exact Bernstein or positive-influence bounds, or locate a counterexample. Either result would advance the full optimizer classification.

## Execution, reproducibility and limits

Verified local run of the self-contained full-integer checker:

ALL_CHECKS_PASS PREFIX719-R6 ['43/384', '91/768'] 120

Its companion JSON records the exact interval, strict rational enclosures, 9,529 survivor coefficient count, all 120 rational test pairs via a declared index list and pair-list SHA256, the scientific pin and unresolved questions. Python Fraction is used for acceptance decisions; no floating-point thresholds or inferred CI result are used. Complete original source and method are given by the code and frozen scientific pin; prior PREFIX-705 monotonicity certification is a declared mathematical dependency.

The previous author-certified global exclusion lower bound from PREFIX-718 remains 139018/147456 of D (about 94.2776%). PREFIX-719 contributes a different theorem, **no new excluded area**, no claimed full-square optimizer, no independent review or project mathematical admission.

No authenticated shared-task CLAIM, Owner transition, formal Result or Review is implied. Research source publication is separate from active control identity; the new session issuance attempt returned SESSION_ISSUANCE_QUOTA and the original dispatch lookup was QUEUED when checked. Historic RA-0AA45C8056A76CE3060E2C23 is provenance, not current execution capability.

**Next exact unit:** attempt a certified sign determination or counterexample for J off diagonal on the surviving frontier, and a certified sign analysis of \Theta'(p) in (43/384,91/768), while retaining q-uniformity and the full-square global optimizer as distinct unsolved obligations. Compare the diagonal restricted optimum with feasible boundary witnesses (0,149/1000), (0,146/1000) without assuming dominance.
