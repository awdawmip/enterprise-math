# P019 Supplement 23 — Common Minimum Relation Geometry Across Higher Collision Powers

Status: `RESEARCH WIP / EXACT INTEGER MINIMIZER THEOREM PROVED`

## 1. Problem

Supplement 10 shows that for `s>2` a single block's scaled power defect generally grows with its bulk quotient, unlike the bounded square residue at `s=2`. That does **not** imply that the relation coordinates of a globally optimal fiber arrangement grow with bulk.

This supplement proves the opposite: every power `s>=2` chooses the same minimum relation geometry, determined only by capacities and the total residue allocation.

## 2. Unit-slot balancing theorem

Let total capacity be

\[
M=\sum_i m_i
\]

and write the grand total by Euclidean division

\[
\boxed{C=Mq+r,\qquad0\le r<M.}
\]

For

\[
\sum_{u=1}^M|x_u|^s,
\qquad\sum_u x_u=C,
\]

with `s>=2`, every global minimizer uses only the two values

\[
\boxed{q\text{ and }q+1,}
\]

with exactly `r` unit slots equal to `q+1`.

A purely integer exchange proof suffices: if two slots differ by at least two, moving one unit from the larger to the smaller strictly decreases the cost because the integer forward difference `|t+1|^s-|t|^s` is strictly increasing for `s>=2`.

## 3. Residue allocation across coarse blocks

Let `h_i` be the number of `q+1` unit slots inside coarse block `i`. Then

\[
\boxed{0\le h_i\le m_i,}
\qquad
\boxed{\sum_i h_i=r,}
\]

and the coarse block total is

\[
\boxed{c_i=m_iq+h_i.}
\]

Conversely, every such bounded residue allocation constructs a global minimizer. The coarse minimizer set is therefore independent of `s>=2`.

## 4. P019-X81 — Bulk quotient cancels from the minimum weighted relation field

Substitute the minimizing totals into

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

The bulk terms cancel exactly:

\[
\boxed{Z_{ij}=m_jh_i-m_ih_j.}
\]

Minimum relation geometry is therefore independent of the bulk quotient `q`.

## 5. P019-X82 — Capacity-only bound

Since `0<=h_i<=m_i`,

\[
\boxed{|Z_{ij}|\le m_im_j.}
\]

The bound is independent of total bulk magnitude and of the power `s>=2`.

## 6. P019-X83 — Every `s>=2` shares the same argmin relation set

If

\[
\mathcal M_s(C,\mathbf m)
=\arg\min_{\sum c_i=C}\sum_i\Psi_{m_i,s}(c_i),
\]

then for every `s>=2`,

\[
\boxed{
\mathcal M_s(C,\mathbf m)
=
\{(m_iq+h_i)_i:0\le h_i\le m_i,\ \sum_i h_i=r\}.
}
\]

Thus power order changes the minimum value, not the minimum relation geometry.

## 7. Why `s=1` differs

At `s=1`, many unbalanced same-sign allocations also achieve the minimum `|C|`. The graph layer is therefore insensitive to internal crowding in a way that collision-sensitive layers `s>=2` are not.

## 8. No contradiction with the higher-power defect result

A single fixed block's scaled power defect may grow with `q` for `s>2`, while the **globally optimized relation arrangement** remains residue-only and bounded. These are different questions: bulk-sensitive value defect and bulk-invariant argmin relation geometry can coexist.

## 9. Integer exchange implementation

`src/enterprise_math/discrete_fiber_convexity.py` implements the exact slope

\[
\Psi(c+1)-\Psi(c)=|q+1|^s-|q|^s,
\]

one-unit exchange costs, and strictly decreasing exchange minimization. Tests verify powers `1..5`, signed totals, slope monotonicity, exact exchange increments, and convergence to the closed min-plus minimum.

## 10. Next steps

1. extend X83 from power penalties to general strict discrete-convex collision penalties;
2. study orbit structure of the bounded residue-allocation relation fields;
3. compress minimizer witnesses using bounded `Z` rather than fine unit states;
4. test whether changing observation order in physical pressure tests changes only value or also preferred relation geometry;
5. map these results carefully to established discrete-convex/M-convex resource-allocation theory.
