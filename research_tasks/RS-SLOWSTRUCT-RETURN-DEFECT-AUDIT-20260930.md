<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SLOWSTRUCT-RETURN-DEFECT-AUDIT-20260930",
  "title": "回返缺陷证书的独立复核与算子证据边界",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "第七轮有作者推导和217项算子接口检查，尚无独立数学审查；真实模回返与可达反馈历史未被该测试覆盖。",
  "next_action": "读取固定第七轮原件及机器前沿，建立公式/假设/证据矩阵，先核对内部反回返与模标签回返的合取。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ce048414104a0ae74a7924bc6bf936752129a9ba/research_notes/direct_followups/20260929_slow_return_defect_6f6b1c93.md",
    "https://github.com/awdawmip/enterprise-math/blob/e7555422469f19a3c5765212dc3f37f559c3477e/research_notes/direct_followups/20260929_slow_return_defect_frontier_6f6b1c93.json",
    "https://github.com/awdawmip/enterprise-math/blob/051a57aa522aa464ddf27cd27a87e47056e4d16b/research_notes/direct_followups/20260927_slow_carry_filter_6f6b1c93.md",
    "https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/gram_research/SINGLE_WALKER_QUERY_REDUCTION.md",
    "https://drive.google.com/file/d/1BCC7H4tQ9ihLxd7sqbMU4ch0JrJHXMHg/view"
  ],
  "evidence_status": "AUTHOR_SOURCE_NOT_ADMITTED_OPERATOR_INTERFACE_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "slow-structure",
    "return-defect",
    "residual-fidelity",
    "typed-brc"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SLOWSTRUCT-RETURN-DEFECT-AUDIT-20260930",
  "parent_objective_id": "PO-SLOWSTRUCT-COHERENT-COMPRESSION-6F6B1C93",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SLOWSTRUCT",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 回返缺陷证书：独立复核与实现边界审计

## Mother question

第七轮回返缺陷证书、反例定位和全程后续读出误差界，哪些在精确声明的原生两臂模型中成立？已记录的算子接口执行究竟验证了哪些命题，哪些模回返和真实反馈历史前提仍未验证？本任务是对已有材料的独立复核，不把作者推导作为已接受定理。

## Frozen inputs and scope

直接数学原件：https://github.com/awdawmip/enterprise-math/blob/ce048414104a0ae74a7924bc6bf936752129a9ba/research_notes/direct_followups/20260929_slow_return_defect_6f6b1c93.md
机器前沿：https://github.com/awdawmip/enterprise-math/blob/e7555422469f19a3c5765212dc3f37f559c3477e/research_notes/direct_followups/20260929_slow_return_defect_frontier_6f6b1c93.json
双进位前序：https://github.com/awdawmip/enterprise-math/blob/051a57aa522aa464ddf27cd27a87e47056e4d16b/research_notes/direct_followups/20260927_slow_carry_filter_6f6b1c93.md
完整两臂来源：https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/gram_research/SINGLE_WALKER_QUERY_REDUCTION.md
原始执行包定位：https://drive.google.com/file/d/1BCC7H4tQ9ihLxd7sqbMU4ch0JrJHXMHg/view，SHA256=df9808c2bee3365d46e3f1c2b674245115cad457711c37a1c7ee1b2e88124e78；前沿记录尺寸95202字节。取回时重新核对完整字节；本任务发布者本轮未重新取回该二进制包。

现有证据只支持61坐标有理正交算子接口测试：来源报告217项检查、1801次BRC核调用；百万地址例只验证内部Delta，未验证c^3=1，不能当成真实求阶实验。上述统计是被审计对象，不是本任务独立重演结果。保留原作者贡献关系；与原作者共享实质推导者只能交付共同复核，不得标独立审查。

继承项目当前P000、残差保真与ACTUAL_TYPED_BRC_ONLY约束。不得以原生维数降至6替代完整61坐标，除非原来源的完整字不变子空间准入覆盖。范围仅为固定有限历史，不增加物理带宽、一般求阶加速或定理准入结论。

## Hard target and required outputs

1. 对原件公式(1)-(4)逐条提交命题、假设、证明或最小分离见证，重点核对J的左右次序、单位范数、R的有效范围、内部反回返与c^R=1的合取，以及同一后续完整仪器的适用范围。
2. 复核受限双进位查询和高位前缀定位：包含终端无溢出、非交换字顺序、前缀子缺陷可加性；将已有负控证据映射到确切条件，必要的独立重演与既有运行分列。
3. 复核实际尾地址和分离配对数P，边界为空、非最小回返、重复模标签、原始尺度B/L，以及非零缺陷不能将尾部无证搬回开头。复核平方验收P*Delta<=epsilon^2*L^2*mu所需mu>0的证书及取得成本。
4. 输出CLAIM_AUDIT.json、AUDIT_REPORT.md和最小复核证据。每项区分SYMBOLIC_VALID、OPERATOR_INTERFACE_VERIFIED、MODULAR_PREMISE_PENDING、NATIVE_HISTORY_PENDING、CORRECTED或REFUTED；给出整体可接入范围及禁止外推范围。

## Research value to preserve

这项审计让后续实验能继承正确的证书与反例，而不是重复早期符号推导或把接口测试升级成真实Shor运行。保留无效实例和非零缺陷；正确的否定或修正同样是有价值结果。

## Success, kill, and return criteria

成功要求每项关键命题都有可回读证明或明确反例，执行证据与推导证据分开，原始字节和核版本有绑定。发现反例即保存最小见证并冻结相关错误主张，不能为获得预期结果修改原输入。无法取得原执行包不妨碍先完成符号审计，但不能声称执行重演已完成。不得仅凭来源报告的217项检查判定独立审计通过。终局限于本任务：给出实际有效范围、尚未解决的缺口及后续原生集成应采用的精确修正版；不关闭母问题。
