<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R052-FORMAL-PLANE-PI-TYPABILITY-MULTIPLICITY-COHERENCE",
  "title": "R052 — Formal Plane Pi: Typability, Multiplicity and Coherence",
  "kind": "PURE_MATHEMATICS_RESEARCH",
  "owner": "program/formal-plane-pi",
  "base_state": "NEW_MOTHER_QUESTION",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_PI_TYPING / FORMAL_GEOMETRY / COHERENCE_THEORY",
  "frontier": "Determine when pi-role objects first become well-typed in weak formal plane languages, whether distinct roles can coexist without equality, and which minimal additional axioms force symbolic coherence before any classical Euclidean identification.",
  "next_action": "Freeze a diverse formal-plane signature family from the R052 foundation packet, prove typability/no-go results and role multiplicity, build a coherence-axiom lattice, investigate finite/refinement models, and only then allow a sealed symbolic comparison with the classical Euclidean plane.",
  "dependencies": [
    {"target":"research_inputs/R052_FORMAL_PLANE_PI_FOUNDATION_PACKET_20260813.md @ b6a34afb213558e974569ef63c19db606b882931","action":"CONSUME_AS_ONLY_PROBLEM_PACKET","satisfied":true},
    {"target":"FOUNDATIONAL_LOGIC.md / foundational_logic.json","action":"CONSUME_AS_SEMANTIC_DISCIPLINE_ONLY","satisfied":true},
    {"target":"native_semantics_admissibility.json Gate V3","action":"CONSUME_AS_TYPING_DISCIPLINE_ONLY","satisfied":true}
  ],
  "evidence_status": "PURE_FORMAL_FOUNDATION_RESEARCH",
  "hard_block": null,
  "tags": ["R052","formal-plane","pi","typability","multiplicity","coherence","finite-refinement","pure-math"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "NEW_RESEARCHER_ID_REQUIRED",
  "identity_lane": "R052",
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242","review_state":"PASS","temporary_overrides":[]}
}
-->

# R052 — Formal Plane Pi: Typability, Multiplicity and Coherence

Status: `READY / P0 / PURE FORMAL MATHEMATICS / ENGINEERING ISOLATED / NOT CANONICAL`

## 0. Purpose

This task opens a new pure-mathematics mother question independent of the R046–R051 engineering-success line.

The central question is:

> What is the weakest formal notion of a plane under which one or more internally defined `pi-role` objects become well-typed, and under what additional axioms are independently defined pi-roles forced to coincide?

This task is **not** to recover the decimal expansion of classical pi, and it is **not** to assume the textbook circumference/diameter definition and re-express it.

Core research order:

`TYPABILITY -> MULTIPLICITY -> COHERENCE -> IDENTIFICATION`

Forbidden order:

`KNOWN CLASSICAL PI -> CHOOSE STRUCTURE -> RECONSTRUCT SAME DEFINITION`.

## 1. Required inputs and isolation

At startup consume only:

1. current project-level `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` as semantic discipline;
2. current `native_semantics_admissibility.json` Gate V3 as type discipline;
3. `research_inputs/R052_FORMAL_PLANE_PI_FOUNDATION_PACKET_20260813.md` from exact source commit `b6a34afb213558e974569ef63c19db606b882931`.

Before the formal role/theorem freeze, do **not** consume mathematical content from:

- R046 engineering-success atlas/kernel/interface;
- R047 engineering calibration target/results;
- R048 G2 candidate mechanisms;
- R049 engineering holdout protocols;
- R050 matrices, bridge results, debts or Pareto observations;
- R051 quantitative-data targets/source-selection results.

Do not use classical pi decimal/numerical approximations as a theorem, model, role, refinement, or axiom selection signal at any stage.

If project context incidentally exposes any forbidden target-specific information, record `CONTEXT_CONTAMINATION_RISK`, quarantine it, and do not use it to generate, modify, rank or kill a formal signature or pi-role.

## 2. Stage A — Formal-plane signature explosion and freeze

Do **not** start by choosing Euclidean geometry.

Generate and analyze **4–8 serious formal-plane signatures or signature families** with meaningfully different logical strength. The foundation packet gives examples of possible ingredients but does not require them.

For each signature/family, freeze:

1. signature ID and name;
2. primitive sorts;
3. primitive relations/operations;
4. scalar/codomain sorts, if any;
5. exact axioms;
6. what makes the model `plane-like` in this task;
7. model examples;
8. nonmodels / degeneracies;
9. automorphism/equivalence notion;
10. definable derived structure;
11. structures explicitly absent;
12. whether finite models exist;
13. whether refinement/coarsening is meaningful;
14. exact dependency graph.

At least one serious signature must be weak enough that a scalar pi-role may plausibly be **not well-typed**.

