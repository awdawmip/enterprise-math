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
  "task_id": "RS-HBW-WL-WM-RECONCILE-20260927",
  "title": "心跳世界 WL／WM 加权提升的范围与接口整合",
  "frontier": "同名加权提升模块存在WL和WM两版，定义、API和验证编号不相同；尚无可互换性证书。",
  "next_action": "先对照两版种子、保护层和输出状态，确定COMPLETE、部分纤维和NO_LIFTS是否表达同一个命题。",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-HBW-WL-WM-RECONCILE-20260927",
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

# 心跳世界 WL／WM 加权提升的范围与接口整合

Status: published task specification; scientific result not yet produced.

## 0. Mother question

同一冻结ControlPacket输入及观察下，WL和WM两版的共同质量提升结果何时相同、何时不可互换？先回答部分输出的仿射闭包是否具有同样的健全性与完备性承诺。

## 1. Frozen inputs and scope

固定素数p、原生六轴、有限正权ControlPacket、源与目标端口和保护精度。科学作用与观察必须经既有已分型BRC接口；源引用中保留原权重、重数、线性作用与平移的载体，明确当前线性进位观察不保证原子词或平移落点。精度层m和时间拍t分别建模。本题消费的是有证明和本地计算证据的候选，不假定已获独立认可。

完整冻结依赖包见源目录 PUBLICATION.json；SHA-256 882167fc6b3fbdf58d9804032805bcf09f65652257b72534594c106b51918f55。原包提交9d04076c502f03254659ba51d3d6a839b475c444。

WL接口为WeightedLiftProblem、lift_weighted_kernel、WeightedLiftResult；WM接口为WeightedLiftSeed、lift_weighted_seed、WeightedLiftCertificate。不得拿一版的测试数量作为另一版验证。包含已公布的二进制换对应例、三进制三等质量动作例，以及类分裂反例；需自行核对每个算例的定义范围。

## 2. Hard target and required outputs

给出字段级输入／输出与观察对应表；对能够对齐的范围证明对应并用原BRC行作用证书核验；对不能对齐的范围交付最小反例或明确缺项。提出不覆盖原字节的接口整合方案，并列出所有仍不能共同复用的证明条件。输出同输入差异证据、测试范围和供子任务使用的精确载体合同。

## 3. Research value to preserve

先识别真正共同的接口和不可丢的差异，避免后续跨层程序无意混用两版证书；同时保存双方独有结果。

## 4. Success, kill, and return criteria

成功：至少完成一个共同范围的对应证明与一个边界核对，给出可执行整合建议。若发现论证或类型错误，冻结最小反例，不把候选转成已接纳事实。若两版实质相同，返回去重证书而不另造算法；若不同，保留两版用途并明确子任务应选哪一个。已有原始证据不重做为新发现。
