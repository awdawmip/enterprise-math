# R40 — Evidence, verification scope and next R41 unit

**Recorded:** 2026-11-10 (Asia/Shanghai).
**Frozen S23/AV scientific input:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
**R39 predecessor:** commit `299f6986939404fbb10e9085a111a5bd462180ab`.
**Mathematical status:** author-derived exact identity and finite computation; independent project theorem review pending.

## Exact runs

The locally executed full program `VERIFY_R40.py` generated the deterministic 14-family `CERTIFICATE_R40.json`, SHA-256:
`c5338336afd23f3bba4b76732f0d19d57b9a36003d09a8d7ec65480fb0c8b76a`.
Final line: `PASS_R40_ENDPOINT_COBBOUNDARY_14_CASES c5338336afd23f3bba4b76732f0d19d57b9a36003d09a8d7ec65480fb0c8b76a`.

The complete exact tests cover near-rational theta=1/3+sqrt(2)/10^k, near fifth/seventh, sqrt(2)-1 and sqrt(3)-1, historical m in {16,21,31,32,50,72,128,129,257}, source J up to 10^15 and window N up to 10^12, two short source-window brute-force oracles, and negative source indices. Comparisons use exact rational `Fraction`, integer square root isolation, an independently coded Euclidean Floor Sum reference and last-source rank/select per historical owner.

The **remotely published, standalone** `VERIFY_R40_COMPACT.py` is independently executable (Python 3 standard library only) and checks four families with full arc-count comparisons at four thresholds and exact last-source boundary checks. Its observed output:

```
NEAR_THIRD_21 m 21 query_calls 627 owners 21
MIXED_128 m 128 query_calls 3802 owners 128
SQRT2_129 m 129 query_calls 3831 owners 129
NEGATIVE_WINDOW m 16 query_calls 144 owners 16
PASS_R40_COMPACT_FOUR_EXACT_FAMILIES
```

## Timing observations, not a complexity theorem

Local Python 3-run median R39 Floor Sum / R40 coboundary respectively:
- near 1/3 m=21: 5.424 / 0.849 ms;
- mixed m=128: 13.013 / 8.789 ms;
- mixed m=257 with 45 narrow owners: 8.335 / 8.615 ms;
- near 1/3 m=21 and J=10^15: 6.309 / 0.946 ms.

These samples are sensitive to implementation, input bit length, memory and threshold sharing. The new method removes Euclidean *sum* calls within the count primitive, yet does more scalar integer divisions in some cases; precise end-to-end bit costs are unsettled.

The complete local run bundle, `R40_RESEARCH_BUNDLE.zip`, contains `PROOF.md`, `VERIFY_R40.py`, `VERIFY_R40_COMPACT.py`, `CERTIFICATE_R40.json`, `BENCHMARK_R40.py/json`, `EVIDENCE.md`, and `NEXT_TASK.md`. The GitHub proof and compact self-contained verifier supply an independent remotely reproducible minimum; the full certificate remains conversation-side until separately uploaded to an authorized Source surface. GitHub author evidence publication never grants a shared TASK CLAIM.

## R41 precise next question

Can a cost-adaptive hybrid of R37 suffix coverage, R38 congruence channels, R39 shared Floor Sum and R40 endpoint coboundary integrate with the **frozen S23/AV 298 maximal affine-risk intervals**? First reproduce R32's entire exact interval data and SHA-256, keeping owner labels; then measure total integer-bit costs including rational enclosures, preprocessing, scalar floors, Euclidean sums, branch/source representation, memory and output serialization. Evaluate different m and near-rational parameters, with a separate independent oracle. Preserve the original scientific freeze and current owner/claim authority.
