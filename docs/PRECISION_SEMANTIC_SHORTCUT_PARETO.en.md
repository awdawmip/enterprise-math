# Semantic Shortcut Generators: Quotient-First Storage/Depth Pareto

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

Literal word caching precomputes syntax. If the future law has already been quotiented to a simpler exact semantic algebra, the same shortcut-depth idea can be applied **after** semantic collapse.

For the commuting-idempotent k-bit OR algebra this changes the storage law from literal words to semantic subsets while preserving the same execution-depth geometry.

## 1. Semantic effect algebra

Take k singleton semantic generators under bitwise OR. Every exact effect is one subset mask of the k primitive directions.

A word's semantic effect is simply the set of generator names that occur at least once.

Thus literal order and repetition are already quotient-invisible.

## 2. Bounded-support semantic shortcuts

Choose shortcut depth d with `1<=d<=k`.

Promote every nonzero semantic effect with support size at most d to a primitive shortcut generator.

The exact shortcut count is

`G(k,d)=sum_(i=1)^d C(k,i)`.

This is the size of the **semantic image** of all nonempty literal words of length at most d.

## 3. Exact target geodesic

Let target effect T have support size s.

Every shortcut can add at most d target bits, so at least

`ceil(s/d)`

shortcut applications are necessary.

Conversely partition the s target bits into chunks of size at most d and use one shortcut per chunk.

Therefore

`dist_d(0,T)=ceil(s/d)`.

The owner returns an explicit optimal chunk decomposition.

## 4. Worst-case execution distance

The full mask has support k, so the worst-case semantic geodesic is

`R(k,d)=ceil(k/d)`.

Endpoints:

- d=1: k singleton generators, worst-case distance k;
- d=k: all `2^k-1` nonidentity effects are primitive, worst-case distance1.

Every intermediate d gives an exact shortcut-storage/runtime point.

## 5. Exact runtime-budget design inside this shortcut family

If worst-case geodesic budget is r, the minimum shortcut depth is

`d_min=ceil(k/r)`

(with d=1 once r>=k).

Since `G(k,d)` grows strictly with d, this d also minimizes shortcut count within the declared bounded-support family.

## 6. Pareto depth locations

Storage increases strictly with d while runtime is the step function `ceil(k/d)`.

Therefore nondominated depths are exactly

`{ceil(k/r):r=1,...,k}`

with duplicates removed.

These are the same depth locations as the literal block-cache frontier with horizon H=k.

Semantic quotienting changes the **height of the storage coordinate**, not the arithmetic locations where execution depth improves.

## 7. Literal-cache versus semantic-shortcut storage

Literal free-word caching through depth d stores

`S_lit(k,d)=sum_(i=1)^d k^i`

word entries.

Semantic shortcut caching stores

`S_sem(k,d)=sum_(i=1)^d C(k,i)`

exact effects for `d<=k`.

There is a natural surjection

`literal words -> support subset masks`,

so

`S_sem(k,d) <= S_lit(k,d)`.

The semantic table has already removed order and repetition redundancy before precomputation is materialized.

## 8. Sharp storage comparisons

For k=20,d=3:

`S_lit=20+400+8000=8420`,

while

`S_sem=20+190+1140=1350`.

Both permit a full-mask execution in

`ceil(20/3)=7`

shortcut rounds under their respective block/effect models.

For k=8,d=4:

`S_lit=4680`,

while

`S_sem=162`,

and both corresponding shortcut models reach the full semantic mask in2 rounds.

## 9. Full precomputation shows the largest syntax/semantics gap

At d=k:

semantic shortcut storage saturates at

`2^k-1`

nonidentity effects.

Literal word storage through length k is

`sum_(i=1)^k k^i`,

which is vastly larger for growing k.

This gap is exactly the redundancy removed by the commuting-idempotent word quotient.

## 10. Cache-before-quotient versus quotient-before-cache

At the level of resulting exact effect **set**, the two procedures agree:

1. cache all literal words through d, then quotient equal effects;
2. quotient words by semantic equality first, then cache the distinct effects through support size d.

Both produce the same `G(k,d)` semantic shortcut set.

But their materialized storage cost differs dramatically if the first route actually stores the literal table before deduplication.

Therefore transformation order matters operationally even when the final semantic set is identical.

## 11. Relation to the formulaic OR representation

The preceding formulaic-normal-form generation shows an even more compressed representation: do not table the shortcut effects at all; encode any effect directly as a k-bit mask and compose by OR.

Thus the semantic shortcut table is itself an intermediate representation between:

- singleton generators + formulaic composition;
- bounded semantic shortcut table;
- full semantic effect table.

Whether storing shortcuts is useful depends on the execution interface and cost assigned to formula evaluation versus table lookup.

## 12. Stage131 hierarchy

The shortcut result makes the Stage131 storage/depth axis sensitive to **which semantic layer is being cached**.

For the same abstract shortcut depth d one can precompute:

- literal syntax blocks;
- semantic effect blocks;
- or no table, using a formulaic normal form.

All can implement the same exact future law but occupy different resource points.

So the right question is not only

`how deep is the cache?`

but also

`what quotient/normal form was applied before the cache was materialized?`

## 13. Scope boundary

The exact binomial law relies on the free commuting-idempotent semilattice on k primitive directions.

The bounded-support shortcut catalogue is canonical but is **not** claimed globally minimum among all possible shortcut generator sets achieving a given diameter. Target-specific shortcut design can use far fewer effects if only one target or one task region matters.

## Owner-local assets

- `src/enterprise_math/semantic_shortcut_generator_pareto.py`;
- `src/enterprise_math/semantic_shortcut_frontier.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

Boolean semilattices, binomial subset counts, word quotients and shortcut/time-memory tradeoffs are standard prior mathematics/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the quotient-first semantic shortcut Pareto specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
