<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R020-P021-WITNESS-CARDINALITY-DYNAMIC-COMPLETENESS-REAUDIT",
  "title": "R020 P021 Witness/Cardinality Dynamic-Completeness Re-audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Re-audit P021 witness/cardinality compression after R015-R019 by separating static one-step statistics from reusable current-state carriers. Determine exactly when cardinality matrices, witness counts, direction summaries or reduced relation data preserve future reachable support under composition, and when middle-incidence witness information or a task-relative refinement is necessary.",
  "next_action": "Build a declaration/tool inventory of P021 positive and negative compression results, classify each by static versus dynamic semantics, construct minimized composition counterexamples where summaries lose future-readable witness information, and freeze the strongest exact closure criteria and impact matrix without editing canonical P021 semantics.",
  "dependencies": [
    {
      "target": "RS-R019-P018-PRECISION-OBJECT-SEMANTIC-REAUDIT",
      "action": "CONSUME_FROZEN_PRECISION_OBJECT_TYPING",
      "satisfied": true
    },
    {
      "target": "RS-R017-PTH-POWER-UNRESOLVED-CARRIER-CLASSIFICATION",
      "action": "CONSUME_SUPPORT_AND_RECOLLAPSE_BOUNDARY",
      "satisfied": true
    },
    {
      "target": "RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE",
      "action": "CONSUME_RESULT_SUPPORT_GATE",
      "satisfied": true
    },
    {
      "target": "P021 canonical witness/direction/cardinality theorem family",
      "action": "AUDIT_OWNER_ARTIFACTS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R019 accepted Driver return / frozen impact matrix",
    "R017 accepted Driver package / support-completeness boundary",
    "R015/R016 accepted branch-deferral core",
    "P021 canonical owner documents / Lean / executable artifacts on current common surface",
    "research_common_surface.json A3/A4 relation and support bridge entries",
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md"
  ],
  "evidence_status": "DYNAMIC_COMPRESSION_REAUDIT_GATE",
  "last_progress_ref": "R019 Driver acceptance",
  "last_progress_at": "2026-08-11T15:06:00+08:00",
  "hard_block": null,
  "tags": [
    "R020",
    "P021",
    "witness",
    "cardinality",
    "direction",
    "compression",
    "composition",
    "support",
    "future-signature",
    "semantic-audit"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R020",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:87a1272862a3d84b01bc6d2a8617486a2ca998c1ab1cfd016f29c6b6edd7f64e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R020 — P021 Witness/Cardinality Dynamic-Completeness Re-audit

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / DYNAMIC COMPRESSION RE-AUDIT GATE / NOT CANONICAL`

## 1. Mother question

R019 froze a key distinction:

> a mathematically correct statistic or observation of the current fine object is not automatically a sufficient state for the next composition step.

R020 applies this distinction to P021.

The mother question is:

> when may P021 replace fine witness/relation data by cardinalities, direction summaries, matrices, orbit counts, or other compressed objects and still obtain exactly the same declared future result-support after further composition?

Do not assume that a one-step exact count, marginal matrix, or direction summary is dynamically complete.

Conversely, do not invalidate a correct static counting theorem merely because the compressed statistic is not recursively executable.

## 2. Frozen semantic distinctions

Every audited P021 object must be typed, where applicable, as one of:

1. exact fine relation / witness structure;
2. deterministic observation or statistic of that structure;
3. quotient/cell identifier;
4. full fine fibre of structures compatible with the observation;
5. set-valued current result support;
6. multiplicity/path-count observable;
7. task/future-signature refinement sufficient for declared future use.

For dynamic claims distinguish:

- one-step statistic exactness;
- one-step reachable-support exactness;
- multiplicity/count exactness;
- composition exactness;
- repeated compression/re-expansion exactness;
- finite-word future-signature exactness.

Boolean reachable support and path/witness multiplicity are different observables.

## 3. Required audit targets

### R020-T01 — canonical P021 inventory

Build a declaration-level inventory of the current reusable P021 theorem/tool family.

Start from the current common-surface P021 owner/router entries and follow only direct owner artifacts needed to cover:

- direction transport;
- witness incidence;
- direction/cardinality matrices or tables;
- one-step reductions;
- composition results and counterexamples;
- uniform-fibre or other positive exact-reduction regimes;
- executable checks used to support those results.

For every row record:

- exact statement/interface;
- mathematical object being compressed;
- compressed output type;
- observable preserved;
- whether the output is ever reused as input to another operation;
- current evidence status.

### R020-T02 — static theorem versus dynamic carrier

Classify every positive P021 result as either:

A. static representation/statistic theorem only; or  
B. theorem asserting enough closure to reuse the compressed object in later composition.

A static exact formula for a matrix/count/cardinality remains valid even if B fails.

Any B-row must state the actual closure/factorization hypothesis.

### R020-T03 — middle-incidence witness boundary

Reconstruct the smallest P021-style example in which two fine relation/witness systems have the same compressed one-step summary but differ after composition because the middle witness incidence is different.

The counterexample must distinguish at least:

- same one-step cardinality/marginal data;
- different composed reachable result support, if possible;
- or, when reachable support agrees, different multiplicity/path-count.

Minimize by state/witness count.

State exactly which information is missing from the compressed object.

### R020-T04 — support versus multiplicity

For each P021 matrix/counting interface determine whether it preserves:

- Boolean existence/reachable support;
- number of middle witnesses;
- number of paths;
- branch identity/provenance;
- higher incidence correlations.

Use R015/R016 only for the Boolean result-support observable after a legitimate current relational state has already been fixed.

Do not use branch-deferral invariance to erase multiplicity or future-readable witness information.

### R020-T05 — exact dynamic-completeness criterion

Derive the strongest correct criterion for a P021 compression map

\[
q:X\to Q
\]

to be reusable under a declared future relation/operation language.

Express the result by factorization/kernel or support-signature language whenever possible.

At minimum distinguish:

1. deterministic functional descent;
2. one-step coarse successor-support constancy;
3. exact finite-word final support;
4. multiplicity/path-count preservation.

If one clean iff is available for the declared finite setting, prove it. Otherwise return a hierarchy with strict implications/counterexamples.

Do not duplicate R017/R018 generic saturation theorems; specialize or consume them.

### R020-T06 — uniform-fibre positive regime

Re-audit the strongest existing P021 positive theorem in which uniform fibres or another regularity hypothesis makes a cardinality/direction reduction exact.

Determine precisely what becomes exact:

- a one-step count;
- a Boolean support relation;
- a composed count;
- arbitrary finite-word support;
- or some narrower quantity.

If the theorem is stronger than previously appreciated, state the exact closure consequence.
If it is only static/one-step, preserve the theorem and narrow the interpretation.

### R020-T07 — quotient / matrix composition law

For every P021 matrix-like representation used compositionally, compare:

\[
M_{S\circ R}
\]

with the proposed product/composition built from \(M_R,M_S\).

Test both Boolean and arithmetic/counting products when relevant.

Produce minimized examples for every failed blanket identity.

If an exact product law exists under a structural condition, isolate the weakest useful condition and relate it to middle-incidence information.

### R020-T08 — executable semantic-assumption audit

Audit the P021 executables touched by T01–T07.

For each tool identify whether it computes:

- exact relation support;
- one-step cardinalities;
- path multiplicities;
- direction marginals;
- full incidence;
- recursively executable compressed state.

Run focused exhaustive or mutation checks only where the semantic boundary is not already mechanically explicit.

A correct static counting tool is not a tool mismatch merely because its result is not a future-complete state.

### R020-T09 — downstream impact

Return explicit consequences for:

- P010/P011 history/fibre/collision statistics;
- P023 functional/support/composition terminology;
- P018 precision-object typing;
- R014 resource/Pareto accounting;
- A3/A4 relation-to-support bridge.

For P010/P011 specifically decide whether a separate new research task is still warranted.

If their theorem truth is unchanged and only an informational boundary is needed, say so and recommend no new mother task.

## 4. Mandatory decision artifact

Return one frozen theorem/tool impact matrix with columns:

- artifact / theorem;
- fine object;
- compressed object;
- preserved observable;
- static exact?;
- one-step support exact?;
- composition exact?;
- multiplicity exact?;
- new semantic status;
- counterexample / hypothesis;
- required action;
- downstream owner.

Allowed primary row statuses:

- `SEMANTICALLY_STABLE`;
- `THEOREM_STABLE / INTERPRETATION_CHANGED`;
- `CONDITIONALIZED`;
- `COUNTEREXAMPLE_RISK`;
- `TOOL_ASSUMPTION_MISMATCH`.

## 5. Kill pressure

Actively test these failure modes:

- equal cardinality matrices with different composed support;
- equal Boolean support with different path multiplicity;
- uniform one-step fibres that cease to be uniform after composition;
- a summary sufficient for one declared future but not for a larger language;
- a marginal direction table that loses middle-incidence correlation;
- a set-valued support accidentally treated as a count matrix, or vice versa.

Also record negative results when a suspected failure cannot occur under the theorem's actual hypotheses.

## 6. Prior-art/rooting discipline

Generic relation composition, Boolean matrices, path-count matrices, bisimulation/congruence, sufficient statistics, automata/coalgebraic behavioural equivalence, and matrix semiring semantics are prior mathematics.

Root generic results accordingly.

The project-specific residue, if any, is the exact classification of which P021 witness/direction compressions retain which observables under the declared Enterprise Math future languages.

## 7. Scope boundary

This task is a semantic re-audit.

It does not directly rewrite P021/P023/P010/P011 shared semantics.

It does not re-prove a stable static theorem solely because its interpretation becomes narrower.

It does not create descendant tasks.

Return new task candidates to Driver only if a genuine mathematical residue survives.

## 8. Return criteria

Preferred clean return:

`P021_REAUDIT_COMPLETE / DYNAMIC_COMPRESSION_MATRIX_FROZEN / STATIC_ROWS_PRESERVED / COMPOSITION_ROWS_CLASSIFIED / NOT_CANONICAL`

If one or more canonical P021 statements are false in their stated scope:

`P021_THEOREM_BREAK_FOUND / COUNTEREXAMPLE_VERIFIED / OWNER_REPAIR_REQUIRED / NOT_CANONICAL`

If all mathematical statements survive but dynamic interpretation narrows:

`P021_THEOREMS_STABLE / DYNAMIC_CARRIER_SCOPE_NARROWED / TOOL_AUDIT_COMPLETE / NOT_CANONICAL`
