# X6 under P000 V4：有符号六轴原生空间、relative slice quotient 与 common-depth 复位

Status: `DERIVED / CURRENT-P000-REBASED / CORRECTS V7-V15 SPATIAL-PROMOTION DIRECTION`
Date: `2026-09-05`
Authority: current P000 V4 (`SIGNED_NATIVE_SPATIAL_AXES`, pairwise `PERP_E`, 120° native right angle).

## 1. Control correction

P000 V4 now freezes the primitive direction domain as

`SIGNED_NATIVE_SPATIAL_AXES={+E_1,-E_1,...,+E_6,-E_6}`.

Therefore the full native **spatial coordinate** completion must not silently identify a simultaneous shift along all six axes merely because every positive-only 3-axis min-zero observer forgets it.

The earlier V7-V15 object

`G6_D=Z^6/Z(1,...,1)`

remains exact and useful, but is retyped as the maximal **relative six-axis / joint positive-slice coordinate observer**.

It is not the full signed spatial translation group under P000 V4.

## 2. Full signed spatial translation group

Let

`G6_full := Z^6`

with basis `e_1,...,e_6` corresponding to the six positive native spatial axes; `-e_i` is the primitive signed reverse direction already admitted by P000 V4.

A homogeneous connected spatial Cell-center component is naturally an affine torsor for `G6_full` once Cell-center coordinate completeness is admitted.

No classical-rank reduction occurs:

`rank_Z(G6_full)=6`,

but the reason Enterprise spatial dimension is six remains P000 axis count, not this classical rank computation.

## 3. P000 norm/readout

For signed displacement

`z=(z_1,...,z_6) in Z^6`,

pairwise Enterprise orthogonality gives the typed quadratic readout

`||z||_E^2=sum_i z_i^2`.

Hence reversal is symmetric at full spatial strength:

`||-z||_E=||z||_E`.

In particular

`||+e_i||_E^2=||-e_i||_E^2=1`.

This supersedes the interpretation of V12 `{1,5}` as a **full** X6 bidirectional spectrum. `{1,5}` remains the directed positive-only canonical-quotient gauge of `G6_D`; it is not the full signed P000 spatial norm.

## 4. Positive 3-axis slice observation

For any selected three-axis coordinate set `S={i,j,k}`, define the established-style positive min-zero observation

`Obs_S(z)=can3(z_i,z_j,z_k)`.

This map factors through local diagonal shift and therefore intentionally forgets the common visible offset.

Its kernel as a map from the full signed spatial group is

`ker Obs_S = {z : z_i=z_j=z_k}`

which is isomorphic to `Z^4`:

- one common visible offset;
- three omitted-axis signed coordinates.

Thus a 3-axis positive-only observation loses four integer coordinates of a full signed spatial state.

This is stronger and more faithful to P000 V4 than the earlier V7 statement `ker ~= Z^3`, which was already downstream of the global diagonal quotient.

## 5. Joint 20-slice observer

Collect all 20 `SELECT_3_OF_6` coordinate observations.

Two full signed states z,z' have identical observations in **every** 3-axis positive-min-zero coordinate selection iff

`z-z' = h*(1,1,1,1,1,1)`

for some `h in Z`.

Proof: equality of every 3-axis min-zero observation gives equality of every pair difference `z_i-z_j`; therefore all coordinate differences of z-z' are zero, so it is global diagonal. Conversely a global diagonal shift is deleted by every local canonicalization.

Hence the joint slice-observation quotient is exactly

`G6_full / Z*1 = G6_D`.

This gives the exact sequence

`0 -> Z*1 -> Z^6 -> G6_D -> 0`.

The V7 inverse-limit theorem is therefore retained but retyped correctly: it reconstructs the full **relative** coordinate class, not the absolute signed spatial state.

## 6. Common depth is the missing full spatial coordinate combination

Every `z in Z^6` decomposes uniquely as

`z = r + h*1`

with

`r=can6(z) in A6_D`,

`h=min_i z_i in Z`.

Therefore, as a set/chart,

`Z^6 ~= A6_D x Z`.

This is precisely the residual + common-depth split already implemented in the six-axis V2 tooling.

Under current P000 V4, the common depth is not an extra spatial dimension: it is the coordinate of the composite off-native-axis displacement

`D=e_1+...+e_6`.

