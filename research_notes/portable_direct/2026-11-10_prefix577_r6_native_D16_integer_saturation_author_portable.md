# BRC-X6: exact D=16 original-native full-positive integer saturation

**2026-11-10** · Frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` · **AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / GITHUB_AUTHOR_EVIDENCE / UNREVIEWED / NOT_ADMITTED**. This is author-side portable mathematical evidence, not a Source-issued session, winning CLAIM, formal checkpoint, Result or independent review.

## Exact new theorem (D=16)

Preserve all original 96 ports, four signed source ports (6,7,28,29), signs (+,-,-,+), six separately labelled actions per source, nine frozen roots and all 81 signed destination/full-joint-observer flow keys. Let `C∈{0,1}^{24×38}` be the complete exact incidence matrix of the 38 lawful native deterministic policies; let `W∈Z^{81×24}` be their original full-joint-observation conservation matrix.

For **every** `b∈Z_{>0}^{24}` with each source six-coordinate row sum exactly 16 and `Wb=0`, there exists `n∈Z_{≥0}^{38}` with `Cn=b` and `Σ n_j=16`. This is exact **integer saturation at denominator16**. The distinct support bound `||n||_0≤12` is a separate **currently unresolved** D16 question. In particular, this theorem alone does **not** move the already verified 13-minimal reduced-denominator lower bound `D≥16` to `D≥17`.

## Proof: one supported native column and predecessor m=9 saturation

The exact all-one strategy `J=(1,…,1)∈Z^{24}` is conserved and has 268 different six-policy perfect covers; one is policy IDs `(0,9,13,19,27,37)`. For any full-positive denominator16 `b`, let `r=b−J`. Each of four six-action histograms of `r` is nonnegative with total 10 and `Wr=0`.

The **new complete enumeration** proves that all **66,460,433** such residuals `r` have at least one supported lawful deterministic native policy `c_j`, meaning `c_j≤r` coordinatewise. Hence `r−c_j≥0`, still obeys all original 81 signed flow equations, and has total nine per source. **Reuse**, without repeating, the previously proved exact **m=9 integer saturation theorem**: every such nine-unit residual is a sum of nine lawful native deterministic columns. Thus `r` is a sum of ten lawful columns; adding any exact six-policy cover of `J` gives a 16-column representation of `b`.

The predecessor m=9 result is preserved, not recredited:
`awdawmip/enterprise-math@59b1c9a6c60ce8d198fba122148fef920501eee4:research_notes/portable_direct/2026-11-10_prefix577_r6_native_D15_12support_saturation_author_portable.md`.

## Exhaustive exact integer certificates

**Path A** reconstructs all 38 lawful columns from the frozen nine-root kernel and uses an exact 11-dimensional integer basis of the left nullspace of `C`. Here `rank(C)=13`; the full original native `W` has rank9 and adjoining three source-total differences gives exactly rank11. This left-nullspace representation is an **injective coordinate change for the equal-source-total slice**, not a change of model or an observation marginalization.

Every source has exactly `binom(15,5)=3003` ten-action histograms. Exact 2+2 matching examines the complete `3003²=9,018,009` histogram pairs on each side. Each pair's 11 signed coefficients uses a base128 integral encoding; the sum of all four port coefficients lies in [-40,40], avoiding any carry ambiguity, and the total fits a signed 128-bit integer. For every exact match, a 38-bit AND mask tests which lawful policy columns have strictly available action counts at **all four** original sources. The complete output is:

```text
PAIRS_PER_SIDE 9018009
SORT_DONE
D16_M10_BALANCED 66460433 D16_M10_UNSUPPORTED 0 MATCHED_GROUPS 12221
ONE_STEP_INTEGER_SATURATION PASS
```

**Independent Path B** avoids the nullspace computation completely: reconstruct the **81 raw signed joint-flow channels** from the nine original roots and use Python arbitrary-precision, exact signed base128 integer signatures (all complete four-port key coefficients have magnitude ≤40). Its separate 2+2 histogram join returns:

```text
native left signature classes 628595
NATIVE_81_ROOT D16 m10 native invariant residuals 66460433
NATIVE_81_ROOT_EXACT_PASS
```

**Independent rank/semantic check** constructs the original full 81×24 `W` and verifies `rank(W)=9`, `rank(C)=13`, `rank([W;source_sum_differences])=11` and `WC=0`. All three programs were rerun and passed on 2026-11-10.

A conversation-local **11-file independently extracted and SHA-256-verified reproducibility archive** contains the original frozen kernel, input generator, C++ exhaustive verifier, independent 81-key Python verifier, rank checker, executable reproduction README and exact JSON certificate: `BRC_X6_NATIVE_D16_INTEGER_SATURATION_AUTHOR_PORTABLE_20261110.zip`, SHA-256 `338771caf6f3f7ff05ca1fc9cdd9f671e3333fde13fd287dd26d3574245d9fb2`. This ZIP is **not** claimed to be published in GitHub by this Markdown-only note.

## Durable research continuation and next exact step

The prior author checkpoint `EM_H40_TASK_RESEARCH_R11_PORTABLE_20261108@revision61` already recorded all D≤15 results, including D15 **12-distinct-policy** upper bound; do not reprove or recredit them. The **new** immutable scientific unit is D16's 66,460,433 fully enumerated conserved ten-unit residuals and zero non-supported residuals, giving D16 integer saturation.

**Next local scientific unit:** D16 (m=10) **distinct-policy support≤12**. Analyze how a ten-policy residual multiset and the 268 six-policy covers of J can be recombined, then completely enumerate any exceptional sets or build a real 13-minimal 16-denominator counterexample with full 38-column separation certificates. Neither an arbitrary 16-term integer decomposition nor a selected 13-column linear basis establishes the result.

The native Source D25/LIFT/JT2 mother objective remains open; fresh source continuation was read as `SUCCEEDED` without execution authority and `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. The true Original-class H0/B0, `[X]U mod p²`, Frobenius/eta/kappa remain not performed. UR V2 four-file original is still awaiting its authentic `94687` bytes and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; do not repeat already completed UR mathematical proof. Current evidence remains **UNREVIEWED / NOT_ADMITTED**.
