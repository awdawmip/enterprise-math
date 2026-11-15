# R5 — Five-event geometric Q produced solely by path switching

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Source science frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Existing research: `EDGE_SWITCH_BOOLEAN_DIAMOND_CERTIFICATE_THEOREM.md` at PR #2427.

## Theorem (an actual radius-two geometry realizes switch-only Q)

Use five strictly ordered integer events with original gaps `(3,2,2,3)`, hence event coordinates `(0,3,5,7,10)`. The two distinguished **zero-based** gaps are `a=0` and `b=3`; contracting each changes its length from 3 to 2. Centers are chosen from the **same indexed events**, with `K=3`; all events must have nearest-center distance at most `rho=2`. Minimize the integer sum of nearest-center distances.

For original, a-only, b-only and joint closure respectively the event coordinates are:

- `0: (0,3,5,7,10)`
- `a: (0,2,4,6,9)`
- `b: (0,3,5,7,9)`
- `ab: (0,2,4,6,8)`

All four optimal costs are exactly `J=4`. Writing `024` for the center-index set `{0,2,4}`, exhaustive enumeration of all `C(5,3)=10` labeled sets in each mask gives:

```text
F0  = {024}
Fa  = {024,034,124,134}
Fb  = {013,014,023,024}
Fab = {013,014,023,024,034,123,124,134}
```

Thus `P=(Fa∩Fb)\F0=∅` and **`Q=Fab\(Fa∪Fb)={123}`**. In particular the family-level Boolean diamond fails even though the intersection equality holds.

Now encode each increasing three-center tuple as a path from a synthetic start through ranks 1,2,3 to a synthetic sink. Edges retain the center **index and rank**; initial and terminal arcs are included. Let `Ea,Eb,Eab` be the unions of labeled arcs on their respective optimizer paths. Direct enumeration gives the stronger property

```text
Eab = Ea ∪ Eb
```

so **there is no jointly admitted neutral/new edge**. The unique Q-path `123` uses four edges, whose colors under membership in the single-closure graphs are exactly

```text
start→1 : A-exclusive
1→2     : A-exclusive
2→3     : B-exclusive
3→sink  : B-exclusive
```

All four optimizer graphs are path-language faithful: enumerating all increasing 3-center paths accepted by the union-of-edges graphs returns exactly their corresponding F. Thus the previous synthetic graph-only mechanism is **geometrically realizable with five events** in the same indexed-radius-two model.

## Minimality in the declared finite gap alphabet

For `n∈{3,4}`, all original gap words over `{1,2,3}`, all pairs of distinct length-3 gaps contracted to 2 and every `1≤K≤n`, the executable checked 39 configurations, including 16 with a common finite optimal cost. None has nonempty Q. Consequently **five events are minimal for switch-only Q within this declared original-gap alphabet and contraction rule**.

This is a completely enumerated finite minimality statement, not a bound for an unrestricted alphabet of integer gaps. For `n=5`, the displayed witness has `Q={123}`.

## Exact computation and source

Program: `VERIFY_R5_N5_SWITCH_ONLY.py` (Python standard library), independently authored for this result. Execute `python VERIFY_R5_N5_SWITCH_ONLY.py > result.json`. On the executed local version:

- Status: `PASS_R5_N5_GEOMETRIC_SWITCH_ONLY_Q`;
- full result length: 39 smaller-event configurations, 16 common finite optima, no smaller Q;
- `result.json` SHA-256: `d9eb071c990be19f5682c19a934815e846052281c6ceec6b419585f1ac451c56`;
- `VERIFY_R5_N5_SWITCH_ONLY.py` SHA-256: `5b82b8ad0e5acf123362999600f1cf43c3b9b86feefed3212696ee5e439fc861`.

The executable checks exact integer costs, full optimizer families, P/Q membership, color signatures, edge equality, and path-language faithfulness. No floating-point arithmetic or unenumerated cases occur in the stated finite certificate.

## Research consequence and next unit

Two separated geometric contractions can create a new optimal center configuration **solely by splicing two already singly admissible rank-labeled path pieces**. The no-neutral-edge condition by itself is insufficient to guarantee the optimizer Boolean diamond. To understand the 954-event R5 special case, identify the rank/coverage constraint that forbids such A→B switches across its effective cuts 8 and 9; test whether mandatory anchors, center-budget slack or exact cost decompositions provide an intrinsic geometric certificate. Preserve the previous all-64 frozen special-case diamond theorem unchanged.

This work is an **auxiliary one-dimensional integer observer**; no native-X6 transfer, formal task ownership, independent review, or Result admission is asserted.
