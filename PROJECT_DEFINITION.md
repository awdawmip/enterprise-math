# Enterprise Math Project Definition

Status: `ACTIVE / PROJECT-LEVEL DEFINITION / V3`
Date: `2026-08-21`
Driver: `CONTROL_PLANE`

## One-sentence definition

> **Enterprise Math rebuilds the foundations of useful modern mathematical tools from a finite-resolution, precision-aware, integer-first and discretely computable substrate, then classifies when classical algebraic, geometric, trigonometric, analytic and physical tools are exactly recovered, recovered only at finite precision or asymptotically, or require systematic correction.**

Project principle:

`REFOUND, NOT REJECT`.

## 0. Authority chain

This file defines project mission, layers and routing. Mutable concrete geometry is no longer duplicated across several top-level authority files.

The current native-plane foundation is:

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`.

Current downstream frozen definitions include:

- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`

When older 2026-08-16/17 coordinate documents or historical taskbooks conflict with a later explicit foundational correction/supersession, the later correction controls. Older documents remain provenance/history, not competing current authority.

## 1. Current highest native-plane structure

The current Enterprise plane freezes:

- `O_E = 0`;
- the origin is a triple circle-cell boundary intersection, not a cell center and not a cell;
- `ENTERPRISE_CELL = CIRCLE_CELL`, identified by its discrete center;
- nearest center spacing `D_CENTER=1`;
- uniform cell radius `R_CELL=1/sqrt(3)`;
- neighboring cells overlap with positive area and the circle-cell family covers the plane without gaps;
- the native axes are exactly three **positive rays** `E_1,E_2,E_3`;
- native negative axes are not required and must not be silently reintroduced;
- the three positive axes divide one full turn into three native `120°` right sectors;
- `ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`;
- the three axes are pairwise `ENTERPRISE_ORTHOGONAL`, which is native Enterprise orthogonality rather than Euclidean 90-degree perpendicularity in the carrier drawing.

Therefore the older native-plane rule

`three undirected axes -> six native directed directions -> alternating signs every 60 degrees`

is superseded.

`ENTERPRISE_PLANE_DIMENSION = 3` remains project-specific dimension semantics and is not classical linear rank, Euclidean dimension or topological dimension. Under the current plane foundation the three native dimension components are carried by the three positive axis families, not by automatically adjoining an opposite native direction to every axis.

## 2. Current coordinates and length

Native addresses use

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`,

as the glued union of three positive two-axis sector charts:

- `S_12={(a,b,0)}`;
- `S_23={(0,b,c)}`;
- `S_31={(a,0,c)}`.

This is not a common diagonal-shift quotient.

Inside each native `120°` right sector:

`L_E^2=a^2+b^2`.

Hence for a canonical origin-sector triple:

`L_E(a,b,c)^2=a^2+b^2+c^2`,

and `(3,4,0)` has native length `5`.

Historical carrier identities such as `e_1+e_2+e_3=0` or `u+v+w=0`, and the A2/C6 rank-two presentation, are `I0_IMPLEMENTATION_CARRIER / CLASSICAL_COMPATIBILITY` structures only. They do not define native vector identity, native negative axes, coordinate equivalence or native metric.

## 3. Current line and point-to-point structure

Current line identity is

`ENTERPRISE_LINE_IDENTITY = NATIVE_COMPONENT_TRACE`.

One trace may have many discrete single-cell path representatives. For example, the `(3,4)` trace has `35` shuffle/path representatives while native length is `5`.

Arbitrary point-to-point structure uses the frozen **directed native line gauge**. It is positive, translation invariant and triangle-subadditive, but is generally reversal-asymmetric, hence

`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC = false`.

For an unordered endpoint pair, the canonical datum is the bidirectional trace pair together with its bidirectional length spectrum. Many symmetric scalar metrics may be added conditionally, but current premises do not canonically select one.

## 4. BRC

The name and bridge role are retained:

`BRC = Branch-Recoalescence Collapse`.

Classical/orthogonal coordinate semantics may be related to Enterprise coordinate semantics through a typed collapse/readout bridge, but target-side classical definitions may not be copied into native premises.

R062 further freezes the enrichment tower

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`

