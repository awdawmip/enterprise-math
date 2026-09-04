# Post-#1161 free research — hidden-fiber capacity lower bound and carrier-interface independence

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / UNBOUNDED-FIBER NECESSITY + EQUIVARIANT-INTERFACE UNDERDETERMINATION / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessors:
- `research_notes/FREE_RESEARCH_POST1161_FIRST_RETURN_ONE_COUNTER_NO_GO_20260904.md`
- `research_notes/FREE_RESEARCH_POST1161_FCC_VISIBLE_COUNTER_LIFT_NO_GO_20260904.md`
- `research_notes/FREE_RESEARCH_POST1161_BRANCH_MEMORY_LATTICE_20260904.md`

## 0. Problem after the visible-FCC no-go

The scalar AGM first-return observer needs the exact imbalance orbit

\[
d\in\mathbb N_0,
\]

while the branch-resolved process needs the rank-one memory lattice

\[
\mathcal M_D=\mathbb Z^D/\mathbb Z\mathbf1.
\]

The visible FCC six-line readout cannot hide the scalar counter without changing established slice observations. The only spatial possibility left by the current theory is information in the unresolved fibers of

\[
\pi:X_{\rm native}\to Y_{\rm FCC}.
\]

This note proves that any such hidden-fiber realization needs unbounded predictive capacity and that equivariance of `pi` alone cannot decide whether the required hidden state exists.

## 1. Many distinct predictive states over one recoalesced terminal at fixed time

At every repeated commuting-diamond block, both branch witnesses have the same typed terminal. Therefore after `m` blocks every branch history of length `m` reaches the same carrier terminal `y_m`.

Fix a positive integer `d<=m` with the same parity as `m`. Define

\[
w_{m,d}
=
A^{(m+d)/2}B^{(m-d)/2}.
\]

Its prefix imbalance first increases and then decreases, but the final imbalance is `d>0`; hence no nonempty prefix is balanced. Thus `w_{m,d}` is still alive at time `m` and has

\[
|z(w_{m,d})|=d.
\]

The allowed positive `d` values are

\[
1,3,\ldots,m \quad(m\text{ odd}),
\]

or

\[
2,4,\ldots,m \quad(m\text{ even}).
\]

There are exactly

\[
\boxed{\left\lceil\frac m2\right\rceil}
\]

of them.

Different `d` have different future first-return signatures because the earliest possible return time is `d`. Therefore, at the **same carrier terminal and same block time** `m`, exact unlabeled AGM-mass prediction requires at least

\[
\boxed{\left\lceil\frac m2\right\rceil}
\]

distinct hidden states.

Swapping `A/B` gives the corresponding negative signed imbalances. For the branch-resolved language the lower bound doubles to

\[
\boxed{2\left\lceil\frac m2\right\rceil}.
\]

## 2. Uniform finite-fiber no-go

Suppose a proposed native-to-carrier lift has a uniform finite fiber bound

\[
|\pi^{-1}(y)|\le K
\]

for every relevant carrier readout `y`, even after adjoining the time index to the visible observation if desired.

Choose `m` such that

\[
\left\lceil\frac m2\right\rceil>K.
\]

At the common observed state `(y_m,m)`, the construction above supplies more than `K` pairwise predictively distinct unlabeled first-return states. They cannot all be represented in the fiber.

Hence

\[
\boxed{
\text{UNIFORM FIXED-FINITE NATIVE->FCC FIBER}
\not\Rightarrow
\text{EXACT ALL-HORIZON AGM FIRST-RETURN MEMORY}.}
\]

For the branch-resolved language the same conclusion follows from the stronger `2 ceil(m/2)` lower bound.

Thus a hidden-fiber realization must have unbounded effective capacity as time/refinement grows, or else it must abandon exact all-horizon prediction.

## 3. Time does not remove the capacity requirement

P000 types time separately from the six spatial axes. Including the block time `m` in the visible state does not solve the collision, because the lower bound above is already **within one fixed time**.

At fixed `m`, the same `(carrier terminal,time)` supports `ceil(m/2)` distinct unlabeled predictive states.

Therefore

\[
\boxed{
\text{TIME INDEX ALONE} \neq \text{IMBALANCE MEMORY}.}
\]

Any exact Markovization needs an additional state coordinate beyond ordinary time order.

## 4. Abstract equivariant-readout interface

Let a group `G` act on a carrier readout set `Y`; for the current FCC interface take `G=S4`. An equivariant native lift at this abstract interface is a `G`-set `X` with an equivariant map

\[
\pi:X\to Y.
\]

The current carrier algebra constrains the action on `Y` but does not specify the fibers of `pi`.

Two opposite lift interfaces always exist abstractly.

### Singleton lift

