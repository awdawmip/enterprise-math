# Enterprise Math R69 — Exact integer-lift source certification and cache crossover

**Date:** 2026-11-11. **Scientific input pin:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged). **Predecessor:** R68 @ `e09d7379530db556c04789b35293baadc32ac91c`, `research_notes/brc_s23_av_anchored_hull_20261111_r68`. **Claim:** author-side scoped derivation and independent finite exact tests, *not* project-admitted theorem.

## Typed problem

Fix rational anchor `theta0=p/q` with `0<p<q`, a half-open **nonwrapping original-labelled** history arc

`A(theta)=[{a theta},{b theta})`, with integers `0<=a,b<m`,

and a finite collection of distinct source events `(t,branch)` with `t>=0`. Branch identities are retained for future identity-specific delete; the present observer returns the greatest qualifying time (or empty). The formula is an auxiliary circle-source observer, not native Heartbeat X6, and none of these arithmetic operations is presented as native BRC dynamics.

For query `I=[L,U]` rational with `0<L<=theta0<=U<1`, assume the historical cut order is stable, in particular this named arc is nonwrapping throughout `I`. Any event in the source set qualifies at `theta` iff `{t theta} in A(theta)`. The complete carrier remains the separately erasable event set: a current maximum is not a full state for branch-specific deletions.

## Theorem R69.1 — Integer-lift endpoint certificate

For `s in {a,b,t}`, suppose `floor(s L)=floor(s U)=k_s`. Since `s>=0`, for every real `theta in [L,U]` the floor stays `k_s`; thus `{s theta}=s theta-k_s` is affine on this entire interval. Further suppose `{a L}<{b L}` and `{a U}<{b U}`. Their affine gap stays strictly positive on the whole interval, so the selected nonwrapping arc remains valid.

For an endpoint `E=u/v` in lowest terms, set `r_s(E)=s u mod v`. The following are sound statements for **all real theta in I**, including both endpoints:

**IN:** If at **both** endpoints `r_t>=r_a` and `r_t<r_b`, then the source belongs to the named arc throughout `I`.

**OUT-low:** If at both endpoints `r_t<r_a`, the source is excluded throughout `I`.

**OUT-high:** If at both endpoints `r_t>=r_b`, the source is excluded throughout `I`.

In all other cases return `UNKNOWN`, not an incorrect negative. Proof: each difference `{t theta}-{a theta}` or `{t theta}-{b theta}` is affine, and inequalities with strict/weak endpoint treatment hold on an interval exactly when appropriate endpoint inequalities hold. Lower boundary is inclusive; upper boundary is exclusive. This proves soundness, not completeness, of the three-way classifier. The floor-stability condition is sufficient and deliberately conservative at exact wrap endpoints.

**Integer realization.** Each `r_s(E)` uses one product, quotient/remainder of arbitrary-precision integers. No Fraction object or gcd normalization is needed in the per-event comparisons. For `T=bitlength(max(t,a,b))`, `B=bitlength(max(|u|,v))`, all integer products have at most `T+B` bits; end-to-end bit complexity is governed by the actual multiplication/division algorithms and cannot be inferred from the number of tests alone.

The same result applies independently to any frozen Farey/original-label pair known to be adjacent over the certified interval. Merely sorting boundary labels at the anchor without testing interval order is insufficient. The supplied executable chooses the nonwrapping pair from the sorted anchor and checks nonwrapping/floor stability on every query.

## Theorem R69.2 — Minimal-future information and reusable evidence

