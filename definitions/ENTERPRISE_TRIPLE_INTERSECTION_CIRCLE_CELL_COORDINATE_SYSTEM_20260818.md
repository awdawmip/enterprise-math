# Enterprise Math — Triple-Intersection Circle-Cell Coordinate System (Historical Draft)

Status: `SUPERSEDED / HISTORICAL`
Date: `2026-08-18`
Superseded: `2026-08-20`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

This draft is retained only as historical provenance.

It is superseded by:

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

Canonical superseding changes include:

- native origin remains the real triple-intersection point `O_E=0`;
- every circle remains a native cell;
- cell identity is by its discrete center;
- nearest-neighbor cell-center spacing is normalized to `1`;
- every cell radius is `1/sqrt(3)` rather than `1`;
- neighboring cells overlap with positive area;
- the full circle-cell family covers the plane without gaps;
- every circle-boundary intersection is a triple-cell intersection;
- the native axes are **three positive rays parallel to center-center directions**, not angular bisectors;
- no native negative axes are required;
- cell centers carry nonnegative integer three-axis addresses modulo common diagonal shift, canonically normalized by `min(a,b,c)=0`;
- the native three-axis metric is the A2-type quadratic form
  `L_E^2=a^2+b^2+c^2-ab-bc-ca`,
  not the direct orthogonal square sum.

Do not use this 2026-08-18 draft as current foundation except for historical comparison.
