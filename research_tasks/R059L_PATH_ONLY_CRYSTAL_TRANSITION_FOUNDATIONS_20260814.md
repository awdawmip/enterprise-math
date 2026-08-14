# RS-R059L — PATH-ONLY CRYSTAL TRANSITION FOUNDATIONS

Task-ID: `RS-R059L-PATH-ONLY-CRYSTAL-TRANSITION-FOUNDATIONS`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK / SUPERSEDES_UNEXECUTED_LINE_FIRST_TASKBOOK`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R059L`
Date: `2026-08-14`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Current-user semantic correction

This taskbook supersedes, before execution, the earlier:

`research_tasks/R059L_CENTER_THROUGH_PACKET_LINE_FOUNDATIONS_20260814.md`

The correction is stronger than merely redefining a line.

> At the native foundation there is no line. There are only crystal packets, local adjacency, transition events, and paths through adjacent packets. Every transition increments path count by one. A six-channel ingress/egress state may exist only as an explicitly declared ideal ordered-crystal extension. Same-channel ingress/egress is allowed. No edge, boundary, length, straightness, shortest path, or Euclidean geometry is assumed.

R058S remains frozen historical evidence only. Its boundary/edge/chord/periodic-collapse objects are forbidden as R059L native premises.

This is foundation-facing and governed by `FOUNDATIONAL_LOGIC.md` and `native_semantics_admissibility.json`.

---

# 1. Bare N0 substrate

Declare the smallest substrate first.

At minimum:

- a set `V` of crystal packets / packet sites;
- a symmetric local adjacency relation `A(x,y)`;
- packet identity;
- transition-event identity/order for a path realization.

No distinguished center is required in the bare substrate.
No boundary, face geometry, Euclidean embedding, line, distance, length, direction, angle, slope, shortest path, or norm is N0.

Axial coordinates may be used only as `I0_IMPLEMENTATION_CARRIER` to instantiate/check the declared adjacency relation.

---

# 2. Native path object

A finite path is an ordered walk

```text
γ = (x_0, x_1, ..., x_n)
```

with

```text
A(x_j, x_{j+1}) = true
```

for every `j`.

Crucially:

- repeated packets are allowed;
- repeated edges/adjacencies are allowed;
- immediate reversal is allowed;
- loops are allowed;
- self-avoidance is not assumed;
- no-backtracking is not assumed;
- monotonicity is not assumed;
- shortestness is not assumed;
- straightness is not defined.

The path object is a walk/event sequence, not a geometric curve.

---

# 3. Path count

Define the primitive transition count:

```text
C(γ) = n
```

for a path with `n` adjacency transitions.

Operationally:

```text
C_0 = 0
C_{j+1} = C_j + 1
```

for every realized transition event, including reversals, revisits, loops, and repeated use of the same local channel.

Do not call `C` physical length.
Do not multiply it by a lattice spacing and call the result native length.

Stage A may later prove native algebraic properties such as additivity under composable path concatenation, but Stage 0 only freezes the semantics.

---

# 4. Optional ideal six-channel ordered-crystal extension

The user's physical intuition is that an ideal ordered state — perhaps later calibrated to absolute-zero / low-temperature crystal behavior — may support six stable ingress/egress directions.

Do not place temperature in N0.

Instead freeze an optional conditional extension:

`IDEAL_C6_CHANNEL_STATE`.

For the regular six-neighbor carrier, each directed local adjacency incidence may carry a channel label

```text
d ∈ Z/6Z.
```

Required structural relations for this extension must be stated without importing Euclidean angles:

- six channel labels;
- a reversal involution `opp(d)` with `opp(opp(d))=d`;
- for the standard C6 realization, `opp(d)=d+3 mod 6` may be used as implementation notation;
- a cyclic channel permutation may be declared only as part of the ordered-crystal extension;
- D6 relabelings act equivariantly on channel labels.

Whether this six-channel structure is N0-definable from bare adjacency or is genuinely added ordered-state structure is an explicit research question. Until proved, type it as a conditional extension, not as bare N0.

---

# 5. Ingress / egress state

