# Paid discovery of the small odd part of a modular order

Status: AUTHOR_ACTUAL_TYPED_BOUNDED / SHARED_CONTEXT / NOT_ADMITTED.
This unit implements the acquisition step from the preceding whole-period aggregation theorem. It discovers an exact order without an order/factor input; its cost is parameterized by a declared odd-part search budget. It is an arithmetic component, not a new factoring driver, QFT sampler, phase experiment, or physical-model admission.

## Interface and proof

`discover_odd_part(N,b,odd_budget)` accepts integer `N>=2`, a canonical unit candidate `1<=b<N`, and integer budget `Q>=0`. It returns a JSON-compatible record with top-level `status`, `inputs`, `n`, `q`, `s`, `R`, `evidence`, and `metrics`. Booleans are excluded from integer inputs. A typed Euclidean check establishes that b is a unit, retaining the failed trace if it is not.

Let the analysis-only order of b be `R=2^s q`, q odd, and put `n=ceil(log2 N)`. A finite unit group gives `R<=phi(N)<=N-1<2^n`; no primality or factorization of N is needed. Hence n squarings remove the entire two-power part. The actual computed value `c=b^(2^n)` has

`ord(c) = R/gcd(R,2^n) = q`.

The implementation performs all n squarings through actual typed lazy modular columns. It then visits `c^1,...,c^Q` consecutively, stopping at the first observed one. If that happens at step q, every preceding positive exponent was observed not to return, so q is exact, not merely a multiple of the odd order.

After a successful return, actual binary modular exponentiation computes `b^q`. Its order is exactly `2^s`. If `b^q=1`, the recovered exponent is s=0 immediately. Otherwise the implementation squares until the first return to one; its position is exactly s and is bounded by n. Typed integer multiplication assembles `R=q*2^s`, and a typed comparison checks `R<N`. The returned status is `CERTIFIED` only after this whole chain is complete.

If no odd first return occurs within Q, status is `PARTIAL` and `q,s,R` are all null. The paid squaring chain and all tested odd powers remain in the record. No complete order is certified. Budget zero performs the n preprocessing squarings and no odd-return test; it remains PARTIAL even when a separate optimization could infer q=1 from the already observed c. That optimization is not silently credited here.

This establishes the exact-order contract for every valid input on which discovery returns CERTIFIED. It does not guarantee that a chosen small Q suffices on every unit. The worst-case odd part can be large.

## Actual arithmetic and certificate consumption

The executable is `typed_odd_part.py`. Residue products, squares, unit checks, inverse/permutation proofs, order assembly and its final comparison all use the frozen typed BRC arithmetic. Python exponent-bit selection, integer-width calculation, loop indices, label equality and dictionary routing are declared wiring; they do not supply modular values. There is no ordinary modular pow/remainder/gcd reference and no phase or amplitude propagation.

Each discovery call uses a fresh `LazyModularFactory`. Within that call an existing equal multiplier table may be reused, and each distinct actual table receives one complete typed permutation replay. The record retains every such table, its setup and queried-column evidence, verification receipts, auxiliary arithmetic and native source binding. Independent calls, including verification calls, create new instances and pay their costs again.

`verify_odd_part_certificate(record)` accepts a raw or JSON-roundtripped record and returns `{'verified':True,'replay':...}` only after fresh complete typed discovery and strict canonical-JSON comparison. Consumers must take q, s and R from that returned **CERTIFIED replay**. A verified PARTIAL record still supplies no order. The comparison preserves JSON number/boolean distinctions, rejects non-string dictionary keys, and binds scientific chains, sources, outputs and deterministic resource counters. Only process-dependent native-cache call deltas are excluded; this comparison does not authenticate an old run's cache state. Full current native-call receipts are retained by the checker separately.

Wrong outputs, altered chains, omitted tables, changed source bindings, underreported digit cost, and promotion of a PARTIAL attempt are rejected. Failed replay evidence includes both the attempted record and its actual fresh reconstruction. Ordinary schema/input rejections do not create a scientific replay. Arbitrary interrupted dependency calls are not claimed to have a complete automatically recoverable trace.

There is no incremental live cursor in this version. A future larger-Q invocation can restart deterministically using the recorded input, and the prior PARTIAL artifact remains available for audit. Its preprocessing/reverification must be charged again unless a later implementation explicitly certifies reusable live state.

## Cost boundary

