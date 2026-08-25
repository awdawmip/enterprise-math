# CBRC F5B — Source and Target Leak Audit

Status: `CHECKPOINT_B_TARGET_LEAK_AUDIT_PASS`
Researcher-ID: `EM-CBRCF5B-B8E421`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`
Owner branch: `research/cbrc-f5b-positive-separation-regularity-axiom-admission`

## 1. Publication-liveness chronology

1. The owner branch was verified to exist and to be identical to taskbook source `11c5c651df54cf0117f936d5dbf421e37b9b7a34` before the first write.
2. A fresh Researcher-ID `EM-CBRCF5B-B8E421` was allocated.
3. `evidence/cbrc_f5b_execution_stamp.json` was first pushed at commit `861228cce0886f2b501ab69756ca69aff58d01ad` with:
   - `phase = STARTED_BEFORE_MATH`;
   - `admission_verdict = null`;
   - `math_source_read_before_stamp = false`.
4. Remote owner branch was verified identical to that commit.
5. Only then was the taskbook specification read. The taskbook explicitly states that it is specification, not an additional mathematical source.
6. The taskbook revealed that the stamp must also enumerate the three exact mathematical source refs. Before reading any of those mathematical sources, the stamp was schema-completed at commit `0741557dfb97c3eb956c26c6dac1339547e792e1`, preserving the initial stamp commit and recording `schema_completed_before_mathematical_source_read = true`.
7. Remote owner branch was verified identical to `0741557dfb97c3eb956c26c6dac1339547e792e1`.
8. Only after that second verification were the mathematical whitelist sources read.

Therefore:

`math_source_read_before_stamp = false` is historically and materially true.

## 2. Mathematical source whitelist actually read

Exactly three mathematical source documents were used before raw freeze.

### S1 — frozen F5B packet

Declared ref:

`research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b`

The ref resolves as a repository commit/ref. Fetched file blob SHA:

`0878ce5d694331212f081852fc87b4edb165e5ce`.

### S2 — accepted F4 Driver review

Declared ref:

`driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`

The suffix does not resolve as a commit through the contents API. The file at the exact taskbook source commit has blob SHA

`54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`,

which exactly equals the declared suffix. Therefore the source identity is verified by blob identity rather than commit-ref resolution.

No alternate F4 mathematical source was read.

### S3 — accepted F5AR Driver review

Declared ref:

`driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`

This suffix resolves as a repository commit/ref. The fetched file blob SHA is

`7e156a7a62dd1da1c083990bb03948a8719dd974`.

## 3. Governance-only reads

Before mathematics, repository/control metadata and account-level governance entrypoints were read only to route the task, verify branch state and perform publication-liveness writes. Those reads were procedural, not mathematical inputs.

No governance file supplied a mathematical candidate, proof or verdict.

## 4. Firewall audit

Before raw freeze, no mathematical source outside S1–S3 was read or used.

In particular, no downstream coherent-wave material, no R063/R064/R065/FQ mathematics, no rank-two carrier proposal, and no prohibited carrier/phase/scalar target was used.

The period-6 weak-scalar survivor, the pointwise-omission family, and the intermediate P6/P7 conditions were derived during F5B from the accepted F4 period boundary and elementary exact arithmetic; they were not imported from any downstream answer.

## 5. Target-leak audit

The provisional P1 admission was selected by the following internal criteria only:

1. exact sufficiency for the accepted F4 contradiction through the finite-fiber equivalence P1 <=> P2;
2. strict weakening of P0 by leaving pure-kernel scalar values unconstrained;
3. intrinsic expression through the canonical retraction `pi`;
4. compatibility with exact signed cancellation;
5. local coefficient-state semantics rather than a target-shaped global envelope condition;
6. sufficiency with already admitted A0 to close the issued rank-one scope.

No anticipated structure of any rank-two model was used as a selector.

The still-weaker P6/P7 proof-side conditions were not hidden. They are explicitly frozen as model-relative/global envelope conditions and are the reason the report distinguishes `weakest proof-side condition` from `weakest serious local separation axiom`.

## 6. Audit verdict

`TARGET_LEAK_AUDIT_PASS = true`.

`MATHEMATICAL_WHITELIST_EXACTLY_S1_S2_S3 = true`.

`FORBIDDEN_DOWNSTREAM_MATHEMATICS_READ = false`.

`RANK_TWO_CARRIER_SEARCH_OPENED = false`.

`F6_OPENED = false`.
