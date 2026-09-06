# X6 upper integration V2: corrected relational bundles, common A6 base and observer-safe state reduction

Status: `FREE_RESEARCH / EXACT SYNTHESIS + FINITE HOMOGENEOUS-SPACE CHECK / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Task: `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_UPPER_TYPED_EVENT_INTEGRATION_V1_20260906.md`;
- `X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`;
- `X6_FRAME_CHANNEL_DIAGONAL_COUPLING_V4_20260906.md`;
- `X6_ORIENTATION_PRESERVING_CHART_A6_UNIFICATION_V3_20260906.md`;
- `X6_NONFCC_FCC_LATTICE_BASIS_DECODER_V5_20260906.md`.
Checker: `experiments/x6_upper_bundle_integration_v2_20260906/check_upper_bundle_integration.py`.

## 1. Purpose

V1 established that the upper theory is not one giant coordinate vector. It is a typed combination of spatial state, relation/internal state, events with concrete provenance, and observer/context data.

Since V1, several exact structures have converged:

- triadic frame group `R_triad=(C2)^6 semidirect A6`;
- corrected signed internal Q dynamics with a four-twist gauge bundle;
- unsigned channel C3 dynamics and frame/channel projection to `A6`;
- orientation-preserving all-20 chart transport in the same `A6`;
- exact non-FCC carrier decoders.

V2 removes redundant fields and gives the resulting bundle hierarchy.

## 2. Common orientation-preserving relational base

There are three distinct semantic objects with one common finite group action:

1. positive-axis part of the triadic frame update;
2. unsigned channel circulation;
3. orientation-preserving all-20 chart transport.

Their common group is

`A6`.

This does not identify the three object types. It means they can be transported by one common orientation-preserving frame law when a coupling declares them aligned.

The exact frame sequence is

`1 -> (C2)^6 -> R_triad -> A6 -> 1`.

Thus the signed frame contains a 64-fold sign kernel invisible to unsigned channel/chart action.

## 3. Oriented channel passage and oriented three-axis chart are equivariantly isomorphic

An unsigned directed triadic passage on axes `{i,j,k}` is a directed 3-cycle

`i -> j -> k -> i`.

A cyclically oriented three-axis chart is exactly the same combinatorial datum: a 3-subset plus one of its two cyclic orientations.

Both sets have 40 elements.

Under the native axis relabeling action of `A6`, the identity map on the directed 3-cycle data is an `A6`-equivariant bijection

`ORIENTED_CHART_40 ~= DIRECTED_PASSAGE_40`.

Their common stabilizer has order

`360/40=9`.

Semantic guard: they remain different types. The bijection becomes a redundancy-removal rule only inside a declared coupling where the active triadic passage is also the local oriented chart used by the event.

If an observer chart is chosen independently of the active triad, both fields remain necessary.

## 4. Related homogeneous spaces

The same `A6` action gives:

- selected unoriented three-axis set: 20 states, stabilizer 18;
- cyclically oriented chart/passage: 40 states, stabilizer 9;
- fully ordered visible axis slots: 120 states, stabilizer 3.

These are exactly the 18/9/3 normalization fibers from the non-FCC carrier theorem viewed in homogeneous-space form.

So the carrier-normalization ambiguity and the channel/chart group action are two readings of the same `A6` stabilizer structure.

## 5. Corrected signed internal base: 40 passages x 4 twists

For a full ordered signed triad frame

`F=((i0,i1,i2),(s0,s1,s2))`,

define its directed unsigned passage `P(F)` and relative-sign/twist coordinate

`alpha(F)=(-s0*s1,-s1*s2,-s2*s0)`.

The product of the three alpha entries is `-1`, so exactly four twist values occur.

The map from eight absolute sign assignments to four twists has kernel

`(s0,s1,s2) ~ (-s0,-s1,-s2)`.

Thus the twist is the relative signed relation

`(C2)^3 / C2_diagonal ~= (C2)^2`

written as the affine four-state product-`-1` set.

The static corrected signed sector space therefore has

`40*4=160`

states:

`SIGNED_STATIC_SECTOR_160 = ORIENTED_PASSAGE_40 x TWIST_4`

at the level of exact cardinality and the chosen phase-coordinate convention.

## 6. C6 is a phase torsor above the 160 static sectors

The corrected canonical internal update `R_can` leaves both the directed passage and the relative twist sector invariant while cycling through six full ordered signed frames.

Every one of the 160 sectors has exactly six full frames above it, and those six frames form one exact C6 orbit.

Hence the 960 full signed frames are best typed as a disjoint union of 160 C6 phase torsors:

`FRAME_960 -> SECTOR_160`,

fiber `C6`.

There is no need to interpret the six phase labels as six new coordinates. They are positions along the local relation-update orbit.

The old sign-coherent examples occupy one particular twist sector; V5 proves the other three sectors are equally required for general signed-frame covariance.

## 7. SHELL/CLOSURE doubles the phase to C12

Add the relation-stage bit `SHELL/CLOSURE` and the update

`U(SHELL,F)=(CLOSURE,F)`,

`U(CLOSURE,F)=(SHELL,R_can(F))`.

Every static sector now has exactly twelve decorated states and they form one C12 orbit.

Thus:

`DECORATED_INTERNAL_1920 -> SECTOR_160`

has exact C12 fibers.

This recovers the earlier 1920-state count with a sharper structure:

`1920 = 40 directed passages * 4 relative-sign sectors * 12 relation phases`.

Again this is a finite relation bundle over a pivot Cell, not extra spatial dimension.

## 8. Channel state is a quotient, not an independent duplicate

Under the minimal frame/channel coupling, the unsigned channel update is

`pi(g)`

for signed frame event `g in R_triad`.

For one local triadic event this is exactly the directed passage C3 generator.

Therefore, if the full signed frame event and one global axis-channel gauge are already retained, the unsigned channel permutation need not be stored separately for future operations restricted to that minimal coupling.

The reverse is unsafe: channel state loses the 64-fold global sign kernel and, locally, the four twist sectors and C6 phase.

If a physical model introduces additional channel-specific couplings not factoring through `pi`, channel state becomes an independent internal field again.

## 9. Chart state is conditionally redundant, not universally redundant

For a triadic event whose active oriented axes define the local observation chart, the oriented chart is already determined by its directed passage.

But the general observer chart used to inspect a subsystem may be chosen independently from the currently active triad. Therefore the architecture distinguishes:

- `ACTIVE_EVENT_CHART`: derivable from the event passage under the local coupling;
- `OBSERVER_CHART_CONTEXT`: independently chosen readout state when applicable.

Only the first is removable by the 40-state equivariant bijection.

## 10. Carrier observer choice after the non-FCC theorem

For a known centered three-axis native slice there are now two main carrier readout routes.

### Rank-3 direct FCC decoder

For FACE/PATH charts, use the fixed global FCC carrier basis. This is an exact integer isomorphism

`Z^3 -> L_FCC`

with parity decoder and no loss of the selected raw coordinates.

### A6-normalized STAR observer

For any chart, transport its frame to a STAR chart and use the existing planar triangle/circle/gate carrier semantics.

This introduces an 18/9/3 frame-normalization fiber depending on how much local orientation/slot information is fixed and can carry chart holonomy.

These are different observers. The upper state does not select one without an application/future-operation requirement.

## 11. Corrected master information hierarchy

For the current upper program, a safe generic hierarchy is:

`RAW EVENT / PATH-FORMAL + DEPENDENCY ORDER`

`-> SIGNED FRAME EVENT in R_triad + INTERNAL RELATION STATE`

`-> A6 POSITIVE/UNSIGNED RELATIONAL ACTION`

`-> {directed passage, active chart, channel permutation} under declared couplings`

`-> selected carrier observer / PF10 positive traffic / Boolean support`.

Every downward arrow is scope typed.

The corrected local triadic internal hierarchy is:

`decorated full frame 1920`

`-> full frame 960`

`-> signed static sector 160`

`-> directed unsigned passage 40`

`-> active unsigned set 20`.

The exact lost fibers are respectively:

- relation stage `C2` when 1920 -> 960;
- C6 phase when 960 -> 160;
- twist `C2^2` when 160 -> 40;
- chirality/orientation `C2` when 40 -> 20.

These fiber labels state what information is lost; they are not automatically independent physical variables.

## 12. Time remains on events, not in the spatial/internal fiber

The C12 internal phase is a local periodic quotient of relation-update order. It is not full time.

Actual native time remains the dependency/order structure of upper events:

`RAW EVENT WORD -> CERTIFIED DEPENDENCY TRACE/PARTIAL ORDER -> optional scalar linearization`.

Two independent events may be unordered in the native dependency trace even though an external scalar timestamp chooses one serialization.

Conversely, repeated full C12 cycles return to the same local decorated state but represent additional elapsed event history. So neither internal C12 phase nor current state replaces event-time provenance.

## 13. Path provenance remains strictly above all finite frame/internal quotients

Generic rotation retains concrete path/BRC provenance. Frame closure, internal phase and endpoint state do not determine it.

A full triadic frame cycle has 64 distinct shortest microtrace histories with identical final frame/Cell. The atomic triadic force law selects `III` only on its restricted correlated interaction interface; it does not erase generic rotation-path multiplicity globally.

Thus no finite state bundle in this note is claimed to replace unrestricted Path-formal identity.

## 14. Orientation superselection under current triadic/A6 dynamics

All current positive-axis triadic, unsigned-channel and orientation-preserving chart generators lie in `A6`.

Therefore the global orientation coset

`Ori_6 = S6/A6 ~= C2`

is invariant under the present coupled upper dynamics.

The two `Ori_6` sectors are disconnected by all currently admitted orientation-preserving triadic/channel/chart updates.

This is a **current-generator superselection theorem**, not a P000 axiom that orientation-changing native events can never exist. Such an event would require an additional admissible odd positive-axis generator/law.

## 15. What is now actually minimal

There is no one observer-independent minimal state. Minimality is future-language dependent.

Examples:

- unsigned active-port support only: 20-state relation observer;
- local channel circulation / oriented active chart: 40-state observer;
- signed relative interaction sector with phase ignored: 160 states;
- exact deterministic triadic next-state prediction including phase/stage: 1920 local states over the pivot Cell;
- generic exact path-history query: no fixed finite internal quotient suffices; retain Path-formal history or a horizon-proved adequate observer.

This is the strongest operation-safe notion of “minimal upper state” supported by the current program.

## 16. Current integration frontier

The upper structure has now converged to a typed bundle/category architecture:

- **space**: affine X6 Cell torsor;
- **frame**: signed triadic group with exact sequence to A6;
- **internal**: 160 static signed sectors with C6/C12 phase fibers;
- **channel**: A6/C3 readout under minimal coupling, otherwise optional independent field;
- **chart/carrier**: A6 observer transport plus STAR/FACE/PATH carrier choices;
- **time**: dependency trace of events;
- **provenance**: Path/BRC event layer above all finite quotients;
- **precision/root lineage**: separate observer/refinement context.

Remaining work is increasingly law/calibration specific:

1. unequal force quanta and interacting multi-Cell triadic networks;
2. physical rule for generic rotation path weights/sections;
3. channel exchange or sign-sensitive channel coupling beyond minimal `pi` projection;
4. duration/energy calibration of event layers;
5. application-specific quotients for PDE/number-theory/physical models;
6. admissibility and meaning of an orientation-sector-changing native event.

No Foundation promotion or external novelty claim is made.
