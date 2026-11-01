# PREFIX-418｜六项带噪五 Port 模型：两条显式来源曲线的全区间唯一交叉与单调性

**2026-11-01 · Enterprise Math / 进取数论研究6 · 作者侧精确代数与有理区间证书。** 结果分类：`PROVED_FOR_EXPLICIT_SOURCE_FAMILIES / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM`。特别注意：本轮**没有**将两条显式候选曲线在全误差域中的交叉等同于全部真实来源的**全局**最优支路切换。此前 PREFIX-416/417 只给出全局最优角点的局部有效邻域；将它扩展到整个 `0≤ε≤10⁻⁶` 仍为后继证明义务。

## 1. 输入、版本及模型类型

读取并固定以下当时经 GitHub `main` 分支查询核实的快照：

- `GLOBAL_KNOWLEDGE_V1 = awdawmip/chatgpt-global-knowledge@d95e450b75960ec5d9f852cf1fc6ee97589c15a5`。规范入口：`00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`；数学/代码/输出策略、Enterprise Math TASK_RESEARCH 路由、ACTIVE《我眼中的世界》及 P000 均已按需读取。P000 投影中的 `canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` 已与原文件 Git blob 匹配。
- `Enterprise Math scientific/control input = awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`。入口：`AGENTS.md`、`p000_reality_foundation.json`、`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`、`control_plane/current_control_authority.json`、`docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`、`docs/PORTABLE_RESEARCH_PROTOCOL.md`、PREFIX-416、PREFIX-417。

**模型边界**：本研究仍是外部、静态、连续实/复参数的五 Port 相干来源辅助模型。P000 是六维离散空间加独立时间的原生研究框架；外部模型不是 P000 的三维切片，不能用两个复变量的式子替代第三空间分量或原生动力学。BRC 的应用决议为 `COMPOSE_APPLIED`（保留正负复相位来源身份、相干性和联合端口观察）；此证明未执行原生 `typed BRC`，更未证明物理/本体对应。

五 Port 原始矩阵的行依次为：

```
(4,4,0)
(0,-4,4)
(-5+3i,0,-3+i)
(-2-2i,4+4i,2+2i)
(-2,0,5+2i)
```

以前三 Port 规范输出 `(1,u,v)` 定义来源，反演给出

\[
z_4=\frac{5+9i}{2}+\frac{3+7i}{2}u+4iv,\qquad
z_5=\frac{22+15i}{8}(1+u)+\frac{5+9i}{4}v.
\]

设 `β=10⁻⁶`、`0≤ε≤10⁻⁶`、`7/4000≤η≤187/100000`，观测盒为

\[
\bigl||u|^2-1\bigr|\le\varepsilon,\quad
\bigl||1+u|^2-2\bigr|\le\varepsilon,\quad
|v|^2\le\beta,
\]
\[
\bigl||1+v|^2-1\bigr|\le\eta,\quad
\bigl||z_5|^2-709/32\bigr|\le\eta.
\]

第六项 `I4=|z4|²` 是要比较的强度；本证明没有对它预先施加 κ 窗口。

## 2. 两条可重建、精确可行的来源曲线

给定实数 `w`，取 `u=iw`、`v=x+iy`、`t=x²+y²`。定义

\[
\begin{gathered}
P(w)=\frac{245+123w}{16},\quad Q(w)=\frac{-123+245w}{16},\\
A(w)=36+12w,\quad B(w)=-20+28w,\\
J(w)=\frac{53-8w+29w^2}{2},\quad
c(w)=\frac{709(w^2-1)}{64},\quad E=\frac{53}{8}.
\end{gathered}
\]

从原矩阵严格得到

\[
I_4=J(w)+A(w)x+B(w)y+16t,\quad
k:=I_5-709/32=c(w)+P(w)x+Q(w)y+Et,\quad
h:=|1+v|^2-1=2x+t.
\]

**正相位显式来源**：`w+=√(1−ε)`，令

\[
N=P_+^2+Q_+^2,\quad K=\eta-c_+-E\beta,\quad D=N\beta-K^2,\quad S=\sqrt D,
\]

\[
(x_+,y_+)=\left(\frac{KP_++SQ_+}{N},\frac{KQ_+-SP_+}{N}\right).
\]

由构造，`t+=β`、`k+=η` 严格成立。定义该候选的正来源强度增量

