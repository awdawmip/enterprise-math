# R062 Stage 0 — Forgetful Maps and Homomorphism Audit

Researcher-ID: `EM-R062-7C4A91`  
Status: `FORGETFUL_MAPS_CLASSIFIED`

## 1. Path formal sums -> N multiplicity

On the many-object formal path algebra, define entrywise augmentation:

`epsilon(sum_p n_p [p]) = sum_p n_p`.

Because formal addition preserves repeated occurrences/provenance and typed concatenation distributes, augmentation commutes with entrywise addition and with matrix/category convolution over shared intermediate states.

Classification:

`PATH_FORMAL_SUM_TO_N = GLOBAL_HOMOMORPHISM_FOR_PROVENANCE_TAGGED_FORMAL_PATH_OCCURRENCES`.

This is the exact algebraic realization of `PATH_BRC -> N_BRC` used by the positive bridge.

## 2. Ordinary finite path sets -> N cardinality is NOT globally additive

If Path-BRC were instead represented by ordinary sets with idempotent set union, cardinality would not be a global semiring homomorphism.

Minimal counterexample: `A={p}`. Then `|A union A| = 1` while `|A|+|A| = 2`.

Classification:

`PATH_SET_CARDINALITY_TO_N = NOT_GLOBAL_SEMIRING_HOMOMORPHISM`.

On the canonical native trace enumeration used here, witnesses are generated uniquely and branch decompositions are disjoint, so finite-set cardinality happens to recover the same count on this slice. The theorem-level enrichment nevertheless uses formal path occurrences, not this accidental restriction.

## 3. N -> Boolean

Define `beta(n) = 0` when `n=0`, and `1` when `n>0`.

Then over `N`:

`beta(a+b) = beta(a) OR beta(b)`

and

`beta(ab) = beta(a) AND beta(b)`.

Thus `beta` is the standard semiring support homomorphism `N -> B`. The checker exhaustively sanity-checks both laws for `0<=a,b<=20`; the global law follows directly from positivity in `N`.

Classification:

`N_TO_BOOLEAN = GLOBAL_SEMIRING_HOMOMORPHISM`.

## 4. Path -> Boolean direct support

For every typed hom-entry, send a path family/formal sum to `1` iff at least one witness exists. Under object-wise typed union and composition, this is exactly existential relational support.

Classification:

`PATH_TO_BOOLEAN = GLOBAL_SUPPORT_HOMOMORPHISM_FOR_TYPED_UNION_AND_COMPOSITION`.

The shared-middle object is essential: forgetting middle identity before composition is precisely the canonical R023 middle-incidence warning.

## 5. Operation audit

| Operation | Path formal sum -> N | N -> Boolean | Native caveat |
|---|---|---|---|
| branch sum/merge | exact | exact | ordinary set-union cardinality is not exact on overlap |
| typed composition | exact | exact | shared middle state must remain typed |
| recoalescence | multiplicity preserved only by enriched formal sum, not canonical Boolean union | canonical support exact | canonical BRC deliberately discards multiplicity/provenance |
| state relabeling | exact under bijective transport | exact | relabel state and generator labels coherently |
| translated placement | exact | exact | start vertex remains part of typed state/trace |
| trace quotient | not a coefficient forgetful map; separate quotient of witness identity | not equivalent to Booleanization | preserves component content while Booleanization preserves support |

## 6. Conclusion

The requested chain is valid only after its strongest layer is typed correctly:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

It is **not** valid as a blanket claim that ordinary path-set cardinality is a semiring homomorphism. This distinction is a required falsifiability boundary of the bridge.
