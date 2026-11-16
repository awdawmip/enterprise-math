# X6 unit 55 — Helly S12 / native Cell consumer regression is optimization-safe

Date: 2026-11-16. Parent task: RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. Original on-hour Research lane `chatgpt-research-onhour-enterprise-math-20260923`, author EM-X6-FB6990, Source session MCP-082892eb480e45dea6d4b9fcc0491034. **AUTHOR-EXECUTED SYNTHETIC REGRESSION / NOT INDEPENDENTLY REVIEWED / NOT ADMITTED.**

## Prior evidence consumed (not repeated)

The original unchanged Helly producer `scripts/tool_discovery_helly_radon_certificate_calculus.py` is Git blob `6118b3bd04010e05355586d353c9cf0ec38b1070`. It emits a typed fixed-positive S12 chart with A={5,6,7}, B={3,4}, `sample_fixed_positive_chart_address=[5,3,0]`, and `native_cell_address_status=UNSPECIFIED_REQUIRES_CELL_ANCHOR_AND_ORDERED_SIGNED_AXIS_EMBEDDING`. Existing unit54 already exercised the source's 66,675 interval families, positive/negative source types, and independently verified 360 signed two-support X6 endpoint lifts / natural BRC 55,560. Original R063 six-blob Stage0 17 gates and 512 radii were author-executed in unit50. **Neither original computation was rerun in this unit.**

The directly importing active consumer `research_checks/X6_LP003_HELLY_FIXED_POSITIVE_CHART_TYPED_OUTPUT_REGRESSION_20261114.py`, old immutable blob `3ed2051763303e614b30ec17050d03d450da7dd6`, contained 16 `assert`-dependent acceptance expressions (including type fields, no native Cell address, boolean support, Helly-2, chain and Carathéodory). In CPython `-O` and `-OO`, `assert` statements and their side-effect-free predicate calls are not evaluated; a script can print `PASS` without evaluating these gates. This is an actual acceptance-boundary defect in the direct consumer **test script**, not a mathematical counterexample to the Helly producer.

## Repair and adversarial execution

Updated the *existing* typed consumer (no new runtime interface or frozen science change) to call `verify_typed_helly_producer(module)`, using explicit `require(condition, message)` implemented as an always-executed `if not condition: raise AssertionError`. All original exact chart/nativity, support and Helly checks are retained. The original producer remains unchanged; the path continues resolving `scripts/tool_discovery_helly_radon_certificate_calculus.py` in the repository.

The new synthetic adversarial test imports the exact repaired consumer code and checks one valid fixture, seven invalid fixtures: wrong coordinate type, fake native status, illicit `sample_native_address`, wrong chart intersection, a Helly-2 violation, a failed minimal chain and a failed Carathéodory lower-bound. It verifies all four required producer calls are actually made in the positive case. Three local runs under Python (ordinary), `python -O`, and `python -OO` all returned exit 0 and printed:

```
PASS_HELLY_TYPED_GUARD_OPTIMIZATION_SAFE_SYNTHETIC 1_valid 7_invalid
```

The exact patched consumer bytes were locally hashed as Git blob `21bf769020d53959a79bdc6699ae2302bbc530fe`, SHA256 `93c974e8c2f26d48c77cd2904f2abc9252b8b4304e5f35bb3847583d9b966089`; direct main update commit `4536dc07600be58faf44dc4bf16444f4c5bcddaa`. The newly saved adversarial test is Git blob `b98856aaa8034726b0f6eb29e7a0f83a8d84c40f` at commit `e44b8c1354b51c0a429b408cd938eb16916cce33`. Both remote blobs were read back; content identity of the local test and published file was verified by Git OID.

**Evidence limits:** These three runs exercise the real repaired `verify_typed_helly_producer` function with synthetic producer objects; they are not a fresh full execution of the original Helly producer. The prior original-program unit54 remains the separately preserved source evidence. No new native X6 identity, Helly theorem or full 28-LP closure is claimed. The live native address still requires Cell anchor, two named axes and polarities; `[5,3,0]` is local-chart-only.

## Outstanding work and exact successor

1. Continue actual consumers of the historical 28 LP claims beyond the previously verified 11 production modules and six direct tests. This unit adds one **repaired LP003 directly importing consumer** and an adversarial test, not a claim of exhaustive cross-repository downstream reachability.
2. Pin or precisely rule out a historical LP011 signed-native singleton argmax caller and LP019 illegal signed cancellation of positive `N_BRC`, retaining typed nonmatches. Do not mislabel correct weighted-branch `dominant_mass` or chain-complex cancellations.
3. Independently resolve the Driver `REQUEST_REVISION`; author may provide evidence but may not self-review/admit.
4. Original unit52–54 Native checkpoint request `onhour-20261116-0911-x6-unit52-54-native-semantic-progress-v1` was consumed as `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED` (authenticated readback true, Source commit `d05e82e1bf358fbaa927698997f8c42834f8d565`). Same-SID resume for new unit uses original `onhour-20261116-1004-x6-own-run3356-resume-after-unit54-v1`; initially RUNNING/WAIT_ORIGINAL, must reconcile before another protected PROGRESS. No re-claim or maintenance-lane identity.
