# Precision Semantics versus Representation Resources

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

This note does not create a new Foundation Question. It sharpens the meaning of “precision” after the recent semantic-preorder, continuation, coefficient-factorization and future-law compilation results.

The central correction is:

> **semantic precision and the resource cost of representing that precision are different layers.**

Two representations may implement exactly the same declared future theory while having radically different storage, arithmetic width, channel count, work and execution depth.

## 1. Semantic precision comes first

Relative to a declared future theory T, a representation must first answer the semantic questions already established by the project:

- which fine states remain equivalent?
- which operations descend?
- is DOMAIN/definedness preserved?
- which RELATION / witness distinctions remain visible?
- which coefficient laws and reflection guarantees are valid?
- can the representation serve as recursively executable state, or only as a terminal answer?

These determine the task-relative semantic capability profile.

A representation that loses a required capability is not an implementation tradeoff; it is semantically too coarse.

## 2. Resource comparison belongs inside one semantic-equivalence fiber

Suppose two representations implement the same exact T-semantics and can recover the same declared state/output/operation interface.

Then they belong to one semantic-equivalence class for this task.

Only **inside that class** is it meaningful to compare operational resources such as:

- state storage;
- rule/effect table storage;
- coefficient bit width;
- number of parallel channels;
- preprocessing / cache construction;
- normalization work;
- execution depth;
- reconstruction / synchronization cost.

The nondominated implementations form a representation Pareto frontier over one unchanged semantic law.

## 3. More stored rules need not mean more semantic precision

Stage131's chain example exposes the issue sharply.

A sparse adjacent/Hasse basis and a full transitive implication table can generate the same closure law.

The full table can answer in fewer inference rounds because it precomputes consequences. It does **not** automatically represent a finer semantic world.

Thus:

`more rules`

can mean

`more cached execution structure`

rather than

`more semantic precision`.

This distinction should be maintained whenever a rule table is derived from the same underlying exact law.

## 4. CRT coefficient factorization: same arithmetic semantics, different resources

Fix one exact modular arithmetic content L.

CRT permits equivalent representations ranging from:

- one wide mod-L channel;
- several narrower coprime channels;
- fully split prime channels.

All have the same integer-equality/reflection semantics.

What changes is:

- channel count;
- peak arithmetic width;
- rounded storage width;
- optional CRT reconstruction depth;
- parallel execution opportunities.

For `L=210`, exact nondominated `(channels,peak bits)` points include

`(1,8),(2,4),(3,3)`.

A fourth fully split channel adds no peak-width improvement and is dominated.

So arithmetic precision itself has multiple semantically identical operational factorizations.

## 5. Literal future-word caching: same operation language, different depth

For k action generators, cache every literal word effect through block depth d.

Storage grows as

`sum_(i=1)^d k^i`,

while a length-H word executes in

`ceil(H/d)`

cached rounds.

The endpoints are:

- generators only: tiny storage, H rounds;
- full horizon table: exponential storage, one round.

Every nondominated intermediate cache is still executing the **same exact literal future law**.

This is pure representation cost, not semantic refinement.

## 6. Semantic word quotienting: literal syntax and exact operation count differ

Many literal words can induce the same exact operation.

Quotienting words by exact transformation equality yields a semantic operation monoid.

This can drastically reduce stored effect count, but the representation then needs a word-to-effect normalizer.

Therefore:

`number of literal rules/words`

and

`number of exact semantic operations`

are separate complexity coordinates.

Neither alone determines runtime cost.

## 7. Tabulated versus formulaic semantic algebra

Even the number of semantic operations does not determine law-storage complexity.

The commuting-idempotent mask family has

`m=2^k`

exact operation elements.

A generic Cayley table and effect-action table each have `4^k` entries.

Yet every operation is one k-bit mask, composition is bitwise OR, and state application is the same OR formula.

So a large exact semantic algebra can have a compact exact presentation.

This proves:

`semantic algebra cardinality`

and

`semantic algebra presentation complexity`

are different resources.

## 8. Work/depth is also representation-dependent

The same formulaic OR normalizer replaces exponential table storage by runtime circuit work:

