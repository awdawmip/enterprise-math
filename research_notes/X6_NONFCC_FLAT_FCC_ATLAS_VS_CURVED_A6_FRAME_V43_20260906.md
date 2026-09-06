# X6 non-FCC V43: the 16 rank-3 FCC basis charts form a flat carrier-coordinate atlas, not a native-state gluing

Status: `FREE_RESEARCH / EXACT CARRIER GROUPOID + NATIVE-ALIASING NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NONFCC-SLICE-REALIZATION`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_NONFCC_FCC_LATTICE_BASIS_DECODER_V5_20260906.md`;
- `X6_NONFCC_NORMALIZED_STAR_HIDDEN_C3_REPAIR_V42_20260906.md`;
- `X6_ORIENTATION_PRESERVING_CHART_A6_UNIFICATION_V3_20260906.md`.
Checker: `experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py`.

## 1. Two different things had been called “chart transition”

For the sixteen FACE/PATH selections, V5 gives an exact rank-3 FCC basis matrix `M_S` and transition

`A_{T<-S}=M_T^-1 M_S in GL(3,Z)`.

Separately, V3 gives a native orientation-preserving A6 frame lift along adjacent three-axis selections.

These operations have different semantic sources:

- `A_{T<-S}` re-expresses one **fixed FCC carrier lattice point** in another rank-3 carrier basis;
- an A6 lift transports the **native six-axis frame/state** and then applies a carrier observer.

They must not be identified.

## 2. The direct rank-3 FCC carrier atlas is strictly flat

For any three rank-3 FACE/PATH charts S,T,U,

`A_{U<-T} A_{T<-S}`

`=(M_U^-1 M_T)(M_T^-1 M_S)`

`=M_U^-1 M_S`

`=A_{U<-S}`.

Therefore every closed loop of rank-3 carrier basis changes has transition matrix identity.

This flatness is exact over the integers; no numerical approximation or carrier metric is involved.

The sixteen charts therefore form a flat `GL(3,Z)` **carrier-coordinate groupoid** over the common FCC parity lattice `L_FCC`.

## 3. Flat carrier basis change is not native X6 same-state transport

The carrier groupoid keeps the carrier point `y in L_FCC` fixed while changing basis coordinates.

If one takes the decoded coordinate triple in a new selected native subtorsor and silently calls it the same native state, information is changed.

Concrete witness, using carrier atlas order

`(AB,CD,AC,BD,BC,AD)`:

source FACE chart

`S=(AB,AC,BC)`

and target PATH chart

`T=(AB,CD,AC)`.

Take the FCC lattice point

`y=BC=(0,1,1)`.

Its source coordinates are

`n_S=(0,0,1)`.

Its target rank-3 decode is

`n_T=(0,-1,1)`

because

`BC = -CD + AC`

in the fixed FCC carrier.

The corresponding full X6 slice-supported native displacements are

`x_S=+E_BC`,

`x_T=-E_CD+E_AC`.

They are distinct elements of the signed `Z^6` spatial torsor.

Their current native squared component lengths are

`L_E(x_S)^2=1`,

`L_E(x_T)^2=2`.

So one FCC carrier point can encode two different native X6 states with different native lengths when different slice-membership premises are imposed.

Therefore

`SAME FCC POINT != SAME NATIVE X6 CELL/DISPLACEMENT`.

## 4. Why V5 decoder remains correct

V5 explicitly conditions its lossless decoder on known native slice membership.

Under the premise

`x belongs to centered slice S`,

the direct rank-3 FCC point uniquely recovers that slice's raw `Z^3` coordinates.

The failure arises only when one drops the slice-membership type and reinterprets the same carrier point as a member of a different native subtorsor.

Thus V43 strengthens rather than contradicts V5:

`KNOWN S + FCC POINT -> unique S-coordinate`

but

`FCC POINT -> unique full X6 state`

is false.

## 5. Direct carrier flatness cannot encode A6 chart holonomy

V42 gives a closed all-20 chart path

`012 -> 013 -> 034 -> 024 -> 012`

whose A6 frame holonomy fixes visible 012 pointwise and cycles hidden 345.

Any direct FCC rank-3 basis loop, by section 2, has identity carrier-coordinate transition.

Therefore no function of the flat `GL(3,Z)` carrier transition alone can recover the A6 frame holonomy of general chart-switch histories.

This is an exact observer-loss witness:

`CARRIER COORDINATE FLATNESS != NATIVE FRAME FLATNESS`.

## 6. Two valid observer modes

The sixteen non-STAR charts therefore have two useful but incomparable carrier modes.

### Direct fixed-FCC rank-3 mode

Input: known selected native slice S.

Readout: `y=M_S n in L_FCC`.

Strength:

- exact injective raw selected-coordinate encoding;
- exact integer decoder;
- flat `GL(3,Z)` carrier interoperability.

Does not provide the existing planar circle/gate STAR semantics.

### A6-normalized STAR mode

Input: source chart S plus a chosen orientation-preserving normalization lift.

Readout: established planar STAR relative/circle/gate observer.

Strength:

- gives the common STAR visualization/phase/circle interface;
- compatible with native A6 frame transport.

Losses:

- common depth unless repaired;
- normalization frame/holonomy unless repaired as in V42.

Neither mode dominates the other for all future operations.

## 7. Operation-safe switch architecture

Native identity remains the full signed X6 state/frame layer.

Carrier modes are ports over that state, not equivalence relations between native Cells.

The safe architecture is

`FULL X6 STATE / FRAME`

`-> choose typed slice + observer mode`

`-> DIRECT RANK3 FCC` **or** `A6-NORMALIZED STAR`

`-> retain repair data required by the declared future language`.

Switching modes by equating carrier outputs is forbidden unless an explicit operation-safe bridge proves the relevant native state/frame information is recoverable or irrelevant.

## 8. Task closure consequence

The original `RS-X6-NONFCC-SLICE-REALIZATION` questions are now resolved at research strength:

- all 20 selections have intrinsic native signed C6/C12 Cell-path realization;
- fixed FCC carrier types are exactly 4 STAR / 4 FACE / 12 PATH;
- the 16 FACE/PATH charts are exact integer bases of the FCC parity lattice;
- every chart can also be A6-normalized to STAR semantics;
- all normalization loss and route dependence have explicit repair types;
- direct rank-3 carrier transitions are flat but are not native-state gluing;
- a concrete same-carrier/different-native-state counterexample is known.

Remaining questions are application/calibration choices of observer mode, not missing existence of the sixteen non-FCC native slices.

No Foundation promotion or physical interpretation of FACE/PATH carrier distortion is claimed.
