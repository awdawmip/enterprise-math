# Viète stationary integer precision: exact minimal projective state dimension and an explicit depth-3 witness

Status: `FREE_RESEARCH / EXACT ARCHITECTURE-CLASS MINIMALITY THEOREM / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_DYADIC_SLOPE_DEGREE_STATE_LOWER_BOUND_20260903.md`

## 1. Parent lower bound

For the ideal post-seed Viète slope `tau_n`, the parent proves

\[
[\mathbb Q(\tau_n):\mathbb Q]=D_n:=2^{n-1}.
\]

For a stationary rational linear projective precision engine

\[
M\in\operatorname{Mat}_m(\mathbb Q)
\]

whose target projective fixed direction is attached to a simple real eigenvalue and directly exposes `tau_n` as a coordinate ratio, the parent proves

\[
m\ge D_n.
\]

This note constructs a matching engine of dimension exactly `D_n`, so the lower bound is tight for the declared architecture class.

## 2. The slope field is totally real

Let `zeta_n` be the primitive `2^{n+1}`-th root used by the parent and

\[
\tau_n=-i\frac{\zeta_n-1}{\zeta_n+1}.
\]

The parent gives

\[
[\mathbb Q(\tau_n):\mathbb Q]=2^{n-1}.
\]

The maximal real subfield of `Q(zeta_n)` also has degree

\[
\frac12\varphi(2^{n+1})=2^{n-1}.
\]

Since `tau_n` is real and has exactly this degree,

\[
\boxed{
\mathbb Q(\tau_n)=\mathbb Q(\zeta_n+\zeta_n^{-1})
}
\]

as fields inside the cyclotomic extension.

Therefore `Q(tau_n)` is totally real: every algebraic conjugate of `tau_n` is real.

This finite real-conjugate set is what allows one target embedding to be made projectively dominant by a rational polynomial filter.

## 3. Companion-state realization in degree D_n

Let

\[
P_n(x)\in\mathbb Q[x]
\]

be the monic minimal polynomial of `tau_n`, with degree

\[
D=D_n.
\]

Use the transpose companion matrix `C_n` of `P_n`. For every root `sigma` of `P_n`, the vector

\[
v(\sigma)=(1,\sigma,\sigma^2,\ldots,\sigma^{D-1})^T
\]

is an eigenvector of `C_n` with eigenvalue `sigma`.

In particular the target slope is encoded directly by the first coordinate ratio:

\[
\frac{v_2(\tau_n)}{v_1(\tau_n)}=\tau_n.
\]

Thus dimension `D` is sufficient to place the exact target direction inside a rational linear state space. What remains is to make that eigendirection uniquely attracting.

## 4. Rational polynomial separation of the target embedding

Let the distinct real conjugates of `tau_n` be

\[
\tau_n=\sigma_1,\sigma_2,\ldots,\sigma_D.
\]

Because they form a finite set of distinct real points, there exists a real polynomial `r(x)` with

\[
r(\sigma_1)=2,
\qquad
r(\sigma_j)=0\quad(j\ge2).
\]

For example, ordinary Lagrange interpolation supplies one.

Polynomial evaluation at finitely many fixed points is continuous in the coefficients. Therefore the coefficients of `r` can be approximated by rational numbers closely enough to obtain

\[
q(x)\in\mathbb Q[x]
\]

such that

\[
|q(\sigma_1)|>1
\]

and

\[
|q(\sigma_j)|<1\quad(j\ge2).
\]

Hence the rational matrix

\[
A_n=q(C_n)
\]

has the same eigenvectors `v(sigma_j)` and eigenvalues `q(sigma_j)`, with the target eigenvalue uniquely dominant in absolute value.

After multiplying by a common denominator, obtain an integer matrix

\[
\widetilde A_n\in\operatorname{Mat}_D(\mathbb Z)
\]

with exactly the same projective dynamics.

Therefore, for every initial state with nonzero target-eigenvector component,

\[
[\widetilde A_n^k x]
\longrightarrow
[v(\tau_n)]
\]

projectively.

The limiting first coordinate ratio is exactly `tau_n`.

Thus an integer stationary linear projective precision engine exists in dimension

\[
D=2^{n-1}.
\]

## 5. Exact minimality theorem

Combining the parent lower bound with the construction above gives

\[
\boxed{
m_{\min}^{\mathrm{stationary\;integer\;projective}}(n)=2^{n-1}.}
\]

