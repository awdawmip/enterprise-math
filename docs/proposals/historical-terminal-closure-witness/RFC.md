# Historical terminal obligations in prospective parent closure

Status: **PROPOSAL ONLY / NOT EXECUTABLE / NO AUTHORITY GRANTED**.

This RFC proposes a narrowly typed historical terminal closure witness. It does
not implement a witness, change a reducer, select an Objective, repair an old
follow-up packet, or discharge the currently open parent. No new native
operation described here is callable. The existing fail-closed behavior remains
in force until the authenticated transport and Source contracts below are
implemented and reviewed together.

## Fixed evidence and current behavior

The Root supplied Source commit is
`012706a3ac1e42acbd86cab977afac7659264992`. The isolated local copy independently
reproduces its supplied tree, `fecf38f002032638972aaee4e8b6db521fcee583`.
`EXACT_SOURCE_EVIDENCE.json` records the native read-only outputs and all nine
independently recomputed SHA-256/Git-blob pins. This branch did not refresh a
remote ref, execute the mathematical checker, or observe live Issue #240 owners.

The historical child is
`RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`,
publication `TP2-7022EC048DC373BFA4CB`. Its Result is
`RR-680C6257EEF10F6F1C16`; its review is `DR-289F116DBE89C6FA1339`.
The original accepted/narrowed mathematical statements remain evidence. Two
independent control gaps prevent future parent closure:

1. The stored packet `DFU-2D40311F1784F024C5CA` fails the native deterministic
   identity check: the expected identity is `DFU-2D01B09A46FE0376ACC4`.
   The actual native Task state is `AWAITING_DRIVER_REVIEW`, `terminal=false`.
   Appending another packet for the same review conflicts with the one-packet
   authority rule; rewriting or renaming the immutable old packet is prohibited.
2. The publication predates the first operational selection of the prospective
   parent generation `OG-7190F25EA3CAE970C90A`. Its binding is `LEGACY_UNBOUND`.
   A present-day head or sidecar cannot prove operational tenure on 2026-08-29.
   The parent reducer requires proven binding before evaluating Task terminality.

The parent is currently OPEN and the projection is `OBJECTIVE_HEAD_NOT_CLOSED`.
Fixing metadata does not finish the outstanding prior-art audit or any other
child. No date-based exemption, global historical whitelist, synthetic review,
retroactive binding, or Task republication is proposed.

## Why this branch does not safely implement the mechanism

Three integration gaps require explicit native contracts before a Source
compatibility path can participate in closure:

* `research_pre_final_authority.py:36-105` calls
  `research_parent_closure.derive_objective_closure` without authenticated runtime
  events. The Source tree alone cannot prove the absence of a current winning
  Issue #240 CLAIM or an in-flight native mutation.
* `control_plane/research_parent_objective_dispatch_gate.py:32-80` clears owner
  and lease fields after a CLOSED/PARKED overlay. That projected `claim_id=null`
  cannot prove that a pre-existing raw winning CLAIM is absent. Owner checking
  must replay authenticated events **before** Result and parent overlays.
* `control_plane/research_continuation_write_authority.py:45-57,100-159` supports
  Result/review admission. Its non-RESULT branch is the review path, not a
  generic new-record authorization API. Meanwhile,
  `research_objective_driver_authority.py:71-74,87-147` audits generations,
  heads and bindings, not historical witnesses. A new record cannot borrow a
  review receipt or escape the Driver audit by using a new store.

`research_driver_followup._materialization_binding(..., require_current=True)`
can supply genuine DA/session, exact operational review-set and raw RR/DR pins.
Its contract explicitly leaves live-session authentication to the native caller.
It does not prove that a runtime event collection is complete or that no new
CLAIM exists. A payload hash, witness ID, empty `events` array, boolean
`trusted=true`, or caller-supplied observation watermark adds no such authority.
No platform-signed receipt is required or invented by this RFC.

## Proposed meaning and explicit limits

`HISTORICAL_TERMINAL_CLOSURE_WITNESS` would establish only that one precisely
identified historical obligation may be counted as discharged when evaluating
one prospectively controlled parent. It would not establish that the old Task
was published during an Objective's tenure.

