# Enterprise Math Role Identity Protocol

Status: `ACTIVE / CANONICAL ROLE IDENTITY + FINAL-FOOTER + DISPATCH PREALLOCATION CONTRACT`  
Effective: 2026-08-26

## 1. Purpose

Enterprise Math may run many parallel Researcher, Driver, and Foundation Steward conversations. Task IDs identify work; they do not identify which conversation produced a statement, artifact, commit, PR, review, publication, or handoff.

The project therefore uses one stable execution handle per conversation/session, with a **role-specific visible label**:

- `RESEARCHER` → `Researcher-ID`;
- `RESEARCH_DRIVER` → `Driver-ID`;
- `FOUNDATION_STEWARD` → `Steward-ID`.

The underlying handle grammar remains compatible with existing `EM-<LANE>-...` identities. Adding the Steward role does not create another identity database or another task-control workflow.

A role identity identifies a conversation/session instance. It does not grant theorem ownership, Driver authority, Foundation authority, canonical status, or legal identity.

Machine authority:

- `research_identity_state_machine.json`;
- `final_response_identity_policy.json`.

Helper:

`tools/research_identity.py`

## 2. Bootstrap invariant

Before substantive Enterprise Math work begins, any conversation entering any active Enterprise Math role must execute:

`RESOLVE_OR_ALLOCATE_ROLE_IDENTITY`

This applies to:

1. direct user research instruction;
2. official taskbook execution;
3. scheduler `CLAIM`;
4. Driver-mediated manual relay;
5. Foundation Steward maintenance/review work;
6. role conversion into `RESEARCHER`;
7. role conversion into `RESEARCH_DRIVER`;
8. role conversion into `FOUNDATION_STEWARD`;
9. handoff into a new conversation;
10. resumption of an existing Enterprise Math conversation.

Identity registration is provenance infrastructure, not a mathematical hard block. If the registration write path is unavailable, preserve the locally resolved ID and continue as `REGISTER_PENDING`; retry only at a semantic checkpoint.

Identity resolution and identity display are separate obligations. A correctly allocated ID that is omitted from a final response does **not** satisfy the visible-identity contract.

## 3. Resolution order

Resolve in this order:

1. reuse the role identity already visible in the current conversation;
2. restore an unambiguous persisted identity for the same session;
3. for a Driver-mediated manual relay, use the Researcher-ID preallocated in the dispatch envelope;
4. for a scheduler `CLAIM`, use/derive the claim Researcher-ID;
5. otherwise self-allocate a role-appropriate identity locally.

A conversation must not begin substantive role work and only invent an ID at return time.

Role transition in the same conversation may preserve the underlying execution handle while changing the visible role label/scope. Authority never leaks across a role transition merely because the handle is preserved.

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
- `EM-FREE-7A2C`
- `EM-DVR-Q4N7`
- `EM-STW-6B2E91`

`EM-DRIVER-01` is reserved for the explicitly designated primary Driver continuity conversation.

Default non-task role lanes are:

- non-primary Driver: `DVR`;
- Foundation Steward: `STW`.

## 5. Taskbook versus runtime identity

A reusable taskbook defines work, not a particular runtime conversation. Therefore a taskbook must not contain a fixed `researcher_id`, `driver_id`, or `steward_id`.

Published taskbooks declare:

`identity_policy: AUTO_RESOLVE_OR_ALLOCATE`

and may declare an `identity_lane`.

Publisher provenance belongs to the immutable publication record. A Researcher, Driver, or Foundation Steward publishing a task uses the execution ID of the current role session as `publisher_id`; this does not bind that ID to later task execution.

For a **Driver-mediated manual relay**, runtime binding happens in a separate dispatch envelope. The Driver preallocates one Researcher-ID with:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

This keeps taskbook identity reusable while each actual manual execution has concrete provenance.

## 6. Scheduler integration

Scheduler `CLAIM` remains Researcher execution identity. If `researcher_id` is missing, derive:

`EM-<LANE>-SHA256(task_id + NUL + claim_id)[0:6].upper()`

Live claim events must match the live Researcher-ID when one is supplied.

Foundation Steward identity is not a scheduler-claim identity by default. Steward verification/maintenance is a separate role operation; if a Steward publishes a follow-up task, the resulting task is later claimed by a Researcher through the normal CLAIM path unless its governing task explicitly says otherwise.

## 7. Direct/self-started work