Take

\[
X_0=Y,
\qquad
\pi_0=\operatorname{id}_Y.
\]

Every fiber is a singleton. No nontrivial hidden counter exists.

### Hidden-scalar lift

Take

\[
X_1=Y\times\mathbb N_0,
\]

with

\[
g\cdot(y,d)=(g\cdot y,d)
\]

and

\[
\pi_1(y,d)=y.
\]

Then `pi_1` is equivariant and the hidden coordinate `d` is a `G`-invariant scalar. The same visible carrier action is recovered after projection.

These are **interface models**, not claims that either is the true P000 native state or that the product lift has the required native six-dimensional semantics.

Their role is logical: carrier action plus equivariant readout alone is compatible with both trivial and nontrivial hidden fibers.

## 5. Interface-independence theorem

Consequently, no theorem whose hypotheses contain only

1. the current FCC carrier `S4` action;
2. the existence of an equivariant readout `pi:X->Y`;
3. the already frozen visible carrier algebra;

can deduce either

`HIDDEN_ROTATION_SCALAR_FIBER_MUST_EXIST`

or

`HIDDEN_ROTATION_SCALAR_FIBER_CANNOT_EXIST`.

The two abstract lift interfaces above satisfy the same visible equivariance contract and have opposite hidden-fiber behavior.

Freeze the exact strength:

\[
\boxed{
\text{FCC CARRIER EQUIVARIANCE ALONE}
\text{ UNDERDETERMINES NATIVE HIDDEN MEMORY}.}
\]

This is an interface-independence statement, not a full model-independence theorem for all of P000.

## 6. What extra native structure would decide the question

At least one stronger native condition is required, for example a theorem specifying:

- injectivity or a bounded-fiber law for the native-to-FCC readout;
- exact native cell identity across overlapping slices;
- an intrinsic native fiber coordinate and its rotation action;
- a local native transition law on the hidden fiber;
- a reconstruction theorem from native incidence/history to the hidden scalar.

Different choices have different consequences:

- injective or uniformly finite fibers rule out the exact AGM counter by the capacity theorem;
- an unbounded trivial-scalar fiber could carry the unlabeled counter but would be genuinely additional hidden state;
- a branch-resolved lift requires at least the reflection-odd rank-one lattice `M_D` or equivalent information, not merely its positive orbit.

## 7. Connection to the preexisting FCC native-lift residue

The frozen P000 FCC rotation return already records

`NATIVE_TO_FCC_EQUIVARIANT_LIFT_NOT_PROVED`.

The AGM successor does not solve that general native-lift problem. It contributes a new lower-bound test that any proposed solution must pass:

\[
\boxed{
\text{AGM scalar lift: fiber predictive capacity at time }m
\ge\left\lceil\frac m2\right\rceil,
}
\]

and, if branch-resolved,

\[
\boxed{
\text{resolved lift capacity at time }m
\ge2\left\lceil\frac m2\right\rceil.
}
\]

A proposed native/FCC bridge with bounded hidden degeneracy is therefore falsified immediately for exact all-horizon AGM reconstruction.

## 8. Executable verification

Task-local checker:

`scripts/check_free_research_agm_hidden_fiber_capacity.py`

It verifies for every `m=1..256` and every parity-compatible positive imbalance `d`:

- the explicit history `A^((m+d)/2)B^((m-d)/2)` has length `m`;
- it has no earlier balanced prefix;
- it ends with imbalance `+d`;
- witness swap produces a still-alive history with imbalance `-d`.

Total explicit histories checked: `33024`.

At `m=256` the certified lower bounds are:

- unlabeled states: `128`;
- branch-resolved states: `256`.

The checker was fetched back from `main` and independently replayed successfully.

## 9. Current terminal boundary of this successor line

Combining the post-#1161 results now gives:

\[
\boxed{
\text{visible FCC six-slot counter lift: impossible},
}
\]

\[
\boxed{
\text{uniform finite hidden-fiber counter lift: impossible},
}
\]

\[
\boxed{
\text{unbounded hidden native fiber: not ruled out by carrier equivariance},
}
\]

\[
\boxed{
\text{existence/meaning of that native fiber: not defined by current P000/FCC foundation}.}
\]

Further progress on **G0 promotion** now genuinely requires new information at the existing `NATIVE_TO_FCC_EQUIVARIANT_LIFT_NOT_PROVED` frontier. More AGM/Catalan algebra cannot decide the missing native fiber ontology.

The exact non-G0 architecture remains complete and executable:

\[
\boxed{
\text{native commuting diamond}
\to
\text{N1 branch-memory lattice / one-counter quotient}
\to
\text{N2 first-return mass}
\to
\text{AGM chord/mean RG}.}
\]
