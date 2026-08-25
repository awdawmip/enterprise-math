# Diagonal Gauge Refoundation — Phase B global path typing

Status: `RAW REFOUNDATION CANDIDATE / EXACT CURRENT-SOURCE TYPING`
Date: `2026-08-25`
Researcher-ID: `EM-DGR-8C2D41`
Owner branch: `research/diagonal-gauge-refoundation`
Depends on Phase A package at owner head `90c7797e88d4ed8944eb3533e7d49d6d7732a314`.

Primary disposition:

`ZERO_DISPLACEMENT_TRIAD_HAS_NONTRIVIAL_CLOSED_PATH_WITNESSES__IDENTITY_PATH_REFUTED__CURRENT_NATIVE_LINE_AND_BRC_FIBERS_REMAIN_TWO_COMPONENT_ONLY`

## 1. Exact current source facts used

From `PACKET_PATH_FOUNDATION.md`:

- native PATH is an ordered adjacency walk;
- every transition contributes exactly `1` to `PATH_COUNT`;
- loops and immediate reversal are allowed;
- path count is not geometric length.

From the frozen native line definition:

- in a translated/current sector, `X_iX_j` and `X_jX_i` are two distinct cell trajectories with the same terminal;
- a reverse-third-family nearest-center carrier edge reaches that same carrier terminal;
- that reverse-third edge is not a member of the `T_{1,1}^{(ij)}` native line trace.

From the BRC multipath bridge:

- the current component-typed BRC line skeleton contains only `{X_i,X_j}` for a fixed sector;
- the third-family edge lies outside that declared line language;
- component typing precedes carrier enrichment.

No global three-generator line trace is assumed.

---

## 2. Minimal closed-loop theorem

Fix a translated sector `S_ij(P)` and its local `(1,1)` commuting diamond.

Let

`p_1 = X_i X_j`,

`p_2 = X_j X_i`

be the two distinct length-2 cell paths from the sector anchor cell `s` to their common terminal cell `t`.

Let

`e_k^- : s -> t`

be the frozen reverse-third-family nearest-center shortcut.

Because native adjacency paths permit reversal, the reversed adjacency transition

`(e_k^-)^{-1} : t -> s`

is a valid one-transition path.

Define

`L_1 = p_1 ; (e_k^-)^{-1}`,

`L_2 = p_2 ; (e_k^-)^{-1}`.

### Theorem DG-B1 — two nontrivial closed path witnesses

`L_1` and `L_2` are two distinct native PATH witnesses from `s` back to `s`, each with

`PATH_COUNT=3`.

They are not the identity path, whose transition count is `0`.

Freeze candidate:

`COMMUTING_DIAMOND_PLUS_REVERSE_THIRD_EDGE_YIELDS_TWO_LENGTH3_NATIVE_CLOSED_PATHS = true`.

This theorem is path/adjacency-level. It does not call either loop a native line.

---

## 3. Endpoint displacement of the loops

Phase A gives in the derived diagonal displacement group

`g_i+g_j=-g_k`.

The shortcut `e_k^-` has the same endpoint displacement as `X_iX_j` but is a different path/line object. Therefore its reversed transition has endpoint displacement `g_k`.

Hence

`End_D(L_1)=End_D(L_2)=g_i+g_j+g_k=0`.

### Theorem DG-B2 — zero displacement is not identity path

The current system admits concrete witnesses with

`ENDPOINT_DISPLACEMENT=0`

and

`PATH_COUNT=3`.

Therefore

`ZERO_DERIVED_DISPLACEMENT != IDENTITY_PATH`.

This sharpens the Phase-A boundary. The correct statement is not `X_1X_2X_3=id`; it is that a three-transition closed excursion may have zero endpoint displacement while retaining nontrivial path provenance.

---

## 4. Iterated loop family

Because each `L_a` returns to the same start cell, any concatenation of `m` choices from `{L_1,L_2}` is automatically composable.

### Theorem DG-B3 — exponential closed-history lower bound

For every `m>=1` there are at least

`2^m`

distinct native path histories from `s` to `s` with transition count `3m`, obtained by blockwise concatenation of the two commuting-diamond loops.

This is a lower bound, not a complete classification of all length-`3m` closed paths.

It follows immediately that the unrestricted native PATH layer may have arbitrarily many nontrivial histories with the same endpoint. This is consistent with PF-06 and is not a defect.

