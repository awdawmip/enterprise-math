# R059D Stage AM — Canonical BRC Circle Collapse and Source/Target Non-Isometry

Task-ID: `RS-R059D-STAGE-AM-CANONICAL-BRC-CIRCLE-COLLAPSE-NONISOMETRY`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

## Frozen accepted inputs

Read-only:

1. Stage AD exact source coverage bridge and C-family semantics;
2. Stage AG N Beatty/Sturmian jump theorem;
3. Stage AH autonomous N boundary generator;
4. Stage AI algebraic circle constant theorem `kappa_E^2=12`, `kappa_E>0`;
5. Stage AJ uniform N/C_s one-layer phase theorem;
6. Stage AK target fixed-length native turn-orbit theorem;
7. Stage AL canonical native resolver rigidity theorem inside final `ADM_E=A0-A8`.

Do not modify any prior-stage result file.

## Driver working truth

Treat as the theorem direction:

> The orthogonal/source circle and the canonical Enterprise circle are not two coordinate descriptions of one metric circle. BRC is a collapse/comparison bridge from a continuous source realization to a unique native target turn orbit. It preserves the compatible cyclic/radius structure required for comparison, but source Euclidean arc metric does not descend as the target circumference metric.

The target circle is already fixed independently by AL. Stage AM must never use the source circle to re-select or redefine the target orbit.

## Hard target

Prove the strongest justified form of:

`CANONICAL_BRC_CIRCLE_COLLAPSE_ESTABLISHED__SOURCE_TARGET_NONISOMETRY_PROVED`.

At minimum construct a rigorous BRC relation/map between a typed orthogonal source circle state and the canonical Enterprise target orbit and prove:

1. source/target state semantics are explicitly distinct;
2. target is the already frozen AL canonical orbit;
3. the bridge is D6-equivariant and cyclic-order compatible;
4. every target orbit state has nonempty source compatibility fiber;
5. the source circle is fully covered by the target fibers, with only controlled boundary overlap/ties;
6. the bridge is generally many-to-one at finite target precision;
7. source arc-length is not a well-defined target one-turn invariant under collapse;
8. no isometric identification may silently equate source circumference with target turn period;
9. the accepted target constant remains `kappa_E^2=12`, independent of source metric choice.

Preferred stronger conclusion:

`SOURCE_EQUIDISTANCE_ARC_METRIC_DOES_NOT_DESCEND_THROUGH_CANONICAL_BRC`.

## Stage 0 — type freeze

Freeze the two sides before any comparison.

### Source side

Define a typed orthogonal compatibility circle state `C_perp(O,r)` using the already accepted source/teacher semantics. Classical continuous metric or the equivalent source quadratic chart may be used only on the source side.

Freeze source concepts separately:

- `SOURCE_POINT_STATE`;
- `SOURCE_CYCLIC_ORDER`;
- `SOURCE_RADIUS_CLASS`;
- `SOURCE_ARC_MEASURE` if used;
- `SOURCE_CIRCUMFERENCE_FUNCTIONAL` if used.

### Target side

Use the AL canonical Enterprise circle exactly as frozen:

- fixed-length segment state;
- local integer turn operator `tau_E`;
- canonical endpoint orbit;
- minimal period `T_r=C_E(r)`;
- `kappa_E^2=12`.

Do not define target membership by source distance, source Q, source angle or source circumference.

Required artifact:

`R059D_STAGE_AM_TYPED_SOURCE_TARGET_PROTOCOL.json`.

## Stage A — canonical BRC circle bridge

Construct the comparison bridge using already frozen BRC/coverage machinery and the AL target.

Preferred object:

`Phi_BRC,r : C_perp(O,r) -> O_E(O,r)`

if a canonical function is derivable.

If exact boundary ties make a single-valued function artificial, freeze a relation

`R_BRC,r subset C_perp(O,r) x O_E(O,r)`

and type its fibers explicitly.

The bridge must be derived from existing compatibility/coverage/incidence semantics; no radius-specific tuning, target-word lookup, or hand assignment of source arcs to target states.

Required properties to prove where true:

