# RS-R059L — UNIT-PACKET PATH-ONLY CRYSTAL FOUNDATIONS (REISSUE V2)

Task-ID: `RS-R059L-UNIT-PACKET-PATH-ONLY-CRYSTAL-FOUNDATIONS-V2`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK / REISSUE_BEFORE_EXECUTION`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R059L`
Date: `2026-08-14`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Reissue authority

This taskbook supersedes **before execution** the unexecuted taskbook:

`research_tasks/R059L_PATH_ONLY_CRYSTAL_TRANSITION_FOUNDATIONS_20260814.md`

The old bytes remain historical and must not be executed.

This V2 reissue is governed by the active Enterprise Math base specialization:

- `PACKET_PATH_FOUNDATION.md`
- `packet_path_foundation.json`
- `FOUNDATIONAL_LOGIC.md`
- `foundational_logic.json`
- `native_semantics_admissibility.json`

If any older R059L/R058S language conflicts with `PACKET_PATH_FOUNDATION`, the packet/path foundation controls N0 typing.

---

# 1. Current native foundation

The current preferred bare foundation is intentionally smaller than geometry.

## 1.1 UNIT PACKET AXIOM

For every declared carrier/dimension/precision layer and every crystal packet `x`:

```text
UNIT_PACKET(x) = 1
```

This is dimension-independent.

Do **not** reinterpret it as:

```text
1D packet -> native length 1
2D packet -> native area 1
3D packet -> native volume 1
```

The packet contributes only the native integer unit `1`.

For a finite occupied packet configuration `C`:

```text
PACKET_COUNT(C) = |C|
```

This is static object count.

## 1.2 DIMENSION IS RELATIONAL

Dimension, if present, belongs to relations among packets, for example:

- adjacency/incidence structure;
- channel structure;
- stacking/higher-order incidence;
- refinement relation;
- symmetry/automorphism structure.

Dimension does **not** alter `UNIT_PACKET=1`.

## 1.3 UNIT TRANSITION AXIOM

For every actual transition event across declared adjacency:

```text
x -> y
TRANSITION_COUNT += 1
```

A path with `n` adjacency transitions has:

```text
PATH_COUNT = n
```

This is dynamic event count.

`PATH_COUNT` is **not** geometric length.

## 1.4 STATIC / DYNAMIC TYPE SEPARATION

Keep distinct:

```text
PACKET_COUNT      = static object count
TRANSITION_COUNT  = dynamic event count
```

A revisit may increase transition count without increasing occupied packet count.

---

# 2. Bare N0 substrate

At minimum declare:

- `CRYSTAL_PACKET`;
- packet identity;
- symmetric local `ADJACENCY(x,y)`;
- optional `OCCUPANCY(x)` when a state/configuration is needed;
- `TRANSITION_EVENT` identity/order;
- `PATH` as ordered transition history;
- `PACKET_COUNT`;
- `TRANSITION_COUNT`.

No distinguished center is required.

No dimension-specific packet weight is allowed.

Implementation coordinates may only encode/check the declared relations and are `I0_IMPLEMENTATION_CARRIER`.

---

# 3. Native path

A finite path is an ordered walk:

```text
gamma = (x_0, x_1, ..., x_n)
```

with every successive pair adjacent.

Explicitly allowed:

- revisit;
- loop;
- immediate reversal;
- repeated use of the same adjacency;
- repeated use of the same packet;
- arbitrary admissible channel reuse when channel semantics are declared;
- same-channel ingress/egress.

Not assumed:

- self-avoidance;
- no-backtracking;
- monotonicity;
- shortestness;
- straightness;
- geodesicity;
- efficiency.

A path is event history, not a geometric curve.

---

# 4. Precision / refinement

Every packet at every declared precision layer remains native quantity `1`.

If one coarse packet is related to `r` finer packets under a declared refinement relation:

```text
coarse packet quantity = 1
fine packet quantity   = 1 for each fine packet
fine packet count      = r in that refined representation
```

Forbidden:

```text
fine packet native quantity = 1/r
```

