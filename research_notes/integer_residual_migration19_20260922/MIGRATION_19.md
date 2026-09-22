# Migration 19 — Phase32 report replay through the existing data reader

Status: locally validated candidate, not default/main/browser admission.
Remote baseline: `1a7ae808f63c8e3b9a463c1738c50bf485709096` (M18).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual change

`phase32_report.py` reads `NOLLM_PHASE32_MACHINE_REPORT_V1`, reconstructs the
saved machine configuration, pitch, original precision budget and CV-squared
readout scale, and reuses the existing Phase32 producer to compare every report
field. The actual existing `core.read_data` dispatch gains three lines for this
schema. Ordinary visual JSON/CSV and the separate multiplicative-report reader
retain their prior routes. No phase, BRC, root, interval, cell or tie algorithm
changes; the unchanged producer and old reader are pinned by Git-blob tests.

```bash
PYTHONPATH=src:tools/nollm_visual_toolkit \
python -m nollm_visual_toolkit.phase32_report phase32_exact.json \
  --verified-report checked.json --hex-data cells.csv
```

With no output arguments, this verifies without writing. `core.read_data` also
accepts this report and returns the existing V2 data carrier after replay.

## Source and observation semantics

CLI lexical pitch remains lexical: `0.50` is `50/100`, not inferred from a
float or replaced by `1/2`. Existing direct Python reports can instead contain
only the explicit integer-ratio source; the reader accepts that original shape
without fabricating text. The unchanged certifier uses inverse pitch as scale.

Original precision is replayed, not automatically refined. A low-budget
`UNRESOLVED_BOUNDARY` remains a valid reproducible observation; complete-coordinate
export refuses unresolved cells. Both saved histogram readouts must have the
same positive integer scale or both be null. `readout: null` stays null; custom
histogram dimensions and ordered counts are retained.

Parsing rejects duplicate keys, float/nonfinite tokens, non-JSON values and
invalid schemas. Full typed JSON comparison distinguishes booleans from integers.
The dedicated reader has explicit byte/nesting/decimal-string resource limits;
these are not mathematical-domain restrictions. The existing generic core reader
still does ordinary JSON schema inspection before dispatch, so its whole file
intake is not claimed to have the dedicated reader's bounded-allocation contract.

V2 exports retain all identities including zero, the original complete machine
report, exact pitch and precision, and no ideal pixel fields. Positive occupancy
metrics continue to exclude zero. Reports outside the V2 coordinate range remain
valid reports but cannot be exported by clamping or guessing. The adapter takes a
detached source snapshot before replay; a later mutation of the caller's object
cannot attach an unverified source to the verified cells.

Replay establishes deterministic consistency, not authorship/authentication or
independent mathematical proof. A consistently changed source and all its results
may form another valid report. Imported cells are an A2 observer, not native X6.

## Validation

248 recorded tests: 246 passed, zero failures/errors, two retained template skips.
All 39 new reader tests passed. The 209-test M18 gate is retained without weakened
expectations. Its two skips are only deterministic HTML/site tests because the
unchanged production `phase32_lab.html` is absent from this focused source slice;
there are no numerical skips. Existing exact-policy targets remain
`certified_hex.py` and `angular_dispersion.py`, not the mixed data/display module.

The new tests exercise both source shapes, complete models and certificates,
custom/null readouts, true local lexicographic ties, zero/nonclosure, tampering,
detached sources, missing BRC, disabled display functions, real CLI subprocess,
JSON/CSV, old-reader compatibility and existing collision/neighborhood/trajectory/
profile consumers. All semantic output checks precede writes, including aliases
and hardlinks. This is not filesystem rollback after an I/O failure.

Nine 4096-identity populations (three modes x pitches 0.50, 1, 3/2) and one 65536
population all matched the unchanged M18 producer: full model, complete point
certificates, full report, identity records, original report metadata and CSV
roundtrip. The 65536 golden/pitch-one population has 47497 occupied positive cells,
18038 collision excess and zero unresolved identities. These are finite replay
checks, not independent numeric-oracle tests or a universal termination proof.

A clean baseline patch replay repeated all 248 tests and all ten populations.
Five implementation files, tests.json and all four population reports match
byte-for-byte. Patch SHA256:
`0ffc3c3d81658244b45e580855611cf97b1cc2495e3ed634396235ebc80a5564`.

## Delivery and remaining scope

```bash
python tools/run_migration19.py
python tools/benchmark_migration19.py --mode golden
python tools/benchmark_migration19.py --mode hash
python tools/benchmark_migration19.py --mode spiral
python tools/benchmark_migration19.py --count 65536 --mode golden --pitches 1
```

The delivery is a source slice, not a complete checkout. To run the existing
production M13 route locally, its unchanged `multiplicative_report.py` was
materialized and verified as blob `b15c73d205f89558df45c75867ffd38180bf6a5a`.
That materialization is not a production change. Apply `migration19.patch` to the
pinned M18 source; never copy the isolated `src/enterprise_math/__init__.py` over
the production package. Tests need the inherited Node runtime and mpmath oracle;
production replay reuses BRC and does not depend on mpmath.

Phase32 browser migration, M15 real-template/full-root-package admission,
independent review, whole-repository regression, defaults and code-main cutover
remain pending. No browser/DOM/native navigation test was newly executed in M19.
Next: migrate the actual Phase32 browser's uint32 carrier and exact pitch input
while preserving this reader's source/budget semantics; do not rebuild BRC.
