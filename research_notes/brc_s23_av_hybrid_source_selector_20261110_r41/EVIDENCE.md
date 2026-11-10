# R41 exact evidence and reproducibility

Scientific input freeze: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Project-scoped author-side proof/experiment, 2026-11-10.

## Local actually executed Python runs

`python VERIFY_R41_STANDALONE.py`:
```
S23 {'scan': 164, 'remaining': 0, 'floors': 0, 'thresholds': 0} oracle_calls 3960
NEAR_THIRD_21 {'scan': 84, 'remaining': 18, 'floors': 2402, 'thresholds': 58} oracle_calls 581
MIXED_257 {'scan': 869, 'remaining': 0, 'floors': 0, 'thresholds': 0} oracle_calls 7109
PASS_R41_HYBRID_SUFFIX_COBBOUNDARY_THREE_EXACT_FAMILIES
```

`python VERIFY_R41_INTEGRATION.py`, using exact prior R32/R33/R36 scripts and the R32 298-run TSV from the bundled `src/`:
```
R41_FULL_298 HYBRID 3 initial stages 298 runs (-4017401528447, 15321634290944) 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
R41_FULL_298 ENDPOINT_ONLY 3 initial stages 298 runs (-4017401528447, 15321634290944) 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
PASS_R41_298_AFFINE_RUNS_WITH_HYBRID_AND_R40_FORCED_ENDPOINT
```

`python VERIFY_R41.py` additionally tested the optional certified q-lane partition on five parameter families, an exact independent Floor Sum oracle, and both full-298 strategies; completed:
`PASS_R41_HYBRID_CERTIFIED_LABELS_AND_298_AFFINE_RUNS`.
The deterministic JSON `CERTIFICATE_R41.json` and actual predecessor source scripts are included in the local bundle. `VERIFY_R41.py` is the extended multi-method validator; the remote standalone script verifies the core hybrid theorem independently.

## Python benchmark, three samples per case (medians)

| Family | R40-only ms | R41 adaptive ms | R41 adaptive exact work |
|---|---:|---:|---|
| S23, m=128 | 11.785 | 1.994 | 164 certified sources, zero fallback floors |
| Mixed near-third, m=257 | 39.695 | 7.368 | 869 certified sources, zero fallback floors |
| Very-near-third, m=21 | 1.369 | 1.425 | R40 direct: 2,442 certified endpoint scalar floors |

Timing is machine- and Python-implementation-dependent. The full benchmark JSON and logs are retained in the bundled experiment record. All algorithms returned identical owner-labelled source vectors in the same cases.

## Source dependency and reproducibility notes

`VERIFY_R41_STANDALONE.py` is self-contained: it embeds the unchanged R40 exact arithmetic and Euclidean Floor Sum oracle from [R40 commit ea6e28c](https://github.com/awdawmip/enterprise-math/blob/ea6e28c0ce180328ca883f713fb08bfece5a7581/research_notes/brc_s23_av_endpoint_coboundary_20261110_r40/VERIFY_R40.py) followed by R41's suffix/coboundary method and tests. It uses Python 3 standard library.

`VERIFY_R41_INTEGRATION.py` and extended `VERIFY_R41.py` require the original source programs under `src/`: R32 `VERIFY_R32.py`, R33 `VERIFY_R33.py`, R36 `VERIFY_R36.py`, R37/R38/R39/R40 verifiers, and `AFFINE_RUNS_R32.tsv`. The immediately supplied local `R41_RESEARCH_BUNDLE.zip` contains these bytes so the actual end-to-end result is reproducible without reconstructing missing prior author-side code.

The previous R32 six-column affine-run digest is `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`. The hybrid and forced R40 configurations both reproduced its exact bytes. This is a full S23/AV risk replay; not a proof of a universal bit-complexity improvement.

## Review/authority status

Native activity and current S23 owner verification were attempted through the authorized project control gateway; its result-read returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`. No session identity, active CLAIM or shared task completion is asserted. This Draft PR is an author-side scientific artifact. Independent mathematical review is pending.
