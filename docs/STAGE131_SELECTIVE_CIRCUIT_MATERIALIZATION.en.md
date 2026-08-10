# Stage131 — Selective Rooted-Circuit Materialization

Status: `RESEARCH BRIDGE / NONCANONICAL`

The complete rooted-circuit table is exponentially large. The corrected width/depth value spectrum makes the next question operational:

> under a finite storage/fan-in/workload budget, which one-round minimal-premise rules should actually be materialized?

For an important task contract—queries whose seed sets are exactly the root's inclusion-minimal premises—the selection problem becomes exact and tractable at the aggregated `(premise width, base depth)` level.

## 1. Minimal root premises form an antichain

Distinct inclusion-minimal premise sets P and Q for the same root cannot satisfy `P proper_subset Q` or `Q proper_subset P`.

Otherwise the larger set would not be inclusion-minimal.

Therefore, if the workload queries are exactly rooted-circuit premise sets, materializing macro `P=>root` cannot accidentally make a different minimal query Q fire through P.

This removes cross-candidate interaction for this specific query contract.

The owner explicitly checks the antichain property on enumerated small AND trees.

## 2. Additive circuit benefit

Let

- `d(P)` = root derivation depth from P under the local basis;
- `f(P)` = frequency/weight of exact query P.

Without the macro, query P costs d(P) rounds. With exact materialized rule `P=>root`, it costs one round.

So gross weighted saving is

`v(P)=f(P)*(d(P)-1)`.

Because minimal queries form an antichain, total benefit of a selected macro set is the sum of the selected candidate benefits under this task contract.

## 3. Type aggregation avoids exponential enumeration

In a balanced AND tree, the corrected value spectrum groups circuits by

`(width,base_depth)`

and records the multiplicity of each type.

If workload frequency is symmetric within each type, every member of one type has identical storage/value data.

The compiler therefore optimizes over a small type table rather than enumerating the exponentially large premise antichain.

## 4. Unit-rule storage budget

If every materialized circuit costs one rule, the exact optimizer is simple:

1. compute benefit per circuit for every type;
2. sort types by benefit;
3. select as many circuits as possible from the highest-benefit types until the rule budget is exhausted.

Ties can prefer narrower fan-in without changing weighted benefit.

For uniform frequency, benefit is simply `d-1`, so deepest circuits are selected first.

## 5. Premise-literal storage budget

If storing `P=>root` costs `|P|` premise literals, selection becomes a bounded 0/1 knapsack:

- item cost = premise width;
- item benefit = `f(P)*(d(P)-1)`;
- multiplicity = number of circuits of that `(width,depth)` type.

The executable planner binary-decomposes type multiplicities, so multiplicities such as hundreds of thousands do not require enumerating one DP item per circuit.

## 6. Fan-in cap gives an exact speedup ceiling

The value-spectrum theorem says exact depth-d circuits have minimum width `d+1`.

Therefore with maximum allowed premise fan-in W,

`d_max(W)=min(h,W-1)`

for W>=2.

The maximum one-round saving available under that cap is

`max(0,d_max(W)-1)`.

So hardware or rule-language fan-in limits translate directly into a maximum materializable proof-depth shortcut.

## 7. Narrow deepest circuits exist in exponential multiplicity

At exact depth d, the minimum-width circuits have width `d+1`.

Their count is exactly

`2^(d-1)`.

Reason: a minimum-width depth-d premise must put a minimum-width depth-(d-1) configuration on exactly one child side and use the other child atom directly. There are two choices of side, giving the recurrence

`C_d=2 C_(d-1)`, `C_1=1`.

Thus even a tight fan-in cap can leave multiple high-speedup candidates.

Example: depth5 has16 width6 circuits. Any one of them saves four rounds for its exact premise query.

## 8. Best benefit per premise literal under uniform workload

For an exact depth-d circuit,

`benefit <= d-1`

and

`width >= d+1`.

So its per-premise-literal efficiency is at most

`(d-1)/(d+1)`.

The minimum-width depth-d circuits attain this bound.

Moreover

`(d-1)/(d+1)`

increases strictly with d.

Therefore, under uniform per-circuit query weight, the narrowest circuits from the deepest available depth class have the globally best direct round-saving per premise literal.

This is a ranking theorem, not a complete knapsack theorem: integer budget leftovers and type multiplicities can still make mixed selections optimal.

## 9. Height-5 unit-rule example

The height5 root contains depth counts

`1,3,21,651,457653`.

With uniform query frequency and a budget of10 circuit rules, the compiler chooses ten depth5 circuits. By the narrow-width tie rule it chooses width6 instances first.

Resources:

- 10 stored circuit rules;
- 60 premise literals;
- max fan-in6;
- gross weighted round saving40.

The selected fraction of the complete table is tiny even though every selected macro comes from the highest-value depth class.

## 10. Height-5 premise-literal example

With premise-literal budget60 and uniform frequency, the exact bounded-knapsack planner also chooses ten width6/depth5 circuits:

- total premise storage60;
- gross saving40.

The type-level DP reaches this answer without enumerating458329 individual root circuits.

## 11. Workload can reverse depth priority

Depth is only potential saving. Actual benefit is frequency times saving.

A frequently queried depth2 circuit can dominate a rarely queried depth4 circuit.

The compiler accepts type-level frequency weights and selects according to weighted benefit rather than structural depth alone.

Thus selective materialization is workload-relative in exactly the same sense as the chain shortcut presentation.

## 12. Scope of the additive theorem

The antichain argument makes benefits additive only for the declared workload of **exact minimal-premise root queries**.

If queries are arbitrary supersets, one selected circuit may help many seed sets. If selected macros are allowed to participate in further reusable derivations, macros can interact. Then the global value function is no longer a sum of independent candidate values.

That stronger continuation-state optimization belongs to a later proof-DAG / Horn macro compilation layer.

## 13. Stage131 interpretation

The complete rooted-circuit table is the maximal one-round cache. The selective compiler turns it into a budgeted execution layer:

`semantic basis`

`-> exponentially large circuit opportunity spectrum`

`-> workload/storage/fan-in filter`

`-> selected execution macros`.

This is the positive use of the rooted-circuit minimality boundary: do not mistake the complete table for the minimal law, but also do not discard its shortcuts blindly.

## Owner-local assets

- `stage131_selective_circuit_materialization.py`;
- unit-rule, fan-in, knapsack and antichain tests;
- `STAGE131_SELECTIVE_CIRCUIT_MATERIALIZATION.{en,zh}.md`.

## Prior art / status

Knapsack, antichains and workload-weighted caching are standard prior mathematics/CS. The Enterprise Math value is the Stage131 selective materialization compiler over the rooted-circuit width/depth opportunity spectrum.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.