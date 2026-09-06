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

Reusing the same `request_id` for a different source commit fails closed. The path-safe restriction is part of the transport contract because the request id names the immutable receipt file.

`session_observations` is optional. If supplied, it must already satisfy the exact owner-scope liveness contract accepted by `research_control_dispatch.py`. Generic conversation activity must never be converted into an observation by this bridge.

## Execution contract

For each relevant request-producing push to `main`, the workflow:

1. gives that exact source commit an independent workflow concurrency key, so a newer request cannot replace an older pending request;
2. fetches every current raw comment from GitHub Issue #240 using GitHub's server response;
3. preserves the raw comment objects so `tools/research_dispatch.py` performs its existing server-envelope authentication and authorization checks;
4. runs the checked-out repository's current `research_control_dispatch.py` with that raw event snapshot;
5. accepts router exit code `0` or the canonical `NO_DISPATCH` exit code `2`;
6. records the request id, source commit, immutable receipt path, Issue #240 comment count, last comment id, comment-snapshot SHA-256, router exit code, and exact router JSON;
7. persists the request result at `control_plane/chatgpt_dispatch_receipts/<request_id>.json` using a fresh-main retry loop;
8. updates `control_plane/chatgpt_dispatch_receipt.json` only if `control_plane/chatgpt_dispatch_request.json` on the freshly fetched `main` still names the same request id.

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

The per-request receipt layer additionally prevents connector sessions from depending on a mutable single latest-output file when multiple requests overlap. It is transport durability only; all semantic routing authority remains with the canonical router and its current repository contracts.
