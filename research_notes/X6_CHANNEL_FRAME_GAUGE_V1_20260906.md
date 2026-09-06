# X6 channel-frame gauge V1: when the 720 channel↔axis frames are gauge and when they become observable

Status: `FREE_RESEARCH / EXACT DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Depends on: `X6_CELL_CHANNEL_INTERNAL_STATE_V1_20260906.md`
Checker: `experiments/x6_cell_internal_state_v1_20260906/check_channel_frame_gauge.py`.

## 1. Problem

PF-10 gives six abstract relational channel labels. X6 gives six native unsigned spatial axis labels. V1 showed that a bridge between them is a bijection

`phi:C -> A`

and that there are `6!=720` such bridges.

The question is whether those 720 choices are physical internal states or only coordinate/gauge choices.

## 2. Relabeling action

Let `h in S(C)` be a channel relabeling. For a channel vector `I`, matrix `M`, and bridge `phi`, define

`I^h(c)=I(h^-1 c)`,

`M^h(c,d)=M(h^-1 c,h^-1 d)`,

`phi^h = phi o h^-1`.

The axis-side pushforward is

`(phi_* I)(a)=I(phi^-1 a)`,

`(phi_* M)(a,b)=M(phi^-1 a,phi^-1 b)`.

Direct substitution gives

`(phi^h)_*(I^h)=phi_*I`,

`(phi^h)_*(M^h)=phi_*M`.

The same statement holds for any finite family of channel-indexed tensors transformed covariantly under relabeling.

## 3. Gauge theorem

Let `P_C` be a channel package whose declared operations/observers are equivariant under channel relabeling, and let `P_A` denote the same package with axis labels.

Then the pushforward map induces a canonical bijection

`(Bij(C,A) x P_C) / S(C)  ~=  P_A`.

Proof:

- well-definedness is the pushforward invariance above;
- surjectivity: choose any bridge `phi` and pull an axis package back to channels;
- injectivity modulo gauge: if `phi1_*P1=phi2_*P2`, take `h=phi2^-1 o phi1`; then `(phi1,P1)` relabels exactly to `(phi2,P2)`.

Therefore the 720 channel-axis frames are not 720 physical states when channel labels carry no independent external meaning. They are a gauge torsor.

## 4. When the frame becomes observable

The theorem has an explicit boundary. If a future operation is not channel-relabeling equivariant, the quotient is unsafe.

Example: an external device/observer says “read raw channel `c0`” and does not transform that selector when the internal channel labels are relabeled. Two gauge-related representations can then give different outputs.

Likewise, if channel `c0` carries an externally fixed material parameter, memory register, coupling constant or port identity that is not moved under the relabeling action, the bridge to spatial axes becomes relationally observable and must be retained together with that external structure.

Hence:

`FRAME_IS_GAUGE <=> DECLARED_FUTURE_LANGUAGE_IS_CHANNEL_RELABELING_EQUIVARIANT`.

This is an observer/operation-scoped statement, not an ontological claim that channel frames can never be physical.

## 5. Relation to triadic internal state

The triadic internal fiber can therefore be represented in two equivalent ways under the gauge lease:

1. abstract channel package + bridge `phi`;
2. directly axis-indexed signed port package.

For the current intrinsic X6 triadic dynamics, the second representation is smaller and avoids carrying a 720-fold gauge redundancy.

PF-10 `I/O/M` remains useful as the abstract channel interface. A concrete device or later physical model may restore a channel bridge as a real relational variable by adding non-equivariant channel-specific couplings.

## 6. BRC / quotient classification

This result is a direct specialization of the existing Operation-Safe Quotient discipline:

- population: `(phi, channel package)`;
- gauge branches: channel relabelings;
- observer: axis-side pushed package;
- future operation lease: channel-relabeling-equivariant operations only;
- quotient: channel-label gauge orbit.

No new general-purpose quotient family is required.

The exact checker verifies 3,600 nontrivial frame/relabeling covariance identities using all 720 frame choices and the adjacent-transposition generators of channel `S6`, and gives a fixed-name observer counterexample.

## 7. Current consequence

For the current upper-structure program, do not multiply the 1920-state triadic internal fiber by 720 merely because PF-10 channel labels are available.

Use

`X6 spatial Cell x TRIADIC_INTERNAL_1920`

as the intrinsic axis-indexed interaction carrier unless a task explicitly introduces channel-specific external structure. Then attach the channel-frame relation at that interface and rerun the observer-safety test.

No Foundation promotion is claimed.
