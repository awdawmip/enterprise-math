# Parity m7 CONTROL v2: independent changed-scope and full-binding static review

Reviewer: EM-DVR-BFF6DC, genuine Driver SID MCP-47562f9f432d4978a7bea0dd60ecc4aa / DA-144D0C4639CACEEE75DC.
Disposition: **CONTROL_REVISE / NO_START. One remaining mandatory interface defect.**
This report is a separate immutable review of the new v2 package. It does not amend the original v1 REVISE, the original eight-file scientific candidate, or the historical Taskbook V1.

## Exact object and review method

The frozen local input is Root EM-DVR-18C67B's FROZEN_CONTROL_LAUNCHER_CODEC_V2_HANDOFF.json, 3516 bytes, SHA256 f6ee1e806738d03c4b4a380283b60e0e8fa13b3deab063cee286b0532425bbff. It binds these five members, 72477 bytes total:

| Member | Bytes | SHA256 |
|---|---:|---|
| parity_m7_launch_v2.py | 20903 | 1ece17be25f1af557ef8cd70e45b036b3d444979d934350b63fc9e645d4de323 |
| parity_m7_source_codec_v2.py | 5404 | 686ee4a0729011c274d9a1ad36be8d9dcf1ad13af2e22ff39f5fdb8df9f53225 |
| test_control_only.py | 7571 | 891c9edc227205afe161f1b0abcb672e04d1f1dc681874254d8c75d01c9a4bb6 |
| CONTROL_RESOURCE_CUSTODY_AND_RUNTIME_BINDING.md | 13170 | 6459dfe7f6571edfe277507bb9d9e33ab60aeb3167cc978ff58b4732d8e2fbb9 |
| EXACT_V1_TO_V2_CONTROL_DIFF_AND_COST_GATE.json | 25429 | f7c6180de705841b6a9e0f393d80301968bd571e761531541c9cb680439e7cda |

I personally read all five complete members and the complete handoff and verified their full UTF-8 bytes, SHA256 and Git blob hashes against the handoff. I also reconstructed the four unified text diffs with CONTROL-only string/file operations and verified exact equality to the frozen diff declaration. Codec v2 has exactly the same bytes and Git blob as codec v1; only its filename changed. The original v1 four-member freeze remains unchanged.

The scientific integration object remains author EM-DIRECT-88303D's exact eight files, 57773 bytes, and original 7926-byte handoff at actual Source 443361c5cfef441b73bb838984ffb6b6830bb357. The original science handoff SHA is 5ae056c2d670101cf64696b12364ce36c2efacbd96185269ada20d2c780ce41c. This review includes the interface of the unchanged workload, budget, output schema and execution contract; it does not rerun their algorithms. The earlier independent scientific-core static PASS and full-package REVISE are actual Source 1b16addb9b95bd48ac0230bf48bf323738ccf743. The original v1 CONTROL report is 17522 bytes / c0466f9076652f361557510ac3f80c94dd6e7f3402587f4ca3ccca7d2e9048d8, now actual Source 1f5a27f625bfd65e59ed74109bd5dd4041fb76be with its original 1292-byte freeze, exact two added notes.

At this report's freeze, the new v2 input was consumed as FROZEN_LOCAL_CANDIDATE_PENDING_SOURCE_PUBLICATION. A later actual immutable v2 Source requires a separate fresh full-byte binding; no future commit is asserted here.

This is a NONBLIND review. I previously reviewed the scientific core and v1 CONTROL layer, prepared a local nonpublished Taskbook as the assigned Driver, and reviewed the Owner resource contract and historical cost provenance. Root wrote both CONTROL versions and ran its own synthetic tests. The scientific author wrote both producer and checker. I supplied no mathematical algorithm, certificate, candidate repair, or replacement implementation. My review used text reading, hashes, JSON metadata and exact text diff checks only: **zero candidate imports, AST parses, compilation, smoke tests, numerical samples or scientific executions**.

Root's stated eleven final synthetic CONTROL tests were read as source definitions; I did not run them and do not present them as my observations. They provide Root-attributed regression evidence for their specified fixtures, not a scientific certificate or genuine Native authorization. In particular the post-start-failure test mocks both metadata validation and collect; it does not create a scientific child.

