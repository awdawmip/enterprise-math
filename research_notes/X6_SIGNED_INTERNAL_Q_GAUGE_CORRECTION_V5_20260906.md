# X6 signed internal Q correction V5: tokenwise update, four-twist bundle and signed-frame gauge covariance

Status: `FREE_RESEARCH / EXACT CORRECTION + DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Checker: `experiments/x6_signed_internal_q_correction_v5_20260906/check_signed_internal_q_correction.py`.

## 1. Correction target

The current V1 internal note and V3 channel note wrote the signed triadic frame update as

`R(d0,d1,d2)=(-d1,-d2,-d0)`.

That formula is correct on the sign-coherent subfamily used in several earlier examples, but it is **not** the action of one fixed canonical triadic generator `Q_S=J_S rho_S` on an arbitrary signed port frame.

Concrete witness on the oriented axes `(1,2,3)`:

`tau=(+E1,-E2,+E3)`.

The fixed canonical generator sends tokenwise

`+E1 -> -E2`,
`-E2 -> +E3`,
`+E3 -> -E1`,

so the correct result is

`(-E2,+E3,-E1)`.

The historical tuple-reordering formula instead gives

`(+E2,-E3,-E1)`.

Therefore the global signed formula and the old naive full-sign-equivariance check must be corrected.

This is a research-layer correction only. P000 and the signed-X6 spatial Foundation are unaffected.

## 2. Correct canonical tokenwise update

Represent a full ordered signed triad frame as

`F=((i0,i1,i2),(s0,s1,s2))`,

with distinct underlying axes and `sr in {+1,-1}`.

For the canonical oriented generator

`Q_S(E_i0)=-E_i1`,
`Q_S(E_i1)=-E_i2`,
`Q_S(E_i2)=-E_i0`,

the tokenwise update is

`R_can(F)=((i1,i2,i0),(-s0,-s1,-s2))`.

Equivalently, token `r` keeps its provenance slot, moves to the next axis in the oriented triad, and flips its own sign.

Exact laws remain

`R_can^2: axes shift twice, signs unchanged`,

`R_can^3: same axes, all three signs reversed`,

`R_can^6=1`.

Every frame still has exact period six. Hence all previously correct cardinalities remain:

- 960 full ordered signed frames;
- 160 C6 orbits;
- 1920 SHELL/CLOSURE decorated states;
- 160 decorated C12 cycles.

## 3. What survives unchanged downstream

The correction does **not** change the unsigned axis order:

`(i0,i1,i2) -> (i1,i2,i0)`.

Therefore all results depending only on the unsigned directed passage remain valid:

- 20 active unsigned three-channel supports;
- 40 directed unsigned C3 passage states;
- PF-10 passage fiber size 24;
- triadic unsigned channel circulation C3;
- the projection `R_triad -> A6`;
- the exact frame group `R_triad=(C2)^6 semidirect A6`, order 23040;
- the frame/channel diagonal coupling and its 64-element sign kernel;
- the all-20 chart/triadic/channel common A6 skeleton.

So this is a surgical correction to the **signed internal phase and covariance layer**, not a collapse of the upper program.

## 4. Why naive full signed-frame equivariance fails

The canonical family `Q_S=-rho_S` is covariant under unsigned axis relabeling: relabel the ordered axes and the same canonical rule is obtained.

But conjugating by an independent sign-frame change generally changes the edge signs of the generator.

Let a sign gauge assign `epsilon_i in {+1,-1}` to each selected axis. Then

`g Q_S g^-1(E_i_r)`

`= alpha'_r E_i_{r+1}`

with

`alpha'_r = - epsilon_{i_r} epsilon_{i_{r+1}}`.

Unless the three sign gauges agree appropriately, the three `alpha'_r` are not all `-1`.

Therefore

`CANONICAL_Q_FAMILY != CLOSED_UNDER_INDEPENDENT_SIGN_FRAME_CONJUGATION`.

The previous V1 statement `R(g tau)=g R(tau)` for arbitrary independent sign flips was too strong.

## 5. Gauge-covariant signed C6 generator bundle

The correct closure is obtained by allowing the general signed 3-cycle

`Q_{S,alpha}(E_i_r)=alpha_r E_i_{r+1}`

with

`alpha_r in {+1,-1}`

and the single constraint

`alpha_0 alpha_1 alpha_2 = -1`.

Then

`Q_{S,alpha}^3 = -I_S`,

