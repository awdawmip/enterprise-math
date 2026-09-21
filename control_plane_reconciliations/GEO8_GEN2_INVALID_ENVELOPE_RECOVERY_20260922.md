# GEO8 Gen2 invalid-envelope recovery checkpoint

Status: `RECOVERY_PENDING / NONEXECUTABLE_CONTROL_NOTE / NO_RUNTIME_AUTHORITY`
Recorded-at: `2026-09-21T23:52:24Z`
Mode: `CONTROL_PLANE_MAINTENANCE`
Task: `RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE`
Publication: `TP2-75A6C3F81E2D094B67CF` (Gen2)
Inspected-control-source: `45b1921519dbf7178ea7eb8f6245e2b29156e668`
Refreshed-main: `c36b4791b042f500e875d1d29f94e0f2fb26ac7e`

This note is not a scheduler event, Result, Driver review, replacement authorization, task publication or successful reopen. It does not reset a claim or grant execution. Old CLAIM/ER/RR/HANDOFF and scientific bytes remain unchanged.

## CURRENT_STATE

The matching historical startup packet `control_plane/chatgpt_startup_packets/EMREQ-CTRL-20260921T232205Z-RESEARCH-7A41D2.json` actually says `CLAIM_NEW_OWNER`, source `fe0f5541d24655cc138eaca8aeb29a76dac2a14b`, for this exact Gen2. This incident is not a NO_DISPATCH or shared-latest-receipt error.

Current publication bytes pin `sha1:98d2c500a84d1b7dfe75327925567b8700dcb118`. The branch draft RR instead contains `sha1:98d2c500b1e01d86c15b7d8b8bb569a27098d031` and no `write_authorization`. Its reference is NOT authorized for formal review, terminality or successor publication.

The main Result directory at the inspected snapshot contains only historical `RR-68BA014D54542DA7221C.json`, not the new Gen2 draft. The subsequent main comparison contains only dispatch transport changes. The owner work branch still resolves to `326a7d5b802880f0a86de9c9ec7db2c695f8efc9`.

Classification by unit:

- `VERIFIED_COMPLETE`: durable publication and full-byte recovery of the Gen2 revalidation audit at `70507c68b94faae7259e422b39ebfed72692c1ee`. Its checker PASS and zero-math-drift conclusions retain researcher-reported strength; this inspector did not repeat the mathematical checker or perform independent Driver review.
- `CORRUPT_OR_CONFLICTED`: the formal envelope represented by `ER-FB306185F1323177C4FB` / `RR-E4CA978B5A377CE0506E`; the RR has the directly verified wrong pin and missing mandatory write authorization. Do not copy it into operational main or rewrite it in place.
- `UNFINISHED`: lawful current-publication execution/Result freeze and subsequent independent review. A diagnostic comment alone has not completed either.
- `UNKNOWN`: the exact current full canonical reduced task state after the faulty frozen HANDOFF. This inspection did not run the complete current-source reducer with the full stable raw event stream. Source-level HANDOFF behavior is not misrepresented as a fresh canonical readback.

## COMPLETED_WORK

The bounded local byte check reconstructed the fetched 4020-byte audit and matched Git blob `4b4db00cc64aa2ee5ad8db30ba255b0328288df6`; its SHA-256 is `164b0f5548de8393a6e1b23543b04a022f1b6775888cfac8dd48a79b4514c6d1`.

SHA-256 of Task-ID + NUL + `CLM-7901302A48F64F15545A` gives suffix `66A466`, agreeing with `EM-GEO8BORSUKR6-66A466`. Correct syntax/determinism is not itself proof of accepted ownership or a real session binding.

Three isolated tests of the unchanged `_fixed_source_candidate` function from `control_plane/research_continuation.py` (blob `facaf8a5af2c6478ba28484b70a621d90f60dd54`) confirm that the old `branch@commit + path` locator returns None, while the exact audit and RR blob URLs below are recognized as source candidates. Locator recognition does not grant artifact validity. No runtime code, state, registry, role, claim, Result, review or mathematical artifact was changed.

## EVIDENCE_AND_ARTIFACT_LOCATIONS

