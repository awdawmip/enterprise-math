<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-HR-ENTERPRISE-HELLY-RADON-CERTIFICATE-CALCULUS",
  "title": "Tool Discovery — Enterprise Helly / Radon Finite-Certificate Calculus",
  "kind": "RESEARCH",
  "owner": "research/tool-enterprise-helly-radon-certificates",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Discover bounded local certificates for global feasibility, compatibility, gluing, or obstruction across Enterprise discrete structures.",
  "next_action": "Extract Helly/Radon/Caratheodory local-to-global mechanisms, define Enterprise constraint classes and certificate numbers, and test reuse on at least two distinct global-compatibility problems.",
  "dependencies": [
    "current Enterprise foundational logic",
    "current native foundation router",
    "historical Helly / Radon / Caratheodory mechanisms used only as comparison and inspiration"
  ],
  "source_refs": [
    "awdawmip/enterprise-math@00765cc76ea71f789481fbe91c29d852bbf6b209:FOUNDATIONAL_LOGIC.md",
    "awdawmip/enterprise-math@00765cc76ea71f789481fbe91c29d852bbf6b209:definitions/00_CURRENT_NATIVE_FOUNDATION.md"
  ],
  "foundation_questions": [],
  "evidence_status": "DRIVER_OPENED_TOOL_DISCOVERY",
  "last_progress_ref": null,
  "last_progress_at": "2026-08-22T21:54:00+08:00",
  "hard_block": null,
  "tags": [
    "tool-discovery",
    "helly",
    "radon",
    "caratheodory",
    "finite-certificate",
    "local-to-global"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "TDHR",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d5cbe89c8620ca6efa2af5219900424485c85bba1fc042576e17034c10e38299",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Tool Discovery — Enterprise Helly / Radon Finite-Certificate Calculus

Status: `READY / DRIVER_APPROVED / PARALLEL TOOL DISCOVERY`

## 0. Mother question

Does Enterprise Math contain natural classes of global feasibility or compatibility problems for which failure/success is controlled by a bounded-size local certificate?

The target pattern is not a copied convexity theorem. It is a reusable implication of the form

`ALL SMALL SUBFAMILIES PASS  ->  WHOLE FAMILY PASSES`,

or its obstruction dual

`GLOBAL FAILURE  ->  SMALL FAILURE WITNESS`,

with the smallest valid bound treated as an Enterprise certificate number for the declared constraint class.

## 1. Historical mechanism to extract

Study the operational relationship among:

- Helly-type bounded subfamily intersection tests;
- Radon-type forced partition/intersection phenomena;
- Caratheodory-type bounded generating witnesses;
- nerve/minimal-obstruction viewpoints where relevant.

Do not assume convexity, Euclidean dimension, or classical affine combination exists natively. Identify the abstract ingredients responsible for finite certificates.

## 2. Build an Enterprise constraint language

Define at least one precise abstract class of constraints with:

1. a state/realization space;
2. a family of local constraints or admissible subsets;
3. a precise notion of global feasibility/compatibility;
4. restriction to subfamilies;
5. a witness object for failure or success;
6. symmetry/relabeling behavior.

Then define a candidate certificate number `h(C)` or prove that no finite bound exists for that class.

Do not hide growing problem size inside the definition of a “local” constraint.

## 3. Required theorem pressure

For each positive finite-certificate class, determine:

- existence of a finite certificate bound;
- the best proven bound;
- exact small sharp examples when possible;
- minimal obstruction families;
- whether a Radon-like partition principle or Caratheodory-like generator bound is equivalent, stronger, weaker, or unrelated;
- algorithmic consequence: how many local checks replace one global search.

A mere finite brute-force bound depending on total state count is not enough to qualify as a Helly-style tool unless it compresses the problem structurally.

## 4. Cross-domain tool test

A positive tool verdict requires reuse on at least **two genuinely different Enterprise compatibility problems**.

Candidate categories include, but are not limited to:

- sector/path/chart gluing or common realization;
- compatibility of multiple precision/refinement/lift constraints;
- BRC/path-support simultaneous feasibility;
- component/event relation consistency;
- another current global-consistency problem with a distinct state type.

The same certificate calculus must drive both applications. Two separately proved bounded cases do not establish one tool.

## 5. Obstruction-first route is allowed

If finite Helly numbers fail broadly, classify exactly why. Useful outcomes include:

- an explicit infinite family with unbounded minimal obstruction size;
- a structural condition that restores bounded certificates;
- a hierarchy `class restriction -> finite certificate number`;
- a dual invariant measuring distance from local-to-global closure.

A sharp no-go plus the weakest repair condition is a strong tool-discovery outcome.

## 6. Tool acceptance gate

Classify the final result using exactly one leading verdict:

- `ENTERPRISE_FINITE_CERTIFICATE_CALCULUS_DISCOVERED`
- `CLASS_RESTRICTED_HELLY_TOOL_DISCOVERED`
- `RESULT_NOT_TOOL`
- `EXACT_NO_GO_FOR_BOUNDED_CERTIFICATES`

Use `ENTERPRISE_FINITE_CERTIFICATE_CALCULUS_DISCOVERED` only if all are present:

- explicit reusable constraint interface;
- finite local certificate theorem with nontrivial structural bound;
- extraction of minimal failure/success witnesses;
- successful reuse on two distinct Enterprise problem families;
- an exact negative boundary describing when the certificate theorem fails.

## 7. Deliverables

Return:

1. formal constraint/certificate definitions;
2. theorem proofs or exact no-go family;
3. sharpness witnesses on small instances;
4. historical comparison and conservative novelty statement;
5. executable bounded verification where useful;
6. a `TOOL API` section: constraint input, certificate output, bound, witness extractor, composition behavior, failure modes;
7. two cross-domain demonstrations;
8. the leading verdict from Section 6.

Do not modify current Foundation definitions in this task.