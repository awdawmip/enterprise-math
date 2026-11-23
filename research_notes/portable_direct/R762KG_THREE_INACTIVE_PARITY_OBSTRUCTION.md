# R762KG — Three inactive Ports: an exact parity counterexample despite a feasible positive example

**Date:** 2026-11-23. **Status:** EXACT_FINITE_COUNTEREXAMPLE / AUTHOR_VERIFIED / NOT_REVIEWED.

## Model and scientific freeze

This follows R762KF and retains its auxiliary **unsigned** six-axis Port–Euler observer, all 20 triple-support colors, and the same frozen source `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. It makes no change to primitive signed native `TRIADIC_CLOSURE_E` or ordered BRC provenance. Each support color must occur its positive prescribed number of times. An event joins two distinct active pair Ports belonging to the same triple; an Euler realization must be connected and positive-even-degree on all active Port vertices.

Remove **exactly three** of the fifteen pair Ports, leaving twelve active pair-Port vertices.

## Theorem KG.1 — No three-Port deletion pattern has all-positive universality

The \(\binom{15}{3}=455\) choices of three missing pair Ports have exactly two types.

- **440 non-matching patterns** contain two missing pair Ports that share an axis. Their union is a triple whose color has at most one active Port, and hence **zero legal events**. Thus no strictly-positive all-color inventory can be realized.
- **15 perfect matchings** consist of three pairwise disjoint missing pair Ports. These are all (S_6)-equivalent to `01,23,45`. They leave all twenty triple colors with at least two active Ports, but **not every strictly positive inventory is realizable**: the following explicit parity counterexample works for each after relabeling.

### Explicit nonrealizable positive inventory with all 20 colors

Fix inactive Ports `01,23,45`. Exactly twelve triple colors are forced (one legal event edge) and eight are flexible (three legal event edges). Assign to **each** flexible support color multiplicity 1. Assign to the four forced support colors
[
013, 015, 245, 345
]
multiplicity 2, and assign each of the eight other forced colors multiplicity 1. This is a strictly positive inventory of (8\cdot1+4\cdot2+8\cdot1=24) graph events.

Order the twelve active Port vertices lexicographically as
```text
02 03 04 05 12 13 14 15 24 25 34 35
```
and identify a mod-2 boundary vector with the XOR of the bit positions of odd-degree vertices. The forced edges at odd multiplicities have combined boundary **4010** (integer bitmask). Since each of the eight flexible colors must occur exactly once, its contribution must select exactly one of three legal graph edges.

Complete direct integer enumeration over all \(3^8=6,561\) edge selections yields **1,881 distinct flexible boundary vectors**, **none equal to 4010**. Thus the forced parity boundary cannot be cancelled. Every event graph for this precise positive inventory has at least one odd-degree vertex. This proves there is **no** Euler realization for the inventory, independently of connectivity.

The attached executable `R762KG_THREE_INACTIVE_EXACT_COUNTEREXAMPLE.py` contains the entire exact finite check. Its exhaustion criterion uses a direct standard-library Cartesian product, independent of a heuristic or probabilistic search. It also enumerates all 455 three-Port deletion patterns to verify the 440/15 split and the unusable-triple obstruction.

### The matching type still has feasible positive inventories

A constructive positive control prevents over-interpreting the obstruction: set **all twenty support multiplicities to 2**, yielding 40 total events. For the twelve forced colors choose their single edge; for the eight flexible colors in lexicographic order

```text
024 025 034 035 124 125 134 135
```

use the first legal edge for seven colors and the **second legal edge for the eighth**. (Use the code's actual `C` list as normative; the illustrative list above is not the source of the certificate.) This twenty-edge selection is connected on the twelve active Ports, as checked by the program. Duplicating each selected edge makes all degrees positive even, retaining exact multiplicity 2 per color. It is a valid 40-event Euler realization.

Therefore the disjoint three-missing-Port observer admits some positive inventories, but has precise parity-dependent inadmissible inventories; the geometric zero-edge obstruction applies to the other 440 choices.

## Verification, scope, next question

All counts are exact: 455 removed-Port configurations; 440 sharing-axis obstructions; 15 perfect-matchings; 6,561 complete flexible-choice tuples for the displayed 24-event counterexample; 1,881 distinct reachable flexible parity vectors; zero target matches; and one explicitly verified 40-event connected positive-even example.

This theorem is an **auxiliary unsigned** observation-graph statement. It does not assert a physical prohibition or possibility for the signed primitive P000 model, nor does it replace the native triadic closure axiom. Independent review `NOT_REVIEWED`.

Next: classify which 3-Port perfect-matching inventory parities and multiplicity patterns admit an Euler realization, and seek the smallest sufficient-state correction when a Port–Euler quotient loses ordered BRC provenance. Compare the stronger typed signed native Cell/Link/Port requirements separately.
