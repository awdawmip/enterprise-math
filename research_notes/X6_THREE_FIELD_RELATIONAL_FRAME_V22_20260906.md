# X6 upper V22: three labeled pure-triadic fields are minimally sufficient to resolve the residual S6 frame gauge

Status: `FREE_RESEARCH / EXACT FINITE-SYMMETRY FRAME THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- `X6_SINGLE_TRIADIC_FIELD_DYNAMICS_NOGO_V21_20260906.md`;
- `X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md`;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`.
Checker: `experiments/x6_three_field_relational_frame_v22_20260906/check_three_field_relational_frame.py`.

## 1. Minimal-field orbit

For every perfect matching M of the six native axes, V18 supplies a trade vector `v_M`. Retain both orientations

`h=+v_M` and `h=-v_M`.

There are

`15*2=30`

such oriented minimal pure-triadic field states.

S6 acts transitively on these 30 states. The stabilizer of each field has order

`720/30=24`.

This reproduces the V21 canonical field stabilizer without fixing a particular matching.

## 2. Labeled context fields

A multi-Cell context is called **labeled** here when the source identity of each field is retained, e.g. fields arriving from distinct neighboring Cells or distinct declared internal ports.

For a labeled tuple

`(h_1,...,h_r)`,

the residual axis-frame gauge is the pointwise stabilizer

`Stab(h_1,...,h_r)=intersection_a Stab(h_a)`.

This is different from an unordered bag of fields, whose stabilizer may also permute equal-status sources. The theorem below is explicitly about labeled contexts.

## 3. One field leaves a 24-fold gauge

Every one of the 30 fields has stabilizer order 24.

Therefore one pure-triadic context cannot identify a unique S6 frame.

This is the symmetry source of the V21 deterministic-selector obstruction.

## 4. Two labeled fields never fully resolve S6

Exhaustively classify the `C(30,2)=435` unordered pairs of distinct labeled field values by pointwise stabilizer size.

The exact census is:

- 15 pairs: stabilizer order 24;
- 240 pairs: stabilizer order 3;
- 180 pairs: stabilizer order 4.

The order-24 cases are the two opposite orientations `+v_M,-v_M` of the same matching, which have the same stabilizer.

For fields from different matching contexts, the residual stabilizer is either

`C3` (order 3)

or

`V4` (order 4).

In particular the stabilizer is never trivial.

Therefore **no pair of labeled minimal pure-triadic fields is sufficient to fix the full S6 axis frame**.

## 5. Three labeled fields can have trivial stabilizer

For the `C(30,3)=4060` triples of distinct field values, the exact pointwise-stabilizer census is:

- 3360 triples: stabilizer order 1;
- 400 triples: stabilizer order 3;
- 300 triples: stabilizer order 4.

Thus a generic triple of labeled minimal fields has trivial stabilizer.

An explicit free triple is supplied by the positive orientations of the three matchings

`M1={{0,1},{2,3},{4,5}}`,

`M2={{0,1},{2,4},{3,5}}`,

`M3={{0,2},{1,3},{4,5}}`.

The only axis permutation fixing all three oriented field vectors is the identity.

Hence, within this 30-state minimal field family:

`MINIMUM LABELED FIELD CONTEXTS FOR TRIVIAL S6 STABILIZER = 3`.

This is a finite symmetry theorem about this field family, not a universal arity axiom for all possible internal fields.

## 6. Free field triples are relational frame tokens

Fix one reference free triple

`H_*=(h_1^*,h_2^*,h_3^*)`.

Its S6 orbit has size 720 because its stabilizer is trivial.

Therefore every field triple in this orbit is represented by a **unique** `g in S6`:

`H=g H_*`.

So a free labeled field triple can serve as a complete relational S6 frame token. It resolves the 720-fold abstract axis/channel relabeling ambiguity at the finite-symmetry level without using an externally preferred spatial origin.

This does not mean the fields are spatial axes. They are internal triadic relation states whose joint pattern fixes a frame.

## 7. Relation to the 720 axis-channel frame gauge

The existing axis-channel theorem gives a 720-element torsor of bijections

`phi:C6_channels -> six native axis families`.

A free labeled pure-field triple also has a 720-element free S6 orbit.

Once a typed physical bridge specifies how the field-source labels and channel labels are compared to one reference configuration, the free field triple can remove the **axis relabeling** ambiguity in `phi` by determining the unique S6 frame element.

Important boundary:

this does not by itself prove a canonical channel-to-axis identification. A bridge between channel labels and the relational field sources remains semantic input. The theorem only says the residual S6 symmetry obstruction can be completely removed by three suitable labeled field contexts.

## 8. Symmetry obstruction removed does not mean law derived

If the pointwise stabilizer of the full input context is trivial, the T7 fixed-point obstruction to an equivariant deterministic choice disappears.

But this is only a **permission theorem**:

`TRIVIAL INPUT STABILIZER -> NO SYMMETRY-ONLY OBSTRUCTION`.

It does not uniquely choose:

- the next active triad;
- an Ori6 event;
- a force law;
- a channel update;
- a time schedule.

A dynamical rule is still needed. Different covariant rules can be written once the context contains a complete frame.

## 9. Relation to V17/V21

V21 shows one field naturally leaves a branched active-triad relation and cannot by itself produce a total deterministic J(6,3) successor.

V22 shows that adding relation context can genuinely remove the residual symmetry:

- one field: 24-fold residual gauge;
- two fields: residual C3 or V4 at best;
- three generic labeled fields: no residual S6 gauge.

This gives a sharp route for future multi-Cell dynamics: a local update may become deterministic only after sufficient neighboring/internal relation context is admitted, rather than by imposing a global tie-breaking convention.

## 10. Current frontier

Closed for the 30-state minimal field orbit:

- transitivity and 24-element one-field stabilizer;
- full two-field intersection census and two-field impossibility;
- full three-field intersection census;
- existence and explicit witness of free triples;
- three labeled fields as the minimal symmetry-complete relational frame context.

Next target:

construct and classify the **lowest-complexity covariant update laws** permitted on a free three-field context, and test whether any law determined solely by the canonical pure-triadic coupling can generate nontrivial J(6,3) holonomy/Ori6 charge rather than adding an arbitrary frame-coordinate convention.

No Foundation promotion or physical three-neighbor law is claimed.
