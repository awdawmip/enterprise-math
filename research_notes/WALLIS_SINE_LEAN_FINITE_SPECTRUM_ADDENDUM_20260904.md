# #1159 Lean finite-spectrum addendum

Status: `FREE_RESEARCH / LEAN-GREEN FINITE SPECTRUM STRENGTHENING / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Parent theory packet: `research_notes/WALLIS_SINE_DISCRETE_ROTATION_SPECTRAL_PRECISION_THEOREMS_20260903.md`
PR: `#1172`, branch `free/1159-spectral-precision-lean-w59a`

## 1. Scope

This addendum records the finite algebraic/spectral content that is now compiled by the
project-pinned Lean toolchain.  It does not promote any theorem to Foundation and it does
not use a continuous circle/Fourier/Sturm--Liouville spectrum as input.

The current #1158 correction remains in force: the cross-family completion bridge may use
the preserved cyclic-interpolation / shortest-root completion results, but none of the
#1159 Lean theorems below depends on the superseded `C2` graph-cover-holonomy model.

## 2. Exact finite sine determinant is now Lean-complete

The finite Dirichlet carrier is the recursive tridiagonal matrix `dirichletMatrix z n`.
The normalized finite determinant is

\[
F_M(x)=\frac1M\det L_{M-1}\!\left(\frac{x^2}{M^2}\right).
\]

Lean now proves the exact formula

\[
\boxed{
F_M(x)=
\sum_{j=0}^{M-1}
\frac{(-1)^j x^{2j}}{(2j+1)!}
\prod_{r=1}^{j}\left(1-\frac{r^2}{M^2}\right).
}
\]

The key newly isolated central-factorial identity is

\[
\boxed{
(2j+1)!\binom{M+j}{2j+1}
=M\prod_{r=1}^{j}(M^2-r^2),
\qquad j<M.
}
\]

Equivalently,

\[
\boxed{
\frac{\binom{M+j}{2j+1}}{M^{2j+1}}
=\frac1{(2j+1)!}
\prod_{r=1}^{j}\left(1-\frac{r^2}{M^2}\right).
}
\]

Thus the finite `sin(x)/x` coefficients are exactly normalized centered/central-factorial
coefficients.  The ordinary sine-series coefficients arise when the finite quadratic
defect factors complete to `1`.  This is a structural project interpretation, not a
historical novelty claim.

Lean files:
- `EnterpriseMath/Precision/DirichletCoefficients.lean`;
- `EnterpriseMath/Precision/DirichletExpansion.lean`;
- `EnterpriseMath/Precision/DirichletNormalizedCoefficients.lean`;
- `EnterpriseMath/Precision/DirichletFiniteSine.lean`.

Pinned-green milestones:
- normalized central-factorial coefficient layer: Lean workflow `#1248`;
- full finite determinant formula: Lean workflow `#1254`.

## 3. The formal spectral polynomial is the actual finite Hermitian charpoly

Lean now proves for every finite size `n`:

\[
\boxed{L_n(z)\text{ is Hermitian}}
\]

and the exact scalar-shift relation

\[
\boxed{zI-L_n(0)=-L_n(z).}
\]

Using `Matrix.eval_charpoly`, determinant sign under negation, and the already formalized
continuant determinant theorem, Lean proves

\[
\boxed{
P_n=\chi_{L_n(0)},
}
\]

where `P_n = dirichletSpectralPoly n` is the monic signed-continuant polynomial.
Consequently the finite spectral polynomial splits over `R` by the standard finite
Hermitian-matrix theorem already present in mathlib.

Lean files:
- `EnterpriseMath/Precision/DirichletMatrix.lean`;
- `EnterpriseMath/Precision/DirichletPolynomial.lean`;
- `EnterpriseMath/Precision/DirichletSpectrumBridge.lean`.

Pinned-green milestones:
- Hermitian/scalar-shift matrix structure: Lean workflow `#1268`;
- charpoly equality + real splitting: Lean workflow `#1270`.

## 4. Parity factors are now genuine real spectral sectors

For an odd fine chain, Lean had already proved the exact polynomial factorization

\[
P_{2n+3}=P^+_n P^-_n,
\]

