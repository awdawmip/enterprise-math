# R059D Stage AC — Enterprise Square / Root Native Triangle Law

Researcher-ID: `EM-R059D-7C2A91`

Task: `RS-R059D-STAGE-AC-ENTERPRISE-SQUARE-ROOT-NATIVE-TRIANGLE-LAW`

## Primary disposition

`N1_N2_CONTROLS_UNDERDETERMINE_NATIVE_EXTENSION`

Stage AC independently constructs the canonical Enterprise-orthogonal triangle carrier `T_n`, enumerates exact discrete readouts through `n=256`, and proves the resulting recurrences symbolically. The candidate triangular root law is mathematically valid for one predeclared native readout branch, but it is **not uniquely selected** by the frozen geometry and the two supplied controls.

## Native construction

The implementation chart writes `(p,q)` for repository point `(p,-q,0)` and uses only the declared Enterprise-axis adjacency relations. The chart is I0 only; it does not redefine the Enterprise plane as rank 2.

The canonical triangle has vertex carrier

`D_n={(p,q) in Z_{≥0}^2 : p+q≤n}`

with three unit-adjacency boundary families corresponding to the two generating rays and the closing Enterprise-axis family.

An orientation-preserving translated `T_1` motif has vertices

`{(i,j),(i+1,j),(i,j+1)}`

for `i,j≥0`, `i+j≤n-1`.

No formula `3n`, triangular number, Euclidean area, or classical square root appears in the native generator.

## Area readout

The predeclared area primitive counts typed unit adjacency incidences on the three triangle sides.

Each new layer contributes exactly three incidence labels:

`(OU,n), (OV,n), (UV,n)`.

Hence

`A_0=0`, `A_n=A_(n-1)+3`,

and exact induction proves

`A_n=3n`.

Status:

`AREA_LAW_STATUS = THREE_SIDE_INCIDENCE_AREA_LAW_PROVED`

This is a rebuilt G1/N2 Enterprise readout, not Euclidean perimeter, Euclidean area, or an N0 packet weight.

## Root readout: two surviving exact branches

Before global scoring, two simple root primitives survived the frozen controls `R_1=1`, `R_2=3`.

### Branch A — all orientation-preserving T1 occurrences

Count

`P_n={(i,j): i,j≥0, i+j≤n-1}`.

Layer `n` contributes exactly the `n` indices satisfying `i+j=n-1`. Therefore

`R_full(0)=0`, `R_full(n)=R_full(n-1)+n`,

and exact symbolic derivation gives

`R_full(n)=n(n+1)/2`.

So the candidate triangular law is **proved conditional on selecting this primitive**.

### Branch B — T1 occurrences attached to either generating ray

Count only motifs with `i=0` or `j=0`. For `n≥1`, each set has `n` members and their only overlap is `(0,0)`, hence

`R_two_ray(n)=2n-1`.

This branch is symmetric under interchange of the two generating rays, uses only task-declared structure, and also satisfies

`R_1=1`, `R_2=3`.

## First unsupplied discriminator

At `n=3`, the common independently derived area is

`A_3=9`,

but the two root readouts are

`R_full(3)=6`,

`R_two_ray(3)=5`.

Thus the frozen data do not determine whether the next Enterprise root pair is `9↔6` or `9↔5`.

This is not finite-sample uncertainty. Both branches have exact set definitions and exact symbolic closed forms. No frozen primitive-selection theorem chooses the triangular branch over the two-ray branch.

Status:

`ROOT_LAW_STATUS = UNDERDETERMINED_NATIVE_EXTENSION`

## Enterprise square/root inversion

Once either root readout is selected, mutual inversion on the canonical triangle domain is exact because `A(n)=3n` is injective and both root readouts are strictly increasing.

Full-T1 branch:

`ENTERPRISE_ROOT_full(3n)=n(n+1)/2`

`ENTERPRISE_SQUARE_full(n(n+1)/2)=3n`

Two-ray branch:

`ENTERPRISE_ROOT_two_ray(3n)=2n-1`

`ENTERPRISE_SQUARE_two_ray(2n-1)=3n`

Both reproduce all four frozen operation controls. Therefore the operation pair is not yet unique.

`T_0` degenerates to the single origin and has zero side incidences and zero motifs, so both surviving branches naturally support `0↔0` on this degenerate triangle extension.

Status:

`INVERSION_STATUS = UNDERDETERMINED_BETWEEN_TWO_EXACT_NATIVE_READOUT_BRANCHES`

## Relation to earlier R059D

Only after the AC laws were independently derived was the full-T1 branch compared with Stage AA. Its increment `ΔR_full(n)=n` matches the old orbit-frontier sequence `|O2(k)|=k+1` under the comparison index `k=n-1`.

This is a compatibility match, not a selection theorem. The two-ray branch has later increment `2` and does not match. Therefore Stage AA's earlier no-go remains valid and is not retroactively overwritten.

`PRIOR_R059D_BRIDGE_STATUS = DIAGNOSTIC_COMPATIBILITY_ONLY__EXACT_SELECTION_BRIDGE_OPEN`

No exact bridge to historical BRC collapse coordinates is established; a separate bridge stage is still required.

## Classical compatibility

`ENTERPRISE_ROOT` and `ENTERPRISE_SQUARE` remain distinct from classical `sqrt` and `x^2`. Classical values are recorded only after native generation and do not enter the generator or symbolic proof.

## Verification

Exact native enumeration covers `n=1..256` plus the degenerate `n=0` control. The deterministic checker performs 1,318 checks covering replay of every generated row, the supplied controls, the `n=3` discriminator, independent symbolic recurrence certificates, underdetermination/inversion semantics, and target-leakage scanning.

CI is not required for this research checkpoint.

## Final status

- `AREA_LAW_STATUS = THREE_SIDE_INCIDENCE_AREA_LAW_PROVED`
- `ROOT_LAW_STATUS = UNDERDETERMINED_NATIVE_EXTENSION`
- `INVERSION_STATUS = UNDERDETERMINED_BETWEEN_TWO_EXACT_NATIVE_READOUT_BRANCHES`
- `PRIOR_R059D_BRIDGE_STATUS = DIAGNOSTIC_COMPATIBILITY_ONLY__EXACT_SELECTION_BRIDGE_OPEN`
- Primary disposition: `N1_N2_CONTROLS_UNDERDETERMINE_NATIVE_EXTENSION`

`STOP_FOR_DRIVER_REVIEW`
