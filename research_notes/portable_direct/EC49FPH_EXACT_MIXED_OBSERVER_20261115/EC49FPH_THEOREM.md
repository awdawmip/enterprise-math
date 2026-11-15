# EC49FPH — Exact four-probe mixed-observer minimum in native BRC root-domain 16943

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is independent portable research; no formal Task/CLAIM/Result or independent mathematical review is asserted.

## Fixed scientific input and operator

Freeze the original native BRC evidence at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, original corpus SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. The exact root-cost table in the prior EC49FPG evidence has SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f` and comes from the original named-byte-root Trie operator, not a collapsed or relabeled model. Source: [EC49FPG PR #2472](https://github.com/awdawmip/enterprise-math/pull/2472) and its companion complete evidence archive `EC49FPG_TWO_DOMAINS_GAUGE_EVIDENCE_20261115.tar.xz`.

For configuration K, named root r in {03,05,06,07}, and allowed optional demand subset S, let P_K(r,S) be the exact minimum native Trie-prefix coverage cost for all mandatory r-demands plus S. A legal complete allocation q assigns each optional label to one eligible named root; T_K(q) = sum_r P_K(r,S_r(q)). Named roots, demands and byte provenance remain distinct.

Fix the **entire original legal-root-domain class containing configuration 16943**, not a sample: 310 original configurations, 141 distinct rooted P-vectors and 139 distinct terminal T-vectors. Its six optional labels are 5,7,15,17,19,21. There are 144 legal full allocations and 84 reachable individual (named-root, optional-subset) cost coordinates.

A primitive scalar query is either (i) one complete allocation terminal integer T_K(q) from the 144 possibilities, or (ii) one exact named-root/subset cost integer P_K(r,S) from the 84 possibilities. **Query choices are fixed in advance** and the aim is to distinguish all 141 rooted P-profiles using the minimum number of these exact scalar queries.

## Theorem — exact minimum is four

In this fixed native BRC class, the minimum number of *fixed* primitive scalar queries drawn from the entire 228-query menu is exactly **4**. An optimal explicit tuple is:

- complete allocation T(34),
- complete allocation T(36),
- complete allocation T(66),
- root-05 mandatory baseline P(05, empty optional subset).

The 0-based allocation index is taken with optional labels ordered 5,7,15,17,19,21 and eligible named roots ascending. Exact selected allocation maps:

| index | label 5 | label 7 | label 15 | label 17 | label 19 | label 21 |
|---|---|---|---|---|---|---|
| 34 | 05 | 06 | 07 | 07 | 07 | 06 |
| 36 | 05 | 07 | 05 | 06 | 03 | 03 |
| 66 | 05 | 07 | 07 | 07 | 05 | 03 |

The selected four-dimensional integer response tuple takes 141 distinct values over the 141 rooted profiles, proving the upper bound. In particular, this improves the EC49FPG exhibited five-number tuple of four terminal queries plus one root baseline; the new result has three terminal queries plus one root baseline.

### Exhaustive lower-bound certificate

Enumerate every unordered pair of the 141 distinct rooted states: C(141,2)=9,870. For a candidate query Q define E(Q) to be the 9,870-bit integer with bit i set precisely when the i-th rooted-state pair yields identical exact integer responses to Q. The complete 144 terminal +84 named-root menu produces **228** masks, with **209 distinct masks**. Equality after a fixed collection of queries is exactly the bitwise intersection of their masks.

Every single query mask is nonzero, and none of C(209,2)=21,736 distinct-mask pairs has zero intersection. These pairs produce **19,622 distinct nonzero intersection masks**. For **all 19,622** two-query residual masks R and **all 209** possible third query masks E, exact integer bitwise evaluation yields `R & E != 0`. This is **4,100,998** checked mask intersections. Hence every choice of at most three fixed scalar queries leaves a rooted pair observationally indistinguishable. The four-query upper construction proves minimality.

For comparison, the 139 distinct terminal T-profiles require exactly four *terminal-only* fixed queries: 144 terminal masks yield 10,153 distinct pair intersections, all overlapping every third terminal mask, while indices 64,140,72,31 separate all 139 profiles. The 141 rooted states cannot be fully separated using any number of terminal-only queries because the two known nonzero gauge pairs (17928,38165) and (24541,38166) are T-identical but P-distinct. This precise information-loss mechanism accounts for the indispensable named-root information in the four-query witness.

### Reproducibility and scope

The new standard-library Python verifier `VERIFY_EC49FPH.py` reads the **complete frozen original master and exact EC49FPG root-cost CSV**, checks both SHA256 values, reconstructs the class via all 38,169 original configuration eligibility signatures, checks all 141 rooted states and 139 terminal states, builds all 228 exact scalar query masks, and executes the full three-probe exclusion and four-probe witness tests. The underlying cost operator was already independently spot-checked against a second Python byte-prefix Trie in EC49FPG; that parent verifier was re-executed this round and returned `EC49FPG_FINITE_CHECK_PASS`. The current theorem is an exact finite combinatorial optimum *conditional on those frozen native integer root costs*. The executable script and machine certificate accompany this note.

**Continuing question:** determine the optimal *adaptive* mixed-query worst-case depth, and whether a different first named-root probe allows a three-decision adaptive strategy; the present four-query theorem is explicitly for nonadaptive fixed queries. Extend the distinction/repair method to the remaining legal-root-domain classes and investigate subset-dependent (nonconstant) invisible residual gauges.

## Provenance and operational state

Original source: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; parent exact research: [PR #2472](https://github.com/awdawmip/enterprise-math/pull/2472). The exact topic lookup `RS-EC49AS` returned `NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `15a1dc32184706aa832a48e7142f36df1cca6562` (read observation 2026-11-15T04:33:04.681515Z). This research is preserved as portable evidence without asserting a formal owner/CLAIM. Author proof and finite verification precede independent review.
