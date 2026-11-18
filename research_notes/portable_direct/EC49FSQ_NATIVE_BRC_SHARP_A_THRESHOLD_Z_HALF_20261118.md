# EC49FSQ-T: Exact sharp q32/q34 price-swap transition at z=1/2

Date: 2026-11-18; original frozen BRC16943 science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Source dependency: EC49FSN PR #2706@0842017a6bfdc83e7af59c6d2be0493dd53d58da for a=1/2 boundary; EC49FSQ PR #2715 for saturation lemma, raw native data, higher-a finite exact Bellman research. Independent portable science, no formal Task CLAIM/Result/Review/Activity admission asserted.

## Theorem: an exact all-real two-phase price-axis with sharp rational transition

Let F(a,b,z)=141V(a,b,z)/t be the unrestricted optimal total deterministic adaptive identification cost across the 141 original named joint-response states, using all 228 original physically named observations (310 original configurations, uniform prior). The original q32,q34,q140 costs are (1-a)t,(1-b)t,(1-z)t, respectively, with all remaining q priced t>0.

Fix b=7/16 and z=1/2. For every real a in [1/2,1], define direct D(a)=F(a,7/16,1/2) and price-exchanged S(a)=F(7/16,a,1/2). Put

a_* = 133/246.

Then the full unrestricted original-native Bellman optimum is exactly

\[
\boxed{D(a)=
\begin{cases}
3451/16-18a,&1/2\le a\le133/246,\\
4515/16-141a,&133/246\le a\le1;
\end{cases}}
\]

\[
\boxed{S(a)=2177/8-141a,\qquad1/2\le a\le1.}
\]

Consequently the exact price-exchange cost penalty is

\[
\boxed{D(a)-S(a)=
\begin{cases}
123a-903/16,&1/2\le a\le133/246,\\
161/16,&133/246\le a\le1.
\end{cases}}
\]

At a=1/2 this difference is 81/16, at a=133/246 it is 161/16, and for all higher a it stays exactly 161/16. This is a **sharp saturation transition** for the direct-optimal cost slope: before a* the optimal slope is -18, after a* the slope is -141. The upper phase is realized by an optimal tree that uses q32 on all 141 named-profile paths.

## Exact feasible original-native tree witnesses

All witness tuples count (U,N32,N34,N140) uses across all 141 equally weighted state paths:
- Direct below threshold: (319,18,75,141), cost 3451/16 - 18a (original EC49FSN, q140-root).
- Direct above threshold: (313,141,43,24), cost 4515/16 - 141a (first observed as exact Bellman optimal at a=1,z=1/2 in EC49FSQ-H).
- Exchanged for all a: (311,10,141,69), cost 2177/8 - 141a (EC49FSN complete original-named q34-saturated tree).

The first and third full trees are original EC49FSN immutable published lossless witnesses. The second cost vector comes from original full-228 Bellman tree recovery; full lossless JSON for that new tree has not yet been separately published. Its feasibility and exact native path-use vector are certified by the primary original-source solver, and the full-tree publication remains the next evidence strengthening action.

## Exhaustive exact endpoints and independent recalc

| a | Orientation | Full native exact Bellman | Primary reached subsets | Independent original 94-family decoder | Independent reached subsets |
|---|---|---:|---:|---:|---:|
| 1/2 | Direct | 3307/16 | 10579 | 3307/16 | 9852 |
| 1/2 | Exchanged | 1613/8 | 10286 | earlier EC49FSN checks | — |
| 133/246 | Direct | 135107/656 | 10475 | 135107/656 | 9726 |
| 133/246 | Exchanged | 64253/328 | 9966 | 64253/328 | 9255 |
| 1 | Direct | 2259/16 | 6787 | 2259/16 | 5480 |
| 1 | Exchanged | 1049/8 | 6583 | 1049/8 | 5075 |

All rational values are exact, not approximated. This run independently rebuilt the original named observations from the 94-family data/CSV and matched the three nontrivial primary endpoint values at a=1/2 direct and a=133/246 both orientations, in addition to the two a=1 orientations established in EC49FSQ-H.

## Proof for every real a, not just the finite anchors

1. Every complete original-native decision tree has an affine total price cost as a function of a; hence unrestricted F is concave in a (pointwise minimum of affine functions).
2. At a=1/2, exact unrestricted Bellman D=3307/16 and the feasible unsaturated original EC49FSN tree (319,18,75,141) has exactly that cost.
3. At a*=133/246, exact unrestricted Bellman D=135107/656, and **both** feasible tree planes (319,18,75,141) and (313,141,43,24) coincide at that value:
   3451/16-18a* = 4515/16-141a* = 135107/656.
4. On the entire interval [1/2,a*], concavity and exact endpoint equality give D(a) at least the affine chord 3451/16-18a, while the fixed complete original tree attains that chord, giving equality.
5. At a*, the other globally optimal original tree uses q32 on all 141 profile paths. The saturated-observer lifting lemma therefore proves D(a)=D(a*)-141(a-a*) for **every** a∈[a*,1].
6. At a=1/2, the exchanged original tree (311,10,141,69) is globally optimal and uses q34 on all 141 paths. The same lemma gives S(a)=1613/8-141(a-1/2)=2177/8-141a for every a≥1/2.
7. Subtracting the exact formulae gives the stated two-phase price-exchange difference. Their slopes differ (123 vs 0) and the affine planes cross at the unique interior value a*=133/246. Thus this is the true sharp breakpoint for this full one-dimensional price slice.

Neither a floating-grid inference nor an assumed global simplification of the original named observation system is used.

## Status and next frontier

AUTHOR_PROVED / EXACT_PRIMARY_FINITE_EXHAUSTIVE_AT_LOAD_BEARING_VERTICES / INDEPENDENT_PARTIAL / NOT_REVIEWED. Complete original-native witness for the newly saturated phase is still to be published losslessly before advertising a full tree-replay evidence level for this new strategy.

Next: recover and publish the original solver's exact full named-response tree for (313,141,43,24), verify it distinguishes all 141 states, then extend this z=1/2 rational breakpoint across a nearby b,z rectangle; determine how the saturation boundary becomes a polyhedral surface, preserving all original joint responses.
