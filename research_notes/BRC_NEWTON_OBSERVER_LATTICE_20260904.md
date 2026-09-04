# BRC Newton observer lattice and finite-horizon linear observability

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T55/T56, main-backed PR #1196 and Foundation PR #1198

## 1. Problem

WBRC-T56 fixes one observer: the complete residual Newton jet.  Under that observer the exact source-state quotient is the `(rho,k)` fiber-sum map.  But T56 also exhibited a strict boundary: an edge-only observer is weaker and therefore permits a coarser quotient.

The next question is not another Newton asymptotic formula.  It is:

> how do exact safe quotients change when the declared Newton observer changes, and when the observer is allowed to look a finite number of declared Newton operations into the future?

This note gives two exact answers:

1. coordinate-projection observers form a finite Boolean lattice whose kernel quotients form the opposite lattice;
2. under a **frozen Newton schedule** (roots, multiplicities and scales declared in advance), finite-horizon future observers are ordinary exact rational linear observability maps, so safe kernels can only shrink as the horizon grows.

The second statement deliberately does **not** linearize autonomous Newton root/scale selection.  A perturbed state need not naturally select the same schedule.

## 2. Coordinate observer lattice

Fix the T56 source Taylor positions `I`, residual coordinates

`C = {(rho,k)}`,

and the full fiber-sum map

Pi : Q^I -> Q^C.

Every coordinate in C has at least one source position, so Pi is surjective.

For any declared coordinate observer `O subset C`, let

P_O : Q^C -> Q^O

be coordinate restriction and define

Phi_O = P_O o Pi,
K_O = ker Phi_O.

Then

Q^I / K_O ~= Q^O,
rank Phi_O = |O|,
dim K_O = |I|-|O|.

Thus two source states are equivalent for observer O iff their fiber sums agree on every coordinate in O; all unobserved residual coordinates may vary arbitrarily.

### Order reversal

If O1 subset O2, then

K_O2 subset K_O1.

A richer observer therefore admits only a finer safe quotient.

Because Pi is surjective, the lattice operations are exact:

K_(O1 union O2) = K_O1 intersection K_O2,
K_(O1 intersection O2) = K_O1 + K_O2.

Hence coordinate observers and their safe kernels are anti-isomorphic finite lattices.

For the five-coordinate T56 witness, all `2^5=32` observer subsets and all ordered observer pairs can be checked exactly over Q.

## 3. Full residual versus edge-only

Let

E = {(rho,k) in C : rho=1}.

Then the T56 full residual observer is O=C, while the current-edge observer is O=E.

If strict coordinates exist, E is a proper subset of C and therefore

K_C proper subset K_E.

This restates the T56 edge-only witness as a general dimension theorem:

full-residual quotient dimension = |C|,
edge-only quotient dimension = |E|.

No claim is made that either observer is universally preferable.  The declared future questions determine the lease.

## 4. Frozen Newton schedule as a linear operation family

Now start from a finite residual Newton coefficient space V over Q.

Freeze a finite schedule

S = ((x_0,r_0,theta_0), ..., (x_(h-1),r_(h-1),theta_(h-1))).

For one declared step, substitution

x = x_t + theta_t^s y

followed by division by `theta_t^(r_t s)` is linear in the coefficient state.  On each monomial `(sigma,k)` it gives

sigma^s x^k
 ->
 sum_(j=0)^k binom(k,j) x_t^(k-j)
 (sigma theta_t^(j-r_t))^s y^j.

After equal-coordinate aggregation this is an exact rational linear map

T_t : V_t -> V_(t+1).

Crucially, T_t is a **declared scheduled substitution**.  It does not assert that every perturbed coefficient vector would autonomously choose `(x_t,r_t,theta_t)`.

## 5. Finite-horizon observer

Let P_t be any exact linear observer on V_t (for example the scale-one edge coefficients).  Define the horizon-h signature

H_h(v) = (
  P_0 v,
  P_1 T_0 v,
  P_2 T_1 T_0 v,
  ...,
  P_h T_(h-1)...T_0 v
).

Then

K_h = ker H_h
    = intersection_(t=0)^h ker(P_t T_(t-1)...T_0).

Therefore

K_(h+1) subset K_h.

Looking farther into the declared future can only refine, never coarsen, the operation-safe quotient.

The exact quotient dimension is the rational rank of the stacked finite-horizon observability matrix.  This is classical finite-dimensional linear observability specialized to exact Newton substitution coordinates.

## 6. Strict three-level Newton witness

Use six initial residual coordinates:

- `(1,0)`, `(1,1)`, `(1,2)`;
- `(1/2,1)`, `(1/4,0)`;
- `(1/16,0)`.

Freeze two scheduled Newton substitutions with

x_t=-1,
r_t=2,
theta_t=1/2

for t=0,1, and observe only scale-one edge coefficients at every time.

Then:

- horizon 0 sees exactly the three current-edge coordinates, rank 3;
- horizon 1 additionally sees `(1/2,1)` and `(1/4,0)`, rank 5;
- horizon 2 additionally sees the deep `(1/16,0)` coordinate, rank 6.

Thus the safe kernel dimensions strictly descend

3 -> 1 -> 0.

This is an explicit exact example where a coefficient invisible to the present edge becomes observable only after two declared Newton substitutions.

## 7. Relation to T6

T6 supplies the general future-observation principle: states may be merged only when the declared future operation family cannot distinguish them.

The present result is not executable reuse of `operation_quotient.py`:

- T6 implementation uses finite deterministic state sets and endomaps;
- the Newton observer problem uses finite rational vector spaces and exact linear maps.

The correct reuse is conceptual plus the same observer-first discipline.  The executable specialization is ordinary rational matrix/kernel arithmetic.

## 8. Hard boundaries

- COORDINATE_OBSERVER_LATTICE != ALL POSSIBLE NONLINEAR OBSERVERS.
- FULL_RESIDUAL != EDGE_ONLY.
- FROZEN_NEWTON_SCHEDULE != AUTONOMOUS_NEWTON_SELECTION.
- HORIZON_REFINEMENT != CLAIM THAT EVERY PERTURBED STATE FOLLOWS THE SAME ROOT/SCALE PATH.
- SAFE_QUOTIENT_IS_OBSERVER_AND_OPERATION_LEASE_TYPED.
- SOURCE_TAYLOR_PROVENANCE and EXPLICIT_POSITIVE_BRANCH_PROVENANCE remain distinct carriers.
- No generic control-theory novelty, complete Puiseux solver, multi-generator algebraic field, signed branch interference or infinite-state claim is made.

## 9. Next frontier

Two non-equivalent continuations remain:

1. **chamber-stable autonomous observability**: characterize coefficient neighborhoods on which the Newton root/multiplicity/scale schedule itself remains fixed, so the frozen linear observer becomes an actual autonomous future observer;
2. **genuine multi-generator translated roots**: when old algebraic coefficient data remain live and a new irrational root cannot be absorbed into the current generator.

The first is the lower-complexity continuation because it extends T56/T6 without changing the algebraic coefficient carrier.
