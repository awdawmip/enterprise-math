# FQ010 — Two-Interface Freeze

Researcher-ID: `EM-FQ010-CA2555`

Task: `RS-FQ010-LINE-SCALE-SEMANTIC-ADMISSION-COMPARATIVE-REFOUNDATION`

## Provenance boundary

This comparison begins strictly after the accepted R065 Phase-A blind freeze. The following facts keep their original provenance typing:

- R065 cleanly reconstructed the typed-token presentation groupoid and the component-type relation.
- R065 proved scalar underdetermination from the blind primitive substrate.
- `Q_K=|R_type|` is a Driver post-freeze deterministic consequence inside the frozen definability envelope; it was not blindly selected as a preferred scalar.
- No R065 Phase-A result assigned magnitude, norm, length, or squared-scale semantics.

Sources used exactly as declared by the FQ010 taskbook:

- `research_results/R065_PHASEA/R065_PHASEA_BLIND_CANDIDATE_OR_NO_GO_FREEZE.json@fa9a6a7932afc898a0b834b7d3b0033526ec226f`
- `research_results/R065_PHASEA/R065_PHASEA_DEFINABILITY_SPACE.md@fa9a6a7932afc898a0b834b7d3b0033526ec226f`
- `driver_reviews/R065_PHASEA_PRIMITIVE_INTRINSIC_FINITE_READOUT_DRIVER_REVIEW_20260822.md@18f429470bcb5b7df41c46dad2c5a29964629a09`

## Interface K — relation/readout formulation

Let `U` be the finite unit-token carrier and let

`tau: U -> C`

be the already-supplied component-type observation, where `|C|=3` and admissible contents have support at most two.

Define the relation

`R_type = {(x,y) in U x U : tau(x)=tau(y)}`.

This is exactly `ker(tau)` at relation strength. It is definable from the supplied typing, independent of token names, and equivariant under component relabeling.

Only after the relation is fixed define the numerical readout

`Q_K := |R_type|`.

If the component multiplicities are `(n_c)`, then the relation is the disjoint union of complete ordered-pair blocks

`tau^{-1}(c) x tau^{-1}(c)`,

hence

`Q_K = sum_c n_c^2`.

This formula is derived from the relation; it is not a premise used to select the relation.

**Frozen typing:**

- component typing: declared primitive substrate;
- `R_type`: `N0_DEFINABLE_DERIVED` relation;
- `Q_K`: `N2_READOUT_COLLAPSE` after choosing finite cardinality of the relation carrier;
- identification of `Q_K` with squared native line scale: not yet granted by this freeze.

## Interface F — FQ008 scalar-first formulation

The exact comparison source is:

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@b6ec6eb58f1c724657db7c5bd7deb82827774439`.

On one two-channel sector, FQ008 uses a scalar field `Q` with:

1. axis square calibration
   - `Q(n,0)=n^2`,
   - `Q(0,n)=n^2`;
2. local transverse scalar independence
   - `Q(a+1,b+1)-Q(a+1,b)-Q(a,b+1)+Q(a,b)=0`.

The resulting sector sum-of-squares law is derived, not independently assumed:

`Q(a,b)=a^2+b^2`.

### Source status versus theorem status

These must not be conflated.

- **Referenced source status:** the exact FQ008 refoundation is present at commit `b6ec6eb...` as the supplied integration-candidate definition.
- **Current FQ010 owner-base status:** the same definition path on `research/fq010-line-scale-semantic-admission` still contains the earlier `9866e523...` formulation in which the sector sum-of-squares/Pythagorean law is primitive. Therefore the FQ008 source is not silently treated as the current owner-base Foundation definition.
- **Theorem status:** independently of repository integration status, the two FQ008 scalar conditions imply the sector sum-of-squares field exactly on the declared nonnegative integer sector. FQ010 proves the converse scalar equivalence to `Q_K` separately.

## Frozen comparison surface

| Dimension | Interface K | Interface F |
|---|---|---|
| Starting object | typed token content | sector scalar field `Q` |
| Structural relation | `R_type=ker(tau)` derived | not required |
| Numerical step | choose `|R_type|` | impose scalar conditions |
| Axis square | derived from cardinality | primitive scalar condition |
| Transverse independence | derived from block disjointness/cardinality | primitive scalar condition |
| Sum of squares | derived | derived |
| Relation information retained | yes before scalarization | no, scalar only |
| Scale role | separate N2 semantic assignment | separate scalar semantic assignment |

## Freeze conclusion

The two interfaces are frozen for FQ010 comparison without mutating any Foundation definition. Numerical equality is not taken as semantic equivalence, and `Q_K` is not called squared line scale until the admission classification explicitly addresses that role.
