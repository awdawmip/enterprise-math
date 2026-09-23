# Autonomous scheduled research recovery — 2026-09-23

Scope: CONTROL_PLANE_MAINTENANCE / NO_NEW_MATHEMATICS. The parent research program remains open and is executed by its existing scheduled roles.

## Deployed repair

- MCP code [PR 8](https://github.com/awdawmip/em-research-mcp/pull/8), merge `74a3a4e079713e3931c852389989ba5604c596d6`, is deployed as version 0.6.5.
- Release `/opt/em-research-mcp/releases/em-recovery-5b7f60e1b59a`; archive SHA-256 `5b7f60e1b59abf366854db367e5901e0635f69686bfd124d79a5bf5b8c5a7815`.
- Production configuration SHA-256 remains `62bdb3edd2abf0afd4684c75abd60e0db182484cd7968bcee5b29caad7816572`; all 156 reviewed Source code pins, authentication, private HTTPS behavior and live databases are retained. Activation did not create any research session, claim, Result or review.
- [Deployment and acceptance evidence](https://github.com/awdawmip/em-research-mcp/blob/e36852781ea10ae2140e9770314dfcc64c0d0a5c/docs/evidence/autonomy-20260923/VALIDATION.json).
- Source commit `48b9b0580f571e27eed8b09026429803771cf408` publishes the shared execution protocol and exact public contracts. The taskbook policy digest stays `sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73`; existing tasks were not invalidated.

Read current `control_plane/current_control_authority.json`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, ordinary-chat control documentation and the exact task/frontier. Follow current authority instead of using this dated observation as a new permission grant.

## Operational behavior

The existing three Researcher schedules, one Driver schedule and one control-maintenance schedule remain the execution structure. Control maintenance explicitly owns recovery coordination. A new role is not required merely to consume two existing reviews; the two reference passes serve distinct purposes and still require truthful contribution/context disclosure.

`status` now exposes exact Driver operation contracts, enum values and recovery discovery. Definite pre-admission rejections return an actionable contract. `recovery_status {}` finds the actual logical conversation's original pending requests, unopened claims, run generations and unpublished final upload pointers. It is a read-only local projection; it grants neither current Source ownership nor proof of chat liveness.

Recover unknown effects under the original request ID, then restore existing work, then use canonical dispatch. Same-conversation compaction retains the stable conversation ID; a genuinely new conversation registers its own actual execution identity and continues from Source. Released or expired claims can resume through the existing typed transaction. Early takeover of a live claim still requires genuine admissible observations and predecessor CAS. Database silence alone is not such an observation.

At a real turn end/handoff, persist the verified frontier and a precise next action, then use the authorized release path where appropriate. In-turn checkpoints preserve the current owner; a pending freeze keeps release=false. Platform cutoff does not disable a recurring task. Schedules must not require a user to send “continue”.

## Verification

- Production-host isolated unit suite: 191 passed, 11 explicit opt-in scenarios skipped.
- Separate fresh actual-Source fixture: passed in 739.349 seconds. It exercised two existing reviews, contribution-overlap refusal, pass1 persistence/idempotence, Driver A close, new Driver B restoring Source, pass2, synthesis, publication, immutable V2 successor materialization, dispatch and close. All writes used an isolated in-memory provider; no real mathematics or production claim was created.
- Ordinary GitHub transport [status #886](https://github.com/awdawmip/kimi-query-bridge/issues/886#issuecomment-5786678735) and [recovery #887](https://github.com/awdawmip/kimi-query-bridge/issues/887#issuecomment-5786679195) both returned matched SUCCEEDED receipts after activation. The former exposes all four exact independence literals; the latter confirms the maintenance conversation has no research session or claimed work.
- All 17 changed MCP files and all eight Source protocol/contract files were read back in full and matched exact bytes.

## Actual GEO6 recovery frontier

The original failure was KQB #792, `INVALID_REFERENCE_INDEPENDENCE`, before native admission. Another scheduled control run published the literal-enum documentation at Source `56259052bd629b7e16224212ea431268d11f762a` and closed support issue #1498. Preserve that provenance; the 0.6.5 repair adds machine-readable contracts, actionable errors and general recovery.

Real Driver r11 (`EM-DVR-A5A686`, session `MCP-98288d02291d47c9b0ebffd45b7e3be7`) independently progressed Result `RR-B5DB25EC13BF1C42DC9B` for Task `RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS`:

- Intake `RVI-3665327656EACA84F2F0`.
- Pass1 `RVP-8A73E9DEB29F93C5D84E` (semantic).
- Pass2 `RVP-212F0EF75EEAFFEF3C8E` (adversarial).
- Both disclose `SHARED_CONTROL_CONTEXT_DISCLOSED` and bind exact review-set SHA-256 `7cb308262f266dff501f2c2c9be23dc040277526a5ed35ea47b01b5f4e3e2efa`.
- Original reviews `DR-4187E7655E4E30A30253` and `DR-B36C8071BB5E68A81A32` retain exact bytes/authors; no third review was appended.

At verified Source `bf123ba3f2cbf42fd2ea15c947a265ce58eb40eb` (08:21 +08 readback), r11 has also published synthesis `RVS-A5B3F54695D286E9735A`. Its operational ACCEPTED/FOLLOWUP_TASK judgment retains the existing semantic-selector integration route and explicitly forbids inventing a direct mathematical successor or duplicate task. It grants no Working Truth or canonical promotion. Consume this synthesis and existing `DFU-24003FFDCADFA610E1B4`, then re-read the current flow/routing for the remaining legal unit. Do not replay passes or synthesis. No extra Driver run was triggered by this repair.

The same verified Source also contains a new real CM(-24) external-prior-art checkpoint by `EM-DIRECT-01C0C9`, task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT`, claim `MCP-162d5049182372dd29b776af`. It records a finite-Clausen bridge, source classifications and a 77-prime regression report, with explicit remaining theorem-level audit and no-repeat units. Its declared verification is AUTHOR_REPORTED_SOURCE_BYTES_ONLY_NOT_MATHEMATICAL_ACCEPTANCE. This is evidence that a real research lane persisted research while the control repair ran; this maintenance did not independently certify its mathematics.

## Scheduled-prompt snapshot

The adjacent `autonomy_20260923_prompts/` files preserve the reviewed prompt texts and their saved-UI verification. All five were saved, navigated away from, reopened and matched exactly after only CRLF-to-LF / trailing-whitespace normalization; Root independently verified their SHA-256 values. Final verification time: 2026-09-23T00:20:25.265030Z. All five remain enabled. They are deployment evidence, not a second task registry. Use the live schedule and current Source contracts for execution. Original task IDs, frequencies, phases, notification behavior and enabled state are preserved.

The repair closes this control-maintenance scope. The scheduled research parent continues, including GEO6 synthesis/follow-up and other already assigned research; it is not declared complete.
