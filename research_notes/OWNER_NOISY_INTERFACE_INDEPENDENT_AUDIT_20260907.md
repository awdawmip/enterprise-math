# Owner budgeted-noise interface: independent audit

Status: `PASS / LOCAL_INTERFACE_AUDIT`.
Auxiliary work package: `/root/exact_solver`; no registered research identity,
official task/claim, Driver disposition, or Foundation promotion is asserted.

Read-only reviewed files and SHA256:

- `experiments/owner_joint_observer_20260907/noisy_recovery.py`:
  `52638faba84a41562642bddb73b5bf22bb9138b919c617dd77e009e8d7022f11`.
- `experiments/owner_joint_observer_20260907/test_noisy_recovery.py`:
  `1d88c0b8580647df70ee5eeb9e0a30fd81319da9686f17515909b2979617dbc5`.

The previously audited Phase-I certificate solver and finite raw-marginal
stability theorem are dependencies. This review inspected the new consumer
and tests, rather than restarting either dependency's audit.

## Mathematical compilation and result scope

The implementation correctly compiles the union of every candidate-cell
projection and every explicitly supplied noisy address, separately for all
20 labeled raw axis triples. It retains explicit zeros. Outside that union
both the predicted mass and supplied data are zero, so no residual term is
omitted. In particular, neither noise outside the carrier nor a candidate
projection missing from the data is silently discarded. Signed rational
noise and inconsistent table totals are admitted without treating them as
nonnegative BRC populations.

For a mass vector `v>=0`, the equations are
`A v + r_plus - r_minus = y` and
`sum(r_plus+r_minus)+slack=budget`, with all variables nonnegative.
They are equivalent to `||A v-y||_stack,1<=budget`:

- Any compiled solution gives `|y-A v|<=r_plus+r_minus` componentwise.
- Given a fit within budget, take positive/negative parts of `y-A v` and
  put the unused budget in the nonnegative slack variable.

The signs, variable indices, final budget row, and empty-carrier case agree
with this equivalence. The interface is a feasibility test at a supplied
budget; its explicit `optimality_claimed=False` and `uniqueness_claimed=False`
are appropriate. It does not compute or promise the minimum residual.

The independent original-equation certificate verifier runs before either a
success or an infeasibility result is interpreted. A Farkas obstruction is
returned only for this compiled **declared carrier and budget** and retains
the rows, rhs, candidate cells, observation labels, and witness. It must not
be read as nonexistence on all raw X6 cells or at a larger budget.

## Actual BRC residual and conditional error bound

The reported distribution uses only the verified nonnegative mass columns.
Its observed tables are then rebuilt through the existing BRC observer.
The actual residual uses a freshly constructed union of those output tables
and copied noisy input tables. It does not reuse the compiler's row list,
assume the auxiliary residual variables are minimal, or replace actual
residual with the requested budget.

Consequently `(111/20)*(truth_noise_budget+actual_residual)` has the stated
conditional interpretation. The returned premises require a finite
nonnegative truth with at most seven distinct spatial cells, the same anchor
and labeled raw observer, and the declared stacked truth-noise bound.
`truth_premises_verified=False` correctly avoids certifying an unknown truth.
After a successful fit, that theorem does not require the truth's support to
lie in the declared carrier; such membership would instead be a sufficient
condition relevant to existence of a fit at an adequate budget. The interface
keeps these two roles separate.

## Failure handling and resource bounds

Exact input checks reject floats, bools, malformed labels, and duplicate
candidate cells. Coordinate lists are copied into immutable tuples.
Candidate, observation, and dense-tableau entry caps are enforced before
dense compilation or solver invocation. They raise a resource exception
with no mathematical conclusion. The advertised tableau count is correctly
`height*(width+height+1)`; it is expressly not a total-memory, pivot-count,
bit-complexity, or wall-time guarantee. Execution exceptions propagate.
Forged primal and dual witnesses are rejected as arithmetic failures rather
than becoming a successful fit or an infeasibility theorem.

## Independently executed evidence

1. `python -m unittest test_noisy_recovery -v` in the experiment directory:
   all **9 tests PASS**. Their substantive cases cover negative/off-carrier
   noise, inconsistent totals, implicit zeros, auxiliary cancellation,
   unknown truth outside the carrier, forged witnesses, and resource failure.
2. A separate inline exact probe used seed `202609071909`, eight single-cell
   systems and eight two-cell systems. Inputs included missing candidate
   addresses, signed rational noise, and explicit off-carrier values.
   The one-variable minimum came from a constrained median; the two-variable
   minimum came from exact intersections of the objective's kink lines and
   the nonnegative quadrant boundaries. Neither oracle called Phase I or
   reused the interface's compiled matrix.
3. Each of those 16 independently solved systems was tested at its exact
   optimum, at `optimum+1/13`, and at `max(0,optimum-1/7)`: **48 checks PASS**,
   comprising 32 feasible fits and 16 independently verified Farkas failures.
   Feasible outputs also matched a direct independent raw-table residual
   calculation and the conditional-bound arithmetic.

No substantive defect was found in the reviewed bytes. These finite tests
supplement the exact compilation argument; they do not establish runtime
performance for larger carriers or convert budgeted fitting into optimization.
