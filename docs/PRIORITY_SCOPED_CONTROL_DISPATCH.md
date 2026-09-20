# Ordinary priority-scoped control dispatch

Classification: `NO_NEW_MATHEMATICS / CONTROL_PLANE_MAINTENANCE`
Effective: 2026-09-20
Canonical entrypoint remains `research_control_dispatch.py`.

## Contract

A request to take any P0 task is an ordinary queue constraint, not an exact-task delegation. It must not require a Driver assignment, a user-supplied Task-ID, or a new authorization event merely to select within that priority.

The existing connector request accepts optional `priority`, exactly one of `P0`, `P1`, `P2`, `P3`. Omission preserves existing behavior. Null, empty, unknown or non-string values are rejected by the bridge. Priority filtering and either exact-assignment field are mutually exclusive; the existing assignment-authority checks remain unchanged for genuine exact-task delegations.

Example shape only; use a fresh caller-unique request ID:

```json
{
  "schema": "ENTERPRISE_MATH_CHATGPT_CONTROL_DISPATCH_REQUEST_V1",
  "request_id": "replace-with-fresh-unique-id",
  "kind": "ANY",
  "priority": "P0"
}
```

Local canonical equivalent:

```sh
python research_control_dispatch.py --events actual-issue-240-comments.json --kind ANY --priority P0
```

The CLI requires an explicit event snapshot for priority-scoped routing. The bridge still obtains raw authenticated Issue 240 comments through its existing binding transport. This change adds no workflow, scheduler, role identity, task registry, autonomous executor or background-execution guarantee.

## Selection and authority

The router computes its existing canonical effective-state snapshot, then restricts candidates by their effective `priority` before leased-owner recovery, fresh-task selection and cohort-lane selection. The kind filter still applies. Cohort scope follows the canonical parent task priority.

Within the requested scope, existing recovery-before-fresh behavior, HANDOFF_READY/READY ordering and deterministic tie-breaks remain unchanged. Unfiltered callers are unchanged. No stored task priority, publication, dependency, claim, lease, review, parent objective or mathematical status is rewritten.

A returned `selection_filter` binds kind/priority in the immutable receipt route. The reason explicitly names the scope. Scoped `NO_DISPATCH` means no dispatchable route in that scope at that snapshot, not that the whole queue is empty. Unknown owner liveness remains `VERIFY_SESSION_LIVENESS`. No lower-priority fallback is permitted.

A selected task still requires the existing actual CLAIM/authorization or guarded adoption. The filter never grants execution or mathematical acceptance.

## Verification performed for this change

Base source: `80542befe28c34228acc582492e11a3f84c78a97`.

Before editing, local source bytes were verified against Git blob IDs:
- router: `20c3c778d9255f9dff4702e7f0c345f73f77ed7b`;
- existing bridge: `9be46d9b483192730d142bb9b6c7e98046ed3748`.

Local verification passed:
- 16 source-unit router/CLI tests in `tests/test_priority_scoped_dispatch.py`;
- 15 executions of the actual changed bridge request-validation Bash block, covering omission, P0-P3, malformed values and mixed assignments;
- YAML parsing, all existing workflow Bash blocks through `bash -n`, and Python syntax parsing.

The unit tests execute the actual router and selector function ASTs while mocking repository/event inputs and the liveness leaf. They are not full repository integration, live dispatch, CLAIM acceptance, or a completed P0 research task. Full repository regression was not run in the partial local snapshot. Actual live request/receipt verification must be reported separately.

## Boundary correction

Do not turn a normal priority request into an exceptional exact-task delegation because an older bridge lacks a filter. Repair the ordinary canonical entrypoint. Do not fabricate an assignment, raise a task's priority, remove its gates, or label this maintenance fix as completion of a registered P0 task.
