# Enterprise Math Project Definition

Status: `ACTIVE / PROJECT-LEVEL DEFINITION`
Date: `2026-08-15`

## One-sentence definition

> **Enterprise Math does not aim to discard the mature tools of existing mathematics. It aims to rebuild their foundations: starting from finite resolution, discrete state, integer-first structure, and precision-aware number theory, then re-deriving algebraic, geometric, trigonometric, analytic, and physical tools and determining where classical systems are exactly recovered, approximately recovered, or systematically corrected.**

Project-level principle:

`REFOUND, NOT REJECT`

That is:

**rebuild the foundation rather than abolish the tool.**

---

## 1. What the project is trying to do

Enterprise Math treats the extraordinary success of continuous mathematics, Euclidean geometry, calculus, trigonometry, vector analysis, and related systems as evidence that must be preserved and explained.

The project does not challenge the usefulness of those concepts. It challenges a deeper assumption:

> When mathematics is used to describe nature, must the classical definitions currently attached to those concepts also be nature's most primitive definitions?

The research direction is:

```text
finite-resolution / precision-aware numbers
    ↓
integer and discrete states
    ↓
relations, collapse, paths, counts, forward evolution
    ↓
vector and algebraic structure
    ↓
rebuilt length, angle, metric, area, and other geometric quantities
    ↓
rebuilt sin / cos / tan, pi, projection, coordinate decomposition, and analytic tools
    ↓
comparison with Euclidean geometry, continuous analysis, and engineering formulas
    ↓
classification: exact recovery / finite-precision recovery / asymptotic recovery / domain-restricted recovery / systematic correction
    ↓
physical and engineering calibration
```

The aim is therefore not to create a language isolated from modern mathematics. It is to give the useful parts of modern mathematics a more explicit foundation.

---

## 2. What “definition is not inherited” means

Enterprise Math uses the rule:

> `Definition is not inherited.`

This is now interpreted precisely.

### What may be inherited

- concepts;
- terminology;
- notation;
- mature computational tools;
- correct conditional mathematics;
- long-running engineering success;
- classical formulas as calibration targets and interoperability interfaces.

The following concepts are all retained:

- VECTOR;
- LENGTH;
- ANGLE;
- NORM;
- DOT PRODUCT / PAIRING;
- SIN / COS / TAN;
- AREA / VOLUME;
- pi;
- Euclidean geometry;
- continuum models;
- and other classical mathematical tools that have proved useful.

### What may not be inherited automatically

A classical definition does not become a primitive Enterprise Math definition merely because it has worked for centuries.

Therefore:

> **Concepts may be inherited; definitions must re-earn their foundational status.**

A classical definition may ultimately be re-derived exactly, or even shown to be uniquely natural at the appropriate layer. That is a successful recovery, not a failure of the program.

---

## 3. Relation to Euclidean geometry

Enterprise Math is **not anti-Euclidean**.

Euclidean geometry is one of the most successful tool systems in mathematics and a major reference model for the project.

The program is to:

1. avoid preloading all Euclidean definitions into the native substrate;
2. rebuild geometric objects from the discrete / precision-aware number-theoretic base;
3. compare the rebuilt objects with Euclidean results;
4. preserve every structure that is re-proved correct, stable, and useful;
5. develop explicit corrections where finite precision, small scale, or special state structure produces systematic deviations.

Recovery classifications include:

- `EXACT_RECOVERY`;
- `FINITE_PRECISION_RECOVERY`;
- `ASYMPTOTIC_RECOVERY`;
- `DOMAIN_RESTRICTED_RECOVERY`;
- `SYSTEMATIC_DEVIATION`;
- `NONRECOVERY`.

The intended outcome is a deeper, more explicit, precision-aware version of the geometric toolchain, not difference for its own sake.

---

## 4. Project layers

### P0 — number and precision substrate

Core themes include:

- finite-information / precision-defined numerical states;
- integer-first exact arithmetic;
- explicit scale and resolution;
- discrete state;
- collapse / quotient / merging;
- relation and forward evolution.

Precision is part of state, not merely an error bar attached after computation.

### P1 — discrete objects, paths, and algebra

Includes:

- unit packets;
- adjacency;
- occupancy;
- transition events;
- paths;
- packet count;
- transition/path count;
- branching / recoalescence;
- vectors, modules, group actions, coordinates, and other mature algebraic structures.

Different integers must remain typed distinctly:

`PACKET_COUNT != TRANSITION_COUNT`.

Likewise:

`TRANSITION_COUNT` does not automatically define `GEOMETRIC_LENGTH`.

This does not deny LENGTH. It means LENGTH requires its own rebuilt definition.

### P2 — rebuilt geometry

From frozen P0/P1 structure, define and study:

- length;
- distance;
- angle;
- norm;
- inner product / bilinear pairing;
- projection;
- straightness;
- line / curve;
- area / volume;
- curvature;
- boundary;
- other geometric objects.

