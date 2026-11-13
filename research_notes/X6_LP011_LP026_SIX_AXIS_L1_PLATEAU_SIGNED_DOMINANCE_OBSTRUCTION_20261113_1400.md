# LP011 / LP026 — full six-axis L1 median plateau defeats a three-axis one-bit native lift

Date: 2026-11-13, on-hour TASK_RESEARCH; parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`, author-side existing researcher `EM-X6-FB6990`, Source session `MCP-082892eb480e45dea6d4b9fcc0491034`. **NONBLIND / AUTHOR-PROVED / EXECUTED STANDALONE EXACT CHECK / UNREVIEWED / NOT_ADMITTED**. No independent admission or new native semantic PROGRESS claimed.

## Frozen science and relevant earlier result

Use the fixed P000 V5 X6 signed spatial Cell torsor `Z^6`, its component norm `G(z)=sum z_i²`, native signed shortest-axis BRC multiplicity `B(z)=T(z)!/prod |z_i|!`, `T(z)=sum |z_i|`, and joint min-zero observer `rho(z)=z-min(z)D`, `D=(1,1,1,1,1,1)`. Frozen native foundation source `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical reference `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Source locations are distinct from active behavioral norms.

Consume the existing selected **three-axis** exact median-sign length recovery `research_checks/X6_LP011_SIGNED_MEDIAN_BIT_LENGTH_RECOVERY_20261112.py` (current observed Git blob `6cf4cc629e05f0c20465bfd691ffd488239d433a`) as previously completed scope. The following new theorem concerns **six** native axes. It tests whether the three-axis information repair extends to the whole X6.

## Exact general theorem: integer depth minimizers of six-axis signed L1

Let `r=(r1,...,r6)` be any nonnegative integer vector with `min(r)=0`, and let `s1<=s2<=...<=s6` be its sorted coordinates. Every native lift of this relative observer is uniquely `z(h)=r+hD`, `h in Z`. Its signed shortest-axis path length is

`T_r(h)=sum_{i=1}^6 |h+r_i|`.

The **complete integer minimizer interval** is

`argmin_{h in Z} T_r(h) = {h in Z: -s4 <= h <= -s3}`.

The common minimum is `s4+s5+s6-s1-s2-s3`. Proof: `T_r` is a convex piecewise-linear function, with changes of slope at `-s_i`; its subgradient contains zero exactly between the third and fourth ordered breakpoints. Throughout that interval, the first three terms have nonpositive signed offsets and last three nonnegative ones, so their sum equals the stated expression. Outside it, moving toward the interval strictly decreases the sum. Integer endpoints are exact because all `s_i` are integers.

Therefore `rho` and `T` alone can leave `s4-s3+1` distinct native depth values even at **minimum** path length. In particular, no fixed number of extra bits can recover the native Cell from `(rho,T)` uniformly over all such r: an injective depth register needs at least `ceil(log2(s4-s3+1))` bits on that fiber. This is a lower bound on recovery information, not an assertion of the cost of a particular implementation.

## Unbounded exact family, and BRC / norm / median-sign collision

For any integer `M>=1`, take `r=(0,0,0,M,M,M)`. Every `k=0,...,M` yields a distinct native Cell displacement

`z_k=(-k,-k,-k,M-k,M-k,M-k)`

with the same `rho(z_k)=r` and the same shortest length `T(z_k)=3M`. Moreover

`G(z_k)=3[k²+(M-k)²]` and
`B(z_k)=(3M)!/[k!³ (M-k)!³]`.

Thus `G(z_k)=G(z_{M-k})` and `B(z_k)=B(z_{M-k})`. For interior indices `1<=k<=M-1`, the two central order statistics of `z_k` have signs `(-,+)`, independent of k. For `1<=k<M/2`, native dominant signed axes are `{(+e4),(+e5),(+e6)}`; their mirror `z_{M-k}` instead has dominant axes `{(-e1),(-e2),(-e3)}`. For even M and k=M/2 the six signed axes tie in absolute magnitude.

**Small explicit collision (M=3):**
- `x=(-1,-1,-1,2,2,2)`; `y=(-2,-2,-2,1,1,1)`, with `x!=y`.
- Both have `rho=(0,0,0,3,3,3)`, `T=9`, `G=15`, `B=45360`, and both middle-coordinate sign bits `(-,+)`.
- Yet `Dom_signed(x)={(4,+),(5,+),(6,+)}` and `Dom_signed(y)={(1,-),(2,-),(3,-)}` (one-based native axis labels).

This is a counterexample to reconstructing **full six-axis signed LP011 dominance** from `(rho,T,G,B,sign(median_low),sign(median_high))` without additional depth/orientation information. It does not contradict the existing **selected three-axis** theorem: in three dimensions, the L1 median minimizer has no even-dimensional flat interval.

## Actual executed exact finite checker

New original author-side executable: `research_checks/X6_LP011_LP026_SIX_AXIS_L1_PLATEAU_AND_DOMINANCE_COUNTEREXAMPLE_20261113_1400.py`, immutable commit `5227b475943dc8b38c7225359a6cbc7bdffe3a11`, observed Git blob SHA-1 `24e5fd33306154f7c1b7246be7d4018ca4b080a0`, byte-identical to the locally executed 2,984-byte Python source, local SHA-256 `ace340a48612fa1c4a031da7203ab69cf2b538a8a4fc3a78a60b77e3f3d2899c`.

Local command `python X6_LP011_LP026_SIX_AXIS_L1_PLATEAU_AND_DOMINANCE_COUNTEREXAMPLE_20261113_1400.py` exited 0 and returned `PASS_X6_LP011_LP026_SIX_AXIS_L1_MEDIAN_PLATEAU`. Exhaustive scope: all 665 min-zero `r in {0,1,2}^6`, each with 13 integers `h in [-6,6]` (**8,645 exact length/profile comparisons**); 280 non-singleton minimizer profiles and 580 total minimal lifts within those profiles. Separately, 90 explicit family lifts `M=1..12` checked native `rho,T,G,B`, including the concrete signed-dominance collision. All arithmetic is exact integer / factorial, no floating point.

The algebraic proof is for all `r in N^6` and `M>=1`. Finite regression verifies its implementation on the stated finite domains. This checker is an author-side **standalone proof regression**, not a new execution of the earlier original Cover/BRC benchmark, not a new physical triadic event law, and not an independent Driver review.

## Downstream LP action and exact continuation

- **LP011**: do not transplant the selected three-axis `(rho,L1,median-sign)` recovery to the full X6 by claiming a uniformly one-bit native signed-dominance decoder. A current caller must retain depth `h`, or enough genuinely proven information for its target `Dom_signed`. The witness above discriminates the layers directly.
- **LP026 / LP003 / LP005**: the full `(rho,h)` native lift remains lossless. A finite-horizon register or sharp streaming capacity may still be exact under its own horizon, as already established by the separate Driver source-import checks; this theorem does not invalidate them.
- **LP019 / BRC**: shortest-path BRC mass is symmetric on this two-lift collision and cannot function as an orientation witness; preserve native signed axis labels and, where required, the actual path provenance.
- No current production consumer is alleged broken from this theorem alone. Historical LP011 and LP019 purported wrong-caller provenance remains `UNRESOLVED_PROVENANCE`; existing 30 bounded current-executable audits and their judgments are retained, not repeated.

**Highest existing immutable frontier:** earlier Source cover regression 516299 PASS, signed LP026 integration and depth register PASS, 30 bounded current consumers and 23 historical definitions inspected, 28-row crosswalk. The remaining mother target is exact active downstream dependency coverage and historical wrong-caller attribution (or a clearly bounded unresolved class), then independent Driver `REQUEST_REVISION` reconciliation.

**Next exact action:** identify real active consumers (particularly a six-axis native dominant selector or quotient-to-native BRC decoder) that might infer signed dominance from `rho,T` or selected-median bits; compare actual code against the `M=3` collision. If incorrect, patch that precise consumer and run its original source regression. If correct, record a line-specific KEEP and continue the declared source corpus.

**Execution custody:** known original researcher `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`, original winning CLAIM `MCP-bdd4acf9d96a8f1f0dfab4e9`, original RUN `RUN-756de85b94c23b46b181f7b8`; latest historical resume `onhour-20261113-1259-own-x6-resume-v1` SUCCEEDED at generation 2/revision 1. Fresh canonical continuation read `onhour-20261113-1408-x6-current-continuation` was QUEUED at writing; do not treat historical RUN pointer as fresh execution authorization. No native semantic PROGRESS for this new proof is asserted. All pending operations must be reconciled by their original IDs.
