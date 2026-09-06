# X6 Cell internal state V1: triadic port frames, channel-frame torsor, and PF-10 information-loss hierarchy

Status: `FREE_RESEARCH / EXACT FINITE DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Consumes:
- `X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`;
- PF-10 ideal six-channel ingress/egress/passage counts;
- `X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md`;
- `X6_NATIVE_EVENT_TIME_AND_MARKOV_MEMORY_V1_20260906.md`;
- existing BRC recurrent-port collapse interface.

Method reuse:
- T0 BRC for occurrence/provenance layers;
- T7 finite symmetry for channel-frame canonical-choice audit;
- T6 operation-safe quotient for PF-10 projections;
- existing `recurrent_port_signature` only for positive-rational hidden channel blocks satisfying its stability/context hypotheses.

## 1. Spatial Cell versus internal fiber

A native spatial Cell is still one point of the X6 affine torsor. Internal relation state is a separate fiber over that Cell.

For a Cell `c`, write schematically

`DECORATED_STATE_c = SPATIAL_CELL_c x INTERNAL_c`.

No internal coordinate introduced below is a seventh spatial axis.

## 2. Full ordered signed triadic port frame

Let

`D6_signed={+e_1,-e_1,...,+e_6,-e_6}`.

Define a triadic port frame

`tau=(d_0,d_1,d_2)`

where the three signed directions have distinct underlying native-axis labels. Tuple position retains force-token/provenance identity.

The number of such frames is

`6*5*4*2^3 = 960`.

Define the intrinsic triadic update

`R(d_0,d_1,d_2)=(-d_1,-d_2,-d_0)`.

Then exactly

`R^2(tau)=(d_2,d_0,d_1)`,

`R^3(tau)=(-d_0,-d_1,-d_2)`,

`R^6(tau)=tau`.

Because the underlying axes are distinct and the directions are nonzero, every orbit has exact size six. Hence the 960 frames split into

`960/6 = 160`

triadic C6 orbits.

This recovers the `20 three-axis selections * 8 sign patterns = 160` static signed-triad cases after the appropriate provenance quotient.

## 3. Full local deterministic triadic Cell fiber

Add the interaction mode

`p in {SHELL,CLOSURE}`.

Define the local successor

`F(tau,SHELL)=(tau,CLOSURE)`,

`F(tau,CLOSURE)=(R tau,SHELL)`.

Then `F^12=1`, and every state has exact period twelve. Therefore the full equal-unit ordered triadic internal carrier has

`960*2 = 1920`

states, partitioned into 160 disjoint C12 cycles.

This finite fiber is sufficient for the deterministic equal-unit atomic-scatter law with exact token/port correspondence. It is not claimed to be the universal minimum for every observer or for unequal-quantum/internal-field dynamics.

## 4. Signed-frame equivariance

Any signed native-axis frame symmetry acts componentwise on `tau`. Because signed frame maps satisfy `g(-d)=-g(d)`, one has

`g R(tau)=R(g tau)`.

Thus the local port-frame dynamics is equivariant under the full signed coordinate-frame symmetry, not only one chosen FCC chart.

This is an internal relation statement over X6; it does not promote the full signed frame group to the complete physical rotation dynamics.

## 5. Six PF-10 channels are not automatically the six X6 axes

PF-10 supplies an abstract six-channel set `C={0,...,5}`. X6 supplies six native axis labels `A={E_1,...,E_6}`.

Equal cardinality does not define an identification.

An axis-channel bridge is a bijection

`beta:C -> A`.

There are exactly

`6! = 720`

such bridges. Under axis relabeling they form a torsor; no one bridge is fixed by the full axis-label symmetry. Therefore no canonical `channel_i = E_i` assignment follows from the number six alone.

A concrete channel/axis coupling model must carry or derive an `AXIS_CHANNEL_FRAME` datum. This is a T7 canonical-choice obstruction.

## 6. PF-10 instantaneous readout after choosing a bridge

Assume one axis-channel frame `beta` has been supplied. Map each signed port to its unsigned channel by forgetting sign after applying `beta^{-1}`.

For `tau=(d_0,d_1,d_2)`, define the instantaneous PF-10-style readouts:

- ingress support `I_tau`: one occurrence on each of the three used channels;
- egress support `O_tau`: the same three channels;
- directed passage relation `P_tau`: the three channel transitions
  `axis(d_0)->axis(d_1)`,
  `axis(d_1)->axis(d_2)`,
  `axis(d_2)->axis(d_0)`.

Thus `P_tau` is an oriented 3-cycle on three of the six channels.

### Exact fiber sizes

There are only `C(6,3)=20` possible I/O supports. Each I/O support has

`960/20 = 48`

full triadic port frames above it.

There are

`C(6,3)*2 = 40`

possible oriented 3-cycle passage relations. Each has exactly

`960/40 = 24 = 3*2^3`

full frames above it.

The natural hidden factors are:

- three cyclic choices of token-origin/matching phase;
- three independent signed-port bits.

Therefore even an instantaneous directed PF-10 passage matrix is not a full triadic internal state when signed force phase or token provenance remains observable.

## 7. PF-10 cumulative counts are not a Markov state for rotation

PF-10 `I,O,M` are cumulative counts. Addition makes their totals insensitive to event order.

Take two different active triad passage orientations `A` and `B` on the same three unsigned channels. Histories

`H_1=A;B`

and

`H_2=B;A`

have identical cumulative `I`, `O`, and `M=P_A+P_B`.

But their active last passage states differ. A future operation “continue the currently active triadic rotation” advances from `B` in `H_1` and from `A` in `H_2`, producing different next passage relations.

Hence

`CUMULATIVE_PF10_COUNTS != MARKOV_COMPLETE_INTERNAL_STATE`

for rotation/time observers.

At minimum the active relation/phase must be retained in addition to aggregate traffic counts whenever future operations inspect or continue it.

## 8. Scope-typed minimal-state hierarchy

For the present equal-unit triadic sector:

- unsigned active channel support only: 20 states;
- unsigned directed passage orientation: 40 states;
- full ordered signed triad frame: 960 states;
- full deterministic shell/closure triadic state: 1920 states.

These are not competing ontologies. They are a quotient hierarchy for different observer/future-operation languages.

Dropping from a finer layer to a coarser layer requires a T6 operation-safety certificate.

## 9. Positive port collapse versus signed/internal phase

The existing `recurrent_port_signature` tool Schur-eliminates a stable hidden **nonnegative rational** recurrent block and returns an effective boundary matrix, with optional hidden loop-zeta data for observers that require it.

It is reusable for PF-10-like positive channel-mass dynamics when:

- hidden dynamics is stable in the declared sense;
- all allowed contexts interact only through the retained ports;
- the observer asks only for the declared positive-rational boundary semantics (plus zeta when requested).

It is not a valid way to erase:

- signed force-port bits;
- C3 token/matching phase;
- Path-formal branch history;
- time/event ordering;
- any hidden state directly queried by future operations.

Thus a safe decorated model keeps positive channel mass and signed/provenance relation state as separately typed factors until a stronger theorem couples or quotients them.

## 10. Current internal-state contract

The smallest reusable template supported by the current results is

`INTERNAL_c = (POSITIVE_CHANNEL_TRAFFIC, ACTIVE_RELATION_STATE, PROVENANCE_MEMORY)`.

For the deterministic equal-unit triadic law, `ACTIVE_RELATION_STATE` may be represented exactly by `(tau,mode)` and the atomic branch itself is derived as `III`, so that branch bit need not be stored **inside that law scope**.

For generic rotation paths, branch/path provenance remains separate and may be unbounded under unrestricted future-history observers.

## 11. Current frontier

Closed here:

- exact finite triadic port-frame carrier and C6 action;
- exact 1920-state shell/closure decorated fiber for the restricted law;
- full signed-frame equivariance;
- 720-fold axis-channel bridge torsor and no-canonical-identification result;
- exact PF-10 readout fiber sizes 48 and 24;
- cumulative-count Markov obstruction;
- precise boundary for reuse of positive recurrent-port collapse.

Still open:

1. derive a physical/native axis-channel bridge instead of choosing a frame;
2. unequal-quantum and multi-triad concurrent internal states;
3. channel state exchange between neighboring Cells;
4. signed/phase interaction laws beyond positive channel mass;
5. duration/energy/physical calibration of internal transitions.
