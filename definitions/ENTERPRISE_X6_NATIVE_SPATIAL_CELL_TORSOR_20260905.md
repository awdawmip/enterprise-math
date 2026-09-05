# Enterprise X6 native spatial Cell torsor

Status: `ACTIVE / FOUNDATION / P000-V4-BOUND / SIGNED-SIX-AXIS`
Date: `2026-09-05`
Authority: P000 V4 + direct user mandate to complete the six-axis theory/tool layer as common Enterprise Math foundation.
Research provenance:
- `research_notes/X6_P000_V4_SIGNED_AXIS_REFOUNDATION_V16_20260905.md`;
- `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md`;
- `research_notes/X6_JOINT_OBSERVER_PRESERVATION_AUDIT_V18_20260905.md`.

## 1. Scope

This definition freezes the **native spatial Cell-center identity** only.

It does not say that all packet state is spatial coordinate state. Occupancy, channel state, force relations, fields, time-indexed relations, Path-formal history, BRC branch identity/multiplicity/weight and other declared decorations remain separately typed over the spatial Cell object.

Freeze:

`X6_NATIVE_SPATIAL != FULL_DECORATED_PACKET_STATE`.

`INTERNAL_OR_TIME_STATE != ADDITIONAL_SPATIAL_AXIS`.

## 2. Full signed spatial coordinate carrier

Current P000 V4 defines six native spatial axes and the primitive signed direction domain

`{+E_1,-E_1,...,+E_6,-E_6}`.

Freeze the full spatial translation group

`G6_FULL := Z^6`

with standard basis `e_1,...,e_6` corresponding to `+E_i`; `-e_i` corresponds to the already-P000 primitive signed reverse direction `-E_i`.

Define `X6_NATIVE_SPATIAL` to be an affine torsor for `G6_FULL`.

A chosen Cell anchor `c_*` supplies a relative chart

`coord_{c_*}:X6_NATIVE_SPATIAL -> Z^6`.

The anchor is a Cell chosen for coordinates; it is not the geometric origin `O_E`.

Freeze:

`X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`.

`FULL_NATIVE_SPATIAL_CELL_CENTER_IDENTITY_IS_COMPLETE_IN_SIX_SIGNED_AXIS_COORDINATES = TRUE`.

`CELL_COORDINATE_ZERO = CHOSEN_CELL_ANCHOR != GEOMETRIC_ORIGIN_O_E`.

Enterprise dimension remains defined by P000 native-axis count. No conclusion about native dimension is derived from ordinary module rank.

## 3. Primitive coordinate adjacency

The pure coordinate adjacency actions are

`T_i^+(z)=z+e_i`,

`T_i^-(z)=z-e_i`.

They give twelve distinct directed primitive coordinate neighbours at every spatial Cell.

Freeze:

`X6_PURE_COORDINATE_ADJACENCY = SIGNED_UNIT_NATIVE_AXIS_STEPS`.

A displacement supported on more than one native axis is not promoted to a new primitive straight direction. Under P000 V4 it is a composite native path/readout.

Additional non-coordinate adjacency/channel mechanisms, if later admitted, are separately typed and do not silently mutate this coordinate graph.

## 4. Native orthogonality and full spatial metric

P000 already freezes for all distinct axes

`E_i PERP_E E_j`

and

`ENTERPRISE_RIGHT_ANGLE=120_DEGREES`.

For signed displacement

`z=(z_1,...,z_6) in Z^6`,

define the native six-axis component quadratic readout

`L_E(z)^2 = sum_i z_i^2`.

For Cells P,Q define

`D6(P,Q)=coord(Q)-coord(P)`

and

`d6(P,Q)^2=sum_i D6_i(P,Q)^2`.

This is anchor-independent, symmetric under reversal and satisfies the ordinary finite component triangle inequality.

Freeze:

`FULL_X6_SIGNED_AXIS_NORM_SQUARED = SUM_OF_SIX_SIGNED_COMPONENT_SQUARES`.

`L_E(+e_i)=L_E(-e_i)=1`.

