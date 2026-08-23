<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HIGHDIM-PRIME-WALL-FILTER-ALGEBRA-EQUIVALENCE-AUDIT",
  "title": "High-Dimensional Prime Walls — Filter Algebra and Classical Equivalence Audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_CLASSICALLY_EQUIVALENT_OR_RESIDUALLY_NEW_CLASSIFIED",
  "next_action": "Independently prove, narrow, or refute H1-H8 in the frozen statement packet, then perform a source-backed classical-equivalence audit that separates exact combinatorics, theta/divisor-sum infrastructure, project-specific presentation, and any genuine residual content.",
  "dependencies": [
    "research_inputs/HIGHDIM_PRIME_WALL_FILTER_EQUIVALENCE_PACKET_20260823.md@0173b1ea489a4811d42b77b9e8d977d327c4d08e"
  ],
  "source_refs": [
    "research_inputs/HIGHDIM_PRIME_WALL_FILTER_EQUIVALENCE_PACKET_20260823.md@0173b1ea489a4811d42b77b9e8d977d327c4d08e"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "prime",
    "high-dimensional",
    "theta-series",
    "divisor-sums",
    "support-spectrum",
    "equivalence-audit"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "HDPWA",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
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

# High-Dimensional Prime Walls — Filter Algebra and Classical Equivalence Audit

Task-ID: `RS-HIGHDIM-PRIME-WALL-FILTER-ALGEBRA-EQUIVALENCE-AUDIT`

Intended owner branch:

`research/highdim-prime-wall-equivalence-audit`

Hard target:

`HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_CLASSICALLY_EQUIVALENT_OR_RESIDUALLY_NEW_CLASSIFIED`

## Context

A free 2D-19D experiment produced exact support-spectrum identities, a lambda-filter family, dimension convolution, four- and eight-dimensional primality walls, and higher-dimensional residual observations.

Several components visibly touch classical theta-series and divisor-sum theory. The current need is not another numerical sweep. It is an exact independent derivation followed by a disciplined equivalence audit that prevents classical formulas from being relabeled as new Enterprise mathematics while preserving any genuinely useful project-specific transform or decomposition.

## Parent-Chain Identity

Lineage is `REPLAY` from a frozen statement packet, not continuation of a completed taskbook.

The parent chain is:

`USER HIGH-DIMENSIONAL PRIME DIRECTION -> PRIME BATCH DRIVER -> INDEPENDENT EQUIVALENCE AUDITOR`.

No free-research worker identity or conclusion is inherited. Runtime Researcher-ID allocation is external.

## Locked Source Package

Use:

`research_inputs/HIGHDIM_PRIME_WALL_FILTER_EQUIVALENCE_PACKET_20260823.md@0173b1ea489a4811d42b77b9e8d977d327c4d08e`.

Before the internal proof checkpoint is frozen, do not read Draft PR #595, branch `research/free-highdim-prime-collapse-basins-20260823`, its scripts or notes, or the source GLOBAL_KNOWLEDGE event.

After that checkpoint, external primary mathematical sources and standard authoritative references may be used for the classical-equivalence audit. The source free-research proof remains withheld until the final independent return is frozen.

## Previous Outputs

No prior taskbook output closes H1-H8.

The finite zero-mismatch ranges and source checkpoint hashes in the packet are provenance signals only. They are not proof evidence and must not determine the derivation route.

## Input Artifact Provenance

The packet is a statement-only extraction from a free-research checkpoint whose Enterprise branch head and GLOBAL_KNOWLEDGE event are frozen in the packet.

It includes exact candidate formulas so that the task can test theorem strength, but it excludes source derivations, code, interpolation choices, and source interpretations.

## Exact Research Question

For each candidate H1-H8:

1. prove it at its exact natural scope, narrow it with necessary hypotheses, or refute it;
2. identify the shortest classical formula, generating-function identity, or representation theorem to which it is equivalent;
3. determine whether the Enterprise construction adds a new invariant, only a new presentation, or no additional mathematical capability;
4. state every prohibited inference, especially claims about primality algorithms, factoring complexity, native negative axes, or novel Sato-Tate phenomena.

The final report must assign one packet-approved classification label to every H-item and one aggregate verdict:

- `FULL_CLASSICAL_EQUIVALENCE_WITH_USEFUL_PROJECT_PRESENTATION`;
- `MIXED_CLASSICAL_AND_RESIDUAL_PROJECT_STRUCTURE`;
- `SCOPE_NARROWING_REQUIRED`;
- `MATERIAL_COUNTEREXAMPLE`;
- `OPEN_AFTER_EXACT_PARTIAL_CLASSIFICATION`.

The hard target is not met by proving only the prime-wall biconditionals. The filter algebra, dimension convolution, lambda=2 criterion, and twelve-dimensional boundary must also be classified.

## Scope Guard

### In scope

- exact coefficient/generating-function proofs for support decomposition and dimension convolution;
- derivation of the fixed-face survival identity;
- derivation of `Q4` and `Q8` as exact arithmetic functions;
- proof of the stated prime biconditionals and semiprime excess formula;
- precise formalization and proof audit of the lambda=2 uniqueness criterion;
- prime powers and general odd-composite formulas;
- theta-series, Jacobi square theorems, modular forms, Hecke eigenvalues, and Sato-Tate only as needed for exact equivalence classification;
- identification of any quotient/residual object not already exhausted by classical formulas.

### Out of scope

- numerical confirmation presented as proof;
- claiming a bit-complexity improvement from shell counts computed in time polynomial in the integer value;
- declaring signed-coordinate theta multiplicity to be a native Enterprise negative-axis structure;
- presenting the twelve-square Sato-Tate example as new;
- opening the source free-research derivation before freeze;
- expanding to higher dimensions merely to find another visual pattern.

Kill condition:

If an H-item reduces exactly to a classical identity, classify it as such even when the Enterprise coefficient combination was discovered independently. If a coefficient or hypothesis fails on an exact composite, preserve the smallest counterexample and narrow or refute the claim.

## Required Outputs

Produce:

1. Full report:
   `research_output/HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_20260823.md`
2. Reducer result:
   `research_output/reducer_results/HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_REDUCER_20260823.md`
3. Independent exact checker:
   `experiments/highdim_prime_wall_filter_equivalence_checker.py`
4. H1-H8 classification matrix:
   `research_output/HIGHDIM_PRIME_WALL_H1_H8_CLASSIFICATION_20260823.csv`
5. Classical source map with theorem-level citations:
   `research_output/HIGHDIM_PRIME_WALL_CLASSICAL_SOURCE_MAP_20260823.md`
6. Evidence event stream:
   `research_output/evidence/HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_20260823.jsonl`

The source map must distinguish primary theorem sources, later expositions, and project-specific inferences.

## Validation Standard

Required validation includes:

- independent symbolic derivations of H1-H7;
- exact treatment of the `n=0` term in convolution identities;
- direct computation from definitions on a declared finite range;
- separate arithmetic-function computation of the same quantities;
- composite pressure covering prime powers, squarefree products of two and three primes, and numbers with `4`-adic complications;
- a deliberately incorrect wall coefficient vector as a negative control;
- a proof that the prime biconditional follows from an exact divisor-sum characterization rather than empirical uniqueness;
- a criterion-level audit showing exactly what lambda=2 uniqueness quantifies over;
- primary-source verification of the twelve-square/Sato-Tate classification.

Any residual novelty claim must survive subtraction of all identified classical divisor-wall and convolution content and must be stated as a precise object with a falsifiable test.

## Evidence Policy

Keep four evidence layers separate:

1. independent exact proof;
2. independently authored computation;
3. external classical-equivalence evidence;
4. post-freeze source comparison.

Only layers 1-3 enter the independent classification. Layer 4 may diagnose agreement or source-specific presentation but may not upgrade an unproved item.

## Reporting Requirements

Use the repository-standard six report sections, and add:

- `Independent Proof Checkpoint`;
- `H1-H8 Verdict Table`;
- `Classical Equivalence DAG`;
- `Project-Specific Residual Test`;
- `Complexity and Semantic Nonclaims`;
- `Final Aggregate Verdict`.

Freeze the report before reading the withheld source branch or source proof. Stop after the independent return; package reconciliation belongs to the Driver.

## Repository Closure Protocol

Use the inherited repository closure protocol with no task-specific deviation. Promote the proof report, reducer, checker, classification matrix, source map, and evidence stream as one reviewable evidence package before archival.