`Q_{S,alpha}^6 = I`.

There are exactly four allowed edge-sign patterns:

`(-,-,-)`, `(-,+,+)`, `(+,-,+)`, `(+,+,-)`.

The canonical generator is the representative `(-,-,-)`.

Under a sign-frame gauge `epsilon`, the twist transports by

`alpha'_r = epsilon_{i_r} epsilon_{i_{r+1}} alpha_r`.

The product constraint is invariant because every `epsilon_i` occurs twice. The eight local sign gauges act transitively on the four twist patterns with a two-element kernel given by simultaneous reversal of all three selected signs.

Hence the **four-twist bundle**, not one fixed canonical representative, is the object closed under full signed-frame gauge covariance.

## 6. Exact covariance theorem

Let `g_epsilon` be an independent sign-frame change on the selected axes. Then

`g_epsilon Q_{S,alpha} g_epsilon^-1 = Q_{S,alpha'}`

with the transported twist above.

Equivalently on signed port frames,

`Q_{S,alpha'}(g_epsilon F)=g_epsilon(Q_{S,alpha}F)`.

Thus:

- unsigned `S6` covariance can use the canonical representative directly;
- full signed-frame covariance requires transport of the four-state twist/gauge datum.

This correction does not enlarge `R_triad`: every twist is a sign-kernel conjugate of a canonical `Q_S` and already lies in `(C2)^6 semidirect A6`.

## 7. The four internal C6 sectors over every directed passage

Fix one unsigned directed passage cycle. Its 24 full signed/provenance frames split into exactly four C6 orbits.

For a phase-origin representative with signed token vector `(s0,s1,s2)`, define

`alpha_state=(-s0*s1,-s1*s2,-s2*s0)`.

Then

`product(alpha_state)=-1`,

so `alpha_state` is one of the same four twist patterns.

Global reversal `(s0,s1,s2)->(-s0,-s1,-s2)` leaves `alpha_state` unchanged, and the corrected canonical C6 update preserves the pattern in its moving phase coordinates.

For each of the 40 directed passages, the four C6 orbits realize the four possible `alpha_state` values exactly once.

This gives a useful identification:

`SIGNED INTERNAL C6 ORBIT SECTOR <-> FOUR-STATE RELATIVE-SIGN/TWIST CLASS`

once the oriented passage and phase convention are fixed.

It also explains why the sign-coherent orbit naturally picks the canonical `(-,-,-)` representative.

## 8. Relation to PF-10 and channel A6

PF-10 unsigned passage forgets the four-state signed sector completely. All four twists have the same unsigned 3-cycle projection.

Therefore the current channel hierarchy becomes more precise:

`concrete Path/BRC provenance`

`-> signed triadic frame + twist/relative-sign sector`

`-> unsigned triadic frame element in R_triad`

`-> A6 channel permutation`

with observer-specific collapses between them.

The V3 channel result remains valid after replacing its historical signed `R` formula by the corrected tokenwise statement: after forgetting signs, the axis tuple still undergoes a cyclic reindexing, so the directed unsigned passage is invariant along the internal C6 phase.

## 9. Required source corrections

The following current research artifacts must be read with this V5 correction:

- `X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`: replace its signed `R` formula and downgrade naive full sign-flip equivariance to the four-twist gauge-covariant theorem;
- `check_triadic_port_frame.py`: replace historical tuple-reordering `R` and the false independent-sign equivariance assertion;
- `X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md`: its pure-translation gauge/flatness theorem remains valid; only the displayed internal `R` shorthand in the coupling section is corrected;
- `X6_TRIADIC_CHANNEL_FIELD_V3_20260906.md` and checker: unsigned C3 theorem remains valid; update the signed `R` explanation/check implementation;
- V4 frame/channel coupling and V3 all-20 A6 integration remain mathematically unchanged.

## 10. Verification

The exact checker verifies:

- a concrete mixed-sign counterexample to the historical formula;
- all 960 corrected signed frames and 160 exact C6 orbits;
- 160 exact decorated C12 cycles;
- 40 directed passages with four signed orbit sectors each;
- all four product-`-1` twist patterns;
- unsigned axis-relabeling covariance;
- explicit failure of naive independent-sign canonical covariance;
- full sign-gauge covariance after twist transport;
- unchanged PF-10 20/40 observer cardinalities and 48/24 fibers.

No Foundation promotion or external novelty claim is made.