These concepts are permitted. Each definition must state its dependencies, precision layer, and any additional choices.

### P3 — rebuilt trigonometric and analytic tools

Using rebuilt geometry, reconstruct or retype:

- sin / cos / tan;
- inverse trigonometric functions;
- Pythagorean-type identities;
- law-of-cosines-type relations;
- the foundational semantics of pi;
- coordinate transformations;
- vector decomposition;
- limits, completion, and other analytic tools where appropriate.

Classical formulas are not forbidden. They are major recovery tests.

### P4 — classical compatibility layer

Compare rebuilt tools with:

- Euclidean geometry;
- classical trigonometry;
- continuous analysis;
- PDE / Fourier / spectral methods;
- engineering computation.

The question is:

**Why does the classical formula work, under what conditions does it work, how does precision enter, and where is correction required?**

### P5 — physics and engineering

Only after mathematical definitions and bridge semantics are frozen should the project calibrate:

- physical length;
- physical angle;
- time and velocity;
- mechanics, materials, and fields;
- probability / statistical physics;
- quantum bridges;
- cosmological models;
- engineering prediction and experiment.

A mathematical object does not acquire physical meaning merely because its name resembles a physical quantity.

---

## 5. Current two-dimensional three-axis vector plane

A current algebraic carrier is:

`Lambda = {(a,b,c) in Z^3 : a+b+c=0}`

with generators:

`u=(1,-1,0)`

`v=(0,1,-1)`

`w=(-1,0,1)`

satisfying:

`u+v+w=0`.

Hence:

`PLANE_DIMENSION=2`

`AXIS_COUNT=3`

and six directed steps:

`D6={+u,-u,+v,-v,+w,-w}`.

This uses the mature concept of vector directly. The six BRC6 outputs are structured directed vectors rather than six unrelated labels.

This carrier does not pre-decide the final definitions of LENGTH, ANGLE, NORM, or trigonometric functions. Those tools remain to be rebuilt on top of the same substrate.

---

## 6. Length, cell count, and path count must remain distinct

Enterprise Math currently distinguishes:

1. **packet/cell count** — how many discrete units belong to a declared object or segment;
2. **transition/path count** — how many actual adjacency transitions occurred;
3. **geometric length** — a geometric quantity that requires a separately frozen definition and calibration.

These may coincide in simple regimes, but they are not definitionally identical.

A task may therefore state:

`SEGMENT_PACKET_COUNT = 4`

or:

`TRANSITION_COUNT = 4`

but should state:

`LENGTH = 4`

only after the rebuilt LENGTH semantics and the correspondence theorem are frozen.

This distinction is intended to make the concept of length more precise, not to eliminate it.

---

## 7. Research method: explain why mature mathematics works

The core inverse method is:

```text
classical / engineering success
    ↓ evidence, not native definition
native discrete mechanism
    ↓
exact mathematical structure
    ↓
rebuilt mature tool
    ↓
classical recovery / deviation / correction
```

Research discipline includes:

- raw-history versus compressed-count verification;
- exact integer arithmetic where available;
- preservation of negative results;
- no target leakage;
- no copying the desired classical answer into the premise;
- classical recovery must be a derived result, not a hidden assumption.

---

## 8. What Enterprise Math is not

Enterprise Math is not:

- renaming every classical concept merely to look novel;
- declaring that length, angle, or trigonometry do not exist;
- declaring Euclidean geometry wrong as a whole;
- forcing every classical formula to deviate;
- treating a discrete grid as only a low-resolution approximation of an assumed continuum;
- assigning physical meaning automatically to every combinatorial object;
- replacing proof with finite enumeration.

The actual objective is:

> **Preserve the best tools of modern mathematics while rebuilding their foundation into a finite-resolution, precision-aware, discrete-computable system that can explain classical success and expose corrections where needed.**

---

## 9. Success criteria

A successful Enterprise Math foundation should eventually:

1. support rich algebra and geometry on its own substrate;
2. reconstruct mature tools such as length, angle, and trigonometric functions;
3. explain why classical Euclidean / continuous mathematics succeeds so broadly in engineering;
4. state the validity domain and precision conditions of classical tools;
5. provide computable corrections where finite-resolution or discrete effects matter;
6. reuse the same foundational mechanisms across independent phenomena rather than fit targets one by one;
7. ultimately produce new experimentally testable predictions where the classical framework is less natural.

---

## 10. Project stack

The long-term stack is:

```text
number
→ precision
→ discrete state
→ relation and count
→ algebra and vector structure
→ rebuilt geometry
→ rebuilt trigonometry and analysis
→ classical compatibility / correction
→ physics
→ engineering
```

Project-level slogan:

> **Do not tear down the old mathematics; give it a better foundation.**

This file is the project-level definition. Foundational research discipline is governed by `FOUNDATIONAL_LOGIC.md`, `foundational_logic.json`, and `native_semantics_admissibility.json`. Geometric-tool refoundation details are recorded in `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`.
