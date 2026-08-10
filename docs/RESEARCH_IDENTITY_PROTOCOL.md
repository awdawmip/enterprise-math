# Enterprise Math Research Identity Protocol

Status: `ACTIVE / CANONICAL VISIBLE IDENTITY + AUTO-BOOTSTRAP CONTRACT`  
Effective: 2026-08-11

## 1. Purpose

Enterprise Math may run many parallel ChatGPT research conversations. Task IDs identify work, but they do not identify which conversation produced a statement, artifact, commit, PR, or handoff.

Every Enterprise Math research conversation therefore carries one stable, human-readable `Researcher-ID`.

A Researcher-ID identifies a **research conversation/session instance**, not a human legal identity, theorem owner, task authority, or canonical status.

The identity mechanism must work even when the user starts a task directly, uses an existing taskbook, accepts an automatic scheduler dispatch, or changes the role of an already-open conversation without using a Driver-generated prompt.

Machine state authority:

`research_identity_state_machine.json`

Local resolver/helper:

`tools/research_identity.py`

## 2. Top-level bootstrap invariant

Before substantive Enterprise Math work begins, any conversation entering either role:

- `RESEARCHER`
- `RESEARCH_DRIVER`

must execute:

`RESOLVE_OR_ALLOCATE_RESEARCH_IDENTITY`

This trigger applies to all entry paths:

1. direct user research instruction;
2. official taskbook execution;
3. scheduler/Issue #240 `CLAIM`;
4. role conversion into `RESEARCHER`;
5. role conversion into `RESEARCH_DRIVER`;
6. handoff into a new conversation;
7. resumption of an existing Enterprise Math conversation.

The identity bootstrap is a provenance requirement, not a mathematical gate. Failure to write a central registry record is never a `HARD_BLOCK`.

## 3. Resolution algorithm

Resolve in this order:

1. If the current conversation already visibly carries a Researcher-ID, reuse it.
2. If an unambiguous persisted identity for the same conversation/session is available, restore it.
3. If the session is entering through a scheduler `CLAIM`, use the CLAIM identity. If the CLAIM omitted one, the scheduler derives one automatically from `task_id + claim_id`.
4. Otherwise generate a new local short-code ID immediately and keep it stable for the rest of the conversation.
5. Register/update the human directory when the write path is available; otherwise mark registration pending and continue.

Never delay actual research merely to obtain a prettier sequential number.

## 4. ID grammar

Two forms are valid.

### 4.1 Existing/curated sequential handles

`EM-<LANE>-<NN>`

Examples:

- `EM-R011-01`
- `EM-R012-01`
- `EM-R005A-01`

These remain valid for already assigned conversations.

### 4.2 Automatic handles

`EM-<LANE>-<SHORTCODE>`

where `SHORTCODE` is 4–8 uppercase alphanumeric characters.

Examples:

- `EM-R012-K7M4`
- `EM-P017-8C21F4`
- `EM-DIRECT-91AB3C`
- `EM-DVR-Q4N7`

The lane is normally supplied by taskbook field `identity_lane`, otherwise derived from the compact `Rxxx`/`Pxxx` prefix of `task_id`.

The primary Driver continuity conversation may use the reserved ID:

`EM-DRIVER-01`

A different Driver conversation must not silently adopt `EM-DRIVER-01`; it auto-allocates a `DVR` handle unless explicitly designated as the primary Driver continuity conversation.

## 5. Taskbook contract

New Driver-approved taskbooks must declare:

```text
identity_policy: AUTO_RESOLVE_OR_ALLOCATE
```

They may additionally declare:

```text
identity_lane: R012
```

A taskbook must **not** preassign a fixed Researcher-ID, because one task may be executed by multiple conversations over time or in parallel.

Legacy taskbooks without the field automatically inherit this global identity protocol.

Taskbook authority and identity remain separate:

- `task_authority = DRIVER_APPROVED` says the task is dispatchable;
- `Researcher-ID` says which conversation is executing it.

## 6. Scheduler state-machine integration

`tools/research_scheduler.py` is identity-aware.

For each accepted `CLAIM`:

- if `researcher_id` is supplied and valid, use it;
- if omitted, automatically derive:

```text
EM-<LANE>-<SHA256(task_id + NUL + claim_id)[0:6].upper()>
```

