# R059D Stage W Driver Review — Homogeneity Trivialization

Date: 2026-08-16
Driver: EM-DVR-R0457K / CONTROL_PLANE
Researcher-ID: EM-R059D-9C6B2A
Reviewed owner branch: `research/r059d-stage-w-triaxial-integer-cell-root-collapse-atlas`
Reviewed final head: `8f6ecd12146cac254e5b0668a1bb59e8a21961c4`
Frozen parent: `a9929a5bd666e621cb1bd77adb464df0d35db399`
Taskbook source: `ce0c98cb2e729d8773443b1f3ebdf8fb4328365b`

## Driver disposition

`EXECUTION_INTEGRITY_PASS__SCIENTIFIC_TARGET_RETYPE_REQUIRED`

The Stage-W artifacts are preserved immutable, but the conclusions

- `P1_IDENTITY_UNIQUE...`
- `SQUARE_ROOT_PRECOLLAPSE_REJECTED...`

MUST NOT be promoted as conclusions about the intended triaxial integer-cell collapse ontology.

## Reason

The researcher introduced an additional W0 premise:

`translation_homogeneity = a named direction has the same stored coordinate increment at every cell`.

Together with the first-step control

`+u -> (1,-1,-1)`

this forces

`coord(n * +u) = (n,-n,-n)`

before the root-family test begins.

That assumption rules out by construction the user-target mechanism in which, for example,

`+u first cell -> (1,-1,-1)`

but the second-cell transverse precollapse values may be

`-sqrt(2), -sqrt(2)`

and only after integer completion become something such as

`(2,-1,-1)`.

The taskbook explicitly required underdetermination to be recorded if first-shell controls were insufficient; it did not authorize a homogeneous additive stored-coordinate law.

Therefore the W result is a valid negative control only:

`HOMOGENEOUS_ADDITIVE_COORDINATE_MODEL_TRIVIALIZES_TO_P1_AND_EXCLUDES_NONLINEAR_ROOT_COLLAPSE_BY_CONSTRUCTION`.

It does not adjudicate the intended nonhomogeneous cell-count/root-collapse model.

## Preserved useful results

- provenance and parent immutability PASS;
- checker 1918/1918 PASS for the model actually implemented;
- integer-only stored-coordinate typing remains valid;
- old zero-sum raw coordinate ontology remains inapplicable to the user-supplied `(1,-1,-1)` control;
- the W0 homogeneous model is now a frozen rejection/control model.

## Superseded scientific freezes

The following Stage-W statements are model-conditional and must not be consumed as project-wide facts:

- `SQUARE_ROOT_PRECOLLAPSE_REJECTED_BY_THIRD_SHELL_WITHIN_W0_ATLAS`;
- `P1_IDENTITY_UNIQUE_WITHIN_TESTED_ROOT_ORDER_REGISTRY_AND_RADIUS3`;
- `FIVE_TO_FOUR_OR_NINE_NOT_ADJUDICATED_BECAUSE_SQRT_MODEL_REJECTED`.

They remain true only under the unauthorized-for-target W0 homogeneous coordinate model.

## Next

Reissue Stage W from the Stage-U frozen parent, not from the first-round W head.

The reissue must freeze a strict firewall:

- cell identity may have homogeneous adjacency structure;
- STORED TRIAXIAL COORDINATES may NOT be assumed additive, translationally homogeneous, or path-summable;
- `C(cell+d)-C(cell)=C(d)` is forbidden unless independently derived;
- `C(nu)=nC(u)` is forbidden unless independently derived;
- first-shell controls constrain only first shell;
- pure-axis transverse integer sequences are unknown and must be inferred from count-derived precollapse values and multi-path/off-axis consistency.
