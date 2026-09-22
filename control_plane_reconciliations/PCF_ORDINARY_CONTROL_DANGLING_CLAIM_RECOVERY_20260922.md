# PCF ordinary-control dangling-claim recovery

Status: `RECOVERY_PENDING / CONTROL_PLANE_ONLY / NO_NEW_MATHEMATICS / NO_EXECUTION_AUTHORITY`
Recorded-at: `2026-09-22T03:22:00Z`
Task: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`
Publication: `TP2-8D3D94C1C621740A50AB`
Inspected-source: `763bf0c889aa99cd6a95c5c8da003a8dbe909f99`

This record preserves a control recovery frontier. It is not a scheduler event, CLAIM, release, Result, review, Driver verdict, mathematical acceptance, or permission to preempt a live owner.

## CURRENT_STATE

The ordinary-control researcher chain for logical client `chatgpt-em-hourly-research-primary` contains exactly eight requests in the inspected GitHub view: status, dispatch, continuation, artifact, session_start, prepare, continuation_prepare, and claim. The final claim request `claim-20260922-hourly-primary-0141-08` succeeded, creating Issue-240 CLAIM comment `5770046151` / claim `MCP-68051fbea4fad1873535a880` for Researcher `EM-DIRECT-B2FC0C`, session `MCP-1d2c0a43015d4e8a91bd899df7d0a684`. Its native receipt explicitly says `execution_started=false` and directs the client to call `open` before execution. No `open`, `publish_checkpoint`, or `freeze` request exists in that logical client chain after the CLAIM.

Current canonical continuation projection observed at `2026-09-22T03:19:38Z` reports this task `LEASED` with the same claim and `last_owner_activity_at=2026-09-22T01:43:13Z`; route action is `VERIFY_LIVENESS_THEN_PREPARE_EXPLICIT_TAKEOVER`, `execution_authorized=false`. Ordinary-control currently does not grant client-declared takeover of a still-live claim merely because its originating chat disappeared.

The claim execution intent exists at `research_execution_records/RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT/ER-51B093D8798187DEAF88.json` and remains `record_state=CLAIM_INTENT`. The current main snapshot has no Result directory for this Gen2 task, so a canonical Result freeze has not been observed.

## CLASSIFICATION

- `VERIFIED_COMPLETE`: predecessor PCF5/PCF6 20-row prior-art/duplication classification and its hash-verified handoff frontier. The current execution intent preserves this as `VERIFIED_COMPLETE_DO_NOT_REPLAY`.
- `UNFINISHED`: `GEN2_CURRENT_PUBLICATION_EXECUTION_AND_RESULT_FREEZE`, including canonical `open`, current-source execution, Result writer, immutable readback, and frozen-return HANDOFF.
- `CORRUPT_OR_CONFLICTED`: none newly established by this patrol for the preserved predecessor mathematics.
- `UNKNOWN`: whether a newer authorized executor will refresh, release, or lawfully supersede the still-leased claim after this observation. Resolve only from newer server-authenticated state.

## CONTROL DIAGNOSIS

This is not the earlier `CAPABILITY_MISMATCH_HEAD_OF_LINE` condition. The private ordinary-control service is currently enabled for session registration, claim, artifact write, Result write, Driver write, and review write. The failure mode is instead `CLAIM_SUCCEEDED_BUT_OPEN_NOT_STARTED`, followed by loss of the originating execution conversation while the owner lease remained.

The replacement control inspector must not borrow the predecessor session or call `open` as that researcher. A stale conversation does not erase the server lease, and the current ordinary-control contract still protects a live claim until canonical recovery permits succession.

## RECOVERY

1. Protect the exact claim while canonical state still reports it live. Do not create a competing CLAIM or fabricate activity.
2. On each recovery-capable researcher entry, read the exact current continuation/runtime before fresh dispatch.
3. If newer server activity proves the original executor active, consume it and stop recovery.
4. If the claim becomes canonically released/expired or a supported typed stale-takeover path becomes available, create a **new real Researcher session** with a fresh logical control conversation, preserve all predecessor contributor IDs and the exact frontier, then resume only `GEN2_CURRENT_PUBLICATION_EXECUTION_AND_RESULT_FREEZE`.
5. After any future CLAIM succeeds, obtain and verify the canonical `open` receipt before treating execution as started. Do not leave another silent claim merely because CLAIM transport succeeded.
6. Run only the canonical execution/Result writer path. Do not replay the completed 20-row audit, hand-build a Result, strengthen PCF5/PCF6, or infer historical novelty from absence.
7. After a writer-produced Result is read back and admitted, publish only the canonical frozen-return HANDOFF for independent Driver review.

## EVIDENCE

- Ordinary-control claim request: `awdawmip/kimi-query-bridge#37`, request `claim-20260922-hourly-primary-0141-08`.
- Native CLAIM: Enterprise Math Issue #240 comment `5770046151`.
- Execution intent: `research_execution_records/RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT/ER-51B093D8798187DEAF88.json`.
- Current continuation observation: ordinary-control request `continuation-pcf-20260922T0316-patrol04`, observed `2026-09-22T03:19:38Z`.

## TAKEOVER_CONDITIONS

A recovery executor must use its own current real Researcher session and current canonical role authority. Preserve the exact task/publication, source pins, contributor provenance, theorem strength, no-repeat list, and all existing task constraints. A replacement conversation is not authority to impersonate `MCP-1d2c0a43015d4e8a91bd899df7d0a684` or to mutate the still-live claim before canonical succession permits it.
