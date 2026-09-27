<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "dependencies": [
    "RS-HBW-WL-WM-RECONCILE-20260927"
  ],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/9fcdbe1ad147a125464ae35fcf1dff493cec505d/research_notes/heartbeat_weighted_lift_20260927_AD0416/README.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fcdbe1ad147a125464ae35fcf1dff493cec505d/research_notes/heartbeat_weighted_lift_20260927_AD0416/RESEARCH_NOTE.md",
    "https://github.com/awdawmip/enterprise-math/blob/9fcdbe1ad147a125464ae35fcf1dff493cec505d/research_notes/heartbeat_weighted_lift_20260927_AD0416/THEOREM_LEDGER.json",
    "https://github.com/awdawmip/enterprise-math/blob/9fcdbe1ad147a125464ae35fcf1dff493cec505d/research_notes/heartbeat_weighted_lift_20260927_AD0416/snapshot/src/enterprise_math/heartbeat_weighted_germ_lift.py",
    "https://github.com/awdawmip/enterprise-math/blob/6dd526fbf08aa97baea181548c0d8240f7c12b82/src/enterprise_math/heartbeat_weighted_germ_lift.py",
    "https://github.com/awdawmip/enterprise-math/blob/6dd526fbf08aa97baea181548c0d8240f7c12b82/research_notes/heartbeat_weighted_germ_lift_20260927_AD0416/THEOREM_LEDGER.json"
  ],
  "evidence_status": "SOURCE_BACKED_RESEARCH_CANDIDATES_UNREVIEWED_NOT_ADMITTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "HEARTBEAT_WORLD",
    "BRC",
    "FIRST_TIER_PORTFOLIO",
    "RESIDUAL_FAITHFUL"
  ],
  "identity_lane": "HB-WEIGHTED-REPAIR",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "parent_objective_id": "PO-HBW-WEIGHTED-REPAIR-20260927",
  "user_directive": "2026-09-27：写入github，太大文件传到google drive，然后把后续研究方向发布到状态机。",
  "historical_contribution_disclosure": [
    "EM-DIRECT-AD0416; authorship is not independent review"
  ],
  "registration_is_task_claim": false,
  "task_id": "RS-HBW-WEIGHTED-MULTILAYER-FAMILY-20260927",
  "title": "心跳世界：多层共同质量修复族的符号传播",
  "frontier": "一位修复纤维可整体表示为仿射空间，但没有跨多层保持有限表示的证书。",
  "next_action": "把两层后的共同参考系关系写成原修复参数的精确约束，判定新约束是否仍为仿射，或必须分裂。",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HBW-WL-WM-RECONCILE-20260927",
  "successor_gate": {
    "new_information_gap": "一位仿射性不控制多位乘积交叉项、精度进位和后续动作类细分。",
    "why_parent_result_does_not_close_it": "整合只确定两版可复用范围，不给出新的多层闭合关系；原WL/WM证据只覆盖一位。",
    "discriminating_outcomes": [
      "跨层仍仿射且给出条件",
      "出现非线性或类分裂且给出见证",
      "在限定子族可闭合、其余保留未决"
    ],
    "kill_condition": "若只能重述一位结果或逐个展开所有修复而无新增证书，停止该路线并返回未压缩成本与障碍。",
    "alternative_route_or_free_exploration_considered": "比较逐帧一位迭代、稳定子像与核路线、以及直接研究不可提升反例；不预设仿射形式永远最佳。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "该问题有独立的跨层输入输出和可证伪目标，不能由源码整合或关闭原一位任务解决。"
  },
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-HBW-WEIGHTED-MULTILAYER-FAMILY-20260927",
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

# 心跳世界：多层共同质量修复族的符号传播

Status: published task specification; scientific result not yet produced.

## 0. Mother question

不逐个展开一位纤维内的参考系，怎样将完整修复族继续推进到m+2及更深精度，并准确保留类碰撞、对应更换和共同障碍？

## 1. Frozen inputs and scope

固定素数p、原生六轴、有限正权ControlPacket、源与目标端口和保护精度。科学作用与观察必须经既有已分型BRC接口；源引用中保留原权重、重数、线性作用与平移的载体，明确当前线性进位观察不保证原子词或平移落点。精度层m和时间拍t分别建模。本题消费的是有证明和本地计算证据的候选，不假定已获独立认可。

完整冻结依赖包见源目录 PUBLICATION.json；SHA-256 882167fc6b3fbdf58d9804032805bcf09f65652257b72534594c106b51918f55。原包提交9d04076c502f03254659ba51d3d6a839b475c444。

以整合任务返回的明确载体合同为准。必须包含p=2与p=3的小型输入、完整6×6修复的声明范围、共同参考系及每边辅助标量。三进制A_t=[[1,3t],[0,2]](t=0,1,2)三块重复、各质量1/3，作为大纤维诊断输入；一位18参数结论仅按原范围使用。

## 2. Hard target and required outputs

提出可复核的跨层族载体、更新关系与健全性证明；给出保持仿射的充分条件，或首次必须拆分的反例。小型输入用既有BRC证书作完备对照，完整六轴实例只能在已证范围内声明。预算截断必须保留尚未展开的族，不能用样本代表完整性。记录输入规模、表示规模、实际展开数及剩余障碍。

## 3. Research value to preserve

把浅层数亿个修复的紧凑表示延续为可用于后续研究的结构，而不是每升一层就恢复逐个枚举。

## 4. Success, kill, and return criteria

成功：完成至少连续两次提升的整体族证书和一个非平凡实例；或交付证明单一仿射族不足的最小反例及必要修复状态。不得以浅层自由度多推断无限可提升。若新表述等价于逐个枚举且没有表示优势，返回精确成本与更适合的边界，保留有价值的障碍。
