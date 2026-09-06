# X6 Cell internal state V1R: corrected triadic port frames and PF-10 information-loss hierarchy

Status: `FREE_RESEARCH / EXACT FINITE DERIVATION / CORRECTED 2026-09-06 / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Correction authority: `X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`.

## 1. Spatial Cell versus internal fiber

A native spatial Cell is one point of the signed X6 affine torsor. Internal relation state is a separate fiber over that Cell:

`DECORATED_STATE_c = SPATIAL_CELL_c x INTERNAL_c`.

No internal coordinate below is a seventh spatial axis.

## 2. Full ordered signed triadic port frame

Represent a triadic port frame as

`F=((i0,i1,i2),(s0,s1,s2))`,

where `i0,i1,i2` are distinct native axis labels, the tuple positions retain force-token/provenance identity, and `sr in {+1,-1}`.

There are

`6*5*4*2^3 = 960`

full frames.

For the canonical oriented triadic generator `Q_S=J_S rho_S`,

`Q_S(E_i0)=-E_i1`,
`Q_S(E_i1)=-E_i2`,
`Q_S(E_i2)=-E_i0`.

Therefore the correct tokenwise frame update is

`R_can((i0,i1,i2),(s0,s1,s2))`

`=((i1,i2,i0),(-s0,-s1,-s2))`.

The superseded shorthand `R(d0,d1,d2)=(-d1,-d2,-d0)` is valid only on restricted sign-coherent examples and must not be used for arbitrary signed frames.

Exact laws:

`R_can^2`: axes shift twice and token signs return;

`R_can^3`: the same ordered axes with all three token signs reversed;

`R_can^6=1`.

Every frame has exact period six, so the 960 frames form 160 C6 orbits.

## 3. Full local deterministic triadic Cell fiber

Add relation mode

`p in {SHELL,CLOSURE}`

and define

`F(FRAME,SHELL)=(FRAME,CLOSURE)`,

`F(FRAME,CLOSURE)=(R_can(FRAME),SHELL)`.

Then every state has exact period twelve. The restricted equal-unit internal carrier therefore has

`960*2=1920`

states in 160 C12 cycles.

This is sufficient for the declared deterministic equal-unit atomic-scatter interface. It is not a universal finite summary of unrestricted Path-formal history.

## 4. Correct symmetry statement

The canonical `Q_S=-rho_S` family is covariant under **unsigned axis relabeling**: relabel the oriented axes and the same canonical construction results.

The earlier statement that one fixed canonical representative satisfies naive equivariance under every independent axis sign flip was too strong.

Under an independent sign-frame change the generator is conjugated to a general signed 3-cycle

`Q_{S,alpha}(E_i_r)=alpha_r E_i_{r+1}`

with

`alpha_0 alpha_1 alpha_2=-1`.

There are four such twist patterns. They form one sign-gauge orbit, and the full four-twist family is the object closed under signed-frame gauge covariance. See V5 for the exact transport law.

This correction does not enlarge the established frame group `(C2)^6 semidirect A6`.

## 5. Six PF-10 channels are not automatically the six X6 axes

PF-10 supplies an abstract six-channel set `C`; X6 supplies six native unsigned axes `A`. Equal cardinality does not define an identification.

An axis-channel bridge is a bijection

`beta:C -> A`,

with `6!=720` possible choices. Current V2 work further shows that under full translation symmetry and channel-relabeling equivariance these choices form one global gauge torsor rather than 720 physical states at every Cell.

## 6. PF-10 instantaneous readout

After choosing one bridge `beta`, forget spatial sign only for the PF-10 positive-count readout.

For an ordered frame on axes `(i0,i1,i2)`:

- ingress/egress support uses the three selected channels;
- directed passage support is the oriented cycle
  `i0 -> i1 -> i2 -> i0`.

Exact fiber sizes remain:

- 20 unsigned I/O support states, each with 48 full signed frames;
- 40 directed unsigned passage states, each with 24 full signed frames.

The 24 hidden states above one directed passage consist of three phase-origin choices and eight signed-port patterns.

The corrected tokenwise `R_can` still changes the unsigned axis tuple only by cyclic reindexing, so the directed unsigned passage is invariant along one internal C6 orbit.

## 7. Four signed C6 sectors over each directed passage

Each of the 40 directed unsigned passages has 24 full signed frames. Under corrected `R_can` those 24 frames split into exactly four C6 orbits.

For one phase-origin representative define

`alpha_state=(-s0*s1,-s1*s2,-s2*s0)`.

Its product is `-1`; the four possible values are exactly the four signed-generator twist patterns from V5. Thus the signed internal phase has a four-state relative-sign/twist sector invisible to PF-10 unsigned passage.

## 8. Cumulative PF-10 counts are not Markov complete

PF-10 `I,O,M` are cumulative positive counts. Histories using two opposite passage orientations in opposite orders can have identical cumulative counts while retaining different active last-passage state.

Therefore

`CUMULATIVE_PF10_COUNTS != MARKOV_COMPLETE_INTERNAL_STATE`

for observers that continue the active rotation/triadic process.

At minimum the active relation state must remain when future operations inspect it.

## 9. Scope-typed observer hierarchy

For the current equal-unit triadic sector:

- unsigned active channel support: 20 states;
- unsigned directed passage orientation: 40 states;
- phase-origin-free oriented signed passage: 320 states;
- full ordered signed frame: 960 states;
- full SHELL/CLOSURE state: 1920 states.

The quotient `960 -> 320` forgets a three-element phase-origin fiber and is operation-safe for the corrected signed-cycle successor at that observer strength.

If cyclic orientation is also erased, the 160 unordered signed triads are generally not Markov safe: 120 of the 160 have two possible next unordered states depending on the erased cyclic orientation.

Each downward projection therefore requires the existing operation-safe quotient/observer lease.

## 10. Positive port collapse versus signed/internal phase

The existing recurrent-port signature tool applies to stable hidden nonnegative-rational blocks under its declared context lease. A unit-weight deterministic C12 internal cycle is recurrent with eigenvalue 1 and is not such a stable hidden block.

The tool therefore cannot silently erase the signed internal phase or Path-formal provenance. Direct finite quotients such as active support or unsigned passage remain available under their narrower observer leases.

## 11. Current corrected frontier

Closed in the corrected V1/V5 layer:

- 960 ordered signed triad frames;
- 160 exact canonical C6 orbits;
- 1920 SHELL/CLOSURE states and 160 C12 cycles;
- 20/40 PF-10 unsigned observer cardinalities and 48/24 fibers;
- four signed C6 orbit sectors over every directed passage;
- unsigned-axis covariance of the canonical generator;
- four-twist gauge-covariant completion under independent sign-frame changes;
- cumulative-count Markov obstruction.

The global channel-frame gauge/flat-transport V2, unsigned channel C3 V3, frame/channel projection V4 and all-20 A6 integration remain valid after this signed-layer correction.

No Foundation promotion is made.
