# R059D Stage M — BRC6 Equal-L Endpoint Branch-Count Microgrammar Robustness

Task-ID: `RS-R059D-STAGE-M-BRC6-EQUAL-L-ENDPOINT-BRANCH-COUNT-MICROGRAMMAR-ROBUSTNESS`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-m-brc6-endpoint-count-microgrammar-robustness`

## 0. Frozen parent and Driver disposition

Stage L is frozen at owner head:

`da350b7b1e2ae21491e6251fdf2ba9cf0d4557ca`

All BRC6 Stage J/K/L artifacts are immutable.

Driver accepts Stage L at exactly this strength:

- `BRC6_EQUAL_L_ENDPOINT_BRANCH_COUNT_COLLAPSE_ESTABLISHED`;
- `BRC6_ENDPOINT_COUNT_TRUE_STATE_DYNAMICS_ESTABLISHED`;
- all six candidates use the same `ALIGNED_SEGMENT_CELL_COUNT=L=4`;
- `L` is only the common aligned-endpoint evaluation boundary and is never a selector score, optimization variable, or tie-break;
- in the inherited affine two-state CPBC quotient, endpoint count is `B_d=C_(L-1)^d=C_3^d=A_d+3I[d]`;
- Stage-L count-mode is the unique strict argmax of the six endpoint counts, with exact maximal ties unresolved;
- six-outcome coverage and exact true O/M/I state dynamics are established;
- semantic strength is only `CANONICAL_WITHIN_FROZEN_ENDPOINT_BRANCH_COUNT_COLLAPSE_AXIOMS`;
- `BRC6_NATIVE_CANONICALITY = NOT_ESTABLISHED`.

Stage M attacks the remaining implementation dependence: does endpoint branch-count selection survive when the internal count-preserving branching/recoalescence microgrammar is changed while **the same four packet cells and the same equal-L endpoint boundary remain fixed**?

## 1. Core scientific question

Keep the BRC6 collapse observable fixed:

`B_d = exact admissible branch/history multiplicity arriving at candidate d's next aligned endpoint`.

Keep:

`L(d)=4` for every `d in C6`.

Do not change L between microgrammars.

Vary only the **internal relational branch/recoalescence microgrammar carried on those same four continuation cells**.

For each pre-frozen microgrammar `g`, compute:

`B_d^(g)(sigma)`

by raw-history enumeration and by exact CPBC compression, prove equality, and apply the same Stage-L collapse:

`BRC6_g(sigma)=unique argmax_d B_d^(g)(sigma)`.

Question:

Does the selected channel remain the same across admissible microgrammars, or is BRC6 still microgrammar-dependent?

This is the main Stage-M identifiability test.

## 2. Lane firewall

Continue only the BRC6 lane owned by `EM-R059D-9C6B2A`.

Do not consume the old graded-relay Stage-J side lane (`EM-R059D-4C7E21`) as a premise.

Do not read/consume `R059P_*`, `R059L_*`, or reopen `R059C` results.

Consume only frozen BRC6 Stage J/K/L lineage.

## 3. Foundation and length firewall

Native foundation remains packet/path only.

Freeze:

`ALIGNED_SEGMENT_CELL_COUNT=L=4`.

Every admissible raw history used for endpoint scoring occupies exactly the same four declared continuation packet cells in order of continuation-cell index `0,1,2,3`; the endpoint is cell index `3=L-1`.

Internal branching may use declared relational/channel microstates **at those same packet cells**. It may not add candidate-specific packet cells or change the endpoint boundary.

Forbidden:

- candidate-dependent L;
- changing L to obtain a preferred winner;
- shortest/longest path;
- geometric length/distance;
- angle/vector/straight/turn semantics;
- hidden target information;
- arbitrary numeric edge/transition weights.

Any integer multiplicity greater than one must arise from distinct explicitly declared raw histories / internal relational transition classes and must be verified by enumeration on tiny seeds.

## 4. Microgrammar registry — freeze before scoring

Construct and freeze a finite exact registry before evaluating the Stage-L witnesses.

At minimum include the following semantic classes, realized without adding packet cells:

### M-G0 — AFFINE_UV_REPLAY

