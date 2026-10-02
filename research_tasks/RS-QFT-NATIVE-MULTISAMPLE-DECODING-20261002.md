<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QFT-NATIVE-MULTISAMPLE-DECODING-20261002",
  "title": "原生 QFT：低精度多样本到求阶的解码桥梁",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "尚未证明原生低精度输出满足短寄存器联合解码所需的数论关系和概率保证。",
  "next_action": "冻结原生样本联合律及公开参数 s∈{1,2,4}、L=n+ceil(n/s)，逐项列出解码定理需要的浓缩、独立性/相关性与误差假设，并找出首个未证桥梁。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/README.md",
    "https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/gram_research/SINGLE_WALKER_QUERY_REDUCTION.md",
    "https://github.com/awdawmip/enterprise-math/blob/d5e5ff75902240b9cbdefde7eb221567d3c31c95/research_notes/HEARTBEAT_RP3_ROW_QUERY_FILTER_182592BF_20260927.md",
    "https://github.com/awdawmip/enterprise-math/blob/07bab8333ff49b33fcca51693c0f1c7ab27a1d5c/research_notes/HEARTBEAT_RP7_SIGNED_BLOCK_RESAMPLING_C971348E_20260927.md"
  ],
  "evidence_status": "PUBLISHED_RESEARCH_SPECIFICATION_NOT_EXECUTED_SOURCE_CANDIDATES_UNREVIEWED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "QFT",
    "LOW_PRECISION",
    "ORDER_FINDING",
    "THEORY"
  ],
  "claim_lease_minutes": 1440,
  "identity_lane": "QFT-LP",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "parent_objective_id": "PO-QFT-LOW-PRECISION-ORDER-THEORY-20260927",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-QFT-NATIVE-MULTISAMPLE-DECODING-20261002",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS"
  }
}
-->

# 原生 QFT：低精度多样本到求阶的解码桥梁

Status: task specification only; scientific work not started.

## Mother question

原生低精度样本在什么可证明条件下支持多样本联合解码，从而恢复阶、阶的倍数或非平凡因子？样本数量与解码费用能否一同受控？

## Frozen inputs and scope

本任务来自用户保存的《低精度原生读出与经典求阶：十二周理论研究计划》及 2026-10-02 的“发布一些关键任务到状态机”指示。存档原文见 research_notes/plans/20260927_LOW_PRECISION_ORDER_RESEARCH_PLAN.md（原始 UTF-8 文件 SHA-256：7470cb969ba49b50d5ee5b120fd92bef7903eeaf038caeaee93bdaba14003c82）。只发布任务；十二周不从发布日期起算，研究尚未启动。

固定 source_refs 中的不可变来源版本。原生初态、模乘调度、反馈顺序、完整坐标与残差、单 walker 提议及工作标签更新均须按来源定义。现有 61 维实数载体和有限字库的声明范围必须保持；任何规模推广另证构造性与成本。保留 P000 和实际 typed BRC 约束，新增科学计算只能通过实际 BRC 接口，不新增经典三角函数、高精度传播器或理想 QFT 数值参考运行。外部经典算法只作为明确标记的符号比较对象。

这些来源是作者稿或原作者执行证据，未因本次发布而成为已接受定理；未来执行先核对所用命题的精确假设与证据状态。公开输入是 (N,a) 及声明的调度、历史和种子；阶、因子、完整支持集及预先解出的模乘地址不是免费输入。

令 n=ceil(log2 N)。首轮固定公开取舍参数 s∈{1,2,4}、L=n+ceil(n/s)；这些是待分析配置，不能预设成功，也不能按真实阶选参。保留标准宽度的符号后处理对照。外部理论入口为计划所列 Seifert/Ekerå 短寄存器求阶及 Ekerå 2021 Appendix A（https://eprint.iacr.org/2018/797）；执行时核对精确版本、原始定理与假设，本任务发布不认定它已适用于原生过程。

分别建模寄存器长度、设计性门截断、局部读出误差、表示误差以及多次采样的共享随机状态。不得把原生样本直接替换为理想 Shor 样本，不运行新的理想 QFT 数值参考。

## Hard target and required outputs

1. 交付“原生分布条件—寄存器长度—样本数—解码总成本—成功概率”的精确定理。明确有效数论关系及概率质量，若有相关样本，使用实际联合分布或证明充分的条件独立性。
2. 正向分支必须在至少一个公开可识别的非退化无限原生输入族上证明所用分布条件，再连接解码结论；仅套用抽象 TV 三角不等式或重述外部理想样本定理不算桥梁已建立。通用情况未闭合时保留准确限制。
3. 若正向条件在冻结原生模型中失败，交付具体失效假设及可复核的原生反例/障碍，保留外部解码结果为条件性定理，不强行拼接。有限反例只反驳对应普遍命题，不替代一般复杂度下界。
4. 区分并分别认证阶倍数、精确阶、非平凡因子。a^k=1 mod N 只验证 k 为阶倍数；最小性或因子提取需要额外的明示步骤。候选筛选不能用真阶或因子作判据。
5. 纳入样本生成、误差/质量证书、格维数、规约、枚举、验证、失败重启和预处理费用；样本数由信息量与失败预算证明决定。近似样本到解码成功率的传递需对实际联合核给出有效界，所有被调用的采样器接口单列。

## Research value to preserve

将可生成的原生样本与可验证数论答案连接起来，区分采样正确、解码成功与精确阶/非平凡因子三个不同目标。

既有 RS-QFT-MASS-WEIGHTED-APPROX-CERT-20260927 / TP2-96E6EEEAE62D04B03180 负责轨迹一致的完整行近似器 u(h,w) 的质量证书，2026-10-02 读回为 READY / NEEDS_DISPATCH。本任务不修改其任务书、不重复其全局证书交付。三个新任务为同一规划下的独立工作包，理论启动无串行硬依赖；组合结论必须等待所用接口有可定位的实际交付。发现等价在研或已完成交付时，返回精确去重证据和剩余增量，不重做已验证单位。
该任务可先完成桥梁条件的理论分析；整体高效算法结论额外依赖直接读出或压缩后端的完整资源定理，以及使用的误差证书已满足自身假设。不能用相互引用掩盖循环依赖。

## Success, kill, and return criteria

接受新的原生桥梁与明确资源/成功率定理，或冻结原生模型中准确定位的失效机制与反例。只实现经典后处理、只调整 L、用隐藏答案筛样本或无证明替换理想分布均不通过。

若桥梁不能成立，分别交付原生采样结论和条件性解码结论，并列出最小未决接口；不声称已解决一般经典高效求阶。输出证明、假设依赖图、失败预算与资源账，科学验证维持最小实际 BRC 范围。达到限定硬目标后返回父规划评价，不自动开启实验或后续轮次。
