# X6 Unit127 — original signed-triad full-module native BRC execution and optimization false-PASS

**Date:** 2026-11-18. **Parent:** PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. **Task:** RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2. **Research lane:** chatgpt-research-onhour-enterprise-math-20260923 (not the CONTROL_PLANE_MAINTENANCE lane).

**State:** AUTHOR-SOURCE-EXECUTED / EXACT-ORIGINAL-MODULE / CONTROLLED-FAULT-REPLAY / UNREVIEWED / NOT_ADMITTED. This is a new native-integration result following Unit126, not a freeze, independent review, or repetition of the R063 original C3/C4 512-case benchmark.

## 1. Precise frozen and current source boundary

The unchanged current triadic module `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py` was read through the authorized GitHub connector at blob **d5f6dfcfd0dedbe46feae3bc1b227185af417c2f**, exactly reproduced byte-for-byte in an isolated local directory and verified with the Git blob algorithm (5420 bytes). The frozen signed native kernel `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, obtained at scientific-input commit `59538f585d037d09ef687b28715c4bc1a3f9fe03`, was also exactly reproduced and verified at blob **300a96e3dc24bf6fff73743037a0347a8bc83176** (2852 bytes). No original-source file was modified in the working checkout or GitHub.

This is a *current actual downstream implementation against the task's immutable BRC input*, not a claim that the September 6 module existed at the earlier September 5 scientific pin.

The actual original module's **13 source-level Python `assert` statements** include line 55 `brc.shortest_event_count(sub(b,a))==2`, line 56 `brc.shortest_path_multiplicity(sub(b,a))==2`, and source lines 63–78 which enumerate 20 choices of three axes, 8 sign sheets and 3 start-to-transported-target pairs per case. The former Unit126 helper typing check was source-faithful but did **not** execute this original complete module. This execution closes that explicit integration gap.

## 2. Full-module experiment

For each of CPython normal / `-O` / `-OO`, the **unchanged original program** exits 0 and prints an identical 11-line `PASS_X6_TRIADIC_ATOMIC_SCATTER_V1` report:

- 160 signed triad cases; 1,280 joint branch combinations; the reported common branch is `III`;
- six ordered phases, two unordered sign-sheet states, repair fiber C3;
- 2,493 checked degree vectors and 20 ordered / 10 unordered six-force decompositions;
- eight hidden lifts of a fixed effective pair.

A Python function-call profiler, installed *outside* the unchanged module and filtering calls by the original `signed_brc.py` filename, observed:

| Program and mode | `shortest_event_count` calls | `shortest_path_multiplicity` calls | Exit |
|---|---:|---:|---:|
| Original normal | 960 (480 direct, 480 nested) | 480 | 0 |
| Original `-O` | **0** | **0** | 0 |
| Original `-OO` | **0** | **0** | 0 |
| Opt-in strict normal | 960 | 480 | 0 |
| Opt-in strict `-O` | 960 | 480 | 0 |
| Opt-in strict `-OO` | 960 | 480 | 0 |

The opt-in strict test is derived from the *same exact AST* by changing **only** the 13 `Assert` nodes to ordinary `if not test: raise AssertionError` checks. It uses the exact same untouched native BRC implementation. All six clean-mode printed outputs have SHA256 **03f98b37a4dcf346cc3a7063206f84253a3b7c1a219f1892f7967cd55201c2a2**.

## 3. Controlled mutation and observed false-PASS

Only in temporary copies, replace the native implementation of `shortest_path_multiplicity` by `return 0`. The untouched original normal-mode test catches this corruption immediately (`AssertionError`, exit 19 from the external runner). The untouched original `-O` **and** `-OO` tests still print the identical full PASS report and exit 0, because zero BRC calls occur in the optimized program. Under the strict AST guard, **all three** modes reject this corruption (external runner exit 19, `guard_2`).

This is a concrete false-PASS for the original triadic full-module checker in optimized Python modes. It does **not** say that the clean original triadic mathematics is incorrect: the normal clean run passes with actual BRC calls, and the 480 original Unit126 source callers are valid anchored signed-unit-neighbor pairs. It does not generalize the `midpoint_options` helper to arbitrary translated Cells.

## 4. Corrective scope and downstream audit disposition

For the current triadic source, the smallest repair is to make the original 13 mathematical validators active under optimization, while leaving the original scientific input, event model and printed acceptance criteria unchanged. The opt-in strict verifier demonstrates this behavior and mutation sensitivity, but does not patch the original upstream file without a separate guarded implementation decision. Classify this original consumer as `PRESERVE_PATH_BRC / NATIVE_ASSERT_GUARD_REQUIRED` at the exact module source lines cited above.

**Evidence:** [executable pinned replay](../research_checks/X6_UNIT127_TRIADIC_NATIVE_ASSERT_FULL_MODULE_REPLAY_20261118.py) and [12-case original/strict/mutant result certificate](../research_checks/X6_UNIT127_TRIADIC_NATIVE_ASSERT_FULL_MODULE_RESULTS_20261118.json). The portable runner expects the two original source paths in a checkout, validates both actual Git blobs, creates isolated temporary working copies, uses an external call profiler and checks every 12-case expected exit/call count. No original scientific Result is admitted by these tests.

**Remaining:** The broader 28-LP active/current downstream dependency graph and alleged LP011 historical native signed argmax / LP019 positive natural N-BRC subtraction callsites still require exact independent source:line evidence. Their historical attribution remains `UNRESOLVED_PROVENANCE`. The existing independent Driver REQUEST_REVISION and R063 Issue #2416 review are separate; no new CLAIM or Driver identity is inferred from this author result.

**Next exact action:** Add this original module's 13-assert optimization gap to the existing 28-LP typed consumer ledger with source:line/observed-calls; inspect remaining actual current consumer imports rather than add auxiliary theorems. On the original X6 RUN, checkpoint Unit126–127 proof/certificate pointers and submit Native PROGRESS only after fresh same-owner claim/source verification, without replaying earlier requests.
