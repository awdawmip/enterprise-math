<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-EXT-BRC-CCF-TEMPORAL-RELIABILITY-20261116",
  "title": "共因失效可靠性与时序相关性的精确 BRC 保真证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "公开可靠性研究已给出 k-out-of-n 共因失效的 DBN/Markov 基线；本轮获得两个独立精确有理小模型，证实独立边缘化可能抹去同源故障及跨时关联。尚无针对有限任务事件族的 BRC 可观察状态与主流概率模型核验接口及完整成本结果。",
  "next_action": "固定无修复 2-out-of-3 共因冲击模型和二态二时刻 HMM，独立验证 exact fractions；冻结未来查询语言，再实现事件/来源保真 BRC 载体、与条件 DP/显式 DTMC 的等值反例检验和开销账，先交付最小可重现证书。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@34deb84cc62b1b73f372ca06fa20a08210de10f8:definitions/EM_FOUNDATION_STARTUP.json",
    "awdawmip/enterprise-math@34deb84cc62b1b73f372ca06fa20a08210de10f8:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "awdawmip/enterprise-math@34deb84cc62b1b73f372ca06fa20a08210de10f8:research_task_records/RS-BRC-RESTRICTED-PORT-QUOTIENT-20261005/TP2-18142D0E079087C682E1.json",
    "awdawmip/enterprise-math@34deb84cc62b1b73f372ca06fa20a08210de10f8:research_task_records/RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028/TP2-8FD66B1B48BE87DA1AC1.json",
    "https://doi.org/10.1002/qre.70203",
    "https://www.stormchecker.org/",
    "https://prismmodelchecker.org/"
  ],
  "evidence_status": "EXACT_RATIONAL_MICROCASES_DERIVED_AND_CHECKED; LITERATURE_ABSTRACT_AND_TOOL_SCOPE_VERIFIED; EXTERNAL_BASELINE_NOT_EXECUTED; GENERAL_EFFICIENCY_OR_NATIVE_PHYSICAL_BRIDGE_NOT_CLAIMED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "EXTERNAL_RELIABILITY",
    "COMMON_CAUSE_FAILURE",
    "BRC",
    "EXACT_RATIONAL",
    "FINITE_HORIZON",
    "OBSERVER_FIDELITY",
    "TEMPORAL_PROVENANCE"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-EXT-BRC-CCF-TEMPORAL-RELIABILITY-20261116",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION"
}
-->

# 共因失效可靠性与时序相关性的精确 BRC 保真证书

Status: scientific microcase verified; formal task publication and owner state are separate.

## Mother question

对于公开文献中的有限 k-out-of-n 共因失效（CCF）与带隐藏环境的时序失效模型，能否把有理概率路径转换成带事件来源、时间顺序与未来查询语义的正权 BRC 载体，并证明哪些状态可安全合并？是否存在明确定义的查询族，使 BRC 在**保真证书、可解释的关联来源或实际总成本**上获得可测的收益，而不是只重命名现有 DBN/DTMC/BDD 计算？

这是外部可靠性模型的有类型数学应用，不声称 k-out-of-n、CCF、DBN、Markov 或概率模型检验是本项目新发明。外部概率语义不得自动等同原生 X6 物理定律；若要求原生嵌入，另列编码、第三切片分量、读出及被保持操作的明确证明义务。

## Frozen inputs and scope

