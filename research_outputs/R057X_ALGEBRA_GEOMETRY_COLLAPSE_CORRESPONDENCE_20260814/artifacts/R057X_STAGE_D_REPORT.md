# R057X Stage D — Frozen STAR Residual-Structure Comparison

Researcher-ID: `EM-R057X-5E8C41`

Status: `STAGE_D_FROZEN / AWAITING_DRIVER_REVIEW / DIAGNOSTICS_ONLY / NOT_THEOREM / NOT_CANONICAL`

## Frozen inputs

- A Stage-G residual diagnostic checkpoint: `4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0`
- G Stage-H residual diagnostic checkpoint: `21f051e5f2cfe276a1a746112968ca7d8ca6dedee2efe9fe006da94e47f9726b`
- X Stage-C1 STAR comparison checkpoint: `1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`
- Taskbook source: `f7dc5d4084e765d90cb1b93473c3dfd399e67dea`

No R057Y gravity-pilot evidence was read or consumed.

## D0 reproduction/provenance

PASS.

A reproduces all 144 circles x D1/D2/D3 frozen Stage-F metrics with exact difference zero and reports no refit, optimizer, teacher/K/operator expansion, parser/context mutation, or assembly/readout change.

G H0 reproduces 204/204 frozen values with max absolute difference `8.881784197001252e-16`; sparse publication byte reproduction is `PASS_8_OF_8`, and no optimization/refit occurred.

Both diagnostics descend from their frozen STAR-transfer checkpoints and reference the same X Stage-C1 semantic anchor.

## D1 cause-ledger crosswalk

- Assembly switching: `COMMON_REJECTED` as a residual cause; both arms rate it `NOT_SUPPORTED`.
- Finite-scale effect: `COMMON_SUPPORTED`.
- Unexplained residual structure: `COMMON_SUPPORTED`, but a shared nonzero remainder is not itself a common mechanism.
- Feature covariance drift: `G_STRONGER` (`A=WEAK_SUPPORT`, `G=SUPPORTED`).
- Packet-mixture evolution: `G_STRONGER` (`A=WEAK_SUPPORT`, `G=SUPPORTED`).
- Phase mixture: `G_STRONGER` (`A=WEAK_SUPPORT`, `G=SUPPORTED`).
- Orientation mixture: `ARM_SPECIFIC_OBSERVABLE` (`A=NOT_AVAILABLE`, `G=WEAK_SUPPORT`).

`WEAK_SUPPORT` and `SUPPORTED` remain distinct.

## D2 normalized trajectory shapes

A shows strong early/middle residual decline, followed by residual MSE/bias rebound at R=448/640. This rebound occurs only after class-mixture TV has contracted to roughly 0.02-0.03 on the largest transitions and covariance rotations have become comparatively small. Therefore A freezes `RESIDUAL_REBOUND_AFTER_MIXTURE_CONTRACTION=SUPPORTED`.

G's frozen D2 RMSE decreases strongly from R=7 to R=47, rebounds at R=71, contracts at R=113, and rebounds again at R=181. Within-arm RMSE ranking from low to high is `[47, 113, 181, 71, 29, 17, 11, 7]`. However motif entropy is nonmonotone and does not establish packet-mixture contraction before the rebounds; AREA/RUN_DEFECT covariance also continues to rotate. Thus G freezes `RESIDUAL_REBOUND_AFTER_MIXTURE_CONTRACTION=INSUFFICIENT`.

Cross-arm result: `COMMON_POST_MIXTURE_REBOUND_SIGNATURE` is not frozen; status is `INSUFFICIENT`.

## D3 STAR-coordinate residual geometry

A's deployed STAR covariance rotations are about 9-13 degrees at earliest radius transitions, mostly below 2 degrees beyond R=128, and <=0.43 degrees on nested windows; effective rank stays near 2.2. The persisted summary does not expose a per-feature AREA-vs-RUN_DEFECT variance trajectory, so no feature-stability ordering is inferred.

G's AREA/RUN_DEFECT correlation changes sign 4 times over the ordered radius grid, while leading-eigen share ranges from `0.570720357807` to `0.945315056653`. This is descriptive evidence of genuine residual/design-geometry rotation, not merely amplitude change.

Therefore:
- `RUN_DEFECT more stable than AREA in both arms`: NOT ESTABLISHED.
- `AREA specifically noisier in both arms`: NOT ESTABLISHED.
- `A/G residual geometry differs only by amplitude`: REJECTED descriptively; G retains materially stronger rotation/mixture burden.

## D4 common unexplained signature

`COMMON_ASSEMBLY_SWITCHING_EXCLUSION = SUPPORTED`.

`COMMON_FINITE_SCALE_RESIDUAL_COMPONENT = SUPPORTED`, but only as a weak matched structural statement; no shared functional radius law is claimed.

`COMMON_POST_MIXTURE_REBOUND_SIGNATURE = INSUFFICIENT`.

`G_CARRIER_MIXTURE_BURDEN_STRONGER = SUPPORTED_DESCRIPTIVELY`; this is not a claim that one carrier is intrinsically better.

## D5 primary disposition

`MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE`

Reason:

1. Both arms independently exclude assembly switching as the dominant residual cause.
2. Both independently support a finite-scale residual component.
3. Both retain an unexplained structured remainder.
4. The stronger matched post-mixture rebound signature is not established.
5. G has stronger diagnosed feature-covariance, packet-mixture and phase burden, plus a weak orientation burden, while the corresponding A causes are only weakly supported or unavailable.
6. Therefore the common residual component is real but incomplete; carrier-specific mixture/covariance structure remains material.

This is not `COMMON_RESIDUAL_MECHANISM_SUPPORTED`, because common cause labels and nonzero residuals do not meet the taskbook's high threshold for a matched mechanism.

It is not `CARRIER_SPECIFIC_RESIDUAL_STRUCTURE_DOMINANT`, because assembly exclusion and finite-scale structure are common across both arms.

## Next route

If Driver accepts Stage D, first isolate the common residual component from carrier-specific mixture/covariance effects before any new operator proposal. This Stage D does not create or authorize a generator.

## Hard-prohibition audit

PASS: no refit, optimizer, symbolic regression, new teacher, K expansion, feature/operator/surrogate creation, parser/segmentation/assembly/readout change, coefficient copying, raw A/G fit-error leaderboard, residual-driven generator invention, or R057Y consumption.