- surjective onto the canonical target orbit;
- D6 equivariant;
- orientation/cyclic-order preserving modulo tie fibers;
- source radius-class compatible with target anchor radius label;
- translation covariant;
- finite target states receive connected source arc/interval fibers if that follows from the construction;
- all source states are accounted for.

Required artifact:

`R059D_STAGE_AM_CANONICAL_BRC_CIRCLE_BRIDGE.json`.

## Stage B — fiber theorem

Characterize BRC fibers, not just the image.

For each target orbit state/edge `e_k`, define its source fiber `F_k`.

Prove the strongest true form of:

- `F_k` nonempty;
- fibers occur in canonical cyclic order;
- interiors are disjoint;
- neighboring fibers meet only at tie/boundary states;
- union of all fibers is the source circle;
- finite target precision forces nontrivial many-to-one fibers for sufficiently large/continuous source state space.

If point fibers rather than arc fibers occur under one bridge convention, audit the neighboring cell/edge fiber object and state which carrier is the correct comparison unit.

Required artifact:

`R059D_STAGE_AM_BRC_FIBER_THEOREM.json`.

## Stage C — metric descent test

This is the central theorem gate.

Let `mu_perp(F_k)` be the source arc measure of the fiber corresponding to one target elementary turn, when source arc measure is defined.

Test whether there exists a target-local constant `lambda(r)` such that every elementary target turn corresponds to equal source arc measure.

Preferred theorem:

`mu_perp(F_k)` is not constant in `k` for nontrivial radii, or more generally source arc measure is not determined solely by the target one-turn state.

A successful proof may use:

- exact source boundary locations of BRC fiber transitions;
- inequivalent fiber widths;
- D6-sector symmetry plus within-sector nonuniformity;
- explicit first exact radius at which equal source-arc fibers fail;
- symbolic nonuniformity rather than decimals.

Do not infer non-isometry merely because the final constants differ. Prove the local descent obstruction independently if possible.

Required artifact:

`R059D_STAGE_AM_SOURCE_ARC_DESCENT_AUDIT.json`.

## Stage D — circumference / period non-isometry theorem

Freeze distinct functionals:

- source circumference: integration/arc measure around `C_perp`;
- target circumference: minimal legal-turn period `T_r`.

Prove that BRC compatibility does not imply equality of these functionals.

Preferred theorem:

`SOURCE_ARC_CIRCUMFERENCE_IS_NOT_A_BRC_INVARIANT`.

Formalize the implication boundary:

If one *additionally* imposed an isometry axiom that every target turn carried a common source arc unit and total source circumference descended exactly to target turn count under a fixed unit normalization, then the source and target circumference/diameter constants would be forced to coincide. This extra axiom is not part of BRC and should be shown false or unsupported by Stage C.

Keep any source circle constant symbol typed as `kappa_perp` / `pi_source`; do not identify it with `kappa_E` by notation.

Required artifact:

`R059D_STAGE_AM_CIRCUMFERENCE_NONISOMETRY_THEOREM.json`.

## Stage E — realization separation theorem

Prove the bridge is not a mere coordinate reparameterization/isometry of one circle geometry.

Strong target:

`ORTHOGONAL_CONTINUOUS_CIRCLE_AND_ENTERPRISE_NATIVE_CIRCLE_ARE_DISTINCT_REALIZATIONS_CONNECTED_BY_NONISOMETRIC_BRC_COLLAPSE`.

Sufficient ingredients:

- continuous/many-state source versus finite target orbit at fixed radius;
- nontrivial BRC fibers;
- target circumference defined by turn period rather than source arc integration;
- source metric failing to descend as target metric;
- target canonicality independently established by AL.

This theorem is a realization/semantic separation statement. It is stronger than saying the coordinate triples look different.

Required artifact:

`R059D_STAGE_AM_REALIZATION_SEPARATION_THEOREM.json`.

## Stage F — typed source-constant compatibility audit

Only after the non-isometry theorem is frozen, audit the classical source-side circumference constant as a typed compatibility fact.

Allowed:

