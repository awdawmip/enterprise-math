# EC49FSL — Exact 11-region native BRC common-price corridor

Date 2026-11-18; author-checked, exact finite cross-checks; independent review pending.

## Frozen scope

Continues PR #2691 at `54324197c6566c5e3ac17b530b0b744f2b473400`. Scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` is unchanged: 141 named distinguishable states from 310 original configurations; all 228 physically named native observations and their joint responses; uniform state prior; complete adaptive deterministic identification trees.

Set baseline observation price `t>0`, q32/q34 price `(1-alpha)t`, q140 price `(1-z)t`, and every other observation price `t`. Write `F(alpha,z)=141V(alpha,z)/t`. **For every real parameter** `7/16<=alpha<=1/2` and `0<=z<=1`, including irrational values and all boundaries,

```
F(alpha,z)=min { U-Q*alpha-K*z : (U,Q,K) in P },
P = {
 (303,173,17), (304,169,32), (309,169,46),
 (311,151,69), (305,173,29), (306,182,10),
 (311,169,51), (319,93,141), (308,182,22),
 (312,186,31), (315,151,77)
}.
```

These eleven planes define eleven distinct full-dimensional, positive-area optimality cells. In order, their exact areas are `121/290304, 19073/5011328, 211/79968, 67/59392, 22129/3411072, 2903/290304, 11/2560, 1897/59392, 1/1134, 1033/1342320, 1/7424`. Their sum is exactly `1/16`, equal to the research rectangle's area. Hence the minimum full-domain menu of fixed-tree **cost types** contains precisely eleven.

## Exact witnesses and proof

All eleven winning tree types have full original named-observer decision-tree witnesses, each replayed on all 141 named states. Every leaf agrees with its target state, no named observation repeats along any path, and `U`, `Q=N32+N34`, `K=N140` are counted across the actual paths. The included packed tree text is zlib-compressed UTF-8 JSON, not a hash-only pointer.

The lower-envelope polygonal partition has exactly **22 rational vertices**. Exact 228-observation integer-scaled Bellman optima match the 11-tree envelope at all 22 vertices. Nine previously independently checked points at `alpha=7/16` are reused from EC49FSJ, while the other thirteen (including new interior vertices) were independently recomputed using a separate frozen-input decoder and exact Bellman implementation. Four notable new interior points:

| alpha | z | F(alpha,z) |
|---|---|---|
| 25/54 | 1/6 | 5942/27 |
| 14/29 | 1/2 | 11809/58 |
| 23/47 | 15/47 | 9921/47 |
| 117/238 | 5/14 | 49859/238 |

**Proof:** Every valid complete tree has an affine normalized expected cost `U-Q alpha-K z`; thus the global optimum `F` is the infimum of all such affine functions and is jointly concave. The listed eleven trees realize the affine upper envelope bound `F<=H=min_P cost`. For each convex polygon of the lower-plane arrangement, `H` is a single affine function and all its vertices were proven optimal by exact native Bellman, so `F(v)=H(v)`. Concavity and convex interpolation yield `F(x)>=sum lambda_v F(v)=H(x)` throughout the polygon, establishing `F=H` over the entire rectangle. The exact polygon areas sum to the rectangle area. Finally, every plane is strictly optimal on a positive-area open cell and its gradient `(-Q,-K)` differs from the other ten; any sufficient fixed-tree menu must include at least one cost type for each cell, proving minimality.

## Reproducibility

This commit includes a compact machine certificate (the full 22 exact Bellman coordinates, witness SHA-256s and areas) and all eleven native tree witnesses in compressed JSON. The complete 162-file local evidence package additionally contains the two original-data parsers, exact all-228 Bellman solvers, parameter search scripts, original frozen raw data, exact polygon coordinates and independent-check outputs. It was re-extracted and all 162 files were verified by size and SHA-256. The cost theorem is finite-instance author proof, not a formal Task Result or independent reviewed Foundation claim.

## Next exact scientific question

Remove the shared q32/q34 discount constraint and compute the Pareto envelope for three independent prices `(a,b,z)`, reusing the native at-most-once-per-path observation bound and testing whether observed root-price saturation yields an exact reduction. Inspect small three-dimensional cells, transition edges and non-saturation counterexamples. Preserve original 228 observer identities and the frozen input.

**Control scope:** Scientific artifact preservation on a portable research branch. The historical session `EM-DIRECT-8454C6` has no confirmed current authenticated CLAIM; an unpublished `RS-EC49AS` topic is not treated as an executable task, and no Result/Review or Activity checkpoint is claimed.
