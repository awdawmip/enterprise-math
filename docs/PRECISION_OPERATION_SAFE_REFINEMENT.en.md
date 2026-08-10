# Coarsest Operation-Safe Semantic Refinement

Status: `RESEARCH BRIDGE / NONCANONICAL`

A semantic precision join can sometimes be realized by refining state distinctions rather than changing representation type. For finite states and a finite family of total unary future operations, there is a unique **coarsest** observational refinement that makes all required operations descend safely.

## 1. Problem

Let X be a finite fine-state set.

Let `E_0` be the current observational equivalence/partition.

Let U be a finite family of total unary operations on X that the declared future language must execute on the quotient.

An operation u is safe for equivalence E when

`x E y -> u(x) E u(y)`.

We seek the largest equivalence

`E_* subseteq E_0`

preserved by every `u in U`.

This is the least additional state precision needed to realize the declared operation capability.

## 2. Refinement operator

Define

`Phi_U(E)`

`= E intersect intersection_(u in U) (u x u)^(-1)(E)`.

Equivalently, within each current partition block, split states by the vector of current target blocks reached under all required operations.

Then iterate

`E_(k+1)=Phi_U(E_k)`

from `E_0`.

Every step refines or leaves the partition unchanged.

## 3. Finite termination

If one step is strict, at least one partition block splits and the block count increases.

On |X| finite states, the number of strict steps is therefore at most

`|X| - number_of_blocks(E_0)`.

So the iteration reaches a fixed point after finitely many semantic-repair steps.

The fixed point is an exact stop certificate for this total-unary operation family.

## 4. Fixed point is operation-safe

At a fixed point

`E_*=Phi_U(E_*)`.

Therefore for every `u in U`:

`E_* subseteq (u x u)^(-1)(E_*)`,

which is exactly

`x E_* y -> u(x) E_* u(y)`.

Every required operation descends uniquely to the quotient by `E_*`.

## 5. Coarsest/maximal property

Let F be any equivalence satisfying

`F subseteq E_0`

and preserved by every operation in U.

Then by induction:

`F subseteq E_k`

for every k.

Indeed, if `F subseteq E_k`, operation preservation gives

`F subseteq (u x u)^(-1)(E_k)`

for every u, so

`F subseteq Phi_U(E_k)=E_(k+1)`.

Hence

`F subseteq E_*`.

Therefore `E_*` is the **largest** operation-safe equivalence contained in the original observational equivalence, equivalently the **coarsest state refinement** that realizes all required operations.

This repair is unique.

## 6. One split need not be enough

Operation safety can reveal distinctions only after downstream blocks have themselves split.

Sharp four-state cascade:

initial

`{0,1}|{2,3}`.

One operation:

`0->2`, `1->3`, `2->0`, `3->3`.

First iteration splits only the downstream block:

`{0,1}|{2}|{3}`.

Now targets of0 and1 land in distinct blocks, so the second iteration splits the first block:

`{0}|{1}|{2}|{3}`.

Thus semantic repair requires closure to a congruence fixed point, not one local response signature in general.

## 7. Relation to semantic precision joins

Suppose a task join demands:

- at least the state distinctions already present in `E_0`;
- operation capabilities U.

If the representation class allows arbitrary finite partition refinement of X, the join is always realizable: replace `E_0` by `E_*`.

Moreover the theorem gives the canonical minimal lift.

This is a positive counterpart to the scalar-modulus nonrealizable join.

## 8. Two different outcomes for nonrealizable current joins

The semantic-preorder line now distinguishes two cases.

### A. Join realizable by state splitting

Required operations are ordinary functions on the same fine state X.

Then the coarsest operation-safe refinement `E_*` gives a canonical state lift.

### B. Join not realizable in the current representation class

Example: require mod `p^2` numeric detail and generic integral-domain branch reflection while restricting states to scalar quotients `Z/MZ`.

No modulus works. Merely splitting residue classes inside that representation family cannot restore the missing algebraic law.

One must change representation type, e.g. retain explicit witness/branch data.

So “increase precision” can mean either:

- refine the existing state partition to the required congruence; or
- leave the representation family and add a new semantic channel.

## 9. Relation to safe-operation monoids

For one quotient, the safe operation family consists of transformations preserving its equivalence.

Here the direction is reversed: U is declared first, and the quotient is refined until U lies inside its safe-operation family.

Thus safe-operation analysis and semantic refinement are adjoint design questions:

`given quotient -> which operations survive?`

versus

`given required operations -> what is the coarsest quotient that supports them?`

This provides a direct constructive bridge between the A2 safe-operation algebra and the task-relative semantic precision preorder.

## 10. DOMAIN / partial-operation boundary

The theorem assumes total unary operations on one fixed fine-state set.

For partial/guarded operations, definedness is itself future-visible state. One must first retain the DOMAIN channel or use the partial-operation quotient machinery. Splitting only by target blocks is insufficient if some operation is undefined on one member of an equivalence class.

So the result is a total-operation core, not a replacement for FQ-006/P024 guarded semantics.

## 11. Prior-art boundary

Congruence refinement, deterministic automaton partition refinement and invariant equivalences are standard prior mathematics/computer science. The Enterprise Math value is the semantic precision interpretation:

> **when a future operation requirement can be repaired by state detail alone, there is a unique coarsest operation-safe state refinement; otherwise the representation type itself must change.**