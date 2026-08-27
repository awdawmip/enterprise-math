<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-OBSERVATION-HISTORY",
  "title": "P022 Observation-History Composite Franel Escape Closure — Current-Policy Replay",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Resume the latest durable P022 observation-history frontier at owner head 603ef1c72245612359f8b59cab7a492de21a9166 and close, refute, or sharply isolate the remaining composite Franel escape mechanism after the first-reentry kernel, transfer-depth reductions, and forced-midpoint harmonic pairing.",
  "next_action": "At owner head 603ef1c72245612359f8b59cab7a492de21a9166, combine the forced-midpoint scale identity with the exact harmonic pairing U_p=2T_p to attack the surviving equal-depth signature v_p(F_(2k-1))=v_p(F_m)>0. Derive the first p-adic correction at the forced midpoint/third-index transfer, test whether equal first jets are impossible in the surviving residue classes, and if not freeze the smallest exact exceptional condition rather than enlarging a finite cutoff.",
  "dependencies": [
    "legacy research_scheduler.json RS-P022-OBSERVATION-HISTORY frozen baseline",
    "legacy HANDOFF durable frontier at program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
    "owner-branch durable continuation program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166"
  ],
  "source_refs": [
    "docs/P022_BARLOW_FRANEL_LUCAS_RANK.en.md@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_forced_midpoint_scale_hasse.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_midpoint_harmonic_pairing.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_reflection_first_jet.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_terminal_depth_lift.py@program/p022-geometry-v2"
  ],
  "evidence_status": "LEGACY_HANDOFF_REPLAY / OWNER_BRANCH_152_COMMIT_DURABLE_CONTINUATION_RECOVERED / COMPOSITE_FRANEL_ESCAPE_FRONTIER_OPEN",
  "last_progress_ref": "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166",
  "last_progress_at": "2026-08-12T17:28:26+08:00",
  "hard_block": null,
  "tags": [
    "P022",
    "observation-history",
    "Barlow",
    "Franel",
    "p-adic",
    "identifiability",
    "legacy-migration"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-OBSERVATION-HISTORY",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_IDENTIFIABILITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022OBS",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022 Observation-History Composite Franel Escape Closure — Current-Policy Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

The P022 observation-history route reduces finite hidden-tail identifiability to the visibility of prime valuation rows in a Franel-defect coordinate system. After the recovered owner-branch work, the remaining question is no longer the old finite determinant problem: can a prime valuation row escape every available composite defect because Franel zero depths transport and cancel exactly, or can the surviving escape signature be ruled out by an exact arithmetic obstruction?

The task is to close that residual mechanism at its present strongest form, or freeze the smallest exact exceptional condition if a universal closure is false or currently unjustified.

## Frozen inputs and scope

Use `program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166` as the durable replay source. Treat the following owner-branch results as frozen inputs unless an explicit contradiction is found:

- the first-reentry kernel classification for twin-centered primitive rows;
- the prime-boundary deletion / path-coboundary interpretation of complete invisibility;
- midpoint residue obstructions and the reduction to exceptional arithmetic sectors;
- exact Franel zero-transfer and reflection laws;
- the q-adic first-jet and terminal-transfer reductions already encoded on the branch;
- the forced-midpoint scale identity reducing continued escape to equality of two positive Franel depths with the adjacent depth zero;
- the exact forced-midpoint harmonic pairing `U_p = 2 T_p (mod p)`.

The recovered branch is 152 commits ahead of the historical handoff source, so old intermediate fronts are not to be replayed. Finite experiments may falsify or map exceptional sectors, but they do not by themselves establish all-prime identifiability.

## Hard target and required outputs

Hard target:

`P022_COMPOSITE_FRANEL_ESCAPE_CLOSED_OR_MINIMAL_EXACT_EXCEPTION_FROZEN`

Required outputs:

1. derive the next exact p-adic relation implied by the forced-midpoint harmonic pairing and the existing transfer-depth identity;
2. determine whether the surviving equal-depth signature can occur in the admissible prime/residue constellation;
3. if it is impossible, give a proof-level obstruction and reconnect it to observation-history row visibility;
4. if it can occur or the present inputs do not decide it, state the smallest exact exceptional condition and exhibit a verified witness or a sharply bounded no-go statement;
5. add only task-local exact computation needed for falsification/regression, clearly separated from proof;
6. freeze a durable return that names the exact remaining frontier, hard block if any, and the strongest reusable theorem or obstruction established.

## Research value to preserve

This route already replaced a large finite rank calculation by an arithmetic visibility theory for composite Franel defects. Closing the last depth-cancellation mechanism would upgrade the P022 observation-history result from strong finite/unimodular evidence plus structural reductions to a reusable all-index identifiability mechanism. Even a negative result is valuable if it isolates an explicit p-adic exceptional class rather than leaving a vague “composite index” gap.

## Success, kill, and return criteria

Success is an exact arithmetic argument that rules out the surviving escape signature under the stated P022 hypotheses and therefore forces a visible row, or an exact counterexample/exception theorem that proves such a universal argument false.

Kill any proposed shortcut that only raises a numerical cutoff, assumes unproved generic nonvanishing, replaces depth equality by residue nonvanishing, or silently imports a stronger theorem than the frozen source provides. If the first p-adic correction reduces to a genuinely independent unresolved congruence, freeze that congruence precisely and return it as the minimal residue rather than continuing by brute force.

A finite scan is regression or falsification evidence only. The task return must distinguish proved identities, computational observations, and unresolved arithmetic premises.
