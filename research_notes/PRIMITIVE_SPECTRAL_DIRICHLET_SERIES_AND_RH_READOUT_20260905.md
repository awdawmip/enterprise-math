# Primitive spectral Dirichlet series and an RH readout

Status: `FREE_RESEARCH / EXACT SPECTRAL REFORMULATION / NOT_AN_RH_PROOF / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Primary issue: `#1159`
Cross-line relevance: RH research.

## 0. Boundary

This note does **not** prove the Riemann hypothesis and does not claim novelty for the classical Dirichlet generating function of Jordan totients.

Its content is a typed bridge:

- the arithmetic coefficients arise internally as primitive moments of the finite Dirichlet rotation spectrum;
- the denominator `1/zeta(s)` arises from the same spectral Mobius decomposition that produced the primitive factors;
- RH can therefore be restated as a pole-location statement for an explicitly defined primitive spectral Dirichlet series.

---

## 1. First primitive reciprocal spectral moment

For a primitive denominator `d>1`, define

\[
\boxed{
Z_1^{\rm prim}(d)
:=
\sum_{\substack{1\le r<d\\(r,d)=1}}
\frac1{u_{r,d}}.
}
\]

The finite spectral/Jordan theorem gives exactly

\[
\boxed{
Z_1^{\rm prim}(d)=\frac{J_2(d)}6.
}
\tag{RH-1}
\]

Thus the arithmetic function `J_2/6` is not introduced externally; it is a finite primitive spectral observable.

---

## 2. Its Dirichlet series

For `Re(s)>3`, absolute convergence gives

\[
\begin{aligned}
\mathcal Z_{\rm spec}(s)
&:=
\sum_{d\ge2}
\frac{Z_1^{\rm prim}(d)}{d^s}\\
&=
\frac16
\sum_{d\ge2}\frac{J_2(d)}{d^s}.
\end{aligned}
\]

The standard divisor identity

\[
J_2=\mu * (n\mapsto n^2)
\]

gives

\[
\sum_{d\ge1}\frac{J_2(d)}{d^s}
=\frac{\zeta(s-2)}{\zeta(s)}.
\]

Since `J_2(1)=1`,

\[
\boxed{
\mathcal Z_{\rm spec}(s)
=
\frac16
\left(
\frac{\zeta(s-2)}{\zeta(s)}-1
\right).
}
\tag{RH-2}
\]

This identity first holds in the absolute-convergence half-plane and then supplies the meromorphic continuation through the zeta quotient.

---

## 3. Prime local factor from spectral denominator Frobenius

The same identity factors as

\[
\boxed{
\sum_{d\ge1}
\frac{J_2(d)}{d^s}
=
\prod_p
\frac{1-p^{-s}}{1-p^{2-s}}.
}
\tag{RH-3}
\]

The numerator is the Mobius/primitive exclusion factor, while the denominator carries the weight-2 eigencharacter `p^2` of the denominator-Frobenius operator

\[
\mathsf F_pJ_2=p^2J_2.
\]

Thus the local Euler factor has a direct finite-spectral interpretation:

```text
primitive denominator exclusion      -> (1-p^-s)
weight-2 spectral Frobenius character -> (1-p^(2-s))^-1
```

No RH conclusion follows merely from this factorization.

---

## 4. Exact RH pole reformulation

Let `rho` be a nontrivial zero of `zeta(s)`.

Then

\[
0<\Re\rho<1.
\]

Hence

\[
-2<\Re(\rho-2)<-1.
\]

The zeta function has no zero in that open strip: its nontrivial zeros lie in `0<Re<1`, and its trivial zeros are the negative even integers.  Therefore

\[
\zeta(\rho-2)\ne0.
\]

So every nontrivial zero of `zeta(s)` is a genuine pole of

\[
\frac{\zeta(s-2)}{\zeta(s)},
\]

with the same multiplicity.

Consequently:

\[
\boxed{
\text{RH}
\iff
\text{every nonreal pole of }\mathcal Z_{\rm spec}(s)
\text{ arising from a nontrivial zeta zero has }\Re s=\frac12.
}
\tag{RH-4}
\]

Equivalently, RH is the critical-line pole statement for the Dirichlet series of the first primitive reciprocal finite-spectral moment.

This is a reformulation only.

---

## 5. All primitive moment Dirichlet series share the same denominator

