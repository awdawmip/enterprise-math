# Stage131 — Rooted-Circuit Coverage Workloads

Status: `RESEARCH BRIDGE / NONCANONICAL`

The selective materialization parent is additive for exact inclusion-minimal root-premise queries. Arbitrary seed supersets introduce overlap: several rooted circuits can be contained in the same seed set. In the root-only shortcut model, the exact objective becomes weighted maximum coverage.

## 1. Arbitrary root seed queries

For seed set S that derives the root under the local Horn basis, let

- `d0(S)` be base root depth;
- `f(S)` be workload frequency.

A selected rooted circuit `P=>root` applies iff `P subseteq S`.

If `d0(S)<=1`, direct root materialization has zero execution value. Otherwise any applicable selected circuit makes the root a one-round answer.

## 2. Exact weighted coverage objective

For selected circuit family A:

`F(A)=sum_S f(S)*max(d0(S)-1,0)*1{exists P in A: P subseteq S}`.

Thus each rooted circuit defines a set of workload queries it covers, and each query has weight `f(S)*max(d0(S)-1,0)`.

## 3. Minimal-premise workload is the modular special case

Distinct inclusion-minimal root premises form an antichain.

Therefore every positive-saving minimal-premise query is covered only by its own circuit. Depth-one local-rule circuits have zero materialization value and are explicitly treated as zero-value items.

So the parent additive/knapsack compiler is exactly the disjoint-coverage special case.

## 4. Strict overlap / nonadditivity

On a height-2 AND tree, let

`P={H1_0,L2,L3}`

and

`Q={L0,L1,L2,L3}`.

The seed set `P union Q` has base root depth2 and contains both rooted circuits.

Materializing P alone saves one round. Q alone also saves one round. Materializing both still saves the query only once:

`F({P,Q}) < F({P})+F({Q})`.

This is the smallest explicit transition from additive value to overlapping value in the current tree family.

## 5. Monotone submodularity

Coverage is monotone: adding a circuit cannot uncover a query.

It also has diminishing returns. If `A subseteq B`, then adding a new circuit P after B can only cover a subset of the queries it would newly cover after A.

Hence

`F(A union {P})-F(A) >= F(B union {P})-F(B)`.

The owner exhaustively checks monotonicity/submodularity over the complete height-2 rooted-circuit family under mixed weighted seed workloads.

## 6. Unit-rule budget becomes weighted maximum coverage

With unit cost per materialized root circuit and rule budget B, selective caching is weighted maximum coverage.

The branch provides:

- greedy marginal-gain selection;
- a bounded exact enumerator for tiny circuit families;
- regression comparing greedy and exact on small workloads.

Classical maximum-coverage/submodular approximation results are prior art and are not claimed as new mathematics here.

## 7. Nonuniform storage becomes budgeted submodular coverage

If circuit cost is premise width, premise-literal count, hardware fan-in cost, or another nonuniform charge, the same root-only objective becomes budgeted monotone-submodular coverage.

This differs from the parent's additive bounded knapsack solely because arbitrary seed queries can be covered by several circuits.

## 8. Workload semantics changes the optimization class

The same exact Horn closure and same rooted-circuit opportunity table now induce different optimization problems:

- exact minimal-premise workload -> modular/additive selection;
- arbitrary root seed workload -> weighted coverage/submodular selection;
- reusable intermediate macro execution -> proof-DAG / closure interaction beyond plain coverage.

So the execution workload is part of presentation mathematics, not a post-hoc benchmark.

## 9. Scope boundary

This theorem assumes every selected macro concludes the same root and is used only as a direct root shortcut.

If selected macros can conclude intermediate atoms and enable one another, a query may improve without containing one selected root circuit directly. Then value is no longer a pure coverage function.

That reusable-state regime is the next Stage131 frontier.

## Owner-local assets

- `stage131_circuit_coverage_workload.py`;
- overlap/submodularity/greedy/exact-small tests;
- `STAGE131_CIRCUIT_COVERAGE_WORKLOAD.{en,zh}.md`.

## Prior art / status

Weighted maximum coverage and monotone submodular optimization are standard prior mathematics/CS. The Enterprise Math value is the exact Stage131 mapping from arbitrary seed workloads to circuit-coverage interactions.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.