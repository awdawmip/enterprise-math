# GEOMETRIC TOOL REFOUNDATION POLICY

Status: DRIVER-FROZEN PROJECT POLICY
Date: 2026-08-15
Driver: EM-DVR-R0457K / CONTROL_PLANE

## Core principle

Enterprise Math does **not** aim to abolish Euclidean geometry or its mature tools.

The goal is:

`REFOUND, NOT REJECT`.

Classical concepts such as vector, length, angle, norm, dot product, sine, cosine, tangent, area, and related geometric constructions remain legitimate mathematical concepts and engineering tools.

What is withheld is only their **automatic inheritance as native foundational definitions**.

`Definition is not inherited` means:

- keep the concept;
- keep successful classical formulas as evidence, calibration targets, and interoperability targets;
- rebuild or re-derive the definition from the project's discrete / precision-defined number-theoretic substrate;
- determine exactly when the rebuilt object agrees with the classical Euclidean object;
- record any finite-precision or discrete deviations as mathematical findings rather than treating them as forbidden.

## Layering

### G0 — discrete arithmetic / relational substrate

May contain declared integer or precision-defined number axes, packet counts, adjacency, transition events, exact vector-module operations, and other explicitly frozen primitive relations.

### G1 — rebuilt geometric primitives

May define, when a task requires them:

- VECTOR;
- LENGTH;
- ANGLE;
- NORM;
- DOT / BILINEAR PAIRING;
- PROJECTION;
- AREA / VOLUME;
- other geometric readouts.

These names are not forbidden. Their definitions must be explicitly frozen and typed.

### G2 — rebuilt trigonometric / analytic tools

May define or reconstruct:

- sin;
- cos;
- tan;
- inverse trigonometric relations;
- Pythagorean-type identities;
- law-of-cosines-type relations;
- coordinate/vector decompositions.

Classical identities may be recovered exactly, approximately, or only on a declared domain. The status must be proved, not assumed.

### G3 — Euclidean compatibility / calibration layer

Classical Euclidean geometry is a major reference model and tool layer.

Tasks may explicitly compare rebuilt definitions against classical Euclidean results and classify:

- EXACT_RECOVERY;
- FINITE_PRECISION_RECOVERY;
- ASYMPTOTIC_RECOVERY;
- DOMAIN_RESTRICTED_RECOVERY;
- SYSTEMATIC_DEVIATION;
- NONRECOVERY.

A classical formula's success is evidence and a calibration target; it is not by itself proof that the classical definition belongs in G0.

## Current three-axis plane carrier

A discrete two-degree-of-freedom plane may be represented as

`Lambda = {(a,b,c) in Z^3 : a+b+c=0}`

with three axis generators

`u=(1,-1,0)`
`v=(0,1,-1)`
`w=(-1,0,1)`

and

`u+v+w=0`.

The six directed vector steps are

`{+u,-u,+v,-v,+w,-w}`.

This vector carrier is an algebraic substrate. It does not forbid later definitions of length, angle, norm, or trigonometric functions on the same carrier.

## Stage-specific premise rule

A task may say that a quantity is **not a premise for that task** without declaring the concept globally forbidden.

For example, a BRC6 branch-count selector may freeze:

`LENGTH_NOT_USED_AS_SELECTOR_PREMISE`

while still allowing LENGTH to exist elsewhere as a rebuilt geometric readout.

Likewise:

`ANGLE_NOT_USED_AS_SELECTOR_PREMISE`

or

`TRIG_NOT_USED_AS_SELECTOR_PREMISE`

mean only that the current theorem does not depend on those readouts.

## Prohibited mistake

Do not write project-wide claims of the form:

- NO LENGTH;
- NO ANGLE;
- NO TRIGONOMETRY;
- NO NORM;
- NO EUCLIDEAN GEOMETRY.

unless a narrowly scoped historical experiment explicitly requires temporary withholding.

Preferred wording:

- CLASSICAL_LENGTH_DEFINITION_NOT_INHERITED;
- CLASSICAL_ANGLE_DEFINITION_NOT_INHERITED;
- CLASSICAL_TRIG_DEFINITION_NOT_INHERITED;
- EUCLIDEAN_RESULT_USED_AS_CALIBRATION_NOT_PREMISE.

## Scientific objective

The objective is to repair and improve the toolchain built above classical Euclidean geometry by giving its concepts a more explicit discrete / precision-aware foundation, while preserving compatibility wherever the classical tool is already correct and useful.
