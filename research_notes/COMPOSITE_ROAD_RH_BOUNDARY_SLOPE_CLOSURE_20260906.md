# Composite-road RH boundary slope closure and simplicity detector

Status: `RESEARCH FRONTIER / CORRECTED / CONDITIONAL THEOREM UNDER RH + RH/SIMPLICITY EQUIVALENT CRITERIA / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-ROAD-BOUNDARY-SLOPE-CLOSURE-20260906`
Correction event: `EM-FREE-C4A91D-RAW-COMPLETED-ROAD-CORRECTION-20260906`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_LAYER_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_COMPLETED_SCHUR_PICK_20260906.md`

## 0. Required distinction

Two energies are different and must not be conflated.

On `s=1/2+it`, let

\[
Z_a(s)=\frac{\zeta(s)}{\zeta(s+a)},
\qquad
C_a(s)=\frac{\xi(s)}{\xi(s+a)}=K_a(s)Z_a(s).
\]

The **raw positive-road energy** is

\[
\mathcal Q_a
=\|E_a-E_0\|_{\rm road}^2
=\frac1{2\pi}\int_{\mathbb R}
\frac{|1-Z_a(1/2+it)|^2}{1/4+t^2}\,dt.
\]

The **completed Schur energy** is

\[
\Delta_a
=\frac1{2\pi}\int_{\mathbb R}
\frac{|1-C_a(1/2+it)|^2}{1/4+t^2}\,dt.
\]

Poisson/Schur applies exactly to `Delta_a`, not directly to `mathcal Q_a`.

## 1. Completed Poisson-Schur decomposition

Assume RH. Then `C_a` is Schur on the right half-plane. With

\[
d\omega(t)=\frac{dt}{2\pi(1/4+t^2)},
\]

define

\[
D_a=\int[1-|C_a(1/2+it)|^2]d\omega(t)\ge0.
\]

Poisson's formula at the centered half-plane point `z=1/2`, equivalently `s=1`, gives

\[
\boxed{
\Delta_a
=2\left[1-\frac{\xi(1)}{\xi(1+a)}\right]-D_a.
}
\]

Let

\[
\lambda_1=\frac{\xi'(1)}{\xi(1)}
=1+\frac\gamma2-\frac12\log(4\pi).
\]

Then

\[
\Delta_a\le2\lambda_1a+O(a^2).
\]

## 2. Exact completed radial-defect slope

Under RH, index distinct signed zero ordinates by real `\lambda` and multiplicities `m_\lambda`. Then

\[
|C_a(1/2+it)|^2
=\prod_\lambda
\left(
\frac{(t-\lambda)^2}{a^2+(t-\lambda)^2}
\right)^{m_\lambda}.
\]

Define

\[
d(m)=\frac1{2\pi}\int_{\mathbb R}
\left[1-\left(\frac{u^2}{1+u^2}\right)^m\right]du.
\]

The beta integral gives

\[
\boxed{d(m)=m\frac{\binom{2m}{m}}{4^m}.}
\]

For one zero cluster, scaled convergence gives the contribution

\[
\frac{d(m_\lambda)}{\lambda^2+1/4}.
\]

The global interchange is rigorous. Use

\[
1-\prod_\lambda q_\lambda\le\sum_\lambda(1-q_\lambda),
\]

\[
1-q_\lambda(t)
\le m_\lambda\frac{a^2}{a^2+(t-\lambda)^2},
\]

and the exact convolution

\[
\frac1{2\pi a}\int_{\mathbb R}
\frac{a^2}{a^2+(t-\lambda)^2}
\frac{dt}{1/4+t^2}
=
\frac{a+1/2}{\lambda^2+(a+1/2)^2}.
\]

For `0<a\le1/2` this is at most `1/(\lambda^2+1/4)`, and

\[
\sum_\lambda\frac{m_\lambda}{\lambda^2+1/4}<\infty
\]

under RH. Finite separated zero sets give the matching lower limit. Hence

\[
\boxed{
\lim_{a\downarrow0}\frac{D_a}{a}
=
\sum_\lambda\frac{d(m_\lambda)}{\lambda^2+1/4}.
}
\]

Since

\[
\sum_\lambda\frac{m_\lambda}{\lambda^2+1/4}=2\lambda_1,
\]

one obtains the completed slope

\[
\boxed{
\lim_{a\downarrow0}\frac{\Delta_a}{a}
=
\sum_\lambda
\frac{c(m_\lambda)}{\lambda^2+1/4},
}
\]

where

\[
c(m)=m-d(m)
=m\left(1-\frac{\binom{2m}{m}}{4^m}\right).
\]

## 3. Completion error is lower order

Write

\[
K_a(s)=
\frac{s(s-1)}{(s+a)(s+a-1)}
\pi^{a/2}\frac{\Gamma(s/2)}{\Gamma((s+a)/2)},
\]

and `J_a=K_a^{-1}`, so `Z_a=J_aC_a`.

Define the explicit archimedean error

\[
A(a)^2
=\frac1{2\pi}\int_{\mathbb R}
\frac{|1-J_a(1/2+it)|^2}{1/4+t^2}\,dt.
\]

Under RH, `|C_a|\le1`, hence

\[
\boxed{
|\sqrt{\mathcal Q_a}-\sqrt{\Delta_a}|\le A(a).
}
\]

For every fixed `a_0<1`, uniform Stirling/digamma bounds applied to

\[
\partial_a\log J_a(s)
=
\frac1{s+a}+\frac1{s+a-1}
-\frac12\log\pi
+\frac12\psi((s+a)/2)
\]

show

\[
\boxed{A(a)=O(a)\qquad(a\downarrow0).}
\]

Thus the completion difference is one order smaller in norm than the `sqrt(a)` road boundary layer.

## 4. Raw positive-road slope and RH rate

Because `\sqrt{\Delta_a}=O(\sqrt a)` and `A(a)=O(a)`,

\[
|\mathcal Q_a-\Delta_a|
\le A(a)[2\sqrt{\Delta_a}+A(a)]
=o(a).
\]

Therefore the raw road has the same first-order slope:

\[
\boxed{
\lim_{a\downarrow0}\frac{\mathcal Q_a}{a}
=
\sum_\lambda
\frac{c(m_\lambda)}{\lambda^2+1/4}
\quad\text{under RH}.
}
\]

Also RH implies `mathcal Q_a=O(a)`. Conversely `mathcal Q_a=O(a)` gives road-Hilbert membership for a sequence `a\downarrow0`, so Burnol implies RH. Hence

\[
\boxed{
RH\iff\mathcal Q_a=O(a)
\iff\|E_a-E_0\|_{\rm road}=O(\sqrt a).
}
\]

## 5. Simplicity detector

For `m=1`, `c(1)=1/2`; for `m>1`, `c(m)>m/2`. Therefore under RH

\[
\lim_{a\downarrow0}\frac{\mathcal Q_a}{a}\ge\lambda_1,
\]

with equality iff every nontrivial zero is simple.

Consequently

\[
\boxed{
RH\ \&\ \text{all nontrivial zeros simple}
\iff
\mathcal Q_a=\lambda_1a+o(a).
}
\]

This is an equivalent reformulation, not a proof.

## Status correction

The original version of this note incorrectly identified the raw road energy with the completed Schur energy. That identification is withdrawn. The completed radial-defect theorem is retained, and the raw-road rate/slope/simplicity conclusions are recovered through the explicit `A(a)=O(a)` completion comparison above.
