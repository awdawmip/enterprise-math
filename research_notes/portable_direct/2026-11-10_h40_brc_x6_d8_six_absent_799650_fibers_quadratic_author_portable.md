# BRC-X6 native degree-eight integer fibers: exact-six-absent-action quadratic connectivity

**2026-11-10 | AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.** Original scientific source frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native four sources `(6,7,28,29)`, signed `(+,-,-,+)`, six distinct labelled actions/source, 96 native flow ports, all nine frozen signed joint-flow roots and exactly 38 legal deterministic policies. This is independently checkable author-side evidence, not a Source-native CLAIM/Result/Driver review.

## Exact finite theorem

Let `C ∈ {0,1}^{24×38}` be the full four-source, 24-label marginal incidence matrix of these 38 **native-legal** deterministic policies; `rank_Q(C)=13`. Let `b ∈ col_Q(C)∩Z_{≥0}^{24}` have each six-coordinate source-block summing to 8, and have **exactly six zero coordinates** among its 24 labelled-action counts (all remaining 18 strictly positive). Then its degree-eight nonnegative integer fiber

```
F_8(b) = { n ∈ Z_{≥0}^{38} : C n = b, Σ_j n_j=8 }
```

is **nonempty and connected under legal pair exchanges** `e_i+e_j ↔ e_k+e_l` with `C_i+C_j=C_k+C_l`. Every exchange preserves the full 24 marginal counts and nonnegative strategy multiplicities. The underlying 38 source-native policies individually satisfy the frozen 96-port/nine-root signed joint-flow conservation. Equality of 24 observable action counts is not a claim of equality of each of the 96 internal port flows across representations.

## Independent exhaustive checks and constructive finite proof

1. **Exact rational-column-span census.** Reconstruct `C` from the full legal policy list. Its exact rational left kernel has dimension 11. Enumerate all `binom(24,6)=134,596` absent-label sets. For each, enumerate positive integer six-action compositions per source totaling 8; use the 11 independent integer left-kernel equations and two-source/two-source meet-in-the-middle to find **799,650** rational-column-span integer targets, across **2,442** feasible absent-label sets. Signatures are exact, integer and collision-free; this enumeration contains every target of the theorem domain.

2. **Independent exact integer representations.** Exhaust the `binom(45,8)=215,553,195` unordered, repetition-allowed eight-policy multisets from the 38 native legal policies. Using a 24-coordinate lossless 4-bit integer count signature (all per-coordinate counts ≤8), find exactly **41,609,812** eight-policy multisets with six missing labels and **799,650** distinct represented target vectors. The independent complete degree-eight subset-zeta/Möbius support census agrees with the multiset count. Equality of the independently enumerated rational-column-span target set size and represented target set size proves every target has a nonnegative integer representation.

3. **Full quadratic exchange graph.** All `binom(39,2)=741` unordered native policy pairs fall into **605** full-24-incidence equal-sum classes; choose anchors to construct **136** sufficient two-for-two exchanges. Exhaustive safe-pruned search finds all **41,609,812** degree-eight six-absent multiset vertices (202,308,851 recursion nodes; 125,523,629 safe prunes). Across **5,751,935** eligible six-policy complements, iterate all 136 equal-sum pair exchanges, check support is exactly six-absent and both endpoint vertices exist, and apply DSU to their lossless combinatorial-rank IDs. The exhaustive program records **181,208,844** legal edge occurrences and exactly **40,810,162** successful unions, giving **41,609,812 − 40,810,162 = 799,650** connected components. Every edge preserves the exact 24-coordinate target, so every component lies inside one target fiber. There are exactly **799,650** represented target fibers and each contains at least one component. These two finite counts match; hence each target has precisely one connected component. The explicit optimized union-only program returns `CERTIFICATE_STATUS=PASS_SIXZERO_COMPLETE_UNION_ENUMERATION`.

Class breakdown of exact-six-zero integer targets, matching the independent rational-span census:

| Missing-action profile across the four sources (sorted) | Feasible label sets | Exact rational-span = represented targets |
| --- | ---: | ---: |
| (2,2,1,1) | 1150 | 612,562 |
| (2,2,2,0) | 168 | 38,544 |
| (3,1,1,1) | 264 | 39,108 |
| (3,2,1,0) | 712 | 103,896 |
| (3,3,0,0) | 64 | 5,360 |
| (4,1,1,0) | 48 | 120 |
| (4,2,0,0) | 36 | 60 |
| **Total** | **2442** | **799,650** |

## Cumulative frontier and next exact unit

Prior verified D8 0–5 missing-label support layers have **669,627** rational-span integer targets and **60,386,146** eight-policy multisets, all represented and pair-swap connected. Including the present exact-six-zero theorem yields **1,469,277** connected nonempty D8 fibers / **101,995,958** multiset states within the **at-most-six absent labels** domain. No universal statement is made about untested support layers or arbitrary degrees.

The next smallest uncompleted unit is **D8 with exactly seven absent action labels**: complete the rational-span target census and independent integer fiber graph classification; preserve finite counterexamples and original full native signed readout if they occur. Reuse the verified 38-policy/nine-root frozen input; do not reprove existing degree 2–7 or degree-8 0–6 work.

**Reproduction materials:** exact 22-file portable archive `BRC_X6_D8_SIX_ZERO_NATIVE_FIBERS_AUTHOR_PORTABLE_20261110.zip` SHA-256 `31e62ac38ee5cd2275bbb4716d6cd59cf9a388b2a3f519db307e9540284f6254`. It contains executable `d8_six_zero_rational_span.cpp`, `d8_six_zero_target_census.cpp`, `d8_six_zero_union_only.cpp`, independent native 96-port/nine-root validator and integer left-kernel provenance, logs, exact JSON certificate and per-file SHA256 manifest. An optional slower per-vertex recheck in `d8_six_zero_connectivity.cpp` did not finish; the successful complete union-only checker plus independent target count proves the stated result. This archive is a local user-deliverable and has not been Source-native published; actual GitHub theorem content and immutable commit are independent verifiable evidence.

D25/LIFT/JT2 remains a separate lawful Source track with frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` and no author-side borrowed session, CLAIM or native result. Original UR V2 four-file bundle, if recovered, must satisfy exactly 94,687 bytes and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; previously completed UR mathematics is not repeated.