P000 explicitly says an off-native-axis direction is a composite native path rather than a new primitive axis. So

`COMMON_DEPTH = COMPOSITE SIX-AXIS SPATIAL DISPLACEMENT COORDINATE`,

not `SEVENTH SPATIAL AXIS` and not automatically `INTERNAL CELL MEMORY`.

## 7. Existing V2 depth carry becomes the exact full-coordinate chart cocycle

Let full states be encoded by `(r,h)` with `r=min-zero` and `h in Z`.

For residuals a,b define the already-main-backed carry

`c(a,b)=min_i(a_i+b_i)`.

Then ordinary signed translation addition on `Z^6` becomes

`(a,h)*(b,k)=(can6(a+b), h+k+c(a,b))`.

Thus the V2 depth-carry 2-cocycle is not merely an optional cover decoration: it is the exact change-of-section cocycle for the full signed six-dimensional coordinate group.

Associativity is exactly the previously verified cocycle identity.

## 8. Full diagonal displacement is real spatial movement

Let

`D=(1,1,1,1,1,1)`.

In full X6 spatial coordinates:

`D != 0`,

`||D||_E^2=6`.

It is a six-step composite native path (many orderings in Path-formal/BRC), not a primitive straight direction.

Every positive-min-zero 3-axis coordinate observer sees

`Obs_S(D)=0`.

So `D` is a concrete nonzero full spatial displacement invisible to every positive-only 3-axis coordinate observation.

This supplies a strict algebraic realization of

`SLICE_OBSERVATION != FULL_CELL_STATE`.

## 9. Three-axis triangle lift

For `S={i,j,k}` let

`H_S=e_i+e_j+e_k in Z^6`.

Then

`Obs_S(H_S)=0`.

For the four established FCC/K4 Cell slices, the local positive triangle closes in the selected observer while the full signed spatial state changes by `H_S`.

The complementary displacement satisfies in the **full** group

`H_S + H_{S^c}=D`,

not `H_{S^c}=-H_S`.

The earlier minus relation holds only after passing to the relative quotient `G6_D` where D is killed.

## 10. S6 axis permutation skeleton

`S6` acts on `Z^6` by permuting coordinates. It preserves:

- the six signed native axis pairs;
- the full sum-of-squares P000 norm;
- primitive coordinate adjacency `z -> z +/- e_i`;
- the diagonal subgroup `Z*1`;
- the joint relative quotient `G6_D`;
- the 20 coordinate selections.

Hence the exact positive-axis permutation skeleton remains `S6`, and the FCC/K4 `S4` remains a 24-element subgroup.

## 11. BRC consequences

For positive-only six-axis paths of length m from a chosen anchor, the full endpoint is the exact occurrence vector

`n=(n_1,...,n_6) in N_0^6`, `sum n_i=m`.

The exact N-BRC multiplicity is simply

`m! / product_i n_i!`.

There is **no nontrivial full spatial return using only positive steps**.

The V9 formula

`m! / product_i(a_i+k)!`

remains exactly correct for the relative endpoint observer `a=can6(n)` at fixed path length, because the length determines the omitted common depth

`k=(m-sum a_i)/6`.

Thus V9 is retyped from `full Cell return kernel` to `relative endpoint + path-length reconstruction kernel`.

In particular the former numbers 720 at length 6 and 7,484,400 at length 12 count paths whose **relative min-zero endpoint** is zero; their full signed endpoints are respectively D and 2D, not the starting Cell.

## 12. Correct current X6 candidate

The strongest P000-V4-compatible spatial candidate is therefore

`X6_NATIVE_SPATIAL = AFFINE TORSOR OVER Z^6`.

A coordinate chart based at any Cell anchor uses six signed integers.

The current three-axis min-zero addresses are lower-information positive-only slice observations, not the full address type.

Path history, BRC multiplicity, channel/occupancy state and time remain richer typed layers over the spatial Cell object.

## 13. What remains for Foundation promotion

Only the expected Cell-center typing bridge remains:

`FULL_NATIVE_SPATIAL_CELL_CENTER_IDENTITY_IS_COMPLETE_IN_THE_SIX_SIGNED_AXIS_COORDINATES`.

Under current P000 V4 this is the direct full-dimensional lift of `CELL_IDENTITY_IS_BY_CELL_CENTER` and is now structurally preferable to the obsolete min-zero full-space candidate.
