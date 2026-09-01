<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "base_state": "READY",
  "leverage": "HIGH",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT",
  "title": "PCF restricted routes external prior-art / duplication audit",
  "owner": "research/pcf-restricted-routes-external-prior-art-audit",
  "priority": "P1",
  "frontier": "Place the accepted PCF5 restricted-support theorem and PCF6 corrected-carrier obstruction against the strongest classical and standard algebraic antecedents without changing either theorem's mathematical strength.",
  "next_action": "Audit PCF5 against Strassen/Pollard-Strassen, factorial/product-tree/batch-gcd and related support-compression methods; audit PCF6 against CRT/idempotent/product-ring decomposition; classify exact antecedent, strict specialization, project-specific typed residue, or duplication.",
  "dependencies": [
    "RR-D4F90C15C5BB4261230D",
    "RR-6F3A91D2C5E74B08A621"
  ],
  "source_refs": [
    "RR-D4F90C15C5BB4261230D",
    "RR-6F3A91D2C5E74B08A621"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "tags": [
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "DRIVER_AUTO_FOLLOWUP",
    "PCF",
    "prior-art",
    "duplication-audit"
  ],
  "registry_key": "RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT",
  "identity_lane": "PCF-PRIOR-ART"
}
-->

# PCF restricted routes external prior-art / duplication audit

Status: `READY / DRIVER REVIEW FOLLOW-UP`

## 0. Mother question

At the exact accepted strengths of PCF5 and PCF6, which parts are standard classical/algebraic antecedents, which are strict specializations, and which project-specific typed residues remain after a source-backed external prior-art and duplication audit?

## 1. Frozen inputs and scope

Freeze `RR-D4F90C15C5BB4261230D` at the restricted fixed-kappa covered-family support-compression strength only, and freeze `RR-6F3A91D2C5E74B08A621` at the corrected free-rank-2 oriented mixed-realization obstruction only. Do not upgrade either Result into universal factoring, a factoring lower bound, a speedup theorem, or a general H-dependent impossibility theorem.

For PCF5, explicitly compare against classical Strassen/Pollard-Strassen style factoring, factorial/product-tree/batch-gcd constructions, and standard support/product compression. For PCF6, explicitly compare against CRT idempotents, product-ring decomposition, trace/determinant selectors, and standard finite-algebra realization language. Source-backed comparison is required; project-internal naming alone is not evidence of novelty.

## 2. Hard target and required outputs

Hard target: `PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`.

Return a cited comparison matrix that classifies every load-bearing ingredient as `EXACT_ANTECEDENT`, `STRICT_ANTECEDENT`, `STANDARD_METHOD_REPACKAGING`, `PROJECT_SPECIFIC_TYPED_RESIDUE`, or `NO_MATERIAL_MATCH`. Explain which accepted claims remain useful even when a mechanism is standard. Any `NO_MATERIAL_MATCH` row must explicitly state that it is not a novelty certificate.

## 3. Research value to preserve

The Driver acceptance closes evidence-integrity uncertainty but does not by itself establish novelty. This audit prevents classical batch-gcd/product-tree or CRT/idempotent machinery from being renamed as a new factoring mechanism, while preserving exact typed obstructions and restricted-family statements that may still be valuable as project-local boundaries.

## 4. Success, kill, and return criteria

Success is an exact source-backed duplication boundary for both Results. Kill any novelty or superiority claim that depends only on renamed standard machinery. If the strongest comparison cannot be completed from reliable sources, return the unresolved rows rather than inferring novelty. Do not alter PCF5/PCF6 mathematics, publish a factoring claim, or create a new algorithmic successor from this maintenance audit.
