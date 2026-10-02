<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QFT-DIRECT-BOUNDED-READOUT-20261002",
  "title": "原生 QFT：有界随机直接读出的构造与总成本",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "两臂读出恒等式已知，但按能量分布抽坐标与访问对应坐标尚无可计费的低成本原生构造。",
  "next_action": "冻结合法 (h,z) 输入和原提议核，把 q(j) 的采样、坐标访问及随机比特生成展开为一个完整算法，再定位第一个需要完整行或隐藏答案的步骤。",
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
  "registry_key": "RS-QFT-DIRECT-BOUNDED-READOUT-20261002",
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

# 原生 QFT：有界随机直接读出的构造与总成本

Status: task specification only; scientific work not started.

## Mother question

能否在原生合法查询上，不恢复完整行，直接生成正确读出比特，并给出包含能量坐标采样成本的构造定理或明确访问模型下的障碍？

## Frozen inputs and scope

本任务来自用户保存的《低精度原生读出与经典求阶：十二周理论研究计划》及 2026-10-02 的“发布一些关键任务到状态机”指示。存档原文见 research_notes/plans/20260927_LOW_PRECISION_ORDER_RESEARCH_PLAN.md（原始 UTF-8 文件 SHA-256：7470cb969ba49b50d5ee5b120fd92bef7903eeaf038caeaee93bdaba14003c82）。只发布任务；十二周不从发布日期起算，研究尚未启动。

固定 source_refs 中的不可变来源版本。原生初态、模乘调度、反馈顺序、完整坐标与残差、单 walker 提议及工作标签更新均须按来源定义。现有 61 维实数载体和有限字库的声明范围必须保持；任何规模推广另证构造性与成本。保留 P000 和实际 typed BRC 约束，新增科学计算只能通过实际 BRC 接口，不新增经典三角函数、高精度传播器或理想 QFT 数值参考运行。外部经典算法只作为明确标记的符号比较对象。

这些来源是作者稿或原作者执行证据，未因本次发布而成为已接受定理；未来执行先核对所用命题的精确假设与证据状态。公开输入是 (N,a) 及声明的调度、历史和种子；阶、因子、完整支持集及预先解出的模乘地址不是免费输入。

令 x=v_h(z)、y=T_h v_h(P_i^{-1}z)，S=||x||²+||y||²。S>0 时 C=2<x,y>/S、p_+=(1+C)/2。第一版固定原工作标签提议和更新，只替换读出比特生成；若改变块接受或标签重抽，必须另证完整联合转移核。S=0 不定义比值，证明其在精确提议下不可达，并规定异常时有限退出。

候选接口：q(j)=(x_j²+y_j²)/S，U_j=2x_j y_j/(x_j²+y_j²)。抽 J~q 后以 (1+U_J)/2 生成比特。恒等式本身是基线；q 的可构造性及访问成本是未解问题。若使用其他随机量 U，需在给定公开 (h,z) 条件下满足 U∈[-1,1] 与 E[U|h,z]=C。缓存与共享随机性属于算法状态，不能改变同一查询所声明的对象。

## Hard target and required outputs

1. 交付完整访问模型、伪代码、随机源合同、零坐标/零伙伴/拒绝处理和 bit/work 联合律证明。必须展开 q 的归一化、采样与坐标访问，不能将“能调用 q”留作免费预言机后宣称实现已闭合。
2. 正向分支：对一个公开可识别、含非零反馈的非退化无限输入族，给出无需预知阶或因子的构造及总位复杂度，证明相对完整行恢复具体节省的资源；若只能得到参数化接口定理，明确标记条件性，另给首个未闭合原语的精确问题。
3. 负向分支：对明确限定的访问/表示模型，给出不可识别反例、查询成本归约或无法节省的严格见证。仅证明某一候选退化不等于所有低精度采样器不可能。困难性论证限于可生成的原生查询，不准自由加参考臂；区分任意合法查询与具有足够真实采样质量的查询。
4. 成本包括初建、地址和坐标生成、整数位长、随机位、拒绝/重启、内存与（若近似）条件偏差认证。近似变体须证明裁剪后条件期望误差，分子分母分别无偏不够；在同提议机制下明确给出单步及全程误差累计的适用条件。

## Research value to preserve

检验能否直接产生正确读出比特而无需恢复完整行，明确弱接口究竟减少了哪些必需信息与费用。

既有 RS-QFT-MASS-WEIGHTED-APPROX-CERT-20260927 / TP2-96E6EEEAE62D04B03180 负责轨迹一致的完整行近似器 u(h,w) 的质量证书，2026-10-02 读回为 READY / NEEDS_DISPATCH。本任务不修改其任务书、不重复其全局证书交付。三个新任务为同一规划下的独立工作包，理论启动无串行硬依赖；组合结论必须等待所用接口有可定位的实际交付。发现等价在研或已完成交付时，返回精确去重证据和剩余增量，不重做已验证单位。

## Success, kill, and return criteria

接受可定位的新构造及完整成本证明，或上述访问模型中的严格负结果。只重述 E_q U=C、小维数、少数顶层查询、经验成功率或条件预言机定理不算接口闭合。候选仍需完整行时保留正确性基线并停止宣称加速；无法闭合的原语保留为未决项。

交付证明稿、假设与来源状态表、可复核资源账；只有新接口需要时提供实际 BRC 最小验证。任务终止处明确正结果、限定模型负结果和未决余量，并返回父规划作后续判断。
