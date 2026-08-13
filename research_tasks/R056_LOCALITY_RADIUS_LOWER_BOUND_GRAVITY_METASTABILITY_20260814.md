<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R056-LOCALITY-RADIUS-LOWER-BOUND-GRAVITY-METASTABILITY",
  "title": "R056 — Locality-Radius Lower Bounds for Fixed-N Gravity Metastability",
  "kind": "MATHEMATICAL_RESEARCH",
  "owner": "program/fixed-n-gravity-locality-obstruction",
  "base_state": "NEW_GENERATION_AFTER_R055_D1_METASTABILITY",
  "priority": "P0",
  "leverage": "LOCALITY_LOWER_BOUND / METASTABILITY_NO_GO / MINIMAL_COOPERATIVE_ESCAPE",
  "frontier": "Determine whether every fixed bounded-support strict-descent cooperative rearrangement is eventually trapped by the centered-shell family, or whether a finite local cooperative rule escapes R055 metastability at arbitrarily large shell radius.",
  "next_action": "Freeze the locality model, shell-escape protocol and computation registry; return all three hashes before heavy search; prove the exact multi-replacement energy identity; then attack the bounded-support obstruction theorem before bounded construction and holdout search.",
  "dependencies": [
    {
      "target": "research_inputs/R056_LOCALITY_RADIUS_LOWER_BOUND_GRAVITY_METASTABILITY_PACKET_20260814.md @ 67ec92f83bc8cb401e0a86170081daa137ea24a5",
      "action": "CONSUME_AS_FROZEN_PROBLEM_PACKET",
      "satisfied": true
    },
    {
      "target": "R055 full-workspace evidence @ ea0781f564b8c4016d592521a50c02888e2f371d",
      "action": "READ_ONLY_VERIFY_REQUIRED_ANCHORS; DO_NOT_MUTATE_R055",
      "satisfied": true
    }
  ],
  "evidence_status": "LOCALITY_BARRIER_RESEARCH_AFTER_R055_METASTABILITY",
  "hard_block": null,
  "tags": ["R056","fixed-N","gravity-relaxation","locality-radius","cooperative-moves","metastability","strict-descent"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R056",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R056 — Locality-Radius Lower Bounds for Fixed-N Gravity Metastability

Status: `READY / P0 / NEW GENERATION / NOT CANONICAL`

## Mother question

R055 proved an infinite family of centered-shell traps for the one-cell nearest-neighbor strict-descent law. R056 determines whether that failure persists for **every fixed bounded-support cooperative strict-descent move class**, or whether a finite local cooperative rule can escape at arbitrarily large shell radius.

Use the frozen packet as the complete mathematical specification.

## Stage 0 — freeze first

Before heavy search create, freeze and return:

- `R056_LOCALITY_MODEL_SHA256`
- `R056_SHELL_ESCAPE_PROTOCOL_SHA256`
- `R056_COMPUTATION_REGISTRY_SHA256`

No expensive cooperative enumeration before these hashes are returned.

## Stage A — exact algebra

Prove/check the packet's exact multi-replacement `DeltaG` identity and its centered-shell reduction. Record all equality cases needed for the obstruction proof, especially `DeltaQsum=0`.

## Stage B — theorem first

Primary target:

`BOUNDED_SUPPORT_STRICT_DESCENT_OBSTRUCTION`.

Attempt to prove that for every fixed finite `(m,rho)`, sufficiently large centered shells admit no strictly `G`-decreasing admissible `D(m,rho)` move.

Preferred strengthening: prove `rho_m(r)->infinity`, ideally with an explicit linear lower bound in `r` for each fixed `m`.

If false, return an exact counterexample family and classify the smallest finite local cooperative escape class actually established.

## Stage C — bounded exact search

Use only the construction radii and cooperative caps frozen in the packet. Derive geometric pruning before subset enumeration. For `m=1`, extend exact `rho_1(r)` substantially further when cheap. For `m>=2`, keep search bounded and exact.

Finite search is evidence/counterexample discovery, not a replacement for an all-scale theorem.

## Stage D — freeze theorem status

Before strict holdout freeze and return:

`R056_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256`.

The ledger must separately classify the multi-replacement identity, eventual bounded-local trapping, divergence/lower bounds for `rho_m(r)`, finite-local escape, and any exact `rho_1(r)` law.

## Stage E — strict holdout

Open only the packet's frozen holdout radii. Do not change the move semantics, cooperative caps, search conventions or theorem statement after holdout.

## Primary return classification

Return exactly one:

- `BOUNDED_SUPPORT_STRICT_DESCENT_OBSTRUCTION_PROVED`;
- `FINITE_LOCAL_COOPERATIVE_ESCAPE_FOUND`;
- `LOCALITY_BARRIER_OPEN_WITH_EXACT_BOUNDED_EVIDENCE`.

If bounded strict locality is obstructed, do **not** introduce plateau/uphill dynamics inside R056; that is a later generation.

## Deliverables

Return every artifact required by the frozen packet, exact checker/tests, and finally:

`R056_ARTIFACT_MANIFEST_SHA256`.

The main deliverable is the locality theorem/counterexample. If enumeration becomes combinatorially expensive, checkpoint the exact completed region and continue the proof route rather than expanding the sweep.