Valid revalidation audit:

https://github.com/awdawmip/enterprise-math/blob/70507c68b94faae7259e422b39ebfed72692c1ee/research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/gen2_revalidation_audit_20260922.json

Invalid formal RR, retained ONLY as diagnostic history (Git blob `aec6abde35955dd6da1ca057fcac23d8b2a679f3`):

https://github.com/awdawmip/enterprise-math/blob/326a7d5b802880f0a86de9c9ec7db2c695f8efc9/research_result_records/RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE/RR-E4CA978B5A377CE0506E.json

Authoritative Gen2 publication (Git blob `1c0df15abbee12e385528c8ab72c7f5556f37621`):

https://github.com/awdawmip/enterprise-math/blob/c36b4791b042f500e875d1d29f94e0f2fb26ac7e/research_task_records/RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE/TP2-75A6C3F81E2D094B67CF.json

Actual server events/provenance:

- CLAIM 5768944007, created 2026-09-21T23:27:00Z; claim `CLM-7901302A48F64F15545A`. Its body contains no session_id; a later native writer must use its own genuine current execution binding, not invent an old one.
- Frozen HANDOFF 5769039237, created 2026-09-21T23:35:01Z, references the invalid RR.
- Researcher diagnostic 5769063884, created 2026-09-21T23:37:07Z, explicitly NOT A SCHEDULER EVENT.
- Activity provenance supplied by the researcher: `RA-GEO8GEN2-66A466-20260922` (not independently audited here).

https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5769039237

https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5769063884

## REMAINING_WORK

First obtain the exact fresh canonical continuation/runtime projection on a capable native host or connected authorized MCP, preserving its source commit and complete stable raw Issue 240 snapshot. Do not substitute a bare JSON event list, an empty stream, a fabricated trusted-loader marker or the historical pre-claim packet.

If the current projection is already legally recovered by another executor, consume that exact result and do not repeat the action. Otherwise determine the existing authorized recovery transaction for the observed state before issuing a new CLAIM.

Source-level dead ends already excluded:

- `UNBLOCK` only accepts a BLOCKED reducer state; it is not a generic reopen of FROZEN_RETURN.
- `RECONCILE_HANDOFF_SCOPE` only resolves the exact unresolved untyped HANDOFF_READY obligation, with no live owner/hard block/frozen state. It cannot simply relabel this explicitly frozen HANDOFF as CONTINUATION.
- A frozen HANDOFF releases ownership in the pure reducer; absence of a current claim does not imply NEEDS_DISPATCH or authorize reclaim.
- Ordinary Result control replacement requires source-backed Driver authority and matching execution plus a valid corrected Result. It is not authority to manufacture the missing post-cutover receipt.
- Do not edit the historical HANDOFF to exploit the edited-event rejection rule, fabricate a NEEDS_REVISION review, create a new task generation to escape the fault, or relax native write gates.

Once the exact lifecycle is lawfully execution-eligible, the authorized real executor continues only the formal envelope unit: current TP2/taskbook pin, native execution record, actual current runtime state/raw events/source snapshot, canonical Result writer, full immutable readback and native admission check, then frozen HANDOFF. The inspector does not perform this Researcher/Driver action or declare it completed.

## TAKEOVER_CONDITIONS

Retain the original research contributor and evidence exposure. Consume the audit and unchanged Gen1 science without rerunning the 33-atom / 528-edge / 15/13 / 10/7 work merely because envelope recovery failed. Preserve the exact restricted-template scope: no b(6)=33, b(6)>=33, general <=32 partition impossibility or full R4-transfer impossibility. P000 and all task-local source/firewall/regression/stop constraints remain unchanged.

The unresolved operational dependency is a verified native current-state and recovery/write transaction. No complete existing EM checkout was present in this execution environment; plugin discovery did not expose the project's MCP. Partial source reads and the isolated locator tests are not whole-repository verification. This is not evidence that every authorized host lacks the capability.

Restored frontier: exact evidence locators and this durable recovery context only. Canonical reopen, accepted new CLAIM, Result authorization and Driver review remain unperformed here.
