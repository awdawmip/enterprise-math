# Input-integrity review correction and v2 saved-record check

Status: V1_STATIC_PASS_WITHDRAWN / V2_SAVED_RECORDS_PASS. Shared-context author review, not independent formal admission. No scientific computation was run by this reviewer.

The earlier v1 static PASS was incorrect. I failed to follow the real wrapper initialization path. `adjacent_trace.load_frozen()` returns the free-trace module and an imported HBW module; that module does not expose a module-level `old`. The existing runner imports `native_relative_port` explicitly from the frozen `helper.OLD` directory and attaches it to a `Work` instance if needed. Treating `hbw.old` as an initialized interface was an unjustified assumption.

The preserved v1 tool receipt reports chunk `d0d632`, exit 1. Its saved failure is at `IMPORT_FROZEN_WRAPPERS` with `AttributeError: module 'free_trace_frozen_hbw' has no attribute 'old'`. The failure has no native admission, arithmetic operations, or native-call payload. This was an import-only failure, not a failed arithmetic result. The old source, plan, STARTED, failure and actual tool receipt remain untouched.

V2 source `041032580718b64d2c9645015d04839062d4dca4e7001b1e6387bbe7d7b03e28`, plan `80ae98bba7de2bdc7bf2c54ae492cc672e714a036ac7c5ae23361f215e3477cc` use the explicit import after STARTED. I read the actual helper, free-trace loader, HBW initializer and existing adjacent run path. `helper.OLD` resolves to the directory containing the pinned `native_relative_port.py`; the input check needs its `source_check()` and `lm.Arithmetic`, not a Work object. The remaining declared arithmetic consists of one multiply, two compares and one divide. No ordinary host scientific answer is substituted.

The coordinator's unique v2 tool receipt, chunk `e54843`, reports exit 0. The new stdlib-only `read_input_integrity_correction.py` reads the complete existing gzip, checks its source/plan/STARTED/guard bindings, actual tool output, native vendor and arithmetic source hashes, then consumes all four operation traces using two source-pinned saved-wiring audit functions. Those functions inspect recorded carries, bit routing and native column lookups; they do not call the scientific arithmetic modules or recompute answers through host multiplication, modulo or gcd.

All 43,148 native digit cells pass. The one arithmetic stream has 4 typed operations, 433,427 recorded host bit-wiring operations and 406 arithmetic bit-length calls. The process admitted the native catalog once; the later arithmetic native-call delta is zero. Catalog invocation count and digit work are separate quantities.

The saved result says the supplied labels multiply to the displayed block, not to the full decimal input. Its typed division of the full input by that block returns quotient `1000000000000000000000000000001` and remainder zero. This establishes input consistency only. It is neither a primality proof nor evidence that the independent factor-blind public-clock runner discovered the supplied factors.

Raw SHA-256: `a5ec56bfd6423118fa822eeed923d384e38e52e873bb40ac9e34e688702f99a1`; gzip SHA-256: `e73fac814ac934047839f2c0e3ac9da80f3110fa529b87b69957758904cb927d`. The accompanying `INPUT_INTEGRITY_RECORD_CORRECTION.json` binds this new reader and the preserved v1 failure. This review supersedes only my incorrect v1 PASS; it does not rewrite the execution history.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1, reviewer's actual canonical read. The scientific execution records retain the coordinator's separate actual read/guard.
