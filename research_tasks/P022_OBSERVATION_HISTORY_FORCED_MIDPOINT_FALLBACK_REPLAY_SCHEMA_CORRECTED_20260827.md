<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-OBSERVATION-HISTORY",
  "title": "P022 Observation-History Franel Forced-Midpoint Fallback — Schema-Corrected Current-Policy Replay",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Freeze and independently replay-verify the strongest durable P022 primitive-twin forced-midpoint capture theorem: for target primes q congruent to 5 or 23 modulo 24 whose first Franel zero is a nontrivial twin center r, prove that q<6r-1 forces positive defect capture no later than the midpoint segment, while isolating q>=6r-1 as the exact surviving high-range frontier.",
  "next_action": "Start from program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166. Audit the exact signed midpoint support, primitive-zero exclusions, the q=23 mod 24 prime-midpoint dangerous index, and the earlier twin-blackout capture implication; run an independent exact recurrence falsification scan and freeze the bounded theorem without claiming the high-range residue is solved.",
  "dependencies": [
    "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166",
    "src/enterprise_math/p022_barlow_forced_midpoint_fallback.py@blob:6c6e8399e622f36015367aa4694e9de62adcb8d7",
    "src/enterprise_math/p022_barlow_twin_transport_closure.py@blob:80bd39a143ed0b4cb8ca5624128b4f823db00d8d",
    "docs/P022_BARLOW_FRANEL_THIRD_INDEX_FROBENIUS_CHARACTER_ORBIT.en.md@blob:dca0e45c4cf263e05b6fef62ff39ab74ace3c397"
  ],
  "source_refs": [
    "src/enterprise_math/p022_barlow_forced_midpoint_fallback.py",
    "src/enterprise_math/p022_barlow_franel_midpoint_harmonic_pairing.py",
    "src/enterprise_math/p022_barlow_twin_transport_closure.py",
    "src/enterprise_math/p022_barlow_twin_general_high_transfer.py"
  ],
  "evidence_status": "DURABLE_OWNER_THEOREM_RECOVERED / INDEPENDENT_REPLAY_AND_RETURN_FREEZE_OPEN",
  "last_progress_ref": "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166",
  "last_progress_at": "2026-08-12T09:28:26+00:00",
  "hard_block": null,
  "tags": ["P022","Barlow","Franel","primitive-twin","forced-midpoint","capture","legacy-migration","schema-corrected"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-OBSERVATION-HISTORY",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_AND_COLLISION_GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022",
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

# P022 Observation-History Franel Forced-Midpoint Fallback — Schema-Corrected Current-Policy Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

The historical P022 observation-history generation continued far beyond its last control-plane handoff and left a substantial durable owner branch. The strongest bounded closure at the current owner head is the forced-midpoint fallback theorem for primitive Franel primes arising from nontrivial twin centers.

Let `q>5` be prime with `q=5 or 23 (mod 24)`, let

`m=(q-1)/2`,

and suppose the first positive Franel zero modulo `q` occurs at a nontrivial twin center `r`. Determine exactly whether the regime

`q < 6r-1`

is completely captured by the defect family no later than the midpoint segment, including the exceptional signed-support geometry when `q=23 (mod 24)` and `m` is prime.

The purpose of this replay is to turn that durable owner theorem into one explicitly bounded, independently checked research return. It must not promote the unresolved high range `q>=6r-1` to a solved statement.

## Frozen inputs and scope

The following owner-local facts may be consumed after exact statement audit:

- forced midpoint: `F_m=0 (mod q)` in the target residue classes;
- adjacent Franel zeros modulo a prime are impossible below the singular index;
- primitive first-zero rank makes every smaller positive support index a `q`-unit;
- for `q=5 (mod 24)`, and also for `q=23 (mod 24)` with composite midpoint, all signed support above `B=(q+1)/6` collapses to `(m-1,+1)`;
- for `q=23 (mod 24)` with prime midpoint, the exact support above `B` is `(h-1,+1),(h,-1),(m-1,+1)` with `h=(m+1)/2`;
- if the dangerous index `h-1` vanishes after the primitive rank, its odd boundary `m-2` is a nontrivial multiple of three and the existing twin-blackout valuation formula captures it earlier.

The recovered owner branch also contains later high-range transport modules. Those are context only; they are not needed to prove the bounded fallback theorem.

## Hard target and required outputs

`P022_FORCED_MIDPOINT_FALLBACK_CAPTURE_EXACT_AND_INDEPENDENTLY_REPLAY_VERIFIED`

Required outputs:

1. a precise theorem statement with all residue, primitivity and range hypotheses;
2. an exact proof audit of the signed support localization above `B=(q+1)/6`;
3. an exact proof audit of the `q=23 (mod 24)`, prime-midpoint dangerous-index branch;
4. a conclusion that the marker is captured either at the dangerous earlier defect or at `D_m`, hence no later than `m`;
5. an independent exact-integer recurrence/support falsification scan over a substantial finite prime range, clearly labeled as regression rather than proof;
6. a durable return at `research_returns/P022_OBSERVATION_HISTORY_FORCED_MIDPOINT_FALLBACK_RETURN_20260827.md`;
7. an explicit residue statement that `q>=6r-1` remains open to the already-existing high-range transport route.

## Success, kill, and return criteria

Success requires the general bounded implication to follow from exact integer identities and the frozen owner-local lemmas with no appeal to the finite scan. The finite scan must find zero counterexamples to the stated implication in its declared range.

Narrow or fail the result if any signed-support term above `B` was omitted, if the dangerous index can cancel the midpoint without an earlier positive defect, or if the claimed range equivalence between `r>B` and `q<6r-1` is incorrect. In that event, return the smallest counterexample or missing premise.

The return must preserve the exact high-range residue rather than silently relabeling it solved.

## Research value to preserve

This replay closes a genuine legacy generation without pretending that the entire P022 Franel observability program is complete. It converts a large, historically overgrown owner branch into a sharply bounded theorem with an explicit next frontier: the primitive-twin high range `q>=6r-1` and its fixed-transfer obstructions.

This schema-corrected generation changes only the mandatory publication body headings and role provenance needed by the current control plane; it does not add, delete, strengthen, or weaken the mathematical hard target of the superseded publication.