merely to preserve a continuum area/volume measure.

Cross-precision comparison is a relation between packet languages. Do not presuppose a continuum measure equality, unique coarse path, or fixed path-count scaling law.

---

# 5. Area / volume / surface typing

At N0 there is no `AREA` or `VOLUME` primitive.

The shared native source for later effective area/volume/d-content readouts is packet count:

```text
PACKET_COUNT + carrier/precision semantics
    -> possible later effective area / volume / d-content readout
```

Do not derive N0 content from powers of a prior length.

A future surface/interface-like quantity is a separate relational problem and may involve adjacency-cut counts; do not identify it automatically with packet count.

---

# 6. Optional ideal C6 channel extension

The bare foundation does not require six channels.

A separately declared ordered carrier may activate:

`IDEAL_C6_CHANNEL_STATE`.

For packet `x`, one may record integer counts:

```text
I_x[0..5]   ingress counts
O_x[0..5]   egress counts
M_x[a,b]    ingress-channel a -> egress-channel b passage counts
```

Explicitly allowed:

```text
M_x[d,d] > 0
```

No channel pair may be automatically interpreted as:

- straight;
- turn;
- angle;
- curvature;
- opposite direction;
- displacement vector.

Channel labels are relational state labels only.

Temperature, absolute zero, thermal noise, and defect density are future physical calibration variables, not mathematical premises for the channel structure.

---

# 7. Geometry firewall

The following are withheld from theorem-critical Stage-0 premises:

```text
LINE
STRAIGHTNESS
DISTANCE
LENGTH
SHORTEST PATH
GEODESIC
DISPLACEMENT MAGNITUDE
EDGE
BOUNDARY
PERIMETER
CHORD
ANGLE
SLOPE
CURVATURE
RADIUS
AREA
VOLUME
EUCLIDEAN GEOMETRY
VORONOI BOUNDARY GEOMETRY
```

Also forbidden as N0 premises:

- `Q(a,b)=a^2+ab+b^2` as a metric;
- classical pi;
- circle/square/rectangle/cube geometry;
- R057 fitted rules;
- R058S whole-chord / edge-density / primitive-period collapse results;
- earlier R059L line/balance/Christoffel proposals.

Older mathematics may survive only after correct N1/N2/N3 retyping.

---

# 8. Stage 0 — semantic freeze only

## 8.1 Hard stop

Stage 0 must stop before:

- path winner/ranking;
- shortest-path computation as geometry;
- metric fitting;
- line/straightness construction;
- conservation-law interpretation;
- grammar/model search;
- geometry/calibration against classical shapes.

Tiny deterministic sanity examples are allowed only to verify bookkeeping and typing.

## 8.2 Required frozen artifacts

Freeze at least:

1. `R059L_UNIT_PACKET_PROTOCOL.json`
2. `R059L_BARE_PACKET_SUBSTRATE_PROTOCOL.json`
3. `R059L_OCCUPANCY_STATIC_COUNT_PROTOCOL.json`
4. `R059L_PATH_EVENT_PROTOCOL.json`
5. `R059L_PATH_COUNT_PROTOCOL.json`
6. `R059L_STATIC_DYNAMIC_COUNT_TYPE_PROTOCOL.json`
7. `R059L_PRECISION_REFINEMENT_UNIT_PROTOCOL.json`
8. `R059L_IDEAL_C6_CHANNEL_EXTENSION_PROTOCOL.json`
9. `R059L_INGRESS_EGRESS_STATE_PROTOCOL.json`
10. `R059L_GEOMETRY_WITHHOLDING_PROTOCOL.json`
11. `R059L_NATIVE_SEMANTICS_CLAIM_LEDGER.json`
12. `R059L_COMPUTATION_REGISTRY.json`
13. deterministic Stage-0 checker output

## 8.3 Claim-ledger minimum

The claim ledger must explicitly type at least:

