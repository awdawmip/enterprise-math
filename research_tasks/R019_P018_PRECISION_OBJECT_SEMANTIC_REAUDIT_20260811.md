<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R019-P018-PRECISION-OBJECT-SEMANTIC-REAUDIT",
  "title": "R019 P018 Precision-Object Semantic Re-audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Re-audit P018 after R015-R017 by typing every precision object and theorem as exact state, deterministic selector/projection, quotient cell, set-valued support, or task-relative refined carrier; separate static representation from dynamic closure/composition and identify only the rows that truly require repair.",
  "next_action": "Build a theorem/tool inventory for P018 canonical owner artifacts, test dynamic exactness where a projection is reused between future operations, and return a frozen impact matrix before any semantic rewrite.",
  "dependencies": [
    {
      "target": "RS-R017-PTH-POWER-UNRESOLVED-CARRIER-CLASSIFICATION",
      "action": "CONSUME_ACCEPTED_CARRIER_BOUNDARY",
      "satisfied": true
    },
    {
      "target": "P018 canonical theorem/tool family",
      "action": "AUDIT_OWNER_ARTIFACTS",
      "satisfied": true
    },
    {
      "target": "P023 deterministic quotient sector",
      "action": "USE_FUNCTIONAL_SAFE_BASELINE",
      "satisfied": true
    }
  ],
  "source_refs": [
    "research_common_surface.json::P018_P023_power_free_action_basis",
    "research_common_surface.json::P018_centered_prime_radius",
    "EnterpriseMath/Quotient/PowerFreeActionBasis.lean",
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md",
    "R017 accepted Driver package / journal checkpoint"
  ],
  "evidence_status": "SEMANTIC_REAUDIT_GATE",
  "last_progress_ref": "R017 Driver acceptance and first R009/P023 impact audit",
  "last_progress_at": "2026-08-11T14:27:00+08:00",
  "hard_block": null,
  "tags": [
    "R019",
    "P018",
    "precision",
    "projection",
    "carrier",
    "cell",
    "support",
    "quotient",
    "semantic-audit"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R019",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:87a1272862a3d84b01bc6d2a8617486a2ca998c1ab1cfd016f29c6b6edd7f64e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R019 — P018 Precision-Object Semantic Re-audit

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / SEMANTIC RE-AUDIT GATE / NOT CANONICAL`

## 1. Mother question

After R015-R017, determine exactly what mathematical object each P018 “precision” construction represents and which old conclusions remain valid.

Do not assume that a precision map always returns one operational state.

For every audited object distinguish, where applicable:

1. exact fine state;
2. deterministic selector/projection;
3. quotient or cell identifier;
4. full fine fibre;
5. set-valued result support;
6. task/future-signature refinement.

The goal is classification before repair.

## 2. Required audit targets

### R019-T01 — canonical P018 inventory

Build a complete owner-level inventory of the currently reusable P018 theorem/tool family, starting from the common-surface P018 entries and following only their direct canonical owner artifacts.

For every theorem, executable and Lean declaration record:

- exact statement/interface;
- mathematical owner/source;
- current evidence status;
- input state type;
- output precision-object type;
- whether future operations are applied to the output.

Do not treat documentation aliases as separate theorem owners.

### R019-T02 — semantic typing matrix

Assign every row exactly one primary status:

- `SEMANTICALLY_STABLE`;
- `THEOREM_STABLE / INTERPRETATION_CHANGED`;
- `CONDITIONALIZED`;
- `COUNTEREXAMPLE_RISK`;
- `TOOL_ASSUMPTION_MISMATCH`.

For every non-stable row state the minimal reason and the smallest required action.

### R019-T03 — representation versus operational closure

Separate theorems that only describe/encode a precision class from theorems that require the projected object to support later execution.

A static representation theorem is not invalid merely because repeated execution on that representation is not exact.

Conversely, any theorem/tool that composes future operations after projection must identify the exact compatibility condition it uses.

### R019-T04 — re-projection / repeated-collapse audit

For each P018 quotient or precision projection `q` that is used between future operations, classify the relevant operation family using the R017 distinctions:

- deterministic functional descent;
- fine-support exactness;
- one-step full-cell exactness;
- finite-word composition exactness;
- repeated saturation/re-projection exactness.

Where a claimed dynamic closure does not follow, produce a minimized counterexample rather than silently strengthening the stored state.

### R019-T05 — P018/P023 power-free action basis

Re-audit the canonical power-free action-basis theorem and its Lean/executable realization.

Determine whether its least-separating-set result is unchanged because it is explicitly a deterministic observation-family separation theorem, or whether any surrounding interpretation incorrectly upgrades it into a universal precision carrier.

Preserve the theorem if stable; distinguish theorem truth from project-wide interpretation.

### R019-T06 — centered-prime-radius and other arithmetic-only P018 slices

Audit P018 arithmetic specializations that do not execute a coarse state through later operations.

Confirm whether they are semantically independent of the new carrier distinction. Do not reopen elementary arithmetic results without a concrete dependency.

### R019-T07 — executable semantic-assumption inventory

For each P018 executable touched by T01, record whether it implements:

- exact-state arithmetic;
- deterministic projection;
- quotient-cell computation;
- set-valued support;
- repeated re-projection.

Run focused regression or mutation tests only where the semantic label is ambiguous or a dynamic-exactness claim is made.

Do not rewrite a correct deterministic-sector tool merely because broader semantics now exist.

### R019-T08 — downstream interface impact

Return explicit consequences for:

- P021 witness/cardinality compression;
- P010/P011 history/collision semantics;
- P023 terminology;
- R009 deterministic lower-collapse sector;
- R014 resource accounting.

For each downstream area state whether R019 supplies a hard dependency, an informational constraint, or no material change.

## 3. Mandatory decision artifact

Return one theorem/tool impact matrix with columns:

- artifact / theorem;
- old semantic reading;
- actual mathematical type;
- new status;
- proof validity;
- executable validity;
- counterexample if any;
- minimal repair/relabel action;
- downstream owner.

The matrix, not prose alone, is the acceptance object.

## 4. Kill pressure

Actively search for these failure modes:

- a quotient label treated as a literal representative;
- one-step exactness used as if it implied composition exactness;
- a deterministic separation theorem treated as support completeness;
- repeated projection introducing extra fine representatives;
- hidden future-dependent coordinates dropped by a precision map.

Also record negative results: if a suspected failure is absent, say why.

## 5. Scope boundary

This task audits P018 and may add owner-local research/test evidence needed to decide status.

It does not rewrite P018/P023/R009 shared semantics and does not open descendant tasks.

A genuinely new mathematical residue should be returned to Driver as a proposal candidate, not silently expanded.

## 6. Return criteria

Preferred clean return:

`P018_REAUDIT_COMPLETE / IMPACT_MATRIX_FROZEN / STABLE_ROWS_PRESERVED / REPAIR_ROWS_ISOLATED / NOT_CANONICAL`

If a canonical P018 theorem is actually false in its stated scope:

`P018_THEOREM_BREAK_FOUND / COUNTEREXAMPLE_VERIFIED / OWNER_REPAIR_REQUIRED / NOT_CANONICAL`

If all theorem statements survive and only interpretation/tool labels change:

`P018_THEOREMS_STABLE / SEMANTIC_RELABELLING_ONLY / TOOL_AUDIT_COMPLETE / NOT_CANONICAL`