## Mandatory finding V2-C4B: binding failures inside the workload are misclassified as 70

The v2 fix correctly distinguishes the initial launcher file/hash phase from ordinary code/checker errors, but its phase boundary is too early for the frozen interface.

In parity_m7_launch_v2.py:

- Lines 278–286 verify the original handoff and the eight frozen candidate files while stage is INPUT_HASH.
- Line 292 switches stage to CODE_CHECKER.
- Line 298 then calls the unchanged workload.run_from_bytes.
- Line 315 returns 64 for a ValueError/OSError only while stage is INPUT_HASH; the same exception in CODE_CHECKER returns 70.

The unchanged workload performs additional binding checks after that switch. In original workload.py lines 53–66 it resolves the required pinned mathematical-source carriers and checks byte limits, SHA256 and Git blob; lines 59, 63 and 66 explicitly raise ValueError for a binding mismatch. A missing required carrier also raises an OSError subclass in this same path. Lines 70–85 subsequently check the four implementation carriers and their byte/SHA/blob bindings, with explicit ValueError mismatches at lines 71, 77, 81 and 84. None of these paths is a mathematical checker disagreement.

Consequently an honest missing source carrier, or a carrier whose bytes differ from the admitted source pin, is classified as 70 by v2. This follows directly from the text and exception flow; I did not create or execute such an input. The initial eight-file launcher check does not eliminate this case: those eight files exclude the five mathematical-source bodies loaded from repository_root by the workload.

The immutable EXECUTION_CONTRACT.json launcher_exit_contract["64"] expressly covers “Malformed input or code/source/manifest binding mismatch; no accepted certificate.” Its ["70"] covers “Scientific code exception or checker disagreement; no accepted certificate.” The v2 resource document likewise promises input/hash64 and code/checker70. The current implementation therefore does not satisfy the full frozen exit contract.

**Required outcome:** all original contract binding failures must retain the declared binding-failure disposition, while genuine scientific-code/checker disagreements retain their declared disposition. A new immutable candidate must demonstrate the complete boundary by static interface evidence and any author-owned CONTROL-only tests it uses. This report supplies no repair code and does not amend the scientific workload or its exception types.

Both current exits reject a certificate. This defect neither produces a false trace sign nor supplies a mathematical counterexample; it remains mandatory because exact failure reporting is part of the admission and no-retry workflow. A Native or manual wrapper must not silently reinterpret the frozen exit meanings.

Provenance of this finding: I independently sent this exact stage/source-carrier difference to Root after reading v2 and the original workload. The scientific author then independently sent the same locators as an author-side confirmation; Root had also supplied the earlier v1 checker-exception concern. This disclosure does not turn either author's observation into an independent review vote.

## Disposition of the original C1–C5 findings

C1, output snapshot contamination: **resolved in this changed scope.** V2 removes the hypothetical meter precharge. The original shared meter therefore has output_emitted=0 when workload.py records its pre-final-serialization snapshot, as required by OUTPUT_SCHEMA.json. The unchanged workload serializes once and charges its returned bytes once. After the workload returns, launcher lines 299–300 require result length at most 8MiB minus 65536 before stdout emission. Excess is a BudgetStop, not a truncated complete certificate. Parent stdout cap independently enforces the same result bound.

C2, final freshness and preparation cutoff: **resolved for the declared captured-start boundary.** The original genuine Native/Source observation is retained in the validated evidence. V2 fsyncs PREPARED and the attempt directory/parent first, then calls final_start_clock at line 364. That function rechecks observation age in [0,60] and now strictly before 06:53:04 UTC, and captures UTC and monotonic job origins. Candidate/repository path resolution, Popen/preexec/interpreter startup, imports, hashes and compilation are subsequent job work and are charged to that same origin; this is not a new clock started only at Budget construction. There is no claim that a later child wall-clock instant itself is before the preparation cutoff: the declared phase transition is this captured whole-job start. A forged local timestamp is not evidence of freshness; the actual actor must first have made the genuine observation.

