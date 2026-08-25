# CBRC F5B — Source and Target Leak Audit

Status: `FINAL_TARGET_LEAK_AUDIT_PASS`
Researcher-ID: `EM-CBRCF5B-B8E421`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`

## 1. Publication-liveness chronology

1. Before the first write, the owner branch was verified identical to taskbook source `11c5c651df54cf0117f936d5dbf421e37b9b7a34`.
2. Fresh Researcher-ID `EM-CBRCF5B-B8E421` was allocated.
3. `evidence/cbrc_f5b_execution_stamp.json` was pushed at `861228cce0886f2b501ab69756ca69aff58d01ad` with:
   - `phase=STARTED_BEFORE_MATH`;
   - `admission_verdict=null`;
   - `math_source_read_before_stamp=false`.
4. The remote branch was verified identical to that stamp commit.
5. The taskbook specification was then read. The taskbook expressly states that it is specification, not an additional mathematical source.
6. Before any whitelisted mathematical source was read, the stamp was schema-completed with the exact mathematical refs at `0741557dfb97c3eb956c26c6dac1339547e792e1`.
7. The remote branch was verified identical to `0741557dfb97c3eb956c26c6dac1339547e792e1`.
8. Only then were the three mathematical sources read.

Therefore `math_source_read_before_stamp=false` is historically true.

## 2. Exact mathematical sources

Exactly three mathematical documents were used before raw freeze.

### S1

`research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b`

Fetched blob SHA:

`0878ce5d694331212f081852fc87b4edb165e5ce`.

### S2

`driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`

The suffix does not resolve as a commit through the contents API. At the exact taskbook source commit, the file blob SHA is exactly:

`54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`.

Thus source identity was verified by exact blob identity. No alternate F4 mathematical source was read.

### S3

`driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`

The ref resolves and the fetched blob SHA is:

`7e156a7a62dd1da1c083990bb03948a8719dd974`.

## 3. Governance-only reads

Account-level bootstrap/manual and project control metadata were read only to route the task, verify branch state and perform publication-liveness writes. They supplied no mathematical candidate, proof or verdict.

## 4. Firewall

No mathematical source outside S1–S3 was used before raw freeze.

No downstream coherent-wave material, R063/R064/R065/FQ mathematics, rank-two carrier proposal, or prohibited target family was read or used.

The period-6 survivor, the pointwise-omission family, and P6/P7 were derived inside F5B from the accepted F4 period boundary and exact elementary arithmetic.

## 5. Selector audit

The admitted P1 rule was selected only because it is:

- sufficient through finite-fiber P1<=>P2;
- strictly weaker than P0;
- intrinsic via the canonical retraction;
- compatible with exact signed cancellation;
- local rather than target-shaped;
- sufficient with already admitted A0 to close rank one.

No anticipated rank-two structure was used as a selector.

The weaker P6/P7 conditions are explicitly retained as model-relative proof-side conditions rather than hidden or promoted.

## 6. Verdict

`TARGET_LEAK_AUDIT_PASS = true`.

`MATHEMATICAL_WHITELIST_EXACTLY_S1_S2_S3 = true`.

`FORBIDDEN_DOWNSTREAM_MATHEMATICS_READ = false`.

`RANK_TWO_CARRIER_SEARCH_OPENED = false`.

`F6_OPENED = false`.
