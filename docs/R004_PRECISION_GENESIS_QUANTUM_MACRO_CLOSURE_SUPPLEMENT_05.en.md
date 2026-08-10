# R004 precision genesis — Supplement 05: isotropic divisor-grid expansion and finite macro crossover

Status: `PROVED_WIP + EXECUTABLE_CHECKED + CANDIDATE_PHYSICAL_INTERPRETATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_04.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 04 found a canonical arithmetic scale-axis rank but also exposed a weakness in the first prime-product geometry candidate: using the prime-power values themselves as spatial side lengths generally produces unequal global axis lengths.

This supplement moves the geometry to the divisor lattice itself. Prime **exponents**, not prime-power magnitudes, become the intrinsic coordinates. The resulting model is exactly axis-symmetric whenever the active exponents are equal.

## 1. Divisor lattice as an exact finite exponent grid

Let

\[
\lambda=\prod_{i=1}^D p_i^{a_i}.
\]

Every positive divisor of `lambda` has a unique representation

\[
d=\prod_{i=1}^D p_i^{e_i},
\qquad
0\le e_i\le a_i.
\]

Thus the divisor set is in bijection with the finite integer box

\[
\boxed{
X_\lambda
=\prod_{i=1}^D\{0,1,\ldots,a_i\}.
}
\]

Connect two divisor states when exactly one exponent changes by `+1` or `-1`. This is precisely the Hasse graph of the divisor lattice and the Cartesian product of paths of side lengths `a_i+1`.

Therefore

\[
\boxed{|X_\lambda|=\prod_i(a_i+1)=\tau(\lambda),}
\]

\[
\boxed{
|E_\lambda|
=\sum_i a_i\prod_{j\ne i}(a_j+1),
}
\]

and the intrinsic graph diameter is

\[
\boxed{\operatorname{diam}(X_\lambda)=\sum_i a_i.}
\]

The shortest-path metric is the established `L1` distance on exponent coordinates. All of this is standard finite divisor-lattice/graph mathematics.

## 2. Precision one is genuinely one point

At

\[
\lambda=1
\]

there are no active prime factors and hence no exponent coordinates. The divisor grid is the singleton

\[
X_1=\{()\}.
\]

Its arithmetic rank is zero, it has one vertex, no edges and diameter zero.

Crucially, the future value of `D` is not encoded in the factorization of `1`. A later rank-opening event must introduce new prime support. This preserves the strong R004 boundary that precision-one pregeometry must not silently contain a hidden already-expanded coordinate carrier.

## 3. Isotropic genesis family

Choose a squarefree post-genesis support

\[
P=p_1p_2\cdots p_D.
\]

Consider the refinement sequence

\[
\boxed{\lambda_a=P^a,\qquad a=0,1,2,\ldots.}
\]

At level `a>=1`, every active prime exponent equals `a`. Hence

\[
X_{P^a}
\cong
\{0,1,\ldots,a\}^D.
\]

The exact profile is

\[
\boxed{
|V_a|=(a+1)^D,
}
\]

\[
\boxed{
|E_a|=D\,a\,(a+1)^{D-1},
}
\]

\[
\boxed{
\operatorname{diam}(X_{P^a})=Da.
}
\]

For `D=3`:

| level `a` | scale | grid | vertices | diameter |
| --- | --- | --- | ---: | ---: |
| 0 | `1` | point | 1 | 0 |
| 1 | `P` | `2x2x2` | 8 | 3 |
| 2 | `P^2` | `3x3x3` | 27 | 6 |
| 3 | `P^3` | `4x4x4` | 64 | 9 |

This gives a finite expanding-grid candidate with fixed dimension after the first support-opening event.

## 4. Prime-label independence

Let `P` and `Q` be any two squarefree integers with the same number `D` of prime factors. At the same level `a`, the divisor exponent grids of `P^a` and `Q^a` are both exactly

\[
\{0,\ldots,a\}^D.
\]

Ignoring the arithmetic labels attached to the coordinate axes, they are graph-isomorphic by the identity map on exponent vectors.

Consequently every unlabeled graph observable derived only from the exponent grid—vertex count, edge count, diameter, shell/ball structure and the finite distance spectrum—depends only on `(D,a)`, not on which primes occur in `P`.

Thus the candidate no longer asks “why specifically `2,3,5`?” The genuine unresolved question is

\[
\boxed{
\text{why does the first support-opening event have rank }D=3?
}
\]

## 5. Exact nested expansion

The geometry is not rebuilt independently at every level.

The states of level `a` are exponent vectors

\[
0\le e_i\le a.
\]

These form an exact subset of the level `a+1` states

\[
0\le e_i\le a+1.
\]

Moreover, every old Hasse edge remains an edge and no new edge appears between two old states. Therefore

\[
\boxed{
X_{P^a}
\text{ is an induced subgraph of }
X_{P^{a+1}}.
}
\]

Expansion adds only the new outer exponent layers.

## 6. Canonical coarsening by gcd

Let `c|f` be two scale factors and let `d|f` be a divisor-state at the fine scale. Define

\[
\boxed{
\Gamma_{f\to c}(d)=\gcd(d,c).
}
\]

This removes exactly the prime exponents unavailable at the coarse scale and clamps retained exponents to the coarse maxima.

If

\[
c\mid m\mid f,
\]

then standard gcd absorption gives

\[
\boxed{
\Gamma_{m\to c}(\Gamma_{f\to m}(d))
=
\Gamma_{f\to c}(d).
}
\]

Hence divisor-grid coarsening is path independent along nested scales.

For the isotropic sequence, coarsening from `P^(a+1)` to `P^a` simply clamps every exponent `a+1` to `a`.

## 7. Rank opening and contraction are different from ordinary precision change

The prime-axis rank remains the support size

\[
D_{\mathrm{scale}}(\lambda)=\omega(\lambda).
\]

For one refinement `mu=lambda*r`,

\[
\boxed{
D_{\mathrm{scale}}(\mu)-D_{\mathrm{scale}}(\lambda)
=
|\operatorname{supp}(r)\setminus\operatorname{supp}(\lambda)|.
}
\]

Thus increasing an existing prime exponent raises precision without opening a new candidate dimension.

The reverse statement is equally important. A coarsening can reduce precision while leaving rank unchanged. For example

\[
180\to60\to30
\]

keeps support `{2,3,5}` and rank `3` throughout. By contrast

\[
30\to6\to2\to1
\]

has rank sequence

\[
3\to2\to1\to0.
\]

Therefore

\[
\boxed{
\text{precision contraction}
\not\Rightarrow
\text{dimension/rank contraction}.
}
\]

Any black-hole-like interpretation of local precision contraction must prove that coarse dynamics actually removes prime support; exponent loss alone is insufficient.

## 8. Path-independent rank accounting

Because support only changes by set union along refinement, the sum of all rank-opening increments along any divisibility path from `1` to a final scale `lambda` is

\[
\boxed{\omega(\lambda).}
\]

Different factorization schedules may open several new primes at once or one at a time, but the total is path independent.

Likewise, along any descending divisor path from `lambda` back to `1`, the total number of lost support axes is again

\[
\boxed{\omega(\lambda).}
\]

when each loss is counted at the step where that prime disappears entirely.

This is the clean mathematical version of an R004 “opening/contraction loop.” It is only a rank potential on the scale lattice; it is not evidence that cosmological genesis and black-hole physics are physically dual processes.

## 9. Exact finite distance spectrum

For a path with `n` vertices, define the ordered-pair distance polynomial

\[
A_n(z)
=n+2\sum_{s=1}^{n-1}(n-s)z^s.
\]

The coefficient of `z^s` counts ordered coordinate pairs at path distance `s`.

For a rectangular product grid with side lengths `n_1,...,n_D`, the exact ordered `L1` pair-distance spectrum is the coefficient sequence of

\[
\boxed{
\prod_{i=1}^D A_{n_i}(z).
}
\]

This follows because coordinate distances add and independent coordinate-pair counts multiply. R004 computes the product only through finite integer convolution.

For the binary three-dimensional cube the ordered spectrum is

\[
(8,24,24,8),
\]

so the unordered distinct-pair spectrum is

\[
(0,12,12,4).
\]

## 10. Geometry-driven quantum-to-classical toy crossover

The threshold-record bridge defines

\[
\eta(x,y;d_{\mathrm{rec}})
=
\frac{\max(d_{\mathrm{rec}}-d_G(x,y),0)}{d_{\mathrm{rec}}}.
\]

Thus

\[
\eta=0
\iff
 d_G(x,y)\ge d_{\mathrm{rec}}.
\]

On a one-dimensional path `P_N`, the number of unordered distinct pairs at distance at least `d` is exactly

\[
\boxed{
Z(N,d)=
\begin{cases}
0,&N\le d,\\
(N-d)(N-d+1)/2,&N>d.
\end{cases}
}
\]

because there are `N-s` unordered pairs at distance `s`.

For fixed positive `d`, the fraction

\[
Z(N,d)/\binom N2
\]

is nondecreasing with `N`; this can be checked by an exact finite difference, with no infinite-size limit.

For `d=3`, the zero-overlap fractions at `N=3,4,5,8,16` are

\[
0,\quad 1/6,\quad 3/10,\quad 15/28,\quad 91/120.
\]

The same calculation extends to product grids through the distance polynomial above.

For the three-dimensional isotropic grids with record resolution `2`, side lengths `1,2,3,4,5` give exact zero-overlap pair fractions

\[
\boxed{
0,\quad 4/7,\quad 11/13,\quad 13/14,\quad 149/155.
}
\]

Because equal-rank squarefree supports produce the same unlabeled exponent grid, this entire record-crossover sequence is also independent of the specific prime labels.

This gives an exact finite candidate mechanism for increasing classical record distinguishability as the geometry expands. It remains a toy because the threshold-record law and the physical record resolution have not been derived from a real apparatus/environment interaction.

## 11. Revised strongest R004 candidate

The most economical current construction is now:

1. precision one is `lambda=1`, one divisor state and rank zero;
2. one genesis event introduces a squarefree support `P` of rank `D`;
3. subsequent isotropic refinement uses `lambda_a=P^a`;
4. the divisor Hasse graph is the nested expanding grid `{0,...,a}^D`;
5. geometry controls the toy environment-record overlap through graph distance;
6. the zero-overlap fraction can be calculated exactly from a finite distance polynomial;
7. Bell-locality and measurement-independence constraints remain separate causal requirements and cannot be replaced by observable no-signalling alone.

The construction removes several arbitrary choices from earlier R004 toys, but one decisive question remains completely open:

> what finite causal law selects the genesis rank `D`, and why should the selected physical value be exactly three while also reproducing quantum Bell correlations and the observed large-scale symmetries?

That question is now a much sharper target than the original statement that “precision increase creates space.”
