# One-window signed-gap execution

Status: AUTHOR_EXECUTED_BOUNDED / SHARED_CONTEXT / NOT_ADMITTED.

The one-window observer is implemented and its declared bounded check passed once. This is the later execution record for `../ONE_WINDOW_REDUCTION.md`; that reviewed proof keeps its original IMPLEMENTATION_PENDING writing-time label unchanged. The complete three-window baseline, its 1,764-pair typed enumeration and all seven original files are unchanged.

## Actual method and comparison

For `U=2^k`, `H=2^(g-k-1)` and `L=2UH`, the four bit-pair classes partition the full interval pairs. Thus `T_L=2J_zero+J_plus+J_minus`, and `K=4J_zero-T_L`. The new code computes `U,H,L`, one existing window weight, the existing interval count and the signed outer combination through the actual typed integer runner. The interval and window counts are nonnegative; the signed result can be negative. The raw denominator exponent remains `2g`. The scope is unchanged: physical stride one, one negative bit, arbitrary positive counting modulus, no order/address certificate or full Gram integration.

The checker read the entire frozen original payload and verified its compressed and decompressed hashes. For each of the same nine tuples it computed all residues with fresh one-window arithmetic, compared them to the original actual values and retained pointers into the old complete production/enumeration traces. Every new complete certificate then passed one fresh JSON-round-trip reconstruction. No old production or exhaustive enumeration was executed again.

All 31 residue comparisons passed. Six new tamper controls were rejected: signed value, window count, full-interval count, displayed identity, boolean input and source pin. The first four performed full fresh verification whose complete failed-comparison receipts are retained. The last two rejected before arithmetic replay. Negative results and the `R=1` zero result passed. There was no unexpected failure, grid expansion or retry.

## Observed resource comparison

| `(g,k,R)` | Frozen three-window production digits | Fresh one-window production digits |
| --- | ---: | ---: |
| `(1,0,3)` | 7,715 | 4,029 |
| `(2,0,3)` | 15,104 | 8,570 |
| `(2,1,3)` | 15,492 | 8,043 |
| `(3,0,6)` | 58,462 | 37,565 |
| `(3,1,3)` | 27,706 | 14,999 |
| `(3,2,2)` | 1,427 | 664 |
| `(4,1,7)` | 83,688 | 49,560 |
| `(4,2,1)` | 1,103 | 475 |
| `(5,4,3)` | 54,781 | 13,706 |
| Total | 265,478 | 137,611 |

Production saved 127,867 digit replays on these exact cases. All nine totals decreased. This is a historical recorded-operation comparison, not a simultaneous wall-time benchmark or a guaranteed factor-three speedup. Memoization and the added interval arithmetic explain why query-count reduction is not an exact operation-count ratio. The new total remains above the original tiny exhaustive comparator's 76,977 digits; that unfavorable comparison remains part of the result.

| Fresh work | Typed arithmetic operations | Adder digit replays | Counted host bit wiring | Counted arithmetic bit-length calls |
| --- | ---: | ---: | ---: | ---: |
| Production | 32,946 | 137,611 | 1,494,901 | 93,645 |
| Positive certificate replay | 32,946 | 137,611 | 1,494,901 | 93,645 |
| Negative verification replay | 8,688 | 16,116 | 176,496 | 23,540 |

The new process made one actual `recurrent_mass_power` call on 12 states at depth one, producing all eight full-adder columns. Production then used 31 window queries, 319 moment requests, 126 cache hits and 193 moment nodes. The maximum recorded recursion depth was five and recorded boundary-integer size was 11 bits. These do not claim to bound unobserved low-level temporaries. Actual native calls, digit-column applications and partial host-wiring counts are distinct resources; source hashing, object handling, serialization and other CPU costs remain additional.

The recorded 26.25 seconds includes frozen-baseline I/O and checking before final success serialization. Its scope differs from the original run, which also executed the exhaustive comparator, so their elapsed times must not be presented as a speed ratio. The new artifact finished writing at 2026-09-27 05:03:33 UTC. Another agent's separate timing work began around 05:03:30 UTC, potentially overlapping this final serialization tail. No timing-isolation claim is made. Both this run and the original baseline each paid their own one native primitive call in separate processes.

## Exact evidence and bindings

| File | SHA-256 |
| --- | --- |
| `one_window_signed_gap.py` | `c15e80d580fc8aa52821cb8b0526ada4cd31933cd089bdb1fa1199d1de1ff8b7` |
| `check_one_window_signed_gap.py` | `6594ebf9495dfabf1ce2878f4a9bc5cde80d45d0747e92d71e1e27e096e1a87e` |
| `ONE_WINDOW_RESULTS.json.gz` | `d465513608449d40b081a6ae62acff51f75ef5990f7bc911cec632a5b705e3de` |
| Decompressed one-window payload | `37ec0d4b7939a70d9157239bfebec7c88a387ff6a2f046a2701f87641d5d78f9` |
| Frozen baseline gzip | `2b7ff5fe1cd62fbabe3f48fbaf157aeccdc6614f46a5c6d284edff3a412dbc9b` |
| Frozen baseline payload | `76d1087ef58144303b624c2935a045eb15dcd9264f32dd1c09378431e9663110` |

The one-window payload has 34,118,508 raw bytes and 1,333,492 compressed bytes. The actual consumed startup guard is SHA-256 `56612f05af8edd9ae544b767fd6be47cd7f4a1585c9659b6678f5ca5f17a3084`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. The core/source dependencies and full-digit/carry records are retained in every complete certificate. The exact frozen full-adder and floor-moment sources remain those documented in `../DEPENDENCIES.md`.

`ONE_WINDOW_SUMMARY.json` records the run. `read_one_window_evidence.py` performed only existing-byte decoding, hash checks and recorded-cost aggregation, producing `ONE_WINDOW_READBACK.json`; it imports no native arithmetic. Its larger JSON readback was deferred until the other agent's timing run finished. The reader's metadata subtraction/sums are resource accounting, not an alternative scientific evaluator.

The top-level checker consumes the startup guard and preserves unexpected partial work to a separate exclusive-write failure artifact. Complete successful results do not silently overwrite earlier files. Full strict-JSON replay distinguishes booleans from integers, rejects unsupported keys and checks all mathematical fields; only the cache-dependent native-call delta is omitted from semantic equality. This is shared-context author evidence, not independent admission, general arbitrary-mask compression, or a full QFT simulation claim.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
