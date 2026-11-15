# EC49FQE — Exact all-price phase diagram for native BRC class 16943, 310-configuration prior

Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Date: 2026-11-16. This is independent portable research; no canonical Task CLAIM, Result, or external mathematical review is asserted.

## Proposition and frozen input

The scientific input is the existing frozen pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Master file SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Named-root cost CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Class 16943 has 310 legal original configurations and 141 distinct complete named-root cost profiles, 144 terminal scalar observations and 84 named-root scalar observations. The task is to identify the rooted profile under unrestricted finite-depth adaptive observations, pricing each named-root observation at `r>0` and each terminal observation at `t>0`. The 310 original configurations are equiprobable, inducing exact multiplicity weights on the profiles.

**Theorem.** For every positive real ratio `x=r/t`, the globally minimum expected cost is `(R*r+T*t)/310`, with the following complete 16-piece phase diagram:

| Ratio x | Cumulative weighted root reads R | Cumulative weighted terminal reads T |
|---|---:|---:|
| 0 < x ≤ 26/71 | 1033 | 0 |
| 26/71 ≤ x ≤ 29/57 | 962 | 26 |
| 29/57 ≤ x ≤ 31/60 | 791 | 113 |
| 31/60 ≤ x ≤ 48/83 | 731 | 144 |
| 48/83 ≤ x ≤ 3/5 | 648 | 192 |
| 3/5 ≤ x ≤ 51/83 | 638 | 198 |
| 51/83 ≤ x ≤ 2/3 | 555 | 249 |
| 2/3 ≤ x ≤ 17/24 | 549 | 253 |
| 17/24 ≤ x ≤ 8/11 | 213 | 491 |
| 8/11 ≤ x ≤ 7/9 | 202 | 499 |
| 7/9 ≤ x ≤ 11/14 | 193 | 506 |
| 11/14 ≤ x ≤ 7/8 | 179 | 517 |
| 7/8 ≤ x ≤ 33/35 | 147 | 545 |
| 33/35 ≤ x ≤ 1 | 112 | 578 |
| 1 ≤ x ≤ 3 | 5 | 685 |
| x ≥ 3 | 4 | 688 |

Adjacent policies tie exactly at the common endpoints. R and T count observations accumulated along all 310 original-configuration paths, rather than unique decision-tree nodes. The table gives exact optimal value, not a classification of all equivalent optimal trees.

## Proof

Let `S` be a non-singleton subset of the 141 rooted profiles and `W(S)` its total multiplicity among the 310 configurations. For every informative legal observation `q`, let `S_v` denote the response fiber for value v and `p(q)` the relevant positive root/terminal observation price. The exact weighted Bellman recurrence is

`C(S)=min_{q splits S} [p(q)*W(S) + sum_{v:|S_v|>1} C(S_v)]`, with `C({s})=0`.

Because each informative query strictly reduces every nonsingleton response fiber, induction on |S| proves that the recursion minimizes over *all finite adaptive identification trees*. A non-splitting query can be removed at strictly lower cost. The implementation enumerates all 228 source-grounded observations, collapsing identical response partitions only after retaining a cheapest representative. Each observation and multiplicity is an exact integer; all endpoint certificates use positive integer prices and exact integer arithmetic, not approximate numerical optimization.

**15 complete endpoint solves.** Full unrestricted Bellman values are checked at the following reduced ratios, with exact integer costs for the price pair `(a,b)`:

| r:t | Exact total weighted optimum |
|---|---:|
| 26:71 | 26858 |
| 29:57 | 29380 |
| 31:60 | 31301 |
| 48:83 | 47040 |
| 3:5 | 2904 |
| 51:83 | 48972 |
| 2:3 | 1857 |
| 17:24 | 15405 |
| 8:11 | 7105 |
| 7:9 | 5905 |
| 11:14 | 9207 |
| 7:8 | 5389 |
| 33:35 | 23926 |
| 1:1 | 690 |
| 3:1 | 700 |

