# ChatGPT control-dispatch bridge

Status: `CONTROL_PLANE_TRANSPORT / NO_NEW_MATHEMATICS / NO_CLAIM_AUTHORITY`

## Purpose

Provide a deterministic GitHub transport for ChatGPT sessions that have the managed GitHub connector but cannot directly execute repository Python or invoke the self-hosted Supervisor MCP.

The bridge closes exactly one transport gap:

```text
MANAGED_GITHUB_CONNECTOR
-> REQUEST_FILE_PUSH
-> RAW_GITHUB_ISSUE_240_COMMENT_SNAPSHOT
-> research_control_dispatch.py
-> IMMUTABLE_REQUEST_RECEIPT_ON_MAIN
-> LATEST_COMPATIBILITY_RECEIPT_WHEN_STILL_CURRENT
```

It does not replace the canonical router and does not introduce a second task selector.

## Files

Request trigger:

```text
control_plane/chatgpt_dispatch_request.json
```

Immutable receipt for each completed request:

```text
control_plane/chatgpt_dispatch_receipts/<request_id>.json
```

Latest compatibility receipt:

```text
control_plane/chatgpt_dispatch_receipt.json
```

Workflow:

```text
.github/workflows/chatgpt-control-dispatch-bridge.yml
```

## Request contract

```json
{
  "schema": "ENTERPRISE_MATH_CHATGPT_CONTROL_DISPATCH_REQUEST_V1",
  "request_id": "caller-unique-id",
  "kind": "RESEARCH",
  "session_observations": {
    "schema": "ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2",
    "observations": []
  }
}
```

`kind` is one of `RESEARCH`, `GOVERNANCE`, or `ANY`.

`request_id` is a caller-unique durable receipt key and must match:

```text
[A-Za-z0-9][A-Za-z0-9._-]{0,127}
```

A real request-producing push must use a fresh `request_id`. Reusing an already-materialized id from a different request-producing source fails closed. A workflow-only validation replay is not a new request and therefore has no durable receipt-write authority at all; it may execute the router for validation but cannot collide with or replace the existing immutable receipt.

`session_observations` is optional. If supplied, it must already satisfy the exact owner-scope liveness contract accepted by `research_control_dispatch.py`. Generic conversation activity must never be converted into an observation by this bridge.

### Explicit assignment of a registered line-Driver GOV task

An Owner may delegate an exact registered governance task to an activated Driver
through this same canonical router. This bounded entry covers dependency-free,
task-global `GOVERNANCE` publications. Ordinary priority selection is unchanged.
Nonempty dependency models, blocked or closed tasks, non-open parent gates,
cohort lanes and pending Result reviews cannot use this entry to bypass their gates.

The current source-backed `AUTHORIZE` event must contain the typed field
`assigned_governance_task` with exactly `task_id`, `publication_id` and
`parent_objective_id`. Its existing immutable DA record preserves the whole
authenticated `source_body`. The event's `driver_id` identifies the delegate.
Reason prose is not parsed as a grant, and the request below cannot grant its own
delegation. A new real AUTHORIZE may record an already explicit Owner delegation
prospectively; retain all older DA/CLAIM/ER and omitted-selection evidence.

Add an `assigned_driver_task` object to the existing V1 connector request with
`kind: "GOVERNANCE"`. No new request path or second task registry is needed:

```json
{
  "schema": "ENTERPRISE_MATH_ASSIGNED_GOVERNANCE_DRIVER_REQUEST_V1",
  "driver_id": "EM-DVR-EXAMPLE",
  "task_id": "GV-EXAMPLE",
  "publication_id": "TP2-EXAMPLE",
  "parent_objective_id": "OBJ-EXAMPLE",
  "driver_authority_record_id": "DA-EXAMPLE",
  "driver_authority_record_sha256": "sha256:EXACT_CURRENT_DA_FILE_DIGEST",
  "expected_claim_id": null,
  "session_id": "actual-calling-session"
}
```

The example IDs are structural examples, not live authority. Use exact current
values. Local execution accepts the same object through
`research_control_dispatch.py --events <actual-issue-240-snapshot.json> --kind GOVERNANCE --assigned-driver-task <request.json>`
or `--assigned-driver-task-json`. The bridge always supplies the current raw
server-comment stream and includes validated assignment provenance in both the
immutable receipt and the compact packet, retaining its 8192-byte limit.

For an unowned target, `expected_claim_id` is explicitly null. A returned
`CLAIM_NEW_OWNER` still requires the existing execution-intent/real-CLAIM/runtime
authorization sequence. A route is not execution authority.

