# Pure positive-road RH energy criterion and finite falsification witnesses

Status: `RESEARCH FRONTIER / PROVED RH-EQUIVALENT POSITIVE-ROAD CRITERION + FINITE FALSIFIER FAMILY / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-PURE-ROAD-ENERGY-FINITE-WITNESS-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T170500+0800-em-free-c4a91d-pure-road-energy-finite-witness.md`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_SLOPE_CLOSURE_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md`
Highest constraint: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`

## 1. Positive full-road discrepancy measure

For `a>0`, define

\[
\mathcal R_a(n)=\prod_{p\mid n}(1-p^{-a})>0,
\qquad \mathcal R_a(1)=1,
\]

\[
c_a=\frac1{\zeta(1+a)},
\qquad
S_a(x)=\sum_{n\le x}\mathcal R_a(n),
\qquad
E_a(x)=S_a(x)-c_ax,
\]

and `E_0=1_[1,infinity)`.

Let

\[
\nu_a=\sum_{n\ge2}\mathcal R_a(n)\delta_n,
\qquad
\lambda_a=c_a\,dx,
\qquad
\mu_a=\nu_a-\lambda_a.
\]

Then, up to integer endpoints,

\[
\mu_a((0,x])=E_a(x)-E_0(x).
\]

Define the road discrepancy energy

\[
\boxed{
\mathcal Q_a
=\int_0^\infty
|\mu_a((0,x])|^2\frac{dx}{x^2}
=\|E_a-E_0\|_{\rm road}^2.
}
\]

The discrete arithmetic part is entirely positive and uses the full integer population; primes are not selected.

## 2. Pure-road RH criterion

The completed Schur/Poisson result gives under RH

\[
\mathcal Q_a
\le
2\left[1-\frac{\xi(1)}{\xi(1+a)}\right]
=2\lambda_1 a+O(a^2),
\]

where

\[
\lambda_1=1+\frac\gamma2-\frac12\log(4\pi).
\]

Conversely, if `mathcal Q_a=O(a)` as `a\downarrow0`, then `E_a` belongs to the road Hilbert space for a sequence tending to zero, and Burnol's converse criterion implies RH.

Therefore

\[
\boxed{
RH\iff \mathcal Q_a=O(a)
\quad(a\downarrow0).
}
\]

Equivalently,

\[
RH\iff\|E_a-E_0\|_{\rm road}=O(\sqrt a).
\]

The boundary-slope theorem further gives, under RH,

\[
\lim_{a\downarrow0}\frac{\mathcal Q_a}{a}
=\sum_\rho\frac{c(m_\rho)}{|\rho|^2},
\qquad
c(m)=m\left(1-\frac{\binom{2m}{m}}{4^m}\right).
\]

Hence

\[
RH\ \&\ \text{all nontrivial zeros simple}
\iff
\mathcal Q_a=\lambda_1a+o(a).
\]

These are equivalent criteria, not proofs.

## 3. Exact finite road Green energy

For integer `N>=2`, let

\[
\mathcal Q_{a,N}
=\int_0^N|\mu_a((0,x])|^2\frac{dx}{x^2}.
\]

Then `mathcal Q_(a,N)` increases with `N` and

\[
\mathcal Q_a=\sup_N\mathcal Q_{a,N}
\]

with value possibly infinite.

The finite cumulative-measure Green kernel is

\[
K_N(u,v)=\frac1{\max(u,v)}-\frac1N.
\]

Thus

\[
\mathcal Q_{a,N}
=\iint_{(0,N]^2}K_N(u,v)d\mu_a(u)d\mu_a(v).
\]

Expanding discrete road against the continuous background gives

\[
\boxed{
\begin{aligned}
\mathcal Q_{a,N}
={}&\sum_{2\le m,n\le N}
\mathcal R_a(m)\mathcal R_a(n)
\left(\frac1{\max(m,n)}-\frac1N\right)\\
&-2c_a\sum_{2\le n\le N}
\mathcal R_a(n)\log\frac Nn
+c_a^2N.
\end{aligned}
}
\]

The continuous integrals used in the expansion are exact:

