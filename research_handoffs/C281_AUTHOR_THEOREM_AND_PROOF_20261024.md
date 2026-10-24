# C281 — 四组碰撞外包区域的单切线全局严格正性证书

**2026-10-24 · AUTHOR EXACT · UNREVIEWED · NOT ADMITTED**

## 来源与范围

账户 GLOBAL_KNOWLEDGE_V1 固定读取 main@8edfec2fa963580701d0c8912648b6a9965493ec（规范入口、P000、ACTIVE 心跳世界及研究政策）；Enterprise Math 读取 main@4f7169291a872467496de179666f456e67869749（原生X6、portable research、控制合同）。原始数据继承 C275 自包含精确79节点、35基本盒，先前C279已用11,245叶建立同一父盒的严格正性。此处给出**数学上不同的、无需任何二分叶的解析证书**，并将统一裕量从此前作者级 $10^{-6}Q$ 改进到 $Q/4000$。不主张原生GF(2)-BRC或六维Cell定理。

记活动节点集合 $I=\{5,50,55,56\}$、其余固定节点 $J$；$Q=2^{128}$、$H=2^{166}$、$A=6912\cdot50000^2/17^2$、$Z=141421356237309504880/10^{20}$。固定节点 $U_0<\dots<U_{78}$ 与35个基本盒的全部有理输入在自包含程序中。

固定支路 $T_j$ 与活动支路 $M_k$ 定义为

$$
B_j=\left\lfloor \frac{QA}{H[(2-U_j^2)(3-U_j^2)]^3}
 \prod_{r\neq j}\frac{Z-U_r}{|U_j-U_r|}\right\rfloor>0,
\quad
T_j(v)=B_j\prod_{k\in I}\frac{(Z-v_k)|U_j-U_k|}{(Z-U_k)|U_j-v_k|},
$$

$$
M_k(v)=\frac{QA}{H[(2-v_k^2)(3-v_k^2)]^3}
 \prod_{j\in J}\frac{Z-U_j}{|v_k-U_j|}
 \prod_{r\in I\setminus\{k\}}\frac{Z-v_r}{|v_k-v_r|},
\quad F(v)=\sum_{j\in J}T_j(v)+\sum_{k\in I}M_k(v).
$$

研究域 $P$ 为四维有理**辅助读出参数盒**，不是独立的原生低维世界：

$$
P=[1/135,6/409]\times[34/49,28/39]
\times[60/77,87/109]\times[19/24,41/51].
$$

**C281定理**：对 $P$ 内全部满足原节点邻域、正分母和 $v_5<v_{50}<v_{55}<v_{56}$ 的合法实数配置，

$$
\boxed{F(v)>\frac{4001}{4000}2^{128}.}
$$

精确有理端点检查表明 $P$ 完整包含 H(8,18)、H(13,18)、H(18,25)、H(18,34)，包括无限接近 $v_{55}=v_{56}$ 的合法部分，碰撞奇点本身不属于定义域。

## 证明：凸核减去受控凹分子

对每一个79条严格正支路 $S_s\in\{T_j,M_k\}$，定义 $N_j=I$（固定支路），$N_k=I\setminus\{k\}$（活动支路）。在固定极点不穿越且节点顺序严格保持的凸有序域内，

$$
C_s(v)=\log S_s(v)-\sum_{r\in N_s}\log(Z-v_r)
$$

为凸函数。固定支路的非恒定项是 $-\sum_{r\in I}\log|U_j-v_r|$；活动支路的非恒定项是 $-3\log(2-v_k^2)-3\log(3-v_k^2)$、$-\sum_{j\in J}\log|v_k-U_j|$、$-\sum_{r\ne k}\log|v_k-v_r|$。这些在当前无极点有序域上均凸。**不假定整个 $\log S_s$ 凸**；其凹贡献 $\log(Z-v_r)$ 必须支付误差预算。

选单个有理锚点

$$
t=(1253/125000,\ 70489/100000,\ 79171/100000,\ 41/51).
$$

设每个坐标的盒端点为 $l_r,h_r$，并定义

$$
\rho_r=\max(t_r-l_r,h_r-t_r),\qquad
e_r=\frac{\rho_r^2}{2(Z-h_r)^2},\qquad E_s=\sum_{r\in N_s}e_r.
$$

由于 $\frac{d^2}{dx^2}\log(Z-x)=-1/(Z-x)^2\ge-1/(Z-h_r)^2$，
积分二阶余项及凸核的支撑切线给出对所有合法 $v\in P$：

$$
\log S_s(v)\ge \log S_s(t)
 +\nabla\log S_s(t)\cdot(v-t)-E_s.
$$

应用 $e^x\ge1+x$，无需任何浮点指数计算，

$$
S_s(v)\ge S_s(t)[1+\nabla\log S_s(t)\cdot(v-t)-E_s].
$$

这条式子即使方括号为负也有效。各支路相加形成一个全局仿射下界：

$$
F(v)\ge F(t)+\nabla F(t)\cdot(v-t)-E,\qquad
E=\sum_s S_s(t)E_s.
$$

固定支路的精确对数梯度是

$$
\partial_{v_r}\log T_j(t)=-\frac1{Z-t_r}-\frac1{t_r-U_j}.
$$

活动支路的本坐标和其他坐标分别为

$$
\partial_{v_k}\log M_k(t)=
\frac{6t_k}{2-t_k^2}+\frac{6t_k}{3-t_k^2}
-\sum_{j\in J}\frac1{t_k-U_j}
-\sum_{r\ne k}\frac1{t_k-t_r},
$$

$$
\partial_{v_r}\log M_k(t)=-\frac1{Z-t_r}+\frac1{t_k-t_r},\quad r\ne k.
$$

以上所有在锚点的质量、梯度、误差项都是精确有理数。标准库 Fraction 直接给出 $\nabla F(t)$ 四个分量符号为 $(+,+,+,-)$，故仿射函数在整个 $P$ 的最小端点是 $v_*=(l_5,l_{50},l_{55},h_{56})$。唯一必须检验的有理数不等式为

$$
L=F(t)+\nabla F(t)\cdot(v_*-t)-E,\qquad
\boxed{4000L>4001Q}.
$$

程序逐分支以原始整数质量计算，确切执行分数交叉比较。只为展示的值：$F(t)/Q\approx1.000870361011162$、$E/Q\approx0.000577896808836$、仿射端点增量$/Q\approx-0.000005995193132$，所以 $L/Q\approx1.000286469009194$。这些小数不是判断证据。定理证毕。

## 验证及未完成事项

自包含 C281_ONE_TANGENT_EXACT_REPLAY.py 包含源模型全部79节点、35基本盒和每条质量计算，在常规Python标准库 Fraction 上核验单次严格比较、四组父盒包含及梯度符号；本地已执行且隔离解包重跑均返回 C281_ONE_TANGENT_GLOBAL_EXACT_PASS。完整中文较长证明及同一模型的本地科研包亦保留为作者材料。

BRC适用性：79条正质量支路保留标签，不把加权总量直接等同原生带符号/相位/端口的BRC；原生状态到辅助读出的观察与未来操作保真桥仍开放。下一步对凸核证明、C275的187条阈值交叉线段、C254编号3/11分母奇点及原生桥接开展独立复验。

原生 em_control_tasks 返回 CONTROL_QUOTA、em_session_start 返回 STATIC_READONLY_SCOPE_DENIED（operation_sent=false），所以没有活动Owner实时核验、正式CLAIM、Source Result、Driver审查或数学接纳。本研究仅作为GitHub作者级分支证据；不经Google Drive绕过权限拒绝。
