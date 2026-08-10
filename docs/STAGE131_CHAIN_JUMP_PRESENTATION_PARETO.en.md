# Stage131 — Chain Jump Presentations and the Storage / Inference-Depth Frontier

Status: `RESEARCH BRIDGE / NONCANONICAL`

The unary-chain counterexample already established that rooted circuits are a one-round minimal-premise table, not a globally minimal rule basis: transitive unary implications are semantically redundant relative to adjacent/Hasse edges.

The next question is operational rather than semantic:

> if derived implications are allowed to be stored deliberately, how much inference depth can they buy?

For a chain this becomes an exact finite presentation problem.

## 1. Chain law

Fix

`x_0 => x_1 => ... => x_n`.

The exact closure law is simply

`x_i => x_j` for every `i<j`.

Three objects must be distinguished:

- semantic closure law;
- stored implication presentation;
- synchronous forward-chaining depth under that presentation.

Different presentations can realize the same closure law with different storage/depth costs.

## 2. Translation-invariant jump presentation

Choose jump lengths

`L subseteq {1,...,n}`

with `1 in L` so every adjacent target remains reachable.

For each `ell in L`, store every valid positional rule

`x_i => x_(i+ell)`

for `0<=i<=n-ell`.

This keeps the law exact: every stored jump is already a transitive consequence of the adjacent chain, and the length1 rules preserve the original closure.

## 3. Exact storage law

Jump length ell occurs at exactly

`n-ell+1`

source positions.

Therefore

`S_n(L)=sum_(ell in L)(n-ell+1)`.

This nonuniform positional cost matters. A long jump is cheaper than a short jump because it fits at fewer positions.

## 4. Exact inference-depth law

Starting from x_0, a derivation path to x_t is exactly a decomposition

`t=ell_1+...+ell_r`, `ell_i in L`.

Hence the earliest synchronous round at which x_t can appear is the minimum number of jump lengths summing to t.

Let

`lambda_L(t)=minimum coin count representing t from L`.

Then

`round(x_t)=lambda_L(t)`

and the full closure depth is

`D_n(L)=max_(1<=t<=n) lambda_L(t)`.

The executable layer independently simulates synchronous implication closure and verifies equality with the dynamic-programming coin count.

## 5. Adjacent/Hasse endpoint

For

`L={1}`:

`S_n=n`,

`D_n=n`.

This is the minimal transitive-reduction style basis for the chain and the slowest endpoint considered here.

## 6. Full transitive/rooted-circuit endpoint

For

`L={1,2,...,n}`:

all transitive implications are stored.

Then

`S_n=n(n+1)/2 = binom(n+1,2)`

and

`D_n=1`.

This is the one-round complete unary circuit table.

It is semantically redundant relative to the adjacent basis but operationally depth-optimal.

## 7. Binary jump construction

Take

`L={1,2,4,8,...}`

through n.

A distance t is reached in exactly `popcount(t)` jumps, so

`D_binary(n)=floor(log2(n+1))`.

The rule count is

`J(n)=sum_(d=1)^n bit_length(d)`

with closed form, writing `m=floor(log2 n)`,

`J(n)=(m+1)(n+1)+1-2^(m+1)`.

Thus binary jumps give an exact

`O(n log n) storage / O(log n) inference-depth`

construction between the two endpoints.

## 8. Binary is not generically Pareto-optimal

Because jump lengths have positional costs, the binary length basis can be dominated.

Smallest sharp example: n=3.

### Binary lengths `{1,2}`

storage:

`3+2=5`,

depth2.

### Lengths `{1,3}`

storage:

`3+1=4`,

depth2.

The longer jump is cheaper because it occurs at only one source position.

Therefore binary jumps are a useful closed-form circuit presentation, not the universal Stage131 optimum.

## 9. General Stage131 optimization problem

Inside the translation-invariant jump class, the exact design problem is:

minimize jointly

`S_n(L)=sum_(ell in L)(n-ell+1)`

and

`D_n(L)=max_t lambda_L(t)`

over jump sets `L` containing1.

This is a weighted additive-basis / coin-system optimization problem.

The weights arise from how many positional implication rules each jump length induces.

