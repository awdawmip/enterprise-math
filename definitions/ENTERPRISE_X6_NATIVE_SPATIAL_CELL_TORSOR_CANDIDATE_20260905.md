# Enterprise X6 native spatial Cell torsor — Foundation candidate

Status: `FOUNDATION CANDIDATE / P000-DERIVED / EXACT COORDINATE LAYER / NOT YET CURRENT-ROUTER PROMOTED`
Date: `2026-09-05`
Source mandate: direct user request to complete six-axis theory/tools as common research foundation and construct `X6_native` from Cell/path principles.

## 1. Scope: spatial Cell identity, not every state decoration

P000 freezes the full Enterprise spatial state as six native spatial dimensions and keeps time separately typed. Packet/Path permits additional occupancy, channel, relation, BRC and history state.

Therefore define here only the **native spatial Cell-center state space**:

`X6_NATIVE_SPATIAL`.

A later physical/full packet state may be a typed decoration/fibre over this spatial base. Such a fibre is not an additional spatial dimension and does not alter the Cell center address unless separately promoted by Foundation.

## 2. Derived displacement group

Freeze the six-axis derived displacement carrier

`G6_D = Z^6 / Z(1,1,1,1,1,1)`.

This is the universal compatible completion of the declared six-axis / three-axis coordinate-observation system. Its ordinary classical rank is not the Enterprise spatial dimension.

Freeze guard:

`CLASSICAL_RANK(G6_D) != NATIVE_SPATIAL_DIMENSION`.

`NATIVE_SPATIAL_DIMENSION = NATIVE_AXIS_COUNT = 6` from P000.

## 3. Canonical positive section

For `z in Z^6`, define

`can6(z)=z-min_i(z_i)*(1,...,1)`.

Let

`A6_D={d in N_0^6:min(d)=0}`

be the derived displacement section.

Define the separately typed primitive spatial Cell-center address carrier

`A6_E={a in N_0^6:min(a)=0}`

with semantic tag `NATIVE_X6_CELL_CENTER_RELATIVE_ADDRESS`.

Although

`underlying_set(A6_E)=underlying_set(A6_D)`,

freeze

`A6_E != A6_D AS SEMANTIC TYPES`.

No two primitive addresses are identified by a diagonal quotient: tuples with all components positive are simply not canonical primitive `A6_E` addresses.

This extends the accepted three-axis `A_E/A_D` separation rather than reviving the prohibited primitive point diagonal quotient.

## 4. X6 is affine: no Cell is the geometric origin by definition

Define `X6_NATIVE_SPATIAL` as an affine torsor for `G6_D`.

There is no distinguished Cell that must equal the geometric origin. A chosen Cell anchor `c_*` provides a coordinate chart

`coord_{c_*}:X6_NATIVE_SPATIAL -> A6_E`.

Changing the Cell anchor changes coordinates by a `G6_D` translation but not Cell identity.

Thus the established fact “geometric origin is a triple-intersection and is not a Cell” remains intact.

Freeze:

`CELL_COORDINATE_ZERO = CHOSEN_AFFINE_CELL_ANCHOR, NOT O_E`.

## 5. Six native coordinate translations and adjacency

Let `E_i` be the six P000 positive native spatial axes. Their coordinate translations act by

`T_i([z])=[z+e_i]`.

In the canonical section:

`T_i(a)=can6(a+e_i)`.

Path reversal is

`T_i^{-1}(a)=can6(a-e_i)`.

The inverse is an adjacency event in reverse order, not a primitive native negative axis.

Define the **pure coordinate adjacency candidate** by the 12 actions `T_i^{+/-1}`. They are 12 distinct directed coordinate neighbours at every spatial coordinate state.

Freeze:

`X6_PURE_COORDINATE_ADJACENCY_CANDIDATE = SIX_POSITIVE_AXIS_STEPS + THEIR_PATH_REVERSALS`.

`PATH_REVERSAL != NEW_NATIVE_NEGATIVE_AXIS`.

Promotion of this coordinate graph to the complete native Cell adjacency graph is part of this Foundation admission; additional carrier/channel adjacency, if later declared, must be separately typed rather than silently changing the coordinate graph.

## 6. Pairwise orthogonality and full directed gauge

P000 already defines

`E_i PERP_E E_j` for all `i!=j`

and native right angle `120 degrees`.

For a displacement class g define

`D6(g)=can6(g)`

and

`ell6(g)^2=sum_i D6_i(g)^2`.

For Cells P,Q define

`D6(P->Q)=can6(coord(Q)-coord(P))`;

this is anchor-independent as a displacement class.

The directed gauge is positive, definite, integer-homogeneous and satisfies the triangle inequality. It is generally asymmetric under path reversal.

A unit positive-axis displacement has squared gauge 1; its reverse decoder has five 1s and one 0, squared gauge 5. Projection to any selected three-axis coordinate slice containing that axis gives a local min-zero reverse component pattern `(0,1,1)` up to order; on an already-established three-axis Cell slice this exactly recovers the accepted local reverse squared gauge 2.

## 7. Native 3-axis coordinate selections versus established Cell slices

For every 3-subset `S` of the six axes define the **coordinate observation**

`Obs_S([z])=can3(z|_S)`.

