# Migration 18 — Phase32 exact textual machine CLI

Status: locally validated candidate, no default/browser/main cutover.
Remote baseline: awdawmip/enterprise-math@44c5f034d38726990f83ff3e05d5b0eff520cea7 (M17).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual change

The real phase32_lab command now accepts --machine-only with --cell-pitch,
--cell-bits, --cell-max-bits and --readout-scale. The new typed machine config
contains only integer phase inputs, histogram dimensions and selected factors.
It rejects, rather than silently drops, legacy pitch/camera/view fields. The
old displayed/default path is unchanged in the tested object and JSON cases.

The existing textual ratio parser is reused: 0.50 remains 50/100, and 2/2 is
not reduced. Pitch is lattice spacing, so the unchanged Phase32 certifier uses
its inverse: 50/100 pitch supplies 100/50 scale. This is not inferred from a
float. build(..., include_display=False) retains complete exact cell certificates,
phase source and precision without calling display validation or pixel functions.

Only build and main change existing function ASTs. All old phase generation,
metrics, multiplication, hex_data, rendering and local lexicographic tie functions
remain unchanged. BRC reuse is REUSE_EXECUTED_UNCHANGED, including the uint32
carrier, exact divisions/roots and true-tie adapter. No new scalar family.

## Use

```bash
PYTHONPATH=src:tools/nollm_visual_toolkit \
python -m nollm_visual_toolkit.phase32_lab \
  --machine-only --count 4096 --mode golden --cell-pitch 0.50 \
  --report phase32_exact.json --hex-data phase32_cells.csv
```

Machine config input is NOLLM_PHASE32_MACHINE_CONFIG_V1, produced by
phase32_lab.machine_config(). It supports seed, prime overrides, sectors/rings
and factors a/b. --config and explicit --count/--mode cannot be mixed. It does
not accept the old displayed configuration as an exact source.

Machine reports use NOLLM_PHASE32_MACHINE_REPORT_V1 and preserve source spelling,
precision, exact CV-squared readouts, phase/product defects and a cell summary.
The live model retains full point certificates; the report avoids duplicating
that potentially large list. --readout-scale none explicitly keeps ratio-only
readout:null. Zero phase remains undefined; spiral nonclosure is not erased.

JSON/CSV exports reuse the existing visual-data V2 carrier and retain all IDs,
including zero. No ideal pixel fields are fabricated. Positive collision metrics
exclude zero, as in M17. A low-budget unresolved report remains usable, but a
requested complete-coordinate export fails before any requested write. Similarly,
a source beyond the V2 coordinate domain can be reported but is not truncated
into V2. Input/output aliases and hard links are rejected. These semantic checks
do not claim filesystem rollback after an I/O failure.

## Validation

The gate records 209 tests: 207 passed, zero failures/errors and two expected
source-slice skips. All 26 new tests passed; 183 tests are retained. The only
skips are the original deterministic-HTML and site-template tests because the
unchanged phase32_lab.html is not in this focused source slice. Numerical skips
are zero and no retained expectation was weakened. Exact-policy checks cover
certified_hex.py and angular_dispersion.py, not the mixed display/CLI module.

The new tests exercise actual in-process and subprocess CLI paths, exact lexical
sources/inverse pitch, malformed inputs, custom integer configuration, readout
scales/null readouts, no-display execution with float/display functions disabled,
JSON/CSV consistency, low-budget reconstruction, carrier limits, detached reports,
no-clobber checks, zero/nonclosure and local true ties. Eighteen complete legacy
or displayed-exact object cases stay equal to frozen M17. One new legacy routing
test explicitly stubs render; it is not a browser test. An initial test-loader
error omitted the frozen module's package name; only that test fixture was fixed
and the failure log was retained.

Nine 4096-identity actual CLI cases (golden/hash/spiral times pitches 0.50,1,3/2)
and a 65536 golden/pitch-one case pass. Complete certificates, phase/factor
states, all identity records and exact statistics equal frozen M17. Every case
is fully certified. The 65536 case has 47497 occupied positive-population cells,
18038 collision excess and zero unresolved identities. These are finite checks,
not a universal termination proof, independent implementation or speed claim.

Clean replay on the byte-verified local M17 source slice reproduced all tests
and all ten population cases. Five source/fixture files, the test report and
four population JSON files match byte-for-byte. Patch SHA256:
524af1b1e6acb1b7a104a8f9afd4073c12e7676205e5dce69142dad5cca1472d.

Reproduce: python tools/run_migration18.py. For population checks run
python tools/benchmark_migration18.py --mode golden (then hash and spiral), and
python tools/benchmark_migration18.py --count 65536 --mode golden --pitches 1.

## Boundaries and recovery

Phase32 HTML/browser still uses the old observer. --machine-only explicitly
rejects --out/--preview/--site, and exact flags cannot silently affect legacy HTML.
The generic multiplicative report reader does NOT accept this new Phase32 schema;
its dedicated reader is the next actual consumer. Full-package/M15 admission,
Phase32 browser migration, native file/http/Safari/iOS, independent review,
whole-repository regression, default changes and code-main integration remain
separate and unpassed. Geometry remains declared A2, not native X6/P000.

The delivery bundle is a focused source slice, not a complete application or
repository mirror. Never copy its isolated src/enterprise_math/__init__.py into
production. Apply migration18.patch to the pinned M17 source; do not replace
whole source directories. Older local M13 evidence in bundle history is provenance,
not current remote M13 authority. The current validation files and source manifest
control this slice.

Next: add a reader for the Phase32 machine report, preserving its exact source,
pitch, original precision and readout settings. Reuse the current arithmetic;
keep browser and complete-package acceptance on their separate tracks.
