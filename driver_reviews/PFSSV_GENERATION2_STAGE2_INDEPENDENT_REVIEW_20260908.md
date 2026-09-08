# PFSSV Stage 2 — independent output and candidate-return review

Status: **PASS_WITHIN_OBSERVATION_AND_NEGATIVE_BOUNDARY_SCOPE**
Reviewer: execution_gate_review, internal independent review; no formal Driver authority exercised.

## Exact reviewed inputs

The review used the six versions in `stage2-actual-frozen-source/`, the exact candidate return, and immutable source Git objects at `f662d48f4615fe6d08a55225c7c36ecd15f91518`. It did not read editing mathematical source or run the generator.

- Actual-output manifest: `D:/em/TEMP/pfssv-stage1-20260908/stage2-actual-publication.json`, SHA256 `8c5db3a9ea21b5a43324051066b786cb92872afce80970c4bd567cb1b24dc5a5`.
- Candidate return: `D:/em/research-pfssv-revision-20260908/research_returns/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_REVISION_RETURN_20260908.md`, SHA256 `907783453bed7593872901bdaaadffe8c3f91f29e3dd8460a4bd330a72de7fc9`.
- Cross-table readout: `D:/em/TEMP/pfssv-stage1-20260908/stage2-frozen-readout.json`, SHA256 `37991c535f70111bec3f8e37218561a12ab7b7f8bfee0997d27a50e99bc64fb9`.
- Executed source SHA256 `a6a604207d189c10ba8146ca8e9897b4ce9b62b38b38682044a0f981f74e8cc0`, Git blob `6b7711d8dc4e1d9e8e6abeaa00ed80a66910e4cc`.

All six output hashes and lengths matched. The published precompute file SHA256 `7a7e8fe1a11fe157130c4fdf93638db08f54095f6ae5adf20be663d10edf036b` matched its immutable source, and its entire nested contract equals the final contract.

## Independent findings

**Complete observation package.** The exact seven scales times three widths occur once each, in the original order, in cell data, summary, precompute and readout. The independent metadata pass joined 8998 observation rows, 9480 stratum/channel records and 69536 target records. It checked row/rank/count/residue bindings, the full serialized profile dimensions and row-to-profile counts, trim/overflow/diagonal accounting, all stratum membership sets, source maxima, target bindings and violation flags. All 21 rows of the return's numeric table matched independently aggregated frozen data. This is integrity and consistency checking of an already executed dataset, not another independent enumeration of all prime pairs or a new generator run.

**The 18/3 split is exact.** There are 18090 violating cell/target/residue entries: 15400 with positive-total targets and 2690 with zero-total targets. Eighteen cells have a positive-total source and positive-total target witness. The only three cells with zero-target-only witnesses are:
- X=100000, width 3/1000: four violations;
- X=100000, width 1/1000: one violation;
- X=300000, width 1/1000: eight violations.

The first original-design positive witness is X=100000, width 1/100, band 6, p residue 13, q residue 11: p193 sends channel count 1 to p163, whose window [614,619] has residue capacity 0. The adjacent residue-11 addresses are 611 and 641. Both total row counts are 2, and both the full group and positive subset have size 2. Thus the specified assignment remains reachable with probability 1/2 after the old positive-total mask. The same general argument applies to each positive-target witness: a violating maximum source necessarily has positive total count, so deleting zero-total rows preserves both labels and leaves positive assignment probability. The reported split is a join over the exact declared strata, not a replay of archived floating-point code or old random draws.

**Interpretation stays narrow.** The capacity bound is an upper bound on possible prime occupancy because it already counts all integers of the residue in the fixed target window. A permitted assignment exceeding it cannot be an admissible occupancy of that window. The original scalar permutation distribution nevertheless remains mathematically defined. Neither the entries nor their sum are independent trials, distinct-prime counts or a p-value. The obstruction does not refute all conditional randomization, establish Null B failure, or refute semiprime residual structure.

**Native evidence is consistent.** Static comparison confirmed the previously reviewed PrimePrefix, DIV/ROOT helpers, log interval readout and CoordinateBins logic unchanged from Stage 1. The Stage 2 changes retain separate log overflow while expressly using the old band-7 label only in its original Null A audit. Canonical code-object profiling still captures the original native calls; transport only packages returned event bytes.

An independent byte-only pass decoded all 385 chunks, checked each chunk and whole-stream identity, all 99846 definition digests and 202772 references to earlier definitions. The 302618 events are exactly 293797 DIV, 22 ROOT and 8799 LOG, matching the author's recorded calls and returns. The raw bytes total 100831585 with SHA256 `d230e70c3ffd99ff882324e7af5cffc80f41f6ca10da35356934a4851ae34669`; the transport SHA256 is `efc2bedcda8da81f9948098943815011024c2c6d2e7711f209151ed983192fa4`. This verifies existing evidence, not fresh native execution or transitive certification of every import.

## Original eight obligations

The original taskbook at `2aa103eee829b78fa7784674ec1be4c3c5052a79` was read; its SHA256 is `b4e6011b736026ab2a5fc247f8a3750163cd33909fe25cf04bec6391078157d3`.

| Obligation | Supported state of this candidate |
|---|---|
| 1. Exact generator and independent spot checks | Complete observed design; prior bounded Stage 1 independent path remains evidence. No exhaustive second 21-cell enumeration claimed. |
| 2. Prior freeze and honest exposure | Revision precompute object preserved; original holdout blindness cannot be recreated. |
| 3. Raw and corrected summaries | All observed profiles supplied; corrected/signed/null arrays remain unavailable, not zero. |
| 4. Two valid scientific null families | Deterministic Null A capacity obstruction supplied; 512/4096 scientific screens not executed. Unmet as a two-valid-null comparison. |
| 5. Cross-scale signed residual statistics | Not executed; observation profiles do not discharge it. |
| 6. Family-wise null threshold | Not executed; no null ranks or calibrated residual effect sizes claimed. |
| 7. Blind holdout | Six holdout observations are post-exposure reanalysis, not blind validation. |
| 8. Strong scientific terminal return | This partial negative boundary is honestly reported; the original strong residual classification/effect-size/null-rank requirement remains undischarged. |

The original primary family-wise statistic is one-dimensional. This review does not add a newly invented joint q-rank null as an extra original hard gate.

## Recommendation and actual checks

The proposed `NEGATIVE_BOUNDARY` and `RESULT_ONLY` are rigorous **for this model-interpretation obstruction and corrected observation package**, while the mother hard target and parent remain OPEN. They must not be presented as fulfilling the original eight scientific obligations, formal Driver acceptance, Working Truth, or a residual-structure refutation. Subsequent canonical Result and Driver transactions are outside this review.

The author's sole full invocation receipt and its 21 progress lines plus final line were checked: exit 0, 224.922 seconds externally, zero scientific null draws. The exact published EOF-fixed source also has independently read matching 18-test logs (0.087 seconds unittest; 0.547 seconds process) and selected two-file static PASS. Earlier preserved test receipts have different source hashes and were not used as final-source evidence.

The independent metadata/byte pass itself returned exit 0, tool chunk `d933fe`, internal 5.641 seconds, observed tool wait 6.4675444 seconds. One earlier JavaScript orchestration string failed to parse before any subprocess began; it was a wrapper error, not a numerical failure. No mathematics, tests or generator were rerun. The companion receipt retains the actual metadata-check source, output, argv, input pins and evidence boundaries.
