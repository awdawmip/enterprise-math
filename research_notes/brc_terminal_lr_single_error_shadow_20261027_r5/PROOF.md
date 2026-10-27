# R5 | 终端似然比的错误率充分性与末层碰撞的单错误率投影定理

作者侧证明与精确有理数证书；2026-10-27（Asia/Shanghai）。性质：**外部有限双测度观察树的数学结果**。Research-Activity-ID: `RA-EMR5-20261027-T11-SINGLEERROR-1244`；作者记录身份 `EM-R5-T11-SINGLEERROR-LOCAL`（客户端标签，非原生认证身份）。截至本记录，本任务没有原生 CLAIM、Result、独立 Driver 审查或 P000 原生动力学提升。

## 0. 固定来源、对象、复用边界

- GLOBAL_KNOWLEDGE_V1 读取快照：`awdawmip/chatgpt-global-knowledge@38f2ce9b16a62b599384a0021497f9ef85f293ed`。已读取规范 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`、`P000_STARTUP.json`，并比对其 `canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` 与 P000 原文件 Git blob；读取 ACTIVE 世界观。
- Enterprise Math 基线：`awdawmip/enterprise-math@313c67fe3677a609ce73cdda0c32e6ed9c303dd9`；读取 `AGENTS.md`、`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`、`definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`、`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`、`docs/PORTABLE_RESEARCH_PROTOCOL.md` 与 `control_plane/research_delivery_policy.json`。
- 前沿复用：[`research_notes/brc_n3_weak_strong_lumpability_gap_20261027_r5/PROOF.md`](../../research_notes/brc_n3_weak_strong_lumpability_gap_20261027_r5/PROOF.md)，此前14叶模型及四观测量的严格支撑差 `1/2400`。本轮新推导提供该例的更精细投影解释与可移植解析证书；再次独立计算256/32种确定性停止模式，未把已有差距冒充另一项新发现。
- **类型声明**：本研究用正有理数路径到达质量、P/Q 似然比、支路来源与占用质量；与 BRC 的有类型正质量记账原则兼容。样本时间 `t` 是外部观测序号，`Y=P/Q` 是统计读出，不是心跳世界原生六维坐标或物理时间。对六维 Cell 路径的原生传输仍需要显式嵌入、观察与后续运算保持证明。

## 1. 定义

给定深度为 `N` 的有限无行动反馈观察树，叶路径 `\omega` 上严格正的两个概率 `P(\omega),Q(\omega)`，总质量各为1。设终端完整路径似然比 `Y(\omega)=P(\omega)/Q(\omega)`。观察/继续动作不会改变该固定观察树的两种物理概率。一个完整历史策略在每个节点随机选择停止判 P、停止判 Q、继续，终端强制停止；局部随机化在两种假设下服从同一条件法则。

压缩策略只能依赖 `(t,r_t)`，其中 `r_t=P(h)/Q(h)` 是物理历史的精确似然比。它使用该节点的局部随机动作，**不保留初始持久随机种子**。四个观察量按次序定义为

\[
O=(e_P,e_Q,T_P,T_Q)
=\big(P(D=Q),Q(D=P),E_P\tau,E_Q\tau\big).
\]

记完整策略和压缩策略的像为 `O_full`、`O_LR`；错误率二元投影为 `E`，时间二元投影为 `T`。

## 2. 定理 A：任意有限期限，终端似然比可完整恢复两个错误率

**命题。** 对任意 `N`、任意严格正有限双测度树、任意完整历史行为策略，都存在一项**只在终端 `(N,Y)` 判决**的无持久种子策略，使其 `(e_P,e_Q)` 与前者完全一致。因而

\[
\boxed{\operatorname{pr}_{e_P,e_Q}O_{\mathrm{full}}
=\operatorname{pr}_{e_P,e_Q}O_{\mathrm{LR}}=\mathcal E.}
\]

若 `\mathcal Y` 是不同终端似然比的有限集合，`q_y=Q(Y=y)`，则还有一个完全可计算的表示：

\[
\boxed{\mathcal E=\left\{\left(\sum_{y\in\mathcal Y}yq_y\theta_y,\ 
1-\sum_{y\in\mathcal Y}q_y\theta_y\right):\ 0\le\theta_y\le1\right\}.}
\]

它是一个有限二维 zonotope；若 `P,Q` 有理，则是有理凸多面体。对**任意有符号实数** `\alpha,\beta`：

\[
\boxed{\min_{O\in O_{\rm full}}(\alpha e_P+\beta e_Q)
=\min_{O\in O_{\rm LR}}(\alpha e_P+\beta e_Q)
=\beta+\sum_yq_y\min(0,\alpha y-\beta).}
\]

**证明。** 将原策略 `\pi` 的随机停止判决 `D` 定义到每条完整叶路径上：对即使早停的路径也继续抽取尚未看的物理后缀，但保留早先判决。此延拓仅用于数学耦合，不要求原策略实际追加观测。独立动作硬币的条件分布不随 `P/Q` 假设改变。对每个 `y` 令

\[
\theta_y=Q_\pi(D=Q\mid Y=y),\qquad q_y=Q(Y=y)>0.
\]

在 `Y=y` 的所有完整路径上都有 `dP/dQ=y`，所以

\[
P_\pi(D=Q,Y=y)=yQ_\pi(D=Q,Y=y)=yq_y\theta_y.
\]

从而 `e_P=\sum_y yq_y\theta_y`，`e_Q=1-\sum_yq_y\theta_y`。改用“始终观察到 N，只按 Y 以概率 `\theta_y` 判 Q”的压缩策略，即同时复制两项错误率；反向包含显然。将有符号线性目标写作 `\beta+\sum_yq_y(\alpha y-\beta)\theta_y`，在每个独立区间 `[0,1]` 上逐项取最小值即得公式。全程不需要初始公共随机种子。证毕。

**先验知识定位。** 终端似然比的二元判决充分性属于经典 Neyman–Pearson/统计实验思想；这里给出完整随机停止策略的精确可达集合版本，**不主张经典基础定理本身是原创**。外部背景：[Penn State STAT415 Neyman–Pearson](https://online.stat.psu.edu/stat415/lesson/26/26.1)；随机策略占用质量的相关背景：[Laroche–Tachet des Combes, ICML 2023](https://proceedings.mlr.press/v202/laroche23a.html)。本证明独立于这些网页结论。

## 3. 定理 B：碰撞只在倒数第二层出现时，双时间观测量完全保真

**命题。** 假定在所有非终端且不是倒数第二层的时间 `0\le t\le N-2`，每个物理历史的 `(t,r_t)` 在该时层唯一；仅 `t=N-1` 的历史可以共享相同似然比（终端可以任意合并）。那么对任意完整历史行为策略 `\pi`，存在无持久种子的 `(t,r)` 策略 `\widehat\pi`，使

\[
\boxed{(T_P,T_Q)(\widehat\pi)=(T_P,T_Q)(\pi).}
\]

其共同时间像 `\mathcal T` 是凸多面体；若物理质量有理，它是有理凸多面体。

**构造与证明。** `0\le t\le N-2` 没有 `(t,r)` 碰撞，压缩策略逐节点直接复制完整策略的所有停止/继续动作（停止判决标签可以随后更换）。因此所有 `t=N-1` 历史的真实 `Q` 到达质量 `m_h` 在两种策略中一致。对一个末层相同似然比类 `G_r`，记原策略继续概率 `c_h`，令

\[
M_r=\sum_{h\in G_r}m_h,\qquad
\widehat c_r=\begin{cases}
\sum_{h\in G_r}m_hc_h/M_r,&M_r>0,\\
0,&M_r=0.
\end{cases}
\]

`P` 到达质量与 `Q` 质量逐历史相差同一似然比 `r`，故该类在两种策略中的继续 `Q` 质量均为 `\sum m_hc_h`，继续 `P` 质量均为 `r\sum m_hc_h`。在第 `N` 层所有路径强制停止，末层的后继具体概率核不再影响**终端时刻的存活质量**。较早存活质量已相同，因而由恒等式

\[
E_\mu\tau=\sum_{t=0}^{N-1}\mu(\tau>t),\quad\mu\in\{P,Q\},
\]

两项期望精确相同。对完整历史策略，以每个物理节点到达/继续质量为变量的线性流守恒方程，精确表示全部可行随机策略；其有界可行域是多面体，投影到两项时间期望仍为多面体。压缩时间像与完整时间像相同，故也凸；有理数据时有理。证毕。

**边界。** 本结论关涉 `(T_P,T_Q)`；末层不同隐藏历史的下一观察核会改变终端错误率与时间量的联合可达性，因而不能由此推出四元像完全相等。若在 `t\le N-2` 已有碰撞，前层动作的共享约束使本构造需要额外核条件。

## 4. 推论：两种三元投影相等，但四元可达像可以不同

在定理 B 条件下，给定任何目标时间对 `T\in\mathcal T`，压缩策略先实现这组时间期望；接着令所有停止节点均以固定概率 `u` 判 Q，则无论停止时间分布如何，总有 `e_P=u`。令所有停止节点均以概率 `v` 判 P，则总有 `e_Q=v`。故

\[
\boxed{\operatorname{pr}_{e_P,T_P,T_Q}O_{\rm full}
=\operatorname{pr}_{e_P,T_P,T_Q}O_{\rm LR}
=[0,1]\times\mathcal T,}
\]
\[
\boxed{\operatorname{pr}_{e_Q,T_P,T_Q}O_{\rm full}
=\operatorname{pr}_{e_Q,T_P,T_Q}O_{\rm LR}
=[0,1]\times\mathcal T.}
\]

因此，若有严格的**有符号线性支撑差**，使用 `\alpha e_P+\beta e_Q+\gamma T_P+\delta T_Q` 作为目标时，`\alpha\beta\ne0` 是这个拓扑下发生差距的必要条件；任何只涉及一个错误率和双时间的线性目标，其两类全局最优值必相同。本推论不声称只依赖这两个错误率加某一个时间的三元投影也必相等。

## 5. 14叶正有理数实例：四元分离与所有上述低维投影恢复并存

重新复用前沿的14叶双测度树：初层 `Q(a)=1/3,r_a=2`，`Q(b)=2/3,r_b=1/2`。`a,b` 分别以 `(1/8,1/8,3/4)` 到 `(u,v,w)`；第二层绝对似然比分别是 `a:(1,1,7/3)`、`b:(1,1,1/3)`。四个 `u/v` 节点的终端似然比集合 `Y=(1/2,1,3/2)`，条件 `Q` 核 `(s,1-2s,s)`，其中

\[
(s_{au},s_{av},s_{bu},s_{bv})=(1/10,2/5,1/5,3/10).
\]

两处 `w` 节点各只有一个保持似然比的终端子节点。叶质量均严格正，`P(\omega)=Y(\omega)Q(\omega)`，两测度归一化与每个父节点的似然比守恒由附件精确验证。

早停完整策略：根继续；`a` 在时刻1判 P、`b` 继续；第二层 `bu` 判 P、`bw` 判 Q、`bv` 继续；`bv` 末层当 `Y=1/2` 判 Q，其他判 P。它实现

\[
O_F=\left(\frac{43}{240},\frac{19}{40},\frac{17}{12},\frac74\right).
\]

终端似然比的 `Q` 分布为

\[
(q_{1/3},q_{1/2},q_1,q_{3/2},q_{7/3})=(1/2,1/16,1/8,1/16,1/4).
\]

根据定理 A，固定全部路径持续观察到时刻3，再选 `\theta_{1/3}=1,\theta_{1/2}=2/5`、其余 `\theta_y=0`，便有

\[
O_{\rm term}=\left(\frac{43}{240},\frac{19}{40},3,3\right).
\]

因此两项错误率**同时**精确恢复；时间已发生改变。

根据定理 B，另一压缩策略在 `a` 早停、`b` 继续，于第二层唯一可达的 `r=1` 合并类采用继续概率 `1/2`：两个真实历史 `bu,bv` 的 `Q` 到达质量各是 `1/12`，原策略仅在 `bv` 继续，故合并后总继续 `Q/P` 质量均为 `1/12`。所得双时间期望为 `17/12,7/4`。再以统一概率 `43/240` 判 Q，或统一概率 `19/40` 判 P，分别得到

\[
O_{e_P,T}=\left(\frac{43}{240},\frac{197}{240},\frac{17}{12},\frac74\right),\quad
O_{e_Q,T}=\left(\frac{21}{40},\frac{19}{40},\frac{17}{12},\frac74\right).
\]

可见两种三维投影均精确保真。与此同时，复核前沿的有符号目标

\[
J=e_P+\frac34e_Q+\frac{11}{200}T_Q
\]

取得完整最优 `379/600`，压缩最优 `1517/2400`，严格差 `1/2400`。该差距说明 `O_F` 的**完整四元向量**无法由任意实数局部随机化的压缩策略实现，虽然上述各投影存在精确恢复。由于本目标对共享局部动作概率逐变量多重仿射，其全局极小值在确定性顶点上实现；本轮用 Fraction 穷举256种完整、32种压缩停止模式，独立验证该差距。

无时间权重时，对 `(\alpha,\beta)=(1,3/4)` 应用定理 A 的精确错误率支持公式，得到共同最优 `101/192`。这一计算说明上面的严格差距是**错误率与采样时间的联合约束**，而非终端错误率本身难以由似然比表达。

## 6. 验证强度、方法来源、后继义务

`VERIFY.py` 使用 Python 3 标准库 `fractions.Fraction`，逐叶检查概率正性、归一化、父子似然比守恒、原完整策略四向量、终端随机判决、两个时间保持压缩策略、错误率支持值和256/32模式下的四元支撑差。实际输出 `EXACT_OUTPUT.txt` 以 `ALL EXACT CHECKS PASSED` 结束。该执行覆盖上述具体14叶模型；定理 A/B 的任意 `N` 与实数局部随机化范围来自明确的耦合和占用流代数证明。

**已解决的局部问题**：给定末层碰撞模型，哪些坐标投影完全可以恢复？答案为错误率二元投影（任意 `N`）、时间二元投影与两种单错误率/双时间三元投影（碰撞仅在倒数第二层的模型）。

**母问题仍开放**：寻找 `conv(O_LR)=O_full` 但 `O_LR\ne O_full` 的有限正有理数模型，或者证明非平凡类别不可能。下一步应精确分析同时包含两项错误率及至少一项时间读数的耦合约束；先完成四坐标有理凸包包含证明，再寻全实数多项式不可实现证书。参见 `NEXT_TASK.md`。

本结果是**作者侧数学证明+精确计算+可追踪来源**；正式原生 claim/result、独立审核及原生心跳传输需要各自的实际证据。
