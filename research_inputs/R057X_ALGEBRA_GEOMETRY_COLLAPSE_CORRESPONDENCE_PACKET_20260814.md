# R057X Problem Packet — Algebra–Geometry Collapse Correspondence

Status: `FROZEN PROBLEM PACKET / CROSS-ARM AFTER INDEPENDENT SERIOUS CHECKPOINTS / NOT CANONICAL`

## 0. Purpose

R057-A and R057-G were intentionally firewalled through their first serious grammar checkpoints. Both checkpoints are now frozen. R057X may therefore compare them without retroactively contaminating their discovery provenance.

R057X asks:

> Which collapse structures discovered independently in the algebraic and geometric arms are genuinely the same mathematical motif, which are representation-specific, and which should be transferred as new Stage-C hypotheses?

R057X is initially a **correspondence and transfer-design task**, not another fitting contest.

## 1. Frozen input checkpoints

### R057-A

Researcher: `EM-R057-6A31F2`

Stage-B head / delivery checkpoint:
`5de5822275834dd9b078c8a82dc308220a5dbb9c`

First serious grammar checkpoint SHA-256:
`bc991398000dd1b18ef53967a15b5f2d07c99afee8bdb17cd0a411c73d5cd6bd`

Other frozen Stage-B hashes:

- `R057_G000_SEARCH_RESULTS_SHA256=b7be23991e5d8345c1b8eb86726cb84f654971f73a0fd792a51438bf8e371934`
- `R057_G000_FRONTIER_SHA256=df23c5c45f9fc1fd129ee1345ec26cb202530e694be401e6ad514da93f210f4b`
- `R057_GRAMMAR_GENEALOGY_SHA256=83b85dbeee26f4289e662f84b3e57182d30f34410f1919dedd572c13bf532f07`
- `R057_OPERATOR_LIBRARY_GENEALOGY_SHA256=376d299de90abc933d0255d94e775e0acc382a6819951e05f4590e617aa41ccc`
- `R057_STAGE_B_EXACT_CHECK_RESULTS_SHA256=d3dbb2b6f5ad43e90172c85f9ba1b4d6779029b140fa48db9fea32bd81176f5b`

Frozen A observations include:

- uniform whole-chord dominates all fixed-k OP000 compositions for k=2..8;
- best simple rule is k=7 whole chord;
- best low-complexity structural rule is whole-chord(7) plus one K7 class exception `[3,4]`;
- independent per-k pattern is effectively `c(k)=1` except one K7 class;
- high-capacity discrete class lookup improves substantially but is not compact.

### R057-G

Researcher: `EM-R057G-93D4A8`

Stage-B head:
`6fa16d1f6393cf82a72be2d878c8f2bce8301c21`

First serious grammar checkpoint SHA-256:
`e7b215e6ff5b51c647d804161327b117a50dfbb213481734895b66de3afd9459`

Other frozen Stage-B hashes:

- `R057G_G0_SEARCH_RESULTS_SHA256=2fb081a449bd91efd33afb5ba26961e245c3f5cd2a9b7133de5a9db8b7f0c44b`
- `R057G_G0_FRONTIER_SHA256=30d4d6d3159ce38006b4153b164a0adb628eae9ed2960abf28039c8b1f73dcb9`
- `R057G_GRAMMAR_GENEALOGY_SHA256=6cd3917e5c1b91163eebe25612fe657774a96db5ab413bb4a3e9fe3fd46fb70b`
- `R057G_STAGE_B_CHECK_RESULTS_SHA256=fba896dcb8eca8b14c71f97b32c21b2e169919284e9cbeedfb2f663c0755e26d`

Frozen G observations include:

- exhaustive simple collapse-count search gives `c(k)=1` / whole packet chord for k=1..6;
- K6 class/turn/context partition exceptions improve only modestly over whole chord;
- direct teacher-center arc is machine-zero because of winding/telescoping and must be classified as a teacher-geometry anchor, not a lattice-only collapse law;
- compact non-telescoping teacher-feature rule: tangent projection;
- compact fitted rule: tangent alignment plus radial signed-deviation coefficient `-1/15`;
- 93-class tangent-scale lookup reaches floating-point-zero T0 error and is explicitly supervised overfit;
- direct `2*pi*r` remains `TARGET_LITERAL_DEGENERATE` and is excluded from structural claims.

## 2. Representation mismatch is part of the problem

Do **not** compare raw errors as though A and G used the same carrier.

R057-A uses its frozen TD000 digitized hex/Voronoi-cell boundary representation.

R057-G uses `TRIANGULAR_FACE_CENTROID_DISK_OUTER_EDGE_CONTOUR_V1` with T0 phases/orientations.

