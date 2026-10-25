# R288 — BRC 清洁负平移尾部的一步正核、双基底归约与逐指标渐近

2026-10-25。AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 0. 固定对象、读取来源、权限边界

固定 GLOBAL_KNOWLEDGE_V1 的同一份已核实不可变 main 快照：awdawmip/chatgpt-global-knowledge@7b33f8066e9993e7c941959a9d738ed405248eb8。已读 00_BOOTSTRAP.md、OPERATING_MANUAL.md、Enterprise Math 项目入口、P000（ACTIVE_LOCKED）和 ACTIVE 世界观。固定 Enterprise Math 控制源：awdawmip/enterprise-math@3756eadf96b9f1447cde25ff4b653a85e3a26d66；另读 docs/PORTABLE_RESEARCH_PROTOCOL.md、研究活动及 BRC 使用规范。

确切数学输入：R279@24f2d7515ac6bb8201d74c5dcdc1d61b6a11b159（Laurent GF）、R283@98eb41b63bb29c9b32d79ba5d9b4ef74d0975fa0（固定负平移代数核）、R287@c2279fcee701cf874e7a865b86fab100137e8de0（负尾二步传播与镜像定理）；均为作者侧成果，尚未独立 Driver 数学接纳。

研究对象仅为六边正权、有序、原始来源词无相邻 00、终态 q0 的**辅助 BRC**；不是 P000 原生 X6 Cell 动力学。初态 q0, (ε,k)=(+1,0)，边的 (q',η,c)：
- q0: bit0 (q2,-1,-1), bit1 (q2,+1,-1)
- q1: bit0 (q0,-1,-1), bit1 (q0,+1,-1)
- q2: bit0 (q1,+1,+1), bit1 (q2,+1,-1)

效果有序复合 (ε,k)★(η,c)=(ηε,ηk+c)。P_n(ε,k) 计原始路径正整数重数。设

$$
F_m^\epsilon(x)=\sum_{n\ge0}P_n(\epsilon,-m)x^n,\qquad
\Delta_m^\epsilon=F_m^\epsilon-F_{m+2}^\epsilon.
$$

复用结论：REUSE_APPLIED；保留来源位次序、效果符号、全部整数重数和不同纤维；形式级数幂次不是物理心跳时间。

## 1. 定理 A：所有长度的一步正核

由 R283，记

$$
a=1+2x^4-x^6,\quad
D=a^2-4x^2=(1-x^2)(1-x^6)(1-3x^2+x^4),
$$
$$
u=\frac{a-\sqrt D}{2x}=x+O(x^3),\quad
J=\frac1{(1+x^2)\sqrt D}.
$$

分别对 m≥1（正符号）、m≥2（负符号）有精确形式恒等式

$$
F_m^+=x^2Ju^m(1-x^2+x^4-xu),\qquad
F_m^-=x^4Ju^{m-2}(1-xu).
$$

此前仅使用 m 增加 2 的传播，本轮注意到完整的一步恒等式：

$$
\boxed{F_{m+1}^\epsilon=uF_m^\epsilon,\quad
\Delta_{m+1}^\epsilon=u\Delta_m^\epsilon,\quad
\Delta_{m+r}^\epsilon=u^r\Delta_m^\epsilon\ (r\ge0).}
$$

范围同上。R286/R287 的 h(y) 为唯一形式固定点

$$
h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2,\qquad y=x^2.
$$

该递推正系数且严格提高次数，故 h∈y⁴ Z_{\ge0}[[y]]，且 [y^j]h>0 当且仅当 j≥4。既有 R286 精确恒等式

$$
\boxed{u=x(1+y)(1+h)\in x\mathbb Z_{\ge0}[[y]].}
$$

因此单个基底差级数**若**全系数非负，其后所有相邻 m 的差级数皆非负。不需将 m 分成两个奇偶子序列，且未宣称任何未证基底已满足此条件。

## 2. 定理 B：消去根式的整数乘积式

形式根方程 xu²−au+x=0 给出 sqrt(D)=a−2xu=x(u^{-1}−u)，从而

$$
\boxed{1-u^2=\frac{u\sqrt D}{x},\quad
J(1-u^2)=\frac{u}{x(1+y)}.}
$$

代入 Δ_m=(1−u²)F_m，得到**全部长度精确系数恒等式**

$$
\boxed{\Delta_m^+=\frac{xu^{m+1}}{1+y}(1-y+y^2-xu)},\quad m\ge1,
$$
$$
\boxed{\Delta_m^-=\frac{x^3u^{m-1}}{1+y}(1-xu)},\quad m\ge2.
$$

令 T(y)=u/x=(1+y)(1+h)，则

$$
\boxed{
\Delta_m^+
=x^{m+2}(1+y)^m(1+h)^{m+1}[1-2y-y(1+y)h]},\quad m\ge1,
$$

$$
\boxed{
\Delta_m^-
=x^{m+2}(1+y)^{m-2}(1+h)^{m-1}[1-y(1+y)(1+h)]},\quad m\ge2.
$$

这是无根式、仅整数形式级数的可复核恒等式。末项的括号含负系数，不能将乘积自动视作非负证书。

## 3. 定理 C：R287 四基底缩为二基底，条件候选 28 缩为 26

R287 的四个候选 Δ_13^+, Δ_14^+, Δ_11^−, Δ_12^− 并不独立：

$$
\boxed{\Delta_{14}^+=u\Delta_{13}^+,\qquad
\Delta_{12}^-=u\Delta_{11}^-.}
$$

由于 u 系数非负，只须尝试证明两个目前**仍未证明**的全系数非负命题：

$$
\boxed{\Delta_{13}^+\succeq0,\quad\Delta_{11}^-\succeq0.}
$$

若二者成立，由一步传播，全部正符号 m≥13 和负符号 m≥11 的负尾纤维逐步非增。结合 R286 已证明的正 k 镜像支配，对所有 n 得到条件式

$$
\boxed{\Lambda_n=\max\left(
\{P_n(\epsilon,0):\epsilon=\pm1\}
\cup\{P_n(+1,-m):1\le m\le13\}
\cup\{P_n(-1,-m):1\le m\le11\}\right).}
$$

其中固定候选恰为 2+13+11=26 个；**条件不可删去**。R287 在 m=12 的正符号、n=24 给出 Δ 差 −56，在 m=10 的负符号、n=20 给出 −5，因此不能把“全长度一步尾部单调”的起始索引分别提前到12与10。

## 4. 定理 D：固定指标尾部差值的直接渐近及最终符号分类

此证明只用 R283 精确核，不使用 R280/R281 的局部极限定理/Edgeworth。记

$$
\varphi=\frac{1+\sqrt5}{2},\quad \rho=\varphi^{-2}=\frac{3-\sqrt5}{2},\quad
g(y)=\sqrt{\frac{1-3y+y^2}{1+y+y^2}},
$$

选择常数项为 1 的分支。根据 (1−y³)=(1−y)(1+y+y²)，

$$
\sqrt D=(1-y^3)g(y),\quad
T(y)=\frac{a(y)-(1-y^3)g(y)}{2y}.
$$

g 的最近奇点唯一位于正实 ρ；另一个分子零点为 ρ^{-1}>1，分母零点模长为1。相应开缝域内平方根展开：

$$
g(y)=\frac{5^{1/4}}2\sqrt{1-y/\rho}\,[1+O(1-y/\rho)],
$$

故

$$
\boxed{T(y)=\varphi-\beta\sqrt{1-y/\rho}+O(1-y/\rho),\quad
\beta=\frac{5^{1/4}}{\varphi}>0.}
$$

令 W_m^\epsilon(y)=Δ_m^\epsilon(x)/x^{m+2}。由上面的精确恒等式，

$$
W_m^+(y)=\frac{T^{m+1}(1-y+y^2-yT)}{1+y},\quad
W_m^-(y)=\frac{T^{m-1}(1-yT)}{1+y}.
$$

在 (y,T)=(ρ,φ) 处求 T-偏导，利用 1−ρ+ρ²=2ρ：

$$
\partial_TW_m^+(\rho,\varphi)=
\frac{\varphi^m\rho^2(m-2\varphi)}{1+\rho},
\qquad
\partial_TW_m^-(\rho,\varphi)=
\frac{\varphi^{m-2}(m\rho-1)}{1+\rho}.
$$

平方根的标准系数转移定理（唯一主奇点）给出，对每个**固定**合法整数 m，当 j→∞：

$$
\boxed{[y^j]W_m^+(y)=
C_m^+\rho^{-j}j^{-3/2}[1+O_m(j^{-1})],\qquad
C_m^+=\frac{\beta\varphi^m\rho^2(m-2\varphi)}
{2\sqrt\pi(1+\rho)}},\quad m\ge1;
$$

$$
\boxed{[y^j]W_m^-(y)=
C_m^-\rho^{-j}j^{-3/2}[1+O_m(j^{-1})],\qquad
C_m^-=\frac{\beta\varphi^{m-2}(m\rho-1)}
{2\sqrt\pi(1+\rho)}},\quad m\ge2.
$$

主项都非零：2φ≈3.236，1/ρ=φ²≈2.618，均非整数。因此各固定指标的**最终符号**严格分类为

- 正符号 m=1,2,3 最终严格为负；m≥4 最终严格为正。
- 负符号 m=2 最终严格为负；m≥3 最终严格为正。

关键两个基底有 C_13^+≈140.0122633871139956、C_11^-≈45.9104917028012953，故各自最终为正。这只是非有效（无显式起始整数）的固定 m 定理，仍不证明第3节需要的全部系数非负，也不允许令 m 随 j 增长而直接使用 O_m。

## 5. 实际验证与下一步

执行了 Python 无界整数程序：原始来源词独立穷举 n≤14，共32767条；六边动态规划 n≤700；一步核 F_(m+1)=uF_m 7332项精确一致；四个关键基底/后继的无根式差值 2804项逐长一致。Δ_13^+、Δ_11^- 分别在343、344个有效长度层上非负，最小值均1；重现较低指标的四个严格负差反例。固定索引的代数奇点常数和 j=300 缩放系数独立比较，方向一致。详见本目录验证程序及 EXACT_EVIDENCE.json；有限计算绝非无限非负性证明。

下一最小单元：对两个明确多项式滤波后的 h 级数构造真正的无穷非负证书：

$$
A(y)=(1+y)^{13}(1+h)^{14}[1-2y-y(1+y)h],
$$
$$
B(y)=(1+y)^9(1+h)^{10}[1-y(1+y)(1+h)].
$$

可以复用 R285 的有理数比值正锥、可审核 P-递推证书或非负语法分解。成功后去掉26候选归约的条件，再求全局有效 N_peak，最后独立审查 clean/dirty 依赖以处理 B_n=Λ_n。P000/ACTIVE 世界观原件未被更改。

**真实权限**：GitHub 身份 awdawmip；原生 em_control_tasks: CONTROL_QUOTA；原生 em_session_start: STATIC_READONLY_SCOPE_DENIED (operation_sent=false)。当前活跃 Owner 未能权威核实，没有原生 CLAIM、Source Result 或独立 Driver 数学接纳。GitHub 持久化仅是作者侧研究记录。
