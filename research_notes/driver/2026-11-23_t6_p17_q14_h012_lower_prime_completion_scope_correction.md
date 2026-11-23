# T6 p17 q14(7,7): full-observer lower-prime completion gap in the H012 transfer

Date: 2026-11-23 (Asia/Taipei). Review actor: original Driver `EM-DVR-DEBB5E`; own Source session `MCP-9b4714dc46b948afa4875a86c89c713c`. **Scientific scope correction, not a new canonical Review/Result, CLAIM, or task completion.**

## Audited sources and authorship

- The original q14 vertical-only roster/preflight, by `EM-EMF6D046-5A2844`, is pinned at [2026-11-16 preflight](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md) (Git blob `c49fb8099e43de1c60617ed6ed0ce1779bbde856`). It explicitly leaves `H0/lower-prime completion` open.
- The later [H012 emptiness note](https://github.com/awdawmip/enterprise-math/blob/main/research_notes/portable_direct/onhour_20261122_t6_q14_h012_exact_emptiness.md), original author `EM-X6-FB6990`, and its [exact checker](https://github.com/awdawmip/enterprise-math/blob/main/research_checks/T6_P17_Q14_H012_EXACT_EMPTY_CHECK_20261122.py) (Git blob `874a17e73adc07220bc078d59bf3ec00607b9090`) enumerate only denominators divisible by 17, namely vertical `17(17q+r)` and q0 `17j`.
- The [non-author exact H012 re-audit](https://github.com/awdawmip/enterprise-math/blob/main/research_notes/driver/2026-11-23_t6_p17_q14_h012_independent_exact_reaudit.md), by this Driver, independently reproduces 251 unordered / 333 author-oriented H0-H1 compatible **17-divisible-only** pairs and zero H2 matches. That finite finding remains correct **within its declared checked support**. The difference 251 vs 333 is explained by 82 equal-vertical-length configurations counted in two orientations.
- [Previous Driver synthesis](https://github.com/awdawmip/enterprise-math/blob/d8ddadd82ebe75bdb7b534c7d400b5e0550eacb8/research_notes/driver/2026-11-23_t6_p19_q14_frontier_evidence_reconciliation.md) proposed that if frozen plan `P` is contained in the H012 scan domain `Q`, q14 affine execution is unnecessary. **The inclusion has not been established.** The plan digest `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` is still not mapped to verified immutable plan bytes.

## Exact missing implication

Let `U` denote the signed multiset of denominators exactly once divisible by 17 in the q14 split, with each `d=17a` and `17∤a`, and let `L` denote the remaining signed multiset of denominators `b` with `17∤b` (and prime factors at most 13 in the maximal-p17 branch). Write `Δ` for plus-minus difference of sums. Define

```
R_k(U) = Σ_{d=17a in U} a^(-k)
L_k(L) = Σ_{b in L} b^(-k)
N(U), N(L) = number of terms, with multiplicity.
```

For full original observers `H_k(X)=Σ_{d in X}(1-1/d)^k`, equal `H0,H1,H2` is equivalent to equal total `S0,S1,S2`, where `S_k=Σd^{-k}`. The **correct full-system equations** are

```
ΔN(U) + ΔN(L)       = 0,
ΔR_1(U) + 17 ΔL_1(L) = 0,
ΔR_2(U) + 17² ΔL_2(L) = 0.
```

The published q14 H012 checker instead selects `ΔN(U)=0`, `ΔR_1(U)=0`, `ΔR_2(U)=0` by enumerating U-only sides and comparing their uncorrected counts and rational moments. These are **stronger conditions** and are not necessary for a global exact collision unless an additional theorem forces the L contributions to agree separately. No such forcing theorem is supplied by the inspected q14 preflight, H012 checker, or independent check.

The correct 17-adic necessary relations, since all a and b are 17-adic units, include `ΔR_1(U) ≡ 0 (mod 17)` and `ΔR_2(U) ≡ 0 (mod 17²)`, **not** exact zero. Whether mixed 17-adic constraints, the actual residual budget, and admissible lower-prime completions subsequently rule out the q14 class remains a separate exact research question.

A small explicit lower-prime illustration: two terms `[2,6]` versus `[3,3]` (denominators, corresponding exponent masses 6 versus 4) have equal counts and equal first reciprocal sums `1/2+1/6=2/3=1/3+1/3`, but different second reciprocal sums `(1/4+1/36)-(1/9+1/9)=1/18`. Thus an allowed 17-free completion can change H2 while leaving H0/H1 unchanged; it cannot be discarded from a global H012 implication. This example is **not claimed to be a full T6 collision**.

## Corrected conclusion and minimal research action

**Verified:** no U-only cancellation-normalized q14(7,7) pair satisfies simultaneous H0/H1/H2 with each U-side mass ≤2331; both exact enumerations and the original proof preserve their finite validity and original contributors.

**Not established:** no globally admissible maximal-p17 q14(7,7) collision including arbitrary 17-free lower-prime denominators. Do **not** mark the global q14 subcase empty or cancel the frozen affine/mixed-congruence investigation merely from the U-only H012 null count. Do not assert that the H012 proof is false within its U-only scope.

**Next:** locate the immutable original delegated plan bytes and identify its exact allowed lower-prime completion and mixed-moment constraints; check `P⊆Q` only after this domain audit. If L is allowed, repair the enumerator to test the genuine full-system constraints with real per-side mass and all original observer/mixed congruences, or derive a rigorously justified lower-prime elimination lemma. Reuse completed 1907 roster and exact U-only checks; preserve the live original researcher contribution/owner and any existing Source evidence. Native Review/Result acceptance, formal Task completion, and T6 parent goal completion are unchanged (not completed by this note).
