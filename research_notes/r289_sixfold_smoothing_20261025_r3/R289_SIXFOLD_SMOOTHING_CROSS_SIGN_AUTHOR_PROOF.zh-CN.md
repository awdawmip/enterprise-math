# R289 — 六重系数平滑的最小正性阈值与跨符号邻接差不等式

日期：2026-10-25。作者侧形式幂级数证明；正式数学审查与 Enterprise Math 原生 Source 接纳均未发生。

## 1. 对象、基准与依赖

本研究仅适用于 R268–R288 的**正权、有序、无连续 00、终控制态 q=0**的六边 BRC 辅助自动机。初始 (q,ε,k)=(0,+1,0)；原始来源位 b=0/1 的 (q',η,c) 依次为 q0: (2,−1,−1)/(2,+1,−1)，q1: (0,−1,−1)/(0,+1,−1)，q2: (1,+1,+1)/(2,+1,−1)。完整效果有序右复合 (ε,k)★(η,c)=(ηε,ηk+c)。P_n(ε,k) 保留完整效果标签和每条原始词的正整数重数。x,y 是形式计数变量，不是 P000 原生二维空间或物理时间。

本轮读取 GLOBAL_KNOWLEDGE_V1 canonical main@972e5f7da51e4b5000a3e3ee7eebf97598356537：00_BOOTSTRAP、OPERATING_MANUAL、项目 router、P000_STARTUP、原 P000、ACTIVE 世界观与 BRC/数学/活动/代码规则；P000 原件 Git blob=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc，与 startup projection 匹配。Enterprise Math 当次读取源 main@0a807eb162573e056297ef91313f4534ef895d10，含 docs/PORTABLE_RESEARCH_PROTOCOL.md、docs/RESEARCH_ACTIVITY_PROTOCOL.md 与 research_persistence_policy.json。

精确公式依赖：
- R283@98eb41b63bb29c9b32d79ba5d9b4ef74d0975fa0 的 Laurent Green 核（依赖 R279）；
- R286@83aaa25e0bf6e34ad65c80498a45ed8a6648f060 的正系数 h 方程；
- R288 本日晚间作者分支 research/r288-algebraic-adjacent-gap-20261025-t3-2204 的根式消去；以及早前 research/r288-one-step-tail-20261025-t3-1923 的一步传播。
这些是作者侧、尚未经独立 Driver 接纳的数学输入。BRC 复用判断：REUSE_APPLIED，使用来源路径、完整效果、正整数系数与代数 Green 核，没有以总质量代替各纤维。

定义 F_m^ε(x)=∑_{n≥0}P_n(ε,−m)x^n，Δ_m^ε=F_m^ε−F_{m+2}^ε。置 y=x²，令 h∈y⁴ℕ[[y]] 唯一满足

\[
h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2,
\]

并令 w(y)=(1+y)(1+h(y))=u(x)/x∈ℕ[[y]]。因为每个右侧含 h 的项严格提高 y 次数，h 的非负整数系数逐项唯一且归纳非负。

## 2. 新引理 A：差分正性及六重平滑（全系数、全部长度）

由 h 的固定点方程**原样移项**：

\[
\boxed{L(y):=(1-y)h(y)=
y^4+(2y^2+y^3+y^4)h(y)+y(1+y)^2h(y)^2\succeq0.}
\]

这里 \(\succeq0\) 指所有形式系数非负。故任意整数 j≥1：

\[
\boxed{(1-y)h^j=Lh^{j-1}\succeq0.}
\]

定义平滑核

\[
T_r(y)=\frac{1-y}{1+y}w(y)^r
=(1-y)(1+y)^{r-1}(1+h)^r,\quad r\ge1.
\]

**定理：**

\[
\boxed{T_r(y)\succeq0\quad\Longleftrightarrow\quad r\ge6.}
\]

其中充要性针对所有正整数 r，且 r=6 是最小的无穷系数非负阶数。

**充分性证明。** 对 r=6 展开：

\[
T_6=(1-y)(1+y)^5+
(1+y)^5\sum_{j=1}^6{6\choose j}(1-y)h^j.
\]

第二项因为上面已证的 (1-y)h^j 和二项式系数而逐项非负，最低次数为 y⁴。第一项恰是有限多项式

\[
(1-y)(1+y)^5=1+4y+5y^2-5y^4-4y^5-y^6.
\]

从 h 方程取前三个正次数 h₄=h₅=1、h₆=3；因而 L₄=1、L₅=0、L₆=2。第二项的 j≥2 部分始于 y⁸。j=1 的六倍贡献在 y⁴、y⁵、y⁶ 上分别为 6、30、72，恰好压过第一项的 −5、−4、−1。于是

\[
\boxed{([y^0]T_6,\ldots,[y^6]T_6)=(1,4,5,0,1,26,71).}
\]

次数≥7 时第一项恒为零，第二项已证非负，因此 T₆ 整体非负。任意 r≥6 还满足 T_r=w^{r-6}T_6，由 w∈ℕ[[y]] 得 T_r≽0。

**必要性证明。** 因 h∈y⁴ℕ[[y]]，对 r≤5 有 T_r≡(1-y)(1+y)^{r-1} (mod y⁴)。依次取 (r,负系数次数,系数) 为 (1,1,−1)、(2,2,−1)、(3,2,−1)、(4,3,−2)、(5,3,−2)，说明这五个 r 都不具备系数非负性。证毕。

附带精确支撑：T₆ 的 y³ 系数为零，y⁰,y¹,y² 和所有 yⁿ (n≥4) 系数均严格正；后者由 L_n 在 n≥6 时至少包含 2h_{n-2}>0、以及乘 (1+y)^5 的正系数传播得到。

## 3. 新定理 B：跨符号负平移邻接差的统一正系数恒等式

R288 已从 Green 核精确消去根式，得到

\[
\Delta_m^+=x^{m+2}\frac{w^{m+1}(1-y+y^2-yw)}{1+y},\quad m\ge1,
\]
\[
\Delta_m^-=x^{m+2}\frac{w^{m-1}(1-yw)}{1+y},\quad m\ge2.
\]

因此对所有整数 m≥3，计算得无近似的**跨符号代数协同关系**：

\[
\begin{aligned}
x^2w^4\Delta_m^- -\Delta_{m+2}^+
&=\frac{x^{m+4}w^{m+3}}{1+y}
\big[(1-yw)-(1-y+y^2-yw)\big]\\
&=x^{m+4}y\frac{1-y}{1+y}w^{m+3}\\
&=\boxed{x^{m+4}yT_{m+3}(y)\succeq0.}
\end{aligned}
\]

第三步使用的是**已经完整证明的** T_{m+3}≽0，因为 m+3≥6。因此本式给出对全部原始来源长度成立的跨符号**非负卷积差**，并未暗中取绝对值、改变原始来源顺序或丢弃仿射效果。

特别在 R288 两个真正待证基底处：

\[
\boxed{
x^2w^4\Delta_{11}^- -\Delta_{13}^+
=x^{15}yT_{14}\succeq0.
}
\]

这里“乘以正核后比较”**不等于** Δ_{11}^-≽Δ_{13}^+，也不能从乘积系数非负反推出 Δ_{11}^- 本身非负。相反，两个基底

\[
\Delta_{11}^-\succeq0,\qquad \Delta_{13}^+\succeq0
\]

仍是独立尚未解除的全系数正性义务；不能把本定理冒充无条件 26 效果窗口、全局峰值阈值 N_peak 或 B_n=Λ_n 证明。

## 4. 精确复算与边界

实际执行 JavaScript BigInt 验证器 R289_verify_smoothing.js，独立从 h 固定点迭代和 w 的整数卷积构造系数至 y^96，穷尽比较 T_r (1≤r≤20)、最小阶数五个负例、T_r=T₆w^{r-6}、跨符号 m=3..15，以及两个符号的一步传播。另由六边来源位、无相邻00 和完整仿射效果的独立动态规划至 n=110，精确交叉检查 3,441 个 Δ 系数。全部 PASS。

上述有限机器检查只确证给定索引与长度内实现的一致性；**全长度**结论来自 §2 的非负形式级数证明与 §3 的精确代数恒等式。没有独立 Lean 验证，也没有 R283 Green 输入的独立 Driver 接纳。

验证输出机器事实：3,201 个一步传播系数、1,261 个跨符号卷积差系数通过。T₆ 的前12个系数为 1,4,5,0,1,26,71,138,303,738,1776,4236。

## 5. 权限、写入及下一最小研究问题

真实 GitHub 认证主体 awdawmip；原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED (operation_sent=false)；Gateway 只读身份不授予研究 CLAIM。此结果仅为作者侧论证、独立 GitHub 研究证据；活跃 Owner 未能权威核实，未取得 Source Result、独立 Driver 审查或数学接纳。P000/ACTIVE 世界观未改。

下一小问题：在已经证明最小非负平滑核 T₆ 的条件下，针对 Δ⁺₁₃ 和 Δ⁻₁₁ 搜索**明确非负的形式分解**（例如 w、T₆、L=(1-y)h 与非负整系数多项式的有限组合），或者对其系数构造带明示整数起点的有效有理数正锥，再对剩余有限前缀精确检查。这两项自身仍未证明，全长度 26 效果候选归约继续保持条件。

数学状态：AUTHOR_PROVED_WITH_R283/R286/R288_DEPENDENCIES / SHARP_SIXFOLD_COEFFICIENT_REGULARIZER / CROSS_SIGN_NONNEGATIVE_SYZYGY / EXACT_DP_CHECKED / DRIVER_UNREVIEWED / NOT_ADMITTED。
