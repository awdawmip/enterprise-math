# Endpoint signed-gap execution

The single authorized bounded run passed: all 31 residues over the nine declared tuples agree with the frozen actual one-window results. Every new production certificate was freshly replayed. Eight invalid inputs and eight altered certificates were rejected. No prior scientific computation was rerun, no new fixture was added, and the executed dispatcher and checker were not modified afterward.

This is a separately versioned integer-observer result, with shared-context author evidence and no formal admission. It is not a phase propagator, full Gram integration, or a claim of a general Shor simulation speedup. `ENDPOINT_IDENTITIES.md` and `ENDPOINT_SYMBOLIC_REVIEW.md` preserve their pre-execution status; this later note records the actual execution.

## Arithmetic result and scope

The production path selects the highest-bit identity first, then the lowest-bit odd/even-modulus identities, then the unchanged frozen one-window interior path. Actual typed arithmetic constructs the powers, parities, half-residue and signed outer products. The raw denominator exponent stays `2g`. Negative counts are retained.

The 31 results comprise 11 highest-bit, three lowest-bit odd-modulus, six lowest-bit even-modulus and 11 interior queries. Endpoint queries use 34 unsigned interval-count calls in total and **zero** floor-window or floor-moment calls. Only the 11 interior queries retain the old floor-window machinery. Complete I/O readback confirms that their nested frozen requests equal the historical requests in full, including operation ranges; their production digit costs are unchanged.

The declared grid covers `g=1` endpoint priority, both low-bit parity branches, highest-bit even modulus, negative results and an interior `R=1` case. Endpoint `R=1` is established symbolically but was not added as a new runtime fixture. The modulus is an input counting modulus, not a newly certified modular order. No order, factor, inverse-of-one, or ideal quantum reference was computed.

## Production comparison

The old values and operation receipts were read from the entire hash-bound `ONE_WINDOW_RESULTS.json.gz`, without importing or rerunning its checker. This historical payload points to the earlier actual three-window/exhaustive comparison. The present run is not a matched timing benchmark.

| `(g,k,R)` | Selected branch | New production digits | Recorded one-window digits | Difference |
|---|---|---:|---:|---:|
| `(1,0,3)` | Highest | 298 | 4,029 | 3,731 fewer |
| `(2,0,3)` | Lowest, odd modulus | 496 | 8,570 | 8,074 fewer |
| `(2,1,3)` | Highest | 421 | 8,043 | 7,622 fewer |
| `(3,0,6)` | Lowest, even modulus | 1,002 | 37,565 | 36,563 fewer |
| `(3,1,3)` | Interior fallback | 14,999 | 14,999 | Equal |
| `(3,2,2)` | Highest | 374 | 664 | 290 fewer |
| `(4,1,7)` | Interior fallback | 49,560 | 49,560 | Equal |
| `(4,2,1)` | Interior fallback | 475 | 475 | Equal |
| `(5,4,3)` | Highest | 1,199 | 13,706 | 12,507 fewer |
| **Total** | | **68,824** | **137,611** | **68,787 fewer** |

The six endpoint cases account for 3,790 new digits versus 72,577 recorded digits. The three interior cases account for 65,034 digits in both versions. These are fixture-level operation counts. The older exhaustive fixture cost, 76,977 production digits, is also historical and is not an asymptotic comparator or a new execution claim.

## Complete fresh costs

| Recorded metric | Production | Positive replay | Failed-certificate replay |
|---|---:|---:|---:|
| Complete evidence records | 9 | 9 | 6 |
| Typed arithmetic operations | 14,562 | 14,562 | 5,029 |
| Full-adder digit replays | 68,824 | 68,824 | 17,391 |
| Host bit-wiring operations | 747,472 | 747,472 | 190,476 |
| Host bit-length calls in arithmetic | 41,870 | 41,870 | 14,113 |
| Signed wrapper operations | 14,162 | 14,162 | 4,875 |
| Floor-moment nodes | 83 | 83 | 26 |
| Floor-window queries | 11 | 11 | 3 |
| Moment requests / cache hits | 129 / 46 | 129 / 46 | 38 / 12 |
| Maximum moment recursion depth | 5 | 5 | 3 |
| Maximum observed signed-boundary integer bits | 9 | 9 | 5 |
| Native core call delta | 1 | 0 | 0 |

All fresh production and replay work totals **155,039 digit replays**, 34,153 typed arithmetic operations, 1,685,420 recorded host bit-wiring operations and 97,853 recorded arithmetic bit-length calls. Host validation, dictionary routing, JSON I/O and hashing are not represented by those arithmetic counters. The maximum-bit metric observes the inherited signed-operation boundaries; it is not a bound on every hidden temporary integer.

