# Migration 13 — machine report replay and existing data-reader integration

Status: locally tested candidate; no main/default/full-package admission.
Baseline: awdawmip/enterprise-math@ab57af004d75d483c819e371501059cda1dbc39e.
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual consumer

Existing core.read_data now recognizes NOLLM_MULTIPLICATIVE_MACHINE_REPORT_V1.
It routes the original JSON text through multiplicative_report, replays the
existing M12 float-free field and readout functions, then supplies the existing
visual-data V2 carrier. Original JSON/CSV visual-data inputs retain their old
path. Only core.read_data changes an existing production function; all M12
multiplicative/BRC/cell algorithms are unchanged. This extends a report consumer,
not a new arithmetic family or standalone numerical prototype.

The reader preserves lexical scale, unreduced denominator, phase inputs,
initial/max precision, custom histogram dimensions and readout scale. It compares
all persisted output fields against the replay, including exact statistics,
all-pairs audit and cell summary. JSON-level comparison distinguishes true/1 and
false/0. Duplicate keys, float/nonfinite tokens, missing budgets and mismatching
source/output fields are rejected. Reader byte, nesting and histogram-allocation
limits are resource limits, not claims about the arithmetic domain.

A low-budget unresolved report replays at that same budget. It is not upgraded
to CERTIFIED_ALL. Report validation/copy remains available; full visual-data
conversion rejects unresolved or out-of-carrier coordinates without guesses.
No ideal pixel fields are manufactured. The imported data retains source
statistics and a canonical report SHA256. This is deterministic consistency,
NOT source authentication, an author signature or independent proof.

## Explicit display boundary and command

machine_report_startup(report, display_scale=...) requires a separate explicit
display parameter and invokes the existing browser_startup function. Original
exact scale spelling and precision survive; input reports remain unmodified.
Browser scale domain 1/4..4 is unchanged. Because that browser currently uses
8 rings, 32 sectors and readout scale 1000000, other report observations are
rejected at this display boundary rather than silently reinterpreted. Such
reports remain valid for machine replay and data import.

The command invokes the real report reader, not a rendering stub:

```bash
PYTHONPATH=src:tools/nollm_visual_toolkit python -m nollm_visual_toolkit.multiplicative_report exact.json --verified-report checked.json --hex-data cells.csv
PYTHONPATH=src:tools/nollm_visual_toolkit python -m nollm_visual_toolkit.multiplicative_report exact.json --startup startup.json --display-scale 2
```

Without output flags the command validates and prints the replay status. Startup
JSON is an input to the existing browser, NOT proof that a browser executed it.
Semantic preflight precedes writes; input/output aliases and hard links are
rejected. Late filesystem failure rollback is not claimed.

```python
from nollm_visual_toolkit import core
cells = core.read_data('exact.json')
nearby = core.neighborhood(cells, '3')
```

## Verified scope

173 tests passed: 25 new report tests and all 148 retained tests, zero failures,
errors or skips. No retained expectation was weakened or changed. The new tests
exercise actual core.read_data, JSON/CSV roundtrips, detached exports, exact
replay without display functions, real CLI/subprocess invocation, malformed
reports, lexical identity, low-budget replay, source-only null readouts, 12
custom observation cases, and explicit projection boundaries. An initial test
found source-only readout=null needed explicit handling; it was fixed and the
failure log retained.

Twelve real CLI producer -> reader -> data-consumer cases at 4096 identities
(four phase schemes x three scales) pass. Identity records, entire persisted
statistic objects, cell summaries, JSON/CSV roundtrips and the existing collision
consumer agree. All twelve happen to be fully certified; dedicated 512-identity
low-budget tests preserve unresolved cases. These are finite checks, not a
universal proof, performance claim or new 65536-population test. One combined
benchmark hit a tool timeout after eleven completed cases; only the unfinished
case was rerun. Per-case report persistence was added to the benchmark runner.

A clean M12 bundle plus migration13.patch passed the same 173 tests; six
source/fixture files and deterministic test reports match. Existing exact-policy
checks pass their two declared arithmetic files, not the mixed reader/display
module. Retained Node checks are previous readout/kernel tests, not a new DOM,
HTML navigation or native WebCrypto run.

Patch SHA256: 41a20e2d1ca26d656401ea2d8073032e57b190a6cc697c1e16b9b19322732535.
Reproduce: python tools/run_migration13.py; python tools/benchmark_migration13.py.

## Remaining scope

Complete package installation/entrypoints and actual browser consumption of
imported startup packets still require integration validation. No HTML template,
browser script, production default, native X6/P000 geometry or main code changed.
Custom browser histogram/readout settings remain unsupported; do not synthesize
them by discarding source observation parameters. The next unit is complete
package/data-viewer integration on the candidate with these imported sources.

This bundle is a focused source slice over M12, not a repository mirror or full
HTML application. NEVER overwrite production with the inherited isolated
src/enterprise_math/__init__.py. Apply migration13.patch only to the pinned M12
source. Independent review, native file/http/Safari/iOS acceptance, whole-repo
regression, other production consumers and historical research remain separate.
