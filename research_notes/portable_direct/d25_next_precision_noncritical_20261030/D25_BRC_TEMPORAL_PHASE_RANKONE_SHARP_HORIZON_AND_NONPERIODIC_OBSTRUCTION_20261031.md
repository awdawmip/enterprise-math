# D25/LIFT — BRC 时间相位残差：周期秩一未来观察界、逐周期锐性与非周期障碍

**日期：**2026-10-31。**类别：**独立作者侧辅助数学研究，`AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。**冻结科学 Source pin：**`c47e13e4aba0e006366f989d6334d443f6333ae3`（不随控制 HEAD 更新）。**母目标：**在保留正整数 BRC 来源重数、观察端口、共享隐藏标签和操作时序的条件下，为未来充分残差给出可证明的有限条件或精确障碍。没有将辅助有限状态索引解释为原生六轴空间维度。

## 1. 研究接口与上一单元的适用范围

前序同 PR 的 `D25_BRC_TRANSITION_RANK_FINITE_OBSERVER_HORIZON_AND_SHARP_STATIONARY_LIFT_20261031.md` 对**时间齐次**转移 `B_y=diag(J(y))T` 证明了转移秩有限观察界。原生《HEARTBEAT_WORLD_NATIVE_X6_TIME》明确把时间作为独立有序事件参数，`fixed_heartbeat_program=null`，因此不能由已有坐标/时间定义自动推出 `B_{t,y}=B_y`。本单元研究时间变化的额外必要信息，并给出一种可核验的周期性恢复条件。

令 `H∈{A,B}` 是隐藏来源类型，`Y` 是有限联合观察端口集合。每个系统具有 `m_H` 个来源标签，初始整数行向量 `a_H>0`；每次输出 `y` 保留原始非负整数路径重数 `J_{H,t,i}(y)>0`，之后按严格正整数矩阵 `T_{H,t}>0` 更新隐藏标签。定义

\[
B_{H,t,y}=\operatorname{diag}(J_{H,t}(y))T_{H,t},\qquad
F_H(y_1\cdots y_n)=a_H^\top B_{H,0,y_1}\cdots B_{H,n-1,y_n}\mathbf 1,\qquad F_H(\epsilon)=a_H^\top\mathbf1.
\]

原始路径重数均为正整数；本文为**判等**临时在 `Q` 上使用线性空间或比值，既不把分数作为原始路径重数，也不把隐藏状态与 native X6 位置认同。观测范围为时间有序的完整联合词，允许重复任意长度；无直接隐藏标签读口、无干预改变 `T_{H,t}` 的额外操作。后者若存在，需要新的对应/重证。

## 2. 定理 A：任意时间变化时，隐藏秩单独不足以给未来界

**命题。**对于任意整数 `N≥1`，存在两种系统，各仅有**一个**隐藏标签、所有转移 `T_t=[1]`（逐时刻有理秩为1）、四个严格正整数观察端口，每时刻的总输出路径质量均为5；二者在全部长度小于 `N` 的观察历史完全相同，而在长度恰好 `N` 首次不同。

**整数构造。**置 `Y=(00,01,10,11)`、`a_A=a_B=[1]`。系统 A 在每个时间 `t` 的四端口权为 `(2,1,1,1)`；系统 B 除 `t=N-1` 外均相同，唯在该时刻的四端口权为 `(1,2,1,1)`。于是

\[
F_A(u)=F_B(u)\quad(|u|<N),\qquad
F_A((00)^N)=2^N,\quad F_B((00)^N)=2^{N-1},
\]

且每种系统对全部长度 `t` 的词求和恒为 `5^t`。构造中的状态转移、初始整数质量及每时刻总质量都完全匹配，分裂仅来自有序时间观察端口。由于 `N` 任意，**不存在只依赖逐时刻隐藏矩阵秩1的统一有限未来观察界**。这不是否定任何固定有限时间窗，而是说明时间变化的操作约束不可省略。

## 3. 定理 B：周期时间变化可提升为齐次、保留整数来源

假定各系统的整个**观察发射与转移**联合序列具有一个**已证最小或非最小正周期** `p_H`：`B_{H,t+p_H,y}=B_{H,t,y}` 对所有 `t,y`，初始相位固定为0。设

\[
r_{H,s}=\operatorname{rank}_{\mathbb Q}(T_{H,s}),\quad
\rho_H=\sum_{s=0}^{p_H-1}r_{H,s},\quad R=\rho_A+\rho_B.
\]

构造 `p_Hm_H` 维相位提升矩阵 `\widetilde B_{H,y}`，仅将相位 `s` 的正整数行映射到相位 `s+1\pmod{p_H}`，相应矩阵块为 `B_{H,s,y}`；初始行 `\widetilde a_H` 仅在相位0持有 `a_H`，终止列在全部相位取1。

则对每个观察词逐项有**相同的带重数整数路径数**：

\[
F_H(u)=\widetilde a_H^\top\widetilde B_{H,u}\mathbf 1.
\]

`\widetilde B_{H,y}` 的行空间在所有 `y` 下恒为同一空间 `V_H=Row_Q(\widetilde T_H)`，其维数恰为 `\rho_H`：因为 `diag(J_{H,s}(y))` 全对角正数可逆、各相位到不同下一相位的块不重叠。对于差分联合系统，所有非空词对应的行向量都进入维数 `R` 的 `V_A⊕V_B`。线性空间增长与闭包给出：

\[
\boxed{F_A(u)=F_B(u)\text{ for every }0\le |u|\le R
\quad\Longrightarrow\quad F_A(u)=F_B(u)\text{ for all finite }u.}
\]

如果另外 `a_H^\top∈Row_Q(T_{H,p_H-1})`（使相位0初始行属于相位提升的转移行空间），则上界可缩为 `R-1`。这个通用周期结果仅是前序时间齐次线性闭包法的**严格整数保真相位提升应用**；不宣称一般 `R` 上界锐利或原生时间自动周期化。

## 4. 定理 C：共同周期、每相位秩一时，最优界恰好 `p+1`

两种系统均为同一周期 `p≥1`、同一已知初始相位0，每相位严格正整数转移的有理秩为1。对各系统存在正整数列 `u_s,v_s` 使 `T_s=u_s v_s^\top`，令 `K_s=v_s^\top\mathbf1>0`，下标按 `p` 周期取值。定义

\[
G_H(y)=\bigl(a_H^\top\operatorname{diag}(J_{H,0}(y))u_{H,0}\bigr)K_{H,0},
\]

以及相位 `s` 的有理观察因子

\[
q_{H,s}(y)=
\bigl(v_{H,s-1}^\top\operatorname{diag}(J_{H,s}(y))u_{H,s}\bigr)
\frac{K_{H,s}}{K_{H,s-1}}
\quad(s\in\mathbb Z/p\mathbb Z).
\]

这些 `q` 仅是精确判等的比值坐标，原始 `F` 仍是整数。逐次展开秩一矩阵积，任意 `t≥1` 得到

\[
\boxed{F_H(y_1\cdots y_t)=G_H(y_1)\prod_{i=2}^t q_{H,(i-1)\bmod p}(y_i).}
\]

**定理。**若两系统对全部长度 `0≤t≤p+1` 的有序词具有相同正整数路径重数，则其**全部未来有限观察历史等价**。

**证明。**一步等价给出全部 `G_A(y)=G_B(y)>0`。对于每个 `s=1,...,p-1,0`，相位 `s` 第一次作为后续相位分别出现在长度 `s+1`（`s≥1`）或长度 `p+1`（`s=0`）；比较任一固定正整数前缀的相邻两长度词，`F_t/F_{t-1}=q_s(y_t)`，逐相位逐端口确定 `q_{A,s}=q_{B,s}`。该因子按周期重复，故上式给出全部未来逐词等价。初始空词已单独假定。证毕。

**逐周期锐性。**对任意 `p≥1`，取两个标签、初始 `a=(1,2)`、每个相位的共享转移

\[
T_s=\begin{pmatrix}1&1\\1&1\end{pmatrix}\quad(\text{严格正、rank}=1).
\]

在相位0设两端口 `Y=(0,1)` 的输出向量

\[
\begin{array}{c|cc}
&y=0&y=1\\\hline
J_{A,0}&(2,2)&(4,1)\\
J_{B,0}&(4,1)&(2,2)
\end{array}
\]

其余相位 `s>0` 两系统都令两个端口均为 `(1,1)`。对于两个端口，第一步均有 `a\cdot J_{H,0}(y)=6`；首次相位0之后隐藏标签经秩一转移刷新为相同的双坐标行，直至相位0再次出现。故所有长度 `t≤p` 的逐词整数历史相同，但在长度 `p+1` 的词 `(0)^{p+1}` 上：

\[
\boxed{F_A((0)^{p+1})=24\cdot2^p,\qquad F_B((0)^{p+1})=30\cdot2^p.}
\]

亦即 `p=1` 时 `48` 对 `60`，`p=2` 时 `96` 对 `120`。这里每相位两个端口按隐藏标签逐项求和的输出向量在两系统完全相同（相位0为 `(6,3)`，其他为 `(2,2)`），故对每个长度的**全部观察词求和得到相同总原始路径质量**。因此 `p+1` 对每个 `p≥1` 都不可统一缩短；隐藏转移秩1本身无法删除时钟相位残差。

## 5. 实际作者侧精确检查与证据范围

`d25_brc_periodic_rankone_temporal_horizon_checker_20261031.py` 仅用 Python 标准库无界整数和 `Fraction`：

- 对 `p=1,...,7` 的锐性实例逐一枚举所有长度 `0,...,p+1` 的二端口词，总计 **1009** 个逐词比较；其中 `t≤p` 的 **501** 个逐词相等检查通过；对各 `t` 验证两系统总原始路径质量完全相同。
- 对非周期单标签构造 `N=1,...,6`，在各声明长度枚举四端口词、检查前缀等价、首分裂及每个长度 `5^t` 的精确来源总质量。
- 对 `p=1,...,4`、`m=2,3` 的 **24** 组固定随机种子严格正秩一参数，独立逐字展开真实矩阵乘法并与上式因子乘积比较 **2856** 个整数历史字，全部一致。
- 对 `p=2,3`、`m=2,3` 的 **12** 组周期正整数转移模型，逐例使用精确 `Fraction` 验证相位提升转移秩等于各相位转移秩之和；展开提升矩阵与原生辅助分时递推 **1140** 个观察字结果逐一相等。

本检查程序输出同目录 JSON 证书，结果为 `PASS`。这些是声明有限输入上的作者交叉检查；一般定理由上述证明支持，不是独立复核、形式化内核证明或原生 X6 计算。

## 6. BRC 来源保真含义、已有工作与下一原生验收

当前 BRC 承载的是**带标签路径的非负整数重数**，观察端口是**时间有序联合输出**，隐藏标签演化包括周期钟相位。时间齐次低秩结论 `REUSE_APPLIED`；周期性相位提升 `COMPOSE_APPLIED`；非周期任意延迟障碍 `AUTHOR_DERIVED`。即使即时输出总质量一致，某相位下未观察到的相关性仍可在未来改变端口词。不是相位自动成为空间第七轴：原生空间仍为六轴，时间独立，本文的有限相位是**假定的动力学控制索引**。

精确原生验收需要由合法执行者取得：真实 `X6` 带标签状态/来源编码，真实时间有序操作 `T_{t}`, 观察端口 `J_{t,y}`, 原始整数权重；验证与辅助 `B_{t,y}` 的推前/更新交换，确认整个 `B_{t,y}` 具有**同一个已证明**有限周期或提供可证明的其他有限控制器；并检验逐相位秩与观察完整性。当前 P000/Heartbeat World 不提供固定 heartbeat program，因此本文定理仅给出严谨的**类型化准入条件**，没有完成 native bridge。

外部先例：经典加权有限自动机、Hankel/有理级数的线性表示与等价性已经成熟（例如 Kiefer 2020, *Notes on Equivalence and Minimization of Weighted Automata*, arXiv:2009.01217；Balle–Panangaden–Precup 2015, arXiv:1501.06841）。本稿不声称创立该一般代数方法；新增作者侧贡献限定为所述整数 BRC 时间索引接口、严格正逐周期锐性族、以及时间无约束时的精确延迟见证。与现有 D25 的时间齐次秩界不同，不重复旧证明。

**状态与责任路径（本轮观察）：** Source Gateway 0.6.11 读到 `research_authority_granted=false`, `executor_binding_configured=false`, `source_sync.control.state=CODE_REVIEW_REQUIRED`；自身 checkpoint 读取 `ACCESS_DENIED`，历史原请求 `r40_20261029_0840_exact_d25_continuation_read_v1` 与 `emr20261029_1650_source_continuation_read` 的 receipt 均为 `CONTROL_REQUEST_NOT_FOUND`。本作者当前没有已核实的 Source session/CLAIM/run；需由实际获准的原生 Researcher 恢复身份/权属、合法 writer/provenance/checkpoint，再交实际独立 Driver。已有草案与本稿均是作者侧 portable evidence，不能填 Source predecessor 的 `completed_units`；若收到 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` 种子，需先完整 readback 初始 input_artifacts 且 `completed_units=[]`。

UR V2 原始四文件 bundle 仍须找到**同一真实对象** `94687 bytes` 与 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` 同时成立，本轮有界挂载目录/Library/GitHub 只读检索未获得字节对象；已完成 UR 数学不重算。有关另一路 native H0/B0 p373 仍由现有支持 Issue #1559 跟踪，不以辅助 rank-one 检查代替。保护 P000、ACTIVE 世界观与冻结 science pin；原定时任务原相位/启用/通知不更改。
