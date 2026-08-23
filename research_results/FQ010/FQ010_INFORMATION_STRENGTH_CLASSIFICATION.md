# FQ010 — Information-Strength Classification

Researcher-ID: `EM-FQ010-CA2555`

## 1. Objects being compared

The task requires an information-order comparison among:

1. primitive typed content `(U,tau)`;
2. `R_type=ker(tau)` as a relation/partition object;
3. `Q_K=|R_type|` as a scalar;
4. the FQ008 scalar field `Q`.

The comparison is about recoverable information, not merely equality of formulas.

## 2. Information order

At the declared strengths,

`primitive typed content  ->  R_type  ->  Q_K`

and the FQ008 theorem gives

`Q = Q_K`

on the declared sector domain.

Therefore the scalar nodes have equal theorem information:

`Q_K <=> Q`.

The arrows above are generally noninvertible.

### Typed content -> relation loses component labels

`R_type` remembers which tokens lie in the same type fiber but forgets the literal component names. Component relabeling therefore changes `tau` while preserving the same unlabeled partition structure.

This loss is intentional and compatible with the full `S3` gauge symmetry.

### Relation -> scalar loses partition information

`Q_K` counts relation pairs but does not retain how those pairs are organized into equivalence blocks.

This is a strict loss even after quotienting away token names and component labels.

## 3. Explicit orbit-level collisions

### Collision at 25

Two inequivalent unlabeled contents are:

- `(0,0,5)`, with one occupied component block of size `5`;
- `(0,3,4)`, with two occupied component blocks of sizes `3` and `4`.

Yet

`0^2+0^2+5^2 = 0^2+3^2+4^2 = 25`.

Thus the scalar does not determine occupied-support cardinality, total token cardinality, or block-size multiset.

### Collision at 65

Two two-component states are:

- `(0,1,8)`;
- `(0,4,7)`.

Both satisfy

`1^2+8^2 = 4^2+7^2 = 65`,

but their block-size multisets differ.

This shows that information loss persists even when both states have exactly two occupied components.

## 4. Same scalar is not same relation

The scalar map

`R_type -> |R_type|`

is many-to-one. Therefore a proof that FQ008 and K produce the same scalar does not imply that FQ008 reconstructs:

- the component partition;
- which tokens are same-component;
- the multiplicity multiset;
- the line's component provenance.

If `(U,tau)` is separately supplied, those objects can be re-derived from the primitive substrate. That recovery is not caused by the scalar.

## 5. Presentation-level collision is even stronger

Even when two relations have the same block-size multiset, distinct assignments of token occurrences to blocks can yield different literal relations on a fixed named carrier while remaining isomorphic under token renaming. Thus literal relation information exceeds unlabeled partition information, which itself exceeds cardinality information.

The FQ010 semantic comparison uses the presentation-independent level, so the orbit-level witnesses above are sufficient to prove strict loss without relying on arbitrary token names.

## 6. Classified order

A precise order is:

`(U,tau)`

`> R_type as a labeled relation`

`>= unlabeled component partition / block-size multiset`

`> Q_K`

`= Q_FQ008`.

The first `>=` becomes strict when literal component labels or token occurrences are counted as information; after quotienting the allowed presentation gauges, `R_type` still retains the partition/block-size structure that the scalar loses.

## Result

`RELATION_VS_SCALAR_INFORMATION_STRENGTH_CLASSIFIED = PASS`.

`Q_K_AND_FQ008_HAVE_IDENTICAL_SCALAR_THEOREM_CONTENT = TRUE`.

`Q_K_OR_FQ008_SCALAR_RECONSTRUCTS_RELATION_INFORMATION = FALSE`.

The K route therefore has a genuine information-layer advantage before scalarization, but that advantage does not by itself assign a scale meaning to the scalar readout.
