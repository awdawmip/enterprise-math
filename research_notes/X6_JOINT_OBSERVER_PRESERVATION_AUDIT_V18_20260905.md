# X6 signed spatial model × Joint Relation Observer Preservation audit

Status: `DERIVED / MANDATORY-CONTRACT-AUDITED / ANTI-COLLAPSE SAFE`
Date: `2026-09-05`

## 1. Governing contract

Current P000 V4 makes `ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` mandatory before information-reducing projections.

The contract requires default retention of joint directions, carry, path provenance, multiplicity and interaction coordinates until an exact observer/future-operation descent certificate is proved.

## 2. Population retained at the full spatial layer

The signed X6 candidate begins from the complete six-axis coordinate population

`G6_FULL=Z^6`

with all 12 signed primitive one-axis directions preserved distinctly.

A multi-axis vector is not deleted merely because it is reconstructible from primitive steps: it remains a full spatial endpoint displacement and its ordered path realizations remain available in Path-formal/BRC layers.

Thus

`RECONSTRUCTIBLE_FROM_AXIS_STEPS != REDUNDANT_AS_ENDPOINT_OR_PATH_OBSERVER`.

## 3. Relative quotient requires an explicit repair coordinate

The map

`q:Z^6 -> G6_REL=Z^6/Z*1`

is information reducing. Its exact fibre is the global diagonal coordinate `h in Z`.

The V2 residual/common-depth chart supplies an exact repair coordinate:

`z <-> (can6(z), min(z))`.

Therefore any computation that descends to `G6_REL` but may later need full spatial coordinates must retain `COMMON_DEPTH`.

Freeze audit rule:

`DROP_COMMON_DEPTH -> SAFE ONLY FOR OBSERVERS PROVED INVARIANT UNDER GLOBAL_DIAGONAL_TRANSLATION`.

No such global safety certificate is presumed merely from the existence of min-zero slice coordinates.

## 4. Slice projection requires more retained information

For one selected 3-axis positive-min-zero observer, the fibre is `Z^4`: visible common offset plus three omitted signed coordinates.

Thus using a slice address as a substitute for full spatial state is unsafe unless the intended observer/future operations are proved fibre-constant.

P000 already states `SLICE_OBSERVATION != FULL_CELL_STATE`; the signed X6 model realizes that distinction exactly.

## 5. Endpoint compression versus path/BRC

Even the full signed endpoint `z in Z^6` is a quotient of ordered path history.

For an off-axis displacement with support >=2, exact shortest-path multiplicity is

`||z||_1! / product_i |z_i|! > 1`.

Therefore endpoint coordinates do not determine path order, branch identity or provenance.

Safe hierarchy:

`PATH-FORMAL / WEIGHTED BRC`

`-> SIGNED SIX-AXIS OCCURRENCE/TRACE DATA`

`-> FULL SPATIAL ENDPOINT Z^6`

`-> RELATIVE SIX-AXIS OBSERVER G6_REL + REPAIR COMMON_DEPTH`

`-> SELECTED 3-AXIS MIN-ZERO OBSERVER + EXPLICIT HIDDEN COORDINATES WHEN NEEDED`

`-> COARSER TOTAL/BOOLEAN READOUT`.

Each downward arrow requires the actual observer/future-operation descent certificate if the richer data may be needed later.

## 6. Why the signed full model is safer than the older quotient candidate

The superseded full-spatial proposal `X6=G6_REL` erased the global diagonal because all positive-only 3-axis observations erased it.

That inference violated the current preservation rule:

`LOCAL_OBSERVER_REDUNDANCY != GLOBAL_REDUNDANCY`.

Current P000 V4 signed axes show the erased diagonal is a genuine composite spatial displacement with norm squared 6. So the quotient was not safe at the full spatial observer.

The signed `Z^6` candidate fixes this by retaining the road/background coordinate first and deriving every quotient explicitly.

## 7. BRC first-line resolution

Matched existing methods:

- six-axis V2 residual/common-depth exact carry;
- Path-formal -> N-BRC -> Boolean enrichment bridge;
- Weighted-BRC positive rational provenance/multiplicity discipline.

Reuse resolution:

- `REUSE_APPLIED/EXECUTED`: V2 common-depth split/carry used as exact quotient repair coordinate and section cocycle;
- `COMPOSE_APPLIED`: signed spatial endpoint + BRC ordered path layer;
- no new top-level BRC family is introduced.

Hard boundary checked:

`POSITIVE_WEIGHTED_BRC != SIGNED_OR_PHASE_CANCELLATION` and `ENDPOINT_RECOALESCENCE != PATH_IDENTITY`.

## 8. Admission consequence

Promoting `X6_NATIVE_SPATIAL=AFFINE_TORSOR(Z^6)` is compatible with the mandatory information-preservation contract because it is the **retaining** spatial carrier. The lower min-zero/relative/slice structures remain typed projections with explicit lost-coordinate descriptions and repair data.
