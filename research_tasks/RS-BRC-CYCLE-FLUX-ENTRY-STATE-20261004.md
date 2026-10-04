<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-CYCLE-FLUX-ENTRY-STATE-20261004",
  "title": "循环通量、路径顺序及入口状态的联合闭合证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已证明净变化不能识别循环核、生成森林加弦通量可恢复累计边流，累计通量相同仍可能入口状态不同；P02已正式发布用于约束Cell/切片/端口映射强度，但尚未给出真实允许的端口重标记/来源保留规则下，累计环计数加有限入口状态何时足够迭代。",
  "next_action": "在消费P02当前正式任务边界后，固定≤6 Cell、≤8有向连接的完整窗口，逐来源定义边流、入口更新和两种合法回路；先构造整数守恒与容量可行域，再求能组合的最小当前状态，若不闭合则给出最短顺序反例。",
  "dependencies": [
    "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P04",
    "private-evidence:CONVERSATION_FRONTIER.md",
    "private-evidence:evidence/residual_deferred_collision_R1/PROOF.md",
    "https://github.com/awdawmip/enterprise-math/blob/b6ad9074f8348ff4cd15832d8f6c7b3300c048f1/research_task_records/RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004/TP2-99169E1D950AC2D48D06.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P02_CURRENT_PUBLICATION_VERIFIED; PRIOR_CYCLE_AND_ORDER_RESULTS_CONSUMED_AT_DECLARED_STRENGTH; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "CYCLE_FLUX",
    "PATH_ORDER",
    "ENTRY_STATE",
    "JOINT_CLOSURE",
    "INTEGER_CONSERVATION",
    "FINITE_CERTIFICATE"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-CYCLE-FLUX-ENTRY-STATE-20261004",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P04",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004",
  "successor_gate": {
    "new_information_gap": "净变化只给边流的边界，累计环计数虽能恢复累计边流，但在累计通量相同的状态之间，入口状态与路径顺序仍可能决定后续更新。尚未给出在P02允许的端口重标记和来源保留强度下，什么有限入口状态足以与环通量组成可迭代闭合状态。",
    "why_parent_result_does_not_close_it": "P02只负责Cell身份、三维切片、原生端口和读出的最小语义桥；它不证明循环核的闭合坐标，不处理累计通量相同而入口状态不同的未来分叉，也不判定路径顺序何时可以安全删除。因此即使P02成功，本任务的动态联合闭合问题仍然开放。",
    "discriminating_outcomes": [
      "在固定≤6 Cell、≤8有向连接窗口内，给出逐来源边流、弦边循环通量、有限入口状态组成的可组合当前状态，并证明所有声明更新在该状态上闭合。",
      "给出最短严格反例：两个整数守恒、容量可行、累计边流/环通量相同的合法历史，在同一允许后续操作下因入口状态或顺序不同产生不同未来；据此证明必须保留额外入口坐标或必要顺序。"
    ],
    "kill_condition": "若最低入口状态仍不闭合，则保留被反例证明必要的顺序或入口残差，不得把结论扩大为所有历史都不可压缩；若完整有限域证明环通量加有限入口状态已闭合，则以该证书停止，不增加无关历史字段。",
    "alternative_route_or_free_exploration_considered": "可以只保存全部历史、只保存净变化，或重做已完成的三环矩阵证明；前两者分别过度保留或已知不足，后者重复旧成果。本项选择≤6 Cell、≤8连接和两种合法回路，直接检验最小可组合状态。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P02是语义映射桥，本项是动态闭合证书；所需交付物是循环核、入口更新、路径顺序的有限状态证明或反例。独立成任务可消费P02提供的映射强度，同时保持已完成循环/延迟碰撞结果不被重跑，并为P06等安全状态压缩任务提供明确边界。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 循环通量、路径顺序及入口状态的联合闭合证书

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

对一个不超过 6 个 Cell、8 条有向连接的完整有限窗口，逐来源定义边流、入口更新及两种合法回路后，累计循环通量加多少入口状态才足以形成可组合、可迭代的当前状态；若仍不足，最短必须保留路径顺序的严格反例是什么？

## Frozen inputs and scope

共同项目语义服从 P000。P02 `RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004` 已正式发布，当前 publication 为 `TP2-99169E1D950AC2D48D06`；本任务只消费其能够正式建立的 Cell / 三维切片 / 原生端口 / 读出映射强度。若 P02 对某些映射最终只允许 `UNKNOWN` 或 `EXTERNAL_CANDIDATE`，本任务保持同样强度，不自行升级为原生 X6 动力学。

已冻结前沿包括：净变化不能识别循环核；生成森林加弦通量可以恢复累计边流；累计通量相同仍可能入口状态不同；先前延迟碰撞条件模型还给出“多个事件一般不能任意换序、漏掉的下游因果相遇也要修正”的有界见证。上述均作为已完成输入消费，不重复运行，不把条件模型提升为唯一真实力学。

私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。公开任务书只保留必要任务元数据，不公开原始附件、完整日志或私有下载地址。

## Hard target and required outputs

固定一个完整有限域：不超过 6 个 Cell、8 条有向连接；逐来源记录非负整数边流，明确每条容量、共同 Cell 去重、操作区间的左右端点语义及至少两种合法回路。选择一个生成森林并用弦边表示循环核，但不得重复已完成的三环矩阵证明。

在该域上定义候选当前状态，例如“边界/累计流 + 独立环通量 + 有限入口状态”，然后逐项检查声明更新能否仅由当前状态组合计算。至少交付：
- 完整输入版本、连接表、来源标签、容量与两种回路定义；
- 整数守恒与容量可行证书，禁止负质量解释；
- 循环核坐标、树重建和共同 Cell 去重的可回放证明；
- 所选最低入口状态的精确定义以及每种允许更新后的状态转移；
- 若闭合，给出覆盖完整声明有限域的未来等价证书；
- 若不闭合，给出累计边流/环通量相同但未来不同的最短入口状态或顺序反例，并只保留反例证明必要的信息；
- 若实际执行代码或证书，分列端口/来源获取、弦边传感、树重建、顺序更新、存储与输出费用，并保留原始回执；未执行项单列。

证明范围和有限执行必须分开。不得因存在一个顺序反例就宣称所有历史不可压缩，也不得把累计通量恢复边流误写成它同时恢复入口状态或事件顺序。

## Research value to preserve

边界净变化会把循环核完全隐藏，而累计循环通量虽然能补回累计边流，却仍可能丢掉决定下一步的入口状态与路径顺序。若不知道哪一部分顺序真正必要，状态压缩会在未来更新时产生不可检测的分叉；反过来，保存全部历史又失去有限状态计算的价值。一个完整的 ≤6 Cell、≤8连接闭合证书或最短反例，可以把“累计通量、入口状态、必要顺序”分型，并为后续受限操作语言下的安全状态压缩提供可证明边界。

## Success, kill, and return criteria

成功：整数守恒、容量可行、循环核证书和未来区分见证全部可重放；共同 Cell 不重复计量；逐来源信息不被边际替代；候选入口状态在完整有限域中闭合，或其失败由最短反例精确定位。已完成的循环矩阵/延迟碰撞结果仅作边界检查，不重复计为新执行。

停止/否定：若最低入口状态仍不闭合，则保留反例证明必要的入口残差或顺序，不宣布所有历史不可压缩；若环通量加有限入口状态已对完整声明域闭合，则以证书停止，不增加无用历史字段。

本任务结束于该闭合证书、最短反例或明确安全未决；不自动进入 P05/P06 的干预或通用状态压缩研究。
