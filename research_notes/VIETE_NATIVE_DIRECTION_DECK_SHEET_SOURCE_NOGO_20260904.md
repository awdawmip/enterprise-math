# Viète native direction/deck sheet source audit: bidirectional segment and FCC antipodes do not supply the fixed-radius H sheet

Status: `FREE_RESEARCH / EXACT CURRENT-SEMANTICS SOURCE NO-GO / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Depends on:
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`
- `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`
- `driver_reviews/R059D_STAGE_AT4_S1_DISCRETE_CELL_STATE_CORRECTION_20260817.md`
- `research_notes/VIETE_DIRECTION_SHEET_SWEEP_CHIRALITY_V4_CORRECTION_20260904.md`

## 1. Question

The corrected #1158 typing distinguishes:

\[
H:u\mapsto-u
\]

as the direction/half-turn deck involution from

\[
S:u\mapsto u^{-1}
\]

as sweep-chirality inversion.

The connected cover

\[
C_3\leftarrow C_6
\]

needs an `H`-typed two-sheet direction carrier before its loop holonomy can even be discussed.

Does current native Foundation already contain such a carrier under another name?

The two obvious candidates are:

1. the bidirectional canonical segment pair `BSEG_E(P,Q)`;
2. the antipodal direction pairs in the centrally symmetric FCC carrier.

Both fail at the required native fixed-radius strength.

## 2. What the rotating-segment state actually requires

The current discrete rotation correction freezes:

`ROTATING_SEGMENT_NATIVE_STATE = ONE_CELL_PER_TRAJECTORY_STEP`.

For a fixed-length rotating segment, the minimum candidate state is

\[
S=(\rho,C,\epsilon),
\]

where:

- `rho` is the fixed vector radius;
- `C` is the current native Cell;
- `epsilon` is local sweep orientation.

Thus a candidate `H` direction sheet for this object must be compatible with the **same fixed-radius rotation object**. It cannot obtain its second sheet merely by changing the object’s basepoint, changing its native gauge, or invoking a carrier-only opposite ray.

## 3. BSEG is a genuine C2 pair, but of the wrong typed object

For a nonzero unordered endpoint pair `{P,Q}`, current R061 semantics freezes

\[
BSEG_E(P,Q)
=\{T(P\to Q),T(Q\to P)\}.
\]

Endpoint swap acts freely on these two canonical directed traces. Therefore, as a bare set with involution, `BSEG_E(P,Q)` is indeed a legitimate free `C2` torsor.

This is useful and should not be denied.

However, its two elements are **independently decoded directed native traces with different basepoints**.

Current Foundation explicitly allows them to have different:

- sector labels;
- component triples;
- path-fiber cardinalities;
- directed line gauges.

Moreover

\[
\boxed{T(P\to Q)^{-1}\neq T(Q\to P)}
\]

for every nonzero segment.

Thus endpoint swap is not traversal inversion of one fixed directed trace object.

## 4. Fixed-radius witness: the positive-axis unit segment

The frozen unit positive-axis segment has bidirectional length spectrum

\[
\boxed{SPEC_E(P,Q)=\{1,\sqrt2\}.}
\]

Hence the two canonical directions of the same unordered endpoint pair do not even share one directed native radius/gauge value.

A fixed-radius rotation sheet `H` must relate two states of the same rotating object at the same declared `rho`.

Therefore the canonical BSEG swap cannot be identified with the required fixed-radius half-turn sheet merely from current line semantics.

Freeze:

`BSEG_ENDPOINT_SWAP_C2 = REAL_NATIVE_TORSOR`.

`BSEG_ENDPOINT_SWAP_C2 != FIXED_RADIUS_ROTATION_H_SHEET`.

The distinction is semantic, not cardinality-based.

## 5. Anchored rotation makes the mismatch stronger

The vector-radius rotation program treats `rho` as the fixed radius of one rotating segment and `C` as the current tip/Cell state along that shell.

Swapping the ordered endpoints of a segment changes which endpoint is used as the source/base for the independently decoded canonical trace.

That is not the same operation as keeping the same rotation center/base and moving the tip to a half-turn state on the same radius shell.

Classically those two pictures can be related by a negative vector. Current native geometry deliberately does not supply primitive negative axes, so that identification is not available for free.

Therefore:

\[
\boxed{
\text{ENDPOINT SWAP}
\neq
\text{ANCHORED HALF-TURN OF ONE FIXED-RADIUS NATIVE ROTATING SEGMENT}
}
\]

at current Foundation strength.

## 6. FCC antipodes are also the wrong layer

The selected FCC coordinate carrier has a centrally symmetric first shell. Its 12 contact rays form six unoriented line families

\[
[v]=\{v,-v\}.
\]

This looks like an immediate source of a two-sheet direction bit.

But current FCC Foundation explicitly freezes:

- FCC is a **carrier readout**, not native identity;
- the six line families are **unoriented carrier line families**;
- chart-local sign is an implementation/readout orientation, not a primitive native negative axis;
- carrier direction relations are not native vector relations;
- until the exact native-to-carrier bridge is proved, do not identify a native positive ray with a Euclidean opposite-pair quotient.

Therefore the FCC antipodal pair cannot be imported as the native `H` sheet required by #1158.

Freeze:

`FCC_ANTIPODAL_RAY_PAIR = CARRIER_DIRECTION_DATA`.

`FCC_ANTIPODAL_RAY_PAIR != NATIVE_FIXED_RADIUS_H_SHEET`.

## 7. Two tempting shortcuts are independently blocked

The two candidates fail for different reasons:

### Native BSEG pair

It is genuinely native, but its two elements are different directed trace objects with potentially different gauges/basepoints. It is not a same-`rho` anchored half-turn sheet.

### FCC antipodal pair

It has exactly the desired carrier antipodality, but it is not native. Current typing explicitly forbids promoting the carrier sign to a primitive native negative direction.

Thus neither source satisfies both requirements simultaneously:

\[
\boxed{
\text{NATIVE}
+
\text{SAME FIXED-RADIUS ROTATION OBJECT}
+
\text{FREE H INVOLUTION}
}
\]

from current commitments.

## 8. Current native information lower bound for the H sheet

The #1158 cycle-cover route therefore requires a genuinely new bridge object or theorem at the direction-sheet layer.

The weakest target is not “add a negative axis”. A more precise requirement is:

> For each coarse fixed-radius orientation state in the declared quotient, construct a two-element fiber `D_x` with a free involution `H`, such that both elements are states/readouts of the same fixed-radius rotating object and the fiber is compatible with Cell transport.

No primitive signed coordinate axis is required by this formulation.

What must be proved is the existence and operation-safe transport of the **two-sheet direction torsor**, not a classical vector-space negative direction.

Call this missing object provisionally

\[
\boxed{DIRECTION\_DECK\_TORSOR_{\rho}}.
\]

This is a research target name, not a Foundation promotion.

## 9. Once D exists, the previous holonomy theorem applies

Suppose a future native theorem constructs such a direction/deck torsor over the coarse cycle.

Then the generic finite `C3/C2` transport classifier immediately applies to its edge transitions. The only gauge-invariant loop datum is the XOR holonomy class.

Thus the native work should not re-prove cohomology/holonomy mathematics. It should prove:

1. the **typed existence** of `DIRECTION_DECK_TORSOR_rho`;
2. which holonomy class its actual Cell transport realizes;
3. which classes are effective.

This is now a sharply bounded geometric problem.

## 10. Relation to sweep epsilon

Current local sweep variable `epsilon` remains useful, but it is `S`-typed rather than `H`-typed.

At the quarter-turn seed the `H` and `S` actions happen to exchange the same two root states, so `epsilon` may label the two seed roots up to a global convention.

From the next refinement onward the `V4` theorem proves that `H` and `S` separate. Therefore `epsilon` cannot substitute for the missing direction/deck torsor throughout the tower.

## 11. Updated #1158 native frontier

Inside the six-gate/cycle-cover route, the first unresolved G0 object is now exactly:

\[
\boxed{
\text{a native fixed-radius direction/deck }C_2\text{ torsor over the coarse orientation quotient}
}
\]

with no silent use of:

- endpoint-swapped BSEG as same-radius reversal;
- FCC carrier antipodes as native negative directions;
- sweep chirality as the deck sheet.

After that object exists, the remaining problems are its nontrivial/effective loop holonomy and the cross-layer principal-root chart bridge already isolated elsewhere.

This is the smallest current native object that #1158 still lacks before the existing finite holonomy/refinement machinery can take over.
