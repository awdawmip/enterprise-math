<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "title": "原始证据、版本归属与真实未决字段的定点修复",
  "kind": "GOVERNANCE",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "S5-A/W8、S5-B/W16、附件S11与远端S11存在版本/归属边界；S15由xhome执行，支持身份EM-S15SUPPORT-866CDE仅作只读审查；原S15冻结input hash及历史memo仍未知。",
  "next_action": "仅按原执行端、原回执和不可变字节查缺，先建立版本—作者—代码—输入—输出—时间证据图，并逐字段标记实得、缺失或冲突。",
  "dependencies": [],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "SHOR",
    "EVIDENCE",
    "PROVENANCE",
    "MAINTENANCE"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "parent_objective_id": "OBJ-BRC-SHOR-SLICE-UNFINISHED-BRANCHES-20261004",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P01",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "MAINTENANCE",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 原始证据、版本归属与真实未决字段的定点修复

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

怎样只依赖原执行端、原回执和不可变字节，恢复本研究链中真实可恢复的版本、作者、代码、输入、输出和时间证据，并把无法恢复的字段保持为明确 UNKNOWN，而不通过重跑制造原始记录？

## Frozen inputs and scope

本任务只处理证据与版本归属，不产生新的数学结论。冻结前沿：S5-A/W8、S5-B/W16、附件S11与远端S11存在版本/归属边界；S15由xhome执行，支持身份EM-S15SUPPORT-866CDE仅作只读审查；原S15冻结input hash及历史memo仍未知。

私有源包为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`，整包 SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`。公开任务书只暴露必要任务元数据，不公开原始附件、完整日志或私有下载地址。重点核对 S5-A/W8、S5-B/W16、附件S11、远端S11、S14/S15、xhome 执行与 EM-S15SUPPORT-866CDE 只读审查之间的版本和作者边界。

禁止把重新运行得到的新文件写成旧运行时序、旧缓存或旧身份的证据；禁止修改争议历史活动来消除冲突。

## Hard target and required outputs

建立一份逐字段的证据图，至少覆盖版本、作者/执行身份、源码、冻结输入、缓存/记忆状态、输出、运行时序、验证与回执。每个字段必须标记为 `VERIFIED`、`CONFLICT` 或 `UNKNOWN`，并给出真实证据定位或缺失原因。

若原件可恢复，必须对不可变字节或原回执做匹配核验；若不可恢复，保留 null/UNKNOWN，不以重新执行填补。另列读取、解包、哈希、归档和校验费用，并明确这些费用不是科学运行成本。

## Research value to preserve

后续 S15、缓存、执行树、三维切片残差和实现优化任务都依赖正确的版本与作者边界。若把两个 S5、两个 S11、外部执行和独立审查混为同一来源，后续任何因果、性能或科学归因都会污染。因此这项治理工作本身值得进入任务机，即使最后只得到有边界的 UNKNOWN。

## Success, kill, and return criteria

成功：争议字段均有可核验定位，且任何不可恢复项保持 UNKNOWN；输出可作为后续任务的来源索引而无需重跑已完成科学实验。

返回：原件不存在、权限不可得或证据互相冲突而无法裁定时，返回精确缺口和冲突集合；不得从缺失推导科学结论。

停止：一旦所有声明字段已被分类并完成证据定位，即结束本任务；不扩展为新的 S15 实验、缓存优化或三维切片动力学研究。