---

## 5. Why this does not inflate the frozen native line fiber

The frozen native line identity `T_{a,b}^{(ij)}` allows only component-preserving words in `{X_i,X_j}`.

The closing third-family edge lies outside that language.

Therefore the paths `L_1,L_2` are **not** representatives of `T_{0,0}`, `T_{1,1}`, or any other frozen two-component line trace merely because they close.

Freeze candidate:

`CLOSED_NATIVE_PATH != NATIVE_LINE_TRACE_IDENTITY`.

`DIAGONAL_ZERO_DISPLACEMENT_LOOPS_DO_NOT_DRESS_R061_LINE_FIBER_UNDER_CURRENT_LINE_MEMBERSHIP`.

Thus the finite binomial line fibers and the jitter/parabola two-generator fibers remain unchanged.

---

## 6. Current BRC boundary

The R062 component-typed BRC line bridge is declared on a fixed sector skeleton with generator relations `{R_i,R_j}`.

The third-family edge is explicitly outside that line skeleton.

Therefore the Phase-B closed loops are not automatically elements of the current `PATH_FORMAL_BRC` object used to realize one native line.

A future **global packet-path BRC** may include all three direction families, but that is a new N1/enrichment typing problem.

Freeze candidate:

`CURRENT_R062_LINE_BRC_FIBER_REMAINS_TWO_COMPONENT_ONLY`.

`GLOBAL_THREE_COMPONENT_PATH_BRC = NOT_YET_FROZEN`.

---

## 7. I0 carrier-wide balanced word family

At the classical/implementation triangular carrier level, the three oriented nearest-neighbor direction families may be represented by lifted increments with total

`e_1+e_2+e_3=0`.

This relation is permitted as `I0_IMPLEMENTATION_CARRIER` / adjacency realization data but not as a primitive native Euclidean vector identity.

Under that carrier labeling, every word with equal counts `m` of the three direction families returns to its starting carrier center, and the formal labeled word count is

`(3m)!/(m!)^3`.

Classification:

`I0_BALANCED_DIRECTION_WORD_CLOSURE = EXACT_CARRIER_COMBINATORICS`.

However selection of this entire labeled subfamily as one canonical native three-component trace/path fiber is **not** currently frozen.

Therefore the earlier `~27^m/m` asymptotic may be retained only as an I0/N1 conditional family count, not as the multiplicity of a frozen native line object.

---

## 8. Stronger semantic correction to the earlier parabola discussion

The correct hierarchy is now:

1. generic native PATH layer already permits nontrivial loops and repeated histories;
2. current native LINE selects a finite two-component trace language and therefore deliberately excludes third-family loop dressing;
3. diagonal gauge tracks endpoint displacement and forgets path provenance;
4. BRC enrichment can retain path multiplicity only on an explicitly declared typed skeleton.

Hence same endpoint / zero displacement is compatible with a large path fiber without forcing line-identity collapse.

This is precisely why diagonal gauge can be restored at the displacement layer without undoing R061/R062 line typing.

---

## 9. Phase-B verdict

Freeze candidate verdicts:

- `BALANCED_TRIAD_ZERO_DISPLACEMENT = EXACT_DERIVED`;
- `NONTRIVIAL_LENGTH3_CLOSED_NATIVE_PATH_WITNESSES = ESTABLISHED`;
- `BALANCED_TRIAD_IDENTITY_PATH = REFUTED`;
- `GLOBAL_THREE_GENERATOR_NATIVE_LINE_TRACE = NOT_ESTABLISHED`;
- `CURRENT_TWO_COMPONENT_LINE_FIBERS = UNAFFECTED`;
- `CURRENT_R062_COMPONENT_TYPED_LINE_BRC = UNAFFECTED`;
- `GLOBAL_THREE_COMPONENT_BRC_ENRICHMENT = OPEN_N1_TYPING`.

## 10. Next

Phase C should audit whether the derived diagonal displacement group can be made the **canonical endpoint forgetful object** for arbitrary PATH/BRC while remaining non-injective on provenance, and whether this produces a clean commuting diagram

`PATH -> TRACE / PATH-FORMAL BRC -> ENDPOINT DISPLACEMENT G_D -> BOOLEAN SUPPORT`

without changing current line identity.
