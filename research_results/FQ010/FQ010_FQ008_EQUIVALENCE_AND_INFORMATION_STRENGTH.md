# FQ010 — FQ008 Equivalence and Information Strength

Researcher-ID: `EM-FQ010-CA2555`

## Domain

Work on one declared two-channel sector with nonnegative integer coordinates `(a,b)`. The three sectors are obtained by component relabeling.

For Interface K,

`Q_K(a,b)=|R_type|=a^2+b^2`.

For Interface F, use exactly the FQ008 integration-candidate conditions at

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@b6ec6eb58f1c724657db7c5bd7deb82827774439`:

- `Q(a,0)=a^2` and `Q(0,b)=b^2`;
- `Delta_a Delta_b Q=0` on every elementary sector plaquette.

## 1. K -> F

### Axis-square calibration

On an axis only one component fiber is occupied with size `n`. Therefore

`R_type = U x U`

for that one fiber, and

`Q_K(n,0)=|U x U|=n^2`.

The same holds on the other active axis.

### Transverse independence

For

`Q_K(a,b)=a^2+b^2`,

compute exactly:

`Q_K(a+1,b+1)-Q_K(a+1,b)-Q_K(a,b+1)+Q_K(a,b)=0`.

Relationally, this is the numerical shadow of

`R_type=(U_a x U_a) disjoint_union (U_b x U_b)`:

adding tokens to one component does not create same-component relation-pairs with the transverse component.

### Sector sum of squares

It follows immediately that Interface K satisfies the full FQ008 scalar interface and its derived sector theorem.

Thus

`K_SCALAR => FQ008_SCALAR_AXIOMS`.

## 2. F -> K-scalar

Assume the FQ008 scalar conditions only.

Define the first difference

`D_a(a,b)=Q(a+1,b)-Q(a,b)`.

The vanishing mixed second difference is exactly

`D_a(a,b+1)=D_a(a,b)`.

Hence `D_a(a,b)` is independent of `b`. Summing first differences from `0` to `a-1` gives

`Q(a,b)-Q(0,b)=Q(a,0)-Q(0,0)`.

Axis calibration gives `Q(0,0)=0`, `Q(a,0)=a^2`, and `Q(0,b)=b^2`. Therefore

`Q(a,b)=a^2+b^2`.

But the K cardinality theorem gives

`Q_K(a,b)=a^2+b^2`.

So on every sector-supported content,

`Q=Q_K`.

By the allowed component relabelings this holds on all three native sectors.

Therefore

`FQ008_SCALAR_AXIOMS <=> Q_K_SCALAR_FIELD`

on the declared sector domain.

## 3. What the reverse direction does not recover

The reverse implication is scalar-strength only.

From equality

`Q(a,b)=Q_K(a,b)`

one does **not** reconstruct the relation object `R_type` from the scalar value. The scalar remembers only one integer.

For example,

- orbit signature `(0,0,5)` has `Q_K=25`;
- orbit signature `(0,3,4)` also has `Q_K=25`.

The corresponding component partitions are not isomorphic: one has one occupied block of size `5`, the other has two occupied blocks of sizes `3` and `4`.

Likewise,

- `(0,1,8)` and `(0,4,7)` both give `Q_K=65`;
- their partition block-size multisets differ.

Thus scalar equality cannot recover support count, total token count, block-size multiset, or same-component relation.

If the primitive typed content `tau` is separately retained, `R_type` can of course be re-derived from `tau`; that is independent of the scalar and must not be misreported as scalar reconstruction.

## 4. Theorem equivalence versus semantic equivalence

The exact result is:

- **scalar theorem content:** equivalent;
- **relation information content:** not equivalent;
- **semantic origin:** different;
  - F starts from a scalar field plus two scalar conditions;
  - K starts from a definable relation and then chooses its finite cardinality.

Therefore `same scalar theorem output` is strictly weaker than `same relational information content`.

## 5. FQ008 source status separated from theorem status

- `FQ008_SOURCE_STATUS`: supplied integration-candidate at `b6ec6eb...`; not the definition version present on the FQ010 owner-base, which still has the `9866e523...` primitive Pythagorean formulation.
- `FQ008_THEOREM_STATUS`: exact discrete theorem on the declared sector domain; bidirectional scalar equivalence with `Q_K` is proved above.

No Foundation source is modified by this classification.

## Result

`FQ008_BIDIRECTIONAL_SCALAR_EQUIVALENCE_CLASSIFIED = PASS`.

`FQ008_SCALAR_EQUALITY_RECONSTRUCTS_R_TYPE = FALSE`.

`RELATION_INFORMATION_STRICTLY_EXCEEDS_ITS_CARDINALITY_READOUT = TRUE`.
