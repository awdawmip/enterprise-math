# EC49FSK — Full continuous nine-region native BRC price corridor

Date: 2026-11-18. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Inherited sources: EC49FSJ PR #2691 @ `54324197c6566c5e3ac17b530b0b744f2b473400`, and current EC49FSK 15/32 slice in this branch.

## Exact theorem

Keep the original BRC16943 instance: 141 distinct named profiles, 310 original configurations and all 228 named physical observations, with their full joint source response vectors. The prior is uniform. A legal strategy is a finite complete adaptive deterministic identification tree, with no observation repeated along a state path.

For two real discounts \(\alpha\in[7/16,15/32]\) and \(z\in[0,1]\), the prices are \((1-\alpha)t\) for q32 and q34, \((1-z)t\) for q140, and \(t>0\) for all other named observations. Write \(F(\alpha,z)=141V(\alpha,z)/t\) for the global minimum expected identification cost.

**For every real \((\alpha,z)\) in this closed rectangle,**

\[
\boxed{\displaystyle
F(\alpha,z)=\min_{(U,Q,K)\in\mathcal P}\{U-Q\alpha-Kz\}
}
\]

where the complete minimal **nine-type** menu is

\[
\begin{aligned}
\mathcal P=\{&
(303,173,17),\;(304,169,32),\;(305,173,29),\\
&(306,182,10),\;(308,182,22),\;(309,169,46),\\
&(311,151,69),\;(311,169,51),\;(319,93,141)\}.
\end{aligned}
\]

Here \(U\) is the sum of observation counts over all 141 input paths; \(Q=N_{32}+N_{34}\) and \(K=N_{140}\). Each type has a losslessly retained *complete original named-observer tree* correctly distinguishing all 141 profiles. All trees have depth at most 4.

There are nine strict positive-area convex optimal strategy regions. The nine exact region areas, in the same order, are:

| (U,Q,K) | exact area | Root |
|---|---:|---:|
| (303,173,17) | 121/290304 | q34 |
| (304,169,32) | 29/10752 | q34 |
| (305,173,29) | 3755/1161216 | q34 |
| (306,182,10) | 1391/290304 | q34 |
| (308,182,22) | 25/1161216 | q34 |
| (309,169,46) | 3/2240 | q34 |
| (311,151,69) | 53/73728 | q34 |
| (311,169,51) | 17/10240 | q34 |
| (319,93,141) | 1207/73728 | q140 |

These areas sum *exactly* to \(1/32\), the rectangle area. The small previously unrecognized positive-area (308,182,22) region proves that two boundary slices alone can conceal an optimal interior strategy. Its triangle vertices are \((15/32,1/6)\), \((15/32,39/224)\) and the **new exact interior triple junction**

\[
(\alpha,z,F)=\boxed{(25/54,\;1/6,\;5942/27)}.
\]

The other 18 distinct polygon vertices lie on the two rectangle boundary lines \(\alpha=7/16\) and \(\alpha=15/32\). Exact polygon coordinates and all 19 optimum values are in `EC49FSK_2D_NINE_REGION_CERTIFICATE.json`.

## Proof and executed verification

1. From the source-pinned 141 named profiles and complete original 228 physical observations, generate the exact Bellman subset recurrence. The first solver uses integer-scaled rational prices. An independently implemented decoder of the original 94-family source obtains the same response partitions (after explicitly mapping its alternative 84-subset enumeration order) and a separately implemented Bellman recurrence.
2. The primary solver computed exact Bellman minimum costs for all **19 distinct rational polygon vertices**. The independent second decoder and Bellman solver were **actually executed for all 19 vertices** and agreed in every case. Both use the complete native named observation set. Proof/checker evidence is retained in the self-contained archive; no continuous parameter sampling is used as a substitute.
3. Nine complete native decision trees were replayed for each of the 141 original named profiles, with response-labelled paths, no repeated named observation on a path, correct unique terminal labels, and maximum depth 4. Their integer \((U,Q,K)\) count vectors agree with the nine planes above. Tree SHA256 values and lossless compressed bytes are published with the machine certificate.
4. For each of the nine planes, rational half-plane clipping against all other candidates produces a convex polygon of strict positive area. All polygon vertices were collected and deduplicated to 19 distinct points. Exact polygon-area summation gives the whole rectangle; the interiors are disjoint because they are strict optimality regions.
5. Let \(G(\alpha,z)\) be the infimum of all legal tree affine costs, a jointly concave function. Let \(L(\alpha,z)\) be the lower envelope of the nine realized tree affine costs, so \(G\le L\). Every polygon vertex satisfies \(G=L\) by exhaustive exact Bellman calculation. For a point inside a polygon, express it as a convex combination of polygon vertices: concavity gives \(G\) at least the corresponding convex combination of endpoint optimum values, equal to that polygon's affine witness cost \(L\). Hence \(G=L\) throughout the polygon and the whole rectangle. Distinct gradients on nine positive-area regions prove at least nine fixed-tree cost types are necessary; the nine witnesses show sufficiency.

## Status, provenance and next front

Research: **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED (19/19) / NOT_REVIEWED**.
This is a theorem about the finite pinned BRC observer-identification model, not a new physical heartbeat law or a change to P000, native X6, the six-dimensional spatial basis, or the source firewall. Source pin unchanged. Both witness tree carrier and exact rational vertices retain full named-observer provenance.

Current original control lookup for topic `RS-EC49AS` on current Source `b58f8fd29e81e7bb5fbdbcf3547ffc8c94fcdb42` returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY`, observed 2026-11-18 02:35:54.931649 UTC. This is independently published portable mathematics, with no new formal CLAIM, Result, Review or Activity checkpoint.

**Next scientific unit:** classify \(\alpha\in[15/32,1/2]\), \(z\in[0,1]\), using the exact α=15/32 face as the next boundary. Decide whether new interior positive-area types arise, compute the exact algebraic/rational phase junctions, and preserve source-named complete tree witnesses. Follow the actual evidence rather than presupposing a fixed phase count.
