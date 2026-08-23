<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-IE-WEIGHTED-INCIDENCE-ENERGY-DIRICHLET-CALCULUS",
  "title": "Tool Discovery A — Weighted Incidence Energy / Dirichlet Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "MEDIUM_HIGH",
  "frontier": "ENTERPRISE_WEIGHTED_INCIDENCE_ENERGY_TOOL_CLASSIFIED",
  "next_action": "Classify whether explicitly weighted finite incidence/flow data supports a reusable quadratic-energy/Dirichlet/minimum-energy calculus distinct from T3 and from the sibling Laplacian/chip-firing candidate; otherwise freeze the strongest extension/composition/specialization/no-go verdict.",
  "dependencies": [
    "enterprise_toolbox_registry.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "research_method_inventory.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "tool_invocation_policy.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5"
  ],
  "source_refs": [
    "src/enterprise_math/collapse_incidence.py@7af320f5a0c0bde90ba227f0eded044786e84060",
    "enterprise_toolbox_registry.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "research_method_inventory.json@main:bd10bc351dbe7c90b47a3ffba3ef7796479170f5",
    "task:RS-TD-LP-DISCRETE-LAPLACIAN-CHIP-FIRING-POTENTIAL-CALCULUS"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": [
    "tool-discovery",
    "A",
    "incidence-energy",
    "dirichlet-form",
    "quadratic-form",
    "flow",
    "effective-resistance",
    "weighted-incidence"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDIE",
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

# Tool Discovery A — Weighted Incidence Energy / Dirichlet Calculus

Task-ID: `RS-TD-IE-WEIGHTED-INCIDENCE-ENERGY-DIRICHLET-CALCULUS`

Intended owner branch:

`research/tool-weighted-incidence-energy-dirichlet`

## 0. Driver capability-gap classification

This task begins from a deliberately skeptical position.

Current Enterprise source already has exact incidence-count machinery. In particular `collapse_incidence.py` constructs a finite 0/1 incidence matrix, Gram overlap counts, and higher collision spectra, and explicitly states that those counts are **not** identified with force, energy, probability, or thermodynamic entropy.

Therefore:

`BARE_INCIDENCE != ENERGY`.

Any positive energy calculus must consume extra declared data such as positive edge weights, conductances/resistances, an inner product, or another exact quadratic-form semantics.

There is also strong possible overlap with the sibling A+ task

`RS-TD-LP-DISCRETE-LAPLACIAN-CHIP-FIRING-POTENTIAL-CALCULUS`.

A separate global energy family is **not presumed**. The correct terminal result may be:

- an extension/subtool of the Laplacian candidate;
- a T3 + Laplacian composition;
- a narrow weighted-domain specialization;
- or an exact no-go for deriving energy from current incidence semantics.

Hard target:

`ENTERPRISE_WEIGHTED_INCIDENCE_ENERGY_TOOL_CLASSIFIED`.

## 1. Mother question

When an Enterprise problem explicitly supplies a finite incidence carrier plus positive or otherwise admissible quadratic weights, can the project obtain a reusable exact energy calculus?

Candidate capability:

> weighted incidence / boundary data -> quadratic Dirichlet or flow energy -> gradient/circulation decomposition -> minimum-energy solution and certificate -> optional effective pairing/resistance under precise graph hypotheses.

The task is about reusable finite quadratic-form reasoning, not about importing physical terminology into unweighted combinatorics.

## 2. Admissible semantic input

The researcher must state the minimum extra structure required.

Possible supported modes include:

### Graph-potential mode

- finite vertices `V`;
- finite edges `E` with arbitrary auxiliary orientation;
- positive conductance weights `c_e>0`, or positive resistance weights with explicit reciprocal convention;
- a scalar potential `u:V->K` over an exact ordered field/ring appropriate to the claim.

### Flow mode

- the same finite incidence data;
- an edge flow `j:E->K`;
- divergence/source vector `b`;
- positive resistance/conductance quadratic weights.

### General weighted-chain mode

Only if rigorously justified:

- a finite boundary/coboundary operator;
- an explicitly declared positive-definite or positive-semidefinite inner product on the relevant chain/cochain spaces.

Bare 0/1 incidence, overlap multiplicity, or path count is insufficient.

## 3. Candidate API to classify

A positive tool may expose a narrower API, but should classify operations of approximately this strength:

- `VALIDATE_WEIGHTED_INCIDENCE`;
- `BOUNDARY` / `COBOUNDARY`;
- `WEIGHT_MATRIX` or exact weight operator;
- `DIRICHLET_ENERGY(u)`;
- `FLOW_ENERGY(j)`;
- `LAPLACIAN_FROM_ENERGY` — when the quadratic form induces the appropriate operator;
- `GRADIENT_FLOW`;
- `CIRCULATION_SPACE`;
- `ORTHOGONAL_DECOMPOSE` — only when an inner-product semantics makes this meaningful;
- `DIRICHLET_MINIMIZER` — fixed-boundary minimum-energy potential;
- `THOMSON_MINIMIZER` — fixed-divergence minimum-energy flow, when supported;
- `MIN_ENERGY_CERT` — exact Euler-Lagrange/orthogonality or algebraic certificate;
- `EFFECTIVE_RESISTANCE` or `EFFECTIVE_PAIRING` — only under the graph assumptions needed for the theorem;
- `KRON_REDUCE` / Schur complement — only if exact positivity and boundary semantics are proved;
- `OBSTRUCTION` — nonpositive weights, singular unsupported form, missing boundary data, or semantic non-applicability.

A function that merely squares and sums arbitrary incidence entries is `RESULT_NOT_TOOL`.

## 4. Structural laws required

### 4.1 Orientation invariance

Show that physically/semantically meaningful energy outputs are invariant under changing auxiliary edge orientations, with flows or incidence signs transformed consistently.

### 4.2 Positivity / semidefiniteness

State exactly which hypotheses imply

`E(x) >= 0`

and characterize the zero-energy kernel at the supported level.

For a connected weighted graph with positive conductances, constants may form the potential kernel; for disconnected carriers, classify components separately.

Do not generalize this to arbitrary signed or nonsymmetric weights.

### 4.3 Polarization / bilinear form

If a quadratic energy induces a bilinear pairing, state the exact coefficient assumptions and polarization identity.

### 4.4 Dirichlet principle

Classify the exact finite minimization theorem for potentials with fixed boundary values.

Return uniqueness conditions and a compact certificate, not only a search result.

### 4.5 Thomson / flow principle

When flow semantics are supported, classify minimum-energy flow under a fixed divergence/source constraint and its relation to gradient potentials.

### 4.6 Gradient-circulation orthogonality

If the input supports a finite Hodge-like decomposition, prove the exact orthogonality and direct-sum statements.

Do not use the word `Hodge` to import manifold/smooth structure not present in the finite complex.

### 4.7 Reduction law

If Schur/Kron reduction is included, prove which boundary response/energy quantity is preserved and under what positivity/invertibility assumptions.

## 5. Mandatory dedup / ownership audit

### Sibling Laplacian/chip-firing candidate

This is the most important comparison.

If the Laplacian candidate already supplies the quadratic form, potential solver, and minimum-energy certificates with the same semantic input, then this task must classify as:

`SUBTOOL_OR_EXTENSION_OF_LAPLACIAN`

rather than creating another global family.

Conversely, if chip-firing/stabilization and weighted Dirichlet minimization require substantially different input/output contracts, state the precise boundary.

The two tasks may run in parallel; neither task's positive result is a premise of the other.

### T3 — Typed Incidence Circuit

T3 owns cycle/cut/path-defect certificates on finite incidence skeletons.

A weighted energy tool may use T3 circulation/cut structure, but the quadratic minimum-energy problem requires additional weight semantics.

If all new work is only a scalar weighting of T3 circuits with no new variational law or certificate, classify as a T3 extension/specialization.

### T9 — Holonomy / Gluing

Cycle energy and loop holonomy are different typed objects. Nonzero energy does not imply nonzero holonomy, and vice versa.

### T4/T8 — fibers and relation spectra

Existing incidence overlap spectra count shared targets. They do not become a quadratic energy without a declared inner product/weight interpretation.

## 6. Two-domain reuse gate

If a separate or broadly reusable energy tool is claimed, demonstrate it on at least two genuinely different families.

### Application A — weighted path/flow skeleton

Use a finite weighted incidence graph with explicit boundary/source data.

Demonstrate at least one of:

- minimum-energy potential;
- minimum-energy flow;
- gradient/circulation decomposition;
- exact effective resistance;
- boundary-preserving reduction.

### Application B — distinct weighted Enterprise defect/relation system

Use another independently weighted finite object, for example:

- a precision defect transport with a declared quadratic penalty;
- a relation/collapse carrier with externally declared reliability/capacity weights;
- another finite chain/cochain system whose inner product has independent semantic justification.

The second application must not obtain its weights merely by copying graph degree or geometric coordinates from implementation.

If no second natural weighted Enterprise family exists, downgrade to `DOMAIN_SPECIALIZATION_ONLY` rather than inventing one.

## 7. Required negative boundary

Produce exact counterexamples or non-applicability statements for at least:

- unweighted bare incidence;
- negative edge weights causing loss of positivity;
- zero weights causing additional kernel/singularity;
- nonsymmetric interaction incorrectly treated as an undirected Dirichlet form;
- disconnected carriers and kernel multiplicity;
- an overlap Gram count incorrectly called energy;
- effective resistance requested without an electrical-network-like weight semantics;
- a minimum-energy solution incorrectly promoted to a native geometric shortest path;
- a finite quadratic form incorrectly promoted to thermodynamic or physical energy.

## 8. Classical prior-art discipline

Graph Dirichlet forms, weighted Laplacians, electrical networks, Thomson/Dirichlet principles, effective resistance, finite Hodge decomposition, Schur complements, and Kron reduction are classical mathematics.

The return must separate:

1. classical theorem content;
2. current Enterprise T3/T4/T8/T9 overlap;
3. overlap with the sibling Laplacian/chip-firing candidate;
4. new Enterprise semantic interface/composition if any;
5. theorem novelty, if any;
6. packaging or domain-specialization-only value.

`DECLARED_WEIGHTED_ENERGY_INTERFACE != NATIVE_ENERGY_PRIMITIVE`.

## 9. Deterministic checker

Required executable:

`scripts/tool_discovery_weighted_incidence_energy_dirichlet_check.py`

Minimum exact regression:

- path/tree/cycle graphs with positive integer/rational weights;
- orientation flips;
- disconnected graph kernel examples;
- zero and negative weight counterexamples;
- Dirichlet minimization versus exhaustive small rational/integer candidates where appropriate;
- Thomson minimum-flow checks;
- gradient/circulation orthogonality on small examples;
- effective resistance identities on simple networks if claimed;
- Schur/Kron reduction preservation if claimed;
- explicit comparison with bare incidence overlap counts;
- two Enterprise applications if a global tool is claimed;
- mismatch count `0` for every exact theorem/check pair.

Use exact rational/integer linear algebra for theorem-level checks when possible.

## 10. Tool acceptance gate

A separate positive global tool requires:

1. explicit extra weight/inner-product semantics;
2. reusable quadratic-energy/minimization API;
3. a nontrivial exact variational, orthogonality, reduction, or certificate law;
4. hard negative boundaries;
5. two-domain reuse;
6. real compression or minimization certificate beyond scalar bookkeeping;
7. a convincing reason not to place the capability inside the sibling Laplacian tool or T3.

Allowed terminal classifications:

- `NEW_GLOBAL_TOOL_FAMILY`;
- `NEW_ENTERPRISE_WEIGHTED_ENERGY_INTERFACE`;
- `SUBTOOL_OR_EXTENSION_OF_LAPLACIAN`;
- `EXTEND_T3_WITH_WEIGHTED_VARIATIONAL_LAYER`;
- `COMPOSE_T3_WITH_LAPLACIAN`;
- `DOMAIN_SPECIALIZATION_ONLY`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`;
- `EXACT_NO_GO_FROM_BARE_INCIDENCE`.

The hard target closes with the strongest justified classification; a downgrade is a valid success.

## 11. Required artifacts

Return:

1. `research_notes/TOOL_DISCOVERY_WEIGHTED_INCIDENCE_ENERGY_DIRICHLET_RESULT_20260823.md`
2. `scripts/tool_discovery_weighted_incidence_energy_dirichlet_check.py`
3. optional reusable source module only if the acceptance gate is met.

The report must include:

- Researcher-ID;
- exact source baseline;
- weight/inner-product semantic contract;
- dedup/ownership table;
- theorem/status ledger;
- comparison with the Laplacian candidate;
- two-domain reuse evidence or explicit reason for specialization downgrade;
- hard counterexamples;
- checker summary;
- strongest final classification.

## 12. Stop condition

Freeze the terminal classification and required artifacts, then stop this task.

Do not create a separate energy family merely to preserve the historical candidate name.

---

Driver issue note:

`A HISTORICAL TOOL CANDIDATE; BARE INCIDENCE DOES NOT DEFINE ENERGY, AND SUBSUMPTION BY THE LAPLACIAN TOOL IS A FIRST-CLASS TERMINAL OUTCOME.`