- total bit work for a length-H word: `kH`;
- parallel normalization depth: `ceil(log2 H)`;
- one final state application.

Thus a compact law formula can reduce memory while increasing runtime work, without changing semantics.

The correct resource vector must therefore include **work** as well as depth and storage.

## 9. Sufficient answer versus sufficient state remains a semantic boundary

Representation Pareto must not be used to hide a semantic mismatch.

A terminal trace answer can be sufficient for one query yet too coarse to serve as future executable state. The continuation-closure theorem measures the extra distinctions required to restore operation stability.

That repair changes semantic capability and belongs **before** resource optimization.

Only after the required executable state has been fixed should alternative encodings/caches/factorizations of that state be compared as resource-equivalent implementations.

## 10. Nonrealizable semantic joins still require representation lift

Likewise, if a joined future theory requires capabilities that no member of the current representation family can simultaneously support, no amount of cache tuning or table factorization solves the problem.

The state/representation type must first be lifted to realize the semantic join.

Resource Pareto starts after semantic realizability has been established.

## 11. Proposed two-level precision architecture

For a declared task T, route precision questions in two levels.

### Level A — semantic precision / capability

Determine the minimum exact state/interface needed for T:

- observation kernel;
- DOMAIN/RELATION/witness channels;
- coefficient reflection requirements;
- safe operation language;
- continuation/executable-state closure.

This layer is ordered by the task-relative semantic precision preorder.

### Level B — representation resources

Among all exact implementations of that semantic object, optimize a resource vector such as

`rho(R)=(state bits, law storage, coefficient width, channel count, preprocessing, work, depth, reconstruction cost)`.

There need not be one least representation; keep the Pareto frontier.

## 12. Exact-law compiler as the operational object

For resource analysis, a law should be treated not merely as a set of extensional rules but as an **exact compiler/executor package** containing enough information to:

1. identify / decode the represented state;
2. normalize or locate a declared future operation;
3. execute it exactly on the represented state;
4. expose the declared outputs/witness channels.

Different packages can realize the same semantic law with different resource vectors.

This is the appropriate object for Stage131 resource comparisons.

## 13. Storage-only comparisons can reverse after compiler cost is included

A semantic effect store may be much smaller than a literal word table, but if computing the effect ID requires replaying the entire word, execution depth can return.

A formulaic normal form may remove a Cayley table, but it replaces lookup with arithmetic/circuit work.

A split CRT representation may lower peak arithmetic width, but a scalar consumer may pay reconstruction depth.

Therefore every compression claim must state **what decoder/normalizer/executor is assumed**.

## 14. Prior Stage131 statement should be sharpened

A safer formulation is:

> The same exact relation/future law can have multiple operational representations with different storage, work and execution-depth costs. When those representations induce the same declared future semantics, the difference is a representation-resource Pareto, not a semantic precision difference.

Semantic precision changes only when the representation gains or loses task-relevant distinctions/capabilities.

## 15. Foundation routing rule

Before saying one representation is “more precise” than another, ask in order:

1. Do they implement the same declared future semantics?
2. If not, compare them using the semantic capability preorder.
3. If yes, do **not** call the larger table/state automatically more precise.
4. Compare their operational resource vectors and identify the nondominated Pareto points.
5. Include decoder/normalizer/reconstruction costs, not just stored payload size.

## 16. Evidence routes

Recent executable research supporting this synthesis includes:

- task-relative semantic precision preorder;
- coarsest operation-safe / partial / relation-support state repair;
- continuation debt from terminal answer to executable state;
- bounded local-law reflection and contextual decoding;
- constrained modular sensor Set Cover;
- CRT sensor factorization Pareto;
- literal future-word block-cache Pareto;
- finite semantic transformation-monoid normalizers;
- formulaic commuting-idempotent word algebra.

These remain research/Draft evidence; this note does not promote them to canonical Foundation by itself.

## Prior art / status

Time-memory tradeoffs, CRT, automata/monoids, circuit representations and Pareto optimization are standard prior mathematics/CS. The Enterprise Math value is the precision-first routing that separates **what semantic world is retained** from **how that exact world law is operationally represented**.

No new FQ. No canonical-main or `EXECUTABLE_CHECKED` claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