Exact replay of Stage L's inherited two-state affine CPBC quotient.

### M-G1 — SINGLE_SPLIT_RECOALESCE

At one internal continuation boundary, one declared source class has two distinct internal relational continuations at the same packet-cell sequence; both recoalesce before/at the common endpoint.

### M-G2 — DELAYED_SPLIT_RECOALESCE

A split/recoalescence pattern placed at a different continuation-cell boundary while keeping the same four packet cells and endpoint.

### M-G3 — TWO_STAGE_SPLIT_RECOALESCE

Two successive internal branching events with exact endpoint recoalescence.

### M-G4 — LAUNCH_CLASS_SPLIT_CONTROL

A branching construction acting on the launch-count source class rather than the inherited incidence source class, still with the same four packet cells.

### M-G5 — ENDPOINT_EQUIVALENT_INTERNAL_REWRITE

A microgrammar that has a different internal history organization but is proved to induce the same endpoint branch-count functional as one other registry member. This is a positive control for endpoint sufficiency.

Internal-state relabelings/conjugacies must be included as equivalence controls where useful.

All six candidate channels must use the **same microgrammar g** at a given evaluation. Candidate-specific grammar choice is forbidden.

Every grammar must be C6-covariant under simultaneous channel relabeling.

## 5. Raw-history oracle gate

Before using any microgrammar as positive evidence, prove on unit seeds and tiny integer seeds:

`CPBC endpoint count = raw-history multiplicity`.

Required raw-history cases include:

- one launch seed only;
- one incidence seed only;
- mixed launch/incidence seeds;
- multiplicity >1;
- internal split;
- recoalescence of distinct histories;
- same-cell internal-state reuse where declared;
- exact endpoint tie cases.

No support-only collapse is allowed.

If two histories recoalesce into the same endpoint microstate, counts add as natural integers.

## 6. Endpoint transfer functional

For each microgrammar `g`, derive an exact closed endpoint transfer functional

`B_d^(g) = F_g(current local exact count signature for candidate d)`.

Do not assume it is affine unless proved.

If the grammar is linear over natural-number counts, derive the exact coefficient/action from raw histories; do not introduce arbitrary weights.

Record which current local fields the functional actually depends on.

## 7. Microgrammar robustness classifications

For a fixed state `sigma`, compare all frozen admissible `g`.

Use these exact classes:

- `MICROGRAMMAR_STRONG_CONSENSUS_RESOLVED`: every grammar has a unique winner and every winner is the same channel;
- `MICROGRAMMAR_COMPATIBLE_WITH_TIES`: at least one grammar resolves channel d, every other grammar either resolves the same d or has an exact maximal tie, and no grammar uniquely selects a conflicting channel;
- `MICROGRAMMAR_DEPENDENT`: two admissible grammars uniquely select different channels;
- `MICROGRAMMAR_ALL_UNRESOLVED`: every grammar is unresolved.

Freeze nonempty robust/dependent domains if found.

If `MICROGRAMMAR_DEPENDENT` exists, do not promote endpoint-count BRC6 to a grammar-independent native law.

## 8. Mandatory witness replay

Re-evaluate at minimum:

- `W_ASYM_BASE`;
- `W_CONSENSUS_DOMINANT2`;
- `W_FULLY_SYMMETRIC`;
- `W_S1_TIE_S2_RESOLVE`;
- `W_SIGNATURE_INSUFFICIENT_PAIRS`.

For each `(witness, grammar)` store:

- exact six-vector `(B_0^g,...,B_5^g)`;
- unique winner or unresolved;
- raw-history / CPBC equality certificate;
- cyclic relabeling covariance.

Search a bounded exact integer witness box for both robust and dependent examples; freeze the box before scoring.

## 9. Structural theorem targets

Try to prove exact sufficient conditions for microgrammar-independent winners.

Priority targets:

### M-T1 COMPONENTWISE / CONE DOMINANCE

If one candidate dominates every other candidate in all nonnegative seed components actually used by every frozen grammar, prove that every grammar selects it or ties only when the endpoint functional collapses the strict difference.

### M-T2 ENDPOINT-FUNCTIONAL EQUIVALENCE

