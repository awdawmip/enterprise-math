# R059D Stage AM Report — Canonical BRC circle collapse and source/target non-isometry

Researcher-ID: `EM-R059D-AM-8E3C64`

Task: `RS-R059D-STAGE-AM-CANONICAL-BRC-CIRCLE-COLLAPSE-NONISOMETRY`

## Primary disposition

`CANONICAL_BRC_CIRCLE_COLLAPSE_ESTABLISHED__SOURCE_ARC_METRIC_NONDESCENT_PROVED__DISTINCT_REALIZATIONS`

## Result

Stage AM constructs a canonical comparison/collapse relation between the accepted orthogonal continuous source circle and the already-canonical AL Enterprise fixed-length turn orbit.

The bridge does not choose the target. AL already fixed the target uniquely inside final `ADM_E`.

For each canonical target elementary turn `e_k=(p_k,p_(k+1))`, define the source fiber `F_k` as the closed source-circle angular interval between the rays through the two target endpoints in the accepted source compatibility chart.

This gives a closed-fiber BRC relation with the following exact properties:

- every target turn has a nonempty connected source arc fiber;
- fiber interiors are disjoint;
- neighboring fibers overlap only on their common target-vertex source ray;
- all source-circle states are covered;
- the target turn set is fully hit;
- cyclic order is preserved;
- D6 equivariance holds;
- translation covariance holds;
- the relation is many-to-one at every finite target radius.

The correct comparison carrier is a target elementary turn/edge, not a target vertex. A vertex is a fiber boundary/tie state.

## Exact local non-isometry

For consecutive target rays `p=(a,b)`, `q=(c,d)`, source angular width `Delta` obeys

`tan(Delta)=sqrt(3)*(ad-bc)/(2ac+2bd+ad+bc)`.

The first radius where elementary target turns receive unequal source arc fibers is exactly `r=3`.

The canonical first sector is `222`.

The first two turns give

- `(3,0)->(2,1)`: `tan(Delta_0)=sqrt(3)/5`;
- `(2,1)->(1,2)`: `tan(Delta_1)=3sqrt(3)/13`.

These are unequal. Both target turns are the same primitive target symbol `2` and each has native turn weight one.

Therefore there is no target-local constant source arc unit for one legal turn at `r=3`.

Hence

`SOURCE_EQUIDISTANCE_ARC_METRIC_DOES_NOT_DESCEND_THROUGH_CANONICAL_BRC`.

This conclusion is local and exact. It does not infer non-isometry from a later comparison of circumference constants.

## Circumference semantics

Source circumference is total source Euclidean arc measure.

Target circumference is the minimal legal-turn period

`T_r=C_E(r)=C_N(r)`.

Because the source fibers of elementary target turns are not equal in source arc measure, BRC compatibility does not identify these two functionals.

Thus

`SOURCE_ARC_CIRCUMFERENCE_IS_NOT_A_BRC_INVARIANT`.

The already-proved target theorem remains

`kappa_E^2=12`, `kappa_E>0`,

with `kappa_E=lim T_r/(2r)`.

The source constant is separately typed as `kappa_perp`; standard source mathematics may call it `pi_source`. Stage AM does not identify it with `kappa_E` and proves no new theorem about the algebraicity of the standard real number pi.

## Realization separation

The source circle is continuous. The canonical target circle has finitely many elementary turn states at every finite integer radius. The BRC relation has nontrivial connected source arc fibers and is therefore a quotient/collapse, not a bijective coordinate reparameterization.

Together with local arc-metric nondescend, this proves

`ORTHOGONAL_CONTINUOUS_CIRCLE_AND_ENTERPRISE_NATIVE_CIRCLE_ARE_DISTINCT_REALIZATIONS_CONNECTED_BY_NONISOMETRIC_BRC_COLLAPSE`.

## Structures preserved by BRC

- compatible radius-class label `r`;
- translation covariance;
- D6 action;
- source/target orientation and cyclic order;
- complete source coverage;
- complete target surjectivity.

## Structures not descending as target metric

- source pointwise continuum;
- source arc density per target turn;
- source circumference integral as the native target turn-period functional.

## Deterministic validation

The frozen checker validates:

- every `r=1..256` full canonical target cycle;
- checkpoints `512,1024,4096`;
- exact AG-compatible target period;
- strictly positive source angular cone for every target turn;
- a strict interior source-direction sample for every fiber;
- tie-ray consistency;
- D6 covariance;
- translation covariance;
- simple canonical target cycle;
- D6-repeated fiber tangent signatures;
- `r=1,2` equal-fiber controls;
- exact first nonuniform witness at `r=3`.

Pre-history-gate checker result:

`2580/2580 PASS`

Digest:

`2018fda8340885b7fbb6950c7196d4d9176ac7dc6ef3a27180009cd699df9f18`

Finite replay is implementation evidence only. The fiber cover and non-isometry theorem are symbolic.

## Semantic firewall

Stage AM does not:

- use the source circle to choose or retune the target;
- define target length by source/Euclidean distance;
- assume BRC is isometric because both objects are called circles;
- identify source circumference with target period;
- use standard pi numerics as a target-selection signal;
- collapse `kappa_perp` and `kappa_E` into one symbol;
- consume Stage AN or later work.

`STOP_FOR_DRIVER_REVIEW` after checker/history/manifest/checkpoint freeze.