The reduced scheduler state exposes:

- `researcher_id`
- `last_researcher_id`
- `identity_source`
- `identity_lane`

For live-claim events (`HEARTBEAT`, `PROGRESS`, `HANDOFF`, `HARD_BLOCK`, `DONE`), an explicitly supplied Researcher-ID must match the live claim identity. Missing identity fields remain accepted for historical event compatibility.

A new CLAIM after handoff/lease expiry receives a new identity unless the caller explicitly reuses the same conversation ID.

## 7. Direct task and role-transition bootstrap

When no scheduler CLAIM exists, the conversation self-resolves identity.

Reference command:

```bash
python tools/research_identity.py allocate \
  --task RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY \
  --role RESEARCHER
```

For a direct research request without an official task ID:

```bash
python tools/research_identity.py allocate --role RESEARCHER
```

For a non-primary Driver role transition:

```bash
python tools/research_identity.py allocate --role RESEARCH_DRIVER
```

For the designated primary Driver continuity conversation:

```bash
python tools/research_identity.py allocate \
  --role RESEARCH_DRIVER \
  --primary-driver
```

If the conversation already has an ID and the user changes its role, preserve the ID and update `Research-Role` / `Research-Task` metadata. A genuinely new conversation gets a new ID.

## 8. Registration

Human-readable directory:

`awdawmip/chatgpt-global-knowledge/projects/enterprise-math/RESEARCHER_DIRECTORY.md`

Registration is used for routing and human observability; it is **not** the uniqueness source for automatic IDs.

This avoids a startup race where two sessions both need to read and increment a shared number before working.

Registration state may be:

- `REGISTERED`
- `REGISTER_PENDING`

If the central write path is unavailable:

1. keep the locally generated ID;
2. show it in the conversation;
3. persist it in the first report/commit/PR/handoff;
4. register at the next semantic checkpoint if convenient;
5. continue research immediately.

## 9. Visible chat marker

Every substantive Enterprise Math final response ends with:

`Researcher-ID: <ID> / <TASK-or-CONTROL_PLANE>`

Examples:

`Researcher-ID: EM-R012-K7M4 / RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY`

`Researcher-ID: EM-DRIVER-01 / CONTROL_PLANE`

If a `Global-Knowledge-Sync:` line is also required, the Researcher-ID line is immediately before it so the sync marker remains last.

## 10. Commit identity

Identity must be visible in GitHub's ordinary commit list.

Semantic-checkpoint commit subjects begin with the Researcher-ID:

`[EM-R012-K7M4] R012: formalize genesis-index`

Driver/control-plane commits:

`[EM-DRIVER-01] governance: update identity state machine`

When supported, also include trailers:

```text
Researcher-ID: EM-R012-K7M4
Research-Task: RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY
Research-Role: RESEARCHER
```

Legacy commits are not rewritten solely to add identity metadata.

## 11. PR, report and handoff identity

Research PR titles begin with `[<Researcher-ID>]`.

PR bodies and human reports show near the top:

```text
Researcher-ID: EM-R012-K7M4
Research-Task: RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY
Research-Role: RESEARCHER
```

Machine-readable manifests/handoffs carry equivalent fields:

```json
{
  "researcher_id": "EM-R012-K7M4",
  "research_task": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
  "research_role": "RESEARCHER"
}
```

## 12. Driver responsibility

The Driver maintains the human directory and resolves ambiguous historical returns, but the Driver is **not** required for identity creation.

When the Driver dispatches a researcher explicitly, it may assign a curated sequential ID. When a conversation starts outside that path, the conversation self-allocates automatically under this protocol.

If a return arrives with no identity and mapping is ambiguous, do not guess. Allocate a fresh handle on the next execution boundary and preserve the provenance ambiguity.

## 13. Identity does not replace isolation or authority

Researcher-ID is observability/provenance only. It does not weaken or replace:

- task isolation;
- theorem-owner isolation;
- Driver/taskbook authority;
- proposal review;
- Foundation stewardship;
- canonical promotion gates;
- theorem status discipline.

The intended invariant is simple:

> Any Enterprise Math conversation that starts doing research must know who it is before it starts producing research, regardless of how that conversation was launched.
