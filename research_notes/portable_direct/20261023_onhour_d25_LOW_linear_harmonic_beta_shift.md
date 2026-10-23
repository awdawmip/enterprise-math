# D25/LIFT — LOW 线性 harmonic 层的精确 Beta 平移消去

**日期 / 类型**：2026-10-23，TASK_RESEARCH 作者数学材料，AUTHOR-PROVED RATIONAL IDENTITY / EXACT-FRACTION CROSSCHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_FORMAL_CLAIM / NOT_NATIVE_BENCHMARK。

**来源和隔离**：Research logical lane = chatgpt-research-onhour-enterprise-math-20260923（仅为来源说明，非 Source 授权）。母任务 RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT，Task publication TP2-B6F4FC938FF94941C1B7。冻结原生 checkpoint/source pin c47e13e4aba0e006366f989d6334d443f6333ae3，不因当前 main 更新而改变。本作者已经看过 LOW/B11/WZ 证据，不能作独立审阅。复用已验证的 WZ、D24 first digit、Beta adjoint、高段一阶 jet、低段二阶 jet 和 2026-10-23 精度隔离/锐性反例，不重做这些成果。

**规范**：GLOBAL_KNOWLEDGE_V1 验证主干 main@bf441dbd96e3aff7f1df531c6569d56fa048a10b；P000 ACTIVE_LOCKED、适用世界观 ACTIVE。本文为外部精确有理数/模素数证明，不属于 X6 native 实验或物理桥接。

## 1. 新单元的定理

令 m≥1 为整数，p=6m+1（模 p 的应用要求 p 素数），定义

\[
b_n=\frac{(-1)^n}{2^n}\binom mn,\quad w_n=6n-1,\quad
A_{a,n}=H_a-H_{a-n},\quad
L_n=-\frac12A_{m,n}+\frac23A_{2m,n}+\frac13A_{4m,n}.
\]

记

\[
B_m(x)=(x-\tfrac12)^m,\quad
P_1(x)=\tfrac23\sum_{r=1}^{m}x^r+\tfrac13\sum_{r=1}^{3m}x^r,
\]

\[
C_m=\frac12\sum_{j=1}^{m}\frac{(-1)^j}{j}
+\frac23(H_{2m}-H_m)+\frac13(H_{4m}-H_m),
\]