For every `n>=1`, the ordinary primitive moment has the universal Jordan expansion

\[
Z_n^{\rm prim}(d)
=\sum_{r=1}^n A_{n,r}J_{2r}(d),
\qquad A_{n,r}\in\mathbf Q.
\]

Therefore, for `Re(s)>2n+1`,

\[
\boxed{
\sum_{d\ge2}
\frac{Z_n^{\rm prim}(d)}{d^s}
=
\frac1{\zeta(s)}
\sum_{r=1}^n
A_{n,r}\zeta(s-2r)
-
\sum_{r=1}^nA_{n,r}.
}
\tag{RH-5}
\]

Thus the entire primitive spectral-moment hierarchy carries the same arithmetic denominator `zeta(s)`.

Cancellation at a particular zeta zero can occur for special higher-moment numerators, so the first moment (RH-2) is the cleanest exact RH-equivalent pole observer.

---

## 6. Master primitive-logarithm Dirichlet series

Recall the normalized primitive factor identity in formal phase:

\[
-\log\widehat\Psi_d(U(t))
=
\sum_{r\ge1}\kappa_rJ_{2r}(d)t^r.
\]

Define coefficientwise in `t`

\[
\boxed{
\mathfrak P(s,t)
:=
\sum_{d\ge2}
\frac{-\log\widehat\Psi_d(U(t))}{d^s}.
}
\tag{RH-6}
\]

This is interpreted as a formal power series in `t` whose coefficients are meromorphic functions of `s`; no single common absolute-convergence half-plane is asserted for all `t`-coefficients at once.

Coefficientwise Jordan summation gives

\[
\boxed{
\mathfrak P(s,t)
=
\frac1{\zeta(s)}
\sum_{r\ge1}
\kappa_r\zeta(s-2r)t^r
-
\mathcal K(t),
}
\tag{RH-7}
\]

where

\[
\mathcal K(t)=\sum_{r\ge1}\kappa_rt^r=-\log U'(t).
\]

Thus one formal identity packages the complete primitive spectral divisor hierarchy into shifted zeta quotients.

---

## 7. Spectral Mobius interpretation of the reciprocal zeta factor

The factor `1/zeta(s)` is exactly the Dirichlet generating series of the Mobius function:

\[
\frac1{\zeta(s)}=\sum_{n\ge1}\frac{\mu(n)}{n^s}.
\]

In #1159 the same `mu` already appears before any Dirichlet series, through the finite primitive factor extraction

\[
\widehat\Psi_d
=
\prod_{e\mid d}H_e^{\mu(d/e)}.
\]

So the analytic reciprocal-zeta denominator in (RH-7) is the Dirichlet-series image of the finite spectral primitive/Mobius decomposition.

This is the conceptual bridge:

```text
finite divisor lattice of spectral scales
  -> primitive Mobius extraction
  -> Jordan/Frobenius weights
  -> Dirichlet transform
  -> shifted-zeta numerator / zeta denominator
```

---

## 8. What this does and does not suggest for RH research

The useful research target is not “the spectral formula proves RH”.  It does not.

What it supplies is a finite-algebraic source for an RH-equivalent meromorphic observer.  Any genuine new RH leverage would have to add a property of the primitive spectral coefficients or of the BRC/decimation dynamics that is **stronger than the already-known Jordan-totient Dirichlet series identity**.

Potential nontrivial directions include:

1. a positivity/total-positivity statement for a transformed primitive spectral kernel that survives Dirichlet/Mellin passage;
2. a self-adjoint or unitary completion whose resolvent trace equals a nontrivial transform of `mathcal Z_spec`;
3. `p`-adic constraints on the spectral Riccati coefficients `beta_n` that are not merely Bernoulli theory in disguise;
4. a BRC transfer realization in which the `1/zeta(s)` pole denominator is forced by an operation-safe spectral determinant rather than introduced through classical Dirichlet convolution.

Until one of those extra structures is proved, (RH-4) remains a rigorous reformulation, not progress on the location theorem itself.

Freeze:

`FIRST_PRIMITIVE_SPECTRAL_MOMENT_DGF = (ZETA(s-2)/ZETA(s)-1)/6`.

`RH = CRITICAL_LINE_POLE_STATEMENT_FOR_THIS_SPECTRAL_DGF`.

`SPECTRAL_REINTERPRETATION != RH_PROOF`.
