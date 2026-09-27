# Typed signed scalar-gap observer

Status: AUTHOR_EXECUTED / BOUNDED_CHECKS_PASS / SHARED_CONTEXT / NOT_ADMITTED.

This package implements one bounded entry into the signed-gap refinement. For integers `g >= 1`, `0 <= k < g`, `R >= 1`, and `0 <= r < R`, it computes

    K(g,k,R,r) = sum_{0 <= x,y < 2^g; y-x = r (mod R)}
                    (-1)^(bit_k(x)+bit_k(y)).

The physical stride is exactly one. The public modulus `R` is only a counting modulus: the API does not certify it as a work permutation's order, discover an address logarithm, infer factors, or propagate a quantum state. No complete Gram sampler is connected here. The current package needs pinned external runtime sources and is not a self-contained runtime distribution.

## Exact reduction and API

Write `U=2^k`, `H=2^(g-k-1)`, and `x=2UA+Ue+v`. For each `delta` in `0,+1,-1`, the frozen `window_weight(H,U,2,R,r,delta)` counts the pairs `(A,v),(A',v')` with

    2U(A'-A) + v'-v = r-U delta (mod R).

The two equal-bit choices have sign +1 and each contributes `J_zero`. The two unequal choices have sign -1 and contribute `J_plus` and `J_minus`. Consequently

    K = 2 J_zero - J_plus - J_minus.

This derivation preserves every pair. The three `J` values are nonnegative, but `K` can be negative; it is a correlation coefficient rather than a probability. In a surrounding gap formula its raw factor remains `4^-g`, recorded as denominator exponent `2g`. No normalization by the signed sum is performed. At `R=1` the single negative bit gives complete cancellation.

`SignedGapObserver.one_negative(g,k,R,r,stride=1)` returns the signed coefficient, three weight values, typed scale construction, request indices and exact operation ranges. A single observer can reuse its floor-moment cache across requests. `export_certificate()` retains all requests and complete signed/unsigned arithmetic traces. `verify_certificate(certificate, replay_capture=...)` reconstructs the requests in their original order and compares the full strict-JSON semantic certificate. It distinguishes booleans from integers and rejects nonstring object keys. Only the runtime cache-dependent `native_kernel_calls_delta` field is excluded from equality; fresh replay costs are returned separately. It does not attest the truth of a caller-supplied native-call statistic.

Every magnitude addition, multiplication, signed difference, division and scale doubling follows the frozen typed arithmetic route. Python handles public loop indices, sign/magnitude encoding, record routing, source hashing and resource metadata. It supplies no ordinary modular-arithmetic reference or substitute state propagator. The arithmetic source ultimately composes all eight actually executed full-adder input columns while retaining each digit/carry trace.

Inputs use exact Python integers, excluding booleans. Unsupported strides are rejected rather than silently reduced. The more general typed gcd/inverse stride reduction proved in the symbolic note is not implemented by this unit.

## Actual execution and evidence boundary

The checker fixes nine `(g,k,R)` tuples:

    (1,0,3), (2,0,3), (2,1,3), (3,0,6), (3,1,3),
    (3,2,2), (4,1,7), (4,2,1), (5,4,3).

It evaluates every canonical residue for each tuple. One independent typed exhaustive histogram per tuple is reused for those comparisons. Its bit extraction uses two actual Euclidean divisions, differences and remainder buckets use typed signed arithmetic, and each bucket receives an actual typed signed addition. No host `%`, `pow`, or ordinary integer summation supplies its mathematical answer. The checker also performs complete JSON round-trip certificate replays, input boundary rejection and trace/value/source tampering rejection.

The checker consumes the stage's actual `STARTUP_GUARD.json` and retains its hash and receipt. It refuses to overwrite existing result files. Unexpected interruption records the known stage, bound sources, completed cases, available active typed work, current and completed negative controls, and all actual core calls in a distinct exclusive-write failure artifact. Nonstring-key corruption attempts are preserved as typed key-entry arrays rather than coerced into ordinary JSON object keys.

After compile-only shared-context review, the declared checker was executed once and exited successfully. All 31 residue equalities in the nine tuples passed against 1,764 actual typed pair observations. All 15 invalid-input checks and nine certificate-tampering checks were rejected. Five tampering checks required fresh typed replay; all five complete failed-verification replay receipts are retained. The other four were rejected before typed replay. There was no unexpected failure artifact, additional grid, or scientific rerun.

| `(g,k,R)` | Actual coefficients in residue order | Three-floor digit replays | Exhaustive digit replays |
| --- | --- | ---: | ---: |
| `(1,0,3)` | `2,-1,-1` | 7,715 | 68 |
| `(2,0,3)` | `2,-1,-1` | 15,104 | 377 |
| `(2,1,3)` | `2,-1,-1` | 15,492 | 381 |
| `(3,0,6)` | `12,-11,10,-10,10,-11` | 58,462 | 2,293 |
| `(3,1,3)` | `2,-1,-1` | 27,706 | 1,997 |
| `(3,2,2)` | `0,0` | 1,427 | 1,942 |
| `(4,1,7)` | `10,-1,-8,4,4,-8,-1` | 83,688 | 11,940 |
| `(4,2,1)` | `0` | 1,103 | 7,883 |
| `(5,4,3)` | `2,-1,-1` | 54,781 | 50,096 |

Complete evidence is `SIGNED_GAP_RESULTS.json.gz`, compressed SHA-256 `2b7ff5fe1cd62fbabe3f48fbaf157aeccdc6614f46a5c6d284edff3a412dbc9b`; its decompressed payload SHA-256 is `76d1087ef58144303b624c2935a045eb15dcd9264f32dd1c09378431e9663110`. The compressed file has 3,037,709 bytes, representing 97,157,549 raw JSON bytes. `SIGNED_GAP_SUMMARY.json` reports the scientific run. The separate `read_signed_gap_evidence.py` only decoded that existing payload, verified hashes/source bindings, and aggregated recorded resource metadata into `SIGNED_GAP_READBACK.json`; it executed no scientific arithmetic.

The executed source SHA-256 values are `86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a` for `signed_gap.py` and `83bd08d2345246754ab9da2453d84af2ef2b70ccf7546dd5d9efb2c8badf5eff` for the checker. The consumed startup guard SHA-256 is `56612f05af8edd9ae544b767fd6be47cd7f4a1585c9659b6678f5ca5f17a3084`. The run's measured 40.93 seconds covers checking before final success serialization; it is not an isolated algorithm timing or an end-to-end publication time.

## Cost and reusable boundary

For one requested residue, the proven algorithm performs three degree-three floor-moment queries, a constant-size signed outer combination, and `O(g)` typed doublings in this implementation. The magnitude bit lengths are polynomial in `g+log(R+1)` and the floor recursions have logarithmic Euclidean depth. It does not enumerate `R` or all pairs to produce one answer. The checker deliberately requests all residues of small `R` and runs a separate exhaustive comparator; those verification costs must not be attributed to a one-query API claim or hidden from total experimental work.

The observed resource totals are:

| Work | Typed arithmetic operations | Adder digit replays | Counted host bit wiring | Counted arithmetic bit-length calls |
| --- | ---: | ---: | ---: | ---: |
| Three-floor production | 55,420 | 265,478 | 2,866,745 | 155,743 |
| Typed exhaustive comparator | 7,497 | 76,977 | 833,613 | 24,538 |
| Positive complete certificate replay | 55,420 | 265,478 | 2,866,745 | 155,743 |
| Negative verification replay | 21,712 | 40,870 | 445,165 | 57,999 |

The whole process made one actual `recurrent_mass_power` call on the 12-state full-adder graph at depth one. Its eight input columns were then reused in the counted digit transducers. The production path made 93 window queries and 711 moment requests, with 462 cache hits and 249 distinct moment nodes. Its maximum observed recursion depth was five and maximum recorded boundary integer bit length was 12; neither statistic bounds unobserved low-level temporaries.

The three-floor production total is worse than the exhaustive comparator on these small fixtures. This negative constant-cost result is retained, alongside the exact cancellation cases that were cheaper. A low native-call count does not establish low total cost. Full receipt retention, serialization, allocation, cache lookup, sign routing, index control and machine-integer implementation costs are additional costs. Host bit counts come from the frozen arithmetic trace-cost convention and are not complete CPU-operation counts. No default Python stack or resource bound is a theorem of unrestricted practical execution.

The positive contribution is a concrete signed coefficient family with no dependence on the numeric size of a large odd period in its arithmetic-stage bound. Arbitrary Walsh masks, many-gap convolution, paid modular order/address acquisition and non-scalar matrix windows remain outside this interface. The implementation is a sufficient integer observer, not a general Shor dequantization claim.

## Frozen sources

The proof is `sep27-qft-boundary/gram_structure/SIGNED_GAPS_REFINEMENT.md`, SHA-256 `1a84d09ed1fecdf7a42de9c1b1e48da881c820e544214011703c79a688938776`; the earlier boundary package is unchanged.

The reused implementation is `sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py`, SHA-256 `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`, at EM commit `c0f04346c520fddc8016c86227b3b6cc2e9f30f6`, path `research_notes/directed_recovery/20260927_C6438C/qft_adaptive/nonzero_structure/typed_floor_moments.py`. Its floor-moment proof is adjacent, SHA-256 `20a93f15f241f9c3220c031032cc2af697e4d4a448669f5b637396c1a05529d4`.

The existing lazy integer arithmetic and sparse full-adder runtime are restored through that frozen stage's dependency chain. Actual exported evidence contains their file hashes and native source commit `0852cad130c1d877174d235687cf60c19f318c58`. This wrapper does not change physical primitives, precision profiles, residual storage or source admission.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