- `UNIT_PACKET=1` as current declared base axiom;
- dimension as relational, not packet weight;
- packet count as static integer object count;
- transition count as dynamic integer event count;
- adjacency as declared local relation;
- path as arbitrary adjacency walk/history;
- path count as exact transition count and `NOT_PHYSICAL_LENGTH`;
- refinement as relation between packet languages with `NO_NATIVE_FRACTIONALIZATION`;
- coordinates as I0 only;
- C6 state as optional carrier-specific relational extension unless separately derived;
- ingress/egress/passage counts as non-geometric integers;
- temperature as calibration-only;
- line/length/distance/edge/boundary/area/volume withheld from N0;
- R057/R058S and earlier line-first R059L results withheld from native premises.

## 8.4 Deterministic sanity registry

Use only tiny exact examples sufficient to test semantics, including at least:

- one packet occupied;
- finite occupied set count;
- one adjacency transition;
- two transitions;
- immediate reversal;
- loop;
- repeated packet visit;
- repeated adjacency use;
- same-channel ingress/egress under optional C6 state;
- one refinement example showing coarse packet `1` and every fine packet still `1`;
- static/dynamic count divergence under revisits.

No example may be ranked as straighter/shorter/better.

## 8.5 Checker hard failures

The Stage-0 checker must fail if any frozen Stage-0 artifact:

1. assigns a dimension-dependent native packet weight;
2. assigns fine packets fractional native weights solely due to refinement;
3. identifies packet count with native area/volume measure;
4. identifies transition/path count with geometric length;
5. forbids revisit/loop/immediate reversal/same-adjacency reuse by default;
6. forbids same-channel ingress/egress under the optional C6 extension;
7. promotes line/straightness/shortest-path distance/metric/edge/boundary/perimeter/chord/angle/curvature/area/volume to bare N0;
8. requires temperature/absolute zero as a mathematical premise for channel structure;
9. consumes R057/R058S geometry/collapse rules as native premises.

## 8.6 Required returned hashes

Return at least:

- `R059L_UNIT_PACKET_PROTOCOL_SHA256`
- `R059L_BARE_PACKET_SUBSTRATE_PROTOCOL_SHA256`
- `R059L_OCCUPANCY_STATIC_COUNT_PROTOCOL_SHA256`
- `R059L_PATH_EVENT_PROTOCOL_SHA256`
- `R059L_PATH_COUNT_PROTOCOL_SHA256`
- `R059L_STATIC_DYNAMIC_COUNT_TYPE_PROTOCOL_SHA256`
- `R059L_PRECISION_REFINEMENT_UNIT_PROTOCOL_SHA256`
- `R059L_IDEAL_C6_CHANNEL_EXTENSION_PROTOCOL_SHA256`
- `R059L_INGRESS_EGRESS_STATE_PROTOCOL_SHA256`
- `R059L_GEOMETRY_WITHHOLDING_PROTOCOL_SHA256`
- `R059L_NATIVE_SEMANTICS_CLAIM_LEDGER_SHA256`
- `R059L_COMPUTATION_REGISTRY_SHA256`
- Stage-0 checker SHA256 / PASS summary

Then stop for Driver review.

---

# 9. Future Stage A — object/event path algebra (NOT YET AUTHORIZED)

Only after Stage-0 Driver acceptance may later work consider exact algebraic consequences such as:

- path concatenation associativity where composable;
- transition-count additivity;
- path reversal involution;
- endpoint/interior ingress-egress bookkeeping identities;
- closed/open path integer signatures;
- C6 passage-matrix identities;
- invariants under packet relabeling;
- refinement relations between packet/path languages.

Do not import continuum flux/current/divergence semantics before exact integer identities exist.

---

# 10. Future geometry remains downstream

Only after stable packet/event/path algebra exists may later generations ask whether effective notions of direction, persistence, displacement, distance, length, straightness, surface, or geometry emerge as derived classifications/readouts.

The required arrow is:

```text
UNIT_PACKET=1
  + packet relations
  + UNIT_TRANSITION=1
  -> integer object/event structure
  -> exact path algebra
  -> derived statistics/quotients
  -> only later effective geometry
```

Never reverse this arrow.
