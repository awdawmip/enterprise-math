# X6 Unit110 — LP011 original-native mutation sensitivity and full always-on invariant checking

**Date:** 2026-11-18. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Status:** `AUTHOR-SOURCE-EXECUTED / EXACT-INTEGER / UNREVIEWED / NOT_ADMITTED`. This is an opt-in correction of a real validation gap, not the original R063/Helly benchmark, formal Result or independent review.

## Real observation (not a hypothetical mathematical theorem)

Unit109 established that the Unit108 LP011 version performs 3,375 original `signed_brc.shortest_path_multiplicity` calls even under `python -O/-OO`. The exact Unit108 source Git blob `296e4cdb8b5710a6b2017f24e4b6059a2554714e`, however, still had **13 assertion statements** covering the observer reconstruction, signed three-to-six-axis embedding, reversal, signed maximizer and shortest-path invariants. These assertions, unlike the already repaired native call, are removed under optimization.

The missing condition is substantive. With the selected named axes `(0,2,5)`, mutate the test-only `embed3` implementation from `out[k] = x` to `out[k] = 0`. The native module still receives a valid six-axis vector and returns a correct BRC number for **that wrong vector**. The local reference `c6` also evaluates the wrong vector. Consequently the Unit108 comparison of actual native BRC to `c6` agrees, while the intended native embedding of the original `d` has silently disappeared. Under `-O/-OO`, the original `D6` and `c3 == c6` checks are omitted, and the fully executed script **incorrectly prints PASS with 3,375 reported native calls**. Normal Python rejects the corruption.

A second test-only mutation `return frozenset(negative) -> return frozenset()` breaks the signed residual observer. It likewise passes Unit108 under `-O/-OO` while failing normally. These are controlled mutation witnesses, not claims that any repository production function was originally corrupted.

## Fix and actual full original-module experiment

Created a new **versioned** `research_checks/X6_UNIT110_LP011_FULL_ALWAYS_ON_NATIVE_V3_20261118.py` (Git blob `8d45dc1c88fd8dc897b6abe6d538de3185a135cd`) from exact Unit108 input. All 13 remaining assertions became always-on `if not (...): raise AssertionError`; the native module is **mandatory** and its original Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176` is checked at runtime before import. The original Unit108, frozen P000 V5 and native `signed_brc.py` are unchanged.

Ran true CPython subprocess execution in normal, `-O` and `-OO` over **all 3,375 signed triples in `[-7,7]^3`**, with the exact pinned source originally stored at `59538f585d037d09ef687b28715c4bc1a3f9fe03`. All three strict-mode executions exited 0, reported 3,375 actual native-function invocations and emitted the same JSON output as the original unmutated Unit108, with SHA256 `fba4072526686d8bf1c1415c977f565d8c652788f34a9d58e5b85831a8f8ff33`. Original output preserves 644 tied-dominance states, 1 zero, 1,513 legacy-selector agreements.

| Controlled fault | Unit108 normal | Unit108 -O/-OO | Unit110 normal/-O/-OO |
| --- | --- | --- | --- |
| Zero the selected-axis embedding | FAIL | **False PASS** | FAIL at always-on embedding check 04 |
| Erase negative-observer return | FAIL | **False PASS** | FAIL at always-on observer check 03 |
| Remove original native module | Original optional no-import | Original optional no-import | All modes FAIL, explicit dependency |
| Alter native source Git blob | Original LP011 had no blob guard | Original LP011 had no blob guard | All modes FAIL, exact pin guard |

All mutation tests used temporary copies. The program `research_checks/X6_UNIT110_LP011_MUTATION_SENSITIVITY_REPLAY_20261118.py` independently replays exact source pins, baseline and two mutations, and fails its own execution if the required contrast is absent. The JSON certificate `research_checks/X6_UNIT110_LP011_ALL_INVARIANT_MUTATION_RESULTS_20261118.json` records the exact outcomes and scope.

**Proof strength:** syntactic AST reasoning establishes the all-mode execution of explicit conditional branches; actual local subprocess outcomes establish this finite 3,375-vector and mutation coverage. This does not prove arbitrary consumers correct, does not establish any historic **wrong native argmax caller**, and is not independent review.

## Effect on mother task and next executable unit

The Unit109 finding (native function calls execute in optimized modes) remains correct, but it was **insufficient** to conclude the LP011 *whole semantic validation* retained meaning in optimized modes. Unit110 closes the embedding/observer/shortest-BRC assertion-elision hole in a new opt-in consumer.

Next: inspect the exact original LP019 versioned consumer for remaining `assert`-only *signed/thickness and word-count formulas*. If actual test-only mutation can survive optimized execution, apply the same source-pinned, opt-in always-on correction and run the original-native three-mode experiment. Separately retain `LP011/LP019 historical wrong-caller = UNRESOLVED_PROVENANCE`, the remaining 28-LP real caller ledger, independent Driver `REQUEST_REVISION`, and R063 benchmark support Issue #2416. No maintenance-lane identity is used.
