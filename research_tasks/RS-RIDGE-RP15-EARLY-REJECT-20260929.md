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
  "task_id": "RS-RIDGE-RP15-EARLY-REJECT-20260929",
  "registry_key": "RS-RIDGE-RP15-EARLY-REJECT-20260929",
  "title": "RP15：有证书的失败精度候选提前终止",
  "frontier": "RP15已将候选C/J认证改为准确聚合并延后物化，但每个失败候选仍完整扫描当前工作场。",
  "next_action": "冻结字段扫描顺序，先构造未扫描贡献的保守界，证明一个候选在何种条件下可在扫描结束前安全判失败。",
  "tags": [
    "BRC",
    "SHOR",
    "RIDGE_PRECISION",
    "EARLY_REJECT",
    "EXACT_TARGET"
  ]
}
-->

# RP15：有证书的失败精度候选提前终止

## Mother question

能否在尚未扫描当前完整工作场全部贡献时，利用已扫描部分与未扫描部分的可靠界，证明某个精度候选必定失败，从而提前终止该候选，同时严格保持 RP15 的第一个合格 K、准确误差扣账、返回字段、随机轨迹和因子停止点？

## Frozen inputs and scope

冻结参考为 source_refs 指向的 RP15 实现与证据。实际 b12 BRC 门、18 代表与 61 完整模式语义、全部非零工作标签、符号、准确二进制指数、模乘相遇关系、门序、原 toward 截位、候选顺序、方向误差定义和准确扣账均保持不变。未扫描贡献不得视为零。

方向误差仍为 gamma^2 = 1 - J^2/(A*C)。A 是原完整条件场质量，C/J 是候选完整场范数和配对。必须保留已有非单调反例：更高尾数位数不保证 gamma 单调下降，因此不得用未经证明的二分或跨位跳跃代替原候选顺序。

首项工作只允许改变认证的求值顺序，不允许通过增精、删除标签、改采样目标或读取未知阶与因子取得所谓收益。

## Hard target and required outputs

给出已扫描部分与未扫描部分的数据类型、界条件和安全拒绝判据，并证明任何提前拒绝都不可能跳过 RP15 原本应接受的候选。无法判定时必须继续扫描；首个可能合格候选最终仍准确得到 C、J、gamma、扣账和完整返回场。

实现一个局部扩展和独立检查器，逐项比较第一个合格 K、失败回退、预算余额、完整字段、位概率、随机请求、随机数终态、因子结果和停止点。生产早退证书与审计补算必须区分；没有精确计算的失败候选不得伪填精确 C/J/gamma。

除继承回归外，预声明新的极端符号、指数、近阈值字段与求因子种子。记录已访问项数、额外界构造费用、整数位长、临时存储、准备费用、认证部件时间和取得已验证因子的总时间，并保留无收益或更慢结果。

## Research value to preserve

RP15 已经消除了失败候选的规范 Row 物化，但仍对每个候选完整遍历当前工作场。该任务只攻这一剩余扫描费用；一个可证明且可复用的早退判据，或证明早退在该结构中不值得的准确负结果，都可防止后续重复试错。

## Success, kill, and return criteria

正确性通过必须同时有保守证明和完整同目标回归；性能成功还必须在计入界构造费用后减少实际工作或总求因子成本。正确但更慢只能标为方法成立、性能目标未满足。

如果未扫描贡献无法形成足够早的有效界，返回最小反例、触发过晚范围和剩余缺口并终止该方案。不得以改变精度预算、改输出分布或忽略非单调反例来满足成功条件。
