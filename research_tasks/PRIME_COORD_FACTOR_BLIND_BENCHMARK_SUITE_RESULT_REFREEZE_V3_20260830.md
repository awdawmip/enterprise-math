<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
  "title": "PCF2 sealed factor-blind benchmark 结果完整性重冻结 V3",
  "kind": "RESEARCH",
  "owner": "research/prime-coord-factor-blind-benchmark-suite",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Recover the already-completed PCF2 sealed N-only benchmark as a current reviewable Result with a complete output manifest, preserving the frozen corpus, public parameters, leakage tests, candidate/baseline results and no-speedup boundary without retuning the scored run.",
  "next_action": "Reproduce the frozen PCF2 return, benchmark artifacts and both checkers from the pinned prior branch, emit a no-math/no-score-delta revision return, and freeze a new Result-ID that binds every frozen output with Git blob SHA-1 and SHA-256.",
  "dependencies": [
    "research_tasks/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_READY_AFTER_PCF1_20260827.md@main",
    "research_objective_records/ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION/OG-AA2BAD92F59DC97880C7.json@main"
  ],
  "source_refs": [
    "research/prime-coord-factor-blind-benchmark-suite-em-pcf2-4b7c91@dce4a309f8d799030081ed82e310c26a92d8f465",
    "research_returns/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_RETURN_20260827.md@blob:90275518a1edf495cc120959a7fcc009ecdc22bc"
  ],
  "evidence_status": "BENCHMARK_FROZEN_AND_SEALED / RESULT_ENVELOPE_INCOMPLETE / NO_SCORE_DELTA_RECOVERY",
  "last_progress_ref": "Draft PR #740 / RR-03A546B894E6AF3840CA",
  "last_progress_at": "2026-08-27T12:20:00+00:00",
  "hard_block": null,
  "tags": ["PCF2","prime-coordinate-factor-extraction","benchmark","N-only","sealed-corpus","result-integrity","no-score-delta"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF2R3",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE",
  "successor_gate": {
    "new_information_gap": "PCF2 completed and handed off a sealed benchmark, but the frozen Result manifest pins only the return although the same branch froze three benchmark artifacts, two exact checkers and the execution record; current Driver review cannot consume that evidence chain.",
    "why_parent_result_does_not_close_it": "The immutable old Result cannot be edited. The benchmark must be re-frozen under the current digest contract before it can serve as the canonical falsification surface for later N-only candidates.",
    "discriminating_outcomes": [
      "a new Result-ID reproduces the exact frozen corpus, parameters, scored outputs and leakage checks and binds every output with SHA-1/SHA-256",
      "replay detects score/corpus/parameter drift, forcing substantive benchmark revision rather than integrity recovery",
      "one or more old frozen outputs cannot be reproduced, preventing benchmark canonicalization"
    ],
    "kill_condition": "Do not retune the 89-case corpus, public seeds, candidate polynomials, baseline budgets or scored outputs; do not turn finite benchmark performance into a factoring theorem or speedup claim.",
    "alternative_route_or_free_exploration_considered": "Leaving the old branch-only benchmark orphaned would force every future N-only candidate to invent an incompatible falsification surface. Rebuilding a new benchmark from scratch would erase the value of the frozen scored run. Integrity-only re-freeze is the smallest safe recovery.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The current publication generation can only create a new immutable Result through a new execution chain; the old Result is immutable and incomplete."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF2 sealed factor-blind benchmark 结果完整性重冻结 V3

## Mother question

PCF2 已经冻结了一个 dual-compartment、factor-blind 的 exact-integer benchmark，但旧 `RR-03A546B894E6AF3840CA` 只在 manifest 中绑定 return，无法在当前 Result contract 下作为 canonical benchmark evidence。如何在**零 corpus/score/parameter 漂移**条件下把这套 benchmark 恢复成可审核、可复用的控制面？

## Frozen inputs and scope

冻结旧研究 branch：`research/prime-coord-factor-blind-benchmark-suite-em-pcf2-4b7c91@dce4a309f8d799030081ed82e310c26a92d8f465`。

冻结旧 scored benchmark 的语义：

- candidate worker 输入仅允许 `N + independent public seed + candidate id + precommitted public parameters`；
- private factors 只存在于 corpus/verifier compartment；
- 6 个 deliberate leakage/adaptive payload 必须继续 `6/6` 被拒；
- frozen corpus 仍为 89 个 composites、8 个 adversarial families、3 个 bit bands；
- Prime Fusion quadratic public probes `74/89`；
- Prime Fusion sixth-power probes `84/89`；
- trial division `89/89`；
- Fermat(4096) `83/89`；
- fixed-schedule Pollard rho `89/89`；
- Pollard p-1(B1=256) `39/89`；
- raw operation counts 仍只是 algorithm-local exact proxies，不得包装成 wall-clock 比较；
- finite corpus evidence 只用于 regression/falsification，不得提升成无限族 factorization theorem。

旧 branch 实际冻结的 load-bearing outputs 至少包括：

1. `research_returns/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_RETURN_20260827.md`；
2. `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/README.md`；
3. `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/benchmark_result_summary.json`；
4. `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/parameter_manifest.json`；
5. `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/replay_schema.json`；
6. `scripts/check_prime_coord_factor_blind_benchmark_suite.py`；
7. `scripts/check_prime_coord_factor_blind_benchmark_suite_independent.py`；
8. current revision execution record；
9. new immutable Result record。

不得通过只 manifest return 的方式再次冻结。

## Hard target and required outputs

Hard target:

`PCF2_SEALED_FACTOR_BLIND_BENCHMARK_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_SCORE_DRIFT`。

必须：

- 精确复现 frozen benchmark；
- revision return 明确 `NO_CORPUS_DELTA / NO_PARAMETER_DELTA / NO_SCORE_DELTA`；
- 两个 checker 都必须跑通；
- 新 execution record；
- NEW Result-ID；
- Result manifest 对所有本次冻结输出给出 `path + Git blob SHA-1 + SHA-256`；
- 独立 verifier 继续逐行确认成功项满足 `1<d<N` 且 `d|N`；
- benchmark 成功后只作为版本化 control surface，未来新 extractor 必须经新的 authorized benchmark generation 才能加入，不能回改这次 scored run。

## Research value to preserve

这条支线不是“又一个 factoring heuristic”。它的价值是建立一个**可重复、factor-blind、不会把 hidden factors 泄给 candidate worker**的共同实验地板。新发布的 `N-coupled asymmetric singularization`、未来 PCF/Prime-Fusion N-only candidate、以及任何声称存在公开 asymmetry generator 的方法，都需要在同一 sealed surface 上被验伪，而不是各自选择有利样本。

## Success, kill, and return criteria

成功只是 benchmark evidence chain 恢复，不是算法成功。

Kill conditions：

- 修改 corpus、seed、candidate polynomial、baseline budget 或任何 frozen score；
- 把 factor labels 暴露给 candidate worker；
- 漏 manifest frozen outputs；
- 只跑主 checker、不跑 independent verifier；
- 用有限 89-case 结果声称 asymptotic factoring speedup；
- 在 re-freeze 中偷偷加入新的 candidate 并改变 scored generation。
