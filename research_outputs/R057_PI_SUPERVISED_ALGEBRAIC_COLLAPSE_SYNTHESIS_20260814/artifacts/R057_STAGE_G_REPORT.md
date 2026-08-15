# R057-A Stage G — Frozen STAR Residual-Structure Diagnostics

Researcher-ID: `EM-R057-6A31F2`

Status: `STAGE_G_FROZEN_STAR_RESIDUAL_DIAGNOSTICS / AWAITING_DRIVER_REVIEW / NOT_THEOREM`

## Scope

Diagnostics only. Frozen TD000+TD001, K<=8, Stage-F D1/D2/D3 coefficients, STAR operators, cyclic/oriented-D6 assembly and readout were reused unchanged. No coefficient refit, optimizer, teacher/K/feature/operator expansion, parser/context change, new G numeric fitting table, or diagnostic-driven generator proposal was used.

## G0 reproduction gate

`R057_A_STAGE_G_REPRODUCTION_GATE_SHA256 = db0e3ba0b415166ac17018fd580906eda71fae6be988b8c6b886b5d499219396`

D1/D2/D3 frozen global metrics reproduce with exact zero numeric difference for every Stage-F metric. Diagnostics therefore proceed.

## G1 deployed packet mixture

The actual frozen deployment is dominated by K7 collapsed packets plus deterministic short raw fillers. D1/D2 K7 edge fractions remain roughly 0.96–0.98 across radii, while deployed class-mixture TV is largest at the smallest radius transitions and contracts to ~0.02–0.03 at the largest transitions. Class entropy remains high within the active deployed classes, so no single packet class takes over.

Packet-mixture evolution has descriptive support for residual drift: D1 residual-RMSE step vs successive-radius class-mixture TV has Spearman rho `0.64545` (`p=0.03196`). The same statistic is weaker for D2. Frozen per-radius coefficient steps do not track class-mixture TV.

## G2 feature geometry

For actual deployed packet occurrences, the 4D STAR covariance principal direction rotates by roughly 9–13 degrees at the earliest D1/D2 radius transitions, then mostly below 2 degrees beyond R=128. Nested-window principal rotations are <=0.43 degrees and covariance effective rank stays near 2.2. This supports a finite-scale feature-geometry effect, but not a consistent explanation of coefficient drift. Covariance eigenvalue ratios are reported strictly as covariance anisotropy, never as regression-Hessian condition numbers.

## G3 cyclic active set

D1 and D2 select exactly the same class-count multiset on `73.61%` of teachers. The median positive edge-weighted difference where they change is `0.03237`. D2 absolute-residual advantage vs active-set-change magnitude is essentially uncorrelated (`Spearman rho=-0.04113`, `p=0.62450`).

The frozen solver exposes class-count multiset and best cyclic start offset. It does **not** expose ordered tiling path, tie/degeneracy count, or best-vs-second-best margin. Those fields are frozen as `NOT_AVAILABLE`; the parser was not modified.

## G4 residual stratification

Phase identity remains material: phase-mean residual standard deviation is ~0.39 of overall residual standard deviation for D1/D2, with P02 persistently negative. But the 12 phases have equal weight at every radius, so changing phase mixture cannot cause scale drift.

Absolute residual vs `1/R` has Pearson correlation `0.54680` for D1, `0.54412` for D2 and `0.57251` for D3 (all `p<2e-12`). Residual error declines strongly from small radii into the R=160–224 region, then rebounds at R=448/640.

## G5 cause ledger

- `PACKET_MIXTURE_EVOLUTION = WEAK_SUPPORT`
- `FEATURE_COVARIANCE_DRIFT = WEAK_SUPPORT`
- `ASSEMBLY_ACTIVE_SET_SWITCHING = NOT_SUPPORTED`
- `PHASE_MIXTURE = WEAK_SUPPORT`
- `FINITE_SCALE_EFFECT = SUPPORTED`
- `UNEXPLAINED_RESIDUAL_STRUCTURE = SUPPORTED`

The strongest conclusion is negative/diagnostic: the permitted frozen observables do **not** provide one mechanism that consistently explains both coefficient drift and residual drift. The large-radius residual rebound remains after packet-mixture and covariance trajectories have already become comparatively stable. This is not authorization to invent a generator.

## Frozen artifacts

- `R057_A_STAR_RESIDUAL_DIAGNOSTIC_ATLAS_SHA256 = 1641be057d6527cc07bd54bb2dbb9c61b754bb8fe4273c393322b5e65a4732d9`
- `R057_A_STAR_MOTIF_MIXTURE_TRAJECTORY_SHA256 = 994587710181c284f53121ae195b19dc11071091dc462c75ba7e2b7cd36bfd23`
- `R057_A_STAR_FEATURE_GEOMETRY_SHA256 = 4d319dcd88e8c9de22b4db4a85bf7119b3ca5e76a471a040de49fb4760bc43b8`
- `R057_A_STAR_ASSEMBLY_ACTIVE_SET_DIAGNOSTICS_SHA256 = a921e4c8f0d75680b4fe39a11ae2961f6a510dc11e134479bce2cacde6bb8548`
- `R057_A_STAR_RESIDUAL_CAUSE_LEDGER_SHA256 = 1fcd7956546f38626de9dd350cf27d4960da8a241ca523d249638ba47ac7bee3`
- `R057_A_STAGE_G_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256 = 4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0`
