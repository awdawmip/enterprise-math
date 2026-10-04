<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-INTERVENTION-SINGLE-TRACE-IDENTIFIABILITY-20261004",
  "title": "层间干预与单条连续观察记录的可识别性",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "三Cell门控差分与隐藏寄存器行为等价反例、五Cell实例的1,0,1三步数量重建及两步最坏失败已完成符号推导；P02/P03已正式发布用于约束原生映射强度和来源—出口联合残差，但P05尚未执行单条无重置记录下的来源配对可识别性证书。",
  "next_action": "消费P02/P03当前正式任务边界后，冻结已有五Cell实例、同一无重置干预语义和一个来源敏感读出；将每次读数写成给定有理区间，枚举全部合法初态/当前态与来源配对，输出整条记录一致的精确可行状态集合，并给出最短区分或不可识别见证。",
  "dependencies": [
    "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004",
    "RS-BRC-SOURCE-EXIT-PAIRING-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P05",
    "private-evidence:CONVERSATION_FRONTIER.md",
    "https://github.com/awdawmip/enterprise-math/blob/dc172bf5c36d37ca90b1c340c09754d6655183de/research_task_records/RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004/TP2-99169E1D950AC2D48D06.json",
    "https://github.com/awdawmip/enterprise-math/blob/dc172bf5c36d37ca90b1c340c09754d6655183de/research_task_records/RS-BRC-SOURCE-EXIT-PAIRING-20261004/TP2-DCA5A080B5E0D5135648.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P02_P03_CURRENT_PUBLICATIONS_VERIFIED; PRIOR_GATED_AND_ONE_TRACE_SYMBOLIC_RESULTS_CONSUMED_AT_DECLARED_STRENGTH; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "INTERVENTION",
    "SINGLE_TRACE",
    "IDENTIFIABILITY",
    "SOURCE_PAIRING",
    "RATIONAL_INTERVAL",
    "EXACT_FEASIBLE_SET",
    "NO_RESET"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-INTERVENTION-SINGLE-TRACE-IDENTIFIABILITY-20261004",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P05",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-SOURCE-EXIT-PAIRING-20261004",
  "successor_gate": {
    "new_information_gap": "P03定义来源—出口联合配对在禁配、容量和未来读出下需要保留的残差，但并未回答在固定五Cell实例中，允许的主动干预与单条无重置连续记录是否足以识别这些来源配对。已有数量重建不恢复来源，隐藏寄存器又可模拟部分输入输出，因此主动可识别性仍开放。",
    "why_parent_result_does_not_close_it": "P03处理的是联合分配的有限域未来等价分类；它不固定干预序列、不研究一条连续记录的前缀区分能力，也不处理有理读数区间下的精确后验可行集。P02只提供可使用的Cell/切片/端口映射强度，也不能替代本任务的干预可识别性证明。",
    "discriminating_outcomes": [
      "对已有五Cell实例及固定干预/读出语义，完整枚举所有合法状态后，给出每条允许观测记录对应的精确可行状态集合；对可识别配对给出最短区分前缀，对不可识别配对给出同路径同干预下的严格不可区分见证。",
      "给出隐藏寄存器或行为等价严格反例：不同来源配对在所有声明干预与有理误差区间内产生相同记录，从而只能识别行为等价类而不能识别原生层间位置。"
    ],
    "kill_condition": "若新增读出无法在P02/P03允许强度下绑定来源语义，或给定误差区间使多个合法状态始终不可分，则返回精确可行集与不可识别类并停止；不得以拟合、点估计、重置实验或补造隐藏状态宣告来源已识别。",
    "alternative_route_or_free_exploration_considered": "可改用多条独立轨迹、每步重置、直接读取完整隐藏状态或增加多个传感器，但这些都会绕开“同一条无重置观察路径+一个新增来源敏感读出”的原问题。本项坚持该最小干预窗口，以得到可证的识别边界。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P03确定联合来源配对残差本身的必要性，本项研究主动观测是否能从单条连续记录恢复该残差，交付物是精确后验集合、最短区分前缀或不可识别反例。独立成任务既消费P02/P03边界又不扩大其范围，并为后续安全状态压缩与干预设计提供明确可识别性接口。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 层间干预与单条连续观察记录的可识别性

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

在已有五 Cell 实例上，只增加一个来源敏感读出，并沿同一条**无重置**连续观察路径施加既定干预；每次读数只知道一个给定有理区间时，究竟能恢复哪些来源配对、初态或当前态？对不能唯一恢复的情形，精确可行状态集合和最短不可识别反例是什么？

## Frozen inputs and scope

共同项目语义服从 P000。P02 `RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004` 与 P03 `RS-BRC-SOURCE-EXIT-PAIRING-20261004` 已正式发布；本任务只消费它们正式允许的 Cell / 三维切片 / 端口映射强度，以及来源—出口联合残差的定义强度，不预设它们尚未执行出的科学结论。任何仍为 `UNKNOWN` 或 `EXTERNAL_CANDIDATE` 的映射继续保持该强度。

已冻结的前沿是：三 Cell 门控差分和隐藏寄存器行为等价反例已经完成；已有五 Cell 模型在既定 `1,0,1` 三步干预下可以重建数量，而两步存在最坏失败；这些符号结果不等于来源配对已经可识别。本任务不重复上述推导，而是在同一五 Cell 实例上增加一个来源敏感读出，研究单条不重置记录能否消除来源歧义。

私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。公开任务书只保留必要任务元数据，不公开原始附件、完整日志或私有下载地址。

## Hard target and required outputs

冻结已有五 Cell 状态空间、既定干预语义和一条无重置连续记录。新增读出必须明确说明它在 P02/P03 允许强度下如何依赖来源；若只能作为外部候选读出，则按该强度研究，不提升为原生 X6 传感器。

每个时刻的实际读数写成有理端点区间 `[l_t,u_t]`，不以中心值或拟合值替代。对完整合法状态域，定义“与整条干预—读出记录一致”的精确可行集合。至少交付：
- 完整输入版本、五 Cell 状态定义、干预序列、读出函数及每个有理误差区间；
- 明确重建目标是初态、当前态、来源配对或它们的组合；若同时研究多个目标，分别给出映射和等价类；
- 覆盖全部合法状态的记录等价分类，不只抽样；
- 对能识别的状态/配对给出最短区分前缀或最短干预—读出见证；
- 对不能识别的状态/配对给出同一路径、同干预、同误差区间下的严格不可区分对，必要时给隐藏寄存器模拟见证；
- 用已有 `1,0,1` 三步数量重建作为冗余一致性检查，但不把数量一致性冒充来源一致性；
- 若实际执行代码或证书，分列路由/干预次数、真实读数取得、可行集合计算、证书、来源存储与输出费用，并保留原始回执；未执行项单列。

输出必须是精确有限集合、等价类或有证明的区间/约束描述；不得用单点估计补造未被记录区分的隐藏状态。

## Research value to preserve

被动边际、数量或总读出可以恢复“有多少”，却可能无法恢复“来自哪里”。主动干预若设计得当，可能把来源配对差异转成时间上的可观察差异；但同一路径不重置时，隐藏寄存器也可能吸收这些差异，从而产生行为等价。把每次读数保留为有理区间并计算完整可行状态集合，可以精确区分“唯一识别”“只识别到等价类”和“完全不可识别”，为后续压缩、控制和传感设计提供不依赖点估计的边界。

## Success, kill, and return criteria

成功：同一路径、同干预语义覆盖全部合法状态；初态/当前态/来源配对的重建目标被明确区分；每条记录对应的可行集合可回放；可识别者有最短区分见证，不可识别者有严格等价反例；已有三步数量重建只作一致性检查，不重复计为新执行。

停止/否定：若隐藏寄存器能够在声明干预和读出下模拟不同来源配对，则只报告行为等价类，不宣称恢复原生层间位置；若来源敏感读出无法合法绑定，或误差区间使所有候选保持不可分，则返回完整可行集合和缺失来源边界，不用拟合或增加未授权传感器修补。

费用分别记录路由/干预次数、真实读数取得、精确后验集合计算、证书/来源存储与输出。任务结束于该识别证书、不可识别反例或明确安全未决；不自动进入 P06 的通用状态压缩研究。
