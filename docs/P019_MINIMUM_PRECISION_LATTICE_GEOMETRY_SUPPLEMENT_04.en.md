# P019 Supplement 04 — Fiber-Minimum Contraction, Tagged Radial Balls, and Exact Dimensional Closure

Status: `RESEARCH WIP / CORE IDENTITIES PROVED COMBINATORIALLY`  
Scope: finite-precision radial balls, dimension contraction, min-plus composition, collision interpretation, block-size-tagged boundary recursion  
Discipline: integer states, finite minima, finite differences, and discrete relations only; no calculus or continuum limit is used.

## 1. The problem left by Supplement 03

Supplement 03 proved that, for primitive graph balls in `A_p`, the cut boundary in a fixed primitive direction is in exact bijection with an `A_{p-1}` graph ball of the same radius.

For the quadratic radial energy

\[
E(x)=\sum_i x_i^2,
\]

or equivalently `q=E/2`, the same statement fails if the contracted object is forced to be an **untagged** ordinary lower-dimensional radial ball.

The failure is not a failure of dimensional closure. The missing information is the relation context recording how many original unit slots were merged into each visible coordinate.

Keeping that block-size tag restores exact closure.

## 2. P019-X04 — Fiber-minimum square energy of one block

For `m>=1` integer slots constrained by

\[
a_1+\cdots+a_m=c,
\]

define

\[
\psi_m(c)
:=
\min\left\{\sum_{i=1}^m a_i^2:\sum_i a_i=c\right\}.
\]

Write

\[
|c|=mq+r,
\qquad 0\le r<m.
\]

The minimum is attained by distributing the total as evenly as possible, hence

\[
\boxed{
\psi_m(c)
=(m-r)q^2+r(q+1)^2.
}
\]

In particular,

\[
\boxed{\psi_m(1)=1\quad\forall m\ge1.}
\]

Thus the statement that one unit remains one unit under arbitrary finite slot capacity becomes an exact integer minimum-energy invariant.

For `|c|<=m`,

\[
\psi_m(c)=|c|.
\]

The square energy exceeds raw unit count only once units must overlap because the available slots are exhausted.

## 3. Direct connection to the P011 collision spectrum

For `n=|c|` nonnegative units placed in `m` slots with occupancies `a_i`,

\[
a_i^2=a_i+2\binom{a_i}{2},
\]

so

\[
\sum_i a_i^2
=n+2\sum_i\binom{a_i}{2}.
\]

Therefore

\[
\boxed{
\psi_m(n)
=n+2J^{\min}_2(n,m),
}
\]

where

\[
J^{\min}_2(n,m)
=
\min_{a_1+\cdots+a_m=n}
\sum_i\binom{a_i}{2}.
\]

Quadratic radial energy can therefore be read discretely as unit count plus twice the unavoidable minimum pair-collision count.

## 4. P019-X05 — Dimension addition is min-plus composition

For all `m,n>=1`,

\[
\boxed{
\psi_{m+n}(c)
=
\min_{a+b=c}\left(\psi_m(a)+\psi_n(b)\right).
}
\]

This is immediate by partitioning the `m+n` slots into two groups, minimizing inside each group for fixed group totals, then minimizing over all splits of the total.

Hence block-size addition is represented on the energy side by min-plus convolution:

\[
\boxed{
\psi_m\;\square\;\psi_n=\psi_{m+n}.
}
\]

Associativity follows from integer addition:

\[
(\psi_a\square\psi_b)\square\psi_c
=
\psi_a\square(\psi_b\square\psi_c)
=
\psi_{a+b+c}.
\]

The contraction result is therefore independent of grouping order.

## 5. Block-size-tagged contracted radial energy

Let

\[
\mathbf m=(m_1,\ldots,m_k),\qquad m_i\ge1,
\]

record how many original slots are hidden inside each currently visible coordinate block.

For

\[
c=(c_1,\ldots,c_k),\qquad \sum_i c_i=0,
\]

define

\[
\boxed{
E_{\mathbf m}(c)
=
\sum_{i=1}^k\psi_{m_i}(c_i).
}
\]

The original `A_p` square energy is the special case

\[
\mathbf m=(1,1,\ldots,1)
\]

with `p+1` blocks, because `psi_1(c)=c^2`.

Define the tagged radial ball

\[
B_{\mathbf m}(T)
=
\{c:\sum_i c_i=0,\ E_{\mathbf m}(c)\le T\}.
\]

The integer tag `m_i` is relation context, not a continuous parameter.

## 6. P019-X06 — Exact closure under fiber-minimum contraction

Merge blocks `i,j` into

\[
c_*=c_i+c_j,
\qquad
m_*=m_i+m_j.
\]

Then the minimum energy over the full high-dimensional fiber with fixed `c_*` is

\[
\min_{a+b=c_*}
\left(\psi_{m_i}(a)+\psi_{m_j}(b)\right)
=
\psi_{m_i+m_j}(c_*).
\]

Thus the fiber-minimum contraction

\[
(\pi_*E)(y):=
\min_{\pi(x)=y}E(x)
\]

maps the family into itself:

