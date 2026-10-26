<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DISC-COMPAT-20261026-05",
  "title": "手征费米子、倍增与规范一致性",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "一个选定的离散原生动力学能否恢复低能手征粒子与相互作用，而不产生不符合观测的额外轻粒子或规范不一致？",
  "next_action": "先从任务09得到有效3+1维与粒子读出的对应，再从实际更新律或候选提取低能描述，逐项判定所选定理的四个前提。缺少桥则先返回缺项。",
  "dependencies": [
    "RS-DISC-COMPAT-20261026-00",
    "RS-DISC-COMPAT-20261026-01",
    "RS-DISC-COMPAT-20261026-09"
  ],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/p000_reality_foundation.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/foundational_logic.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/research_constraints/heartbeat_brc_only.json",
    "https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md",
    "https://github.com/awdawmip/chatgpt-global-knowledge/blob/1f73bff7ce37e663922e3c8dd29411441b0e37a7/projects/enterprise-math/NATIVE_WAVE_COMMON_RESIDUAL_CURRENT.md",
    "https://github.com/awdawmip/enterprise-math/blob/18d4a6d12ab7d8ab0897e9336c81ac07238fd30c/research_notes/discrete_light_objections_20261026_9c8ddfc415e7.md",
    "https://doi.org/10.1016/0550-3213(81)90361-8",
    "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.25.2649",
    "https://arxiv.org/abs/hep-lat/9802011v1",
    "https://doi.org/10.1016/0550-3213(82)90011-6"
  ],
  "evidence_status": "SPECIFICATION_ONLY_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "discrete-compatibility",
    "empirical-pressure",
    "foundation-facing"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DISC-COMPAT-20261026-05",
  "parent_objective_id": "OBJ-DISCRETE-EMPIRICAL-COMPATIBILITY-20261026",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DCMP",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# RS-DISC-COMPAT-20261026-05 — 手征费米子、倍增与规范一致性

## 0. Mother question

一个选定的离散原生动力学能否恢复低能手征粒子与相互作用，而不产生不符合观测的额外轻粒子或规范不一致？

父目标：OBJ-DISCRETE-EMPIRICAL-COMPATIBILITY-20261026。本项来自用户直接提出的反证与经验兼容性方向；集合内建议执行组为B，全局排序仍由已登记的默认级别决定。任务依赖：RS-DISC-COMPAT-20261026-00, RS-DISC-COMPAT-20261026-01, RS-DISC-COMPAT-20261026-09。

## 1. Frozen inputs and scope

原生基线是 X6 六空间轴及独立定型时间，原生120度关系不等同普通平面角。波允许非邻接/全域自洽机制；不得追加固定物理拍长或每拍一格。激活、正分支质量、相位、能量及共同余量分开定型。三维、仪器、物质和时间/能量标定属于待解释的读出层。

用户本次要求主动寻找不兼容及缺项。固定基线用于定位失败，不授予基线免于证据的地位。此任务不直接改写保护文件；应如实返回具体假设组合或桥的失败。

现有工具复用状态：REUSE_APPLIED。使用 BRC 类型区分及联合关系在允许未来操作下的观测保真条件，识别被错误压缩的状态。任何新原生数值操作遵守已固定的 BRC-only 路线；外部成熟公式只作为成功约束/条件定理，不冒充已完成原生推导。若现有接口不足，明确 EXTEND_EXISTING_TOOL 的字段和必要性。

冻结 ModelCapsule 版本、读出、参数域、随机性来源和允许操作。实验特定干扰参数须事先声明且有标定依据；每种现象临时新增任意余量函数不构成统一模型。依赖尚未返回时可完成前提/接口审计，不得把未定义接口写成物理预测。

本项专有前提：固定 Lüscher1998 §2列出的自由欧氏平移不变Dirac版本：动量算符解析周期、正确低动量形式、除原点外可逆、朴素γ5反对易四项不能同时满足。先建立有效3+1维手征桥，不能把六原生空间加独立时间直接代入四维γ5。其他Nielsen–Ninomiya版本另列前提，不拼接为普遍禁令。

## 2. Hard target and required outputs

第一步：先从任务09得到有效3+1维与粒子读出的对应，再从实际更新律或候选提取低能描述，逐项判定所选定理的四个前提。缺少桥则先返回缺项。

