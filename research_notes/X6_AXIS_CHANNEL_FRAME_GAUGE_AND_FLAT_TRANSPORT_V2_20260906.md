# X6 axis-channel frame V2R: global gauge torsor, square holonomy and symmetry-forced flat transport

Status: `FREE_RESEARCH / EXACT CONDITIONAL DERIVATION / CORRECTED 2026-09-06 / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Depends on: corrected `X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md` and V5 signed-Q correction.

## 1. Axis-channel frame field

PF-10 has an abstract six-channel label set `C`; X6 has six native unsigned spatial axis labels `A`.

An axis-channel frame at Cell `x` is a bijection

`beta_x:C -> A`.

There are `6!=720` choices at one Cell. Equal cardinality does not canonically select one.

For a primitive spatial edge `x -> x+e_i`, define channel-label transport

`U_{x,i}=beta_{x+e_i}^{-1} o beta_x in Sym(C)`.

The reverse edge carries `U_{x+e_i,-i}=U_{x,i}^{-1}`.

This is relational frame transport, not a spatial coordinate.

## 2. Square holonomy theorem

For distinct axes `i,j`, compare the two spatial paths around one X6 square. Define

`H_{x;i,j}`

`=(U_{x+e_j,i} U_{x,j})^{-1}(U_{x+e_i,j} U_{x,i})`.

Then channel-frame transport is path-independent on that square iff

`H_{x;i,j}=1`.

So the commutativity of spatial endpoints does not by itself erase internal channel-path provenance.

## 3. Translation-invariant connection

If pure spatial translation has no location-dependent channel rule,

`U_{x,i}=U_i`,

then square flatness is exactly

`U_i U_j=U_j U_i`

for all `i,j`.

When this holds, displacement transport is

`U(z)=product_i U_i^{z_i}`

independent of the chosen primitive-step ordering.

## 4. Full S6 covariance forces trivial pure-translation permutation transport

Assume the deterministic pure-translation rule is fully equivariant under simultaneous axis/channel relabeling:

`U_{g(i)}=g U_i g^{-1}`

for every `g in S6`.

Fix axis `1`. Its stabilizer is `S5`. Hence `U_1` must lie in the centralizer of that `S5` inside `S6`. The common fixed point `1` must be preserved and the restriction to the other five labels lies in the center of `S5`, which is trivial.

Therefore

`U_1=1`,

and by equivariance

`U_i=1`

for all axes.

Thus, under the stated deterministic permutation model,

`FULL_S6_COVARIANCE + TRANSLATION_INVARIANCE`

forces

`PURE_SPATIAL_CHANNEL_TRANSPORT = IDENTITY`.

## 5. Global gauge consequence

Under this theorem one frame chosen at one Cell transports unchanged across pure spatial translations. The 720 initial identifications are related by global channel relabeling.

For channel-relabeling-equivariant future operations they form one global gauge torsor rather than 720 physical states per Cell:

`AXIS_CHANNEL_FRAME = GLOBAL_GAUGE_TORSOR(S6)`.

No canonical element is selected.

If an external device, material parameter, memory register or other future operation attaches fixed non-equivariant meaning to a named channel, the frame becomes relationally observable and must be retained.

## 6. When channel holonomy can reappear

The flatness theorem applies only to bare, translation-invariant, fully S6-equivariant deterministic channel permutations driven solely by the spatial step label.

Nontrivial channel evolution may arise from extra typed data such as:

- active triadic/internal state;
- local field/order parameter;
- symmetry breaking;
- time-dependent interaction;
- non-permutation channel mixing;
- retained path history.

Such evolution belongs to internal dynamics, not bare X6 translation.

## 7. Coupling to corrected triadic internal dynamics

With one global gauge frame chosen, the corrected 960 signed triadic port frames can be represented consistently in channel labels throughout X6.

The nontrivial internal update is **not** the superseded arbitrary-sign shorthand `(-d1,-d2,-d0)`.

For an ordered triad `S=(i0,i1,i2)` and signed token frame

`F=((i0,i1,i2),(s0,s1,s2))`,

the canonical tokenwise update is

`R_can(F)=((i1,i2,i0),(-s0,-s1,-s2))`.

Under independent signed-frame gauge changes the canonical generator is transported inside the four-twist bundle

`Q_{S,alpha}(E_i_r)=alpha_r E_i_{r+1}`,

`alpha_0 alpha_1 alpha_2=-1`.

See `X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`.

This correction does not change the present V2 spatial flatness theorem because that theorem concerns pure channel transport under spatial translation, not the signed internal triadic update.

## 8. Observer boundary

Raw PF-10 channel numbers are gauge-dependent until a frame convention/calibration is supplied.

Gauge-invariant outputs may include support cardinality, unlabeled incidence isomorphism type, conjugacy-invariant passage properties and any fully equivariant pushed-forward tensor package.

The exact gauge theorem can be expressed as

`(Bij(C,A) x channel_package)/S(C) ~= axis_indexed_package`

whenever all admitted operations are channel-relabeling equivariant.

## 9. Current V2 frontier

Closed under the declared deterministic permutation model:

- channel edge connection and square-holonomy formula;
- translation-invariant flatness iff direction transports commute;
- full S6 covariance forces trivial pure-translation channel permutation;
- the 720 frame choices reduce to one global gauge torsor under an equivariant observer lease.

Still open:

- symmetry-broken/non-permutation transport;
- channel transfer between neighboring interacting subsystems;
- field/time dependent channel laws;
- physical channel calibration.

The signed internal-phase correction is contained in V1R/V5 and does not alter these V2 results.

No Foundation promotion is made.
