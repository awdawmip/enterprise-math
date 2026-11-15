# EC49FQF — Sharp first-observation switches and forced mixed acquisition order in native BRC class 16943

Date: 2026-11-16. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is an independently persisted portable research return, not an authenticated Task Result or a Foundation promotion.

## Model and sources

Use frozen science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, with original-master SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e and named-root profile CSV SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. Native class 16943 has 310 original configurations inducing 141 distinct full named-root profiles. There are 144 terminal scalar queries (cost t>0) and 84 named-root scalar queries (cost r>0). An adaptive finite tree must identify the full named-root profile, and query choices may depend on previous responses.

Let x=r/t. A feasible tree π has aggregate integer query counts Rπ,Tπ, weighted by either U (each of the 141 distinct profiles has weight one) or M (each of the 310 original configurations has weight one). Its unnormalised cost in t units is Lπ(x)=Rπ x+Tπ.

## Theorem: the first observation type has a single exact transition

| Prior | Every global optimum begins with a named-root query | Both first-query types are optimal | Every global optimum begins with a terminal query |
|---|---|---|---|
| U, 141 root profiles uniform | 0 < x < **153/184** | x=153/184 | x > 153/184 |
| M, 310 original configurations uniform | 0 < x < **17/24** | x=17/24 | x > 17/24 |

At x=153/184, U's exhaustive optimal first indices are {32,34,153,161}. At x=17/24, M's are {59,88,153,161}. Terminal query indices are 0..143 and root indices are 144..227. The previous native partition canonicalisation has 209 distinct response partitions and no cross-type duplicate, so these type conclusions are unaffected by same-type query equivalence.

The already proved pure-root-optimality loss points are x0(U)=4/7 and x0(M)=26/71. More precisely:

* At 0<x<x0, every optimal strategy is pure-root; at x=x0 a pure-root optimum still exists and every optimum begins root-first.
* At x0<x<x1, with x1 the first-query transition above, **every** optimum begins root-first but subsequently uses terminal observations on at least one positive-weight path. Every optimum in this open region is mixed.
* At x=x1, optimal root-first and terminal-first strategies coexist; all optima are mixed.
* At x>x1, every optimum begins terminal-first and necessarily uses named-root observations later along some path. Every optimum is mixed.

The sharp mixed-but-root-first window widths are 335/1288 (U) and 583/1704 (M); the two initial-query switch prices differ by 17/138.

## Proof

**1. Exact global Bellman premises and first-branch certificates.** EC49FQD (PR #2521) proves the full 11-line, 10-breakpoint optimal cost envelope for U. EC49FQE (PR #2524) proves the 16-line, 15-breakpoint envelope for M. Their 25 exact rational endpoint certificates compute the unrestricted Bellman optimum with all 228 queries and include 228 forced-first-query total costs. The independent EC49FQF verifier computes the minima over the root indices and terminal indices separately, rechecks the exact incumbent cost, adjacent affine-line equality, and original certificate content SHA256 hashes. Before the stated switch each endpoint has root-only first-query minimisers; after the switch each has terminal-only first-query minimisers; precisely at the switch both types minimise. All 25 endpoints are explicitly enumerated in the attached machine summary.

**2. Interior prices from endpoint optimality.** On each cost phase [a,b], the already proved global optimum is one affine line L(x). For any feasible finite tree π, Lπ(x)-L(x) is affine and is nonnegative at a and b. If π is optimal at any interior y, that affine difference vanishes at an interior point while nonnegative at both endpoints, hence is identically zero on [a,b]. Thus π must be optimal at both endpoints, and its first-query type belongs to the intersection of the two endpoint minimising types. These intersections contain only the stated type on the appropriate side of each switch. This classifies **every** optimal tree rather than merely the witnesses extracted by the Bellman solver.

**3. Low-price tail.** At x0, the exact optimal totals are R0 x0 with (R0(U),R0(M))=(362,1033), achieved by pure-root trees. For any π and 0<x<x0,

Lπ(x) = (x/x0)Lπ(x0) + (1-x/x0)Tπ >= R0 x+(1-x/x0)Tπ.

Equality at the global minimum therefore requires Tπ=0. All optimal trees are root-only on this low tail.

**4. High-price tail.** Independent source re-evaluation gives exactly two terminal-invisible doubleton fibers: {17928,38165} and {24541,38166}, each profile having original multiplicity one. Every full-identification tree consequently needs at least four aggregate named-root observations under U and M. At x=3, globally optimal trees attain L*(3)=308 (U), 700 (M), with totals (R,T)=(4,296) and (4,688). Hence for all x>=3, L*(x)=4x+296 (U) and 4x+688 (M). If π is optimal at x>3, then

Lπ(x)>=L*(3)+(x-3)Rπ = L*(x)+(x-3)(Rπ-4),

so Rπ=4. A root-first query contributes at least 141 (U) or 310 (M) root observations; therefore **every** high-tail optimum starts with a terminal query. New exact unrestricted Bellman runs at (r,t)=(1,4) and (4,1), with independent 310-configuration replay, confirm both tails.

**5. Necessity of mixed acquisition and sharpness.** For x>x0, the feasible policies (R,T)=(355,4) for U and (962,26) for M are strictly cheaper than the pure-root optima, since 7r>4t or 71r>26t respectively. Terminal-only observers cannot separate the two terminal-invisible doubletons at any positive price. Thus **all** global optima for x>x0 use both query types. At the exact first-query switch the exhaustive forced-first Bellman arrays include optimisers of both initial types, making the quoted thresholds sharp.

## Exact validation, status and continuation

An independent rational/first-query endpoint verifier checked 10 U and 15 M full endpoint certificates, all 228 initial query costs at each, the global lower bound, and both adjoining affine totals. Two additional unrestricted runs at x=1/4 and x=4 yielded respectively (U,M)=(362,1033) and (312,704) total integer costs. An independently implemented replay recognised all 310 configurations at both new prices. The terminal-only fiber check returned exactly the two weight-one doubletons above. The attached 2026-11-16 evidence archive EC49FQF_SHARP_INITIAL_OBSERVATION_EVIDENCE_20261116.tar.xz (SHA256 9a7c44cc6adb7d27c22ffff30ef60210b02662e1e071817f3ed2aa3ad1aa6e9f) contains all source inputs, all 25 prior complete endpoint certificates, both new full tail certificates, code and logs. The GitHub JSON here is a summary with source hashes; auditing saved certificates is distinct from recomputing the Bellman solver at every anchor.

Next: classify the exact optimal **first-query index** sets, including symmetric alternatives within each affine phase; then study prior interpolation between profile-uniform and multiplicity-uniform priors while retaining the full named-root residual and immutable science freeze. At this run's scoped GitHub directory read, RS-EC49AS has no formal immutable publication directory, so no current CLAIM/Result or owner is claimed.