At least one serious signature should be finite/discrete or admit finite approximants if mathematically coherent.

Do not rank signatures by closeness to classical geometry.

Freeze:

`R052_FORMAL_PLANE_SIGNATURE_FAMILY.json`

and return its SHA-256 before proceeding to Stage B.

## 3. Stage B — Typability and no-go audit

For each frozen signature, determine which kinds of pi-role statements are even expressible.

The required logical order is:

1. role language well-typed?
2. role object exists?
3. role invariant/equivariant under the signature's equivalences?
4. role unique?
5. if nonunique, classify the ambiguity when possible.

Use theorem-level arguments where possible, including model-theoretic/automorphism/choice/scaling/codomain obstructions.

Examples of valuable results:

- no scalar codomain exists, so a scalar role is ill-typed;
- a role depends on an unmarked basepoint/orientation and therefore is not invariant;
- affine or similarity freedom leaves a family of inequivalent role values;
- finite symmetry forces every candidate invariant of a given type to be trivial;
- a role exists only after an additional quotient/readout layer is added;
- two models are elementarily/structurally indistinguishable in the weaker language but assign different candidate role values under an expansion.

Do not add structure merely to rescue a failed role. Record the missing structure as a typed debt/result.

Return:

`R052_TYPABILITY_LEDGER.json`

`R052_NO_GO_AND_UNDERDETERMINATION_LEDGER.json`

## 4. Stage C — Independent pi-role generation and freeze

Only after Stage A signatures are frozen, generate **3–8 serious internally defined pi-role constructions** across the signature family.

A role may be scalar-valued, group-valued, quotient-valued, limit-derived or otherwise typed. It need not initially live in the real numbers.

Possible inspirations include rotation-like, winding-like, boundary/valuation-like, refinement-limit, recurrence/group-action, turning/curvature, isoperimetric or spectral roles, but these are examples only.

Every role must freeze:

1. role ID;
2. signature dependency;
3. codomain/type;
4. exact construction;
5. exact role predicate;
6. dependency graph;
7. native/operational/readout/limit-derived stratum;
8. invariance/equivariance theorem or failure;
9. existence theorem or failure;
10. uniqueness theorem or counterexample;
11. parameter/choice dependence;
12. known degeneracies;
13. finite-computability status;
14. reason it is not merely a renamed classical formula.

No role may be selected or repaired because it resembles a known decimal value.

Freeze:

`R052_PI_ROLE_REGISTRY.json`

and return its SHA-256 before Stage D.

## 5. Stage D — Multiplicity and coherence attack

Actively try to separate independently defined roles.

For each meaningful pair or family of roles, attempt both directions:

- construct a model satisfying the shared weaker signature where the roles differ or one is undefined;
- identify additional axioms under which equality/coherence can be proved.

Do **not** assume:

`pi_rotation = pi_winding = pi_boundary = pi_measure = pi_spectral = ...`.

Build a typed axiom/dependency lattice recording:

- which equality uses which axioms;
- whether each axiom appears necessary, sufficient, or only currently used;
- deletion witnesses/countermodels where an axiom is removed;
- whether equality is exact, quotient-level, or only asymptotic under refinement.

A major theorem target is a minimal or irredundant package `A*` for which at least two independently frozen pi-roles are forced to coincide.

A major negative target is a theorem that no universal role equality follows from a broad weak plane class.

Return:

`R052_ROLE_MULTIPLICITY_MATRIX.json`

`R052_COHERENCE_AXIOM_LATTICE.json`

`R052_MODEL_COUNTEREXAMPLES.json`

## 6. Stage E — Finite/refinement program

For every role/signature where a finite/refinement formulation is natural, build exact finite models or refinement towers without selecting them against classical pi.

Possible form:

`P_0 -> P_1 -> P_2 -> ...`

with internally defined role objects `p_n^(i)`.

Study:

- exact recursion/update law;
- invariance under refinement choices;
- convergence/stabilization in an exactly defined topology/order/algebraic sense;
- dependence on refinement path;
- equality or separation of role limits;
- finite counterexamples to naive coherence;
- rate statements only when theoremically justified.

If computation is used, separate:

- exact theorem;
- bounded exhaustive verification;
- numerical exploration/conjecture.

Do not compare sequences to decimal digits of classical pi.

Return:

`R052_FINITE_REFINEMENT_PROGRAM.json`

`R052_EXACT_CHECK_RESULTS.json`

plus checker/tests for machine-checkable finite claims.

## 7. Stage F — Sealed classical identification

This stage may open **only after**:

- Stage-A signature-family hash is frozen;
- Stage-C role-registry hash is frozen;
- theorem/counterexample statements from Stages B–E are frozen.

At that point, and only then, classical Euclidean plane mathematics may be used as a **comparison model**.

