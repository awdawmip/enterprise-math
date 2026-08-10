# P017×P018 Generation 4 Supplement 02 — affine Möbius/support recovery

Status: `PROVED_WIP STRUCTURE / signed short-interval estimate open`

This supplement gives a second, lower-dimensional recovery map at the same
fourth-root cutoff.  Instead of using the second support moment, it couples one
Möbius moment to the first support moment.

## A1. Exact affine type table

Let

\[
U=k^2+2k,\qquad z=z_3(k)=\lfloor U^{1/4}\rfloor,
\]

and let `n` be a `z`-rough state in `(k^2,U]`.  Define

\[
c(n)=\#\{p:z<p\le k,\ p\mid n\}.
\]

Because `Omega(n)<=3`, the complete arithmetic type table is:

| type | `mu(n)` | `c(n)` | `2-mu-c` |
|---|---:|---:|---:|
| prime | -1 | 0 | 3 |
| squarefree semiprime | +1 | 1 | 0 |
| squarefree triple | -1 | 3 | 0 |
| repeated triple `p^2 q` / `p q^2` | 0 | 2 | 0 |
| prime cube `p^3` | 0 | 1 | 1 |

A repeated semiprime `p^2` cannot occur strictly between consecutive squares.
The factor-size argument from Supplement 01 puts every factor of a three-factor
state at most `k`, so the support depths in the table are exhaustive.

Thus

\[
\boxed{
2-\mu(n)-c(n)
=3\,1_{\mathbb P}(n)+1_{\{n=p^3\}}.
}
\]

This is the exact sign × factor-depth coupling sought in the preceding parity-
transport generation.

## A2. Global affine identity

Write

\[
R_3=\#\{n\in I_k:(n,P_z)=1\},
\]

\[
M_3=\sum_{\substack{n\in I_k\\(n,P_z)=1}}\mu(n),
\]

\[
S_1=\sum_{\substack{n\in I_k\\(n,P_z)=1}}c(n),
\]

and let `C_3` be the number of rough prime cubes in the interval.  Summing the
pointwise table gives

\[
\boxed{
3\pi(I_k)=2R_3-M_3-S_1-C_3.
}
\]

The cube correction is globally tiny:

\[
\boxed{C_3\le1.}
\]

Indeed, if `a^3<b^3` both lay in the interval, then `a^3>k^2`, hence
`a>k^(2/3)`, while

\[
b^3-a^3\ge3a^2+3a+1>2k,
\]

contradicting the window length.

Therefore a prime-free square interval forces the rigid affine signature

\[
\boxed{
2R_3-M_3-S_1=C_3\in\{0,1\}.
}
\]

Equivalently, the sufficient criterion

\[
\boxed{2R_3-M_3-S_1\ge2}
\]

already proves a prime in the square interval.

## A3. Relation to the quadratic support route

The quadratic Generation-4 identity is

\[
3\pi(I_k)=3R_3-3S_1+2S_2+N_2.
\]

The affine identity is genuinely different as an analytic interface:

- quadratic route: unsigned rough count + first and second support moments;
- affine route: unsigned rough count + first support moment + one Möbius moment.

Both are exact finite reconstructions of the same prime indicator, but they ask
for different new analytic information.  The affine route is the shorter
realization of `sign × factor-depth coupling`: squarefree triples are cancelled
by combining their negative Möbius sign with their support depth three, while
repeated triples are cancelled because Möbius vanishes on square factors.

The only type not perfectly cancelled is `p^3`, and the cube layer has capacity
at most one.

## A4. Why this does not reduce to ordinary Möbius cancellation

An unrestricted short-interval estimate for

\[
\sum_{n\in I_k}\mu(n)
\]

does not control `M_3`: the latter is conditioned on absence of every prime
factor `<=z~k^(1/2)`.  The conditioning is exactly the fourth-root rough sieve
which creates the finite support-depth table.

Likewise, controlling `M_3` alone is insufficient.  The exact defect is the
*correlated* combination

\[
\boxed{\Delta_{\rm aff}(k)=2R_3-M_3-S_1.}
\]

A proof needs to show that the Möbius sign distribution and medium-prime column
occupancy cannot conspire to make `Delta_aff` equal the tiny cube correction.

This is weaker and more precise than demanding full pointwise cancellation
`M_3=o(R_3)`: any estimate satisfying

\[
M_3+S_1\le2R_3-2
\]

is enough.

## A5. Prior-art placement

Friedlander--Iwaniec's asymptotic sieve breaks the classical parity problem by
adding Möbius-sensitive bilinear information to the ordinary sieve axioms.  The
present affine defect is a square-diagonal specialization of the type of signed
information one would need; no claim is made that the asymptotic-sieve axiom is
known for intervals of length `2 sqrt(X)` at the rigid square endpoint.

Matomäki--Radziwill and later short-interval multiplicative-function work gives
powerful Möbius/Liouville information in other averaging regimes, but it does
not directly supply this pointwise, fourth-root-rough conditioned affine
inequality.  The distinction must be retained.

## A6. Current preferred attack

Generation 4 now has two equivalent but analytically non-equivalent frontiers:

1. quadratic overlap defect

   \[
   3R_3-3S_1+2S_2;
   \]

2. affine Möbius/support defect

   \[
   2R_3-M_3-S_1.
   \]

A high-value next theorem would bound one of these defects pointwise while
using the square endpoint, rather than applying independent generic norms to
its terms.  Whichever defect admits the stronger square-specific correlation
estimate should become the primary parity-breaking route; the other remains an
exact cross-check.
