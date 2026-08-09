# P019 Supplement 15 — Capacity-Weighted Relation Field and One Deleted Internal Relation per Dimension Contraction

Status: `RESEARCH WIP / EXACT INTEGER RELATION LAWS PROVED`

## 1. Motivation

Supplement 14 defined the tree-independent unit-slot pair field

\[
d_{ij}=x_i-x_j.
\]

After dimensional contraction, however, a coarse block may contain several original unit slots. Using the naive difference `c_i-c_j` would then mix blocks of different capacities.

The correct integer generalization cross-multiplies the difference in per-slot load instead of introducing fractions.

## 2. Capacity-weighted relation field

For each current block let

\[
m_i\in\mathbb N_{>0}
\]

be its capacity / number of original unit slots and let

\[
c_i\in\mathbb Z
\]

be its integer total. Define

\[
\boxed{Z_{ij}=m_jc_i-m_ic_j.}
\]

When all blocks are units, `m_i=m_j=1`, so

\[
\boxed{Z_{ij}=c_i-c_j=d_{ij}.}
\]

The ordinary pair-difference field is therefore the unit-capacity special case.

## 3. P019-X43 — Weighted antisymmetry and three-block closure

Immediately,

\[
\boxed{Z_{ii}=0,}
\qquad
\boxed{Z_{ij}=-Z_{ji}.}
\]

For every three blocks `i,j,k`,

\[
\boxed{m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.}
\]

This is the capacity-weighted version of the unit three-cycle law.

## 4. P019-X44 — Weighted field + capacities + grand total recovers all block totals

Let

\[
M=\sum_i m_i,
\qquad
C=\sum_i c_i.
\]

Then

\[
\sum_jZ_{ij}
=
Mc_i-m_iC.
\]

Therefore

\[
\boxed{Mc_i=m_iC+\sum_jZ_{ij}}
\]

and, whenever exact divisibility holds,