This does not restore classical `90 degree` orthogonality. The quadratic rule is the current P000 Enterprise `PERP_E / 120 degree` component rule.

## 5. Three-axis positive-min-zero coordinate observers

For every 3-subset `S={i,j,k}` of the six axes define the coordinate observer

`Obs_S(z)=can3(z_i,z_j,z_k)`,

where `can3` subtracts the minimum of the selected three integers and returns the established nonnegative min-zero three-component address/readout.

There are `binom(6,3)=20` native **coordinate selections**.

Strength guard:

- all 20 maps are native coordinate observers;
- only the current FCC/K4 four-star subatlas is presently frozen with the complete overlapping-circle Cell realization and its local trajectory theorems;
- the other 16 coordinate selections are not silently promoted to already-realized circle-cell slices.

For one selected S,

`ker(Obs_S)={z:z_i=z_j=z_k} ~= Z^4`.

The selected observer therefore forgets one common visible offset plus the three omitted signed coordinates.

Freeze:

`SLICE_OBSERVATION != FULL_CELL_STATE`.

`OMITTED_COORDINATE != ZERO_COORDINATE`.

## 6. Joint relative observer and the role of common depth

The complete family of all twenty positive-min-zero coordinate observations determines a full signed state exactly modulo

`Delta := Z*(1,1,1,1,1,1)`.

Hence the joint relative coordinate observer is

`G6_REL := Z^6 / Delta`.

Exact sequence:

`0 -> Delta -> G6_FULL -> G6_REL -> 0`.

The earlier six-axis min-zero object `G6_D` is therefore retained with the canonical type

`G6_D = G6_RELATIVE_COORDINATE_OBSERVER`,

not full spatial Cell identity.

Every `z in Z^6` decomposes uniquely as

`z = r + h*(1,...,1)`

with

`r=can6(z)` nonnegative/min-zero and `h=min_i z_i in Z`.

Thus

`Z^6 <-> A6_D x Z`

is a lossless chart.

The existing V2 common-depth carry

`c(r,s)=min_i(r_i+s_i)`

is the exact change-of-section 2-cocycle:

`(r,h)*(s,k)=(can6(r+s),h+k+c(r,s))`.

Freeze:

`COMMON_DEPTH = COMPOSITE_GLOBAL_DIAGONAL_SPATIAL_COORDINATE`.

`COMMON_DEPTH != SEVENTH_SPATIAL_AXIS`.

Any projection dropping common depth requires an observer/future-operation safety certificate under the mandatory Joint Relation Observer Preservation contract.

## 7. Full diagonal composite displacement

Let

`D=(1,1,1,1,1,1)`.

Then in full X6:

`D != 0`,

`L_E(D)^2=6`.

D is a six-axis composite native path displacement, not a primitive new direction.

Every current-style positive-min-zero three-axis coordinate observer satisfies

`Obs_S(D)=0`.

Thus D is an explicit full spatial displacement invisible to every such lower-dimensional positive coordinate observer.

## 8. Established local triangle relations versus full X6

For any coordinate selection S define

`H_S=sum_{i in S}e_i`.

Coordinate-wise

`Obs_S(H_S)=0`.

For the four established FCC/K4 Cell slices, this gives the full-state lift of their local positive-triangle/reverse-third terminal relation: the selected slice observation may close while full X6 changes by `H_S`.

For complementary triples,

`H_S+H_{S^c}=D` in full X6.

Only after passing to `G6_REL` does this become `H_{S^c}=-H_S`.

Promoting every 3-of-6 coordinate-triple projection identity to a full-state return would collapse all six axis actions to a single `C3` action and is therefore forbidden as a silent lift.

## 9. Rotation skeleton

Every permutation of the six positive axis labels acts on `Z^6` by coordinate permutation and preserves:

- the twelve signed primitive coordinate directions;
- the P000 quadratic readout;
- the joint diagonal subgroup and relative quotient;
- the twenty three-axis coordinate observers.

Freeze the exact finite axis-permutation skeleton

`X6_AXIS_PERMUTATION_ROTATION_SKELETON = S6`.

