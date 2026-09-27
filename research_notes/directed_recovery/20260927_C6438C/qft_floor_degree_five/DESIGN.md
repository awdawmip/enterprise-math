# Degree-five single-floor execution plan

Status: CODE_ONLY / NOT_EXECUTED / SHARED_CONTEXT / NOT_ADMITTED. The declared checker has not been imported or scientifically run. Syntax compilation is permitted; a coordinator-provided actual startup guard and explicit execution decision precede the one planned run.

## Contract and source

`typed_floor_degree_five.py` is frozen at SHA256 `755fcaf04832a5328e2464214f736ac661c410b3505edf10ab5218f935e2a7c7`, with proof `DEGREE_FIVE_RECIPROCITY.md` at `1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6`. Its 21 outputs are

    F[p,e](n,m,a,b) = sum_(0<=j<n) j^p floor((a*j+b)/m)^e,
    p>=0, e>=0, p+e<=5.

Inputs are exact Python integers, excluding booleans, with `n>=0,m>=1` and signed `a,b`. Constant powers include `0^0=1`. Scientific magnitude operations use the frozen actual signed BRC arithmetic base `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`. Its lazy, sparse and integer-precheck ancestry is separately pinned in the checker and in every exported query certificate. Neither an ideal propagator nor host pow/division/remainder is a comparator.

The recurrence normalizes signed coefficients, then applies a one-child Euclidean transpose. The source and proof were reviewed separately. This plan tests that implementation; it does not make a mixed-floor evaluator, infer an order/address, propagate phase states, or complete Shor sampling.

## Public checker-side certificate interface

- `DegreeFiveObserver.query(n,m,a,b)` records inputs, all 21 outputs, complete moment-node and signed-operation spans, and actual cache routing.
- `export_certificate()` produces schema `BRC_DEGREE_FIVE_QUERY_CERTIFICATE_V1`, full source/proof/checker/design pins, exact index family, requests and complete native integer evidence. It refuses unfinished work.
- `verify_degree_five_certificate(cert, replay_capture=...)` accepts a decoded JSON object and constructs a fresh observer. It replays requested inputs and compares the complete strict JSON structure. Tuples normalize to lists for serialization; booleans remain distinct from integers; non-string keys and floating values are rejected. Only the nonnegative integer `actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta` is excluded because its value depends on the process catalog cache. All digits, operations, node details, source/native proofs and other costs remain in equality.
- `incomplete_snapshot()` collects existing fields only. It does not call an arithmetic routine, build the catalog, complete a missing node, or assert a full certificate. An arithmetic exception leaves an inflight request and the observer refuses further queries. An ordinary invalid input before arithmetic leaves it unchanged and reusable.

The replay API lives in the checker for this bounded unit; no science module is changed. This is a correctness harness, not a hardened service for untrusted unbounded input. A malicious request list can request expensive work; no unproved global resource limit is supplied.

## Declared cases and independent typed comparator

The nine fixed `(n,m,a,b)` cases are:

    (0,5,3,1), (1,7,-3,-2), (4,5,0,3),
    (5,7,2,1), (6,5,13,-4), (7,4,-3,9),
    (8,9,7,-11), (9,7,0,21), (4,1,-2,3).

These cover empty length, one sample, normalized zero floor, zero height, lattice transpose, signed normalization, positive quotient extraction, constant nonzero floor, and unit modulus. The checker requires the complete five-branch set in recorded nodes. There are 189 output equalities and 44 finite-sum samples. These are declared fixtures, not a random accuracy estimate or a scaling benchmark.

For each case a separate `TypedFiniteSums` uses only the base arithmetic methods. At each public index `j` it computes `a*j+b` and its Euclidean quotient/remainder with typed operations, constructs powers by repeated typed multiplication, and adds all 21 terms into signed buckets. It does not call `moments`, `power_sums`, or the new `small_power`. Every sample retains affine and power spans and every term's prior bucket, term, new bucket and operation span. Scientific values are not recomputed with ordinary host arithmetic. Index loops, degree selectors, zero/type tests, hashes and cost aggregation are administrative wiring.

Each production certificate is JSON-round-tripped and freshly replayed. A separate paid cache/reuse control computes `(5,7,2,1)`, rejects an invalid modulus with unchanged state, then repeats the same valid request. The second request must be a cache hit with zero extra signed operations and nodes; the complete two-request certificate is also freshly replayed. A contained invalid-input observation in the original production case is not charged twice.

## Negative controls and unfinished work

Ten invalid input tuples are rejected before arithmetic: booleans in numeric positions, negative length, zero/negative modulus, a string, `None`, and floating length. Seventeen certificate controls are planned:

- Ten full paid replays followed by mismatch: a degree-five output, a different valid input, node output, normalization coefficient, transpose child, exact numerator, omitted zero term, signed trace, native proof field, and digit cost.
- One paid valid-prefix request followed by an invalid modulus. Its retained snapshot must contain the completed first request and raw arithmetic, `complete_certificate=false`, and no invented second node.
- Six early controls: extension pin, proof pin, schema, boolean first input, non-string key and boolean runtime counter.

The changed-valid-input control replays that changed input and must fail the complete evidence comparison; it is not expected to match the original honest replay. The other full replays must match their honest certificates after the one runtime-field exclusion. Attempted objects are stored with key types preserved, so `False` and `0` or integer and string keys cannot disappear into a metadata comparison.

No deliberate mid-operation scientific failure is injected by this grid. Unexpected exceptions are nevertheless captured in an outer `BaseException` handler. A LIVE registry exposes the production observer, finite comparator, fresh replay observer, completed output, current attempted input/certificate, native CALLS and disjoint intervals. Collection reads fields only and isolates per-field snapshot errors. Recursive child nodes that already completed are kept; a parent's internal local reconstruction that was never appended is **not** falsely reconstructed. The runner's existing raw operations, cache and inflight outer request show the interrupted boundary. Runtime/filesystem failure can still prevent writing a failure file; no unconditional durability claim is made.

## Costs, one-shot execution and reporting limits

The run starts in a fresh process and requires zero prior native calls. Empty-case export may itself instantiate the full-adder catalog; that call lies inside the first production interval even if its arithmetic stats contain zero digits. The checker expects one actual catalog call over the complete run, and retains its full receipt. This is not a claim of one arithmetic operation: all typed calls, digit replays, bit wiring and bit-length calls are separately recorded.

Costs are partitioned into production, typed finite sums, positive replay, cache control, cache replay, and paid negative replay. Early input intervals are zero-work but retained. Every runner instance is charged once by its final receipt; nested node ranges, detached snapshots and repeated evidence references are not new work. Peak recursion/observed integer size are maxima, not additive costs. Global native counts come from contiguous disjoint CALLS intervals, not a sum of overlapping catalog receipts.

`DEGREE_FIVE_RESULTS.json.gz` retains the complete raw evidence, `DEGREE_FIVE_SUMMARY.json` its hash and accounting. Unexpected failure writes `DEGREE_FIVE_FAILED_EXECUTION.json.gz`. Existing success or failure artifacts cause the main runner to refuse another execution. Sources and the startup guard are hashed before/after; the guard must authorize the current actual research activity with no sync debt. This check is an execution precondition, not a substitute for the coordinator's source review.

Elapsed time covers the checker before final serialization, including independent references and extensive replays. It is not a matched benchmark. Python allocation, hashing, JSON processing, interpreter internals and filesystem costs are not included in the digit counter. No asymptotic practical speedup is inferred from these bounded fixtures.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1 (author-read snapshot; coordinator may supply a journal-only refreshed guard).
