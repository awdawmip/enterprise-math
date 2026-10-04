<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004",
  "title": "三维切片重叠、全局晶胞身份与原生端口的最小对应桥",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "全局已采用六原生轴、三维切片且无原生平面；现有RS-BRC-BASELINE-RESIDUAL-20261002有界复盘已完成，但近期关系图仍是候选，尚无实际X6三维切片选择、重叠Cell身份及原生邻接/端口绑定。",
  "next_action": "先消费父任务已完成材料的最小必要窗口，建立Cell身份、切片选择、第三分量语义、邻接/端口和读出的来源表；无法绑定的字段保持UNKNOWN并给出精确缺口。",
  "dependencies": [],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "https://github.com/awdawmip/enterprise-math/blob/dfb768b45753e43847cc06199173b9ad3b00e22e/research_task_records/RS-BRC-BASELINE-RESIDUAL-20261002/TP2-20E37C57649A74D4E563.json",
    "https://github.com/awdawmip/enterprise-math/blob/dfb768b45753e43847cc06199173b9ad3b00e22e/research_objective_heads/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; BASELINE_TASK_CURRENT_HEAD_VERIFIED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION; GENERATION_2_CORRECTS_MALFORMED_RECORD_BYTES_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "X6",
    "THREE_DIMENSIONAL_SLICE",
    "CELL_IDENTITY",
    "NATIVE_PORTS",
    "MAPPING"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P02",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "successor_gate": {
    "new_information_gap": "现有完整X6残差复盘与近期候选图模型都没有给出三维切片选择、全局Cell身份、重叠Cell去重、第三分量语义以及原生邻接/端口/读出的逐项绑定。",
    "why_parent_result_does_not_close_it": "父任务已完成有界隐藏残差/X6复盘，但其结论不提供三维切片嵌入或端口对应；两个读出向量、低维图节点和候选传导关系都不能据此自动升级为原生切片或原生动力学。",
    "discriminating_outcomes": [
      "建立来源可核验的Cell身份—切片选择—三分量—邻接/端口—读出映射，并证明共同Cell不重复计量、遗漏第三分量不默认补0。",
      "无法建立合法映射时，精确列出缺失证据并将模型保持为外部受控关系模型，不宣称原生X6动力学。"
    ],
    "kill_condition": "若当前可得原生输入不足以逐端口绑定来源，立即返回有边界缺口；不得通过重跑父任务、启动Octave/X6 pilot、补零第三分量或命名重标来制造原生映射。",
    "alternative_route_or_free_exploration_considered": "允许把现有关系图保留为明确标注的外部候选模型并继续条件命题；不以重启已完成baseline、扩大无关X6实验或泛化自由探索代替本项有限映射检查。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "父任务的有界X6残差复盘已经完成；本项需要不同的语义/结构交付物和明确停止条件。独立成任务可以消费父成果而不篡改其终局边界，也能让后续P03/P04等只依赖已核验的映射强度。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 三维切片重叠、全局晶胞身份与原生端口的最小对应桥

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

Publication correction: 本 generation 仅修复首个不可变 publication record 的字段字节错误；科学任务范围、父任务、父目标与停止条件均不变。

## Mother question

在不重启已完成的 `RS-BRC-BASELINE-RESIDUAL-20261002` 实验的前提下，能否给出全局 Cell 身份、三维切片选择、三分量语义、邻接/端口及读出的最小可验证对应；如果不能，精确返回缺失的原生证据。

## Frozen inputs and scope

心跳世界空间按 P000 保持为六原生轴离散 X6；当前研究对象是其中一层三维切片，不存在原生二维平面。两个坐标或两个读出分量不能决定切片维数，遗漏第三分量不得默认补 0。共同 Cell 的重叠读出按同一身份去重，不同 Cell 间传播、端口与邻接必须另行绑定来源。

父任务 `RS-BRC-BASELINE-RESIDUAL-20261002` 的有界 X6/隐藏残差复盘作为已完成输入消费，不重跑。有限图、几格运输模型和低维读出保持候选/外部关系强度，除非取得来源可核验的原生映射。私有源包只作为授权恢复入口；公开任务书不公开原始附件、完整日志或私有下载地址。

## Hard target and required outputs

形成 `Cell identity -> slice selection/embedding -> third-coordinate semantics -> native adjacency/port -> readout` 对应表。每项给出真实来源与允许操作范围；不能验证者标记 `UNKNOWN` 或 `EXTERNAL_CANDIDATE`。至少交付输入版本和父任务/目标绑定、逐端口来源和 Cell 去重规则、三维切片三分量定义或未知边界、有限命题/反例或最小缺口，以及实际执行时的来源读取/构表/核验/原生输入取得费用。不得用命名、重标号、补零或重跑父实验填补。

## Research value to preserve

后续来源—出口配对、循环通量、单路径可识别性和联合参考/原生残差对应都依赖“同一 Cell、三维切片、原生端口”的严格含义。该桥可以防止低维读出或候选图被误升格为完整原生动力学；即使只得到有边界缺失证据，也能约束后续证明强度。

## Success, kill, and return criteria

成功要求逐端口来源可核验、共同 Cell 不重复计量、第三分量不默认补 0，并且切片选择/嵌入、邻接/端口、读出和允许操作范围均可回放。若无法建立合法映射，返回缺失字段、冲突来源和可安全使用的外部候选强度并停止；不得靠重跑父任务、Octave/X6 pilot、命名重标或补零升级结论。完成最小桥或确认不可建立后即结束，不自动扩展为更广 X6 实验、性能优化或物理归因。
