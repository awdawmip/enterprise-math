# EC49FSG — exact seven-phase native BRC q140 discount at joint q32/q34 discount 5/16

Date: 2026-11-18. Frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status AUTHOR_PROVED / TWO_EXACT_NATIVE_BELLMAN_IMPLEMENTATIONS / NOT_INDEPENDENTLY_REVIEWED.
Continuation of [EC49FSF #2681](https://github.com/awdawmip/enterprise-math/pull/2681), EC49FSE #2678 and EC49FSD #2675.

## Model and result

Preserve original BRC16943 all 141 named response profiles induced by 310 raw configurations, all 228 named physical observers and their joint response fibers, uniform named-profile prior, and all complete deterministic adaptive trees. q32 and q34 each cost 11t/16 (joint discount 5/16); q140 costs (1-z)t, other observers t>0, and z ranges across all real [0,1]. Define F(z)=141 V(z)/t.

**Exact full-domain seven-phase theorem:**

| z interval | F(z) | U | N32 | N34 | N140 | root | max depth |
|---|---|---:|---:|---:|---:|---:|---:|
| [0,1/16] | 993/4 - 13z | 297 | 15 | 141 | 13 | q34 | 3 |
| [1/16,1/12] | 1987/8 - 15z | 299 | 21 | 141 | 15 | q34 | 3 |
| [1/12,1/6] | 1989/8 - 18z | 298 | 17 | 141 | 18 | q34 | 3 |
| [1/6,7/32] | 2005/8 - 30z | 300 | 17 | 141 | 30 | q34 | 3 |
| [7/32,5/16] | 4017/16 - 32z | 302 | 22 | 141 | 32 | q34 | 3 |
| [5/16,479/1456] | 4107/16 - 50z | 302 | 4 | 141 | 50 | q34 | 3 |
| [479/1456,1] | 2293/8 - 141z | 301 | 7 | 39 | 141 | q140 | 3 |

Shared endpoint values match exactly. Seven distinct active q140-use gradients on seven nonempty open intervals imply that a fixed-tree menu needs at least seven affine cost types, and the seven replayed complete trees attain this minimum.

## Nine? No: eight exact independent Bellman vertices

| z | F(z) |
|---|---|
| 0 | 993/4 |
| 1/16 | 3959/16 |
| 1/12 | 1977/8 |
| 1/6 | 1965/8 |
| 7/32 | 3905/16 |
| 5/16 | 3857/16 |
| 479/1456 | 349787/1456 |
| 1 | 1165/8 |

Every entry was recomputed with two separate original-raw-data decoders and exact rational/integer finite Bellman routines over the full 228 physically named observers. The witness for each open phase was replayed for all 141 named profiles and matched its exact tuple (U,N32,N34,N140). Exact 228-observer response partitions, not reduced representative observers, were supplied to both algorithms.

## Proof

For each complete reduced tree T, its total cost in units normalized by uniform 141-profile weighting is affine in z: C_T(z)=U(T)-(5/16)(N32(T)+N34(T))-z N140(T). The exact finite Bellman recursion minimizes over informative physical observations and recursively partitions the candidate set, with singleton value zero. Every informative response block is a strict smaller subset, so the recursion covers every complete adaptive tree. Thus F(z)=min_T C_T(z) is concave in z.

At each listed vertex the two native Bellman calculations certify the global optimum value. Each row has an exactly replayed complete tree with that row's affine cost, agreeing with Bellman at both endpoints l,r. For any z=(1-theta)l+theta r, concavity gives F(z)>=(1-theta)F(l)+theta F(r)=C_T(z), and tree feasibility yields F(z)<=C_T(z). Hence equality for all real z on every interval. Disjoint phase interiors have distinct slopes, establishing minimality of the seven affine-cost-type menu.

## New mathematical separation and next problem

Existing adjacent exact slices yield four phases at joint discount alpha=1/4 (EC49FSE), **seven phases at alpha=5/16 (this result)**, and eight at alpha=3/8 (EC49FSF). Thus the strategy-topology of the exact native observation-price problem changes at least twice somewhere in the interval alpha in [1/4,3/8]; this is a conclusion about slice phase counts and does not yet locate the exact bifurcation alpha. The next discriminating question is to locate and certify the rational 2D parameter vertices and their incidence and to test whether additional phase births/deaths occur between these three certified slices.

Verification scope is the stated 141-profile finite native BRC instance, full real z interval and exact weights; no physical calibration or independent review. Current published branch is a durable Draft artifact, not formal Task/CLAIM/Result/Review or scientific admission.
