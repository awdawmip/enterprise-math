# Prior Chat CFD checkpoint preserved into canonical source

Status: HISTORICAL_CHECKPOINT_PRESERVED / CURRENT_TASK_MAPPING_VERIFIED
Recorded: 2026-09-10T22:16:02+08:00

This directory preserves the substantive text/data from the Chat CFD checkpoint created before current repository state was recovered. The local package itself had SHA256 `e57da1c40035b39eb55f6ee692a4b5cbbffa91d2c1ab7fa62e1559c37270e606` and size 64364 bytes; its packaging is not task authority.

The repository already preserved the original three-dimensional probe at `research_notes/CFD-B1F673/prior_3d/probe.py`. This directory adds the earlier benchmark result JSON, task-set manifest, and pressure-interface provenance note so that the prior Chat checkpoint is source-visible rather than trapped in a local artifact.

The later, higher durable frontier remains `awdawmip/enterprise-math@e40e5303234c5e8bd725528aad9bff9edf0c059d:research_notes/CFD-B1F673/main/summary.json`. Nothing here rolls that frontier back.

## Original draft intent -> current canonical task

| Original local draft | Current canonical coverage |
|---|---|
| `RS-CFD-HYBRID-RAW-VORTEX` | `RS-CFD-SPECTRAL-HYBRID-20260910` |
| `RS-CFD-CANCELLATION-ENVELOPE` | `RS-CFD-CANCELLATION-GROUPS-20260910` + `RS-CFD-ROUNDING-ENVELOPE-20260910` |
| `RS-CFD-TRAJECTORY-CERTIFICATION` | `RS-CFD-TRAJECTORY-CERTIFICATION-20260910` |
| `RS-CFD-INDEPENDENT-BENCHMARK-REVIEW` | `RS-CFD-TRAJECTORY-VERIFY-20260910` |
| `RS-CFD-ITHACA-ROM-OBSERVERS` | `RS-CFD-ROM-ITHACA-20260910` |
| `RS-CFD-BASILISK-OBSERVERS-AMR` | `RS-CFD-AMR-BASILISK-20260910` |
| `RS-CFD-OPENFOAM-PRESSURE-PORTS` | `RS-CFD-PRESSURE-GAMG-20260910` |
| `RS-CFD-LBM-SEMANTIC-GATES` | `RS-CFD-LBM-CODEGEN-20260910` |
| `RS-CFD-PRIOR-ART-AUDIT` | `RS-CFD-PRIOR-ART-AUDIT-20260910` |

Eight rows were already covered by immutable V2 publications on current main before this completion transaction (with cancellation represented by two narrower canonical tasks and independent benchmarking incorporated into trajectory verification). Only the two genuinely missing residual tasks are newly published here. Historical drafts remain provenance, not a second task machine.

## Preserved files in this directory

- `prior_local_main_results.json`: exact earlier local main-task benchmark/result JSON.
- `prior_taskset_manifest.json`: exact earlier local nine-draft manifest, preserved as historical metadata.
- `RAW_VORTEX_INTERFACE.md`: exact earlier pressure/raw-vortex interface provenance note.
- `completion_preflight.json`: scoped equivalent publication preflight for the two new tasks.

The local archive also contained helper scripts and generated draft taskbooks. Their operative mathematical/engineering source is either already in `prior_3d/probe.py`, captured by the exact result/provenance files above, or superseded by the canonical taskbooks listed in the mapping. No stale statement that remote publication was unavailable is treated as current state.
