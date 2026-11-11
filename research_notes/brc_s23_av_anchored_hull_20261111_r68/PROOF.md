# Enterprise Math R68 — Anchor-overlap certificate hull and bounded persistent-source cache

**Research date:** 2026-11-11. **Scientific pin (unchanged):** 43ec6098b1330ae86d0a7863be336c5d97f6ef34. **Predecessor:** R67 source commit 61fe92fec15686405eb54a7c7ae7e3f5d33b88cf, research_notes/brc_s23_av_certificate_cache_20261111_r67. **Status:** author's mathematical proof and executable exact rational experiments; independent review pending.

## Typed model and observer

This is the auxiliary exact rational circle-source observer studied in R62–R67, not native Heartbeat X6 dynamics or a physical residual claim. Fix a rational anchor 0<θ0<1, m≥2 original historical labels, observation (j,x), label z, and a finite set of separately erasable branch-bearing source events (t,b). At parameter θ, historical boundaries are {vθ} for v=0,…,m−1, and the target A_z(θ) is its original-labelled half-open circular arc, with cyclic order stable on a certified parameter interval. Event (t,b) belongs to A_z(θ) when {x+(t−j)θ} lies in that arc. The observed latest source is max t among qualifying events, or empty. The full persistent carrier retains each (t,b), necessary for future branch-specific deletion even when current observer values coincide.

An R65/R66 exact rectangle exclusion certificate for immutable subtree C, query signature q=(θ0,j,x,m,z,next_label), and closed rational interval I=[L,U], asserts

∀θ∈I ∀(t,b)∈C: {x+(t−j)θ} ∉ A_z(θ),

including closed endpoints and the required stability of original history order. A failed or inconclusive rectangle produces no positive certificate. R67 caches these results as a list of parent intervals and reuses an entry for a contained query interval.

## Theorem R68.1 — positive anchor-intervals combine exactly

Let I1=[L1,U1] and I2=[L2,U2] be closed rational intervals containing the **same fixed anchor θ0**. Suppose both have sound positive exclusion certificates for exactly the same immutable source subtree C and exact query signature q, including the relevant historical-order assumptions. Set

H=[min(L1,L2), max(U1,U2)].

Then the exclusion proposition and historical order assumptions hold for every real θ∈H.

**Proof.** θ0∈I1∩I2, so the two intervals intersect and I1∪I2=H. Each parameter of H belongs to at least one certified interval. The exclusion and history-order predicates are true at that point. The source membership of C does not change because the subtree is immutable. No extra assumption about internal source phase ordering is needed. QED.

**Corollary R68.2.** For any finite sequence of valid positive intervals with the same C and q, one pair of rational endpoints (minimum left, maximum right) describes their exact union. A new query J⊆H reuses the positive result after two endpoint comparisons, with no original rectangle computation. This remains sound when applying the rectangle *sufficient test* directly to H would return INCONCLUSIVE: both original certified intervals cover H.

**Theorem R68.3 — bounded LRU correctness.** Store at most B distinct (immutable subtree identity, exact query signature) keys with one positive interval hull per key. On a cache miss, evaluate the unchanged R66 certificate. Eviction can affect computational work but not truth: it discards a reusable proof and introduces no affirmative conclusion. Immutable path-copying preserves members and extrema of shared subtrees across different roots. A changed ancestor has a different identity; every current-root query must recompute its nominal winner separately. Hence any eviction order, including LRU, preserves soundness of the certified answer. QED.

**Why overlap matters.** If one uses arbitrary nonanchored intervals, merging their hulls is unsound. Exact example m=2, z=0, j=x=0, target A0(θ)=[0,θ), source t=4. For θ in [1/10,1/5], {4θ}=4θ>θ; for θ in [17/50,9/25], {4θ}=4θ−1>θ. The source is excluded on both closed intervals. At θ=1/4 between them, {4θ}=0∈[0,θ), so the source is included. The fixed-anchor intersection condition in R68 prevents this error.

## Exact executable experiments

