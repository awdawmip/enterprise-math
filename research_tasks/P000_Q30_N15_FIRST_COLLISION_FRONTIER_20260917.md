<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-Q30-N15-FIRST-COLLISION-FRONTIER",
  "title": "P000 Q30 n=15 first collision frontier",
  "kind": "RESEARCH",
  "owner": "research/p000-q30-n15-first-collision-frontier",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Independent review has accepted the recovered exact n<=14 collision-free prefix for the frozen primitive-return-profile initialized ordinary 1-WL observable. The first unclassified size is n=15; the n<=14 result alone neither proves nor disfavors a first equal-packet collision there.",
  "next_action": "Freeze the exact Q30 observable and U_BR(15) object class, derive an exhaustive sector decomposition and coverage certificate before large enumeration, then test exact stabilized-packet equality for every nonisomorphic representative and either exhibit the first collision witness or certify the complete n=15 prefix.",
  "dependencies": [],
  "source_refs": [
    "research_result_records/RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE/RR-15457ACA568B33A04CE7.json",
    "research_result_reviews/RR-15457ACA568B33A04CE7/DR-CC898FED6F444A808B06.json",
    "driver_reviews/P000_Q30_N14_EVIDENCE_RECOVERY_DRIVER_REVIEW_20260917.md",
    "research_tasks/P000_Q30_N14_EVIDENCE_RECOVERY_CANONICALIZATION_GATE_20260909.md",
    "git:awdawmip/enterprise-math@b90378c332e0dbf80aad0c09d363047abb2ee2f3:research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_RETURN_PROFILE_1WL_N14_EXACT_KERNEL_ORBIT_CERTIFICATE_V2.json"
  ],
  "evidence_status": "DRIVER_ACCEPTED_N14_RECOVERY / N15_UNRESOLVED",
  "last_progress_ref": "research_result_reviews/RR-15457ACA568B33A04CE7/DR-CC898FED6F444A808B06.json",
  "last_progress_at": "2026-09-17T06:54:00+00:00",
  "hard_block": null,
  "tags": [
    "P000",
    "Q30",
    "n15",
    "return-profile",
    "1-WL",
    "collision-frontier",
    "BRC",
    "exact-enumeration"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-Q30-N15-FIRST-COLLISION-FRONTIER",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000Q30N15",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE",
  "successor_gate": {
    "new_information_gap": "Whether the frozen Q30 observable remains injective on U_BR(15), the first size not covered by the accepted n<=14 evidence.",
    "why_parent_result_does_not_close_it": "The predecessor is an evidence-recovery task bounded to n=14. Its accepted result explicitly makes no statement for n>=15.",
    "discriminating_outcomes": [
      "An explicit pair of nonisomorphic U_BR(15) graphs with exactly equal frozen stabilized packets is found and independently replayable.",
      "An exhaustive coverage certificate plus exact packet comparison proves no collision at n=15, extending only the finite prefix through n=15.",
      "A precise coverage, provenance, or tractability obstruction prevents a trustworthy complete n=15 decision; the task returns that smallest obstruction without extrapolation."
    ],
    "kill_condition": "Stop if the execution changes the frozen observable, substitutes digests for exact packet equality, or cannot certify exhaustive coverage of the claimed search domain.",
    "alternative_route_or_free_exploration_considered": "Closing Q30 at n<=14, switching to a stronger observer, and unrelated free exploration were considered. The n=15 boundary is preferred because it is the smallest direct falsification/extension test of the existing mother question and does not require importing a stronger observable.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The recovery task is complete and cannot legally expand beyond n=14. A separate continuation isolates the genuinely new finite frontier, its computational burden, and its own stop criteria."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 Q30 n=15 first collision frontier

Status: `READY / P1 / HIGH / EXACT FRONTIER / PUBLISHED_REGISTERED`

## Mother question

For the unchanged Q30 observable — primitive simple-cycle return profiles used to initialize ordinary 1-WL, followed by the same anonymous stabilization packet — is there a first nonisomorphic equal-packet collision on `U_BR(15)`? If not, can the collision-free finite prefix be extended exactly through `n=15` with a complete coverage certificate?

## Frozen inputs and scope

The accepted predecessor establishes only the bounded prefix through `n=14`. Freeze its exact observable, packet semantics and provenance. The present task changes only the object size to `n=15`.

BRC discipline is mandatory at the execution boundary: preserve the object carrier, the reduction/sector coordinates used for exhaustive coverage, and the exact observer separately. Kernel or sector coordinates may organize enumeration but are not a stronger graph observable. Digests are integrity pins only; collision identity is exact stabilized-packet equality, followed by an independent nonisomorphism check for any repeated packet.

Do not introduce 2-WL, spectral data, zeta data, full cycle-incidence data or any other stronger feature to make the task pass. A graph canonicalizer may be used only as an enumeration/deduplication implementation aid if its role is kept separate from the Q30 observer and its coverage use is independently checkable.

## Hard target and required outputs

Hard target: `Q30_N15_FIRST_COLLISION_FRONTIER_EXACTLY_DECIDED_OR_MINIMAL_OBSTRUCTION_RETURNED`.

Required outputs are:

1. an explicit `U_BR(15)` sector/decomposition specification and independent completeness criterion;
2. exact persistent representative evidence sufficient to replay the claimed search domain;
3. exact frozen Q30 packet construction and equality test;
4. if a repeated packet occurs, an explicit smallest reproducible pair plus an independent nonisomorphism witness;
5. if no repeated packet occurs, exact per-sector counts, automorphism/orbit or equivalent coverage checks and a full finite-prefix certificate limited to `n<=15`;
6. a deterministic checker or replay package whose finite claims can be independently rerun;
7. a current execution/result/return package that distinguishes mathematical status from execution state and states the finite boundary precisely.

## Research value to preserve

`n=15` is the first unclassified size after the independently accepted recovery of the complete `n<=14` prefix. It is therefore the smallest direct test that can either falsify the current injectivity pattern with a concrete collision or strengthen only the finite lower bound by one size. The task is valuable because either outcome is sharply discriminating and because it does not rely on a stronger observer or on extrapolation from the existing finite data.

Closure was considered: stopping at `n<=14` would preserve a valid result but leave the mother question's immediate falsification frontier untouched. Unrelated exploration may proceed independently, but it cannot answer this exact first-open-size question.

## Success, kill, and return criteria

Return `COLLISION_FOUND` only with exact packet equality and an independently checkable nonisomorphism witness for a concrete pair.

Return `NO_COLLISION_THROUGH_N15` only after exhaustive coverage of the frozen `U_BR(15)` domain is certified and all exact packets are checked. This remains a finite result and must not be generalized to larger `n`.

Return `MINIMAL_OBSTRUCTION` if exhaustive coverage, source integrity, exact replay or required computational feasibility fails. Name the first exact obstruction and preserve all completed sector evidence without inferring a theorem from an incomplete census.

Terminate immediately if the frozen observable is strengthened, if hashes replace semantic equality, or if a claimed no-collision result lacks an auditable coverage certificate.