C3, replay across resumed generations: **resolved in the honest fixed-store scope.** attempt_path now returns parent/TASK, independently of RUN, claim and generation. Exclusive mkdir therefore refuses the same unit after a resumed generation or claim succession if its durable attempt directory remains. PREPARED/UNKNOWN must be retained. This is one actual actor's stable per-unit storage obligation, not a distributed idempotency service and not protection against choosing a new alias or deleting evidence. The actual workflow must bind and preserve that same directory across succession.

C4, checker ValueError reported as input failure: **the original checker path is resolved, but V2-C4B above remains.** Stage CODE_CHECKER correctly sends the original checker disagreement ValueError to 70. It also sends later source/input/code-binding errors to 70, so the full required distinction is not yet established.

C5, post-start custody failure misreported as denied77: **resolved for caught ordinary exceptions in this scope.** SCIENCE_ATTEMPTED is set before the single collect/spawn attempt. An ordinary parent collect or custody exception after that flag produces 70 with explicit worker_may_have_started=true and UNKNOWN/noRetry. PREPARED remains. A pre-attempt metadata failure remains 77/no worker may have started. An unknown spawn is conservatively treated as possibly started. Process termination/power loss may produce no final receipt; surviving PREPARED still means UNKNOWN and never authorizes a new invocation. No machine receipt is promised after a process cannot run.

The initial v1 report remains REVISE with five findings; these v2 dispositions neither overwrite its bytes nor retroactively state that v1 was acceptable.

## Whole-job resource and output interface

The launcher's eight exact size/SHA pins match the original scientific handoff. Inside one child, it rechecks the freeze and all eight files before loading the scientific budget and workload. It uses cached verified bytes for those two loads, while the original workload checks its own implementation carriers before producer/checker loading. Original-source and implementation checks occur within the same science job and inherited memory ceiling. This ordering does not make their failure-exit classification correct; V2-C4B still applies.

A single original Budget receives the genuine parent monotonic start. There are not separate producer and checker 300-second or 20M-operation allowances. The original exact-operation and rational bit counters remain in the frozen algorithms; no output is computed in this review. Static enforceable ceilings do not prove that an actual successful run fits them. A real run may stop at time, memory, operation, integer-bit or output limits with no trace-sign conclusion.

The parent sets the timeout from the remaining time since the same start and collects bounded pipes; the child inherits RLIMIT_AS512MiB, RLIMIT_CPU300, RLIMIT_FSIZE8MiB and zero core dumps before the new interpreter. Original Budget checks and its timer use the same start. The documented address-space scope is the scientific child, not total model memory, parent Python RSS, filesystem cache or an externally measured global peak. CPU and peak_RSS are explicitly null/UNKNOWN in the outcome. RLIMIT_CPU and an address-space ceiling are not measured actual cost.

The seccomp filter checks Linux x86_64 architecture, denies x32, and blocks the declared socket/network syscalls with no inherited network descriptor under the normal subprocess setup. Unsupported platforms fail before science. This is a network restriction for the frozen cooperative workload, not a general sandbox for hostile Python or a protection against arbitrary actor invocation of internal child mode. Only the legitimate parent workflow is the admitted entry.

Output accounting is coherent in the intended byte-payload model: child result <=8MiB−64KiB, stderr <=16KiB, and PREPARED/outcome/stderr/tiny receipt together <=64KiB. The parent emits a small receipt rather than duplicating the certificate to stdout. Overflow, timeout or incomplete/exceptional outcome cannot be marked a complete scientific candidate. An oversize or failed persistence may leave only a partial artifact plus PREPARED; that is an honest incomplete/UNKNOWN attempt with no retry, not an accepted certificate.

Status0 and2 remain only complete-candidate labels: respectively all coefficients positive, or this fixed certificate plan inconclusive. Neither is Native acceptance. An actual independent full result review, complete raw artifact custody, and the actual Native workflow would still be required. No result, coefficient sign, certificate length, measured runtime or successful scientific invocation has been generated here.

## Report codec, custody and outstanding per-run bindings

The unchanged ASCII codec copies, hashes and partitions the exact returned raw byte string; it does no polynomial recomputation. It admits at most8MiB raw, 32 ordered parts of at most262144 bytes and an index of at most32768 bytes. The maximum carrier payload is 8421376 bytes. Raw job evidence up to8388608 bytes plus this carrier is at most16809984 bytes, below17MiB. Every original part's bytes/SHA/Git blob and the reconstructed original length/SHA are checked by unpack. It neither uploads Source nor authorizes a Native artifact path.

