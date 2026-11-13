# R36 exact execution evidence — 2026-11-10

Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Local full verifier and integration were actually executed with Python Fraction and integer arithmetic.

Full standalone verifier result: PASS_R36_BATCH_LAST_SOURCE_EXACT_FIVE_FAMILIES.
S23 m=128 n=389: four exact increment runs; R389=(-7551,28800); three Farey stages, 19 batched F rank queries, 259 source-owner lookups, zero per-arc Floor Sum queries for F after rank preprocessing, 2304 whole-risk source count calls, 261 independent phase reconstructions, 33536 independent owner-count checks.

sqrt2-1 m=16 n=96: seven runs, R96=(106,-254), five stages, 23 F queries, 80 phase reconstructions and 1296 independent arc checks.
sqrt3-1 m=32 n=180: 11 runs, terminal (929,-1268), five stages, 34 F queries, 148 phase reconstructions and 4768 independent arc checks.
1/3+sqrt2/10^7 m=21 n=126: one run, terminal (-105,315), 36 stages, 71 F queries, 105 phase reconstructions and 2226 independent arc checks.
sqrt2-1 m=16 n=320: 16 runs, terminal (-463,1120), eight stages, 50 F queries, 304 phase reconstructions and 4880 independent arc checks. This case exercises the non-scanning dense-stage rank/select implementation.

The compact verifier was executed with the original R34 source and printed:
R36 PREFIX [(129, 164, (16, -61)), (165, 292, (-43, 164)), (293, 328, (0, 0)), (329, 389, (-43, 164))] F QUERIES 19 OWNER LOOKUPS 259
PASS_R36_COMPACT_BATCH_EXTINCTION

Integration: original R33 quotient-jump + R32 bulk compiler with the R36 prefix. Output:
PREFIX 4 no individual events, fibre-extinction queries 19
STAGES 78 Euclidean jump decisions 28
TAIL 148 direct bulk blocks, FINAL 298 runs
RESULT (-4017401528447, 15321634290944)
SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
PASS_R36_298_TRILLION_HORIZON_BYTE_IDENTICAL

The standalone extended source and generated full certificate, including per-arc last-source indices and strict rational interval endpoints, are available in the R36 downloadable research bundle from the same turn; this remote text is a subset of the evidence, not a claim of canonical mathematical acceptance. Mathematical independence review pending.

Native research service registration/control: session_start and task list requests initially returned QUEUED; a subsequent read of their receipts was blocked by BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false. Thus no Researcher-ID, Research-Activity-ID, shared owner or formal CLAIM is asserted in this R36 record. The GitHub author branch is an independent unclaimed scientific draft. No credentials were written.
