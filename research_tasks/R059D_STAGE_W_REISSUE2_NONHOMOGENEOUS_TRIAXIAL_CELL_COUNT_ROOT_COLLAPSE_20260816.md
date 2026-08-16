# R059D Stage W REISSUE2 — Nonhomogeneous Triaxial Cell-Count Root-Collapse Atlas

Task-ID: `RS-R059D-STAGE-W-REISSUE2-NONHOMOGENEOUS-TRIAXIAL-CELL-COUNT-ROOT-COLLAPSE`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-w-reissue2-nonhomogeneous-root-collapse-atlas`
Frozen parent: `a9929a5bd666e621cb1bd77adb464df0d35db399`

## 0. Reissue reason and supersession

The first Stage-W execution at owner head

`8f6ecd12146cac254e5b0668a1bb59e8a21961c4`

is preserved immutable but is NOT the answer to this experiment.

Driver review disposition:

`EXECUTION_INTEGRITY_PASS__SCIENTIFIC_TARGET_RETYPE_REQUIRED`.

The first round introduced an unauthorized-for-target assumption:

`TRANSLATION_HOMOGENEITY = a named direction has the same stored coordinate increment at every cell`.

Together with `+u -> (1,-1,-1)`, this forced

`C(nu)=n C(u)=(n,-n,-n)`

before root testing and therefore trivialized the experiment to `p=1` by construction.

Do NOT consume as project conclusions:

- `P1_IDENTITY_UNIQUE...`
- `SQUARE_ROOT_PRECOLLAPSE_REJECTED...`
- the first-round linear formula `coord(C[a,b,c])=(a-b-c,-a+b-c,-a-b+c)`.

They are retained only as the negative control:

`HOMOGENEOUS_ADDITIVE_COORDINATE_MODEL_TRIVIALIZES_TO_P1`.

The previously superseded Stage V remains superseded.

## 1. Core semantics

Freeze before computation:

### 1.1 Stored crystal-cell coordinate

`INTEGER_CELL_COORDINATE = (U,V,W) in Z^3`.

Every stored component is an integer.

### 1.2 Precollapse algebraic value

A value such as `sqrt(2)` may occur only as

`PRECOLLAPSE_ALGEBRAIC_VALUE`.

It is never a stored coordinate.

### 1.3 Cell identity is not coordinate

The finite sheet needs an independent identity scaffold so that multiple paths can be recognized as reaching the same cell without using the coordinate formula under test.

Use a purely combinatorial C6/A2 cell-ID index `(a,b) in Z^2` ONLY for cell identity and adjacency.

Freeze the six channel moves around the sheet as:

- `+u : (a,b) -> (a+1,b)`
- `-w : (a,b) -> (a+1,b-1)`
- `+v : (a,b) -> (a,b-1)`
- `-u : (a,b) -> (a-1,b)`
- `+w : (a,b) -> (a-1,b+1)`
- `-v : (a,b) -> (a,b+1)`

This index is an `ADJACENCY_ID`, not a triaxial coordinate and not a metric embedding.

It is allowed to be translationally homogeneous as an identity scaffold.

The STORED TRIAXIAL COORDINATE MAP from cell IDs into `Z^3` is UNKNOWN and MUST NOT inherit that homogeneity automatically.

## 2. Absolute firewall against first-round trivialization

The following statements are FORBIDDEN as premises:

- `C(cell+d)-C(cell)=C(d)`;
- `C(path concatenation)=sum of first-step coordinate increments`;
- `C(nu)=n C(u)`;
- a named spatial direction has a fixed stored-coordinate increment everywhere;
- stored coordinates form a group homomorphism from the cell-ID scaffold;
- first-shell coordinate triples are vector generators for all later shells.

Any of these may be recovered only if independently forced by the atlas after nonhomogeneous candidates have been tested.

The checker MUST contain explicit rejection tests for accidental reintroduction of these premises.

## 3. Hard user controls

Freeze only these as hard observations:

- origin cell `O` has stored coordinate `(0,0,0)`;
- one adjacency step in `+u` reaches a neighbor whose stored coordinate is `(1,-1,-1)`.

The intended interpretation is:

> moving one cell in `+u` counts one positive unit on the u-axis and one negative unit relative to each of the other two axes.

Cyclic candidates

- `+v -> (-1,1,-1)`
- `+w -> (-1,-1,1)`

and sign-inverted negative directions are symmetry hypotheses to audit. They may be adopted as a frozen symmetric subcase only after a separate `FIRST_SHELL_SYMMETRY_DECLARATION` artifact makes the assumption explicit. Also retain a minimally constrained control where only the `+u` observation is hard.

## 4. The target example is NOT a premise

The key example to test is:

- first `+u` cell: stored `(1,-1,-1)`;
- second consecutive `+u` cell has primary count `U=2` by direct cell counting;
- a candidate transverse precollapse law may produce `-sqrt(2),-sqrt(2)`;
- integer completion may then produce stored `(2,-1,-1)` or `(2,-2,-2)` or another atlas-consistent integer triple depending on the derived rule.

Do not assume square root.
Do not assume lower completion.
Do not assume the second-cell answer.

The experiment must let count algebra and global consistency decide.

## 5. Stage W2-0 — Build the cell-ID atlas first

Enumerate the independent C6/A2 cell-ID scaffold to:

- complete radius 3;
- radius 4 if cheap;
- pure-axis rays through at least `n=36` for all six orientations.

For every cell ID preserve:

- all shortest path words;
- selected reversal/loop paths;
- neighbors;
- cyclic images;
- inversion image.

No stored-coordinate value beyond the hard first-step control may be obtained by summing first-step increments.

## 6. Stage W2-1 — Count ledgers, not coordinate increments

For each path to a cell, build elementary signed event-count ledgers before proposing a root law.

At minimum keep for each axis `i in {u,v,w}`:

### Direct signed count

`D_i = #(+i) - #(-i)`.

