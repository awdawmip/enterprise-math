# U27F-10 frozen fixture boundary and observer arithmetic (2026-11-19)

Scope: bounded source-input examination under Task `RS-CELL-U27F-10-INDEPENDENT-AUDIT-20261012`. The three named fixtures were read from GitHub `68452be67a2bfdd02b6010c116fdc2f022848611`; companion JSON records their actual Git blobs and 14 machine-evaluated checks. No original U27 code or proof archive was available in this execution.

## Valid observations

The first missing graph edge is `(1,2)` and the subsequent post-carry lost edge is `(2,3)`. Removing only `(1,2)` from the four-edge full square reproduces the three-edge damaged graph. The second loss is different and belongs to that damaged graph. An analysis that collapses these releases into one event would change the frozen episode.

At the frozen interruption, body B has moved from `[1,0,0,0,0,0]` to `[1,0,1,0,0,0]`; token 2 is held at B, token 3 is free at `[1,1,0,0,0,0]`. Bound/held/free token keys partition the four tokens exactly. The pending reference coordinates match the current four body cells. Incidence is `PENDING` and the fixture explicitly forbids automatic cached commit. These checks validate internal consistency of this source extract; they do not establish a legal stable successor.

The separate order-observer extract reports early-loss mean work `1567/784`, late-loss mean work `2`, and same-survival `783/784`. The exact arithmetic gives
`2 - 1567/784 = 1/784 = 1 - 783/784`.
This identity holds for the three published values. It does not, from marginals alone, identify the per-history mechanism responsible for the difference or establish equality of the stopping-time events. That requires the original transition system and joint history data.

## Scope and recovery

Frozen original archive: `em_u27_followup_tasks.zip`, SHA-256 `a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7`. It was not available through current Library/Source retrieval; the three compact fixtures are not a substitute for original `NOTE.md`, `work_exposure.py`, complete 56-state evidence, or original code. Reviewer independence remains unverified; this is a **bounded input/evidence check**, not an independent mathematical review or a published Result.

Next discriminating unit: recover exact archive and verify its hash, identify the 56-state initial distribution and stopping event implemented in `check_u27.py`, compare the original per-history early/late observer joint outputs against the fixture identity. If original materials remain unavailable, preserve this precise input gap and continue other tasks without claiming review completion.
