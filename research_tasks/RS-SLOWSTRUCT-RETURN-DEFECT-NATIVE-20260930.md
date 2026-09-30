<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SLOWSTRUCT-RETURN-DEFECT-NATIVE-20260930",
  "title": "回返缺陷证书的真实原生集成与同信息成本对照",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已有小规模算子接口实现，真实模回返/反馈历史集成与净成本证据待做；只消费前置审计确认的主张。",
  "next_action": "取得前置审计有效范围，绑定冻结源的真实模乘列和反馈历史，再生成并验证不含隐藏阶的候选R。",
  "dependencies": [
    "RS-SLOWSTRUCT-RETURN-DEFECT-AUDIT-20260930"
  ],
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
  "registry_key": "RS-SLOWSTRUCT-RETURN-DEFECT-NATIVE-20260930",
  "parent_objective_id": "PO-SLOWSTRUCT-COHERENT-COMPRESSION-6F6B1C93",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SLOWSTRUCT",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SLOWSTRUCT-RETURN-DEFECT-AUDIT-20260930",
  "successor_gate": {
    "new_information_gap": "原件的内部算子检验没有建立真实模乘回返、可达原生历史和端到端成本之间的对应。",
    "why_parent_result_does_not_close_it": "前置任务审计证明和现有证据，不执行真实反馈银行与模乘列的整链集成，也不提供候选发现成本账。",
    "discriminating_outcomes": [
      "真实原生链路正确且限定输入有净收益",
      "链路正确但发现或认证开销超过节省",
      "发现接口反例或证书不满足，保留残差而不压缩"
    ],
    "kill_condition": "前置审计否定必需主张且无可采用修正版，或真实输入不能支持完整标签/原字次序/误差验收；输出反例与精确缺口而非声称成功。",
    "alternative_route_or_free_exploration_considered": "比较直接利用同一回返信息的经典求阶、原始行查询与不删除残差的精确配对估计；不强制完整回返表路线。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "将独立审计与实际实现成本实验隔离，防止作者自证；依赖门控制准入，母问题尚未完成但没有必要重演已存接口测试。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 回返缺陷证书：真实模乘与反馈历史集成及总成本对照

## Mother question

在真实的类型正确模乘和反馈字历史上，从公开N、基数及已观测历史出发，能否得到有用的回返缺陷证书，并在计入候选发现、认证和剩余抽样全部成本后，比持有同样信息的基准更便宜？

## Frozen inputs and scope

前置审计任务：RS-SLOWSTRUCT-RETURN-DEFECT-AUDIT-20260930。启动时读取其实际终局与准确证明版本；只有明确允许集成的主张进入快速路径。若结论为修正或否定，不绕过该结论，可提交带反例的无准入结果。
数学原件与已执行接口边界：https://github.com/awdawmip/enterprise-math/blob/ce048414104a0ae74a7924bc6bf936752129a9ba/research_notes/direct_followups/20260929_slow_return_defect_6f6b1c93.md；https://github.com/awdawmip/enterprise-math/blob/e7555422469f19a3c5765212dc3f37f559c3477e/research_notes/direct_followups/20260929_slow_return_defect_frontier_6f6b1c93.json。
实际原生两臂及行查询源：https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/gram_research/SINGLE_WALKER_QUERY_REDUCTION.md。沿用其中绑定的模乘列和有序反馈入口，不重新实现普通传播器来冒充原生路径。先前的217项算子接口测试作为来源消费，不作为本任务新完成的实验。
执行包：https://drive.google.com/file/d/1BCC7H4tQ9ihLxd7sqbMU4ch0JrJHXMHg/view，全文件SHA256=df9808c2bee3365d46e3f1c2b674245115cad457711c37a1c7ee1b2e88124e78。完整61坐标默认保留；只在已获精确不变子空间准入范围内报告降维结果。现有N21/a2/t4只可作桥接小例，不能据此报告默认分解位宽的复杂度。

## Hard target and required outputs

1. 接通真实模乘回返验证、反馈字提取、双进位J(R,I)、Delta及受限查询反例定位。候选R必须来自公开输入和已记录的生成过程，不输入隐藏阶、因数或事后选择的有利答案。发现用的预样本和生产样本保持证据上的独立关系。
2. 实現INVALID_RETURN、NO_SHORTENING、EXACT_BOUNDARY、RETAIN_RESIDUAL、CERTIFIED_TRUNCATION或NO_CERTIFIED_COMPRESSION六类可区分结果；零质量、mu下界不足、无效候选、非最小回返、重复标签和实际尾地址均有负控，不将非零缺陷自动判成噪声。
3. 对实际可达原生历史验证完整原状态与精确边界/残差分解，包括共同尺度和至少一段后续两臂读出。近似删除只用经审计的平方验收，计入多次替换、统计置信失效和预算耗尽的总误差。配对后批估计使用可变自配对修正；同标签先合并再取范数。
4. 预先冻结至少两组原生程序可支持的输入及其位宽、边界和预算；报告每个被访问历史的候选来源、R、Delta、B、mu/可得性、缺陷位置、区间宽度和处置。小规模完整枚举仅用于同一BRC后端校验，不进入快速路径。
5. 统一成本账至少包含候选发现、模回返核验、反馈字构造、BRC核调用/图尺寸、系数位长、内存、收据大小、重试/失败、抽样与认证次数。以同一输入、成功率/误差预算和同样已获得的回返信息对比原行查询/批估计。分开比较仅精确合并、保留残差和获证删除，不以减少样本数代替总成本结论。
6. 输出源码增量、固定输入清单、完整可回读证据、COST_LEDGER.json、RESULT.md和最小续接状态。首要可验结论是接口正确且成本透明；只有实际数据支持时才报告限定输入下的净收益。

## Research value to preserve

把已执行的内部算子检验推进到真实模标签与可达反馈历史，定位证书成本和节省成本的交叉点。得到无净收益或低证书命中率也应保留，它能排除把复杂度藏进回返发现或高精度估计的路线。

## Success, kill, and return criteria

前置审计有效范围必须满足。成功至少需要真实接口绑定、边界/残差不变量的证据、全部失败处置和同信息基准成本账；不要求强行取得加速。反例或无净收益时输出可复验的限制结论，不调整口径隐藏发现成本。只有便携推导或接口说明而无实际原生链路时，返回PARTIAL并准确标注缺失执行，不能声称集成完成。实验可在真实可用且满足原约束的宿主执行，不把某一操作系统或本机路径作为数学前提。不生成一般多项式求阶、物理慢波或独立定理准入结论。
