# PREFIX-408：非零 I3 噪声下的最优临界半径与 PSD 秩缺口证书

日期：2026-11-01。项目：Enterprise Math / 进取数论，研究6。类型：外部**静态**复振幅五 Port 逆问题；作者侧精确证明、符号/有理数运行核验。状态：UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。不是 P000 原生 X6、三维研究层或 typed BRC 动力学的结论。

冻结输入：全局主干经 GitHub 实读及 compare 确认；旧网关同步 pin 7b33f806 显著落后，故**不把它当作当前主干**。GLOBAL_KNOWLEDGE_V1 main@eefc162283b2f27ce1333bde7e9ff7cc81e6b1d1；Enterprise Math main@71f5e22a2d4de499694c6db4bf7f195df6d63ab0。延续 research_notes/2026-11-01_prefix407_exact_rank_one_boundary_certificate.md。已读取规范入口、P000、ACTIVE 世界观、当前 portable research 及自主研究协议。当前作者属于本轮便携研究，不据上轮本地 R-ID 冒充原生身份或 CLAIM。

## 1. 精确输入与观察接口

原始复矩阵

\[
A=\begin{pmatrix}
4&4&0\\
0&-4&4\\
-5+3i&0&-3+i\\
-2-2i&4+4i&2+2i\\
-2&0&5+2i
\end{pmatrix},\qquad \det A_{1:3}=-32+32i\ne0.
\]

归一化 W=A_{1:3}Y=(1,u,v)^T；记

\[
a=5/2+9i/2,\quad b=3/2+7i/2,\quad c=4i,\qquad
d=11/4+15i/8,\quad e=5/4+9i/4.
\]

读数为 I1=1、I2=|u|²、Cu=|1+u|²、I3=|v|²、Cv=|1+v|²、I4=|a+bu+cv|²、I5=|d(1+u)+ev|²；系数可由 A·(A前3行)^{-1} 回算。

单相干来源提升为 H=WW*，H 是 Hermitian PSD 且 rank(H)=1。PhaseLift 型松弛去除秩一要求，所有读数改为对 H 的线性观测；混合 PSD 可行不代表单来源可实现。来源、相位和不同支路不可直接合并。

## 2. 定理 A：I3∈[0,β] 的精确临界半径

给定 β≥0 与 κ≥0，规定 I2=1、Cu=2 准确，并要求

\[
0\le I3\le\beta,\quad 41-\kappa\le I4\le41+\kappa,\quad
0\le Cv\le10,\quad 0\le I5\le100.
\]

定义

\[
\beta_c=\frac{(\sqrt{45}-\sqrt{41})^2}{16}
=\frac{43-3\sqrt{205}}8\in(0,1/100)
\]

及

\[
\boxed{\kappa_*(\beta)=
\begin{cases}
4-8\sqrt{45\beta}+16\beta,&0\le\beta\le\beta_c,\\
0,&\beta\ge\beta_c.
\end{cases}}
\]

**定理：** 在以上**全部**联合观测约束下存在真正的复来源，**当且仅当** κ≥κ*(β)。特别地，对任意 β>0 都覆盖非零的 I3 测量区间宽度；这是准确阈值，不是充分但非必要估计。

**证明。** I2=1、Cu=2 强制 Re u=0 与 |u|=1，故 u=±i。设 w=a+bu，直接计算 |w|² 对 u=i 等于37，对 u=-i 等于45。由于 |v|≤√β、c=4i，随 v 在闭圆盘内变化，|w+cv| 的所有可能值精确组成 [max(0,|w|-4√β),|w|+4√β]：三角不等式给出包含关系，选 v 与 w 同向或反向得到所有中间值。

当 0≤β≤βc，令 t=√β，有 4t≤√45-√41。对 u=-i 分支始终 I4≥(√45-4t)²≥41，其与41的最小距离是
D45=(√45-4t)²-41=4-8√45·t+16t²。
另一方面，由严格凹性 √45+√37<2√41，有 √37+4t≤√37+√45-√41<√41，因此 u=i 分支始终 I4<41，其与41的最小距离为 D37=41-(√37+4t)²。精确比较
\[
D37-D45=8t(\sqrt{45}-\sqrt{37}-4t)\ge0
\]
（t>0 时严格正），所以所有来源都满足 κ≥D45。

构造达到该界的来源：取 u=-i，w=a-bi=6+3i，并令
\[
t=\min(\sqrt\beta,\sqrt{\beta_c}),\qquad
v=\frac{i t}{\sqrt{45}}(6+3i)=\frac{t}{\sqrt{45}}(-3+6i).
\]
则 |v|²=t²≤β，w+4iv=(1-4t/√45)w，故 I4=(√45-4t)²。β≤βc 时恰达到 D45，β≥βc 时恰等于41。此来源同时满足额外观测，因为 |v|<1/10，从而 Cv=|1+v|²<(11/10)²<10；又 |d|<4、|e|<3、|1-i|=√2<3/2，所以 I5=|d(1-i)+ev|²<(63/10)²<100。完整充分性成立。证毕。

## 3. 定理 B：I2、Cu、I3 同时带噪的全称 PSD 秩一排除

设 ε∈[0,1/100]、β≥0、κ≥0。考虑**任意** Hermitian PSD 三阶矩阵 H（H11=1），满足

