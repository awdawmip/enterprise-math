# P019 Supplement 16 — Partition Relation Quotients and the Unified Directional Excavation Theorem

Status: `RESEARCH WIP / EXACT FINITE INTEGER THEOREMS PROVED`

## 1. Goal

The earlier research path encountered an apparent conflict:

- graph-ball directional excavation contracts exactly to an ordinary lower-dimensional ball;
- radial-ball formulas fail if the merged capacity tag is erased.

Supplements 04–15 show that the failure is not radial geometry itself but deletion of block-capacity / relation context during coarsening.

This supplement compresses the result into one partition-relation theorem.

## 2. Tree-free partition quotient

Start from a current weighted relation state

\[
(m_i,c_i,Z_{ij}),
\qquad
Z_{ij}=m_jc_i-m_ic_j.
\]

Take any partition of the current block indices,

\[
\Pi=\{A_1,\ldots,A_k\}.
\]

Define coarse capacity and total

\[
\boxed{M_\alpha=\sum_{i\in A_\alpha}m_i,}
\qquad
\boxed{C_\alpha=\sum_{i\in A_\alpha}c_i,}
\]

and coarse relation

\[
\boxed{
Z^{\Pi}_{\alpha\beta}
=
\sum_{i\in A_\alpha}
\sum_{j\in A_\beta}Z_{ij}.
}
\]

Direct expansion gives

\[
\boxed{
Z^{\Pi}_{\alpha\beta}
=M_\beta C_\alpha-M_\alpha C_\beta.
}
\]

Thus an arbitrary partition quotient remains inside the same weighted relation family.

## 3. P019-X50 — Partition coarsening composes exactly

If `Sigma` is coarser than `Pi`, one may first construct `Z^Pi` and then quotient again. Since quotient entries are finite double sums,

\[
\boxed{
(Z^{\Pi})^{\Sigma/\Pi}=Z^{\Sigma}.
}
\]

Hence

\[
\boxed{
\text{coarsen, then coarsen again}
=
\text{coarsen directly to the final partition}.
}
\]

A binary contraction tree is only one execution schedule for decomposing the same partition quotient into two-block merges. The final present coarse relation state does not depend on that tree.

## 4. P019-X51 — Dimension is partition block count minus one

With fixed grand total, a partition with `k` coarse blocks has

\[
\boxed{dim_{relation}(\Pi)=k-1.}
\]

One binary merge changes `k -> k-1`, hence

\[
\boxed{dim\to dim-1.}
\]

Starting with `N` singleton units and ending at one block removes exactly `N-1` independent relation degrees. For `A_p`, `N=p+1`, so `p=N-1`.

## 5. P019-X52 — The merge fiber is the kernel direction of the coarse quotient

Consider only two blocks to be merged, with capacities `m,n`, child totals `a,b`, parent total `c=a+b`, and `M=m+n`.

Holding the coarse parent state fixed leaves all fine lifts

\[
(a,b)=(a,c-a),
\qquad a\in\mathbb Z.
\]

Adjacent lifts differ by the primitive internal redistribution

\[
(a,b)\to(a+1,b-1).
\]

The internal weighted relation is

\[
z=na-mb=Ma-mc,
\]

so one primitive fiber move gives

\[
\boxed{z\to z+M.}
\]

All merged external relations

\[
Z_{uk}=Z_{ik}+Z_{jk}
\]

remain unchanged. The merge fiber is therefore a one-dimensional integer relation line invisible to the coarse quotient.

## 6. Tagged collision-power balls

For block capacities

\[
\mathbf m=(m_1,\ldots,m_k)
\]

and totals `c_i`, define

\[
\boxed{
E_{\mathbf m}^{(s)}(c)=\sum_i\Psi_{m_i,s}(c_i)
}
\]

and the fixed-total ball

\[
\boxed{
B_{\mathbf m}^{(s)}(T)
=
\{c:\sum_i c_i=C,\ E_{\mathbf m}^{(s)}(c)\le T\}.
}
\]

For `A_p`, take `C=0`.

## 7. P019-X53 — Unified directional excavation bijection

Fix donor block `j` and receiver block `i`. Define the directional cut boundary

\[
C_{\mathbf m,j\to i}^{(s)}(T)
=
\{c\in B_{\mathbf m}^{(s)}(T):
 c+e_i-e_j\notin B_{\mathbf m}^{(s)}(T)\}.
\]

Merge `i,j` into a parent block of capacity `m_i+m_j`, producing capacity tuple `m'`. Let

\[
\pi_{ij}(c)
=
(c_i+c_j,\text{all other totals}).
\]

Then