Therefore correspondence must be defined at semantic/operator-role level first:

- raw path ↔ raw path;
- whole packet endpoint chord ↔ whole packet endpoint chord;
- contiguous composition ↔ contiguous geometric chord partition;
- packet class / turn pattern ↔ packet class / turn pattern;
- high-capacity class lookup ↔ high-capacity class lookup;
- teacher-feature operators have no automatic A analogue and must be marked `UNMATCHED_TRANSFER_CANDIDATE` until explicitly constructed.

A numerical score from one arm is not directly comparable to a numerical score from the other unless a later matched bridge corpus is explicitly constructed.

## 3. Initial hypotheses to test, not assume

H1 `WHOLE_CHORD_DOMINANCE_CORRESPONDENCE`:

Both arms independently prefer effective collapse count one / whole packet chord in their simplest lattice-only searches.

H2 `SPARSE_EXCEPTION_CORRESPONDENCE`:

Departures from whole chord may concentrate in a small family of turn/curvature patterns rather than depending arbitrarily on every packet class.

H3 `TEACHER_FEATURE_CORRECTION_TRANSFER`:

G's compact tangent/radial correction may indicate the kind of algebraic correction operator A should add in Stage C, rather than merely increasing K.

H4 `TELESCOPING_ANCHOR_QUARANTINE`:

The direct teacher-center arc identity is useful as a geometry sanity anchor but should not be transferred as a discovery of lattice collapse structure.

H5 `LOOKUP_COMPRESSION_TARGET`:

Both arms' high-capacity lookups should be analyzed for common low-dimensional generators or residual patterns before more arbitrary capacity is added.

All H1-H5 begin as `CROSS_ARM_HYPOTHESIS`, not theorem.

## 4. Stage-0 freeze for R057X

Before detailed cross-arm analysis, freeze and return:

- `R057X_CORRESPONDENCE_PROTOCOL_SHA256`
- `R057X_INPUT_CHECKPOINT_REGISTRY_SHA256`
- `R057X_CROSS_ARM_TRANSFER_META_PROTOCOL_SHA256`

These must freeze:

1. exact A/G input checkpoint hashes;
2. semantic-role matching rules;
3. prohibition on direct cross-carrier raw-score comparison;
4. provenance label `CROSS_ARM_INSPIRED_POST_SERIOUS_CHECKPOINT` for any later A/G modification motivated by X;
5. separation of `OBSERVED_CORRESPONDENCE`, `TRANSFER_HYPOTHESIS`, `EMPIRICAL_PATTERN`, and theorem status;
6. explicit quarantine of teacher-center telescoping and target-literal baselines from lattice-only correspondence claims.

Stop after Stage 0 for Driver review.

## 5. Stage A — frozen-checkpoint correspondence only

After Driver approval, compare the existing frozen checkpoints **without new fitting and without changing either arm**.

Produce:

- operator-role correspondence matrix;
- common-motif ledger;
- exception-pattern comparison;
- teacher-dependency stratification;
- cross-arm transfer candidate list;
- matched/unmatched status for each serious frontier representative.

Priority question:

> Is the independently observed whole-chord dominance a robust common motif despite different discretizations, and what residual structure remains after factoring it out?

## 6. Stage B — matched bridge design

Only after Stage-A correspondence is frozen, design a matched bridge corpus or matched packet probes if needed to compare residual laws numerically across carriers.

Do not retroactively alter either original checkpoint.

## 7. Stage C — transfer authorization

Return explicit proposed changes for R057-A and R057-G. Each proposed change must say:

- source arm and frozen source checkpoint;
- target arm;
- mathematical motif being transferred;
- exact new operator/feature/context suggestion;
- why it is not just copying target labels;
- expected complexity impact;
- provenance label `CROSS_ARM_INSPIRED_POST_SERIOUS_CHECKPOINT`.

Actual Stage-C fitting remains owned by the target A/G researcher and must enter that arm's genealogy.

## 8. Primary success modes

- `CROSS_ARM_WHOLE_CHORD_MOTIF_CONFIRMED`
- `SPARSE_EXCEPTION_STRUCTURE_CORRESPONDENCE_FOUND`
- `GEOMETRIC_CORRECTION_OPERATOR_TRANSFER_CANDIDATE_FOUND`
- `ALGEBRA_GEOMETRY_COLLAPSE_DICTIONARY_FOUND`
- `CROSS_ARM_MOTIF_NOT_ROBUST`
- `CORRESPONDENCE_OPEN`

R057X is not canonical mathematics unless later separately promoted.