On success, logical modular column requests comprise n preprocessing squares, q consecutive odd-return steps, at most `2*bit_length(q)-1` binary-power actions, and s recovery squares. Thus the logical bound is `O(n+q+log q)` and the finite-budget bound is `O(n+Q+log Q)` when Q>=1 and discovery succeeds. The PARTIAL case uses n+Q requests. This is polynomial in **Q**, not in log Q.

New multiplier tables also require actual typed inverse/permutation setup and a separate full verification. Their bit costs, column bit costs, auxiliary checks, arbitrary-width values, complete traces, serialization and output storage are additional. The metrics separate setup, column, verification and auxiliary adder-digit replays. Cached native primitive calls are not equivalent to the number of digit operations. The evidence size is not a bound on peak live memory.

The same information is available to a classical comparator. If the simulator's multiplier is `b=a^(2^k)`, its odd order part is also the odd part of ord(a). After discovering q, paid computation of `a^q` and its first square return recovers ord(a); a good-base half-order/gcd test may then find factors without reconstructing QFT readouts. Those operations and possible failure must be charged. This module makes no factoring advantage claim for this structured input class.

## Bounded execution and observed costs

The declared checker completed once successfully. Six CERTIFIED results equal independent **actual typed** consecutive first-return enumeration, with no expected order passed to the discovery. Every positive result also passed a JSON roundtrip and full typed replay. Two insufficient-budget attempts replayed as PARTIAL, and 20 input or forged-certificate controls rejected.

| N | b | Q | q | s | R | Discovery column requests | Full-return reference requests | Discovery adder digits | Reference adder digits |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 0 | 1 | 3 | 1 | 94 | 78 |
| 17 | 3 | 1 | 1 | 4 | 16 | 11 | 16 | 3,687 | 1,808 |
| 97 | 5 | 3 | 3 | 5 | 96 | 18 | 96 | 26,925 | 16,567 |
| 21 | 2 | 3 | 3 | 1 | 6 | 12 | 6 | 3,828 | 903 |
| 21 | 4 | 3 | 3 | 0 | 3 | 11 | 3 | 1,949 | 820 |
| 65 | 3 | 3 | 3 | 2 | 12 | 15 | 12 | 10,536 | 2,655 |

The N97 fixture separates R from q by a factor of 32 and reduces requested columns from 96 to 18. It nevertheless has **higher total counted adder-digit work** because its 12 distinct multiplier tables each incur setup and verification. The N17 pure-two-power case has the same tradeoff. This run establishes a useful order-discovery interface and its logical parameter dependence; it does not demonstrate a total-cost improvement over the paid reference on these fixtures.

The PARTIAL attempts are `(97,5,Q=2)` and `(17,3,Q=0)`, with 16,371 and 3,642 adder-digit replays respectively. They are retained, not retried until a desired outcome appeared. The successful cases have separate declared larger budgets.

The full checker records one actual native core call, followed by many explicit digit replays through the frozen native full-adder catalogue. Its timed scientific/checking section was 6.6519963999744505 seconds on this host; final gzip serialization is outside that timer. These are warm-cache-aware local facts, not a speedup ratio. Raw records retain all positive, partial, replay, independent reference and rejected-certificate work, including distinct table instances rather than merging equal inputs across calls.

Frozen source/evidence bindings:

- `typed_odd_part.py`: `188defd9307e461e8617243f76a8b6109309d6ac6b1834a71511172b58a6618c`.
- `check_odd_part.py`: `ab4c674f58241cd1c1c0e2246e62565c6d2400abd8e39cd62b1a2174010135b0`.
- Frozen `lazy_modular.py`: `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4`.
- `ODD_PART_RESULTS.json.gz`: 1,372,223 bytes, SHA256 `61206b671705f083bbe8c1ea066c4a8e77896a182ddd058fe8f5c4ddc9d9b18a`.
- Decompressed payload: 16,971,842 bytes, SHA256 `c885c4b10f78b1cda18ba75cd061138801d7b239c877c242b2cf64e51c0ce4a0`.

The checker pins source hashes before and after execution. The current startup guard is the immutable activity readback at EM `41396f6f3662eada17d59fa376dc54026b59252c`; the BRC-only policy MD and machine JSON were reread from the saved canonical `06788df022dbd11720132b4ed0882ce8e41b3b8a` responses before execution. No frozen source was changed and no remote publication was performed by this unit.

The immediate continuation is paid target-address recovery from this replayed q/s/R, followed by the existing full-period matrix contraction. A target outside the generated cyclic subgroup must still be recognized or rejected using a paid membership/address procedure; discovering the order does not grant a discrete-log oracle.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
