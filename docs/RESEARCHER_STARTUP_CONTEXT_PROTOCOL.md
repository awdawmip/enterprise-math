# Researcher startup context protocol

Status: `ACTIVE / CONTROL-PLANE / NO_NEW_MATHEMATICS`
Schema: `ENTERPRISE_MATH_RESEARCHER_COLD_START_ENVELOPE_V1`

## Problem

A fresh TASK_RESEARCH conversation must not spend most of its usable context on repeated governance text before mathematical work begins. The previous static context checker only measured selected repository policy files and explicitly did not measure global-knowledge input, connected-tool output, dynamic task packets, or product tokenization. That checker remains useful but is not an end-to-end cold-start proof.

## Canonical compact packet

Every request-producing ChatGPT canonical dispatch bridge run now builds one immutable packet:

`control_plane/chatgpt_startup_packets/<request_id>.json`

Schema:

`ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1`

The packet is a source-pinned projection of the exact immutable dispatch receipt and exact immutable task publication. It is **not** a claim, Result, review, theorem, Working Truth, or mathematical authority.

Freeze:

`COMPACT_STARTUP_PACKET != TASK_CLAIM`.

`COMPACT_STARTUP_PACKET != MATHEMATICAL_AUTHORITY`.

`FULL_DISPATCH_RECEIPT = DIAGNOSTIC_SURFACE_NOT_ORDINARY_STARTUP_CONTEXT`.

`CURRENT_CONTROL_AUTHORITY_FULL_READ = TRIGGERED_CONTROL_DIAGNOSTIC_NOT_ORDINARY_TASK_START`.

## Task projection

When a dispatch target exists, the builder:

1. resolves the exact immutable publication at `research_task_records/<task-id>/<publication-id>.json`;
2. resolves its exact `taskbook_path`;
3. verifies the current taskbook bytes against `taskbook_blob_sha1`;
4. extracts only these authoritative sections when all are present:
   - Mother question;
   - Frozen inputs and scope;
   - Hard target and required outputs;
   - Research value to preserve;
   - Success, kill, and return criteria;
5. inlines that exact projection only if the complete startup packet remains within the hard packet budget.

If the exact projection is too large, the builder omits it entirely and tells the consumer to fetch the exact taskbook. It never truncates or paraphrases task semantics merely to satisfy the context budget.

## First dependency

The startup packet may include one `first_dependency_ref` only when an exact repository path can be resolved without directory discovery. Preferred evidence is:

1. an explicit future `startup_read_plan.first_dependency_ref` in the immutable publication;
2. an exact durable-frontier path from `last_progress_ref`;
3. an exact unsatisfied dependency path;
4. an exact source-ref path.

If none is exact, the value is null. A null dependency does **not** authorize directory enumeration. After understanding the task, use bounded targeted search (`topn <= 20`) and then exact-file reads.

Freeze:

`UNKNOWN_FIRST_DEPENDENCY != DIRECTORY_ENUMERATION_AUTHORITY`.

## Ordinary new-researcher hot path

The intended path is:

`GLOBAL_BOOTSTRAP -> ENTERPRISE_TASK_BOOTSTRAP -> P000 -> HOST_INJECTED_AGENTS_IF_PRESENT -> EXACT_COMPACT_STARTUP_PACKET -> INLINE_TASK_PROJECTION_OR_EXACT_TASKBOOK -> FIRST_EXACT_DEPENDENCY_IF_NEEDED -> SUBSTANTIVE_RESEARCH`.

Ordinary startup must not remotely fetch `AGENTS.md` merely for task start. It must not load the full dispatch receipt, full current-control-authority JSON, full Issue #240 stream, recursive repository tree, or high-fanout task/result directories unless a concrete diagnostic condition makes that surface necessary.

## Produce and consume one current request

For a connector-only TASK_RESEARCH conversation, use the managed GitHub connector
to read the current `main` blob of `control_plane/chatgpt_dispatch_request.json`,
then update that exact path with optimistic concurrency using this minimal JSON:

```json
{
  "schema": "ENTERPRISE_MATH_CHATGPT_CONTROL_DISPATCH_REQUEST_V1",
  "request_id": "chatgpt-20260908T000000Z-0123456789abcdef",
  "kind": "RESEARCH"
}
```

Replace the example ID with a fresh timestamp/random suffix for this request;
never submit the literal example or reuse an already materialized ID. The full
ID must match `[A-Za-z0-9][A-Za-z0-9._-]{0,127}`. `kind` accepts `RESEARCH`,
`GOVERNANCE`, or `ANY`; an ordinary researcher uses `RESEARCH`. The optional
`session_observations` field is omitted on a fresh start. Add it only when actual
owner-scope evidence satisfies the existing V2 liveness contract, never to turn
an unknown conversation into a stale owner or to invent identity/claim evidence.

