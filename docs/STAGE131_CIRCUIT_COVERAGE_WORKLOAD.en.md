# Stage131 — Rooted-Circuit Coverage Workloads

Status: `RESEARCH BRIDGE / NONCANONICAL`

The selective materialization parent is additive when every workload query is exactly one inclusion-minimal root premise. Allow arbitrary seed supersets and candidate interactions appear immediately—but in a very specific form: weighted maximum coverage.

## 1. Arbitrary seed-set queries

Let S be any seed set that already derives the root under the local Horn law.

Let

`d0(S)`

be its base root derivation depth and `f(S)` its workload frequency.

A materialized rooted-circuit macro `P=>root` can fire on S exactly when

`P subseteq S`.

If at least one selected circuit can fire, the root answer becomes one round.

## 2. Exact coverage objective

For selected circuit family A, the gross weighted round saving is

`F(A)=sum_S f(S)*(d0(S)-1)*1{exists P in A with P subseteq S}`,

with zero contribution from queries whose base depth is already0 or1.

So each candidate circuit P covers the workload queries whose seed sets contain P, and each query has weight

`f(S)*(d0(S)-1)`.

This is exactly a weighted coverage function.

## 3. Strict nonadditivity appears as overlap

If two circuits P and Q both lie inside the same workload seed set S, then each one individually can reduce that query to one round, but selecting both cannot save the same query twice.

Hence

`F({P,Q})`

can be strictly smaller than

`F({P})+F({Q})`.

The owner includes a height-2 AND-tree seed query with two distinct depth-2 circuits contained in one base-depth-2 seed set; each candidate alone gives saving1 and the pair still gives saving1.

## 4. Monotonicity

Adding a materialized circuit can only cover more queries, never uncover an already covered query.

Thus

`A subseteq B -> F(A)<=F(B)`.

## 5. Submodularity / diminishing returns

Let `A subseteq B` and candidate circuit P not already in B.

The new queries covered by adding P to B are a subset of the new queries covered by adding P to A, because B has already covered at least as many queries.

Therefore

`F(A union {P})-F(A)`

`>= F(B union {P})-F(B)`.

So F is monotone submodular.

The branch exhaustively verifies the inequality over every candidate subset of the full height-2 rooted-circuit family under a mixed weighted workload.

## 6. Minimal-premise workload is the modular special case

When every workload seed set is itself an inclusion-minimal root premise:

- distinct circuits are incomparable by inclusion;
- a positive-saving minimal query is covered only by its own circuit;
- depth-1 local rules have zero materialization value.

Hence positive-value coverage sets are disjoint singletons and F becomes additive/modular.

This recovers the parent unit-rule/knapsack compiler exactly.

## 7. Unit-rule budget becomes maximum coverage

If every selected circuit costs one rule and the budget is B, the arbitrary-seed problem is weighted maximum coverage with B selected sets.

This is standard prior optimization. The branch provides:

- a literal greedy marginal-gain compiler;
- a bounded exact enumerator for tiny circuit families as an oracle;
- regression showing strict diminishing returns and budget-monotone greedy value.

The standard greedy approximation theory belongs to prior submodular optimization rather than a new Enterprise Math theorem.

## 8. Premise-literal cost becomes budgeted coverage

If circuit P costs `|P|` premise literals or another nonuniform storage charge, the same objective becomes a budgeted monotone-submodular coverage problem.

This is structurally different from the additive bounded knapsack in the parent minimal-premise workload.

The change is caused entirely by query overlap, not by any change in the closure law.

## 9. Query language changes the optimization class

The same rooted-circuit candidates and same exact Horn world therefore produce different optimizer classes:

### Exact minimal-premise root queries

`additive/modular value -> sorting or knapsack`.

### Arbitrary root seed queries

`overlapping coverage -> monotone submodular maximum coverage`.

### Reusable intermediate macro execution

Selected rules can alter derivation depths of intermediate atoms and help one another compose. The objective moves beyond root-only coverage into proof-DAG / closure interaction.

Thus workload semantics is not a secondary detail; it determines the mathematical presentation problem.

## 10. Height-2 overlap witness

For the height-2 tree, one circuit is

`{H1_0,L2,L3}`

and another is

`{L0,L1,L2,L3}`.

The seed union

`{H1_0,L0,L1,L2,L3}`

has base root depth2 and contains both circuits.

Materializing either circuit makes the query one round. Materializing both still saves only one round.

This is the smallest explicit transition from additive circuit value to overlap value in the current AND-tree family.

## 11. Root-only scope boundary

The coverage theorem assumes selected circuits all conclude the same root and are used only as direct root shortcuts.

If a selected macro concludes an intermediate atom, it can reduce the enabling time of another selected macro. Then a query can improve even without containing one selected root circuit as a subset.

That reusable-state regime is no longer plain coverage and is the next Stage131 frontier.

## 12. Stage131 interpretation

The selective materialization hierarchy is now:

`complete rooted-circuit opportunity table`

`-> exact minimal-premise workload: additive value`

`-> arbitrary seed workload: submodular coverage`

`-> reusable proof state: interacting derivation macros`.

The semantic closure law stays fixed throughout. Only the declared execution/workload contract changes.

## Owner-local assets

- `stage131_circuit_coverage_workload.py`;
- coverage, overlap, greedy/exact-small and submodularity tests;
- `STAGE131_CIRCUIT_COVERAGE_WORKLOAD.{en,zh}.md`.

## Prior art / status

Weighted maximum coverage and monotone submodular optimization are standard prior mathematics/CS. The Enterprise Math value is the exact Stage131 mapping from arbitrary seed workloads to coverage interactions.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.