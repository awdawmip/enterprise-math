# R059D Stage AC — ENTERPRISE SQUARE / ROOT NATIVE TRIANGLE LAW

Task-ID: `RS-R059D-STAGE-AC-ENTERPRISE-SQUARE-ROOT-NATIVE-TRIANGLE-LAW`
Generation: `R059D`
Stage: `AC`
Status: `DRIVER_APPROVED_TASKBOOK`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Researcher-ID: `EM-R059D-7C2A91`
Date: `2026-08-16`

## 0. Mission

Determine the native law behind the newly named operations:

- `ENTERPRISE_ROOT` / 进取开方
- `ENTERPRISE_SQUARE` / 进取平方

using only the frozen Enterprise-plane geometry and exact discrete counting.

The user supplied two controls:

- `T_1=((0,0,0),(1,0,0),(0,-1,0))` has Enterprise area readout `3` and Enterprise edge/root readout `1`;
- `T_2=((0,0,0),(2,0,0),(0,-2,0))` has Enterprise area readout `6` and Enterprise edge/root readout `3`.

Therefore the only frozen operation controls at task start are:

`ENTERPRISE_ROOT(3)=1`

`ENTERPRISE_SQUARE(1)=3`

`ENTERPRISE_ROOT(6)=3`

`ENTERPRISE_SQUARE(3)=6`

The general law is OPEN.

Do not assume the candidate triangular-number law in the generator.

## 1. Frozen project geometry

Use the current project-level native axis definition:

- an Enterprise plane has `3` Enterprise dimensions / `3` native undirected axes / `6` directed directions;
- choose one directed axis direction as `+u`;
- every adjacent `60°` sector flips sign;
- the second ray used by `T_n` is the adjacent Enterprise-orthogonal direction represented in the frozen chart by `(0,-n,0)`;
- the three native axis families are pairwise `ENTERPRISE_ORTHOGONAL` in the project sense;
- Euclidean `90°`, Euclidean metric, Euclidean area and classical square root are compatibility-layer objects, not native premises.

Primary sources:

- `PROJECT_DEFINITION.zh-CN.md`
- `PROJECT_DEFINITION.md`
- `project_definition.json`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`

If lower-level historical A2/C6 documents conflict with the current project-level native dimension definition, the project-level definition controls.

## 2. Triangle family

For integer `n>=1`, define

`T_n = (O,U_n,V_n)`

with

`O=(0,0,0)`

`U_n=(n,0,0)`

`V_n=(0,-n,0)`.

This is the canonical two-axis Enterprise-orthogonal triangle family for this stage.

Do not replace it with a Euclidean right triangle or with an A2 rank-2 coordinate surrogate.

## 3. Required native construction

Construct `T_n` directly from the frozen Enterprise-plane directional structure.

For each `n`, expose enough exact combinatorial data to make the readouts independently replayable. At minimum record:

- the two axis rays from `O`;
- the closing boundary between `U_n` and `V_n` under the native adjacency relation;
- all elementary native layers / packets / incidences used by the area readout;
- all elementary native layers / packets / incidences used by the edge/root readout;
- the incremental contribution from layer `n` relative to `n-1`;
- exact provenance from raw geometry to final integer readout.

The implementation may discover the correct primitive count, but it must not define the primitive count by the target formula.

## 4. Target-leakage prohibition

The following are hypotheses to test, NOT premises:

`H_AREA: A_n = 3n`

`H_ROOT: R_n = n(n+1)/2`

`H_DELTA_ROOT: R_n-R_{n-1}=n`

`H_SQUARE: ENTERPRISE_SQUARE(n(n+1)/2)=3n`

The enumeration/generator must be able to run with these formulas removed from source.

Allowed use of the hypotheses:

- after native values are generated, compare observed values against the hypotheses;
- after the finite sequence is observed, attempt a symbolic proof from the actual primitive construction.

Forbidden:

- using `3*n` as the area generator;
- using `n*(n+1)//2` as the root generator;
- using a lookup table seeded from the expected sequence;
- selecting among ambiguous native counts by whichever one matches the expected formula.

If multiple equally native constructions reproduce `n=1,2` but diverge later, report underdetermination.

## 5. Deterministic enumeration

Run exact integer enumeration for at least

`1 <= n <= 64`.

Use a larger bound if cheap, preferably `n<=256`.

For every `n`, record:

- `n`;
- triangle vertices;
- native area readout `A_n`;
- native root/edge readout `R_n`;
- first differences `Delta A_n`, `Delta R_n`;
- second differences where defined;
- primitive-count provenance;
- whether the output matches each candidate hypothesis.

No floating point is needed for the native theorem.

Classical values such as `sqrt(3n)` may be printed only in a clearly separated compatibility table and must not feed the native generator.

## 6. Theorem extraction

After enumeration, attempt exact symbolic derivation.

### 6.1 Area law

If the native construction yields constant per-layer area increment, prove the exact recurrence and closed form from primitive geometry.

Do not call `A_n=3n` established merely because 64 samples match.

### 6.2 Root law

If the native construction yields layer increments

`1,2,3,...`,

prove why layer `n` contributes exactly `n` native units.

Only after that may the triangular-number closed form be promoted:

`R_n = 1+2+...+n = n(n+1)/2`.

### 6.3 Enterprise square / root inversion

If both laws are proved, characterize the legal native domain and prove mutual inversion on that domain.

Candidate legal sets, to be proved or refuted rather than assumed:

`ROOT_DOMAIN = {3n : n>=1}`

`ROOT_RANGE = {n(n+1)/2 : n>=1}`

`SQUARE_DOMAIN = ROOT_RANGE`

