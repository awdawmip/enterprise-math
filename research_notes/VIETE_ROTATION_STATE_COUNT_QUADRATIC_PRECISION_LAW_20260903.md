# Viète line-segment rotation precision: quadratic scalar error law in the number of finite orientation states

Status: `FREE_RESEARCH / EXACT ASYMPTOTIC STATE-COUNT PRECISION LAW / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parents:
- `research_notes/VIETE_GATE_DISTANCE_HALVING_AND_GATE_PI_READOUT_20260903.md`
- `research_notes/VIETE_TARGET_FREE_TWO_SIDED_GATE_BRACKET_20260903.md`
- `research_notes/VIETE_INTRINSIC_QUARTERING_ASYMPTOTIC_20260903.md`

## 1. Finite orientation-state count

At binary cover depth `m`, use the finite gate state space

\[
G_m=C_{3\cdot2^m}.
\]

Its number of orientation states is

\[
\boxed{M_m:=|G_m|=3\cdot2^m.}
\]

For `m>=2`, the lower scalar gate readout is

\[
\Pi_m^-:=\Pi_m^{\rm gate}
=\frac{M_m}{6}s_m.
\]

The target-free completion constant is

\[
L:=\Pi_{\rm rot}.
\]

## 2. Convert dyadic-depth error into state-count error

The intrinsic quartering theorem in gate indexing gives

\[
L-\Pi_m^-
\sim
\frac{L^3}{6\,4^{m-1}}.
\]

But

\[
M_m^2
=9\cdot4^m,
\]

so

\[
4^{m-1}=\frac{M_m^2}{36}.
\]

Substitution yields

\[
L-\Pi_m^-
\sim
\frac{L^3}{6}\frac{36}{M_m^2}
=
\frac{6L^3}{M_m^2}.
\]

Therefore

\[
\boxed{
M_m^2\bigl(L-\Pi_m^-\bigr)
\longrightarrow
6L^3.
}
\]

This is the direct discrete line-segment rotation-state precision law.

## 3. Quadratic convergence in orientation-state count

Equivalently,

\[
\boxed{
L-\Pi_m^-\asymp M_m^{-2}.
}
\]

Thus doubling the number of finite orientation states quarters the leading scalar completion error.

The previous “one cover bit -> two scalar precision bits” theorem is exactly the logarithmic form of this state-count law.

No classical `pi` is used in the statement or coefficient: the coefficient is the intrinsically generated `6 L^3`.

## 4. Upper readout and certified interval width

The target-free upper gate readout is

\[
\Pi_m^+
=
\frac{M_m}{6}\frac{s_m}{c_m}.
\]

The exact interval width is

\[
W_m:=\Pi_m^+-\Pi_m^-.
\]

From the earlier intrinsic asymptotics,

\[
W_m
\sim
\frac{L^3}{2\,4^{m-1}}.
\]

Hence

\[
\boxed{
M_m^2 W_m
\longrightarrow
18L^3.
}
\]

Since

\[
\Pi_m^-<L<\Pi_m^+,
\]

the upper error is

\[
\Pi_m^+-L
=W_m-(L-\Pi_m^-).
\]

Therefore

\[
\boxed{
M_m^2(\Pi_m^+-L)
\longrightarrow
12L^3.
}
\]

The asymptotic certified interval is thus one-sided asymmetric:

- lower deficit coefficient `6 L^3`;
- upper surplus coefficient `12 L^3`;
- total width coefficient `18 L^3`.

## 5. Exact finite contraction remains stronger than the asymptotic law

The state-count asymptotic says the error is second order in `1/M_m`.

At finite depth the bracket theorem gives the stronger stepwise statement

\[
\frac{W_{m+1}}{W_m}<\frac14
\]

for every refinement.

Since

\[
M_{m+1}=2M_m,
\]

this means the certified uncertainty contracts **strictly faster** than the naive quadratic scaling `M^-2` at every finite step and approaches exact quadratic scaling asymptotically.

## 6. Classical compatibility only renames the intrinsic coefficient

After the separate internal/cross-family and classical compatibility bridges identify

\[
L=\Pi_{\rm rot}=\pi,
\]

the state-count law becomes

\[
\boxed{
\pi-\Pi_m^-
\sim
\frac{6\pi^3}{M_m^2}.
}
\]

Likewise

\[
M_m^2W_m\to18\pi^3.
\]

But these are classical names for target-free laws already proved using `L`.

## 7. Comparison with the Wallis finite spectrum

The independently derived #1159 Wallis completion has a finite tail certificate of order

\[
W_\infty-W_N=O(N^{-1})
\]

in its mode cutoff `N`.

#1158 has just proved

\[
L-\Pi_m^-=O(M_m^{-2})
\]

in finite orientation-state count `M_m`.

These are different finite resource models, so the exponents should not be read as a raw algorithmic speed comparison. But they do show that the common internal completion constant `L=tau` is approached through different discretization geometries:

- Viète: binary orientation-state refinement, second-order scalar completion in state count;
- Wallis: parity-mode spectral cutoff, first-order certified tail in mode count.

The equality `L=tau` therefore links two genuinely different finite precision mechanisms rather than duplicate formulas.

## 8. Precision ontology

At #1158 strength the finite line-segment rotation precision state now has a direct resource interpretation:

\[
\boxed{
\text{ORIENTATION STATE COUNT }M
\longmapsto
\text{SCALAR COMPLETION ERROR }\sim6L^3/M^2.
}
\]

Together with the exact cover-depth coordinate and the native integer-trace rationalization scale, this distinguishes:

1. how many orientation states the refinement permits;
2. how accurately the scalar completion constant is certified;
3. how an ideal orientation is represented by native integer traces when exact trace realization fails.

This is a concrete quantitative meaning of “line-segment rotation precision.”

## 9. Boundary

The theorem is exact for the finite G1 orientation-cover model. It does not assert that G0 Cell rotation has exactly `M_m=3*2^m` native instantaneous Cell states on a physical shell.

`M_m` is the state count of the finite orientation **quotient/refinement**, not a count of native Cells.

Promoting this law to G0 requires the still-open proof that physical Cell rotation realizes the connected binary orientation-cover semantics.
