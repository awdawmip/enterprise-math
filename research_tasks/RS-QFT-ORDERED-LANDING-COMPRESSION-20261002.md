<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QFT-ORDERED-LANDING-COMPRESSION-20261002",
  "title": "原生 QFT：时间顺序兼容的落点条件压缩",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "低维读出或低秩核不控制模乘落点条件与有序矩阵权重的联合构造、表示及收缩成本。",
  "next_action": "以可构造后缀等价类的落点分支程序为首轮模型，定义状态合并必须保持的未来读出关系，并分别推导构造宽度与中间收缩宽度。",
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
  "registry_key": "RS-QFT-ORDERED-LANDING-COMPRESSION-20261002",
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

# 原生 QFT：时间顺序兼容的落点条件压缩

Status: task specification only; scientific work not started.

## Mother question

能否以可构造的后缀等价类/落点分支程序，同时保留模乘落点条件、有序原生矩阵权重与未来读出，并严格降低构造及收缩成本？

## Frozen inputs and scope

本任务来自用户保存的《低精度原生读出与经典求阶：十二周理论研究计划》及 2026-10-02 的“发布一些关键任务到状态机”指示。存档原文见 research_notes/plans/20260927_LOW_PRECISION_ORDER_RESEARCH_PLAN.md（原始 UTF-8 文件 SHA-256：7470cb969ba49b50d5ee5b120fd92bef7903eeaf038caeaee93bdaba14003c82）。只发布任务；十二周不从发布日期起算，研究尚未启动。

固定 source_refs 中的不可变来源版本。原生初态、模乘调度、反馈顺序、完整坐标与残差、单 walker 提议及工作标签更新均须按来源定义。现有 61 维实数载体和有限字库的声明范围必须保持；任何规模推广另证构造性与成本。保留 P000 和实际 typed BRC 约束，新增科学计算只能通过实际 BRC 接口，不新增经典三角函数、高精度传播器或理想 QFT 数值参考运行。外部经典算法只作为明确标记的符号比较对象。

这些来源是作者稿或原作者执行证据，未因本次发布而成为已接受定理；未来执行先核对所用命题的精确假设与证据状态。公开输入是 (N,a) 及声明的调度、历史和种子；阶、因子、完整支持集及预先解出的模乘地址不是免费输入。

首轮模型限定为时间顺序兼容的落点分支程序：状态须共同携带落点条件以及对未来原生读出的充分信息，边按冻结调度排序。合并关系由公开输入构造，必须保持完整标签、重数、符号、残差与后续操作的语义；不能把非交换权重换成交换统计量。

RP7 的带符号族与对跖无合并条件是待核对的已有反例来源，不重新包装为本任务新结果。若以块作为状态，父块访问、块接受及接受后的标签重抽必须共同定义，单行接受不能代替整块联合律。首轮不同时承诺所有张量、字符和块压缩路线。

## Hard target and required outputs

1. 给出精确定义的表示类、可计算合并判据、成员与父状态查询算法，以及从完整原生过程到该表示的语义保持定理；构造不得调用未知阶或因子。
2. 正向分支：公开定义一个非退化无限输入族，证明成员可识别、表示可构造，给出构造时间、层宽、存储和中间收缩宽度/总位复杂度界。证明所保留的信息足以重建声明的两臂读出或完整 bit/work 核；只有小宽度描述存在而无构造不通过。
3. 负向分支：在同一明确表示类上，构造两条被合并但未来原生读出不同的路径/状态，或给出所需宽度、构造信息量、收缩成本的严格下界。说明障碍量词，不能把该模型负结果推广为一般经典求阶不可能。
4. 分别列出发现分组、成员判断、父块访问、矩阵有序乘积、收缩和近似认证费用。零历史、固定规模、只压缩 QFT 核及 RP7 对跖已知边界只能作对照。

## Research value to preserve

把压缩瓶颈落实为落点条件与有序权重的共同信息，避免只压缩核而把指数复杂度转移到分组或认证。

既有 RS-QFT-MASS-WEIGHTED-APPROX-CERT-20260927 / TP2-96E6EEEAE62D04B03180 负责轨迹一致的完整行近似器 u(h,w) 的质量证书，2026-10-02 读回为 READY / NEEDS_DISPATCH。本任务不修改其任务书、不重复其全局证书交付。三个新任务为同一规划下的独立工作包，理论启动无串行硬依赖；组合结论必须等待所用接口有可定位的实际交付。发现等价在研或已完成交付时，返回精确去重证据和剩余增量，不重做已验证单位。
另与 RS-BRC-SHOR-PROJECTED-ALLOCATION-CERTIFICATE-20261002 保持接口边界：它关注候选依赖源投影和全阶段资源证书，本任务研究未来读出等价关系及有序落点表示的数学宽度/可构造性；资源证书可复用，不重新发布同一证书机制。

## Success, kill, and return criteria

成功必须新增一个带构造与总成本的无限族压缩定理，或限定表示类中的严格障碍。若仍须遍历完整支持集来发现等价类，或认证与完整枚举同阶，作为精确成本障碍返回；有限分组成功、低秩核或经验内存下降不足以验收。

交付表示定义、证明或反例、完整成本表、假设和未决项。需要计算时仅使用实际 BRC 对新合并规则做最小完整联合律核对。任务完成后由实际信息增量决定组合或关闭，不把负结果抹除或自动启动更宽模型。
