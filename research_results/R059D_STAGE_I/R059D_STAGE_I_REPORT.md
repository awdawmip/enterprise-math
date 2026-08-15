# R059D Stage I — Uniform Relay-Coupling Family / Symmetry-Constrained Attenuation

Researcher-ID: `EM-R059D-4C7E21`

Taskbook source: `4e2224f4ebbbe1b9f5c4d50b06de37aed491d146`

Frozen parent Stage-H head: `c1da1cd2b9b4967077badd6c5f09b1fc3f874f66`

## Disposition

`UNIFORM_RELAY_COUPLING_FAMILY_FOUND`

Stage I finds one stationary local syntactic rule graph with one finite integer parameter `lambda` that has both an arbitrary-N regenerative/system-spanning regime and an arbitrary-N bounded-localized regime under the same real tagged adjacency intervention.

This is a mathematical relay-coupling axis only.

## Uniform family

Freeze

`D_lambda = |lambda| + 1`.

The controller uses only current `CURRENT_INGRESS`, current local source support (`S_SELF`, hence `M_FRONT` on the canonical front collision), fixed channel actions, and the exact local divisibility predicate

`M_FRONT mod D_lambda = 0`.

At a canonical one-resident relay collision:

1. every incoming relay-ingress source-tag lineage receives `V` and leaves relay-direction support;
2. the resident `START` lineage receives `RELAY_DIRECTION` iff `D_lambda | M_FRONT`;
3. otherwise that resident remains `HOLD`.

Hence the exact causal-support transfer is

`Phi_lambda(M) = 1` if `D_lambda | M`,

`Phi_lambda(M) = 0` otherwise.

All lambda values use exactly the same clauses and action graph. There is no `if lambda==special then controller A else controller B` table.

## Real-I3 regimes

The real tagged perturbations `G_I3_H_STEP` and `G_I3_H_INV_STEP` both seed `M_FRONT=1`.

For `lambda=0`, `D_lambda=1`, so

`1 -> 1 -> 1 -> ...`.

This is a nonzero recurrent relay class and gives

`RESPONSE_PARTICIPANT_COUNT_CLOSURE = N`

for every `N>=2`, `q>=2`.

Thus:

`SYSTEM_SPANNING_REGENERATIVE_RESPONSE`.

The recruitment timing is the Stage-G relay timing:

`E_SPAN = q*(N-1)-1`.

For every finite `lambda != 0`, `D_lambda>=2` and `D_lambda` does not divide the real-I3 seed `M=1`, so

`1 -> 0`.

The first resident is causally recruited at the collision boundary, but no outgoing relay front survives. Therefore:

`RESPONSE_PARTICIPANT_COUNT_CLOSURE = min(N,2)`,

with closure generation `q-1` for `N>=2`.

For `N>2` this is:

`BOUNDED_LOCALIZED_RELAY_RESPONSE`.

The same laws hold under the H_INV mirror.

## Permutation-equivariant attenuation obstruction

Suppose M incoming co-moving source-tag lineages have exactly the same controller-visible signature.

A deterministic permutation-equivariant rule cannot select a unique proper nonempty subset of these M lineages to continue. Any selected subset must be invariant under the transitive permutation action, hence must be either empty or all M.

Therefore unique causal-support transfers such as

- `M -> M-1`,
- `M -> M-d` for `0<d<M`,
- `M -> floor(M/2)`

cannot be realized by selecting a proper subset of the indistinguishable incoming cohort without lineage identity or another genuine symmetry-breaking local state.

CPBC branching does not evade the obstruction. It can generate raw histories containing different k-subsets, but permutation equivariance requires the full orbit of equivalent k-subsets, and CPBC aggregate source-lineage support contains all M incoming source identities. Raw-history splitting is therefore not unique causal-support attenuation.

Legal symmetry-preserving one-resident operations include all-incoming continuation, all-incoming extinction, resident join (`M->M+1`), and resident replacement after the whole incoming cohort settles (`M->1` or `M->0`).

The Stage-I positive family uses exactly the final mechanism; it never chooses one named incoming lineage.

Freeze:

`PERMUTATION_EQUIVARIANT_RELAY_ATTENUATION_OBSTRUCTION = ESTABLISHED`.

## Large-M classification

`M_FRONT` was already a frozen exact current local integer, so the Stage-I large-M lane is valid.

For arbitrary initial `M>=1`:

- `lambda=0`: `M -> 1 -> 1 -> ...`.
- `lambda!=0`: if `D_lambda | M`, then `M -> 1 -> 0`; otherwise `M -> 0`.

Thus all nonzero lambda values extinguish after at most two transfer evaluations from arbitrary M, including all frozen `M~10^36` probes.

There is no ordered intrinsic M threshold. For `lambda!=0`, the first step is a divisibility residue partition.

## Parameter boundary

Under the real-I3 seed:

- `lambda=0`: participant count `N`;
- `lambda!=0`: participant count `min(N,2)`.

This is an exact:

`RELAY_COUPLING_PARAMETER_BOUNDARY`

at `|lambda|=0` versus `|lambda|>=1`.

Within the real-I3 domain the response count is nonincreasing in `|lambda|`; freeze this only as:

`RELAY_COUPLING_PARAMETER_RESPONSE_ORDER`.

It is not an N- or M-intrinsic macro/micro boundary.

`INTRINSIC_N_MACRO_MICRO_CROSSOVER = NOT_IDENTIFIED`.

## Required control replay

The frozen Stage-H controls remain controls:

- G1: regenerative, no parameter axis;
- CAP_C: same C-grammar but every finite C is eventually zero, so it lacks a finite recurrent endpoint;
- AMPLIFY: amplifying, no parameter axis;
- PERIOD_12: nonzero periodic, no parameter axis;
- EVENTUAL_ZERO: zero, no parameter axis;
- BRANCHING_MIXED: mixed, no parameter axis.

They are not used as a disjoint-controller pseudo-parameterization.

## Scheduler robustness

`S_SYNC` and `S_ALL_ORDERS_SNAPSHOT` have the same `Phi_lambda`, response class, participant count, and H/H_INV mirror classification.

Execution-order Cartesian multiplicity remains diagnostic only.

## Firewalls

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

Even though a uniform mathematical parameter axis exists, no physical calibration has been established.

## Checker

The deterministic checker validates the frozen family graph, parameter registry, exact transfer law over broad integer boxes, huge-M stress, real-I3 response formulas, both schedulers/mirrors, the permutation-invariant-subset theorem, CPBC orbit-union distinction, and kill gates.

Final parent immutability is additionally verified by GitHub compare before checkpoint freeze.

## Stop

`STOP_FOR_DRIVER_REVIEW`
