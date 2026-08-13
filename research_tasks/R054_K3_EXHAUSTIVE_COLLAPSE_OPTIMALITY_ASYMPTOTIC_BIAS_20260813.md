<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R054-K3-EXHAUSTIVE-COLLAPSE-OPTIMALITY-ASYMPTOTIC-BIAS",
  "title": "R054 — Exhaustive K=3 Collapse Optimality and Asymptotic Bias Obstruction",
  "kind": "CALIBRATED_MATHEMATICAL_RESEARCH",
  "owner": "program/pi-supervised-crystal-boundary",
  "base_state": "NEW_GENERATION_AFTER_R053_OPTIMIZER_FAILURE",
  "priority": "P0",
  "leverage": "GLOBAL_POLICY_OPTIMALITY / LOCALITY_OBSTRUCTION / ASYMPTOTIC_PI_BIAS",
  "frontier": "Remove R053's optimizer freedom by exhaustive enumeration of a frozen 27-policy K=3 chord family on a completely fresh radius/phase split, then determine whether the globally selected bounded-local rule approaches the classical circumference target or whether the entire frozen family has a provable asymptotic bias/phase obstruction.",
  "next_action": "Serialize and hash the already-frozen R054 split and parser/library contract before any policy score; audit the fresh construction K=3 type catalog; if it remains exactly three classes, freeze and exhaust all 27 mappings, select by the predeclared validation rule, hash the winner before strict holdout, then attack its and the full class's asymptotics without enlarging K.",
  "dependencies": [
    {
      "target": "research_inputs/R054_K3_EXHAUSTIVE_COLLAPSE_OPTIMALITY_PACKET_20260813.md @ 157e23b4d8a00dff4ad4f356a7f7b173b4187aee",
      "action": "CONSUME_AS_FROZEN_GENERATION_PACKET",
      "satisfied": true
    },
    {
      "target": "R053 immutable checkpoint / GLOBAL_KNOWLEDGE b5bea91a289a530c71eaf96b9dd98ae79ad91fe6",
      "action": "CONSUME_ONLY_AS_FROZEN_PREVIOUS_GENERATION_AND_NEGATIVE_OPTIMIZER_EVIDENCE",
      "satisfied": true
    }
  ],
  "evidence_status": "EXHAUSTIVE_FINITE_POLICY_CLASS_AND_ASYMPTOTIC_OBSTRUCTION_RESEARCH",
  "hard_block": null,
  "tags": [
    "R054",
    "triangular-lattice",
    "K3",
    "exhaustive-policy",
    "circumference",
    "pi-supervision",
    "tangent",
    "asymptotic-bias",
    "locality-obstruction"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R054",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": [
      {
        "conflict_id": "FL-04-NO-OUTPUT-COPYING-INTO-INPUT",
        "scope": "R054 teacher-side pi scoring and post-freeze target comparison only",
        "reason": "R054 is explicitly a calibration/inverse-reconstruction generation testing a frozen local policy class, not a foundational derivation of classical pi.",
        "replacement_behavior": "Classical pi may be used only as the teacher target during construction/validation scoring and post-freeze evaluation; student inference may not read pi, teacher radius, teacher center, center phase, or classical tangent; no supervised result may be promoted to a foundational native-pi derivation.",
        "expires_when": "R054 generation returns"
      }
    ]
  }
}
-->

# R054 — Exhaustive K=3 Collapse Optimality and Asymptotic Bias Obstruction

Status: `READY / P0 / FRESH GENERATION / R053 IMMUTABLE / NOT CANONICAL`

## 0. Driver intent

R053 established that local collapse contains useful signal, but it did **not** establish that its learned rule was optimal. Its forward-greedy learner was directly falsified by a simpler already-declared `CHORD3-all` rule.

Do not patch R053. Do not reinterpret its strict holdout as training data. Do not jump to a larger local neighborhood merely because the greedy learner failed.

R054 asks a sharper question:

> If optimizer freedom is removed completely inside a small frozen K=3 chord family, what is the actual globally selected policy on fresh data, and is any remaining large-scale pi bias an optimizer artifact or a genuine obstruction of this bounded-local model class?

This task is successful if it cleanly identifies the finite-class optimum and either proves a scale theorem/no-go or leaves the asymptotic question honestly OPEN.

---

## 1. Frozen generation packet

Consume exactly:

