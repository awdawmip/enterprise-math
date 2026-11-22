# Research activity registration

This is owner bookkeeping for direct research and FREE Phase A. It does not
register a formal task, claim, Result, review, Working Truth, or mathematical
acceptance. FREE registration requires no question and opens no research catalog.
Formal task execution keeps its existing publication/claim/firewall gates.

Activity provides the required visibility of research sessions; missing registration
remains bookkeeping debt. It is not a prerequisite for independent derivation or
source publication. Reuse an existing own Activity; missing registration, an unfinished
index or an absent observation sidecar does not veto reading, mathematics or
saving the actual scientific file. The lightweight `guard` reports association
and debt separately. Run `audit` only when checking observation evidence; it
keeps its strict source checks. Neither mode grants a Task claim or permission
to rewrite another author's record. No new per-turn startup read is required.

The executable schema is in [`tools/research_activity.py`](../tools/research_activity.py);
[`research_persistence_policy.json`](../research_persistence_policy.json) owns the
checkpoint persistence requirement. This protocol does not replace either.

## Start, including a connector-only ChatGPT host

Use this section when creating a missing Activity association. Reuse an existing
own record. Ordinary research and scientific-file publication do not require
running registration, a guard, or an audit at each step.

With local execution, run:

```text
python tools/research_activity.py register --mode FREE_AXIOM_DISCOVERY --session-id <stable-actual-session-key> --researcher-id <resolved-Researcher-ID>
```

For ordinary directed or already-informed research use `--mode TASK_RESEARCH`.
This legacy mode label does not assert that a formal Task exists. No Task ID or
topic is required. Use `FREE_AXIOM_DISCOVERY` for the explicit FREE role and retain
its Phase-A information barrier; the mode or a new ID never certifies CLEAN prior
context. Disclose actual agenda/result exposure in the candidate provenance. The command creates only a local record and returns its path/hash plus
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

When recording an activity, persist this unique file to EM and obtain the full
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

Activity association is separate bookkeeping and may cover a coherent batch of
research. A verified scientific file does not need a second copy, a separate JSON
manifest, or an observation sidecar merely to count as saved. The full observation
format below is for an Activity source recorded as `EM_SOURCE_OBSERVED`; it is not
a checklist for each deduction, file save, or substantive response. A source
recorded without its observation remains `VERIFY_EM_PUBLICATION` for that evidence
audit, without undoing an independently verified scientific publication.

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

Preserve the actual full-file tool label: `github_fetch_file`,
`mcp__GitHub__fetch_file`, or `mcp__codex_apps__github_fetch_file` for the supported
connector response shape. These exact labels share the same checks; a generic
`fetch` or `fetch_blob` response does not supply this repo/ref/path observation
contract. The separate `em_mcp_github_contents` format also requires its complete
matching raw GitHub Contents response. Existing observations keep their original
labels and bytes.

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

`checkpoint` validates the newly supplied observations and preserves existing
events without replaying their stored receipts. The lightweight `guard` checks
the current record and original session association; it does not read historical
sidecars or verify a registration observation. Run the separate `audit` only when
an observation-evidence audit is needed. That audit validates the persisted
history, reading each distinct sidecar once within the call; a later audit reads
and validates it again. The audit's record contents and hash come from the same
read snapshot. Source bindings, event order, immutable receipts, write locks,
CAS and idempotency keep their existing checks at their applicable boundaries.

New sidecars use canonical JSON. A persisted receipt's path and SHA-256 identify
its actual stored bytes, including the original whitespace and key order. The
reader verifies that byte binding, parses unambiguous JSON, and checks every
source and verification field; it never substitutes a re-encoded JSON digest
for the stored identity. Duplicate keys and non-JSON numeric constants are
rejected. A matching outer digest never skips full content/blob/repo/ref/path,
immutable URL, tool-format, session, history, write-lock or CAS checks. Existing
records and sidecars are not rewritten to adopt a different serialization.

新旁证文件仍使用规范 JSON。已有文件的路径和 SHA-256 绑定其原始存储字节，
包括空白和键顺序。读取时先核对原字节，再拒绝重复键和非 JSON 数值常量，
并完整核验来源及观察字段；不能用重新序列化后的摘要替换原文件身份。
来源内容、Git blob、仓库／提交／路径、不可变 URL、工具格式、原会话、
历史顺序、写锁和 CAS 检查保持不变，也不改写旧记录或旧旁证文件。

## Startup, final boundary, and owner visibility

Unshared derivation may begin without activity pre-registration. The canonical
runtime guard permits that local scope with `authorized=false`; it grants no
task claim or protected write. Ordinary final reporting does not require an
Activity guard or audit. An actual record update still preserves the original
identity, history and CAS rules.

When checking an existing live association, supply its `activity_id` and actual
`session_id`. Omission returns `BIND_CURRENT_RESEARCH_ACTIVITY_SESSION`; a
mismatched session is rejected. UNKNOWN retrospective records do not establish
a live session or formal completion authority.

Only an explicit observation audit needs `activity_registration_source` (or the
CLI's `--registration-json`): the full repo/commit/path/SHA/readback for the
**current exact activity record**. A stale observation does not verify the updated
record. The lightweight guard does not use this observation input.

```text
python tools/research_activity.py guard --activity-id <RA-id> --session-id <current-session-key>
python tools/research_activity.py audit --activity-id <RA-id> --session-id <current-session-key> --registration-json <current-activity-publication.json>
python tools/research_activity.py list --limit 20
```

The last command supports `--after <next_cursor>`. Canonical
`research_control_dispatch.py` also adds `research_activity_overview` when records
exist; this is an output field, not a dispatch subcommand or claim queue.
The overview reports stored metadata only. It retains historical debt and lists
recorded repairs separately; an explicit observation audit verifies their exact
evidence. It does not reread research sources during every dispatch.

Formal task completion is a separate operation through
`tools/research_runtime_guard.py pre-final --formal-task-completion` and its actual
task/owner/parent-liveness requirements. Activity bookkeeping does not supply that
authority or close an open parent with executable work. In an explicit observation
audit, `new_semantic_progress=false` (or `--no-new-semantic-progress`) records a
boundary without new research; it does not clear an existing debt. Repository guards cannot intercept
arbitrary chat messages by themselves: the ChatGPT startup/continuation routers
must preserve the actual shared-task and record-write checks. Ordinary reporting
and material preservation remain available without an activity registration or
checkpoint; see [current research protocol](PORTABLE_RESEARCH_PROTOCOL.md).
