# X6 Native Time — Unit255: exact original-BRC incompatibility of the positive-only triadic transfer candidate

Date: 2026-11-22 07:00 Asia/Hong_Kong. Parent `PO-X6-UPPER-STRUCTURE-20260906`; Task `RS-X6-NATIVE-TIME-DYNAMICS` / publication `TP2-91D4A7C2F63805BE21A3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`; original provenance Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`.

**Status: AUTHOR_PROVED / EXACT_ORIGINAL_BRC_REPLAY_EXECUTED / UNREVIEWED / NOT_ADMITTED / NATIVE_PHYSICAL_EXECUTION_PENDING.** This is a scoped compatibility test of an actual saved candidate, not a new model of physical time.

## Fixed original sources

- Frozen P000 native X6 signed Cell torsor: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
- Original 36-case Unit245 complete BRC witness: `f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`; blob `113d2102fe393bfd6f77bf7cca093b4cecf6796f`.
- Another Researcher's conditional candidate: `f41c2690daba467ecbde99615a1337e67be46ffd:research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md`; blob `66b3a856b3c566512ada2c2201c6888b06cb0bbc`. Its movement law only offers `c -> c + E_{i_r}` for one of three **positive** frame axes, preserving an intact triad. It explicitly marks physical Port permission and environment update as candidate assumptions.

The original OUTER chart embeds in the selected X6 three-axis restriction as `a=(e1,e2,e3,-e1,-e2,-e3)`, `x_(2r)=P+a_r`, `x_(2r+1)=P+a_r+a_(r+1)`, with `P` chosen as chart Cell anchor. The checker reconstructs every signed primitive displacement from these integer six-axis Cells, retaining the original triad label, chronological event order, occupancy, Port direction, and ring winding.

## Theorem — the positive-only guarded candidate cannot perform a nontrivial original Cell-return

Let a labeled intact triad start at a native Cell `c` in the affine `Z^6` torsor. Suppose each transfer step permitted by a candidate law has displacement `+e_i` for some signed-chart *positive* native basis index `i`. For a finite path of length `M`, the final displacement is `sum_i n_i e_i` with `n_i >= 0` and `sum_i n_i=M`. A full native Cell return requires all `n_i=0`, hence `M=0`. Therefore **every nonempty closed return requires an allowed negative native primitive transition**. This holds separately for each intact triad and does not rely on a C24 sensor or a new physical law.

More quantitatively, for any serial path of two labeled triads that individually return to their initial full X6 Cells, let `n_(T,i,+)`, `n_(T,i,-)` be the signed-axis counts. Native Cell equality gives `n_(T,i,+)=n_(T,i,-)` for each `T,i`. Consequently if `N` primitive movement events occurred,

\[
N_+=N_-=N/2.
\]

This is an exact compatibility constraint for the **original movement ledger**. A candidate authorizing only the positive half of the signed alphabet cannot realize any nonzero original complete-return certificate.

## Actual immutable signed-BRC replay

The current V8 verifier re-executed the Unit245 compact route decoder across all 36 original fully ordered witnesses, checking occupancy exclusion, exact permitted directed center pair, signed native-axis one-step displacement, two labeled returns and the original `(-12,+12)` ring winding. It did **not** search for substitute paths or alter the frozen input. All checks passed.

| Quantity | Exact replay |
|---|---:|
| Original complete witnesses | 36 |
| Chronological primitive movement events | 1,312 |
| Positive signed-axis events | 656 |
| Negative signed-axis events | 656 |
| Positive ring steps / negative ring steps | 530 / 530 |
| Positive center-spoke steps / negative center-spoke steps | 126 / 126 |
| Witnesses executable entirely with the positive-only candidate | **0** |
| Replay violations | 0 |

For the two 28-event witnesses `(i,j)=(6,0)` and `(8,2)`, **all four center Port steps are positive-axis movements**, yet each witness still requires precisely **14 negative original ring steps**; a positive-only candidate can therefore appear to support the center Port while being unable to execute the actual two-triad closed BRC trajectory. The first optimum has six positive/six negative e1 steps, four/four e2, four/four e3; the second exchanges the six/four distribution between e1 and e2.

The exact negative-event cost matrix in ingress/egress order `0,2,4,6,8,10` is

```text
15 19 18 19 19 23
19 15 23 19 19 18
16 18 16 24 19 16
14 15 20 18 22 17
15 14 17 22 18 20
18 16 16 19 24 16
```

The matrix equals exactly one half of Unit245's original event-cost matrix; it is **a necessary signed-transition budget**, not the number of physically executed Port events.

## Closest real native acceptance question

The 2026-11-18 resource-guard candidate is a correct *conditional* positive three-way choice proof within its own stated scope. Its positive-only transition interface cannot furnish the signed primitive events needed by the frozen Unit245 test. The smallest **interface question**, rather than a presumption of new physics, is whether Source admits the same intact-three-token occupancy/conservation guard on **negative** signed-axis transfers, and which negative directions are actually permitted for each triad frame. A read-only rejection by Source of one needed negative ring step is already a decisive result against running the original witness under that guard. A positive-only Port acceptance is insufficient.

For a native test, obtain the real signed force-triad update and ordered environment/Cell ledger first; choose the already saved Unit245 route for each admissible directed Port pair, and preserve the independent event-3 C24 and event-7 C3 readouts from Units251–252 only if an actual calibrated observer exists. No replacement shortest-route search, new task claim, other owner's identity, R063 benchmark substitution or physical measurement is asserted.

Original #2903 typed-continuation Source materialization support remains separate. There is no newly verified winning CLAIM; protected Native semantic PROGRESS for Units233–255 remains pending. Keep this result as author-side GitHub evidence and Activity only, until a genuine accepted native control path and independent review exist.
