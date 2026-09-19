# Exact MCP control-code admission delta

Observed: 2026-09-19T20:32:36.954193Z.
Role: CONTROL_PLANE_MAINTENANCE.
State: offline reviewed-pin proposal ready; live service unchanged.

## Current boundary

The configured authenticated HTTPS MCP endpoint initializes and answers em_status successfully. A new JT2 generation-3 task request failed with UPSTREAM_CODE_REVIEW_REQUIRED after control PR1468 and PR1493 reached the project main branch. The failed operation did not create a Task or CLAIM. Its unchanged raw receipt is recorded beside the delta.

The service's existing CanonicalControl.code_check compares the entire control Python blob map against its reviewed_python_blobs configuration. Local current service policy is pinned to de49e82f7332b04c64fcce9d46b67c82bf4c55c5. Against the reviewed source at 35d15f3d2594c63583f9f9b3e41a22ccfb56418e, exactly three existing paths differ: the publication newline gate, the runtime reducer, and frozen-Result authority isolation. Current main 3f728c2f43adbde0fcc9e6d94267b3cd8324cd14 adds only the verified JT2 data packet over that control source.

## Exact review evidence and offline validation

PR1468's two changed production modules passed 115 scoped tests plus publication, reference and current-control checks. PR1493's changed production module passed 83 scoped tests plus complete Result/review integrity, followup-cause, reference and current-control audits, with an additional bounded technical peer review. Both PRs were merged and all published bytes were fully read back. Mathematical Result/Review dispositions and all ten PCF7 evidence dependencies remain unchanged.

The unmodified service code_check was executed locally twice against the same complete source copy: the original reviewed map rejected exactly the observed three paths; replacing only those three reviewed hashes and the source-reference metadata passed. Every other configuration field remained identical in memory. The local configuration file and live service were not changed. This is an offline admission check, not a successful live task replay or remote deployment.

## Artifacts

- research_artifacts/PCF7_RESULT_CONTROL_ISOLATION_20260920/mcp_code_admission_delta.json
- research_artifacts/PCF7_RESULT_CONTROL_ISOLATION_20260920/mcp_task_gate_failure.json
- https://github.com/awdawmip/enterprise-math/pull/1468
- https://github.com/awdawmip/enterprise-math/pull/1493
- research_artifacts/PCF7_RESULT_CONTROL_ISOLATION_20260920/technical_review.json
- Local reproducer: D:/em/TEMP/research-resume-20260920/check_mcp_admission_delta.py

## Next operator action

Use the ordinary service-admission process to review the exact module changes and current live configuration, compare the expected old/new blobs in the attached delta, preserve every unrelated pin and all authority settings, and update only admitted pins if authorized. Recheck a read-only live task operation afterward. A changed live baseline requires fresh scope review; the local proposal is not a blind configuration replacement.

Claim writes and executor binding remain disabled. No credential, claimant, execution authority or mathematical acceptance is created by this proposal. The separate rejected MCP checkpoint-write command remains unexecuted and was not retried through another route. Existing Source-native research authorizations and verified publications retain their own evidence.

The user's bounded research window still ends at 2026-09-19T20:56:15Z; this admission residue does not extend it.
