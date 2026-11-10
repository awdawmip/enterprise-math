# Author-side review record

The root agent delegated read-only review to `/root/robust_review`, sharing the
current experimental context. The review covered the four new kernel routes,
the harness, source adapter and mathematical note. It involved no timings,
remote writes or independent formal acceptance.

Correctness findings were incorporated before the final optimized verification:
the compact padded interval must contain its source bounds, not have identical
endpoints; its one-bucket shift must cover the interval; layout selection remains
distinct from actual half-spill acceptance; root and recursive diagnostics remain
separate. No kernel correctness blocker remained.

The subsequent proof-text review identified a missing hypothesis in the
positive20-cluster lemma. The final THEORY.md explicitly permits only cluster
values and external tails in that positive family, excluding interior-gap
contamination. It also states |E|<=actual tail occurrences, qualifies prefix
statistics after early abort, distinguishes spill occurrences from recursion
edges, limits the17-tail rejection to the stated construction, and corrects
the four-bin lower bound to >=65,512. These corrections changed the proof text,
not the frozen algorithm or input recipes.

The harness owner separately reviewed analyze_results.py without editing or
executing it during timing. Candidate references, ratio orientation and stage
counts were consistent:9 ordinary controls,16 total prior-plus-pdq controls,
and40 evaluation conditions after excluding old deterministic mechanisms.

Actual executed optimized and sanitizer results, and the benchmark's output
checks, are recorded in the execution receipts. This review narrative is not a
substitute for those results.
