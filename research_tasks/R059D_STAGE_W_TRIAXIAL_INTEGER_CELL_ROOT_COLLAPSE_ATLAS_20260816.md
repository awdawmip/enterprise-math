# R059D Stage W — Triaxial Integer-Cell Root-Collapse Atlas

Task-ID: `RS-R059D-STAGE-W-TRIAXIAL-INTEGER-CELL-ROOT-COLLAPSE-ATLAS`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-w-triaxial-integer-cell-root-collapse-atlas`
Frozen parent: `a9929a5bd666e621cb1bd77adb464df0d35db399`

## 0. Supersession / scope reset

This Stage W is a deliberate conceptual reset after the Driver/user correction on 2026-08-16.

The previously issued Stage V post-credit/stabilizer continuation was **superseded before execution**. Do not execute it and do not import its proposed selector mechanism as a premise here.

The older provisional branch `research/r059d-stage-w-triaxial-cell-coordinate-collapse` is also superseded before execution by this more precise Stage-W taskbook.

Stage U and earlier frozen artifacts remain immutable historical results. They may be used only as controls where explicitly requested below; they are not the answer to this experiment.

## 1. Core correction to freeze before any calculation

This task distinguishes three types that MUST NOT be conflated:

1. `INTEGER_CELL_COORDINATE`
   - the stored address/readout of a crystal cell on the three-axis coordinate system;
   - every coordinate component is an integer;
   - no fractional or irrational cell coordinate is legal.

2. `PRECOLLAPSE_ALGEBRAIC_VALUE`
   - an intermediate number generated from integer cell counts/relations before completion;
   - may be irrational (e.g. `sqrt(2)`), but is NOT a cell coordinate;
   - must not be stored or described as a crystal-cell address.

3. `COLLAPSE/COMPLETION`
   - maps the precollapse algebraic value to an admissible integer coordinate layer according to a rule that must be inferred from global cell-grid self-consistency;
   - do NOT assume nearest-integer rounding, floor, ceiling, midpoint threshold, probability, or arbitrary branch preference.

Freeze the user-supplied first-step control:

- origin `O = (0,0,0)`;
- one step in `+u` has integer cell coordinate `U1 = (1,-1,-1)`;
- by cyclic axis relabeling, candidate one-step controls are:
  - `+u : (1,-1,-1)`
  - `+v : (-1,1,-1)`
  - `+w : (-1,-1,1)`
  - negatives obtained by exact sign inversion, unless the atlas itself refutes this symmetry.

Important: this task does **NOT** assume the old zero-sum carrier sheet `x+y+z=K`. In fact `(1,-1,-1)` is a direct control against imposing that as the raw integer cell-coordinate law.

Do not use `e_i-e_j`, `x+y+z=K`, or Stage-S/T transfer bookkeeping as a positive premise for the new integer-cell coordinate atlas unless the new atlas independently recovers an equivalent relation in its own typing.

## 2. Scientific target

The target is intentionally elementary:

> Number nearby crystal cells, assign their integer three-axis coordinates, enumerate multiple paths to the same cell, and infer whether the non-primary axis count is generated through a root-like precollapse law whose completion to integers is forced by atlas consistency.

The working example to TEST (not assume as theorem):

- after one `+u` step: integer coordinate `(1,-1,-1)`;
- after two `+u` steps, a candidate precollapse relation is `(2,-sqrt(2),-sqrt(2))`;
- completion may then give `(2,-1,-1)` or another integer address depending on the globally self-consistent rule.

The task must decide whether square-root structure is supported, rejected, underdetermined, or only one member of a broader root family.

## 3. Stage W0 — Semantic freeze and minimal neighborhood

Before fitting any root law, construct the exact combinatorial neighborhood around the origin using only:

- crystal cells;
- adjacency;
- named three-axis directions `u,v,w` and their negative orientations;
- unit transition events;
- integer coordinate labels.

Required:

- origin;
- all 6 first-neighbor cells;
- all distinct cells reachable in exactly 2 adjacency transitions;
- all distinct cells reachable in exactly 3 adjacency transitions, if computationally modest.

Every cell must have:

- a stable cell ID independent of path;
- every shortest and selected non-shortest path from origin up to the tested radius;
- candidate integer coordinate triples derived from the frozen local direction semantics;
- explicit duplicate/recoalescence resolution when multiple paths reach the same cell.

Do not identify cells merely because a guessed coordinate formula says they are equal. Cell identity must come first from the frozen adjacency construction; coordinates are then tested against that identity.

## 4. Stage W1 — Integer coordinate atlas

Construct `TRIAXIAL_INTEGER_CELL_ATLAS` for radius at least 2, preferably 3.

For each cell record:

- cell ID;
- graph shell / transition distance from origin (bookkeeping only; do not call geometric length);
- all path words used to reach it;
- integer coordinate triple `(u,v,w)`;
- sign pattern;
- axis permutations / inversion images;
- neighboring cell IDs.

Hard gates:

- all stored cell coordinates are integers;
- one real adjacency transition must map to one neighboring cell;
- a cell reached by two different paths must receive one and only one integer coordinate triple;
- inverse path must return exactly to the prior cell/address;
- cyclic relabeling `u->v->w->u` and global sign inversion must be audited, not silently assumed if the atlas contradicts them.

If the initial one-step coordinate controls alone are insufficient to assign unique further coordinates, record the underdetermination rather than inventing a law.

## 5. Stage W2 — Root-family candidate generation from cell counts

Now, and only now, fit simple elementary candidate relations between a primary-axis integer count `n` and the other two axes' PRECOLLAPSE ALGEBRAIC VALUES.

Test finite low-order root families such as:

`r_p(n) = n^(1/p)` for integer `p = 1,2,3,4,5,6`

plus only very simple count-derived alternatives that can be expressed using elementary-school algebra/arithmetic and are motivated by the atlas.

For a `+u` ray candidate, a symmetric root model may take the form:

`PRE_u(n) = (n, -r_p(n), -r_p(n))`

but this form is a hypothesis to test, not a native axiom.

For every candidate root order `p`, build an exact table for at least `n=0..N`, where `N` reaches several completed powers (e.g. for square root at least beyond 16, preferably 25 or 36 if cheap).

Record:

- perfect `p`th powers;
- open intervals `k^p < n < (k+1)^p`;
- exact algebraic precollapse values where possible (symbolic radicals, not floating point as proof);
- legal integer completion candidates `k` and `k+1` for the root magnitude;
- resulting candidate integer coordinate triples after each possible completion.

Do NOT choose floor/ceiling/nearest yet.

## 6. Stage W3 — Collapse rule inferred by atlas self-consistency

For each candidate root order and each ambiguous `n`, propagate both legal integer completion possibilities into the nearby cell atlas.

Use only exact consistency constraints such as:

- same cell via different paths must have same integer coordinates;
- adjacency moves must land on already enumerated neighboring cells;
- inverse transition must undo the prior transition exactly;
- cyclicly equivalent situations must transform consistently if cyclic covariance survives W1;
- opposite orientation must transform consistently if inversion covariance survives W1;
- no two distinct cells may be forced to the same coordinate triple unless the atlas independently identifies them as the same cell;
- every enumerated cell must receive a coordinate if the candidate claims to cover the tested domain.

For each ambiguous completion point, keep a signed ledger:

`LOWER_COMPLETION`
`UPPER_COMPLETION`

with exact consequences and the first contradiction (if any).

The desired output is not a guessed threshold. The desired output is a table showing which branch is:

- `FORCED_LOWER_BY_ATLAS`
- `FORCED_UPPER_BY_ATLAS`
- `BOTH_SELF_CONSISTENT`
- `NEITHER_SELF_CONSISTENT`
- `NOT_YET_DECIDED_AT_TEST_RADIUS`

## 7. Stage W4 — Direct audit of the 5 -> 4 / 9 control

If and only if the square-root model survives earlier gates, explicitly retype the old scalar question:

`sqrt(5)` lies between integer coordinate levels `2` and `3`.

The corresponding square-count endpoints are `4` and `9`.

Audit whether the atlas forces:

- `sqrt(5) -> 2`, equivalently `5 -> 4`;
- `sqrt(5) -> 3`, equivalently `5 -> 9`;
- both remain possible;
- or the square-root model itself fails before this point.

No nearest rounding, midpoint, Euclidean distance, stabilizer, post-credit reward, or probability is allowed to settle this control.

If a different root order is selected by the atlas, construct the analogous completed-power control instead of forcing the old 5 example into it.

## 8. Stage W5 — Determine whether root order itself is forced

Compare all surviving low-order root candidates using the same fixed atlas.

Classify each candidate:

- `REJECTED_BY_FIRST_SHELL`
- `REJECTED_BY_SECOND_SHELL`
- `REJECTED_BY_THIRD_SHELL`
- `SURVIVES_TEST_RADIUS`
- `UNIQUE_SURVIVOR`
- `MULTIPLE_ROOT_ORDERS_SURVIVE`
- `NO_TESTED_ROOT_ORDER_SURVIVES`

Do not overclaim a unique universal law from a small radius. If square root is the only survivor through the tested radius, freeze only:

`SQUARE_ROOT_UNIQUE_WITHIN_TESTED_CANDIDATE_REGISTRY_AND_RADIUS`

not a universal physical theorem.

## 9. Stage W6 — Closed-form / recurrence extraction

If a consistent atlas and root/completion pattern emerges, try to express it in the simplest possible integer arithmetic form.

Priority order:

1. direct counting recurrence;
2. perfect-power interval rule;
3. elementary inequality rule;
4. only then a compact closed form.

Examples of acceptable elementary forms to investigate (NOT assume):

- largest integer `k` such that `k^p <= n`;
- smallest integer `k` such that `n <= k^p`;
- alternating / shell-dependent choice;
- path-dependent but globally reconcilable recurrence;
- a fixed interval partition forced by cell-count crossings.

Any rule must regenerate the integer atlas, not merely fit one ray.

## 10. Mandatory controls / anti-triviality

The researcher must explicitly test and preserve failures for:

- floor-only completion;
- ceiling-only completion;
- nearest-integer completion;
- midpoint threshold completion;
- alternating lower/upper by parity;
- arbitrary fixed donor/axis preference;
- old zero-sum `(x+y+z=K)` carrier rule;
- old transfer vector `(1,-1,0)` interpreted as raw cell coordinate.

These are controls, not allowed premises.

At least one off-axis/mixed-path cell must be used to distinguish models that fit the pure `+u` ray equally well.

## 11. Deterministic computation discipline

Primary proof mechanism must be exact integer/radical arithmetic and explicit finite cell enumeration.

Allowed:

- Python with integers, `fractions.Fraction`, symbolic radicals or exact polynomial comparisons;
- finite BFS/graph enumeration of the tiny local cell neighborhood;
- exact path/recoalescence tables.

Forbidden as proof mechanism:

- floating-point curve fitting;
- ML;
- numerical optimization;
- Euclidean coordinate embedding used to invent the rule;
- nearest-distance classification;
- exhaustive huge search over arbitrary formulas.

This should be solvable with elementary algebra plus exact bookkeeping.

## 12. Required artifacts

At minimum freeze:

1. `R059D_STAGE_W_INTEGER_CELL_COORDINATE_PROTOCOL.json`
2. `R059D_STAGE_W_ORIGIN_FIRST_SHELL_ATLAS.json`
3. `R059D_STAGE_W_RADIUS2_CELL_ATLAS.json`
4. `R059D_STAGE_W_RADIUS3_CELL_ATLAS.json` if computationally modest, else explicit reason omitted
5. `R059D_STAGE_W_MULTI_PATH_COORDINATE_CONSISTENCY.json`
6. `R059D_STAGE_W_ROOT_ORDER_CANDIDATE_REGISTRY.json`
7. `R059D_STAGE_W_ROOT_PRECOLLAPSE_TABLE.json`
8. `R059D_STAGE_W_COLLAPSE_BRANCH_CONSISTENCY_LEDGER.json`
9. `R059D_STAGE_W_FIVE_TO_FOUR_OR_NINE_CONTROL.json`
10. `R059D_STAGE_W_MODEL_REJECTION_LEDGER.json`
11. `R059D_STAGE_W_SIMPLE_RULE_EXTRACTION.json`
12. `R059D_STAGE_W_TRIVIALITY_LEAKAGE_LEDGER.json`
13. deterministic checker source/output
14. report
15. manifest
16. frozen checkpoint.

## 13. Required explicit statements in report

The report MUST state clearly:

- `CELL_COORDINATES_ARE_INTEGER_ONLY`;
- radicals are `PRECOLLAPSE_ALGEBRAIC_VALUES`, not coordinates;
- whether `(1,-1,-1)` one-step semantics is globally self-consistent;
- whether square root is supported/rejected/underdetermined;
- whether the collapse branch is forced by cell-atlas consistency;
- whether `5->4/9` is resolved, still ambiguous, or inapplicable;
- whether any rule survives off-axis/multi-path tests;
- exactly what remains unidentified.

## 14. Firewalls

Do not import as positive proof:

- Stage-U stabilizer selector calculus;
- Stage-V post-credit calculus;
- nearest rounding;
- probability;
- physical force/energy/strain;
- Euclidean angle/length/distance;
- zero-sum carrier sheet;
- old `e_i-e_j` transfer coordinate as raw cell address;
- hidden orientation preference.

Stage-U and earlier results remain preserved historically, but this experiment is explicitly testing whether the coordinate ontology underneath them was mis-typed.

## 15. Allowed outcomes

Positive and negative results are equally valid. Useful freezes include:

- `INTEGER_CELL_ATLAS_ESTABLISHED`
- `ONE_STEP_COORDINATE_1_NEG1_NEG1_CONFIRMED`
- `SQUARE_ROOT_PRECOLLAPSE_SUPPORTED`
- `SQUARE_ROOT_PRECOLLAPSE_REJECTED`
- `ROOT_ORDER_NOT_IDENTIFIED`
- `COLLAPSE_RULE_FORCED_BY_MULTI_PATH_SELF_CONSISTENCY`
- `COLLAPSE_RULE_REMAINS_MULTIBRANCH_AT_TEST_RADIUS`
- `FIVE_TO_FOUR_FORCED`
- `FIVE_TO_NINE_FORCED`
- `FIVE_TO_FOUR_OR_NINE_STILL_UNRESOLVED`
- `OLD_ZERO_SUM_TRANSFER_COORDINATE_ONTOLOGY_REJECTED_FOR_INTEGER_CELL_ATLAS`
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED`.

After all required artifacts and checks:

`STOP_FOR_DRIVER_REVIEW`.
