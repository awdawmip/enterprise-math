# Degree-five single-floor execution result

Status: ACTUAL_BOUNDED_PASS / SHARED_CONTEXT_AUTHOR_REVIEW / NOT_ADMITTED. One coordinator-authorized scientific run completed. The subsequent reader imported only pinned stdlib I/O helpers and inspected saved records; it did not rerun the arithmetic.

The nine declared cases produced all 189 moment equalities against a separate actual typed finite sum. All 44 sample records and 924 signed term/bucket updates were retained. The full record includes empty, normalization, constant-zero, zero-height and transpose branches; all 21 entries of each completed recursive node were checked against the saved operation sequence. The cache/reuse control also passed: invalid input left the state unchanged and the next valid repeat used the existing cache with no additional signed arithmetic or node.

The 17 certificate controls comprise ten full paid replays followed by mismatch, one paid valid prefix followed by invalid input, and six early zero-work rejections. Ten separate input controls rejected before arithmetic. The changed-valid-input control actually replays the changed input; it is not mislabeled as a replay of the original fixture. No deliberate mid-operation scientific failure was injected. The preserved-prefix test does not establish recovery from such a failure.

## Complete record and bindings

- Source: `typed_floor_degree_five.py`, SHA256 `755fcaf04832a5328e2464214f736ac661c410b3505edf10ab5218f935e2a7c7`.
- Checker: `check_degree_five.py`, SHA256 `975b574b85a3531da4443bf9f70cd4644ccc4ceadec81359506a2d00da3b1223`.
- Design: `DESIGN.md`, SHA256 `f6eb1b1e7b7dece0956e2ead166fbb9e901be3f5c9a44a1b367d1130206b7c22`.
- Proof: `DEGREE_FIVE_RECIPROCITY.md`, SHA256 `1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6`.
- Actual startup guard: `6f718b837610e417935e468381b0da97d38203d551b04505e8264e71d8cf2c4f`, activity `RA-CAAAC604CB513AEA8BBC1DFC`, allowed and without sync debt.
- `DEGREE_FIVE_RESULTS.json.gz`: 3,468,068 bytes, SHA256 `b044570bb55e81ea0ff1fe73ef35af6fa7438281c2d6dac87c1c31f3ee251c9f`. Its 88,217,988 decoded bytes have SHA256 `da675f8e04929116dac64552775f85ad75d39c71a03f78aad7c45d571fdf267e`.

`read_degree_five_records.py` traverses all 40 charged streams, all signed-to-typed links and saved native adder cells, the full recurrence reconstruction and all finite-sum records. Its result is `DEGREE_FIVE_RECORD_READBACK.json`, SHA256 `1acdef86e92b72f50b7c2bee72e3dcd85157bed36b2ce1bee23f87e55d8f291d`. The reader hash is embedded in that JSON. Source/ancestry hashes, the complete startup guard and native provenance were matched to the saved records. Only the declared process-dependent native-call delta is excluded in strict full-certificate replay equality; scientific values and costs remain bound.

The same author wrote the checker and this readback. This is an additional complete recorded-evidence check, not an independent admission or a new arithmetic execution.

## Paid costs and the unfavorable small-case comparison

| Category | Distinct streams | Digit replays | Typed operations |
|---|---:|---:|---:|
| Production | 9 | 120,943 | 12,452 |
| Independent typed finite sums | 9 | 19,294 | 2,480 |
| Positive fresh replay | 9 | 120,943 | 12,452 |
| Cache/reuse control | 1 | 10,311 | 1,309 |
| Cache-control fresh replay | 1 | 10,311 | 1,309 |
| Paid negative replay | 11 | 260,494 | 28,855 |
| Total | 40 | **542,296** | **58,857** |

The total also contains 57,809 signed operations, 5,776,792 counted bit-wiring operations, 176,212 counted arithmetic bit-length calls, 113 completed moment nodes, 115 moment requests and two cache hits. Nested node spans and overlapping boundary snapshots were not charged again.

The run has one actual 12-state native catalog call. It occurred during the first **empty production export**, before any arithmetic operation. Therefore every per-`Arithmetic` native-call delta is zero; the actual catalog work is retained and counted through the disjoint global CALLS intervals. Reporting only those per-instance deltas would incorrectly erase this setup cost. One catalog call does not mean one arithmetic operation.

| `(n,m,a,b)` | Production digits | Finite-sum digits |
|---|---:|---:|
| `(0,5,3,1)` | 0 | 0 |
| `(1,7,-3,-2)` | 2,592 | 135 |
| `(4,5,0,3)` | 901 | 461 |
| `(5,7,2,1)` | 10,311 | 892 |
| `(6,5,13,-4)` | 31,571 | 4,285 |
| `(7,4,-3,9)` | 23,774 | 2,486 |
| `(8,9,7,-11)` | 35,394 | 3,490 |
| `(9,7,0,21)` | 7,329 | 6,081 |
| `(4,1,-2,3)` | 9,071 | 1,464 |

All eight nonempty small fixtures cost more than direct finite summation in this metric. The value of this unit is the exact degree-five contract and its verified recursive implementation, not a measured practical speedup. The proof's bit-complexity statement and these small-instance costs are separate conclusions.

The reported 39.7466 seconds covers the whole checker before final serialization, including references and negative replays. It is not a matched performance comparison. Arithmetic counters omit allocation, JSON, hashing, interpreter internals and other uninstrumented host work. The full saved evidence is intentionally larger than the mathematical output.

## Continuation boundary

The single-floor degree-five API can now be consumed with its source and replay costs. This does not close the general two-floor recurrence. The reviewed unit-residual subfamily supplies a separate symbolic reduction that may consume this backend; it still needs its own implementation and bounded execution. No new order discovery, matrix-valued chronological correlation, phase propagation or full Shor sampler was executed here.

Unexpected scientific interruption remains bounded by the documented available-field snapshot behavior: raw operations and completed children are preserved when possible, while an uncompleted parent's local reconstruction is not invented. No unexpected failure artifact was produced in this run. The successful source and raw evidence are frozen; future changes require a distinct successor record rather than overwriting this result.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1 for the author's policy read; the actual execution uses the coordinator's newer bound guard recorded above.
