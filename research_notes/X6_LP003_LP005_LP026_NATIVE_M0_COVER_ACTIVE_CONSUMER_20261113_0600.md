# X6 LP003/005/026 — current native m=0 cover and signed Cell step consumer repair

Date: 2026-11-13. Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Author side: `EM-X6-FB6990` / Research lane `chatgpt-research-onhour-enterprise-math-20260923`; source-derived analysis, NONBLIND / UNREVIEWED / NOT_ADMITTED. No historical RR or P000 mutation.

## Exact current authority and consumer scope

- Frozen task scientific baseline: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Current `p000_reality_foundation.json` (read blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`): `X6_NATIVE_SPATIAL_TRANSLATION_GROUP=Z^6`, signed primitive steps, integer common depth is a native composite diagonal coordinate, not an extra axis; min-zero is a derived observer.
- Actual current executable consumers audited: `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` (original blob `3f7d9e62a4dd66e7888a69ff87276b283c891aac`), `check_x6_cover.py` (original blob `ba0a4fe90234186f12386b671b4d1cfef9b39648`), `x6_coordinate.py` (read blob `dd6dd7e74b83be09bb7545ee92357eda445c6ca3`), and `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` (read blob `ac32f6d82a91db99297e587cf63b0df95cece514`).
- Previous author-side full `check_x6_coordinate.py` project import PASS 58,989 and 4,096 raw lifts already Source-published at `onhour-20261113-0522-own-custody-v7-progress-publish` (verified SUCCEEDED). **Do not repeat or conflate it with this different `check_x6_cover.py` consumer.**

## Actual verified code problem, repair and algebra

The old live `x6_cover.py` header called `m=1` “coordinate-complete Cell identity”, and `check_x6_cover.py` explicitly said “m=1 ... depth never changes Cell identity”. That is a valid classification *within the quotient-cover family*, but unqualified native-Cell terminology conflicts with current P000 V5. This was an actual present executable-doc consumer, not merely a suspected historical misuser.

Let `D=(1,1,1,1,1,1)`. For every `z∈Z^6`, define `h=min_i z_i`, `r=z-hD`. Then `r` is the unique min-zero representative and `z=r+hD`. At modulus `m=0`, the existing `CoverState.step(i,s)` computes `v=r+hD+s e_i`, `h'=min_i v_i`, and `r'=v-h'D`. Consequently the native reconstruction after the step is `r'+h'D=z+s e_i` **for every integer starting displacement and either sign of the primitive step**; signed spatial square norm is `Σ_i(z_i+s[e_i]_i)^2` (the chosen Cell anchor is explicit).

By contrast, `m≥1` identifies `z` and `z+mD`: both have the same `r` and depth residue `h mod m`, although they are distinct native Cells with different signed displacements. In particular, `CoverState(r=0,h=0,m=1)=CoverState(r=0,h=1,m=1)`, while the same states differ for `m=0`. Therefore a generic finite-m `CoverState` cannot be used as a complete native Cell identity.

The live source repair:
1. Retypes `m=1` as coordinate-complete **relative quotient observer**, `m=0` as actual signed-native depth-preserving encoding; preserves all finite-m mathematical operations.
2. Adds `CoverState.signed_native_displacement()` which returns `coordinate.signed_native_lift(depth)` **only if modulus=0**, and raises `ValueError` for every finite-m cover. This creates an explicit type safety boundary instead of relying on documentation alone.
3. Extends the *original* `check_x6_cover.py` with cross-module `Spatial6.step` native equality and square-norm checks over all `[-2,2]^6` starting displacements, both signs and six axes, plus finite-cover rejection and m=1 collision. Source path remains unchanged; no substitute checker is offered as the project's original regression.

GitHub CAS source edits:
- `x6_cover.py`: commit `f16225dfeb249790884a4f7e77acd591ba6b59ac`, new blob `171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd`.
- `check_x6_cover.py`: commits `85c40f2511aaadf07a0c1908397afd0f9aedac19` and `be3778775fc728fb2388279ef3c2105823aa2cbe`, final blob `65778c6ccb44eb9bb15c0123ac51423dd10c8686`.
- Each updated complete file was independently fetched again from current GitHub main and final blob rechecked.

## Actual execution distinction

A **local standalone exact-integer reference calculation** (not imported from the repository modules) evaluated the `r,h` step relation on all `5^6 = 15,625` starting displacements and `12` signed directions per start: `187,500` steps and `390,625` identity/norm assertions, all passed. This supports the elementary proof and the intended regression design.

**Not executed in this run:** the modified original repository `check_x6_cover.py` end-to-end import with the actual four current modules. Consequently, the author-side GitHub test change is `SOURCE_PATCHED / EXACT_REFERENCE_EXECUTED / ORIGINAL_PROJECT_CHECK_PENDING`, **not** `NATIVE_IMPORT_PASS` or formal Source Result. Next exact acceptance action: execute `python experiments/x6_native_coordinate_completion_v7_20260905/check_x6_cover.py` from a real checkout containing the four exact blobs above, collect stdout/exit status and hashes, then update its original-check execution certificate. This is not the previously completed `check_x6_coordinate.py` regression.

## Parent/frontier

Preserve 28-LP ledger and the already published frozen historic 72, signed 30/846, closed-disk carrier proof, LP019 FCC 48 carrier-only return and LP028 60-chart certificates. Remaining: complete the **declared finite actual consumer/dependency coverage** (in particular LP011/LP019 historical wrong-call provenance remains UNRESOLVED_PROVENANCE), run the modified original cover checker, satisfy Driver REQUEST_REVISION and obtain independent semantic review where appropriate. No new selector, task, claim, reviewer or P000 authority is asserted.

Research lane session `MCP-082892eb480e45dea6d4b9fcc0491034`, researcher `EM-X6-FB6990`, prior run `RUN-1e81bbcb1938961eb41db249`, prior claim `MCP-9ce362c91287345702dd387d` are **provenance pointers only until fresh reauthorization**. Earlier Source PROGRESS `onhour-20261113-0522-own-custody-v7-progress-publish` is SUCCEEDED; continuation read `onhour-20261113-0610-current-task-continuation` was QUEUED as last checked. Do not reissue its operation under a new ID; reconcile that request.