Both an authorized direct-main write and a branch/PR merge are valid publication
routes. A request becomes durable bridge input when its change reaches `main`;
a PR validation run alone does not persist the request packet. Refresh the
actual write target and use its expected head/blob before the write or merge.
On a concurrent-write rejection, re-read that exact target and retry with a fresh
guard, preserving other writers' changes. Do not create a second scheduler.

Record the request ID and the actual request-producing main commit. The existing
`.github/workflows/chatgpt-control-dispatch-bridge.yml` executes the canonical
router and persists this exact output path:

`control_plane/chatgpt_startup_packets/<request_id>.json`

Read that one packet, verifying schema
`ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1`, the exact `request_id`, and
`source_sha` against the request-producing main commit. Read the supplied task
projection or exact pinned taskbook, then the first exact dependency if needed.
Do not substitute the mutable latest receipt or another request's packet. A
packet missing immediately after request publication may be pending: inspect
only that request's bridge run when needed and retain the exact request key.
Do not issue duplicate requests or poll unrelated CI. A successful workflow is
transport evidence; the packet's typed `action` still decides the next step.

| Packet `action` | Required next step |
| --- | --- |
| `CLAIM_NEW_OWNER` | Follow the current CLAIM protocol for the exact publication and any lane; refresh live claim authority before the write and verify the winning claim before mathematical execution. The packet itself is not a claim. |
| `ADOPT_OWNER_CLAIM` | Preserve the exact winning claim, task/publication and lane, verify its durable frontier, and use the existing runtime adoption guard. Do not create a replacement claim. |
| `VERIFY_SESSION_LIVENESS` | Obtain only the required exact owner-scope evidence. Submit a fresh request with valid V2 observations when evidence exists; report the precise missing evidence otherwise. This action is not `NO_DISPATCH`. |
| `NO_DISPATCH` | Report no dispatch for this exact request/source snapshot. Do not infer permanent queue exhaustion or scan the queue manually. |

An unknown action, mismatched request/source, or missing identity/publication/lane
binding needed for the returned action is a bounded diagnostic, not permission
to guess a task or manufacture authority. The exact immutable receipt named by
the packet is then a triggered diagnostic surface. Request IDs identify
transport attempts, not Researcher-IDs. Existing research identity, CLAIM,
runtime, frozen-input and mathematical-admission rules continue to apply.

## Cached legacy-path 404 recovery

If an older conversation attempts the root `research_task_registry.json` and
receives 404, do not treat that absence as an empty queue or a failed current
dispatcher. Perform one bounded control rebase:

1. Resolve fresh canonical global-knowledge `main` and its current Enterprise
   Math TASK bootstrap; resolve fresh Enterprise Math `main` and read this exact
   startup protocol from that same source snapshot. Record the resolved SHAs;
   a cached SHA remains historical provenance, not a freshness check.
2. If the current entry uses the request/compact-packet path above, classify the
   missing legacy registry as a stale entry reference. Do not recreate it,
   search for an alternate V1 registry, or enumerate task directories/Issue #240.
3. Continue in the same conversation with the canonical request above, or consume
   this conversation's already-published exact request packet. Preserve an
   existing winning owner claim and durable unfinished frontier; recovery never
   grants a new claim or authorizes replay of completed mathematics.

This exception is triggered by the old-path failure; it does not add an extra
diagnostic preload to ordinary startup. A 404 for a currently required request,
packet, publication or taskbook is a different failure: check only the exact
repository/ref/path and connector response, distinguishing a pending packet,
stale ref, access/endpoint failure or genuine source-integrity mismatch. If the
required current source cannot be read or verified, report that concrete
blocker and the preserved request/frontier. Do not repeat the same lookup,
rebuild the legacy control plane, or label every 404 as harmless.

## Budgets

Canonical component ceilings are in `research_context_budget.json`.

- compact startup packet hard max: `8192` bytes;
- ordinary remote source reads before substantive mathematics: `<= 2`;
- aggregate raw cold-start soft target: `<= 65536` bytes;
- aggregate raw cold-start hard envelope: `<= 81920` bytes.

The hard component ceilings sum below the aggregate hard envelope. This is a raw-byte guard, not a claim about provider tokenization. Product/runtime token measurement remains a separate platform concern.

## Bridge persistence and concurrency

The compact packet is persisted in the same request-producing transaction as the immutable dispatch receipt. It has no mutable `latest` pointer. Consumers use the exact request ID.

A workflow-only replay still performs live routing and packet construction for validation, but it has no durable receipt/packet write authority. A request ID that already owns a receipt must also own a matching startup packet after this protocol's cutover; an orphan or mismatched packet fails closed.

## Validation

`control_plane/check_context_budget.py` validates the static policy plus the component-level cold-start envelope.

`tests/test_researcher_startup_packet.py` covers exact projection, large-task fallback, digest mismatch, and no-target routes.

`tests/test_researcher_startup_context_envelope.py` runs the packet builder against the repository's current real dispatch receipt and verifies that diagnostic bulk fields do not leak into the compact packet.

`.github/workflows/researcher-startup-context-validation.yml` is the permanent gate.
