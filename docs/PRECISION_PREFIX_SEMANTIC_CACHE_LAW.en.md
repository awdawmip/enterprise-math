# Horizon Cache Growth under Prefix Semantic Quotients

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

Caching every literal future word through horizon H can be exponentially expensive. If exact semantic quotienting is performed **before** cache materialization, the cache growth law can change qualitatively.

For the terminal/discovery/timing prefix ladder the distinct-operation cache sizes are all available in closed form.

## 1. Literal syntax cache

Including the empty word, the number of literal words of length at most H is

`C_lit(k,H)=1+sum_(h=1)^H k^h`.

For k>1:

`C_lit=(k^(H+1)-1)/(k-1)`.

This is exponential in H.

## 2. Terminal semantic cache

A terminal effect is a generator subset of size at most H.

Therefore

`C_terminal(k,H)=1+sum_(s=1)^min(k,H) C(k,s)`.

Once H>=k:

`C_terminal=2^k`.

The cache stops growing entirely with future horizon.

## 3. Discovery-order semantic cache

A discovery effect is an ordered list of distinct generators of length at most H.

Hence

`C_discovery(k,H)=1+sum_(s=1)^min(k,H) P(k,s)`.

Once H>=k it saturates at the finite discovery monoid size

`1+sum_(s=1)^k P(k,s)`.

Again, no further horizon growth is required.

## 4. Full-timing semantic cache

At exact word length h, an s-phase timing form has count

`P(k,s) C(h-1,s-1)`.

Summing over all exact lengths `h<=H` gives

`1 + sum_s P(k,s) sum_(h=s)^H C(h-1,s-1)`.

By the hockey-stick identity:

`sum_(h=s)^H C(h-1,s-1)=C(H,s)`.

Therefore the exact full-timing cache size is

`C_timing(k,H)=1+sum_(s=1)^min(k,H) P(k,s) C(H,s)`.

This is the closed-form count of all RLE prefix-semantic operations of total length at most H.

## 5. Fixed-k timing cache is polynomial rather than exponential

For H>=k:

`C_timing(k,H)=1+sum_(s=1)^k P(k,s) C(H,s)`.

This is a degree-k polynomial in H.

The top term is

`k! C(H,k)`,

whose leading coefficient is1.

Thus

`C_timing(k,H)=Theta(H^k)`

for fixed k.

The branch verifies mechanically that the k-th forward difference is constantly `k!` after H>=k.

## 6. Four cache-growth regimes

For fixed k:

### Literal provenance

`Theta(k^H)`.

### Full prefix timing

`Theta(H^k)`.

### Discovery order

Finite saturation at `1+sum P(k,s)`.

### Terminal set

Finite saturation at `2^k`.

Therefore changing the declared semantic observation layer can change horizon-cache growth from exponential to polynomial to constant.

This is a semantic effect first and a representation-resource effect second.

## 7. Sharp k=5,H=5

Through horizon5:

- literal words:3906;
- full timing semantic operations:1546;
- discovery operations:326;
- terminal operations:32.

Even at a short horizon, each quotient level materially changes the table size.

## 8. Sharp k=5,H=20

Through horizon20:

- literal words: `119,209,289,550,781`;
- full timing semantic operations: `2,514,181`;
- discovery operations:326;
- terminal operations:32.

The literal/timing entry-count ratio already exceeds ten million.

The timing cache is still much larger than the discovery cache because exact durations remain future-visible.

## 9. k=1 boundary

With one generator:

- literal words through H: H+1 including identity;
- full timing operations: H+1;
- discovery operations:2 once H>=1;
- terminal operations:2 once H>=1.

There is no literal redundancy left to remove at the timing level because word length itself is the complete prefix semantic state.

The polynomial formula correctly specializes to degree1.

## 10. Cache after quotient, not quotient after materialized cache

The formulas describe **distinct semantic cache entries**.

One may obtain them either by:

1. materializing every literal word then deduplicating;
2. normalizing directly into the semantic quotient and storing each semantic form once.

The final semantic key set agrees, but the first route may transiently pay the full exponential literal storage/work.

So an exact semantic normalizer should normally sit before cache materialization when the quotient is already part of the declared future semantics.

## 11. Class count and total cache count are different growth degrees

At one exact word length H, full timing semantic classes grow like

`Theta(H^(k-1))`.

Caching **all lengths through H** adds one cumulative degree:

`Theta(H^k)`.

This distinction matters when sizing a bounded-horizon future table.

## 12. Fiber geometry still matters inside the timing cache

The prefix-fiber generation shows that timing classes have nonuniform literal fibers.

Therefore equal semantic entry counts do not imply equal expected dedup benefits under nonuniform workloads.

The current closed form is an exact worst-case **distinct-entry count**, not an average cache-hit theorem.

## 13. Stage131 consequence

The cost of “cache the future through H” is undefined until the semantic cache key is named.

Possible exact keys include:

- literal word;
- full timing RLE;
- discovery order;
- terminal effect.

Their horizon growth laws are fundamentally different.

Thus Stage131 must specify both:

`what semantic quotient defines one cache entry?`

and

`what horizon/reuse interface is being cached?`

before a storage/depth comparison is meaningful.

## Owner-local assets

- `src/enterprise_math/prefix_semantic_cache_law.py`;
- `tests/test_prefix_semantic_cache_law.py`;
- this bilingual theorem note.

## Prior art / status

Hockey-stick identities, falling factorials and memoized semantic-state tables are standard prior combinatorics/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the exact prefix-semantic horizon-cache growth specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
