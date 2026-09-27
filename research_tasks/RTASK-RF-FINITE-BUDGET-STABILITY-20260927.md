<!-- ENTERPRISE_MATH_TASK_V1
{"task_id":"RTASK-RF-FINITE-BUDGET-STABILITY-20260927","title":"有限记忆与修复预算下的残差稳定性边界","kind":"RESEARCH","owner":"taskbook/unassigned","base_state":"READY","priority":"P2","leverage":"MEDIUM","frontier":"不能从每个有限制备有正逸出，推断统一正下界；也不能从每个有限时域可稳定，推断一个有限资源状态能永久稳定。需将观察记忆、修复代价和量词顺序同时固定。","next_action":"在所给五状态有理模型取 epsilon=1/16,q=1/2,eta=1/8,T=5,B=1，枚举预算合法的确定性观察策略，比较保留上一线索与丢弃线索的存活率。","dependencies":[],"source_refs":["awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:enterprise_toolbox_registry.json","awdawmip/enterprise-math@71c2ed5444fab5388f9e2c8dc1414cb55f46f400:research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md","https://arxiv.org/abs/1708.02235"],"evidence_status":"PUBLISHED_RESEARCH_QUESTION_NOT_RESULT","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["residual-fidelity","finite-certificate"],"created_by_role":"RESEARCHER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RTASK-RF-FINITE-BUDGET-STABILITY-20260927","parent_objective_id":"OBJ-RESIDUAL-FAITHFUL-DISCRETE-RELATIONS","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","origin_kind":"DIRECT_USER_DIRECTION","task_lineage":"NEW_DIRECTION","parent_task_id":null,"successor_gate":null,"policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73","review_state":"PASS","temporary_overrides":[]}}
-->

# 有限预算稳定性：量词、记忆和修复都要付账

## Mother question
保留过去仍有用的线索，能否在同样资源下延长可验证的保持时间？是否只是把成本藏进了控制器、计时或条件修复？经典随机控制和亚稳态已有成熟方法，本任务不声称“有限时间稳定”是新概念，而以一个完全声明的有限族寻找精确的记忆收益或无收益边界。

## Frozen inputs and scope
五状态 C0,C1,H0,H1,F。初态 C0,C1 各质量 1/2；F 为失败吸收态。C_b 的观察公开 b，下一步确定转到 H_b；H0,H1 共享观察 H。H 状态可选普通动作 a in {0,1}：a=b 时以 1-epsilon 存活，否则以 1-q 存活；失败转 F，存活后以 eta 翻转 b、以 1-eta 保持。也可选 repair，消耗一个预算单位，确定转到 C_b；此动作占用一个真实模型步，不是免费瞬时重置。参数为有理数，0<epsilon<q<1，0<=eta<=1/2。T 为总步数，B 为总修复次数上限。
比较预先声明的控制器类：政策可读取当前观察、步号、剩余预算和至多 m 位额外记忆。m=0 仍拥有步号/预算侧信息，必须与 m>0 共享；不能让对照组失去它们，也不能把预算编码产生的信息隐藏不报。私有随机性如允许，须在两组同样声明；启动单元先限确定性策略。安全集为除 F 外所有状态；目标是存活至 T 的概率，不是每条路径都安全。
所有转移为有限正有理 BRC 质量包，零概率支路省略。这里预算是操作成本，不自动对应物理能量或温度；不使用相位相消解释概率质量损失。该有限族独立于旧未审查物理候选，不接管其任务或把旧数值升格。

## Hard target and required outputs
先取 epsilon=1/16,q=1/2,eta=1/8,T=5,B=1，给出至少两个明确策略的逐支路质量证书，并精确求出声明策略类内的最优值；有限穷举必须列出策略完备性定义。随后对至少一个非退化参数子族，证明 m=0 与有限 m 的最优保持概率、所需预算或时域之间的严格差距及同阶/匹配界，或证明在声明的侧信息条件下没有优势。
以显式 Bellman/策略证书为验证基线，不把常规动态规划本身当作新增工具。控制器内存、预算计数器、计时器、初态制备及数值位数全部计成本。先考虑 eta=0 或固定正 eta 的有理子族时必须标明适用边界；repair 的占步效应不能被误说为提高物理寿命。
分别检验固定 B 的长时域、随 T 增长的 B，以及允许参数 epsilon 随准备资源变化的三种不同问题。二态基线 p_B=1/(B+1) 只用于展示“每个 B 有正逸出但 inf_B p_B=0”的量词差异，不能作为五状态族的证明或完成交付。新目标需超过该基线。

## Research value to preserve
将“必须零逸出才有稳定结构”的旧倾向改为可量化的保持-残差-资源关系，同时防止一味保存历史。可复用输出是有显式观察类的有限预算稳定性证书或障碍，不是一般永久稳定性断言。物理应用须另建与实际 BRC 原生算子的对应，不由本模型自动获得。

## Success, kill, and return criteria
成功为一个参数族的可证权衡或否定边界，附可独立重算的小型有理证书。只显示一组数值更好、忽略失败分支、免收修复成本或混淆量词均不通过。若预算/时钟已经编码所需记忆而使拟议差距消失，保留这一反例并改为准确的无优势结论；不得悄悄削弱对照策略。结束时列明证明范围、实际执行项及一个仍有信息增益的问题。
