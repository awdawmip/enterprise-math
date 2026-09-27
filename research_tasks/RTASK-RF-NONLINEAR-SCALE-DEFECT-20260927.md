<!-- ENTERPRISE_MATH_TASK_V1
{"task_id":"RTASK-RF-NONLINEAR-SCALE-DEFECT-20260927","title":"非线性守恒更新的跨尺度残差与局部闭合","kind":"RESEARCH","owner":"taskbook/unassigned","base_state":"READY","priority":"P2","leverage":"MEDIUM","frontier":"线性平均与非线性通量不交换；尚未在声明的有限守恒族中分清块内矩、边界关联和跨尺度组合误差各需保留什么。","next_action":"在四点周期环比较 u=(1,0,0,1) 与 v=(0,1,1,0)，两两平均相同；以 lambda=1/2 写出一次细更新后的块均值并定位被遗漏的边界通量。","dependencies":[],"source_refs":["awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:enterprise_toolbox_registry.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md","https://arxiv.org/abs/1708.02235"],"evidence_status":"PUBLISHED_RESEARCH_QUESTION_NOT_RESULT","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["residual-fidelity","finite-certificate"],"created_by_role":"RESEARCHER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RTASK-RF-NONLINEAR-SCALE-DEFECT-20260927","parent_objective_id":"OBJ-RESIDUAL-FAITHFUL-DISCRETE-RELATIONS","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","origin_kind":"DIRECT_USER_DIRECTION","task_lineage":"NEW_DIRECTION","parent_task_id":null,"successor_gate":null,"policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73","review_state":"PASS","temporary_overrides":[]}}
-->

# 非线性守恒族的跨尺度缺陷

## Mother question
当我们先更新细状态再取块均值，与先取均值再更新粗状态不一致时，哪些差异必须携带到下一步？只保留均值或块内方差能否闭合，还是还需要相邻块边界的排列与关联？本任务是一族有限代数模型的研究，不是宣称已解决连续流体方程或证明原生物理定律。

## Frozen inputs and scope
周期环含 n 个点，n 为 4 的倍数；u_i in [0,1] intersect Q，0<lambda<=1 为有理数。定义 F_lambda(u)_i=u_i-lambda*(u_i^2-u_(i-1)^2)/2，所有下标模 n。Q 按 (0,1),(2,3),... 两两取平均；同一步物理比较的粗作用取 F_(lambda/2)。先验证更新的区间不变性及总和守恒，不将其当成未声明前提。Q 是观察而非把原生 Cell 任意细分的许可。
定义 D_Q(u)=Q F_lambda(u)-F_(lambda/2)(Qu)。再取第二层 Q，比较 F_(lambda/4)。所有连续尺度、熵、PDE 解释只作待证明的有效对应；本轮只固定有限有理输入和精确观察。现有 T0 仿射作用不能直接执行该非线性族：先给出带正确类型和证明的 BRC 扩展或保留符号关系，不用普通数值推进器冒充已完成的原生计算。

## Hard target and required outputs
第一见证固定 n=4,lambda=1/2，u=(1,0,0,1)，v=(0,1,1,0)。检查 Qu=Qv，逐项计算 QF_lambda(u),QF_lambda(v)，明确边界排列如何重现为不同未来读数。该见证只是启动单元，不是整个任务的完成标准。
推导一般 n 的精确 D_Q 表达与两层组合律 D_21(u)=Q_2 D_1(u)+D_2(Q_1u)，各层参数和类型必须一致。组合恒等式本身是基线；新增目标是至少一个可压缩边界/关联统计族的闭合证明和有限 T 误差传播界，或一个表明仅凭指定块内有限阶矩不能闭合的参数化反例族。
分别计量空间支撑、块尺度、T、表示位数和残差界。须指出误差传播在哪种范数及条件下稳定，是否随 T/尺度增长；不得用一轮细网格匹配推论全部时域。给出精确质量守恒证书、四/八点最小反例以及可独立验证的有理输入输出。声称熵不增、连续极限或精度优势时须另给证明，不把它们列为既成结果。

## Research value to preserve
保留的是非线性粗化遗漏的结构，而不只是把浮点误差改名为残差。该问题将尺度组合、BRC 的联合权重/作用信息和有限证书结合，可直接区分必须保留的边界信息与可安全舍弃的细节。文献中的守恒离散、滤波应力、MZ 记忆已存在；新颖性只可能来自本族的可计算闭合/障碍与带成本接口。

## Success, kill, and return criteria
成功必须超过一个四点算例：交付有参数的闭合/稳定界或明确局部闭合下界。若只可能保存全细网格，完整说明成本和反例，不称为突破。若更新族的目标性质不成立，保留反例并限缩结论，不改变方程后沿用旧证书。没有正则性/一致紧性等额外条件，不声称解决一般非线性弱极限、奇点或湍流。任务结束保留所有已证范围和下一可检验问题。
