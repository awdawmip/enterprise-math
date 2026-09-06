# Pure positive-road RH energy criterion and finite falsification witnesses

Status: `RESEARCH FRONTIER / CORRECTED / PROVED RH-EQUIVALENT POSITIVE-ROAD CRITERION + FINITE FALSIFIER FAMILY / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-PURE-ROAD-ENERGY-FINITE-WITNESS-20260906`
Correction event: `EM-FREE-C4A91D-RAW-COMPLETED-ROAD-CORRECTION-20260906`
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

Define the raw road discrepancy energy

\[
\boxed{
\mathcal Q_a
=\int_0^\infty
|\mu_a((0,x])|^2\frac{dx}{x^2}
=\|E_a-E_0\|_{\rm road}^2.
}
\]

The discrete arithmetic part is entirely positive and uses the full integer population; primes are not selected.

## 2. Correct pure-road RH criterion

The completed Schur energy `Delta_a` and raw road energy `mathcal Q_a` are distinct. Let

\[
C_a(s)=\frac{\xi(s)}{\xi(s+a)},
\qquad
Z_a(s)=\frac{\zeta(s)}{\zeta(s+a)},
\qquad C_a=K_aZ_a.
\]

Under RH the completed energy satisfies

\[
\Delta_a\le
U_{\rm comp}(a):=
2\left[1-\frac{\xi(1)}{\xi(1+a)}\right].
\]

Set `J_a=K_a^{-1}` and

\[
A(a)^2=
\frac1{2\pi}\int_{\mathbb R}
\frac{|1-J_a(1/2+it)|^2}{1/4+t^2}\,dt.
\]

The corrected comparison theorem gives, under RH,

\[
|\sqrt{\mathcal Q_a}-\sqrt{\Delta_a}|\le A(a),
\qquad A(a)=O(a).
\]

Hence define

\[
\boxed{
U_{\rm road}(a)
=\left[\sqrt{U_{\rm comp}(a)}+A(a)\right]^2.
}
\]

Then under RH

\[
\mathcal Q_a\le U_{\rm road}(a)
=2\lambda_1a+O(a^{3/2}),
\]

where

\[
\lambda_1=1+\frac\gamma2-\frac12\log(4\pi).
\]

Conversely, if `mathcal Q_a=O(a)` as `a\downarrow0`, then `E_a` belongs to the road Hilbert space for a sequence tending to zero, and Burnol's converse implies RH. Therefore

\[
\boxed{
RH\iff\mathcal Q_a=O(a)
\iff\|E_a-E_0\|_{\rm road}=O(\sqrt a).
}
\]

The corrected boundary-slope theorem further gives, under RH,

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

The continuous integrals are exact:

\[
\int_0^N K_N(n,y)dy=\log(N/n),
\qquad
\iint_{[0,N]^2}K_N(u,v)dudv=N.
\]

For one-pass evaluation, if

\[
A_n=\sum_{k=2}^n\mathcal R_a(k),
\]

then

\[
\sum_{m,n\le N}\frac{\mathcal R_a(m)\mathcal R_a(n)}{\max(m,n)}
=
\sum_{n=2}^N
\frac{\mathcal R_a(n)^2+2\mathcal R_a(n)A_{n-1}}n,
\]

and the `-1/N` contribution is `-A_N^2/N`.

Each finite observable retains every composite road weight and every pairwise Green interaction.

## 4. Countable finite-inequality RH criterion

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

## 5. Correct finite falsification certificates

The raw finite energy must be compared with `U_road`, not with the smaller completed bound `U_comp`.

Under RH,

\[
\mathcal Q_{a,N}\le\mathcal Q_a\le U_{\rm road}(a).
\]

Therefore any rigorous finite computation satisfying

\[
\boxed{
\mathcal Q_{a,N}>U_{\rm road}(a)
}
\]

falsifies RH.

If RH is false, there cannot exist arbitrarily small `a` with finite `mathcal Q_a`, or such thicknesses would form a sequence and Burnol would imply RH. Hence some `a_0>0` exists such that `mathcal Q_a=infinity` for every `0<a<a_0`. For each such `a`, monotonicity in `N` forces a finite `N` with

\[
\mathcal Q_{a,N}>U_{\rm road}(a).
\]

Thus false RH still produces finite full-road falsification witnesses at every sufficiently thin road scale, including all sufficiently fine dyadic levels.

The earlier threshold `mathcal Q_(a,N)>U_comp(a)` is withdrawn for raw road energy.

## 6. Optional background-free lower envelope

Write

\[
D_{a,N}=\sum_{m,n}\mathcal R_a(m)\mathcal R_a(n)
\left(\frac1{\max(m,n)}-\frac1N\right),
\]

\[
B_{a,N}=\sum_n\mathcal R_a(n)\log(N/n).
\]

For arbitrary continuous background density `c`, the finite energy is

\[
D_{a,N}-2cB_{a,N}+c^2N,
\]

whose exact minimum is

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

Thus

\[
\mathcal Q^{\min}_{a,N}>U_{\rm road}(a)
\]

is a robust sufficient finite falsifier. No completeness claim is made for this minimized family.

## 7. Research meaning

This remains the current purest realization of “合数是路，素数是坑”:

- every `n>=2` contributes positive road mass;
- prime filtering disappears from the arithmetic criterion;
- composite/composite interactions are retained through the Green kernel `1/max(m,n)`;
- only a deterministic continuous road density is subtracted;
- the prime field appears only after the singular zero-thickness derivative.

The current hard target is unchanged: prove `mathcal Q_a=O(a)` directly from the finite full-road Green energies, without importing an RH-equivalent analytic continuation estimate.

## Correction record

The first version incorrectly used the completed Schur upper bound directly for raw road energy. The exact finite Green formula, countable criterion, raw rate criterion, raw slope, and finite-witness completeness survive; only the comparison proof and the falsifier threshold are replaced by the explicit completion-error bound above.
