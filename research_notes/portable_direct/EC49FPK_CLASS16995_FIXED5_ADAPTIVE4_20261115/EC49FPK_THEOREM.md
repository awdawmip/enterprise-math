# EC49FPK — Exact fixed and adaptive terminal-observation minima in original native BRC class 16995

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Exact source, model and domain

Scientific source remains pinned at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The frozen original source SHA256 is `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; the 49,272-row rooted-cost CSV from EC49FPG has SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. See [EC49FPG PR #2472](https://github.com/awdawmip/enterprise-math/pull/2472). Original signed/named byte-prefix Trie cost semantics, labels and source branches are unchanged.

The **complete** original eligible-root-domain class containing configuration 16995 consists of 242 source configurations, 112 distinct reachable named-root cost vectors and 324 legal complete terminal allocations. For source configuration K, named root r and allowed subset S, let P_K(r,S) be the original exact integer minimum prefix-cover cost. For each legal complete allocation q, observe the exact integer `T_K(q)=Σ_r P_K(r,S_r(q))`. All 112 rooted profiles also induce distinct full terminal profiles.

Allocation indices are zero based, with optional demand labels increasing and each label's legal root choices increasing in the order 03,05,06,07. A fixed observer chooses all allocations before seeing responses; an adaptive observer may choose each later allocation from previously observed exact integer responses. Scalar observations have unit cost; adaptive depth is worst case across all 112 rooted profiles.

## Theorem 1 — fixed terminal-query minimum = 5

Five terminal queries with exact indices **(44,167,290,297,312)** distinguish all 112 profiles.

For the lower bound, consider four source-configuration witness pairs:

| Pair | Number of distinguishing complete terminal queries |
|---|---:|
| (17148,37956) | 16 |
| (17148,37996) | 36 |
| (17380,19343) | 36 |
| (16995,17380) | 54 |

Their four sets of distinguishing query indices are **pairwise disjoint**. Therefore any putative four-query separator must choose precisely one query from each set. There are exactly **16×36×36×54=1,119,744** possible four-query combinations of this forced form. An exhaustive exact-integer verifier checks each candidate against every one of the 6,216 unordered pairs of rooted profiles; **at least two distinct profile pairs remain indistinguishable for every candidate**. This proves that no four-query separator exists. The five-index construction supplies the matching upper bound.

## Theorem 2 — adaptive worst-case depth minimum = 4

For every one of the **324 first queries**, at least one non-singleton exact-response fiber admits no adaptive depth-two suffix using the 324 allowed queries. This is checked by enumerating each prospective second query and, for each second-response fiber, all potential third queries. Consequently no adaptive depth-three tree separates all 112 profiles.

For the upper bound, choose initial query **4** and construct an exact response-dependent tree of depth at most four. The verifier emits the entire tree and follows the exact query/response history for all 112 rooted profiles. They terminate at 112 distinct leaves, with leaf-depth histogram **3,33,43,33** for depths 1,2,3,4, respectively. Thus

```
m_fixed(16995) = 5
d_adaptive(16995) = 4
```

## Reproduction and evidence

The accompanying Python verifier starts from the predecessor's complete exact native BRC-rooted cost and frozen-source checks. Its new sections use only exact Python integers, bitmasks, exhaustive finite combinations and memoized response fibers; no floating-point comparison, probabilistic sampling or solver-relaxation optimality claim. The local verification of both the original class/cost witnesses and the two new optima passed (`EC49FPK_OPTIMA_PASS`, 2026-11-15).

The full original input, rooted-cost table, C++17 native exporter, runnable verifier, complete adaptive decision-tree output, certificate, execution log and SHA256 manifest are preserved in the user-facing evidence archive `EC49FPK_CLASS16995_FIXED5_ADAPTIVE4_EVIDENCE_20261115.tar.xz`, SHA256 `2289bacb28d285b02036af5898f66104f85e314524a33b57990bc2d79cb897e7`. It is a conversation attachment, not claimed to reside in this GitHub commit. This GitHub PR preserves the theorem and reproducible source code.

Scope is the original finite native BRC cost observer, not an assertion about physical-time dynamics. Independent mathematical review and any formal Task/CLAIM/Result status are separate from the author-side finite certificate.

**Next research questions:** minimum expected number of queries under a declared prior (with no imposed maximum depth), heterogeneous costs of terminal versus named-root measurements, and subset-dependent terminal-invisible root gauges in further complete eligible-root classes.
