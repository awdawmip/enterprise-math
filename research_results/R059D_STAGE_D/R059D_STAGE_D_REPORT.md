# R059D Stage D — Alignment-Period / Count-Signature Structural Robustness

Researcher-ID: `EM-R059D-4C7E21`  
Taskbook source: `3bb0e9d7c0078818f5e224b7524cf72812a4ab8a`  
Frozen Stage-C parent: `441c554fbb13e3c7faba94561f2ea8b64d3b6c4b`  
Owner branch: `research/r059d-stage-d-alignment-period-robustness`

## Primary disposition

`MIXED_ALIGNMENT_PERIOD_STRUCTURAL_ROBUSTNESS`

Stage C's q=3 autonomous mechanism is not fully generic, but it is also not isolated. A single q-independent finite count-signature controller exists on an infinite alignment-period family:

`q = 3 or q >= 5`.

The exact exceptional alignment periods are:

`q in {2,4}`.

Those exceptions are not merely failures of S1. They satisfy an exact current-count symmetry obstruction.

## 1. Alignment period semantics

The aligned tagged family is parameterized by

`X_(i+1) = H^q X_i`

with H-orbit order `qN`.

`q` is only a relational alignment period / H-word exponent. It is not distance, length, physical spacing, area, volume, or any physical scale.

The launch is frozen from Stage C:

1. START branches to `{H,H_INV}`;
2. after `H_FAMILY`, the three-round search skeleton uses `V`;
3. post-V continuation is chosen only from current ingress plus frozen exact count signatures;
4. `sigma_N=V` is evaluator/stopping readout only.

Both schedulers remain active: `S_SYNC` and `S_ALL_ORDERS_SNAPSHOT`.

## 2. Exact post-V count field

Let

`z_i^- = H^-1 V X_i`,
`z_i^+ = H V X_i`.

At the post-V boundary, the exact aggregate count field has the symbolic form

`C(H^m V X_0) = kappa * (1[m=+1 mod q] + 1[m=-1 mod q])`.

Here `kappa>0` is scheduler-dependent but common:

- sync: `kappa = 2^(N-1)`;
- all-orders snapshot: `kappa = 2^(N-1)*(N!)^2`.

Therefore for branch sign `s in {+1,-1}` and a fixed probe offset `r`,

`C(H^r z_i^s) = kappa*(1[s+r=+1 mod q] + 1[s+r=-1 mod q])`.

The support bit is exactly

`B_(r)(z_i^s)=1`

iff

`s+r = +1 or -1 (mod q)`.

This formula is independent of tiny-N fitting and is the large-N proof carrier.

## 3. Verbatim Stage-C A1 replay

A1 is replayed unchanged:

- `B_(+1)=0 -> H`;
- `B_(+1)=1 -> H_INV`.

The exact branch signatures are:

- `B_(+1)(z_i^+)=1` iff `q=3`;
- `B_(+1)(z_i^-)=0` for every `q>=2`.

Hence:

- `q=3`: nontrivial D0 first aligned return at round 3 for every `N>=1`;
- every large-N `q!=3`: A1 gives the same H continuation to both branch classes and fails D0;
- `q=2,N=1`: a finite-orbit degeneracy has `H^2=id`, so round-3 D0 occurs, but the launch branch positions are already aliased and configuration support is singleton. This is not nontrivial Stage-D evidence.

For `q!=3`, later A1 post-V clouds are common H-shifts of the same two-branch pattern. A1 continues to read `B_(+1)=0` on both branches, so the paired histories remain H^2 apart. Exact tagged recoalescence would require `qN|2`.

## 4. Branch-signature classification

### S1

`S1={INGRESS_CLASS,B_(+1)}` distinguishes the post-V branches iff `q=3`.

### S2

`S2={INGRESS_CLASS,B_(+1),B_(+2)}` distinguishes iff `q=3 or q>=5`, equivalently iff `q not in {2,4}`.

### S3

Adding `B_(-1),B_(-2)` introduces no new q-class. S3 has the same distinguishability domain as S2.

### S4

Exact integer magnitudes/comparisons on the same fixed probe set also have the same branch-sign domain.

At q=2, magnitudes reveal doubled source multiplicity, so S4 can recognize that some alignment-period class is different. But the two branch classes inside q=2 remain indistinguishable. Thus magnitude information does not remove the branch obstruction.

## 5. COUNT_SIGNATURE_SYMMETRY_OBSTRUCTION

For `q=2` or `q=4`, define the packet relabeling `tau = H^2`.

The post-V count field obeys `C(tau x)=C(x)` exactly, because the residue support `{+1,-1}` is invariant under `+2` precisely for q=2 or q=4.

Also `tau(z_i^-)=z_i^+`.

Both branches have current ingress `V`, and tau preserves the declared channel labels. Thus every current-count signature equivariant under the frozen relational relabelings gives the same value on the paired branch positions.