\[
\boxed{c_i=(m_iC+\sum_jZ_{ij})//M.}
\]

Thus

\[
\boxed{(m_i),\ C,\ (Z_{ij})}
\]

is a tree-independent relation representation of the current coarse block state.

Capacity tags are no longer auxiliary metadata; they are part of the integer relation law itself.

## 5. P019-X45 — Block merge is capacity addition plus relation addition

Merge blocks `i,j` into a new block `u`:

\[
\boxed{m_u=m_i+m_j,}
\qquad
\boxed{c_u=c_i+c_j.}
\]

For any untouched block `k`,

\[
Z_{uk}=m_k(c_i+c_j)-(m_i+m_j)c_k,
\]

so

\[
\boxed{Z_{uk}=Z_{ik}+Z_{jk}.}
\]

Relations among untouched blocks are unchanged.

Thus the forward rule for dimensional contraction in the canonical weighted relation field is simply:

> **add capacities and add external relation rows.**

No high-dimensional geometry has to be solved again.

## 6. P019-X46 — The deleted internal relation is exactly the contraction imbalance

Before merging `i,j`, their internal relation is

\[
\boxed{Z_{ij}=m_jc_i-m_ic_j.}
\]

This is exactly the imbalance tag `z` used throughout Supplements 09–13.

But X45 shows that every external coarse relation after the merge depends only on the sums `c_i+c_j` and `m_i+m_j`, not on `Z_ij`.

A merge therefore genuinely deletes this one internal relation degree from the coarse relation field.

## 7. P019-X47 — One deleted `z` exactly reverses the two child totals

Let parent capacity/total be

\[
M=m+n,
\qquad c=a+b,
\]

with internal relation

\[
z=na-mb=Ma-mc.
\]

Then

\[
\boxed{a=(mc+z)//M,}
\qquad
\boxed{b=c-a,}
\]

provided

\[
\boxed{M\mid(mc+z).}
\]

Hence the coarse parent state, split capacities `(m,n)`, and the deleted internal relation `z` uniquely recover the child totals. Child-to-external weighted relations can then be reconstructed from the recovered totals and capacities.

For one current-state merge, the lost internal relation is a complete reverse fiber coordinate.

## 8. P019-X48 — Each dimension contraction removes exactly one relation degree

With `k` current blocks and fixed grand total `C`, block totals have `k-1` independent integer degrees. The weighted relation field is equivalent to them, so

\[
\boxed{dim_{relation}=k-1.}
\]

After merging two blocks the block count is `k-1`, hence

\[
\boxed{dim'_{relation}=k-2.}
\]

Therefore

\[
\boxed{dim_{relation}-dim'_{relation}=1.}
\]

X46/X47 identify the complete deleted scalar fiber coordinate as

\[
\boxed{Z_{ij}.}
\]

Thus in this relation model:

> **one discrete dimensional contraction deletes one independent internal relation.**

This is stronger than merely saying that a coordinate count fell by one: the deleted object parameterizes the merge fiber and reverses the merge when retained.

## 9. P019-X49 — The merge fiber is an arithmetic lattice of internal relations

Fix coarse parent capacity/total `(M,c)` and child capacities `m,n`. Every fine split is parameterized by `a in Z`, with `b=c-a`, and

\[
z=Ma-mc.
\]

Hence all legal `z` lie in one congruence class:

\[
\boxed{z\equiv-mc\pmod M.}
\]

Advancing `a->a+1` gives

\[
\boxed{z\to z+M.}
\]

The unconstrained merge fiber is therefore a one-dimensional arithmetic lattice.

Under a P019 collision-power/slack constraint, Supplement 07's feasible split interval

\[
a\in[L,U]
\]

becomes

\[
\boxed{z\in\{ML-mc,\ M(L+1)-mc,\ldots,MU-mc\}.}
\]

Its multiplicity is

\[
\boxed{U-L+1=\frac{z_{max}-z_{min}}{M}+1.}
\]

Thus P011 fiber multiplicity, P019 interval witnesses, and the weighted relation field are three views of the same structure.

## 10. Forward merge as relation collapse; retained `z` as reversible completion

If the forward merge keeps only merged capacity, merged total, and merged external weighted field, fine states with different internal `z` values enter the same coarse state. This is a genuine many-to-one relation collapse.

If the internal `z` is also retained, the two child totals can be reconstructed.

Hence

\[
\boxed{\text{merge without }z=\text{relation collapse},}
\]

while

\[
\boxed{\text{merge with }z=\text{a reversible-completion candidate}.}
\]

This interfaces directly with P010/P011 history/fiber language. Whether physical ontology actually retains `z` is a separate hypothesis; mathematically we distinguish the forward coarse map from its explicit witness completion.

## 11. Reinterpreting Contraction Atlas

Contraction Atlas no longer has to be understood as creating `z`.

The cleaner order is:

1. the tree-independent weighted relation field `Z` already exists;
2. a binary contraction tree selects a nested family of block cuts;
3. each internal node reads the corresponding cut relation `Z(A,B)` as a local coordinate;
4. tree rotation chooses a different nested cut family;
5. local reassociation changes between these cut-sum coordinate systems.

Thus

\[
\boxed{
\text{Contraction Atlas}
=
\text{hierarchical cut charts of the weighted relation field}.
}
\]

## 12. LEGO interpretation

A block capacity `m_i` is the number of original unit slots already merged into that coarse LEGO block.

Merging performs only

\[
\boxed{m_i+m_j}
\]

and

\[
\boxed{c_i+c_j},
\]

while all external relations add linearly.

The unit `1` therefore need not change numerical identity when dimension changes; dimensional change occurs in relation degrees and block-capacity structure.

## 13. Interface with spherical excavation

For original unit blocks, `m_i=1`, so the weighted field is the ordinary pair-difference field.

Under a primitive directional merge `i,j -> u`, the previous graph-ball coordinate contraction can now be read as:

- delete the internal relation `Z_ij`;
- set capacity `1+1=2`;
- add the two external relation rows.

This opens a path to rewrite the three-dimensional cavity-to-two-dimensional-ball theorem entirely in weighted-relation contraction language rather than external Euclidean projection language.

## 14. Implementation and validation

Added:

- `src/enterprise_math/weighted_relation_field.py`
  - `weighted_relation_field`
  - `weighted_relation_field_is_closed`
  - `recover_totals_from_weighted_field`
  - `merge_weighted_relation_field`
  - `split_two_block_totals_from_internal_relation`
  - `weighted_relation_dimension`
- `tests/test_weighted_relation_field.py`

Integer enumeration checks:

- unit capacities reduce to ordinary difference fields;
- weighted three-block closure;
- exact recovery from field+capacities+grand total;
- external relation additivity under forward merge;
- the deleted internal relation equals `z`;
- reverse split from `z`;
- relation dimension drops by one on every merge.

## 15. Next steps

1. rewrite graph-ball directional contraction X02/X03 directly as a weighted-field merge theorem;
2. express tagged radial/collision-power fiber intervals as arithmetic progressions of the internal `Z_ij`;
3. search for a tree-independent future-safe quotient on weighted relation fields that can replace large historical contraction flags;
4. reinterpret P021 witness joins as the question of which deleted internal relations must be retained for future composition;
5. study multi-step deleted-`Z` provenance without importing unnecessary continuous topological language.
