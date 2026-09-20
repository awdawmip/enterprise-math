# Migration 04 — certified browser cells

Status: tested opt-in candidate; browser navigation and production admission pending.
Baseline: `82ffedbf54b2c35ca105b848a01696804a69df26`.
Code: `167ee06ae64b606dfcd99506a4d4c501257a2bb8`.
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Implemented

The actual multiplication webpage calls NollmCertifiedHex.population when the
integer-residual engine is selected. The Python builder embeds the script.
Signed floor is implemented over the existing natural-domain BRC browser division
port, not JavaScript truncation. Dyadic intervals, root-polynomial residuals,
shared quarter-turn radicals, tie priorities and source records match unchanged
M03 Python. This is a declared 65,536-phase A2 observer, not native X6 or a new
general arithmetic family. BRC Python runs unchanged in the reference; it is not
claimed to execute in the browser.

Scale is original text: `0.50` retains `50/100`; `2/2` retains `2/2`.
A Number cannot enter the textual scale API. Invalid text/range fails before
state replacement. This UI range is 1/2 through 3; it does not restrict the
general positive source ratios of the standalone certified-cell module.

The precise cell and source stay separate from approximate rendering. An
unresolved identity has null cell, is rendered only from its interval midpoint,
and is explicitly marked. Any unresolved population member leaves all four
complete occupancy/collision/excess/load totals null. There is no float fallback.

## Caller and state contract

`NumberFieldLab.configure({...})`, restore and preset now return Promises.
Await the current configuration before consuming reports. During computation
old cells/pixels are cleared and reports/certificates are unavailable. An older
concurrent generation cannot publish over a newer one. Digest/other failure
clears totals and rejects report/certificate requests; retry can recover.

Example in an already loaded lab page:

```javascript
await NumberFieldLab.configure({
  cellEngine: 'certified', cellScale: '1/2',
  cellBits: 64, cellMaxBits: 192,
  overrides: {'3': 16384}, selected: 3
});
NumberFieldLab.certificate(3); // exact cell ["-1", "1"]
```

Session V2 saves textual scales and precision budgets. V1 restores explicitly
as legacy float, never guessing an intended exact rational. A V1 object that
spoofs exact fields is rejected. The old engine remains the default for this
slice. Camera math, pixel conversion and the old atan2 histogram remain marked
approximate; pixel overlap does not merge identities.

## Validation and limits

78 numerical/HTML tests passed (58 retained + 2 recovered HTML tests + 18 new);
zero failures/errors/skips. 69 Chromium DOM checks passed, including 27 original
UI old-field comparisons, ties, unresolved display, V1/V2, pending reads, race
replacement and digest failure. Twelve full Python/Node population records
match: nine at 4,096 and three at 65,536; all certified. The latter occupancy
counts at scale one are golden 47,491, rank 14,634 and zero 257. Finite results
are not exhaustive proof or independent review. Timings are telemetry only.

IMPORTANT: this host blocked file: and localhost browser navigation with
ERR_BLOCKED_BY_ADMINISTRATOR. No managed restriction was bypassed. DOM tests
execute the original generated HTML via set_content on about:blank; a clearly
marked Python-hashlib SHA256 test adapter supplies the absent secure-context
Web Crypto. Node tests use native Web Crypto. This does NOT pass real file
loading, native browser crypto, saved-file navigation or Safari/iOS gates.

The original full toolkit/Enterprise Math initializers and whole repository were
not executed. The delivery is a source slice with its inherited ISOLATED EM
initializer. NEVER overlay that initializer onto production. Apply only the
pinned `migration04.patch`. Clean replay passed the same 78 + 69 checks and
matched all ten code/fixture file bytes. Replays are not additional new tests.

## Reproduce

```bash
python tools/run_migration04.py
python tools/test_migration04_dom.py --chromium /usr/bin/chromium
python tools/benchmark_migration04.py
```

The numerical runner requires Python, mpmath and Node with native Web Crypto
(tested Node 22.16.0). DOM tests additionally require Playwright and an installed
Chromium. Missing dependencies fail explicitly. The runner installs nothing,
dispatches no workflow, and implies no persistent executor. Full raw reports,
logs and a DOM screenshot are included in the bundle under evidence/migration04.

## Next unfinished unit

Run the real generated and saved files in an authorized navigable browser with
its native Web Crypto; verify the full package import and existing callers of
the new async API, including the gallery page. Then review the explicit default
switch. Do not redo M01-M04 arithmetic or claim the new engine is already main.
Further production geometry, general algebraic closure, complex amplitudes,
historical experiment migration and independent admission remain separate.
