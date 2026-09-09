<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-PCF5-PCF6-PRIOR-ART-DRIVER-REVIEW",
  "title": "PCF5/PCF6 prior-art and duplication Driver review gate",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "PCF5 and PCF6 are mathematically accepted at narrow frozen strengths, but their classical antecedent/duplication boundary is not yet source-classified. Portfolio use is blocked until the current audit task returns and a Driver checks its cited comparison matrix.",
  "next_action": "After a current-generation prior-art audit Result exists, refresh exact Result bytes, verify every load-bearing source/application/classification, preserve PCF5/PCF6 accepted scopes, and record a terminal Driver disposition without turning NO_MATERIAL_MATCH into novelty.",
  "dependencies": [
    {
      "task_id": "RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT",
      "required_artifact": "current-generation immutable prior-art/duplication Result"
    }
  ],
  "source_refs": [
    "research_task_records/RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT/TP2-8D3D94C1C621740A50AB.json",
    "research_result_reviews/RR-D4F90C15C5BB4261230D/DR-E001B08CCF15959E6228.json",
    "research_result_reviews/RR-6F3A91D2C5E74B08A621/DR-51103D9B49E679F16EAD.json",
    "research_artifacts/PCF_PERSISTENT_LINE_DRIVER_20260909/dossier.md"
  ],
  "evidence_status": "BLOCKED_ON_CURRENT_PCF5_PCF6_PRIOR_ART_RESULT / SOURCE_APPLICATION_DRIVER_REVIEW_REQUIRED",
  "last_progress_ref": "research_result_reviews/RR-6F3A91D2C5E74B08A621/DR-51103D9B49E679F16EAD.json",
  "last_progress_at": "2026-09-02T13:12:00+00:00",
  "hard_block": {
    "missing_object": "current-generation PCF5/PCF6 prior-art audit Result",
    "owner": "RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT",
    "unblock_condition": "A current-generation immutable Result exists for the prior-art/duplication task."
  },
  "tags": [
    "PCF",
    "PCF5",
    "PCF6",
    "driver-review",
    "prior-art",
    "duplication",
    "governance"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-PCF5-PCF6-PRIOR-ART-DRIVER-REVIEW",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCFPADRV",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF5/PCF6 prior-art and duplication Driver review gate

Status: `BLOCKED / PUBLISHED_REGISTERED / DRIVER SOURCE-APPLICATION REVIEW`

## Mother question

Does the current PCF5/PCF6 comparison Result correctly classify the strongest classical antecedents and the surviving project-local residue without changing the two accepted mathematical theorems or inferring novelty from an incomplete search?

## Frozen inputs and scope

This task is blocked until `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT` / `TP2-8D3D94C1C621740A50AB` has a current-generation immutable Result.

Freeze PCF5 at `RESTRICTED_SUPPORT_COMPRESSION_PROVED / FIXED_KAPPA_COVERED_FAMILY_ONLY` and PCF6 at `FUNCTORIAL_REALIZATION_OBSTRUCTED / CORRECTED_FREE_RANK_2_ORIENTED_MIXED_REALIZATION_ONLY`.

The Driver review must check source identity, theorem applicability and the classification of each load-bearing mechanism against Strassen/Pollard-Strassen, factorial/product trees, batch gcd, CRT idempotents, product-ring decompositions and trace/determinant selector language. An absent material match is an unresolved historical-search outcome, not a novelty certificate.

No factoring speedup, lower bound, universal algorithm or general H-dependent impossibility is under review.

## Hard target and required outputs

Hard target:

`PCF5_PCF6_PRIOR_ART_BOUNDARY_EXACTLY_REVIEWED_AND_TERMINAL_DISPOSITION_RECORDED`

Required Driver outputs:

1. refresh and bind exact current Result bytes;
2. verify the cited comparison matrix row by row at the strength actually used;
3. preserve standard antecedents as standard and isolate only exact project-specific typed residue;
4. record a terminal disposition or the smallest source/application revision needed;
5. update the PCF dossier and incremental ledger;
6. expose the accepted prior-art boundary to portfolio synthesis without changing PCF5/PCF6 mathematics.

## Research value to preserve

The prior-art task is useful only if its classification can be independently checked. A dedicated Driver gate prevents classical batch-gcd/product-tree or CRT/idempotent language from being promoted through imprecise citation while also preserving any genuinely useful typed residue.

This separates mathematical acceptance from historical/duplication interpretation.

## Success, kill, and return criteria

Success is a terminal Driver disposition on the current source-backed comparison Result.

Request revision for missing load-bearing citations, inapplicable theorem transfer, unsupported novelty language, or any attempt to strengthen PCF5/PCF6.

Do not publish a mathematical successor from this review. The blocked portfolio-synthesis task owns that decision.
