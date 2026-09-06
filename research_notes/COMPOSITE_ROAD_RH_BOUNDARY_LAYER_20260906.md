# Composite-road RH boundary layer: universal zero profile and square-root obstruction

Status: `RESEARCH FRONTIER / CONDITIONAL THEOREM UNDER RH + CONJECTURAL GLOBAL SLOPE / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-ROAD-BOUNDARY-LAYER-20260906`
Parent: `research_notes/COMPOSITE_ROAD_RH_FUTURE_PORT_POSITIVE_DEFORMATION_20260906.md`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T151200+0800-em-free-c4a91d-road-boundary-layer.md`

## 1. Setup

Use the positive all-integer road field

\[
\mathcal R_a(n)=\prod_{p\mid n}(1-p^{-a}),\qquad
E_a(x)=\sum_{n\le x}\mathcal R_a(n)-\frac{x}{\zeta(1+a)},\quad a>0.
\]

Let

\[
\mathcal H_{road}=L^2((0,\infty),dx/x^2),
\qquad E_0=\mathbf1_{[1,\infty)}.
\]

By the exact Burnol transform from the parent note, under RH

\[
\|E_a-E_0\|_{road}^2
=\frac1{2\pi}\int_{\mathbb R}
\frac{\left|\zeta(\tfrac12+it)/\zeta(\tfrac12+a+it)-1\right|^2}
{\tfrac14+t^2}\,dt.
\]

## 2. Universal zero boundary-layer profile

Assume RH. Let

\[
\rho=\frac12+i\gamma
\]

be a nontrivial zero of multiplicity `m`. Locally write

\[
\zeta(\rho+z)=z^m h(z),\qquad h(0)\ne0.
\]

Put `t=gamma+a u`. For every fixed compact set of real `u`, as `a->0+`,

\[
\frac{\zeta(\rho+iau)}{\zeta(\rho+a+iau)}
\longrightarrow
\left(\frac{iu}{1+iu}\right)^m
\]

uniformly.

Thus every critical-line zero creates a universal spectral boundary layer of width `a`; only its multiplicity remains in the scaled profile.

For a finite collection `F` of distinct zeros, their `O(a)` neighborhoods are disjoint for all sufficiently small `a`. Rescaling each neighborhood gives

\[
\liminf_{a\downarrow0}
\frac{\|E_a-E_0\|_{road}^2}{a}
\ge
\sum_{\rho\in F}
\frac{c(m_\rho)}{|\rho|^2},
\]

where

\[
c(m)=\frac1{2\pi}\int_{-\infty}^{\infty}
\left|\left(\frac{iu}{1+iu}\right)^m-1\right|^2du.
\]

An elementary Laplace/Beta evaluation gives

\[
\int_{\mathbb R}
\left|\left(\frac{iu}{1+iu}\right)^m-1\right|^2du
=2\pi m\left(1-\frac{\binom{2m}{m}}{4^m}\right),
\]

hence

\[
\boxed{
c(m)=m\left(1-\frac{\binom{2m}{m}}{4^m}\right).}
\]

Taking increasing finite sets gives the rigorous conditional bound

\[
\boxed{
\liminf_{a\downarrow0}
\frac{\|E_a-E_0\|_{road}^2}{a}
\ge
\sum_{\rho}
\frac{m_\rho\left(1-\binom{2m_\rho}{m_\rho}/4^{m_\rho}\right)}{|\rho|^2}.
}
\]

The sum is over distinct nontrivial zeros.

## 3. Universal square-root lower obstruction

For `m>=1`,

\[
\frac{\binom{2m}{m}}{4^m}\le\frac12,
\]

so `c(m)>=m/2`.

Under RH the classical xi/Hadamard identity becomes

\[
\sum_{\rho}\frac{m_\rho}{|\rho|^2}
=2+\gamma-\log(4\pi).
\]

Therefore

\[
\boxed{
\liminf_{a\downarrow0}
\frac{\|E_a-E_0\|_{road}^2}{a}
\ge
1+\frac\gamma2-\frac12\log(4\pi)
=0.0230957089661\ldots
}
\]

and consequently

\[
\|E_a-E_0\|_{road}
\not=o(\sqrt a).
\]

So, conditional on RH, the positive all-integer road approaches its zero-thickness limit but cannot do so faster than square-root scale in this Hilbert norm. This quantifies the parent note's non-differentiability theorem.

## 4. Multiplicity-sensitive candidate slope

For every fixed finite height `T` avoiding zero ordinates at its endpoints, the same local argument gives an actual `a->0` limit for the truncated spectral integral; only the global high-frequency tail prevents immediate passage to all zeros.

This motivates the explicit conjecture

\[
\lim_{a\downarrow0}
\frac{\|E_a-E_0\|_{road}^2}{a}
=
\sum_{\rho}
\frac{c(m_\rho)}{|\rho|^2}.
\]

This equality is **not proved**.

If all zeros are simple, `c(1)=1/2` and the candidate slope reduces to

\[
1+\frac\gamma2-\frac12\log(4\pi).
\]

If a zero has multiplicity greater than one, then `c(m)>m/2`; hence, if the global slope formula is eventually proved, excess boundary slope above the classical simple-zero constant becomes a direct multiplicity-sensitive observable.

## 5. Exact remaining tail target

The immediate unresolved unit is the uniform tail interchange

\[
\boxed{
\lim_{T\to\infty}\limsup_{a\downarrow0}
\frac1a\int_{|t|>T}
\frac{\left|\zeta(\tfrac12+it)/\zeta(\tfrac12+a+it)-1\right|^2}
{\tfrac14+t^2}\,dt=0.
}
\]

If this is proved under RH, the conjectural slope becomes a theorem. The target is deliberately stated as a future-port/tail-response estimate and is compatible with the current `SPECTRAL_TAIL_FESHBACH_CERTIFICATE`; no claim is made that the existing certificate alone proves it.

## 6. Highest-constraint and BRC interpretation

- The first derivative at `a=0` retains only the first contact layer and loses higher composite interaction orders. It is therefore an observer, not a redundancy certificate.
- The global road is finite-energy for positive thickness under RH, while its prime tangent is globally singular. Hence `TAKE_FIRST_JET_BEFORE_GLOBAL_TAIL_CONTROL` is information-unsafe for this route.
- Positive Weighted-BRC is applicable at `a>0`; the boundary derivative is signed/analytic and remains outside positive recoalescence.
- This note does not alter P000 or promote a theorem into Foundation.

## Primary reference

Jean-Francois Burnol, *On an analytic estimate in the theory of the Riemann Zeta function and a Theorem of Baez-Duarte*, arXiv:math/0202166.
