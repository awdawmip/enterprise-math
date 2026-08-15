# R059D Stage-J Parallel Researcher Identity Map

Date: 2026-08-15
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Status: `DRIVER_CONTROL_PLANE_IDENTITY_CORRECTION`

## Purpose

Two R059D Stage-J executions overlapped in time after the Driver superseded the original graded-relay Stage-J task with the BRC6 next-channel-selection reissue.

They must remain separate researcher lanes.

## Lane A — old graded-relay Stage J

- Researcher-ID: `EM-R059D-4C7E21`
- Taskbook: `research_tasks/R059D_STAGE_J_GRADED_RELAY_COUPLING_LOCALIZATION_20260815.md`
- Taskbook source: `4cf097ff21a9275805fb8ab49cefdd5ff42c4c92`
- Owner branch: `research/r059d-stage-j-graded-relay-coupling-localization`
- Driver status: `SUPERSEDED_SIDE_RESULT_ONLY`

Any result from this lane remains attributable to `EM-R059D-4C7E21` and must not be merged into the BRC6 Stage-J result merely because both carry generation label R059D Stage J.

## Lane B — BRC6 reissue Stage J

- Control-plane Researcher-ID: `EM-R059D-9C6B2A`
- Taskbook: `research_tasks/R059D_STAGE_J_BRC6_NEXT_CHANNEL_SELECTION_ALGEBRA_REISSUE_20260815.md`
- Taskbook source: `3ca99589c5c3ade32c9cc164cdc3b3c4f6e15b7b`
- Owner branch: `research/r059d-stage-j-brc6-next-channel-selection`
- Frozen result head: `9f2b70d6cca5ccd66a46cc6dd18730f40a6add72`
- Frozen provenance parent: `03650b38df5950b86cb2636db9e43094683b1bc8`
- Driver status: `AUTHORITATIVE_BRC6_MAINLINE`

### Identity-label collision note

The already-frozen BRC6 Stage-J artifacts and commit messages contain the stale embedded label `EM-R059D-4C7E21` because the second researcher executed before a distinct ID had been assigned.

This is a provenance-label reuse only. The taskbook source, owner branch, frozen parent, and result head uniquely identify the BRC6 execution as the separate Lane B above.

Do not rewrite or mutate the frozen BRC6 artifacts to replace the embedded ID. From this control-plane record forward, the authoritative Researcher-ID for the BRC6 lane is:

`EM-R059D-9C6B2A`.

## Mandatory disambiguation rule

For any later Stage-J result/review, identify lane by the tuple:

`(Researcher-ID, taskbook source, owner branch, provenance parent/result head)`.

Never identify solely by `R059D Stage J` or by the stale embedded researcher label inside frozen BRC6 artifacts.