This classifies rotations that act only by permuting the six distinguished positive-axis labels. It does not assert that the complete native rotation dynamics is only finite or only an axis permutation.

The established FCC/K4 six-line atlas subgroup embeds as

`S4 < S6`.

Under this carrier subgroup the twenty coordinate selections split into orbit types `4 STAR + 4 FACE + 12 PATH`; only the four STAR selections are the currently frozen FCC close-packed Cell slices.

## 10. P000 direction gate and BRC multipath theorem

For signed spatial displacement `z`, the minimum primitive transition count is

`N_min(z)=sum_i |z_i|`.

The P000 spatial component length is

`L_E(z)=sqrt(sum_i z_i^2)`.

Hence

`L_E(z) <= N_min(z) <= sqrt(6) L_E(z)`.

For nonzero integer displacement,

`PRIMITIVE_STRAIGHT_SEGMENT <=> SUPPORT_SIZE(z)=1 <=> N_min(z)=L_E(z)`.

If support size is at least two, the displacement is a composite native path and the exact number of ordered shortest path realizations is

`B_min(z)=N_min(z)! / product_i |z_i|! > 1`.

This is the exact N-BRC multiplicity underlying a coarse off-native-axis multipath/jitter readout.

More generally, for path length M and target z, write

`a_i=max(z_i,0)`, `b_i=max(-z_i,0)`, `K=(M-||z||_1)/2`.

If K is not a nonnegative integer then endpoint multiplicity is zero. Otherwise

`N_M(z)=M! * sum_{k_1+...+k_6=K} product_i 1/[(a_i+k_i)!(b_i+k_i)!]`.

Positive-rational signed-axis branch weights have the corresponding exact weighted formula. Path-formal and Weighted-BRC remain richer observers and are not replaced by spatial endpoint coordinates.

## 11. Positive-only BRC and the relative observer

For a path using only the six positive axes, the full endpoint from the chosen anchor is its exact occurrence vector

`n in N_0^6`, `sum_i n_i=m`.

Its N-BRC multiplicity is

`m!/product_i n_i!`.

No nontrivial positive-only path returns to the full signed spatial origin.

If an observer retains only the relative min-zero endpoint `r=can6(n)` and path length m, then the omitted common depth is reconstructed by

`k=(m-sum_i r_i)/6`,

when this is a nonnegative integer, and the relative-endpoint multiplicity becomes

`m!/product_i(r_i+k)!`.

Thus prior V9 formulas remain valid after retyping as relative-endpoint + path-length formulas.

## 12. Observer/provenance hierarchy

Mandatory safe hierarchy:

`PATH-FORMAL / WEIGHTED-BRC`

`-> SIGNED SIX-AXIS TRACE / OCCURRENCE DATA`

`-> X6_NATIVE_SPATIAL ENDPOINT Z^6`

`-> G6_REL + REPAIR COMMON_DEPTH WHEN NEEDED`

`-> SELECTED 3-AXIS MIN-ZERO OBSERVER + EXPLICIT HIDDEN COORDINATES WHEN NEEDED`

`-> COARSER SUPPORT/TOTAL READOUT`.

No downward projection is globally declared safe merely because the source can later be algebraically reconstructed in some restricted setting; observer and future-operation scope must be certified.

## 13. Current open spatial questions after this admission

Closed here:

- full spatial Cell-center coordinate identity;
- signed primitive coordinate adjacency;
- six-axis component metric;
- twenty coordinate projections and their information loss;
- joint relative observer/common-depth decomposition;
- S6 axis-permutation rotation skeleton;
- primitive-line versus composite-multipath path calculus.

Still open above this foundation:

- complete native rotation dynamics beyond axis permutations;
- Cell/channel/internal-state dynamics and their coupling to spatial coordinates;
- detailed native realization of the sixteen non-FCC three-axis coordinate selections;
- admissible `TRIADIC_CLOSURE_E` incidence/dynamics beyond the P000 arity/angle definition;
- physical parameter calibration and time evolution;
- application-specific safe quotients and observer bridges.
