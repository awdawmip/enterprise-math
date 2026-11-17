# OAI7-090-A — Original finite-checker run and exact certificate scope (2026-11-17)

Task: RS-OAI7-090-A-20261007-6F2A81; publication TP2-79BD2127769C593E5315.
Researcher: EM-DIRECT-207199; owner CLAIM MCP-da50655f1bc8c7a7fe420cf4; RUN RUN-881dbd8f1db5f00e6350facf (resumed generation 2).
This is first-party author execution evidence; not independent mathematical review or project theorem admission.

## Frozen original source and byte identity

- Repository: openai/math, commit adc7f1241b42e322a6451854ab7e4b4c146bf78a.
- Path: preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py
- Git blob SHA-1: 23768a5c2d88e100399bb5c4347447e86a7160cb (matching the task's exact checker pin).
- File size: 12726 bytes. Local Git blob hash recomputed as 23768a5c2d88e100399bb5c4347447e86a7160cb, matching the separately fetched GitHub connector file.
- Local original source SHA-256: 5689152e970b652a8e40c3c120eda3b45320c8745968a5cb416fa9b9dbdc5385.
- Upstream verification/README.md Git blob SHA-1 e2b9d904c74538450cea628476bcd6c772776c23: Python 3 standard library, assertions enabled, zero exit/no output is success, script writes no result files.

## Exact command and captured outcome

Executed without modifying original source, with Python 3.13.5 (sys.flags.optimize=0), in isolated mode:

```sh
/usr/bin/time -f 'WALL_SECONDS=%e MAX_RSS_KB=%M' timeout 150s python3 -I -B /mnt/data/OAI7_090_original_check_certificate.py > /mnt/data/OAI7_090_original_checker_run.log 2>&1
```

Start UTC: 2026-11-17T12:33:13Z; end UTC: 2026-11-17T12:33:17Z.
Actual command exit code: **0**. No stdout/stderr emitted by checker. Only the external `time` wrapper wrote:

```text
WALL_SECONDS=4.20 MAX_RSS_KB=98956
```

The run was not timed out. Captured log SHA-256: f153447f55c45e45a93d8702769394b70411faa75cbbc2a08cf1c3326125a56e.

## Finite coverage mapped to checker constructs

- `envtable()`: outward-rounded interval checks for the pi enclosure, finite residue polynomial bounds, matrix/envelope coefficients, absolute tail constants, curvature and finite Taylor remainder. These are individual finite assertions, not global analytic propagation.
- `approx()`: two 20-by-20 interpolation inversions with positive interval pivots and norm caps, residual/near checks and bounded coefficient norms.
- `powsol(data)`, `bern(X)`, `vmin(row)`, `test(X)`: 14 (m,y) configurations. The positive-sign branch has 14 degree-20 Bernstein tables (294 row bound checks); the ordinary opposite-sign branch 13 degree-20 tables (273 row checks); the exceptional m=1,y>0 branch replaces the latter with four degree-22 tables (92 row checks). Thus **27 × 21 + 4 × 23 = 659** Bernstein row-bound evaluations, beyond the other scalar assertions.

## Evidence boundary

This exit-0 result verifies that the exact pinned Python checker completed its asserted finite calculations in this execution. It does **not** independently prove correctness of the manuscript's infinite-series correction, global sign/positivity propagation for all scales, sharp Gaussian minorants, Fourier/energy transfer to all locally finite centered-density-one configurations, or any transfer from external Euclidean R² to Enterprise Math native X6, six-axis cells, signed path provenance or triadic dynamics. The manuscript's strong universal-energy claim remains an external source proposition requiring independent proof review.

Reuse the prior staged source-map audit `OAI7_090_FINITE_CHECKER_SCOPE_MAP_20261117.md` alongside this exact execution receipt. Preserve the initial task Source pins and actual author/source-exposure history; no theorem acceptance or separate Driver review is asserted.
