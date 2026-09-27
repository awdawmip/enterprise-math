# Matched prefix result review

Status: SHARED_CONTEXT_REVIEW. No material defect found in the inspected final implementation or saved comparison evidence. This is an author-team review, not independent admission. No scientific experiment was rerun; the only computation in this review reads saved bytes, hashes, exact JSON values, counters, and timing metadata.

## Evidence inspected

The final `prefix_comparison/compare_guarded_prefixes.py`, its summary, and the entire decompressed `MATCHED_PREFIX_RESULTS.json.gz` were read. `read_matched_evidence.py` is the administrative checker; its complete extracted result is `MATCHED_PREFIX_METADATA_AUDIT.json` in this directory. The earlier `MATCHED_PREFIX_DESIGN_REVIEW.md` remains a review of the earlier source, before the author added full correlation/observer comparisons and explicit no-new-column assertions.

Bindings verified against the current files:

| Object | SHA-256 |
|---|---|
| Final comparison source | `78e70a1a27273ae3651cd3e7807d5774e4168e3c51119f26853634b52fd3aa6b` |
| Boundary implementation | `875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83` |
| Frozen uniform implementation | `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28` |
| Saved gzip, 640,228 bytes | `a8157798dd3831afd9a760d623e5216774e5c3b27b50f99a522301ec001570b1` |
| Decompressed payload, 15,942,154 bytes | `d45f67df6dc75448a8b1e1e87a33f7a6c4ab1f85069344123a61234caf4a8e6d` |

The raw payload, summary, current source hashes, byte counts, and 1,664 saved native-call records agree. The author checker additionally asserted source hashes unchanged across execution. This review does not repeat native-word admission or reinterpret a saved result as a fresh native replay.

## Same scientific work and cache state

All six pairs use width four and the fixed positive history `1000`. Each pair shares an admitted program and the same immutable WordCertificateBank. A separately recorded paid uniform warmup precedes the measured runs for each program. The first pair runs old then new; the second runs new then old. Every run constructs a fresh engine, so its Gram cache begins empty while modular/primitive caches are warm.

For every pair, strict canonical JSON-byte comparison confirms identical plans, ledger, terminal mass, complete saved correlations, and complete signed positive-path observer streams. This comparison preserves the distinction between Boolean and integer values. The author also compares scientific query/application counters. The measured native-call count is identical on both sides: 73 for N=21,a=2; 116 for N=21,a=4; 54 for N=65,a=3. Evidence capture adds no native calls in these runs.

Every measured factory-column counter has zero increment. The review additionally compares the complete ordered positive and inverse table-instance contents with the corresponding paid warmup: permutation bindings and all queried-column records agree. The saved instance counts are respectively 6, 4, and 8. Instances remain separate even when their modulus/multiplier values coincide. This closes the narrower limitation of checking only the factory's forward-table counter.

The inherited evidence contains some live engine lists, but `run_prefix` never advances or otherwise mutates that engine after obtaining evidence. Table export returns detached certificate data. Later runs share the admitted program, not the completed engine; the saved results therefore do not reproduce the earlier intermediate-snapshot aliasing bug. This is not a general promise that arbitrary callers may retain live evidence and then mutate its engine: intermediate captures still require detachment.

## Timing and accounting

The calculation clock begins before engine construction and covers construction, four advances, and terminal mass. It stops before evidence capture. The through-evidence clock also includes evidence and the intervening counter/ledger snapshot work. Cold certificate construction and warmup are separately recorded and excluded from both measured windows.

| N,a | Binding checks before evidence, old → new | Native calls per measured run, both | Calculation old/new ratios, two runs | Through-evidence old/new ratios |
|---|---:|---:|---:|---:|
| 21,2 | 86 → 6 | 73 | 5.079, 4.970 | 4.626, 4.565 |
| 21,4 | 62 → 6 | 116 | 3.169, 3.148 | 3.051, 3.026 |
| 65,3 | 114 → 6 | 54 | 7.088, 7.019 | 5.778, 5.732 |

Thus an accurate bounded statement is: **these six warmed fixed-prefix calculation windows were 3.15–7.09 times faster, and their windows through evidence were 3.03–5.78 times faster, with unchanged saved scientific observations and native-call counts.** Ratios of summed old/new times are 4.824 for calculation and 4.359 through evidence; these are aggregate descriptive ratios, not an estimator of a universal speedup.

All 1,664 actual native calls are accounted for:

| Recorded phase | Native calls |
|---|---:|
| Twelve measured runs | 972 |
| Three paid warmups | 243 |
| Shared cold WordCertificateBank | 205 |
| Remaining shared native admission before these phases | 244 |
| Total | 1,664 |

The cold word certificate took 8.230 seconds. The paid warmups through evidence took 1.281, 1.102, and 1.709 seconds respectively. The entire author's experiment took 24.867 seconds. Native-call counts do not measure all host cost, typed digit replays, certificate serialization/storage, or memory; no such total-cost claim follows from this table.

## Claim boundary

The evidence supports reducing repeated full certificate-binding checks at trusted synchronous public boundaries while preserving the inspected calculations. It does not establish full output-law equality, cold-start speedup, asymptotic acceleration, or general performance for other histories and widths. These runs share a process, bank, and cache preparation and are not independent trials; ordinary system load was not controlled. The trusted synchronous-object, mutation, inherited transaction, and evidence-lifetime qualifications in `FINAL_SHARED_CONTEXT_REVIEW.md` remain applicable.

No new ideal propagation, phase approximation, mathematical oracle, or scientific result was introduced by this review. The matched checker and saved science files were not modified.
