# Stage131 — Workload-Weighted Shortcut Presentations

Status: `RESEARCH BRIDGE / NONCANONICAL`

Worst-case inference diameter is only one execution contract. If a Stage131 system sees a nonuniform distribution of premise/target queries, the best exact shortcut presentation should depend on that workload.

This generation keeps the semantic closure law fixed and changes only the operational objective.

## 1. Weighted query language

For chain

`0<1<...<n`,

assign nonnegative query weight

`mu(i,j)`

to each comparable pair `i<j`.

For exact stored presentation E, define weighted execution cost

`C_mu(E)=sum_(i<j) mu(i,j) dist_E(i,j)`.

After dividing by total query mass, obtain expected inference depth.

This is a different task contract from worst-case directed diameter.

## 2. One-shortcut exact gain theorem

Start from adjacent edges and add one shortcut

`a->b`, `b-a>=2`.

A query `i->j` can use the shortcut iff

`i<=a` and `b<=j`.

When it can, the adjacent path length `j-i` becomes

`(a-i)+1+(j-b)`.

Therefore every spanning query saves exactly

`b-a-1`

rounds, independent of i and j.

Hence the total weighted gain is

`Gain_mu(a,b)`

`=(b-a-1) * sum_(i<=a,j>=b) mu(i,j)`.

The optimal one-shortcut presentation maximizes

`shortcut length saved x query rectangle mass`.

This is an exact closed objective, not a simulation heuristic.

## 3. Query locality changes which derived implication is valuable

The formula makes the Stage131 caching rule explicit:

- a long shortcut has high per-query saving;
- but it is valuable only if many important queries span it.

Thus one should not rank transitive implications by semantic redundancy alone. Their operational value is workload-sensitive.

## 4. Single-query extreme

If all workload mass lies on one nonadjacent query

`i->j`,

the unique maximum-saving shortcut is exactly

`i->j`.

It reduces that declared query from `j-i` rounds to one.

The rest of the chain can remain almost as slow as before.

For endpoint-only workload `0->n`, storing direct edge `0->n` gives expected depth1 but global worst-case diameter `n-1`.

This is optimal for the declared workload and poor for the all-pairs continuation contract.

## 5. Uniform all-pairs workload

Give every comparable pair unit weight.

For one shortcut a->b define positive segment lengths

`x=a+1`,

`y=b-a-1`,

`z=n-b+1`.

Then

`x+y+z=n+1`.

There are exactly

`x*z`

queries spanning the shortcut, and each saves y rounds. Hence total gain is

`xyz`.

## 6. Closed uniform optimum

Among positive integer triples with fixed sum, the product xyz is maximized exactly when the parts differ pairwise by at most one.

Therefore the uniform one-shortcut optimum is obtained by splitting `n+1` into three nearly equal positive parts and translating those parts back into shortcut coordinates.

No O(n^2) shortcut search is needed; the branch provides a closed constructor from the balanced triples.

## 7. Uniform expected depth formula

The adjacent chain has total all-pairs distance

`n(n+1)(n+2)/6`

and pair count

`n(n+1)/2`.

So adjacent expected depth is

`(n+2)/3`.

If `P_3(n+1)` is the maximum product of three positive integer parts summing to `n+1`, the optimal one-shortcut expected depth is

`(n+2)/3 - P_3(n+1)/(n(n+1)/2)`.

The product is obtained from the balanced parts:

- `3q`: `q^3`;
- `3q+1`: `(q+1)q^2`;
- `3q+2`: `(q+1)^2 q`.

## 8. Uniform optimum also achieves worst-case one-shortcut optimum

For the same segment variables, the one-shortcut worst-case diameter is

`max{x+y-1, y+z-1, x+z-1}`

`= n - min{x,y,z}`.

A balanced triple maximizes the minimum part and therefore attains the optimal one-shortcut worst-case diameter

`floor((2n+1)/3)`.

So every uniform expected-depth optimum is also worst-case optimal.

The converse need not hold: worst-case optimality only needs the smallest segment as large as possible, while product optimality further balances the larger segments.

## 9. n=1024 uniform example

Adjacent presentation:

- 1024 rules;
- uniform expected depth342;
- worst-case diameter1024.

One balanced shortcut gives:

- 1025 rules;
- expected depth `34899219/131200`, approximately266.0;
- worst-case diameter683.

Thus one stored derived implication improves both average and worst-case execution substantially under uniform workload.

## 10. Nonuniform workload can intentionally trade worst-case depth away

For an endpoint-only query on the same long chain, direct `0->1024` makes the expected workload depth exactly1 using the same one extra rule.

But its global diameter remains1023.

Therefore two n+1-rule presentations can occupy very different points in

`expected workload depth x worst-case continuation depth`.

No single “best shortcut” exists until the task contract declares the objective.

## 11. More than one shortcut: interaction becomes nonadditive

With several shortcuts, shortest paths can compose multiple cached rules. Their gains are no longer the sum of independent rectangle scores.

The branch therefore includes an exact small-n budget optimizer:

- adjacent edges are forced;
- choose any optional shortcut subset within the rule budget;
- compute literal shortest paths;
- minimize weighted query cost;
- tie-break by worst-case diameter and then storage.

This is exhaustive for small chains and serves as a pressure-test oracle, not a scalable optimizer.

## 12. Three-axis operational frontier

A nonuniform presentation should be evaluated at least by

`stored rules`

`x expected workload inference depth`

`x worst-case continuation diameter`.

These axes can move independently.

A workload curve may first reduce expected depth to its minimum1 and then use additional storage only to reduce worst-case continuation depth.

So even after the query workload is fully optimized, continuation capability can remain a separate resource.

## 13. Relation to semantic precision

The closure law is unchanged throughout. Query weights do not alter which implications are true.

They alter which semantically redundant implications are worth caching.

Thus workload belongs to **presentation optimization**, not to semantic closure truth.

This is another form of future-language relativity:

- same exact world;
- same exact closure;
- different declared usage/query distribution;
- different optimal stored presentation.

## 14. Relation to TC-spanner prior art

Worst-case bounded-hop shortcuts align with TC-spanner/shortcut graph objectives.

The workload-weighted objective changes the operational criterion from maximum reachable-pair distance to weighted/expected shortest-path cost.

The generic shortest-path optimization viewpoint is prior graph/algorithmic territory; the project-specific role is to expose query workload as another Stage131 precision-presentation resource.

## Owner-local assets

- `src/enterprise_math/stage131_chain_workload_shortcuts.py`;
- `src/enterprise_math/stage131_uniform_workload_shortcut.py`;
- `tests/test_stage131_chain_workload_shortcuts.py`;
- `docs/STAGE131_CHAIN_WORKLOAD_SHORTCUTS.{en,zh}.md`.

## Prior art / status

Shortest-path shortcutting, weighted query optimization and graph design are standard prior mathematics/CS. The Enterprise Math value is the explicit Stage131 rule-caching interpretation and exact one-shortcut workload theorem.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.