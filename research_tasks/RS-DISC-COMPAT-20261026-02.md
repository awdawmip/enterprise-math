<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DISC-COMPAT-20261026-02",
  "title": "公共余量的 Bell/CHSH 关联与禁止可控超光速信号",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "同一公共余量机制能否同时产生违反 CHSH 的有限设置关联和操作性无信号边缘分布？",
  "next_action": "先检查拟用公共余量是否仍满足该分解；若满足，以四个±1响应和正权重给出有限设置上界，而后才设计非局域候选。",
  "dependencies": [
    "RS-DISC-COMPAT-20261026-00"
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
    "https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195",
    "https://arxiv.org/abs/1508.05949v1",
    "https://arxiv.org/abs/1511.03189v2"
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
  "registry_key": "RS-DISC-COMPAT-20261026-02",
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

# RS-DISC-COMPAT-20261026-02 — 公共余量的 Bell/CHSH 关联与禁止可控超光速信号

## 0. Mother question

同一公共余量机制能否同时产生违反 CHSH 的有限设置关联和操作性无信号边缘分布？

父目标：OBJ-DISCRETE-EMPIRICAL-COMPATIBILITY-20261026。本项来自用户直接提出的反证与经验兼容性方向；集合内建议执行组为A，全局排序仍由已登记的默认级别决定。任务依赖：RS-DISC-COMPAT-20261026-00。

## 1. Frozen inputs and scope

原生基线是 X6 六空间轴及独立定型时间，原生120度关系不等同普通平面角。波允许非邻接/全域自洽机制；不得追加固定物理拍长或每拍一格。激活、正分支质量、相位、能量及共同余量分开定型。三维、仪器、物质和时间/能量标定属于待解释的读出层。

用户本次要求主动寻找不兼容及缺项。固定基线用于定位失败，不授予基线免于证据的地位。此任务不直接改写保护文件；应如实返回具体假设组合或桥的失败。

现有工具复用状态：REUSE_APPLIED。使用 BRC 类型区分及联合关系在允许未来操作下的观测保真条件，识别被错误压缩的状态。任何新原生数值操作遵守已固定的 BRC-only 路线；外部成熟公式只作为成功约束/条件定理，不冒充已完成原生推导。若现有接口不足，明确 EXTEND_EXISTING_TOOL 的字段和必要性。

冻结 ModelCapsule 版本、读出、参数域、随机性来源和允许操作。实验特定干扰参数须事先声明且有标定依据；每种现象临时新增任意余量函数不构成统一模型。依赖尚未返回时可完成前提/接口审计，不得把未定义接口写成物理预测。

本项专有前提：Bell 局域分解 P(a,b|x,y)=sum_lambda rho(lambda)P(a|x,lambda)P(b|y,lambda)，另需设置与 lambda 的适当统计独立。允许任意复杂或任意多共享隐藏状态，也不能在保留这些条件时突破 CHSH≤2。全域更新已使局域分解不能自动假定。

## 2. Hard target and required outputs

第一步：先检查拟用公共余量是否仍满足该分解；若满足，以四个±1响应和正权重给出有限设置上界，而后才设计非局域候选。

1. 固定四种设置、±1输出、归一化联合分布及 CHSH 约定。
2. 一个局域分解适用性判定：成立则直接输出条件性不可行证明；不成立则指出实际违反的是哪项前提。
3. 把 P_op(a,b|x,y) 明确定义为实际可实现受控设置协议下的操作分布，检验其本地边缘对远端可控设置不变；如使用因果干预记号，列出允许的干预及其物理实现。另行区分被动条件分布 P(a,b|x,y) 和干预分布；放宽设置独立性时不得从条件相关直接推出可控传讯。说明有限样本误差或严格界。
4. 至少对一个已核验无主要漏洞实验的统计量和实验流程给出原生机制预测；保留选择、损失、时间窗和设置生成的条件。

有限基准：x,y∈{0,1}，a,b∈{−1,+1}。16个确定性局域响应四元组对每个隐藏状态均有 C=a0(b0+b1)+a1(b0−b1)∈{−2,+2}。在设置独立、非负归一化权重及条件局域分解下，故 |S|≤2；随机局域响应也不能突破。目标侧对照表 P(a,b|x,y)=[1+ab(−1)^(xy)/√2]/4 给出 S=2√2 和均匀单边缘。它是外部检验输入，直接抄入并不构成原生解释。

## 3. Research value to preserve

用有限实验即可决定正权重共享随机性是否足够，并约束放宽局域性后的真实成本。

保存推导、失败见证、模型/参数版本及准确来源范围，使另一个执行者能在不重造成功前提的情况下接续。理论不适用只结束特定定理路线；相关经验目标仍然保留。

## 4. Success, kill, and return criteria

成功须给出一项可核验的兼容预测、条件性否定、最小保真反例或准确缺项。相容判断仅限所声明协议和误差。排除判据：CHSH始终≤2的模型不能恢复相关实验；能达到大相关但允许远端可控改变本地边缘分布且无实验容许机制者排除；只贴上共享余量标签或直接抄入量子概率表者缺项。

统一返回枚举：COMPATIBLE_WITHIN_SCOPE, EXCLUDED_WITHIN_SCOPE, MISSING_COMPONENT, THEOREM_NOT_APPLICABLE, EVIDENCE_UNRESOLVED, DERIVATION_OR_IMPLEMENTATION_ERROR。每项附假设清单、读出与参数版本、目标统计及误差、来源/未读范围、最小冲突集或缺失接口、下一项可区分检验。用新版本追踪任何修订。

已得出本项有限结论后保存并回到父目标的证据矩阵；本项终结不自动证明整个研究计划完成。正式任务定义不等于执行结果，也不授予科学结论。

## 5. Native / effective audit

declared_native_substrate: X6、独立时间、类型化分支/共同余量；不额外假定固定格速、局域更新或原生连续流形。

effective_definitions_withheld_from_native_premises: 本项外部时间、距离、相位、能量、量子算符和有效场论记号均须明确桥接。

mature_concepts_retained_for_refoundation: 同一公共余量机制能否同时产生违反 CHSH 的有限设置关联和操作性无信号边缘分布？

engineering_success_constraints_consumed: 设置是可操控输入；输出是实际探测记录。明确源、装置、环境和余量的联合分布。

candidate_native_mechanism_or_collapse: 复用 BRC 正权重联合分支及观测保真；若需非局域更新，明确可操控部分与不可操控关联的差别。

bridge_or_readout_if_any: 设置是可操控输入；输出是实际探测记录。明确源、装置、环境和余量的联合分布。

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
- https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195
- https://arxiv.org/abs/1508.05949v1
- https://arxiv.org/abs/1511.03189v2
