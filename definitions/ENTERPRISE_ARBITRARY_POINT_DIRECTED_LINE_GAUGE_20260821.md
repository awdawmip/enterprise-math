# 进取任意点原生直线：Translated Trace 与有向 Line Gauge

Status: `ACTIVE / CANONICAL / FROZEN`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Canonical acceptance source:

`driver_reviews/R061_STAGE2_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_DRIVER_REVIEW_20260821.md`

## 1. Scope

This definition extends the frozen origin-based native component-trace line formula to arbitrary integer-addressed native coordinate vertices.

It freezes an exact **directed** point-to-point native line object and directed line-length gauge.

It does **not** freeze a symmetric metric.

## 2. Canonical directed displacement decoding

Let `P,Q` be arbitrary native coordinate/triple-intersection vertices.

Use the frozen implementation carrier only to calculate the signed carrier difference

`delta_I(P,Q)=(r,s) in Z^2`.

Let

`m=min(r,s,0)`.

Define the canonical native positive-axis displacement address

`D_E(P->Q)=(r-m,s-m,-m)`.

Then

- all three components are nonnegative;
- the minimum component is zero;
- the triple is unique;
- no native negative axis is introduced.

Freeze:

`DIRECTED_NATIVE_DISPLACEMENT = UNIQUE_NONNEGATIVE_MIN_ZERO_DECODE`.

This decoding is not a native common-diagonal quotient. It is a carrier-to-native chart decode.

## 3. Translated sector typing

Write

`D_E(P->Q)=(A,B,C)`.

If `P=Q`, then `(A,B,C)=(0,0,0)`.

If exactly one component is positive, the displacement lies on one translated positive native axis.

If exactly two components are positive, the unique zero component selects one translated native right sector:

- `(A,B,0)` -> `S_12(P)`;
- `(0,B,C)` -> `S_23(P)`;
- `(A,0,C)` -> `S_31(P)`.

Translated positive axes have two adjacent sector presentations that glue to one physical directed axis identity.

Freeze:

`ALL_INTEGER_DIRECTED_DISPLACEMENTS_POSITIVE_AXIS_DECOMPOSABLE = true`.

`DISPLACEMENT_DECOMPOSITION_UNIQUE_UP_TO_AXIS_GLUE = true`.

## 4. Translated line identity

For an open translated sector `S_ij(P)` with local native components `(a,b)`, define

`T_{P;a,b}^{(ij)}=(P,[X_i^a X_j^b])`

under the frozen component-preserving commutation law

`X_iX_j ~ X_jX_i`.

The minimal concrete identity therefore contains:

- start vertex `P`;
- translated sector label `(ij)`;
- native component trace class.

The start vertex is required to distinguish parallel translated segments.

Freeze:

`ARBITRARY_POINT_ENTERPRISE_LINE_IDENTITY = TRANSLATED_NATIVE_COMPONENT_TRACE`.

## 5. Translated incidence and path fiber

At every start vertex `P`, translation of the frozen circle-cell incidence gives exactly one sector-local incident anchor cell for each translated open sector.

Define

`Sigma_P^(ij): P -> C_P^(ij)(0,0)`.

For the translated trace define

`Realize_E(T_{P;a,b}^{(ij)})`

`= { Sigma_P^(ij); w : w in Sh_{a,b}(X_i,X_j) }`.

Every prefix is one circle cell, every center move is nearest-neighbor/overlap valid, and every representative terminates at the translated terminal cell incident to `Q`.

Freeze:

`ARBITRARY_POINT_PATH_FIBER_EXACT = true`.

`PATH_FIBER_CARDINALITY_TRANSLATION_INVARIANT = true`.

Cardinality:

`|Realize_E(T_{P;a,b}^{(ij)})|=binom(a+b,a)`.

## 6. Same endpoint versus same line remains distinct

Translated third-family carrier shortcuts may reach the same carrier endpoint.

They do not preserve the native `ij` component trace.

Freeze:

`SAME_CARRIER_ENDPOINT != SAME_NATIVE_LINE_IDENTITY`.

`TRANSLATED_REVERSE_THIRD_SHORTCUT = CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`.

No jump-count rule is used to make this distinction.

## 7. Directed native line gauge

For

`D_E(P->Q)=(A,B,C)`,

define

`ell_E(P->Q)^2=A^2+B^2+C^2`.

Because `min(A,B,C)=0`, at most two components are active, so this is exactly the frozen native Pythagorean law in the selected translated `120°` right sector.

Freeze:

`POINT_TO_POINT_NATIVE_LINE_LENGTH_OBJECT = DIRECTED_NATIVE_LINE_GAUGE`.

The gauge satisfies:

- `ell_E(P->P)=0`;
- positivity for distinct integer vertices;
- translation invariance;
- compatibility with the frozen origin norm;
- axis-glue compatibility;
- triangle inequality.

It is not graph jump count and not carrier Euclidean distance.

## 8. Triangle inequality

Let `D1,D2` be the canonical nonnegative displacement triples for `P->Q` and `Q->R`.

Before canonical decode, their composed component list is `D1+D2`.

Let

`m=min_i(D1_i+D2_i)`.

The canonical triple for `P->R` is

`D12=D1+D2-m(1,1,1)`.

Since `m>=0`, every component of `D12` is no larger than the corresponding component of `D1+D2`.

Hence

`||D12||_2 <= ||D1+D2||_2 <= ||D1||_2+||D2||_2`.

Therefore

`ell_E(P->R) <= ell_E(P->Q)+ell_E(Q->R)`.

Freeze:

`DIRECTED_NATIVE_LINE_GAUGE_TRIANGLE_INEQUALITY = true`.

## 9. Reversal map without negative native axes

Let

`D_E(P->Q)=(A,B,C)`

and

`M=max(A,B,C)`.

Then the reverse directed displacement decodes exactly as

`D_E(Q->P)=(M-A,M-B,M-C)`.

Freeze:

`REVERSAL_TRACE_REDECOMPOSITION_WITHOUT_NATIVE_NEGATIVE_AXES = true`.

This reverse positive-axis trace is generally not the same object as the path-groupoid inverse of the forward trace representative.

## 10. Reversal-length asymmetry

Forward and reverse squared gauges are

`ell_f^2=A^2+B^2+C^2`,

`ell_r^2=(M-A)^2+(M-B)^2+(M-C)^2`.

Their exact difference is

`ell_r^2-ell_f^2=M(3M-2(A+B+C))`.

Thus symmetry occurs exactly on

`2(A+B+C)=3M`.

It fails in general.

Smallest nonzero canonical obstruction:

`D_f=(1,0,0)`, `ell_f^2=1`,

`D_r=(0,1,1)`, `ell_r^2=2`.

The translated `3-4-5` branch also shows the asymmetry:

`(3,4,0)` has squared forward gauge `25`, while its reverse decode `(1,0,4)` has squared gauge `17`.

Freeze:

`REVERSAL_LENGTH_SYMMETRY = false`.

`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC = false`.

Do not call `ell_E` a metric.

## 11. Interpretation boundary

The accepted object is an asymmetric/directed native line gauge attached to an oriented native component trace.

This definition does not decide whether Enterprise geometry should ultimately have:

- only the directed gauge;
- a separate orientation-free segment invariant;
- a symmetric scalar metric derived from additional principles;
- or a future contradiction-driven supersession of one of the current frozen premises.

Freeze open question:

`CANONICAL_UNORIENTED_NATIVE_SEGMENT_INVARIANT = OPEN`.

`SYMMETRIC_NATIVE_POINT_DISTANCE = OPEN_OR_IMPOSSIBLE_UNDER_CURRENT_PREMISES`.