Executable: check_r68.py (Python 3.10+ standard library). It imports the *unchanged* R67 exact kernel check_r67.py from the sibling predecessor folder, available on this author branch. Reproduction:

python research_notes/brc_s23_av_anchored_hull_20261111_r68/check_r68.py --cap 64 --count 80 --output /tmp/r68.json

Use --cap none or --cap 16 for the alternative bounded cases. Each variant is run independently in its own process with seed 68001. The verifier compares uncached R66, the original R67 list, the new R68 hull, and an independent per-event R62/R64-style linear certification with exact Fraction arithmetic. Each certified result is checked against exact direct-source oracle at rational endpoints and three interior points. This covers original label order, changed query labels and observations, repeated source timestamps with distinct branch IDs, insertion, branch-specific deletion, and retained persistent roots.

Each variant executed 80 exact models, 1,600 matched interval queries, and 8,000 independent oracle checks. All 1,600 were certified identically and the linear competitor agreed on latest source values in all 1,600 cases. Rectangle checks per identical workload: **uncached R66 7,959; R67 list 6,883; R68 hull 6,067**. R68 saved 816 more rectangle computations than the R67 list (11.85% of the latter), and 1,892 versus uncached R66 (23.77%). R68 recorded 408 hull extensions. Original R67 list stored 1,912 interval entries in this run; R68 unrestricted hull held 688 keys, and capped versions held 64 or 16 keys. Unrestricted, cap-64, and cap-16 all had 1,892 hits in this clustered query order, although the capped versions evicted 624 and 672 keys respectively.

An adversarial workload alternated 17 historical-label signatures over 85 queries. Uncached source rectangles=630, unrestricted hull=422 with 208 hits, **cap-2 hull=630 with zero hits and 258 evictions**. A separate 400-request unique-observation workload produced **zero cache hits** and 2,975 rectangle checks both with and without cap-32 cache. This is a reproducible no-reuse regime in which bookkeeping may increase runtime. One timing run (400 queries) was 0.180849 s without cache versus 0.197010 s with cap 32; these are host-specific elapsed times.

The clustered workload used source-time magnitude up to 8 bits, anchor denominators up to 8 bits, interval denominators up to 37 bits, and observation denominators up to 7 bits. Each run's exact numeric counters and timing are in R68_CERTIFICATE_SUMMARY.json; the executable can regenerate the fuller JSON with all per-method counters.

## Work and memory accounting

For K retained keys, one hull stores O(K) pairs of exact rational endpoints, plus immutable-node identity references and exact signature hashes; under cap B the cache uses O(min(K,B)) entries. Expected hash table operations are O(1) *dictionary steps*, with rational hashing, comparison, multiplication, division and gcd costs depending on integer bit widths. Each hit does two exact rational containment comparisons in place of one constant-count affine interval rectangle evaluation. When every signature is new, cache work is pure overhead. Source index creation, path-copy allocations, nominal winner, history sort, precision conversion, complete bit operations and observer output must be accounted for before global complexity comparison.

On these small-source models the independently implemented exact linear competitor was faster than the tree/hull path despite doing more per-source boundary work. This is a useful crossover witness: a structure must be chosen for actual (n,m,query) regime, not solely by a rectangle-check count. No complexity improvement over a matched linear baseline is asserted from the present small-regime numbers.

## R69 continuation

Measure integer numerator/denominator operand counts and gcd bit work end-to-end for linear, tree, uncached R66, list R67, and hull R68, including tree-building, path-copy memory and eviction under matched single-label interval-query output. Explore n=16,64,256,1024, m=2,8,32; θ denominator lengths 16,64,256; sparse query reuse and t near 10^18. Develop a selectively admitted cache based on measured expected certificate savings versus allocation, exact comparison and hashing, and find empirical crossovers. Any transfer to native BRC operations must preserve its own typed carrier and exact correspondence evidence.

**Author scope:** independent durable research frontier only; no shared CLAIM, native Result, independent review, Foundation promotion, P000 change, or physics claim.