Keep the old Taskbook/publication, ER, RR, DR, report, return, checker and DFU
bytes and IDs. Keep `task_result_state` and the follow-up reader unchanged: the
old DFU remains invalid and the Task does not become operationally terminal
through this mechanism. Do not add a corrected packet or modify the frozen
legacy-review baseline.

The closure output would separately identify
`historically_discharged_child_task_ids` and exact witness evidence. These IDs
must not be added to `terminal_active_child_task_ids`. Execution, mathematical
acceptance, Working Truth, Foundation, canonical promotion, parent completion
and final-interaction grants remain false. The current parent can become
complete only through a genuine CLOSED successor and all its independent child
obligations; PRE_FINAL still evaluates actual liveness separately.

## Authenticated transport boundary to add first

The native entrypoint must construct a complete, fresh Issue #240 runtime
observation internally. Client request payloads must not accept runtime comments,
normalized events, collection-complete assertions or observation boundaries.
The proposed `materialize-request.schema.json` intentionally excludes them.
Client `expected_pins`, successor routes and scope-preservation prose are only
preconditions to be checked against independently read canonical evidence.
They are not a scope verdict, an absence proof, or an authorization declaration.
Schema `uniqueItems` is not canonical-path uniqueness: the server must reject
duplicate/conflicting canonical paths and duplicate/conflicting successor routes,
and require the exact independently derived evidence and obligation sets.

The internal context must retain the actual raw server comment envelopes,
repository/issue identity, authenticated collection process, completed pagination
boundary and observation time. The implementation must explicitly define the
freshness window and behavior for collection errors, truncated pages, edits and
missing evidence. A last-comment ID or timestamp alone is not proof of complete
collection. A collection with no events must be distinguishable from no
collection. Unknown or stale observations fail closed.

The writer must run in the existing authenticated control transaction, with the
same serialization/fencing used for native ownership mutations. Refresh exact
Source authority at the mutation boundary; recheck collection/ownership and
pending writes before committing. Abort or recompute if the Source head or
runtime observation changes. An out-of-band manual Git commit without that
runtime boundary cannot substitute for this writer.
Implementation review must establish that the serialization/fencing covers
**every** authoritative CLAIM ingress, including Issue comments produced outside
the ordinary native queue. A Source ref CAS does not lock a later Issue comment.
If a producer cannot participate in the same transaction boundary, the transport
must define a safe guard/observation protocol for that producer; an undocumented
assumption that the current worker lock covers all channels is insufficient.

Pass a new **internal-only** typed runtime context explicitly through the witness
writer, closure reducer and PRE_FINAL projection. Do not serialize it into a
caller-supplied parent status object. Recollect at each future closure/PRE_FINAL
boundary; the witness's creation-time observation never proves present liveness.
This is a coordinated Source/native-backend change, not a Source-only waiver.

## Witness writer and read-time checks

The prospective record shape is described in `record-shape.json`. It is an
interface proposal, not a currently admitted record schema. The writer must:

1. Authenticate the current real Driver session at the native boundary. Require
   enabled Source-backed DA, an active exact DA/session at the current action,
   current Source head, and exact payload binding. Never accept an arbitrary
   backfilled action time from the client.
2. Require the exact current historical publication and same parent, still
   `LEGACY_UNBOUND`; reject an existing direct or sidecar binding. Pin the nine
   historical files and every original DFU successor publication/Taskbook.
   Validate the Task/publication/ER/RR/DR/DFU identities and all underlying
   output/report bindings, not just a list of self-consistent hashes.
3. Require the original RR and single immutable ACCEPTED terminal DR to remain
   in the current canonical operational view. Reject any new Result, second
   review, authority hold/quarantine, unresolved review synthesis, replacement
   or nonterminal disposition. This RFC does not bypass original Driver or
   Result audits and does not re-review mathematics.
4. Treat the DFU only as evidence. Explicitly prove that packet-ID disagreement
   is the sole compatibility fault, while its complete native gate obligations,
   publisher, parent, recommendation and successor publication pins all remain
   valid. Do not simply stop after the first ID error, ignore other exceptions,
   or inject a corrected packet into an operational selector.
5. Explicitly map every original successor obligation to its exact lawful
   current same-Task publication through a complete supersedes chain. Preserve
   parent, scope and all gates; validate every intermediate publication and
   Taskbook. Require the current successor's genuine prospective Objective
   binding. A superseding publication is not an automatic acceptance transfer.
   Outstanding successors remain independent current children and prevent
   parent completion until their own authority is terminal.
