# Durable task continuation protocol

Status: ACTIVE_CANONICAL_CONTROL_EXTENSION.
Authority: explicit user architecture/MCP refactor request,2026-09-20.
Contracts: control_plane/executor_succession_policy.json; control_plane/current_control_authority.json.
Core: control_plane/research_continuation.py.
Native write plan: control_plane/research_continuation_writer.py.
Identity: research_identity_state_machine.json.
Scope: cross-conversation control continuity, with no new mathematical admission.

## Persistent work and replaceable execution

The sole task authority remains immutable V2 task publication plus authenticated runtime events, current Result/Review state and role contracts. Inventory, packets, checkpoint locators and line dossiers are projections or evidence; none is another executable task registry.

Preserve Task-ID/publication, hard target and source firewall, immutable branch/frontier refs, completed and unresolved units, contribution/exposure history, Result/Review bindings, pending remote effects and original scope. A new authorized conversation may assume the same task or line responsibility without a private predecessor reply. Existing named authors remain authors, not permanent execution locks.

## Roles and Source identity

MCP issues real execution sessions and native role IDs. The record research_session_records/MCP-UUID.json states SOURCE_SESSION_BOUND and does not assert a platform-signed conversation ID. Researcher activity uses the native RA schema. Driver activation uses a separate authenticated event and immutable DA; governance execution does not fabricate a researcher RA. Foundation authority is not granted by registration.

Client scopes, the private per-session capability and current canonical role/claim authority are separate gates. Public identity bytes do not authenticate possession of an execution capability. A new session does not erase prior contributions or source exposure. Legacy external enrollment is an explicit operator exception, not the default new-conversation path.

## Ownership transition

TAKEOVER is a typed continuation on a new authenticated CLAIM with a new real execution identity/ER. It requires the exact current publication, predecessor claim/comment and preserved frontier. The reducer serializes competing attempts by authenticated event order/CAS. One winning epoch fences previous execution writes; retries do not extend leases or produce a second winner.

Active exact sessions are protected. Canonical accepted owner activity controls the stale threshold; a caller cannot supply an older last_activity_at to steal a recently active task. Prepared transitions are checked again immediately before submission and during reduction. Source-backed completed handoff permits RESUME. Missing/expired ownership takes the normal fresh route after frontier reconciliation.

Driver AUTHORIZE succession separately binds the exact old DA and source comment, its new session and intended authority. A lost Driver is not a required contact. Old DA execution is fenced by the winning succession, while reviews remain evaluated against authority valid at their original time.

## Evidence and publication boundaries

Current control source and artifact source commits are distinct. Verify actual Git blobs or a trusted loader manifest; a dirty/untracked local file cannot be advertised as HEAD:path. Explicit task inputs and authenticated progress/checkpoint refs may identify immutable branch candidates. They become verified pins only after actual bounded readback, with task/publication/manifest/firewall checks. Preserve unknown or missing evidence honestly.

## Current normative context

Read or reuse current behavioral rules separately from the task's immutable scientific inputs. The `current_normative_context` field in continuation and compact startup packets is a set of current-read locators. It does not attest that those rules were fetched or applied. Resolve its `main` locators to the current applicable rule snapshot, or reuse a still-valid verified snapshot under the governing entry. A bundled historical account snapshot remains a cache/source locator; it does not freeze current behavioral policy for later work.

For users already authorized to use the private account knowledge repository, enter `awdawmip/chatgpt-global-knowledge` through `00_BOOTSTRAP.md` and `OPERATING_MANUAL.md`. The `conclusion_contract` in `knowledge/preferences/OUTPUT_TEMPORAL_SEMANTICS_POLICY.json` owns general judgment and expression rules; `knowledge/preferences/MATH_RESEARCH_POLICY.json` owns mathematical evidence and proof standards. Follow their current routes without copying their bodies into taskbooks or delegation prompts. Public contributors follow the public project guides and need no private-repository access.

For TASK research, Driver decisions and audited, frozen FREE Phase B, apply the single public method record [`research_priorities/research_method.json`](../research_priorities/research_method.json). FREE Phase A retains the existing primitive substrate and source firewall. It may use generic account principles when authorized; it defers this project's method record, research agendas and tool/result menus until the existing freeze boundary.

These rule locators stay outside `source_artifacts`, `frontier_template.artifacts`, task publication bindings and frozen evidence. Reading current rules preserves the original scientific input pins, P000, proof scope, provenance, source exposure and review/role authority. An older packet without this field uses this same protocol entry. Updating source code or documentation establishes no deployment result: use actual service/packet readback to establish which generator is running, and retain any existing code-review or deployment requirements.

## Source publication and authorization

Source artifact/checkpoint publication occurs before a PROGRESS/HANDOFF pointer is emitted. A generated plan, a queued job, an upload, a transport checkpoint or an unknown response is not completed Source publication. Multi-file native output sets use current-head non-force CAS, then complete blob/content readback. Unknown outcomes use durable operation reconciliation; do not blind-retry a mutation.

New Result freeze requires actual-current claim/session/epoch and fresh authenticated events. New review requires current DA/session, current Result bytes and contribution-independence checks. Receipt payload digests bind the declared operation and evidence. The exact legacy cutover manifest preserves pre-existing bytes but exempts no original integrity or mathematical check. Post-cutover records lacking valid authorization remain raw history without operational result/review authority.

The official control/writer path rejects fenced execution. This does not physically prevent a repository owner from writing arbitrary files, and local evidence receipts are not platform-signed chat identity. Canonical adoption remains guarded.

## Read performance and recovery

A task-specific packet reduces the exact task. Whole-inventory projection may be an asynchronous bounded job; paginate one fixed client-owned as-of snapshot rather than recomputing all tasks for every page. A refresh creates a new snapshot. Any subsequent write rechecks live authority and publication; a list page never grants ownership.

After process/chat loss, reconcile completed Source operations, preserve VERIFIED_COMPLETE work, minimally resolve UNKNOWN evidence and continue the smallest UNFINISHED unit. Distinguish an orphaned actor, a missing Source intake, an integrity fault and a real mathematical obstruction. Do not reclassify a mathematical block as executable merely to avoid waiting.

## Migration and acceptance

The migration preserves existing task semantic states and immutable RR/DR bytes. Existing branch returns may be integrated byte-for-byte with their real historical origin and explicit pre-cutover proof; this is evidence intake, not mathematical acceptance. The T6 return intake preserves its original actual published RR bytes and GLOBAL_T6_OPEN disposition.

Acceptance includes new sessionB continuing sessionA's immutable branch checkpoint without private history; authentic activity preventing takeover; exact-CAS competition; no old-writer freeze/late old-format authority; Driver loss and replacement; GOV and RESEARCH role separation; no session-key bypass through request-ID reuse or public RA; real Source publication/readback; and unchanged P000/discovery/promotion semantics.