## 10. Exact small-chain Pareto fronts

The executable layer enumerates every jump set for `n<=20`.

Representative storage/depth frontiers:

### n=3

`(3,3), (4,2), (6,1)`.

### n=4

`(4,4), (5,3), (6,2), (10,1)`.

### n=6

`(6,6), (7,5), (8,4), (9,3), (12,2), (21,1)`.

### n=8

`(8,8), (9,7), (10,6), (11,5), (12,4), (15,3), (19,2), (36,1)`.

Some storage/depth pairs may have several different jump sets. The frontier is therefore a presentation family, not one canonical basis.

## 11. Two-length family already gives a strong middle regime

Take

`L={1,q}`, `2<=q<=n`.

Storage is

`S=2n-q+1`.

Writing

`n=Aq+R`, `0<=R<q`,

the full closure depth is exactly

`D=A+max(q-2,R)`.

This follows because the shortest representation of t uses as many q-jumps as possible and fills the remainder with unit jumps.

Choosing q around the square-root scale gives an O(n)-storage / O(sqrt(n))-depth regime, already far from both endpoints.

## 12. Geometric/radix jump families

For base b>=2, take

`L={1,b,b^2,...}`

through n.

Storage is

`len(L)(n+1)-sum(L)`,

roughly `O(n log_b n)`.

Derivation depth is maximum base-b digit sum through n.

When `n=b^m`, the exact depth is

`m(b-1)`.

Binary is the b=2 specialization. Larger b uses fewer jump scales and typically trades lower storage for larger inference depth.

## 13. n=1024 resource landscape

Several exact presentations for the same chain closure law:

### Adjacent

- storage1024;
- depth1024.

### Best two-jump presentation

Within `{1,q}`, the lexicographically best depth/storage choice is `q=38`:

- storage2011;
- depth62.

### Base3 geometric

- storage6082;
- depth12.

### Binary

- storage9228;
- depth10.

### Full transitive table

- storage524800;
- depth1.

These are exact resource points, not a claim that every listed point lies on the unrestricted global frontier.

## 14. Rooted-circuit interpretation

The chain proves a useful correction to “redundancy.”

A transitive implication can be:

- **semantically redundant** — deleting it does not change closure;
- **operationally useful** — storing it shortens the number of inference rounds.

Rooted circuits naturally retain many such execution shortcuts because they are organized by one-round minimal premises rather than by global rule-basis minimality.

So the negative boundary on global minimality is not a defect to remove; it exposes a storage/execution resource axis.

## 15. Semantic basis versus execution presentation

The adjacent basis answers:

> what is the smallest obvious generator/basis for this chain relation?

A jump presentation answers:

> which derivable implications should be cached so that closure executes under a chosen depth/storage budget?

These are different optimization problems.

The first is semantic compression. The second is presentation engineering.

## 16. Relation to A2/P023 presentation work

The same architecture appeared in exact action macros:

- generator transitions minimize primitive stored law;
- precomputed macros spend storage to reduce execution depth;
- circuit presentations such as binary powers can beat flat macro tables.

Stage131 chain jumps are the implication-rule analogue of that presentation theory.

## 17. Next mathematical frontier

The exact finite chain problem now invites stronger tools:

- additive bases and restricted coin systems;
- shortcut/spanner design on ordered DAGs;
- circuit/DAG sharing;
- nonuniform jump sets varying by source position;
- storage weights other than one rule = one unit;
- expected-depth objectives under nonuniform query distributions;
- multi-premise Horn/closure systems beyond unary chains.

The binary construction is therefore a bridge, not an endpoint.

## Owner-local assets

- `src/enterprise_math/stage131_chain_jump_presentation.py`;
- `tests/test_stage131_chain_jump_presentation.py`;
- `docs/STAGE131_CHAIN_JUMP_PRESENTATION_PARETO.{en,zh}.md`.

## Prior art / status

Transitive reduction/closure, shortcutting, graph spanners, coin systems and additive bases are standard prior mathematics/CS. The Enterprise Math value is the explicit Stage131 interpretation:

> **a closure-law basis and an execution-efficient rule presentation are different objects, and semantically redundant transitive rules form a controllable storage/inference-depth resource.**

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.