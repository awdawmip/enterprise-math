# Enterprise X6 signed native spatial Cell torsor — Foundation candidate

Status: `FOUNDATION CANDIDATE / P000-V4-ALIGNED / EXACT SIGNED COORDINATE LAYER / NOT YET CURRENT-ROUTER PROMOTED`
Date: `2026-09-05`

## 1. Native spatial object

Current P000 V4 freezes:

- six native spatial axes;
- signed primitive direction domain `{+E_i,-E_i}`;
- pairwise Enterprise orthogonality of distinct axes;
- native right angle `120 degrees`;
- off-native-axis apparent directions as composite native paths, not new primitive axes.

Define the candidate native spatial Cell-center state space

`X6_NATIVE_SPATIAL`

as an affine torsor for

`G6_FULL = Z^6`.

A chosen Cell anchor supplies a relative coordinate chart `coord:X6_NATIVE_SPATIAL -> Z^6`; the anchor is not the geometric origin `O_E`.

Freeze candidate guard:

`CELL_COORDINATE_ZERO = CHOSEN_CELL_ANCHOR != GEOMETRIC_ORIGIN_O_E`.

## 2. Six signed coordinate directions

The basis vector `e_i` represents one unit along `+E_i`; `-e_i` represents one unit along `-E_i`.

These are the twelve primitive signed coordinate directions already admitted by P000 V4. No extra primitive diagonal direction is introduced.

Pure coordinate adjacency is

`z -> z +/- e_i`.

Any displacement supported on more than one native axis is a composite native path at primitive-line strength, even though it has a perfectly valid multi-axis endpoint coordinate.

## 3. Full spatial norm and distance

For signed displacement `z=(z_1,...,z_6)`, P000 pairwise Enterprise orthogonality gives

`L_E(z)^2=sum_i z_i^2`.

Hence

`L_E(-z)=L_E(z)`

and each primitive signed axis unit has squared norm 1.

For Cells P,Q define

`D6(P,Q)=coord(Q)-coord(P) in Z^6`

and

`d6(P,Q)^2=sum_i D6_i(P,Q)^2`.

At the full signed spatial level this readout is symmetric. This does not import a classical `90 degree` angle: the quadratic component rule is the current P000 `PERP_E/120 degree` rule.

## 4. Three-axis positive min-zero observations

For every selected 3-of-6 coordinate set `S={i,j,k}`, define

`Obs_S(z)=can3(z_i,z_j,z_k)`

with the already-established three-axis min-zero decoder.

There are 20 native coordinate selections. Only the FCC/K4 four-star subatlas currently has the fully established overlapping-circle Cell realization; the other 16 are coordinate selections until separately realized.

For one selected S, the kernel is

`ker Obs_S = {z:z_i=z_j=z_k} ~= Z^4`.

Thus the selected positive-only observation forgets:

- one common offset among the visible three signed coordinates;
- all three omitted signed coordinates.

## 5. Joint relative observer

The complete family of 20 positive-min-zero coordinate observations determines a full signed state only modulo the global diagonal subgroup

`Delta=Z*(1,1,1,1,1,1)`.

Hence their joint relative-coordinate object is

`G6_REL = Z^6/Delta`.

This is exactly the V7-V15 `G6_D` object, now correctly typed as a relative/joint-slice observer rather than the full spatial Cell torsor.

Exact sequence:

`0 -> Z*1 -> G6_FULL -> G6_REL -> 0`.

## 6. Min-zero residual + common depth is lossless for the full state

Every signed coordinate vector z has a unique decomposition

`z=r+h*1`

where

`r=can6(z)` is a nonnegative min-zero six-tuple and

`h=min_i z_i in Z`.

Thus

`Z^6 <-> A6_D x Z`

as an exact coordinate chart.

The existing six-axis V2 common-depth carry is precisely the section cocycle for addition in this chart:

`(r,h)*(s,k)=(can6(r+s), h+k+min_i(r_i+s_i))`.

Common depth is a composite six-axis spatial displacement coordinate, not a seventh primitive spatial axis.

## 7. Full diagonal displacement

Let

`D=(1,1,1,1,1,1)`.

Then

`D != 0 in G6_FULL`,

`L_E(D)^2=6`.

D is a composite six-step native-axis displacement. Every positive-min-zero 3-axis coordinate observation maps D to zero.

Therefore D is a concrete full spatial motion invisible to every current-style positive 3-axis coordinate observer.

## 8. Established local triangle lift

For a selected coordinate triple S define

`H_S=sum_{i in S}e_i`.

At coordinate-observer strength

`Obs_S(H_S)=0`.

For the four established FCC/K4 Cell slices, this is the correct full signed spatial lift of the local three-positive-axis triangle/reverse-third terminal relation: the slice observation closes, while the full state changes by `H_S`.

For complementary triples,

`H_S+H_{S^c}=D`.

Only after passing to `G6_REL` does this become `H_{S^c}=-H_S`.

## 9. Rotation skeleton

All six-axis coordinate permutations act on `Z^6` and preserve signed coordinate adjacency, the P000 norm, Delta, the relative quotient and the 20 coordinate selections.

Freeze candidate finite skeleton:

`X6_POSITIVE_AXIS_PERMUTATION_SKELETON = S6`.

The current FCC/K4 atlas-preserving subgroup is the known embedded `S4`.

This is not a claim that the complete native rotation dynamics is only finite or only an axis permutation.

## 10. BRC hierarchy

For a pure positive-axis path of length m, its full signed endpoint from the chosen anchor is its exact six-axis occurrence vector

`n in N_0^6`, `sum n_i=m`.

N-BRC multiplicity at that full endpoint is

`m!/product_i n_i!`.

There is no nontrivial return to the full signed spatial anchor using only positive steps.

If the observer forgets common depth and retains only `r=can6(n)` together with path length m, then

`n=r+k*1`, `k=(m-sum r_i)/6`,

and the previously derived relative-endpoint formula is recovered exactly.

Path-formal/Weighted-BRC remains richer than spatial endpoint identity and retains ordering, branch identity, multiplicity, weight and provenance as required by the observer contract.

## 11. Cell identity scope

This Foundation candidate identifies only **spatial Cell-center identity** with the signed six-axis coordinate torsor.

It does not say that occupancy, channel state, forces, time-indexed relations, fields, BRC path history or other packet decorations are determined by spatial coordinates.

Freeze candidate typing:

`X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`.

`FULL_PACKET_STATE MAY FIBRE OVER X6_NATIVE_SPATIAL`.

`INTERNAL_OR_TIME_STATE != ADDITIONAL_SPATIAL_AXIS`.

## 12. Admission statement

The only semantic admission needed is the full-dimensional lift of the already-established slice rule `CELL_IDENTITY_IS_BY_CELL_CENTER`:

`FULL_NATIVE_SPATIAL_CELL_CENTER_IDENTITY_IS_COMPLETE_IN_SIX_SIGNED_AXIS_COORDINATES`.

Under current P000 V4, this candidate preserves rather than quotients the signed native-axis state and is therefore the preferred current X6 spatial completion.