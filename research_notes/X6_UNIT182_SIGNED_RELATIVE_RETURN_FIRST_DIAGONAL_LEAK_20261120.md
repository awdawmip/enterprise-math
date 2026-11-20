# X6 Unit182 — first exact positive-min-zero observer return leak in the signed native BRC walk

**Date:** 2026-11-20. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; **publication:** `TP2-B4A441B23DA3159232C2`; **mother:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Logical Research lane:** `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). **Frozen science:** `59538f585d037d09ef687b28715c4bc1a3f9fe03`; **historical comparison:** `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. **Status:** AUTHOR_PROVED / EXACT_INTEGER_DP_CHECKED / GITHUB_SOURCE_READBACK / UNREVIEWED / NOT_ADMITTED.

## Question and existing interfaces consumed

The frozen historical X6 V9 kernel at `research_notes/X6_BRC_C6_GRADE_AND_EXACT_MULTINOMIAL_KERNEL_V9_20260905.md` (blob `7eea4b5f9146090d16dfa6463087039666b50b3f`, §3–5) counts six **positive-only** axis words ending at a **relative** min-zero coordinate. It calls a length-`6k` relative return `(6k)!/(k!)^6`. The later frozen signed X6 V17 kernel at `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md` (blob `aa005cd62c45d7f4105632257db9186b115c5b29`, §4–5) counts **twelve signed** primitive directions at **full** integer endpoints. The promoted native spatial definition `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`, §7–11) distinguishes `Z^6` from `Z^6/Z(1,...,1)` and records the unobserved common-depth coordinate. These are typed reusable inputs, not theorem claims re-originated in this unit.

**New precise local question:** Under the already-defined min-zero map `can6`, when does a length-`M` *signed-native* path become an **observer return** without being a **full spatial return**, and how many such paths exist?

## Exact fiber theorem (all integer event lengths)

Write \(\mathbf 1=(1,1,1,1,1,1)\). For a full signed-axis endpoint \(z\in\mathbb Z^6\), let \(S_M(z)\) be the number of ordered length-\(M\) words over the twelve directions \(\pm e_i\) with net endpoint \(z\), using the frozen V17 integer formula (zero outside its parity/length support). For canonical relative endpoint \(a=\operatorname{can}_6(z)=z-\min(z)\mathbf1\), define \(R_M(a)\) by counting the same signed-native length-\(M\) words **after** reading only their relative endpoint.

Then exactly
\[
\boxed{R_M(a)=\sum_{h\in\mathbb Z} S_M(a+h\mathbf1),\qquad
 S_M(z)=[x^z]\left(\sum_{i=1}^{6}(x_i+x_i^{-1})\right)^M.}
\]
The sum is finite since \(\sum_i|a_i+h|\le M\) is necessary, and its addends count disjoint path endpoints. In particular the missing integer \(h=\min(z)\) is the necessary exact observer-fiber repair for full **spatial endpoint** recovery; ordered Path-formal branch identity remains separate.

For the relative zero observer \(\operatorname{can}_6(z)=0\), every full endpoint is exactly \(z=h\mathbf1\). Every such endpoint requires at least \(6|h|\) primitive events. Thus, for all nonnegative integers \(M<6\),
\[
\boxed{R_M(0)=S_M(0).}
\]
The same equality holds at every odd \(M\), because \(z=h\mathbf1\) has even coordinate sum, whereas every primitive event flips the parity of the total coordinate sum.

At the first possible discrepancy \(M=6\), the two **nonzero diagonal** endpoints are \(+\mathbf1\) and \(-\mathbf1\). Each has precisely \(6!=720\) shortest signed-axis path words, while the genuine full native zero-return count is \(S_6(0)=19,920\). Hence
\[
\boxed{R_6(0)=19,920+720+720=21,360,\qquad
 R_6(0)-S_6(0)=1,440.}
\]
Here the V9 positive-only `Return_6=720` counts exactly the \(+\mathbf1\) lift, **not** the signed full-spatial zero return; the negative counterpart supplies the other 720. The quantity 1,440 counts **distinct ordered signed-axis path witnesses whose nonzero full endpoints collapse to the relative zero** (720 all-positive, 720 all-negative). It is not signed/amplitude cancellation or subtraction of positive N-BRC multiplicities.

More generally, for every \(k\ge1\), the two extremal endpoints \(z=\pm k\mathbf1\) occur at length \(6k\), and each has exactly \((6k)!/(k!)^6\) shortest ordered words. Therefore
\[
\boxed{R_{6k}(0)-S_{6k}(0)
 \;\ge\;2\,\frac{(6k)!}{(k!)^6}>0.}
\]
The equality is exact for \(k=1\); for larger \(k\), additional nonzero diagonal lifts may contribute. This inequality is an exact integer count lower bound, not an approximation or a physical law.

