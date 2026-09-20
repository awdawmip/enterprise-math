# Migration 14 — installed console reader and exact dependency contract

Status: locally validated candidate; production package-data/native-browser acceptance remains pending.
Baseline remote: `b380f5dc0136480815ae89e1976e4fac20faf102` (M13).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual change

M13 already routed the existing `nollm-viz validate/convert/profile/render/site`
commands through `core.read_data`, so no parallel viewer was added. M14 verifies that
installed console path and repairs its packaging boundary.

The toolkit stays standalone for ordinary visual-data V2 work. `pyproject.toml`
now declares an `exact` extra requiring `enterprise-math==0.1.0`; it is not a
base dependency. Machine-report replay still refuses to approximate when BRC is
unavailable. `core.read_data` converts that lazy-runtime failure into a normal
ValueError, so installed `nollm-viz` exits with code 2 and a clear message instead
of an uncaught traceback. No exact arithmetic, cell algorithm, tie rule, report
schema or observer quotient changes in this slice.

## Installed console gate

A wheel was built with the real M13 package entrypoints and the new dependency
metadata, installed into a fresh venv, and exercised in two states.

Without Enterprise Math, ordinary `demo -> validate` works. Machine-report input
fails explicitly with `requires Enterprise Math BRC ... no approximate fallback`.

For source-slice replay only, the exact runtime was supplied by a test-only
`enterprise-math==0.1.0` fixture containing byte-identical remote
`core.py/division.py/exact_arithmetic.py`. Its minimal `__init__.py` is NOT the
production Enterprise Math package and is never published as production code.
With that runtime present, installed `nollm-viz` successfully executed:

- `validate` directly on the M12 machine report;
- `convert` to JSON and CSV;
- `profile --axis s`;
- `render` to embedded visual-data HTML;
- `site` with a manifest and embedded page;
- installed `preview_server` HTTP readback.

All 256 identities are retained. Render and site embed exactly the same adapted
visual-data object as convert. Their fingerprint equals validate. The adapted
data contains certified A2 cell centers and no `ideal_*` pixel fields. Metadata
retains `DETERMINISTIC_REPLAY_NOT_AUTHENTICITY`; the adapter does not turn replay
into provenance authentication or native X6 state.

## Validation and explicit boundary

148 retained M12 arithmetic/machine tests pass with zero failures/errors/skips.
The installed-console harness passes 17 checks. It checks exact source blobs,
wheel metadata, standalone legacy install, missing-dependency fail-closed
behavior, JSON/CSV/profile/render/site consistency and local HTTP readback.

The local M12/M13 source slice does not contain the unchanged production
`workbench.html`; render/site therefore use an explicit minimal
`__PAYLOAD__/__FINGERPRINT__` test fixture for dispatch validation. This is NOT
production template acceptance and not a DOM/browser test. Likewise the test
runtime is not the full Enterprise Math package. Full root-package installation,
production workbench package-data, native browser navigation/Safari/iOS,
whole-repository regression, independent review, default activation and main
code cutover remain pending.

BRC reuse resolution: `REUSE_EXECUTED_UNCHANGED`. The new work is packaging and
caller/error-surface integration; no BRC reimplementation was introduced.

## Next

Materialize and execute the actual production `workbench.html` plus the complete
Enterprise Math root package in an installed environment, then run browser smoke
on the rendered machine-report page. Preserve M13 deterministic replay, M12
machine config/precision, local axial lexicographic tie semantics and no-fallback
behavior. Do not rebuild M01–M13 arithmetic.
