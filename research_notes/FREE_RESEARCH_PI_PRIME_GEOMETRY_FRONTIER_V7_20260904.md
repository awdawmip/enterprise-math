# Free Research — Pi-to-Prime Geometry Frontier V7

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_REAL_SMOOTHING_CLOSED / PNT_ZERO_ENERGY_EQUIVALENCE_CLOSED / QUOTIENT_OPERATOR_NILPOTENT / PSEUDOSPECTRAL_REMAINDER_GAP_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_PARTITIONED`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V6_20260904.md`

## 1. Current completed chain

At the present research strength,

\[
\boxed{
\begin{aligned}
\tau^2
&=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1},\\
\text{prime }p
&=\text{irreducible Krawtchouk birth direction},\\
p^a
&=\text{winding-layer birth},\\
\det\mathcal W_M
&=\operatorname{lcm}(1,\ldots,M),\\
\psi(M)
&=\log\det\mathcal W_M,\\
\Psi_2(M)
&=2M\log M+O(M),\\
\psi(M)&\sim M,\\
\pi(M)&\sim M/\log M.
\end{aligned}}
\]

The PNT closure uses classical real Selberg smoothing fed by the finite prime-winding/Hamming provenance carrier. No external novelty is claimed for the classical theorem or its real-variable smoothing step.

---

## 2. PNT as finite zero energy

For prime-power quotient actions up to `Y_N=floor(sqrt N)`, let `U_N` be their total weight `Lambda(a)/a` and let `E_N` be the positive sum of one-edge, direct pair-edge, and transported pair-edge signless energies.

Then

\[
4U_N^2|\psi(N)/N-1|^2\le3\mathfrak E_N
\]

and

\[
\boxed{
\psi(N)\sim N
\iff
\mathfrak E_N/U_N^2\to0.
}
\]

Thus the prime number theorem is exactly the macroscopic zero-energy phase of a finite prime-power quotient 2-complex.

---

## 3. Universal quotient 2-simplices

For arbitrary action labels `a,b>=1`,

\[
q_bq_a=q_{ab}.
\]

Consequently every ordered pair of histories forms an odd quotient triangle:

\[
2f(n)
=\delta_a f(n)+\delta_{ab}f(n)-\delta_bf(q_a(n)),
\]

with local square coercivity. This arbitrary-action theorem is Lean formalized.

The weighted endpoint variance is the complete graph Laplacian of the one-step quotient cloud and is the canonical centered fluctuation coordinate.

---

## 4. Spectral-target correction

Fix a finite state space `{0,...,N}` with value zero at state `0`. For every action `a>=2`,

\[
(Q_af)(n)=f(\lfloor n/a\rfloor)
\]

strictly lowers positive states. Any positive weighted return operator

\[
P_N=\sum_aw_aQ_a
\]

is therefore strictly triangular and nilpotent.

If

\[
L_N=\min\{k:2^k>N\},
\]

then

\[
P_N^{L_N}=0,
\qquad
\operatorname{Spec}(P_N)=\{0\}.
\]

Hence an ordinary eigenvalue gap is already perfect and contains no useful remainder information.

The exact inverse is

\[
(I+P_N)^{-1}
=I-P_N+P_N^2-\cdots+(-1)^{L_N-1}P_N^{L_N-1},
\]

so

\[
\|(I+P_N)^{-1}\|_{\infty\to\infty}\le L_N=O(\log N).
\]

For deterministic quotient by `2`, this logarithmic amplification is attained exactly. Therefore a residual of order `1/log N` yields only an `O(1)` bound by one-step inversion.

This explains the historical failure of the naive spectral-gap route.

---

## 5. Correct remainder invariant

The missing object is not an eigenvalue but a weighted lower singular-value, curvature, or pseudospectral estimate on the arithmetic sector:

\[
\boxed{
\|(I+P_N)f\|_{\mathcal H_N}^2
+\mathcal C_N(f)
\ge c\|f\|_{\mathcal H_N}^2,
}
\]

where `C_N` is the direct/transported odd-simplex collision energy.

The full pair-simplex family suppresses coherent alternating chains by comparing every two-step route with its direct product edge. Its total weight is of order `(log N)^2`, so unlike one fixed prime triangle it survives normalization.

---

## 6. Formal and computational state

Lean formalized:

- arbitrary quotient composition;
- arbitrary odd-triangle identity;
- local signless coercivity;
- `2-2-4` specialization and exact `-1`-mode exclusion;
- finite quotient-word product recoalescence;
- binary depth lower bound for action products;
- forced arrival at zero beyond binary depth.

Exact Fraction checkers verify:

- harmonic recoalescence and coefficient `2`;
- pair-simplex weighted gap and Gram variance;
- quotient nilpotence, finite Neumann inverse, and sharp logarithmic sup-norm amplification.

---

## 7. Current boundary

Closed:

- geometric prime births and windings;
- `psi` as a finite trace-log;
- PNT normalization by real smoothing;
- PNT zero-energy equivalence;
- finite quotient-simplex fluctuation carrier;
- ordinary spectral/eigenvalue analysis no-go.

Open:

- a native lower singular-value or curvature estimate for the weighted arithmetic quotient complex;
- direct decay of the zero-energy observable without importing the classical smoothing closure;
- a quantitative bound for `psi(x)-x`;
- any RH-scale assertion.

---

## 8. Next mother question

Can the degree-three positive provenance packet be represented as, or shown to dominate, the carré du champ of the degree-two quotient complex in a logarithmic Hilbert norm, with a uniform singular gap after the nilpotent one-step directions are factored out?

This is the correct next target. Further eigenvalue calculations of the finite quotient operator cannot help, because its spectrum is already identically zero.
