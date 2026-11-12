# X6 / LP026 — pinned source-import regression execution (2026-11-13)

**Evidence type:** independently executed, source-byte-pinned Python regression of a previously published auxiliary theorem. **Author:** current RESEARCH_DRIVER verification unit. **Execution environment:** local ephemeral container, CPython 3.13.5. **Observation:** 2026-11-12 16:09 UTC (2026-11-13 00:09 Asia/Taipei). This is an execution report, not a new Result, native review, CLAIM, integration promotion or task/parent closure.

## Exact inputs and execution method

Retrieved four source files through the authorized GitHub connector from `awdawmip/enterprise-math` canonical `main`. Materialized byte-for-byte into an isolated local directory preserving the original relative paths. Before execution, confirmed **Git object blob SHA-1 equality** for all four local files against GitHub-returned blob IDs; the original test script independently repeated three module-pin checks before import.

| Source path | Verified Git blob SHA-1 |
|---|---|
| `research_checks/X6_LP026_SHARP_STREAMING_DEPTH_SIDE_REGISTER_SOURCE_IMPORT_20261112_DRIVER.py` | `5f4c279813087e774e471bc9d96cb7b156a38630` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` | `ef66285d8ae81569cbbd3195b3e38daae37944ef` |
| `experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py` | `3f7d9e62a4dd66e7888a69ff87276b283c891aac` |
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` | `300a96e3dc24bf6fff73743037a0347a8bc83176` |

Test script original publication: `2c9309ab0c0b8b2b6d835fd40e8c99f2dcf2d595`. Scientific scope: `research_notes/driver/2026-11-12_x6_finite_depth_signed_brc_cover_rotation_descent_and_minimum_memory.md`, §10. Directly exercised imported `CoverState.step` / `Coord6` and `signed_brc.endpoint_multiplicity`, not independently reconstructed substitutes.

Invocation after exact materialization:
```shell
python research_checks/X6_LP026_SHARP_STREAMING_DEPTH_SIDE_REGISTER_SOURCE_IMPORT_20261112_DRIVER.py
```

## Observed execution receipt

- **Exit code:** `0`; **stderr:** empty.
- **Python:** `3.13.5`.
- **stdout SHA-256:** `a8e65aa55ca957fd250246573e43efbe3d7d6c9ef7b25fe33d285225f8ae0f0a`.
- **stderr SHA-256:** `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- **checker SHA-256:** `196a25ecb9f39f81bdb4cc0651318118c2676009e9d1688295b10dc8ab04f2ea`.

```text
PASS_X6_LP026_SHARP_STREAMING_DEPTH_SOURCE_IMPORT
moduli_1_to_6_horizons_0_to_6 42
actual_source_CoverState_step_checks 425376
actual_source_signed_BRC_comparisons 27690
cover_ball_fiber_groups_checked 82723
```

The script's complete stdout additionally printed the three source Git-blob pins above. Execution tested 42 finite configurations (moduli 1–6; horizons 0–6), endpoint-layer counts, cover-side register transitions, cross-length endpoint uniqueness, sharp fibre capacity and exact signed-BRC endpoint multiplicities through length 4. No assertion failed.

**Scope and provenance:** The passed executable is the previously published Driver-authored checker with precisely its pinned source dependencies; the container was not a complete repository checkout or project CI environment. This is actual pinned-source import execution. Mathematical proof and Native Result admission remain separate. The source modules and original author-side work retain their existing authors and task ownership.

## Routing

Link this evidence to the existing X6/LP026 owning scientific frontier and its already published §10 result through the correct current Task/Result intake, with independent review as required. Original F7 Native Review is an unrelated ongoing Driver authorization/adapter dependency. Do not create a duplicate task/CLAIM merely to move this verification report.

## Additional nontrivial-capacity stress runs (same pinned module imports)

After the 42-case script pass, imported its unchanged `check(modulus,horizon)` function from the byte-exact checker into a short local invocation, without editing the four source files. The following calls returned normally with assertions satisfied:

| Modulus | Horizon | Sharp capacity `1+floor(H/(3m))` | `CoverState.step` checks | Signed-BRC checks | Fibre groups |
|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 3 | 124,368 | 1,375 | 12,755 |
| 1 | 8 | 3 | 286,416 | 1,375 | 23,477 |
| 1 | 9 | 4 | 605,340 | 1,375 | 40,489 |
| 2 | 7 | 2 | 124,368 | 1,375 | 18,892 |
| 2 | 8 | 2 | 286,416 | 1,375 | 36,586 |
| 2 | 9 | 2 | 605,340 | 1,375 | 65,630 |
| 2 | 12 | 3 | 3,920,280 | 1,375 | 273,882 |

The `m=1,H=9` case exercises the **four-state** bounded-horizon register; `m=2,H=12` exercises a three-state register over longer paths. These are additional finite regression results, not a changed theorem. A subsequent `m=3,H=9` call was not reached before the surrounding batch process timed out; no outcome is claimed for that call. Individual previously printed completed cases retain their observed pass status.
