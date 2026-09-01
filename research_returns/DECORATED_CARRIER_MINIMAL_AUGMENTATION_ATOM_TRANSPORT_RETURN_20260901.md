# Decorated Carrier Minimal Augmentation - Frozen Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

- Task-ID: `RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT`
- Publication-ID: `TP2-DCE2A9D900EF145F0E77`
- Researcher-ID: `EM-DCTRMIN-7BC444`
- Claim-ID: `chatgpt-dctrmin-20260901-1045`
- Execution record: `ER-DEB4D6566F79BCBC451B`
- Execution branch: `research/decorated-carrier-minimal-augmentation-atom-transport-em-dctrmin-7bc444`
- Hard target: `MINIMAL_TRANSPORT_AUGMENTATION_HIERARCHY_CLASSIFIED`
- Terminal verdict: `SUCCESS`

## Frozen theorem

The exact augmentation hierarchy over the accepted decorated-carrier reduct is:

1. `L0 -> L1`: after explicitly admitting the opposite-pair `C2` connection primitive, unframed classes are `H^1(X;F2)` as already accepted by the parent result.
2. `L1 -> L2`: use the typed split extension
   `1 -> C3=A3 -> S3 ->sgn C2 -> 1`.
   The marked carrier state canonically selects the `C2` stabilizer split, so no arbitrary global numbering or independent `S3` section is required. For fixed `L1` holonomy `h`, relative `S3` lifts modulo kernel gauge are exactly `H^1(X;C3_h)`, where the nontrivial `C2` element acts on `C3` by inversion.
3. `L2 -> L3`: use
   `1 -> V4 -> S4 -> S3 -> 1`.
   For fixed `L2` holonomy `rho`, relative atom lifts modulo kernel gauge are exactly `H^1(X;V4_rho)`. The four homomorphic sections `S3 -> S4` are conjugate by `V4`; their coordinate differences are twisted coboundaries, hence all four represent the same unframed zero lift class. Section choice is gauge/presentation, not independent structural data.

For the accepted free-rank normal form with `beta=rank(pi_1 X)`:

`d2 = dim_F3 H^1(X;C3_h) = 0` if `beta=0`, `beta` if `h=0`, and `beta-1` if `h!=0`.

For `beta>=1`,

`d3 = dim_F2 H^1(X;V4_rho) = 2*beta - 2 + dim_F2(V4^im(rho))`.

Thus on one loop the `L3` dimensions are exactly `2,1,0` for identity, transposition, and 3-cycle `S3` holonomy respectively.

The naturality boundary is exact: split zero lift classes are canonical after the lower object is fixed, but the frozen lower reduct supplies no preferred nonzero `C3` or `V4` kernel-cohomology class. Any such nonzero choice is exogenous additional structure.

## Evidence

Detailed proof:
`research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/full_research_return_20260901.md`

Machine-readable atlas:
`research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/augmentation_atlas_20260901.json`

Deterministic checker:
`research_checks/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_CHECK_20260901.py`

Observed exact local execution before freeze:

`PASS checks=8384; L1_to_L2=C3_twisted_H1; S3_sign_kernel=3; marked_split=canonical; L2_to_L3=V4_twisted_H1; S4_kernel=4; sections=4_all_V4_gauge; L3_one_loop_dims=id:2,transposition:1,3cycle:0; clean_single_multi_equality=PASS`

The checker covers the required clean backbone, single pinch, multiple pinch, equality strata, `H^1` dimensions 0/1/2+, minimal same-reduct/different-augmentation witnesses, all four `S4` sections, and gauge-quotient counts.

## Boundary and disposition

`MINIMAL_TRANSPORT_AUGMENTATION_HIERARCHY_CLASSIFIED = SATISFIED`.

Recommended Driver freeze strength:

`L0_TO_L1_EXOGENOUS_C2_H1 + L1_TO_L2_SIGN_KERNEL_C3_TWISTED_H1_WITH_D2_BETA_OR_BETA_MINUS_1 + L2_TO_L3_V4_TWISTED_H1_WITH_D3_2BETA_MINUS_2_PLUS_FIXED_DIM + ALL_S4_SECTIONS_GAUGE_EQUIVALENT + ZERO_SPLIT_LIFTS_CANONICAL_BUT_NO_NONZERO_CLASS_FORCED`.

No Working Truth, Foundation authority, canonical theorem promotion, factorization semantics, or historical novelty is claimed.

Recommended next action: `DRIVER_REVIEW`. If accepted, close `OBJ-DECORATED-CARRIER-TRANSPORT-AUGMENTATION-MINIMALITY`; do not publish a successor merely to choose an `S3/S4` section or atom frame, since those choices have been classified as gauge/presentation.
