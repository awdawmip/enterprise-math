# Direct signed-gap implementation: shared-context static review

Status: `PASS_STATIC_REVIEW_NO_BLOCKING_FINDING`. This is a shared-context author review, not independent admission. I read both complete sources and the two mathematical notes. I did not import the implementation, execute its checker, or perform new numerical science. Actual execution and raw-result verification remain separate work.

## Exact reviewed files

| File | SHA-256 |
|---|---|
| `direct_gap/direct_signed_gap.py` | `3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521` |
| `direct_gap/check_direct_signed_gap.py` | `be69a1937c9ab1e04ad4fe6f650c412c5cad5def247b2d40f97042b926e5ce6f` |
| `DIFFERENCE_AUTOCORRELATION.md` | `c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf` |
| `DIFFERENCE_REVIEW.md` | `23533f9752926749aaacc2c8431815656df350fb72e426ae9e5091237862fc52` |

I also inspected the frozen signed-gap strict input/JSON/semantic helpers and the actual floor-moment arithmetic methods. In particular, `exact_div` records exactly one signed Euclidean-division operation with the live tuple `(quotient, remainder)`; the new adapter's tuple assertion matches that implementation.

## Mathematical and typed-operation binding

The ten coefficient/factor pairs at source lines 73–141 match the low-branch polynomial plus its upper-half correction. Both moment tables use the modulus `P`, slope `R`, and offsets `b` and `b+U`; this argument order matches `moments(n,m,a,b)`. The stored differences implement `q_plus=q+delta` with `delta` in `{0,1}`. The reductions for `q*delta`, `j*q*delta`, and `q^2*delta` respectively divide the correct numerators by 2, 2, and 6, using checked typed exact division. The weighted `d`, `dq`, `d*delta`, and `dq*delta` sums use `d=b+R*j` correctly. No degree-four moment is hidden in the formula.

The overlap and tail expressions agree at `s=U`; the low formula handles `s=0` without inserting an extra tail. Each request retains both oriented progressions, with heads `r` and `R-r`. Thus `r=0` includes zero once, and a half-modulus residue retains two contributions even when their magnitude progressions coincide. Empty ranges produce a typed zero and no moment-table request. Scalar symmetry of negative displacements is sufficient here; it is not an arbitrary matrix-seed transpose rule.

Scales, lengths, coefficients, moment differences, weighted sums, all ten terms, and the final sum use the inherited typed signed/magnitude methods. Host arithmetic is confined to public loop/index/exponent metadata, sign/zero routing, hashes, and accounting. The raw denominator exponent `2*g` records the unchanged `4^-g` normalization; the implementation does not numerically propagate a quantum phase. Every calculated expression is connected to signed-operation ranges and the complete underlying arithmetic trace. Progression-head operations precede their local progression range but remain explicitly linked and included in the enclosing request range.

## Replay, negatives, and failure capture

The verifier reconstructs requests in order with a fresh observer. It compares the complete strict JSON semantics, including returned values, operation links, moment nodes, cache statistics and source/proof fields. Only the explicitly validated nonnegative runtime field `native_kernel_calls_delta` is excluded. Consequently ordinary Python `True == 1` does not make a changed serialized certificate acceptable. Fresh complete replay is appended before semantic-mismatch rejection; a failure during replay retains the available incomplete typed trace.

The checker declares nine input tuples containing 31 residues. Every one calls this direct observer, including endpoints. It asserts no inherited window queries, both orientations, and two ten-entry tables per nonempty progression. Historical answers are read from the entire hash-bound one-window payload, with its previous baseline pins checked; neither historical implementation nor exhaustive science is rerun. The dedicated half-modulus assertion and removal-of-one-orientation negative control exercise multiplicity.

There are eight strict input-rejection cases and nine certificate mutations. Six mutations should incur and save complete fresh replays; source/schema rejection and the boolean input should fail before scientific arithmetic. This is a static description of intended coverage, not a claim that these tests already passed. On normal successful or rejected paths the counters separate production, positive replay and negative replay. The actual raw evidence must confirm those counts after execution.

The `LIVE` registry retains completed output, the active production observer, current attempted forged certificate, completed negative attempts, current replay captures, and all global native calls. The outer failure handler serializes these available records with an exclusive-create filename. It does not promise recovery from import-time failure, failure of the serializer/filesystem itself, or an internal primitive exception before that primitive has retained its trace. This boundary does not undermine the planned ordinary assertion/verification failure retention. Success and failure artifacts are not silently overwritten.

## Cost and claim boundary

At most four top-level moment-table calls is not a four-operation cost claim. Recursive nodes, cache lookups, all ten entries, coefficient work, signed-to-native traces, and both replay classes remain chargeable. The declared comparison is typed digit counts against recorded history, not a timing benchmark or a proof that direct evaluation beats endpoint shortcuts. No order/address discovery, arbitrary Walsh-mask computation, full Gram integration, or general Shor-simulation improvement follows from this bounded checker.

The reviewed sources have no blocking static defect. A single bounded actual run may proceed under the root's current guard; its result must be assessed from the resulting evidence rather than this review.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
