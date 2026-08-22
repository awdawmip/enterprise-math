# R064 Phase A — Local Context Equivalence Classification

Freeze: `2026-08-22T15:49:42+08:00`  
Task: `RS-R064-PHASEA-N0-FIRST-LOCAL-INTERACTION-CARRIER-RECONSTRUCTION`

## Scope

An elementary event is one occurrence in a frozen finite sector-local path representative. Its N0 pair-local reduct retains only:

1. whether the two occurrences have the same source representative;
2. if they have the same source, whether their intrinsic positions are equal / earlier / later;
3. the ordered source-sector memberships;
4. the two native component tags;
5. for distinct sectors, the shared-axis incidence already present in the three-sector atlas.

The remainder of each source word is deliberately not retained. Numeric position indices used by the checker are implementation coordinates; only equality and intrinsic finite order are semantic.

## Exact automorphism group

The declared atlas has three distinct axes and one two-axis sector for every unordered axis pair. No preferred global orientation is declared. Every permutation of the three axes preserves sector incidence, shared-axis identity and component typing, and induces a relabeling of every finite path representative. Conversely any substrate automorphism restricts to a permutation of the three axes.

Therefore:

`Aut(N0_local_atlas) = S3`, of order `6`.

The statement in the line-trace definition that the construction transports cyclically proves that the 3-cycle is admitted; it does not introduce an orientation predicate excluding reflections.

## Eleven pair-local orbits

Write `SS` for same source and `DS` for distinct source. When sources are distinct and sectors differ, `SHARED` means the event tag is the unique axis common to the two sectors and `PRIVATE` means the other axis of that event's own sector.

The complete smallest relational quotient has exactly 11 classes:

1. `SS_EQ_SAME`
2. `SS_LT_SAME`
3. `SS_LT_DIFF`
4. `SS_GT_SAME`
5. `SS_GT_DIFF`
6. `DS_SAMESECTOR_SAME`
7. `DS_SAMESECTOR_DIFF`
8. `DS_DIFFSECTOR_SHARED_SHARED`
9. `DS_DIFFSECTOR_SHARED_PRIVATE`
10. `DS_DIFFSECTOR_PRIVATE_SHARED`
11. `DS_DIFFSECTOR_PRIVATE_PRIVATE`

There are 66 labeled abstract contexts before quotienting. Each of the eleven classes is one `S3` orbit of size six, hence every pointed local-context orbit has trivial stabilizer.

This classification is exhaustive because:
- same source implies same sector and gives exactly `EQ/LT/GT`;
- equality of positions forces equality of the event occurrence and therefore equality of its component tag;
- distinct sources in the same sector have only `SAME/DIFF` component relation at pair-local strength;
- any two distinct sectors in the three-sector atlas share exactly one axis, so each ordered event is either `SHARED` or `PRIVATE`, yielding the four ordered combinations above.

## Regression

The deterministic checker enumerates every positive component word of lengths 1 through 5 in every native sector:

- source words: `186`;
- event occurrences: `774`;
- ordered event pairs: `599076`;
- observed classes: `11`;
- unclassified mismatches: `0`.

Observed pair counts are recorded in `R064_PHASEA_REGRESSION.json`.

## Component-only quotient is strictly weaker

For the candidate component carrier, forgetting sector/source/order reduces an ordered event pair to `(tag_1,tag_2)`. Under `S3` this has only two orbits:

- `DIAGONAL`: `tag_1 = tag_2`;
- `OFF_DIAGONAL`: `tag_1 != tag_2`.

The quotient is N0-definable, but the act of requiring a future process law to factor through this quotient is **not** forced by the full eleven-class N0 context. That distinction is theorem-critical.
