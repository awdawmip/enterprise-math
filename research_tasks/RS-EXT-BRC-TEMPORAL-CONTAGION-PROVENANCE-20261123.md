<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-EXT-BRC-TEMPORAL-CONTAGION-PROVENANCE-20261123",
  "title": "时序接触网络传播的来源追踪与最小 BRC 保真状态",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "三节点两次接触的 SI 有理完全枚举给出相同聚合边但 P(C 感染)=1/4 与 0；双源接触给出相同 P(B 感染)=3/4 但来源条件概率 2/3 与 1/3。已给出感染集合在来源无关转移下的精确未来安全商引理；均为作者校核、未独立复核。尚无有类型 BRC 传播映射、时序 SIR 对照、真实性能结论。",
  "next_action": "复算固定 SI 两类微例及保真商引理；冻结完整时序接触词、感染来源观察及允许后续干预；构造有类型有理正权 BRC 接口、最短拒绝见证；与显式有理 DP 和外部时序 SIR 接触/成对消息传递基线比较；逐项核算端到端成本。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@aec1279101507edbfcc4e9489d68404960792bd4:research_notes/portable_direct/2026-11-23_external_temporal_epidemic_exact_provenance_seed.md",
    "awdawmip/enterprise-math@d424092fd468a3818c4a7c428943c4a165052642:definitions/EM_FOUNDATION_STARTUP.json",
    "awdawmip/enterprise-math@d424092fd468a3818c4a7c428943c4a165052642:definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json",
    "awdawmip/enterprise-math@d424092fd468a3818c4a7c428943c4a165052642:src/enterprise_math/predictive_quotient.py",
    "awdawmip/enterprise-math@d424092fd468a3818c4a7c428943c4a165052642:src/enterprise_math/composition_safe_collapse.py",
    "https://doi.org/10.1103/PhysRevE.84.016105",
    "https://doi.org/10.1103/PhysRevX.9.031017",
    "https://doi.org/10.1007/s41109-021-00363-w"
  ],
  "evidence_status": "AUTHOR_VERIFIED_EXACT_RATIONAL_SI_MICROCASES_AND_QUERY_RELATIVE_QUOTIENT_LEMMA; EXTERNAL_PRIOR_ART_VERIFIED; NO_INDEPENDENT_REVIEW; NO_BRC_EXECUTION; NO_SIR_BASELINE_EXECUTION; NO_SPEEDUP_OR_NATIVE_PHYSICAL_TRANSFER",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "EXTERNAL_TEMPORAL_NETWORK",
    "EPIDEMIC_SI_SIR",
    "EXACT_RATIONAL",
    "BRC",
    "TEMPORAL_PROVENANCE",
    "SAFE_QUOTIENT",
    "SOURCE_ATTRIBUTION"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-EXT-BRC-TEMPORAL-CONTAGION-PROVENANCE-20261123",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EPID2026",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION"
}
-->

# 时序接触网络传播的来源追踪与最小 BRC 保真状态

研究强度：公开外部 SI 模型的两个作者核算精确有限实例 + 有条件商引理；没有宣称新的流行病学理论、可靠性算法加速或 X6 原生物理对应。原始算例见冻结来源笔记。

## Mother question

已知带时标的接触事件及有理感染/恢复律，何种最小状态可以同时保留指定传播概率、时间可达性、首个传播来源及条件性来源干预查询？已有 BRC 正有理路径表示能否提供对外部时序 SIR 模型实际有价值的安全压缩/拒绝证书、复用查询优势或明确成本边界，而非重复通用预测商或现有接触式消息传递算法？

## Frozen inputs and scope

科学源固定在本任务 source_refs 的精确 commit：P000 的六维原生离散 Cell + 独立时间与三维切片概念保持原义，来源和路径在安全取商前保留；外部 SI/SIR 接触图不自动构成 X6 原生空间或物理定律。外部起点是标号有限节点和**有序**接触 `(t,u,v,p_t)`；每次仅当 u 已感染且 v 易感，才按 `p_t∈Q∩[0,1]` 尝试传染。微例为**无恢复 SI**，引入 SIR 时必须另明示逐事件恢复时序、恢复概率、更新次序和观察窗口，不把 SI 算例冒称 SIR 结论。接触可定向；原始顺序不可先聚合成静态边。

