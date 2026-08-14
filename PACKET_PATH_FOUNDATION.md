# Enterprise Math Packet / Path Foundation

Status: `ACTIVE / BASE-ONTOLOGY SPECIALIZATION`
Authority: `PROJECT-LEVEL FOUNDATIONAL RESEARCH LOGIC`
Effective: `2026-08-14`

This file specializes `FOUNDATIONAL_LOGIC.md` for the current Enterprise Math native substrate. It is intentionally smaller than classical geometry.

## Core statement

> **A crystal packet is the native unit. In every dimension and at every declared precision layer, one crystal packet has native quantity exactly 1. Dimension belongs to relations among packets, not to the quantity carried by an individual packet. A path is only a sequence of adjacency transitions; every transition contributes exactly 1 to path count.**

The native foundation therefore begins from integer counting of objects and events, not from line, length, area, volume, edge, boundary, angle, or continuum geometry.

---

## PF-01 — UNIT PACKET AXIOM

For every declared dimension / carrier stratum `d` and every crystal packet `x` in that stratum:

```text
UNIT_PACKET(x) = 1
```

Equivalently, for every finite packet set `C`:

```text
PACKET_COUNT(C) = sum_{x in C} 1 = |C|.
```

Hard consequences:

- a 1D packet is not assigned a native `length = 1`;
- a 2D packet is not assigned a native `area = 1`;
- a 3D packet is not assigned a native `volume = 1`;
- a higher-dimensional packet is not assigned a dimension-specific measure;
- the packet itself simply contributes the native integer unit `1`.

Classical names such as length/area/volume may later be attached to readouts of packet counts under additional semantics, but those names are not part of the unit axiom.

---

## PF-02 — DIMENSION IS RELATIONAL, NOT A PACKET WEIGHT

Dimension is encoded, if at all, by relational structure such as:

- adjacency / incidence pattern;
- local channel structure;
- stacking or higher-order incidence;
- refinement relations;
- automorphism / symmetry structure;
- other explicitly declared relations.

Dimension does **not** change `UNIT_PACKET(x)=1`.

Two carriers may have different dimensions or relation structures while every individual packet in each carrier still has native quantity `1`.

---

## PF-03 — OCCUPANCY / CONTENT IS COUNTING

For a finite occupied configuration `C`, its native static content is:

```text
OCCUPIED_PACKET_COUNT(C) = |C|.
```

This is a native integer count.

Later effective interpretations may include:

- 2D effective area readout from packet count;
- 3D effective volume readout from packet count;
- higher-dimensional effective content/measure readout from packet count.

These are semantically downstream. The foundation does not define area by `length^2`, volume by `length^3`, or any continuum measure.

A 3D surface-like quantity is **not** automatically packet occupancy count. A future surface/interface readout may instead depend on adjacency cuts or other relational counts. That is a separate derived problem.

---

## PF-04 — ADJACENCY IS THE ONLY REQUIRED LOCAL RELATION FOR PATH

The minimal path substrate is:

```text
CRYSTAL_PACKET
ADJACENCY
TRANSITION_EVENT
PATH
PATH_COUNT
```

No native premise is made for:

```text
LINE
STRAIGHTNESS
DISTANCE
LENGTH
EDGE
BOUNDARY
PERIMETER
CHORD
ANGLE
CURVATURE
RADIUS
AREA
VOLUME
EUCLIDEAN COORDINATE GEOMETRY
```

Implementation coordinates may encode/check adjacency but do not make their geometry native.

---

## PF-05 — UNIT TRANSITION AXIOM

If `x` and `y` are adjacent crystal packets and a transition event occurs

```text
x -> y,
```

then exactly one event is counted:

```text
PATH_COUNT += 1.
```

Every adjacency transition has native event quantity `1`.

No metric weight, edge length, direction cosine, Euclidean displacement, or energy-derived cost is attached at N0.

For a path

```text
gamma = (x_0, x_1, ..., x_n)
```

with each successive pair adjacent:

```text
PATH_COUNT(gamma) = n.
```

This count is the number of transition events, not a geometric length.

---

## PF-06 — PATH IS A WALK, NOT A GEOMETRIC CURVE

Native paths explicitly allow:

- revisit of an earlier packet;
- loops;
- immediate reversal;
- repeated use of the same adjacency;
- arbitrary reuse of local channels when such channels are later declared;
- same-channel ingress/egress in an ideal channel state.

Therefore native path semantics do not assume simplicity, geodesicity, monotonicity, straightness, or shortestness.

A shortest-path rule, no-backtracking rule, balanced-word rule, line rule, or metric geodesic rule is an added N1 operational semantics, never silently N0.

---

## PF-07 — STATIC COUNT AND DYNAMIC COUNT ARE DISTINCT

