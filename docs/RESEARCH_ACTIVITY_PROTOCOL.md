# Research activity registration

This is owner bookkeeping for direct research and FREE Phase A. It does not
register a formal task, claim, Result, review, Working Truth, or mathematical
acceptance. FREE registration requires no question and opens no research catalog.
Formal task execution keeps its existing publication/claim/firewall gates.

The executable schema is in [`tools/research_activity.py`](../tools/research_activity.py);
[`research_persistence_policy.json`](../research_persistence_policy.json) owns the
checkpoint persistence requirement. This protocol does not replace either.

## Start, including a connector-only ChatGPT host

With local execution, run:

```text
python tools/research_activity.py register --mode FREE_AXIOM_DISCOVERY --session-id <stable-actual-session-key> --researcher-id <resolved-Researcher-ID>
```

For ordinary direct research use `--mode TASK_RESEARCH`. No Task ID or topic is
required. The command creates only a local record and returns its path/hash plus
the required publication action. It does not publish to GitHub.

A connector-only host can create the following equivalent JSON directly at
`research_activity_records/<activity_id>.json` through managed GitHub. Replace
every placeholder with a real current value; choose one fresh `RA-` ID with an
8–96 character alphanumeric/underscore/hyphen suffix and reuse it for retries.
Use the same stable session key throughout this activity. Do not invent a
ChatGPT server session ID: a locally assigned stable key must be described as
such when handed off. The timestamp is the current registration observation
time, not an invented earlier start time.

```json
{
  "schema": "ENTERPRISE_MATH_RESEARCH_ACTIVITY_V1",
  "activity_id": "RA-<fresh-unique-suffix>",
  "registration_key": "session:<actual-stable-session-key>:FREE_AXIOM_DISCOVERY",
  "registration_origin": {"kind": "LIVE_SESSION", "source_tracking_key": null},
  "mode": "FREE_AXIOM_DISCOVERY",
  "researcher_id": "<resolved-Researcher-ID>",
  "session_id": "<actual-stable-session-key>",
  "session_state": "KNOWN",
  "recorded_at": "<current-ISO8601-time-with-timezone>",
  "authority": {
    "task_registration": false,
    "claim": false,
    "review": false,
    "working_truth": false,
    "mathematical_acceptance": false
  },
  "checkpoints": []
}
```

Persist this unique file to EM before substantive research and obtain the full
file at the returned immutable commit. Match the exact content and returned Git
blob. A permitted direct-main CAS write is a lightweight option; a PR/CI wait is
not an activity-registration prerequisite. A source-branch record is remotely
persisted but not automatically visible in canonical main: give owner its exact
link and retain the pending intake distinction. Local files, KB identity entries,
and an unverified `published=true` do not establish remote registration.

For retrospective capture, keep the same complete schema but use
`registration_origin={"kind":"RETROSPECTIVE_SOURCE","source_tracking_key":"<exact-source-derived-key>"}`,
`registration_key="source:<same-exact-source-derived-key>"`, `session_id=null`,
and `session_state="UNKNOWN"`. Use `mode="UNKNOWN_RESEARCH"` and
`researcher_id=null` if the old source does not establish them. The CLI equivalent
is `register --mode UNKNOWN_RESEARCH --source-tracking-key <exact-source-derived-key>`.
This record tracks old source; it does not authorize a current session to research.

## Semantic checkpoint and observed publication

Write the smallest faithful authorized EM research artifact. A branch source is
valid provenance without implying main admission or mathematical acceptance.
An EM source already present must not be copied again merely because the activity
was unregistered. A KB-only checkpoint is `SYNC_DEBT`.

`checkpoint --source-json` accepts this shape; the `readback.result` is the actual
full managed tool response, not a reconstructed success flag:

```json
{
  "em_sources": [{
    "repository": "awdawmip/enterprise-math",
    "commit": "<immutable-40-hex-commit>",
    "path": "research_notes/<exact-frontier>.md",
    "sha256": "<actual-64-hex-content-sha256>",
    "readback": {
      "tool_name": "github_fetch_file",
      "observation_id": "<locally-assigned-observation-id>",
      "arguments": {
        "repository_full_name": "awdawmip/enterprise-math",
        "ref": "<same-immutable-commit>",
        "path": "research_notes/<same-exact-frontier>.md"
      },
      "result": {
        "isError": false,
        "structuredContent": {
          "content": "<actual-full-file-content>",
          "encoding": "utf-8",
          "sha": "<actual-Git-blob-sha1>",
          "display_url": "https://github.com/awdawmip/enterprise-math/blob/<same-commit>/research_notes/<same-exact-frontier>.md"
        }
      }
    }
  }],
  "kb_sources": ["<optional-exact-KB-journal-reference>"]
}
```

An original `call_id` may be preserved if the tool exposed one; never fabricate
it. An `observation_id` is explicitly local provenance. The helper checks full
content, SHA-256, Git blob, repo/ref/path, and immutable URL. Its imported JSON is
not server-signed or cryptographically authenticated, and the helper makes no
network request. Missing observed publication remains `VERIFY_EM_PUBLICATION`.
Use `em_sources:[]` for an actual KB-only checkpoint, not an invented EM pin.

```text
python tools/research_activity.py checkpoint --activity-id <RA-id> --event-id <stable-progress-event-id> --expected-sha256 <current-record-byte-sha256> --source-json <payload.json>
```

The helper preserves all prior events and writes immutable observation sidecars
under `research_activity_records/<RA-id>/readbacks/<receipt-sha256>.json`.
Publish the updated record and new sidecars together using fresh remote old-blob
or commit CAS/non-force semantics. A stale writer must reload and preserve another
writer's events. A byte-equivalent event retry is idempotent; a conflicting event
ID is rejected. To repair debt, append a **new** event with
`--repairs-event-id <earlier-event-id>` and observed EM source. No empty or
unverified successor can clear debt. Connector-only transport must preserve this
same schema/history and actual hashes; unavailable verification stays explicit
until the helper or an authorized execution host can check it.

## Startup, final boundary, and owner visibility

The canonical runtime guard returns `REGISTER_RESEARCH_ACTIVITY` for an unbound
ordinary research state. Its activity branch never returns task authorization.
Use `activity_id`, `session_id`, and `activity_registration_source` in that state.
The latter has the same repo/commit/path/SHA/readback shape as an EM source above,
but targets the **current exact activity record**. A stale record readback cannot
authenticate an updated checkpoint record.
Live guards require the caller's explicit current `session_id` to match the
record. Omission returns `BIND_CURRENT_RESEARCH_ACTIVITY_SESSION`; it does not
reuse a prior session. UNKNOWN retrospective records support read-only
persistence checking, never live activity permission or research `RETURN_FINAL`.

```text
python tools/research_activity.py guard --activity-id <RA-id> --session-id <current-session-key> --boundary startup --registration-json <current-activity-publication.json>
python tools/research_activity.py guard --activity-id <RA-id> --session-id <current-session-key> --boundary pre-final --event-id <current-event-id> --registration-json <current-activity-publication.json>
python tools/research_activity.py list --limit 20
```

The last command supports `--after <next_cursor>`. Canonical
`research_control_dispatch.py` also adds `research_activity_overview` when records
exist; this is an output field, not a dispatch subcommand or claim queue.
The overview reports stored metadata only. It retains historical debt and lists
recorded repairs separately until the activity guard revalidates their exact
evidence. It does not reread research sources during every dispatch.

`tools/research_runtime_guard.py pre-final` additionally consumes
`research_checkpoint_event_id` and the original primitive `parent_liveness`
inputs from `tools/active_turn_liveness.py`. Persistence does not close an open
parent with executable work. `new_semantic_progress=false` (or the activity CLI's
`--no-new-semantic-progress`) handles a stop before new research without inventing
a result; it never clears an existing debt. Repository guards cannot intercept
arbitrary chat messages by themselves: the ChatGPT startup/continuation routers
must invoke or faithfully apply these entry and checkpoint boundaries.
