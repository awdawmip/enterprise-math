# Free Research — Pi-to-Prime Geometry Frontier V8

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_CLOSED_BY_REAL_SMOOTHING / PNT_ZERO_ENERGY_EQUIVALENCE / AUGMENTED_SINGULAR_GAP_CLOSED / SCALAR_PROVENANCE_NO_GO / ORDERED_OPERATOR_LIFT_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V7_20260904.md`

## 1. Stable completed chain

The current prime extension of the endogenous full-turn geometry is

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
\psi(M)&=\log\det\mathcal W_M,\\
\Psi_2(M)&=2M\log M+O(M),\\
\psi(M)&\sim M,\\
\pi(M)&\sim M/\log M.
\end{aligned}}
\]

The PNT closure uses classical real Selberg smoothing after the finite prime-winding/Hamming carrier supplies the positive degree-two energy. Classical PNT novelty is not claimed.

---

## 2. Finite zero-energy formulation

At square-root action cutoff, the complete positive odd-simplex energy satisfies

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

Thus PNT is exactly the macroscopic zero-energy phase of the finite prime-power quotient 2-complex.

---

## 3. One-step spectrum versus full-complex singular gap

The one-step quotient operator is strictly triangular and nilpotent. Its eigenvalue spectrum is `{0}`, but its inverse `(I+P_N)^-1` has sharp logarithmic sup-norm amplification. Therefore ordinary eigenvalues do not control the remainder.

For the augmented differential retaining one-step, direct pair-edge, and transported pair-edge defects,

\[
\boxed{
\|\mathscr D_Sf(n)\|^2
\ge\frac43U^2|f(n)|^2.
}
\]

Hence the normalized augmented operator has lower singular value at least

\[
2/\sqrt3.
\]

The geometric singular gap is already closed. The remaining issue is to prove arithmetic decay of the corresponding energy.

---

## 4. Scalar provenance is insufficient

A scalar convolution coefficient at product label `c=ab` remembers the final endpoint `q_c(n)` but loses the ordered intermediate vertex `q_a(n)`.

For `n=100` and `18=2*9=9*2`, both paths end at `5`, but pass through `50` and `11`. A field can make their transported defects different. Therefore no scalar function of `c` can reconstruct the transported energy.

This is an exact history/no-resurrection barrier:

\[
\boxed{
(a,b)\mapsto ab
\text{ is too forgetful for the remainder operator.}
}
\]

---

## 5. Required next object

The next degree-three packet must be operator-valued and retain ordered path provenance:

\[
(a,b,q_a(n),q_{ab}(n)).
\]

The scalar sequence

\[
\Lambda_3=D\Lambda_2+\Lambda*\Lambda_2
\]

is only its product-label pushforward. It has the correct total positive mass but not enough incidence data to recover the transported carré du champ.

The target is

\[
\boxed{
\mathscr D_Y^*\mathscr D_Y
\preccurlyeq
\mathbf P_{3,Y}+\mathbf B_Y,
}
\]

where `P_3,Y` is an ordered path-provenance operator and `B_Y` is a controlled boundary operator.

---

## 6. Current formal state

Lean-green finite core already includes:

- arbitrary quotient composition;
- arbitrary odd quotient triangles;
- local square coercivity;
- exact exclusion of the `2-2-4` sign-reversing mode;
- finite quotient-word recoalescence to division by the product label;
- forced zero arrival beyond binary history depth.

Exact Fraction checkers cover weighted odd-simplex gaps, Gram variances, nilpotence, finite Neumann inversion, and sharp logarithmic pseudospectral amplification.

---

## 7. Boundary

Closed:

- prime-birth/winding geometry;
- `psi` trace-log geometry;
- PNT at real-smoothing theorem strength;
- PNT zero-energy equivalence;
- augmented quotient-complex singular gap;
- ordinary eigenvalue route no-go;
- scalar provenance-loss no-go.

Open:

- canonical ordered operator-valued degree-three lift;
- arithmetic asymptotics for that lift;
- native quantitative decay of `psi(x)-x`;
- any RH-scale claim.

---

## 8. Next mother question

Can the existing exact branch-history substrate construct the minimal ordered degree-three runtime key that preserves transported quotient defects, and can its positive operator mass be estimated sharply enough to dominate the centered prime-winding carré du champ?
