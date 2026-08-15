# R059D Stage J — Graded Relay-Coupling / Endogenous Localization Scale

Researcher-ID: `EM-R059D-4C7E21`  
Taskbook source: `4cf097ff21a9275805fb8ab49cefdd5ff42c4c92`  
Frozen parent Stage-I head: `03650b38df5950b86cb2636db9e43094683b1bc8`

## Disposition

`ENDOGENOUS_GRADED_RELAY_COUPLING_FAMILY_FOUND`

Stage J finds a single stationary syntactic family, `J_PHASE_HIT_RELAY_GATE`, that passes the stronger graded-response gate under the same real tagged adjacency perturbation.

The family does **not** use a propagation counter. Its graded state is the current relational ingress phase carried by the front.

## Frozen graded state

For the H orientation define the current exact phase-support vector

`F=(F_H,F_V,F_V_INV)`,

where each component is the number of source-tag lineages currently supported at the relay-front packet with the corresponding current ingress.

On the real-I3 reachable positive class exactly one phase component is positive and the total phase support is one. Define

- `p=0` for current ingress H,
- `p=1` for current ingress V,
- `p=2` for current ingress V_INV.

This is reconstructible from current state. It contains no tag identity, recruitment index, time, target, horizon, or remaining range.

## Exact transport certificate

Away from a recruitment collision the stationary transport actions are

- `p=0`: `V`,
- `p=1`: `V_INV`,
- `p=2`: `H`.

Thus the three-transition words are

- `p=0`: `V, V_INV, H`,
- `p=1`: `V_INV, H, V`,
- `p=2`: `H, V, V_INV`.

Using only the frozen relational relations `V V_INV = id` and `H V = V H`, every word is exactly one H relation and ends in the same current ingress phase with which it began.

Therefore each phase is transported by one H adjacency every three transition events, and the phase itself is regenerated.

The H_INV mirror is obtained by the fixed channel relabeling `H <-> H_INV`.

## Uniform lambda family

Freeze one rule family:

`J_PHASE_HIT_RELAY_GATE`.

Lambda occurs only in one exact local predicate

`STOP_lambda(p) := [p + lambda = 0]`.

At a one-resident collision:

1. every incoming source lineage in the current phase takes the same H_INV terminal action;
2. if `STOP_lambda(p)` holds, the resident stays HOLD and the relay ends;
3. otherwise the resident launches phase `p+1 mod 3`.

No proper subset of an indistinguishable incoming phase class is selected.

The syntactic clause graph and action alphabet are identical for all lambda.

## Exact transfer law

At successful collisions:

`p -> p+1 mod 3`.

At a stop hit:

`p -> ZERO`.

Starting from real `G_I3_H_STEP`, the seed has `p0=0`, so the successful phase sequence is

`0,1,2,0,1,2,...`.

The j-th resident collision is at

`e_j = 3*(q*j - 1)`.

## Exact response grades

For all integers `q>=2`, `N>=2`:

- `lambda=0`:
  `P_lambda(N,q)=min(N,2)`;
- `lambda=-1`:
  `P_lambda(N,q)=min(N,3)`;
- `lambda=-2`:
  `P_lambda(N,q)=min(N,4)`;
- `lambda notin {0,-1,-2}`:
  `P_lambda(N,q)=N`.

Hence for every `N>=5`:

`2 < 3 < 4 < N`.

This gives one system-spanning response law and three distinct bounded-localized laws in one stationary syntactic family.

The H_INV mirror has the same response formulas.

## Why this is not a direct parameter cap

The family never compares lambda with recruitment count, elapsed generations, M magnitude, or a monotone counter.

The current phase is a genuine ingress class and repeats after three successful relays:

`0 -> 1 -> 2 -> 0`.

Thus it cannot encode remaining range monotonically. Lambda selects whether a currently realized relational phase is absorbing. Parameters outside `{0,-1,-2}` never stop even after arbitrarily many relays.

Stage-H `CAP_C` is retained only as a lower-tier control and is retyped under the stricter Stage-J gate as `DIRECT_PARAMETER_CAP_CONTROL`, because its reachable `M_FRONT=1,2,...` is exactly the recruitment-depth counter and C is the stop cap.

## Symmetry theorem

Stage-I proper-subset obstruction remains active inside each phase class.

If M source-tag lineages share the same current ingress and visible signature, within-class `S_M` equivariance still forbids selecting exactly k of them for `0<k<M`.

Stage J avoids this obstruction by using **already distinguishable current ingress classes**, not identity. Incoming members of the occupied phase all settle identically; the resident START tag is relationally distinguishable and may launch the successor.

A one-signature stationary quotient with no evolving current state remains binary: if the signature transmits once it repeats and transmits forever; otherwise it stops immediately. A nontrivial evolving current relational/count state is therefore required to escape that binary quotient without direct cap. The three-phase ingress state is an explicit sufficient realization; global minimum state cardinality is not claimed.

## Large integer stress

After the phase-state transfer theorem was frozen, Stage J stresses exact single-phase vectors

`F = M*e_p`

for `M` around `10^36` and frozen neighbors.

For every `M>=1`, all M indistinguishable incoming lineages settle together. The resident either creates one unit successor phase or ZERO depending only on `p+lambda=0`.

Therefore arbitrary huge M maps in one collision to either

`e_(p+1)` or `ZERO`.

No ordered M threshold exists.

Freeze:

`NO_ORDERED_INTEGER_BOUNDARY`.

## Parameter order

Define the frozen phase-hit time

`tau(lambda)=1-lambda` for `lambda in {-2,-1,0}`,
and `tau(lambda)=infinity` otherwise.

Then

`P_lambda=min(N,tau(lambda)+1)`

for finite tau, and `P_lambda=N` otherwise.

The invariant phase-hit preorder is

`lambda=0  ≺  lambda=-1  ≺  lambda=-2  ≺  unmatched lambda`.

Ordinary signed-integer ordering or `|lambda|` ordering is **not** promoted; it is parameterization-dependent.

Freeze:

`RELAY_COUPLING_PHASE_HIT_RESPONSE_ORDER`.

## Scheduler robustness

`S_SYNC` and `S_ALL_ORDERS_SNAPSHOT` use the same collision snapshot. The incoming phase class and resident each have deterministic snapshot actions, so execution order cannot change the phase transfer, stop predicate, or participant closure.

Cartesian order multiplicity remains diagnostic only.

## Crossover firewall

Freeze:

- `RELAY_PARAMETER_PHASE_CLASS_BOUNDARY`;
- `NO_ORDERED_INTEGER_BOUNDARY`;
- `INTRINSIC_N_MACRO_MICRO_CROSSOVER = NOT_IDENTIFIED`.

No physical interpretation is promoted.

## Checker

Deterministic checker result before final parent-immutability promotion:

- checks: `8922 / 8922 PASS`;
- failures: `0`;
- digest: `98ad3266d91bfb66f6fcce3138f1813a66ee2032eebd929d50adef55215aca33`.

Huge-N and huge-integer checks use only closed-form / finite-state formulas.

## Firewalls

Continue:

- `PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`;
- `PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`;
- `PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`;
- `QUANTUM_BRIDGE = NOT_ESTABLISHED`.

Final repository identities are frozen separately in the artifact manifest and checkpoint.

`STOP_FOR_DRIVER_REVIEW`