\[
\int_0^N K_N(n,y)dy=\log(N/n),
\qquad
\iint_{[0,N]^2}K_N(u,v)dudv=N.
\]

For one-pass evaluation, let

\[
A_n=\sum_{k=2}^n\mathcal R_a(k).
\]

Then

\[
\sum_{m,n\le N}\frac{\mathcal R_a(m)\mathcal R_a(n)}{\max(m,n)}
=
\sum_{n=2}^N
\frac{\mathcal R_a(n)^2+2\mathcal R_a(n)A_{n-1}}n,
\]

and the `-1/N` contribution is `-A_N^2/N`.

Each finite observable therefore retains every composite road weight and every pairwise Green interaction.

## 4. Countable finite-inequality criterion

Set `a_j=2^{-j}`. Under RH there are finite `C,j_0` such that

\[
\mathcal Q_{2^{-j},N}\le C2^{-j}
\]

for every `j>=j_0` and every finite `N`.

Conversely, if such `C,j_0` exist, monotone convergence gives finite road energy for a sequence `a_j\downarrow0`, and Burnol implies RH. Hence

\[
\boxed{
RH\iff
\exists C<\infty,j_0:\
\forall j\ge j_0,\forall N\ge2,
\ \mathcal Q_{2^{-j},N}\le C2^{-j}.
}
\]

This is a countable family of finite arithmetic inequalities, not a single finite certificate of truth.

## 5. Finite falsification certificates

Under RH, for every `a>0`,

\[
\mathcal Q_a\le
U(a):=2\left[1-\frac{\xi(1)}{\xi(1+a)}\right].
\]

Therefore any rigorous finite computation with

\[
\boxed{\mathcal Q_{a,N}>U(a)}
\]

falsifies RH.

If RH is false, there cannot exist arbitrarily small `a` with finite `mathcal Q_a`, or those thicknesses would form a sequence and Burnol would imply RH. Hence some `a_0>0` exists such that `mathcal Q_a=infinity` for every `0<a<a_0`. For every such fixed `a`, monotonicity in `N` forces a finite `N` with

\[
\mathcal Q_{a,N}>U(a).
\]

Thus false RH produces finite full-road falsification witnesses at every sufficiently thin road scale, including all sufficiently fine dyadic levels.

## 6. Optional background-free lower envelope

Write

\[
D_{a,N}=\sum_{m,n}\mathcal R_a(m)\mathcal R_a(n)
\left(\frac1{\max(m,n)}-\frac1N\right),
\]

\[
B_{a,N}=\sum_n\mathcal R_a(n)\log(N/n).
\]

If the continuous background density is temporarily allowed to be any real `c`, the energy is

\[
D_{a,N}-2cB_{a,N}+c^2N.
\]

The exact minimum over `c` is

\[
\boxed{
\mathcal Q^{\min}_{a,N}
=D_{a,N}-\frac{B_{a,N}^2}{N}.
}
\]

Since the true `c_a` is one admissible density,

\[
\mathcal Q_{a,N}\ge\mathcal Q^{\min}_{a,N}.
\]

Thus `mathcal Q^min_(a,N)>U(a)` is an even more robust finite falsifier that does not need `c_a` on the left-hand arithmetic side. No completeness claim is made for this minimized family.

## 7. Research meaning

This is the current purest realization of the user rule “合数是路，素数是坑”:

- all `n>=2` contribute positive road mass;
- prime filtering disappears from the arithmetic criterion;
- composite/composite and composite/integer interactions are retained through the Green kernel `1/max(m,n)`;
- only a deterministic continuous road density is subtracted;
- the prime field appears only after the singular zero-thickness derivative, which is not the working state used here.

The new hard target is now purely road-based: prove `mathcal Q_a=O(a)` directly from the finite full-road Green energies, without importing an RH-equivalent analytic continuation estimate.

## Reuse resolution

- `T8_RELATION_OBSERVABLE_SPECTRUM`: `COMPOSE_APPLIED` to the pairwise Green road observable;
- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED` to finite truncation/falsification witnesses;
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; background minimization is only a lower envelope, not a lossless quotient;
- positive Weighted-BRC: `REUSE_APPLIED` to the full positive road mass, while continuous centering remains a separately typed signed discrepancy.