The foundation contains at least two irreducible integer count types:

```text
STATIC OBJECT COUNT:
PACKET_COUNT / OCCUPIED_PACKET_COUNT

DYNAMIC EVENT COUNT:
PATH_COUNT / TRANSITION_COUNT
```

They must not be conflated.

Revisiting a packet increases transition count when a transition occurs but does not create a new packet in an occupied-set count.

This separation is foundational:

```text
object exists -> +1 object unit
transition occurs -> +1 event unit
```

---

## PF-08 — PRECISION / REFINEMENT DOES NOT FRACTIONALIZE THE PACKET UNIT

At every declared precision layer `delta`, every packet at that layer still has native quantity `1`.

If one coarse packet is represented by `r` finer packets under a refinement relation, the native statements are:

```text
coarse packet quantity = 1
fine packet quantity   = 1 for each fine packet
fine packet count      = r for that refined representation
```

Do **not** assign each fine packet native quantity `1/r` merely to preserve a continuum measure.

Cross-precision comparison is a relation between different packet languages / refinement layers. It is not an equality of native packet counts.

Any physical unit conversion or scale-normalized measure is a downstream readout and must retain the precision/carrier tag.

---

## PF-09 — PACKET SHAPE DOES NOT ALTER THE UNIT

External/decorative packet shape does not alter:

```text
UNIT_PACKET = 1.
```

Packet shape may matter only if it changes admitted relational structure, for example adjacency, channel incidence, symmetry, stacking, or refinement.

A boundary drawing cannot by itself change the native packet quantity or create native length/area/volume.

---

## PF-10 — IDEAL CHANNEL STATES ARE ADDITIONAL RELATIONAL STRUCTURE

An ideal ordered carrier may possess a finite local channel structure. In the currently studied ideal six-channel case one may record, for a packet `x`:

```text
I_x[0..5]   ingress counts
O_x[0..5]   egress counts
M_x[a,b]    ingress-channel a -> egress-channel b passage counts
```

Allowed:

```text
M_x[d,d] > 0
```

No channel pair is automatically named straight, turn, angle, curvature, or opposite.

The six-channel structure is not universalized to every dimension by fiat. Channel cardinality belongs to the declared carrier relation structure.

Temperature is not a native premise. Absolute-zero / low-temperature interpretations are future physical calibration questions, not mathematical axioms.

---

## PF-11 — AREA / VOLUME ARE EFFECTIVE READOUT NAMES, NOT NATIVE PRIMITIVES

If later a 2D engineering language maps packet count to an effective area quantity, or a 3D engineering language maps packet count to an effective volume quantity, the shared native source is still:

```text
N = PACKET_COUNT.
```

Thus the foundational direction is:

```text
packet count + carrier/precision semantics
    -> effective area / volume / d-content readout
```

not:

```text
length -> area -> volume -> infer packet quantity.
```

The success of classical area/volume formulas is evidence to be explained later; their definitions are not copied into N0.

---

## PF-12 — LENGTH IS DELIBERATELY UNDEFINED AT N0

`PATH_COUNT` is not declared to be geometric length.

Different paths may have different transition counts while sharing endpoints or other relational data; repeated loops may increase path count without changing occupancy.

Therefore the foundation deliberately postpones:

- distance;
- length;
- displacement magnitude;
- shortestness;
- straightness;
- line;
- metric/geodesic structure.

Any future length must be derived from an explicitly admitted relational/readout structure and must not retroactively redefine `PATH_COUNT`.

---

## PF-13 — FOUNDATION REGRESSION GATE

A foundation-facing task violates this base specialization if it silently assumes any of the following as native:

- dimension-specific packet weight;
- fractional packet weight caused solely by refinement;
- line / straightness;
- shortest-path distance;
- geometric length from transition count;
- edge / boundary / perimeter / chord;
- area or volume formulas from powers of length;
- Euclidean angle / slope / curvature;
- Voronoi or polygon boundary geometry;
- temperature as the reason a mathematical channel relation exists.

Such mathematics may remain valid after retyping to N1/N2/N3, but it cannot be cited as an N0 derivation.

---

## Minimal current base

The currently preferred minimal foundation is therefore:

```text
CRYSTAL PACKET                     quantity 1
ADJACENCY                          declared relation
OCCUPANCY                          optional state predicate
TRANSITION EVENT                   quantity 1 per adjacent transition
PATH                               ordered transition history
PACKET COUNT                       static integer count
PATH / TRANSITION COUNT            dynamic integer count
OPTIONAL RELATIONAL CHANNEL STATE  carrier-specific, non-geometric
PRECISION / REFINEMENT RELATION    separately declared when used
```

Everything else must be derived, calibrated, or retained at a later semantic stratum.
