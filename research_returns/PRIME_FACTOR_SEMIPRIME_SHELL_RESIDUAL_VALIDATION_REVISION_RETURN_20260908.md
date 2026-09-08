# PFSSV generation-2 correction return: complete observations and a null-support boundary

Status: CANDIDATE_RETURN_AWAITING_RESULT_FREEZE_AND_DRIVER_REVIEW

```json
{
  "task_id": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION",
  "publication_id": "TP2-2029B5CCC5EEC5F0132C",
  "execution_record_id": "ER-EB2A78D7B88A292B412B",
  "terminal_verdict": "NEGATIVE_BOUNDARY",
  "hard_target_disposition": "PARTIAL_OBSERVATION_COMPLETE_NULL_SUPPORT_FAILURE_HARD_TARGET_OPEN",
  "method_harvest": "RESULT_ONLY",
  "independence": "SHARED_AMBIENT_CONTEXT_DISCLOSED",
  "source_exposure": "NONBLIND_DISCLOSED"
}
```

The original 21-cell observation design was completed once with exact generator bounds, complete geometric support, genuine prime-rank coordinates and full serialized observation profiles. Every cell has a deterministic counterexample to interpreting every draw of the original Null A scalar permutation as an admissible occupancy of its specified factor windows. Eighteen cells retain counterexamples after restricting to positive-total-count rows; three have only zero-total-target counterexamples in this audit. The scientific corrected/signed residual, two-null, family-wise and blind-validation gates remain undischarged.

`NEGATIVE_BOUNDARY` describes this supported model-interpretation boundary. The mother target `SEMIPRIME_FACTOR_SHELL_CROSS_SCALE_RESIDUAL_STRUCTURE_VALIDATED_OR_REFUTED` remains open. This return does not choose any of the original strong residual-artifact or no-stable-residual terminal classes. The parent Objective also remains open.

## 1. Scope, authority and source versions

This is the same-task revision of the original experiment, under claim `chatgpt-pfssv-r2-20260908T101753Z-456f906e`. The actual claim comment was 5583750861 at 2026-09-08T10:31:14Z; same-claim progress comment 5584381966 at 11:24:30Z extended the observed lease to 13:24:30Z. Canonical runtime authorization was performed by the owner before the execution. This document does not create a claim, a Driver review, a Result, Working Truth or a theorem status.

