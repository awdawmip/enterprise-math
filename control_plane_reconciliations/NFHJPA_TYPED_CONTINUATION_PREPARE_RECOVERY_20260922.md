# NFHJPA ordinary-control typed-continuation prepare recovery

Status: `RECOVERY_PENDING / CONTROL_PLANE_ONLY / NO_RESEARCH_AUTHORITY`
Date: `2026-09-22`
Task: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT`
Publication: `TP2-39ACFC69F85D8661CFBF`
Conversation: `auto-r11-20260922-1019-a7c9`
Successful continuation request: `nfhjpa-cont-auto-r11-20260922-1019-07` / `awdawmip/kimi-query-bridge#344`
Failed prepare request: `prepare-auto-r11-20260922-1019-08` / `awdawmip/kimi-query-bridge#345`
Researcher session registered before prepare: `MCP-e5f45fcb97eb4fb1a2958b507f031384` / `EM-DIRECT-E9AAFA`

This note is not a CLAIM, execution authorization, research checkpoint, mathematical result, HANDOFF, or task-state mutation.

## CURRENT_STATE

The exact continuation request completed successfully and reported the Task as `HANDOFF_READY / NEEDS_DISPATCH`, with no live claim and route `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION`. The Task retains predecessor history (`last_claim_id=CLM-NFHJPA-20260922-0658-1A7C9E`) and the continuation packet is therefore the current source of typed predecessor/frontier context.

The client then submitted ordinary `prepare` using only:

`{"dispatch_request_id":"dispatch-auto-r11-20260922-1019-06"}`

The canonical native adapter rejected it with:

`TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR`

No new CLAIM or execution authority resulted from that failed prepare.

## ROOT_CAUSE

Current ordinary-control guidance separates fresh-dispatch preparation from predecessor-aware continuation:

- `prepare(dispatch_request_id=...)` prepares a genuinely fresh dispatch route;
- `continuation_prepare(packet_request_id=...)` is the typed path for a canonically released/no-live-claim predecessor while `runtime.dispatch_state=NEEDS_DISPATCH`;
- `claim` accepts a successful `prepare`, `prepare_exact`, or `continuation_prepare` request.

This Task had a predecessor and a successful exact continuation packet, but the client discarded that typed packet and called the generic fresh `prepare`. The rejection is therefore a client routing defect, not `NO_DISPATCH`, not a capability mismatch, and not evidence that the research task is mathematically blocked.

## CLASSIFICATION

- `VERIFIED_COMPLETE`: canonical dispatch and exact continuation readback for this execution attempt; current Researcher session registration.
- `CORRUPT_OR_CONFLICTED`: the failed generic `prepare` route selection for a predecessor-bearing Task. No canonical task/result bytes are classified corrupt by this finding.
- `UNFINISHED`: typed continuation preparation, winning CLAIM, OPEN, and the substantive Task research thereafter.
- `UNKNOWN`: substantive research completion for the current Task. Do not infer completion from the predecessor metadata or from the continuation packet.

## MINIMAL_RECOVERY

1. Before retrying, refresh the exact Task continuation and check whether another legal Researcher has already claimed/opened it. Protect any live owner.
2. If the Task remains released with `dispatch_state=NEEDS_DISPATCH` and predecessor history requiring typed continuation, do not submit another generic `prepare` and do not rerun fresh dispatch merely to escape the error.
3. Use the current successful continuation packet as the source and invoke canonical `continuation_prepare` with its `packet_request_id`, a bounded reason, and only the frontier fields/artifact references required by current Source. Preserve current source pins and predecessor provenance; do not invent completed units.
4. After successful `continuation_prepare`, use the returned prepare request for `claim`, read back the winning canonical CLAIM, and immediately continue to `open` in the same execution turn. Only an authorized successful `open` starts execution.
5. If current continuation instead shows a live claim, stale-session takeover route, frozen state, or another specialized lane, follow that current route rather than forcing `continuation_prepare`.

## CLIENT_GUARD

Research clients must not decide `prepare` versus `continuation_prepare` from the dispatch action string alone. After an exact continuation read, predecessor-bearing released tasks must preserve and consume the typed continuation packet. A native `TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR` rejection is a deterministic signal to stop generic fresh preparation, re-read the current continuation once, and use the typed continuation path if its current state permits it. Do not describe this error as no task or as a research failure.