Researcher:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER
```

Free Researcher:

```bash
python tools/research_identity.py allocate \
  --role RESEARCHER \
  --lane FREE \
  --research-mode FREE_AXIOM_DISCOVERY
```

Non-primary Driver:

```bash
python tools/research_identity.py allocate --role RESEARCH_DRIVER
```

Primary Driver:

```bash
python tools/research_identity.py allocate \
  --role RESEARCH_DRIVER \
  --primary-driver
```

Foundation Steward:

```bash
python tools/research_identity.py allocate --role FOUNDATION_STEWARD
```

The Steward helper defaults to the `STW` lane and renders `Steward-ID`.

## 8. Mandatory visible marker on every final response

Canonical machine contract:

`final_response_identity_policy.json`.

Freeze:

`ACTIVE_ENTERPRISE_MATH_ROLE -> EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER`.

This applies to every assistant message on the `final` channel while `RESEARCHER`, `RESEARCH_DRIVER`, or `FOUNDATION_STEWARD` is active. It includes short status replies, readiness/completion receipts, handoffs, blocked/no-go conclusions, refusals, and ordinary role answers. Commentary/progress/tool messages are not final responses and do not require the footer.

Researcher marker resolution:

1. active explicit task → `Researcher-ID: <ID> / <TASK_ID>`;
2. no task + free mode → `Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY`;
3. other direct task research → `Researcher-ID: <ID> / TASK_RESEARCH`.

Driver marker:

`Driver-ID: <ID> / CONTROL_PLANE`

Foundation Steward marker:

`Steward-ID: <ID> / FOUNDATION_STEWARD`

The marker appears **exactly once**. Registration state such as `REGISTER_PENDING` never suppresses it.

If `Global-Knowledge-Sync:` is also emitted, the role identity marker appears immediately before it and the Global-Knowledge-Sync line remains last.

## 9. Registration

Compatibility registration root:

`awdawmip/chatgpt-global-knowledge/projects/enterprise-math/researchers/`

The folder name is historical; it may contain Researcher, Driver, and Foundation Steward records.

Registration is a routing/observability view, not the uniqueness source for automatic IDs. It must never become a required remote write before substantive work.

## 10. Commit, PR, report, and handoff metadata

Commit/PR subjects continue to use the underlying handle:

`[EM-R020-ABC123] ...`

Researcher metadata:

```text
Researcher-ID: EM-R020-ABC123
Research-Task: RS-R020-...
Research-Role: RESEARCHER
```

Driver metadata:

```text
Driver-ID: EM-DVR-Q4N7
Research-Task: CONTROL_PLANE
Research-Role: RESEARCH_DRIVER
```

Foundation Steward metadata:

```text
Steward-ID: EM-STW-6B2E91
Research-Task: FOUNDATION_STEWARD
Research-Role: FOUNDATION_STEWARD
```

Machine payloads expose `execution_id` plus the role-specific `researcher_id`, `driver_id`, or `steward_id`. Legacy records are not rewritten solely for naming cleanup.

## 11. Handoff semantics

Same-conversation continuation preserves the same underlying role identity unless the user or governing role transition explicitly establishes a new execution session.

A genuinely new manual dispatch receives a new preallocated Researcher-ID unless the Driver is explicitly routing back to the same conversation.

The execution ID belongs to the role session, not to a taskbook forever.

## 12. Driver and Steward responsibility

The Driver maintains the portfolio/human directory but is not the only source of identity creation. When the Driver creates a manual user relay, the Driver must preallocate the Researcher-ID.

Foundation Steward authority is defined by `foundation_steward.json` and the Foundation/backflow contracts. `Steward-ID` only makes that role execution traceable; it does not broaden or self-create Steward authority.

If a historical return/review arrives with a malformed or missing ID, preserve provenance honestly. Normalize only when the mapping is unambiguous; otherwise allocate a fresh handle at the next execution boundary.

## 13. Identity does not replace isolation or authority

Role identity is observability/provenance only. It does not weaken or replace:

- task isolation;
- theorem-owner isolation;
- Driver authority;
- Foundation Steward authority;
- task publication contracts;
- proposal/candidate review;
- canonical promotion gates;
- theorem status discipline.

The intended invariant is:

> Every active Enterprise Math role resolves its execution identity before substantive work begins and emits exactly one role-appropriate identity marker on every final response, without turning identity persistence into a research-time GitHub dependency.