\[
\boxed{
E_{(\ldots,m_i,m_j,\ldots)}
\xrightarrow{\text{merge }i,j}
E_{(\ldots,m_i+m_j,\ldots)}.
}
\]

Dimension information is not erased; it becomes block-size context.

## 7. Closed energy change for moving one unit

The forward finite difference is

\[
\boxed{
\psi_m(c+1)-\psi_m(c)
=2\left\lfloor\frac{c}{m}\right\rfloor+1.
}
\]

Therefore moving one unit from block `j` to block `i` gives

\[
\boxed{
\Delta E
=2\left(
\left\lfloor\frac{c_i}{m_i}\right\rfloor
-
\left\lfloor\frac{c_j-1}{m_j}\right\rfloor
\right).
}
\]

For all `m_i=1`, this reduces to

\[
\Delta E=2(c_i-c_j+1),
\]

the original square-energy change along a primitive root.

## 8. P019-X07 — Exact dimensional closure of radial cut boundaries

Fix a directed transfer `j -> i`. For a contracted lower-dimensional state `y`, keep all other blocks and `c_i+c_j` fixed and parameterize the fiber by `a=c_i`.

Its fiber energy

\[
F_y(a)
=
\psi_{m_i}(a)
+
\psi_{m_j}(c_*-a)
+
R_y
\]

is discretely convex because the first differences of `psi_m` are nondecreasing.

Therefore the sublevel set

\[
\{a:F_y(a)\le T\}
\]

is, when nonempty, a finite integer interval. Along the directed transfer `a -> a+1`, each nonempty fiber has exactly one edge leaving the interval through its right endpoint.

The fiber is nonempty exactly when

\[
\min_aF_y(a)\le T.
\]

By X05,

\[
\min_aF_y(a)
=
\psi_{m_i+m_j}(c_*)+R_y,
\]

which is precisely the energy of the merged tagged state.

Hence there is an exact bijection

\[
\boxed{
\text{directed cut edges of }B_{\mathbf m}(T)
\text{ in channel }j\to i
\;\longleftrightarrow\;
B_{\mathbf m'}(T),
}
\]

where `m'` is obtained by replacing `m_i,m_j` with `m_i+m_j`.

Thus

\[
\boxed{
|C_{\mathbf m,j\to i}(T)|
=
|B_{\mathbf m'}(T)|.
}
\]

The earlier failure of an untagged radial identity is therefore reinterpreted: deleting the block-size tag after contraction loses essential relation context. With the tag retained, the radial cavity boundary is exactly dimension-recursive.

## 9. Unified interpretation of graph and radial geometry

Primitive graph cost is a contraction fixed family: its fiber minimum after coordinate merging has the same untagged form. Thus

\[
B_p^G(r)\to B_{p-1}^G(r).
\]

Quadratic radial energy is context-sensitive but closed inside the tagged `psi_m` family:

\[
(1,1,\ldots,1)
\to
(2,1,\ldots,1)
\to
(3,1,\ldots)
\text{ or }(2,2,1,\ldots)
\to\cdots.
\]

Any grouping order leading to the same final block partition gives the same energy by X05.

Therefore:

- graph geometry is contraction-closed and context-free;
- radial geometry is contraction-closed and context-sensitive.

This supports the P019 prototype

`relative state = integer distance + precision tag + relation context`.

## 10. Dimension and information retention

The original `A_p` has `p+1` unit slots. After any sequence of contractions,

\[
\sum_i m_i=p+1.
\]

Hence the current visible relation dimension is `k-1`, while hidden internal capacity remains encoded in the block sizes. The original total slot count is exactly recoverable from `sum m_i`.

After all blocks merge, there is one block of size `p+1`; the zero-sum condition forces its visible coordinate to zero, so the geometry collapses to a single point while the original capacity remains stored in the tag.

## 11. Main interpretation

The LEGO principle now has a precise integer form:

\[
\boxed{
\text{unit slots add}
\Longleftrightarrow
\text{block sizes add}
\Longleftrightarrow
\text{fiber energies min-plus compose}.
}
\]

The invariant `psi_m(1)=1` guarantees that the minimum unit does not change with dimension.

The identity

\[
\psi_m(n)=n+2J_2^{\min}(n,m)
\]

also shows that square cost need not be introduced as a continuum length primitive; it admits a fully discrete interpretation in terms of unit count plus unavoidable collision.

## 12. Status and next steps

The finite integer identities and combinatorial bijections above are the current claims. No physical identification of `psi_m` with energy, gravity, curvature, or natural-space ontology is asserted.

Next priorities:

1. formalize X04-X07 in Lean, especially the balanced minimizer, min-plus associativity, and unique-exit fiber theorem;
2. turn `block_sizes` into typed relation context rather than an unstructured tuple;
3. test whether different contraction trees with the same final partition preserve not only energy but incidence and collision spectra;
4. investigate higher `J_k` analogues beyond the pair-collision `J_2` case;
5. formulate graph and radial contraction under one fiber-minimum operator language;
6. map prior art in infimal projection, discrete convex analysis, min-plus convolution, and lattice contraction before making novelty claims.
