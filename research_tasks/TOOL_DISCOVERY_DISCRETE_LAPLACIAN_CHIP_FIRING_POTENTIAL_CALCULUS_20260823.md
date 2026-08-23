<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-LP-DISCRETE-LAPLACIAN-CHIP-FIRING-POTENTIAL-CALCULUS",
  "title": "Tool Discovery A+ — Discrete Laplacian / Chip-Firing / Potential Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "ENTERPRISE_DISCRETE_LAPLACIAN_CHIP_FIRING_POTENTIAL_TOOL_CLASSIFIED",
  "next_action": "Determine whether finite typed Enterprise incidence/transition data supports a genuinely reusable Laplacian/chip-firing/potential calculus beyond T3/T5/T6/T9; build the narrowest exact tool interface or prove that the candidate is only an existing-tool composition/alias.",
  "dependencies": [
    "enterprise_toolbox_registry.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "research_method_inventory.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "tool_invocation_policy.json@main:f83f349d1521185ac3e99db574959d0b797cacf2"
  ],
  "source_refs": [
    "enterprise_toolbox_registry.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "research_method_inventory.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "src/enterprise_math/adjoint_boundary_precision.py@a1e73b6d97f116cbb1127d1ba08a47a061318897",
    "docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md@main:f83f349d1521185ac3e99db574959d0b797cacf2"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": [
    "tool-discovery",
    "A+",
    "laplacian",
    "chip-firing",
    "sandpile",
    "potential",
    "incidence",
    "finite"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDLP",
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

# Tool Discovery A+ — Discrete Laplacian / Chip-Firing / Potential Calculus

Task-ID: `RS-TD-LP-DISCRETE-LAPLACIAN-CHIP-FIRING-POTENTIAL-CALCULUS`

Intended owner branch:

`research/tool-discrete-laplacian-chip-firing-potential`

## 0. Driver classification and capability gap

This is an A+ historical-tool discovery task.

Current coverage audit at the frozen source baseline found:

- no registered T0–T9 family whose declared interface is a discrete Laplacian, chip-firing/sandpile stabilization, or least-action potential calculus;
- no curated method-inventory entry named for Laplacian, chip firing, sandpile, odometer, or harmonic potential;
- repository searches for `laplacian`, `chip firing`, and `Morse` produced no direct current-source owner;
- `src/enterprise_math/adjoint_boundary_precision.py` is an order-adjoint threshold-pullback calculus, not a graph Laplacian or chip-firing system.

This is only a **capability-gap candidate**. The researcher must still compare against the closest current owners, especially T3 incidence circuits, T5 precision/refinement, T6 operation-safe quotient, T9 holonomy/gluing, and any current source discovered during execution.

Do not claim novelty merely because classical graph-Laplacian/chip-firing mathematics has not yet been packaged in Enterprise Math.

## 1. Mother question

Can finite typed Enterprise incidence or transition data support a reusable exact calculus with the following genuinely new capability?

> Convert local vertex/transition imbalance into a finite potential/divergence object, perform local conservative redistribution, obtain a canonical stabilization when termination hypotheses hold, and return exact least-action/odometer or obstruction certificates.

The task is tool discovery, not a request for one more theorem.

Hard target:

`ENTERPRISE_DISCRETE_LAPLACIAN_CHIP_FIRING_POTENTIAL_TOOL_CLASSIFIED`.

## 2. Admissible mathematical input layer

Start from a finite explicitly declared combinatorial carrier such as:

`Gamma=(V,E,s,t,tau)`

with finite vertices, finite incidences/transitions, and optional type labels.

Allowed optional input, only when explicitly supplied:

- a sink or sink set;
- integer edge multiplicities or explicitly typed nonnegative edge weights;
- an integer chip/defect state `c:V->Z`;
- a boundary condition or declared source/sink vector.

Edge orientation may be used as an auxiliary presentation if the final object is proved independent of that orientation.

Do not silently infer adjacency, metric, conductance, Euclidean distance, smoothness, probability, continuum PDE structure, or spectral geometry when the input does not contain it.

## 3. Candidate API to classify

The researcher may rename/refine the API, but a positive tool should expose explicit operations of approximately this strength:

- `INCIDENCE` — typed incidence/boundary matrix or equivalent finite relation;
- `DIV` — exact divergence/imbalance of an integer edge flow;
- `LAPLACIAN` — finite combinatorial Laplacian on declared vertex potentials;
- `FIRE` — one legal local redistribution/toppling move;
- `STABILIZE` — terminal configuration under an explicit termination regime;
- `ODOMETER` — number/vector of firings giving the terminal state;
- `LEAST_ACTION_CERT` — exact minimality/uniqueness certificate for the odometer;
- `REDUCED_LAPLACIAN` — sink-reduced operator when a sink is part of the input;
- `EQUIVALENCE_CLASS` — chip-firing/cokernel class when semantically justified;
- `OBSTRUCTION` — finite witness when termination, uniqueness, or conservation hypotheses fail.

A result consisting only of `L=D-A` as a matrix identity is `RESULT_NOT_TOOL`.

## 4. Structural laws required for a positive result

At least the following must be classified exactly.

### 4.1 Presentation invariance

Show which outputs are independent of arbitrary edge orientation, vertex relabeling, and other declared presentation gauges.

### 4.2 Conservation / controlled dissipation

For a legal firing move, state exactly what total integer quantity is conserved and what may be lost into a declared sink.

### 4.3 Commutativity / abelian stabilization

Under a precise finite termination hypothesis, determine whether legal firing order changes the stabilized state or odometer.

If the standard abelian result is used, prove or cite it at the exact declared strength and distinguish classical theorem content from Enterprise interface work.

### 4.4 Termination

Give necessary/sufficient or at least sharp sufficient hypotheses for termination.

Examples to distinguish include:

- finite connected graph with an accessible sink;
- sinkless conservative graph;
- directed graph;
- weighted or signed variants.

Do not treat finite state size alone as a termination proof when firing counts are unbounded.

### 4.5 Least action / potential certificate

Determine whether stabilization has a least-action or superharmonic/odometer characterization that yields a compact exact certificate, not merely a replay log.

### 4.6 Algebraic invariant

Classify the exact role of the reduced Laplacian cokernel / critical group / sandpile group, if used.

Do not promote the group to native ontology; it is a derived tool object on an already declared finite incidence carrier.

## 5. Required separation from current tools

A positive new tool or extension must explain why the following are insufficient by themselves.

### T3 — Typed Incidence Circuit Calculus

T3 detects cycles, cuts, cocircuits, and path defects. It does not currently provide legal local redistribution, sink stabilization, least-action odometers, or sandpile equivalence classes.

If the proposed tool reduces entirely to T3 plus linear algebra, classify it as `COMPOSE_EXISTING_TOOLS` or `EXTEND_EXISTING_TOOL`.

### T5 — Integer Precision / Refinement

T5 already owns carry/borrow and finite detail transport. A chip-firing application to precision defects is not a new tool unless the shared local-conservation/stabilization layer is genuinely reusable outside precision.

### T6 — Operation-Safe Quotient

T6 preserves declared operation/observation semantics under quotienting. Chip-firing equivalence or stabilization must not be confused with operation-safe quotient construction.

### T9 — Holonomy / Cocycle / Gluing

T9 detects loop/gluing defects. A potential that trivializes a defect on a graph may compose with T9, but `nonzero holonomy` and `nonzero Laplacian/divergence` are not interchangeable invariants.

## 6. Two-domain reuse gate

A positive global tool must be exercised on at least two genuinely different Enterprise problem families.

Required minimum:

### Application A — incidence/path/provenance

Use a finite typed incidence or path skeleton to show one of:

- exact decomposition of a local imbalance into potential plus circulation information;
- compact certificate of conservative versus nonconservative flow;
- canonical redistribution normal form not already supplied by T3.

### Application B — precision/collapse/gluing defect redistribution

Use a distinct finite state family, for example a precision/carry defect field or another locally conserved defect system, to show:

- stabilization;
- odometer/least-action certificate;
- or an exact obstruction.

The second application may not be a trivial renaming of the first graph.

A third application is welcome but not required.

## 7. Required negative boundary

At minimum classify:

- no declared finite incidence/adjacency -> tool not applicable;
- sinkless stabilization may fail to terminate or may not select a unique terminal state;
- directed graphs need extra hypotheses and may lose undirected abelian properties;
- negative or arbitrary signed weights require separate semantics;
- potential values do not automatically define geometric distance or energy;
- a finite Laplacian does not imply continuum harmonic analysis, a PDE limit, spectral dimension, or Euclidean conductance;
- an implementation embedding is not a native metric.

Produce explicit smallest counterexamples for failed generalizations.

## 8. Classical prior-art / novelty discipline

The mathematical core of graph Laplacians, chip firing, abelian sandpiles, reduced Laplacians, critical groups, and least-action principles is classical.

The research return must separately classify:

1. classical theorem reused;
2. pre-existing Enterprise specialization, if any;
3. new Enterprise semantic interface or composition;
4. genuinely new theorem, if one appears;
5. no-new-tool / alias outcome.

`CLASSICAL_THEOREM_PACKAGED_FOR_ENTERPRISE != NEW_MATHEMATICS`.

A high-value tool-composition result is acceptable.

## 9. Deterministic checker

Required executable:

`scripts/tool_discovery_discrete_laplacian_chip_firing_potential_check.py`

Minimum exact regression:

- several connected undirected graphs with sink, including path, cycle-with-sink, tree, and a nontrivial multigraph;
- orientation-invariance checks;
- conservation / sink-loss checks;
- all legal firing orders for small configurations where exhaustive replay is finite;
- stabilization uniqueness;
- odometer least-action comparison;
- reduced-Laplacian/cokernel small examples;
- explicit sinkless nontermination or nonuniqueness counterexamples;
- cross-domain application regressions;
- mismatch count `0` for every theorem/check pair claimed as exact.

Finite enumeration is regression evidence, not the proof of the general theorem.

## 10. Tool acceptance gate

A positive result must provide:

1. explicit reusable input/output interface;
2. at least one nontrivial structural law or invariant/certificate;
3. an exact negative/failure boundary;
4. reuse on at least two genuinely different Enterprise problem families;
5. at least one application with real compression, canonical normal form, certificate, decomposition, or search reduction beyond restating a pointwise formula;
6. exact dedup classification against current Toolbox and current executable source.

Allowed final classifications include:

- `NEW_GLOBAL_TOOL_FAMILY`;
- `EXTEND_T3`;
- `EXTEND_T5`;
- `COMPOSE_EXISTING_TOOLS`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`;
- `EXACT_NO_GO`.

The hard target closes when the strongest justified classification is frozen, not only when a new family is discovered.

## 11. Required artifacts

Return:

1. `research_notes/TOOL_DISCOVERY_DISCRETE_LAPLACIAN_CHIP_FIRING_POTENTIAL_RESULT_20260823.md`
2. `scripts/tool_discovery_discrete_laplACIAN_CHIP_FIRING_POTENTIAL_check.py`
3. optional reusable source module only if the tool gate is actually met.

The report must include:

- Researcher-ID;
- exact source baseline;
- tool-coverage/dedup table;
- theorem/status ledger;
- two-domain reuse evidence;
- hard boundaries/counterexamples;
- checker summary;
- strongest final classification.

## 12. Stop condition

After freezing the classification and required artifacts, stop this task.

Do not automatically open a second stage merely because the first classification is positive.

---

Driver issue note:

`A+ HISTORICAL TOOL CANDIDATE; SEEK LOCAL-CONSERVATION/STABILIZATION CAPABILITY, NOT A RENAMED GRAPH-LAPLACIAN THEOREM.`