1. 固定一个原始定理版本和适用性表；若适用，输出净手征数/倍增障碍。
2. 低能模态、手征、额外模态质量与耦合的清单；若只能得到成对自由费米子，明确未完成手征相互作用。
3. 一个明确规避方案及代价：修改了什么、是否保持稳定性、可控因果和低能规范约束。
4. 规范流与异常匹配的最低一致性接口；不要求此任务一口气重建整个标准模型。

最小交付是上述第一步的真实结果、一个精确条件障碍或一份可定位的缺项；不要求先补全整个世界模型。

## 3. Research value to preserve

阻止只恢复标量波或自由Dirac方程就宣布重建真实物质。

保存推导、失败见证、模型/参数版本及准确来源范围，使另一个执行者能在不重造成功前提的情况下接续。理论不适用只结束特定定理路线；相关经验目标仍然保留。

## 4. Success, kill, and return criteria

成功须给出一项可核验的兼容预测、条件性否定、最小保真反例或准确缺项。相容判断仅限所声明协议和误差。排除判据：在全部定理前提成立时仍声称得到禁止的孤立手征谱，返回矛盾；额外未抑制模态与目标粒子谱不符则排除；未定义粒子/相互作用桥则缺项。

统一返回枚举：COMPATIBLE_WITHIN_SCOPE, EXCLUDED_WITHIN_SCOPE, MISSING_COMPONENT, THEOREM_NOT_APPLICABLE, EVIDENCE_UNRESOLVED, DERIVATION_OR_IMPLEMENTATION_ERROR。每项附假设清单、读出与参数版本、目标统计及误差、来源/未读范围、最小冲突集或缺失接口、下一项可区分检验。用新版本追踪任何修订。

已得出本项有限结论后保存并回到父目标的证据矩阵；本项终结不自动证明整个研究计划完成。正式任务定义不等于执行结果，也不授予科学结论。

## 5. Native / effective audit

declared_native_substrate: X6、独立时间、类型化分支/共同余量；不额外假定固定格速、局域更新或原生连续流形。

effective_definitions_withheld_from_native_premises: 本项外部时间、距离、相位、能量、量子算符和有效场论记号均须明确桥接。

mature_concepts_retained_for_refoundation: 一个选定的离散原生动力学能否恢复低能手征粒子与相互作用，而不产生不符合观测的额外轻粒子或规范不一致？

engineering_success_constraints_consumed: 低能粒子、散射、手征选择规则作为必须解释的外部目标。

candidate_native_mechanism_or_collapse: 先使用原生关系与更新，不以连续Dirac算符代替缺失动力学；有效描述须标明推导或假设。

bridge_or_readout_if_any: 低能粒子、散射、手征选择规则作为必须解释的外部目标。

rebuilt_tool_definition_if_any: 本任务集未宣布新工具已成立；复用观测保真。执行若需扩展，明确类型、允许操作、保真目标及与现有工具的差异。

classical_recovery_or_deviation_class_if_any: 必须返回具体协议上的恢复误差或可测偏差，不能用名称相同代替恢复证明。

successes_explained: 本次仅建立约束与任务定义，尚无已执行的原生兼容性结果。

successes_unexplained: 本任务的现象与相互依赖接口，直至实际机制预测和证据比较完成。

target_leakage_audit: 不以待解释的目标概率/公式定义所有原生对象后再声称推导；外部有限检验表只作比较输入。

weakest_justified_ontology_statement: 在所列条件下检验一个明确模型族；无法由单一结果推及全部离散或全部连续本体。

## 6. Sources and reading scope

完整来源及逐篇读取范围见 [来源表](../research_notes/DISCRETE_COMPATIBILITY_SOURCES_20261026.json)。来源链接只是允许读取入口，不代表各全文已读。

- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/p000_reality_foundation.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/foundational_logic.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/research_constraints/heartbeat_brc_only.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md
- https://github.com/awdawmip/chatgpt-global-knowledge/blob/1f73bff7ce37e663922e3c8dd29411441b0e37a7/projects/enterprise-math/NATIVE_WAVE_COMMON_RESIDUAL_CURRENT.md
- https://github.com/awdawmip/enterprise-math/blob/18d4a6d12ab7d8ab0897e9336c81ac07238fd30c/research_notes/discrete_light_objections_20261026_9c8ddfc415e7.md
- https://doi.org/10.1016/0550-3213(81)90361-8
- https://journals.aps.org/prd/abstract/10.1103/PhysRevD.25.2649
- https://arxiv.org/abs/hep-lat/9802011v1
- https://doi.org/10.1016/0550-3213(82)90011-6
