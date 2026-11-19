# X6 Unit161 — Frozen P022 growth consumer versus native signed-X6 shortest-path mass

**Date:** 2026-11-19. **Task:** RS-X6-LEGACY-PLANE-RECONCILIATION / publication TP2-B4A441B23DA3159232C2. **Research lane:** chatgpt-research-onhour-enterprise-math-20260923. **Author:** EM-X6-FB6990; existing session MCP-082892eb480e45dea6d4b9fcc0491034. **Scientific input:** 59538f585d037d09ef687b28715c4bc1a3f9fe03. **Historical comparison:** fd2bcff10ca6e147348b6c1236027fc0d2877df3. **Status:** AUTHOR_PROVED / EXACT_BIGINT_EXECUTED / GITHUB_AUTHOR_EVIDENCE / UNREVIEWED / NOT_ADMITTED.

## Actual frozen implementation-to-test consumer

At the historical comparison pin, `src/enterprise_math/p022_barlow_growth.py` (blob `4185cafdb3e4ad4f55c58ff111747013e710af43`) defines `barlow_layer_shell_total_geodesic_paths` beginning at line 75, `barlow_shell_total_geodesic_paths_closed` beginning at line 116, and `growth_constant_integer_equation` at line 159. Its frozen direct consumer `tests/test_p022_barlow_growth.py` (blob `8e8418a87a1fbbdad9ba5ff03cbe532af0f6f224`) imports these at lines 3–13 and validates the P022 layer formula against the Barlow graph's **own** endpoint geodesic sum at lines 26–53, plus FCC/HCP specializations at lines 56–63 and the period-growth equation at lines 66–87. The helper `src/enterprise_math/p022_barlow_stacking.py` (blob `cfa12c17671692d1fe0371b7d80e4cc019fbcf54`) defines graph neighbours at lines 75ff., effective vertical signs at 114ff., and the endpoint shortest path calculation at 188ff.

This is a **real frozen production-function → test-consumer edge**. The consumer tests a derived periodic Barlow contact graph, not a native six-axis Cell graph, and no verified actual source call at these locations converts its path count to the native X6 N-BRC. This ledger entry records a correct typed consumer, not an invented LP011/LP019 bug.

The active scientific-input source `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` at 59538f585d037d09ef687b28715c4bc1a3f9fe03 fixes signed primitive adjacency in six axes and exact shortest-path N-BRC multiplicity in §§3 and 10. This mathematical population is separate from both P022 triangular-layer coordinate carriers and final six-nonnegative-field Cell addresses. P000's Enterprise 120° orthogonality and the selected three-dimensional slice are unchanged.

## Exact native signed-X6 path-mass theorem and comparison

Let `M_6(r)` count **all ordered primitive signed-axis geodesics of length r from one chosen Cell**, counted with their endpoint/source multiplicities, in the six-axis signed spatial Cell torsor. A primitive path is shortest iff it never uses both +e_i and -e_i for the same axis i: an opposite pair would cancel and shorten it by two; conversely a word with one sign choice per used axis has length equal to its endpoint L1 displacement.

For r≥0 and S(r,j) the ordinary Stirling number of the second kind, with S(0,0)=1,

\[
\boxed{M_6(r)=\sum_{j=0}^{\min(6,r)}\binom6j\,2^j\,j!\,S(r,j)
=\sum_{k=0}^{6}(-1)^{6-k}\binom6k 2^k k^r.}
\]

For r=0 interpret 0^0=1 in the finite inclusion-exclusion sum. **Proof:** choose j distinct axes, choose one of their two signs on each, and arrange the r labeled steps so every chosen axis occurs at least once. The surjection count is j!S(r,j). Inclusion-exclusion over omitted chosen coordinates gives the second expression exactly. The leading exponential term is 64·6^r; all remaining bases are ≤5, so `lim_{r→∞} M_6(r)^(1/r)=6`. The result is a combinatorial consequence of the signed primitive adjacency, **not** a new P000 axiom or a proof about all decorated path-state packets.

