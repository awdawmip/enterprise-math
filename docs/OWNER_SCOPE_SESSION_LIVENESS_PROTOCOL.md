# Owner-Scope Session Liveness Protocol

Status: `ACTIVE / CHAT-ONLY OWNER-SCOPE LIVENESS / V1`
Effective: `2026-08-28`
Classification: `NO_NEW_MATHEMATICS`
Machine contract: `research_dispatch_contract.json`
Canonical router: `research_control_dispatch.py`
Role transitions: `control_plane/role_transition_matrix.json`

## 1. Purpose

Enterprise Math distinguishes three facts:

`OWNER_LEASE`

`!= CONVERSATION_ACTIVITY`

`!= OWNER_SCOPE_SESSION_LIVENESS`.

A chat may still be active while the exact Researcher execution it once owned is suspended, abandoned, switched to control maintenance, switched to Driver/Steward/FREE, or working on a different task. Generic chat activity must not keep an unrelated Researcher CLAIM leased indefinitely.

This protocol defines how a chat-only control agent supplies the ephemeral V2 liveness observations consumed by `research_control_dispatch.py`.

## 2. Exact owner scope

An ordinary owner scope is identified by:

- exact `task_id`;
- exact current winning `claim_id`.

A cohort-lane owner scope additionally requires:

- `execution_cohort_id`;
- `execution_lane_id`.

The activity timestamp has authority only for that exact scope.

## 3. Allowed evidence

`ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2` accepts only:

### `TASK_RESEARCH_RESPONSE`

A latest independently verified assistant response that can be bound to continued `TASK_RESEARCH` under the exact current winning claim/scope.

The evidence need not repeat the claim ID in prose when the conversation-to-claim binding is independently known, but the observation supplied to the router must pin the exact current `claim_id`.

### `DURABLE_EXECUTION_PROGRESS`

A verified durable task/execution frontier change produced under the exact current claim/scope, such as an authorized checkpoint/result/output/commit that genuinely advances that execution.

A status poll or unrelated repository change is not durable execution progress.

## 4. Evidence that does not count

Do not refresh a task owner scope from:

- CLAIM creation time alone;
- a `CONTROL_PLANE_MAINTENANCE` reply;
- a Driver reply while not executing the exact task under TASK_RESEARCH;
- a Foundation Steward reply while not executing the exact task under TASK_RESEARCH;
- a FREE discovery reply;
- a reply about another task or another cohort lane;
- generic “still working” text with no verified binding to exact owner execution;
- CI/status polling without durable task progress;
- a response bound to an old/foreign `claim_id`.

Freeze:

`CHAT_IS_ACTIVE != CLAIM_EXECUTION_IS_ACTIVE`.

`ROLE_SWITCH_AWAY_FROM_TASK -> DESTINATION_MESSAGES_DO_NOT_REFRESH_TASK_LIVENESS`.

## 5. Chat-only observation procedure

When canonical dispatch needs liveness evidence for a valid leased owner scope:

1. resolve the current winning claim/scope from canonical runtime authority;
2. identify the latest independently visible activity that genuinely belongs to that exact execution;
3. if the conversation changed role after that activity, ignore later destination-role messages for this task liveness clock;
4. if the latest valid evidence is older than the configured stale threshold, route stale adoption;
5. if exact evidence cannot be verified, leave liveness **unknown** rather than guessing active;
6. if another fresh task/lane exists, unknown ownership of one scope does not block independent fresh dispatch;
7. when no fresh target exists and exact owner liveness is unknown, return `VERIFY_SESSION_LIVENESS`, not `NO_DISPATCH`.

Do not poll another conversation repeatedly. Verify only when stale adoption is being considered or a valid lease would otherwise cause a false terminal dispatch result.

## 6. Observation payload

Example ordinary task response:

```json
{
  "schema": "ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2",
  "observations": [
    {
      "task_id": "RS-EXAMPLE",
      "claim_id": "CLM-EXAMPLE",
      "activity_evidence_kind": "TASK_RESEARCH_RESPONSE",
      "last_verified_activity_at": "2026-08-28T15:00:00+00:00"
    }
  ]
}
```

Example cohort lane durable progress:

```json
{
  "schema": "ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2",
  "observations": [
    {
      "task_id": "RS-EXAMPLE",
      "execution_cohort_id": "COH-1",
      "execution_lane_id": "LANE-A",
      "claim_id": "CLM-EXAMPLE-LANE-A",
      "activity_evidence_kind": "DURABLE_EXECUTION_PROGRESS",
      "last_verified_activity_at": "2026-08-28T15:00:00+00:00"
    }
  ]
}
```

`claim_id` mismatch is ignored as liveness evidence; it cannot keep the current winner active.

## 7. Role-switch examples

### TASK -> CONTROL

Last TASK response at 10:00; control maintenance continues until 10:30.

For the task owner scope, the last activity remains **10:00**. Control messages do not reset it to 10:30.

### TASK -> DRIVER

A Driver review at 10:20 does not refresh a suspended Researcher CLAIM. Driver authority and task-execution liveness are separate facts.

### TASK -> FREE

FREE activity does not refresh the old TASK claim. The same conversation is also `ANCHOR_EXPOSED` for blind FREE provenance.

### CONTROL -> TASK

Do not inherit control-message timestamps. Recompute the exact current claim and resume/adopt it only through canonical runtime rules.

## 8. Adoption

When the exact owner execution is stale but the owner lease remains valid:

`STALE OWNER SCOPE + VALID CLAIM`

`-> ADOPT EXISTING WINNING CLAIM`

`-> NO SECOND CLAIM`

`-> VERIFY DURABLE FRONTIER`

`-> RESUME FIRST UNFINISHED UNIT`.

The stale conversation does not release the owner claim merely by becoming stale; replacement adopts the same authority.
