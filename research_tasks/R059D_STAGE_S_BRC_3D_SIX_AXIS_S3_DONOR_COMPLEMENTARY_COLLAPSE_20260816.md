# R059D Stage S — 3D Six-Axis / S3 Donor-Symmetry / Complementary Collapse

Task-ID: `RS-R059D-STAGE-S-BRC-3D-SIX-AXIS-S3-DONOR-COLLAPSE`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-s-brc-3d-six-axis-s3-donor-collapse`
Frozen parent: `83d318944534b2e5e38479d959eb4c1746fc7e8b`

## 0. Immutable ancestry and allowed sources

Stage R frozen owner head:

`83d318944534b2e5e38479d959eb4c1746fc7e8b`

Stage R taskbook source:

`628b2979d3e772e59ee8a92c1f367f8b12bb6667`

Stage J/K/L/M/N/O/P/Q/R artifacts remain immutable.

Read and obey project-level files:

- `PROJECT_DEFINITION.md`
- `PROJECT_DEFINITION.zh-CN.md`
- `project_definition.json`
- `FOUNDATIONAL_LOGIC.md`
- `foundational_logic.json`
- `native_semantics_admissibility.json`
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`

Also consume the frozen 3D notation convention from main:

- `THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md`
- `three_dimensional_relational_axis_convention.json`

Convention commits:

- human-readable: `753db6aad3dca730b76bafdc6d48abdb8103d431`
- machine-readable: `6fb5a8124b5991143c67bffcb68a4b168b34ccb0`

These convention files provide names/orientation notation only; they are not allowed to smuggle in a metric, angle, Euclidean length, or selector preference.

## 1. Scientific question

Test whether the BRC pure-algebra/completion-neighbor/context framework established in 2D generalizes nontrivially to the frozen 3D six-axis carrier.

Do **not** assume that the 2D two-branch `Z2` structure remains the correct symmetry object in 3D.

The central issue is:

> for one elementary recipient event in 3D, do three symmetric donor branches emerge exactly, what is their symmetry type, and what minimal context/post-credit is required to continue or initialize one branch?

## 2. 3D relational carrier

Freeze four relation-coordinate carriers:

`X1,X2,X3,X4`

with affine sheet:

`X1+X2+X3+X4=K`.

Displacement module:

`Lambda3={(d1,d2,d3,d4) in Z^4 : d1+d2+d3+d4=0}`.

Prove rank over `Z` is 3.

The six **unoriented transfer axes** and positive orientation convention are:

- `U`: `+u=e1-e2=(1,-1,0,0)`; donor `X2 -> X1`
- `V`: `+v=e2-e3=(0,1,-1,0)`; donor `X3 -> X2`
- `W`: `+w=e3-e1=(-1,0,1,0)`; donor `X1 -> X3`
- `P`: `+p=e1-e4=(1,0,0,-1)`; donor `X4 -> X1`
- `Q`: `+q=e2-e4=(0,1,0,-1)`; donor `X4 -> X2`
- `R`: `+r=e3-e4=(0,0,1,-1)`; donor `X4 -> X3`

Negative orientation is additive inverse.

Freeze only after checking:

`D12={+/-u,+/-v,+/-w,+/-p,+/-q,+/-r}`

has cardinality 12 and lies in `Lambda3`.

Recheck exact relations:

`u+v+w=0`

`u=p-q`

`v=q-r`

`w=r-p`.

Axis names are convention; BRC must not prefer positive labels.

## 3. Symmetric pre-collapse derivation

Take the mandatory elementary control:

`Delta X1 = +1`.

Before completed collapse, impose only the explicitly declared transverse permutation symmetry among `X2,X3,X4`:

`Delta X2*=Delta X3*=Delta X4*=a`.

Together with affine conservation derive or refute:

`1+3a=0`

hence

`a=-1/3`.

Freeze status carefully:

`-1/3` is an unresolved symmetric pre-collapse algebra/precision carrier state, not a packet weight and not geometric projection.

