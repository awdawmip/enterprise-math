# R059D correction — triaxial raw vector coordinates before collapse

Status: `PROJECT_RESEARCH_CORRECTION_ANCHOR`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## Correction

The current line of thought must distinguish two objects that were previously conflated:

1. `RAW_TRIAXIAL_VECTOR_COORDINATE`: the simultaneous readings of one plane vector on all three relational number axes;
2. `COLLAPSED_INTEGER_CELL_ADDRESS`: the completed integer address assigned to a crystal cell after collapse.

The transfer bookkeeping vectors such as `(1,-1,0)` are not to be assumed to be the raw three-axis readings of the geometric/relational vector before collapse.

## Local six-neighbor calibration candidate

Take three oriented reference axes `a,b,c` in one relational plane, with the positive directions cyclically balanced and `a+b+c=0`. Under the symmetric projection/readout calibration where a unit axis has self-readout `1` and equal transverse readouts `-1/2`, the six nearest radial directions around the origin have raw triaxial readouts:

- `+a : ( 1,   -1/2, -1/2)`
- `-c : ( 1/2,  1/2, -1  )`
- `+b : (-1/2,  1,   -1/2)`
- `-a : (-1,    1/2,  1/2)`
- `+c : (-1/2, -1/2,  1  )`
- `-b : ( 1/2, -1,    1/2)`

A consistent ring-one integer-address orientation can be recorded as:

- `+a -> ( 1,-1, 0)`
- `-c -> ( 1, 0,-1)`
- `+b -> ( 0, 1,-1)`
- `-a -> (-1, 1, 0)`
- `+c -> (-1, 0, 1)`
- `-b -> ( 0,-1, 1)`

This table is a calibration hypothesis to be proved/retyped, not a native collapse law yet.

## Main scientific target

Instead of guessing BRC selectors abstractly, explicitly label the crystal cells around the origin with:

- raw simultaneous three-axis readouts;
- completed integer cell addresses;
- componentwise up/down collapse events from the raw readout to the integer address.

Then infer the collapse-direction grammar from the resulting exact local atlas.

For example, under the table above:

`(1,-1/2,-1/2) -> (1,-1,0)`

means the two equal transverse half-values do not both collapse the same way: one goes to `-1`, the other to `0`. Around the six-cell ring the assignment rotates cyclically, and inversion must map the positive-direction collapse pattern to the exact negative pattern.

The target is to determine whether this local coordinate atlas itself reveals the internal collapse rule, before introducing stabilizer/post-credit machinery.

## Firewalls

- Do not identify raw triaxial readout with collapsed cube/integer address.
- Do not assume `(1,-1,0)` is the precollapse coordinate of the corresponding vector.
- Do not use the superseded Stage-V post-credit pullback route as the next active scientific mechanism.
- Do not hard-code a nearest-rounding selector.
- Do not promote Euclidean projection as native without a later refoundation proof; it is currently a calibration/readout candidate used to expose the coordinate pattern.
- Preserve all previously frozen negative theorems only within their stated scopes.

## Immediate next experiment

Before another large taskbook, construct the exact radius-1 and radius-2 cell-coordinate atlas around the origin and test:

1. whether raw triaxial vector readouts compose consistently under translation;
2. whether each completed cell address is recovered by a deterministic cyclic component-collapse pattern;
3. whether the collapse pattern is covariant under the sixfold plane symmetry and inversion;
4. whether the pattern generalizes from the six nearest cells to the next shell without adding an arbitrary selector.

Only after this atlas is understood should a new BRC stage be issued.
