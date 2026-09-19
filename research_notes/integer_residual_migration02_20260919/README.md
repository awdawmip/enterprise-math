# Integer + residual migration 02 — actual browser consumer

Candidate continuation of `d05ed3be25c025314a863b26daf134aaeb8c3b7e`.
Researcher: EM-DIRECT-4A5102; activity: RA-1094DE57986E6E3FDCEA65DA.
No new Task-ID, CLAIM, theorem promotion or main integration.

## Implemented

The existing page now bins modular phases using exact integer quotient/remainder and displays CV **squared** as integer/scale plus rational residual. Its primary exported `angular_cv_squared_exact` record retains ordered counts, unreduced numerator and denominator and the complete scaled BRC trace. Every exact integer is a decimal string across JSON and HTML save/reload.

`angular_dispersion_browser.py` is a narrow BigInt port of the already-executed Python `angular_dispersion.py` + `exact_arithmetic.py` interface. It is embedded using the toolkit's existing Python-template packaging convention. It does not secretly call a server or invoke Python in the browser. Cross-language validation compares complete records, not rounded decimal displays.

The old floating `angular_cv` remains a specifically labeled compatibility/display field, not the primary exact result. Polar phase membership is tagged `EXACT_MODULAR_PHASE_BINS`. Legacy A2 membership still uses atan2 and is tagged `APPROXIMATE_ATAN2_BINS`: exact statistics of approximate input bins do not certify geometric membership. No X6 or native path provenance is invented.

## Verified

The authentic toolkit initializer, web module and original HTML template were pinned and run first: 36 tests passed (including the two HTML tests omitted in migration01). The final suite has 47 tests with zero skips, including 11 new Node/Python/integration-contract tests. A standalone isolated build without an Enterprise Math installation also passes.

4,080 complete BRC record comparisons, 66,180 integer phase-bin cases, 676 comparison pairs and 270 rational threshold cases passed. Chromium executed 72 actual-page scenarios up to 65,536 records. Complete old reports match a separately executed frozen original template; new exact records match Python BRC. Actual report-button download, saved HTML reopening, gallery preset execution and raw-data preservation passed, with no page errors or network requests. See validation.json and browser_validation.json (execution summary). The frozen original template is retained under fixtures/; the runner recomputes original and new pages without an external baseline corpus.

## Reproduce

From a complete source checkout with the candidate applied:

```sh
python tools/run_migration02.py
python tools/run_migration02.py --browser --chromium /path/to/chromium
```

Node is required. The browser option requires already-installed Playwright and Chromium; it does not install anything or dispatch hosted CI. Missing Node or skipped tests are not accepted as success. The source-slice delivery bundle executes a real toolkit initializer but a clearly marked isolated Enterprise Math initializer; never copy that initializer into production.

## Remaining and recovery

Package-level toolkit and real-page coverage are now filled. Full Enterprise Math initialization, whole-repository regressions, independent review and main integration remain unverified. The Python exact gate passes for the unchanged angular module; it is not a JavaScript AST gate. Browser file-URL navigation and Safari/iOS are not claimed.

Continue from these native-path changes, not from another new scalar prototype. The inspected multiplication Python/UI uses CV for observation/reporting; no ranking/threshold caller was found in this limited scope. After complete-checkout integration, the next numerical boundary is `rounded_hex`: preserve the explicit tie rule and unresolved-boundary state rather than introducing tolerance equality. Keep the two separate obligations: exact statistic given counts, and certified source-to-bin/cell membership.
