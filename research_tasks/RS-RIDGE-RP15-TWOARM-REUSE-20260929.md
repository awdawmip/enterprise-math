<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/3f52bb1f223c2dbb53c764cfec07958a886c53f0/research_notes/HEARTBEAT_RP15_FUSED_606AA6D3_20260928.md",
    "https://drive.google.com/file/d/1jnfc8MTaYTtxyPsL3WTzCN059TZxT3Dn/view"
  ],
  "evidence_status": "SOURCE_BACKED_AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED",
  "last_progress_ref": "research_notes/HEARTBEAT_RP15_FUSED_606AA6D3_20260928.md",
  "last_progress_at": "2026-09-28",
  "hard_block": null,
  "claim_lease_minutes": 1440,
  "identity_lane": "RIDGE-RP15-C97134",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "parent_objective_id": "OBJ-BRC-SHOR-RIDGE-PRECISION-COST-20260929",
  "historical_contribution_disclosure": [
    "EM-DIRECT-C97134; this publishing conversation continues the RP15 author context and is not an independent reviewer."
  ],
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-RIDGE-RP15-TWOARM-REUSE-20260929",
  "registry_key": "RS-RIDGE-RP15-TWOARM-REUSE-20260929",
  "title": "RP15：两臂完整字段构造的同目标复用",
  "frontier": "RP15减少了候选认证对象费用，但实际两臂场构造、标签遍历与中间对象成本仍完整发生。",
  "next_action": "冻结原 prepare 数据流，分解门作用、模乘索引、两臂带符号 join、规范化与质量求和，选择一项可证明消除的重复工作。",
  "tags": [
    "BRC",
    "SHOR",
    "RIDGE_PRECISION",
    "TWO_ARM",
    "EXACT_TARGET"
  ]
}
-->

# RP15：两臂完整字段构造的同目标复用

## Mother question

在保持 RP15 实际两臂带符号合成、完整工作场和选位规则不变的前提下，能否减少字段构造、标签遍历、规范化或中间对象的重复费用，并在取得原验证器确认的因子的总成本上兑现？

## Frozen inputs and scope

使用 source_refs 指向的冻结 RP15 包与原采样、预算和后处理器。RP15 已经完成候选 C/J 聚合与延后候选物化，并测试过 prepare 阶段质量聚合；这些既有单元不得重新包装为本任务的新发现。

所有真实工作标签、标签相遇关系、符号、准确指数和实际门序必须保留。两臂先按完整有符号状态合成，再计算范数。不得以正质量代替振幅关系，不得按前两个分量、范数相等或未证明的哈希等价合并工作行，也不得移动非线性截位边界。

首项工作是把原 prepare 数据流拆成门作用、模乘索引、两臂 join、行规范化、质量求和和选中分支物化的实际费用与依赖，再选择一个可消除的重复单元。

## Hard target and required outputs

明确新的求值顺序、缓存或复用对象，并证明返回的两臂完整原始字段、分支质量、位概率、量化输入和后续字段保持相同；未物化的分支在需要审计或后续使用时必须可准确重建。

在同一随机带上逐项比较原实现与新实现的全部科学事件、候选与预算、返回字段、随机请求、随机数终态、因子结果和停止点。若生产诊断因惰性求值不再保存某些未使用对象，必须明确哪些量未计算，而不是填入推测值。

冻结新负载、方法顺序、失败处理和资源口径，分别报告预建门库条件及至少一个新进程准备场景的成本。任务 A 的成果只有在独立验收并明确绑定后才可组合；本任务先给出不依赖任务 A 的单项结果。

交付可恢复代码、证明或最小反例、完整字段与随机带证据，以及门作用次数、标签访问、整数位长、临时对象、存储和直到取得已验证因子的成本分解。

## Research value to preserve

RP15 已经证明认证层可以在不改变目标的前提下降低对象构造费用，但完整两臂工作场仍是主要未压缩计算入口。本任务用于判断哪一部分能安全共享，以及哪些相干依赖使某种重排必然无效。

## Success, kill, and return criteria

只有同目标完整对应通过后才比较性能；载体维数、缓存命中率或对象数量本身不能替代总成本。若没有总体优势，保留原路径并报告部件收益或净亏损，不按不同 N 事后挑最快实现冒充统一策略。

如果拟议复用破坏标签关系、门序、截位位置或无法减少真实工作，返回准确反例与不可删依赖后终止该方案。不得宣称通用廉价幅值接口、经典多项式 Shor 或物理硬件优势。
