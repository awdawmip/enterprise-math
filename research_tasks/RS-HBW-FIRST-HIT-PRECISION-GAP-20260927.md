<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/9fcdbe1ad147a125464ae35fcf1dff493cec505d/research_notes/heartbeat_weighted_lift_20260927_AD0416/README.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fcdbe1ad147a125464ae35fcf1dff493cec505d/research_notes/heartbeat_weighted_lift_20260927_AD0416/RESEARCH_NOTE.md"
  ],
  "evidence_status": "SOURCE_BACKED_RESEARCH_CANDIDATES_UNREVIEWED_NOT_ADMITTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "HEARTBEAT_WORLD",
    "BRC",
    "FIRST_HIT",
    "PRECISION_GAP",
    "RESIDUAL_FAITHFUL"
  ],
  "claim_lease_minutes": 1440,
  "identity_lane": "HB-WEIGHTED-REPAIR",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "parent_objective_id": "PO-HBW-WEIGHTED-REPAIR-20260927",
  "historical_contribution_disclosure": [
    "EM-DIRECT-AD0416; source authorship is not independent review"
  ],
  "task_id": "RS-HBW-FIRST-HIT-PRECISION-GAP-20260927",
  "title": "心跳世界：首达观察的安全降精度与首次分歧边界",
  "frontier": "已有k=1见证显示普遍作用证书先失效而指定初态首达观察仍暂时一致，但尚无参数族边界或较弱观察证书。",
  "next_action": "固定WL证据中的原始初态、U/V/E_k族和首达读出，先对一般k推导普遍证书失效阈值与可达观察首次可能分歧的上下界。",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HBW-WL-WM-RECONCILE-20260927",
  "successor_gate": {
    "new_information_gap": "现有WL证据只给出一个固定k=1的阈值分离见证，尚未刻画普遍作用证书失效与指定初态首达分布首次变化之间的参数化间隔。",
    "why_parent_result_does_not_close_it": "WL/WM整合任务解决接口与命题范围的可互换性，不给出指定初态、指定未来操作语言下的首达观察保真阈值；多层修复族和稳定子任务研究的也是不同对象。",
    "discriminating_outcomes": [
      "给出非平凡k参数族上的观察保真区间及首次分歧边界",
      "证明较弱观察证书不能避免普遍证书并给出参数化反例",
      "仅在明确子族成立并准确标出其余UNKNOWN范围"
    ],
    "kill_condition": "若研究只能重跑k=1的R=3/4见证或只比较最终命中概率而不能得到参数化边界、严格反例或资源改进，则停止该路线并返回未解决边界。",
    "alternative_route_or_free_exploration_considered": "比较完整安全输入证书、从指定初态的可达子链证书、有限有理链最小化及直接构造最短分歧见证；不预设较弱证书一定更便宜。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "该问题有独立的参数、输出与可证伪目标，既不由WL/WM接口整合自动解决，也不与多层transporter或稳定子生成任务重复。"
  },
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-HBW-FIRST-HIT-PRECISION-GAP-20260927",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 心跳世界：首达观察的安全降精度与首次分歧边界

Status: published task specification; scientific result not yet produced.

## 0. Mother question

在指定初态、允许操作和首达读出下，普遍作用证书开始失效的精度阈值，与实际首达时间分布首次发生变化的精度阈值相差多少？能否给出不先验证全部安全输入格、但对声明未来语言足够的可计算观察保真判据？

## 1. Frozen inputs and scope

固定 enterprise-math@9fcdbe1ad147a125464ae35fcf1dff493cec505d 的两个 source_refs，WL snapshot 与 WM 主干模块保持分型，不把二者当作可互换副本。原生六轴按二维块重复三次；取 U=diag(2,1)、V=diag(1,2)、E_k=I+2^k E_12，k>=1。基线在活动端口 U、V 各有质量 1/4，停止质量 1/2；扰动为 U、UE_k 各 1/8，V 为 1/4，停止质量 1/2；停止后恒等。

初态必须逐项复用原 WL 证据声明的完整原生表示，并在新交付物中显式写出，不得换成更方便的初态。保留原 ports、weight、multiplicity、action、translation 和观察限制。精度阈值 R 与时间拍 t 分开建模，目标是完整首达时间分布及其生成函数，不只比较某一时刻样本或最终命中概率。科学作用继续使用冻结来源的正质量 BRC 接口，不把修复数量计作概率。

来源中 k=1 的作者见证为：R=3 时指定可达观察链一致；R=4 时首次在 t=8 分歧，基线 56/131072、扰动 57/131072。本任务把它当作待复核起点，而不是参数族结论或独立接纳事实。

## 2. Hard target and required outputs

对至少一个非平凡 k 参数族，定义并刻画三个量：普遍作用证书的首次失效阈值、从声明初态出发的完整首达分布首次变化阈值，以及变化阈值下的最小分歧时间。给出支持参数族的证明、显式上/下界或参数化反例，不能把 k=1 数值直接外推。

交付声明观察、初态与时域的精确保真证书，并至少包含一例“普遍证书已失效而观察证书仍成立”。对实际分歧给出最短见证和精确有理质量差。有限有理链的标准等价检查或生成函数相等只能作为验证基线；新增价值必须来自该原生族的边界定理、较弱充分条件、严格反例或可证明资源改进。

报告可达状态构造、最小化、验证和整数位数成本。预算不足或尚未覆盖的状态必须标记 UNKNOWN，不得用“未发现差异”替代等价证明。

## 3. Research value to preserve

区分“当前精度下看不见”与“在声明未来操作语言下始终无关”，为低精度研究建立比普遍全输入证书更贴近目标观察的安全边界。该任务保留全部正质量、来源和残差，不把这一问题与 QFT 的有符号振幅抵消混成同一种代数。

## 4. Success, kill, and return criteria

成功：得到明确 k 参数族的观察保真范围和边界证书，或证明拟议降精度策略必失败的参数化反例。只重跑 R=3/4、把最终命中概率相等当作完整首达律相等、混同 R 与 t、忽略不可达或 UNKNOWN 质量，均不通过。

若 WL/WM 对照表明所需观察接口在两版中不兼容，则分别保留各自正确范围并返回确切缺口，不覆盖任一版本。若最新任务已覆盖同一交付物，则停止重复发布方向并返回去重证据。
