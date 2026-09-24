# D24 session rollover and P11 continuation repair — 2026-09-24

Scope: CONTROL_PLANE_MAINTENANCE / NO_NEW_MATHEMATICS. Existing research results, ownership records and contributor provenance remain authoritative; this repair does not accept the UR candidate or promote mathematics.

## Deployed changes

- MCP [PR #10](https://github.com/awdawmip/em-research-mcp/pull/10), reviewed head `9c5cbb2b9b56a34011786b887159063a5bb5032f`, merged as `ae9584c88879c0abf052240946b55061158ea8be`. Authenticated service is version 0.6.6.
- Release `/opt/em-research-mcp/releases/em-rollover-d694b5df3bf1`; archive SHA-256 `d694b5df3bf186db4a049ed4dfd7e78222004c50ea2352f406b85543a6d1aac1`.
- Source [PR #1513](https://github.com/awdawmip/enterprise-math/pull/1513), reviewed commit `4072d4452c3c5a7438b1b07a7bf9805de0807760`, merged as `7e96d54c0b421c43a3992b483c3514e4a63c0371`.
- Exactly one of the 156 reviewed Source code pins changed: `control_plane/research_continuation.py`, `3ebf85f7fca2416e1234ed8f450f73019d5499b2` → `d9ff789c583d1d3016dd8ab48fcc366ae839e2e6`. Configuration SHA-256 is now `ba56c3ad82c06f65e472acad546545c4b178b93492831b01cf3bd6b3e6fb3c25`.
- Source code/pin activation used a short coordinated quiesce after verifying no pending writes. Backup: `/var/backups/em-research-mcp/automation-20260924T005148Z`. Credentials, private HTTPS/proxy settings and live databases were preserved; no database restoration or operator-created research identity/claim occurred.
- Current ordinary-chat and autonomous-execution instructions were published at `611745b585da7805e1bd2bca9cce42bc3dd91058`.

## Root causes and repair semantics

D24 needed a new successor identity, while the old service session could not close because it retained protected staging. The original proposed PR also omitted the real inbox allowlist and had two crash windows that could leave a permanent disposition fence. The completed implementation preserves all complete/incomplete staged bytes and original request provenance in a neutral immutable Source archive, retains immutable local rows, records a separate verified disposition and then permits the existing strict close path. It does not masquerade as a checkpoint publication. Unknown publication effects reconcile the original request. Source-live claims and pending writes still block the transition. Own active Driver DA can preserve neutral evidence and is revoked only by normal native close.

P11 retained its exact current publication ID as an unchanged initial progress marker. Treating that ID as a path made its input seed unavailable. The Source repair recognizes only the exact current initial marker/time, with a real predecessor, no live claim, no checkpoint and no source firewall; it returns verified task input with `completed_units=[]`. Genuine progress and D24's verified Source checkpoint retain precedence.

## Validation

- Final Linux release: **209 passed**, 13 explicit opt-in cases skipped.
- Fifteen targeted Source input-readback tests passed and received independent review.
- Twenty-one focused staging/inbox/lifecycle cases cover 27 uploads, incomplete parts, immutable original requests, real ordinary-inbox routing, crash/idempotency boundaries, pending mutations, live/unopened claims, preserved-row immutability and successor contribution inheritance.
- Actual-Source Researcher fixture passed checkpoint/HANDOFF → neutral preservation → old close → new identity under the same logical subject → preserved checkpoint → successor CLAIM/open. The actual-Source Driver case passed active DA → neutral preservation without revocation → normal close and native DA revoke. Provider writes were isolated in-memory writes. The Driver test's incorrect assumption about a filtered public field was corrected; production code and the passing Researcher AST were verified unchanged before reusing that evidence.
- All 17 MCP changed files and both Source code/test files matched complete immutable readback.
- Live ordinary [status #1679](https://github.com/awdawmip/kimi-query-bridge/issues/1679#issuecomment-5805485570) exposes the preservation contract; [recovery #1680](https://github.com/awdawmip/kimi-query-bridge/issues/1680#issuecomment-5805485877) succeeded.
- Live P11 `sep24-p11-live-seed-0853` succeeded at Source `e4b7d48b075569413099837879b26a6fbd1877b2`. It returned the correct current-publication input seed, no fabricated completed research, and preserved predecessor `MCP-79b4691b230793bc2649deb2` / comment `5786385410`. Its actual `artifact` read `sep24-p11-live-input-read-0900` succeeded with complete hash verification (publication blob `3456915a95dee4f313ba83535c1eefb59eefc002`).

## Real D24 transition

The actual existing logical research conversation is `chatgpt-research-hourly-enterprise-math-20260923`. Maintenance did not copy that ID to issue role-bound operations.

Its original session `MCP-106daeb9d4df43f1bc477337723ce089` / `EM-DIRECT-A71FA7` autonomously submitted `preserve-staging-20260924-r11-0902`. It succeeded and preserved **27 uploads / 112258 bytes** under Source `2951c2ea36352fd71d17ef3a85ca772a49f3f3bc`:

`research_session_staging_dispositions/MCP-106daeb9d4df43f1bc477337723ce089/SD-191fdf4304433f8d9912.json`

Manifest Git blob `18804ab186e3ba733ae3618f70683d827102bd86`; classification `NEUTRAL_STAGING_PRESERVATION_NOT_RESEARCH_PROGRESS`. Authority, execution, mathematical acceptance and research-progress flags are all false. The owner read the neutral manifest through the actual API and legally closed the old service session through `session-close-old-20260924-r11-0912`.

The actual owner then completed `session-start-successor-20260924-r11-0915`: new session `MCP-e6cc623799404ca09be0012f8654712c`, Researcher `EM-DIRECT-B9BCE8`. Server-known prior contributions retain `EM-DIRECT-A71FA7` and `EM-DIRECT-C4D02C`; the inherited Task checkpoint separately retains its complete contributor provenance.

`continuation-d24-successor-20260924-r11-0916` succeeded at Source `7957404f10107f8eb0c1fc9b40d5412ee50f6cee`, with `persisted_checkpoint=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED`, no live owner, and original predecessor `MCP-b31f628f33669c90cd07c7ef` / comment `5795862262`. The actual lane's `continuation-prepare-d24-successor-20260924-r11-0919` then **SUCCEEDED**.

Real execution acceptance is complete:

- `claim-d24-successor-20260924-r11-0921`: SUCCEEDED, new claim `MCP-ffaa21ed1d1a6cd0acf37ad9`.
- [Authenticated unedited CLAIM](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5805751992), server author awdawmip, mode RESUME, exact predecessor CAS and original six artifact pins. All three original frontier contributors remain present.
- `open-d24-successor-20260924-r11-0923`: SUCCEEDED, run `RUN-73b9c960558b3076f06c59d1`, generation 1, revision 0, owned by real successor `EM-DIRECT-B9BCE8` / `MCP-e6cc623799404ca09be0012f8654712c` under unchanged publication `TP2-C0E85430A37213F301EB`.

These are production lane receipts, separate from the isolated tests. No maintenance impersonation or manual replay created them. The old loop is closed at the control/execution boundary; this does not mean the UR candidate has passed independent mathematical review.

## Continuation boundary

D24's governing publication remains `TP2-C0E85430A37213F301EB`. Its earlier Source checkpoint SHA-256 `f98f11396fa5750f8c64e7645a5c82d10ac57f316e33afdfbca2545a1361f3cf` and four verified output artifacts must be consumed, not replayed. Contributors `EM-DIRECT-A71FA7`, `EM-DIRECT-C4D02C`, `EM-DIRECT-F4FEA6` remain part of the research provenance. The seed coexisting in the packet describes absent owner-PROGRESS events and does not override the verified checkpoint.

New actual session: fetch current exact D24 continuation, prepare with only its successful `packet_request_id` and truthful `reason`, then the lane performs its own CLAIM/open. The smallest scientific unfinished unit is UR/JT0 Result packaging, freeze and independent review. LIFT/JT2 remains deferred until UR terminal acceptance; the auxiliary cancellation notes are not a substitute for that formal return.

Current scheduled-task UI could not be inspected: no browser was available, including one documented hidden-IAB initialization attempt. No schedule prompt, timing, notification, Run/Stop or Pause/Resume was changed this turn. Real backend requests and Source artifacts provide the live observations above; yesterday's UI state is not presented as current evidence.
