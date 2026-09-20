# Migration 10 — exact CLI-to-browser startup

Status: locally tested candidate; no default or main-code cutover.
Baseline: `29d08589033166fa87fe2989cbcb5a61e7118850` (M09).
Code commit: `9c23567067524f1280826d1abd90b48c96385508`.
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual change

The existing multiplicative CLI and render function now pass the original exact
scale text and integer precision budgets into the generated browser startup.
`--cell-scale 0.50` starts certified membership directly and preserves 50/100;
`2/2` remains 2/2. The old float `--scale` remains a separate display parameter.
One typed startup packet is shared by the generated HTML and machine report.
Generating a packet is not evidence that a browser executed it.

Browser membership remains restricted to [1/4,4], tested by integer inequalities.
A broader positive source uses explicit `--machine-only --report/--hex-data`,
without generating a misleading legacy HTML page. Out-of-range HTML requests
fail rather than clamp, round, or silently change engines. HTML-only exact
startup is supported without first duplicating population work in Python.
No-option calls preserve the old seed shape and V1 report semantics.

The existing browser consumer rejects missing, unknown, conflicting and
engine-downgraded startup data. Saved-page root configuration must agree with
its saved session, independent of property ordering. Initial pending/failed
states expose no complete cell totals or readable stale report; older startup
completion cannot overwrite a newer configuration. V1 sessions still restore
legacy explicitly. Original scale sources and full cell summaries survive
saved-HTML re-execution and actual JSON downloads.

## Verified scope

60 code tests passed: 20 new startup tests and 40 retained tests, zero failures,
errors or skips. Two retained expectations were deliberately advanced for the
new CLI contract; a source-AST check preserves every preexisting Python
mathematical function other than the intentionally changed main/render callers.
The original template and Python/BRC/BigInt cell algorithms remain unchanged.
Node comparisons use native Web Crypto and actual rendered engine scripts.

45 real Chromium DOM checks passed with zero uncaught page errors: exact first
load with the old quantizer disabled, matching CLI summary, full quarter-turn
tie certificates, lexical controls, saved-page re-execution, two JSON downloads,
nine malformed startup cases, digest failure/recovery, deferred-start race,
V1 restore, and deliberately unresolved low-budget startup. All 512 identities
remain drawn in the low-budget case; unknown cells and complete totals are not
guessed. Screenshot was visually inspected.

The retained M04 suite passed 78 numerical/HTML tests and its two exact-policy
targets; its DOM harness passed 69 checks. These are regressions, not new tests.
The clean M09-input patch replay passed the same 60 code and 45 DOM checks;
all eight source/fixture files and deterministic test/DOM JSON reports matched.

Browser tests execute real generated HTML via set_content on about:blank with
an explicitly identified test-only hashlib SHA256 adapter. Production HTML has
no such adapter. Known managed file/http navigation restrictions were neither
retried nor bypassed. This does NOT validate native browser Web Crypto, actual
saved-file navigation, Safari/iOS, full wheel/whole-repository integration, or
independent mathematical admission. Certified --preview remains gated.

Output preflight rejects conflicting output paths (including resolved symlink
aliases), out-of-domain seeds, and unresolved requested hex exports before
writes. This is semantic preflight, NOT a multi-file filesystem transaction:
later I/O failure rollback and hard-link alias handling are not claimed.

## Reproduce

```bash
python tools/run_migration10.py
python tools/test_migration10_dom.py --chromium /usr/bin/chromium
PYTHONPATH=src:tools/nollm_visual_toolkit python -m nollm_visual_toolkit.multiplicative --count 4096 --cell-scale 0.50 --out exact.html --report exact.json
PYTHONPATH=src:tools/nollm_visual_toolkit python -m nollm_visual_toolkit.multiplicative --count 64 --cell-scale 5 --machine-only --report exact-five.json
```

Requires available Python, mpmath and Node; DOM additionally requires Playwright
and installed Chromium. No dependency installation, hosted workflow or background
executor is introduced. This source-slice bundle is not a full repository mirror.
Its inherited isolated src/enterprise_math/__init__.py must NEVER overwrite
production. Apply migration10.patch only to the pinned M09 source.

Patch SHA256: `4df5fc272b42f89282d1c9a08d4d9cef28c1dc2c48636f17a17b367470d9ad8f`.

## Remaining work

Default and main integration require separate native-browser/full-package
acceptance. The next independent numerical migration is to reconcile Python
exact-mode statistic/product readouts with the browser's no-approximate-metric
contract, preserving custom histogram dimensions, V1 legacy payloads and typed
residual readout scales. Do not rebuild arithmetic or repeat M01-M09. Geometry
remains a declared A2 observer, not native X6/P000 or general transcendental closure.