There are `binom(6,3)=20` native three-axis coordinate selections under the P000 `SELECT_3_OF_6_SPATIAL_AXES` semantics.

Important strength boundary:

- all 20 are exact coordinate projections of the six-axis completion;
- only the current FCC/K4 four-star subatlas is presently frozen with the full overlapping-circle Cell realization, typed local trajectories and three-step local Cell-return semantics;
- the other 16 coordinate selections are not silently promoted to already-realized circle-cell slices.

For every coordinate selection S:

If `i in S`, then

`Obs_S(T_i x)=T_i^S Obs_S(x)`.

If `i notin S`, then

`Obs_S(T_i x)=Obs_S(x)`.

Therefore omitted axes act on the full spatial coordinate state while being exactly invisible in that selected coordinate observation.

The hidden coordinate kernel is

`ker Obs_S ~= Z^3`,

generated by the omitted three axes.

This is the exact spatial-coordinate meaning of P000 omitted-coordinate semantics.

## 8. Coordinate triangle holonomy and the established four Cell slices

For any coordinate selection `S={i,j,k}`, define the full coordinate displacement

`H_S=e_i+e_j+e_k in G6_D`.

Purely at coordinate-observer strength,

`Obs_S(H_S)=0`,

while

`H_S != 0` in full X6, and

`H_{S^c}=-H_S`.

For the four currently established FCC/K4 Cell slices, this coordinate identity supplies the correct full-state lift of their already-frozen local three-axis triangle/reverse-third terminal relation: the local observation closes while the full six-axis coordinate state may carry omitted-coordinate holonomy.

For the remaining 16 coordinate selections, `Obs_S(H_S)=0` is only a coordinate-projection identity until a corresponding native Cell-slice realization is separately established.

As a negative boundary, if one were to impose `H_S=0` in the full state for **all 20** coordinate selections, all six axis generators collapse to one `C3` action. Therefore no full X6 theory preserving six distinct coordinate axes may globally promote every coordinate-triple projection identity to a full-state return law.

## 9. Rotation skeleton

Every permutation of the six native axes preserves the coordinate torsor structure, min-zero section, pure coordinate adjacency candidate, pairwise Enterprise orthogonality and sum-of-squares component gauge.

Freeze the finite positive-axis permutation skeleton

`X6_AXIS_PERMUTATION_ROTATION_SKELETON = S6`.

This is not a claim that every native rotation is only an axis permutation, nor that every S6-moved 3-axis coordinate selection already has the current FCC circle-cell realization.

The existing FCC/K4 atlas-preserving group embeds as

`S4 < S6`.

Under that carrier subgroup the 20 native three-axis coordinate selections split into 4 K4 stars, 4 K4 faces and 12 K4 path triples. Only the four stars are the currently frozen FCC close-packed Cell slices.

The local visible C3 on an established slice is the `A3` subgroup of the visible S3 axis-permutation stabilizer. For other coordinate selections this is an exact coordinate-label symmetry, not yet a claim of a realized Cell-slice rotation process.

## 10. Cell identity versus common-depth covers

Connected coordinate-faithful covers

`Z^6 / mZ(1,...,1)`

classify possible additional common-depth/internal relational memory over the six-axis coordinate state in the natural commuting translation model class. The already-main-backed common-depth cocycle gives their exact composition law.

Under this Foundation candidate they are treated as **additional Cell decoration/internal relational state**, not alternative six-dimensional spatial coordinate spaces.

Freeze candidate typing:

`X6_NATIVE_SPATIAL = COORDINATE TORSOR G6_D`.

`OPTIONAL_CELL_INTERNAL_FIBRE != ADDITIONAL_SPATIAL_COORDINATE`.

`PATH/BRC HISTORY != CELL_CENTER_IDENTITY`.

This does not assert that every possible future physical/internal state over a Cell is classified by the `m`-cover family; the `m` theorem only classifies connected commuting coordinate-faithful endpoint covers whose extra equality relation lies in the global diagonal.

## 11. BRC interface

For pure positive six-axis **coordinate paths** of length m with min-zero coordinate endpoint a, exact terminal N-BRC multiplicity is

`m! / product_i(a_i+k)!`

when `k=(m-sum a_i)/6` is a nonnegative integer, and zero otherwise.

The exact positive-rational weighted analogue multiplies this multinomial by `product_i w_i^(a_i+k)`.

The canonical coordinate-endpoint grade is `sum a_i mod6`.

Path-formal BRC remains above endpoint coordinates and retains ordering/provenance/multiplicity as required by the observer. These formulas become native Cell-endpoint formulas only for the pure coordinate subcategory after coordinate-adjacency admission.

## 12. Admission statement

This candidate is ready for Foundation admission under the P000-derived spatial typing statement:

`FULL NATIVE SPATIAL CELL CENTER IDENTITY IS THE SIX-AXIS COORDINATE TORSOR`.

This is the full-dimensional lift of the existing slice principle `CELL_IDENTITY_IS_BY_CELL_CENTER`, not a claim that every dynamic/internal state of a packet is exhausted by coordinates.

It does not make the geometric origin a Cell, does not identify FCC carrier Euclidean coordinates with native six-dimensional coordinates, does not infer six dimensions from the classical rank of `G6_D`, and does not promote unestablished coordinate selections to already-realized circle-cell slices.
