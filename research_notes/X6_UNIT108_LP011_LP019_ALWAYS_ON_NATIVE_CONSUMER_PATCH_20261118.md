# X6 Unit108 — opt-in strict original-BRC consumer variants, preserved frozen and current sources

**Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, 2026-11-18. **Status:** `AUTHOR-SOURCE-PATCHED / REMOTE-BYTES-VERIFIED / INTEGRATION-NOT_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Trigger: exact Unit107 consumer validation failure

Unit107's source-audited, independently executed Python `assert`-elision proof shows that two **existing** X6 test consumers report unchanged native comparison counters under `-O` and `-OO` while native calls located inside those `assert` statements are skipped altogether. This is a concrete test-effect counting error; historical LP011 native argmax and LP019 nonnegative natural path count wrong callers remain `UNRESOLVED_PROVENANCE`.

Original tested current source references:
- `research_checks/X6_LP011_TYPED_DOMINANT_CONSUMER_20261112.py`, git blob `cf2c11d47a4abf5a462c4c96540a125f0f942a8d`: optional original Source import at lines 83–86, imported `shortest_path_multiplicity` at 104, followed by `imported_module_calls += 1` at 105.
- `research_checks/X6_LP019_SIGNED_THICKNESS_AND_BRC_FIBERS_20261112_ONHOUR.py`, git blob `24664a814c83b471febaabb4a1c0b0ae0c59d571`: original module Git blob guard at 102, `endpoint_multiplicity` check at 112, counter at 116, return assertions at 128–131.

## Actual authorized source changes, without replacing originals

Two **new versioned opt-in full-source variants** were created from the current exact original bytes with narrowly scoped, one-occurrence checked replacements and GitHub immutable readback:

1. `research_checks/X6_UNIT108_LP011_TYPED_DOMINANT_CONSUMER_ALWAYS_ON_NATIVE_V2_20261118.py`: commit `7b0ddbd5f8bd311c5693d9fd3bb36219b6b1dc0c`, blob `296e4cdb8b5710a6b2017f24e4b6059a2554714e`. The import-loader check is always-on; imported native `shortest_path_multiplicity(embed3(d))` is assigned outside `assert`, explicitly equality checked, and only then does the original `imported_module_calls` counter increment. The original optional absence of `signed_brc.py` remains reported as `existing_native_brc_imported=false` rather than native success.
2. `research_checks/X6_UNIT108_LP019_SIGNED_THICKNESS_ALWAYS_ON_NATIVE_V2_20261118.py`: commit `10ebab9e493b76814083dd60c52eea4398d8071d`, blob `c1842fbd34fb6fffa08a40a709b4838a6f2a5640`. The original exact Git blob pin guard is now always-on. Each original native `endpoint_multiplicity` result is assigned and checked outside `assert` before the counter increments, and original `return_multiplicity` probes are now always-on. The expected original blob value and frozen benchmark input objects were **not** changed.

Each replacement targeted a single exact code span, verified against the original Source bytes. The original two GitHub paths were left unmodified. No new native benchmark, schema, task, claim, scheduler, or hosted CI was created.

## Proof of control-flow repair and current validation limits

In the new variants, Python optimization can remove other remaining supplementary `assert` statements, but **cannot remove an expression statement assigning the native API return value or a subsequent conditional explicit `raise`**. The native comparison counter is incremented only after the call and its explicit equality check. The fixed pin value cannot be bypassed by removing an assertion.

This is a complete syntactic and semantic control-flow correction to the two affected native call sites. Its Source bytes were checked remotely; however, **neither complete patched program has been run against its real `signed_brc.py` dependency** in this run. In particular, no output claiming 3375/10364 true, identical native calls across all Python modes has yet been generated. Local Unit107's self-contained reproduction is not a substitute for such integration tests. Additional existing non-native assertions were deliberately left untouched to keep the patch scoped; future -O overall PASS claims need those separate invariant semantics considered.

**Acceptance next:** materialize exact original `signed_brc.py` (LP019 pinned blob `300a96e3dc24bf6fff73743037a0347a8bc83176`) with its compatible dependencies; run both versioned variants in normal, `-O`, `-OO`, require original real API calls 3375 and 10364 respectively if the selected original path is available and its pin matches, and require matching computed values and explicit failure on bad pin. Repair any observed dependency-version mismatch as a separate reproducible pin-bound issue, never by silently replacing frozen input.

R063 native original reproduction remains Issue #2416 and is untouched. Unit107 proof, 28-LP typed corpus and independent Driver `REQUEST_REVISION` remain separate obligations. Native Source PROGRESS for Units105–108 must await live same-RUN authorization, not a checkpoint from another lane.