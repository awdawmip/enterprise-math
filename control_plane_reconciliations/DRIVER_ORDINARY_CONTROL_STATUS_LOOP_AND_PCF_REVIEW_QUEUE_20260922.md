# Driver ordinary-control status loop and PCF review-queue recovery

Status: `CONTROL_RECOVERY_CHECKPOINT / NONEXECUTABLE_NOTE / NO_DRIVER_AUTHORITY`
Recorded-at: `2026-09-22T08:26:30Z`
Mode: `CONTROL_PLANE_MAINTENANCE`
Inspected-main-before-write: `ce8b4c57edb481f57f48481e0a7a5b125483c6a3`

This note is not a scheduler event, Driver activation, Driver review, Result, follow-up packet, task publication, or mathematical acceptance. It grants no research or Driver authority.

## CURRENT_STATE

### PCF current-publication Result

`RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT / TP2-8D3D94C1C621740A50AB` has now completed the previously unfinished current-publication execution/freeze unit.

Canonical Result: `RR-96D4CCDABC18462C8D5F`.

The Result is present on main, binds execution `ER-60B8A1FF82C42D8B8723`, claim `MCP-773897ff5858aaf6d7e47dd7`, Researcher `EM-PCF-D9D300`, and carries `ENTERPRISE_MATH_CONTROL_WRITE_AUTHORIZATION_V1`. Issue #240 has a matching `FROZEN_RETURN_AWAITING_DRIVER_REVIEW` HANDOFF. The Result itself says independent Driver review remains required.

No `research_result_reviews/RR-96D4CCDABC18462C8D5F/` directory was present at inspected main. Therefore:

- predecessor 20-row PCF5/PCF6 classification: `VERIFIED_COMPLETE / DO_NOT_REPLAY`;
- current-publication canonical Result freeze: `VERIFIED_COMPLETE`;
- independent Driver review: `UNFINISHED`;
- no new mathematical corruption was established by this patrol.

### Research scheduler after PCF freeze

A fresh ordinary-control RESEARCH dispatch (`dispatch-20260922T0819Z-auto11-02`) returned `CLAIM_NEW_OWNER` for `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT`, source `ce8f0ec32f053aafa18544c9d5714a5a8eb54c8c`. A new Researcher `session_start` request followed, and main advanced to `ce8b4c57edb481f57f48481e0a7a5b125483c6a3` by registering the new session. This is active research routing and must not be preempted by control maintenance.

## DRIVER CLIENT DEFECT OBSERVED

The ordinary-control chain for conversation `chatgpt-driver-automation-20260922-1558` did not advance to a Driver session during the inspected bridge history:

1. issue `#246`, request `status-20260922T0759Z-driver4`, was rejected with `ONE_JSON_BLOCK_REQUIRED`;
2. issue `#247`, request `status-20260922T0801Z-driver4b`, then succeeded and reported `session=null`, `session_registration_enabled=true`, `driver_activation_enabled=true`, and review/driver-write operations enabled;
3. issue `#253`, request `status-20260922T0806Z-driver4c`, repeated the same successful status with the same material capability result and still `session=null`;
4. repository search for that exact conversation found no subsequent `session_start` or `driver_activate` request in the inspected bridge state.

This is a client control-flow stall: repeated capability discovery after a successful status is not Driver progress and must not substitute for `session_start -> driver_activate -> inventory/continuation/review`.

## MINIMUM REPAIR

The existing hourly Driver automation prompt was changed only at the client-control layer:

- at most one successful ordinary-control `status` capability probe per new Driver turn;
- if status succeeds with `session=null` and session/Driver activation enabled, immediately perform `session_start(role=RESEARCH_DRIVER)` and then canonical `driver_activate`;
- an initial `ONE_JSON_BLOCK_REQUIRED` format rejection may be corrected once with exactly one JSON code block, after which execution must continue rather than polling status again;
- two equivalent status/receipt reads with no new state are classified as control-loop stall and must switch to the next canonical action or persist an exact blocker;
- status success is capability discovery only, never Driver authority or review completion;
- `RR-96D4CCDABC18462C8D5F` is explicitly included as a current frozen Result requiring independent Driver review if no other Driver has already produced one.

No scheduler priority, task publication, claim, lease, Result, mathematical statement, review record, follow-up packet, P000 rule, or admission gate was modified.

## EXISTING FOLLOW-UP RECOVERY

The earlier Factor recovery record `control_plane_reconciliations/FACTOR_BLIND_BRIDGE_TERMINAL_REVIEW_FOLLOWUP_MATERIALIZATION_20260922.md` remains authoritative for its exact defect. This patrol did not create a duplicate Factor review or fabricate a follow-up packet. The updated Driver client still requires review-to-follow-up materialization closure before treating an accepted terminal review as operationally closed.

## NEXT

A fresh Driver turn should use its own real session and current source-backed Driver authority, then consume existing canonical evidence:

1. do not repeat capability-only status polling;
2. do not review a Result that already has a current valid review;
3. if `RR-96D4CCDABC18462C8D5F` still lacks a review, review it only through the canonical session-bound Driver writer and preserve all contributor-independence and source-binding gates;
4. after any review, complete or explicitly preserve the typed follow-up/materialization state instead of creating a second review;
5. continue other independent Driver work when one follow-up adapter or whole-repository validation remains externally blocked.
