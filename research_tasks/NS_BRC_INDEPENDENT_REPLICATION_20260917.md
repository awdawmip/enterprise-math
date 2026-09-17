<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NS-BRC-INDEPENDENT-REPLICATION-20260917",
  "title": "Independent Replication and Proof Audit of the NS/BRC Research Chain",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The NS/BRC line now depends on a long chain of exact Fourier identities, interval bounds, computer-assisted constants, causal inverse theorems, and restricted-family certificates. No single independent reconstruction has yet rebuilt the decisive chain from raw definitions through the latest certificate.",
  "next_action": "Re-derive the minimum decisive theorem chain with separately written mathematics and code: critical/symmetric bilinear estimates, all-frequency tails, causal inverse interface, response-support identities, and one success plus one obstruction certificate; record every mismatch without repairing it silently.",
  "dependencies": [],
  "source_refs": [
    "research_notes/ns_brc_program_handoff_20260917.md",
    "research_notes/ns-coupled-polarization-20260910.md",
    "research_notes/ns-orthogonal-response-barrier-20260910.md",
    "research_notes/ns-goal-primal-dual-certificate-20260910.md",
    "research_notes/ns-causal-inverse-newton-basin-20260909.md"
  ],
  "evidence_status": "RESEARCH_PROGRAM_INTEGRATION_V1",
  "last_progress_ref": "research_notes/ns_brc_program_handoff_20260917.md",
  "last_progress_at": "2026-09-17T12:53:00+08:00",
  "hard_block": "INDEPENDENT_END_TO_END_REPLICATION_MISSING",
  "tags": ["Navier-Stokes", "BRC", "replication", "audit", "proof", "computer-assisted"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NS-BRC-INDEPENDENT-REPLICATION-20260917",
  "parent_objective_id": "EM-NS-BRC-JITTER-REGULARITY-PROGRAM-20260917",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R-NSRV",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Independent Replication and Proof Audit of the NS/BRC Research Chain

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Does an independent reconstruction of the decisive NS/BRC theorem chain reproduce the stated identities, constants, all-mode bounds, and restricted-family global regularity certificates without relying on hidden state or circular assumptions?

## 1. Frozen inputs and scope

This is an independent replication task, not an optimization task. Use the cited source statements as objects to be checked, but rebuild decisive calculations with separately written code or symbolic derivations wherever feasible.

Prioritize dependencies that affect the current frontier: critical and symmetric bilinear constants, infinite-frequency tail bounds, causal inverse estimates, response-support identities, nonlinear contraction margins, and the distinction between certificate failure and singularity.

Do not repair discrepancies in place. Preserve failing examples, exact inputs, and whether each issue is mathematical, numerical, or documentary.

## 2. Hard target and required outputs

Hard target: `INDEPENDENT_REPLICATION_PASS_OR_PINNED_DISCREPANCY`.

Deliver all of the following:

1. A dependency graph of the smallest chain needed to validate one current restricted-family global NS certificate.
2. Independent derivations of the analytic identities and an independent implementation of the finite exact or interval checks for the decisive constants.
3. Reproduction of at least one success certificate and one no-go/certificate-obstruction example.
4. An audit for hidden assumptions: finite-to-infinite extrapolation, time sampling, branch compression, normalization changes, and use of unproved prior statements.
5. A literature cross-check separating established methods from project-specific formulas, without making a novelty claim unless justified.
6. A final PASS/FAIL/INCONCLUSIVE verdict for each dependency, with exact discrepancy artifacts for every non-PASS item.

## 3. Research value to preserve

The research program is mature enough that independent falsification has higher value than another incremental constant improvement. A replicated chain would make later paper-level work credible; a discrepancy would prevent the portfolio from building further on an undetected error.

## 4. Success, kill, and return criteria

Success is an independent end-to-end reproduction of the decisive chain or a precisely pinned discrepancy that changes theorem strength or routing.

Kill any replication that reuses the same generated numerical files as its only evidence, accepts floating-point agreement without interval/error analysis where the original theorem requires it, or treats literature similarity as proof of the project-specific constants.

Return the verdict matrix and route every material discrepancy back to the Driver portfolio task.
