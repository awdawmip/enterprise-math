# Enterprise Math Role Identity Protocol

Status: `ACTIVE / CANONICAL ROLE IDENTITY + DISPATCH PREALLOCATION CONTRACT`  
Effective: 2026-08-11

## 1. Purpose

Enterprise Math may run many parallel research and Driver conversations. Task IDs identify work; they do not identify which conversation produced a statement, artifact, commit, PR, or handoff.

The project therefore uses one stable execution handle per conversation/session, with a **role-specific visible label**:

- `RESEARCHER` → `Researcher-ID`;
- `RESEARCH_DRIVER` → `Driver-ID`.

The underlying handle grammar remains compatible with existing `EM-<LANE>-...` identities.

A role identity identifies a conversation/session instance. It does not grant theorem ownership, Driver authority, canonical status, or legal identity.

Machine authority:

`research_identity_state_machine.json`

Helper:

`tools/research_identity.py`

## 2. Bootstrap invariant

Before substantive Enterprise Math work begins, any conversation entering either role must execute:

`RESOLVE_OR_ALLOCATE_ROLE_IDENTITY`

This applies to:

1. direct user research instruction;
2. official taskbook execution;
3. scheduler `CLAIM`;
4. Driver-mediated manual relay;
5. role conversion into `RESEARCHER`;
6. role conversion into `RESEARCH_DRIVER`;
7. handoff into a new conversation;
8. resumption of an existing Enterprise Math conversation.

Identity registration is provenance infrastructure, not a mathematical hard block.

## 3. Resolution order

Resolve in this order:

1. reuse the role identity already visible in the current conversation;
2. restore an unambiguous persisted identity for the same session;
3. for a Driver-mediated manual relay, use the Researcher-ID preallocated in the dispatch envelope;
4. for a scheduler `CLAIM`, use/derive the claim Researcher-ID;
5. otherwise self-allocate a role-appropriate identity locally.

A conversation must not begin substantive research and only invent an ID at return time.

## 4. ID grammar

Existing sequential handles remain valid:

`EM-<LANE>-<NN>`

Automatic handles use:

`EM-<LANE>-<SHORTCODE>`

where `SHORTCODE` is 4–8 uppercase alphanumeric characters.

Examples:

- `EM-R012-01`
- `EM-R012-K7M4`
- `EM-P017-8C21F4`
- `EM-DVR-Q4N7`

`EM-DRIVER-01` is reserved for the explicitly designated primary Driver continuity conversation.

A non-primary Driver uses an `EM-DVR-*` handle but displays it as a **Driver-ID**, not a Researcher-ID.

## 5. Taskbook versus dispatch identity

A reusable taskbook defines work, not a particular runtime conversation. Therefore a taskbook must not contain a fixed `researcher_id`.

New Driver-approved taskbooks continue to declare:

`identity_policy: AUTO_RESOLVE_OR_ALLOCATE`

and may declare:

`identity_lane: R020`

For a **Driver-mediated manual relay**, the runtime binding happens in a separate dispatch envelope.

The Driver preallocates one Researcher-ID with:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

The relay queue and the user-visible handoff carry that Researcher-ID. The receiving conversation preserves it from its first substantive response onward.

This solves two different needs without mixing them:

- taskbook remains reusable and instance-free;
- each actual manual execution starts with a concrete Researcher-ID.

## 6. Scheduler integration

Scheduler `CLAIM` remains deterministic.

If `researcher_id` is missing, derive:

`EM-<LANE>-SHA256(task_id + NUL + claim_id)[0:6].upper()`

Live claim events must match the live Researcher-ID when one is supplied.

## 7. Direct/self-started work

Research that starts outside a Driver relay still self-allocates:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER
```

A non-primary Driver conversation self-allocates:

```bash
python tools/research_identity.py allocate --role RESEARCH_DRIVER
```

The primary Driver uses:

```bash
python tools/research_identity.py allocate \
  --role RESEARCH_DRIVER \
  --primary-driver
```

## 8. Visible markers

Researcher final marker:

`Researcher-ID: EM-R020-ABC123 / RS-R020-...`

Driver final marker:

`Driver-ID: EM-DVR-Q4N7 / CONTROL_PLANE`

If `Global-Knowledge-Sync:` is also emitted, the role identity marker appears immediately before it.

## 9. Registration

Compatibility registration root:

`awdawmip/chatgpt-global-knowledge/projects/enterprise-math/researchers/`

The folder name is historical; it may contain Driver records as well as Researcher records.

Registration is a routing/observability view, not the uniqueness source for automatic IDs.

For manual relay, a Driver may create a preallocated identity record before first use. If the write path is unavailable, the relay still carries the ID and registration may follow later.

## 10. Commit, PR, report, and handoff metadata

Commit/PR subjects continue to use the underlying handle:

`[EM-R020-ABC123] ...`

Human metadata is role-aware:

For researcher work:

```text
Researcher-ID: EM-R020-ABC123
Research-Task: RS-R020-...
Research-Role: RESEARCHER
```

For Driver work:

```text
Driver-ID: EM-DVR-Q4N7
Research-Task: CONTROL_PLANE
Research-Role: RESEARCH_DRIVER
```

Machine payloads should expose `execution_id` plus the role-specific `researcher_id` or `driver_id`. Legacy records using `researcher_id` generically are not rewritten solely for naming cleanup.

## 11. Handoff semantics

Same conversation continuation preserves the same role identity.

A genuinely new manual dispatch receives a new preallocated Researcher-ID unless the Driver is explicitly routing back to the same conversation.

The preallocated ID belongs to the execution session, not to the taskbook forever.

## 12. Driver responsibility

The Driver maintains the human directory, but is not the only source of identity creation.

However, when the Driver is already creating a manual user relay, the Driver **must preallocate the runtime Researcher-ID**. It is an error to hand the user an official relay and rely on the receiving researcher to remember an unstated bootstrap action.

If a historical return arrives with a malformed or missing ID, preserve provenance honestly. Normalize only when the mapping is unambiguous; otherwise allocate a fresh handle at the next execution boundary.

## 13. Identity does not replace isolation or authority

Role identity is observability/provenance only. It does not weaken or replace:

- task isolation;
- theorem-owner isolation;
- Driver/taskbook authority;
- proposal review;
- Foundation stewardship;
- canonical promotion gates;
- theorem status discipline.

The intended invariant is now:

> Every Enterprise Math conversation knows its role identity before substantive work begins, and a Driver-mediated manual research relay arrives with its Researcher-ID already bound.
