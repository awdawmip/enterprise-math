# T6 maximal-p13 / vertical order one (0,1): exact global mixed affine exclusion

Date: 2026-11-23, Asia/Hong_Kong. Scientific author lane `chatgpt-research-onhour-enterprise-math-20260923`, original attributed Researcher `EM-X6-FB6990`, Source SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Source Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`; T6 objective remains OPEN. No new winning Task CLAIM/RUN or Native semantic PROGRESS is claimed.

Frozen scientific task: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` @ `d84bd940cfb093cdc60e569f15cad58772a51dca`, blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`. Both signed exponent shapes have side mass <=2331 and equal original \(H_0,\ldots,H_6\). Preserve integer denominators \(a=e+1\), composite identities, signs, multiplicities, valuations and all unrestricted p13-free lower-prime denominators. Apply the previously saved p13² and p13³ exact cancellation lemma solely at its author proof scope.

## Proposition and exact assumptions

For *maximal-p13 valuation-one total positive vertical order 1*, up to side exchange the sole vertical atom lies on the positive side and must have \((q,r)=(1,r)\), \(r=1,\ldots,12\), with denominator \(a=13(13+r)\in\{182,195,\ldots,325\}\) and exponent mass \(a-1\). Its signed 12-variable q0 compensation vector \(u=(u_1,\dots,u_{12})\) is constrained by globally necessary six mixed modular conditions:

\[
\sum_{t=1}^{12}u_t t^{-j}+(13+r)^{-j}\equiv0\pmod{13^j},\qquad j=1,\ldots,6.
\]

The inverse powers are calculated exactly modulo \(13^j\); p13-free atoms are permitted in the full two-sided exponent shapes but vanish under this 13-adic necessary readout. The homogeneous solution module is the complete 12D saturated integer lattice \(\Lambda_{13}\) from the separately checked p13 q0 result. For each fixed r, construct an exact integer particular vector \(u_0(r)\) by six congruence pivots; every solution is \(u=u_0(r)+\Lambda_{13}\), no restriction to a small q0 alphabet or floating tolerances.

With the exact diagonal q0 mass weights \(W=\operatorname{diag}(12,25,\ldots,155)\), the original two side mass limits imply

\[
\|Wu\|_2^2\le \bigl(2331-(13(13+r)-1)\bigr)^2+2331^2=:R_r^2.
\]

For every \(r\), \(R_r^2\le10\,056\,061<d_{\min}\), where the published exact rational Gram–Schmidt \(d_{\min}\) of the saturated weighted lattice is about \(18\,515\,039.35\). Thus every affine lattice solution inside the radius is found by exact descending Gram–Schmidt recursion with only the nearest two integers at each coefficient. The full exact Fraction computation found no terminal sphere points in any r-state. Accordingly, **there is no primitive two-sided shape of the specified q1 (0,1) valuation-one subfamily meeting even these globally necessary conditions**.

## Exact exhaustive audit

| r | Named vertical denominator | Original exponent mass | Radius squared | Exact GS nodes | Sphere leaves |
|---|---:|---:|---:|---:|---:|
| 1 | 182 | 181 | 10056061 | 5 | 0 |
| 2 | 195 | 194 | 10000330 | 5 | 0 |
| 3 | 208 | 207 | 9944937 | 2 | 0 |
| 4 | 221 | 220 | 9889882 | 6 | 0 |
| 5 | 234 | 233 | 9835165 | 6 | 0 |
| 6 | 247 | 246 | 9780786 | 8 | 0 |
| 7 | 260 | 259 | 9726745 | 2 | 0 |
| 8 | 273 | 272 | 9673042 | 2 | 0 |
| 9 | 286 | 285 | 9619677 | 6 | 0 |
| 10 | 299 | 298 | 9566650 | 3 | 0 |
| 11 | 312 | 311 | 9513961 | 4 | 0 |
| 12 | 325 | 324 | 9461610 | 2 | 0 |
| **Total** | **12 states** | | | **51** | **0** |

The actually executed local SymPy/Fraction enumerator returned exactly these twelve rows, zero terminal sphere leaves, and zero budget-valid compensations. The local full JSON certificate has SHA-256 `19973610fc6d4677ff5bbff69126511d975e17b5f2553c60279ef35fe9251ae9`. The compact reproducible checker is `research_checks/T6_P13_Q1_SPLIT0_1_GLOBAL_AFFINE_CHECK_20261123.py`; the compact published version is a derivative of the executed local code, not an independent execution. Neither GitHub publication nor author arithmetic implies nonauthor mathematical review.

The next scientific unit is maximal-p13 valuation-one total vertical order 2: splits (0,2) and unordered (1,1), with exact named side rosters, original two side caps, same complete 12D mixed congruence affine lattice and low-prime completion of survivors. Preserve q0 and q1 as two distinct new completed author units without replicating earlier p17/p19 work. Global \(T_6=2332\) remains OPEN.
