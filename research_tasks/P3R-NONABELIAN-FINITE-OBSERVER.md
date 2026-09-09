<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-NONABELIAN-FINITE-OBSERVER",
  "title": "Non-abelian finite-field observer for homology 3-spheres",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "The abelian observer wall is established, but there is not yet one Enterprise-compatible exact pipeline from a homology 3-sphere group presentation to a finite-field non-sphericity certificate with assumptions and witness-prime provenance fully typed.",
  "next_action": "Specify the smallest finite-field representation certificate and checker for a nontrivial irreducible SL(2,F_q) image, then map the Zentner/Heusener-Zentner/Kuperberg theorem dependencies and GRH tags into that interface.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@cd79471e16df9b4afd924ccae76a626eeb31ec9a:research_notes/POINCARE_BRC_ARITHMETIC_OBSERVER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@c63167f2f911e2425b8a70b0aabcc90574425235:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "ESTABLISHED_EXTERNAL_THEOREM_ROUTE_PLUS_OPEN_ENTERPRISE_CERTIFICATE_PIPELINE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "poincare",
    "homology-sphere",
    "fundamental-group",
    "SL2",
    "finite-field",
    "groebner",
    "witness-prime"
  ],
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

# Non-abelian finite-field observer for homology 3-spheres

Status: `READY / PUBLISHED-INTENT / NONABELIAN-CERTIFICATE`

## 0. Mother question

Can the known representation-theoretic non-sphericity route for integer homology 3-spheres be expressed as a compact exact finite-field observer/certificate pipeline that complements the abelian normal-surface pruning layer?

## 1. Frozen inputs and scope

Use the durable handoff's information-loss wall: integral homology and Smith data cannot distinguish S^3 from the Poincaré homology sphere, so a non-abelian layer is mandatory for this route. Preserve the exact hypotheses and conclusion strength of the Zentner, Heusener–Zentner, and Kuperberg-type results; GRH-conditional and unconditional components must remain separately labeled.

Reuse the existing Gröbner certificate bridge for algebraic search/check separation and the existing effective witness-prime facade when its hypotheses match. Do not equate existence of a finite quotient with triviality/nontriviality of every presentation without the theorem connecting the certificate to the target manifold class.

## 2. Hard target and required outputs

Define a certificate format starting from an explicit finite presentation of pi_1(M) and ending with matrices over a finite field that satisfy all relators and witness a nontrivial/irreducible representation adequate for the stated non-sphericity theorem. Supply a deterministic checker for the finite-field matrix relations and the nontriviality/irreducibility condition used.

Document the theorem dependency chain from a non-spherical integer homology 3-sphere to existence of the complex representation, reduction to a finite field/witness prime, and the resulting certificate. State every number-field, discriminant, ramification, and GRH assumption needed by the chosen effective bound. Include S^3 and the Poincaré homology sphere as control cases and at least one additional homology-sphere example if practical.

## 3. Research value to preserve

This route supplies the non-abelian information that the branch-cokernel observer necessarily loses. A successful finite certificate would produce a two-sided recognition architecture: arithmetic branch pruning on the surface side and finite non-sphericity witnesses on the group side.

## 4. Success, kill, and return criteria

SUCCESS requires an exact finite certificate/checker and a source-audited theorem chain that states whether the result is unconditional or conditional. KILL any step that silently assumes faithful reduction, irreducibility preservation, a small witness prime, or a GRH hypothesis not supplied by the cited theorem.

If a fully effective pipeline is blocked by discriminant/field-construction complexity, return that as the smallest obstruction together with the strongest still-valid non-effective certificate statement. Stop before claiming a new Poincaré proof or a complexity-class improvement not actually established.
