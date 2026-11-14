# X6：从三轴 slice 重叠数据重建全局六轴类的 inverse-limit 定理

Status: `DERIVED / EXACT LOCAL-TO-GLOBAL RELATIVE-OBSERVER RECONSTRUCTION / P000-V5 NATIVE-TYPE CLARIFIED 2026-11-14`
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

This statement determines exactly one **relative six-axis observer class**. It does **not** determine a signed native `Z^6` Cell displacement, the omitted integer common depth, Path-formal history, or decorated packet state. The compatibility theorem is an inverse-limit theorem for derived observations, not a native spatial identity theorem.

## 5. Canonical positive representative

Applying

`can6(z)=z-min(z)*1`

to the reconstructed class produces one unique element of

`A6_D={n in N_0^6:min n=0}`.

Therefore the min-zero six-tuple is not an arbitrary numerical ansatz: it is the canonical positive-only section of the universal local-to-global coordinate completion.

**Current P000 V5 correction (2026-11-14):** the former open promotion question is now resolved in the negative **for `A6_D` alone**. The present native spatial Cell torsor has a complete signed raw chart over `Z^6`, while `A6_D` is only its diagonal-relative observer section. Recovering the signed raw chart from this section additionally requires `h=min_i z_i in Z`, giving `z=can6(z)+h(1,...,1)`. This raw-chart reconstruction is not the separately versioned final public Cell-address codec.

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

`PATH_FORMAL -> X6_NATIVE_SPATIAL_SIGNED_RAW_CHART(Z^6) -> G6_D=Z^6/Z(1,...,1) -> COMPATIBLE_20_SLICE_RELATIVE_OBSERVATIONS`.

The arrows represent typed forgetting/observation only, not bijections; the full native spatial Cell chart itself is anchored at a chosen **Cell**, not at historical geometric origin `O_E`. The separately registered final display/address codec is not identified with raw signed coordinates, `A6_D`, or `(can6,h)` by this theorem.

The theorem only closes the last local-to-global coordinate arrow.

Therefore it avoids the previous type error: no shared line identity is promoted to a shared Cell-transition generator, and no local same-terminal path is declared a full-state return merely because its selected-slice coordinate observation closes.

## 8. Foundation consequence under current P000 V5 (corrected 2026-11-14)

The **original reconstruction theorem in §§1–6 is preserved**: compatible triples determine one element of `G6_D` with a canonical representative in `A6_D`. Its older question of promoting that quotient to *native Cell identity* is not still open in the current Foundation. P000 V5 and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` expressly fix `X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)` and a complete six-signed-axis **raw spatial chart** relative to a chosen Cell anchor.

Define `D=(1,1,1,1,1,1)`, and let `F(z)` be the compatible family of all twenty three-axis min-zero coordinate observations. The exact kernel theorem is

`F(z)=F(w) iff w-z=kD for a unique k in Z`.

**Proof.** Every `can3(z|_S)` forgets a common shift. Conversely equal local classes imply equal pair differences for every pair (each appears in a triple); hence all six coordinates of `w-z` coincide. Thus `F` has precisely the diagonal fibres `z+ZD`. In particular `F(0)=F(D)`, while these are distinct native Cell displacements: `G(0)=0`, `G(D)=6`, and `D` has `6!=720` distinct shortest positive native axis-order words, none a native zero-return. These are exact integer consequences, not a rerun of any original benchmark.

For a chosen Cell anchor, the lossless **raw-coordinate** lift is `z=r+hD` with `r=can6(z)` and `h=min_i z_i`; dropping `h` is an actual information-losing observer projection. This correction does not promote all twenty coordinate selections to realized FCC carrier geometry, recover Path-formal ordering/weights from an endpoint, or reinterpret the current separately versioned public six-nonnegative-field final Cell-address contract as a min-zero raw chart. Native spatial identity is settled by P000 V5; decorated state/history and observer-safe quotient operations require their own explicit typed contracts.

**Source/disposition:** LP-003/005/022/026 current theorem-facing consumer repair; historical 2026-09-05 V10 algebra survives at `PRESERVE_OBSERVER` strength, but the previous `A6_D -> primitive Cell?` pending-promotion narrative is `SUPERSEDED`. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`. AUTHOR-VERIFIED / UNREVIEWED / NOT_ADMITTED; independent Driver revision, exhaustive 28-LP coverage and original R063 same-object benchmark remain separate obligations.
