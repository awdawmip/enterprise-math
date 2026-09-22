# PCF Driver review — Task completion assessment schema recovery

Status: `RECOVERY_PENDING / CONTROL_PLANE_ONLY / NO_REVIEW_AUTHORITY`
Date: `2026-09-22`
Task: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`
Publication: `TP2-8D3D94C1C621740A50AB`
Result: `RR-96D4CCDABC18462C8D5F`
Failed ordinary-control request: `review-pcf-96d4-20260922-57e1bc4af8d2` / `awdawmip/kimi-query-bridge#339`
Inspected Enterprise Math main: `cee127e33943bcc2e28bbfb12e867ad2a84c9389`

This record is a recovery locator only. It is not a Driver review, follow-up packet, review authorization, Result mutation, scheduler event, mathematical acceptance, or parent-objective closure.

## CURRENT_STATE

The current-publication PCF Result is already frozen through the canonical Result writer and remains the durable research frontier. The completed predecessor 20-row PCF5/PCF6 prior-art/duplication classification remains `VERIFIED_COMPLETE / DO_NOT_REPLAY`.

Driver `EM-DVR-AEFA30`, session `MCP-5e901ed1c4d043578e0e0301fd1bcbd5`, obtained source-backed Driver authority and published durable draft review artifacts. The formal ordinary-control `review` mutation in bridge Issue #339 was then rejected by the canonical native writer with:

`ERROR: Driver Task completion assessment requires exact typed fields`

The failed native mutation committed no canonical review. At the inspected main, `research_result_reviews/RR-96D4CCDABC18462C8D5F/` is absent. Therefore the formal review remains `UNFINISHED`; the draft report is evidence/provenance only and must not be treated as an operational review.

## ROOT_CAUSE

Current `research_driver_followup.py::_driver_task_completion_assessment` requires exactly one pinned report comment block with schema `ENTERPRISE_MATH_DRIVER_TASK_COMPLETION_ASSESSMENT_V1`. Its JSON object must contain exactly these ten fields and no others:

- `schema`
- `driver_id`
- `task_id`
- `publication_id`
- `result_id`
- `result_record_sha256`
- `original_hard_target_disposition`
- `disposition`
- `terminal_scope`
- `assessment`

The first nine fields except `assessment` are exact typed bindings. `schema` must be `ENTERPRISE_MATH_DRIVER_TASK_COMPLETION_ASSESSMENT_V1`; `driver_id` must equal the current reviewing Driver; `task_id`, `publication_id`, `result_id`, `result_record_sha256`, and `original_hard_target_disposition` must bind the current persisted raw Result; `disposition` must be `SATISFIED`; `terminal_scope` must be `TASK`; `assessment` must be a nonempty bounded judgment.

The failed draft report instead used only:

`schema, terminal_scope, disposition, result_id, result_sha256, assessment`

It therefore omitted `driver_id`, `task_id`, `publication_id`, `original_hard_target_disposition`, used the noncanonical key `result_sha256` instead of `result_record_sha256`, and did not satisfy the exact-field set before any later binding checks could run.

The raw Result's `original_hard_target_disposition` is:

`PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`

A Driver Task-completion assessment may explicitly judge the Task satisfied at Task scope, but that judgment does not rewrite the immutable Result field or strengthen the PCF5/PCF6 mathematics.

## CLASSIFICATION

- `VERIFIED_COMPLETE`: current-publication PCF Result freeze and predecessor 20-row prior-art/duplication evidence frontier.
- `VERIFIED_COMPLETE`: source-backed Driver session/authority existed for the failed attempt, and durable draft review/follow-up artifacts were published.
- `CORRUPT_OR_CONFLICTED`: only the failed draft completion-assessment payload shape for canonical review admission; this classification does not apply to the Result or mathematics.
- `UNFINISHED`: one lawful canonical Driver review write, then its required follow-up/materialization lifecycle.
- `UNKNOWN`: whether the existing follow-up draft will pass every downstream native gate after the completion-assessment defect is corrected. Do not infer success; let the canonical writer validate it.

## MINIMAL_RECOVERY

1. Before any retry, refresh current Enterprise Math main and check whether another independent Driver has already created a valid canonical review for `RR-96D4CCDABC18462C8D5F`. If yes, consume it and do not duplicate the review.
2. If no review exists, use a real current `RESEARCH_DRIVER` session with current source-backed authority. Do not borrow the old session or Driver ID after that execution context is gone.
3. The current Driver must produce its own pinned review report. Build the completion-assessment block from the current persisted Result bytes and the current Driver identity; recompute `result_record_sha256` at the review-write boundary. Do not edit the historical draft in place to impersonate its author.
4. Publish/read back the corrected review artifact, then invoke the canonical `review` writer once. A failed writer attempt is not a review and must not be converted to acceptance by prose.
5. If the review succeeds, immediately inspect the canonical review record and `research_driver_followup` state. Complete only the typed follow-up/materialization required by current source; do not create a second review to advance the queue.
6. Preserve PCF scope exactly: no historical-novelty claim, factoring speedup/lower bound/universal algorithm claim, general H-dependent impossibility claim, or replay of the verified 20-row audit.

## CLIENT_GUARD

Driver clients preparing Task-scope closure must read the current completion-assessment schema from Source instead of inventing a shortened JSON block. Before `review`, verify the assessment field set is exactly the current source-required set and that every Result/Driver binding is current. A native `NATIVE_VALIDATION_REJECTED` result caused by the assessment schema is a client/control defect to repair; it is not review-authority failure and not a research blocker.