### Transverse signed event balance

A positive move on either of the other two axes contributes a negative transverse event relative to axis `i`; a negative move contributes a positive transverse event.

Define path-derived signed cross balance

`Q_i = (# negative moves on the other two axes) - (# positive moves on the other two axes)`.

Also retain separated nonnegative counts

`Q_i_plus = # negative moves on the other two axes`

`Q_i_minus = # positive moves on the other two axes`

so that both a net-root and split-root interpretation can be tested.

These are EVENT COUNTS only. They are not stored coordinates.

For the pure `+u^n` ray:

- `D_u=n`, `Q_u=0`;
- `D_v=D_w=0`;
- the transverse negative-event count magnitude is `n`.

Thus a square-root candidate naturally gives `-sqrt(n)` on the transverse channels without assuming any coordinate homogeneity.

## 7. Stage W2-2 — Elementary candidate families

Test only a small predeclared registry of count-derived algebraic forms. No formula fishing after seeing outcomes.

For integer root order `p=1..6`, test at least:

### Model N — net-root balance

For each axis:

`R_i = D_i + sgn(Q_i) * |Q_i|^(1/p)`

with the sign convention checked against the `+u -> (1,-1,-1)` control.

### Model S — split-root balance

For each axis:

`R_i = D_i + (Q_i_plus)^(1/p) - (Q_i_minus)^(1/p)`

again with exact sign audit.

### Model H — first-round homogeneous linear control

Retain the previous additive/homogeneous rule only as a negative/trivial control, not as a discovery candidate.

The researcher may add at most TWO further elementary count formulas if they arise directly from the count ledger and are frozen before scoring. Any addition must be justified with a pre-score registry commit.

No Euclidean projection, angle, norm, fitted coefficient, ML, or optimization.

## 8. Stage W2-3 — Path independence gate on PRECOLLAPSE values

This gate occurs BEFORE integer collapse scoring.

For the same cell ID reached by multiple paths, determine whether each candidate model gives the same symbolic precollapse triple after exact cancellation of inverse moves.

Important control:

A path with an inserted immediate reversal must not change the cell's precollapse state after exact path reduction if the model claims cell-state semantics rather than history semantics.

Classify each model/root order:

- `PRECOLLAPSE_PATH_INDEPENDENT`
- `PRECOLLAPSE_HISTORY_DEPENDENT`
- `REQUIRES_NET_CANCELLATION_BEFORE_ROOT`
- `REQUIRES_SPLIT_COUNTS`
- `INCONSISTENT_WITH_CELL_STATE_SEMANTICS`.

Do not hide history dependence by choosing a preferred path.

## 9. Stage W2-4 — Integer completion branches

For every surviving precollapse component `r`:

- if `r` is integer, completion is exact;
- if `k<r<k+1`, both adjacent integer completions `k` and `k+1` remain legal until eliminated by atlas consistency;
- preserve sign correctly for negative components.

Do not use nearest rounding, floor, ceiling, midpoint, or probability as default.

For pure `+u` ray define unknown transverse integer sequence

`a_n >= 0`

with stored candidate

`C_u(n)=(n,-a_n,-a_n)`

only in the symmetric subcase.

Freeze

`a_0=0`, `a_1=1`.

For each root order list the two legal values of `a_n` at every nonperfect-power `n`.

## 10. Stage W2-5 — Off-axis self-consistency must decide branches

This is the central test.

Propagate legal completion combinations onto mixed-path cells such as:

- `+u,+v`
- `+u,-v`
- `+u,+w`
- `+u,+u,+v`
- cyclic equivalents
- paths with reordered commuting adjacency events that reach the same CELL_ID
- paths containing exact reversal loops.

Use only:

- same cell ID -> one stored integer triple;
- inverse cell-ID move must reverse to the prior cell;
- candidate cyclic/inversion covariance, when explicitly declared;
- distinct cell IDs should not be forced to one stored triple unless a separately stated noninjective coordinate ontology is being tested;
- every claimed coordinate rule must cover all tested cells, not only pure rays.

