<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RTASK-POWER-ROBUST-MARK-GAP-20260927",
  "title": "POWER 最小跨度下抗丢失位置数的上下界间隙",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "最小跨度已有公式；0<=e<=H/3的最少位置仍处于sqrt(2(e+1)H)必要下界与sqrt(8(e+1)H/3)构造上界之间。",
  "next_action": "先在固定e=1和e=2、A=H+e的模型下，分析强制边界条带和跨中点配对是否给出比现有计数更强的限制；再选择一个可证明改进的参数族。",
  "dependencies": [
    "RTASK-POWER-ROBUST-INTAKE-20260927"
  ],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/src/enterprise_math/group_ring_span_erasures.py",
    "https://github.com/awdawmip/enterprise-math/blob/aa895b880ebc259e91f97506ef2fc63b8cd1842b/research_activity_records/RA-POWER-REVIEW-16243626C61A.json"
  ],
  "evidence_status": "LEGACY_RESEARCH_CANDIDATE_PINNED_NOT_INDEPENDENTLY_ADMITTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "POWER",
    "robust-period-identification",
    "user-directed-followup"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RTASK-POWER-ROBUST-MARK-GAP-20260927",
  "parent_objective_id": "OBJ-POWER-ROBUST-SPARSE-PERIOD-IDENTIFICATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "POWER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RTASK-POWER-ROBUST-INTAKE-20260927",
  "successor_gate": {
    "new_information_gap": "最小跨度并不确定最少位置；已有上、下界常数不同。",
    "why_parent_result_does_not_close_it": "父任务只纳入并核对既有候选基线，不解决此项优化；父任务当前尚无Result，本子任务须待其依赖满足，不能把计划当完成。",
    "discriminating_outcomes": [
      "给出声明范围内严格新界或有效构造",
      "给出限制当前路线的精确反例或结构性障碍",
      "预算不足或只重复旧结果，保留明确未决项"
    ],
    "kill_condition": "成功须给出严格的新界、新构造或具范围的排除证据。只有删点局部最优、若干较小样本或更快实现而无所声明的新数学信息，返回PARTIAL。若候选只靠增加跨度或隐含保护位置获益，按模型不符保留反例，转回本任务限定范围。",
    "alternative_route_or_free_exploration_considered": "已比较结束本研究单元、直接使用满区间、转用经典大步小步，以及另选观察器；这些可处理旧问题，却不回答当前固定资源模型的差异，故保留本有界任务。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "本问题与基线纳入的验证目标不同，并可由另一执行者独立续接；三个子任务共享前置基线，彼此无依赖，避免把不相关难点合成不可完成的大任务。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "legacy_source_activity_id": "RA-POWER-REVIEW-16243626C61A",
  "legacy_source_commit": "6b40284e808edb8bf74ff07ffa9efaf02bcfd021",
  "objective_description": "吸收POWER的有用方法，推进进取数论在有限碰撞观察下的抗丢失稀疏周期识别；本次只登记后续任务。"
}
-->

# POWER 最小跨度下抗丢失位置数的上下界间隙

## Mother question

在精确最小跨度A=H+e、无保护位置、0<=e<=floor(H/3)下，能否严格改进抵抗任意e个位置删除所需的最少位置数下界或构造上界，并明确改进的参数范围？

## Frozen inputs and scope

研究对象：整数位置集 S 包含于 [0,A]，只观察保留位置的精确模幂相等关系。分别识别所有 1<=r<=H，并把 r>H 归入超范围输出；超范围不是一种统一的相等模式。e 表示至多 e 个已知位置的删除；不是数值污染、读数通道删除或物理失效率。默认无保护位置、无隐含阶或离散对数输入、无额外群阶先验。

固定来源的候选结论为 c_D(r)=gcd{d 属于 D:r 整除 d}，空集 gcd=0；目标可识别当且仅当各 r<=H 满足 c_D(r)=r。最小跨度候选定理 A_min(H,e)=e+max_{1<=r<=H}r*ceil((e+1)/r)；0<=e<H 时等于 e+max(H,2e)。它已有自包含证明和有限验证，但尚非独立接纳结果。该跨度定理不是本子问题重新发现的目标。

现有稀疏构造仅保证 0<=e<=floor(H/3)：W=H-floor(H/3)，b=floor(sqrt((e+1)W))，q=ceil(W/b)，S=[0,b+e-1] 与各 [H-j*b,H-j*b+e] 的并集，0<=j<q。各区间是闭整数区间，跨度 H+e；位置数不超过 b+e+(e+1)ceil(W/b)。固定 e 的已有必要/构造量级分别约 sqrt(2(e+1)H) 与 sqrt(8(e+1)H/3)，不是全局最优性或通用求阶复杂度结论。

必须保留反例：H=6,e=4,A=11，删除4,5,6,7后混淆阶4與8；S=(0,1,3,6),H=1,A=6，删除1可混淆阶1与3，故一般支持不能只查奇偶。旧报告中的279项测试不是全仓或本任务新增测试。

精确来源：
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/src/enterprise_math/group_ring_span_erasures.py

## Hard target and required outputs

给出m(H,e)的准确优化定义，保留边界条带{0,...,e}和{H,...,H+e}是必需位置而非保护位置的区别。至少完成一项：某个无限参数族的严格下界改进；更少位置的显式构造及抗删除证明；或一个明确受限构造类不能改进现有界的结构性反例/障碍。提供可检查证书或足够小的完整算例。

若使用有限搜索，保存搜索范围、完备性、预算和实际最优/未定状态，不能把包含极小当成最小。比较必须固定H、e、跨度、观察器和保护条件；位置数收益不替代实际运算成本。

## Research value to preserve

该任务瞄准已明确的构造/必要界间隙，不再重新包装碰撞求阶。无论取得更紧下界、显式改进还是受限构造障碍，都能决定后续应优化组合结构还是改变设计族，并直接约束采样资源。

## Success, kill, and return criteria

成功须给出严格的新界、新构造或具范围的排除证据。只有删点局部最优、若干较小样本或更快实现而无所声明的新数学信息，返回PARTIAL。若候选只靠增加跨度或隐含保护位置获益，按模型不符保留反例，转回本任务限定范围。