The single actual native call was `recurrent_mass_power`, 12 states, depth one, binding all eight full-adder columns through the inherited stage78 primitive. All subsequent integer magnitude work is recorded composition/replay of those actual columns. A count of one native call must not be presented as the total computation cost. The frozen one-window run also used one call in its separate process; this run demonstrates no reduction of that initialization count.

## Negative controls and failure handling

The eight tamper attempts were: wrong branch, wrong odd half-residue, wrong even parity sign, altered interval result, Boolean input, wrong source hash, altered nested interior result, and wrong raw denominator exponent. Six generated complete paid replay certificates before rejection. Boolean input and wrong source were rejected before replay arithmetic. Their attempted certificates, rejection messages and available replay evidence are retained individually in the raw payload.

The separate eight direct input rejections cover a Boolean input, invalid width, both out-of-range bit positions, zero modulus, negative/out-of-range residue and unsupported stride. They produced no arithmetic operations or new native calls. Existing success or failure artifacts are refused before production starts, and result/failure creation uses exclusive writes.

The checker exited once with status zero. No `ENDPOINT_FAILED_EXECUTION.json.gz` exists because there was no unexpected execution failure. This does not erase the expected failed-certificate evidence inside `ENDPOINT_RESULTS.json.gz`. The full stdout is preserved in `ENDPOINT_RUN.log`.

The measured time before serialization was about 11.934 seconds; the result file finished writing at `2026-09-27T05:36:15.616973Z`. This elapsed observation is not used for a matched speed ratio, and no additional benchmark was run. Subsequent reads were pure I/O with no native imports.

## Integrity and activity pins

- Dispatcher `endpoint_signed_gap.py`: `c75e7e82cc0ef2413048153716f5100f3a9d1d4f50c375b7cb1690c3cfe6e036`.
- Checker `check_endpoint_signed_gap.py`: `7b78fe98620531be6fd552887cc00a53d338adbbe9676662d4198fe692ac3d8f`.
- Root identity proof: `e43e061fa0e04022daeb14aa30d9956ebe5ba9365b2aaa9c569d762a29e912c0`.
- Actual startup guard: `ac6cf502305ab0b81a573ba4a5dde69509502824ee629ecc15729aa09adc5d5e`. It reports activity and persistence allowed, no sync debt, and binds the existing `RA-CAAAC604CB513AEA8BBC1DFC` record at immutable EM `4b30da0ac8fb81a35dc9f75eddde85b7095b0a73`, record SHA-256 `ecae8f9abcaf173969598465ae05ffb4c8116c932fd3d0ad8e1e143f4e498b16`.
- Raw JSON: 17,045,774 bytes; SHA-256 `799bd9c51f98f973b6f4201f5684f83c0c427359d756e4a1b7bfdef239d8002e`.
- Gzip original: 721,136 bytes; SHA-256 `f5e256ecb694225bef17843aa78c5adb1ae0df6205e4cf3d3e4819c2e6d6738f`.
- Complete stdout: SHA-256 `18bbaf0d98ae02aa91b0dbc3a2aa5148cbfcb1cc9936b3be673dfdf29ce40320`.
- Pure I/O reader `read_endpoint_evidence.py`: `59639d4ed78fb601d9e654fef457fa82e6f4b401c7b71b2423bd6d4172d2b525`.
- Historical one-window gzip/payload: `d465513608449d40b081a6ae62acff51f75ef5990f7bc911cec632a5b705e3de` / `37ec0d4b7939a70d9157239bfebec7c88a387ff6a2f046a2701f87641d5d78f9`, original member `signed_gap/ONE_WINDOW_RESULTS.json.gz` of the signedgap archive and full readable representation under EM `56b191519b036c6890cae328c3b3812fbc1debb7`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_signedgap/`.

`ENDPOINT_READBACK.json` contains the complete cost aggregates, native source receipt, all nine per-case comparisons and the negative replay counts. Its reader loaded the entire new and historical payloads, checked their hashes and source pins, verified positive replay semantic equality, checked complete nonoverlapping signed-to-arithmetic operation indexing and confirmed all interior frozen-request matches. This is an I/O audit of recorded evidence, not another execution of the mathematical observer.

The next research step can be a symbolic analysis of other sign partitions or certified stride reduction. This completed stage does not supply arbitrary Walsh interval sums, multiple-gap convolutions, or compression of full matrix correlations. Any dialogue can continue those proofs without first reproducing this local run.

Global-Knowledge-Sync: main@bd2873d / GLOBAL_KNOWLEDGE_V1
