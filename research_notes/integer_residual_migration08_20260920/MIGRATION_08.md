# Migration 08 — browser certified cells with multiplicative lexicographic ties

Status: validated browser arithmetic extension; old multiplicative workbench not yet wired.
Baseline: `b0d724fd4cc2a80c750feb07361f3c950d45c825`.
Code: `f33be2c0c51d696c7cd81b73d5269c5b0683dce4`.

M08 extends the existing `certified_hex_browser.py`; it does not introduce a
second browser numeric family. The new `adaptLexicographicCell()` and
`populationLexicographic()` preserve the full M03/M04 base certificate while
selecting the older `multiplicative.py` module's declared nearest-center then
axial `(q,r)` lexicographic tie.

For rational sources, equal-nearest candidates are compared with integer
quadratic distance numerators. For shared-radical sources, the adapter reuses the
existing exact linear-root sign comparison. No `Math.*`, float epsilon, or
midpoint decision is used. The incremental `onCell` callback receives the adapted
wrapper certificate, so a future UI cannot accidentally display the base tie
while its final population uses the local tie.

Cross-language validation compares complete wrapper certificates, not only final
cells. Seven new tests pass. A finite audit exactly reproduces the M06 result:
1,080 certified ties and 504 cases where the base tie rule and the older module's
lexicographic tie choose different equal-nearest cells. Existing M04 regression
also passes: 78 numerical/HTML tests and 69 Chromium DOM checks, zero failures,
errors or page errors.

The actual old `multiplicative_lab.html` still uses floating `sqrt/cos/sin` and
its `round()` function to decide cell membership. M08 is only the reusable
browser certifier needed to migrate that caller next. Known native file/localhost
browser navigation restrictions from M04 were not retried or bypassed.

Next: wire the old workbench to exact textual scale + `populationLexicographic`,
with asynchronous generation, explicit unresolved cells, session V2 and no float
fallback. Keep default switching separate until caller validation passes.
