# R023I — BRC Narrow Shared-Surface Integration Return

Researcher-ID: `EM-R023I-D7ABB0`  
Task: `RS-R023I-BRC-NARROW-SHARED-SURFACE-INTEGRATION`  
Taskbook: `research_tasks/R023I_BRC_NARROW_SHARED_SURFACE_INTEGRATION_20260811.md` @ `e37f7aa26e0bb97d1515fc791ba940db05b6ed50`  
Frozen R023 Draft artifact: `#498`  
Frozen final owner head: `0b72b9e549e1469567764fbe89f9f2baa8b55453`  
Frozen semantic Lean candidate: `6eea57de1d30d6c2fe983121f6e209286a5c9895`  
Frozen module blob: `9905df19ce6f7dd79864384362487cc8f54c3349`  
Mode: `NO NEW MATHEMATICS / EXACT REPLAY / NOT CANONICAL`

## Return class

`R023I_EXACT_REPLAY_COMPLETE / EXTERNAL_MAINTENANCE_GATE_REMAINS / NOT_CANONICAL`

The R023 Boolean/result-support semantic payload replays without theorem-statement, assumption, namespace, or carrier changes. The only expected residual shared-surface gate is the pre-existing repository-tool index drift for `tools/research_identity.py` and `tools/research_taskbook.py`, which is explicitly outside R023I scope.

## Exact file/delta audit

| File | Required role | R023 theorem/assumption change | Status exposed |
|---|---|---|---|
| `EnterpriseMath/Relation/BranchRecoalescence.lean` | exact frozen replay | **NONE**; blob must equal `9905df19...` | `LEAN_CHECKED_WIP` source payload |
| `EnterpriseMath.lean` | root registration | **NONE**; import only | integration candidate, not `LEAN_CHECKED_MAIN` |
| `research_common_surface.json` | machine root/theorem/status router | **NONE**; metadata/routing only | `LEAN_CHECKED_WIP / NOT_CANONICAL` |
| `docs/RESEARCH_COMMON_SURFACE.en.md` | English human theorem/status router | **NONE**; scoped prose only | same WIP boundary |
| `docs/RESEARCH_COMMON_SURFACE.zh-CN.md` | Chinese human theorem/status router | **NONE**; bilingual scoped prose only | same WIP boundary |
| `docs/R023I_BRC_SHARED_SURFACE_RETURN.md` | integration provenance/audit | **NONE** | `NO NEW MATHEMATICS / NOT_CANONICAL` |

No new source/lineage registry sidecar is created. The current `check_references.py` schema validates records that are explicitly registered; it does not require a new lineage component merely because a Lean module is exposed. R023I therefore records prior-art/ownership/status boundaries in the machine/human routers and this integration audit without inventing a new novelty record.

## Claim → Lean declaration map

| Claim ID | Exact shared Lean declaration |
|---|---|
| `NO_RESURRECTION` | `EnterpriseMath.BranchRecoalescence.noResurrection` (point-signature specialization: `pointSignature_noResurrection`) |
| `ONE_STEP_COARSEST` | `EnterpriseMath.BranchRecoalescence.oneStepCoarsest` (R021 relational specialization: `oneStepCoarseSuccessorCoarsest`) |
| `SUPPORT_BRANCH_INVARIANT` | `EnterpriseMath.BranchRecoalescence.supportBranchInvariant` (observable corollary: `supportBranchObservableInvariant`) |
| `FORGETFUL_RECOALESCENCE_IFF` | `EnterpriseMath.BranchRecoalescence.forgetfulRecoalescence_iff` |

## Negative boundaries preserved

- 3-state quotient composition: `threeState_oneStep_exact`, `threeState_quotient_twoStep_coarseSupport`, `threeState_composition_spurious_q1`. The Lean artifact proves the witness; the three-state minimality statement remains limited to the R021 declared exhaustive one-generator/full-starting-fibre search class.
- Middle incidence correlation: `middleIncidence_exact_empty` plus `middleIncidence_coarse_spurious`.
- Current coarse equality insufficient for suffix safety: `sameCurrentCoarse_notSuffixSafe`.

## Semantic boundary audit

The shared wording remains:

`pointwise future-safe factorization baseline -> relational/result-support execution layer -> representation/resource choices`.

Exact-union recoalescence and forgetful replacement remain distinct. Runtime branching does not resurrect distinctions erased from the **complete** runtime encoding. `ONE_STEP_COARSEST` is a factorization/kernel universal property up to relabeling, not literal classifier-codomain identity. The support carrier remains Boolean/set-valued `Set X` only.

Excluded from this integration: R021 representation Pareto/branch-budget material, R022 HashClash/tool-mining results, multiplicity, provenance, probability/weights, signed/amplitude cancellation, new arithmetic specializations, and new Foundation primitives.

## Validation contract

The frozen R023 final owner head already has Driver-accepted standard warnings-fatal Lean run `31484436882` PASS. R023I additionally requires the replayed module blob to equal the frozen blob, valid machine JSON, bilingual/reference checks, exact root-index visibility, and no new shared-surface drift beyond the explicitly known tool-index maintenance defect.