\[
\boxed{
\pi_{ij}:
C_{\mathbf m,j\to i}^{(s)}(T)
\overset{\sim}{\longrightarrow}
B_{\mathbf m'}^{(s)}(T)
}
\]

is a bijection.

Proof: fix a coarse state on the right. Let its merged total be `c`, other-block energy be `E_other`, and slack

\[
\omega=T-E_{other}-\Psi_{m_i+m_j,s}(c)\ge0.
\]

If receiver total is `a`, the fine fiber cost is

\[
f(a)=\Psi_{m_i,s}(a)+\Psi_{m_j,s}(c-a).
\]

Supplement 07 proves the feasible integer splits form an interval `[L,U]`. The transfer `j->i` sends `a->a+1`; therefore the unique fine state inside the ball whose next directed step exits is exactly `a=U`. Every coarse state has exactly one such lift, and every directional boundary state projects to one coarse state. ∎

The proof is identical for every integer `s>=1`.

## 8. The graph/radial conflict disappears

For `s=1`,

\[
\Psi_{m,1}(c)=|c|
\]

is independent of capacity. The merged capacity tag is invisible to ball membership. X53 therefore reduces automatically to

\[
\boxed{
\text{p-dimensional directional graph boundary}
\cong
\text{ordinary (p-1)-dimensional graph ball}.
}
\]

This is Supplement 03's X02.

For `s=2`, `Psi_(m,2)` depends on capacity. The same X53 instead gives

\[
\boxed{
\text{radial directional boundary}
\cong
\text{capacity-tagged lower-dimensional radial ball}.
}
\]

The earlier radial formula failed only because the merged capacity tag was erased and the result was compared with an untagged lower ball.

Thus graph and radial contraction are not incompatible systems. They are

\[
\boxed{
\text{one weighted relation contraction}
+
\text{different observation order }s.
}
\]

## 9. P019-X54 — Total directional boundary in the unit symmetric case

Start with `N` unit blocks. There are `N(N-1)` oriented primitive transfer directions `j->i`. Slot-permutation symmetry makes every merged capacity pattern equivalent to

\[
(2,1,\ldots,1).
\]

Hence the total oriented cut-edge count is

\[
\boxed{
E_{N,s}(T)
=N(N-1)
\left|B_{(2,1,\ldots,1)}^{(s)}(T)\right|.
}
\]

At `s=1`, capacity two becomes invisible, giving

\[
\boxed{
E_{N,1}(T)
=N(N-1)|B_{N-1}^{(1)}(T)|.
}
\]

For `A_p`, `N=p+1`, this recovers

\[
\boxed{E_p(r)=p(p+1)V_{p-1}(r)}
\]

under the threshold conversion `E^(1)=2d_G`.

The early graph-ball formula is therefore an `s=1` instance of X53, not an isolated coincidence.

## 10. Internal `Z_ij` fiber and the boundary root

Inside a fixed coarse fiber,

\[
z=Ma-mc.
\]

Because the feasible receiver totals are `[L,U]`, feasible internal relations are

\[
\boxed{
\{ML-mc,\ M(L+1)-mc,\ldots,MU-mc\}.
}
\]

The directional boundary is the maximum internal relation

\[
\boxed{z_{max}=MU-mc,}
\]

while the opposite direction uses `z_min`.

Thus the fiber root of Supplement 09 may be read entirely as:

> Find the largest legal internal relation state on the kernel relation line that fits the current energy slack.

This has the same integer-root/right-adjoint skeleton as P008.

## 11. Interface with P018 partition precision

P018 treats finite precision through partition/coarse-fiber structure. The weighted relation quotient provides a concrete geometric instance:

- a partition block is a coarse finite-resolution unit;
- capacity is the number of original unit slots retained by that block;
- the weighted field is the relation structure still visible between coarse blocks;
- deleted internal `Z` values are relation details erased by the coarse observation;
- refinement re-exposes selected internal relations.

Dimension contraction and precision coarsening therefore begin to share the same partition language.

## 12. Interface with P010/P011/P021

- P010: merge is many-to-one and history fibers can grow;
- P011: under a finite energy constraint, internal-relation fiber multiplicity is exactly the interval length;
- P021: exact witnesses cannot generally be replaced by cardinality before future joins;
- P019: deleted internal `Z` is the relation-level witness coordinate.

The next future-safe question becomes:

> After a sequence of partition coarsenings, which deleted internal `Z` relations remain observable or composition-relevant under the declared future operation family?

## 13. Implementation and validation

`src/enterprise_math/weighted_relation_field.py` now adds arbitrary partition quotients through `coarsen_weighted_relation_field`, and binary merge is implemented as its two-block special case.

`tests/test_weighted_relation_field.py` checks that arbitrary partition aggregation matches direct capacity/total computation and that nested coarsening is exactly equal to direct final coarsening.

Earlier collision-power boundary tests check the counting shadow of X53 for powers `s=1..4`, multiple partitions, and thresholds; the present supplement supplies the set-level interval-endpoint proof.

## 14. Current unified picture

Dimensional excavation now compresses to

\[
\boxed{
\text{unit LEGO states}
\to
\text{pair relation field}
\to
\text{capacity-weighted partition quotient}
\to
\text{delete one internal }Z\text{ per binary merge}.
}
\]

At the same time,

\[
\boxed{
\text{collision order }s
\to
\Psi_{m,s}
\to
\text{the same directional-boundary quotient theorem}.
}
\]

The current working model therefore gives a concrete positive answer to the low-to-high dimensional generation goal: every finite-dimensional relation contraction is generated by the same binary block merge, and every collision-power ball boundary drops one dimension through the same fiber-endpoint lift.

## 15. Next steps

1. formalize X53 in Lean as a finite-fiber order-adjoint/bijection theorem;
2. implement boundary lifting directly on weighted relation fields without explicit fine-coordinate enumeration;
3. connect P018 abstract partition refinement formally to weighted relation quotients;
4. apply future-safe quotients to families of deleted internal `Z` witnesses;
5. search for the canonical minimum relation memory that preserves a declared future geometry/dynamics language exactly.
