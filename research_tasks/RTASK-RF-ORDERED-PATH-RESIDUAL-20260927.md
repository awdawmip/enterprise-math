<!-- ENTERPRISE_MATH_TASK_V1
{"task_id":"RTASK-RF-ORDERED-PATH-RESIDUAL-20260927","title":"端点条件观察下的有序路径残差与 BRC 联合压缩","kind":"RESEARCH","owner":"taskbook/unassigned","base_state":"READY","priority":"P2","leverage":"MEDIUM","frontier":"T0 已能组合单条仿射作用，T3 已有回路/路径差；但端点筛选后的分布观察不能由端点边缘和作用边缘分开决定，需确定可保真压缩的联合信息。","next_action":"对正词 AB 与 BA，取位移 d_A=(1,0),d_B=(0,1) 及两个整数剪切作用，计算同端点的不同最终作用；再检验候选联合统计在追加 A/B 后是否闭合。","dependencies":[],"source_refs":["awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:enterprise_toolbox_registry.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:research_notes/TOOL_DISCOVERY_NATIVE_ORIENTED_MATROID_CIRCUIT_CALCULUS_RESULT_20260822.md","https://ems.press/journals/rmi/articles/5137","https://arxiv.org/abs/2412.14723"],"evidence_status":"PUBLISHED_RESEARCH_QUESTION_NOT_RESULT","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["residual-fidelity","finite-certificate"],"created_by_role":"RESEARCHER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RTASK-RF-ORDERED-PATH-RESIDUAL-20260927","parent_objective_id":"OBJ-RESIDUAL-FAITHFUL-DISCRETE-RELATIONS","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","origin_kind":"DIRECT_USER_DIRECTION","task_lineage":"INTEGRATION","parent_task_id":null,"successor_gate":null,"policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73","review_state":"PASS","temporary_overrides":[]}}
-->

# 有序路径：端点条件化不能拆掉联合关系

## Mother question
终点相同的路径可能产生不同作用。经典粗糙路径和迭代签名已经保存次序信息，现有 T3 也能表示带类型的路径差；本任务研究它们与 BRC 正质量观察的具体接口，尤其是按终点筛选以后哪些联合统计仍然充分，而非重新命名路径记忆。

## Frozen inputs and scope
先固定字母 A,B 的正词，总长至多 T。位移标签 d_A=(1,0),d_B=(0,1) 只是形式整数地址，不声明额外空间维度。内部向量 y in Q^2，初值 y_0=(1,1)。A 的仿射线性部分 U=((1,1),(0,1))，B 为 V=((1,0),(1,1))，平移均为零；次序依现有 T0 约定，先 A 后 B 对应 VU。各步使用指定的、状态无关的正有理 BRC 权重，支持逐步不同权重。
精确支路原子为 [w,d,L,b]。串联先左后右：[w,d,L,b]*[v,e,K,c]=[wv,d+e,KL,Kb+c]，保留权重、端点、作用关联。观察是每个指定终点 z 的未归一化质量及 y 的次数<=2 矩；仅在质量非零时可取条件比值。允许继续追加指定 A/B 作用包；本项不包含路径特异或状态相关未来权重。
比较端点、字母计数、二阶词统计、回路信息与完整端点-矩联合统计。二阶词统计明确为 AA/AB/BA/BB 有序子序列计数，不把它冒充任意阶连续签名。原始 U,V 是 T0 仿射接口的代数输入，不是用普通矩阵演化替代原生物理运算。

## Hard target and required outputs
AB 与 BA 是启动见证。必须进一步给出端点条件矩族的精确串联/分支组合律，以及明确模型中状态维数、整数位数、构造和查询成本的参数界；单词作用可用一个矩阵表示不等于整个条件分布可用常数内存表示。
至少选择并完成一项非平凡判别：在总长 T 的同计数/同二阶词统计类中构造不同条件观察的参数族，证明固定低阶统计不充分；或证明某个明确受限作用族下低阶统计充分，并展示其出界反例。相同位移边缘和相同作用边缘能否保留条件观察必须用联合见证检查。可用 nilpotent 受限族作对照，但必须完整声明新的作用输入，不改变原 U,V 问题后声称原题已解决。
端点索引的矩生成函数和全端点动态规划是已有思想的实现基线；要求给出可核验的必要性/失效边界或严格成本改进，不能仅呈现又一个全枚举算法。小词长穷举只验证所述有限范围；T 的多项式复杂度不自动是 log T 或整数输入长度的多项式。

## Research value to preserve
将 T0 作用矩、T3 带类型路径差和条件观察联合起来，说明何时一个残差可以安全商掉。原工具的接受范围各自保持，不能从有符号位移的抵消推出正质量消失。本项是新的端点条件分布集成问题，不接管现有 QFT 行查询任务，也不以不同名称重发其困难纤维求和问题。

## Success, kill, and return criteria
成功为可验证的联合压缩定理加必要性界，或对固定次序统计的参数化反例/无压缩界。只复述 AB!=BA、Chen 型组合、单词矩阵积或缓存全部词不算完成。完整保留量、零残差和受限安全压缩均可成立，不能先验要求其中一种。若发现已有完全等价的有效工具则直接复用，记录不同观察/成本边界；交付时说明实际检查范围和未证的新颖性。
