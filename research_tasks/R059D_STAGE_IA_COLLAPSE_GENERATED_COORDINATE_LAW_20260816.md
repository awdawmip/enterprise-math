# R059D Stage IA — SUPERSEDED / DO NOT EXECUTE

Task-ID: `RS-R059D-STAGE-IA-COLLAPSE-GENERATED-COORDINATE-LAW`
Generation: `R059D`
Stage: `IA`
Status: `SUPERSEDED_BY_DRIVER_REVIEW_OF_STAGE_AA`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-16`

## Supersession reason

This task was opened after an incorrect separation of two things that are in fact the same R059D scientific problem:

- identifying the collapse / branch-selection law;
- generating the stored integer coordinate.

The active R059D Stage-AA route already studies exactly the missing coordinate-generating decision on the symmetric primary ray: whether and when the realized staircase coordinate `a_n` advances from `k` to `k+1`, using only information available at the current step and without preloading a future schedule.

Stage AA therefore remains the authoritative continuation. Its failure/success is directly evidence about whether the presently frozen native state can generate the coordinate.

Do not execute a parallel Stage IA coordinate-generator search. Do not create a second coordinate line.

## Current control point

Stage AA frozen owner head:

`a6d57c6a20942b7b6628c1b20802e2219307d0dd`

Stage-AA frozen result includes:

- `SWAP_ORBIT_FRONTIER_COUNT_K_PLUS_1_ESTABLISHED=true`;
- `PRIMARY_GAP_TO_SWAP_ORBIT_FRONTIER_COUPLING_NOT_ESTABLISHED=true`;
- `LOW_N_N3_REMAINS_UNDERDETERMINED=true`;
- `ROOT_DEGREE_REMAINS_UNIDENTIFIED=true`;
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED=true`.

This means the coordinate-generating branch decision remains unidentified under the current native observables. The next Driver action must continue from Stage-AA diagnostics, not restart coordinate generation under a separate stage name.

Historical details of the withdrawn IA proposal remain available in Git history at commit:

`1c6b496f9330697428dfde710d67a18d039b8566`.
