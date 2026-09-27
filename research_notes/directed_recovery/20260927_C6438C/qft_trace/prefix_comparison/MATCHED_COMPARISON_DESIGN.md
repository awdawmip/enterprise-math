# SO trace versus rank-two bank: matched-prefix design

Status: **compile-only, not executed**. This is the next bounded timing comparison, separate from the completed policy correctness check. Root review and a distinct execution authorization precede running the script. No old source or scientific artifact is changed.

`compare_so_trace_prefixes.py` follows the frozen boundary comparison design (`compare_guarded_prefixes.py`, SHA-256 `78e70a1a27273ae3651cd3e7807d5774e4168e3c51119f26853634b52fd3aa6b`). The new script pins that template and the completed SO-policy source `62121d7c1e1a7eafff452990b991ddfe027e65ada5e980881aa4d716de92bd20`; all actual policy and bank dependencies remain frozen. Compilation passed without importing or invoking the scientific program.

## Predeclared scope

Use exactly three programs: `(N,a,t)=(21,2,4)`, `(21,4,4)` and `(65,3,4)`. Every run follows the same fixed positive history `1000` with epsilon `1/3`. Complete 61-column native admission and the existing exact six-coordinate codec are retained. These are diagnostic positive prefixes, not random independent samples or complete output laws.

The old route is `BoundaryCheckedUniform` with the actual old `WordCertificateBank`; the new route is `BoundaryCheckedSOTrace` with the actual `SOTraceBank`. The new route has its own type and certificate/policy/cursor schemas. The source does not substitute a new bank into the old type contract.

Build both cold banks once, with separate call intervals, complete evidence and elapsed times. Cold construction is outside measured warm prefixes; full program/native admission is also separate. For each program, explicitly pay for one old-route preconditioning run of `1000`. Both banks are bound to that same program. Every measured run constructs a fresh Gram engine, while sharing the same actual program's warmed factory and inverse modular caches and native primitive cache.

Measure two paired orders per program: old then new, followed by new then old. Thus there are six pairs and twelve measured fresh engines, plus three paid warmups. Execution is serial in one process. Ordinary operating-system load is uncontrolled; two alternating pairs per fixture are not sufficient for a broad performance distribution or statistical significance claim.

## Timings and counters

The calculation interval includes engine construction, four `advance` calls and final `mass`. The constructor's dependency reads and public binding checks are included; this is the observable API cost being compared. Evidence capture is timed separately. Between those intervals, host counter/table snapshots are also recorded, with their elapsed gap explicit. Detaching the final evidence and JSON/gzip writing are outside the calculation and evidence-capture times.

Each run saves actual native call intervals, Gram/vector/observer counters, full binding-check counts, guard nesting counters and every signed correlation matrix. Before and after the timed computation it records both factory and already-created inverse table instances, preserving their separate identities. All measured runs must create zero new modular columns and perform zero additional column adder-digit replays; the checker asserts this instead of assuming that factory-only warmth covers inverse caches. Final per-program factory/inverse receipts and permutation-verification receipts remain in the raw artifact. Shared cumulative tables must not be summed once per route in later accounting.

No improvement is presumed. The cold trace observer count fell from 205 to 36 in the prior actual bank execution, but SO program binding performs stricter host serialization. Warm queries may therefore be slower. A result showing no gain or a regression must be retained unchanged. Cold single observations, warm prefix timings and complete-program costs remain distinct claims.

## Equality and failure requirements

Every pair must have equal numerical conditional plans, raw terminal mass, selected word IDs, charges and bits. Every retained correlation matrix, the complete actual observer stream, Gram counters and policy counters must agree. Terminal mass must be positive. Old/new certificate hashes and schema bytes intentionally differ; cross-version strict cursor equality is neither tested nor claimed. The completed policy unit already covers new-version strict pending restore, seven cursor failures, two type failures and same-bit budget retry, so this timing script does not repeat those scientific tests.

A target or summary already present causes rejection before scientific setup. Unexpected failure writes a unique `FAILED_EXECUTION_*.json.gz` preserving known context, completed cold/warm/pair evidence, available unfinished state and all actual CALLS. The incomplete snapshot does not call the scientific engine to manufacture a completed certificate. A failed run is never renamed as success or silently repeated. Source hashes are checked again before success serialization.

Expected success files are `SO_TRACE_MATCHED_PREFIX_RESULTS.json.gz` and `SO_TRACE_MATCHED_PREFIX_SUMMARY.json`, plus a separately redirected execution log. None exists or is claimed by this design. Even a successful equality/timing experiment would establish only this bounded comparison, not efficient general QFT dequantization, an asymptotic improvement or a cold-start/full-factorization speedup.