\[
Q_+(\varepsilon,\eta)
=J_+-37+16\beta
+\frac{(A_+P_++B_+Q_+)K+(A_+Q_+-B_+P_+)S}{N}.
\]

**负相位显式来源**：`w−=−√(1+ε)`；取

\[
\begin{aligned}
x(t)&=x_0+x_1t,&x_0&=-\eta/2,&x_1&=-1/2,\\
y(t)&=y_0+y_1t,&y_0&=(-\eta-c_--P_-x_0)/Q_-,&y_1&=(P_-/2-E)/Q_-.
\end{aligned}
\]

定义 `a₂=x₁²+y₁²`，`a₁=2(x₀x₁+y₀y₁)−1`，`a₀=x₀²+y₀²`，`Δ=a₁²−4a₂a₀`。取**较小的正根**

\[
t_-=\frac{2a_0}{-a_1+\sqrt\Delta},
\qquad v_-=x(t_-)+iy(t_-).
\]

于是 `x(t−)²+y(t−)²=t−` 且 `h−=k−=−η`，并定义

\[
Q_-(\varepsilon,\eta)=45-J_--A_-x(t_-)-B_-y(t_-)-16t_-.
\]

这些是**两条明确的来源构造**，不是把全体合法来源中的最大值直接定义成上述式子。

## 3. 新定理：整个闭矩形上的唯一显式候选切换曲线

**定理 418-A。** 对每个 `0≤ε≤10⁻⁶`，上述正、负候选均是完整五项观测盒内的合法、相干、可重建复来源。`G(ε,η):=Q+(ε,η)−Q−(ε,η)` 在闭矩形

\[
\mathcal B=[0,10^{-6}]\times[7/4000,187/100000]
\]

实解析，并具有以下**同时适用于所有 `(ε,η)∈B` 的严格有理界**：

\[
\boxed{\frac{259}{100}<G_{\varepsilon}<\frac{262}{100}},\qquad
\boxed{-\frac{418}{100}<G_{\eta}<-\frac{417}{100}}.
\]

并且

\[
G(\varepsilon,7/4000)>19/100000>0,
\qquad G(\varepsilon,187/100000)<-22/100000<0.
\]

故对每个允许 `ε`，存在**唯一**的显式候选交叉 `ηcand(ε)`，且它是严格递增、实解析的参数曲线，满足

