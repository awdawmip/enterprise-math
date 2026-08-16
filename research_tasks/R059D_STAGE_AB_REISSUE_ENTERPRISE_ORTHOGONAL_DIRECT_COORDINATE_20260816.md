# R059D Stage AB REISSUE — SUPERSEDED

Task-ID: `RS-R059D-STAGE-AB-REISSUE-ENTERPRISE-ORTHOGONAL-DIRECT-COORDINATE`
Generation: `R059D`
Stage: `AB REISSUE`
Status: `SUPERSEDED_DO_NOT_EXECUTE`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-16`

## Supersession reason

This taskbook was issued before the project-level native Enterprise-axis definition was corrected.

It incorrectly reduced the Enterprise plane to a rank-2 direct-coordinate generator and therefore conflicts with the now-authoritative project definition.

Authoritative source surfaces now freeze:

- `ENTERPRISE_DIMENSION = NATIVE_UNDIRECTED_AXIS_FAMILY_COUNT`;
- Enterprise plane = `3` Enterprise dimensions / `3` axes / `6` directed directions;
- the three Enterprise-plane axis families are pairwise `ENTERPRISE_ORTHOGONAL`;
- plane signs alternate across every adjacent `60°` direction;
- our solid spatial world = `6` Enterprise dimensions / `6` axes / `12` directed directions;
- the twelve-direction alternating-sign system closes across four three-dimensional Enterprise subplanes and is unique up to global sign inversion;
- the historical A2/C6 rank-2 carrier is compatibility / implementation structure only, not native Enterprise dimension authority.

See:

- `PROJECT_DEFINITION.md`
- `PROJECT_DEFINITION.zh-CN.md`
- `project_definition.json`
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`

The historical full taskbook remains recoverable from Git history at source commit `0309d08f789bb541301024314b1be18e13a6142a`.

Do not execute the research branch `research/r059d-stage-ab-reissue-enterprise-orthogonal-coordinate` as an active task under the superseded semantics.
