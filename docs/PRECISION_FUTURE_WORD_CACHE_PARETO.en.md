# Future-Law Word Cache: Storage versus Execution Depth

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

Stage131 began with a unary-chain observation: the same closure law can be represented by a small generator basis that needs many inference rounds or by a much larger explicit rule table that executes in fewer rounds.

The same resource law extends to arbitrary finite action languages through block caching of future word effects.

## 1. Literal block-cache model

Let the declared action alphabet have k named generators and let H be the maximum future word horizon.

Choose a cache depth d with `1<=d<=H`.

Store the exact effect of **every literal nonempty word of length at most d**.

The literal cache entry count is

`S(k,d)=sum_(i=1)^d k^i`.

For k>1:

`S(k,d)=k*(k^d-1)/(k-1)`.

For k=1:

`S(1,d)=d`.

## 2. Exact execution depth

Any word of length h can be split into consecutive blocks of length at most d.

Therefore it executes in

`R(h,d)=ceil(h/d)`

cached-operation rounds.

This bound is optimal inside the declared block-cache model: one cached primitive represents at most d input action symbols, so fewer than `ceil(h/d)` primitives cannot cover a length-h word.

## 3. Exact round-budget design

For horizon H and desired worst-case runtime budget r, the least cache depth that can meet the budget is

`d_min=ceil(H/r)`

(with d_min=1 once r>=H).

Literal storage grows strictly with d, so this depth also minimizes literal cache storage among all block caches satisfying the round budget.

Hence the exact storage required for runtime budget r is

`S(k,ceil(H/r))`.

## 4. Endpoint resource laws

### Generator-only execution

Take d=1.

- storage: k generator effects;
- worst-case runtime: H rounds.

### Full word table through horizon H

Take d=H.

- storage: `sum_(i=1)^H k^i`;
- worst-case runtime:1 lookup/application round.

### Intermediate block caches

Every `1<d<H` supplies a strict time-memory compromise whenever it reduces `ceil(H/d)`.

For noncommuting/free word languages, the storage cost grows exponentially with d.

## 5. Sharp free-word storage witness

The owner constructs a finite prefix-append transition system:

- states are all action words of length at most d plus an absorbing overflow state;
- action a appends symbol a while depth remains.

Every distinct literal word w of length<=d sends the empty state to a distinct prefix state.

Therefore all cached word transformations are distinct and

`#unique effects through d = S(k,d)`.

So the literal exponential storage bound is worst-case sharp even on a finite deterministic state system.

## 6. Discrete Pareto frontier

Because storage increases strictly with d, a cache depth is nondominated exactly when it is the **smallest** depth achieving a distinct runtime round count.

The set of Pareto cache depths is

`{ceil(H/r): r=1,...,H}`

with duplicates removed.

Thus the frontier locations depend only on horizon H, not on action count k. k changes the storage coordinate, often dramatically, but not where the execution-depth step function changes.

## 7. Frontier is O(sqrt(H))-sparse

Using

`ceil(H/r)=floor((H-1)/r)+1`,

the classical quotient-value decomposition gives only O(sqrt H) distinct values.

The branch uses the simple bound

`#Pareto points <= 2*ceil(sqrt H)`.

So an H-point design axis collapses to a sparse set of genuinely nondominated cache depths.

## 8. Sharp binary H=8 example

For k=2 and H=8, the nondominated cache depths are

`d=1,2,3,4,8`.

Their exact resource pairs `(literal entries, worst-case rounds)` are

- `(2,8)`;
- `(6,4)`;
- `(14,3)`;
- `(30,2)`;
- `(510,1)`.

Depths5,6,7 are dominated because they cost more storage while still requiring2 rounds.

## 9. Literal storage versus semantic effect storage

The literal table stores one key for every word block. But distinct words may induce the same exact operation.

Let

`N_d=# distinct transformations induced by words of length<=d`.

Always

`N_d <= S(k,d)`.

The inequality can be enormous.

Examples:

- two named generators both equal identity: `N_d=1` for every d while literal storage grows exponentially;
- identity plus a two-state flip: `N_d=2` while literal words grow as `2^(d+1)-2`.

## 10. Semantic compression is not a free O(1) lookup

Knowing that only `N_d` unique effects exist does not by itself let a runtime map an arbitrary literal block to the correct effect in O(1).

One must additionally provide a **word-to-effect / exact normal-form compiler**.

If that compiler simply replays the d generators, the block-cache execution advantage disappears. If it uses a compact algebraic normal form, its own storage and computation cost must be counted.

Therefore the next resource layer is not merely

`literal storage -> unique effect storage`,

but

`literal table storage`

versus

`semantic effect store + normalization compiler cost`.

This is exactly the role played by explicit operational normal forms such as P024's guarded `(T,H)` summary.

## 11. Relation to rooted circuits / chain bases

The original Stage131 chain example compares:

- a sparse Hasse/adjacent basis with long derivation depth;
- a denser transitive/circuit table with shallow execution.

The word-cache theorem is not the same combinatorial table, but it exposes the same structural principle:

> once exact law semantics are fixed, representation can exchange precomputed consequence storage against future composition depth.

For multi-action free languages, the storage side can be exponentially more severe than the unary-chain case.

## 12. Relationship to CRT factorization Pareto

The preceding CRT generation trades arithmetic width against channel count and optional reconstruction depth while preserving one coefficient law.

The present generation trades cached future-law storage against action-composition depth while preserving one operation language.

Together they show at least two independent representation axes:

- factorize the **coefficient state**;
- precompute/factorize the **future operation language**.

A complete precision compiler may need to optimize both simultaneously.

## 13. Scope boundary

This theorem assumes:

- finite total deterministic operations;
- literal word effects are exact;
- cache lookup/application is treated as one operation round;
- storage counts table entries, not byte-level key encoding;
- cache effects themselves fit the chosen state representation.

Partial operations require DOMAIN-aware word semantics; multivalued relations require the corresponding branching/witness interface. The same cache principle may apply after the correct operation normal form is chosen, but it must not erase those semantic channels.

## Owner-local assets

- `src/enterprise_math/future_word_cache_pareto.py`;
- `src/enterprise_math/future_word_cache_frontier.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

Time-memory tradeoffs, block caching, transformation semigroups and quotient-value arithmetic are standard prior mathematics/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the explicit Stage131 future-law block-cache Pareto specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