and

`BRC_IS_EXACT_BOOLEAN_SHADOW_OF_COMPONENT_TYPED_NATIVE_MULTIPATH = true`.

Boolean BRC preserves support, not discarded path identity, multiplicity or provenance. Component labels are necessary to distinguish same endpoint from same native line.

## 5. Precision Mathematics lineage

`Precision Mathematics / 精度数学` is the predecessor of Enterprise Math and is no longer a peer active project.

From 2026-08-21 onward, finite-resolution number lines, precision-defined numbers, precision-aware state and related integer/discrete research belong to Enterprise Math. Historical Precision Mathematics materials remain provenance.

## 6. Account worldview and the six-dimensional/twelve-direction model

The protected account-level `我眼中的世界.md` contains an ACTIVE user-chosen research axiom that models solid space as six Enterprise dimensions / twelve directions. This project cleanup does **not** modify that file.

However, the 2026-08-16 project definition implemented that worldview using a native plane with six directed directions and 60-degree alternating signs. That plane realization has been superseded by the current three-positive-axis / 120-degree foundation.

Therefore the project currently distinguishes:

- `WORLDVIEW_6D_12_DIRECTION = ACTIVE_USER_CHOSEN_RESEARCH_AXIOM`;
- `OLD_60_DEGREE_SIX_DIRECTION_PLANE_REALIZATION = SUPERSEDED`;
- `CURRENT_THREE_POSITIVE_AXIS_TO_6D_WORLD_BRIDGE = OPEN / REQUIRES_REDERIVATION`.

An ACTIVE worldview entry does not silently restore the superseded plane realization.

## 7. Definition is not inherited

`Definition is not inherited` does not prohibit mature mathematical concepts.

VECTOR, LENGTH, DISTANCE, ANGLE, NORM, DOT/PAIRING, PROJECTION, SIN/COS/TAN, AREA/VOLUME, PI, Euclidean geometry and continuum models remain admissible concepts and correct conditional tools at their declared layers.

The forbidden move is to import a successful target-side definition as a native premise and then count its reappearance as a new foundational derivation.

Classical and engineering success is strong evidence and a calibration target, not automatic native ontology.

## 8. Project layers

- `P0`: number, precision, integer structure, discrete state, relations and collapse/quotient;
- `P1`: packet/cell, adjacency, transition, path, branching/recoalescence, Enterprise coordinates and algebra;
- `P2`: rebuilt length, distance, angle, norm, pairing, projection, area/volume, curve and related geometry;
- `P3`: rebuilt trigonometry, pi semantics, coordinate transforms and analytic tools;
- `P4`: classical/continuous/engineering recovery and deviation classification;
- `P5`: physical and engineering calibration only after mathematical semantics are frozen.

Always preserve

`PACKET_COUNT != TRANSITION_COUNT != GEOMETRIC_LENGTH`.

## 9. Recovery classes

Use:

- `EXACT_RECOVERY`
- `FINITE_PRECISION_RECOVERY`
- `ASYMPTOTIC_RECOVERY`
- `DOMAIN_RESTRICTED_RECOVERY`
- `SYSTEMATIC_DEVIATION`
- `NONRECOVERY`

A deviation is not automatically an improvement; it must be derived, reproducible and testable.

## 10. Canonical project stack

`NUMBER -> PRECISION -> DISCRETE STATE -> RELATION/PATH/BRC -> THREE-POSITIVE-AXIS ENTERPRISE COORDINATES -> REBUILT GEOMETRY -> TRIG/ANALYSIS -> CLASSICAL COMPATIBILITY/CORRECTION -> PHYSICS -> ENGINEERING`.

Project slogan:

> **Do not tear down old mathematics; give it a better foundation.**

Foundational discipline is governed by `FOUNDATIONAL_LOGIC.md`, `foundational_logic.json`, `native_semantics_admissibility.json`, and `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`.