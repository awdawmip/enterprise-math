# R72 exact computation and author-side research status

Execution environment: local Python 3, standard-library Fraction; one full checker and one separately executed minimal checker. Original science input freeze: 43ec6098b1330ae86d0a7863be336c5d97f6ef34; R71 author branch provenance: 0b5319d7a0caf90dcd210e291152c6c06bbc2828.

Full checker output (actual): random seed 7220261111; update_checks=11520; versions=2700; query_checks=890; independent_interval_queries=150; independent_interval_strata=572; oracle_points=2670; methods={fallback_after_groups:110,fallback_all:780}; persistent_targeted_versions=12; successful certificate-reuse cases=1. All assertions passed. Independent stratum oracle constructs exact affine jump/intersection points, checks each point and each open cell's rational midpoint; it is different from the integer-level feasibility routine.

Measured family, 1 run (seconds):

n | groups | build | hybrid 20 queries | direct 20 queries
32 | 2 | 0.000493 | 0.001996 | 0.014057
128 | 2 | 0.001935 | 0.001982 | 0.059530
512 | 2 | 0.009187 | 0.002131 | 0.219468
1024 | 2 | 0.019914 | 0.002750 | 0.449537

The fully executed `check_r72.py`, raw `VALIDATION.json`, proof and SHA256SUMS are bundled as a complete local downloadable archive in the originating conversation; this GitHub directory contains the readable theorem and a separately executed minimal exact repro `check_r72_min.py`. The local full script was not copied into this GitHub commit. GitHub artifact branch and a valid author-side session do not establish a formal native task CLAIM, Result or independent Review; those require their own actual readback.

No claim of native BRC dynamics or universal bit-cost speedup.