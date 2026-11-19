# Research-rule follow-up: implementation audit and validation

Recorded: 2026-11-19T14:38:00+08:00
Classification: maintenance evidence; no new research rules or mathematical claims.
Initial Source snapshot: `b1efc6c805661ed7b476e6e730107da6043176ee`.

## Review decision / 复审结论

The November 18 rule changes are already present in main at
[`3097475290506e32677838dce0d24c72df57f28b`](https://github.com/awdawmip/enterprise-math/commit/3097475290506e32677838dce0d24c72df57f28b).
This follow-up preserves the working parts and corrects three remaining implementation/documentation defects. It does not turn input-size targets, behavioral experiments or bookkeeping into research-start prerequisites.

上一轮的 FREE A 分层、取消残差方法配额、科学保存与记账分层、原请求优先的控制短路由、P000 冲突证据记录及 BRC 专用范围区分，已在当前源文件中存在。本次不重复建立规则，而是修复真实遗漏，并明确验证范围。

## Corrections / 本次修复

### Actual connector observations

The Activity validator rejected the real tool label `mcp__codex_apps__github_fetch_file` although its full immutable response matched the existing supported structure. The change adds that exact label and preserves it in the original observation and sidecar. Repository, commit, path, complete content, Git blob and SHA-256 checks remain unchanged. Generic `fetch`, `fetch_blob`, approximate labels and partial reads are not admitted by this full-file observation contract.

The actual read used `control_plane/research_delivery_policy.json` at the initial Source snapshot, blob `f407a7922ba0e3e20ee50c945ff3f167224bf9d2`. Its original envelope is in [activity_observation.json](activity_observation.json), original rejection in [activity_baseline_rejection.json](activity_baseline_rejection.json), and fixed local verification in [activity_validation.json](activity_validation.json). The local observation ID is not a server call ID or signature.

Activity documentation now says explicitly that session visibility remains required and a missing association remains bookkeeping debt; independent reasoning and scientific-file preservation do not require preregistration. This clarifies the existing scopes without changing identity or execution authority.

### Method alternatives in Phase B

The bilingual Phase-B reference now includes the machine contract's existing `ALTERNATIVE_APPROACH_CHOSEN` state. A useful independent implementation may have the same input/output capability as an existing tool. A capability gap is not required. Actual choices and meaningful comparisons belong in the existing result. Novelty/shared-tool acceptance still requires the relevant comparison; alternative choice alone does not prove novelty.

### Historical coordinate gate

The original [job 134982513988](https://github.com/awdawmip/enterprise-math/actions/runs/44355533210/job/134982513988) at candidate `3097475` recorded 65 baseline passes / one baseline failure and 66 candidate passes, then failed at `old.keys() == new.keys()`.

Commit [`dd7b10b680fc7a0c69e551ccf793f7e77d131b65`](https://github.com/awdawmip/enterprise-math/commit/dd7b10b680fc7a0c69e551ccf793f7e77d131b65) had deliberately retired fixed-heading admission and changed four test identities and their assertions. The comparator had not represented these four successors.

The fix maps only those four complete class/method identities from the fixed historical baseline. Their current successors must all pass, even if the historical case failed. Missing, added, duplicate, skipped and errored tests still fail the gate; other new failures and changed failure details still fail. All seven original test files remain unchanged by this follow-up.

## Verification / 实际验证

| Check | Observed result and scope |
|---|---|
| Foundation package generation | `python tools/build_em_foundation_startup.py --check` passed at the initial Source snapshot. |
| Foundation reader | 24 existing tests passed: exact source coverage, cache mismatch/rebuild, frozen scientific refs, bounded error output, precise lookups and executable dependencies. |
| FREE role compatibility | 10 focused tests passed. The separate full-control integration case was not completed in the partial local snapshot. |
| Phase-A integrity and discovery | 11 existing fixture-free tests passed via direct standard-library invocation; this was not reported as a pytest run. |
| Phase-B edited reference | Existing `check_free_role_contract` accepted the edited English reference and used its exact staged read path. Both language versions were compared for equivalent meaning. |
| Activity observations | 37 existing/extended tests passed; [log](activity_tests.log). Actual connector envelope and sidecar round-trip passed. Twelve malformed variants were rejected. |
| Coordinate comparator | Eight tests passed against the final staged file; [log](coordinate_comparison_tests.log). They test constructed XML, exact mapping and preserved rejection behavior. |
| Historical 66-case execution | Reused only as dated CI evidence at `3097475`. The seven target test files have the same blobs at that candidate and the initial Source snapshot. The 66 mathematical tests were not rerun locally in this follow-up. |
| Lean | The original failed job stopped before any subsequent Lean/lake step. No new Lean-kernel success is claimed by these checks. |

FREE A currently contains 45,494 characters / 45,926 UTF-8 bytes; the ordinary package contains 56,042 characters / 56,474 bytes. Both retain the same five pinned sources. P000 axioms, type semantics, conflict policy, invariants and hard errors are preserved. Eight general branch-type commitments are in the initial view; twenty detailed commitments use relevant-question-triggered lookup.

These are source-size and executable-reader observations. They do not measure independent-question diversity, real model behavior, startup latency or end-to-end research efficiency. The reviewers inherited the audit context and were not clean blind research samples.

## Scope of remaining verification

The live console status request returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false` during this review. Repository reads and local tests remained available. This artifact does not assert backend deployment, restored console connectivity or successful business writes.

No real research identity, CLAIM, Result, Review or Activity was created by these tests. No original control request was replayed and no schedule changed. Existing scientific inputs and protected foundations are outside the changed-file set.

The exact changed source/test blobs are in [changed_files.json](changed_files.json). Publication uses the fresh repository parent and checks the expected old file blobs; the final publication receipt and scoped remote readback are reported separately by the integrator.
