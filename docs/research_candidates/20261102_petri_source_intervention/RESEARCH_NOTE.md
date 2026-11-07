# 非执行研究笔记｜随机 Petri 网的隐藏来源干预残差（2026-11-02）

**状态：作者精确证明 + 有理数计算验证；候选，不是 V2 任务发布、CLAIM、Review 或 Foundation 接纳。** 本文件随研究候选 PR 暂存，不登记到 research_tasks / research_task_records。

## 外部问题和现有基线

Leemans et al., *Enjoy the Silence, Part II: Probability-Based Queries on Stochastic Labelled Petri Nets*, PETRI NETS 2025, DOI 10.1007/978-3-031-94634-9_15，已研究静默转换、重复标签的轨迹概率算法。

Orujlu et al., *Partially Observed Structural Causal Models*, UAI 2026, PMLR 337:5111–5137，https://proceedings.mlr.press/v337/orujlu26a.html，研究隐藏结构条件下节点/边级干预的可识别性。

本例针对的区别是**可见轨迹概率相同，但隐藏来源的指定删除干预使未来概率分布不同**。该现象不被宣称为原创新定理；仅作为具有精确反例的跨领域接口与后续判据测试输入。

## 六位置 1-safe 精确模型

位置依次为 p0,pa,pb,py,pz,pf。初始标记在 p0。两条静默来源转换 a:p0→pa 与 b:p0→pb 各携质量 1/2；随后模型 A 在 pa 发出 y、pb 发出 z，模型 B 将二者互换，后继事件权重均为 1。经输出位置静默到 pf，pf 可静默自循环，确保所有有限 firing horizon 都有定义。

对每个整数 T≥2，A 与 B 的完整可见词边际完全相同：
- P_A(y)=P_B(y)=1/2；
- P_A(z)=P_B(z)=1/2；
- 所有其他词的质量为 0。

T=0、T=1 的可见输出都为空词，质量 1。这由两条来源路径逐条构造直接证明，适用于全部有限 T；不是由有限枚举外推。

但来源—可见词联合权重为：

| source | A:y | A:z | B:y | B:z |
|---|---:|---:|---:|---:|
| a | 1/2 | 0 | 0 | 1/2 |
| b | 0 | 1/2 | 1/2 | 0 |

声明干预 delete(a)：原本来自 a 的 1/2 质量改为独立可见的吸收中止 ⊥，幸存 b 的原权重不归一化。在 T≥2，A 给出 P(z)=1/2,P(⊥)=1/2；B 给出 P(y)=1/2,P(⊥)=1/2。重归一化存活分支是另一观察合同，亦可判别，但此处不混用。

## 有理权重恢复恒等式

对有限来源 S 和可见词集合 Y，设 w[s,y]∈Q_{≥0} 为来源—词联合正质量。定义 P(y)=Σ_{s∈S} w[s,y]，D_s P(y)=Σ_{t∈S,t≠s} w[t,y]（删除单一来源，保留非归一化质量）。则

**w[s,y] = P(y) - D_s P(y)。**

因此在**查询族恰为全部 P 与 D_s、输出精确且作用于已声明的来源标签**时，联合表是充分的，任何保真表示必须确定其全部条目。这里的“最小”仅指查询等价的必要区分，不是存储位数最优或相对于一切未来操作的全局最小载体。

证明：上式是非负有理数有限求和逐项抵消；反向由联合表求和回答 P,D_s。普通概率总量或各方向未配对直方图无法代替这一指定来源信息。

## 与 P000/X6/BRC 的类型连接

六个 one-hot 位置标记可作为六维进取原生 X6 中**明确受限的选定锚点整数 chart 表示**，不是全体 Cell 或已验证的心跳动力学。p_i→p_j 的位移 e_j-e_i 含两轴非零分量，在 P000 中是复合方向，不是新发现的“原生斜向单步”；中间原生步骤的合法性本例未证明。firing 次数是独立时间序，⊥ 是过程读出，不是第七条空间轴。

正有理分支质量 + 真实来源标签可作为候选 BRC 带端口载体；P-D_s P 是派生观察差额，不改变正权 BRC 的基础代数。本次代码只调用 Python Fraction 作**外部基线模型精确运算**，未运行 EM 原生 typed BRC 接口，也不声称物理适用性。

## 验证、复杂度及待解决任务

同目录 checker.py 对 T=0..8 精确枚举并断言等边际、干预后的不等边际；全部 Fraction，无浮点。本玩具每步最多两个活路径；枚举一般有并发/回路的网可能指数增长。尚无超过概率自动机、Petri 可见轨迹算法或现有 EM A3 continuation-type kernel 的成本、结构或可识别性优势。

后续若重新考虑发布，须在当前原生任务机完成动态 owner/duplicate 查询，再尝试一个更严格的假设类：有限有界随机 Petri 网 + 来源/静默 ID + 指定干预语言 + 未来拼接，找出最小充分商的**新结构判据或反例**，比较既有理论与 EM A3 任务，按全部预处理、位宽、演化、输出及验证成本核算。

候选接受条件：形成原有研究不能直接覆盖的保真定理/有效反例/可复现效率差异；若仅复现基础线性恒等式则合并为既有工具外部测试，不单开任务。

## 实际状态与阻断

读取 Source main@03411e87397ccb195a0e8a46a715e023007cf646（2026-11-02 当轮）。普通 ChatGPT 私有桥接 status 请求 #6640 的内层结果为 SUCCEEDED（同逻辑会话真实 Researcher session 已登记；无 CLAIM）；tasks 请求 #6641 为 FAILED，错误：

UPSTREAM_CODE_REVIEW_REQUIRED: control_plane/check_current_control_authority.py, control_plane/check_post_cutover_publication_envelope.py, control_plane/check_remote_manual_publication_preflight.py, control_plane/research_continuation.py, control_plane/research_normative_context.py

因此**活跃 owner 动态核对、完整语义查重、V2 等效 preflight、正式发布和可领取状态都未完成**。本 PR 是非执行研究候选材料，**Task-ID / Publication-ID / CLAIM / DA / 原生发布回执均无**。

## 下一研究执行者可直接使用的完整任务提示

“基于本目录精确六位置见证，先读取 Enterprise Math 当前 P000/ACTIVE 世界观与 BRC 载体，检索 EM A3 continuation-type kernel、概率自动机可观测等价、2025 Leemans 等静默随机 Petri 概率查询与 2026 Orujlu 等因果干预。保持文献原有定理范围及外部模型输入；在固定有限有界标记网、正有理权重、指定来源删除和未来拼接下，给出一个相对于已知方法真实有增量的最小充分残差命题、严格反例或可复算性能基线。明确观察语言、干预语义、证明与费用。先用原生任务机查重/owner，正式 task publication 必须按当前 V2 预检及原生回执，不得视本 PR 为已发布任务。” 
