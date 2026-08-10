# Count-Sensitive Branching Signatures

Status: `RESEARCH BRIDGE / NONCANONICAL`

Support branching retains the **set** of successor behavioural types. A future theory that reads branch multiplicity needs a strictly richer aggregator: the number of raw successors of each behavioural type.

This produces a natural-number branching layer between Boolean support and full witness provenance.

## 1. Recursive count branching signature

For observation O and labelled finite relations R_a, define

`μ_0(x)=O(x)`.

At the next depth, for every action a count how many raw target states carry each previous-depth signature:

`μ_(h+1)(x)`

`=(O(x), ( Counter( μ_h(y) : x R_a y ) )_a )`.

The counter is a finite multiset / natural-valued measure on successor behavioural types.

Equality of `μ_h` is therefore the h-round **count-stable/equitable** relation partition: equivalent states agree on the number of successors in every current behavioural class for every action.

On a finite state set, the partition again reaches a fixed point after at most the available number of block splits.

## 2. Natural count -> Boolean support is an exact branching coefficient quotient

Apply

`N -> B`, `n |-> [n>0]`

at every successor behavioural type, recursively.

This drops each positive multiplicity to presence/absence and then merges count-types that erase to the same support-type.

The result is exactly the parent support branching signature `σ_h`.

Thus

`count branching precision`

always refines

`support branching precision`.

This is the branching-operation analogue of the path-count -> path-existence quotient already established in the relation path-count route.

## 3. Sharp multiplicity gap

Use four states `x,y,u,v`, constant observation, and one relation a:

`x -> {u,v}`,

`y -> {u}`,

with u and v behaviourally identical thereafter.

Support branching sees from both x and y only

`{one successor type}`

and therefore merges them.

Count branching sees

`2 * that type`

versus

`1 * that type`

and splits x/y at depth one.

So successor multiplicity is an independent semantic precision coordinate even when target behavioural support is identical.

## 4. Terminal natural path counts are a second projection

Given a count branching signature and a literal word, terminal observed path counts are computed recursively:

- empty word contributes count1 to the current observation;
- for action a, evaluate the suffix on each successor type and multiply by that type's successor multiplicity;
- add all child count vectors.

This produces exactly ordinary natural path counts grouped by terminal observation.

Therefore

`count branching signature -> terminal path-count trace`

is a deterministic projection.

The projection again need not be injective.

## 5. Sharp count-correlation gap

Use eight states

`p,q,r1,r2,s,t,z1,z2`

with constant observation.

Relation a:

`p -> {r1,r2}`,

`q -> {s,t}`.

The two r-states have identical future count type

`b-count=1, c-count=1`.

State s has

`b-count=2, c-count=0`,

while t has

`b-count=0, c-count=2`.

Terminal natural path counts from p and q are nevertheless identical for every word:

- a: 2 paths;
- `ab`: 2 paths;
- `ac`: 2 paths;
- all longer/nonmatching words: identical zero counts in the acyclic fixture.

But at branching depth two:

p has successor-type multiset

`2 * (1,1)`,

whereas q has

`1 * (2,0) + 1 * (0,2)`.

Count branching therefore separates p/q although all terminal path-count traces agree.

The missing information is **how future count behaviour is grouped among successor branches before summation**.

## 6. Two independent aggregation quotients

The current relation lines now expose two different coarse operations.

### Coefficient erasure

`N -> B`

erases multiplicity of the same behavioural type.

### Trace summation

`multiset of successor count-types -> summed terminal word counts`

erases which future count vector belongs to which successor type.

Either can lose task-relevant information.

Thus exact path counts can be numerically richer than support while still being structurally too coarse for a future language that executes a count-valued relation on behavioural classes.

## 7. Deterministic/partial collapse

If every action/source has zero or one successor, every successor multiplicity is already 0 or1.

Then natural count and Boolean support branching signatures coincide at every depth.

So the new count axis is created only by genuine branching multiplicity.

## 8. Relation to #380 path-count precision

The existing path-count route asks what terminal count vector each literal word produces.

This generation asks a stronger operation-interface question:

> before terminal summation, how many successors of each **future behavioural count type** does this quotient state have?

The former is linear-time count trace semantics; the latter is branching-time count semantics / weighted-bisimulation-style precision.

Their strict gap is the count analogue of the support trace-vs-bisimulation gap.

## 9. Raw relation boundary

A raw relation is a set of source-target pairs, so it contains no duplicate parallel edge between the same ordered pair.

The multiplicity counted here is therefore the number of distinct raw target states that fall into one behavioural class.

If literal parallel witnesses/edges themselves carry multiplicity, A4 must expose a richer multigraph/witness object before this compiler is applied.

## 10. Precision hierarchy

For declared relation futures we now have at least:

`terminal Boolean support trace`

`<= support branching / set of successor types`

`<= count branching / multiset of successor types`

and independently

`terminal natural path-count trace <= count branching`,

with strict examples for both comparisons.

Full witness identity/provenance may still require further state beyond count branching.

## 11. Prior-art boundary

Multisets, equitable partitions, weighted bisimulation, path counting and semiring quotients are standard prior mathematics/computer science. A4 retains raw witness/correspondence ownership; P023/A2 retains declared future-signature precision ownership.

The project value is the explicit factorization:

> **multiplicity precision and branching-correlation precision are separate; terminal path counts can preserve the first while still losing the second.**