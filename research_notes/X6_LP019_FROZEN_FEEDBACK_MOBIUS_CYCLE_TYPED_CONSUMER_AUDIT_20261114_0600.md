# X6 LP019 frozen feedback/cycle consumer audit — source-typed sign versus positive BRC

Date: 2026-11-14 (on-hour TASK_RESEARCH). Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable publication `TP2-B4A441B23DA3159232C2`. Status **AUTHOR-PROVED SOURCE-TYPING / INDEPENDENT EXACT FINITE CHECK PASS / UNREVIEWED / NOT_ADMITTED**. This is a scoped downstream provenance increment, not a completed 28-LP dependency graph, not a native Source PROGRESS, and not an independently reviewed Result.

## Frozen domain and source identity

Keep P000 V5 signed native X6 on its project-pinned source (`59538f585d037d09ef687b28715c4bc1a3f9fe03`) and the frozen historical candidate corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Do not reassign historical positive-weight graph kernels to signed Cell dynamics. All five complete original Python file bodies below were read via connected GitHub at the frozen commit. Paths, original Git blobs, and actual relevant call sites:

| Frozen original source and Git blob SHA1 | Exact relevant locations | Typed outcome |
|---|---|---|
| `experiments/brc_feedback_mobius_interaction_check.py` — `7ed252d735e37dd4bca3088f1f2ffa4fac5b446e` | `subset_zeta_table` 78–85, `mobius_interactions` 89–104, `check_kernel` 137–157, pure 3-cycle 268–281 | **KEEP_FEEDBACK_MOBIUS**: multiplicative inversion of rational principal-minor zeta terms; no signed native-axis or path-count cancellation |
| `experiments/brc_cycle_interaction_polynomial_check.py` — `6f37fc8021bf5d9556ed6ff5d5fa34db6b097219` | signed cycle-set coefficient 65–109, polynomial evaluation 112–120, `response_data` 139–155, response derivative assertions 318–348 | **KEEP_DETERMINANT_SIGN**: negative coefficients of `det(I-W)` and its derivatives are algebraic; edge response is positive when stable |
| `experiments/brc_holonomy_parity_thickness_check.py` — `d2aa874c2e0e7bda6b830c98fab6c44817f5ce44` | `root_via_brc_of_power_ratio` 80–91, negative/dynamic boundary 212–230, fixed skeleton 233–258 | **KEEP_RATIONAL_VALUATION**: parity and divergent boundary in rational holonomy, not signed-X6 Cell steps |
| `experiments/brc_feedback_circuit_atoms_check.py` — `0aaad55f87d238388ccec1a22d8bf6b1670ed32b` | nonnegative graph `shortest positive path distances` at 127, rational cycle weights and valuations 241–285 | **KEEP_POSITIVE_GRAPH**: positive weighted graph support/mass, not net displacement |
| `experiments/brc_newton_selector_simple_wall_crossing_check.py` — `678ace41d8d41e5bab45978e9cccfc2309d7d26c` | BRC root-selector wall-crossing checker, uses `brc_critical_degeneracy` 7, original checker conclusion 178 | **KEEP_ROOT_SELECTOR**: selected-root wall, not X6 signed axis dominance |

This finite audit rules out *these named typed locations* as witnesses of the alleged LP019 positive N-BRC signed cancellation, and the Newton root selector as a witness of LP011 native axis argmax misuse. It makes no repository-wide absence claim and leaves the ledger's particular historical wrong-caller allegations **UNRESOLVED_PROVENANCE**. Frozen original scripts were **read, not run** this round.

## Load-bearing exact mathematical distinction

For an edge-weighted nonnegative matrix `W(q)` with spectral radius `rho(W)<1`, define `P(q)=det(I-W(q))>0` and `S=(I-W)^{-1}=sum_{k>=0}W^k`. For one labeled edge `e=(a,b)` with weight `q_e`, write `W(q)=W_0+q_e E_{ab}`. Jacobi's determinant derivative gives

```text
dP/dq_e = -P * S[b,a]
R_e := -(q_e/P)*(dP/dq_e) = q_e*S[b,a] >= 0.
```

Thus the minus sign in the determinant/derivative **does not subtract positive path multiplicities**; it is exactly the transformation from a signed determinant expression to a nonnegative recurrent edge-response. This algebra is valid under the stated positive graph and convergence assumptions, not a proof that a six-dimensional signed native endpoint equals the old graph state.

