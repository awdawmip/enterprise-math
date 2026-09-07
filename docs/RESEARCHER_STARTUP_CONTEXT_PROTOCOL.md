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
