<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RTASK-POWER-PROTECTED-CORE-TRADEOFF-20260927",
  "title": "POWER 明示保护核心与扩展跨度的资源权衡",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "任意支持的保护细类可强制/阻断粗化，但给定保护核心时跨度、位置数、丢失预算的可计算权衡尚未建立。",
  "next_action": "把P作为固定外部输入，先精确分析一个连续保护区间与双端保护条带两类核心，列出对每个r,p哪些细类被强制保留或使混淆不可能。",
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
  "registry_key": "RTASK-POWER-PROTECTED-CORE-TRADEOFF-20260927",
  "parent_objective_id": "OBJ-POWER-ROBUST-SPARSE-PERIOD-IDENTIFICATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "POWER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RTASK-POWER-ROBUST-INTAKE-20260927",
  "successor_gate": {
    "new_information_gap": "已有逐实例最小破坏判据尚未回答保护核心与跨度/采样资源的设计权衡。",
    "why_parent_result_does_not_close_it": "父任务只纳入并核对既有候选基线，不解决此项优化；父任务当前尚无Result，本子任务须待其依赖满足，不能把计划当完成。",
    "discriminating_outcomes": [
      "给出声明范围内严格新界或有效构造",
      "给出限制当前路线的精确反例或结构性障碍",
      "预算不足或只重复旧结果，保留明确未决项"
    ],
    "kill_condition": "至少一个声明核心族的精确可行边界，或严格改进的界/证书，且包含P为空和既有端点反例的退化检查。只报告某次可用保护集合而未计保护成本不合格；不同P、跨度或观察器的比较不可冒充同任务优势。",
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

# POWER 明示保护核心与扩展跨度的资源权衡

## Mother question

给定明确且计入成本的保护核心P，在S包含P、S位于[0,A]、其余位置最多删除e个的模型中，保护资源怎样改变最小可行跨度与最少采样位置？

## Frozen inputs and scope

研究对象：整数位置集 S 包含于 [0,A]，只观察保留位置的精确模幂相等关系。分别识别所有 1<=r<=H，并把 r>H 归入超范围输出；超范围不是一种统一的相等模式。e 表示至多 e 个已知位置的删除；不是数值污染、读数通道删除或物理失效率。默认无保护位置、无隐含阶或离散对数输入、无额外群阶先验。

固定来源的候选结论为 c_D(r)=gcd{d 属于 D:r 整除 d}，空集 gcd=0；目标可识别当且仅当各 r<=H 满足 c_D(r)=r。最小跨度候选定理 A_min(H,e)=e+max_{1<=r<=H}r*ceil((e+1)/r)；0<=e<H 时等于 e+max(H,2e)。它已有自包含证明和有限验证，但尚非独立接纳结果。该跨度定理不是本子问题重新发现的目标。

现有稀疏构造仅保证 0<=e<=floor(H/3)：W=H-floor(H/3)，b=floor(sqrt((e+1)W))，q=ceil(W/b)，S=[0,b+e-1] 与各 [H-j*b,H-j*b+e] 的并集，0<=j<q。各区间是闭整数区间，跨度 H+e；位置数不超过 b+e+(e+1)ceil(W/b)。固定 e 的已有必要/构造量级分别约 sqrt(2(e+1)H) 与 sqrt(8(e+1)H/3)，不是全局最优性或通用求阶复杂度结论。

必须保留反例：H=6,e=4,A=11，删除4,5,6,7后混淆阶4与8；S=(0,1,3,6),H=1,A=6，删除1可混淆阶1与3，故一般支持不能只查奇偶。旧报告中的279项测试不是全仓或本任务新增测试。

精确来源：
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/src/enterprise_math/group_ring_span_erasures.py

## Hard target and required outputs

定义可行性函数或Pareto表，分别计入|P|、|S|、A、e；P必须先声明，不得在见到失败后免费增补。对连续核心、端部条带或一个明确参数族导出精确公式或可核验上下界，并给出达到界的支持集/失效删除见证。

复用粗模r/细模pr判据：同一粗类出现两个受保护细类则该粗化不可能；一个受保护细类则强制保留它；无保护时保留最大细类。验证P为空时恢复无保护最小跨度结论；不要把该结论无条件用于P不空。所有保护假设是模型资源，不是实测物理可靠性。

## Research value to preserve

这项研究把人为保护与增加冗余的代价放到同一模型比较，可回答应该增加跨度、增加可丢失位置，还是保护少量核心。即使只有受限核心族的精确解或反例，也能形成可复用的设计边界，而不与前两任务重复。

## Success, kill, and return criteria

至少一个声明核心族的精确可行边界，或严格改进的界/证书，且包含P为空和既有端点反例的退化检查。只报告某次可用保护集合而未计保护成本不合格；不同P、跨度或观察器的比较不可冒充同任务优势。
