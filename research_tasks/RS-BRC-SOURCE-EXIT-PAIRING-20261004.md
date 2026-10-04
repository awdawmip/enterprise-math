<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-SOURCE-EXIT-PAIRING-20261004",
  "title": "来源—出口配对在禁配、容量及未来读出下的最小残差",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "2×2配对k区间、混合差Δ_H、边际充分条件H_ij=a_i+b_j及最坏误差半跨度已在原对话推导；P02已正式发布用于约束Cell/切片/端口映射强度，但P03尚未执行新的BRC有限域验证。",
  "next_action": "在消费P02当前正式任务边界后，固定≤3来源×3出口、总量≤6的完整有限域，明确禁配/容量与最多两种未来操作；枚举全部合法表，构造最小未来等价分类或严格反例，并保留来源—出口联合信息。",
  "dependencies": [
    "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P03",
    "https://github.com/awdawmip/enterprise-math/blob/d8601baa3f5ada7fc664f08a93c67b5901159414/research_task_records/RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004/TP2-99169E1D950AC2D48D06.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P02_CURRENT_PUBLICATION_VERIFIED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "JOINT_RELATION",
    "SOURCE_EXIT_PAIRING",
    "CAPACITY",
    "FORBIDDEN_MATCHES",
    "FUTURE_READOUT",
    "FINITE_CERTIFICATE"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-SOURCE-EXIT-PAIRING-20261004",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P03",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004",
  "successor_gate": {
    "new_information_gap": "即使P02建立或限制了Cell/切片/端口的语义映射，真实禁配与容量仍会改变来源—出口联合表的可行纤维；最多两步未来读出也未必保持可分解线性，现有2×2无约束矩形基不足以给出完整3×3有限域的合法移动与最小等价类。",
    "why_parent_result_does_not_close_it": "P02的任务范围是原生Cell身份、三维切片、端口和读出之间的最小对应桥；它不枚举来源—出口联合分配、不证明禁配/容量下的可行纤维，也不求多步未来操作下的最小充分残差。因此P02即使成功也只规定本任务可使用的映射强度。",
    "discriminating_outcomes": [
      "对固定≤3×3、总量≤6的完整合法域给出未来等价类、每类见证、跨类区分词、读出极值及必要修复坐标，并证明边际何时充分或不充分。",
      "给出严格反例：在相同边际且满足禁配/容量的合法表之间，至少一个允许的未来操作产生不同读出；或反向证明所有声明未来操作均不读取关联，从而允许安全合并。"
    ],
    "kill_condition": "若无法完整处理声明的有限合法域，则返回安全未决和缺失范围，不以部分枚举或局部极值冒充全域证书；若已证明未来操作对关联完全不敏感，则以可验证合并证书停止，不强行保留无用残差。",
    "alternative_route_or_free_exploration_considered": "可以只停留在已推导的2×2公式，或直接扩大到更高维/更大总量，但前者不足以检验真实禁配与容量，后者增加费用且不能形成最小反例。本项选择≤3×3、总量≤6的封闭有限域作为最小可穷尽扩展。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P02解决语义/映射桥，本项解决联合分配在约束与未来操作下的可识别残差，交付物是完整有限域分类与证书而非端口映射。独立成任务既消费P02边界又不扩大P02范围，并为P04及后续路径/循环任务提供经过约束的联合状态基础。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 来源—出口配对在禁配、容量及未来读出下的最小残差

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

固定一个不超过 3 个来源 × 3 个出口、总量不超过 6 的完整有限域，在明确禁配、容量约束及最多两种未来操作后，来源—出口联合配对中最少必须保留什么残差，才能保证所有允许的未来读出不丢失信息；若边际不足，最小严格反例是什么？

## Frozen inputs and scope

共同项目语义服从 P000。P02 `RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004` 已正式发布，当前 publication 为 `TP2-99169E1D950AC2D48D06`；本任务只消费其能够正式建立的 Cell / 三维切片 / 原生端口 / 读出映射强度，不预设 P02 尚未执行出的科学结论。若 P02 最终只能把某些关系保留为 `UNKNOWN` 或 `EXTERNAL_CANDIDATE`，本任务相应保持同样强度，不自行升级为原生 X6 动力学。

已冻结的数学前沿是：2×2 来源—出口配对可以用一个配对自由度 k 描述；混合差 Δ_H 检验读出是否真正读取关联；当 `H_ij=a_i+b_j` 时边际足够；在只知边际时最坏读出误差由可行 k 区间上的半跨度控制。这些属于已有对话推导，本任务不把它们重报成新成果，也尚未据此执行新的 BRC 程序验证。

私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。公开任务书只保留必要任务元数据，不公开原始附件、完整日志或私有下载地址。

## Hard target and required outputs

选择一个完整、可穷尽的有限域：来源数和出口数各不超过 3，总量不超过 6；明确每条禁配、各来源/出口容量及至多两种允许的未来操作。枚举**全部**合法联合表，不以无约束矩形基替代受约束可行移动。

在该域上构造未来等价关系：两张合法表当且仅当所有声明未来操作产生相同允许读出时才可合并。应至少交付：
- 完整输入版本、禁配/容量/操作定义和合法表总数；
- 每个等价类的代表与见证，以及跨类最短区分词或区分操作；
- 每个读出的全域极值和边际相同但联合不同的严格反例（若存在）；
- 若边际确实充分，给出覆盖整个声明有限域的证明/证书，而非抽样；
- 若需要修复坐标，给出最小附加联合坐标并说明其来源意义；
- 若实际执行代码或证书，分列域构造、可行性/观察调用、证书、存储与输出费用，并保留原始回执；未执行项单列。

证明范围与有限执行必须分开。不得把边际重构写成联合重构，也不得把 P02 的语义映射自动当作本任务的联合分类结果。

## Research value to preserve

来源总量和出口总量可以完全相同，而具体来源—出口配对仍影响后续受约束传播、容量占用或读出。2×2 已给出这种残差的最小原型，但真实禁配/容量会改变可行纤维，多步未来操作也可能破坏简单线性可分解条件。一个完整的 ≤3×3、总量≤6 证书可以判断何时可以安全压缩到边际、何时必须保留配对残差，并为后续循环通量、路径顺序、入口状态与干预可识别性任务提供合法联合状态，而不是依赖无约束直觉。

## Success, kill, and return criteria

成功：声明有限域被完整处理；每个合法表进入且只进入一个未来等价类；每类有可回放见证，跨类有区分操作/词；所有读出极值来自完整合法域；任何必要修复坐标均有明确定义。已有 2×2 结果只作边界检查，不重复计为新执行。

停止/否定：若所有声明未来操作均已证明不读取来源—出口关联，则允许合并并以全域证书结束；若受约束可行域不能完整枚举、验证或证明，则返回安全未决与精确缺失范围，不报告部分极值为全局结论。不得为得到“非零残差”而增加未授权未来操作或扩大模型。

本任务结束于该有限域分类/反例或明确安全未决；不自动进入 P04 的循环通量与入口状态研究。