The codec's report_started_monotonic must be the actual report origin, including semantic/persistence work before pack, not the time pack happens to begin. The actor must record the actual observation/report origins and all later elapsed costs in the per-run handoff and compare the final ledger to the separate300s report cap. A successful local pack does not certify completion of subsequent transport or all reporting within300s. In particular no worst-case Source network latency bound is proved by the 33-file carrier size or Root's synthetic roundtrip. If reporting/custody is incomplete or over budget, preserve the actual raw result and honest nonterminal checkpoint; do not repeat science.

The v2 resource document's reference to parity_m7_source_codec_v1.py is a stale filename for the unchanged codec bytes. This is a nonblocking locator issue for this static object because the exact v2 handoff and file pins are unambiguous; the final Taskbook/handoff must use the actual v2 Source path and hash, not a filename inference.

Before any Task publication/claim/execution, the following genuine integration objects still have to exist and be fully consumed:

1. A newly accepted complete candidate fixing V2-C4B, exact immutable CONTROL Source, and fresh complete reviewer binding. No old PASS covers the new code automatically.
2. A new Taskbook version and canonical record with the actual Parity mother Task and actual OPEN Goal generation, permitted executor/scope, current policy and exact scientific/CONTROL/input/review/Owner-cost Source pins. The historical19723-byte local Taskbook V1 remains unchanged and unpublished.
3. The real selected Researcher's own stable session/current RA and genuine task-read, prepare_exact, claim and open/latest-resume receipts, actual winning Issue events, ER, current generation and current ownership epoch. No Source-main grant, Driver title or local boolean supplies them.
4. A complete verified isolated canonical guard tree including every Python dependency and all loaded policy/JSON/data; a real guard result that agrees with the original Native authorization, Taskbook blob, branch/base and allowed_outputs; actual authentic freshness within60s at captured job start.
5. Exact per-run local input bindings, historical-cost continuation, positive prep remainder, stable per-unit attempt directory, report-origin recording, allowed output namespace, complete lossless Source carrier and bounded metadata/custody plan. Native/Source operations retain their real costs and original receipts.

These are explicit operational admission prerequisites, not additional mathematical defects invented to prevent reversible preparation. Local binding hashes establish consistency of consumed files; they cannot authenticate an invented receipt. I have not manufactured any of these missing actual Native objects.

## Historical preparation and final scope

I independently full-read and hash/blob-verified actual Owner contract Source927cde4c68437808b191d8464a4249375cab4367, 4509 bytes / fd76a558a101eaa2a2496d6827b4424a9ade534850bec16295327753adf6045e, and actual original cost note Sourcec0b15c38837c1c3a4d75d698c7329f3225dc2e39, 6235 bytes / cb95ea955cc42bda6fc211e7766f83a94dd3c037385947758d84ca3f546b657e. The cost note conservatively uses01:53:04 UTC as a lower anchor based on the author's genuine SID creation and explicit self-declaration that this unit was selected afterward. The actual task-specific start, historical CPU, peak RSS, exact operations and tokens are UNKNOWN. The conservative wall debit includes other scope, waits and unclassified intervals rather than treating them as zero. The self-declaration is disclosed, not platform attestation of scope choice.

The first explicit preparation cap is cumulative18000s with hard cutoff06:53:04 UTC; it does not retroactively replace the original future whole-science-job300s limit or wash prior costs away. The last12446s historical snapshot is not a frozen remaining allowance; every subsequent interval continues to count. The real actor must use the actual clock and ledger at start, without Task/actor/conversation or generation resets. Separate report300s and unchanged future science20M/300s/512MiB/8MiB/16384-bit limits remain distinct.

**Final disposition:** v2 makes substantial concrete CONTROL corrections, but one exact binding-failure exit defect remains, so complete package remains **REVISE / NOT_ADMITTED / NO_START**. Scientific core unchanged; zero new scientific executions or sign conclusions. No Task/claim/open, RA, Native science vote or mathematical Result is created by this report. All actual Source archives already reported here are data custody only. The broad research goal remains OPEN.
