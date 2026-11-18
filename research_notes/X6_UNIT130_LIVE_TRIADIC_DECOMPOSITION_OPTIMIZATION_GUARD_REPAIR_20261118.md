# X6 Unit130 — current signed triadic decomposition BRC, always-on actual executable repair

**Date:** 2026-11-18. **Mother objective:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Research lane:** `chatgpt-research-onhour-enterprise-math-20260923`. **Status:** `AUTHOR-CURRENT-SOURCE-PATCH-EXECUTED / EXACT-INTEGER / UNREVIEWED / NOT_ADMITTED`.

## Real current downstream finding

Source `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py` is a live original consumer of the signed six-axis triadic event count and BRC incidence formulas studied in Units124–125. Its original actual main Git blob was `5d0f2cb88a0d4e437b5025e9050e3044f7831cd4`, 5,178 bytes. It used **14 bare Python `assert` mathematical tests** across signed triad type size, decomposition eligibility, greedy-versus-brute feasibility, signed ordered multiplicity, label combinatorics, unordered counts and factorized weight identity. Under CPython `-O/-OO` all those mathematical predicates disappeared; the output still reported `PASS_X6_TRIADIC_DECOMPOSITION_BRC_V2`.

The controlled mutation is on the authentic original source's `formula_signed_ordered(d)`: replace only its return of `n` with `0` in a temporary execution copy. Unmodified original normal Python correctly rejects the wrong formula, but original `-O` and `-OO` still exit 0 and print the unchanged full PASS report. The original clean modes all exit 0 with stdout SHA256 `c7c06070d738fe78128ef2683cfcebf04195658bf2793993bed90e0bd7489dbc`.

## Scoped live repair and CAS

Only the 14 actual original mathematical assert predicates were transformed into unconditional `if not (...) : raise AssertionError('unit130_guard_NN')` validations. In two original single-line `for ...: assert ...` statements, the body becomes an indented ordinary `if`. Original mathematical formulas, loop domains, signed event definitions, output text, external inputs and P000 frozen pins are unchanged. This restores real validation in optimized CPython modes and does not change the model or counts.

- Actual current Source write: `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py`.
- Guarded predecessor blob `5d0f2cb88a0d4e437b5025e9050e3044f7831cd4`; publication commit **`2a80ba850f65bd39ccc4bfa18dc4767e73435f55`**; corrected blob **`d2b4ce1c13f90e31ca1167ee1eea1ef49c24b95d`** (5,802 bytes), fetched and compared byte-for-byte against the tested locally prepared source.
- No Source P000, frozen native signed BRC source `300a96e3dc24bf6fff73743037a0347a8bc83176`, original R063 C3/C4 benchmark or historic prior blob was modified.

## True whole-program validation

The existing module was actually executed in a byte-identical local copy with CPython 3.13.5 in normal, `-O`, `-OO`, clean and controlled-fault variants. All 3 clean patched runs exit 0 and have **identical stdout SHA256 `c7c06070d738fe78128ef2683cfcebf04195658bf2793993bed90e0bd7489dbc`**, exactly the original normal-mode output.

The actual program covers **2,493 candidate degree vectors**, **5,444 signed formula states** (160 atomic and 5,284 two-event count vectors), **25,600 signed two-event input histories**, 20 three-axis choices, 160 signed types and the exact full (D=(1,1,1,1,1,1)), (D=(2,2,2,2,2,2)) ordered/unordered decomposition checks. 14 original mathematical predicates are active in the patched AST with zero remaining `Assert` AST nodes. With the `formula_signed_ordered(d)` fault present, all **three patched execution modes reject it at `unit130_guard_06` (exit 1)**. The old original test had wrongly passed this precise fault in `-O` and `-OO`.

The published [current-source executable and three-mode/fault regression](../research_checks/X6_UNIT130_TRIADIC_DECOMPOSITION_ALWAYS_ON_NATIVE_REGRESSION_20261118.py) pins the corrected Git blob, checks the absence of optimized-away AST asserts, counts the 14 predicates, runs the full existing program in all three modes and injects the same isolated formula fault with the current source in each mode. Its three actual outer modes exit 0 and produce identical JSON SHA256 `4bba5b42e99a1e25e76fd24c1cabee458eb4f2a1bcce82bb0048c8837cc41989`. The [results certificate](../research_checks/X6_UNIT130_TRIADIC_DECOMPOSITION_ALWAYS_ON_NATIVE_RESULTS_20261118.json) records the original/mutant and patched/mutant distinction.

## Mother-task disposition and continuation

**Current downstream source:line classification:** `PRESERVE_PATH_BRC / LIVE_ACTUAL_TRIADIC_BRC_VALIDATOR_REPAIRED / THREE_MODE_MUTATION_SENSITIVE`. The exact affected original locations were its 14 original `assert` mathematical predicates, now 14 stable `unit130_guard_01..14` checks; actual current executable does not hide signed multiplicity or decomposition failures under optimization.

The mathematical statement is the finite exact original signed-triad decomposition census at its original declared input range. This author-side program repair preserves and validates its real path/branch-count semantics, not a claimed general 28-LP or R063 scientific admission.

The immediate next research operation is to extend the canonical 28-LP typed source:line consumer ledger for these two actual repaired current scripts (Unit129's atomic signed-midpoint checker and this Unit130's signed triadic decomposition BRC checker), examine remaining live consumers, and pursue the unlocated historic LP011 native signed argmax and LP019 positive natural BRC subtraction allegations at original frozen file:line. The independently authorized Driver retains its `REQUEST_REVISION` and R063/Helly original six-file, 512-row review via Issue #2416.

Native Source operations remain separate: previous exact `onhour-20261118-1707-x6-own-units126-127-native-progress-v1` and `onhour-20261118-1701-x6-own-exact-continuation-v1` must be consumed by original request ID before any overlapping privileged semantic publication. Author GitHub source, report, and Research Activity are genuinely persisted; independent review/admission remains outstanding.
