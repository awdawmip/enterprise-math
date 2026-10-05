<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-BRC-RATIONAL-CELL-SET-MERGE-CERTIFICATE-20261005",
  "title": "有理晶胞集合更新与近似合并证书的实现边界",
  "frontier": "h=1..3全部商类、代表和半开边界证书已完成；一般多边形集合更新、同历史匹配近似合并和有限代表数量界只有已保存推导。P01已正式发布用于固定相关材料版本。",
  "next_action": "只选择两个已有有理多边形及h≤3的新集合级证书，完整处理半开0/1/2维边界和同label分支；T使用ell_(2h)，预算按A保范/T衰减传播，验证固定历史同一见证与UNSURE返回，不重跑既有7750轨迹。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P19",
    "private-evidence:rational_cell_continuation/BRANCH_AND_MERGE_PROOFS_20261002.md",
    "private-evidence:rational_cell_continuation/APPROXIMATE_MERGE_AND_FINITE_TRACE_COVER_20261002.md",
    "private-evidence:rational_cell_continuation/APPROXIMATE_MERGE_CERTIFICATE_SPEC_20261002.json",
    "private-evidence:EM_S15SUPPORT_RATIONAL_CELL_CERTIFICATE_20261001.json",
    "https://github.com/awdawmip/enterprise-math/blob/dd9b44fafe3e6a02c5c6c8ba825e1f130a05bfe5/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P01_CURRENT_PUBLICATION_VERIFIED; PRIOR_COMPLETED_UNITS_CONSUMED_WITHOUT_REPLAY; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "RATIONAL_CELL",
    "SET_UPDATE",
    "APPROXIMATE_MERGE",
    "HALF_OPEN_BOUNDARY",
    "FIXED_HISTORY",
    "UNSURE"
  ],
  "registry_key": "RS-BRC-RATIONAL-CELL-SET-MERGE-CERTIFICATE-20261005",
  "identity_lane": "P19",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "精确并集与凸包/近似代表实现尚未核对完整半开0/1/2维边界和同一见证整段历史；值域误差也不能代替Q一致性。",
    "why_parent_result_does_not_close_it": "P01只固定证据版本归属；已完成h=1..3商类/代表/半开边界证书不覆盖一般多边形集合更新、同历史匹配近似合并或有限代表实现边界。",
    "discriminating_outcomes": [
      "在两个已有有理多边形和h≤3范围内，给出严格/非严格边界、代表无关、固定历史同一见证、伪路径反例、UNSURE返回和来源关联的可回放集合级证书。",
      "若有限代表或近似合并不能维持同一历史见证/Q一致性，则给出最小反例并限制在外部低维辅助表示，不提升为原生三维切片状态。"
    ],
    "kill_condition": "禁止重跑既有7750轨迹；不得把低维公式因改名升级为原生三维切片，不得默认遗漏第三坐标为0，也不得把有限代表数视为固定有限自治精确状态。",
    "alternative_route_or_free_exploration_considered": "可以重跑轨迹或扩大到一般高维集合，但会重复已完成执行并模糊当前实现边界。本项只做两个已有有理多边形、h≤3的最小集合级证书。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "已有h≤3单元证书完成；本项增加集合并集、覆盖与近似合并的实现和同历史见证要求，是新的集合层问题。"
  }
}
-->

# 有理晶胞集合更新与近似合并证书的实现边界
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
在已有有理晶胞证书上，只取两个已有有理多边形和 `h≤3`，能否实现精确集合更新和近似合并，同时完整处理半开 0/1/2 维边界，并保证整段固定历史使用同一见证？

## Frozen inputs and scope
共同项目语义服从 P000。这里的有理多边形、0/1/2 维边界与两坐标公式是外部/部分辅助表示，**不是原生二维平面，也不是完整三维切片**；遗漏第三坐标不得默认补 0。任何向原生三维切片转移都必须另行给出切片选择、第三坐标语义、读出和关系保持。
P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只固定证据版本和归属。冻结前沿：`h=1..3` 全部商类、代表和半开边界证书已完成；一般多边形集合更新、同历史匹配近似合并和有限代表数量界只有已保存推导。既有 7750 轨迹不重跑。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
只选两个已有有理多边形及 `h≤3` 的新集合级证书。完整处理半开 0/1/2 维边界和同 label 分支；`T` 使用 `ell_(2h)`，预算按 A 保范/T 衰减传播。
交付严格/非严格边界、代表无关、伪路径反例、固定历史同一见证、`UNSURE` 返回和所有来源关联。值域误差不得冒充 Q 一致。边界构造、集合可行性、并集/覆盖、代表点、证书、位长和输出存储全部计费。

## Research value to preserve
单晶胞和短历史证书已经存在，真正缺口在集合运算与近似合并是否会破坏半开边界和同一历史见证。该任务给出可实现边界，而不是把低维辅助表示重命名成原生空间。

## Success, kill, and return criteria
成功：集合级证书覆盖声明的半开边界、固定历史见证和 `UNSURE` 分支，且代表选择无关。
停止/否定：发现伪路径或 Q 不一致即返回反例；不把有限代表视为固定有限自治精确状态，不做原生三维推广。
