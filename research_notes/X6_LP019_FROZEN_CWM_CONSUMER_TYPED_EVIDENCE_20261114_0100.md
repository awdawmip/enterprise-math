# X6 LP019: frozen CWM downstream caller provenance — exact source and executable boundary

Observation: 2026-11-14 (Research lane `chatgpt-research-onhour-enterprise-math-20260923`).
Mother Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; registered publication `TP2-B4A441B23DA3159232C2`.
Scientific pins unchanged: P000 V5 baseline `59538f585d037d09ef687b28715c4bc1a3f9fe03`; frozen comparison corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
Method: read full original source bodies through the authorized GitHub connector at the frozen commit, retain exact Git blobs, and run the one self-contained original code body after byte-for-byte transfer to a local Python 3 interpreter. This is author evidence only; independent Driver review and Source semantic admission have not occurred.

## Three newly scoped frozen consumers

| Frozen exact source | Frozen Git blob SHA-1 | Inspected relevant semantics and status |
|---|---|---|
| `experiments/brc_weighted_local_bisimulation_boundary_check.py` | `c9d22d9b7e4f22884b48ad2801836cfdcd23995b` | lines 47–73: `CWM=(count,total,maximum)` with nonnegative rational weights; 79–112: two distinct local transition presentations induce equal complete future CWM; typed path-weight counterexample, **PRESERVE_PATH_BRC / KEEP**. |
| `experiments/brc_foundation_retrofit_check.py` | `8dbc1bdde0d63979f0b84d431e39864639aca423` | lines 192–255: `omega2(path)` is oriented three-component incidence, `cwm_recoalesce` uses positive fractions and `max(weights)` refers to **branch weight**, not a signed native-axis `argmax`; explicit comparison `omega2(forward)=1`, `omega2(reverse)=-1`, weights 2 and 1/2, aggregate `(2,5/2,2)`. **KEEP at inspected typed sites**, not an LP011 native-dominance wrong caller. |
| `experiments/brc_port_contextual_equivalence_check.py` | `add88bf5b4bd236010a04ec45bd06297628837f6` | lines 140–240, 310–370: `Fraction`-valued Schur/star effective port, hidden loop zeta, determinant and port relabeling; apparent subtraction is matrix algebra rather than a cancellation of positive path-count occurrences. **KEEP at inspected typed sites**, not an LP019 N-BRC signed-cancellation wrong caller. |

The second and third original files were source-inspected, **not re-executed** in this unit. All three are from the frozen pre-rebase corpus, not current native X6 Cell implementations. The report does not assert that every possible caller of these APIs has been inspected.

## Exact executable witness for path-typed LP019 boundary

Source: `experiments/brc_weighted_local_bisimulation_boundary_check.py` at frozen commit; exact fetched Git blob `c9d22d9b7e4f22884b48ad2801836cfdcd23995b`, independently matched to the on-disk source using `git hash-object`. Command `python -S experiments/brc_weighted_local_bisimulation_boundary_check.py`; original top-level `main()` executed, **exit 0**:

```text
BRC weighted local-bisimulation boundary PASS: future_x=future_y=(2,3,2) while local future-class transitions differ
```

Precise finite witness (all edge weights positive integers):
- `x` has paths `x→A1→t` with weight `1·1=1`, `x→B→t` with weight `1·2=2`.
- `y` has paths `y→A1→t` with weight `1·1=1`, `y→A2→t` with weight `2·1=2`.
- Both have `(C,W,M)=(2,3,2)`, while one-step transition CWM by future class `A={A1,A2}, B={B}` differs: `x→A=(1,1,1), x→B=(1,1,1)` versus `y→A=(2,3,2), y→B=(0,0,0)`.

This proves a **concrete finite model non-necessity** of same-class one-step weighted bisimulation for complete-future CWM equality. It does **not** equate signed algebraic coefficient cancellation with positive N-BRC multiplicities, and it supplies no direct native Cell, spatial-sign or primitive-axis history identity.

## Dependency disposition and continued mother objective

For these three specifically inspected historical sources, the maximum operator is typed `M=max(branch weight)` (or rational matrix/port algebra), not native signed axis dominance; no source site checked here supplies the alleged LP011 or LP019 wrong caller. Preserve `LP011_NATIVE_ARGMAX_WRONG_CALLER = UNRESOLVED_PROVENANCE` and `LP019_NBRC_SIGNED_CANCELLATION_WRONG_CALLER = UNRESOLVED_PROVENANCE`.

Highest science to reuse: native-cover original 516,299 exact checks; LP026 signed-BRC cover; full G25 signed shell 7,812 and 1,440 relative double fibres; first G3 20 `(rho,BRC)` collisions; R063 G25 132 double-axis singleton observers; **S6 repaired original checkers 56,510 + 59,003 = 115,513 assertions PASS**, separately certified in `research_notes/X6_LP011_LP026_S6_ORIGINAL_REGRESSIONS_EXECUTED_20261114_ONHOUR.md`, already GitHub- and RA-persisted by another current run, and **not duplicated** here.

Remaining exact step: inspect frozen R061/R062 consumer call-graph edges where `max(weights)` or formal negative coefficients are actually passed into a signed-native Cell/axis or a positive path-count assertion; trace source path, line and call arguments, or keep `UNRESOLVED_PROVENANCE` without inventing a culprit. Full 28-LP dependency closure and independent Driver `REQUEST_REVISION` remain open.

Researcher history: `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`; old RUN `RUN-756de85b94c23b46b181f7b8` with generation 5/revision 4 is read-only provenance, not fresh ownership. Latest own continuation read request `onhour-20261114-0009-x6-own-continuation-read-v1` was QUEUED on observation. No new CLAIM, Native PROGRESS, Scheduler or maintenance lane mutation was attempted.

Status: `SOURCE-PINNED THREE-CALLER BOUNDED INSPECTION / ONE ORIGINAL EXECUTED EXACT CHECK / AUTHOR-VERIFIED / NOT_REVIEWED / NOT_ADMITTED`.