`research_inputs/R054_K3_EXHAUSTIVE_COLLAPSE_OPTIMALITY_PACKET_20260813.md`

Source:

`157e23b4d8a00dff4ad4f356a7f7b173b4187aee`

The packet controls:

- fresh construction/validation/strict-holdout/extrapolation radii;
- fresh center phases;
- K=3 construction type audit;
- exact RAW1/CHORD2/CHORD3 definitions;
- parser contract;
- 27-policy class;
- 100/200-digit ranking replication;
- selection tie-break;
- asymptotic result classes;
- mandatory attacks.

Do not replace its split with a more convenient one after inspecting any candidate score.

---

## 2. R053 is frozen evidence, not mutable training state

Frozen prior anchors:

- protocol SHA-256 `fb8f731160e29d7f11e51c8ffbc70257427d32149e77da462c56d548deed5044`;
- library SHA-256 `7c051a3b141b7fa46a4820b026185c602193bb692d2d8d3a02f385999de0d83f`;
- policy SHA-256 `27d6feec5f2a6761a16e82e3d542cc18d89641388edfdfeb95f8e94a152f7335`;
- artifact-manifest SHA-256 `8289bc68442f2fc1bbc1b736393fb20594855d5b1ec5fdde3555c3a61ac5ecd1`.

The R053 facts that motivate R054 are only:

1. the construction K=3 corpus reduced to three D6 classes;
2. the frozen greedy mapping was `(CHORD3, CHORD3, CHORD2)` on those three classes;
3. `CHORD3-all` beat it on R053 construction, validation, strict holdout, and tangent validation;
4. the frozen greedy policy retained a positive scale bias through the tested post-freeze range;
5. R053 did not prove convergence or a locality obstruction.

Do not reuse any R053 radius/phase pair as R054 selection evidence.

---

## 3. Stage 0 — freeze R054 split and scoring bytes

Before enumerating or scoring policy mappings, serialize:

`R054_SPLIT_SCORING_PROTOCOL.json`

It must exactly reproduce the packet's radii and phases and state:

- construction = 8 radii × 4 phases;
- validation = 6 radii × 3 phases;
- strict holdout = 6 radii × 3 phases;
- holdout opens only after winner policy bytes/hash freeze;
- primary selection metric = validation mean squared error of `Per/(2R)` against classical pi;
- secondary = construction mean squared error;
- tertiary = fewer non-RAW entries;
- final deterministic tie-break = canonical mapping tuple;
- target precision = 100 decimal digits, full decisive rerank = 200 digits;
- tangent labels unavailable for policy selection;
- no R053 pair may appear in R054 selection splits.

Freeze and return:

`R054_SPLIT_SCORING_PROTOCOL_SHA256`.

No policy score is admissible before this hash.

---

## 4. Stage A — fresh K=3 catalog audit

Build every construction crystal boundary exactly from the frozen teacher-cluster rule and enumerate K=3 local types under translation + D6.

Freeze:

`R054_K3_TYPE_CATALOG.json`.

Compare it to the packet's three expected turn classes:

- `T++`;
- `TMIX`;
- `T--`.

If the construction catalog is not exactly these three classes, stop the 27-policy theorem path and return:

`K3_TYPE_CATALOG_CHANGED / NEW_CLASS_FREEZE_REQUIRED`.

Do not add a newly observed type after seeing policy scores.

If the construction catalog is exactly three, continue.

Validation or strict-holdout unseen types use only the frozen RAW1 fallback and must be counted explicitly.

---

## 5. Stage B — freeze exact library/parser and the complete 27-policy class

Implement only the packet's three exact modes:

- RAW1 = one raw edge;
- CHORD2 = endpoint chord of two consecutive raw edges when parser-legal;
- CHORD3 = endpoint chord of three consecutive raw edges when parser-legal.

No learned real coefficient, radius correction, phase correction, or pi-containing local output is permitted.

Freeze:

- `R054_K3_CHORD_LIBRARY.json`;
- `R054_PARSER_CONTRACT.json`;
- `R054_POLICY_CLASS.json`.

The policy class must contain **all and only 27** mappings in `{RAW1,CHORD2,CHORD3}^3` over the three frozen type IDs.

Return:

- `R054_K3_CHORD_LIBRARY_SHA256`;
- `R054_PARSER_CONTRACT_SHA256`;
- `R054_POLICY_CLASS_SHA256`.

The exhaustive class hash must precede any ranking.

