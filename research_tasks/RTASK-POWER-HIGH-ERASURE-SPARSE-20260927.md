<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RTASK-POWER-HIGH-ERASURE-SPARSE-20260927",
  "title": "POWER 高丢失预算下达到最小跨度的稀疏构造",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "现有移位配对证明依赖d>e，只覆盖e<=H/3；更高预算虽有满区间解，尚缺同样跨度下有证明的位置节省。",
  "next_action": "先处理floor(H/3)<e<=floor(H/2)：在A=H+e下找出旧构造中共享端点的最小配对链，计算其最小删除覆盖，再尝试替代布置。",
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
  "registry_key": "RTASK-POWER-HIGH-ERASURE-SPARSE-20260927",
  "parent_objective_id": "OBJ-POWER-ROBUST-SPARSE-PERIOD-IDENTIFICATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "POWER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RTASK-POWER-ROBUST-INTAKE-20260927",
  "successor_gate": {
    "new_information_gap": "高预算d<=e时平移证据可共享位置；满区间的跨度最优性没有提供稀疏实现。",
    "why_parent_result_does_not_close_it": "父任务只纳入并核对既有候选基线，不解决此项优化；父任务当前尚无Result，本子任务须待其依赖满足，不能把计划当完成。",
    "discriminating_outcomes": [
      "给出声明范围内严格新界或有效构造",
      "给出限制当前路线的精确反例或结构性障碍",
      "预算不足或只重复旧结果，保留明确未决项"
    ],
    "kill_condition": "一个声明清晰的参数族具有严格位置节省和全删除模式保证即为实质成功，不要求一轮覆盖全部预算。只有随机删除测试或扩大跨度后的成功属于未达目标。发现共享端点会同时破坏多个证据时，保存最小反例并修正构造；预算耗尽不记作不可能。",
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

# POWER 高丢失预算下达到最小跨度的稀疏构造

## Mother question

在floor(H/3)<e<H且不保护任何位置时，能否构造比满区间更少的位置，仍达到A_min=e+max(H,2e)，并抵抗任意e个已知位置删除？

## Frozen inputs and scope

研究对象：整数位置集 S 包含于 [0,A]，只观察保留位置的精确模幂相等关系。分别识别所有 1<=r<=H，并把 r>H 归入超范围输出；超范围不是一种统一的相等模式。e 表示至多 e 个已知位置的删除；不是数值污染、读数通道删除或物理失效率。默认无保护位置、无隐含阶或离散对数输入、无额外群阶先验。

固定来源的候选结论为 c_D(r)=gcd{d 属于 D:r 整除 d}，空集 gcd=0；目标可识别当且仅当各 r<=H 满足 c_D(r)=r。最小跨度候选定理 A_min(H,e)=e+max_{1<=r<=H}r*ceil((e+1)/r)；0<=e<H 时等于 e+max(H,2e)。它已有自包含证明和有限验证，但尚非独立接纳结果。该跨度定理不是本子问题重新发现的目标。

现有稀疏构造仅保证 0<=e<=floor(H/3)：W=H-floor(H/3)，b=floor(sqrt((e+1)W))，q=ceil(W/b)，S=[0,b+e-1] 与各 [H-j*b,H-j*b+e] 的并集，0<=j<q。各区间是闭整数区间，跨度 H+e；位置数不超过 b+e+(e+1)ceil(W/b)。固定 e 的已有必要/构造量级分别约 sqrt(2(e+1)H) 与 sqrt(8(e+1)H/3)，不是全局最优性或通用求阶复杂度结论。

必须保留反例：H=6,e=4,A=11，删除4,5,6,7后混淆阶4与8；S=(0,1,3,6),H=1,A=6，删除1可混淆阶1与3，故一般支持不能只查奇偶。旧报告中的279项测试不是全仓或本任务新增测试。

精确来源：
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/src/enterprise_math/group_ring_span_erasures.py

## Hard target and required outputs

分别处理H/3<e<=H/2与H/2<e<H，前者跨度H+e、后者3e；明确整数边界。至少对一个非平凡参数族给出显式支持集、位置数上界及抗删除证书；或对一个清晰限定的旧构造扩展证明不能达标。可从一般r到p*r粗化删除判据或路径/多部图覆盖规律着手。

保留H=6,e=4,A=11的阶4/8反例，不得因阶8超出目标而删除它。报告空缺参数区间；不得把满区间已知可行重报为稀疏突破，或把低预算互不相交论证直接外推到d<=e。

## Research value to preserve

该任务直接扩展当前可靠性预算的适用边界。它区分跨度最优与位置节省，能够建立高损失情况下仍可执行的观察设计，或准确限定原移位构造为什么不能延伸。

## Success, kill, and return criteria

一个声明清晰的参数族具有严格位置节省和全删除模式保证即为实质成功，不要求一轮覆盖全部预算。只有随机删除测试或扩大跨度后的成功属于未达目标。发现共享端点会同时破坏多个证据时，保存最小反例并修正构造；预算耗尽不记作不可能。
