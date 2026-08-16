# R059D Stage AA — Reflection-Orbit Frontier / Triangular-Threshold Audit

Task-ID: `RS-R059D-STAGE-AA-REFLECTION-ORBIT-FRONTIER-TRIANGULAR-THRESHOLD-AUDIT`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-4E8B71`
Owner branch: `research/r059d-stage-aa-reflection-orbit-frontier`
Frozen parent: `1806cc135fd38a8e2dd11520f74eebdf5756382e`

## 0. Frozen inputs

Stage Z is accepted as:

`PASS__VALID_FRONTIER_COUNT_WITH_PRIMARY_GAP_COUPLING_NO_GO`.

Consume but do not alter:

- Stage-X binary staircase classification;
- Stage-Y corrected semantic typing;
- Stage-Z exact raw frontier count `|F2(k)|=2k+1`;
- Stage-Z primary-gap freedom theorem;
- Stage-Z obstruction to reflection-equivariant pointwise enumeration of raw ordered-pair frontier states;
- `5->4/9` unresolved.

Do not consume any Stage AB or later result.

## 1. Scientific target

Stage Z showed that the raw ordered-pair frontier is the wrong object for a reflection-fixed primary event if one demands one primary step per raw state.

The next elementary candidate is the reflection quotient itself.

For

`F2(k)=B2(k+1)\B2(k)`

under slot swap

`tau(i,j)=(j,i)`,

define

`O2(k)=F2(k)/<tau>`.

Prove directly:

- one diagonal fixed orbit `{(k+1,k+1)}`;
- `k` off-diagonal two-element orbits;
- therefore `|O2(k)|=k+1`.

This is finite-set counting only, not geometry or area.

The central question is:

> Can one primary +u unit step be independently typed as one **unordered two-slot frontier event** so that a k-layer primary occupancy gap consumes each orbit in `O2(k)` exactly once?

Do not assume the answer is yes.

## 2. Why this candidate is different from Stage Z raw frontier

The explicit u-ray reflection swaps the two transverse coordinate roles v and w. One +u unit step affects both transverse roles simultaneously in the symmetric subcase.

Therefore an unordered/swap-orbit event is at least symmetry-compatible in a way that a single oriented raw pair is not.

But symmetry compatibility is not a coupling proof.

Stage AA must construct or refute an exact primary-side event state that maps to `O2(k)` without using the future gap length or a preselected triangular schedule.

## 3. Hard anti-circularity rules

Forbidden as premises:

- `g_k=k+1`;
- triangular thresholds `A_k=k(k+1)/2`;
- any inverse-triangular/root formula;
- ordering orbit states after seeing the desired schedule;
- defining the primary event state by `n-A_k` unless `A_k` is independently available before the coupling claim;
- using the future endpoint `A_(k+1)` to define the map;
- floor/ceil/nearest/midpoint;
- probability, ML, optimization, reward, stabilizer selection;
- Euclidean angle/length/area/volume;
- axis-name preference between the two transverse slots.

## 4. Stage AA0 — Freeze quotient frontier registry

Before scoring, freeze:

- raw frontier `F2(k)`;
- swap action;
- orbit frontier `O2(k)`;
- exact orbit decomposition;
- `|O2(k)|=k+1`;
- small-k tables at least `k=0..8`.

Also keep raw count `2k+1` as control.

## 5. Stage AA1 — Primary event-state construction

Search only a small predeclared family of elementary primary-side states that can be computed from information available at the current primary step and current completed layer k.

Examples of allowed ingredients:

- current CELL_ID / primary index n;
- current completed staircase level k=a_n, only as an already-realized integer state;
- current local unit-step transition data;
- realized symmetric transverse crossing/no-crossing event;
- finite history since the last **already-realized** layer activation, provided the construction does not assume when the next activation occurs.

Every candidate must define an explicit map or relation to `O2(k)` and must be frozen before global scoring.

## 6. Stage AA2 — Exact coupling gate

For each predeclared candidate, test whether it proves all of:

1. every primary event in the k-layer occupancy interval maps to one orbit in `O2(k)`;
2. no orbit is skipped;
3. no orbit is repeated;
4. the construction is reflection compatible and transverse-slot-name free;
5. the map does not use the unknown future endpoint of the gap;
6. the construction works uniformly for all k.

If all six are proved, then and only then freeze:

`PRIMARY_GAP_TO_SWAP_ORBIT_FRONTIER_COUPLING_ESTABLISHED`.

If no candidate survives, freeze the no-go/underdetermination exactly.

## 7. Stage AA3 — Conditional triangular theorem

Only if AA2 establishes the coupling, derive:

`g_k=|O2(k)|=k+1`.

With `A_1=1`, prove by finite sum:

`A_k=1+sum_{r=1}^{k-1}(r+1)=k(k+1)/2`.

These are activation thresholds.

Do not call this Euclidean geometry.

If the coupling is not established, retain the triangular arithmetic only as a conditional theorem.

## 8. Stage AA4 — Direct low-n discriminator

The square and orbit-triangular schedules first diverge very early.

Audit explicitly:

- `n=1`;
- `n=2`;
- `n=3`;
- `n=4`;
- `n=5`;
- `n=6`.

In particular:

- the user's control permits `a_2=1`;
- a square-floor schedule keeps `a_3=1` and activates level 2 at n=4;
- an orbit-triangular activation schedule would activate level 2 at n=3.

Do not decide between them by preference. Identify what exact current-step count/event evidence, if any, distinguishes `a_3=1` from `a_3=2`.

## 9. Stage AA5 — Relation to 5 -> 4 / 9

Do not force the old square-count question if square coupling remains unproved.

Report separately:

- the square-readout control, still conditional;
- the orbit-triangular completed level at n=5 if AA2 succeeds;
- whether any native statement `5->4` or `5->9` is justified.

If root degree is not square, say explicitly that `5->4/9` is not the native control for the surviving count law.

## 10. Stage AA6 — m-slot symmetric quotient control

As a small control only, for `m=1..4` count swap/permutation-orbit frontiers of `Bm` under slot permutations when elementary.

Do not search broadly.

The purpose is to determine whether `m=2` is structurally selected by the two transverse roles plus their reflection, or whether m-slot ambiguity simply reappears after quotienting.

No physical dimensionality claim.

## 11. Required artifacts

At minimum:

- `R059D_STAGE_AA_ORBIT_FRONTIER_REGISTRY.json`
- `R059D_STAGE_AA_PRIMARY_EVENT_STATE_REGISTRY.json`
- `R059D_STAGE_AA_ORBIT_COUPLING_LEDGER.json`
- `R059D_STAGE_AA_TRIANGULAR_THRESHOLD_THEOREM.json`
- `R059D_STAGE_AA_LOW_N_DISCRIMINATOR.json`
- `R059D_STAGE_AA_FIVE_CONTROL.json`
- `R059D_STAGE_AA_M_SLOT_SYMMETRIC_CONTROL.json`
- `R059D_STAGE_AA_TRIVIALITY_LEAKAGE_LEDGER.json`
- deterministic checker source/output
- report
- manifest
- frozen checkpoint.

## 12. Allowed outcomes

Useful positive/negative freezes include:

- `SWAP_ORBIT_FRONTIER_COUNT_K_PLUS_1_ESTABLISHED`
- `PRIMARY_GAP_TO_SWAP_ORBIT_FRONTIER_COUPLING_ESTABLISHED`
- `PRIMARY_GAP_TO_SWAP_ORBIT_FRONTIER_COUPLING_NOT_ESTABLISHED`
- `TRIANGULAR_ACTIVATION_THRESHOLDS_ESTABLISHED`
- `TRIANGULAR_ACTIVATION_THRESHOLDS_CONDITIONAL_ONLY`
- `LOW_N_N3_DISCRIMINATOR_IDENTIFIED`
- `LOW_N_N3_REMAINS_UNDERDETERMINED`
- `SQUARE_SCHEDULE_NOT_SELECTED`
- `ROOT_DEGREE_REMAINS_UNIDENTIFIED`
- `FIVE_TO_FOUR_OR_NINE_NOT_NATIVE_UNDER_SURVIVING_COUNT_LAW`
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED`.

After all checks:

`STOP_FOR_DRIVER_REVIEW`.
