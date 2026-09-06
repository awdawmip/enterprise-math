# X6 Cell/channel internal state V1: triadic port fiber, channel-frame torsor and observer hierarchy

Status: `FREE_RESEARCH / EXACT FINITE STRUCTURE / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Depends on:
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`;
- `PACKET_PATH_FOUNDATION.md` PF-10;
- `research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- `research_notes/X6_TRIADIC_ATOMIC_SCATTER_V1_20260906.md`;
- `research_notes/X6_NATIVE_EVENT_TIME_V1_20260906.md`.
Checker: `experiments/x6_cell_internal_state_v1_20260906/check_cell_internal_state.py`.

## 1. Scope

The spatial Cell-center identity is already

`X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`.

This note does not add a seventh spatial coordinate. It constructs the first finite **relational interaction fiber over one pivot Cell** required by triadic closure/rotation/time dynamics.

A state in the fiber is not a replacement for Path-formal history. It is a scoped Markov state for the declared triadic interaction interface.

## 2. Channel labels are not axis labels by cardinality

PF-10 admits six abstract channel labels

`C={c0,...,c5}`

with ingress/egress/passage counts `I,O,M`. P000 separately supplies six native unsigned spatial axis labels

`A={E1,...,E6}`.

No current axiom canonically identifies these two six-element sets.

Define an axis-channel frame to be a bijection

`phi:C -> A`.

There are

`6! = 720`

such frames. Under independent relabeling of channels and axes the frame transforms by

`phi -> g_A o phi o g_C^-1`.

Therefore the collection of frames is a torsor/gauge interface, not 720 new physical states. A chosen `phi` is a calibration/readout frame. Current Foundation does not select one distinguished `phi`.

Freeze research boundary:

`CHANNEL_COUNT=6 AND AXIS_COUNT=6 != CANONICAL_CHANNEL_AXIS_IDENTIFICATION`.

## 3. Full ordered signed triad port frame

Let

`F=((i0,i1,i2),(s0,s1,s2))`

where `i0,i1,i2` are distinct native axis labels and each `sr in {+1,-1}`. It represents three labeled signed force/port tokens

`dr=sr E_ir`.

The number of such frames is

`6*5*4*2^3 = 960`.

For the oriented triad `(i0,i1,i2)`, the current native generator acts tokenwise by

`Q(E_i0)=-E_i1`,
`Q(E_i1)=-E_i2`,
`Q(E_i2)=-E_i0`.

Hence the correct frame update is

`R((i0,i1,i2),(s0,s1,s2))`

`=((i1,i2,i0),(-s0,-s1,-s2))`.

Important correction: for arbitrary sign patterns this is **not** the same as naively replacing the token tuple by `(-d1,-d2,-d0)`. The latter agrees only on restricted sign-coherent cases and must not be used globally.

Exact laws:

`R^2((i0,i1,i2),s)=((i2,i0,i1),s)`,

`R^3(F)=-F` on all three signed tokens,

`R^6(F)=F`.

No frame has smaller positive period, so the 960 frames split into exactly

`960/6 = 160`

C6 orbits.

## 4. Relation-stage lift gives 160 exact C12 internal cycles

Introduce a relation-stage bit

`b in {Theta,Kappa}`,

where `Theta` is the shell/port relation layer of a triadic interaction rooted at pivot Cell `x`, and `Kappa` is the atomic common-Cell closure layer selected by `TRIADIC_CLOSURE_E`.

Define

`U(Theta,F)=(Kappa,F)`,

`U(Kappa,F)=(Theta,R(F))`.

Then

`U^2=R`,

and every decorated state has exact period 12. Thus the local interaction fiber has

`2*960=1920`

states split into exactly 160 C12 cycles.

Define the current scoped decorated pivot object

`TRIADIC_CELL_FIBER(x) := {x} x FRAME_960 x {Theta,Kappa}`.

It is a relational decoration rooted at `x`, not a new spatial direction and not the complete packet-history state.

## 5. Exact observer hierarchy

The 960 frame states admit several strictly typed observers.

### 5.1 Active unsigned port set

Forget signs, cyclic orientation and phase origin. The active axis/channel subset has

`C(6,3)=20`

values.

Under one triadic update the same three unsigned axes remain active, so this is an operation-safe observer **only for future operations that ask solely which three unsigned ports are active**.

### 5.2 Directed passage support

Retain the oriented three-cycle

`i0 -> i1 -> i2 -> i0`.

There are two orientations for each 3-subset, hence

`20*2=40`

possible directed passage supports. One `R` update cyclically changes the phase origin but leaves this passage support invariant.

With a chosen channel frame `phi`, this gives a PF-10 passage support

`M[phi^-1(i0),phi^-1(i1)] = 1`,

`M[phi^-1(i1),phi^-1(i2)] = 1`,

`M[phi^-1(i2),phi^-1(i0)] = 1`,

with the other entries zero for the one-quantum idealized event. `I` and `O` each have unit support on the same three channels.

This positive-count readout still does not encode spatial signs or C3 phase.

### 5.3 Oriented signed cycle, phase origin forgotten

Retain directed passage support plus the sign attached to every source axis. There are

`40*2^3 = 320`

such states.

Equivalently this is the quotient of the 960 full frames by simultaneous cyclic relabeling of the three token slots. The triadic update `R` descends exactly to these 320 states.

Hence

`960 -> 320`

forgets a 3-element phase-origin fiber.

The missing repair is exactly a `C3` phase pointer when exact C6 phase is required.

### 5.4 Unordered signed triad is generally not Markov safe

If cyclic orientation is also erased, there are only

`20*2^3=160`

unordered signed triads.

Exhaustive checking gives:

- 40 unordered signed states have one possible next unordered state;
- 120 have **two** possible next unordered states, depending on the erased cyclic orientation.

Therefore the quotient from 320 oriented signed cycles to 160 unordered signed triads is not predictive/operation-safe for general signed-triad evolution.

A cyclic-orientation bit repairs this defect.

## 6. Factorization of the finite interaction fiber

At the level of cardinalities and typed observers:

`20 active 3-subsets`

`x 2 cyclic orientations`

`x 2^3 signed port assignments`

`x 3 phase origins`

`x 2 relation stages`

`= 1920`.

Thus one convenient typed factorization is

`TRIADIC_INTERNAL ~= PORT_SUBSET_20 x CHIRALITY_2 x SIGN_8 x PHASE_C3 x STAGE_C2`.

This is a finite relation fiber above a pivot Cell. None of these factors is a new spatial dimension.

## 7. Relation to the previous time-memory lower bound

The preceding time result proved that on one fixed sign-coherent triad orbit, six distinct closure phases share the same pivot Cell but have six distinct deterministic next shell relations.

The present fiber generalizes that observation. At the closure layer, a bare spatial Cell coordinate does not contain the active port subset, cyclic orientation, signs or phase origin. Any future operation that requests those distinctions must retain the corresponding repair coordinates.

Therefore

`SPATIAL_CELL -> INTERNAL_STATE`

is genuinely a fibration/decoration problem, not an omitted seventh spatial coordinate.

## 8. BRC and observer-preservation consequence

This finite hierarchy gives explicit safe and unsafe collapses.

Safe examples under their exact leases:

- full frame -> active port subset, if future operations only ask unsigned active-port support;
- full frame -> directed passage support, if future operations only ask PF-10 unsigned passage support;
- full frame -> 320 oriented signed cycles, if exact phase origin is irrelevant but signed cyclic dynamics remains relevant.

Unsafe examples for stronger futures:

- positive `I/O/M` counts cannot reconstruct sign assignment or phase origin;
- unordered signed triad generally cannot determine its own next unordered signed triad;
- Boolean/total support cannot reconstruct Path-formal branch provenance.

This is a direct application of the existing BRC and Operation-Safe Quotient discipline; no new general-purpose quotient tool is introduced.

## 9. Recurrent port elimination boundary

The current exact recurrent Weighted-BRC port tool Schur-eliminates a **stable** hidden block. A unit-weight deterministic C12 internal cycle is recurrent with eigenvalue 1 and is not such a stable hidden block.

Therefore the present triadic phase cycle cannot be silently removed by the stable recurrent-port signature machinery. An attenuation/escape law or a narrower observer lease would be additional structure.

For observers that merely ask the invariant unsigned passage support, the direct finite operation-safe quotient above is already sufficient and does not require a Schur elimination.

## 10. Rotation covariance

For an unsigned axis relabeling `g in S6`, act on a frame by

`g.F=((g(i0),g(i1),g(i2)),(s0,s1,s2))`.

Then

`R(g.F)=g.R(F)`

when the oriented triad generator is relabeled with the same frame. A chosen axis-channel bridge transports as `phi -> g o phi`, preserving the PF-10 port representation.

Thus the internal fiber is compatible with the current X6 finite frame symmetry; it does not select a preferred global axis/channel labeling.

## 11. Current closure and next gate

Closed at this research stage:

- exact 720-element channel-axis frame torsor;
- 960 full ordered signed triad port frames;
- 160 exact C6 frame orbits;
- 1920 stage-decorated states forming 160 C12 cycles;
- exact 20 -> 40 -> 320 -> 960 -> 1920 observer/repair hierarchy;
- explicit 120-state Markov obstruction after erasing cyclic orientation;
- typed PF-10 `I/O/M` bridge after choosing an axis-channel frame;
- stable recurrent-port elimination boundary.

Still open:

1. decide whether an axis-channel frame is dynamically carried, locally calibrated or only observer-side;
2. include non-unit multiplicities/weights and larger triadic networks;
3. couple multiple interacting pivot fibers through the event-dependency time poset;
4. identify which internal variables survive in application-specific PDE/prime/physical readouts;
5. determine whether a smaller internal state is sufficient under a specifically declared law-selection horizon.

No Foundation promotion or external novelty claim is made.
