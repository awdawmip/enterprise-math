# PCF2 Sealed Benchmark Evidence

Status: `FROZEN / TASK-LOCAL EVIDENCE`

This directory freezes the public parameter manifest, replay/result schema, and compact benchmark result summary for `RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE` / `TP2-FDEB9BE4503CD9C60E59`.

The benchmark is dual-compartment: private factors remain inside corpus generation/verifier state and are never serialized to the candidate worker. Candidate requests contain only `N`, an independent public seed, a candidate identifier, and precommitted public parameters.

Authoring replay:

`python scripts/check_prime_coord_factor_blind_benchmark_suite.py --out /tmp/pcf2_report.json`

Independent public-report verification:

`python scripts/check_prime_coord_factor_blind_benchmark_suite_independent.py --verify-report /tmp/pcf2_report.json`

The final full-report digest and all load-bearing aggregate results are pinned in `benchmark_result_summary.json`. Finite corpus results are regression/falsification evidence only and do not establish an infinite factorization theorem.
