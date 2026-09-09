<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-NONABELIAN-FINITE-OBSERVER",
  "title": "Dependent non-abelian finite-field cross-check for homology 3-spheres",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P3",
  "leverage": "MEDIUM",
  "frontier": "Finite-field representation certificates remain useful for non-sphericity cross-checks, but the general Zentner/Heusener-Zentner route depends on geometrization and therefore cannot close an independent Poincare reproof.",
  "next_action": "Package the finite-field representation checker and map the exact geometrization/GRH dependency chain so the route can be used as a correctly tagged algorithmic cross-check without circular proof claims.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@3359de19ffb776ebfaa59bc7443b171b23d35f4d:research_notes/POINCARE_BRC_CORRECTED_FRONTIER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@8acfeac504eee85f6fbb66018470ad233ef33ff7:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "EXTERNAL_REPRESENTATION_ROUTE_ESTABLISHED_BUT_GEOMETRIZATION_DEPENDENT_FOR_GENERAL_CLOSURE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["poincare","homology-sphere","fundamental-group","SL2","finite-field","cross-check","geometrization-dependency"],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "P3R-NONABELIAN-FINITE-OBSERVER",
  "parent_objective_id": "POINCARE-BRC-RECOGNITION-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P3R3",
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

# Dependent non-abelian finite-field cross-check for homology 3-spheres

Status: `READY / SUPERSEDING-GENERATION / DEPENDENCY-TYPED-CROSS-CHECK`

## 0. Mother question

Can the known representation-theoretic non-sphericity route be packaged as a small exact finite-field certificate/checker while making its geometrization and GRH dependencies impossible to confuse with an independent proof of Poincaré?

## 1. Frozen inputs and scope

The abelian observer wall remains valid: integral homology cannot distinguish S^3 from the Poincaré homology sphere. Non-abelian finite representations are therefore informative cross-checks.

However the general theorem chain from a non-spherical integer homology 3-sphere to an irreducible SL(2,C) representation and the resulting recognition algorithm uses geometrization in the general case. Preserve this dependency explicitly. If an effective finite-field reduction uses a witness-prime theorem with GRH, carry that assumption separately from the geometrization dependence.

Reuse the existing Gröbner-certificate and effective witness-prime interfaces when their hypotheses match. Do not present this route as the missing non-circular bridge.

## 2. Hard target and required outputs

Define a finite certificate from a presentation of pi_1(M) to matrices over a finite field satisfying all relators and the exact nontriviality/irreducibility condition required by the cited theorem. Supply a deterministic checker for those finite-field relations.

Produce a dependency ledger from the manifold hypothesis through complex representation existence, algebraic reduction, witness-prime selection, and finite certificate. Mark each edge as unconditional, geometrization-dependent, GRH-conditional, or merely algorithmic. Include S^3 and the Poincaré homology sphere as control cases and an additional documented example if practical.

## 3. Research value to preserve

Even though it cannot supply an independent Poincaré proof, this route is a useful negative-certificate and regression channel for the broader recognition program. Explicit dependency typing prevents a sophisticated circularity error from re-entering later synthesis.

## 4. Success, kill, and return criteria

SUCCESS requires an exact finite checker plus a source-audited dependency ledger. KILL any claimed independent-closure conclusion as soon as geometrization or an equivalent Poincaré-strength input appears in the theorem chain. Reject any effective small-prime statement whose number-field, ramification, discriminant, or GRH assumptions are not certified.

If the finite certificate is practical but the effective prime bound is not, return the strongest valid non-effective/effective split. Stop with this route classified as cross-check unless a genuinely non-circular theorem is separately proved.