\[
\boxed{\frac{621}{1000}<\eta_{\mathrm{cand}}'(\varepsilon)<\frac{627}{1000}}.
\]

因此对于 `0<ε≤10⁻⁶`：

\[
\eta_{\mathrm{cand}}(0)+0.621\varepsilon
<\eta_{\mathrm{cand}}(\varepsilon)
<\eta_{\mathrm{cand}}(0)+0.627\varepsilon.
\]

此处的全域唯一性**只针对上述两条明确的候选来源曲线**。它没有量化或排除同一相位叶内其他合法来源在部分参数上的潜在更优值；对完整模型全局切换唯一性的既有局部分析及额外证明义务仍不变。

**定理 418-B（两个端点的 10⁻¹⁵ 根隔离）。** 完全有理数区间证书给出

\[
\frac{1806822353106}{10^{15}}<\eta_{\mathrm{cand}}(0)
<\frac{1806822353107}{10^{15}},
\]

\[
\boxed{\frac{1807446320202}{10^{15}}
<\eta_{\mathrm{cand}}(10^{-6})
<\frac{1807446320203}{10^{15}}}.
\]

后一根约为 `0.0018074463202022266`（仅作为显示）。相较 PREFIX-417 的零噪声局部曲率结果，这提供了端点 `ε=10⁻⁶` 的**直接代数证书**，但仍不提升为全来源最优切换点的证明。

## 4. 证明、完整连续区间覆盖与验证方法

(i) 对每个 `ε,η`，`w±` 为实，源由原始矩阵前三行唯一反演。正来源满足 `t+=β,k+=η`；负来源从方程 `t=x(t)²+y(t)²` 的较小正根重建，严格满足 `h−=k−=−η`。采用向外舍入的有理区间计算证明，在整个 `B` 上 `D>0`、`Δ>0`、`a₁<0`、`Q−<0`、`0<t−<β`、`−η<h+<η`。故每个构造是合法真实来源，不是伪解。

(ii) 对所有上述公式逐次使用加法、乘法、除法、开根号的区间扩张，区间端点仅为 `fractions.Fraction`。开根号用 `math.isqrt` 对有理端点以 `10⁻³⁰` 网格精确向外舍入，结果不会错误漏掉真实值。使用一阶双数 (forward-mode dual numbers) 逐步传播 `ε` 与 `η` 两方向的**解析偏导**，其区间包含整个连续矩形上的真导数；没有把有限差分当成证明。

(iii) 检查器直接断言 `Gε∈(259/100,262/100)`、`Gη∈(-418/100,-417/100)`；两个端点符号由对整个 `ε` 区间的一次包含运算验证。强单调和介值定理给出每个 ε 的唯一根；隐函数定理使根曲线实解析，`−Gε/Gη` 的有理区间给出导数范围。

(iv) 对两个具体 ε 端点直接代入上述代数来源并在所列有理根区间端点做严格正负判号；这不依赖浮点二分或外部求解器。独立 SymPy 检查器从原始 5×3 复矩阵重新计算前三 Port 的逆、I4 与 I5 的整体系数恒等式、`N` 恒等式与交叉系数，避免只检验自己预设的归一化结果。

**已实际运行证据**：`prefix418_uniform_candidate_certificate.py`（Python 3 标准库 Fraction/isqrt）输出全部四个 PASS；`prefix418_independent_raw_port.py`（SymPy）输出 raw-matrix PASS；日志见 `prefix418_execution.log`、`prefix418_independent_execution.log`。所有载荷、源码和日志的确切哈希见一同保存的 `prefix418_manifest.sha256`。执行结果是作者侧的区间证书及代数交叉核对；没有独立数学审阅、Lean 证明、原生 typed BRC 实验、正式 CLAIM/Result/Admission。

## 5. 科学对照及下一个判别问题

相关已发表方法：Conca–Edidin–Hering–Vinzant, *An algebraic characterization of injectivity in phase retrieval*, Applied and Computational Harmonic Analysis 38(2), 346–356 (2015), DOI `10.1016/j.acha.2014.06.005`；Candès–Eldar–Strohmer–Voroninski, *Phase Retrieval via Matrix Completion*, SIAM Journal on Imaging Sciences 6(1), 199–225 (2013), DOI `10.1137/110848074`。前者讨论泛型强度观测的代数可识别性，后者讨论结构照明的相位恢复；两者都**不直接证明本固定 Port 的带噪候选全局最优性**。当前模型的新结论来自上述具体有理区间与原矩阵推导。

**2026 年已发表前沿的适用边界。** Amir–Bendory–Dym–Edidin, *The stability of generalized phase retrieval problem over compact groups*, *Applied and Computational Harmonic Analysis* **82** (2026), 101838, DOI `10.1016/j.acha.2025.101838`，在低维结构先验下证明广义相位恢复的唯一性与双 Lipschitz 稳定性；Bendory–Dym–Edidin–Suresh, *Phase Retrieval with Semialgebraic and ReLU Neural Network Priors*, *SIAM Journal on Mathematics of Data Science* **7** (2025), 1705–1728, DOI `10.1137/23M161731X`，研究半代数结构先验下的泛型可识别性。这些成果为本问题的稳定性和半代数消元提供参考，但没有给出本固定五 Port、联合区间噪声下的候选或全局最优支路判定。具体五 Port 的全域最优证明仍需独立完成。

**PREFIX-419（最小未完单元）**：在完整 `ε∈[0,10⁻⁶]` 与 `η∈[0.00175,0.00187]` 上，证明实际两相位叶的全局最优来源分别正好等于第2节两个显式构造，或寻找精确反例（较优的其他 `u,v`）。可先检验正叶的全局支持上界/严格 KKT、负叶二次约束可行集其他连通分支，再对 `(r,s)` 矩形证明真正的角点最优性。该义务一旦解决，上述显式候选唯一性才能被提升为实际最优支路切换唯一性。P000 X6 三维切片及第三分量读出桥接继续作为**独立**研究。

## 6. 控制与保存语义

研究身份：`ChatGPT scheduled conversation / 进取数论研究6`；GitHub 连接认证账号 `awdawmip`。原生服务 `v0.6.11` 当前报告 `research_authority_granted=false`，`executor_binding_configured=false`，`active_jobs=5/5`；因此没有主动声称获得当期 source owner、服务签发会话、CLAIM、独立 Review 或 Admission。此次材料仅是 GitHub 项目中可移植的、作者侧未经审阅的数学研究交付，不是原生状态机的 Result/checkpoint。
