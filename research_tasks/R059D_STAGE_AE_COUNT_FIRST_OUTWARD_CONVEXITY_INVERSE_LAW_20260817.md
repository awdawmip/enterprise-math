# R059D Stage AE — Count-First Outward-Convexity Threshold and Inverse Law

Status: `ACTIVE / DRIVER_TASKBOOK`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Task-ID: `RS-R059D-STAGE-AE-COUNT-FIRST-OUTWARD-CONVEXITY-INVERSE-LAW`
Owner branch: `research/r059d-stage-ae-count-first-outward-convexity`
Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

## 0. Completion estimate / vector

Before:
- raw count law: `~20%`
- AD orbit counting calibration: `0%`
- outward-convexity threshold: `0%`
- inverse law: `0%`

Target after this stage:
- raw count law: `~80%`
- orbit counting calibration: `~90%`
- outward-convexity threshold: `~80%`
- inverse law candidate: `~60%`

Progress vector:
`counting +35 / convexity-threshold +35 / inverse-law +25 / resolver-theory +5`

## 1. Driver working truth

Use the stupid method first: **count cells**.

Freeze the user controls exactly:

| nominal radius r | diameter D | circumference C | volume V |
|---:|---:|---:|---:|
| 1 | 3 | 6 | 7 |
| 2 | 5 | 12 | 19 |
| 3 | 7 | 18 | 37 |

These are controls, not formulas supplied to the generator.

Candidate relations discovered from the controls may be tested/proved, but must not be used to manufacture later rows:

`D_r ?= 2r+1`

`C_r ?= 6r`

`V_r ?= 3r(r+1)+1`

and therefore candidate eliminations:

`C ?= 3(D-1)`

`V ?= (3D^2+1)/4`

`V ?= C^2/12 + C/2 + 1`.

The point of AE is to discover **where the zero-curvature/zero-bulge regime stops**, not to assume these formulas remain globally true.

## 2. Frozen AD input

Stage AD is accepted and immutable.

Accepted disposition:
`COVERAGE_BRIDGE_ESTABLISHED__RESOLVE_RULE_UNDERDETERMINED`.

Consume AD only as frozen data/algorithms:
- exact coverage field;
- resolver N (`NEAREST_CELL_BASELINE`);
- resolver C (`COVERAGE_THRESHOLD`, theta=1/2);
- frozen circle-orbit candidates;
- deterministic replay code/artifacts.

Do not modify AD and do not promote resolver R.

AD checker reference:
`2643/2643 PASS`
`2627ce754fed59485f97c6c861f707f0d1e29b852d514b42272829fc81f7cde7`

## 3. Hard objective

Find, separately for every surviving AD resolver family, the first stable outward-convexity transition:

`LAST_ZERO_BULGE_RADIUS`

`FIRST_STABLE_OUTWARD_BULGE_RADIUS`

Then reverse-engineer exact count laws before and after the transition.

Primary disposition must be one of:

- `OUTWARD_CONVEXITY_THRESHOLD_FOUND__INVERSE_LAW_CANDIDATE`
- `OUTWARD_CONVEXITY_THRESHOLD_FOUND__COUNT_LAW_UNDERDETERMINED`
- `NO_OUTWARD_CONVEXITY_THRESHOLD_THROUGH_AUDIT_RANGE`
- `COUNT_SEMANTICS_FAIL_USER_CONTROLS`

## 4. First gate — identify what D/C/V actually count

Do not assume AD's internal boundary-edge count is the user's circumference count.

For r=1,2,3 test all natural discrete count semantics available from the resolved disk/orbit, at minimum:

- `DIAMETER_OCCUPIED_CELL_COUNT`: occupied cells on a full opposite-axis diameter, endpoints included;
- `DIAMETER_TRANSITION_COUNT`: adjacency transitions on that diameter;
- `BOUNDARY_CELL_COUNT`: occupied cells touching the exterior;
- `INTERFACE_EDGE_COUNT`: edges in the unique occupied/exterior interface cycle;
- `OUTER_SHELL_CELL_COUNT`: cells added from the previous nominal radius under the selected family;
- `VOLUME_OCCUPIED_CELL_COUNT`: total occupied cells.

Find one exact typed triple reproducing all user controls:

`(3,6,7), (5,12,19), (7,18,37)`.

If no exact triple exists, stop the interpretation layer and return `COUNT_SEMANTICS_FAIL_USER_CONTROLS`; preserve all raw counts.

## 5. Radius range

Replay/extend N and C deterministically for:

- mandatory: `r=1..64`;
- target: `r=1..256`;
- extend farther if runtime remains trivial.

Coverage sampling:
- use a frozen sufficiently stabilized sampling for C, with explicit precision audit;
- N is sampling-independent by definition;
- do not change theta or tune any resolver parameter.

## 6. Pure combinatorial zero-bulge baseline

Within one canonical 60-degree Enterprise sector, define the `ZERO_BULGE_BASELINE(r)` as the monotone boundary path connecting the two neighboring axis intercepts whose internal step direction is constant in the triangular implementation carrier.

This is a **combinatorial baseline**, not an Euclidean chord and not an equal-distance locus.

