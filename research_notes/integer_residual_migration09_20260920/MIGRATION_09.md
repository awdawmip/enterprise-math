# Migration 09 — actual multiplicative browser caller

Status: LOCAL_VALIDATED_CANDIDATE; not a default switch or main-code admission.
Baseline: 822bd4fb79c28a5ffb02ba54f311e75d163d7646.
Code: 52d886d1be6e20660ac52d54307a360b5c398c21.
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

The real multiplicative.py render path now adds the exact adapter to the original
multiplicative_lab.html. The original template was finally materialized and
verified as blob 6619c5da7ad03f38766bfc383d60b5505cb863e0; no reconstructed stand-in
is used. Its previous missing-template test exclusion is removed. The M08
certified_hex_browser.py, M03 Python certifier and existing BRC arithmetic are
reused unchanged; this is caller integration, not a new scalar/kernel family.

Exact mode accepts original textual scales (0.50 retains 50/100; 2/2 retains 2/2),
integer precision budgets, and the older module's axial lexicographic tie rule.
The browser range is explicitly 1/4..4; source and camera/display scales remain
separate. Whitespace/newline, Number input and reverse-inferred denominators are
rejected. Checked integer transport to Number is not floating-point rounding.

Cell decisions, angular/area bins and CV-squared residual readouts use integer
operations and the existing certified engines. Approximate CV, iid-reference and
geometric-error fields are omitted in exact mode, not replaced with false zeros.
Pixels remain approximate and cannot feed back into membership. Unresolved cells
retain their identities and intervals; complete occupancy/collision/excess/load
statistics stay null and guessed hex exports are refused. All 512 identities
were drawn in the deliberately unresolved DOM scenario.

The actual UI awaits calculation/restore, clears old geometry AND heatmaps,
rejects stale reports/certificates, suppresses superseded generations, recovers
from digest failure, and detaches exported objects from live provenance. Session
V2 and saved HTML retain exact options. V1 restores legacy explicitly. The current
CLI still seeds the default legacy page; --cell-scale affects its machine outputs
until the exact-start contract is separately integrated. Browser selection of
exact mode is available now; the global default is unchanged.

Validation: 40 caller tests (17 new + all 23 historical), zero failures/errors/
skips; 78 retained M04 numerical/HTML tests passed. The real old-template Chromium
DOM harness passed 44 checks and the earlier M04 DOM harness passed 69, with zero
page errors. Two actual JSON downloads and saved-HTML re-execution were checked.
Twelve 4096-identity cases plus one 65536 valuation/scale-one case matched Python:
all summary fields, ordered identity fields and canonical certificate digests.
All these populations were certified; the 65536 case occupies 44731 cells. These
are finite checks, not a universal proof, performance guarantee or independent review.

Browser limitation: the DOM executes actual generated/saved HTML using set_content
on about:blank and an explicit hashlib SHA256 test adapter. Native Node crypto is
covered separately. Known managed file/http browser navigation restrictions were
not retried or bypassed. Native browser WebCrypto, actual file reopen, Safari/iOS,
full wheel/repository regression and independent admission remain pending.

A clean pinned-source patch replay passed the same 40 tests and 44 DOM checks,
with byte-identical source and JSON validation output. Replays are not new tests.
Source patch SHA256: 87d6f9f289158854bdcfe0bfc92fb63ac3a92ea908cb7a45b02b9c953235cdd7.

Reproduce: python tools/run_migration09.py; python tools/test_migration09_dom.py;
python tools/benchmark_migration09.py. Python, mpmath and Node are needed for the
combined slice tests; the DOM harness needs Playwright and installed Chromium.
No dependency is installed automatically and no hosted workflow is dispatched.

The delivery is a source slice, not a repository mirror. NEVER overlay its
isolated src/enterprise_math/__init__.py on production. Apply migration09.patch
only to the pinned M08 source. Demo: demo/multiplicative.html; choose integer plus
residual in the real engine control. Read RECOVERY_M09.md for remaining work.
