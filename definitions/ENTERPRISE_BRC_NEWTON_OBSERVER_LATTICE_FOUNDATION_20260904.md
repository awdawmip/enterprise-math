# Enterprise Math — BRC Newton Observer Lattice Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION CANDIDATE / MAIN-BACKED RESEARCH / OBSERVER-LEASE TYPED`
Effective: `2026-09-04`
Parent: `ENTERPRISE_BRC_NEWTON_FIBER_QUOTIENT_FOUNDATION_20260904.md`
Evidence: PR #1202

## 1. Scope and prior art

This addendum continues WBRC-T56 from one fixed observer to a family of declared Newton observers and finite declared future schedules.

Finite-dimensional kernel lattices, coordinate projections and linear observability are classical mathematics. No generic novelty claim is made. The Enterprise/BRC content is the exact observer-lease discipline attached to the rational-valuation Newton carrier:

- safe quotient depends on which residual coordinates are declared observable;
- richer coordinate observers admit only finer quotients;
- under a frozen Newton schedule, farther finite-horizon observation can only refine the safe quotient;
- frozen-schedule linearity does not imply that perturbed states autonomously select the same roots, multiplicities or scales.

## 2. WBRC-T57 — coordinate-observer/kernel anti-lattice

Fix the WBRC-T56 source Taylor position set `I`, residual coordinate set

`C = {(rho,k)}`,

and the surjective full fiber-sum map

`Pi : Q^I -> Q^C`.

For any declared coordinate observer `O subset C`, let

`P_O : Q^C -> Q^O`

be coordinate restriction and define

`Phi_O = P_O o Pi`,
`K_O = ker Phi_O`.

Because every residual coordinate in C has a source position, Pi is surjective. Therefore

`Q^I / K_O ~= Q^O`,
`rank Phi_O = |O|`,
`dim K_O = |I|-|O|`.

Two source states are O-equivalent exactly when their T56 fiber sums agree on the coordinates in O.

### Observer inclusion reverses safe-kernel inclusion

If

`O1 subset O2`,

then

`K_O2 subset K_O1`.

Thus a richer observer admits no coarser safe quotient.

The lattice laws are exact:

`K_(O1 union O2) = K_O1 intersection K_O2`,

and, using surjectivity of Pi,

`K_(O1 intersection O2) = K_O1 + K_O2`.

Hence the finite coordinate-observer lattice and this family of safe kernels are anti-isomorphic.

The T56 full-residual observer is `O=C`. The edge-only observer is

`E = {(rho,k) in C : rho=1}`.

Whenever strict residual coordinates exist,

`E proper subset C`

and therefore

`K_C proper subset K_E`.

Canonical ID: `WBRC-T57`.

## 3. WBRC-T58 — frozen-schedule finite-horizon observability

Let V_t be a finite rational residual coefficient space. Freeze a finite schedule

`S = ((x_0,r_0,theta_0),...,(x_(h-1),r_(h-1),theta_(h-1)))`.

For one declared step, substitution

`x = x_t + theta_t^s y`

followed by division by `theta_t^(r_t s)` is linear in the coefficient state. On one monomial `(sigma,k)` it gives

`sum_(j=0)^k binom(k,j) x_t^(k-j) (sigma theta_t^(j-r_t))^s y^j`.

After exact equal-coordinate aggregation this is a rational linear map

`T_t : V_t -> V_(t+1)`.

Let `P_t` be a declared exact linear observer on V_t. Define the horizon-h signature

`H_h(v) = (P_0 v, P_1 T_0 v, ..., P_h T_(h-1)...T_0 v)`.

Then

`K_h = ker H_h`

satisfies

`K_(h+1) subset K_h`.

Equivalently, looking farther into a fixed declared future cannot make the operation-safe quotient coarser.

The quotient dimension is the exact rational rank of the stacked finite-horizon observability matrix.

### Edge-observer witness

For the six residual coordinates

`(1,0), (1,1), (1,2), (1/2,1), (1/4,0), (1/16,0)`

and two frozen steps

`x_t=-1`, `r_t=2`, `theta_t=1/2`,

with scale-one edge observation at every time, main-backed PR #1202 verified

`rank H_0 = 3`,
`rank H_1 = 5`,
`rank H_2 = 6`,

so kernel dimensions are

`3 -> 1 -> 0`.

The `(1/2,1)` coordinate first becomes visible at horizon one; `(1/16,0)` first becomes visible at horizon two.

Canonical ID: `WBRC-T58`.

## 4. Observer lease decision tree

Freeze:

```text
COMPLETE_RESIDUAL_JET_OBSERVER
    -> WBRC-T56 full fiber-sum quotient

DECLARED_RESIDUAL_COORDINATE_SUBSET O
    -> WBRC-T57 coordinate observer quotient K_O

DECLARED_FIXED_NEWTON_SCHEDULE + FINITE FUTURE OBSERVER
    -> WBRC-T58 horizon kernel K_h

AUTONOMOUSLY RESELECT ROOT/MULTIPLICITY/SCALE AFTER PERTURBATION
    -> NEWTON CHAMBER-STABILITY FRONTIER
```

The last branch is not promoted here.

## 5. Hard negative/scope boundaries

```text
FULL_RESIDUAL_OBSERVER != UNIVERSAL OBSERVER
EDGE_ONLY_OBSERVER != FULL_RESIDUAL_OBSERVER
COORDINATE_OBSERVER_LATTICE != ALL NONLINEAR OBSERVERS
FROZEN_NEWTON_SCHEDULE != AUTONOMOUS_NEWTON_SELECTION
LONGER_HORIZON_REFINES_OR_EQUALS; IT DOES NOT COARSEN
SCHEDULED_LINEAR_SUBSTITUTION != CLAIM THAT PERTURBED STATES FOLLOW THE SAME SCHEDULE
SOURCE_TAYLOR_PROVENANCE != EXPLICIT_POSITIVE_BRANCH_PROVENANCE
FINITE_RATIONAL_SCOPE_ONLY
```

Canonical negative IDs: `WBRC-N54..N60`.

## 6. Tool routing

No new top-level family is created. The companion T0 subtool is

`t0.weighted_brc_newton_observer_lattice`.

Production code provides:

- exact coordinate-observer normalization, signature and equivalence;
- observer join/meet and rank/kernel dimension;
- exact frozen scheduled Newton substitution over rational residual coefficient states;
- scale-one edge observation;
- finite-horizon edge signatures;
- exact observability matrices, ranks and kernel dimensions for a fixed schedule.

It does not autonomously select roots, multiplicities or scales.

## 7. Validation

Main-backed PR #1202 verified:

- all 32 observers of a five-coordinate residual witness;
- 3,072 observer-pair lattice/rank checks;
- full-residual kernel dimension 2 versus edge-only dimension 4;
- strict frozen-horizon ranks `(3,5,6)` and kernel dimensions `(3,1,0)`;
- 729 exact coefficient vectors against direct scheduled substitution;
- exact scheduled-step linearity.

## 8. Research frontier after T58

The next lower-complexity frontier is **autonomous Newton chamber stability**: characterize exact coefficient regions on which the selected root, multiplicity and Newton scale remain fixed. Only inside such a certified chamber may a frozen-schedule future observer be interpreted as the actual autonomous Newton future of every allowed perturbation.

A separate, higher-algebraic-complexity frontier remains the genuine multi-generator translated-root carrier.
