# X6 signed/derived S6 rotation: exact integer axis-type repair

Date: 2026-11-13. Task context: `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable P000 V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03` and frozen history `fd2bcff10ca6e147348b6c1236027fc0d2877df3` unchanged. Research lane label: `chatgpt-research-onhour-enterprise-math-20260923`, not maintenance. Scope: actual current executable consumers, not a new Foundation axiom or LP011/019 historical wrong-caller attribution.

## Reproduced failing input in prior exact current implementation

Both `Spatial6.rotate` and `Coord6.rotate` used the admission guard `len(p)==6 and set(p)==set(range(6))`. Python Boolean equality makes `False == 0` and `True == 1`. Thus the exact tuple `(False,1,2,3,4,5)` passed both old guards and was silently treated as a valid S6 permutation, despite not being six exact integer axis labels. `(0,True,2,3,4,5)` has the same defect. This is distinct from the earlier repaired Boolean **direction** defect. A float alias can also pass the set check and then fail at list indexing with a different error.

## Actual guarded code and original-checker changes

1. `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py`: add `any(type(i) is not int for i in p)` in `Spatial6.rotate`. Commit `1ff1bf9076d13ac966a6968511605f3f58281e28`, Git blob `405d9bc752bbf45582f2d0a6d9f91bff9cc5f89e`.
2. `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py`: add the same exact label restriction in `Coord6.rotate`. Commit `9f67abdd1d68cb53c2b13334730c49bd8faa26bc`, blob `9738543aace13f8a72af577e9ad8964c5fd40de8`.
3. The original `check_x6_signed.py` now rejects both Boolean alias permutations on four signed probes. Commit `33834ddedfb948bec353d8e182cde938fe852aab`, blob `83c5ed026c41360696019f2a1d92d3db41910295`.
4. The original `check_x6_coordinate.py` now rejects both aliases on two legitimate derived probes. Commit `352ed946aec1495262dc12a0b4216ef7d9ddff28`, blob `d562df4cedf3aa54fd3ca5db5ee0d17ff873a752`.

Every changed file was conditionally updated against its actual Git blob SHA and fetched back in full; all four readbacks matched the exact proposed text. No P000 source or historical evidence was edited.

## Focused executed exact check and limitations

An independently run Python 3 method-level reproduction, transcribing each corrected `rotate` method's operative body, enumerated all `6!=720` legal permutations for four signed-native and four nonnegative min-zero derived states. All **5,760 valid permutation/state checks** matched the explicitly computed coordinate relabeling. The same reproduction rejected three invalid label tuples on both representations and their four respective states: **24 exact invalid-input checks passed**. Result `PASS_X6_S6_FOCUSED_DOMAIN`. These computations checked the changed method logic with exact Python integer arithmetic; they did **not** execute the original project Python module imports from GitHub in this turn. Consequently the modified original checkers remain `ORIGINAL_REGRESSIONS_PENDING` for this new S6 patch, not silently PASS. Previous 56,502/58,999-check original execution certificate belongs to the *pre-S6-change* source version and remains valid only for that version.

## Mother objective / precise remaining evidence

The historical LP011 signed argmax caller and LP019 positive-count signed-cancellation wrong caller remain `UNRESOLVED_PROVENANCE`; no attribution is inferred from this new Python input defect. Other already established LP checks, G25 shell, G3 collisions, PathSqrt singletons and native cover benchmark are not rerun or reclassified. Independent Driver `REQUEST_REVISION` remains outstanding.

Next exact executable action: run both **modified original** project checkers with their verified dependencies and retain output/exit code; continue exact frozen `experiments/` and `scripts/` caller paths for LP011/019. Any native PROGRESS requires independently established current CLAIM/session/run. Historical Researcher `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`; former RUNs and claims are provenance only, not fresh write authority. The read-only current task request `onhour-20261113-2305-x6-task-read-v1` was QUEUED at last observation; preserve its ID.

Status: `GITHUB_AUTHOR_PATCHED_AND_READBACK_VERIFIED / FOCUSED_EXECUTED / ORIGINAL_REGRESSIONS_PENDING / SOURCE_PROGRESS_UNCONFIRMED / UNREVIEWED / NOT_ADMITTED`.
