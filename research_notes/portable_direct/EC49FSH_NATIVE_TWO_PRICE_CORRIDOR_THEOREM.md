# EC49FSH — 原生 BRC 双价格连续相图：完整矩形走廊定理

2026-11-18 (Asia/Shanghai) · AUTHOR_PROVED / EXACT_FINITE_TWO_IMPLEMENTATIONS / NOT_REVIEWED
Frozen pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
Predecessors: [EC49FSG #2682](https://github.com/awdawmip/enterprise-math/pull/2682), [EC49FSF #2681](https://github.com/awdawmip/enterprise-math/pull/2681).
Independent portable research; no formal Task/CLAIM/Result/Review authority claimed.

## 1. Model and full real-domain theorem

Retain exactly the original BRC16943: 310 raw configurations, all 141 complete named state profiles, all 228 original physically named observations, their full joint response fibers and uniform 141-state prior. Optimize over complete adaptive deterministic identifying trees. q32 and q34 each cost \((1-\alpha)t\), q140 costs \((1-z)t\), all other physical observations cost \(t>0\). Set \(F(\alpha,z)=141V(\alpha,z)/t\).

**Theorem.** For every real \(\alpha\in[5/16,1/3]\) and \(z\in[0,1]\),

\[
\boxed{ F(\alpha,z)=\min_{1\le i\le 7}(U_i-Q_i\alpha-K_i z). }
\]

Each triple \((U_i,Q_i,K_i)\) is attained by a complete original-native witness tree, with \(Q_i=N_{32}+N_{34}\), \(K_i=N_{140}\). Seven fixed-tree affine cost types are necessary and sufficient across the whole rectangle.

| i | Total U | N32 | N34 | Q | N140=K | root |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 297 | 15 | 141 | 156 | 13 | q34 |
| 2 | 299 | 21 | 141 | 162 | 15 | q34 |
| 3 | 298 | 17 | 141 | 158 | 18 | q34 |
| 4 | 300 | 17 | 141 | 158 | 30 | q34 |
| 5 | 302 | 22 | 141 | 163 | 32 | q34 |
| 6 | 302 | 4 | 141 | 145 | 50 | q34 |
| 7 | 301 | 7 | 39 | 46 | 141 | q140 |

## 2. Exact convex optimality polygons

Let \(C_i(\alpha,z)=U_i-Q_i\alpha-K_i z\). Intersect the parameter rectangle with the six half-planes \(C_i\le C_j\) for each i. Rational clipping yields seven convex polygons; vertex pairs below are \((\alpha,z)\).

| i | polygon vertices in boundary order | exact area |
|---|---|---:|
| 1 | (5/16,0), (1/3,0), (5/16,1/16) | 1/1536 |
| 2 | (1/3,0), (1/3,1/9), (5/16,1/12), (5/16,1/16) | 19/13824 |
| 3 | (1/3,1/9), (1/3,1/6), (5/16,1/6), (5/16,1/12) | 5/3456 |
| 4 | (1/3,1/6), (5/16,7/32), (5/16,1/6) | 5/9216 |
| 5 | (1/3,1/6), (1/3,1/3), (5/16,5/16), (5/16,7/32) | 25/9216 |
| 6 | (1/3,1/3), (1/3,32/91), (5/16,479/1456), (5/16,5/16) | 19/52416 |
| 7 | (1/3,32/91), (1/3,1), (5/16,1), (5/16,479/1456) | 1921/139776 |

The seven regions have nonoverlapping interiors and their exact areas sum to \(1/48=(1/3-5/16)\). There are 14 distinct polygon vertices, **all on the two edges** \(\alpha=5/16\) and \(\alpha=1/3\).

## 3. Every polygon vertex checked by two all-228-observer Bellman implementations

Both independent original-raw-data decoders and exact integer/rational Bellman routines have been run on every listed point. Last columns show their respective actually visited dynamic-programming subset counts.

| alpha | z | exact F | primary states | independent states |
|---|---|---:|---:|---:|
| 5/16 | 0 | 993/4 | 11633 | 11155 |
| 5/16 | 1/16 | 3959/16 | 11602 | 11139 |
| 5/16 | 1/12 | 1977/8 | 11601 | 11139 |
| 5/16 | 1/6 | 1965/8 | 11565 | 11097 |
| 5/16 | 7/32 | 3905/16 | 11519 | 11061 |
| 5/16 | 5/16 | 3857/16 | 11483 | 10999 |
| 5/16 | 479/1456 | 349787/1456 | 11476 | 11000 |
| 5/16 | 1 | 1165/8 | 9352 | 8224 |
| 1/3 | 0 | 245 | 11587 | 11066 |
| 1/3 | 1/9 | 730/3 | 11535 | 11029 |
| 1/3 | 1/6 | 727/3 | 11516 | 11017 |
| 1/3 | 1/3 | 237 | 11409 | 10853 |
| 1/3 | 32/91 | 64451/273 | 11385 | 10868 |
| 1/3 | 1 | 434/3 | 9054 | 7923 |

## 4. Proof for every real pair, not a parameter grid approximation

For each complete native identifying tree T, total normalized 141-path cost is affine:
\[
C_T(\alpha,z)=U(T)-\alpha(N_{32}(T)+N_{34}(T))-zN_{140}(T).
\]
All observation prices are nonnegative; deleting noninformative or repeated observations cannot increase cost. Every informative observation strictly partitions the current candidate state subset, so the Bellman recursion over strict candidate subsets, minimizing over all 228 named physical observations, exactly covers every complete adaptive identifying strategy. Therefore \(F=\min_T C_T\) is jointly concave.

For each listed polygon \(P_i\), both exact Bellman implementations certify \(F(v)=C_i(v)\) for every vertex v. Since every point inside the convex polygon is a convex combination of vertices, concavity gives \(F\ge C_i\) there. The full 141-path replayed original native witness tree i achieves \(C_i\), giving \(F\le C_i\). Thus \(F=C_i\) throughout \(P_i\). The seven polygons cover the rectangle and prove the full real-parameter theorem.

Each polygon has strictly positive area and a distinct cost gradient \((-Q_i,-K_i)\), so seven different fixed-tree affine costs are required. The seven witness trees achieve them; every witness has worst-case depth 3.

## 5. Exact simultaneous phase collapse at alpha=1/3

On the upper parameter edge, polygon 1 meets it only at \((1/3,0)\), and polygon 4 meets it only at \((1/3,1/6)\). Consequently the slice \(\alpha=1/3\) has **five** nonempty open intervals:

| z interval | exact F(1/3,z) | N140 |
|---|---|---:|
| [0,1/9] | \(245-15z\) | 15 |
| [1/9,1/6] | \(736/3-18z\) | 18 |
| [1/6,1/3] | \(743/3-32z\) | 32 |
| [1/3,32/91] | \(761/3-50z\) | 50 |
| [32/91,1] | \(857/3-141z\) | 141 |

The vanishing boundaries are \(C_1=C_2\Rightarrow z=1-3\alpha\) at \((1/3,0)\), and \(C_4=C_5\Rightarrow z=1-5\alpha/2\) at \((1/3,1/6)\). Prior exact slices have seven phases at \(\alpha=5/16\) and eight at \(\alpha=3/8\), so phase count is **not monotonically increasing** across these rational slices.

## 6. Reproduction and scope

Accompanying certificate provides all 14 exact vertices, seven rational polygons and the seven preserved native witness-tree filenames and SHA256 values. A verification script checks all 228 original physical observer response maps, replay of all 141 named state paths in each tree, two separate exact Bellman implementations at every vertex, and complete polygon area/affine-region consistency. Use the original frozen native source data in the self-contained EC49FSG evidence archive retained from the preceding research; its PR provenance is above. No scientific pin change or source replacement occurred.

This proves the finite 141-state decision problem for the stated two-parameter rectangle and uniform prior. No independent reviewer, canonical scientific admission, formalized theorem or physical calibration is claimed.

**Next science frontier**: certify the neighboring rectangle \(1/3\le\alpha\le3/8,\ 0\le z\le1\) and locate the exact additional phase births, re-entrance and any interior envelope vertices, then extend to separate discounts for q32, q34 and q140.