For a fixed original-labelled arc, immutable source set, anchor, and event identity, if a positive IN/OUT certificate holds on `I`, it holds on every `J subseteq I`. A prior exact certificate is therefore reusable for nested intervals without repeating its source arithmetic. If overlapping positive intervals assert the same status for the same source and exact observer signature, their union is a valid interval certificate (R68's shared-anchor case is a convenient special case).

Suppose an uncached execution of a fixed workload makes `A` source tests, while a cache makes `C` source tests and `H` source-status certificate hits, always resolving the same required source comparisons. Then `A=C+H` exactly, as an **operation-count identity**. It does not imply a runtime improvement because containment tests, hashing and eviction have cost; a cached source status never substitutes for retaining original event/branch identities.

**Capacity counterexample.** For LRU capacity `B`, cyclically request `B+1` distinct cache keys, with no same-key reuse before the next cycle. Every request misses (after initialization also): the previous instance of that key is evicted before reuse. Thus no policy can infer a positive speedup from a high query count alone without the access pattern and cost model. This is a cache counterexample, not a negative result about source certification or the native residual problem.

## Reproducible exact experiments

`check_r69.py` is a self-contained Python standard-library script; its independent oracle computes source membership using `fractions.Fraction` at both interval endpoints and three interior points. For each query it verifies the whole latest-source answer against this oracle. It compares (i) exact Fraction certificate kernel, (ii) exact integer-lift certificate kernel, (iii) integer-lift plus 64-entry LRU and (iv) integer-lift plus 8-entry LRU. Source set and nominal winner are computed identically in all paths.

Configuration: `theta0=27413/65521`; `m in {8,32,128}`; `n in {16,64,256,1024}`; source times begin at 2 or at `10^18+2`, skipping exact anchor boundary coincidences; widths `delta=2^{-D}` with `D=max(80, bitlength(max source time)+40)`; query reuse counts `1,4,16,64`; every parameter endpoint and oracle point is rational. The experiment tests 96 model/workload cases and 2,040 queries per algorithm (10,200 exact oracle points per algorithm). Every asserted certificate passed. It is a **finite accuracy/engineering check**, not an exhaustive proof of the algorithm beyond Theorem R69.1.

For the 64-query repeated workloads, aggregated over six settings of `m` and source-time scale at each `n`:

| n | Integer uncached event tests | 64-entry cache tests | Cache hits | Integer query time | Cached query time |
| ---: | ---: | ---: | ---: | ---: | ---: |
|16|5,184|81|5,103|44.5 ms|40.6 ms|
|64|12,416|194|12,222|107.3 ms|94.7 ms|
|256|36,736|32,830|3,906|307.0 ms|322.5 ms|
|1024|42,816|39,918|2,898|360.1 ms|381.8 ms|

Measured times are a **single host/process run**, query calls only (five-point oracle checks excluded), not normalized bit-operation counts. At `n=256,1024`, the fixed 64-entry cache often thrashes, and extra bookkeeping outweighed certificate savings. At `n=16,64`, repeated-source patterns allowed more reuse. On the same cases the Fraction kernel took 121.0, 285.4, 829.0, 966.0 ms, respectively, versus integer 44.5, 107.3, 307.0, 360.1 ms. These are special-case implementation timings, not a project-wide asymptotic speedup.

The full per-case evidence can be regenerated using `python check_r69.py --output /tmp/R69_EXACT_BENCHMARK.json`. `R69_SUMMARY.json` records the aggregate counters. No native S23 128-label/78-stage run was performed; only the inherited frozen pin and auxiliary observer are used.

## BRC/observer decision

BRC check = `NOT_APPLICABLE` for the **kernel itself**: its carrier is a one-parameter external circle with original-labelled phase arcs, and it has no defined native X6/BRC branching or typed native-time update. The observer-preservation requirement is nevertheless applied concretely: maximum source time can answer the present observer but does not preserve identity-specific deletion; every branch identity remains in the full source set. No transfer to native BRC is asserted.

## Next actual work

R70: (a) precompute the `a,b` endpoint residues and floors once per query to remove their repeated work from every source comparison; (b) measure input conversion, exact bit-level multiplication/division/gcd and allocation with identical output scope and realistic persistent updates; (c) design an adaptive admission policy based on recent measured hits/evictions and test against adversarial alternating signatures; (d) compare to the *original* R66–R68 implementation on matching datasets, not merely this narrower integer-lift kernel. Any native transfer requires an explicit typed observer map and preserved future operations.

**Authority:** author-side independent research only; active shared owner and formal CLAIM not established; Result/Review and mathematical admission not asserted.