Exact witness from a nonnegative two-state graph:

```text
W = [[1/5, 1/4], [1/3, 0]]
P = 1 - 1/5 - (1/4)(1/3) = 43/60
S = [[60/43,15/43], [20/43,48/43]]
R_(0,0)=12/43; R_(0,1)=5/43; R_(1,0)=5/43.
```

Every edge/path mass here is nonnegative although `P` has negative monomial coefficients. Separately, for the pure directed three-cycle `x=y=z=1/2`, all proper principal subset zeta factors equal one; `det(I-W)=7/8`, `zeta({1,2,3})=8/7`. The third-order Möbius interaction `J_{123}=8/7`, while `J_S=1` for proper nonempty `S`. This Möbius product contains reciprocal exponents; those do not represent negative N-BRC counts.

## Executed independent finite rational corroboration

The actual standalone file `research_checks/X6_LP019_FEEDBACK_DETERMINANT_TYPED_CANCELLATION_20261114.py` was locally executed using exact `fractions.Fraction`; stdout `PASS_X6_LP019_TYPED_FEEDBACK_DETERMINANT_AND_MOBIUS`, exit code 0. It exhaustively checks **256** nonnegative 2×2 matrices whose entries lie in `{0,1/5,1/4,1/3}`, testing **1,024** labeled-edge determinant-derivative identities, plus **64** pure 3-cycle rational cases, and the displayed witnesses. All have exact arithmetic and zero failures. Its executable local bytes SHA256 are `005f5950800fe2a77bd9e55950c0c073169aa09017b9f2497faddf9c95e0dd8d`, Git blob `fd6c60e37c1dfcb7b98ac3806074eb8037bbc6a8`; remotely published code committed at `11a3cae1856d9a5dc73d697f5b361600f86445ad` and exact Git blob read back equal.

**Scope:** These finite checks corroborate the analytic type distinction and cover the declared finite grids; they do not run the five frozen original programs, test arbitrary `n` by exhaustion, certify native LP019 benchmark, or authorize a current Result.

## Parent task continuation packet (author-side only)

- **Mother objective:** reconcile 28 historical LP claim rows with actual signed native X6 science and downstream consumers for independent Driver `REQUEST_REVISION`.
- **Frozen science / do not repeat:** preserve R061/R062 positive-sector 72 and original accepted Stage0; R063 fixed-positive PathSqrt, 132 G25 signed pair chart singleton proof; G25 whole shell and 1,440 observer double fibers; LP026 actual native regressions; previous S6 original checker 115,513 PASS; prior triadic 12-slot to six-slot exact proof and m3 enumeration. No old accepted result is changed here.
- **New current narrow increment:** five specific frozen callable program bodies typed, two exact interface identities and 1,088 finite checks. Typed verdict `KEEP`; the exact wrong historical LP011/LP019 call sites remain unresolved.
- **Next smallest real unit:** trace actual current/frozen `R061/R062`, `Sigma_O^(ij)`, min-zero `can3`, or positive BRC to signed-X6 consumer calls in the remaining named `experiments/`, `scripts/`, and active consumer graph. For a *real* caller, retain exact immutable file/line, input observer type, actual output, whether a non-factorizing native operation is performed, and only then `KEEP/RETYPE/REVISE`. Do not re-execute original benchmarks already covered or turn a negative bounded search into full absence.
- **Research logical conversation:** `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). Original service session `MCP-082892eb480e45dea6d4b9fcc0491034` / Researcher `EM-X6-FB6990` is source-registered with a matching declared host-session label; legacy claims and runs are historical projections, not current write authority. Source continuation original request `onhour-20261114-0608-x6-source-continuation-v1` remained `QUEUED / WAIT_ORIGINAL` when this author-side note was prepared. Reconcile the same request, verify winning claim and CAS, then perform any legitimate current Source publication. Do not register another session or dispatch through maintenance.
- **Unresolved:** current native semantic PROGRESS, 28-LP full real consumer closure, LP011/LP019 exact wrong-caller provenance, independent Driver decision. Scientific conclusion `AUTHOR-PROVED / INDEPENDENT FINITE EXACT CHECK PASS / UNREVIEWED / NOT_ADMITTED`.

Evidence is an author-side research note on GitHub only. It does not grant current Task execution authority, overwrite preserved frontier, or count as a native checkpoint.
