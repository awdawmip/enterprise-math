# R054 Problem Packet — Exhaustive K=3 Collapse Optimality and Asymptotic Bias

Status: `FROZEN GENERATION PACKET / CALIBRATION CONTINUATION / NOT CANONICAL`

## 0. Why this is a new generation

R053 is immutable. Its frozen hashes are:

- `R053_LATTICE_TARGET_PROTOCOL_SHA256 = fb8f731160e29d7f11e51c8ffbc70257427d32149e77da462c56d548deed5044`
- `R053_COLLAPSE_LIBRARY_SHA256 = 7c051a3b141b7fa46a4820b026185c602193bb692d2d8d3a02f385999de0d83f`
- `R053_COLLAPSE_POLICY_SHA256 = 27d6feec5f2a6761a16e82e3d542cc18d89641388edfdfeb95f8e94a152f7335`
- `R053_ARTIFACT_MANIFEST_SHA256 = 8289bc68442f2fc1bbc1b736393fb20594855d5b1ec5fdde3555c3a61ac5ecd1`

R053 found a useful local collapse signal but also falsified its own forward-greedy optimizer: the frozen mapping

`MC0001->CHORD3, MC0002->CHORD3, MC0003->CHORD2`

was beaten on construction, validation, strict holdout, and post-freeze tangent validation by the simpler already-declared `CHORD3-all` baseline. Final-context credit also showed positive replacement credit for `MC0003->CHORD3` after the later choices were present.

This fact may not be used to mutate R053 after holdout. R054 starts a fresh generation with new split bytes and a new freeze.

Provenance checkpoint: GLOBAL_KNOWLEDGE commit `b5bea91a289a530c71eaf96b9dd98ae79ad91fe6` and R053 taskbook source `b741d0413bc589b754906e3dee414f9df3615d0d`.

## 1. Mother question

R054 separates two hypotheses that R053 could not separate:

1. **optimizer failure** — forward greedy failed even inside a tiny finite local policy class;
2. **model-class obstruction** — even the globally best bounded-local K=3 chord policy may retain a nonzero scale bias.

The question is:

> After removing optimizer freedom by exhaustive enumeration of a frozen finite K=3 policy class, does the best policy generalize on an entirely fresh split, and can the residual large-scale bias be proved to vanish, proved to persist, or only left open?

Do not enlarge K and do not add new collapse families merely because the K=3 answer is disappointing. Killing the current class cleanly is progress.

## 2. Teacher/student discipline

This remains **calibration**, not a foundational derivation of classical pi.

Teacher side may use Euclidean circles, radii, symbolic/numerical classical `pi`, circumference `2*pi*R`, and tangent labels only after policy freeze.

Student inference after freeze may use only the discrete boundary, the frozen K=3 type classifier, the frozen parser, and the selected local mode mapping. It may not use pi, teacher radius, teacher center, center phase, or tangent labels.

No result in R054 may be advertised as proving that pi is a native primitive or that the triangular lattice is physically fundamental.

## 3. Fixed lattice and fresh teacher-circle generation

Use the same normalized triangular center lattice:

- `e1=(1,0)`;
- `e2=(1/2,sqrt(3)/2)`;
- exact axial norm `Q(a,b)=a^2+a*b+b^2`;
- regular-hexagonal Voronoi cells;
- teacher cluster `C(R,c)=union{H_lambda : Q(lambda-c)<=R^2}` with exact ties included.

Keep `ell_0` symbolic.

### 3.1 Fresh radii — no R053 radius reuse

Freeze these before any policy scoring:

- construction radii: `[66,74,86,102,118,138,154,178]`;
- validation radii: `[70,90,110,134,146,170]`;
- strict-holdout radii: `[78,94,126,142,166,206]`;
- post-holdout extrapolation radii: `[230,254,286,318,350,398,446,510]`.

None of these radii occurs in any R053 construction/validation/holdout/extrapolation set.

### 3.2 Fresh center phases — no R053 phase reuse

Construction phases:

