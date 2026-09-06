# X6 upper V23: four labeled minimal pure-triadic fields are necessary and sufficient to encode all 20 active triad identities

Status: `FREE_RESEARCH / EXACT FINITE OBSERVER-CAPACITY THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NONFCC-SLICE-REALIZATION`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_THREE_FIELD_RELATIONAL_FRAME_V22_20260906.md`;
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- finite-fiber/observer-preservation principles.
Checker: `experiments/x6_four_field_active_triad_code_v23_20260906/check_four_field_active_triad_code.py`.

## 1. Distinguish two different reconstruction problems

V22 proves that three suitable **labeled** minimal pure-triadic context fields can have trivial joint S6 stabilizer. Thus three fields can remove the global axis-relabeling gauge.

That does not imply that the current active three-axis subset can be reconstructed from the three scalar field values measured on that triad.

V23 asks the stricter observer question:

> how many minimal V18 pure-triadic fields are required so that the vector of their evaluations on an unknown active triad uniquely identifies all 20 possible three-axis subsets?

## 2. Evaluation code

Let the 30 oriented minimal field values be

`H_min={+v_M,-v_M : M perfect matching of K6}`.

Choose r distinct labeled fields

`h_1,...,h_r`.

For an active triad S define its relational signature

`Code_H(S)=(h_1(S),...,h_r(S))`.

Each coordinate lies in `{-1,0,+1}` before the irrelevant V20 scale factor 12.

The field tuple is an **active-triad identity code** iff

`S -> Code_H(S)`

is injective on all `C(6,3)=20` triads.

This is a finite observer-capacity question, not a geometric embedding.

## 3. Exhaustive minimum: r=4

Exact enumeration over all field subsets gives:

- r=1: zero injective field sets;
- r=2: zero injective field sets;
- r=3: zero injective field sets;
- r=4: exactly 480 injective four-field sets.

Therefore

`MINIMAL MINIMAL-TRADE FIELDS FOR FULL 20-TRIAD EVALUATION CODE = 4`.

This is stronger than the simple information bound `3^r>=20`, which only says r>=3. The structured V18 field family has unavoidable collisions for every three-field evaluation map.

## 4. Explicit four-field code

One injective positive-orientation field set comes from the perfect matchings

`M0={{0,1},{2,3},{4,5}}`,

`M4={{0,2},{1,4},{3,5}}`,

`M8={{0,3},{1,5},{2,4}}`,

`M10={{0,4},{1,3},{2,5}}`.

Let the four fields be `v_M0,v_M4,v_M8,v_M10`.

Their 20 signatures are all distinct. Examples:

`012 -> (0,0,+1,+1)`,

`024 -> (+1,0,0,0)`,

`135 -> (-1,0,0,0)`,

`235 -> (0,0,+1,0)`,

`345 -> (0,0,-1,-1)`.

The checker stores and verifies the complete table.

The minimum Hamming and L1 separation between distinct codewords is one, so this is an exact identity code but not an error-correcting code against one arbitrary coordinate error.

## 5. Exact observer reconstruction

For an injective four-field set H, define

`Decode_H : Code_H(T_20) -> T_20`

as the inverse lookup on the twenty realized signatures.

Then

`Decode_H(Code_H(S))=S`

exactly for every active triad.

Thus, in a subsystem where four source-labeled pure-triadic field readings are already legitimate observables, the active-triad label need not also be stored as an independent state variable: it can be reconstructed losslessly from the four readings.

This is an operation-safe quotient only for futures that have continued access to those same four field readings. If the sources disappear or are themselves projected, the active-triad repair coordinate may become necessary again.

## 6. Relation to V22 frame reconstruction

The two minima solve different problems:

- **3 labeled fields**: enough for trivial joint S6 stabilizer / full relational frame token for some field triples;
- **4 labeled fields**: necessary and sufficient to make raw field evaluations injective on all 20 active-triad identities.

A free three-field tuple can determine how axes are relabeled relative to a reference frame while still assigning the same three scalar readings to several possible active triads.

A four-field identity code directly recovers which triad is active from the readings themselves.

Do not conflate frame fixing with object identification.

## 7. Symmetry covariance

For any `g in S6`, transporting both the field set and active triad gives

`Code_{gH}(gS)=Code_H(S)`

when field-source labels retain their positions in the signature vector.

Hence injectivity is preserved over the entire S6 orbit of a four-field code.

A chosen reference four-field code is a relational coordinate convention; no global spatial origin or preferred Euclidean carrier is introduced.

## 8. Counting and source-label boundary

There are exactly 480 **unordered sets of four field values** from the 30-state minimal field orbit that are injective.

If four physical sources are distinctly labeled, every ordering of such a set gives an equivalent 4-coordinate code with permuted coordinate positions.

If field sources are not distinguishable, passing to an unordered multiset of readings can create further collisions. V23 does not claim source-label-free four-field reconstruction.

## 9. Current consequence

The internal/multi-Cell state hierarchy now has two precise capacity thresholds within the minimal field family:

`3 labeled fields -> symmetry-complete relational frame possible`,

`4 labeled fields -> full active-triad identity observable from field values`.

This provides a concrete route for reducing explicit active-triad labels in a sufficiently rich local neighborhood without confusing the reduction with spatial-coordinate collapse.

## 10. Next target

The next question is dynamic rather than static:

> given a four-field identity code and the V20 pairings, which operation-safe update rules can evolve the four field sources and active-triad code without reintroducing arbitrary coordinate tie-breaking, and can such updates generate nontrivial V17 holonomy/Ori6 control?

No Foundation promotion, four-neighbor physical law or error-correction claim is made.
