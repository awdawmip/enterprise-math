<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-TR-TROPICAL-RESIDUATION-IDEMPOTENT-CLOSURE-CALCULUS",
  "title": "Tool Discovery A — Tropical / Residuation / Idempotent Closure Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "MEDIUM_HIGH",
  "frontier": "ENTERPRISE_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_TOOL_CLASSIFIED",
  "next_action": "Classify whether explicitly weighted finite Enterprise transition systems support a reusable idempotent-semiring closure/residuation/fixed-point calculus beyond existing order-adjoint and quotient machinery; otherwise freeze the strongest composition, extension, alias, or no-go verdict.",
  "dependencies": [
    "enterprise_toolbox_registry.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "research_method_inventory.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "tool_invocation_policy.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5"
  ],
  "source_refs": [
    "src/enterprise_math/material_adjoint.py@3a1962b6fe9e62ada6675143e17c3e6ff0fe2fe0",
    "src/enterprise_math/adjoint_boundary_precision.py@a1e73b6d97f116cbb1127d1ba08a47a061318897",
    "enterprise_toolbox_registry.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "research_method_inventory.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": [
    "tool-discovery",
    "A",
    "tropical",
    "residuation",
    "idempotent-semiring",
    "kleene-star",
    "fixed-point",
    "path-closure"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDTR",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Tool Discovery A — Tropical / Residuation / Idempotent Closure Calculus

Task-ID: `RS-TD-TR-TROPICAL-RESIDUATION-IDEMPOTENT-CLOSURE-CALCULUS`

Intended owner branch:

`research/tool-tropical-residuation-idempotent-closure`

## 0. Driver capability-gap classification

This task follows the project-wide reuse-before-invention rule.

Current coverage audit found no registered T0–T9 family and no current executable owner explicitly providing:

- max-plus or min-plus matrix/path closure;
- idempotent-semiring Kleene star;
- residual solution of semiring inequalities;
- finite Bellman-style least/greatest fixed-point closure;
- path-envelope compression over explicitly declared weights.

However, Enterprise Math already contains genuine order-adjoint machinery. In particular:

- `material_adjoint.py` explicitly identifies itself as an E001 specialization of the older P008 adjoint pattern;
- `adjoint_boundary_precision.py` supplies order-adjoint threshold pullback behavior;
- T6 already owns operation-safe quotient and predictive refinement.

Therefore **residuation or adjunction by itself is not a capability gap**.

A positive result must exhibit a genuinely reusable layer whose capability is not exhausted by P008-style monotone adjunction or by T6 quotient construction.

Hard target:

`ENTERPRISE_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_TOOL_CLASSIFIED`.

## 1. Mother question

Suppose an Enterprise problem explicitly supplies a finite weighted transition system or weighted relation. Can one derive a reusable exact calculus that compresses path optimization and monotone inequality solving through an idempotent semiring?

The candidate capability is approximately:

> local weighted transitions -> semiring path composition -> all-path closure / envelope -> residual inequality solver -> least or greatest fixed-point certificate.

The task is to classify this capability, not to import tropical geometry vocabulary wholesale.

## 2. Admissible semantic input

The tool may start only when the caller explicitly supplies the weighted semantics.

Examples of admissible input include:

- a finite state set `X`;
- a finite directed transition relation `E`;
- a declared weight map `w:E->S`;
- a declared idempotent semiring or dioid-like carrier `(S,oplus,otimes,0,1)`;
- or one of the standard finite-path specializations such as min-plus or max-plus, with explicit infinity convention.

The meaning of a weight must be part of the caller's data: cost, grade, delay, score, capacity level, threshold, or another declared quantity.

Forbidden inference:

- bare incidence does not create a cost;
- path length is not a native metric unless independently declared;
- max-plus value is not automatically probability, amplitude, energy, utility, or geometric distance;
- an implementation priority is not mathematical weight.

## 3. Candidate reusable API

A positive tool should classify an interface of roughly this strength:

- `VALIDATE_SEMIRING` — exact finite/declared law checks at the supported level;
- `WEIGHTED_RELATION` — construct the semiring-valued transition matrix/operator;
- `COMPOSE` — semiring matrix/relation composition;
- `PATH_VALUE` — exact value of one path;
- `POWER` — fixed-length path envelope;
- `KLEENE_STAR` or `CLOSURE` — all-length finite closure under precise hypotheses;
- `RESIDUAL_LEFT` / `RESIDUAL_RIGHT` — greatest solution of inequalities such as `A otimes x <= b` or its declared order-dual form when residuation exists;
- `BELLMAN_OPERATOR` — monotone dynamic operator;
- `LEAST_FIXED_POINT` / `GREATEST_FIXED_POINT` — exact finite fixed-point computation under declared order/completeness hypotheses;
- `OPTIMAL_PATH_CERT` — witness path, predecessor structure, or equality certificate;
- `UNBOUNDED_CYCLE_CERT` — witness of an improving cycle or failure of finite optimum;
- `OBSTRUCTION` — missing semiring law, missing weight semantics, incomplete order, or nonresiduated operator.

A wrapper around ordinary shortest-path code without a reusable algebraic contract is `RESULT_NOT_TOOL`.

## 4. Structural laws to classify

### 4.1 Idempotence and canonical order

If `a oplus a = a`, classify the induced natural order precisely.

Do not assume totality unless the chosen semiring has it.

### 4.2 Path composition law

Prove that semiring matrix powers encode fixed-length path envelopes at the exact supported finite level.

Classify zero/unreachable and infinity conventions explicitly.

### 4.3 Closure / Kleene star

State exactly when

`I oplus A oplus A^2 oplus ...`

has a finite algebraic interpretation.

Distinguish:

- finite acyclic carriers;
- bounded simple-path reductions;
- complete idempotent semirings;
- improving cycles;
- star-continuous assumptions if invoked.

### 4.4 Residuation

For each supported operator, prove the exact Galois/residual law, for example:

`A otimes x <= b  iff  x <= A\b`

or the correctly typed analogue.

The researcher must explicitly compare this with P008 order adjunction and state what new multi-state/path-compositional capability remains.

### 4.5 Fixed points

Classify which Bellman/dynamic operators have least or greatest fixed points and how they are computed exactly on the supported finite ordered carrier.

Do not silently invoke completeness outside the declared carrier.

### 4.6 Composition

Show whether closure, residuals, and fixed-point solvers compose across block systems, products, or declared quotients.

Any composition with T6 must preserve T6's semantic quotient requirements.

## 5. Mandatory dedup against current Enterprise tools

### P008 / current order-adjoint machinery

Existing adjoint modules already establish nontrivial finite order adjunctions.

A positive new tool must demonstrate that the important new object is something like:

- path-compositional idempotent linearity;
- all-path closure;
- matrix/operator residuation;
- or fixed-point envelope compression.

If the result is only a one-dimensional monotone-map adjunction, classify it as a prior specialization or extension of the P008 owner.

### T6 — Operation-Safe Quotient

T6 answers which distinctions may be collapsed while preserving declared operations/observations.

A tropical/residuated tool may operate on a quotient after T6 certifies it, but it must not choose the quotient by optimizing a target value.

### T1 — Scale Enumeration

T1 counts scale/shell families; it does not optimize weighted paths. If the new result only enumerates path lengths or score histograms, use T1.

### T3 — Incidence Circuit

T3 may expose cycles responsible for an improving-cycle certificate. The weighted closure value itself is not currently a T3 output.

### T9 — Holonomy / Gluing

Route-dependent weighted path value is not automatically holonomy. If a loop defect is the true invariant, T9 may own the problem.

## 6. Two-domain reuse gate

A positive global family requires two genuinely different Enterprise uses.

### Application A — weighted path/provenance system

Take a finite path or transition skeleton with explicitly declared weights.

Demonstrate a real compression such as:

- replacing exponential path enumeration by a closure operator;
- extracting an optimum plus a finite certificate;
- detecting an improving cycle;
- or solving a family of path inequalities via residuals.

### Application B — threshold/precision/relation propagation

Use a second non-path-renaming application with an independently meaningful ordered weight, such as:

- threshold propagation;
- precision level/cost propagation;
- relation score/capacity propagation;
- finite scheduling or dependency grades if such semantics are explicitly present.

Show a residual or fixed-point calculation that is not merely the same shortest-path example with renamed vertices.

## 7. Required negative boundaries

Produce explicit counterexamples or non-applicability classifications for at least:

- bare unweighted relation;
- non-idempotent addition when the claimed canonical order relies on idempotence;
- a partial order where total-order shortcuts fail;
- improving cycles causing absence of a finite optimum in the selected convention;
- an operator lacking a residual;
- an incomplete carrier where an infinite supremum/infimum is silently assumed;
- an operation-safe quotient that does not preserve the declared weights;
- path-envelope equality incorrectly promoted to a native metric statement.

## 8. Classical prior-art discipline

Tropical algebra, max-plus/min-plus algebra, dioids, residuated mappings, Kleene algebra, Bellman operators, shortest/longest path closure, and related fixed-point mathematics are classical.

The return must separately classify:

1. classical theorem content;
2. prior Enterprise P008/T6/T3/T9 overlap;
3. new Enterprise semantic interface or composition;
4. any genuinely new theorem, if one unexpectedly appears;
5. duplicate/alias/no-tool outcome.

`CLASSICAL_IDEMPOTENT_ALGEBRA_PACKAGED_FOR_ENTERPRISE != NEW_THEOREM`.

## 9. Deterministic checker

Required executable:

`scripts/tool_discovery_tropical_residuation_idempotent_closure_check.py`

Minimum exact regression:

- small min-plus and max-plus matrices;
- fixed-length matrix powers versus exhaustive path envelopes;
- acyclic closure versus exhaustive all-path enumeration;
- finite cyclic examples with and without improving cycles;
- left/right residual law checks on small finite carriers;
- Bellman fixed-point verification;
- unreachable/infinity edge cases;
- relabeling invariance;
- the two Enterprise applications;
- explicit negative counterexamples;
- mismatch count `0` for every exact claim checked.

Avoid floating approximation unless the declared weight carrier itself requires it; integer/rational examples are preferred for the theorem ledger.

## 10. Tool acceptance gate

A positive result must provide:

1. explicit weighted semantic input contract;
2. reusable closure/residual/fixed-point API;
3. at least one nontrivial algebraic law or compact certificate;
4. exact failure boundary;
5. two-domain reuse;
6. real path-search/inequality/fixed-point compression;
7. exact dedup against P008 and T0–T9.

Allowed terminal classifications:

- `NEW_GLOBAL_TOOL_FAMILY`;
- `NEW_ENTERPRISE_TOOL_INTERFACE`;
- `EXTEND_P008_ORDER_ADJOINT`;
- `COMPOSE_P008_T3_T6`;
- `DOMAIN_SPECIALIZATION_ONLY`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`;
- `EXACT_NO_GO`.

The hard target is classification, so a well-proved downgrade is a successful task return.

## 11. Required artifacts

Return:

1. `research_notes/TOOL_DISCOVERY_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_RESULT_20260823.md`
2. `scripts/tool_discovery_tropical_residuation_idempotent_closure_check.py`
3. optional reusable source module only if the tool gate is met.

The report must include:

- Researcher-ID;
- exact source baseline;
- declared semiring/order semantics;
- coverage and dedup table;
- theorem/status ledger;
- two-domain reuse evidence;
- explicit counterexamples;
- checker summary;
- strongest final classification.

## 12. Stop condition

Freeze the terminal classification and required artifacts, then stop this task.

Do not create a successor merely because a tropical/residuated interface works on the selected examples.

---

Driver issue note:

`A HISTORICAL TOOL CANDIDATE; THE GAP IS PATH-COMPOSITIONAL CLOSURE/RESIDUATION/FIXED-POINT CAPABILITY, NOT ADJUNCTION ITSELF.`