Stage 1 and the bounded Driver decision were published at [01b6dd932f62fd3b0a6f3b06d29ff809b04ed62e](https://github.com/awdawmip/enterprise-math/tree/01b6dd932f62fd3b0a6f3b06d29ff809b04ed62e). The decision is [PFSSV_GENERATION2_CAPACITY_GATE_DECISION_20260908.md](https://github.com/awdawmip/enterprise-math/blob/01b6dd932f62fd3b0a6f3b06d29ff809b04ed62e/driver_reviews/PFSSV_GENERATION2_CAPACITY_GATE_DECISION_20260908.md), SHA256 `cfdf23aebe6cb38c3051062218b9ce691a506dcd1f6ee22eb4dfa7a733b5b0ae`. It authorized full observations and deterministic capacity auditing while suspending the 512/4096 scientific null screens.

The actual Stage 2 source and precompute contract were published at [f662d48f4615fe6d08a55225c7c36ecd15f91518](https://github.com/awdawmip/enterprise-math/tree/f662d48f4615fe6d08a55225c7c36ecd15f91518). The precompute version of `research_artifacts/PFSSV_REVISION_20260908/result_summary.json` has SHA256 `7a7e8fe1a11fe157130c4fdf93638db08f54095f6ae5adf20be663d10edf036b`. Its nested `stage2_precompute_contract` is preserved exactly in the final summary, which records that actual prior commit and hash. The executed script SHA256 is `a6a604207d189c10ba8146ca8e9897b4ce9b62b38b38682044a0f981f74e8cc0`; its focused test SHA256 is `4b6e4ce41d0580fd4d697e673e9ad1d0456a3176957a9ead28f30a2cc64a6c61`.

The original script, experiment manifest, discovery freeze, summary, return, Result and execution record remain historical bytes. The new execution record, 34 protected source pins and five additional retained Stage 1/Driver files were checked unchanged. Stage 1 output versions remain in their immutable published source and frozen capture. This return and the six actual Stage 2 output versions are identified durably by the subsequent Result's actual `owner_head`.

The five discovery scales remain 100000, 300000, 1000000, 3000000 and 10000000; the two previously exposed holdout scales remain 30000000 and 100000000. Each uses widths 1/100, 3/1000 and 1/1000. The latter six observations are post-exposure reanalysis. Changing a branch, researcher, seed or generation cannot restore blindness. The author worked within shared ambient context, including the original return, Driver defects and the Stage 1 capacity finding; no blind PRE_MATH stamp is claimed.

## 2. What the exact observation repair does

For each width, let U be the exact floor of X times its rational width multiplier. For every prime p at most floor(sqrt(U)), the allowed q window is

\[
L=\max(p,\lfloor X/p\rfloor+1),\qquad H=\lfloor U/p\rfloor.
\]

Empty integer windows are recorded separately. Every nonempty geometric window is retained even if it contains no primes. The implementation uses a complete bounded prime prefix through 50500000, containing 3029296 primes in this run. This prefix suffices because p is at least 2 and U is at most 101000000. The exact generator uses the existing additive sieve construction with BRC DIV/ROOT bounds; the independent trial-prime spot-check helper declares the finite domain 0 through 50500000 and makes no generic 64-bit Miller-Rabin claim.

With a=pi(L-1) and b=pi(H), q's true ranks are the interval (a,b]. The p coordinate is pi(p) in the complete prefix, independent of whether its observed row is zero. A fixed rank bin (k_j,k_{j+1}] contains exactly

\[
\max(0,\min(b,k_{j+1})-\max(a,k_j))
\]

of those q ranks. The complete rank intervals and the 24-by-24 observed rank grid preserve the joint observation; they are not a joint null model. Full 24-bin raw, p>31, p^4>X and density-flattened observation vectors are serialized, alongside every row's integer bounds, counts and all 30 residue-channel counts.

BRC LOG interval refinement determines the requested coordinate bins, including zero-observed rows that could receive positive permuted mass. Failure to separate a bin would remain an explicit precision boundary. No such boundary was reported in this completed run. Valid rows with p^2>X have u>1/2 and are tracked as overflow instead of being clipped into a density-flat bin. Overflow mass and diagonal p=q counts are distinct and both are preserved; overflow can contain off-diagonal pairs. The old overflow band-7 rule is explicitly tagged only for the original Null A capacity audit. The S3 map remains a derived diagnostic through the original coordinate interpretation; its reconstruction and the bounded orbit checks do not assert that every orbit figure was rendered. Figures are not the original acceptance criterion.

These are task-local T0_BRC and T1_SCALE_ENUMERATION_VALUATION compositions: exact quotient/root boundaries, complete-prefix cumulative count differences and lossless rank-bin interval intersections. The harvest is a `RESULT_ONLY` correction/boundary, not a new global tool family, a primality theorem, or blanket certification of unchanged legacy scripts and every transitive numerical dependency.

## 3. The deterministic Null A obstruction

Within an original coarse-band/p-residue stratum and one q-residue r, a permitted permutation can send any specified source row's channel count to any target row. If the stratum has n rows, that specified assignment has probability 1/n. Let C_r(L,H) be the number of integers of residue r modulo 30 in the target window. It is obtained from the first such address and a BRC quotient bound. If the maximum source channel count exceeds C_r, at least one positive-probability assignment cannot fit into the target's integer residue slots, even before requiring those slots to be prime.

The run audited all applicable strata, all eight original admissible q residues and every target. It performed no random draws, truncation, rejection sampling or distribution repair. It recorded clean target outcomes as well as violations. Capacity nonviolation alone would not prove prime-process validity, finer-window coherence or a joint allocation law.

All 21 cells have capacity counterexamples. The table separates violations with positive-total targets from those with zero-total targets. The source of every violating maximum has positive total count. Therefore, when the target also has positive total count, that specified assignment remains reachable on the positive-total subset of the declared stratum. This is a deterministic support comparison, not a replay of old floating-point code or old random draws.

| X | width | raw pairs | p>31 pairs | p^4>X pairs | zero-total rows | all violating target channels | positive-total targets | zero-total targets |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|
| 100000 | 1/100 | 237 | 70 | 91 | 15 | 25 | 14 | 11 |
| 100000 | 3/1000 | 74 | 23 | 29 | 34 | 4 | 0 | 4 |
| 100000 | 1/1000 | 25 | 9 | 12 | 30 | 1 | 0 | 1 |
| 300000 | 1/100 | 610 | 208 | 226 | 7 | 122 | 106 | 16 |
| 300000 | 3/1000 | 183 | 58 | 63 | 49 | 30 | 7 | 23 |
| 300000 | 1/1000 | 65 | 24 | 25 | 59 | 8 | 0 | 8 |
| 1000000 | 1/100 | 1960 | 683 | 683 | 5 | 248 | 231 | 17 |
| 1000000 | 3/1000 | 585 | 203 | 203 | 58 | 209 | 105 | 104 |
| 1000000 | 1/1000 | 196 | 69 | 69 | 99 | 113 | 40 | 73 |
| 3000000 | 1/100 | 5826 | 2257 | 2126 | 0 | 304 | 304 | 0 |
| 3000000 | 3/1000 | 1743 | 666 | 629 | 45 | 681 | 516 | 165 |
| 3000000 | 1/1000 | 583 | 219 | 209 | 135 | 475 | 182 | 293 |
| 10000000 | 1/100 | 18161 | 7459 | 6522 | 0 | 723 | 723 | 0 |
| 10000000 | 3/1000 | 5472 | 2240 | 1950 | 26 | 1137 | 1012 | 125 |
| 10000000 | 1/1000 | 1832 | 754 | 660 | 146 | 1506 | 854 | 652 |
| 30000000 | 1/100 | 52396 | 22419 | 18137 | 0 | 916 | 916 | 0 |
| 30000000 | 3/1000 | 15664 | 6676 | 5411 | 13 | 1381 | 1343 | 38 |
| 30000000 | 1/1000 | 5201 | 2222 | 1805 | 136 | 2715 | 1953 | 762 |
| 100000000 | 1/100 | 167952 | 75029 | 58534 | 0 | 941 | 941 | 0 |
| 100000000 | 3/1000 | 50326 | 22437 | 17464 | 0 | 3270 | 3270 | 0 |
| 100000000 | 1/1000 | 16827 | 7523 | 5818 | 89 | 3281 | 2883 | 398 |

There are 18090 violating cell/target/residue entries: 15400 with positive-total targets and 2690 with zero-total targets. These entries overlap across widths and channels; they are not independent statistical trials, a number of distinct primes, or a p-value. Eighteen cells have positive-subset witnesses. The three cells with only zero-total-target witnesses in this audit are (X=100000, width=3/1000), (X=100000, width=1/1000) and (X=300000, width=1/1000), with respectively 4, 1 and 8 violating entries. The corrected geometric support includes those targets; no inference that the old support satisfies all other scientific gates follows.

A concrete original-scope positive-subset witness is X=100000, width=1/100: p=193 and p=163 both have total row count 2. In coarse band 6, p mod30=13 and q mod30=11, source p=193 has channel count 1. Target p=163 has q in [614,619], observed channel count 0 and integer residue capacity 0. The specified assignment has probability 1/2 both in the full two-row stratum and in its positive-total subset. This obstruction does not require adding a zero-total row. The earlier Stage 1 probe's p=97/p=127 witness also had total count 2 on both rows; that probe was not substituted for this 21-cell audit.

The supported boundary concerns the universal factor-window occupancy interpretation of this original scalar permutation. The scalar count surrogate still defines a mathematical distribution. This return does not prove that every conditional-randomization approach is invalid, that a future properly stated surrogate is useless, or that prime or semiprime residual structure does not exist. It also does not infer that the original Null B separately failed: that scientific screen was not rerun under the bounded Driver decision.

## 4. Accounting for all eight original output obligations

| Original obligation | Actual delivery and remaining boundary |
|---|---|
| 1. Exact generator and independent spot checks | Complete 21-cell exact observations, complete bounded prime prefix and true rank intervals are delivered. The published Stage 1 new probe and bounded contract tests supply independent spot checks. There was no second independent enumeration of every pair in all 21 cells. |
| 2. Frozen manifest and exposure state | The original historical freeze is preserved; the immutable correction/native plans and the published Stage 2 precompute contract document this revision. The latter was published before this execution. Prior holdout exposure cannot be repaired into a historical blind freeze. |
| 3. Raw and corrected occupancy for every cell/view | All 21 raw, trimmed, density-flat and observed joint-rank profiles and complete row ledgers are present. Scientific corrected, signed-residual and null vectors are explicitly unavailable (`null`), not zero. Derived orbit representation is preserved; no exhaustive figure-rendering claim is made. |
| 4. Two independent null families with valid support | Original Null A received the complete deterministic target-capacity audit and has the stated occupancy-interpretation failure in every cell. The 512/4096 A/B scientific screens were suspended and no new joint kernel was introduced. This obligation remains unmet as a two-valid-null scientific comparison. |
| 5. Fixed-coordinate cross-scale residual profiles and signed statistics | Complete fixed-coordinate observation profiles are serialized. Scientific corrected residual, signed phase and cross-scale correlation statistics were not computed under the stopped null contract. This gate remains open. |
| 6. Family-wise empirical threshold | No max-statistic null threshold, empirical null rank or calibrated residual effect size was recomputed. There are zero scientific null draws. This gate is explicitly undischarged. |
| 7. Blind holdout evaluation | Both original holdout scales were observed at all widths, with prior exposure disclosed. This is not a blind test; the original blind gate cannot be retrospectively satisfied. |
| 8. Replacement return with exact counts and failure modes | This candidate return, the complete six-artifact package and the discrepancy ledger report exact observations and the supported negative boundary. Formal Result freezing and Driver assessment remain owner actions. The strong science hard target is not closed. |

The three reported defects are separated in `discrepancy_ledger.json`: positive-observation support filtering is repaired for observations and explicitly tested for null capacity; the survivor-row `prime_rank` substitute is replaced by true pi(p),pi(q); and full profile serialization is restored. Serialization repair preserves the distinction between actual observation data and missing scientific corrected/signed/null values. A `PASS_COMPLETE_21_CELL_OBSERVATION_AND_CAPACITY_AUDIT` execution label is an engineering completeness label, not a scientific residual verdict.

The original primary family-wise statistic is one-dimensional. The task requires genuine two-dimensional observed prime ranks, which this revision supplies. It did not uniquely specify a new joint q-rank null allocation kernel; the absence of such a newly invented kernel is not added as a new acceptance gate. The existing one-dimensional two-null, signed, family-wise and honest-holdout obligations remain independently open.

## 5. Actual execution, tests and trace identity

The only full invocation was:

```text
python -B -X utf8 scripts/check_prime_factor_semiprime_shell_residual_validation_revision_20260908.py --observation-capacity --precompute-commit f662d48f4615fe6d08a55225c7c36ecd15f91518 --precompute-sha256 7a7e8fe1a11fe157130c4fdf93638db08f54095f6ae5adf20be663d10edf036b
```

It ran with the bundled Python in the authorized research tree from 2026-09-08T11:50:06.436916Z to 11:53:51.350972Z, exit 0. The external monotonic elapsed time was 224.922 seconds; the internal time including trace packaging, decoding and receipt preparation was 224.453 seconds. Final peak process memory, including postprocessing, was 180793344 bytes. The external 1800-second limit was not reached; memory remained below 2 GiB. There was no full-run retry. Stdout SHA256 is `3f7f03fd6f97efc228fba55d63a74e1095401f115afb97d6f0f6d247dc9ee572`; stderr was empty, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The final published source passed 18 targeted contract tests (0.087 seconds in unittest; 0.547 seconds for its subprocess) and the exact-arithmetic static checker on its two Python files. Tests include actual native code-object capture, zero support, true ranks, overflow and interval boundaries, full serialization, exact capacity checks, transport roundtrip, damaged/truncated/ordering/footer rejection and budget rejection. These bounded checks are not a claim of independent exhaustive certification of every mathematical value in the full run. Stage 1's separately preserved 11-test/probe execution is not relabelled as this generation of tests.

Before Stage 2 publication, a byte-only counterexample showed that the earlier decoder accepted a container whose final LF alone was removed. Raw payload bytes were still intact, but the JSONL truncation contract was weaker than intended. The decoder was narrowed to require terminal LF on every header/record, and the original corruption test gained the exact last-byte truncation rejection. The old source/precompute capture and actual failure were preserved, then the 18 tests and static check passed on the revised published source. This repair did not change mathematical observations or trace-event definitions. A prior multi-hunk patch application also failed context verification without applying edits; it was not a mathematical run.

Actual original native code-object call counts equal their captured trace-return counts: DIV 293797, LOG 8799 and ROOT 22. There are 302618 returned-trace events, represented by 99846 full trace definitions and exact repeated-reference events. This reports the mapped native functions actually observed; it is not certification of unchanged legacy numerical paths.

The raw event stream is 100831585 bytes, SHA256 `d230e70c3ffd99ff882324e7af5cffc80f41f6ca10da35356934a4851ae34669`. Its `PFSSV_TRACE_GZIP_BASE64_JSONL_V1` transport is 29555979 bytes, SHA256 `efc2bedcda8da81f9948098943815011024c2c6d2e7711f209151ed983192fa4`. There are 385 ordered chunks of at most 262144 raw bytes, each with its own raw size/hash and gzip+base64 encoding, plus a required whole-stream footer. Gzip uses mtime 0 and compression level 6. The full decoder verified all chunks, exact raw total/hash and equality with the originally captured event bytes during the actual run. Every returned event and integer is preserved; reversible hexadecimal integer representation is used when needed. The raw 512 MiB and encoded 50 MiB budgets were both respected.

The same source exposes a byte-only verification entry:

```text
python -B -X utf8 scripts/check_prime_factor_semiprime_shell_residual_validation_revision_20260908.py --verify-trace research_artifacts/PFSSV_REVISION_20260908/native_trace.jsonl
```

Optional `--decoded-output` writes a new local raw file while verifying it. This replay instruction performs byte decoding, not another mathematical experiment.

## 6. Exact actual output package

All paths below are relative to the repository. They are the six frozen output versions from the sole actual Stage 2 execution; Stage 1 versions remain separately preserved.

| Artifact path | Bytes | SHA256 |
|---|---:|---|
| `research_artifacts/PFSSV_REVISION_20260908/cell_profiles.jsonl` | 15697354 | `f681dd201b2fa1949e0961e7b4e1d5d22ddb4de33e09c4ad0582499b4a9b2885` |
| `research_artifacts/PFSSV_REVISION_20260908/generator_receipt.json` | 452 | `df6fa969b236d81c9e0b1b240e5ee76ebc8ca6b855b5e49023e17a8aa74f0409` |
| `research_artifacts/PFSSV_REVISION_20260908/native_runtime_receipt.json` | 2600 | `bbad0969b9e3713f71fc3f1b407db4a65b271dc74d0b0b8b26e890d270aded3c` |
| `research_artifacts/PFSSV_REVISION_20260908/native_trace.jsonl` | 29555979 | `efc2bedcda8da81f9948098943815011024c2c6d2e7711f209151ed983192fa4` |
| `research_artifacts/PFSSV_REVISION_20260908/discrepancy_ledger.json` | 1741 | `425ab5d81b4e518b41c7f4093445f3895f606578efe460087c06aecf33bdcc7b` |
| `research_artifacts/PFSSV_REVISION_20260908/result_summary.json` | 18798 | `1b6cf5586f7854b184ff3892a86fee3971362fb47f71fccd0bd0b8286fcf14c6` |

The final summary's nested precompute object was compared equal to the published precompute object. Its exact prior source remains f662d48f4615fe6d08a55225c7c36ecd15f91518 with the precompute hash stated above. The original-output preservation checks and the execution/trace identities are retained in the actual receipts. The cell/target mask classification in this return is an integer join over frozen `cell_profiles.jsonl` rows and audit targets, with no new generator calls or random draws; all six original execution outputs stayed byte-identical during that readout.

## 7. Remaining scientific need and handoff

Any further scientific attempt must first state an identifiable target and a statistical contract consistent with target capacity and the relevant fine-window coupling. It must distinguish a scalar surrogate from a factor-window occupancy model and explain which one is being calibrated. Only then should the Driver assess whether a successor has enough value to justify a new bounded task. This return does not initiate a null family, a fresh blind experiment or an auxiliary second-order route. The existing exposed holdouts remain exposed.

The supported candidate is the exact corrected observation package and the stated null-support negative boundary. Formal Result creation, durable owner-head binding and Driver review are pending. No conclusion that semiprime residual structure has been refuted is supported here.

Researcher-ID: EM-PFSSV-E500C7