---

## 6. Stage C — exhaustive construction/validation ranking

Evaluate all 27 mappings. No greedy search is allowed.

Create:

`R054_EXHAUSTIVE_27_POLICY_ATLAS.json`.

Every row must contain at least:

- policy ID and canonical mapping;
- construction MSE/MAE/signed bias/max error;
- validation MSE/MAE/signed bias/max error;
- per-radius and per-phase summaries;
- number of non-RAW entries;
- exact-cover status;
- seam-fallback count;
- unseen-type fallback count;
- 100-digit rank;
- 200-digit rank.

Select exactly by the frozen lexicographic rule. Do not privilege `CHORD3-all` or the old R053 mapping merely because their prior results are known.

Freeze:

`R054_OPTIMAL_POLICY.json`

and return:

`R054_OPTIMAL_POLICY_SHA256`.

The selected mapping must be identical under the 100-digit and 200-digit reruns. If not, return ranking instability rather than choosing by hand.

Also return explicit dispositions:

- rank of `CHORD3-all`;
- rank of the old R053 greedy mapping;
- whether R053's failure was purely optimizer debt inside this restricted class.

---

## 7. Stage D — strict fresh holdout

Only now instantiate the frozen strict-holdout pairs.

Apply all 27 frozen policies without refitting so the selected winner's rank on fresh holdout can be audited without changing selection.

Create:

`R054_FRESH_HOLDOUT_RESULTS.json`.

Report for every policy and especially the selected winner:

- holdout MSE/MAE/bias/max error;
- per-radius/per-phase residuals;
- unseen-type and seam-fallback usage;
- holdout rank;
- validation-to-holdout rank movement;
- whether the selected winner still dominates RAW1 and the old greedy mapping;
- whether a non-selected policy wins holdout, without retroactively replacing the frozen selected winner.

Any holdout winner different from the selected validation winner is evidence about selection instability, not permission to patch.

---

## 8. Stage E — tangent validation remains post-freeze

Classical tangent labels open only after `R054_OPTIMAL_POLICY_SHA256` exists.

Infer tangent direction only from the frozen effective segment vectors.

Create:

`R054_TANGENT_RECOVERY_ATLAS.json`.

Compare at least:

- RAW1;
- CHORD2-all;
- CHORD3-all;
- old R053 greedy mapping;
- R054 selected winner.

Report mean, median, tail/worst misalignment by radius, phase and type. Test whether lower circumference residual correlates with lower tangent error, but do not use tangent to alter policy selection.

---

## 9. Stage F — asymptotic theorem / obstruction attack

This stage matters more than extending the numerical radius range.

For each fixed policy, seek an exact or asymptotic decomposition of perimeter into finitely many radical tile lengths times local-tile counts plus bounded/separately controlled seam terms.

Analyze the frequencies of the K=3 turn classes/parsed tiles as `R` grows. Keep distinct:

- fixed phase;
- uniform-in-phase;
- phase average;
- subsequences;
- finite observations.

For the R054 selected winner, and where possible all 27 policies, classify:

`PI_TARGET_LIMIT_PROVED`

or

`NONZERO_ASYMPTOTIC_BIAS_PROVED`

or

`PHASE_OR_SUBSEQUENCE_LIMIT_SPLIT_PROVED`

or

`OPEN_ASYMPTOTIC_WITH_BOUNDED_EVIDENCE`.

Freeze the theorem/counterexample/open ledger in:

`R054_ASYMPTOTIC_BIAS_LEDGER.json`.

### Strong negative target

Claim

`K3_CHORD_FAMILY_PI_OBSTRUCTION`

only if **every one of the 27 frozen policies** is covered by proof of nonzero asymptotic bias or a phase/subsequence nonconvergence obstruction.

Finite regression, even to very large R, is not such a proof.

### Strong positive target

If a policy is proved to converge to the classical target, state its exact hypotheses and whether convergence is phasewise, phase-averaged, subsequence-only, or uniform.

---

## 10. Stage G — bounded extrapolation only after theorem effort

Use the packet's post-holdout extrapolation radii only after the theorem attack has been formulated.

Return:

`R054_SCALE_BIAS_ATLAS.json`.

Numerical extrapolation may support or attack conjectures but may not upgrade the Stage-F result class.

If the theorem remains OPEN, say so.

---

## 11. Mandatory adversarial controls

