<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RTASK-POWER-ROBUST-INTAKE-20260927",
  "title": "POWER 抗丢失稀疏周期研究：既有成果纳入与续接基线确认",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "十一段直接研究已有来源；尚无正式父任务。需纳入已有最小跨度及稀疏构造，确认可供三个续接问题使用的候选基线和差异清单。",
  "next_action": "先核对固定REPORT的最小跨度命题、观察范围和三个反例，将假设/已证候选/未决点分开列出；不重跑已完整保存的研究作为新增成果。",
  "dependencies": [],
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
  "registry_key": "RTASK-POWER-ROBUST-INTAKE-20260927",
  "parent_objective_id": "OBJ-POWER-ROBUST-SPARSE-PERIOD-IDENTIFICATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "POWER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
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

# POWER 抗丢失稀疏周期研究：既有成果纳入与续接基线确认

## Mother question

如何将已有直接研究的最小跨度证明、抗丢失构造与反例，纳入一个可审计且可独立接续的正式任务来源，而不把既有候选结论冒充已接纳定理？

## Frozen inputs and scope

研究对象：整数位置集 S 包含于 [0,A]，只观察保留位置的精确模幂相等关系。分别识别所有 1<=r<=H，并把 r>H 归入超范围输出；超范围不是一种统一的相等模式。e 表示至多 e 个已知位置的删除；不是数值污染、读数通道删除或物理失效率。默认无保护位置、无隐含阶或离散对数输入、无额外群阶先验。

固定来源的候选结论为 c_D(r)=gcd{d 属于 D:r 整除 d}，空集 gcd=0；目标可识别当且仅当各 r<=H 满足 c_D(r)=r。最小跨度候选定理 A_min(H,e)=e+max_{1<=r<=H}r*ceil((e+1)/r)；0<=e<H 时等于 e+max(H,2e)。它已有自包含证明和有限验证，但尚非独立接纳结果。该跨度定理不是本子问题重新发现的目标。

现有稀疏构造仅保证 0<=e<=floor(H/3)：W=H-floor(H/3)，b=floor(sqrt((e+1)W))，q=ceil(W/b)，S=[0,b+e-1] 与各 [H-j*b,H-j*b+e] 的并集，0<=j<q。各区间是闭整数区间，跨度 H+e；位置数不超过 b+e+(e+1)ceil(W/b)。固定 e 的已有必要/构造量级分别约 sqrt(2(e+1)H) 与 sqrt(8(e+1)H/3)，不是全局最优性或通用求阶复杂度结论。

必须保留反例：H=6,e=4,A=11，删除4,5,6,7后混淆阶4与8；S=(0,1,3,6),H=1,A=6，删除1可混淆阶1与3，故一般支持不能只查奇偶。旧报告中的279项测试不是全仓或本任务新增测试。

精确来源：
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md
https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/src/enterprise_math/group_ring_span_erasures.py

## Hard target and required outputs

提交基线矩阵：每个采用命题的精确表述、假设、固定来源、证明关键步骤、验证范围及疑点；检查A_min公式和e<=H/3构造的逻辑接口。给出三项子任务可用的输入清单和不应重复事项。复用已保存证明与测试，不以从头重写代码作为成功标准。若发现实质错误，给出最小反例、影响命题和修订范围；依赖该命题的子任务不得把它当作可靠基线。

本任务是首次纳入旧直接研究，不存在前任正式Task/Result；不补造其编号。记录原活动RA-POWER-REVIEW-16243626C61A及贡献来源。通过本任务只建立任务局部的可用来源和待审事项；独立审查结论由后续实际程序给出。

## Research value to preserve

已有数学工作若仅保留在聊天和研究活动中，下一执行者容易重做已完成部分或误用候选。这个有限纳入单元将源文、假设、反例、未决目标绑定，允许三个有不同信息缺口的数学任务并行接续，也把原作者贡献与独立判断分开保留。

## Success, kill, and return criteria

完成条件：基线矩阵、引用、三个续接输入及疑点处理齐备，且没有把最小跨度与最少位置混为一谈。若证明存在未闭合关键步骤，返回具体缺口/反例和影响范围，不给无条件可用结论。只有重新跑出同一测试数字、或仅重排文档，不算完成。