**Proof:** The equivalence \(\operatorname{can}_6(z)=a\iff z=a+h\mathbf1\) follows directly from the minimum-normalization definition because \(\min(a)=0\). Different \(h\) correspond to different net full endpoints, and the signed-axis words partition by their endpoint, proving the sum. An event changes one coordinate by \(\pm1\), so the minimum word length to reach \(h\mathbf1\) is \(\sum_i|h|=6|h|\), and the overall endpoint coordinate-sum parity equals word-length parity. For \(M=6\), every word reaching \(\pm\mathbf1\) uses each corresponding signed direction exactly once; the six choices can be permuted in \(6!\) ways. For zero endpoint and \(M=6\), V17's all-length formula has \(K=3\); the partitions of opposite-sign pairs \((3),(2+1),(1+1+1)\) contribute respectively \(120+5,400+14,400=19,920\). The extremal lower bound follows by retaining the two nonnegative terms for \(h=\pm k\) in the exact fiber sum; their multinomial values are precisely \((6k)!/(k!)^6\). This proves all displayed statements without finite exhaustive testing.

## Independent reproducible integer execution

An independently implemented dynamic program enumerated the full six-coordinate signed-word endpoint multiset for every length `M=0..8`, then grouped by `can6`. A separate composition-of-opposite-pairs multinomial evaluator was applied both to **every full endpoint** and **every observer fiber**, giving **81,510 exact integer comparisons**, max 26,577 native endpoints at length eight, zero disagreements. At every length \(\sum_z S_M(z)=\sum_a R_M(a)=12^M\). The 6k extremal formula was separately checked for \(k=1..4\) using exact factorial arithmetic, without running the astronomical full 6k-word dynamic program.

| Events M | Full signed native return S_M(0) | Relative observer return R_M(0) | Extra hidden-diagonal witnesses |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 2 | 12 | 12 | 0 |
| 4 | 396 | 396 | 0 |
| 6 | 19,920 | 21,360 | 1,440 |
| 8 | 1,281,420 | 1,523,340 | 241,920 |

Python normal, `-O`, and `-OO` executed the same saved checker, generated identical result bytes (SHA256 `07236422223b2cc1d4fe3bd967bdee9ad121d92d85a3f7911843523c3d2c0e1e`) and used always-on raises on every load-bearing identity; `pass=true` is only author computational evidence. No native R063 regression or existing benchmark was rerun.

**Executed and Source-persisted artifacts:**

- `research_checks/X6_UNIT182_RELATIVE_SIGNED_RETURN_FIBER_CHECK_20261120.py` @ `a659bf87155b5bbeaacf65e9a5f97c91101f71b9` (Git blob `75520554cbd1469366a7d19f8a279cac98df3f95`, local executed source SHA256 `f83cce3096928c2c8e5c575788ea28dab05a5b819cfd8fcd44551c343ef4e578`).
- `research_checks/X6_UNIT182_RELATIVE_SIGNED_RETURN_FIBER_RESULTS_20261120.json` @ `1afa1aab4f4b30711fbe809fbccb47062521fa32` (Git blob `9161c63a4065f7184402e15b531a2b2a487f1e9c`, SHA256 `07236422223b2cc1d4fe3bd967bdee9ad121d92d85a3f7911843523c3d2c0e1e`).

Each was read back at its immutable commit with complete matching bytes after the GitHub Contents create.

## Source/LP relevance, exact incompletion and custody

The result supplies a **new exact link** between the frozen positive-only V9 relative-return count and signed-native V17 all-length N-BRC, with the precise common-depth lost witness count. It is not a newly discovered erroneous historical executable call: LP011's purported wrong native signed argmax and LP019's purported subtraction of positive native N-BRC remain `UNRESOLVED_PROVENANCE`. The entire previously completed Unit180 frozen 312-test census and Unit181 August60 historical corpus were **consumed**; they were not rerun. The separate supplemental 24-test source note published this same turn is a type-explaining subset of Unit180, not a second closed census and does not change 312/312.

Current original protected Research session remains historically attributed to `EM-X6-FB6990` / `MCP-082892eb480e45dea6d4b9fcc0491034`, original claim `MCP-e2bd88a10565daf08b1d46f5` and run `RUN-b2c1fe16e9806ecf043c89a0`; past generation 2 is not fresh write authorization. Most recent preserved current canonical continuation (Unit181) records last authenticated Native through Unit174, Units175–181 Native semantic association outstanding, and Units149–152 historical association unresolved. Native PROGRESS for this Unit182 requires fresh actual same-lane winning CLAIM/RUN/Source and is **NOT_SUBMITTED**. Independent Driver review remains `UNREVIEWED / NOT_ADMITTED`. Do not use the maintenance lane or borrowed Sites owner custody to publish this author's Native checkpoint.

**Next scientific discriminator:** classify which proposed future native operators factor through \(\operatorname{can}_6\) and exactly which recoverable common-depth state must be retained for step-by-step path semantics, using concrete native signed-axis events and sourced consumer signatures. Preserve named LP011/LP019 offender uncertainty and pursue exact `commit:path:line` only if a real typed misuse is found. Native evidence and review follow their distinct current contracts.
