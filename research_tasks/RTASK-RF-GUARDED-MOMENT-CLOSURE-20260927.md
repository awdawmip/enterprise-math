<!-- ENTERPRISE_MATH_TASK_V1
{"task_id":"RTASK-RF-GUARDED-MOMENT-CLOSURE-20260927","title":"带守卫和状态相关权重的 BRC 线性统计闭合边界","kind":"RESEARCH","owner":"taskbook/unassigned","base_state":"READY","priority":"P2","leverage":"MEDIUM","frontier":"已有固定权重仿射二阶矩收缩；守卫和状态相关权重下，分布的最小充分线性统计及其随时域增长的精确边界尚待确定。","next_action":"对 M=4、T=2，写出 A(x)=min(x+1,M)、R(x)=M-x 的回拉观察张成空间；构造删除一个必要基函数后的非负分布分离见证。","dependencies":[],"source_refs":["awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:enterprise_toolbox_registry.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:lineage_e002_predictive_quotient.json","https://arxiv.org/abs/1708.02235"],"evidence_status":"PUBLISHED_RESEARCH_QUESTION_NOT_RESULT","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["residual-fidelity","finite-certificate"],"created_by_role":"RESEARCHER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RTASK-RF-GUARDED-MOMENT-CLOSURE-20260927","parent_objective_id":"OBJ-RESIDUAL-FAITHFUL-DISCRETE-RELATIONS","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","origin_kind":"DIRECT_USER_DIRECTION","task_lineage":"INTEGRATION","parent_task_id":null,"successor_gate":null,"policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73","review_state":"PASS","temporary_overrides":[]}}
-->

# 带守卫的分布状态：最小充分线性统计

## Mother question
经典连续降阶已经研究记忆项和矩闭合；本任务不宣称这些概念是新发明。问题是：在下述有限、精确的 BRC 作用族中，保留多少线性统计，才能在指定未来词长内准确回答期望观察？现有点状态预测商不能直接当成分布矩压缩：一个一阶观察可区分所有点，却仍不能恢复任意分布。

## Frozen inputs and scope
令 M>=2，X_M={0,...,M}，初始质量 mu 为非负有理函数，不必归一化。观察 O={1,x,x^2}。作用 A(x)=min(x+1,M)、R(x)=M-x，均为全定义整数状态更新；以显式守卫将 A 写为分段仿射 BRC，而非把分数读数当作原生位移。先处理任意长度至多 T 的 A/R 词，再加入随机作用 B：在 x 处以 x/M 选 A，以 1-x/M 选 R；零权支路省略。B 的两个概率是同一完整状态的联合信息，不可独立抽样权重与作用。
定义 P_a^*f(x) 为作用 a 后 f 的条件期望，V_T=span_Q{P_w^*f: f in O, |w|<=T}。目标的“最小”仅指对所有初始 mu 有效的线性质量统计数，包括总质量坐标；归一化后可另列仿射维数。不声称是任意非线性编码的最小比特数。
既有输入为 T0 的仿射 EffectHistogram/MomentState 和 E002 的有限行为等价工具。前者是有来源的研究工具候选，后者的经典划分算法是先行工作；本任务不提升其接受等级。有限直方图和逐词全枚举是比较基线，不是新成果。公开 MZ 文献仅作对照，不能将连续目标侧定义倒灌成原生公理。

## Hard target and required outputs
先回答 M=4,T=2 的明确问题，再给出 A/R 族至少一个随 M,T 变化的闭合基、秩公式或匹配上下界。可优先用端点移动产生的离散样条/截断多项式基，但不得只换名重述 span 定义。证明每个保留统计的更新以及允许的未来范围；加入 B 后须给出基仍充分的证明或一个精确反例，不能照搬固定权重结论。
交付可检查的有理秩证书；对每个声称必要的统计给出删减后的核向量，并拆成非负质量 mu,nu，使当前压缩相同而某个允许未来观察不同。总质量相同或归一化条件必须显式检查。小型 M=2..16,T=0..6 的结果只作证书样本，不替代参数命题。
报告构造、存储、查询和大整数比特增长；完整 M+1 状态展开是合法退路，但不得称为常数成本压缩。符号推导、有限证书或反例均可推进；实际未执行的实现检查保持未执行。

## Research value to preserve
有用增量是守卫/权重关联导致的精确增维律或可证受限闭合，不是再次证明经典有限维秩判据。按 T0 扩展接口给出输入、输出、组合律及失效观察；不建立重复顶层工具。此项是两个已有工具在新分布观察问题上的集成，不是某个已冻结任务换名续阶段。

## Success, kill, and return criteria
成功：一个非平凡参数族的闭合基及必要性见证，或证明指定压缩目标必须随 M/T 增长的下界。只列小表、只复述二阶仿射公式、只保存全部历史不算完成。若发现精确相同问题已有有效结果，复用并返回其来源和剩余差异；若拟议基失败，保留最小反例，改写为否定边界而非强行清零。零残差和安全精确压缩均允许。结束本单元须交付已证范围、未决项和一个具体下一问题。