`SQUARE_RANGE = ROOT_DOMAIN`.

Then prove or refute:

`ENTERPRISE_ROOT(3n)=n(n+1)/2`

and

`ENTERPRISE_SQUARE(n(n+1)/2)=3n`.

Also determine whether `0` should be admitted naturally:

`ENTERPRISE_ROOT(0)=0`

`ENTERPRISE_SQUARE(0)=0`.

Do not add `0` by convention unless the degenerate native geometry justifies it.

## 7. Discriminator cases

At minimum expose exact native derivations for:

- `n=1` -> controls `3 <-> 1`;
- `n=2` -> controls `6 <-> 3`;
- `n=3` -> first unsupplied discriminator;
- `n=4`;
- `n=5`;
- `n=8`;
- `n=16`;
- the maximum enumerated `n`.

The most important first new observation is `n=3`.

If native geometry does NOT produce the candidate `A_3=9`, `R_3=6`, stop the formula-promotion route and report the exact observed values and primitive reason.

## 8. Relation to earlier R059D root/frontier work

Historical R059D W/X/Y/Z/AA work must remain immutable.

This stage may compare the newly derived sequence with prior staircase / frontier / triangular-threshold candidates only AFTER the native geometric law is independently obtained.

Required comparison questions:

1. Does Stage AC give an intrinsic geometric origin for the old triangular-threshold candidate?
2. Does it explain why Stage AA could observe a triangular sequence without being able to select it natively from the old frontier state?
3. Which old claims become retyped as compatibility observations rather than generators?
4. Does this new geometry establish any bridge theorem to earlier BRC root-collapse experiments, or is a separate bridge stage still required?

No historical result may be rewritten as if it had already proved Stage AC.

## 9. Enterprise vs classical operation semantics

Keep two columns throughout:

- native Enterprise operation;
- classical compatibility-layer operation.

Hard semantic separation:

`ENTERPRISE_ROOT(3)=1`

is NOT the classical statement

`sqrt(3)=1`.

Likewise `ENTERPRISE_SQUARE(1)=3` is NOT `1^2=3` in classical arithmetic.

Stage AC studies a new geometry-defined operation pair.

## 10. Required artifacts

Freeze at least:

1. `R059D_STAGE_AC_TRIANGLE_FAMILY_PROTOCOL.json`
2. `R059D_STAGE_AC_NATIVE_AREA_PRIMITIVE.json`
3. `R059D_STAGE_AC_NATIVE_ROOT_PRIMITIVE.json`
4. `R059D_STAGE_AC_ENUMERATION_N1_NMAX.json`
5. `R059D_STAGE_AC_LAYER_INCREMENT_LEDGER.json`
6. `R059D_STAGE_AC_AREA_LAW_PROOF.json`
7. `R059D_STAGE_AC_ROOT_LAW_PROOF.json`
8. `R059D_STAGE_AC_SQUARE_ROOT_INVERSION_PROOF.json`
9. `R059D_STAGE_AC_CLASSICAL_COMPATIBILITY_TABLE.json`
10. `R059D_STAGE_AC_PRIOR_STAGE_BRIDGE_LEDGER.json`
11. deterministic checker source
12. deterministic checker output
13. report
14. manifest
15. frozen checkpoint

All artifacts under:

`research_results/R059D_STAGE_AC/`

## 11. Checker requirements

Checker must reject at minimum:

- `TARGET_FORMULA_USED_AS_GENERATOR`;
- `TRIANGULAR_LOOKUP_TABLE_SEEDED`;
- `CLASSICAL_SQRT_USED_TO_DEFINE_ENTERPRISE_ROOT`;
- `EUCLIDEAN_AREA_USED_AS_NATIVE_AREA_PREMISE`;
- `A2_RANK2_DIMENSION_OVERRIDES_ENTERPRISE_PLANE_DIMENSION`;
- `N1_N2_CONTROLS_FAIL`;
- `FINITE_MATCH_PROMOTED_TO_THEOREM_WITHOUT_SYMBOLIC_DERIVATION`;
- `AMBIGUOUS_NATIVE_PRIMITIVE_SILENTLY_RESOLVED_BY_TARGET_MATCH`;
- `ENTERPRISE_ROOT_AND_CLASSICAL_SQRT_CONFLATED`;
- `HISTORICAL_R059D_RESULT_MUTATED`.

If a theorem is claimed, checker must verify its symbolic certificate / recurrence certificate independently of the finite enumeration table.

## 12. Required disposition

Return exactly one primary disposition:

- `ENTERPRISE_TRIANGLE_LAW_PROVED__SQUARE_ROOT_PAIR_ESTABLISHED`
- `ENTERPRISE_TRIANGLE_SEQUENCE_ESTABLISHED__GENERAL_PROOF_OPEN`
- `NATIVE_GEOMETRY_SELECTS_DIFFERENT_LAW`
- `N1_N2_CONTROLS_UNDERDETERMINE_NATIVE_EXTENSION`
- `SEMANTIC_HARD_STOP`

Also report separately:

- `AREA_LAW_STATUS`
- `ROOT_LAW_STATUS`
- `INVERSION_STATUS`
- `PRIOR_R059D_BRIDGE_STATUS`

Then stop for Driver review.

## 13. Git / ownership discipline

Work only on:

`research/r059d-stage-ac-enterprise-square-root-triangle-law`

Do not modify frozen prior-stage artifacts.

Commit intermediate checkpoints rather than one giant final commit.

At completion leave the working branch internally consistent and provide exact:

- branch head SHA;
- frozen parent SHA;
- checker digest;
- checkpoint digest;
- artifact manifest digest.

Do not merge to `main` without Driver review.