6. Anchor to the exact current selected OPEN generation, its raw digest,
   selection receipt and expected head. Require publication/review times to
   precede that actual selection; never backdate the selection or assert old
   tenure. Pin the original accepted/narrowed scope without strengthening it.
7. Replay the authenticated raw winning-CLAIM reducer before Result and parent
   overlays. Reject any effective claim, valid owner lease with stale/unknown
   session, pending execution write, active cohort, unresolved handoff, new
   unfinished output or other live work on the historical child. The prospective
   successor may continue independently; the witness must not revoke it.
8. Exclusively create one content-bound witness for the exact historical
   Task/publication and OPEN anchor. Conflicts and duplicates fail closed; this
   first narrow version has no latest-wins or replacement selector. Recheck
   authority and byte pins at transaction commit, use non-force Source CAS, and
   read back exact persisted bytes before treating the write as successful.

Add explicit typed admission and audit coverage for the new record store. Do not
pass a new `kind` into the existing Result/review receipt adapter. Creation-time
Driver validity is historical provenance: later lawful Driver succession does
not itself invalidate a persisted witness. Its later use still requires fresh
runtime evidence and the current closure action's independent Driver authority.
No state read, documentation file, or proposal schema admits a witness.

## Narrow future CLOSED inheritance

Initially allow only a CLOSED **direct successor** of the witness's selected
OPEN anchor. Verify exact selection receipts, generation lineage, monotone
times, and current head validity. Require unchanged parent scope, success and
closure criteria, and research-value fields. The CLOSED record must explicitly
include the witness path and content digest in its closure evidence.

At use time repeat all historical pins, current-publication/review-set checks,
successor-chain pins and fresh raw ownership/cohort checks. Evaluate every other
current child through its existing reducer. An OPEN head remains incomplete even
with a valid witness; outstanding prior-art work also remains incomplete.
Reopen, changed scope/criteria, a new publication, a non-direct lineage or a new
unit invalidates applicability and requires a new explicit design/authorization,
not silent inheritance. This version creates no generic re-witness workflow.
Any missing proof or exception retains existing fail-closed behavior.

## Review scope and staged implementation

This proposal-only diff adds documentation, an unadmitted interface shape and
fixed public evidence. It changes no executable module, machine control
authority, historical record, session or task. Existing parent closure tests
(7) and current-publisher binding tests (15) pass on the exact local snapshot;
these are baseline checks, not tests of an implemented witness.

Before implementation, review the backend's authenticating entrypoint and
current full-comment acquisition/transaction boundary together with the Source
writer, explicit new-type admission/audit, parent reducer and PRE_FINAL adapter.
There must be no deployment in which only the closure exemption is active.
No code or real witness should be published until the complete boundary is
reviewable and the following acceptance suite passes.

| Case | Required outcome |
| --- | --- |
| Genuine current Driver, complete native observation, exact historical chain, selected OPEN anchor | One immutable witness; old DFU and Task states unchanged; parent remains incomplete |
| Legal direct CLOSED successor, unchanged scope, explicit witness digest, all other children terminal, fresh no-owner evidence | Historical child listed separately; complete projection may be derived; no direct final grant |
| Any of nine pins/output pins altered; traversal/symlink escape; mismatched IDs | Reject |
| Wrong parent/publication, supersession fork, unselected OG, head/CAS move | Reject |
| Revoked/missing Driver, wrong session, backfilled timestamp, changed payload | Reject |
| Missing/truncated/stale collection; client `trusted=true` or empty events | Reject |
| Winning CLAIM hidden by CLOSED overlay; stale session with valid owner lease | Reject without clearing or fencing the owner |
| New RR, second DR, quarantine, unresolved synthesis, live cohort or unfinished write | Reject |
| Correcting DFU ID or making Task terminal through a witness | Forbidden; original readers unchanged |
| Prior-art successor still active or unreviewed | Parent remains incomplete |
| Reopen, changed scope/criteria, non-direct CLOSED lineage or new publication | Old witness inapplicable |
| Missing witness or any validator failure | Original fail-closed projection preserved |

The existing accepted/narrowed mathematical evidence remains saved throughout.
Completion of this RFC is a Driver control checkpoint, not mathematical or
parent-goal completion.
