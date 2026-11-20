# C85: a finite vector reduction on the complementary compact Haar region

This note supplies an exact finite replacement for the infinite lattice-vector
maximum in the compact part left by `CUSP_POSITION_THEOREM.md`. It does not
evaluate the resulting compact integral or assert its sign.

## 1. A phase-uniform bound for any fixed lattice

Let `B=(v,w)` have determinant one and set

\[
C(B)=\tfrac12\max_{j=1,2}(|v_j|+|w_j|).
\]

Rounding the two coordinates of `B^{-1}x` proves that `C(B)` is an upper
bound for the lattice's covering radius in the coordinate sup norm. The
same bound applies to every translate.

For an interior position `0<theta<1`, put `t=min(theta,1-theta)` and let
`S_theta(B,alpha)` be the full critical scale from the three source phases.
Then it is exactly sufficient, for **all** source phases, to inspect the
primitive vectors `Bn` satisfying

\[
 \boxed{\|Bn\|_\infty\le4C(B)/t.}             \tag{1}
\]

To prove this uniformly, let `z=(1-theta)alpha_0+theta alpha_2-alpha_1`
and `delta=1-|z|`. The window in endpoint-source coordinates is

\[
P_z=[0,1]^2\cap\{z\le(1-\theta)x+\theta y\le z+1\}.
\]

For `z>=0`, it contains the square `[1-delta,1]^2`; for `z<=0`, it contains
`[0,delta]^2`. In either case its coordinate widths are at most `delta/t`.

For every `sigma<delta/(4C(B))`, the contained square has two disjoint
interior sup-norm balls of radius `sigma C(B)`: take centers at its one-quarter
and three-quarter horizontal positions and its vertical midpoint. Each ball
contains a point of the translated lattice `alpha_endpoint+sigma Lambda`,
so the square contains at least two different lattice points. One of them
is a competitor. Therefore

\[
S_\theta\ge\delta/(4C(B)).                   \tag{2}
\]

Any vector whose successful scale is at least the right side of (2) has
both scaled endpoint differences bounded by a width of `P_z`. Its norm is
therefore at most `4C(B)/t`. Vectors outside (1) cannot improve the maximum.
This proves the reduction. When `delta=0`, the section consists of one
point and the critical scale is zero; the same finite formula gives zero.
Replacing a nonprimitive vector by its same-sign primitive divisor never
decreases its critical scale, so primitive vectors suffice exactly.

The proof uses the actual convex section and its entire lattice, preserving
the dependence between all integer labels. It provides a phase-uniform
bound rather than a numerical truncation rule.

## 2. One fixed integer box for the quarter and midpoint comparison

Use the reduced Haar coordinates

\[
 B=R_\phi\begin{pmatrix}y^{-1/2}&xy^{-1/2}\\0&y^{1/2}\end{pmatrix},
 \quad |x|\le1/2,\quad\sqrt{1-x^2}\le y\le5.
\]

Throughout this compact region,

\[
 |v|<11/10,\qquad |w|<9/4,\qquad C(B)<67/40.
\]

Indeed `|v|^4<=4/3<(11/10)^4`, and
`|w|^2<=y+1/(4y)<=101/20<(9/4)^2`. Thus for all
`theta in [1/4,3/4]`, a vector that matters has sup norm below `134/5`.
The row norms of `B^{-1}` give

\[
 |n_1|<(134/5)\sqrt2(9/4)<86,
 \qquad |n_2|<(134/5)\sqrt2(11/10)<42.
\]

Consequently the single fixed set

\[
 \boxed{\mathcal N=\{(m,n)\in\mathbb Z^2:
 |m|\le85,\ |n|\le41,\ \gcd(|m|,|n|)=1\}}     \tag{3}
\]

contains every potentially maximizing direction, uniformly over the compact
Haar region, every source phase, and the whole position interval
`[1/4,3/4]`. It has 8,696 oriented vectors, or 4,348 unoriented directions.
The identity is exact; no asymptotic or probabilistic completeness claim
is being used.

## 3. Exact phase elimination and a three-variable integral

For fixed `B`, `theta`, and phase `alpha`, every candidate's critical scale
is the minimum of three nonnegative affine functions of alpha (zero marks
are omitted). Taking the maximum over the finite set (3) shows that

\[
S_\theta(B,\alpha)\quad\text{is a continuous, piecewise affine function
of }\alpha\in[0,1]^3.                         \tag{4}
\]

This permits exact phase integration by a finite polyhedral partition.
In particular, if `B` and theta are rational, all cells have rational
vertices and the integral

\[
 H_\theta(B)=\int_{[0,1]^3}S_\theta(B,\alpha)^{1/10}d\alpha
\]

is algebraic. One explicit simplex formula, with `L_i>=0` the values of
the selected affine function at its four vertices and `D` the edge
determinant, is

\[
\int_{\mathrm{simplex}}L^q
=\frac{|D|}{(q+1)(q+2)(q+3)}
 \sum_{i=0}^3\frac{L_i^{q+3}}{\prod_{j\ne i}(L_i-L_j)}.
                                                        \tag{5}
\]

Coincident values use the continuous divided-difference limit. The formula
follows by integrating in barycentric coordinates, or by successive
one-dimensional antiderivatives; it also handles boundary values `L_i=0`.
At `q=1/10` it consists of algebraic numbers. This is a finiteness result,
not a claim that the potentially large polyhedral partition has been
enumerated or that its construction is cheap.

For a compact parameter domain without trigonometric coefficients, write
`tau=sqrt(y)` and `r=tan(phi/2)` with `-1<=r<=1`, taking the rotation
interval `-pi/2<=phi<=pi/2`, which is valid modulo lattice sign. Then

\[
R(r)=\frac1{1+r^2}
\begin{pmatrix}1-r^2&-2r\\2r&1-r^2\end{pmatrix},
\quad
B(x,\tau,r)=R(r)
\begin{pmatrix}\tau^{-1}&x\tau^{-1}\\0&\tau\end{pmatrix}.
\]

The complementary contribution is the exact three-variable integral

\[
 \boxed{I_\theta^{\rm compact}(5)
 =\frac{12}{\pi^2}\int_{-1/2}^{1/2}
 \int_{(1-x^2)^{1/4}}^{\sqrt5}\int_{-1}^1
 \frac{H_\theta(B(x,\tau,r))}{\tau^3(1+r^2)}
 \,dr\,d\tau\,dx.}                         \tag{6}
\]

All infinite lattice competition and all three source phases have thereby
been replaced by a finite piecewise algebraic integrand over a compact
semialgebraic domain. Together with the signed cusp theorem, (6) is a
precise remaining integral for the full quarter/midpoint inequality. The
evaluation and an effective sufficiently sharp integration error bound
remain to be supplied.

## Verification

`verify_compact_reduction.py` checks the exact coefficient bounds, the fixed
box cardinality and the simplex formula on representative exact polynomial
cases. The covering argument and the phase reduction above supply the
general mathematical coverage.
