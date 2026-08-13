<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R049-CANDIDATE-BLIND-INDEPENDENT-ENGINEERING-HOLDOUT-CONSTRUCTION",
  "title": "R049 Candidate-Blind Independent Engineering Holdout Construction",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "OUT-OF-SAMPLE ENGINEERING VALIDATION / CANDIDATE-BLIND HOLDOUT",
  "frontier": "Freeze a new real-engineering holdout target before G2 calibration, with no access to R048 candidate definitions or scores, so later evidence can distinguish in-sample debt repair from genuine out-of-sample explanatory success.",
  "next_action": "Build and freeze a candidate-blind holdout atlas from public primary engineering sources; include both new protocol/scale/channel holdouts for the inherited pressure families and an open search for genuinely new independent pressure types.",
  "dependencies": [
    {
      "target": "FOUNDATIONAL_LOGIC.md + foundational_logic.json",
      "action": "CONSUME_ENGINEERING_SUCCESS_INVERSION_METHOD",
      "satisfied": true
    },
    {
      "target": "native_semantics_admissibility.json V3",
      "action": "CONSUME_NO_OUTPUT_COPYING_AND_FOUNDATION_CALIBRATION_SEPARATION",
      "satisfied": true
    },
    {
      "target": "R046/R047 definition-stripped engineering-success methodology only",
      "action": "CONSUME_METHOD_NOT_CANDIDATES",
      "satisfied": true
    }
  ],
  "source_refs": [
    "Engineering success is evidence, not inherited definition",
    "Fresh holdout must be frozen before G2 candidate calibration",
    "R048 candidate details and calibration scores withheld from holdout construction"
  ],
  "evidence_status": "CANDIDATE_BLIND_HOLDOUT_TARGET_CONSTRUCTION",
  "last_progress_ref": "R048 G2 generation returned after debt factorization; independent calibration target not yet built.",
  "last_progress_at": "2026-08-13T08:55:00+08:00",
  "hard_block": null,
  "tags": [
    "R049",
    "engineering-holdout",
    "candidate-blind",
    "out-of-sample",
    "definition-stripping",
    "calibration-target"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R049",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R049 — Candidate-Blind Independent Engineering Holdout Construction

Status: `READY / P0 / HOLDOUT-CONSTRUCTION / G2 CANDIDATES WITHHELD / NOT CANONICAL`

## 0. Mother question

R048 generated a second-generation native family from an abstract failure-derived capability basis. That generation did **not** see target protocols or tolerances, but its capability basis ultimately came from earlier calibration failures. Therefore reusing the same engineering surface alone cannot establish independent validation.

This task asks:

> **Can we freeze a genuinely candidate-blind engineering holdout target, grounded in real protocols and error envelopes, before any G2 calibration, so later tests can distinguish debt-repair from real out-of-sample explanatory power?**

This task builds the test. It does not test candidates.

## 1. Strict candidate blindness

Before the holdout target is frozen, do not read or consume:

- R048 PR #539 content;
- any R048 G2 candidate definition, name, hash, theorem/counterexample, internal structure matrix, productive failure, score, or bridge hypothesis;
- R047C 12x4 calibration matrix or candidate-specific debt vectors;
- any candidate ranking, secondary family, or calibration result that could influence holdout selection;
- classical pi numerical proximity as a target-design criterion.

You may consume repository policy, Foundational Logic V1, Gate V3, and only the high-level inherited pressure-class names listed below. If current project context incidentally exposes candidate-specific material, record `CONTEXT_CONTAMINATION_RISK` and do not use it to choose protocols, tolerances, sources, or pressure types.

## 2. Allowed inherited pressure-class labels

For Block A only, you may know that earlier engineering-success inversion retained four broad effective-side pressure families:

- `GEOMETRIC_MEASURE_COHERENCE`;
- `CYCLE_CLOSURE_AND_RELATIVE_PHASE`;
- `DIFFUSIVE_RELAXATION`;
- `BOUNDED_MODE_SPECTRUM`.

These are target-side labels, not native primitives. Do not import their classical definitions into any native ontology.

Do not read the prior exact protocols/tolerance rows while constructing the new holdout. The new test must be source-independent at protocol/apparatus/scale/channel level.

## 3. Public-source research rule

Use public primary or authoritative sources for the engineering evidence: standards bodies, national metrology institutes, official laboratory protocols, primary technical reports, or peer-reviewed primary engineering papers when no stronger public metrology source exists.

For each source record:

- exact source and date/version;
- what is measured rather than merely calculated;
- controlled inputs/interventions;
- observed outputs;
- scale regime;
- uncertainty/tolerance/error envelope;
- classical/effective representation;
- definition/unit/normalization dependencies;
- weakest definition-stripped operational constraint.

Formula pages alone are not independent empirical evidence.

## 4. Block A — within-family independent holdouts

Freeze at least **one genuinely new holdout protocol for each of the four inherited pressure families**.

A Block-A row must differ materially from the earlier construction surface in at least two of:

- apparatus type;
- measurement chain;
- physical realization/material;
- scale regime;
- intervention variable;
- output channel;
- source/provenance family.

Do not obtain independence merely by citing a newer paper that repeats the same protocol.

For each row, explicitly certify why the measurement chain is independent enough to serve as an out-of-sample holdout.

## 5. Block B — open search for unseen engineering pressures

Search additional engineering domains that were not used to define the four inherited labels. Candidate examples must arise from real successful engineering practice, not from a desire to favor any unknown native mechanism.

Try to identify **2–4 new definition-stripped pressure types**. For every proposed new type:

1. build at least two independent empirical protocol rows if feasible;
2. construct a dependency graph;
3. test whether it reduces to one of the four inherited pressure families or to a shared convention/definition;
4. reject it if it is only a renamed descendant;
5. retain it only if a genuine independent operational residual survives.

It is acceptable to return `NO_NEW_INDEPENDENT_PRESSURE_FOUND` if the dependency quotient kills all candidates. Do not invent novelty to satisfy a quota.

## 6. Definition-stripping and anti-leakage

Reject as target evidence:

- one-number fit to classical pi;
- radians-as-physics;
- Fourier normalization as a foundational constant;
- Gaussian/integral normalization as a foundational constant;
- circle/radius/equidistance definitions counted as measured facts;
- continuum PDE/eigenfunction formulas counted as independent empirical channels;
- calculated values algebraically derived from the same measurement and then double-counted;
- unit conversions counted as new observations.

Preserve the engineering success while stripping inherited definitions.

## 7. Freeze target format

The authoritative R049 holdout object must contain:

- source registry;
- raw engineering rows;
- classical/effective dependency graph;
- definition-stripped constraints;
- dependency quotient;
- Block-A holdout target set;
- Block-B novel-pressure search ledger;
- exact protocol/scale/tolerance envelopes;
- holdout independence certificates;
- contamination audit;
- adversarial leakage tests;
- machine-readable target hash / manifest.

The holdout target must be frozen **before any G2 candidate is opened to this researcher**.

After freeze, candidate calibration may consume the target, but the holdout rows, tolerances, dependency quotient, and scoring eligibility may not change in response to candidate performance. Any later change is a new holdout generation.

## 8. Required adversarial attacks

At minimum attack:

- SAME_PROTOCOL_NEW_SOURCE;
- SAME_DEFINITION_DOUBLE_COUNT;
- UNIT_CONVERSION_AS_NEW_EVIDENCE;
- CALCULATED_OUTPUT_AS_MEASURED_OUTPUT;
- TARGET_CHOSEN_FOR_UNKNOWN_CANDIDATE;
- CLASSICAL_PI_NUMERIC_SELECTION;
- BLOCK_B_RENAMED_OLD_PRESSURE;
- TRAINING_SOURCE_REUSED_AS_HOLDOUT;
- TOLERANCE_INVENTED_WITHOUT_SOURCE.

## 9. Required outputs

Return at least:

- `R049_REPORT.md`;
- `R049_SOURCE_REGISTRY.md/json`;
- `R049_RAW_ENGINEERING_ATLAS.json`;
- `R049_DEPENDENCY_GRAPH.json`;
- `R049_DEFINITION_STRIPPED_CONSTRAINTS.json`;
- `R049_DEPENDENCY_QUOTIENT.json`;
- `R049_BLOCK_A_HOLDOUT_TARGET.json`;
- `R049_BLOCK_B_NOVEL_PRESSURE_LEDGER.json`;
- `R049_HOLDOUT_INDEPENDENCE_CERTIFICATES.json`;
- `R049_CONTAMINATION_AUDIT.json`;
- `R049_ADVERSARIAL_TEST_RESULTS.json`;
- `R049_HOLDOUT_MANIFEST.json`;
- a standard-library checker for hashes, source references, count chains and leakage rules.

## 10. Success / kill / return boundary

Success does not mean finding a candidate that passes. Candidates are absent from this task.

Strong return:

`CANDIDATE_BLIND_INDEPENDENT_ENGINEERING_HOLDOUT_FROZEN / BLOCK_A_COMPLETE / BLOCK_B_QUOTIENTED / CALIBRATION_NOT_RUN / NOT_CANONICAL`

If some inherited family lacks a sufficiently independent public holdout protocol, return the precise source/evidence gap rather than weakening independence.

If all Block-B candidates collapse into inherited families, return that negative result explicitly.

No winner, native pi, or native collapse conclusion is permitted in R049.
