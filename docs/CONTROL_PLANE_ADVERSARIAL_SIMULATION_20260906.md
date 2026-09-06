# Control-plane adversarial simulation — 2026-09-06

Status: `CONTROL_MAINTENANCE_EVIDENCE / NO_MATHEMATICAL_AUTHORITY`

This note records focused failure modes reproduced during the 2026-09-06 control-plane repair sequence. It is audit evidence, not a second control authority.

## Reproduced lifecycle failures

The pre-repair registered-task adapter reproducibly allowed four invalid outcomes:

1. an authenticated registered `DONE` rejected for lacking frozen Result + terminal Driver review could later reappear as a permanent provisional block even after the same live claim had resumed with a valid `PROGRESS` and then expired normally;
2. a claimless `SUPERSEDE` carrying a different task publication id could close the current immutable task generation;
3. a claimless `UNBLOCK` carrying a different task publication id could reopen the current immutable task generation;
4. after the V2 task-publication cutover, a publicationless claimless `SUPERSEDE` could still mutate the current generation.

The permanent regression suite in `tests/test_control_plane_adversarial_simulation.py` locks these boundaries while preserving required positive behaviors: pre-cutover publicationless legacy mutations remain replay-compatible, events already bound by a valid live CLAIM need not repeat `publication_id`, valid PROGRESS/HEARTBEAT can recover from an earlier provisional invalid-DONE attempt, and an ignored wrong-claim event cannot.

## Reproduced GitHub Actions request-loss failure

A temporary Actions probe used the same fixed-concurrency shape previously used by the ChatGPT dispatch bridge:

```yaml
concurrency:
  group: control-plane-concurrency-probe
  cancel-in-progress: false
```

Three rapid request-producing commits were then pushed while the first run deliberately remained active. GitHub cancelled the first two request runs and retained only the newest pending request. The observed request commits were:

- `884fc4fd3163388944276c05d5a3baef2de3b4ca` — cancelled;
- `f5044c3c96a52d89fe56a2742fe82b8927ea5f5a` — cancelled;
- `78229b6bd08c5b467dc443713c5c8984a1acd903` — surviving run.

This demonstrates that `cancel-in-progress: false` does not make a shared concurrency group lossless for pending request traffic.

The probe was repeated after switching to a source-SHA-specific concurrency key. Three overlapping requests then all completed successfully:

- `dfa6ecdc4df3373c4d7eb083237b961ae7d34c00` — success;
- `0701035408fb76cf4a179bb00544a1182acd2839` — success;
- `5fb4da39c349468ef9b1ee3168c8cb45ac07f879` — success.

All temporary probe workflows and trigger files were removed after the experiment.

## Reproduced workflow-replay idempotency failure

After immutable per-request receipts were introduced, production acceptance materialized:

```text
control_plane/chatgpt_dispatch_receipts/chatgpt-20260906-1518-task-research-race-rebase-v1.json
```

for request id `chatgpt-20260906-1518-task-research-race-rebase-v1` from source commit `7983c93c3eeda5e4b7c654bc1392d3a77434e7c5`.

The bridge still triggers when its own workflow file changes. Under the initial immutable-receipt implementation, such a workflow-only maintenance push would execute the unchanged current request under a different `source_sha`, encounter the existing `<request_id>.json`, and fail the duplicate-id check even though no new request had been submitted. Therefore workflow maintenance could impersonate request production.

A second edge case was found while designing the guard: testing only `GITHUB_SHA^1..GITHUB_SHA` is insufficient because one push may contain multiple commits, with the request change in an earlier commit and a workflow change in the final commit. Such a real request would be misclassified as replay.

The final guard therefore classifies a push over the complete GitHub event range:

```text
github.event.before .. GITHUB_SHA
```

and grants durable receipt-write authority only when the request file changed somewhere in that range. A workflow-only push still runs the complete live router for validation but cannot write immutable/latest receipts. An invalid/zero `before` value uses first-parent comparison only as a defensive fallback.

Permanent coverage is in `tests/test_chatgpt_dispatch_bridge_replay_guard.py`.

## Repair invariants

The repair sequence freezes these control invariants:

```text
OLD_PUBLICATION_CLAIMLESS_MUTATION != CURRENT_GENERATION_AUTHORITY
POST_V2_CLAIMLESS_MUTATION_WITHOUT_PUBLICATION != AUTHORITY
REJECTED_DONE_WITHOUT_LATER_APPLIED_EVENT -> PROVISIONAL_FAIL_CLOSED
REJECTED_DONE_WITH_LATER_APPLIED_SAME_CLAIM_CONTINUATION != PERMANENT_BLOCK
IGNORED_WRONG_CLAIM_EVENT != RECOVERY
EVERY_CHATGPT_REQUEST_COMMIT -> INDEPENDENT_WORKFLOW_RUN
EVERY_COMPLETED_CHATGPT_REQUEST -> IMMUTABLE_RECEIPT
STALE_REQUEST_RUN != LATEST_RECEIPT_OVERWRITE_AUTHORITY
WORKFLOW_UPGRADE != NEW_REQUEST
REQUEST_FILE_UNCHANGED_IN_PUSH_RANGE -> VALIDATION_REPLAY_ONLY
REQUEST_FILE_CHANGED_ANYWHERE_IN_PUSH_RANGE -> REQUEST_PRODUCING
VALIDATION_REPLAY != DURABLE_RECEIPT_WRITE_AUTHORITY
RECEIPT != CLAIM
```

The canonical semantic authority remains `research_control_dispatch.py` over the authenticated Issue #240 event stream.