\[
r=H22=I2\in[1-\varepsilon,1+\varepsilon],\quad
s=Cu\in[2-\varepsilon,2+\varepsilon],\quad
t=H33=I3\in[0,\beta],\quad
I4\in[41-\kappa,41+\kappa].
\]

其余 Cv、I5 的任何测量区间可额外交入。令 H12=x+iy，因 s=1+r+2x，必有 x=(s-1-r)/2、|x|≤ε。**对一般 PSD H（不是仅 rank-one 的特例）**，原始第4 Port 的精确恒等式为

\[
I4=\underbrace{7-5r+\frac{39}{2}s+4y}_{j_0}
+16t+2\operatorname{Re}(a\bar c H13+b\bar c H23).
\]

PSD 的 2×2 主子式推出 |H13|≤√t、|H23|≤√(rt)。因此

\[
|I4-j_0|\le16\beta+8\sqrt\beta(|a|+|b|\sqrt r).
\]

利用 |a|=√(53/2)<6、|b|=√(29/2)<4 及 √r≤√(1+ε)≤1+ε/2，得到

\[
\rho=16\beta+8(10+2\varepsilon)\sqrt\beta,\quad
|I4-j_0|\le\rho.
\]

而 j0-41=-5(r-1)+(39/2)(s-2)+4y，于是

\[
|y|\le Y=\frac{\kappa+(49/2)\varepsilon+\rho}{4}.
\]

由 r≥1-ε、|x|≤ε 得到**全连续盒证书**

\[
\boxed{\det H_{\{1,2\}}\ge L_\Delta=1-\varepsilon-\varepsilon^2-Y^2,}
\]

\[
\boxed{\lambda_2(H)\ge L_2=1-2\varepsilon-Y.}
\]

第二式对 H 的左上2×2主块 B 使用 λmin(B)≥min(1,r)-|x+iy|≥1-2ε-Y，再利用 Hermitian 主子矩阵的特征值交错定理 λ2(H)≥λmin(B)。若 LΔ>0，所有可行 H 都排除 rank-one（rank-one 且 H11=1 强制该行列式为0）；若 L2>0，则其到任意秩不超过1矩阵的算子范数距离 ≥L2。该结果使用全部允许的 H13/H23 混合相关性，没有冻结 v 或令交叉项为零。

**纯有理证书：** 对有理 β，可以提供有理 τ≥0 且 τ²≥β，以 ρrat=16τ²+8(10+2ε)τ 代入；验证只需有理数算术与原始恒等式，无需浮点。

**具体全部附加观测均有非零宽度的反例。** 取 ε=1/10000、β=1/1000000、τ=1/1000、κ=1，另要求
Cv∈[1-ε,1+ε]、I5∈[709/32-ε,709/32+ε]。精确得到

\[
\rho=50011/625000,\quad Y=2706169/10000000,
\]
\[
\boxed{L_\Delta=92666648343439/100000000000000>0,\quad
L_2=7291831/10000000=0.7291831>0.}
\]

此测量盒**并非空盒**：H0=diag(1,1,0) 确实满足所有测量，给出 (I1,I2,I3,Cu,Cv,I4,I5)=(1,1,0,2,1,41,709/32)，且 rank(H0)=2。另一方面，**整个连续盒不存在任何单相干复来源**，每个可行 PSD 均与任何 rank-one 矩阵至少相距 0.7291831（算子范数）。

## 4. 执行、外部来源与 BRC 边界

在 Python 3 / SymPy 1.14 中确实执行 research_notes/prefix408_exact_checker.py，从原始 A 重新推导末两 Port 系数、一般 PSD 交叉项恒等式、无理代数临界见证、正宽度有理证书和双来源检查，三个检查均 PASS；准确原始 stdout 在 research_notes/prefix408_execution.log。本说明的全称域来自上述逐式证明，而不把有限测试次数当作完整穷举。未执行通用 CAD/Lean 或原生 X6/typed BRC 演算，未取得独立数学审阅。

背景文献：Candès–Strohmer–Voroninski，PhaseLift: Exact and Stable Signal Recovery from Magnitude Measurements via Convex Programming (arXiv:1109.4499)；Gao Huang–Song Li，PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate (2026-08-03，arXiv:2608.02450)。它们的随机/编码观测假设与此固定五 Port 逆问题不同，不构成冲突。本轮增量是这个**具体确定性 Port 系统**的锐阈值及可回放 PSD 秩缺口证书，并非 PhaseLift 原理的发明。

BRC：COMPOSE_APPLIED，只在来源/相位/联合观察保真层面采用，不声称 REUSE_EXECUTED 的 typed BRC 运算；实/复连续矩阵只作为外部有效模型。P000 原生六轴、120° 原生正角、旋转切片和心跳世界仍按已有公理处理；物理桥梁须另证。

## 5. PREFIX-409：唯一最小未完方向

收窄定理 A 的 Cv 与 I5 为接近名义值的**非零窄区间**，研究 κ*(ε,β,ηv,η5) 的真实联合最优值和可验证代数临界证书；同时把本轮 LΔ/L2 证书并入 PREFIX-405 全六项带噪 NO 体系，补齐只有边界来源的全输入 YES 判定。不得把本文宽 Cv/I5 的临界值冒充窄盒阈值；原生 P000 X6/typed BRC 对应属于另一个证明义务。

正式任务 Owner、CLAIM、Result/Review 与数学准入均未因这一科研文本保存而改变。