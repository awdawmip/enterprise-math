# X6 Unit76 — pinned-axis min-zero is a lossless native two-axis chart

Date: 2026-11-17 (Asia/Hong_Kong). Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2. TASK_RESEARCH author lane: `chatgpt-research-onhour-enterprise-math-20260923`; own Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. This is author evidence, not independent Driver review.

**Frozen mathematical input:** P000 V5 signed X6 at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical pre-rebase corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. No change to P000, source pin, native six-dimensional space or original R063/Helly bench.

## Exact native/observer theorem

Choose three *named* native X6 axes and set the other three coordinates explicitly to zero. In the selected signed `Z^3` chart define `D=Z(1,1,1)`, `can3(z)=z-min(z)(1,1,1)`, and `A={r in N_0^3 : min(r)=0}`.

For an identified selected axis `j in {0,1,2}` and a **known signed integer** `c`, let `H_{j,c}={z in Z^3 : z_j=c}`. Then

`can3|_{H_{j,c}} : H_{j,c} -> A`

is a **bijection**, with completely explicit inverse

`L_{j,c}(r)_i = r_i+c-r_j`.

Proof: for `z in H_{j,c}`, `r_i=z_i-h` and `r_j=c-h` where `h=min(z)`; hence `z_i=r_i+c-r_j`. Conversely for every `r in A`, `z=L_{j,c}(r)` has coordinate `j=c`, and `min(z)=c-r_j`, so `can3(z)=r`. This proves two-sided inversion for **all integer** coordinates. Its algebraic reason is the exact transversal `H_{j,c}` of the diagonal cosets; `H_{j,0} ∩ D={0}`.

On the `c=0` native two-axis subgroup, `L_{j,0}` is a group isomorphism from the quotient `Z^3/D` (represented by `A` with `r⊕s=can3(r+s)`) to `H_{j,0}` under ordinary signed native addition:

`L_{j,0}(can3(r+s))=L_{j,0}(r)+L_{j,0}(s)`;
`L_{j,0}(can3(-r))=-L_{j,0}(r)`.

For `c ≠ 0` the same statement is affine: `L_{j,c}(r⊕s)=L_{j,c}(r)+L_{j,c}(s)-c(1,1,1)`. The selected axis label and pin `c` are semantic **input data**, not inferred from an untagged min-zero triple.

## Exact native R061 adapter and positive BRC counts

Let the actual signed two-axis displacement be `z=(a,b,0)` (the other three native X6 coordinates are zero). Put `r=can3(z)`. The historical fixed-positive R061 reverse decoder in the frozen original `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`, **lines 235–246**, computes, for nonnegative `(a,b,0)`, `M=max(a,b,0)` and

`can3(-z)=(M-a,M-b,M)`.

This formula remains correct as a **relative min-zero inverse**. With the known anchored coordinate `z_3=0`, it recovers the **actual signed native reversal without an added selection bit**:

`L_{2,0}(can3(-z))=(-a,-b,0)`.

Consequently for any `a,b in Z` the native positive shortest-path BRC is reconstructed exactly from the anchored relative observation:

`N_native(z)=(|a|+|b|)!/(|a|!|b|!)`.

It is invariant under native reversal. There is no signed cancellation of natural BRC multiplicities. This reconstructs endpoint/count from the known anchored chart, not an ordered individual path history.

**Typed 3-4-5 witness:** original native `z=(3,4,0)`, native reverse `(-3,-4,0)`, native `G=25` in both directions and native `N_BRC=35` in both directions. Historical inverse observer `r^-=(1,0,4)` has `Σr_i²=17` and naive positive-word count `5`, while `L_{2,0}(r^-)=(-3,-4,0)` repairs both values. Smaller positive-sector mismatch: `z=(0,1,0)` has native reverse count `1`, but `can3(-z)=(1,0,1)` yields naive positive-word count `2`.

## Exact boundary for future consumers

The above lossless lift requires the named coordinate and its actual pin. On the *full* signed three-axis `Z^3`, `can3((3,4,0))=can3((4,5,1))=(3,4,0)` but the raw states are distinct. When a permitted native update changes the pinned coordinate, its new integer value must be retained or recomputed from the correctly labeled action before reusing the inverse. Native step words, branch identities, and historical provenance remain separately typed Path-formal information.

This is a conditional safe adapter for the actual historical R061 two-positive-generator chart and the correctly typed current `diagonal_quotient` executable; it is **not** a full X6 native identity quotient. The historical LP011 allegation of a *wrong native dominant-axis caller* remains `UNRESOLVED_PROVENANCE`, since this R061 `M=max` is a quotient-reverse decoder, not an evidenced singleton native argmax selector. The historical LP019 alleged *positive N-BRC signed-subtraction caller* likewise remains unlocated; the correct R062 natural-positive tower is not that error.

## Actual bounded original-module execution and reproducibility

Read the current executable `src/enterprise_math/diagonal_quotient.py` (Git blob SHA1 `a527e347e33d0a0039258a9b25f48b1f1466d149`) and independently assembled byte-identical pinned source; Git blob comparison **matched exactly**. Imported that exact module, executing its original `canonical_min_zero`, `is_canonical_min_zero`, `diagonal_chart`, `inverse_canonical` and `compose_canonical` functions, checked against direct signed-integer reconstruction and factorial BRC oracle.

Executed all 3 choices of anchored selected axis, every signed free pair `[-12,12]^2`: **1,875** states, 1,875 native inverses and BRC reversal checks; all 7 affine pins `c=-3..3`: **13,125** additional anchored reconstruction checks; every pair of free coordinates in `[-4,4]^2` for two operands across 3 axis pins: **19,683** native composition checks. No mismatch. CPython ordinary, `-O`, `-OO` outputs are byte-identical; machine JSON stdout SHA256 `fd4c7814fedefe27a136243bf918a6eee34ea2f0838a23b29782b979cad5a9fa`.

Reproduction: run `python3 research_checks/X6_UNIT76_ANCHORED_MINZERO_NATIVE_BRC_CHECK_20261117.py --source src/enterprise_math/diagonal_quotient.py`, repeating under Python `-O` and `-OO`. The script verifies the source Git blob before executing it. The declared tests cover the bounded integer domain; the proposition above is an all-integer proof.

## Consumer and mother-task disposition

- `LP003/005/011/019/023/026`: `PRESERVE_OBSERVER + CONDITIONAL_PINNED_TWO_AXIS_NATIVE_LIFT`. R061 original inverse is typed at observer level, and its native signed two-axis reconstruction is exact when third coordinate value and selected axes are declared.
- `src/enterprise_math/diagonal_quotient.py`: `KEEP` — its docstring already states representation-only use, and the author-executed exact tests verify the conditional algebra. No arbitrary implementation patch or revision of another owner.
- `LP011/LP019` historical alleged wrong-call identities: `UNRESOLVED_PROVENANCE`, not closed by a mathematical adapter or a keyword hit. Original archive claim objects have no `source_path`/line fields. The specific positive/min-zero reversal source is classified, not mislabeled as a native argmax bug.
- Required remaining work: exact historical wrong-call source:line if it exists; other current 28-LP downstream source edges; independent Driver `REQUEST_REVISION` and native Source semantic receipt. Original R063/Helly experiments remain completed and not repeated.

Evidence class: `AUTHOR-PROVED / ORIGINAL-CURRENT-MODULE-EXECUTED / FINITE-EXHAUSTIVE-SCOPED / UNREVIEWED / NOT_ADMITTED`.
