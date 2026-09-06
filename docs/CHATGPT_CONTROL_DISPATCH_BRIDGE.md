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
-> DURABLE_RECEIPT_ON_MAIN
```

It does not replace the canonical router and does not introduce a second task selector.

## Files

Request trigger:

```text
control_plane/chatgpt_dispatch_request.json
```

Latest receipt:

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

`session_observations` is optional. If supplied, it must already satisfy the exact owner-scope liveness contract accepted by `research_control_dispatch.py`. Generic conversation activity must never be converted into an observation by this bridge.

## Execution contract

For each relevant push to `main`, the workflow:

1. fetches every current raw comment from GitHub Issue #240 using GitHub's server response;
2. preserves the raw comment objects so `tools/research_dispatch.py` performs its existing server-envelope authentication and authorization checks;
3. runs the checked-out repository's current `research_control_dispatch.py` with that raw event snapshot;
4. accepts router exit code `0` or the canonical `NO_DISPATCH` exit code `2`;
5. records the source commit, Issue #240 comment count, last comment id, comment-snapshot SHA-256, router exit code, and exact router JSON in the receipt;
6. persists only the latest transport receipt. The receipt is not a CLAIM or a runtime event.

## Authority boundaries

Freeze:

```text
BRIDGE_OUTPUT != CLAIM
BRIDGE_OUTPUT != RESULT
BRIDGE_OUTPUT != REVIEW
BRIDGE_OUTPUT != MATHEMATICAL_AUTHORITY
REQUEST_WRITE != TASK_CLAIM
RAW_ISSUE_240_SERVER_COMMENTS -> EXISTING_AUTHORIZATION_FILTER
CANONICAL_ROUTER_REMAINS research_control_dispatch.py
EMPTY_OR_OMITTED_RUNTIME_EVENT_STREAM != LIVE_DISPATCH_VIEW
VERIFY_SESSION_LIVENESS != NO_DISPATCH
```

The bridge never creates or releases a GitHub CLAIM, never changes owner-lease semantics, never invents a Researcher-ID, never promotes mathematics, and never treats the receipt as task authority.

If the returned action is:

- `CLAIM_NEW_OWNER`: follow the existing current CLAIM publication protocol before research starts;
- `ADOPT_OWNER_CLAIM`: preserve the winning claim and use the existing runtime adoption guard;
- `VERIFY_SESSION_LIVENESS`: obtain exact owner-scope evidence, then submit a new request carrying only valid observations;
- `NO_DISPATCH`: report canonical no-dispatch for that exact receipt snapshot.

## Why this exists

`research_control_dispatch.py` accepts an optional `--events` path. The underlying canonical event loader intentionally treats an omitted path as an empty event stream and otherwise accepts only raw authenticated Issue #240 comment objects. Therefore a connector-only caller must not run or mentally emulate the router without first materializing the live Issue #240 server-comment stream. This bridge makes that prerequisite mechanical and auditable.
