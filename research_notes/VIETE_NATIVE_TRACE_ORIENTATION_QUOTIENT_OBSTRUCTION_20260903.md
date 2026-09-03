# Viète native trace-orientation quotient obstruction: endpoint reversal is not trace inversion

Status: `FREE_RESEARCH / EXACT_CURRENT-SEMANTICS BOUNDARY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent note: `research_notes/VIETE_SEGMENT_BISECTOR_ROTATION_PRECISION_20260903.md`

## 1. Question sharpened

The normalized-bisector theorem gives a finite orientation-readout involution law in which reversal acts algebraically as

\[
(c,s)\mapsto(c,-s),
\]

or, in a group character, as

\[
u\mapsto u^{-1}.
\]

Can that reversal be identified directly with the current canonical native operation of swapping the endpoints of a segment?

Current R061 line/segment semantics give a negative answer unless an additional quotient theorem is supplied.

## 2. Current canonical native distinction

For a nonzero segment with endpoints `P,Q`, the canonical directed traces are

\[
T(P\to Q),\qquad T(Q\to P).
\]

The current frozen segment definition distinguishes the groupoid inverse traversal of the first trace from the newly decoded canonical reverse trace:

\[
\boxed{T(P\to Q)^{-1}\neq T(Q\to P)}
\]

for every nonzero segment.

The canonical unoriented segment is therefore not one trace modulo inversion. It is the tagged bidirectional pair

\[
\boxed{
BSEG_E(P,Q)=\{T(P\to Q),T(Q\to P)\}.
}
\]

The orientation tag must be retained.

## 3. Consequence for a rotation-character quotient

Let `chi` be any proposed group-valued orientation character on native directed trace data. Functorial inversion of a traversed trace would require

\[
\chi(T(P\to Q)^{-1})=\chi(T(P\to Q))^{-1}.
\]

If endpoint swap is also required to become orientation inversion, one additionally requires

\[
\chi(T(Q\to P))=\chi(T(P\to Q))^{-1}.
\]

Combining the two equations forces

\[
\boxed{
\chi(T(P\to Q)^{-1})=\chi(T(Q\to P))
}
\]

even though the two arguments are distinct canonical trace objects.

Therefore any such `chi` is necessarily a **nontrivial quotient/collapse** of the current native trace semantics. The identification is not already present in R061 and cannot be silently inherited from classical vector reversal.

Freeze:

`ENDPOINT_SWAP_TO_CHARACTER_INVERSION = REQUIRES_EXPLICIT_QUOTIENT_THEOREM`.

## 4. Gauge evidence that the quotient is genuinely lossy

The current directed native gauge is generally reversal-asymmetric. The canonical unoriented datum is a bidirectional spectrum rather than one symmetric scalar.

For example, the frozen unit positive-axis segment has

\[
SPEC_E=\{1,\sqrt2\}.
\]

Hence endpoint reversal is not, in current native gauge semantics, a length-preserving involution on one scalar line state.

A unit-modulus rotation character may deliberately forget that directed gauge asymmetry, but then it is an effective orientation quotient, not an isometric restatement of the native segment.

Freeze:

`ROTATION_CHARACTER_REVERSAL != NATIVE_DIRECTED_GAUGE_ISOMETRY`.

## 5. Minimum state implication

The current geometry separates:

- instantaneous native state: one Cell;
- native line identity: component trace;
- path representative: one Cell trajectory in the trace fiber;
- unoriented segment: two independently decoded directed traces with retained orientation tag.

Therefore a #1158 bridge cannot be specified merely by saying “the Cell rotates through six/twelve directions.” It must declare which typed object is mapped to the finite orientation state and what information the map intentionally forgets.

The minimum currently defensible bridge domain is trace-aware, e.g. an oriented trace/segment state, not an untyped bare Cell label.

This does not prove that no Cell-plus-memory realization exists. It proves that **current canonical semantics do not provide a Cell-only identification of endpoint reversal with character inversion**.

## 6. Parity boundary corrected at native strength

The predecessor proves at the G1 orientation-readout layer:

- longitudinal Viète factors are reversal-even;
- signed transverse states are reversal-odd;
- scalar precision defect is reversal-even/quadratic.

At native R061 strength, endpoint swap is a different operation from trace inversion and may change the directed gauge. Therefore those parity statements must be attached to the **character reversal** operation, not automatically to canonical endpoint exchange.

A future native bridge must prove an intertwining law of the form

\[
\chi(\operatorname{ReverseNative}(T))
=
\operatorname{InverseCharacter}(\chi(T))
\]

for whichever native reversal operation it chooses. Without that theorem, G1 even/odd parity cannot be promoted to G0 endpoint-swap parity.

## 7. Updated #1158 native bridge obligations

Native promotion of the Viète refinement now requires at least four independently typed ingredients:

1. `DOMAIN`: choose a trace-aware native segment/trajectory state rather than silently using a bare Cell;
2. `QUOTIENT`: construct an operation-safe map to the finite oriented quotient;
3. `REVERSAL`: prove which native reversal operation descends to character inversion, acknowledging that canonical reverse trace is not groupoid inverse;
4. `REFINEMENT`: supply the antipodal quarter-turn extension and prove normalized-bisector compatibility with actual Cell/trace transition semantics.

This is stronger than the earlier generic statement that a Cell-to-orientation bridge is missing. The current line theory identifies an exact reason why the reversal part of that bridge cannot be assumed for free.