- introduce `kappa_perp` as the source circumference/diameter constant under the source orthogonal continuous realization;
- record standard source mathematics in a clearly source-typed section if needed;
- derive the conditional statement that any hypothetical BRC isometry would force `kappa_perp=kappa_E`.

Do not use a classical source theorem to define, tune, or reject the already canonical Enterprise target orbit.

Do not promote a statement about standard real `pi` beyond what is actually proved in this stage.

Required artifact:

`R059D_STAGE_AM_SOURCE_CONSTANT_TYPED_AUDIT.json`.

## Stage G — deterministic replay / visualization data

After theorem definitions freeze, produce deterministic validation across representative radii.

Minimum:

- `r=1..256` full bridge/fiber replay where computationally feasible;
- checkpoints `512,1024,4096`;
- D6 equivariance and cyclic order;
- surjectivity / coverage of source-state samples;
- tie consistency;
- source-fiber width diagnostics;
- at least one exact symbolic or rational nonuniformity witness if Stage C proves nonuniform fibers;
- no theorem change after replay.

Finite sampling of a continuous source circle is implementation evidence only and cannot substitute for fiber/metric proofs.

## Required artifacts

- `R059D_STAGE_AM_TYPED_SOURCE_TARGET_PROTOCOL.json`
- `R059D_STAGE_AM_CANONICAL_BRC_CIRCLE_BRIDGE.json`
- `R059D_STAGE_AM_BRC_FIBER_THEOREM.json`
- `R059D_STAGE_AM_SOURCE_ARC_DESCENT_AUDIT.json`
- `R059D_STAGE_AM_CIRCUMFERENCE_NONISOMETRY_THEOREM.json`
- `R059D_STAGE_AM_REALIZATION_SEPARATION_THEOREM.json`
- `R059D_STAGE_AM_SOURCE_CONSTANT_TYPED_AUDIT.json`
- `R059D_STAGE_AM_PROOF.md`
- `R059D_STAGE_AM_DETERMINISTIC_CHECKER_OUTPUT.json`
- `R059D_STAGE_AM_FROZEN_CHECKPOINT.json`
- `R059D_STAGE_AM_REPORT.md`

## Mandatory semantic firewalls

Target canonicality is already solved by AL. Therefore forbidden:

- using the source circle to choose the target boundary;
- redefining target length as source/Euclidean distance;
- retuning N or C_s from source arc error;
- assuming BRC is isometric because both sides are called circles;
- assuming source circumference equals target period;
- using standard pi numerics as a target-selection signal;
- silently collapsing source and target constants into one symbol.

The source may remain classical/orthogonal. The target must remain Enterprise-native.

## Research discipline

Internal working truth:

`CANONICAL_BRC_IS_A_NONISOMETRIC_COLLAPSE_BETWEEN_DISTINCT_CIRCLE_REALIZATIONS`.

Attack the proof mechanism, not the direction. Only an exact counterexample, formal contradiction, frozen checker failure or Driver/user supersession may replace the direction.

## Dispositions

Use the strongest justified terminal status:

1. `CANONICAL_BRC_CIRCLE_COLLAPSE_ESTABLISHED__SOURCE_ARC_METRIC_NONDESCENT_PROVED__DISTINCT_REALIZATIONS`
2. `CANONICAL_BRC_CIRCLE_COLLAPSE_ESTABLISHED__GLOBAL_NONISOMETRY_PROVED__LOCAL_ARC_NONDESCENT_OPEN`
3. `CANONICAL_BRC_SURJECTIVE_FIBER_THEOREM_PROVED__METRIC_SEPARATION_OPEN`
4. `CANONICAL_BRC_RELATION_ESTABLISHED__FIBER_GEOMETRY_OPEN`
5. `CANONICAL_BRC_FUNCTION_BLOCKED__RELATIONAL_BRIDGE_ONLY`
6. `BRC_REALIZATION_SEPARATION_BLOCKED__EXACT_COUNTEREXAMPLE`

Do not stop at a weaker disposition while a stronger proof route remains live.

`STOP_FOR_DRIVER_REVIEW` only after source/target typing, bridge, fibers and metric-descent status are all frozen.
