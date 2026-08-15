# R059D Stage D - Alignment-Period Count-Signature Robustness

Researcher-ID: `EM-R059D-4C7E21`
Taskbook source: `3bb0e9d7c0078818f5e224b7524cf72812a4ab8a`
Frozen Stage-C parent: `441c554fbb13e3c7faba94561f2ea8b64d3b6c4b`
Owner branch: `research/r059d-stage-d-alignment-period-robustness`

## Primary disposition

`MIXED_ALIGNMENT_PERIOD_STRUCTURAL_ROBUSTNESS`

The Stage-C q=3 mechanism is not generic, but one fixed q-independent finite count-signature controller works on the infinite family `q=3 or q>=5`. The exact exceptional alignment periods are `q in {2,4}`.

`q` is a RELATIONAL ALIGNMENT PERIOD / H-word exponent only. It is not distance, length, physical spacing, area, volume, or a physical macro/micro scale.

## Exact post-V count field

With `X_(i+1)=H^q X_i`, define

`z_i^- = H^-1 V X_i`
`z_i^+ = H V X_i`.

At the post-V boundary,

`C(H^m V X_0)=kappa*(1[m=+1 mod q]+1[m=-1 mod q])`.

For branch `s in {+1,-1}` and frozen probe offset r,

`C(H^r z_i^s)=kappa*(1[s+r=+1 mod q]+1[s+r=-1 mod q])`.

Therefore `B_(r)(z_i^s)=1` iff `s+r` is congruent to `+1` or `-1` modulo q.

## Verbatim Stage-C A1 replay

A1 is replayed without repair:

- `B_(+1)=0 -> H`
- `B_(+1)=1 -> H_INV`

It gives nontrivial D0 first aligned return at round 3 exactly for q=3 for every integer N>=1. The finite case q=2,N=1 reaches D0 only because `H^2=id`, while its launch configuration support is singleton and is not nontrivial Stage-D evidence.

## Signature classification

- S1 distinguishes the post-V branch classes iff q=3.
- S2 distinguishes iff q=3 or q>=5, equivalently iff q is not 2 or 4.
- S3 adds no new q-class over S2.
- S4 exact count magnitudes add no new branch-sign q-class over S2/S3.

At q=2, S4 can detect doubled source multiplicity but still cannot distinguish the two branch classes.

## COUNT_SIGNATURE_SYMMETRY_OBSTRUCTION

For q=2 or q=4 let `tau=H^2`. The current post-V count field satisfies `C(tau x)=C(x)` and `tau(z_i^-)=z_i^+`. Both branch classes have ingress V, and tau preserves the declared channel labels.

Exact V-successor return nevertheless requires opposite local continuations:

- from `z_i^-`: H
- from `z_i^+`: H_INV

Thus every frozen equivariant current-count signature gives the same information to histories that require incompatible return actions. Tied actions preserve off-target CPBC support. Since channel actions commute with tau, paired later histories remain H^2-related. For qN>2 they cannot collapse to one tagged endpoint without symmetry-breaking information that is forbidden by the Stage-D grammar.

Freeze:

`COUNT_SIGNATURE_SYMMETRY_OBSTRUCTION = ESTABLISHED_FOR_q_2_4_WITHIN_FROZEN_EQUIVARIANT_CURRENT_COUNT_GRAMMAR`.

## Uniform finite controller

The fixed controller

- START -> `{H,H_INV}`
- H_FAMILY -> V
- ingress V and `B_(+2)=1` -> H
- ingress V and `B_(+2)=0` -> H_INV

never reads q, N, target, branch provenance, timer, or scheduler order. It gives exact D0 first aligned return at round 3 for every integer N>=1 and every `q=3 or q>=5`, under both `S_SYNC` and `S_ALL_ORDERS_SNAPSHOT`.

Freeze:

`UNIFORM_FINITE_COUNT_SIGNATURE_AUTONOMOUS_RECURRENCE`.

The mirror fixed probe `B_(-2)` gives the same reachable endpoint/count-cloud class.

## Signature resources

Within the frozen subset-closed probe grammar:

- q=3: one support bit with max absolute H exponent 1 is sufficient.
- q>=5: one support bit is sufficient and max absolute H exponent 2 is minimal.
- q=2,4: the full current count field is branch-symmetric, so richer S3/S4 current-count signatures do not remove the obstruction.

A controller uniform on the infinite robust family therefore needs `INGRESS_CLASS + one fixed count-support bit at exponent magnitude 2`.

## Intermediate cloud and N scale-down

For all robust q and all N>=1:

- configuration support: `[1,2^N,2^N,1]`
- cell support: `[N,2N,2N,N]`
- T1: `U_N(4N)=Hfull`
- T2: `6N`
- T3: `2N` cells at `Hfull`, `4N` cells at `Hfull/2`

For sync, `Hfull=2^N`. For all-orders snapshot, `Hfull=2^N*(N!)^3`.

All pre-frozen large-N survivors were scaled downward. D0 first aligned return at round 3 persists for every integer N>=1. Therefore:

`NO_N_CROSSOVER_WITHIN_PROVED_RANGE`.

No `AUTONOMOUS_CONTROLLER_ROBUST_N_CROSSOVER_CANDIDATE` is promoted. Stage-A `N_c=3` remains only `R3_CONTROLLER_SPECIFIC_ALIAS_CANDIDATE`.

## Firewalls

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

No q result is interpreted as a physical scale transition.

## Validation

The deterministic checker validates the exact count field, S1-S4 q classification, `H^2` symmetry iff q is 2 or 4, A1 replay, both one-bit uniform controllers, signature-resource minima, scheduler multiplicities, tiny theorem regressions, and all leakage/triviality firewalls. Tiny enumeration is theorem regression only; large-N claims are symbolic.

`STOP_FOR_DRIVER_REVIEW`.
