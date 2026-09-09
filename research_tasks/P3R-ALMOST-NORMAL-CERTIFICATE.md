<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-ALMOST-NORMAL-CERTIFICATE",
  "title": "Exact modular certificates for normal and almost-normal branches",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "The branch-cokernel and descendant-pruning derivations are mathematically clear, but the exact certificate interface, incremental-update conditions, and almost-normal octagon coordinate adapter are not yet packaged as a reusable verified theorem/checker.",
  "next_action": "Write the exact integer theorem statements and a reference certificate checker, then derive the octagonal almost-normal inhomogeneous target matrix and test the checker on small hand-verified examples.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@cd79471e16df9b4afd924ccae76a626eeb31ec9a:research_notes/POINCARE_BRC_ARITHMETIC_OBSERVER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@c63167f2f911e2425b8a70b0aabcc90574425235:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "PROVED_CORE_DERIVATION_PLUS_OPEN_FORMAL_CERTIFICATE_AND_ALMOST_NORMAL_ADAPTER",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "poincare",
    "almost-normal-surfaces",
    "certificate",
    "BRC",
    "integer-lattice",
    "formalization"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "P3R-ALMOST-NORMAL-CERTIFICATE",
  "parent_objective_id": "POINCARE-BRC-RECOGNITION-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P3R2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Exact modular certificates for normal and almost-normal branches

Status: `READY / PUBLISHED-INTENT / EXACT-CERTIFICATE`

## 0. Mother question

Can the branch-cokernel obstruction be packaged as a small exact certificate system, including safe incremental reuse down the branch tree and the octagonal almost-normal stage of Rubinstein–Thompson recognition?

## 1. Frozen inputs and scope

Preserve the originating derivations: if b is outside im_Z(M_beta), a finite cyclic quotient supplies a prime-power character separator; descendants only delete columns, so the same equality-relaxation nonmembership persists. Keep the distinction between integer-image infeasibility and nonnegative/admissible surface existence.

Extend only to explicitly defined normal or octagonal almost-normal coordinate systems. Do not claim that a separator decides connectedness, nontriviality, simple connectedness, or final 3-sphere recognition. Reuse existing exact Smith/local-support and modular arithmetic machinery instead of creating a parallel generic algebra package.

## 2. Hard target and required outputs

Return precise theorem statements for: branch-cokernel necessity, finite p^k character separation, descendant monotonicity, and the exact conditions under which a cached separator remains valid after additional column deletions or coordinate restriction.

Provide a deterministic certificate format and checker taking M,b,p,k,y and verifying y^T M = 0 mod p^k and y^T b != 0 mod p^k. Derive the target equation for a fixed exceptional octagon location/type and show exactly how the same certificate interface applies. Include small regression examples covering: torsion obstruction, free-part obstruction reduced to a finite prime quotient, a surviving branch with no false rejection, and an almost-normal example.

## 3. Research value to preserve

A compact checker separates expensive search from trusted verification and makes the arithmetic observer reusable by multiple recognition algorithms. Even if the benchmark route is weak, the exact separator/monotonicity package is a clean theorem-level bridge between integer topology encodings and finite observers.

## 4. Success, kill, and return criteria

SUCCESS requires a self-contained exact certificate specification plus proofs/derivations sufficient for independent checking and at least one working implementation or formal skeleton. KILL any proposed incremental shortcut that fails under column deletion, row changes, Euler-characteristic normalization, or octagon-coordinate translation; retain a counterexample.

Return separately what is proved, what is implementation-verified, and what remains conjectural. Stop when the normal and almost-normal certificate boundaries are explicit enough that another researcher can use them without the originating conversation.