\[
V_m=\int_0^1 \frac{P_1(x)}xB_m(x)\,dx,\qquad
I_m=\int_0^1 \frac{P_1(x)}x(3B'_m(x)+B_m(x))\,dx.
\]

**新证明的两条全 m 精确有理数恒等式**：

\[
\boxed{\sum_{n=0}^m b_nL_n=2^{-m}C_m-V_m,}\tag{SH-0}
\]
\[
\boxed{\sum_{n=0}^m b_nw_nL_n
=2^{-m}[3((-1)^m-1)-pC_m]+I_m.}\tag{SH-1}
\]

P_1(x)/x 是多项式，所以 V_m、I_m 是有限有理 Beta moments，并不依赖数值积分。SH-1 的 -p C_m **不能**在 LOW 的除以 p 操作之前丢弃。

## 2. 完整代数证明

对 a≥m 定义

\[
F_{a,m}(z)=\sum_{n=0}^m(-1)^n\binom mn z^n(H_a-H_{a-n}).
\]

在 a=m 时，令参数 \(\varepsilon\) 进入 \((1-z)^{m+\varepsilon}\)，对参数求导、再只保留 z 次数 ≤m 的部分，得到

\[
F_{m,m}(z)=\sum_{j=1}^m\frac{(-z)^j(1-z)^{m-j}}j.\tag{B0}
\]

证明要点：n≤m 的 \(\partial_\varepsilon\binom{m+\varepsilon}{n}|_0=\binom mn(H_m-H_{m-n})\)；另一方面
\((1-z)^m\log(1-z)=(1-z)^m\sum_{j\ge1}(-z/(1-z))^j/j\)，j>m 不影响 ≤m 次系数。因而 (B0) 精确成立。

记 \(D=6z\partial_z-1\)。在 z=1/2 代入 (B0)：

\[
F_{m,m}(1/2)=2^{-m}\sum_{j=1}^m\frac{(-1)^j}{j},
\]
\[
DF_{m,m}(1/2)=2^{-m}\left[
12\sum_{j=1}^m(-1)^j
-p\sum_{j=1}^m\frac{(-1)^j}{j}\right].\tag{B1}
\]

对所有 a≥m，有
\(A_{a+1,n}-A_{a,n}=(a+1)^{-1}-(a+1-n)^{-1}\)，并且

\[
\sum_{n=0}^m\frac{(-1)^n\binom mn z^n}{a+1-n}
=\int_0^1 t^{a-m}(t-z)^m\,dt.
\]

于是取得精确的 **index-shift/Beta 平移**：

\[
F_{a+1,m}(z)-F_{a,m}(z)
=\frac{(1-z)^m}{a+1}-\int_0^1t^{a-m}(t-z)^m\,dt.\tag{SHIFT}
\]

令 \(U_a=F_{a,m}(1/2)\)、\(T_a=DF_{a,m}(1/2)\)，由 SHIFT 及
\(D(t-z)^m|_{z=1/2}=-3B'_m(t)-B_m(t)\) 得

\[
U_{a+1}-U_a=\frac{2^{-m}}{a+1}
-\int_0^1t^{a-m}B_m(t)\,dt,\tag{U}
\]
\[
T_{a+1}-T_a=-\frac{p\,2^{-m}}{a+1}
+\int_0^1t^{a-m}(3B'_m(t)+B_m(t))\,dt.\tag{T}
\]

分别从 a=m 累加至 2m 与 4m。因
\(P_1(t)/t=\frac23\sum_{s=0}^{m-1}t^s+\frac13\sum_{s=0}^{3m-1}t^s\)，再取
\(-\frac12U_m+\frac23U_{2m}+\frac13U_{4m}\) 或对应 T 组合，
并用 \(6\sum_{j=1}^m(-1)^j=3((-1)^m-1)\)，即得 SH-0、SH-1。全过程不假设 p 是素数，不依赖有限采样。

## 3. 直接落到 LIFT/LOW 的新单标量

沿用已发布数学材料的精确定义（原来源见本文件末尾）：

\[
X_{0,m}=2^{-m}+\sum_{n=0}^m b_nw_nL_n+
\underbrace{\int_0^{1/2}B_m(x)
\left(3P'_1(x)+\frac{p-2}{2x}P_1(x)\right)\,dx}_{J_m^{(1)}},
\]

\[
Z_m=\sum_{n=0}^m b_n
\left[2L_n-\frac12\mathcal R_n(1)
+w_n\left(M_n+\frac12\mathcal R_n(J)\right)\right].
\]

已知 \(M_n=K_n+L_n^2/2\)，而 \(P_J(x)=\frac23\sum_{r=1}^mJ_rx^r+\frac13\sum_{r=1}^{3m}J_rx^r\) 与 \(\mathcal R_n\) 是已保留来源的 reflected Beta 观察器。

定义

\[
\Theta_m=2^{-m}[3(-1)^m-2]+I_m+J_m^{(1)},
\]
\[
K_m^{(J)}=\int_0^{1/2}\frac{B_m(x)}{x}P_J(x)\,dx,\quad
J_m^{(2)}=\int_0^{1/2}B_m(x)
\left(3P'_J(x)-\frac{P_J(x)}x-\frac{P_1(x)}{2x}\right)dx,
\]
\[
\mathsf M_m=\sum_{n=0}^m b_n w_nM_n.
\]

**第一项的完全精确消去**：

\[
\boxed{X_{0,m}=\Theta_m-p\,2^{-m}C_m.}\tag{X-new}
\]

另由 SH-0、\(\sum b_n\mathcal R_n(1)=\int_0^{1/2}(B_m/x)P_1\,dx\)，
及此前已证 INT-w 对 \(P_J\) 分部积分（边界 \(B_m(1/2)=0,\ P_J(0)=0\)），严格得到

\[
\boxed{Z_m=
2^{1-m}C_m-2V_m+\mathsf M_m+J_m^{(2)}
+\frac p2K_m^{(J)}.}\tag{Z-new}
\]

对素数 p=6m+1，设 \(\mathcal A_m=(p-1)!/[3^{p-1}(2m)!^3]\)，
\(\chi_p=((4/3)^{p-1}-1)/p\)，原 LOW defect 为
\(\mathscr D_m^{old}=(\mathcal A_mX_{0,m}-1)/p+\mathcal A_mZ_m-\chi_p\)。

(X-new)、(Z-new) 逐项代入得 **完全精确的有理恒等式**

\[
\boxed{
\mathscr D_m^{old}
=
\underbrace{\frac{\mathcal A_m\Theta_m-1}{p}
+\mathcal A_m
\left(2^{-m}C_m-2V_m+\mathsf M_m+J_m^{(2)}\right)-\chi_p}
_{\mathscr D_m^{beta}}
+\frac{p\mathcal A_m}{2}K_m^{(J)}.
}\tag{DEFECT}
\]

已有 accepted first digit 确认 \(\mathcal A_mX_{0,m}\equiv1\pmod p\)；
由 X-new 和各对象 p-integrality 又知 \((\mathcal A_m\Theta_m-1)/p\)
可合法作为整数 digit 在模 p 上读取。因此

\[
\boxed{\mathrm{LIFT/EP}\iff \mathscr D_m^{beta}\equiv0\pmod p.}\tag{NEW-LOW}
\]

(NEW-LOW) 去掉了 LOW 的整个**线性 L_n harmonic 观察层**：
它只剩全局 \(C_m\)、显式 Beta moment 和真正未完的二阶
\(\mathsf M_m\)（其内部仍含 \(L_n^2\)）及 \(P_J\) 部分。
它本身**尚不是**全素数 EP 的证明，更不是原生 benchmark 完成。

p-unit 审计：SH-0/SH-1 的多项式积分分母来自 1,...,4m，所有 H 及 \(\mathcal A_m\) 的分母不含 p；
J_r 原有分母 3r-1 在 r=1,...,3m 内也不被 p=6m+1 素数整除；
\(\mathcal A_mK_m^{(J)}\) p-integral。因而 DEFECT 最后项的 valuation 至少为 1，
可以且只可以在既有 divided-digit 精确构造完成后模 p 投影掉。
BRC 记录保留 n/r 支路、p-adic filtration、来源和观察器映射；
不把有符号有理抵消解释为非负质量抵消。

## 4. 可复核的精确计算证据

两条不同的有理构造：一条按 n 直接构造 \(b_n,L_n,M_n,J_r,\mathcal R_n\)，
另一条按 SHIFT、Beta 多项式积分分别构造 \(C_m,V_m,I_m,\Theta_m,J_m^{(2)}\)。
使用 Python Fraction，所有检查均为精确整数分子/分母比较，未使用浮点。

- m=1,...,7：SH-0、SH-1 两式两路完全相等。
- m=2 (p=13)：\(X_{0,m}=170467/1290240\)；m=3 (p=19)：\(X_{0,m}=273667/4257792\)。与直接原 \(X_0\) 完全相等。
- m=1,2,3,5（p=7,13,19,31）：完整 DEFECT 两路之差严格为
\(p\mathcal A_mK_m^{(J)}/2\)，同时旧/新 defect 取模 p 都为 0。
这仅是四个确切见证；全 m 代数恒等式的证明是第 2、3 节，不由测试外推。
- 有限 Beta 证书的独立核验可使用
\(\int_0^{1/2}x^{r-1}(x-\frac12)^m dx
=(-1)^m m!(r-1)!/[2^{m+r}(m+r)!]\)
及
\(\int_0^1 x^{r-1}(x-\frac12)^m dx
=\sum_{u=0}^m\binom mu(-1/2)^{m-u}/(r+u)\)。

## 5. 任务接续、边界及下一精确动作

**母目标**：D24 RR-AC9B3BA5BD277CE043F5 已冻结，Driver DR-610CB297F3195E8F2D9E ACCEPTED 并路由 D25；保留 frozen D25 Source pin 及原 native checkpoint。新的证明/证书只作为独立作者材料，**UNREVIEWED / NOT_ADMITTED**。

**最小下一数学动作**：对 \(\mathscr D_m^{beta}\) 中
\(\mathsf M_m+J_m^{(2)}-2V_m\) 做 Euler–Beta 参数导数/contiguous-Dixon 与既有 B11 moment 的直接匹配；如不能闭合，则保留这唯一二阶 adjoint defect，而不是重做 WZ/B11 或加高无关阶数。原生 benchmark 对象、输入、版本/验证条件及独立审阅仍为未满足欠项；没有执行或伪称通过。

**Research lane / recovery**：独立于 CONTROL_PLANE_MAINTENANCE 的 chatgpt-hourly-enterprise-math-20260921。桥 Issue #6186 的原请求 recovery-status-20261023-1704-onhour-01 显示本 Research lane 的旧 ACTIVE 投影不具 Source 认证，无 own CLAIM/run；#6187 的 continuation-d25-20261023-1709-onhour-01 为 PREREQUISITE_NOT_SUCCEEDED；#6188 的 dispatch-research-20261023-1710-onhour-01 已从 QUEUED 转为 FAILED/TimeoutExpired（不是 NO_DISPATCH）。此轮通过 GitHub 只读旧回执，不重发、不开 maintenance lane。当前直连服务 em_status 为 0.6.11，verified client sites-em-6abdec598ad48191aebece9a8232f041-ro，research_authority_granted=false；该 MCP toolset 没有 recovery_status 的专用 read action，且不能把另一 subject 的 NOT_FOUND 当作真实队列为空。#1539 仍追踪旧 session-start/source-prerequisite 问题；先由负责路径修复并核验 native continuation/claim/open，后轮从此笔记最高有效数学进度接续。旧三份 staging 继续独立中立保全，不并入 accepted Result。

**不重做 / 不伪报**：本文 GitHub 文件回读只证明中立研究材料在仓库持久化，不会自动生成 session、registered activity、Source checkpoint、Result、freeze 或审阅，不能取代 native benchmark、接受或原 task 输出。

**引用的既有确切材料**：
- research_notes/directed_recovery/20260926_13C1B7/sources/hourly_new/f48dfe9d-4144-4e56-9948-00a764fb3035.md
- research_notes/directed_recovery/20260926_13C1B7/sources/hourly_new/fb9aba8a-6fb9-411b-920b-9bb376d16cd5.md
- research_notes/portable_direct/20261023_onhour_d25_LIFT_precision_firewall_p4_witness.md
- docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md；current Source operation_contract/schema 优先。
