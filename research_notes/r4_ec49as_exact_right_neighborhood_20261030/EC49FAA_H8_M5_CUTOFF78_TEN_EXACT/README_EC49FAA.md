# EC49FAA — Strict-78 signed-native BRC census and ten new exact exclusions

**Date:** 2026-11-04. **Prior frontier:** EC49EXZ at immutable commit `14160f9994887e6f433b21b6bd999726fb68768b`; continued on existing Draft PR #1730. **Evidence status:** AUTHOR_EXACT_FINITE_SIEVE / TEN_INTEGER_DP_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Frozen model and scientific objective

Keep the seven-operation native signed-X6 paths, horizons h=2..8, exactly five complete six-axis positive-step BRC cache keys, at most six distinct nine-history observer signatures, exact rank-nine observation at every horizon, and cost `E` equal to the number of distinct nonempty **ordered signed primitive** path prefixes. Full BRC key, sign, order and transfer signature are retained. Frozen science: Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, account source `773d538180bfb49e24cffeb35c3ee75eb0628e2e`. Current behavioral norms are read separately. P000 and ACTIVE Heartbeat World remain unchanged.

EC49EXZ gives two explicit verified 78-edge feasible constructions. Existing mother bounds are `63 <= E* <= 78`; we now test the **strict** possibility `E<78`.

## FAA-1 — Exact threshold re-screening

The immutable EC49EXY double-collision TSV (Git Blob `61ffbcdba1679479fade3cfd052c2d9d6bbf30ce`) contains exactly **12,356** arrangements and a proved `B_EXY` per arrangement, with `E >= B_EXY`. Exhaustive integer re-count of the TSV:

| B_EXY interval | Arrangements | Effect at threshold 78 |
| --- | ---: | --- |
| 62–77 | 8,074 | Still eligible for precise testing |
| 78 | 2,260 | E<78 excluded |
| 79 | 2,022 | E<78 excluded |
| **Total** | **12,356** | **4,282 now excluded** |

This is a valid reuse of an earlier proved bound for a new threshold, not a claim that any of those 4,282 must have cost >=80.

Of the **first 200** previous EC49EXZ source-ranked cases, 34 have B_EXY>=78, 166 have B_EXY<78. The prior exact integer solver excluded 198 for E<80 and constructed exactly two E=78 cases (source ranks 14,15; original row indices 0,1492). Therefore 164 of those 166 are already excluded for E<78; do not count them again.

## FAA-2 — Ten new exact cutoff certificates

Our new C++17 signed-native prefix trie integer OR-mask DP tested **ten previously untested** cases at zero-based source ranks **202, 203, 208–213, 216, 217**. Each has B_EXY<78 and is outside the previous first-200 sample. All ten returned:

`BOUND_PASS minimum_total_at_least=78`

Their eligible word counts are 201–206; signed-prefix tries contain 917–1,205 nodes; observer color count is 20 or 22. See `EC49FAA_10_CASES.json` for every original source row, SHA256 of the exact solver input, and individual receipt. There were **zero** timeouts and **zero** solver errors on these ten cases.

Proof of solver cutoff soundness: Each subtree state stores minimum extra non-prepaid edges realizing an observation bit-mask. Combining child state masks uses OR; every nonempty child contributes one edge exactly when the edge is not prepaid in the 28-edge h2 core. All costs are nonnegative, so discarding costs >=50 extra (cutoff E=78) cannot remove an improving E<78 solution. A missing full mask at cutoff proves E>=78 for the fixed arrangement. It does *not* rule out an E=78 realization.

The locally executed independent input builder exactly reconstructed both published EXZ witness trie-input SHA256s (A: `67149516a1352665477014d3b6a3ef50628ebbbb98306bd8fa94604ceb8c8424`; B: `458f83b669624d6e2a437bd7347b94d8c8602ed0bc35a5fdb2cecab0044d5c3d`), each with 617 nodes and 158 words, before ten-case DP. The original frozen EC49EXJ C++ solver source was compiled locally; ten certificates were executed and recorded. `REPRO_EC49FAA.py` reuses the original sibling generator and solver, rebuilds each exact input, checks its SHA256 and returns cutoff receipts. The published wrapper has been syntax-checked, but was not independently re-run after GitHub publication.

## Updated strict-improvement search space

Taking disjoint exclusions:
`12,356 - 4,282 - 164 - 10 = 7,900` **not-yet-excluded double-collision arrangements** for E<78 (conditional on the prior EXY classification and EXZ exact first-200 reports). There are no remaining triple-collision candidates under the previous complete exact exclusion chain. **The global proven interval stays `63 <= E* <= 78`.**

## Next EC49FAB

Rank the 7,900 remaining rows by exact native candidate word count; use exact input-hash deduplication and seven-horizon prefix bounds. Either recover an E<=77 legal six-axis BRC witness independently (full keys, 9-history rank, signatures, prefix union), or add exact no-improvement certificates with scope and timeouts preserved. Do not infer global 78 optimality from local exclusions. Native owner/CLAIM, Result and independent Driver admission remain separate obligations.
