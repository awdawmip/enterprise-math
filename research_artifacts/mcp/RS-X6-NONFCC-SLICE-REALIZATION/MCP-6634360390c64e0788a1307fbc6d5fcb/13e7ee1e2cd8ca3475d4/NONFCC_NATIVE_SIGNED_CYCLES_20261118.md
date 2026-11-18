# RS-X6-NONFCC: native signed cycles and carrier-separation lemma (2026-11-18)

Task publication: `TP2-A3C8E1D754209B6F31D4`. Scope: signed-X6 spatial Cell graph and the frozen centered three-axis slices, not an independently reviewed theorem or a physical force-balance claim.

## Premises
`X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`; primitive steps `+e_i,-e_i`, a centered 3-axis slice `X_S(c*)=c*+sum_{i in S} Z e_i`, and the admitted axis-permutation skeleton `S6`. A *simple signed native cycle* is a closed nearest-neighbour Cell path with distinct preterminal Cell vertices, not a `TRIADIC_CLOSURE_E` force event. The historical FCC atlas realizes four STAR triples with full overlapping-circle carrier readout, with S4 permuting the six K4 edge labels.

## Result 1: all 20 triples have simple native C6 and C12 graph cycles
For every 3-subset S=(i,j,k), the signed word
`(+i,+j,+k,-i,-j,-k)`
visits the six distinct vertices
`0,e_i,e_i+e_j,e_i+e_j+e_k,e_j+e_k,e_k`,
then returns to the initial **native Cell**. It is a simple six-edge cycle inside the centered subtorsor. Any closed signed path that uses all three axes requires at least one positive and one negative step on each axis, hence six is minimal for this support condition.

A simple twelve-edge cycle that uses each of the six signed directions twice is
`(+i,+i,+j,-i,-i,+j,+k,-j,+k,-j,-k,-k)`.
Exact integer-coordinate tracing yields 12 distinct preterminal vertices and return to zero; see checker. Of all `6!=720` permutations using `+i,-i,+j,-j,+k,-k` once, exactly **192** are simple signed six-cycles anchored at the start. The finite enumeration and its exact domain are specified in the checker; existence has a direct construction.

## Result 2: native S6 single orbit, atlas S4 three orbits
Coordinate permutations from S6 preserve signed primitive adjacency and `sum_i z_i^2`, and act transitively on all 20 three-subsets. Therefore no S6-invariant predicate of this *pure coordinate graph/metric alone* distinguishes a STAR triple from a FACE or PATH triple. This is a boundary on what native coordinate data can decide, not a claim that the entire native rotation group equals S6.

Identify six axis labels with six K4 edges only for the historical carrier atlas. Its S4 vertex-relabeling subgroup classifies each 3-edge selection by its K4 degree profile: STAR `(3,1,1,1)` gives 4, FACE `(2,2,2,0)` gives 4, and PATH `(2,2,1,1)` gives 12. These are separate, complete S4 orbits and sum to 20. Only the four STAR selections presently have admitted complete FCC overlapping-circle carriers. Native signed graph cycles do not construct additional carriers.

## Non-STAR observer counterexample
Take a FACE triple S consisting of K4 edges `01,02,12`. Let `z=0`, `z'=H_S=sum_{i in S}e_i`. Both `Obs_S` min-zero triples are `(0,0,0)`, although their native endpoints differ. For an omitted axis a, `z''=e_a` also reads `(0,0,0)`, while it lies outside the centered subtorsor `X_S(c*)`. Hence coordinate-observer equality does not imply native Cell equality or slice membership. Circle/gate/overlap carrier assertions require new carrier data and a compatibility argument.

## Evidence, scope, remaining hard target
Direct construction proves native C6 existence and minimal support length; the C12 witness and finite 192/720 count are independently checked with integer arithmetic. The checker exhausts 20 triples and all 24 K4 automorphisms. These statements advance the non-FCC native graph part of the Task, preserve prior four STAR results and named contributors, and do not close the open non-permutation rotation, native triadic incidence, or non-STAR carrier realization/obstruction problem. Next useful unit: test an explicit admissible carrier/triadic-incidence extension on one FACE or PATH orbit and classify exactly which additional invariant it requires.

Scientific pins: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` and `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md` at the same commit. Existing taskbook and proof-strength rules retained.