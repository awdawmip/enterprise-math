# Ordinary-control reviewed-source promotion blocker — 2026-09-23

Status: `ACTIVE_RECOVERY_RECORD / CONTROL_PLANE_ONLY / NO_NEW_MATHEMATICS`

## Current classification

- `VERIFIED_COMPLETE` — NFHJPA exact continuation readback. Request `continuation-20260923-r11-0500-nfhjpa` returned `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` and authenticated the declared Driver review input at immutable Source `af0561c5d24f7ec95f49beaff676c9ed35e9579f`.
- `VERIFIED_COMPLETE` — the same conversation read `driver_reviews/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260829.md` through `artifact-20260923-r11-0503-driver` with complete artifact hash verification.
- `UNFINISHED` — NFHJPA `continuation_prepare`. Request `continuation-prepare-20260923-r11-0504-nfhjpa` failed before CLAIM/open with `UPSTREAM_CODE_REVIEW_REQUIRED: control_plane/research_driver_followup_transaction.py, research_driver_followup.py, research_driver_followup_guard.py`.
- `UNFINISHED` — current ordinary-control Driver activation and PRE_FINAL are blocked by the same upstream-code-review gate. Requests `driver-auto11-activate-20260923-0504-7c1a` and `driver-auto11-prefinal-20260923-0510-7c1a` failed with the identical three-file gate.
- `VERIFIED_COMPLETE` — no new Research CLAIM/open was created by the failed NFHJPA prepare, so there is no dangling CLAIM to recover, heartbeat, release, or take over.

## Exact control mismatch

Ordinary-control `status` for `driver-auto11-20260923-045818-7c1a` reports the private GitHub service enabled for session registration, CLAIM, Driver activation, Result/review writes and the ordinary native operations, but pins `reviewed_source_sha=2a0d54a94cf552bc70548a78467f0a283ce5028e`.

Enterprise Math main was refreshed immediately before this recovery record at:

`558758ed30b208851d3775436f1914dc647de9e2`

The service-reviewed commit is an ancestor. Between it and current main, the exact files named by the native rejection changed:

- `control_plane/research_driver_followup_transaction.py`
- `research_driver_followup.py`
- `research_driver_followup_guard.py`

The current line includes the legitimate follow-up publisher repair whose commit message is `fix: bind follow-up publishers to real immutable review-store paths` (`3db5f407d5a091cb8b36d92fae256725ed4fe749`). This patrol does not revert that repair merely to make an older reviewed-source pin pass.

## Diagnosis

This is a `SOURCE_REVIEW_OR_DEPLOYMENT_GATE`, not:

- a mathematical difficulty;
- a missing local checkout / CLI / visible MCP capability;
- `NO_DISPATCH`;
- a CLAIM-liveness or takeover problem;
- a failure of the NFHJPA authenticated input-artifact repair.

The read-only continuation/artifact path already demonstrates that the older bare-progress-reference recovery is now consumable. The next mutation is blocked earlier by the service's upstream-code-review admission.

## Minimal required repair

An authorized upstream reviewer/deployment path must review and promote the current acceptable Source dependency set containing the three named files, or narrowly correct the operation dependency gate if those files are not actually dependencies of a given operation. The repair must preserve current review/follow-up integrity checks; it must not bypass the gate, fabricate a review, broaden authority, or restore superseded bytes.

After an authorized promotion/change, verify one affected research path before declaring recovery:

1. obtain a fresh ordinary-control `status` and confirm the reviewed Source state has materially advanced or the exact gate has otherwise been canonically resolved;
2. use a fresh real Researcher conversation/session and current NFHJPA continuation packet;
3. consume the authenticated input artifact, then call `continuation_prepare` once;
4. only if that prepare succeeds, continue to canonical CLAIM and `open` and verify `execution_started=true` before calling the task `IN_PROGRESS`.

Driver recovery is independent: a fresh/current Driver must obtain its own legitimate session and Driver activation after the same gate is resolved. This patrol does not generate Driver authority, review, follow-up, or closure.

## Do not repeat while state is unchanged

- Do not repeat `continuation_prepare` merely to reproduce the same upstream-review error.
- Do not fall back to generic `prepare` for the predecessor-bearing NFHJPA continuation.
- Do not repeat `driver_activate` or PRE_FINAL solely to reproduce the same three-file gate.
- Do not fabricate a reviewed-source promotion, authority, review, Result, follow-up packet, or closure.
- Do not revert the current follow-up publisher fix to match the older service pin.
- Do not disable/re-enable the research schedule as a substitute for this repair.

## Durable recovery frontier

`LAST_DURABLE_FRONTIER = NFHJPA continuation + authenticated declared-input artifact readback`

`CURRENT_UNFINISHED_UNIT = authorized ordinary-control upstream Source review/deployment promotion (or exact dependency-gate correction), then one fresh continuation_prepare verification`

`NEXT_RECOVERY_ACTION = refresh ordinary-control status and current main once; if reviewed-source admission changed, verify continuation_prepare -> CLAIM -> OPEN; otherwise keep this blocker without mutation replay`