1. 固定研究输入为 `awdawmip/enterprise-math@34deb84cc62b1b73f372ca06fa20a08210de10f8` 对应的 Source Foundation 启动包及研究世界观所许可的有理正权 BRC、保留联合关系与未来观察的语义；行为控制规则仍随现行 main 更新，不重写冻结科学输入。当前 P000 六维原生空间+独立时间、三维切片和三元原始稳定性不受外部概率模型改变。
2. 外部基线：Li 等，2026-04-01，DOI `10.1002/qre.70203` 的 k-out-of-n CCF 动态贝叶斯网络；同时采用 Storm / PRISM 的有限 DTMC/显式状态与 BDD/MTBDD 概率检验作为可执行对照。论文摘要不能替代原始算例数据，也不能宣称已实际运行软件。
3. **模型 A：** 2-out-of-3，无修复，先抽共同冲击 `S ~ Bernoulli(1/5)`。若 `S=1` 则全部故障；若 `S=0` 则三组件分别独立以 `p=1/10` 故障。系统正常概率精确为
`R=(4/5)*[(9/10)^3+3*(1/10)*(9/10)^2]=486/625`。
单组件故障边缘率 `7/25`，若错误地将该边缘率再次当作组件间独立，则得到 `R_iid=12636/15625`，偏高 `486/15625`。这个反例针对**错误的边缘独立压缩**，不针对明确保留共同冲击的 DBN、BDD 或 Markov 基线。
4. **模型 B：** 隐藏环境 `H,L`，初态各 `1/2`，每一时刻切换 `1/4`、保持 `3/4`，H 态观察到故障概率 `1/4`、L 态 `3/4`，观察条件于完整环境序列独立。定义 `F_1,F_2` 为连续两时刻故障指示。精确计算 `P(F_t)=1/2`，`P(F_1=F_2=1)=9/32`，错误的跨时独立化得到 `1/4`；`P(F_2=1 | F_1=1)=9/16`。双故障四条环境路径带权为 `3/128,3/128,3/128,27/128`，完整 BRC 权重直方图 `{3/128:3,27/128:1}`，`C=4,W=9/32,M=27/128,d=1`。直方图本身丢弃路径标签；涉及未来按环境介入、修复或来源归因的查询不得据此单独取商。

## Hard target and required outputs

首先冻结两个模型的有限完整状态、读出集合（至少单时刻正常概率、两时联合故障、指定共因冲击源、条件概率）和允许操作（时间更新、事件条件化、在给定状态下修复或来源检查）。输出可复现的有理数证书、模型 A 的二项式枚举、模型 B 的四路径清单与两种错误压缩的最短区分见证。

随后把每个正权路径定义成 `(source-id, ordered-event-word, hidden-state-trace, rational-weight)`，明确向 BRC exact-weight histogram、CWM、有限正有理转移/端口算子的投影映射；对于每一拟压缩商 `q`，证明选定未来查询和更新下的 fiber-constancy / 转移相容，或返回最短反例。正权 BRC 不处理有符号/复数相消，任何抽象同构不授予外部工程可靠性精度认证。

至少在 n=3,5,7、k=2..n、T=1..8 的明确参数网格（含有/无共因、带/不带潜在相关）形成一组模型可复算输出，比较显式有理枚举、标准条件 DP、DTMC/BDD/DBN（仅实际运行者列数字），并公开输入模型、算法版本、机器环境、输出校验与完整资源账。费用至少包括原始输入解析、生成有理权重/来源标签、载体转换、预处理、分组或动态规划、查询、多次复用、结果恢复、证书校验和整数位长/内存；核心枚举 `2^n` 或潜在路径指数成本不能被忽略。若软件不可执行，只报告已执行的数学对照与待实测的精确接口，不捏造速度或吞吐。

## Research value to preserve

单时边缘概率不足以恢复共同冲击及跨时联合事件；模型 A 和 B 给出了彼此不同的短小精确见证。公开 CCF/DBN 研究侧重可靠性概率，现有 BRC 通用端口/未来保真工作已覆盖抽象商条件，但尚需领域限定的**译码合同、查询族、最小拒绝证书及和成熟工具公平比较**。本任务的新信息缺口是具体领域的可验证集成和成本评价，不是另立通用 port theorem 或推广正权 BRC 为相位模型。

## Success, kill, and return criteria

成功：两个微型有理输入与输出获独立重算；声明查询族下得到可核验的安全商或严格不可合并见证；至少一个实际基线完成同一概率性质等值比较，提供逐项成本证据。如果首次外部基线依赖未公开数据，则独立构造透明小实例，显式保留不能复制原论文实证的边界。

否定/缩小：若 BRC 仅复述动态规划且在保真、说明力、查询复用和成本方面无实质增量，则如实返回负结果并停止应用扩张，不宣称新方法速度提升。若安全商仅对单一读出有效，不将其升级为任意未来操作的充分状态。只在真实 Result/Driver 审查下决定数学接受；Task 发布不等于 CLAIM、Result 或父目标完成。
