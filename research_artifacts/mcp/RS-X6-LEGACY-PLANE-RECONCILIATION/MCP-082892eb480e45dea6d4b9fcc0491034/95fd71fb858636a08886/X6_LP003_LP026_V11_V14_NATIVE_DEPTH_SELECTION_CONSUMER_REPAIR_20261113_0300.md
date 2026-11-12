# X6 LP003/LP026 — live V11/V14 native-depth selection consumer repair

Date: 2026-11-13, TASK_RESEARCH on-hour lane. Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Evidence state: **AUTHOR-PROVED TYPED COUNTEREXAMPLE / BOUNDED SOURCE CORRECTION / UNREVIEWED / NOT_ADMITTED**.

## Frozen authority, live input and actual defect

Immutable scientific baseline: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json` blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`; its native signed Cell contract `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`, §§2,4,6,7,10–11. The frozen contract identifies native Cell spatial displacement with `Z^6`, native squared norm `G(z)=sum z_i^2`, and relative observer `can6(z)=z-min(z)·1`, with retained common depth `h=min(z)`.

Actually read two **current-main theorem-facing consumers**:
1. `research_notes/X6_COORDINATE_COMPLETENESS_UNIQUENESS_GATE_V11_20260905.md`, original live blob `3c80bdfb74d9482d460e43e46667f18471affc96`: former §1 labeled `sum_i can6(z)_i²` as “P000 component gauge”; §2/4 historically proposed the `G6_D=Z^6/Z1` quotient as native Cell identity, and §5 called every complete diagonal a native Cell loop. The relative coordinate theorem is valid **under its explicitly hypothetical quotient assumption**, while its *current native* reading conflicts with frozen P000 V5.
2. `research_notes/X6_COMMON_DEPTH_COCYCLE_CELL_COVER_BRIDGE_V14_20260905.md`, original live blob `f25c918cd319c8a664cbc8d96a46b169fdf75d1e`: historical §4 labeled `m=1` “coordinate-complete Cell identity” and presented `m=0` as another as-yet undecided depth-memory option, despite current signed native Cell being the `m=0` member. Its algebraic cocycle and whole finite-`m` classification remain valid as typed quotient alternatives.

These are direct **current repo source claims** actually inspected and corrected, not inferred LP011/LP019 historical faulty consumers.

## Exact separating certificate

Let `D=(1,1,1,1,1,1)`. For every integer `m>=1`, the two native spatial Cells `0` and `mD` are different, whereas:
- `can6(mD)=can6(0)=(0,0,0,0,0,0)`;
- in `Z^6/mZ D`, the two images are the **same**;
- `G(mD)=6m²>0`, while `G(0)=0`;
- the signed `6m`-step **positive-only** native words ending at `mD` have multiplicity `(6m)!/(m!)^6>0`, but none of these words is a native Cell return, since raw displacement `mD !=0`.

Thus no finite-`m` quotient including `m=1` can represent the current native Cell identity and native norm; it is an exact lower-information observer. For `m=0`, the chart `z↔(can6(z),min(z))` is bijective and reconstructs `z=r+hD`, so it preserves native identity and native norm. The normal-form multiplication `(a,h)*(b,k)=(can6(a+b),h+k+min(a+b))` is the exact cocycle used in V14.

Independently evaluated exact-integer spot values: `m=1: G=6, (6)!/(1!)^6=720`; `m=2: G=24, (12)!/(2!)^6=7,484,400`; `m=3: G=54, (18)!/(3!)^6=137,225,088,000`; `m=4: G=96, (24)!/(4!)^6=3,246,670,537,110,000`; `m=5: G=150, (30)!/(5!)^6=88,832,646,059,788,350,720`. These finite spot checks corroborate the formula; the identity/quotient conclusion is proved for every integer `m>=1` by the explicit kernel witness.

The `m=1` historical positive-six-axis “closed path” of length 6 has 720 ordered words to `D`, whereas the **current signed native** 6-step return count is `N_6(0)=19,920`, reflecting **different endpoint predicates** rather than contradictory counting.

## Source repair, provenance and remaining scope

- V11 corrected and remote-readback verified: `8f6a7bf348f507606a305c81d4d99ea82776c975`, blob `9d3f797371b4cff9319f823aed899b0b8bc8e7b9`. It now labels the former native quotient theorem **historical conditional**, distinguishes relative and native norms, and retypes diagonal “returns” as observer returns.
- V14 corrected and remote-readback verified: `16ea9fee56ba78c868ef4f836457844bb94e7f7b`, blob `337c96f13ad0b224e3999a31aaef4155909de0b9`. It now selects `m=0` for current P000 native Cell, retaining all finite-`m` quotient formulas and BRC observer hierarchy.
- Neither historical 2026-09-05 frozen baseline nor P000, accepted R063/Result, experiment code, or other lane identities were modified. Existing completed 50,771 original coordinate regression and LP026 cyclic-cover proofs are consumed unchanged.

Next scientific action: inspect remaining **current theorem-facing** uses of `G6_D` / `Coord6.norm_squared` and native endpoint-return semantics at exact source lines, correcting only verified misuse. The original LP011 dominant-axis and LP019 positive-count cancellation purported historical callsites remain `UNRESOLVED_PROVENANCE`; no false attribution is made here. Full 28-LP dependency closure and independent Driver `REQUEST_REVISION` remain open. Native Source progress/checkpoint must be independently confirmed under own winning claim; GitHub source modification alone is not a semantic Result or review.