But exact V-successor return requires incompatible local continuations:

- from `z_i^-`: `H`;
- from `z_i^+`: `H_INV`.

Any controller that assigns the same singleton action loses one branch. Any tied action set retaining both channels preserves off-target CPBC support.

The obstruction extends inductively beyond one round: tau-related histories receive identical action sets and channel actions commute with tau, so paired continuations remain H^2-related. If `qN>2`, they cannot collapse to one tagged target.

Freeze:

`COUNT_SIGNATURE_SYMMETRY_OBSTRUCTION = ESTABLISHED_FOR_q_2_4_WITHIN_FROZEN_EQUIVARIANT_CURRENT_COUNT_GRAMMAR`.

## 6. Uniform finite controller

A fixed one-bit controller using only the pre-frozen offset `+2` is:

- START -> `{H,H_INV}`;
- `H_FAMILY -> V`;
- ingress `V` and `B_(+2)=1 -> H`;
- ingress `V` and `B_(+2)=0 -> H_INV`.

It never reads q, N, a target map, branch provenance, or a timer.

For every `q=3 or q>=5`, the minus branch has `B_(+2)=1` and the plus branch has `B_(+2)=0`. Therefore both branches autonomously reach `V X_i` at round 3.

Freeze:

`UNIFORM_FINITE_COUNT_SIGNATURE_AUTONOMOUS_RECURRENCE`

on the exact infinite q-domain `{3} union {q>=5}`.

The mirror one-bit probe `B_(-2)` gives the same reachable transition relation.

## 7. Signature resource atlas

Within the frozen subset-closed probe grammar:

- q=3: one support bit at H-word exponent magnitude 1 is sufficient;
- q>=5: one support bit is sufficient, but exponent magnitude 2 is minimal;
- q=2,4: no finite current-count probe resolves the branch within the frozen equivariant grammar because the full current count field itself is symmetry-equivalent.

Thus one fixed infinite-family controller needs:

`INGRESS_CLASS + one count-support bit at fixed exponent 2`.

S3 and S4 add no new alignment-period class. These are algorithmic word/probe resources, not geometric reaches.

## 8. Intermediate count cloud

For every robust survivor and every `q=3 or q>=5`, for all integers `N>=1`:

configuration support:

`[1, 2^N, 2^N, 1]`

cell support:

`[N, 2N, 2N, N]`

Traversal signatures:

`T1: U_N(4N)=Hfull`

`T2=6N`

`T3: 2N cells at Hfull; 4N cells at Hfull/2`.

With sync `Hfull=2^N`; with all-orders snapshot `Hfull=2^N*(N!)^3`.

Both schedulers therefore preserve the same endpoint and support/readout classes.

## 9. Large-N and scale-down

The N registry was frozen before q evaluation and includes `10^36`, its ±1/2/3/5/7/11 probes, and two lower huge scales.

The q registry was also frozen before evaluation and includes all q=2..12 plus multiple prime/composite probes above 12.

The large-N proof uses only exact residue/count-field formulas; no O(N), O(qN), or full-history huge enumeration occurs.

Every large-N survivor was then carried downward. For every robust q and every carried q-independent controller:

`D0 first aligned return at round 3`

holds for every integer `N>=1`.

Therefore:

`NO_N_CROSSOVER_WITHIN_PROVED_RANGE`.

No `AUTONOMOUS_CONTROLLER_ROBUST_N_CROSSOVER_CANDIDATE` is promoted.

Stage-A `N_c=3` remains permanently `R3_CONTROLLER_SPECIFIC_ALIAS_CANDIDATE`.

## 10. Structural classification

The evidence separates a broad infinite robust class, covered by one q-independent one-bit controller, from exact exceptional q classes `{2,4}` blocked by current-count symmetry.

Therefore the correct Stage-D disposition is:

`MIXED_ALIGNMENT_PERIOD_STRUCTURAL_ROBUSTNESS`.

This is not `ALIGNMENT_PERIOD_CONTROLLER_COADAPTATION_REQUIRED`: changing the controller is unnecessary on the infinite robust class, and q=2/4 are not repaired by richer S3/S4 count signatures within the frozen grammar.

## 11. Firewalls

Remain frozen:

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

No q-result is interpreted as a physical length-scale or macro/micro transition.

## 12. Deterministic validation

The deterministic checker validates exact post-V count formulas; S1/S2/S3/S4 q classifications; `H^2` field invariance iff q in `{2,4}`; A1 verbatim replay; the uniform B_(+2) and B_(-2) controllers; exact tiny theorem regressions for configuration support, cell support, T1/T2/T3; signature-resource minima; scheduler multiplicity relations; and all mandatory leakage/triviality firewalls.

Tiny enumeration is theorem regression only.

`STOP_FOR_DRIVER_REVIEW`.