Do not use tetrahedral Euclidean angles to derive `-1/3`.

## 4. Completion-neighbor collapse and exact three-branch emergence

Use the inherited completed displacement coordinate layer:

`C=Z`.

For `q=-1/3`, verify:

`PREV_Z(q)=-1`

`NEXT_Z(q)=0`.

For the three transverse coordinates write Boolean completion bits:

`Delta Xj=-1+b_j`, `b_j in {0,1}`.

Substitute into conservation and derive or refute:

`b_2+b_3+b_4=2`.

The exact Boolean solution set should be audited, not assumed.

If the derivation is correct, prove there are exactly three completed branches:

- donor `X2`: `(1,-1,0,0)`
- donor `X3`: `(1,0,-1,0)`
- donor `X4`: `(1,0,0,-1)`.

Then permute recipient labels and prove or refute that the union is exactly:

`{e_i-e_j : i!=j}`

with 12 directed states and 6 unoriented axes, matching the frozen `U,V,W,P,Q,R` convention.

No separate nearest/minimal-distance rule is allowed.

## 5. Branch-fiber symmetry: S3 audit

For fixed recipient `X1`, define the donor branch set:

`B1={X2,X3,X4}`.

The transverse permutation group `S3` acts on this branch set.

Audit exactly:

- transitivity;
- stabilizer of one donor branch;
- whether the action is free;
- whether the branch fiber is a torsor for any canonically declared group.

**Do not call the three-state branch fiber a `Z3 torsor` or `S3 torsor` unless free+transitive action is actually proved.**

Preferred mature language if appropriate:

`TRANSITIVE_S3_HOMOGENEOUS_BRANCH_SET`

rather than torsor.

Prove or refute the 3D symmetry no-go:

At a fully transverse-`S3`-symmetric local input, no deterministic stateless `S3`-equivariant selector can choose one donor branch if the branch set has no global `S3` fixed point.

Audit loopholes:

- hidden donor ordering;
- coordinate-name bias;
- random selection;
- set-valued `{all three donors}` output;
- external/history context.

Random symmetry is not physical probability.

## 6. Straightness post-credit and donor memory

Use the already frozen project definition:

`STRAIGHT = affine rank-one / rank-one integer displacement structure`.

For fixed recipient `X1`, the three primitive transfer vectors are:

`t_2=e1-e2`

`t_3=e1-e3`

`t_4=e1-e4`.

Prove their exact `Z`-linear relations and ranks.

Test the theorem:

A nonempty repeated fixed-recipient transfer sequence has rank-one displacement span iff the same donor branch is used at every step.

If true, freeze only the continuation law:

`donor_(k+1)=donor_k`.

Do **not** let straightness initialize the first donor.

Determine minimum continuation context cardinality needed to preserve full donor identity.

Audit:

- one Boolean bit context;
- two-bit encodings;
- direct three-state donor relation;
- coordinate-free previous donor/recipient relation.

Prefer relational context over arbitrary binary coding unless coding equivalence is explicitly typed.

## 7. Contextual initialization and exact post-credit

Generalize the Stage P/R singleton criterion.

Let exact local/upstream constraints reduce the donor feasible set to:

`A(s,h) subseteq B_i`, where `|B_i|=3` for a fixed recipient.

Classify:

- `A=empty`: inconsistent;
- `|A|=1`: unique donor exactly forced;
- `|A|=2`: partial ambiguity;
- `|A|=3`: full symmetric multibranch.

A legitimate initial donor must come from an independently typed exact context/certificate that makes the **full** feasible set singleton before using the realized branch itself.

Audit possible context classes:

- preexisting donor relation;
- upstream exact coupled relation;
- previous transfer relation (continuation only unless genuinely preexisting);
- oriented algebraic relation;
- ingress/orientation state only if an exact authorized `S3` transformation law is supplied;
- branch-conditioned residue/readout (reject if circular);
- hidden coordinate order (reject).

Prove or refute:

`S3_INVARIANT_POST_CREDIT_CANNOT_INITIALIZE_UNIQUE_DONOR_AT_FULLY_SYMMETRIC_STATE`.

Use exact feasible sets and symbolic symmetry, not scores.

## 8. 2D reduction control

Show explicitly how the 3D construction reduces in the two-dimensional three-carrier case:

- three carriers;
- one recipient plus two transverse carriers;
- symmetric pre-collapse value `-1/2`;
- Boolean constraint `b_1+b_2=1`;
- two donor branches;
- `Z2` exchange structure;
- straight continuation one-bit memory.

This is a consistency check, not permission to assume the 3D result.

## 9. Optional d-dimensional theorem gate

Only after all 3D gates pass, test the algebraic pattern for dimension `d`:

- `d+1` relation-coordinate carriers;
- affine sum constraint;
- one unit recipient event;
- `d` symmetric transverse pre-collapse coordinates `-1/d`;
- completion layer `Z` with neighbors `-1,0`;
- exactly one donor supplying `-1`;
- `d` donor branches per recipient;
- `(d+1)d` directed transfers `e_i-e_j`;
- `d(d+1)/2` unoriented transfer axes.

Do not claim a universal physical dimensional law merely from this algebraic generalization.

## 10. Stage R scalar midpoint boundary

Stage R result is read-only context:

`5 -> 4` is conditionally forced only under explicit midpoint-core axioms `A0+A3+A4+A5`.

Do not reuse scalar order-monotonicity to select a 3D donor branch. Donor branches at the fully symmetric `-1/3` state are permutation-related, not linearly ordered lower/upper endpoints of one scalar gap.

## 11. Large-background/covariance gate

Test exact backgrounds near `10^36` and scales where useful by closed-form integer/rational identities only.

Required covariance audits:

- permutation of four relation-coordinate carriers;
- global inversion of displacement relations;
- additive background `K`;
- positive integer scaling of completion layer/event if explicitly declared.

Do not interpret `K` or scale as length, norm, probability, energy, or selector strength.

## 12. Required artifacts

At minimum produce:

1. `R059D_STAGE_S_3D_RELATIONAL_CARRIER_PROTOCOL.json`
2. `R059D_STAGE_S_SIX_AXIS_D12_REDERIVATION.json`
3. `R059D_STAGE_S_SYMMETRIC_MINUS_ONE_THIRD_DERIVATION.json`
4. `R059D_STAGE_S_THREE_DONOR_COMPLEMENTARY_COLLAPSE.json`
5. `R059D_STAGE_S_S3_BRANCH_SYMMETRY_AUDIT.json`
6. `R059D_STAGE_S_STATELESS_S3_SELECTOR_NOGO.json`
7. `R059D_STAGE_S_STRAIGHT_DONOR_MEMORY_CREDIT.json`
8. `R059D_STAGE_S_CONTEXTUAL_DONOR_SINGLETON_PROTOCOL.json`
9. `R059D_STAGE_S_2D_REDUCTION_CONTROL.json`
10. `R059D_STAGE_S_DIMENSIONAL_GENERALIZATION_LEDGER.json`
11. `R059D_STAGE_S_COVARIANCE_LARGE_BACKGROUND.json`
12. `R059D_STAGE_S_TRIVIALITY_LEAKAGE_LEDGER.json`
13. deterministic checker source/output
14. report
15. artifact manifest
16. frozen checkpoint

## 13. Interpretation firewalls

Do not establish or imply without separate proof:

- physical probability from donor multiplicity;
- Euclidean tetrahedral angle as a native premise;
- physical direction preference from axis naming;
- `S3`-symmetric random choice as native probability;
- a universal absolute donor selector;
- physical dimensionality from the algebraic `d`-generalization alone.

Keep project mode:

`REFOUND, NOT REJECT`.

## 14. Stop condition

After all artifacts/checker/manifest/checkpoint are frozen:

`STOP_FOR_DRIVER_REVIEW`.
