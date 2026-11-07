# Conversation-first validation

Status: review candidate; only bilingual-sync automatic triggers are proposed for manual fallback. No remote workflow has been changed.

## Purpose and boundary

Use an available authorized conversation execution environment for validation,
then publish a coherent, validated checkpoint through the connected GitHub
service. A conversation without executable tools is not a validation executor.
Do not silently dispatch Actions as a substitute for unavailable local checks.

The local entry point covers `quality`, `reference-integrity`, and
`bilingual-sync`. This patch changes automatic triggers only for `bilingual-sync`;
quality and reference-integrity remain automatic. Preserve all checks and propagate real failures. Local receipts
are evidence for review; they are not GitHub check runs, review approval,
mathematical admission, or permission to merge.

## Execution contract

- Use Python 3.12 and the exact candidate source tree in a complete checkout
- Use `scripts/run_conversation_validation.py --help` for the local entry point
- The command manifest is pinned to the source workflow bytes. A changed
  workflow must be reviewed and its manifest regenerated before execution;
  never remove the drift guard merely to make a run pass
- Quality uses `scripts/run_unittest_shard.py --index 0 --count 1`, preserving
  supported top-level test functions, unittest cases, fail-closed discovery,
  operational bootstrap, and the isolated P017 regression. Do not substitute
  plain `unittest discover`, which misses supported function-style tests
- Reference integrity keeps every current command in its existing order and
  stops dependent steps after a failure, matching the original job
- For bilingual same-change validation, supply the real comparison base SHA
  present in the checkout. Explicit full-snapshot mode checks structural pairing
  only and is not evidence that both members changed together
- Keep receipt files and command logs outside tracked source. Record source
  identity, interpreter, workflow/command digests, exit statuses, and omitted
  checks. Partial, failed, interrupted, and unavailable checks must stay visible

## Verified baseline, 2026-09-30

Source: `be31c9c1928a40cebfb390ad97f37868c8b1b5a5`.
The GitHub reference-integrity run
[`36651458428`](https://github.com/awdawmip/enterprise-math/actions/runs/36651458428)
failed in the existing registered-migration dry run. The same command and the
same three source blobs reproduced the same error locally with Python 3.12.14
and exit status 1:

`requested pending migrations do not share one exact baseline blob`

Command: `python control_plane/apply_registered_json_migration.py --migration-id
CSM-RUNTIME-CANONICAL-DISPATCH-004 --migration-id
CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006`.

This is a pre-existing validation failure, not a successful admission. The
migration does not change its inputs or suppress the failure.

## Verified scope and activation

The complete structural bilingual input set (131 registered pairs plus all
other bilingual-named documents in the pinned docs tree) reproduces the four
pre-existing unregistered-document errors in GitHub run
[`36651458393`](https://github.com/awdawmip/enterprise-math/actions/runs/36651458393),
with exit status 1. All 266 fetched prose/template blobs match their Git blob
identities. The real candidate/base same-change comparison was not executed in
this materialized snapshot; the local runner requires a valid clean Git checkout
for that mode and tests its fail-closed preflight.

The 34 reference command definitions match the original workflow exactly. Only
the already failing migration dry run was reproduced locally; the full reference
suite has not been executed. The complete quality suite has not been executed.
Runner unit tests verify the entry point, not the whole research repository.

The proposed first activation changes only bilingual-sync to explicit manual
fallback after user review. Its workflow/job name, commands, concurrency, timeout
and permissions stay unchanged. Quality and reference-integrity continue their
existing automatic checks. Any later trigger migration requires complete local
execution evidence and current check-consumer review. Existing failures stay
failures; no local result automatically satisfies a remote required check.

Keep the authenticated ChatGPT dispatch bridge until equivalent source-bound
event intake and durable receipts are actually verified. Keep Lean validation
until the pinned toolchain/dependencies are locally available. This migration
does not change Cloudflare/security workflows, research-evidence archives,
artifact retention, billing, global-knowledge indexing, or merge/deploy rights.

Batch coherent conversation checkpoints before publication. Do not use skip-CI
markers as a permanent substitute for a reviewed trigger migration.
