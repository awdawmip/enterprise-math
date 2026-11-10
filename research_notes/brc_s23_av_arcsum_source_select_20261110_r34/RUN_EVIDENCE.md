# R34 — actual local exact validation (2026-11-10)

Frozen pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Test environment: local Python 3, integer/Floor Sum arithmetic, standard library only.

```text
$ python /mnt/data/em_r34/VERIFY_R34_PORTABLE.py
PASS_R34_3_STAGES_223_SOURCE_SELECTS_4_PREFIX_RUNS_78_STAGES_298_AFFINE_RUNS
selected 223 runs 298 SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
R128 (0, 0) R389 (-7551, 28800) R1000000000128 (-4017401528447, 15321634290944)

$ cd /mnt/data/em_r34 && python VERIFY_R34_REGRESSION.py
PASS_R34_261_INDEPENDENT_FULL_PHASE_SORTS_AND_PREFIX_INCREMENTS
PASS_R34_GENERIC_HISTORY 64 101/101
PASS_R34_GENERIC_HISTORY 256 101/101
PASS_R34_REGRESSION_COMPLETE
```

Additional local comprehensive verifier `VERIFY_R34.py` generated all 298 exact records using the floor-sum prefix and compared byte for byte against local independent R32 fixture `AFFINE_RUNS_R32.tsv`. Output:

```text
prefix compiler: 3 Farey stages, 2 boundary risk differences, 223 source selects
source stages: [(128, 164, 36), (165, 225, 60), (226, 389, 127)] positive events: 225 compressed increment runs: 4
independent regression: 261/261 floor-sum risk and full phase partitions, both endpoints
full generator: 78 Farey stages, 28 Euclid decisions, 148 long-stage event blocks
affine runs: 298 R32 independent byte match: True SHA256: 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
final risk: (-4017401528447, 15321634290944)
PASS_R34_BULK_PREFIX_SOURCE_SELECT_3_STAGES_AND_AFFINE_298
```

The regression partition sort is a second validation algorithm; the published portable mathematical generator does not sort all future phase positions or iterate the 261 prefix cut updates. The portable checker uses endpoint-exact collision-free branch checks for the short-prefix differences `-127..389`.

Remote GitHub source paths are included next to this record in the same branch; remote existence/readback is tested separately from running Python. The exact portable and regression programs were executed locally before remote publication. Formal independent mathematical review remains pending.
