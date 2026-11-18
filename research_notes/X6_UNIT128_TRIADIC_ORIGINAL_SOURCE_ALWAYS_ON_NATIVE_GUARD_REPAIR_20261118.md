# X6 Unit128 — guarded repair of the real triadic source's optimized-mode native BRC false-PASS

**Date:** 2026-11-18. TASK_RESEARCH under RS-X6-LEGACY-PLANE-RECONCILIATION (TP2-B4A441B23DA3159232C2), mother objective PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Source is an actual current original signed-X6 downstream consumer; research lane `chatgpt-research-onhour-enterprise-math-20260923` only. **State:** AUTHOR-PATCH-EXECUTED / EXACT-GIT-BLOB-PINNED / UNREVIEWED / NOT_ADMITTED.

## Actual original failure and smallest safe patch

Unit127 proved that the original `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py` (blob `d5f6dfcfd0dedbe46feae3bc1b227185af417c2f`) performed 480 genuine native `signed_brc.shortest_path_multiplicity` calls in normal CPython, **zero** in `-O/-OO`, and falsely reported PASS in optimized modes after a controlled zero-BRC implementation mutation.

This unit edited the **existing live current checker** itself, with a GitHub content-SHA guarded update. Exactly the 13 full-module Python `assert` lines were replaced by semantically equivalent always-on `if not (...) : raise AssertionError('triadic_assert_line_N')` checks, preserving original logical predicates, signed triadic event models, operation order, source module imports, original PASS output, and unrelated definitions. No original frozen P000 input, canonical `signed_brc.py`, historical pre-rebase Git commit, or R063 C3/C4 benchmark object was modified.

- Original active file blob: `d5f6dfcfd0dedbe46feae3bc1b227185af417c2f`.
- Corrected active file Git commit: `8ecfb3f81c6ffe3759a4d1b62703169aeaf79397`; corrected blob: **`eb2036264f5b754988a5841ca1d83fab561aa49b`**.
- Corrected original source has **zero AST Assert nodes**, replacing exact original source lines 55, 56, 65, 69, 77, 87, 88, 90, 91, 129, 146, 158, 159.
- Frozen original signed BRC source remains at blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, scientific input pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

## Real tests of the patched existing source

The complete corrected 6,074-byte source was independently reconstructed locally from the original 5,420-byte source, and its Git blob computed *before* the guarded remote update. After writing it to current main, the connector fetched the exact new source bytes by immutable commit and confirmed identical `eb203...` content.

The accompanying original-file regression instrument uses the corrected **actual upstream source** against the same pinned `signed_brc.py` in an isolated copied checkout. A profiler outside the tested program counts real native calls. In each of CPython normal / `-O` / `-OO`:

| Mode | Original signed BRC multiplicity calls, corrected checker | Clean exit | Deliberately incorrect BRC `return 0` |
|---|---:|---:|---|
| Normal | 480 | 0 / PASS | 19 / REJECT |
| `-O` | 480 | 0 / PASS | 19 / REJECT |
| `-OO` | 480 | 0 / PASS | 19 / REJECT |

Each clean mode also performs 960 actual `shortest_event_count` native calls, and each deliberately corrupted mode reaches one native validation before rejecting. All three clean-mode reported stdout SHA256 remain **`03f98b37a4dcf346cc3a7063206f84253a3b7c1a219f1892f7967cd55201c2a2`**, identical to the unchanged original normal output. All faulty modes have exit 19 from the outer tracer and the expected short-circuit failure. The source change is therefore an executable-level correction of a real current consumer, not merely a new auxiliary theory or suggested test.

Reproducible source and results: [six-mode corrected native regression](../research_checks/X6_UNIT128_CURRENT_TRIADIC_ALWAYS_ON_REGRESSION_20261118.py), [exact JSON execution record](../research_checks/X6_UNIT128_CURRENT_TRIADIC_ALWAYS_ON_REGRESSION_RESULTS_20261118.json), original source available in Git history at the pre-patch blob and Unit127 pinned replay. The regression itself pins the corrected module byte identity plus the frozen BRC byte identity; if a later authorized change edits either, an update to expected evidence will be necessary rather than silently accepting new data.

## Typed conclusion and remaining research

**`PRESERVE_PATH_BRC / CURRENT_ACTIVE_CONSUMER_PATCHED / NORMAL_OPTIMIZED_NATIVE_CHECKS_CLOSED`** for the original triadic atomic scatter checker. Unit126's valid 480 anchored midpoint call sites remain unchanged; the broader translated `midpoint_options` typing counterexample remains a separate consumer-interface restriction, not fixed by assert guards.

The task's 28-LP crosswalk and purported historical LP011 wrong native signed argmax/LP019 subtraction of nonnegative natural N-BRC path counts remain **`UNRESOLVED_PROVENANCE`** until their exact original path and operation are source-attested. Original R063 six-file 512-row author execution is already preserved; independent review/admission via existing Driver/Issue #2416 remains pending. The patch does not imply independent admission, nor does saving this report imply Native semantic PROGRESS.

**Next exact action:** append this corrected source:line consumer to the active dependency ledger; examine other existing current consumers at their exact source lines rather than repeat completed experiments; reconcile original run's pending Unit126–127 PROGRESS by its one request ID before writing any overlapping Native PROGRESS; preserve all prior author evidence and original signed/relative observer distinctions.