At each anchor `a:b`, the exhaustive Bellman minimum equals both adjacent displayed costs `R_left*a+T_left*b=R_right*a+T_right*b`. Every row's affine line is realized by an explicit decision tree, source-level replayed against all 310 original configurations, identifying all 141 distinct profiles. The source data, complete tree certificates, generator, independent replay source and machine logs are preserved in the accompanying `EC49FQE_CONFIG_PRICE_FULL` evidence archive; seven new exact breakpoint computations include 29/57, 31/60, 48/83, 51/83, 17/24, 8/11 and 11/14. The other endpoints reuse EC49FQB, EC49FQC, EC49FQD source certificates at unchanged frozen pins.

**Between endpoints.** With terminal price normalized to one, the optimal function `f(x)=inf_π(R_π*x+T_π)` is concave (infimum of affine functions). If the same feasible tree line L touches f at consecutive endpoints a,b, then concavity gives `f(x)≥L(x)` for a≤x≤b, while feasibility gives `f(x)≤L(x)`. Therefore equality holds for *every real x* in the interval, completing all 14 bounded interior pieces.

**Low-price tail.** At x₀=26/71, the Bellman result equals the pure-root cost `1033*x₀`. For 0<x<x₀, any policy costs at least x/x₀ times its cost at x₀ because root prices scale by this factor and terminal prices remain positive at 1. Hence `f(x)≥1033x`; the same pure-root strategy attains the bound.

**High-price tail.** Exact terminal-signature enumeration yields 139 response-signature fibers for 141 rooted profiles, consisting of two nontrivial two-profile fibers and all remaining singletons. Their four original configurations (17928, 38165, 24541, 38166) each have multiplicity one. Every successful identifying tree must use a root observation on each such configuration's path; any terminal-only path would be unable to separate the corresponding pair. Thus *all* identifying trees have at least four weighted root reads. At x=3 Bellman optimum is 700, attained by the tree (R,T)=(4,688). For all x≥3, `f(x)≥f(3)+4(x-3)=4x+688`, and the same tree attains equality.

Consequently the 16 intervals above exhaust all positive real prices, with **15 exact phase-transition ratios**.

## Verification and provenance

Exact integer solver: `EC49FQA_MIXED_PRICE_OPTIMUM.py`; independent 310-configuration source-level validator: `EC49FQA_INDEPENDENT_REPLAY.py`; terminal-invisible fiber enumerator: `EC49FQC_TERMINAL_FIBERS.py`. A new exact rational checker `EC49FQE_PHASE_CHECK.py` validates all 15 certificate endpoints, consistent neighboring lines, source pins, and feasible witnesses. Independent replay returns `EC49FQA_ALL_INDEPENDENT_REPLAYS_PASS`; fiber enumeration returns `TERMINAL_FIBERS_VERIFIED 139`; endpoint/phase audit returns `EC49FQE_ALL_15_ENDPOINTS_AND_16_PHASES_PASS`. The phase checker audits saved certificates; reproducing every global Bellman lower bound requires rerunning the supplied exhaustive solver at each of the 15 ratios. No independent scientific reviewer has adjudicated the theorem.

The prior partial results are preserved in the repository's EC49FQB PR #2515, EC49FQC PR #2518, EC49FQD PR #2521; the complete new evidence archive contains the original SHA256-pinned master/CSV, 15 full tree certificates, original optimizer code, two independent source-replay checkers, logs and a per-file SHA256 manifest. The frozen source input has *not* been repinned by updated control documentation.

## Next research unit and state

This completes the **310-configuration multiplicity prior** that remained open after EC49FQD (which completed the *different* 141-profile uniform prior). Next investigate exact classification of tied optimal first observations and optimal trees at critical prices; nonuniform priors; price-dependent action subclasses; and transfer of residual invisibility beyond native class 16943. The exact control read for `RS-EC49AS` on 2026-11-15 18:34:53 UTC yielded `NO_CANONICAL_PUBLICATION_DIRECTORY`, so this portable scientific artifact claims no formal Task ownership, CLAIM, Result or review.
