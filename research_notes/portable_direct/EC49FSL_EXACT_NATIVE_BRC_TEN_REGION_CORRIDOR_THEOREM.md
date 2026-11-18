# EC49FSL — Ten-region exact native BRC price corridor, alpha 15/32 to 1/2

Date: 2026-11-18. Research mode: independent, portable, non-CLAIM.
Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Precursors: [EC49FSJ PR #2691](https://github.com/awdawmip/enterprise-math/pull/2691) and [EC49FSK PR #2694](https://github.com/awdawmip/enterprise-math/pull/2694), the latter certifying the nine-region rectangle alpha in [7/16,15/32].
No alteration of P000, the six native space dimensions, the three-dimensional research slice, or source-firewall assumptions.

## Exact model and theorem

The pinned finite BRC16943 identification instance has 141 distinct named full profiles, 310 source configurations and all 228 **named native physical observations** with their original joint response vectors. Prior is uniform over the 141 profiles. A legal strategy is a complete deterministic adaptive identification tree; along any full-profile path each named observation is used at most once. An observation's nominal price is t>0, except q32 and q34 both cost (1-alpha)t and q140 costs (1-z)t. Define F(alpha,z)=141 V(alpha,z)/t, where V is the globally minimum expected observation cost over all legal trees.

**Theorem.** For every real alpha in **[15/32,1/2]** and every real z in **[0,1]**,

```text
F(alpha,z) = min { U - Q*alpha - K*z : (U,Q,K) in P },

P = {
 (304,169,32), (305,173,29), (306,182,10), (308,182,22),
 (309,169,46), (311,151,69), (311,169,51), (312,186,31),
 (315,151,77), (319,93,141)
 }.
```

Here U is the total number of observations across all 141 complete profile paths, Q is the total number of q32 and q34 uses, and K is the number of q140 uses. Every member of P has a losslessly preserved, full native named-observer witness tree of depth <=4. The corresponding ten strict positive-area convex regions have distinct gradients; **ten fixed-tree affine cost types are both necessary and sufficient** on this rectangle. Boundary ties are permitted.

The following rational polygon areas, in the order of the displayed set P, sum exactly to 1/32, the rectangle area:

| (U,Q,K) | Exact positive area | Root |
|---|---|---|
| (304,169,32) | 66679/60135936 | q34 |
| (305,173,29) | 6577/2021376 | q34 |
| (306,182,10) | 1/192 | q34 |
| (308,182,22) | 37/43008 | q34 |
| (309,169,46) | 1039/799680 | q34 |
| (311,151,69) | 875/2138112 | q34 |
| (311,169,51) | 27/10240 | q34 |
| (312,186,31) | 1033/1342320 | q34 |
| (315,151,77) | 1/7424 | q34 |
| (319,93,141) | 33289/2138112 | q140 |

The two cost types `(312,186,31)` and `(315,151,77)` are new relative to EC49FSK's nine-region rectangle. The earlier `(303,173,17)` region is absent in this new right-hand rectangle; consequently its number of strict optimal regions is ten.

Three new interior *triple* strategy junctions are exactly

| (alpha,z) | F(alpha,z) | Distinct tied cost types |
|---|---|---|
| (23/47,15/47) | 9921/47 | (304,169,32); (305,173,29); (312,186,31) |
| (117/238,5/14) | 49859/238 | (304,169,32); (309,169,46); (312,186,31) |
| (14/29,1/2) | 11809/58 | (311,151,69); (315,151,77); (319,93,141) |

The right boundary alpha=1/2 retains eight nonempty one-variable phases with transition points z=1/6, 3/14, 1/4, 11/30, 2/5, 1/2, 33/64. Their exact values are in the companion JSON certificate.

## Proof (finite exact global result, continuous domain)

1. **Native response retention.** All 228 physical named observation response vectors and the full profile names are retained. The original-source independent decoder maps any alternate subset enumeration back to the same named q indices. No value-only coalescing or loss of joint response partitions occurs. For any exact rational price triple, the subset Bellman recurrence computes the *global* minimum among all admissible full identification trees on the finite 141-state domain.
2. **Witness upper bound.** Replay each of the ten complete saved witness trees against all 141 native response vectors. Each path ends in its correct unique leaf, repeats no observation and has depth <=4. Its observation counts equal the exact integer triple (U,Q,K). Thus each affine expression in P is an attainable cost, so the unknown true optimum G is pointwise bounded above by L, the minimum of those ten expressions.
3. **Exact geometry and all vertices.** Rational half-plane clipping produces the ten nonempty convex strategy polygons. Their interiors are disjoint and their areas sum to precisely 1/32. They yield exactly **21 distinct rational vertices**: nine at alpha=15/32, nine at alpha=1/2, and three strictly interior. For every vertex the exact unrestricted Bellman minimum equals L. The nine left-edge checks are inherited from the **19/19 independently crosschecked** EC49FSK PR #2694 two-dimensional certificate at immutable commit `82af57b9426076619f91ba4b67bc865df2639f68`. The remaining twelve (nine right-edge and three interior) were calculated and independently crosschecked in the new broader [7/16,1/2] exact original-source run; their receipts, complete original trees and two solver codes are preserved in the self-contained source package. Seven of the left-edge vertices were also independently recomputed in the FSL continuation. These overlap checks are not counted as additional distinct vertices.
4. **Continuous-parameter closure.** G is the pointwise infimum of costs of all full trees, each jointly affine in (alpha,z), hence G is jointly concave. Every point in a convex strategy polygon is a convex combination of its exact vertices. At those vertices G=L and L equals that polygon's witness affine cost. Concavity implies G >= L throughout that polygon; the feasible witness supplies G <= L. Hence G=L everywhere, including all real irrational parameter points and boundaries.
5. **Sharp menu minimality.** Each of the ten positive-area interiors has a unique active gradient (-Q,-K), different from every other listed gradient. Any one fixed tree determines just one affine gradient, so a globally sufficient fixed-tree cost menu requires at least ten types. The ten saved trees attain the bound.

The domain is the pinned finite named-observer identification model, not a physical time-dynamics or native 6-axis rotation theorem. Mathematical status: `AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED`. Independent reviewer/admission and formal task Result remain separate.

## Reproduction, storage and frontier

The companion `EC49FSL_TEN_REGION_MACHINE_CERTIFICATE.json` records all ten exact region polygons/areas, all 21 exact Bellman optimum vertices, their verification provenance and tree file SHA256 values. `EC49FSL_NEW_NATIVE_WITNESSES_ZLIB_BASE64.txt` contains the **two new** original named full trees in lossless compressed form; the eight prior types are inherited from `EC49FSK_NINE_WITNESS_TREES_ZLIB_BASE64.txt`. The original two native Bellman solvers, input source files and prior certificates are retained under the frozen pin and in the predecessor archives. The accompanying verifier checks the exact polygon/tree/vertex certificate, optionally rerunning all native Bellman points.

Original research topic `RS-EC49AS` has no canonical immutable task publication directory in the 2026-11-18 03:05:25 UTC native Source read at `34ac9052d5acd8cadb0ea75bf30d4fe07e346e70`. That read does not establish a live owner projection. Publication is independent portable GitHub evidence, **not** a CLAIM, formal Result, Review, Activity checkpoint or promotion.

**Next independently useful research unit:** lift equality of the q32/q34 discount prices and classify genuinely asymmetric triples (a,b,z), while retaining their named native observation usage counts. First identify whether the symmetric ten-region witness set continues to be sufficient on a certified three-parameter neighborhood and search exact off-diagonal counterexamples/extra Pareto types.
