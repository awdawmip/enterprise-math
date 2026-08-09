# P022 — Componentwise Asymptotics of Two-Sided Event Repair

Status: `ACTIVE RESEARCH SUPPLEMENT / PROVED ASYMPTOTIC / PRIOR-ART SENSITIVE`  
Parent: `P022_BARLOW_REPAIR_VARIANCE_ASYMPTOTIC`  
Owner: `program/p022-geometry-v2`

## 1. Purpose

The parent theorem proves

\[
\frac{\operatorname{Var}(R_N)}N
\to
7-\frac{6+8\sqrt2}{\pi},
\qquad R_N=E_N+B_N.
\]

This supplement separates that constant into the orientation variance, split variance, and mixed covariance.  The separation is useful because the exact finite covariance changes sign at several small horizons, while the asymptotic covariance is strictly positive.

---

## 2. P022-VA04 — orientation variance constant

The orientation repair is exactly

\[
E_N=A_S+A_T,
\]

where `S,T` are independent simple signed walks and `A_S,A_T` count zero visits at pre-step times.

The exact one-sided variance theorem already gives

\[
\frac{\operatorname{Var}(A_S)}N
\to
1-\frac2\pi.
\]

Independence therefore yields

\[
\boxed{
\frac{\operatorname{Var}(E_N)}N
\to
2\left(1-\frac2\pi\right).
}
\]

---

## 3. P022-VA05 — split variance constant

The parent decomposition is

\[
B_N
=
\frac12(A_U+A_V)+\varepsilon_N,
\]

with

\[
\mathbb E[\varepsilon_N^2]=o(N).
\]

The rotated coordinates have Brownian limits

\[
U\rightsquigarrow\frac{B_1+B_2}{2},
\qquad
V\rightsquigarrow\frac{B_1-B_2}{2}.
\]

Each has variance rate `1/2`, so its zero local time is `sqrt(2)` times a standard Brownian zero local time.  Hence

\[
\frac{\operatorname{Var}(A_U)}N
\to
2\left(1-\frac2\pi\right),
\]

and the same for `A_V`.

The normalized Brownian projections `(B_1+B_2)/sqrt(2)` and `(B_1-B_2)/sqrt(2)` are independent, so

\[
\frac{\operatorname{Cov}(A_U,A_V)}N\to0.
\]

Therefore

\[
\boxed{
\frac{\operatorname{Var}(B_N)}N
\to
1-\frac2\pi.
}
\]

The `L^2`-negligible error cannot change this linear coefficient.

---

## 4. P022-VA06 — mixed covariance constant

Again use

\[
E_N=A_S+A_T,
\qquad
B_N=\frac12(A_U+A_V)+\varepsilon_N,
\]

with `E[epsilon_N^2]=o(N)`.

Cauchy–Schwarz and `Var(E_N)=O(N)` imply

\[
\operatorname{Cov}(E_N,\varepsilon_N)=o(N).
\]

Thus only the four original/rotated wall pairs contribute to the linear covariance coefficient.

For every pair among

\[
(S,U),\ (S,V),\ (T,U),\ (T,V),
\]

the normalized Brownian correlation has absolute value `1/sqrt(2)`.  The parent Brownian cross-local-time lemma gives, after restoring the rotated-coordinate variance scale,

\[
\frac{\operatorname{Cov}(A_{\rm original},A_{\rm rotated})}{N}
\to
1-\frac{2\sqrt2}{\pi}.
\]

There are four such pairs and the split principal part has coefficient `1/2`, hence

\[
\boxed{
\frac{\operatorname{Cov}(E_N,B_N)}N
\to
2\left(1-\frac{2\sqrt2}{\pi}\right).
}
\]

Since

\[
\pi>2\sqrt2,
\]

this asymptotic covariance is strictly positive.

So the exact finite sign changes of `Cov(E_N,B_N)` are a transient phenomenon rather than evidence for an asymptotically cancelling mechanism.

---

## 5. Reconstruction of the total variance constant

Combine VA04–VA06:

\[
\begin{aligned}
\frac{\operatorname{Var}(E_N+B_N)}N
&\to
2\left(1-\frac2\pi\right)
+\left(1-\frac2\pi\right)
+4\left(1-\frac{2\sqrt2}{\pi}\right)\\
&=
\boxed{
7-\frac{6+8\sqrt2}{\pi}
}.
\end{aligned}
\]

Thus the parent constant is not an opaque aggregate.  It has a typed decomposition:

\[
\boxed{
\text{orientation fluctuation}
+
\text{split fluctuation}
+
\text{positive cross-wall fluctuation}.
}
\]

---

## 6. Precision consequence

The two repair mechanisms are neither asymptotically independent nor reducible to one scalar event counter before aggregation.

At diffusive scale:

- orientation contributes twice the single-wall variance constant;
- split contributes one copy;
- interaction contributes a strictly positive fourth term.

Therefore a typed repair model contains predictive information lost by storing only the total repair dimension `E+B`, even though both descriptions share the same final fiber size `2^(E+B)`.

This is a concrete P022 specialization of the general warning that equal fiber cardinality need not preserve mechanism identity or future compositional semantics.
