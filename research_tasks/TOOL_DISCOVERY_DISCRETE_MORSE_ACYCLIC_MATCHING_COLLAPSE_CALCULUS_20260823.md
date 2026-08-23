<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TD-DM-DISCRETE-MORSE-ACYCLIC-MATCHING-COLLAPSE-CALCULUS",
  "title": "Tool Discovery A+ — Discrete Morse / Acyclic Matching Collapse Calculus",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "ENTERPRISE_DISCRETE_MORSE_COLLAPSE_TOOL_CLASSIFIED",
  "next_action": "Determine whether finite graded Enterprise incidence objects support a reusable acyclic-matching/Morse-reduction calculus that preserves chain-level invariants and yields real compression beyond T3/T6; otherwise classify the candidate as an existing-tool composition, domain specialization, or no-go.",
  "dependencies": [
    "enterprise_toolbox_registry.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "research_method_inventory.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "tool_invocation_policy.json@main:f83f349d1521185ac3e99db574959d0b797cacf2"
  ],
  "source_refs": [
    "enterprise_toolbox_registry.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "research_method_inventory.json@main:f83f349d1521185ac3e99db574959d0b797cacf2",
    "src/enterprise_math/alexander_descent.py@e48d51a062faa94dfdb6b9dce64ea7d76c7ea95e",
    "docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md@main:f83f349d1521185ac3e99db574959d0b797cacf2"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": [
    "tool-discovery",
    "A+",
    "discrete-morse",
    "acyclic-matching",
    "chain-complex",
    "collapse",
    "topology",
    "finite"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDDM",
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

# Tool Discovery A+ — Discrete Morse / Acyclic Matching Collapse Calculus

Task-ID: `RS-TD-DM-DISCRETE-MORSE-ACYCLIC-MATCHING-COLLAPSE-CALCULUS`

Intended owner branch:

`research/tool-discrete-morse-acyclic-matching-collapse`

## 0. Driver classification and capability gap

This is an A+ historical-tool discovery task.

Current coverage audit at the frozen source baseline found:

- no registered T0–T9 tool family with an explicit Discrete Morse, acyclic Hasse matching, critical-cell, or chain-homotopy reduction interface;
- no curated method-inventory entry for Morse matching/cancellation;
- repository search for `Morse` and for the combined `homology chain complex boundary matching acyclic critical cells` vocabulary produced no direct current-source owner;
- `src/enterprise_math/alexander_descent.py` uses classical combinatorial Alexander duality on a specialized threshold complex, but does not expose a general Morse-reduction engine.

This is only a capability-gap candidate. The researcher must still compare against T2 finite certificates, T3 typed incidence circuits, T6 operation-safe quotient, T7 finite symmetry, T9 gluing/holonomy, `alexander_descent.py`, and any current chain/incidence helper discovered during execution.

Do not claim that classical Forman discrete Morse theory or algebraic Morse cancellation is new mathematics.

## 1. Mother question

Can Enterprise Math obtain a reusable finite collapse tool with this capability?

> Given a finite graded incidence object or chain complex, select/certify an acyclic matching of cancellable incidence pairs, reduce to critical generators, and preserve the exact chain-homotopy/homology information required by the caller while returning lifting/projection certificates.

Hard target:

`ENTERPRISE_DISCRETE_MORSE_COLLAPSE_TOOL_CLASSIFIED`.

The desired output is a reusable reduction/certificate calculus, not a one-off topological theorem.

## 2. Admissible input layer

A positive tool must declare exactly which of the following it accepts.

Preferred minimal input:

- a finite graded set or poset `P`;
- a rank/degree map;
- a cover/incidence relation between adjacent grades;
- incidence coefficients in a declared coefficient ring when chain-level cancellation is requested.

For chain-complex mode require an explicit finite complex

`... -> C_{k+1} --d_{k+1}-> C_k --d_k-> C_{k-1} -> ...`

with exact verification of `d_k d_{k+1}=0`.

For integer coefficients, elementary cancellation of a matched pair requires a unit incidence coefficient (`+1` or `-1`) unless a separate coefficient-localization semantics is explicitly declared.

Do not infer cells, faces, topology, dimension, metric, or homology merely from an arbitrary state-transition graph.

## 3. Candidate API to classify

A positive tool should expose a reusable interface of approximately this strength:

- `VALIDATE_GRADED_INCIDENCE`;
- `VALIDATE_CHAIN_COMPLEX`;
- `MATCH` — propose or accept adjacent-grade matched pairs;
- `ACYCLIC` — exact certificate that the induced directed matching has no closed gradient path;
- `CANCELLABLE_PAIR` — coefficient/domain legality check;
- `CANCEL` — one exact elementary algebraic/topological cancellation;
- `MORSE_REDUCE` — iterate a legal acyclic matching to a reduced complex/object;
- `CRITICAL_GENERATORS` — unmatched cells/generators;
- `MORSE_BOUNDARY` — exact reduced boundary operator when chain data is present;
- `PROJECT` / `LIFT` — maps or witnesses relating original and reduced complexes;
- `HOMOLOGY_CERT` — exact equality/isomorphism certificate at the supported coefficient layer;
- `OBSTRUCTION` — witness of cyclic matching, nonunit incidence, malformed complex, or semantic non-applicability.

An algorithm that simply deletes arbitrary matched nodes from a graph is not Discrete Morse theory and must fail the gate.

## 4. Structural laws required

### 4.1 Acyclic matching condition

State an exact finite criterion for admissible matching.

If using Forman V-path language or an algebraic directed dependency graph, make the equivalence precise.

Return a cycle witness when the condition fails.

### 4.2 Elementary cancellation theorem

Prove/cite at exact strength that a legal matched pair may be cancelled while preserving the declared chain-homotopy/homology information.

For integer coefficients distinguish unit cancellation from field-coefficient cancellation.

### 4.3 Composition

Show how successive elementary cancellations compose and how projection/lift maps or chain homotopies are accumulated.

### 4.4 Critical-generator bound

Classify what critical-cell counts actually certify.

When a coefficient field is fixed, compare critical counts with Betti-number lower bounds if appropriate.

Do not claim optimality of a matching unless it is proved.

### 4.5 Presentation and symmetry

Classify invariance under relabeling/isomorphism of the finite graded incidence object.

A greedy matching order may be presentation-dependent; if so, preserve that fact rather than calling the output canonical.

### 4.6 Termination and complexity

Finite elementary cancellation sequences terminate once each step strictly reduces generator count, but finding an optimal/minimum-critical matching may be computationally hard.

Separate:

- correctness of a supplied acyclic matching;
- deterministic greedy construction;
- exact optimal search on small objects;
- any unproved complexity claim.

## 5. Required separation from current tools

### T2 — finite certificates

T2 extracts bounded incompatibility certificates. Morse cancellation instead aims to reduce a graded incidence/chain object while preserving topological/algebraic invariants. If the candidate only certifies local compatibility, route it to T2.

### T3 — typed incidence circuits

T3 owns cycle/cut/path-defect structure on finite incidence skeletons. A Morse tool may use T3-like cycle detection internally, but its new capability must be acyclic adjacent-grade matching plus invariant-preserving cancellation.

If no chain/topological information survives beyond T3, classify as composition/extension rather than a new family.

### T6 — operation-safe quotient

T6 builds quotients preserving declared future observations/operations. Morse reduction is not automatically an operation-safe semantic quotient.

A homology-equivalent reduced complex may still lose distinctions required by an Enterprise operation language. Keep these notions separate.

### T7 — finite symmetry

T7 may reduce matching search by orbits or diagnose absence of a canonical matching. It does not itself perform Morse cancellation.

### T9 — holonomy/gluing

T9 detects loop/gluing obstruction. A Morse reduction may compress a complex on which T9 is later evaluated, but homology and holonomy are not interchangeable.

## 6. Two-domain reuse gate

A positive global tool must demonstrate reuse on at least two genuinely different Enterprise families.

### Application A — threshold/support complex

Use a finite threshold or support complex, with `src/enterprise_math/alexander_descent.py` as one comparison point if appropriate.

Show that Morse reduction yields a real benefit such as:

- fewer generators/faces before an exact invariant computation;
- a compact critical-cell certificate;
- a decomposition making a duality/tail calculation structurally clearer.

Do not merely reproduce the existing Alexander-dual threshold formula.

### Application B — state/precision/relation complex

Construct a separately motivated finite graded incidence object from another Enterprise family, for example:

- a precision/refinement state complex;
- a relation/collapse state complex;
- a finite gluing/transition cell object whose grading is independently meaningful.

Demonstrate exact compression or obstruction while preserving the declared chain-level invariant.

The second application must not be a renamed threshold complex.

## 7. Hard negative boundary

At minimum produce exact counterexamples or non-applicability statements for:

- arbitrary directed state graph without a graded face/incidence semantics;
- matched pair with nonunit incidence over `Z`;
- matching containing a closed gradient path;
- reduction that preserves homology but not a separately declared operation/observation semantics;
- presentation-dependent greedy matching incorrectly advertised as canonical;
- a complex with torsion where field-only checks miss integral information;
- implementation geometry treated as native topology without a declared incidence meaning.

No claim of continuum topology, smooth Morse functions, manifold structure, or native geometric dimension follows from a finite Morse reduction.

## 8. Classical prior-art / novelty discipline

The researcher must distinguish at least:

- Forman discrete Morse theory;
- algebraic/chain-complex Morse cancellation;
- standard acyclic matching theory;
- classical homology computation;
- existing Enterprise incidence/quotient/certificate machinery;
- any new Enterprise interface or composition.

A positive result may be valuable even if every mathematical theorem is classical.

Accepted novelty labels may include:

- `NEW_ENTERPRISE_TOOL_INTERFACE`;
- `HIGH_VALUE_TOOL_COMPOSITION`;
- `EXTEND_T3`;
- `EXTEND_T6`;
- `DOMAIN_SPECIALIZATION_ONLY`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`.

Do not inflate packaging novelty into theorem novelty.

## 9. Deterministic checker

Required executable:

`scripts/tool_discovery_discrete_morse_acyclic_matching_check.py`

Minimum exact regression:

- tiny simplicial/graded complexes with known homology;
- explicit legal acyclic matchings;
- explicit cyclic matching rejection;
- unit versus nonunit integer incidence examples;
- exact comparison of original/reduced boundary data;
- exact homology comparison at every coefficient layer claimed by the theorem;
- projection/lift or chain-homotopy identity checks on small examples;
- threshold/support application;
- second distinct Enterprise application;
- relabeling invariance checks for theorem-level outputs;
- mismatch count `0`.

If integral homology is claimed, use exact integer arithmetic and a verifiable exact normal-form method; floating rank is not sufficient.

## 10. Tool acceptance gate

A positive result must provide:

1. explicit reusable input/output interface;
2. exact acyclic-matching/cancellation law or certificate;
3. exact failure boundary;
4. reuse on two genuinely different Enterprise problem families;
5. real compression, invariant preservation, certificate, decomposition, or search reduction;
6. exact comparison with T2/T3/T6/T7/T9 and current executable source.

The hard target is classification. It closes with the strongest justified outcome even if that outcome is `COMPOSE_EXISTING_TOOLS` or `EXACT_NO_GO`.

Allowed terminal verdicts include:

- `NEW_GLOBAL_TOOL_FAMILY`;
- `NEW_ENTERPRISE_TOOL_INTERFACE`;
- `EXTEND_T3`;
- `EXTEND_T6`;
- `HIGH_VALUE_TOOL_COMPOSITION`;
- `DOMAIN_SPECIALIZATION_ONLY`;
- `DUPLICATE_ALIAS`;
- `RESULT_NOT_TOOL`;
- `EXACT_NO_GO`.

## 11. Required artifacts

Return:

1. `research_notes/TOOL_DISCOVERY_DISCRETE_MORSE_ACYCLIC_MATCHING_RESULT_20260823.md`
2. `scripts/tool_discovery_discrete_morse_acyclic_matching_check.py`
3. optional reusable source module only if the tool gate is actually met.

The report must include:

- Researcher-ID;
- exact source baseline;
- input semantic contract;
- tool-coverage/dedup table;
- theorem/status ledger;
- critical-cell and reduction statistics for the two applications;
- hard boundaries/counterexamples;
- checker summary;
- strongest final classification.

## 12. Stop condition

Freeze the terminal classification and required artifacts, then stop.

A positive classification does not by itself authorize a follow-on stage.

---

Driver issue note:

`A+ HISTORICAL TOOL CANDIDATE; SEEK CHAIN-HOMOTOPY-PRESERVING FINITE REDUCTION, NOT GENERIC NODE DELETION.`
