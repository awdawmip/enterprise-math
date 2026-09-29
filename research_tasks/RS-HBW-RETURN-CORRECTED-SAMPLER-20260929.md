<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HBW-RETURN-CORRECTED-SAMPLER-20260929",
  "title": "快基线加返回修正的有效采样器",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "快基线P0与有符号Delta尚未组成合法、可计价的修正采样器。",
  "next_action": "依赖返回项契约成立后，先证明正概率采样律与同阈值细化规则。",
  "dependencies": [
    "RS-HBW-RETURN-INTERFERENCE-CERTIFICATE-20260929"
  ],
  "source_refs": [
    "research_notes/heartbeat_outward/20260929_9F026E_PUBLICATION/SOURCE_FRONTIER.md",
    "research_notes/heartbeat_outward/20260929_9F026E_PUBLICATION/SOURCE_MANIFEST.json"
  ],
  "evidence_status": "CANDIDATE_SOURCE_REQUIRES_INDEPENDENT_SCOPE_CHECK",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "registry_key": "RS-HBW-RETURN-CORRECTED-SAMPLER-20260929",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_lane": "HBW-RETURN-9F026E",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HBW-RETURN-INTERFERENCE-CERTIFICATE-20260929",
  "successor_gate": {
    "new_information_gap": "快基线P0与有符号Delta尚未组成合法、可计价的修正采样器。",
    "why_parent_result_does_not_close_it": "误差上界或有符号区间不自动给出正性、终止性和完整抽样分布。",
    "discriminating_outcomes": [
      "有效精确或epsilon受控采样器及全分布证书",
      "特定修正策略的正性/代价失败见证"
    ],
    "kill_condition": "将有符号Delta当正混合，丢弃困难阈值，或隐藏校正预处理。",
    "alternative_route_or_free_exploration_considered": "与精确整数质量树、继续精确事件查询或仅返回认证估计量比较；不强行宣称采样。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "证书接口完成之后仍有独立的概率实现与复杂度问题，需要单独验收而不扩大上游任务。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 快基线加返回修正的有效采样器

## Mother question

给定已核验P0采样器和有界返回项接口，怎样得到原P_N的精确样本或总变差不超过明确epsilon的样本，同时保持实际总成本可核验？

## Frozen inputs and scope

模型及全部原始证据按source_refs固定；源包内THEOREMS.md第1至6节给出定义和候选证明。D=2J-3I，Q=9^T，只有端口1执行a^(2^t)模乘。P0是记录分开分布；Delta(b)为工作相同、记录不同的有序交叉项之和，P_N=P0+Delta/Q。P0的64拍低活跃宽度不意味着原P_N普遍可被精确采样。保持完整可见键、工作相等条件以及同记录内0/2相干。运算入口沿已绑定signed-CWM源码；新增能力须声明对应及代价，不用普通算术改名补证。本任务不研究原生本构推导或直接宣称Shor输出等价。
依赖RS-HBW-RETURN-INTERFERENCE-CERTIFICATE-20260929产出的适用证书/查询，并继承RS-HBW-RECORD-INTERFACE-AUDIT-20260929的有效接口范围。如果前者只有否定结论，不假定修正查询器已存在；应返回可行性缺口或改用已认证的明确替代路线。

## Hard target and required outputs

第一单元：写出所采用的正概率抽样律、归一化依据和每次判定的合法区间；Delta不能直接当凸混合分量。
构造精确修正、保持同一阈值的区间细化，或具有显式TV及失败概率预算的近似采样。必须证明P_N相对于P0的支持关系，特别检查P0(b)=0是否强迫P_N(b)=0，并处理消相干误差、稀有前缀、细化停止和总期望成本。任何额外假设须入契约并可检查。
最小验收用N21/35,T6的非零返回例，外加N77/T6零例；全小实例核对输出映射或整数质量分配，而非只看少量随机频率。保留0/2相干64对32及先前80对16、32/243安全范围。
与P0、已有精确事件/整数质量树比较同输入同样本目标的准备、校正、重试、RNG、缓存和验证成本。禁止读取完整终态答案表作为生产输入；若只在受限族有效，明确给出族和证书费用。

## Research value to preserve

把返回干涉公式变成真正可执行、可证误差的抽样，而不是停在带符号估计量；检验粗精结合是否实际优于精确计算。

## Success, kill, and return criteria

成功：完整抽样律证明、有限全分布证书和分项成本，或对指定修正策略给出严格失败/成本反例。不要丢弃难判定阈值后重抽以制造速度；不要把负权修正直接作为概率。
如果只能产生无偏有符号估计而不能产生合法样本，明确返回该差距。最终结果限定于原候选三端口模型，不推广为一般Shor加速或原生物理发现。