作者算例 A：初态 A 感染，接触 A→B 再 B→C，各 p=1/2，有 `P(C感染)=1/4`；反序先 B→C 再 A→B 得 0。算例 B：A,D 已感染，B 易感；A→B 后 D→B 得 `P(B感染)=3/4`、`P(感染源=A|B感染)=2/3`；反序得同一感染率、来源概率 1/3。每个路径原子及分母见独立笔记。

一个已推导的**有条件外部模型引理**：若每次未来传播门控及其感染概率只依赖当前感染集合和约定接触，而与传染源历史无关，则对于全部现在/未来感染集合读出，`q(I,h)=I` 是精确未来安全商；全节点当前感染位可观察时，它在这个观察族下是最粗商。证明为每一事件感染集合转移概率仅依赖 I，归纳及零步区分；引入首源读出、源条件干预或源依赖传播律时该商不再获保证。本引理是普通有限 Markov 状态合并的实例，不声称新的通用 BRC 定理。

## Hard target and required outputs

固定单事件更新、相同时刻接触的确定次序、全状态 `(SI/SIR状态,有序传播来源,事件时间,有理概率)` 及未来查询语言，明确查询包括：逐节点感染、给定时间窗口感染、时间可达路径、首次传播源、条件源、源条件隔离/干预。为每个查询族给出最小有限输入、全部确切有理输出及验证者可逐路径复核的短证书。对候选商给出有类型观测映射、更新下降证明或最短反例，区分仅观察感染集合时可合并与源归因/干预时必须保留的历史。

复用 Source 中既有 BRC 正有理权载体、`predictive_quotient` 与 `composition_safe_collapse` 的明确适用算法，必要时设计领域封装而非重新发明通用商。提出完整 `(time-stamped contact word, source history, hidden state trace, positive rational weight)` 到 BRC 的映射，验证映射类型、正权性质、总质量、事件顺序、传播源、复合更新，禁止将仅有分数的外部 DP 直接冒称已运行 BRC。最短反例须满足同输入、同操作语义并有实际差异读出。

对 SI 的 n=3、4、5 节点与有限接触序列和 p∈{1/4,1/2,3/4} 建立可精确复算的案例，再选实际可运行的有限 SIR 测例：明确时序接触、感染与恢复参数、初态、观察窗口，若有树形与有环接触各一组更能比较结构限制。与精确有理状态枚举/条件 DP 及公开接触式动态消息传递或时序成对方法进行**同一模型、同一查询、同一误差语义**的核验。若某论文方法本身只计算边际而不支持来源查询，则记录查询能力边界，不伪造不公平性能比。未运行的基线只列为待验。

成本账从输入读取、事件词与来源编码、有理位长、BRC 转换、路径/商构造、状态保存、更新、多次查询、恢复解码及独立校验全量计算；分别报告可观察收益、时间、峰值内存、随接触数/节点数变化。不得隐藏指数枚举或预处理，无证据不声称 BRC 速度优势。给出足以重放的精确算例、有限域覆盖、实际程序版本和缺失边界。

## Research value to preserve

该任务不同于 `RS-EXT-BRC-CCF-TEMPORAL-RELIABILITY-20261116` 的共因设备故障/隐环境模型：重点是时标接触有向路径可达性、传播源分叉与来源依赖干预及针对公开时序传染基线的能力/开销核验。既有 `RS-BRC-RESTRICTED-PORT-QUOTIENT-20261005` 与 `RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028` 负责通用商理论，本任务不重复发表其抽象定理，只为外部传播模型给出具体译码合同、最小保真/拒绝证书和公正成本比较。Pan–Saramäki (2011) 已证明时间路径与静态图差异重要；Koher 等 2019 年 PRX 的接触式动态消息传递以及 2021 年时序 SIR 成对模型已经是既有强基线，不能将时序敏感性冒称首次发现。

## Success, kill, and return criteria

完成至少两个作者微例的独立有理复算、商引理条件与反例覆盖、真实有类型 BRC 映射或其严格不适用见证、至少一项可实际对应的外部基线核验及完整成本表，并公开区分理论证明、有限枚举、软件执行、未完成验证。若 BRC 仅重述成熟 SI/SIR DP 或时序消息传递而在来源/查询复用/证书/成本上无优势，须返回可重放负结果并收束，不通过改名扩张任务。所有数学/实验结果在真实 Result 与独立审查前保持作者研究状态；正式 Task 发布不授予 CLAIM、Working Truth 或 Foundation。