- `C54-0=(1/5,1/10)`;
- `C54-1=(2/5,1/10)`;
- `C54-2=(1/10,2/5)`;
- `C54-3=(3/10,1/5)`.

Validation phases:

- `V54-0=(1/7,3/7)`;
- `V54-1=(2/7,4/7)`;
- `V54-2=(3/7,1/7)`.

Strict-holdout phases:

- `H54-0=(1/11,4/11)`;
- `H54-1=(5/11,2/11)`;
- `H54-2=(3/11,7/11)`.

The strict holdout must not be instantiated/scored until the R054 winner policy bytes and SHA-256 are frozen.

## 4. K=3 fresh type audit before scoring

Canonicalize K=3 consecutive exposed-edge patches under translation + D6, with orientation metadata retained for applying the actual local vector.

R053 observed exactly three classes corresponding to turn pairs:

- `T++`: `[+1,+1]` (R053 MC0001 family);
- `TMIX`: mixed sign `[+1,-1]` or its D6/reversal equivalent (R053 MC0002 family);
- `T--`: `[-1,-1]` (R053 MC0003 family).

Before evaluating any policy score, enumerate the R054 construction split and freeze `R054_K3_TYPE_CATALOG.json`.

If the construction split contains a fourth inequivalent K=3 type, stop the 27-policy claim and return `K3_TYPE_CATALOG_CHANGED / NEW_CLASS_FREEZE_REQUIRED`. Do not silently add a fourth type after seeing policy scores.

Validation/holdout unseen types, if any, use the already-frozen RAW1 fallback and must be reported separately.

## 5. Frozen restricted collapse library

R054 intentionally uses only three exact local modes, fully specified here:

- `RAW1`: consume one exposed edge `(v0,v1)` and output segment `v0->v1`;
- `CHORD2`: when legal, consume two consecutive exposed edges `(v0,v1,v2)` and output exact endpoint chord `v0->v2`;
- `CHORD3`: when legal, consume three consecutive exposed edges `(v0,v1,v2,v3)` and output exact endpoint chord `v0->v3`.

Length is the exact Euclidean length induced by the fixed local algebraic hex-cell coordinates. No learned continuous coefficient is allowed.

Use the same parser contract throughout the generation:

`student-only dihedral-canonical cyclic start/orientation -> deterministic non-overlapping sequential consumption -> seam-ineligible specialized mode falls back to RAW1`.

The parser must cover every raw boundary edge exactly once in its accounting sense and be invariant under cyclic reindexing/reversal/D6 as declared by exact tests.

Freeze library/parser bytes before policy scoring.

## 6. Exhaustive policy class

If and only if the construction catalog is exactly `{T++,TMIX,T--}`, the policy class is the full Cartesian product

`{RAW1,CHORD2,CHORD3}^{3}`,

hence exactly **27 deterministic mappings**.

No forward greedy search, coordinate descent, learned weight, or post-hoc replacement is permitted. Enumerate all 27.

Freeze `R054_POLICY_CLASS.json` and return `R054_POLICY_CLASS_SHA256` before scoring.

For every policy record:

- canonical mapping tuple;
- construction MSE/MAE/bias/max error against classical pi;
- validation MSE/MAE/bias/max error;
- complexity = number of non-RAW entries;
- parse fallback/seam statistics;
- per-radius and per-phase residuals.

Select the unique winner by this pre-frozen lexicographic rule:

1. minimum validation pi-MSE;
2. then minimum construction pi-MSE;
3. then fewer non-RAW entries;
4. then lexicographically smallest canonical mapping tuple.

Repeat the entire 27-policy ranking at 100 and 200 decimal digits. If the selected mapping changes, do not freeze a winner until the precision instability is resolved.

Only after that freeze `R054_OPTIMAL_POLICY.json` and return its SHA-256.

The R053 greedy mapping and `CHORD3-all` are merely named members of the 27-policy class. Their old scores are historical context, not R054 evidence.

## 7. Fresh strict-holdout and tangent validation

After the optimal-policy hash is frozen, instantiate the strict-holdout radius/phase pairs.

