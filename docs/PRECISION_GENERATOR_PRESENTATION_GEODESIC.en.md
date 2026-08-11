# Minimum Precision Design as a Generator-Presentation Geodesic

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The design/execution separation has a direct algebraic form. A generator presentation equips the semantic operation algebra with a word-length or weighted-cost geometry. Minimum precision design can then be the shortest expression of a target semantic effect.

For the Set-Cover OR semilattice this target geodesic is **exactly** Minimum Set Cover.

## 1. Presented OR semilattice

Let the semantic effect state be an m-bit universe mask.

Each primitive action i has mask `a_i` and acts on semantic effects by

`x -> x OR a_i`.

Identity is mask0. The semantic target for full precision is the full mask

`Omega=2^m-1`.

A literal word `i_1...i_h` evaluates forward to

`a_i1 OR ... OR a_ih`.

This forward evaluation is formulaically trivial.

## 2. Generator presentation induces a Cayley geometry

Build the directed right Cayley graph on semantic masks:

`x --i--> x OR a_i`.

Give each generator unit cost. The presentation-induced distance to a reachable effect t is the shortest word length producing t.

Because OR generators are idempotent and commute, repeated occurrences can be removed and order is irrelevant. Therefore shortest words correspond exactly to generator subsets.

## 3. Full-precision design is target distance

For target `Omega`, a generator subset reaches Omega iff its candidate sets cover the whole universe.

Hence

`d_A(0,Omega)=minimum Set Cover cardinality`.

The branch verifies this on every 3-element / 3-generator incidence family.

Thus minimum precision-preserving capability design is literally a geodesic problem in the semantic algebra **after a generator presentation has been chosen**.

## 4. Weighted design is weighted geodesic synthesis

Assign nonnegative cost `c_i` to each primitive generator.

The same Cayley graph with edge cost `c_i` has shortest path cost

`min sum c_i`

over generator subsets whose union reaches the target.

This is exactly weighted Set Cover for the full mask.

The owner cross-checks weighted Dijkstra against bounded brute-force weighted-cover oracles.

## 5. Same abstract monoid, different word metric

The abstract semantic algebra alone does not determine this distance.

For universe size m compare two `m+1`-generator presentations of the same full Boolean semilattice `2^[m]`:

- singleton generators plus one duplicate singleton;
- singleton generators plus one full-universe generator.

Both generate the same `2^m` semantic effects with the same OR law.

Yet

`d_A(0,Omega)=m`

in the duplicate catalogue and

`d_B(0,Omega)=1`

in the full-action catalogue.

The distance gap is `m-1`.

Therefore presentation-induced word metric is not an invariant of the abstract generated monoid.

## 6. Forward execution versus inverse synthesis

The two directions are structurally different.

### Forward

Input: one generator word.

Output: its semantic effect.

For OR semilattice:

`effect = bitwise OR of masks`.

This is linear work in input length and logarithmic parallel depth.

### Inverse

Input: target effect Omega.

Output: minimum-cost generator word/subset reaching Omega.

For the same family this is Set Cover.

Thus a simple forward homomorphism can have a difficult minimum-preimage problem.

## 7. Why explicit-state shortest path does not contradict NP-hardness

If the full semantic monoid is explicitly expanded, it has `2^m` mask states. Standard BFS finds the unit-cost target geodesic in time polynomial in that **expanded** graph size.

But the Set Cover input is compact: m universe coordinates and k generator masks can be stored in O(mk) incidence bits.

The explicit semantic state space is exponential in m.

So the NP-hardness is compatible with easy explicit BFS:

`compact generator presentation -> exponentially large semantic Cayley state space`.

The difficulty is succinct inverse synthesis, not local transition evaluation.

## 8. Presentation size versus semantic state-space size

For k singleton generators on m=k universe elements:

- dense generator incidence proxy: `m*k=m^2` bits;
- explicit semantic effect states: `2^m`.

At m=20 the explicit OR monoid already has over one million states while the generator incidence remains only400 bits under this simple proxy.

This gap explains why “just search the semantic monoid” is not a compact algorithmic representation.

## 9. Target-specific design

The geodesic viewpoint also clarifies that design is relative to a semantic target, not only to the generator algebra.

A partial target mask may have a much shorter geodesic than the full precision target. Different future tasks can therefore induce different design costs inside the same presented algebra.

This is another task-relative precision effect.

## 10. Geodesic synthesis versus generated-algebra closure

Generating the whole semantic algebra and reaching one required target are not the same optimization problem.

The Set-Cover precision target asks for one distinguished full-coverage effect. A generator subset may be optimal for that target without being a minimal generating set of the entire monoid.

This distinction is important when importing terminology from classical generator-rank theory.

## 11. General architectural form

The Set-Cover semilattice suggests the broader pattern:

`free syntax / primitive actions`

`--forward semantic homomorphism-->`

`exact operation algebra`.

Forward execution evaluates the homomorphism.

Inverse design asks for a minimum-resource preimage of a declared semantic target or target region.

There is no generic reason for inverse synthesis complexity to match forward evaluation complexity.

## 12. Stage131 consequence

Stage131 resource analysis should therefore include **presentation geodesic cost** as an upstream resource separate from runtime law representation.

A complete pipeline can have:

- hard target synthesis in the primitive catalogue;
- easy formulaic execution after synthesis;
- additional storage/depth Pareto for representing the chosen execution law.

These costs belong to different phases and should not be collapsed into one scalar “rule complexity”.

## Owner-local assets

- `src/enterprise_math/generator_geodesic_synthesis.py`;
- `tests/test_generator_geodesic_synthesis.py`;
- this bilingual theorem note.

## Prior art / status

Cayley graphs, word metrics, shortest paths, succinct state spaces and Set Cover are standard prior mathematics/CS. P023/A2 retains precision/future-signature ownership. This Draft owns only the explicit target-geodesic interpretation of minimum semantic design.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
