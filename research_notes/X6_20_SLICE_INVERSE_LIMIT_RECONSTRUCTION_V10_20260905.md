# X6：从三轴 slice 重叠数据重建全局六轴类的 inverse-limit 定理

Status: `DERIVED / EXACT LOCAL-TO-GLOBAL RECONSTRUCTION / NO CELL-HISTORY COLLAPSE`
Date: `2026-09-05`
Depends on: established three-axis min-zero address/displacement structure and P000 six-axis selection semantics.

## 1. Pair-overlap object

For two distinct native axis labels i,j, define the derived pair difference

`d_ij = z_i-z_j in Z`.

This is invariant under a common diagonal shift of a local or global coordinate lift. It is a component/readout quantity, not Euclidean displacement.

For any three-axis slice `S={i,j,k}`, an existing min-zero triple `(a_i,a_j,a_k)` determines the three signed differences

`d_ij=a_i-a_j`, `d_jk=a_j-a_k`, `d_ki=a_k-a_i`,

with cocycle identity

`d_ij+d_jk+d_ki=0`.

Hence each three-axis slice has canonical restriction maps to its three two-axis difference overlaps.

## 2. Compatible 20-slice family

Take one three-axis coordinate/displacement class `x_S` for every 3-subset `S subset {1,...,6}`.

Call the family compatible iff whenever two slices contain the same axis pair `{i,j}`, they induce the same integer `d_ij`.

Because every pair of the six axes belongs to four different 3-subsets, this is a strong redundant consistency condition.

## 3. Reconstruction theorem

**Theorem.** Compatible families of all 20 local three-axis displacement classes are in canonical bijection with

`G6_D = Z^6 / Z(1,1,1,1,1,1)`.

### Existence

Fix axis 1 as a temporary gauge and set

`z_1=0`,

`z_i=d_i1` for i=2,...,6.

For any local slice `{i,j,k}`, compatibility gives

`z_i-z_j=d_ij`, etc. Therefore the restriction `[z|_S]` equals the declared local class `x_S`.

### Uniqueness

If z and z' induce the same compatible local family, then every pair difference agrees:

`z_i-z_j=z'_i-z'_j`.

Thus `z_i-z'_i` is independent of i, so z-z' is a global diagonal vector. Hence `[z]=[z'] in G6_D`.

The choice of reference axis only changes z by a diagonal shift, so the reconstructed global class is canonical.

## 4. Universal property

Let Y be any set/object carrying maps to all local three-axis displacement spaces such that the pair-overlap diagrams commute.

Then there is a unique map

`Y -> G6_D`

whose local restrictions are the given slice maps.

Thus `G6_D` is the inverse-limit / universal compatible coordinate completion of the complete native 3-axis observation atlas, at the derived coordinate observer.

This statement does not assert that every Path-formal history or internal packet state is determined by coordinates; it only says there is no further freedom in a globally compatible **six-axis coordinate state** once all local coordinate observations are fixed.

## 5. Canonical positive representative

Applying

`can6(z)=z-min(z)*1`

to the reconstructed class produces one unique element of

`A6_D={n in N_0^6:min n=0}`.

Therefore the min-zero six-tuple is not an arbitrary numerical ansatz: it is the canonical positive-only section of the universal local-to-global coordinate completion.

Promoting the separately typed underlying set to primitive Cell addresses remains the native-coordinate-completeness decision; the coordinate reconstruction itself is already closed.

## 6. Fewer slices can suffice

All 20 slices give maximal redundancy but are not minimal.

A collection of 3-axis slices reconstructs the global class whenever its induced pair-difference data connect all six axis labels sufficiently to determine `z_i-z_j` from a common potential.

For example the four slices

`{1,2,3}`, `{1,2,4}`, `{1,2,5}`, `{1,2,6}`

already determine all six coordinates modulo a common diagonal through their shared `{1,2}` pair and differences to the remaining axes.

The current FCC four-star atlas is a different cover: its slice intersections are only single axis labels, so pair-difference inverse-limit reconstruction is not directly available from quotient classes alone. Its already-merged V2 canonical-min-zero gluing theorem supplies the needed chart-gauge transition data instead.

The two reconstructions agree whenever both are defined.

## 7. Relation to Cell/path observer

A Cell/path model may have richer information than this coordinate inverse limit:

`PATH_FORMAL -> CELL_STATE -> SIX_AXIS_COORDINATE_STATE -> SLICE_COORDINATE_OBSERVATION`.

The theorem only closes the last local-to-global coordinate arrow.

Therefore it avoids the previous type error: no shared line identity is promoted to a shared Cell-transition generator, and no local same-terminal path is declared a full-state return merely because its selected-slice coordinate observation closes.

## 8. Foundation consequence

The remaining native question is no longer “what six-axis coordinate object should we use?” At coordinate-observer strength it is forced to be `G6_D` with min-zero section `A6_D`.

The only remaining promotion question is whether

`FULL_NATIVE_SPATIAL_CELL_IDENTITY -> SIX_AXIS_COORDINATE_STATE`

is injective / state-complete, or whether Cell identity carries additional non-coordinate state invisible to every six-axis coordinate observation.

P000's language strongly favors coordinate completeness for the spatial Cell state, while Path/BRC history remains separately typed; nevertheless this injection must be frozen explicitly rather than inferred from a path quotient.