If two microgrammars induce the same endpoint functional, prove identical BRC6 output/unresolved status for every state despite different internal history organization.

### M-T3 MICROGRAMMAR DEPENDENCE CERTIFICATE

If two explicit admissible grammars reverse a strict endpoint-count ordering on one state, freeze an exact counterexample to grammar-independent canonicality.

## 10. Six-outcome coverage

For any grammar used as a positive resolved BRC6 example, retain the no-absolute-label rule.

Prove six-output coverage by one asymmetric resolved witness plus six cyclic relabelings, not six hand-written absolute-label cases.

## 11. True state dynamics

Use the same three frozen Stage-K relational port carriers and the exact Stage-K/Stage-L event update:

`O_x[d] += 1`

`M_x[i,d] += 1`

`y=T_NODE(x,d)`

`j=T_INGRESS(x,d)`

`I_y[j] += 1`.

At every next decision, recompute each grammar's endpoint counts from the new exact state.

Run representative trajectories for each microgrammar or each distinct endpoint-functional equivalence class.

Record:

- channel-label projection;
- first unresolved epoch;
- first cross-grammar trajectory divergence;
- any exact same-epoch full-state recoalescence;
- `TOTAL_O` monotone-state certificate.

Do not promote repeated label words to full-state cycles.

## 12. Perturbation tests

Under endpoint count-mode, repeat exact perturbations:

- one launch/count token;
- one local incidence event;
- one real tagged launch-contribution adjacency transfer.

For each grammar equivalence class record:

- first BRC6 divergence;
- tie creation/removal;
- unresolved creation/removal;
- trajectory divergence;
- exact full-state recoalescence if any.

Keep L=4 unchanged.

## 13. Large-N exact stress

Use the frozen `N~10^36` system-scale registry.

N remains a common system/count background, never length.

For each grammar, prove symbolically whether a common N background remains candidate-common at the endpoint and therefore cancels from winner/tie comparison.

No huge enumeration.

No length threshold search.

## 14. Interpretation / promotion gate

Permitted positive freezes include:

- `BRC6_ENDPOINT_COUNT_MICROGRAMMAR_ROBUST_DOMAIN_ESTABLISHED`;
- `BRC6_ENDPOINT_COUNT_MICROGRAMMAR_DEPENDENT_DOMAIN_ESTABLISHED`;
- `BRC6_ENDPOINT_FUNCTIONAL_EQUIVALENCE_THEOREM`;
- `BRC6_ENDPOINT_COUNT_TRUE_STATE_MICROGRAMMAR_DYNAMICS_ESTABLISHED`.

Do not promote:

`BRC6_NATIVE_CANONICALITY`

unless a theorem covers the declared admissible microgrammar class rather than only a finite sample.

Continue:

- `PHYSICAL_DIRECTION_CALIBRATION = NOT_ESTABLISHED`;
- `PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`;
- `PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`;
- `PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`;
- `QUANTUM_BRIDGE = NOT_ESTABLISHED`.

## 15. Required artifacts

At minimum:

- `R059D_STAGE_M_MICROGRAMMAR_PROTOCOL.json`
- `R059D_STAGE_M_RAW_HISTORY_ORACLE.json`
- `R059D_STAGE_M_ENDPOINT_TRANSFER_FUNCTIONAL_ATLAS.json`
- `R059D_STAGE_M_MICROGRAMMAR_ROBUSTNESS_LEDGER.json`
- `R059D_STAGE_M_WITNESS_REGISTRY.json`
- `R059D_STAGE_M_STRUCTURAL_THEOREMS.json`
- `R059D_STAGE_M_SIX_OUTCOME_COVERAGE.json`
- `R059D_STAGE_M_TRUE_DYNAMICS_ATLAS.json`
- `R059D_STAGE_M_PERTURBATION_RESPONSE.json`
- `R059D_STAGE_M_LARGE_N_REGISTRY.json`
- `R059D_STAGE_M_TRIVIALITY_AND_LEAKAGE_LEDGER.json`
- deterministic checker + output
- report
- artifact manifest
- frozen checkpoint

Then:

`STOP_FOR_DRIVER_REVIEW`
