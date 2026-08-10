# Stage131 — Rooted-Circuit Table Explosion in a Binary AND Tree

Status: `RESEARCH BRIDGE / NONCANONICAL`

The unary-chain boundary showed transitive redundancy. Multi-premise Horn closure reveals a stronger phenomenon: even when the compositional basis is a tree, the complete one-round rooted-circuit premise table can grow exponentially in the number of leaves because it enumerates all inclusion-minimal ways of making one root derivable.

## 1. Local basis

Take a balanced binary AND tree of height h with

`L=2^h`

leaves.

Every internal node has one local Horn rule from its two children.

The entire compositional basis has only

`L-1=2^h-1`

rules.

This basis derives the root from all leaves in h synchronous rounds.

## 2. What a rooted-circuit premise means here

For one internal node r, a rooted-circuit premise is an inclusion-minimal seed set P such that

`r in Cl(P)`

and `r notin P`.

The table therefore lists every minimal one-round premise pattern from which r could be treated as directly available.

These premises need not lie on one fixed tree level.

## 3. Availability recurrence

Let `A_h(z)` be the generating polynomial for minimal ways to make a height-h node available, **allowing the node itself as a seed**. The coefficient of `z^m` counts minimal availability sets of width m.

For a leaf:

`A_0(z)=z`.

For an internal node, there are two disjoint possibilities:

1. seed the node directly: contribution z;
2. make both children available independently: contribution `A_(h-1)(z)^2`.

Therefore

`A_h(z)=z+A_(h-1)(z)^2`.

## 4. Rooted-circuit width polynomial

The direct-root seed is not a rooted-circuit premise for the root itself, so

`P_h(z)=A_(h-1)(z)^2=A_h(z)-z`.

Coefficient `[z^m]P_h` is exactly the number of inclusion-minimal root premises of width m.

The branch independently enumerates all minimal premise sets through height4 and matches the generating polynomial exactly.

## 5. Exact count recurrence

Let

`M_h=P_h(1)`

be the number of rooted-circuit premises for the height-h root.

Then

`M_1=1`,

and since `A_(h-1)(1)=1+M_(h-1)`,

`M_h=(1+M_(h-1))^2`.

The first values are

`1, 4, 25, 676, 458329, 210066388900, ...`.

This is not an implementation artifact; it is the exact number of inclusion-minimal premise sets for the root.

## 6. Small examples

### Height1

Only one circuit:

`{left leaf,right leaf}`.

So

`P_1(z)=z^2`.

### Height2

There are four root circuits:

- both child nodes;
- left child + two right leaves;
- two left leaves + right child;
- all four leaves.

Thus

`P_2(z)=z^2+2z^3+z^4`.

### Height3

`P_3(z)` is

`z^2+2z^3+3z^4+4z^5+5z^6+6z^7+4z^8`,

whose coefficients sum to25.

## 7. Every premise width occurs

Inductively, `A_(h-1)` has positive support on every degree

`1,...,2^(h-1)`.

Squaring therefore yields every sum

`2,...,2^h`.

Hence

`P_h(z)`

has a positive coefficient at **every** premise width from2 through all `2^h` leaves.

The root therefore has a dense spectrum of minimal premise widths, not merely the level-frontier widths `2,4,8,...`.

## 8. Exponential growth in leaf count

For h>=2,

`M_h >= M_(h-1)^2`,

with `M_2=4`. Therefore

`M_h >= 2^(2^(h-1))`.

Writing `L=2^h`, this is

`M_h >= 2^(L/2)`.

A simple upper recurrence on `1+M_h` gives

`M_h < 2^(2^h-1)=2^(L-1)`.

So the root circuit table is exponential in the number of leaves:

`2^(L/2) <= M_h < 2^(L-1)`.

The local basis remains only `L-1` rules.

## 9. All internal rooted circuits

A height-h tree has `2^(h-t)` nodes of height t.

Therefore the complete rooted-circuit rule count across all internal nodes is

`C_h=sum_(t=1)^h 2^(h-t) M_t`.

Exact examples:

- h=3: 37 rooted-circuit rules versus7 local basis rules;
- h=4: 750 versus15;
- h=5: 459829 versus31;
- h=6: 210067308558 versus63.

The root term quickly dominates the full table.

## 10. Premise-literal storage is even larger

The generating polynomial also records premise storage.

Total premise literals across all root circuits are

`P_h'(1)`.

For h=5:

- root circuits:458329;
- total root premise literals:7048360;
- average premise width is about15.38;
- maximum width is32.

Thus counting only circuit rules still understates the table's actual premise representation cost.

## 11. Why the explosion occurs

At every internal node, each child can be supplied in two conceptually different ways:

- seed the child atom directly;
- derive it from any one of that child's own rooted-circuit premises.

The left and right choices combine independently. This creates the squaring recurrence.

So rooted-circuit enumeration expands every compositional subtree choice into a separate one-round premise alternative.

## 12. Minimal premise table versus compositional basis

The local Horn basis stores **how** conclusions can be built recursively.

The rooted-circuit table stores **every minimal premise set from which each root could be concluded directly in one round**.

Those are different representation contracts.

In the AND tree:

- basis storage is linear in the number of leaves;
- rooted-circuit table storage is exponential in the number of leaves.

Both represent the same closure law.

## 13. Stage131 interpretation

This establishes a stronger negative boundary than unary transitive redundancy:

> rooted circuits are not merely a slightly redundant rule table; in multi-premise closure systems they can be exponentially larger than a compositional basis because they enumerate minimal premise alternatives.

That same explosion is also an execution resource: each stored circuit gives one-round access from its exact premise set.

The right question is therefore not “delete all redundant circuits,” but “which one-round premise macros are worth materializing under the declared storage/depth/workload contract?”

## 14. Relation to the Horn macro presentation

The parent Horn generation stores selected derived macros, such as fixed-span subtree frontiers.

The complete rooted-circuit table corresponds to materializing **all** minimal premise alternatives.

So selected macro caching sits between:

- local compositional basis;
- complete rooted-circuit table.

This is the multi-premise version of the adjacent-basis / sparse-shortcut / full-transitive spectrum from unary chains.

## 15. Presentation resources now include premise antichain size

For multi-premise systems, a presentation can be expensive because of:

- number of stored rules;
- total premise literals;
- maximum premise width;
- number of alternative minimal premise sets per root;
- execution depth under a declared seed/workload language.

Rooted-circuit count is therefore one specific presentation-complexity coordinate, not a universal semantic-size measure.

## Owner-local assets

- `stage131_rooted_circuit_table_explosion.py`;
- tests for recurrence, width spectrum, explicit enumeration and exponential bounds;
- `STAGE131_ROOTED_CIRCUIT_TABLE_EXPLOSION.{en,zh}.md`.

## Prior art / status

Horn closure, minimal generators, antichains and generating functions are standard prior mathematics/CS. The Enterprise Math value is the Stage131 interpretation and exact binary-AND-tree pressure test on rooted-circuit storage semantics.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.