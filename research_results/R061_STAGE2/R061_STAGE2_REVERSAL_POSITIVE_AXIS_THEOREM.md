# R061 Stage 2 — Reversal with Positive Axes Theorem and Obstruction

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Verdict

`REVERSAL_TRACE_REDECOMPOSITION_WITHOUT_NATIVE_NEGATIVE_AXES = true`  
`REVERSAL_LENGTH_SYMMETRY = false`  
`GROUPoid_INVERSE_IS_TARGET_POSITIVE_TRACE_FIBER = false` for every nonzero line in general.

## 1. Exact positive-axis reversal map on displacement addresses

Let

`D(P->Q)=(A,B,C)`

be the canonical nonnegative min-zero displacement triple, and let

`M=max(A,B,C)`.

Then the canonical positive-axis decoding of the reverse displacement is

`D(Q->P)=(M-A, M-B, M-C)`.

Proof: if the implementation carrier coefficients of `D` are `(A-C,B-C)`, negating them and applying the unique min-zero decoding gives exactly the complement triple above.

The result again has nonnegative components and minimum zero. Therefore reversal never needs a native negative axis.

## 2. Sector-label transformation

The reverse sector is determined by which component(s) of the forward triple attain `M`.

For an interior `S12` trace with forward triple `(a,b,0)`:

- if `a>b`, reverse triple is `(0,a-b,a)`, hence reverse sector `S23` with local components `(a-b,a)`;
- if `b>a`, reverse triple is `(b-a,0,b)`, hence reverse sector `S31` with local components `(b,b-a)` in `(E3,E1)` order;
- if `a=b`, reverse triple is `(0,0,a)`, hence the positive `E3` axis.

Cyclic relabeling gives the other sectors.

## 3. Path-groupoid inverse is not the reversed positive trace

A Stage 1 path representative may always be traversed backward by inverse carrier transition morphisms. That remains a valid path-groupoid inverse.

However, the reverse groupoid word uses inverse morphisms of the original axis families. The Stage 2 positive-axis line from `Q` back to `P` is instead defined by the newly decoded positive-sector trace.

The frozen rule

`CARRIER_DIRECTION_RELATION != NATIVE_VECTOR_RELATION`

forbids rewriting the inverse carrier word into that positive trace merely because the endpoints coincide.

Thus the two are distinct objects in general:

- inverse carrier endpoint path;
- canonical positive-axis native line trace from `Q` to `P`.

## 4. Exact length transformation and symmetry locus

Forward squared length:

`L_f^2=A^2+B^2+C^2`.

Reverse squared length:

`L_r^2=(M-A)^2+(M-B)^2+(M-C)^2`.

Their difference is

`L_r^2-L_f^2 = M(3M-2(A+B+C))`.

For a nonzero canonical displacement, symmetry holds iff

`2(A+B+C)=3M`.

Because exactly one component is zero in an open sector, this means the larger active component is exactly twice the smaller active component. Symmetry is therefore exceptional, not general.

## 5. Smallest exact obstruction

Canonical representative up to translation and cyclic axis relabeling:

`P=(0,0,0)`, `Q=(1,0,0)`.

Forward:

`E1` axis, `L_f^2=1`.

Reverse:

`S23` components `(1,1)`, `L_r^2=2`.

No smaller nonzero forward native squared length exists.

## 6. 3-4-5 reversal example

For a translated forward `S12` trace `(3,4)`:

`D_f=(3,4,0)`, `L_f^2=25`.

Its reverse is

`D_r=(1,0,4)`, i.e. translated `S31` local components `(4,1)`,

so

`L_r^2=17`.

Therefore the frozen `3-4-5` native line law cannot simultaneously become a symmetric arbitrary-point distance under the required three-positive-axis translation semantics.
