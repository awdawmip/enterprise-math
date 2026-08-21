# R061 Stage 2 — Point-to-Point Native Metric Audit

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Verdict

`POINT_TO_POINT_LENGTH_WELL_DEFINED = true`  
`TRIANGLE_INEQUALITY = true`  
`REVERSAL_SYMMETRY = false`  
`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC = false`

The surviving object is typed as

`DIRECTED_NATIVE_LINE_GAUGE`.

It is not called a metric.

## 1. Directed point-to-point line length

Let

`D(P->Q)=(A,B,C)`, `min(A,B,C)=0`, `A,B,C>=0`

be the unique directed displacement address derived in the component-decomposition theorem.

Define

`ell_E(P->Q)^2 = A^2+B^2+C^2`.

Because one component is zero, this is exactly the frozen sector law `a^2+b^2` in the active translated sector, and exactly `n^2` on a translated positive axis.

## 2. Properties that pass

The construction satisfies exactly:

- `ell_E(P->P)=0`;
- positivity for `P!=Q`;
- translation invariance on the coordinate-vertex lattice;
- compatibility with the frozen origin norm when `P=O_E`;
- compatibility across the two chart presentations of each positive axis;
- no use of carrier Euclidean distance as native length.

## 3. Exact triangle inequality theorem

The triangle inequality does **not** fail.

Let `D1,D2` be the canonical nonnegative min-zero displacement triples for `P->Q` and `Q->R`. In the implementation carrier, composition is represented before redecoding by the componentwise nonnegative triple `D1+D2`.

Let

`m = min_i (D1_i + D2_i) >= 0`.

The canonical decoded displacement for `P->R` is represented by

`D12 = D1 + D2 - m(1,1,1)`

at the I0 decoding layer. This is not a native diagonal-shift equivalence; it is the unique carrier-to-native decoding step already proved.

Every coordinate of `D12` is between `0` and the corresponding coordinate of `D1+D2`, hence

`||D12||_2 <= ||D1+D2||_2`.

The ordinary Euclidean triangle inequality on the **native component scalar list** gives

`||D1+D2||_2 <= ||D1||_2 + ||D2||_2`.

Therefore

`ell_E(P->R) <= ell_E(P->Q) + ell_E(Q->R)`.

This proof does not use the carrier drawing's Euclidean angle or distance as the native metric.

The deterministic checker independently tested all `81^3 = 531,441` ordered triples in the patch `-4<=p,q<=4` using an exact integer radical comparator and found zero triangle-inequality failure.

## 4. Exact symmetry obstruction

Symmetry fails at the smallest possible nonzero native length.

Take

`P=O_E`,

`Q=P+E1`.

Forward displacement:

`D(P->Q)=(1,0,0)`,

`ell_E(P->Q)^2=1`.

The reverse carrier direction is decoded without any native negative axis as

`D(Q->P)=(0,1,1)` in translated `S23(Q)`.

Therefore

`ell_E(Q->P)^2=1^2+1^2=2`.

Thus

`ell_E(P->Q) != ell_E(Q->P)`.

This is the canonical smallest obstruction up to translation and cyclic axis relabeling.

## 5. Consequence

The Stage 2 translation construction yields an exact translation-invariant, positive, triangle-subadditive **directed** line-length function, but not a symmetric point-to-point distance.

Accordingly:

`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC=false`.

The line identity, path fiber and cross-sector gluing results remain valid and are not repaired or discarded to force metricity.