Report the winner against every frozen 27-class baseline without refitting. At minimum return holdout MSE, MAE, signed bias, max error, phase spread, unseen-type rate, seam fallback, and ranking position.

Only after policy freeze may classical tangent labels be opened. The tangent vector must come solely from each frozen effective segment. Report tangent misalignment for the R054 winner, RAW1, CHORD2-all, CHORD3-all, and the old R053 greedy mapping when all are defined in the new class.

Do not use tangent performance to retroactively select the R054 policy.

## 8. Asymptotic-bias attack

This is the load-bearing mathematical stage.

For each fixed policy `P` in the 27-class, express the perimeter whenever possible as a finite linear combination of exact radical tile lengths with policy-dependent tile counts plus explicitly bounded seam terms.

Investigate the normalized readout

`pi_P(R,c)=Per_P(C(R,c))/(2R)`.

Distinguish rigorously:

- uniform-in-phase limit;
- phasewise limit;
- phase-averaged limit;
- subsequence limits;
- bounded finite-radius observation.

Attempt to derive exact/asymptotic frequency laws for the K=3 turn classes or equivalent local tiles. Do not infer an all-scale theorem from numerical regression.

For the globally selected R054 policy, and ideally for all 27 policies, return exactly one of:

- `PI_TARGET_LIMIT_PROVED`;
- `NONZERO_ASYMPTOTIC_BIAS_PROVED`;
- `PHASE_OR_SUBSEQUENCE_LIMIT_SPLIT_PROVED`;
- `OPEN_ASYMPTOTIC_WITH_BOUNDED_EVIDENCE`.

The strongest desired negative theorem is:

`K3_CHORD_FAMILY_PI_OBSTRUCTION`:

> every policy in the frozen 27-class has a provably nonzero asymptotic pi bias or a provably nonconvergent phase/subsequence obstruction.

Claim it only if every member is covered by proof, not by finite extrapolation.

If the obstruction is proved, the next Driver generation may consider K=4/K=5 or a larger collapse library. R054 itself must not expand K.

## 9. Mandatory attacks

At minimum record:

- `R053_HOLDOUT_REUSED_AS_R054_SELECTION_DATA`;
- `R053_POSTHOC_CHORD3_PATCH_DISGUISED_AS_SAME_GENERATION`;
- `GREEDY_OPTIMALITY_ASSUMED`;
- `CHORD3_ALL_PRIVILEGED_WITHOUT_EXHAUSTIVE_ENUMERATION`;
- `OLD_RADIUS_OR_PHASE_REUSED`;
- `POLICY_CLASS_CHANGED_AFTER_SCORING`;
- `POLICY_CHANGED_AFTER_HOLDOUT`;
- `PI_USED_AT_STUDENT_INFERENCE`;
- `TANGENT_USED_IN_POLICY_SELECTION`;
- `FINITE_RADIUS_REGRESSION_PRESENTED_AS_ASYMPTOTIC_THEOREM`;
- `PHASE_AVERAGE_CONFUSED_WITH_UNIFORM_PHASE_THEOREM`;
- `ANISOTROPY_AVERAGE_CONFUSED_WITH_ISOTROPY`;
- `K_EXPANSION_BEFORE_K3_CLASS_IS_KILLED`;
- `UNSEEN_TYPE_HIDDEN_BY_FALLBACK`;
- `CYCLIC_START_OR_SEAM_ARTIFACT_DRIVES_WINNER`.

## 10. Success / kill boundary

High-value positive result:

`EXHAUSTIVE_K3_POLICY_RECOVERS_PI_AND_TANGENT_ON_FRESH_HOLDOUT` with honest asymptotic status.

High-value negative result:

`K3_CHORD_FAMILY_PI_OBSTRUCTION`, which would justify expanding locality/model class in a later generation.

Also acceptable:

`OPTIMIZER_DEBT_RESOLVED / BEST_K3_POLICY_IDENTIFIED / ASYMPTOTIC_OPEN`.

Do not invent K=4 work merely to avoid an OPEN result.