At minimum attack every item frozen in the packet, including:

- R053 holdout reuse;
- post-hoc CHORD3 patch disguised as the same generation;
- greedy optimality assumption;
- CHORD3-all privilege before enumeration;
- old radius/phase reuse;
- policy-class mutation after scoring;
- post-holdout mutation;
- pi/student inference leakage;
- tangent selection leakage;
- finite regression promoted to theorem;
- phase-average/uniform-phase conflation;
- anisotropy/isotropy conflation;
- K expansion before K=3 kill;
- unseen-type hiding;
- cyclic-start/seam artifact winner.

Return:

`R054_ADVERSARIAL_TEST_RESULTS.json`.

---

## 12. Exact computational checks

Provide deterministic checker/tests for at least:

- split bytes and no R053 pair overlap;
- exact triangular/hex boundary fixtures;
- D6 type canonicalization;
- exact three-mode endpoint-chord geometry;
- parser exact cover/no overlap;
- cyclic/reversal/D6 invariance;
- policy class cardinality exactly 27;
- no duplicate mappings;
- no pi/radius/phase/tangent in student inference;
- 100/200-digit ranking identity;
- winner hash immutability across holdout;
- holdout no-refit;
- extrapolation does not change frozen winner.

Prefer one task-local checker pass and one task-local test pass at the semantic checkpoint.

---

## 13. Required artifacts

Return at least:

- `R054_REPORT.md`;
- `R054_SPLIT_SCORING_PROTOCOL.json`;
- `R054_K3_TYPE_CATALOG.json`;
- `R054_K3_CHORD_LIBRARY.json`;
- `R054_PARSER_CONTRACT.json`;
- `R054_POLICY_CLASS.json`;
- `R054_EXHAUSTIVE_27_POLICY_ATLAS.json`;
- `R054_OPTIMAL_POLICY.json`;
- `R054_FRESH_HOLDOUT_RESULTS.json`;
- `R054_TANGENT_RECOVERY_ATLAS.json`;
- `R054_ASYMPTOTIC_BIAS_LEDGER.json`;
- `R054_SCALE_BIAS_ATLAS.json`;
- `R054_ADVERSARIAL_TEST_RESULTS.json`;
- `R054_EXACT_CHECK_RESULTS.json`;
- `R054_ARTIFACT_MANIFEST.json`;
- one checker and focused tests.

Freeze/report at minimum:

- `R054_SPLIT_SCORING_PROTOCOL_SHA256`;
- `R054_K3_CHORD_LIBRARY_SHA256`;
- `R054_PARSER_CONTRACT_SHA256`;
- `R054_POLICY_CLASS_SHA256`;
- `R054_OPTIMAL_POLICY_SHA256`;
- `R054_ARTIFACT_MANIFEST_SHA256`.

---

## 14. Completion and routing boundary

R054 returns when:

1. the fresh split is frozen and verified disjoint from R053;
2. the construction type audit is frozen;
3. all 27 policies are exhaustively ranked if the three-type precondition holds;
4. one winner is frozen before strict holdout;
5. strict holdout and tangent validation are completed without refit;
6. the asymptotic question receives an exact `PROVED / COUNTEREXAMPLE / OPEN` classification;
7. no K=4/K=5 mechanism is designed inside R054.

Preferred returns include:

`OPTIMIZER_DEBT_RESOLVED / BEST_K3_POLICY_IDENTIFIED / ASYMPTOTIC_OPEN / NOT_CANONICAL`

or

`K3_CHORD_FAMILY_PI_OBSTRUCTION / NEXT_LOCALITY_GENERATION_JUSTIFIED / NOT_CANONICAL`

or

`PI_TARGET_LIMIT_PROVED_FOR_FROZEN_K3_POLICY / NOT_CANONICAL`.

Only the second return class gives the Driver a clean reason to open a later larger-locality generation.

## 15. Advancement vector

Before R054:

- K=3 optimizer certainty: `low -> exact finite-class optimum`;
- fresh holdout independence after R053: `0 -> complete`;
- local circumference rule optimality inside frozen chord class: `unknown -> classified`;
- asymptotic bias theorem status: `empirical only -> proved/counterexample/open exact scope`;
- justification for K expansion: `premature -> evidence-gated`.

Advancement vector:

`optimizer-certainty +60 / fresh-evidence +45 / K3-classification +55 / asymptotic-status +50 / locality-routing +40`.
