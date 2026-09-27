# Exact signed scalar-gap counts

Status: AUTHOR_EXECUTED_BOUNDED / SHARED_CONTEXT_REVIEW / NOT_ADMITTED.

This stage implements an exact integer observer for one contiguous scalar gap with exactly one negative bit. The first preserved version uses three degree-three floor-moment queries. The new version uses one window query and the unsigned pair count `T` for the full interval:

    K(g,k,R,r) = 2 J_zero - J_plus - J_minus = 4 J_zero - T.

The interface supports physical stride one. It does not certify a modular order, discover a target logarithm, or connect this counter to a full Gram sampler. The positive result is a concrete polynomial-bit query algorithm for this restricted sign family, not a general Shor simulator or a proven overall speedup.

The original declared run covered nine `(g,k,R)` tuples and all 31 associated residues. Every result agreed with a separately executed typed exhaustive comparator covering 1,764 pairs; fifteen input rejections, nine tamper rejections and full certificate round-trip replays passed. A second, separately versioned one-window run matched every frozen original value, passed fresh complete certificate replays and six new tamper checks. The original enumeration was not rerun. Negative coefficients, even counting moduli, `R=1`, and the lowest/highest negative bit are preserved in both versions.

Production digit replays decreased in every tested tuple, from 265,478 across the original cases to 137,611 for one window. This is a recorded operation-count comparison with the frozen baseline, not a wall-time benchmark. The new total remains above the small exhaustive comparator's 76,977. One-window positive/negative verification adds 137,611 / 16,116 digit replays. Each separate process made one actual 12-state BRC kernel call and reused all full-adder columns. Native calls, digit replays and host work remain distinct. See `signed_gap/ONE_WINDOW_EXECUTION_NOTE.md` for the final result, and `signed_gap/SIGNED_GAP_OBSERVER.md` for the unchanged first-generation record.

Both seven-file generations are preserved: implementation, checker, pure-I/O reader, explanation, summary, readback record and original results gzip. `STARTUP_GUARD.json`, the one-window proof and final shared-context reviews are published alongside them; the guard's binding also appears in complete raw evidence. The root `activity_observation.json` and `startup_guard.py` remain local administrative provenance and are excluded by the publication selector. Packaging discovers selected gzip artifacts automatically and transports their complete bytes through hashed readable chunks; the ZIP also includes each original gzip. `DEPENDENCIES.md` identifies the external pinned runtime. This is a complete new-stage evidence package, not a dependency-free execution environment.

`CONTINUE.md` provides an immediate mathematical continuation for any dialogue. The mathematical question is not gated on access to a named tool or machine. No new professional query or remote publication was performed by this preparation step; actual source and delivery commits are supplied only by the publisher's final receipts.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
