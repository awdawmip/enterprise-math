<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-A3-RELATION-LATTICE",
  "title": "A3 Sparse Relation Lattice — Star Smith Reconstruction Replay",
  "kind": "RESEARCH",
  "owner": "core/a3-relation-lattice-v3",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "Upgrade the sparse A3 spanning-tree coordinate result from determinant/index data to an exact Smith-normal-form and cokernel classification for primitive and unnormalized star bases, including the sharp cyclicity boundary.",
  "next_action": "Resume from the frozen A3 sparse relation-lattice result at PR #232 head a9c5d25e486ea43d77458870e25f37421121c809; derive the star coordinate matrix reduction to a diagonal-plus-rank-one block, compute every determinantal divisor, freeze the exact Smith factors and cokernel/cyclicity consequences, and independently regression-check them by exact minors.",
  "dependencies": [
    "legacy research_scheduler.json RS-A3-RELATION-LATTICE frozen baseline",
    "PR #232 frozen owner head a9c5d25e486ea43d77458870e25f37421121c809",
    "canonical A3 weighted relation field and relation-lattice kernel/translation-period definitions"
  ],
  "source_refs": [
    "src/enterprise_math/relation_tree_lattice.py@core/a3-relation-lattice-v3",
    "src/enterprise_math/relation_zero_total_orbit.py@core/a3-relation-lattice-v3",
    "src/enterprise_math/relation_lattice.py@core/a3-relation-lattice-v3"
  ],
  "evidence_status": "LEGACY_HANDOFF_REPLAY / TREE_INDEX_AND_UNIT_STAR_LEGALITY_PROVED / FULL_STAR_SMITH_TYPE_OPEN",
  "last_progress_ref": "PR #232 frozen owner head a9c5d25e486ea43d77458870e25f37421121c809",
  "last_progress_at": "2026-08-09T21:30:00+08:00",
  "hard_block": null,
  "tags": [
    "A3",
    "relation-lattice",
    "Smith-normal-form",
    "star-basis",
    "cokernel",
    "legacy-migration"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-A3-RELATION-LATTICE",
  "parent_objective_id": "A3_SPARSE_RELATION_LATTICE_CONTINUATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "A3RL",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# A3 Sparse Relation Lattice — Star Smith Reconstruction Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

For the canonical A3 weighted relation state with positive capacities, the frozen sparse spanning-tree result determines the image-lattice index of total-plus-tree-relation coordinates, but the index alone does not determine the finite cokernel. For a star basis, can the complete Smith invariant-factor decomposition be derived exactly, so that the legal-coordinate obstruction is classified as a finite abelian group rather than only counted by its order?

The intended terminal result is the exact Smith type for every star center and every capacity vector, together with the precise boundary between a single global congruence and genuinely multi-generator torsion.

## Frozen inputs and scope

Use the A3 weighted relation map `Z_ij = m_j p_i - m_i p_j`, the common capacity quantum `g = gcd_i(m_i)`, primitive capacities `a_i=m_i/g`, and translation period `tau=sum_i a_i`. The frozen sparse-tree result gives the exact star index and the unit-primitive-center reconstruction criterion.

The replay may use standard integer-matrix facts about Smith normal form and determinantal divisors. It must derive the specialized invariant factors rather than infer them from the determinant. No E001 contact semantics, continuum interpretation, physical model, or novelty claim is in scope.

## Hard target and required outputs

Hard target:

`A3_STAR_SMITH_NORMAL_FORM_AND_COKERNEL_EXACTLY_CLASSIFIED`

Required outputs:

1. write the primitive and unnormalized star coordinate matrices for an arbitrary center;
2. reduce the primitive matrix by unimodular operations to `1` plus a diagonal-plus-rank-one block;
3. compute all determinantal divisors of that block and derive the full Smith invariant factors, including `N=1`, `N=2`, and `N=3` boundaries;
4. translate the Smith form into the exact finite cokernel decomposition and a sharp cyclicity criterion;
5. recover the previously proved star index as the product of the new invariant factors;
6. independently regression-check the formula by exact integer minors/determinants over a broad finite family without using a computer-algebra Smith-form oracle;
7. record the standard-prior-art boundary and freeze the result in `research_returns/A3_RELATION_LATTICE_STAR_SMITH_RECONSTRUCTION_RETURN_20260827.md`, with any checker and certificate under the task-owned artifact paths.

## Research value to preserve

The old A3 result says how sparse tree topology changes the density of legal integer coordinates. The missing structural information is how that index splits into independent torsion channels. A Smith classification distinguishes a truly single global congruence from several independent local congruence obstructions and therefore gives a stronger precision invariant than determinant size alone.

For unit primitive star centers the earlier one-congruence theorem should appear as an exact special case, not as a separately assumed fact.

## Success, kill, and return criteria

Success requires a general exact proof of the invariant factors and cokernel decomposition, with the determinant/index theorem recovered as a corollary and independent finite regression agreeing at every tested boundary.

Narrow or kill the proposed formula immediately if any exact minor calculation violates the claimed determinantal divisors, if primitive normalization fails to isolate the stated block, or if the invariant-factor divisibility chain requires extra hypotheses not present in A3. In that case freeze the smallest counterexample or the strongest correct restricted theorem.

Finite computation is falsification/regression evidence only. No claim of external novelty or Foundation promotion follows from task completion.
