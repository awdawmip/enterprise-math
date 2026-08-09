# P019 Supplement 11 — Pair Dispersion and Exact Imbalance-Tree Reconstruction

Status: `RESEARCH WIP / EXACT INTEGER IDENTITIES PROVED`

## 1. Motivation

Supplement 09 compressed one square-layer split to parent total `c`, block sizes `m,n`, and the cross-multiplied imbalance `z=na-mb`. The tag `z` reconstructs child totals exactly.

This supplement proves that `z^2` is not merely an encoding trick: it is exactly the new pairwise integer-dispersion term introduced when two blocks are merged.

This gives the square radial observable a relation-based interpretation without making continuous angles or lengths primitive.

## 2. Pair dispersion

For an integer tuple

\[
x=(x_1,\ldots,x_N),
\]

define

\[
\boxed{
P(x)=\sum_{1\le i<j\le N}(x_i-x_j)^2.
}
\]

This is built entirely from pairwise differences of integer states.

## 3. P019-X24 — Basic pair-dispersion identity

For every integer tuple,

\[
\boxed{
P(x)
=N\sum_i x_i^2
-\left(\sum_i x_i\right)^2.
}
\]

Proof: expand all pairwise squares. Each `x_i^2` appears `N-1` times, and use

\[
\left(\sum_i x_i\right)^2
=\sum_i x_i^2+2\sum_{i<j}x_ix_j.
\]

No square root, angle, or limit is involved. ∎

## 4. P019-X25 — Fraction-free block merge law

Split the tuple into blocks with sizes `m,n`, totals `a,b`, and `M=m+n`. Let

\[
\boxed{z=na-mb.}
\]

Write their pair dispersions as `P_L,P_R,P_M`. Then

\[
\boxed{
mnP_M
=
nMP_L
+mMP_R
+z^2.
}
\]

This follows by substituting X24 and using

\[
nMa^2+mMb^2-mn(a+b)^2=(na-mb)^2.
\]

The recurrence is entirely fraction-free.

## 5. Structural meaning of `z^2`

Given the internal dispersions of the two child blocks, the additional cross-block structure created by joining them is controlled exactly by `z^2`.

If `na=mb`, then `z=0`: the two block totals are perfectly proportional to their block sizes and no proportional-imbalance term is added.

Thus `z` simultaneously acts as:

1. a split-reconstruction coordinate;
2. a proportional-allocation defect;
3. a pair-dispersion merge witness.

## 6. P019-X26 — The `A_p` quadratic state `q` is a pure pair relation

For an `A_p` state there are `N=p+1` integer slots and

\[
\sum_i x_i=0.
\]

X24 becomes

\[
P(x)=N\sum_i x_i^2.
\]

P019's radial quadratic state is

\[
q(x)=\frac12\sum_i x_i^2.
\]

Hence

\[
\boxed{P(x)=2Nq(x).}
\]

Conversely, on the `A_p` integer domain `P(x)` is exactly divisible by `2N`:

\[
\boxed{q(x)=P(x)//(2N).}
\]

The division is exact integer division, not a hidden-real operation.

Thus `q` may equivalently be read as a strict integer scale projection of the total squared pair difference over all slot pairs. This does not prove that physical space uses this `q`; it removes the need to make a continuous Euclidean norm primitive.

## 7. P019-X27 — Ordered contraction tree plus imbalance tags reconstructs the leaves

Consider a rooted ordered binary contraction tree. Each leaf is one original unit slot. At an internal node, child sizes are `m,n`, parent total is `c`, and a signed imbalance `z` is stored.

From Supplement 09,

\[
z=(m+n)a-mc.
\]

Whenever the legality condition

\[
m+n\mid(mc+z)
\]

holds, child totals are unique:

\[
\boxed{
a=(mc+z)//(m+n),
\qquad b=c-a.}
\]

Starting at the root total and recursing therefore reconstructs every leaf integer uniquely.

Hence

\[
\boxed{
\text{ordered contraction tree}
+
\text{one signed }z\text{ at every internal node}
+
\text{root total}
}
\]

is a lossless hierarchical encoding of the present fine integer state. Large intermediate child totals need not be stored explicitly.

## 8. Difference from the full oriented contraction history

The full oriented contraction flag from Supplement 07 additionally remembers the temporal ordering of independent merges and the receiver/donor selection history.

An ordered tree with `z` tags retains the final hierarchy and the current fine state, but may forget the actual temporal order of disjoint merges.

Therefore:

- if future queries depend only on the **present fine integer state**, tree+z is one sufficient encoding;
- if future queries ask for the **actual contraction process history**, this compression need not be future-safe.

This is precisely the task-dependence formalized by Supplement 08.

## 9. P019-X28 — Pair dispersion is reconstructible from the imbalance tree

Every leaf block contains one number, so

\[
P_{leaf}=0.
\]

At every internal node use X25:

\[
mnP_M=nMP_L+mMP_R+z^2.
\]

Thus the tree, block sizes, and all `z` tags determine every node's pair dispersion from the leaves upward.

For a zero-sum `A_p` root,

\[
P_{root}=2Nq.
\]

The radial quadratic state `q` can therefore be recovered from local imbalance witnesses on a purely integer relation-contraction tree.

## 10. Relation to spherical excavation

The excavation program originally separated graph/relation boundary from radial/collision-power boundary.

The square layer now supplies a bridge:

- dimensional contraction is represented by the block tree;
- directional split is represented by `z`;
- `z^2` is the local pair-dispersion merge term;
- global `q` is an exact integer projection of total pair dispersion.

At least in the current `A_p` working model, radial information need not be an independent real-valued layer outside relation geometry; it can be reconstructed from pair relations and contraction imbalances.

## 11. Implementation and validation

Added:

- `src/enterprise_math/pair_dispersion.py`
  - `pair_dispersion`
  - `pair_dispersion_identity`
  - `merge_pair_dispersion_identity`
  - `zero_sum_quadratic_separation`
- `tests/test_pair_dispersion.py`

Finite enumeration directly checks X24, X25, and `P=2Nq` on zero-sum `A_p` states.

## 12. Research discipline

Pairwise-square dispersion, variance decomposition, and hierarchical contrast decompositions may have established mathematical neighbors.

X24–X28 are retained here as direct integer derivations and tool connections inside P019; no originality or priority claim is made. Prior-art mapping is required before promotion.

The quantities `P` and `z^2` are not automatically interpreted as physical energy, curvature, or gravity.

## 13. Next steps

1. characterize the exact legality/coherence conditions on a whole tree of `z` tags;
2. derive local integer transformations between `z` systems on different trees representing the same fine state;
3. if those transformations close, seek tree-independent canonical relation coordinates;
4. connect pair-dispersion merge laws to Supplement 08 future-safe quotients and determine when tree shape itself can be erased;
5. compare local `z` transformations with P021 witness joins and intrinsic direction transport.
