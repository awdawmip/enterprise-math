# Viète precision versus relational state complexity: exact gate-degree identity and inverse-square scalar error law

Status: `FREE_RESEARCH / EXACT RESOURCE-SCALING COROLLARY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parents:
- `research_notes/VIETE_DYADIC_SLOPE_DEGREE_STATE_LOWER_BOUND_20260903.md`
- `research_notes/VIETE_STATIONARY_INTEGER_PRECISION_MINIMAL_DIMENSION_20260903.md`
- `research_notes/VIETE_ROTATION_STATE_COUNT_QUADRATIC_PRECISION_LAW_20260903.md`

## 1. Gate level and ideal slope degree

At gate-cover depth `m>=3`, the finite orientation quotient is

\[
G_m=C_{3\cdot2^m}
\]

with state count

\[
M_m=3\cdot2^m.
\]

The corresponding ideal positive Viète slope is the `(m-2)`nd post-quarter-turn half-angle slope in the previous degree indexing.

The degree theorem therefore gives

\[
D_m
=2^{(m-2)-1}
=2^{m-3}.
\]

Hence

\[
\boxed{
D_m=\frac{M_m}{24}.
}
\]

Thus each additional binary orientation cover doubles both:

- the number of finite orientation states;
- the algebraic degree of the exact ideal slope.

## 2. Exact minimum stationary integer projective dimension

The stationary integer/rational projective minimality theorem proves that an exact attracting representation of the ideal slope requires and admits dimension equal to its algebraic degree.

Therefore at gate level `m`:

\[
\boxed{
\dim_{\min}^{\rm stationary\ integer\ projective}(m)
=D_m
=\frac{M_m}{24}.
}
\]

This is an exact equality inside the declared architecture class, not only a lower bound.

## 3. Scalar completion error in gate count

The rotation-state precision theorem gives

\[
M_m^2\bigl(L-\Pi_m\bigr)
\longrightarrow
6L^3,
\]

where

\[
L=\Pi_{\rm rot}.
\]

Using

\[
M_m=24D_m,
\]

we obtain

\[
(24D_m)^2(L-\Pi_m)
\longrightarrow
6L^3.
\]

Therefore

\[
\boxed{
D_m^2(L-\Pi_m)
\longrightarrow
\frac{L^3}{96}.
}
\]

Equivalently,

\[
\boxed{
L-\Pi_m
\sim
\frac{L^3}{96D_m^2}.
}
\]

## 4. Precision–complexity law

Inside the exact stationary integer projective architecture:

\[
\boxed{
\text{SCALAR TRUNCATION ERROR}
\asymp
\frac1{(\text{MINIMUM RELATIONAL STATE DIMENSION})^2}.
}
\]

Thus one additional binary half-angle level causes:

\[
D_{m+1}=2D_m,
\]

while

\[
L-\Pi_{m+1}
\sim
\frac14(L-\Pi_m).
\]

So:

\[
\boxed{
\text{doubling exact stationary relational state width}
\Longrightarrow
\text{quartering scalar completion error asymptotically}.
}
\]

This is the state-complexity form of the “one orientation bit -> two scalar precision bits” law.

## 5. Certified interval width in state dimension

The two-sided target-free bracket has width `W_m` satisfying

\[
M_m^2W_m\longrightarrow18L^3.
\]

Substitute `M_m=24D_m`:

\[
\boxed{
D_m^2W_m
\longrightarrow
\frac{L^3}{32}.
}
\]

Likewise the upper surplus satisfies

\[
M_m^2(\Pi_m^+-L)\to12L^3,
\]

so

\[
\boxed{
D_m^2(\Pi_m^+-L)
\longrightarrow
\frac{L^3}{48}.
}
\]

The lower deficit coefficient is

\[
\frac{L^3}{96},
\]

the upper surplus coefficient is

\[
\frac{L^3}{48},
\]

and total certified width coefficient is

\[
\frac{L^3}{32}.
\]

## 6. Resource hierarchy

#1158 now separates at least four finite resource coordinates:

1. **cover depth `m`** — binary orientation refinement count;
2. **orientation-state count `M_m=3*2^m`**;
3. **exact stationary relational dimension `D_m=M_m/24`** for the ideal slope;
4. **native integer trace magnitude/denominator** when the ideal slope is approximated in low dimension rather than represented exactly.

The first three are rigidly linked inside the stationary exact architecture, while the fourth represents a different low-state/high-magnitude tradeoff.

## 7. Classical naming is later

Using the internal Viète–Wallis bridge and the later classical compatibility

\[
L=\Pi_{\rm rot}=\tau=\pi,
\]

the complexity law becomes

\[
\boxed{
\pi-\Pi_m
\sim
\frac{\pi^3}{96D_m^2}.
}
\]

But the intrinsic law in terms of `L` is prior and target-free.

## 8. Boundary

`D_m` is the exact minimum dimension only for the declared stationary rational/integer **linear projective** encoding of the ideal slope.

Nonstationary, nonlinear, algebraic-coefficient, or approximate low-dimensional engines remain outside this lower-bound/equality class.

Likewise `M_m` is the state count of the finite orientation quotient, not a count of G0 native Cells.
