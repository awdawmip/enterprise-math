# PFSSV generation-2 capacity gate and Stage2 decision

Status: OWNER_STAGE_DECISION / OBSERVATION_AND_CAPACITY_AUDIT_ONLY
Driver-ID: EM-DVR-01E1D9
Task: RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION
Publication: TP2-2029B5CCC5EEC5F0132C
Researcher: EM-PFSSV-E500C7
Claim: chatgpt-pfssv-r2-20260908T101753Z-456f906e
Execution record: ER-EB2A78D7B88A292B412B

This is an owner decision within the existing task. It is not a formal Result review, a new task/claim, Working Truth, theorem promotion or parent-objective closure.

The genuinely executed Stage1 probe used X=2000003 and width 1/1000, not the two archived audit cells or the original 21 cells. It completed in 5.422 seconds, with reported peak process memory 31,055,872 bytes and full native trace 5,803,940 bytes. Eleven contract tests and the two-file exact-arithmetic static check passed. Frozen script SHA256: 37684dece1a454858ca5e89b5cb63ed88a65a2b6f86862aee5e89a30e51bde56. Probe SHA256: 5abb0c6c19050b8559f18e5daef86c11572cfe5968f6f192b0da96676e83e19e. Raw trace SHA256: 160c1321da7b706e1201247f61269e08e46ef7b4e656e17de867303378e38572. The published manifest supplies the remaining exact source and execution pins.

The probe retained 223 geometric rows, including 116 with zero observed prime count; the exact raw pair count was 393. Its capacity witness has coarse band 2, p mod 30 = 7, q mod 30 = 17. The source row p=97 has count 1; the target row p=127 has q in [15749,15763] and integer residue capacity 0. In the two-row stratum, the original permutation assigns 1 to this target with probability 1/2. No random draws, rejection sampling or clipping were used to establish this witness.

The witness rules out interpreting every draw of that scalar permutation law as an admissible occupancy of the specified factor windows. The computational count surrogate still has a mathematical distribution; this is not a proof that every use of a conditional randomization is invalid, that all registered cells have the same defect, or that genuine semiprime residual structure is absent. The old one-dimensional screen does not define a joint q-rank allocation kernel. Full observed prime-rank intervals restore observations, not that missing random kernel. The already exposed holdouts cannot become newly blind.

The next authorized mathematical unit is the complete original 21-cell observation and deterministic capacity audit:

- Use the original five discovery scales, two exposed holdout scales and three widths. Keep exact generator bounds, all geometric support including zero rows, both original trims, diagonal/overflow accounting, genuine pi(p),pi(q) observations and complete one-dimensional raw profiles.
- Audit every applicable original Null A stratum/residue against its exact target integer capacity. Preserve all targets and witness probabilities, including clean or unresolved outcomes. Do not infer the full-scope audit from the one new probe.
- Do not run the 512/4096 scientific null screens in this unit. Do not truncate, re-draw or silently repair their distribution. Mark scientific corrected/null vectors as unavailable and explain the concrete model support gap. No accepted residual refutation/candidate or restored blindness follows from successful execution.
- Freeze the exact Stage2 precompute contract before the run, binding this decision and the published Stage1 source. Preserve that contract object in the final result summary and record its actual prior commit and SHA256. Unresolved BRC interval-bin decisions remain explicit, including zero-observed rows that may receive positive permuted mass.

All immutable task/ER/history and the three frozen Stage1 plan/binding files retain their exact bytes. Stage1 code and output versions remain available in their immutable published source commit and frozen local copy. Stage2 uses new versions of the existing allowed script/test and result output paths; no ER extension, second claim or unregistered stage2_* path is needed. The original resource_probe.json remains unchanged. A new source version must never be labelled as the old Stage1 bytes.

The execution budget is at most 1800 seconds and 2 GiB process memory, with at most 512 MiB of original trace bytes. The native_trace.jsonl output may use an explicitly declared, lossless gzip+base64 JSONL transport envelope with ordered chunks, each raw chunk size/SHA256, whole-stream size/SHA256 and a checked decode path. This changes byte transport only. Preserve every event and integer, verify roundtrip and corruption/truncation rejection, and report both raw and encoded identities. The encoded transport budget is 50 MiB. Compression/postprocessing counts toward actual resource receipts; compression does not enlarge the raw trace or mathematical budget. Any budget failure yields an honest partial frontier.

The window-count composition can be checked symbolically: L=max(p,floor(X/p)+1), H=floor(U/p), a=pi(L-1), b=pi(H). True q-ranks are (a,b], and occupancy of a fixed rank bin (k_j,k_{j+1}] is max(0,min(b,k_{j+1})-max(a,k_j)). A complete prime prefix through floor(U/2) is sufficient since p>=2; p<=sqrt(U) and p<=q provide complete unique pair enumeration. These are task-local T0_BRC/T1 count-window compositions, not a new primality theorem or a joint-null construction.

After the bounded unit, freeze actual outputs and return the scientific limits for Driver assessment. Any new null family or fresh blinded design needs its own explicit statistical contract and successor-value assessment; numerical completion alone cannot create it.