For the same Driver's existing winning owner, supply its exact `expected_claim_id`;
the current claim, ER and owner lease are preserved. `KEEP_CURRENT_SESSION`
requires an existing supported activity kind bound to that exact task/claim and
an explicit matching `session_id` in the session observation. Missing/foreign
session evidence returns `VERIFY_SESSION_LIVENESS`. Independently stale evidence
returns `ADOPT_OWNER_CLAIM` and still requires the existing adoption guard. Generic
Driver activity, claim creation and control publication do not refresh task
liveness. The receipt marks this as current forward revalidation, never as a
reconstructed pre-claim selector result. No route closes a parent objective or
grants mathematical acceptance, Working Truth or Foundation authority.

## Request-producing push

For a `push` event, the bridge defines request production mechanically over the complete GitHub push range:

```text
github.event.before .. GITHUB_SHA
```

If `control_plane/chatgpt_dispatch_request.json` changed anywhere in that range, the run is request-producing and may persist a receipt. This range check is intentionally not limited to `GITHUB_SHA^1`, because one GitHub push may contain multiple commits and the request change may occur before the final commit. A zero/invalid `before` value uses the first parent only as a defensive fallback.

If the request file did not change anywhere in the push range, the run is a validation replay. This is the expected mode when the bridge workflow itself is upgraded while the current request remains unchanged.

Freeze:

```text
REQUEST_FILE_CHANGED_IN_PUSH_RANGE -> MAY_PERSIST_REQUEST_RECEIPT
REQUEST_FILE_UNCHANGED_IN_PUSH_RANGE -> VALIDATION_REPLAY_ONLY
WORKFLOW_UPGRADE != NEW_REQUEST
VALIDATION_REPLAY != IMMUTABLE_RECEIPT_WRITE_AUTHORITY
```

## Execution contract

For every matching workflow run, the bridge still validates the request envelope, fetches the full current Issue #240 server-comment stream, executes the checked-out `research_control_dispatch.py`, accepts canonical router exit code `0` or `2`, and builds a deterministic temporary receipt.

Only for a request-producing push, the workflow additionally:

1. gives that source commit an independent workflow concurrency key, so a newer request cannot replace an older pending request;
2. persists the request result at `control_plane/chatgpt_dispatch_receipts/<request_id>.json` using a fresh-main retry loop;
3. fails closed if that request id already belongs to a different request-producing source;
4. updates `control_plane/chatgpt_dispatch_receipt.json` only if the freshly fetched main request still names the same request id.

The immutable per-request receipt makes every completed request individually recoverable. The latest compatibility receipt is only a convenience pointer; a slow older run is explicitly forbidden from overwriting it after a newer request has become current.

GitHub Actions permits at most one running and one pending job for a single concurrency group; a later pending run may replace an earlier pending run even when `cancel-in-progress` is false. Therefore the bridge MUST NOT use one fixed concurrency group for all ChatGPT requests. Its concurrency key is source-commit-specific.

Receipt-only commits do not match the workflow's push path filter and therefore do not recursively trigger another dispatch run.

## Authority boundaries

Freeze:

```text
BRIDGE_OUTPUT != CLAIM
BRIDGE_OUTPUT != RESULT
BRIDGE_OUTPUT != REVIEW
BRIDGE_OUTPUT != MATHEMATICAL_AUTHORITY
REQUEST_WRITE != TASK_CLAIM
IMMUTABLE_RECEIPT != TASK_CLAIM
LATEST_RECEIPT != TASK_CLAIM
RAW_ISSUE_240_SERVER_COMMENTS -> EXISTING_AUTHORIZATION_FILTER
CANONICAL_ROUTER_REMAINS research_control_dispatch.py
EMPTY_OR_OMITTED_RUNTIME_EVENT_STREAM != LIVE_DISPATCH_VIEW
VERIFY_SESSION_LIVENESS != NO_DISPATCH
```

The bridge never creates or releases a GitHub CLAIM, never changes owner-lease semantics, never invents a Researcher-ID, never promotes mathematics, and never treats any receipt as task authority.

If the returned action is:

- `CLAIM_NEW_OWNER`: follow the existing current CLAIM publication protocol before research starts;
- `ADOPT_OWNER_CLAIM`: preserve the winning claim and use the existing runtime adoption guard;
- `VERIFY_SESSION_LIVENESS`: obtain exact owner-scope evidence, then submit a new request carrying only valid observations;
- `NO_DISPATCH`: report canonical no-dispatch for that exact receipt snapshot.

## Why this exists

`research_control_dispatch.py` accepts an optional `--events` path. The underlying canonical event loader intentionally treats an omitted path as an empty event stream and otherwise accepts only raw authenticated Issue #240 comment objects. Therefore a connector-only caller must not run or mentally emulate the router without first materializing the live Issue #240 server-comment stream. This bridge makes that prerequisite mechanical and auditable.

The per-request receipt layer additionally prevents connector sessions from depending on a mutable single latest-output file when multiple requests overlap. The replay guard prevents workflow maintenance from impersonating request production. Both are transport durability only; all semantic routing authority remains with the canonical router and its current repository contracts.
