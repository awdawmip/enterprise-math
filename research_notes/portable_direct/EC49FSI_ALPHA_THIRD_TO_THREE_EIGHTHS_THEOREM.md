# EC49FSI — Exact native BRC q32/q34–q140 two-price bridge (1/3 ≤ alpha ≤ 3/8)

Research date: 2026-11-18 Asia/Shanghai. Author proof with exhaustive exact finite Bellman checks; independent 228-observer recomputation at the four new interior vertices, and at both boundary slices in inherited EC49FSH/EC49FSF. Mathematical admission: NOT_REVIEWED.

## Frozen scientific universe

Input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. BRC16943 has 310 original configurations giving 141 *distinct named joint-response profiles*. All 228 original physically named observations remain available, with complete deterministic adaptive identification trees and uniform prior on the 141 profiles. This is a finite native-observation experiment, not a claim about unrestricted Heartbeat-world dynamics.

Let t>0. Observations q32 and q34 cost (1-alpha)t each; q140 costs (1-z)t, and all others cost t. Define F(alpha,z)=141*V(alpha,z)/t, where V is the globally optimal expected identification cost.

**Theorem.** For every pair of real parameters 1/3 ≤ alpha ≤ 3/8 and 0 ≤ z ≤ 1,

F(alpha,z) = min over the following eleven triples (U,Q,K) of U - Q*alpha - K*z.

| No. | U | Q=N32+N34 | K=N140 | Exact positive region area |
|---:|---:|---:|---:|---:|
| 1 | 305 | 58 | 141 | 1126817/43330560 |
| 2 | 301 | 168 | 15 | 3623/1112832 |
| 3 | 304 | 177 | 8 | 1/896 |
| 4 | 302 | 169 | 20 | 5/6624 |
| 5 | 311 | 151 | 69 | 1/2380800 |
| 6 | 309 | 151 | 64 | 3089/4860800 |
| 7 | 304 | 169 | 32 | 3/392 |
| 8 | 303 | 173 | 17 | 25/17664 |
| 9 | 309 | 169 | 46 | 1/6272 |
| 10 | 300 | 164 | 18 | 1/2484 |
| 11 | 304 | 151 | 50 | 191/710892 |

Each triple is attained by a complete original-native tree whose every one of the 141 named-state paths was replayed exactly. Its region is the nonempty convex polygon on which its plane is no greater than each of the ten others. Exact rational clipping confirms that their interiors are disjoint and their areas add to 1/24, the entire rectangle area. Every one of the eleven positive-area regions has a distinct gradient (-Q,-K); hence exactly eleven different *fixed-tree affine cost types* are necessary and sufficient for this rectangle. This statement concerns fee types, not uniqueness of decision trees.

### Exhaustive Bellman vertices

All 19 distinct polygon vertices and the exact global Bellman values F:

| alpha | z | F |
|---:|---:|---:|
| 1/3 | 0 | 245 |
| 1/3 | 1/9 | 730/3 |
| 1/3 | 1/6 | 727/3 |
| 1/3 | 1/3 | 237 |
| 1/3 | 32/91 | 64451/273 |
| 1/3 | 1 | 434/3 |
| 21/62 | 5/14 | 101989/434 |
| 8/23 | 3/23 | 5534/23 |
| 5/14 | 5/14 | 3251/14 |
| 58/155 | 2/5 | 35169/155 |
| 3/8 | 0 | 1901/8 |
| 3/8 | 3/56 | 13283/56 |
| 3/8 | 1/16 | 3793/16 |
| 3/8 | 1/6 | 5647/24 |
| 3/8 | 5/14 | 12835/56 |
| 3/8 | 3/8 | 1827/8 |
| 3/8 | 2/5 | 9071/40 |
| 3/8 | 77/192 | 14509/64 |
| 3/8 | 1 | 569/4 |

The previously established exact endpoint certificates are EC49FSH (alpha=1/3) and EC49FSF (alpha=3/8). Four newly interior vertices were checked **again** with a separately reconstructed raw-family 228-observer Bellman solver: (21/62,5/14), (8/23,3/23), (5/14,5/14), (58/155,2/5). Exact values in the table matched in all four checks. Primary exhaustive Bellman evaluations cover all 19 points. This is author-side dual-implementation finite checking, not independent human review.

### Proof for all real parameters

For each reduced complete decision tree T, the sum of query costs across all 141 paths is an affine function C_T(alpha,z)=U(T)-Q(T)*alpha-K(T)*z. The infimum F over admissible trees is jointly concave as the pointwise minimum of affine functions. The exact Bellman recursion on any candidate subset S evaluates, for each original named query q that splits S, |S| times the price of q plus the sum of optimal child-subset costs; it is exhaustive because each informative query strictly reduces the finite candidate set and all 228 original observations are enumerated.

For each positive-area clipped polygon P_i, the exhaustive Bellman result at **every** vertex v equals the affine price C_i(v) of its actual replayed tree. Every point x in P_i is a convex combination of vertices. By concavity F(x) is at least the corresponding convex combination of the vertex values, equal to C_i(x). Since the tree is feasible F(x) ≤ C_i(x). Thus F(x)=C_i(x) throughout P_i. The polygons tile the rectangle by exact rational clipping, proving the full continuous theorem. The eleven distinct gradients on open regions prove the minimal fixed-cost menu count.

### New structural information and smallest remaining unit

There are **four interior multi-phase junction vertices**: two triple intersections, at (21/62,5/14) and (58/155,2/5), and two **quadruple** intersections, at (8/23,3/23) and (5/14,5/14). This exact fourfold degeneracy is a new structural feature of the two-price problem. A very narrow but real phase (U,Q,K)=(311,151,69) has exact area 1/2380800; discrete grids can miss it. The corridor has eleven distinct 2D open strategy regions even though the alpha=1/3 and alpha=3/8 boundary slices have only five and eight open z intervals respectively. Thus slice-by-slice phase counts alone underreport the two-variable Pareto geometry.

Next research: extend to the adjacent alpha corridor (3/8,1/2), and then relax equality of the q32 and q34 discounts in the full three-independent-price model. Preserve original joint fibers and prices; do not infer admission from this draft.

### Sources and reproducibility

Inherited exact model and solver: [EC49FSH PR #2685](https://github.com/awdawmip/enterprise-math/pull/2685), [EC49FSF PR #2681](https://github.com/awdawmip/enterprise-math/pull/2681). This result uses the exact immutable EC49FSH head 79c6ea8ddc08aa1a035e162f69020834e7fd5402 as publication branch parent. The companion machine certificate records 11 full-tree witness hashes, rational polygons and all 19 exact vertex values. The complete non-sensitive local reproducibility bundle contains frozen original data, scripts, all full native trees and run logs.

This is **portable independent research**. Formal RS-EC49AS publication/owner authority was absent in the source read at 2026-11-18T00:26:40Z; no CLAIM, Result, Review or Activity checkpoint is implied by this file.