Allowed:

- interpret a frozen formal signature in the classical Euclidean plane;
- prove symbolically that a frozen role maps to the standard mathematical constant `π` under that interpretation;
- prove two frozen roles coincide in the Euclidean model;
- identify exactly which additional classical assumptions are doing the work.

Still forbidden:

- decimal/numerical pi as a loss or selection signal;
- changing a role definition after identification;
- adding a new axiom because it makes a number closer to classical pi;
- claiming that successful Euclidean interpretation makes the classical definition native.

If identification fails, preserve the failure. Any repair is `NEW_GENERATION_FOR_LATER_TASK`.

Return:

`R052_CLASSICAL_IDENTIFICATION_SEAL.json`

## 8. Required adversarial attacks

At minimum attack:

- `CIRCLE_DEFINITION_SMUGGLED_INTO_STARTING_SIGNATURE`
- `CENTER_OR_RADIUS_SMUGGLED_AS_NATIVE`
- `EQUIDISTANCE_SMUGGLED_AS_NATIVE`
- `RADIAN_OR_2PI_PER_TURN_SMUGGLED_AS_NATIVE`
- `CLASSICAL_PI_NUMERIC_SELECTION`
- `EUCLIDEAN_MODEL_USED_BEFORE_ROLE_FREEZE`
- `ROLE_DEFINED_BY_OUTPUT_COPYING`
- `UNMARKED_CHOICE_PROMOTED_TO_INVARIANT`
- `SCALAR_CODOMAIN_ASSUMED_WITHOUT_TYPING`
- `MULTIPLE_ROLES_ASSUMED_EQUAL`
- `COUNTERMODEL_REPAIRED_AWAY`
- `FINITE_NUMERIC_CONVERGENCE_PRESENTED_AS_THEOREM`
- `REFINEMENT_CHOSEN_AFTER_SEEING_CLASSICAL_MATCH`
- `CLASSICAL_IDENTIFICATION_BACKPROPAGATED_INTO_FOUNDATION`
- `ENGINEERING_TARGET_LEAKAGE`

## 9. No winner requirement

This task does not need one winning definition of formal pi.

Valid return classes include:

- `PI_NOT_WELL_TYPED_ON_WEAK_PLANES`;
- `MULTIPLE_INEQUIVALENT_PI_ROLES_FROZEN`;
- `COHERENCE_AXIOMS_FOUND`;
- `COHERENCE_NOT_FORCED_UNDER_CURRENT_SIGNATURES`;
- `FINITE_REFINEMENT_ROLE_LIMIT_FOUND`;
- `CLASSICAL_IDENTIFICATION_PROVED_AFTER_FREEZE`;
- combinations of the above.

Do not collapse the project to a single role unless strict theorem-level uniqueness/coherence has actually been proved in a declared signature.

## 10. Required artifacts

Return at least:

- `R052_REPORT.md`
- `R052_FORMAL_PLANE_SIGNATURE_FAMILY.json`
- `R052_TYPABILITY_LEDGER.json`
- `R052_NO_GO_AND_UNDERDETERMINATION_LEDGER.json`
- `R052_PI_ROLE_REGISTRY.json`
- `R052_ROLE_MULTIPLICITY_MATRIX.json`
- `R052_COHERENCE_AXIOM_LATTICE.json`
- `R052_MODEL_COUNTEREXAMPLES.json`
- `R052_FINITE_REFINEMENT_PROGRAM.json`
- `R052_THEOREM_COUNTEREXAMPLE_LEDGER.json`
- `R052_CLASSICAL_IDENTIFICATION_SEAL.json`
- `R052_CONTAMINATION_AUDIT.json`
- `R052_ADVERSARIAL_TEST_RESULTS.json`
- exact checker/tests for finite machine-checkable claims.

Freeze and report:

- `R052_SIGNATURE_FAMILY_SHA256`
- `R052_PI_ROLE_REGISTRY_SHA256`
- final artifact manifest/hash.

## 11. Research posture

This is a pure mathematics exploration task.

- No startup theorem/tool preselection.
- No automatic early winner selection.
- Preserve strange but well-typed routes.
- Preserve productive failures.
- Counterexamples are first-class outputs.
- Prior literature may be consulted after the internal signature/role definitions are frozen for attribution and theorem comparison; do not rewrite the frozen generation to imitate prior art.

Module estimate before task:

- formal-plane pi typability: `0% -> 35%` target;
- pi-role multiplicity/coherence: `0% -> 25%` target;
- finite/refinement formalization: `0% -> 20%` target;
- classical identification: optional and downstream only.

Advancement vector:

`formal-typing +35 / coherence +25 / finite-refinement +20 / engineering-calibration +0`.

End state remains `NOT_CANONICAL` unless a later Driver separately promotes a result.
