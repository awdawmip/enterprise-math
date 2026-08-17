# R059D Stage AO — Point-Origin Semantic Addendum

Status: `ACTIVE / MANDATORY_SEMANTIC_OVERRIDE`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Applies to: `RS-R059D-STAGE-AO-MACROSCOPIC-BRC-DENSITY-PROFILE-LIMIT`
Canonical definition: `definitions/ENTERPRISE_POINT_ORIGIN_AND_DISPLACEMENT_ZERO_20260817.md`

## Frozen override

Stage AO must distinguish:

`ENTERPRISE_POINT_STATE_ORIGIN = 1`

from

`ENTERPRISE_DISPLACEMENT_ZERO = 0`.

Use

`rho = r + 1`,

where `rho` is native point-state level and `r` is primitive displacement / step radius.

## Consequences for AO

1. Every existing AO formula using radius `r` continues to use **displacement radius**. Do not shift it to `r+1` inside recurrences, asymptotics, BRC weights or frontier formulas.
2. If a statement concerns the native ordinal/point-state layer itself, write `rho`, not `r`.
3. `r -> infinity` remains the displacement refinement limit; equivalently `rho -> infinity`, with `rho-r=1`.
4. Source/target comparison coordinates remain displacement coordinates; zero components remain `0`.
5. No AG–AN theorem is invalidated merely by this semantic split.
6. AO must include a short semantic audit in its final proof/checkpoint confirming that point-state labels and displacement coordinates were not conflated.

This addendum supersedes any implicit reading of AO's `r=0` as “nonexistence” or of coordinate `0` as the first native point-state. It does not alter the task's mathematical hard target.