At the actual P022 derived contact-graph source, `barlow_layer_shell_total_geodesic_paths` evaluates the layer formula. For r=2 and any nonempty periodic sign pattern, the layers k=±2 contribute 3²=9 each, k=±1 contribute 2·[3·2·(1+2)-6]=24 each, and k=0 contributes 3·2²·(1+1)-6=18. Thus `M_Barlow(2)=18+48+18=84` **for every stacking pattern**, independently of period. Native X6 has `M_6(2)=12+binom(6,2)·4·2=132` and 72 distinct endpoints at signed L1 distance 2. At r=1 both models happen to give 12 geodesics; equal local degree does not imply equal second-shell BRC mass.

The source's periodic growth equation has positive root `lambda_B=2+2^((L+|D|)/(2L))≤4` for period length L, signed period drift D. Consequently the P022 Barlow shell growth and native six-axis signed shortest-path mass have **different exponential growth** (at most 4 versus exactly 6) even in cases with equal 12-regular local adjacency. This uses P022's already documented/proven periodic-growth statement at its declared derived contact-graph scope; the Unit161 independent finite certificate is not a new proof of its asymptotic formula.

## Exact certificate and comparison

The source-typed independent BigInt checker `research_checks/X6_UNIT161_P022_BARLOW_VS_X6_NATIVE_BRC_TYPED_CONSUMER_CHECK_20261119.js` was executed in the connected tool V8 isolate. For every r=0..16 it compares the integer outputs of **three independent native combinatorial implementations**: state DP keeping each axis unused/+/- with no opposite use; Stirling surjection count; and alternating inclusion-exclusion. It reconstructs the historical P022 closed-form layer mass for FCC pattern (-1,) and HCP pattern (-1,1), reporting r=0..10; it checks all 30 stacking period words of lengths 1..4 at radius 2. The canonical JSON result is `research_checks/X6_UNIT161_P022_BARLOW_VS_X6_NATIVE_BRC_TYPED_CONSUMER_RESULTS_20261119.json`. All integer checks passed; no historical P022 pytest suite or original R063/Helly benchmark was run in this unit.

| r | Native six-axis N-BRC mass | P022 FCC contact paths | P022 HCP contact paths |
|--:|--:|--:|--:|
| 0 | 1 | 1 | 1 |
| 1 | 12 | 12 | 12 |
| 2 | 132 | 84 | 84 |
| 3 | 1,332 | 420 | 384 |
| 4 | 12,372 | 1,812 | 1,524 |
| 5 | 106,452 | 7,332 | 5,592 |

A P022 graph edge, an X6 signed primitive step, and a six-nonnegative-field final Cell address are separately typed. `BRC_NATIVE` must not silently import `P022_CONTACT_PATH_COUNT`; this unit establishes an explicit real consumer boundary and a sharp low-radius witness rather than alleging a current erroneous caller.

## Task-state and provenance boundary

Reuses previously verified Unit131 full squared-norm shell/chart distinction, Unit157–158 P022 shell-count source correction, Unit160 Barlow selected-prefix fiber theorem and original Unit50 R063 benchmark PASS. The current unit compares a **different population** (L1 path-length shell and P022 whole contact shell) and a new frozen `p022_barlow_growth → test_p022_barlow_growth` consumer. It neither reruns those older experiments nor treats its derived comparison as finishing the original native benchmark. Historical alleged LP011 wrong argmax and LP019 positive-N-BRC subtraction lack exact verified `commit:path:line`; keep `UNRESOLVED_PROVENANCE`. The 28-LP complete production coverage and independent Driver review remain unfinished.

At author start, original Unit159 Native PROGRESS `onhour-20261119-1758-x6-own-unit159-native-progress-v1` is authenticated `SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED` (Source `688ee0f1f67b42419058f50cf7973e13a08f3c99`). Unit160 author evidence and Activity175 were already saved but its native semantic association was not submitted. Original same-lane continuation `onhour-20261119-1905-x6-own-current-continuation-v1` and same-run resume `onhour-20261119-1909-x6-own-run-c920-after-unit159-resume-v1` are pending at author checkpoint; consume original terminal receipts before any protected native publication. Legacy failed Unit149 request stays terminal and is not replayed.

**Next exact action:** consume original continuation/resume receipts; if same original claim RUN-c92057890282aaaeec520881 remains current and has fresh effective generation, publish one legitimate Native PROGRESS for already-saved Unit160 (and then this Unit161 evidence) without duplicate author source uploads, authenticate Source; continue remaining real 28-LP production edge audit. Preserve request/CLAIM/epoch, frozen science pin, original R063 conditions and independent reviewer boundary.