For any resolved one-sector boundary path `P_r`, define an exact integer signed bulge count:

`BULGE_CELL_COUNT(P_r)`

by counting the elementary triangular/dual lattice cells enclosed between `P_r` and `ZERO_BULGE_BASELINE(r)`:

- outward from the center: positive;
- inward toward the center: negative;
- identical path: zero.

No floating area is allowed.

Also record the exact step word and turn word.

## 7. Outward-convexity criterion

A path is `STRICT_ENTERPRISE_OUTWARD_CONVEX` iff:

1. `BULGE_CELL_COUNT > 0`;
2. its internal nonzero discrete turns all have the same outward sign under the frozen cyclic direction order;
3. there is no inward re-entrant turn;
4. the path is simple;
5. the D6-completed full boundary is one simple closed cycle;
6. the same classification is obtained under reverse traversal after orientation normalization;
7. the same classification holds in all six sectors by symmetry.

Do not use Euclidean curvature, radius, angle, sqrt, pi, or distance to classify convexity.

## 8. Critical radius

For each resolver family `X in {N,C}` compute:

`B_X(r) = BULGE_CELL_COUNT(P^X_r)`.

Define:

`r0_X = max r before the first stable positive regime with B_X(r)=0`

`r*_X = min r such that B_X(r)>0 and STRICT_ENTERPRISE_OUTWARD_CONVEX holds for a declared stability window`.

Default stability window: at least 8 consecutive radii; if transition is late, use at least 16 where available.

If N and C give the same threshold and post-threshold bulge sequence, record:
`RESOLVER_INDEPENDENT_THRESHOLD_CANDIDATE`.

If they differ, do not average; retain both.

## 9. Count ledger

For every radius and resolver, record at minimum:

- r;
- calibrated D;
- calibrated C;
- calibrated V;
- shell increment `DeltaV = V_r - V_{r-1}`;
- `DeltaC`;
- `Delta2V`;
- bulge count B;
- step word;
- turn word;
- boundary-cell count;
- interface-edge count;
- D6 closure status;
- reverse-traversal status;
- precision status.

Explicitly test:

`DeltaV ?= C`

under the calibrated circumference semantics.

## 10. Inverse-law discovery

Only after the ledger is generated, infer exact laws.

Use:
- finite differences;
- exact integer recurrences;
- exact polynomial/rational interpolation as a hypothesis generator;
- independent holdout radii;
- symbolic proof from the observed combinatorial recurrence whenever possible.

Fit separately:

1. zero-bulge regime `r <= r0`;
2. transition window;
3. stable outward-convex regime `r >= r*`.

Derive relations in all useful eliminations:

- D(r), C(r), V(r), B(r);
- C(D);
- V(D);
- V(C);
- B(D/C/V) where exact.

A fitted formula without recurrence/proof is `CANDIDATE_ONLY`.

## 11. Pi firewall

Do not use classical pi, classical circle circumference, Euclidean area, Euclidean equal-distance, or `sqrt(x^2+y^2)` anywhere in the generator or selection logic.

After the count laws are independently obtained, it is allowed to compute diagnostic ratios such as:

`C/D`

and their exact limits if they exist.

If an exact rational/algebraic limit emerges, report it as an Enterprise count invariant candidate. Do not import classical pi for comparison until the end-of-stage compatibility appendix.

## 12. AD independence / no target leakage

Forbidden:
- choosing N or C because one looks more circular classically;
- changing theta;
- using classical arc error to define `r*`;
- injecting the candidate formulas `2r+1`, `6r`, `3r(r+1)+1` into later rows;
- using the user's expected `r*` (none supplied) to tune any rule;
- hiding N/C disagreement.

## 13. Required artifacts

Create under `research_results/R059D_STAGE_AE/`:

- `R059D_STAGE_AE_COUNT_SEMANTICS_CALIBRATION.json`
- `R059D_STAGE_AE_RADIUS_LEDGER.json`
- `R059D_STAGE_AE_BULGE_LEDGER.json`
- `R059D_STAGE_AE_CRITICAL_RADIUS_CERTIFICATE.json`
- `R059D_STAGE_AE_INVERSE_LAW_CANDIDATES.json`
- `R059D_STAGE_AE_SYMBOLIC_PROOFS.json`
- `R059D_STAGE_AE_TARGET_LEAKAGE_AUDIT.json`
- `R059D_STAGE_AE_REPORT.md`
- deterministic checker script/output
- frozen checkpoint/manifest.

## 14. Checker gates

Mandatory:

- exact reproduction of user controls at r=1,2,3 after count-semantics calibration;
- deterministic replay of all ledger rows;
- exact D6 symmetry checks;
- exact forward/reverse convexity classification agreement;
- no forbidden classical constants/formulas in generator;
- candidate-law holdout checks;
- prior AD immutability gate;
- no later-stage consumption.

## 15. Stop rule

Do not proceed to a new resolver or optimize the circle.

Stop after:

1. count semantics are calibrated;
2. radius census is complete;
3. zero/positive outward-bulge threshold is certified or shown absent through the audit range;
4. inverse formulas are classified as proved/candidate/underdetermined;
5. Driver review packet is frozen.

`STOP_FOR_DRIVER_REVIEW`
