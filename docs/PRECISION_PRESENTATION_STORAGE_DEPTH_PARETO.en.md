# Exact Presentation Storage / Execution-Depth Pareto

Status: `RESEARCH BRIDGE / NONCANONICAL`

Once a future law has been recovered exactly, “how much of it should be stored explicitly?” becomes a new precision-resource question. Precomputing more derived transition rules does not add semantic law, but it can reduce future execution depth.

This note formalizes that tradeoff in the literal macro-table representation class and connects it to the readout/state/presentation distinction.

## 1. Generator presentation

Fix an exact state representation of dimension b and k named generator actions with exact transition matrices

`B_a`.

The minimal literal generator presentation stores the k matrices themselves.

A word

`w=a_1...a_h`

is executed by h successive generator applications.

Storage is small; execution depth grows with word length.

## 2. d-macro presentation

Choose macro depth d>=1.

Store the exact transition matrix

`B_w`

for every literal action word w of length1 through d.

These macros are not new physical rules. Each is exactly derivable from the generators by composition.

The number of stored literal macro rules is

`S(k,d)=sum_(i=1)^d k^i`.

For k>1:

`S(k,d)=k(k^d-1)/(k-1)`.

For k=1:

`S(1,d)=d`.

## 3. Exact execution-depth law

Any word of length h can be split into consecutive chunks of length at most d.

Therefore it can be executed using

`D(h,d)=ceil(h/d)`

stored macro transitions.

The executable layer verifies this for noncommuting matrices, so the result does not depend on commutativity.

## 4. Pareto endpoints

### Generator endpoint

`d=1`:

- stored rules = k;
- execution blocks for length h = h.

### Full horizon macro endpoint

`d=h`:

- stored rules = `sum_(i=1)^h k^i`;
- execution blocks =1.

For k>1 this exchanges linear execution depth for exponential literal-table storage.

Neither endpoint is universally superior.

## 5. Nondominated macro depths

Storage strictly increases with d, while `ceil(h/d)` changes only at certain thresholds.

A depth that increases storage without reducing worst-case execution blocks is dominated inside the literal macro-table class.

For `k=2`, `h=12`, the nondominated macro depths are

`d = 1,2,3,4,6,12`,

with

`stored rules = 2,6,14,30,126,8190`

and

`execution blocks = 12,6,4,3,2,1`.

This is a concrete exact storage/depth frontier.

## 6. Semantic redundancy versus execution value

Every macro matrix is semantically redundant relative to the exact generators:

`B_w` can be recomputed from the generator matrices.

But the stored macro is not operationally redundant if execution depth or latency matters.

This is the same structural lesson as transitive rule tables: a rule can add no new closure law while still reducing the number of inference/execution rounds.

Therefore distinguish:

- **semantic basis minimality**;
- **execution presentation efficiency**.

## 7. Reusable transition macros versus terminal answer tables

For each word w, one can store either:

### Transition macro

`B_w`.

It updates state and supports arbitrary later continuation.

### Terminal readout row

`C B_w`.

It answers the terminal query for w but does not by itself retain the successor state needed for an arbitrary suffix.

The readout table may use fewer scalars per word, but it is a weaker contract.

This is exactly the readout-versus-executable-state distinction at the presentation level.

## 8. Scalar storage model

For state dimension b, one literal transition matrix stores `b^2` scalars.

A d-macro transition table therefore stores

`b^2 S(k,d)`

matrix scalars before sparse/compressed encodings.

If the current observation has c output rows, a full terminal readout table through horizon h stores roughly

`c b S(k,h)`

scalars.

The latter can be smaller per word but cannot replace reusable transition state when continuation is required.

These are representation-class counts, not hardware byte guarantees.

## 9. State dimension and macro depth are orthogonal axes

The previous linear-predictive generation may reduce a b-state exact branching machine to an r-dimensional exact linear trace state.

If macro transitions are stored in the chosen state representation, the same macro-depth law applies with matrix cost scaled by the square of the state dimension:

`branching macro storage ~ b^2 S(k,d)`;

`linear predictive macro storage ~ r^2 S(k,d)`.

Thus two distinct optimizations compose:

1. reduce the state representation dimension/type;
2. precompute longer macros to reduce execution rounds.

They should not be conflated.

## 10. Two-dimensional presentation Pareto surface

An exact presentation can therefore be located by coordinates such as

`(state representation, macro depth)`.

Changing state representation changes the cost of every stored rule.

Changing macro depth changes how many rules are stored and how many runtime compositions remain.

The same future law can occupy many points on this surface without changing semantic truth.

## 11. Relation to local-code precision

A third independent axis is the local coefficient code used to reconstruct the generator matrices in the first place.

The full pipeline can therefore trade among:

- local observation/coding range;
- state representation size/type;
- stored macro depth;
- runtime execution depth.

A larger direct numeric code is not the only way to make a task faster; one can also retain structure or precompute derived transitions.

## 12. Relation to Stage131-style transitive rule tables

The present theorem is the dynamic presentation analogue of storing transitive closure rules:

- a small generator/basis table minimizes stored law primitives but requires repeated execution;
- a denser closure/macro table stores derivable rules to shorten execution.

The exact numeric formulas differ by representation, but the resource principle is the same:

`semantic redundancy can buy execution-depth reduction`.

## 13. Representation-class boundary

This theorem is **not** a global lower bound over every possible program/circuit representation.

A specific action semigroup may admit:

- algebraic relations;
- normal forms;
- repeated-squaring strategies;
- DAG/circuit sharing;
- sparse matrices;
- symmetry compression;
- specialized hardware execution.

Those can dominate the literal table.

The theorem owns only the exact Pareto inside the declared literal macro-table class.

## 14. Foundation consequence

“Minimal rule set” and “best exact presentation” are different questions.

A semantically minimal generator set can be an execution-poor presentation. A denser exact presentation can be preferable when depth/latency is itself a resource.

Hence presentation precision must be evaluated at least by

`storage × execution depth × state representation × numeric range`,

not by rule count alone.

## Owner-local assets

- `src/enterprise_math/presentation_storage_depth_pareto.py`;
- `tests/test_presentation_storage_depth_pareto.py`;
- `docs/PRECISION_PRESENTATION_STORAGE_DEPTH_PARETO.{en,zh}.md`.

## Prior art / status

Memoization, transition monoids, macro actions, time-memory tradeoffs and precomputation are standard prior mathematics/CS. The project-specific value is the exact precision/presentation resource routing and its connection to semantic versus operational redundancy.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.