For a realized path and a packet `x`, define event-level ingress and egress records whenever the ideal C6 channel extension is active.

Two compatible representations must be frozen.

## 5.1 Event-level passage pair

For each internal visit event to packet `x`, record an ordered pair

```text
(i,o) ∈ C6 × C6
```

where `i` is the declared incoming channel state and `o` the outgoing channel state under the frozen convention.

Do not attach words such as straight, turn, curvature, reflection, or angle to `(i,o)` in Stage 0.

All admissible locally consistent pairs are allowed unless excluded by the adjacency/channel consistency rules.

In particular:

```text
i = o
```

is allowed.

No rule may reject same-in/same-out merely because a classical geometric interpretation would dislike it.

## 5.2 Aggregate six-channel vectors

For each packet `x`, define integer ingress/egress count vectors

```text
I_x = (I_x^0,...,I_x^5)
O_x = (O_x^0,...,O_x^5)
```

counting how many path events enter/exit through each channel.

The same channel may have both

```text
I_x^d > 0
and
O_x^d > 0.
```

This is explicitly allowed.

Multiple visits and repeated use of a channel accumulate counts.

A richer local passage matrix may be retained as future N1/N2 structure:

```text
M_x[a,b] = number of visit events with ingress a and egress b.
```

Do not optimize or interpret it in Stage 0.

---

# 6. Conservation-like identities are future theorem targets, not premises

For a single finite path, later stages should test/prove exact combinatorial identities such as local ingress/egress balance at interior packets and source/sink imbalance at path endpoints.

For example, after a precise endpoint convention is frozen, a candidate future identity is of the form

```text
sum_d O_x^d - sum_d I_x^d
```

being zero for purely interior visits and carrying endpoint source/sink information for an open path.

For closed paths, a zero-divergence-like identity may emerge.

Do not import continuum flux, divergence, current, momentum, or conservation-law semantics into Stage 0. Those names may be used later only as effective analogies/readouts after exact native identities exist.

---

# 7. No line, no length, no shortest path

The following vocabulary is forbidden from theorem-critical Stage-0 premises:

- line / straight line;
- straightness;
- balanced line;
- Christoffel/mechanical/Sturmian line;
- shortest path / geodesic;
- distance / metric;
- scalar length;
- displacement norm;
- slope / angle;
- midpoint;
- edge / boundary / chord / perimeter;
- Voronoi geometry;
- circle / square / rectangle / cube;
- `Q(a,b)=a²+ab+b²` as metric;
- classical pi;
- R057/R058 fitted/collapse rules.

The earlier balanced-prefix discrepancy and center-line candidate semantics are withdrawn from the foundational Stage 0. They may be reconsidered only later as derived classifications of path statistics if justified.

---

# 8. Temperature typing

Do not claim that six-channel ingress/egress vectors require absolute zero or low temperature at the foundation stage.

Freeze the following semantic separation:

- `IDEAL_C6_CHANNEL_STATE`: exact mathematical ordered-state extension;
- `TEMPERATURE / THERMAL_NOISE / DEFECT_DENSITY`: later physical/calibration variables;
- any claim that low temperature realizes or stabilizes the ideal C6 state must be independently tested and is not a premise of native path mathematics.

Possible later physical questions include whether low-temperature regimes suppress channel-label disorder, defects, or stochastic transition mixing. These are calibration questions, not Stage-0 ontology.

---

# 9. Precision

At this stage, precision/resolution may label the carrier generation itself, but no scalar length is defined.

A path state may carry:

```text
(carrier/resolution identity, path event sequence, transition count, optional C6 channel records)
```

Refinement/coarsening of paths is a future relation to discover; do not presuppose that one fine path has a unique coarse path or that path counts scale by a fixed factor.

---

# 10. Stage 0 — semantic freeze only

## 10.1 Required artifacts

Freeze at least:

