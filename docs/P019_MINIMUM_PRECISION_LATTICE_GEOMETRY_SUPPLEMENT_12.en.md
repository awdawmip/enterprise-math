# P019 Supplement 12 — Contraction Atlas and Local Integer Tree Rotations

Status: `RESEARCH WIP / EXACT LOCAL TRANSFORMS PROVED`

## 1. Problem

Supplement 11 showed that

`ordered contraction tree + root total + internal imbalance tags z`

is a lossless encoding of the present fine integer state.

If different contraction trees encode the same fine state, however, the tree may still be a coordinate choice rather than part of the state itself.

This supplement constructs local integer coordinate changes between binary trees.

## 2. Local rotation of three blocks

Take three adjacent blocks `A,B,C` with sizes `m,n,k` and totals `a,b,c`.

In the parenthesization

\[
((A,B),C),
\]

define

\[
\boxed{u=na-mb}
\]

and

\[
\boxed{v=k(a+b)-(m+n)c.}
\]

After rotating to

\[
(A,(B,C)),
\]

define

\[
\boxed{u'=kb-nc}
\]

and

\[
\boxed{v'=(n+k)a-m(b+c).}
\]

## 3. P019-X29 — Reassociation acts only on imbalance tags

The four integers satisfy

\[
\boxed{
(m+n)u'=nv-ku
}
\]

and

\[
\boxed{
(m+n)v'=(m+n+k)u+mv.
}
\]

Proof: substitute the definitions and collect terms. For example,

\[
nv-ku
=nk(a+b)-n(m+n)c-kna+kmb
=(m+n)(kb-nc).
\]

The second identity is analogous. ∎

Thus a local tree rotation can be performed without reconstructing the leaves or enumerating the fine fiber.

Legal relation states automatically make both numerators divisible by `m+n`.

## 4. P019-X30 — The inverse is also a local integer transform

For the reverse rotation from `A,(B,C)` to `((A,B),C)`, one has

\[
\boxed{
(n+k)u=nv'-mu'
}
\]

and

\[
\boxed{
(n+k)v=(m+n+k)u'+kv'.
}
\]

Hence local rotation is invertible on the legal imbalance lattice.

This is not an arbitrary rational linear map on all of `Z^2`; legal tag states carry the necessary divisibility constraints.

## 5. Unit three-slot example

For

\[
m=n=k=1,
\]

\[
u=x-y,
\qquad
v=x+y-2z,
\]

and after rotation

\[
u'=y-z,
\qquad
v'=2x-y-z.
\]

X29 becomes

\[
\boxed{2u'=v-u}
\]

and

\[
\boxed{2v'=v+3u.}
\]

Every legal integer triple automatically satisfies the required parity.

## 6. P019-X31 — Tree rotation preserves pair-dispersion quadratic content

Let

\[
N=m+n+k.
\]

X29 implies the fraction-free invariant

\[
\boxed{
(n+k)
\bigl(kN u^2+mn v^2\bigr)
=
(m+n)
\bigl(mN {u'}^2+nk {v'}^2\bigr).
}
\]

For three unit slots this reduces to

\[
\boxed{
3u^2+v^2
=
3{u'}^2+{v'}^2.
}
\]

Supplement 11 gives

\[
3u^2+v^2=2P(x,y,z).
\]

Thus reassociation changes relation coordinates without changing the pair dispersion they encode.

## 7. P019-X32 — Contraction Atlas

Fix labeled leaves and a root total.

For every rooted ordered binary tree `T`, collect one imbalance at every internal node into a coordinate tuple

\[
z_T.
\]

Supplement 11 proves that

\[
(T,z_T,root\ total)
\]

uniquely determines the fine leaf state.

X29/X30 provide exact local coordinate transitions between trees related by one rotation.

This suggests the tool name

\[
\boxed{\textbf{Contraction Atlas}}.
\]

Here "atlas" means only a family of discrete coordinate charts:

- binary trees are charts;
- legal imbalance lattices are chart domains;
- reassociation formulas are transition maps.

No continuous manifold is introduced.

## 8. Rotation coherence

Every local rotation formula is obtained by algebraically eliminating the same block totals.

Therefore, if a sequence of legal rotations takes a tree `T` to `T'`, the final tags equal the tags computed directly from the same fine leaf state on `T'`.

Hence on legal imbalance states the transition result depends only on the underlying fine state and the destination tree, not on the intermediate rotation path.

In particular, every closed rotation loop returns the original legal tags.

General associahedral/categorical coherence is established mathematics; P019 makes no priority claim for that general mechanism.

## 9. Can the tree be erased?

This must be decided using the future language of Supplement 08.

### Present-state queries

If future queries depend only on the current fine leaf state or tree-invariant relation observables such as `P` or `q`, then different `(T,z_T)` representations connected by legal rotations are candidate coordinate descriptions of one relation state. Tree shape should not automatically be treated as additional ontology.

### Historical queries

If future queries include which blocks actually merged first, which receiver/donor selection occurred, or causal/provenance history, then quotienting by rotations deletes actual history and need not be future-safe.

Thus

\[
\boxed{
\text{representation tree}
\neq
\text{historical contraction trace}.
}
\]

## 10. Interface with P021

P021 shows that exact witness relations and cardinality shadows cannot be conflated.

Contraction Atlas yields the analogous layers:

- `tree+z`: an exact current-state witness coordinate;
- rotation class: a tree-independent current relation state candidate;
- historical oriented flag: actual process witness.

Collapsing from historical flag to rotation class requires a future-safety proof; it is not automatic.

## 11. Implementation and validation

`src/enterprise_math/pair_dispersion.py` adds:

- `reassociate_imbalances`;
- `reassociation_quadratic_identity`.

`tests/test_pair_dispersion.py` checks, for `m,n,k=1..3` and many signed block totals:

- X29 local transport;
- X31 quadratic invariance;
- the closed three-unit example.

## 12. Further meaning

The LEGO model now acquires an additional property:

> The same unit states may be grouped through different hierarchical orders. When the question concerns the final relation state rather than the actual process history, the grouping-tree difference can be transported by local integer coordinate changes instead of introducing continuous rotation coordinates.

Dimension/relation structure therefore need not be tied to one fixed decomposition tree.

## 13. Next steps

1. implement general tree data and rotation paths and directly verify the four-block pentagon;
2. characterize the minimal congruence constraints defining the legal imbalance lattice;
3. determine whether each rotation equivalence class has a smaller tree-independent integer invariant representation;
4. seek an invariant family richer than `P` that reconstructs the full relation state;
5. further unify Contraction Atlas with P012 automorphism charts, P021 witness transport, and P018 precision detail.
