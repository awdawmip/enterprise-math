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

Use `rho=r+1`, where `rho` is native point-state level and `r` is primitive displacement / step radius.

## Consequences

- Keep all existing AO formulas in `r` as displacement-radius formulas.
- Use `rho` only for native point-state layer labels.
- Keep displacement coordinates and zero components at ordinary `0`.
- Do not reindex AG–AN formulas by mechanical substitution.
- Include a final semantic audit confirming point-state/displacement separation.

This changes semantics, not the AO hard mathematical target.