1. `R059L_BARE_PACKET_SUBSTRATE_PROTOCOL.json`
2. `R059L_PATH_EVENT_PROTOCOL.json`
3. `R059L_PATH_COUNT_PROTOCOL.json`
4. `R059L_IDEAL_C6_CHANNEL_EXTENSION_PROTOCOL.json`
5. `R059L_INGRESS_EGRESS_STATE_PROTOCOL.json`
6. `R059L_TEMPERATURE_TYPING_PROTOCOL.json`
7. `R059L_PRECISION_CARRIER_PROTOCOL.json`
8. `R059L_NATIVE_SEMANTICS_CLAIM_LEDGER.json`
9. `R059L_COMPUTATION_REGISTRY.json`
10. deterministic Stage-0 checker output

## 10.2 Claim ledger minimum

The native-semantics ledger must include claims for:

- bare packet identity / adjacency as declared N0;
- path transition event and path ordering;
- path count as exact event count, with explicit warning `NOT_PHYSICAL_LENGTH`;
- coordinates as I0 only;
- C6 channels as conditional ordered-state extension unless an N0 definability certificate is proved later;
- ingress/egress vectors and passage matrix typing;
- repeated visits / reversals / loops / same-channel ingress-egress admissibility;
- line/straightness/shortestness/metric/length withheld;
- temperature as later calibration semantics, not N0;
- R058S boundary-first results withheld from premises.

## 10.3 Deterministic sanity cases

Use only tiny exact path examples sufficient to verify semantics, such as:

- one hop;
- two-hop same-channel case;
- two-hop channel-change case;
- immediate reversal;
- three-step loop fragment where admitted by carrier;
- repeated packet visit;
- closed cycle;
- path concatenation example.

For each, verify path count increments by exactly one per transition and aggregate ingress/egress bookkeeping is deterministic.

Do not rank paths or call one more straight/short/efficient than another.

## 10.4 Checker rejection gates

The Stage-0 checker must fail if any Stage-0 artifact silently promotes any of the following to bare N0:

- line / straightness;
- shortest path / graph distance;
- physical length;
- Euclidean direction vector / angle;
- Q metric;
- edge/boundary/chord/perimeter;
- temperature as required mathematical premise;
- R058S collapse grammar/whole-chord/period theorem.

The checker must also fail if the protocol forbids:

- repeated packets;
- immediate reversal;
- loops;
- same-channel ingress/egress;

without an explicit later added semantics.

## 10.5 Required hashes

Return at least:

- `R059L_BARE_PACKET_SUBSTRATE_PROTOCOL_SHA256`
- `R059L_PATH_EVENT_PROTOCOL_SHA256`
- `R059L_PATH_COUNT_PROTOCOL_SHA256`
- `R059L_IDEAL_C6_CHANNEL_EXTENSION_PROTOCOL_SHA256`
- `R059L_INGRESS_EGRESS_STATE_PROTOCOL_SHA256`
- `R059L_TEMPERATURE_TYPING_PROTOCOL_SHA256`
- `R059L_PRECISION_CARRIER_PROTOCOL_SHA256`
- `R059L_NATIVE_SEMANTICS_CLAIM_LEDGER_SHA256`
- `R059L_COMPUTATION_REGISTRY_SHA256`
- Stage-0 checker hash / PASS summary

Then stop for Driver review.

---

# 11. Future Stage A — native path algebra (NOT YET AUTHORIZED)

Only after Stage-0 acceptance:

- prove path concatenation associativity where composable;
- prove path-count additivity;
- define/review path reversal as an involution;
- derive exact ingress/egress conservation identities;
- classify closed vs open path source/sink signatures;
- study the finite local C6 passage matrix without metric interpretation;
- test whether the C6 channel extension is reconstructible from bare adjacency up to D6 relabeling;
- investigate which path features survive carrier relabeling and refinement.

No line or length is needed for this stage.

---

# 12. Future geometry must emerge from path statistics

Only after a stable native path algebra exists may later generations ask whether effective notions such as persistence, direction, displacement, straightness, distance, length, or classical rasterization emerge as compressions/readouts of path statistics.

The foundational arrow is therefore:

```text
packet adjacency
  -> transition event
  -> path
  -> path count
  -> optional C6 ingress/egress state
  -> exact path algebra / conservation identities
  -> derived path statistics
  -> only later: direction / distance / geometry
```

Do not reverse this arrow.
