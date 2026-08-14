# R057X Stage E — Common Residual Component Isolation Without Refit

Researcher-ID: `EM-R057X-5E8C41`

Status: `STAGE_E_FROZEN / AWAITING_DRIVER_REVIEW / NOT_THEOREM / NOT_CANONICAL`

Epistemic label: `POST_FIT_CROSS_CARRIER_COMMON_COMPONENT_DIAGNOSTIC / NOT_THEOREM / NOT_CANONICAL`

## Frozen inputs

- `R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT_SHA256 = 7059ec68f6ace7cb46360476b7378b12b06dbb5a426269c20ae598e6bde1e771`
- `R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT_SHA256 = 1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`
- `R057_A_STAGE_G_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256 = 4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0`
- `R057G_STAGE_H_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256 = 21f051e5f2cfe276a1a746112968ca7d8ca6dedee2efe9fe006da94e47f9726b`
- taskbook source `f3b308cafef6780d4becaa0d894f6611906f2f43`

No coefficient refit, optimizer, symbolic regression, new teacher, K expansion, new feature/operator/surrogate, parser/segmentation/assembly/readout change, cross-arm fitted rescaling, R057Y use, or hotspot-driven generator invention occurred.

## E1 — dimensionless scale isolation

Using the frozen C0R V2 carrier units:

- A: `ell_edge_A=1/sqrt(3)`, so `S_A=sqrt(3) R_A`;
- G: `ell_edge_G=1`, so `S_G=R_G`.

Before residual-outcome comparison, Stage E froze the taskbook-recommended symmetric tolerance

`|log(S_A/S_G)| <= log(4/3)`,

with no interpolation and no fitted rescaling.

Exactly eight tolerance-qualified pairs occur:

`(A24,G47), (A32,G47), (A32,G71), (A40,G71), (A56,G113), (A72,G113), (A96,G181), (A128,G181)`.

Hence G radii `7,11,17,29` have no A partner and A radii `160,224,320,448,640` have no G partner. In particular, the strongest early G finite-scale region and A's late nuisance-light/rebound regime do not coexist in a matched dimensionless-scale window.

## E2 — nuisance-light strata

The selection rule was residual-blind.

For G, transition nuisance burden was defined only from frozen non-residual diagnostics:

1. `abs(delta motif entropy)`;
2. `abs(delta AREA/RUN_DEFECT correlation)`;
3. covariance concentration burden = maximum leading-eigen share across transition endpoints.

For each observable the lowest `ceil(n/2)` of seven transitions was retained; ties break by later radius. Their intersection is exactly:

`71->113` and `113->181`.

Thus the strict G nuisance-light radii are `71,113,181`.

For A, the hash-anchored Stage-G summary records the qualitative contraction of packet-mixture TV and covariance rotation, but does not expose the per-transition arrays required to execute the same predeclared lower-half rank rule without rerunning upstream diagnostics. Therefore the strict A nuisance-light rank stratum is `NOT_INSTANTIABLE_FROM_PERSISTED_HASH_ANCHORED_SUMMARY`.

The previously frozen R=448/640 late rebound remains a sensitivity witness only and is not used to define a Stage-E residual-blind stratum.

## E3 — finite-scale component

G's strict nuisance-light radii have D2 RMSE normalized by G's own frozen global RMSE:

- R=71: `0.479437754163028`;
- R=113: `0.287605141206944`;
- R=181: `0.376012650214105`.

All are below one. Since no early G radius remains inside the strict nuisance-light stratum, the predeclared test `EARLY_SCALE_BURDEN_PERSISTS_AFTER_NUISANCE_STRATIFICATION` is not testable there.

A cannot instantiate an exact residual-blind nuisance-light early/late stratum from the persisted summary.

Therefore Stage D's weak `COMMON_FINITE_SCALE_RESIDUAL_COMPONENT` is **not upgraded** by Stage E. Cross-arm E3 status is `INSUFFICIENT`, not `COMMON_FINITE_SCALE_COMPONENT_ONLY`.

## E4 — matched K<=6 motif residual enrichment

Stage B supplies exactly 62 semantic bridge motifs covering every ±1 turn word for K=2..6. Stage E froze an extraction convention for open contiguous K<=6 submotifs of actually deployed packets, including K7 A packets, without raw class-ID matching.

However, neither consumed durable review surface exposes the required sample-level joint table of:

`frozen residual x matched-K<=6 motif exposure`.

The A delivery manifest and G sparse publication index anchor their generated diagnostics by SHA256, but the joint occurrence/residual rows are not present on the consumed durable source tree. Reconstructing them here would require rerunning upstream parser/assembly/prediction diagnostics beyond this read-only Stage-E path.

Accordingly:

`MATCHED_MOTIF_RESIDUAL_ENRICHMENT = INSUFFICIENT`.

No motif is mislabeled `NO_ASSOCIATION` or `LOW_SUPPORT`; missing joint evidence is not a negative association result.

## E5 — nuisance-light STAR residual geometry

For the strict G nuisance-light radii `71,113,181`, frozen AREA/RUN_DEFECT correlation is respectively:

`0.314705272691885, 0.097206875726442, -0.181457587460883`,

with one sign change. Leading-eigen share spans `0.570720357806925` to `0.720330716940981`. Thus G does not collapse to one fixed STAR residual geometry after the low-burden transition filter.

A's exact strict-filtered STAR means/variances/hotspot overlap are unavailable on the persisted summary. Its late low-rotation rebound witness remains descriptive only.

Therefore:

`NUISANCE_LIGHT_RESIDUAL_GEOMETRY = INSUFFICIENT`.

No common AREA-vs-RUN_DEFECT hotspot orientation is isolated.

## E6 — primary disposition

Stage E returns exactly:

`INSUFFICIENT`.

This is not a claim that no common residual component exists. It means the required isolation threshold cannot be met from the current frozen durable surfaces without rerunning forbidden upstream work or adding a new matched diagnostic bridge.

Why the other dispositions are not selected:

- `COMMON_RESIDUAL_COMPONENT_ISOLATED`: no matched motif or matched nuisance-light STAR-geometry signature;
- `COMMON_FINITE_SCALE_COMPONENT_ONLY`: nuisance-stratified finite-scale survival is not established in both arms on matched S;
- `CARRIER_SPECIFIC_NUISANCE_DOMINATES_AFTER_ISOLATION`: isolation is incomplete, so nuisance dominance cannot be attributed;
- `COMMON_COMPONENT_NOT_ISOLATED`: descriptively compatible, but too strong as the primary scientific conclusion because key joint inputs are unavailable.

## Validation

Frozen semantic checks: `71/71 PASS`.

Deterministic file/hash/guard checker: `27/27 PASS`.

Combined recorded validation: `98/98 PASS`.

`CI_NOT_REQUIRED_FOR_RESEARCH`.

## Frozen checkpoint

`R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT_SHA256 = 3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385`

Stop for Driver review. No generator discovery is authorized by this checkpoint.