This equality holds under the architecture contract:

1. fixed finite-dimensional integer/rational linear update;
2. convergence to one simple dominant projective eigendirection;
3. ideal Viète slope read directly as a coordinate ratio of that direction.

Consequently each additional post-quarter-turn half-angle **doubles the exact minimum relational state dimension** in this architecture class.

This is stronger than saying that coefficients or denominators grow. The dimension of the stationary relational state itself must double.

## 6. Depth n=2 recovers the Pell engine

At `n=2`,

\[
D=2.
\]

The parent already gives the explicit minimal integer engine

\[
M_2=
\begin{pmatrix}
2&1\\
1&0
\end{pmatrix},
\]

whose projective ratio tends to

\[
\tau_2=\sqrt2-1.
\]

Thus the Pell recurrence is not merely convenient; it is exactly dimension-minimal inside the stationary integer projective class.

## 7. Explicit dimension-four engine at n=3

At `n=3`, the ideal slope `u=tau_3` has minimal polynomial

\[
P_3(x)=x^4+4x^3-6x^2-4x+1.
\]

Use the transpose companion matrix

\[
C=
\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
-1&4&6&-4
\end{pmatrix}.
\]

The target eigenvector is

\[
v(u)=(1,u,u^2,u^3)^T.
\]

A small exact integer polynomial filter is

\[
q(x)=5+6x-4x^2-x^3.
\]

It gives the integer matrix

\[
\boxed{
M_3=q(C)=
\begin{pmatrix}
5&6&-4&-1\\
1&1&0&0\\
0&1&1&0\\
0&0&1&1
\end{pmatrix}.
}
\]

The four eigenvalues of `M_3` are

\[
2+\sqrt2+\sqrt{4+2\sqrt2},
\]

\[
2-\sqrt2+\sqrt{4-2\sqrt2},
\]

\[
2+\sqrt2-\sqrt{4+2\sqrt2},
\]

and

\[
2-\sqrt2-\sqrt{4-2\sqrt2}.
\]

The first is strictly larger than `5`. The absolute values of the other three are each strictly below `4`. Hence the target eigenvalue is uniquely dominant.

Therefore generic projective iteration of `M_3` converges to

\[
[1:u:u^2:u^3].
\]

Starting from `e_1=(1,0,0,0)^T`, the first states are

\[
(1,0,0,0),
\]

\[
(5,1,0,0),
\]

\[
(31,6,1,0),
\]

\[
(187,37,7,1),
\]

\[
(1128,224,44,8),\ldots
\]

so the first coordinate ratios are

\[
0,
\frac15,
\frac6{31},
\frac{37}{187},
\frac{224}{1128},\ldots
\]

and converge to the exact quartic slope `u`.

This is a constructive witness that the `m>=4` lower bound is sharp at the first quartic Viète layer.

## 8. State dimension versus integer magnitude

The resulting precision hierarchy now has three independent costs:

1. `DYADIC_DEPTH n` — ideal half-angle refinement depth;
2. `STATE_DIMENSION 2^(n-1)` — exact minimum stationary integer projective relational dimension;
3. `ITERATION_SCALE k` — number/size of integer iterations used to approach the target eigendirection.

Increasing only integer magnitude at fixed low dimension cannot reproduce the exact stationary architecture at arbitrary `n`.

This makes the phrase “higher precision” structurally nontrivial: precision can demand more relation coordinates, not only more bits per coordinate.

## 9. Boundary

The exact minimality theorem applies only to the declared stationary integer/rational **linear projective** architecture.

Low-dimensional alternatives remain possible if one allows:

- coefficients depending on `n` or iteration depth;
- nonlinear updates;
- algebraic rather than rational coefficients;
- direct G1 nested-radical state;
- approximate targets without an exact projective fixed point.

The theorem therefore classifies one important native precision architecture rather than asserting a universal computational lower bound.

## 10. Next frontier

Two directions are now sharply separated:

- `GROWING_STATE`: exact stationary integer linear dynamics with provably minimal dimension `2^(n-1)`;
- `LOW_STATE_NONSTATIONARY`: fixed small trace state with depth-dependent integer rules.

The next high-value question is whether the actual Enterprise Cell/trace refinement semantics favors one of these, or instead leaves the nested radical entirely at the G1 algebraic readout layer.
