# Semantic Word Normalization as a Second Storage/Depth Pareto

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The literal block-cache theorem stores precomputed consequences indexed by action words. When many words induce the same exact operation, a semantic normal form can compress those consequences further.

That compression is not free: the runtime must still compute the exact semantic effect of the input word. For finite deterministic state spaces this produces a second, internal Stage131 resource Pareto.

## 1. Finite transformation monoid

Let X be a finite state set with n states and let k total deterministic generators act on X.

Every action word induces one transformation

`F_w:X->X`.

The identity and generated transformations form a finite transformation monoid M.

Write

`m=|M|`.

Because there are only `n^n` total endomaps of X,

`m<=n^n`.

Thus semantic word effects eventually saturate even while literal words continue to grow exponentially with horizon.

## 2. Exact monoid compiler

The owner computes the generated transformation monoid by closure under right multiplication by generators, then constructs:

- canonical effect IDs;
- generator effect IDs;
- the full Cayley multiplication table;
- the exact action of each effect on fine states.

Sequential and balanced-parallel word normalizers are cross-checked against literal word execution.

## 3. Resource point A — direct generator execution

Store only the k generator state maps.

Storage scale:

`k*n` state-table cells.

A length-H word requires H state updates.

This is the smallest direct execution representation in the current comparison.

## 4. Resource point B — full literal word index

Store every literal word through horizon H as a key pointing to its semantic effect ID.

Auxiliary index entries:

`S(k,H)=sum_(i=1)^H k^i`.

Store the m semantic effects once in a shared `m*n` action table.

Runtime for a known whole word is one word lookup plus one effect application; in the round abstraction this is one final application round.

The index is exponential in H for k>1.

## 5. Resource point C — sequential semantic effect automaton

Instead of indexing every word, store only the right-generator transition table:

`current effect ID x next generator -> next effect ID`.

Auxiliary storage:

`m*k` entries.

For a nonempty length-H word, initialize with the first generator effect ID and use H-1 right-generator transitions, followed by one state application.

Total depth is therefore H rounds in the chosen abstraction.

This route does not reduce asymptotic depth relative to direct generator execution, but it evolves a compact semantic effect state instead of repeatedly updating the fine physical state.

## 6. Resource point D — full Cayley parallel normalizer

Store the arbitrary effect multiplication table:

`m*m` entries.

Associativity allows the H generator effect IDs to be reduced by a balanced binary tree without assuming commutativity.

Normalization depth:

`ceil(log2 H)`.

After one state application:

`total depth = ceil(log2 H)+1`.

Thus a larger algebra table trades storage for logarithmic compilation depth.

## 7. Exact Cayley/literal break-even horizon

The semantic effect action table `m*n` is shared by both the literal-index and Cayley representations.

Their auxiliary storage comparison is therefore exactly:

`m^2` versus `S(k,H)`.

The first horizon at which the Cayley representation uses fewer auxiliary cells than the full literal word index is the least H satisfying

`S(k,H)>m^2`.

This is an exact phase boundary in the declared cell model.

## 8. Sharp two-state identity/flip example

Take two states with generators identity and flip.

Then

`m=2`, `k=2`.

At horizon20:

### Generator maps

- generator state cells:4;
- execution depth:20.

### Literal word index

- word entries: `2^21-2 = 2,097,150`;
- shared semantic effect cells:4;
- execution depth:1.

### Sequential semantic automaton

- auxiliary entries: `m*k=4`;
- total depth:20.

### Cayley parallel normalizer

- auxiliary entries: `m^2=4`;
- shared effect cells:4;
- total storage in this cell model:8;
- normalization depth5;
- total depth6.

Here Cayley normalization nearly matches generator storage while reducing execution depth from20 to6, and it avoids the exponential literal table.

## 9. Short horizons reverse the comparison

For the same m=2,k=2 system at H=1:

- literal index has2 entries;
- Cayley table has4 entries.

So the literal representation is smaller.

The exact break-even is H=2 because

`S(2,1)=2<=4`

while

`S(2,2)=6>4`.

Semantic normalization is therefore not a universally superior compression.

## 10. Large monoids reopen the storage/depth tradeoff

Use the parent free-prefix fixture with k=2 and cache depth3. Its generated transformation monoid has

`m=16`.

Then:

- right-generator automaton: `m*k=32` entries;
- full Cayley table: `m^2=256` entries.

At horizon8:

- sequential semantic route total depth8;
- Cayley route total depth4;
- literal word index has510 entries.

So the three points are all materially distinct.

The Cayley/literal auxiliary-storage break-even occurs exactly at H=8 for this fixture.

## 11. Literal table, semantic store and compiler are separate resources

A statement such as

`only m semantic effects exist`

does not by itself define an operationally useful representation.

A complete implementation must specify how an input word is mapped to one of those m effects.

The resource object is therefore at least:

`semantic effect store + normalization mechanism + state action`.

Different normalizers can realize the same exact effect quotient with different storage and execution depths.

## 12. Algebraic normal forms can beat generic Cayley tables

A generic finite monoid table costs `m^2`. Specific operation languages can have a much more compact exact multiplication formula.

P024's guarded word profile `(T,H)` is one example: the normal form carries a closed max-plus-style product rather than an explicit table over all reachable profiles.

Therefore the Cayley table is a universal finite-state construction, not the final optimal representation for every structured action language.

The next improvement axis is **formulaic normal-form algebra versus tabulated monoid algebra**.

## 13. Stage131 hierarchy

The current future-law representation hierarchy is now:

1. sparse generators — minimal stored syntax, maximal runtime composition;
2. semantic right-generator automaton — compact effect state, sequential normalization;
3. semantic Cayley algebra — larger algebra storage, logarithmic parallel normalization;
4. literal block/full-word tables — largest precomputation, shallowest lookup execution.

All can represent the same exact future law.

This is a direct generalization of the original Stage131 observation that relation-law precision has a storage/execution-depth Pareto.

## 14. Scope boundary

The current executable theorem assumes finite total deterministic transformations.

For partial actions, the semantic effect object must preserve DOMAIN. For multivalued relations it must preserve the declared support/count/witness interface. For infinite but finitely parameterized normal-form monoids, table enumeration may be impossible while a formulaic algebra still exists.

So “finite transformation monoid” is one clean positive owner, not a universal replacement for richer operation semantics.

## Owner-local assets

- `src/enterprise_math/semantic_word_normalizer.py`;
- `src/enterprise_math/semantic_word_normalizer_resources.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

Finite transformation monoids, Cayley tables, automata normalization and parallel associative reduction are standard prior algebra/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the explicit semantic-normalizer storage/depth resource specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
