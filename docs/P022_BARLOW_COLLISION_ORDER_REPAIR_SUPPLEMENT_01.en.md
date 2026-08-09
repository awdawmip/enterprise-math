# P022 — Minimum Order Ambiguity and a Third Checkpoint-Scheduling Objective

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE OPTIMIZATION`  
Owner: `program/p022-geometry-v2`  
Depends on: exact collision order-repair cardinality; balanced image/J2 scheduling

## 1. Question

At fixed total horizon `N` and fixed checkpoint count `m`, the complete collision polynomial recovers the segment-length multiset but loses segment order.

For a multiset with multiplicities `t_ell`, the remaining order-repair cardinality is

\[
M_{\rm ord}=\frac{m!}{\prod_\ell t_\ell!}.
\]

Which segment multiset minimizes this residual order ambiguity?

---

## 2. P022-OR04 — exact minimum order-repair cardinality

If all `m` segment lengths are equal, then `M_ord=1`.  This is possible exactly when

\[
m\mid N.
\]

Suppose instead that `m` does not divide `N`.  Then every admissible segment multiset has at least two distinct length classes.

Among all nontrivial partitions

\[
t_1+\cdots+t_s=m,
\qquad s\ge2,
\]

of the number of positions into equal-value multiplicities, the product

\[
\prod_i t_i!
\]

is maximized by the most concentrated multiplicity pattern

\[
(m-1,1).
\]

Therefore

\[
M_{\rm ord}
=\frac{m!}{\prod_i t_i!}
\ge
\frac{m!}{(m-1)!}
=m.
\]

The bound is always attainable when `N>m`, for example by

\[
(1,1,\ldots,1,N-m+1),
\]

whose multiplicities are `(m-1,1)`.

Hence

\[
\boxed{
M_{\rm ord}^{\min}(N,m)
=
\begin{cases}
1,&m\mid N,\\
m,&m\nmid N.
\end{cases}
}
\]

for `1<=m<=N`.

This is an exact finite optimum.

---

## 3. P022-OR05 — ordinary balanced spacing need not minimize order repair

Write the ordinary near-uniform schedule as

\[
N=qm+r,
\qquad0\le r<m.
\]

Its order ambiguity is

\[
M_{\rm ord}^{\rm bal}=\binom mr.
\]

If `r=0`, exact equal spacing is uniquely optimal and

\[
M_{\rm ord}^{\rm bal}=1.
\]

If `r>0`, the global minimum is `m`.  Since

\[
\binom mr=m
\]

only for

\[
r=1\quad\text{or}\quad r=m-1,
\]

we obtain

\[
\boxed{
2\le r\le m-2
\Longrightarrow
M_{\rm ord}^{\rm bal}>M_{\rm ord}^{\min}=m.
}
\]

So balanced spacing is not a universal minimizer once the future cost asks for **order repair after collision aggregation**.

---

## 4. Minimal concrete conflict

Take

\[
N=10,\qquad m=4.
\]

The ordinary balanced segment multiset is

\[
(2,2,3,3),
\]

so

\[
M_{\rm ord}^{\rm bal}
=\binom42
=6.
\]

A more concentrated multiplicity pattern such as

\[
(1,3,3,3)
\]

has

\[
M_{\rm ord}=4.
\]

The canonical witness used by the executable minimizer,

\[
(1,1,1,7),
\]

also has order fiber `4`.

But the earlier checkpoint theorem gives the opposite ranking for two other objectives:

- balanced spacing maximizes observation image size;
- balanced spacing minimizes pair collision `J_2`.

For the two displayed schedules,

\[
|\operatorname{im}O|_{(2,2,3,3)}=144,
\qquad
|\operatorname{im}O|_{(1,3,3,3)}=128,
\]

and

\[
J_2(2,2,3,3)=6688,
\qquad
J_2(1,3,3,3)=7488.
\]

Thus balanced is better for image capacity and pair ambiguity, while the concentrated multiplicity schedule is better for post-aggregation order repair.

---

## 5. Three exact scheduling objectives now disagree

At fixed `N,m`, P022 now has three exact finite objectives:

### A. Observation image capacity

Maximized by ordinary near-uniform segment lengths.

### B. Pair-collision ambiguity `J_2`

Minimized by the same ordinary near-uniform segment lengths.

### C. Complete-collision order repair

Minimized by maximizing repeated segment values:

\[
M_{\rm ord}^{\min}
=
1\text{ or }m.
\]

These objectives coincide in the exact equal-spacing case `m|N`, but can conflict otherwise.

Therefore

\[
\boxed{
\text{checkpoint scheduling is intrinsically multiobjective.}
}
\]

There is no single geometry called “highest precision” unless the future cost functional has first been declared.

This extends the earlier `J_2` versus `J_4` and worst-fiber scheduling conflicts: even after keeping the **complete** collision polynomial, order-repair cost introduces another independent optimization axis.

---

## 6. Precision consequence

The key distinction is not merely “balanced versus unbalanced”.  It is which hidden state the future language penalizes:

- image/J2 penalize coarse merging of microscopic values;
- worst-fiber cost penalizes the largest single ambiguity block;
- order repair penalizes temporal arrangement lost by commutative aggregation.

These are different quotient defects.

A precision controller that optimizes one without declaring the future language can therefore move in the wrong direction for another, even inside one finite deterministic model.

---

## 7. Executable verification

`p022_barlow_collision_order_repair.py` now includes:

- exact `M_ord`;
- the fixed-`N,m` minimum;
- an explicit minimizing witness;
- a predicate comparing ordinary balanced spacing with the order optimum.

The regression exhausts all positive compositions for small `N,m` and verifies the closed `1/m` minimum formula exactly.