with

\[
P^+_n=P_{n+1},
\qquad
P^-_n=P_{n+2}-P_n.
\]

The Hermitian charpoly bridge now upgrades this from a formal continuant factorization to
an actual finite real-spectrum factorization.  Both factors split over `R`, and their
root multisets satisfy

\[
\boxed{
\prod \operatorname{roots}(P^+_n)=n+2,
\qquad
\prod \operatorname{roots}(P^-_n)=2.
}
\]

Writing `q=n+2`, the true parity-sector root-product ratio is therefore

\[
\boxed{
\frac{\prod \operatorname{roots}(P^+)}
     {\prod \operatorname{roots}(P^-)}
=\frac q2.
}
\]

This is the Lean-realized spectral meaning of the `q` and `2` factors previously obtained
at recurrence/determinant level.

## 5. Stronger ordering-free mode decimation theorem

The local decimation polynomial remains

\[
R(z)=z(4-z).
\]

Lean now proves the following stronger finite statement without choosing or sorting the
roots.

Let `z` be any root of the odd-parity fine factor `P^-_n`, with `z != 2`.  Then

\[
\boxed{
R(z)\text{ is a root of }P^+_n.
}
\]

Moreover define the endpoint-corrected parity spectral kernel

\[
\mathcal K_q(z)
:=\frac q2\sqrt z\sqrt{4-z}.
\]

For `z >= 0`, Lean proves

\[
\boxed{
\mathcal K_q(z)
=\frac12\,q\sqrt{R(z)}.
}
\]

Thus the two-to-one renormalization is not merely a fundamental-mode accident: every
non-midpoint odd-parity fine spectral mode has an exact coarse spectral descendant under
`z -> z(4-z)`, and the corresponding endpoint-corrected parity kernel collapses to half
the normalized coarse radius.

Lean file:
- `EnterpriseMath/Precision/DirichletParitySpectrumCurvature.lean`.

Pinned-green milestone:
- `WSR-L41..L43`: Lean workflow `#1274`.

## 6. Relation to original WSR-T08

The original theorem packet states the indexed specialization

\[
\operatorname{Curv}_q(\rho)
=\frac{\rho_{2,2q}}4
=\frac{\rho_{1,q}}2.
\]

The Lean result above is stronger in one direction and deliberately weaker in another:

- **stronger:** it proves the exact two-to-one spectral renormalization for every
  non-midpoint odd-parity root, not only the fundamental root;
- **still pending:** it does not yet sort the real root multisets and identify the smallest
  positive root with the project notation `u_(1,M)`, nor does it identify the two parity
  factor root multisets with the ordered lists `u_2,u_4,...` and `u_1,u_3,...`.

Therefore the fully indexed fundamental-mode equation remains a later ordering
specialization.  It must not be reported as Lean-complete merely from the ordering-free
multiset theorem.

A classical Chebyshev/cosine root formula is available in mathlib and could discharge the
ordering compatibility quickly, but using classical `pi/cos` there would be typed as a
**finite effective compatibility readout**, not as input to the native finite construction.

## 7. Remaining major Lean gaps

1. `WSR-T05`: Hamming-shell/Krawtchouk finite integer spectrum and complement-reflection
   parity are not yet formalized.  This is the next preferred native finite target.
2. Ordered-root specialization of `WSR-T08` remains pending as described above.
3. `WSR-T02`: explicit compact-set `O(M^-2)` analytic error certificate remains pending.
4. `WSR-T04`: the infinite Euler-product completion remains pending.
5. The full analytic part of `WSR-T11/T12` remains pending; only its finite/algebraic
   kernels and rational `tau<4` sign certificate are Lean-green.

The next native finite direction is to formalize the Hamming-shell carrier through the
generating polynomials

\[
G_j(X)=(1-X)^j(1+X)^{m-j},
\]

prove the finite identity

\[
jG_{j-1}+(m-j)G_{j+1}=mG_j-2XG_j',
\]

and extract the `X^k` coefficient to obtain the shell eigenvalue `m-2k` (hence `K_m`
eigenvalue `k`) together with complement-reflection parity from `X -> -X`.
