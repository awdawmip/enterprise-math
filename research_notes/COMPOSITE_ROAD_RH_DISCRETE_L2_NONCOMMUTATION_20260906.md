# Discrete full-road l2 RH criterion and escaping-horizon noncommutation

Status: `RESEARCH FRONTIER / PROVED RH-EQUIVALENT DISCRETE ROAD CRITERION + NONCOMMUTATION THEOREM / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-DISCRETE-ROAD-L2-NONCOMMUTATION-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T180500+0800-em-free-c4a91d-discrete-road-l2-noncommutation.md`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_SLOPE_CLOSURE_20260906.md`

## 1. Exact cell decomposition

Let

\[
\mathcal R_a(n)=\prod_{p\mid n}(1-p^{-a}),
\quad c_a=\frac1{\zeta(1+a)},
\quad S_a(N)=\sum_{n\le N}\mathcal R_a(n).
\]

For `N>=1`, define

\[
A_{a,N}=S_a(N)-c_aN-1.
\]

On the cell `x=N+u`, `0<=u<1`,

\[
E_a(x)-E_0(x)=A_{a,N}-c_au.
\]

On `(0,1)`, the difference is `-c_ax`. Therefore

\[
\mathcal Q_a
=c_a^2+\sum_{N\ge1}I_{a,N},
\]

where

\[
I_{a,N}
=\int_0^1\frac{(A_{a,N}-c_au)^2}{(N+u)^2}\,du.
\]

The unweighted cell mean square is exactly

\[
J_{a,N}
=\int_0^1(A_{a,N}-c_au)^2du
=\left(A_{a,N}-\frac{c_a}{2}\right)^2+\frac{c_a^2}{12}.
\]

Hence

\[
\frac{J_{a,N}}{(N+1)^2}
\le I_{a,N}
\le\frac{J_{a,N}}{N^2}.
\]

Define the midpoint road discrepancy

\[
\boxed{
B_{a,N}
=S_a(N)-1-c_a\left(N+\frac12\right).
}
\]

Then `J_(a,N)=B_(a,N)^2+c_a^2/12`.

Because `1/N^2<=4/(N+1)^2`, `mathcal Q_a` is uniformly equivalent, up to absolute constants and an additive `O(c_a^2)`, to

\[
\mathcal D_a
=\sum_{N\ge1}\frac{B_{a,N}^2}{N^2}.
\]

Since `c_a~a`, the extra `c_a^2` is `O(a^2)`. Thus

\[
\boxed{
\mathcal Q_a=O(a)
\iff
\mathcal D_a=O(a).
}
\]

Combining with the corrected pure-road theorem gives the discrete positive-road RH criterion

\[
\boxed{
RH\iff
\sum_{N\ge1}
\frac{\left[
S_a(N)-1-(N+1/2)/\zeta(1+a)
\right]^2}{N^2}
=O(a)
\quad(a\downarrow0).
}
\]

No prime or von-Mangoldt filter appears on the arithmetic side.

## 2. Finite discrete witnesses

For

\[
\mathcal D_{a,M}
=\sum_{N=1}^M\frac{B_{a,N}^2}{N^2},
\]

the cell bounds relate `mathcal D_(a,M)` to the monotone finite road energy `mathcal Q_(a,M)` by universal constants, with the explicit `c_a^2/12` bookkeeping retained if a sharp bound is desired.

Under RH,

\[
\mathcal Q_a\le U_{\rm road}(a)
\]

from the raw/completed comparison note. Consequently a coarse but explicit sufficient finite falsifier is obtained if a finite midpoint discrepancy sum exceeds the corresponding universal-constant multiple of `U_road(a)`. Using the exact `J_(a,N)/(N+1)^2` cell lower bound removes the coarse factor-four slack.

If RH is false, `mathcal Q_a=infinity` for every sufficiently small `a`; equivalence of the cell series then forces `mathcal D_a=infinity` as well, so some finite `M` eventually violates every RH-compatible `O(a)` bound.

## 3. Escaping-horizon noncommutation

For every fixed finite population, the road weights are analytic at zero thickness. For `n>1`,

\[
\mathcal R_a(n)=a\Lambda(n)+O_n(a^2),
\]

and

\[
c_a=a-\gamma a^2+O(a^3).
\]

Thus for fixed `N`,

\[
B_{a,N}
=a\left[\psi(N)-N-\frac12\right]+O_N(a^2).
\]

Therefore, for every fixed finite `M`,

\[
\mathcal D_{a,M}=O_M(a^2),
\qquad
\mathcal Q_{a,M}=O_M(a^2).
\]

In particular,

\[
\boxed{
\lim_{M\to\infty}\lim_{a\downarrow0}
\frac{\mathcal Q_{a,M}}a=0.
}
\]

Under RH, however, the corrected boundary-slope theorem gives

\[
\boxed{
\lim_{a\downarrow0}\lim_{M\to\infty}
\frac{\mathcal Q_{a,M}}a
=
\sum_\rho\frac{c(m_\rho)}{|\rho|^2}
\ge\lambda_1>0.
}
\]

Thus the limits do not commute.

No fixed finite road segment carries the first-order zero-thickness spectral energy. The RH-sensitive contribution necessarily escapes to larger and larger horizons as `a\downarrow0`.

## 4. Highest-principle consequence

This is a direct mathematical instance of the anti-redundancy rule.

At every fixed finite horizon, composites with many distinct factors enter at higher Taylor order and may look negligible. That does **not** make them globally redundant: after the horizon is allowed to diverge, the infinite road resums remote interaction layers into an `O(a)` spectral energy that is absent from every fixed-horizon first-order limit.

Therefore

`FINITE_HORIZON_SMALLNESS != GLOBAL_ROAD_REDUNDANCY`.

`TAKE_A_TO_ZERO_BEFORE_HORIZON_INFINITY != GLOBAL_RH_OBSERVER`.

## 5. Current hard target

The smallest unresolved unit is now a scale-adapted bound on the escaping tail

\[
\sum_{N\ge M(a)}\frac{B_{a,N}^2}{N^2}
\]

for some `M(a)\to\infty`, strong enough to prove total size `O(a)` without importing RH-equivalent zero estimates.

Natural allowed structures are dyadic/logarithmic shell decomposition, exact future-road ports, and relation-spectrum/BRC compression that preserves composite interactions. No such uniform bound is claimed here.