For every ambiguous completion preserve:

- `FORCED_LOWER_BY_ATLAS`
- `FORCED_UPPER_BY_ATLAS`
- `BOTH_SELF_CONSISTENT`
- `NEITHER_SELF_CONSISTENT`
- `NOT_YET_DECIDED_AT_TEST_RADIUS`.

A model that fits `+u^n` but fails one off-axis cell is rejected.

## 11. Stage W2-6 — Root order and collapse sequence

Compare `p=1..6` only after the path-independence and mixed-cell gates.

For each model/root order report:

- first surviving shell/ray horizon;
- first contradiction;
- surviving completion sequence `a_n` if any;
- whether `p=1` survives for a structural reason distinct from the old homogeneous assumption;
- whether a nontrivial root order survives or is forced.

Allowed freezes include:

- `SQUARE_ROOT_SURVIVES_NONHOMOGENEOUS_ATLAS`
- `SQUARE_ROOT_REJECTED_BY_NONHOMOGENEOUS_ATLAS`
- `ROOT_ORDER_NOT_IDENTIFIED`
- `MULTIPLE_ROOT_ORDERS_SURVIVE`
- `NONTRIVIAL_ROOT_ORDER_UNIQUE_WITHIN_REGISTRY_AND_RADIUS`
- `COLLAPSE_SEQUENCE_FORCED_BY_MIXED_CELL_SELF_CONSISTENCY`
- `COLLAPSE_SEQUENCE_REMAINS_MULTIBRANCH`.

## 12. Stage W2-7 — 5 -> 4 / 9 only after square-root survival

If and only if square root survives the preceding nonhomogeneous gates:

- inspect `n=5`;
- `sqrt(5)` lies between 2 and 3;
- test whether the atlas forces transverse completion 2 or 3;
- retype this on the squared count layer as `5->4` or `5->9`.

Do not adjudicate 5 if square root is already rejected.

## 13. Strong anti-triviality controls

Required controls:

1. first-round homogeneous additive map;
2. floor-only root completion;
3. ceiling-only root completion;
4. nearest root completion;
5. midpoint root completion;
6. arbitrary parity alternation;
7. axis-name preference;
8. old zero-sum raw coordinate ontology;
9. old `(1,-1,0)` raw coordinate;
10. path-sum of stored first-step increments.

The checker must fail if the positive model silently reduces to control 1 or 10 without an independent derivation.

## 14. Required artifacts

At minimum:

1. `R059D_STAGE_W_REISSUE2_CELL_ID_SCAFFOLD.json`
2. `R059D_STAGE_W_REISSUE2_INTEGER_COORDINATE_SEMANTICS.json`
3. `R059D_STAGE_W_REISSUE2_FIRST_SHELL_SYMMETRY_AUDIT.json`
4. `R059D_STAGE_W_REISSUE2_EVENT_COUNT_LEDGER_PROTOCOL.json`
5. `R059D_STAGE_W_REISSUE2_PREDECLARED_ROOT_MODEL_REGISTRY.json`
6. `R059D_STAGE_W_REISSUE2_PURE_AXIS_RAY_TABLE.json`
7. `R059D_STAGE_W_REISSUE2_PRECOLLAPSE_PATH_INDEPENDENCE.json`
8. `R059D_STAGE_W_REISSUE2_MIXED_CELL_COMPLETION_LEDGER.json`
9. `R059D_STAGE_W_REISSUE2_ROOT_ORDER_SURVIVAL_LEDGER.json`
10. `R059D_STAGE_W_REISSUE2_FIVE_TO_FOUR_OR_NINE_CONTROL.json`
11. `R059D_STAGE_W_REISSUE2_FIRST_ROUND_W_NEGATIVE_CONTROL.json`
12. `R059D_STAGE_W_REISSUE2_TRIVIALITY_LEAKAGE_LEDGER.json`
13. deterministic checker source/output
14. report
15. manifest
16. frozen checkpoint.

## 15. Mandatory report statements

The final report must state clearly:

- whether stored coordinates remain integer-only;
- whether the first-step `(1,-1,-1)` control is retained;
- whether cyclic/inversion first-shell symmetry was assumed, derived, or rejected;
- whether precollapse state is path-independent;
- whether any nontrivial root order survives;
- whether collapse choices are forced by mixed-cell consistency;
- whether `5->4/9` is resolved;
- exactly which conclusions of first-round W remain only model-conditional;
- what remains underdetermined.

## 16. Scientific boundary

This is still a small finite atlas experiment.

Do not claim universal BRC, physical geometry, probability, force, energy, or physical dimensionality.

The target is elementary and concrete:

`COUNT ADJACENCY EVENTS -> FORM SIMPLE ROOT-LIKE PRECOLLAPSE VALUES -> COMPLETE TO INTEGER CELL COORDINATES -> REQUIRE THE WHOLE LOCAL CELL ATLAS TO AGREE.`

After all artifacts/checks:

`STOP_FOR_DRIVER_REVIEW`.
