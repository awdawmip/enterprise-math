# R273：六通道正权 BRC 共同效果纤维的精确前导常数及最终峰值相等定理

日期：2026-10-25。**作者侧解析证明、精确整数/符号核验；DRIVER_UNREVIEWED / NOT_ADMITTED。** 本文仅涉及 R268–R272 已固定的二字母、正权、有序、形式六槽 BRC 辅助模型。不能直接外推至 P000 原生六维 Cell、R193 端口或物理心跳。

## 1. 原模型和主定理

每个公开动作字母 a=0/1 对控制 q 的边 (q',η,b) 为：
- q=0：0→(2,−1,−1)，1→(2,+1,−1)；
- q=1：0→(0,−1,−1)，1→(0,+1,−1)；
- q=2：0→(1,+1,+1)，1→(2,+1,−1)。

初始 q=0，完整仿射效果 (ε,k)=(+1,0)，逐步复合 ε'=ηε，k'=ηk+b。DFA r=0 表示无连续00且末字非0（含空词），r=1 表示无00且末字0，r=2 表示已出现00。六种通道是 c=(q,h)，h=1_{r=2}。H_n(c,g) 是长度n、完整效果g的**原始有序词数**，每个原始词正整数权重1。定义

\[
B_n=\max_g\min_{q=0,1,2;\,h=0,1}H_n((q,h),g),\qquad
P_n(g)=H_n((0,0),g),\qquad
\Lambda_n=\max_gP_n(g).
\]

未出现00而终点q=0的词只能在末位1结束（或为空），故 P_n 恰是无00的 q=0 重置效果纤维。于是所有 n 都有 B_n≤Λ_n。

**定理 R273。** 设

\[
\varphi=\frac{1+\sqrt5}{2},\quad
\sigma^2=\frac32+\frac{7\sqrt5}{10},\quad
C_*=\frac1{5\sqrt{2\pi\sigma^2}}
=0.04557296470094735\ldots.
\]

则存在某个有限但本文未数值确定的 N，满足

\[
\boxed{\forall n\ge N:\quad B_n=\Lambda_n},
\qquad
\boxed{B_n\sim\Lambda_n\sim C_*\varphi^n/\sqrt n}.
\]

而且，任何选择的最大重置纤维 g_n=(ε_n,k_n) 都满足 ε_n k_n=o(√n)。**尚不能由此宣布 N=12；也不能断言峰值偏移最终固定。**

## 2. 有序效果的可逆变元与两个有限传输矩阵

令 t=εk，则

\[
t'=t+\epsilon'b,\quad \Delta t=\epsilon'b\in\{-1,+1\},
\quad t\equiv n\pmod2,\quad k=\epsilon t.
\]

这一步保留完整效果、原始路径、正整数重数和顺序。对未出现00的来源词，恰有四类控制/末位状态 A=(q0,last0=false), B=(q1,last0=true), C=(q2,last0=false), D=(q2,last0=true)。再保留 ε=s∈{±1}，组成八个状态 A_s、B_s、C_s、D_s。允许的全部边（目标,Δt）为：

\[
\begin{array}{c|cc}
&0&1\\ \hline
A_s&(D_{-s},+s)&(C_s,-s)\\
B_s&\text{禁止00}&(A_s,-s)\\
C_s&(B_s,+s)&(C_s,-s)\\
D_s&\text{禁止00}&(C_s,-s)
\end{array}
\]

在每条边上放 Laurent 正权 u^{Δt}，得到八态 T_C(u)。初态为 A_+。矩阵幂 (T_C(u)^n)_{A_+,x} 的 u^t 系数是无00的准确原始路径数；它不是有符号振幅。

不限制00时，以 (q,s) 为六种末态，对 q=0、1、2 的边（目标,Δt）分别为

\[
\begin{array}{c|cc}
&0&1\\ \hline
(0,s)&((2,-s),+s)&((2,s),-s)\\
(1,s)&((0,-s),+s)&((0,s),-s)\\
(2,s)&((1,s),+s)&((2,s),-s)
\end{array}
\]

相应六态 Laurent 正权矩阵为 T_F(u)。记 clean 的末控制和符号/标记系数之和为 N_C(q,s,t)，full 系数为 N_F(q,s,t)。六通道与两者满足**逐效果精确恒等式**：

\[
H_n((q,0),(s,st))=N_C(q,s,t),\quad
H_n((q,1),(s,st))=N_F(q,s,t)-N_C(q,s,t). \tag{1}
\]

## 3. 特征多项式、谱投影、方差

直接对第2节完全指定的矩阵做有理函数消元，得到可以原始边独立复算的两个恒等式：

\[
\det(\lambda I-T_C(u))=
(\lambda^2+1)\left[\lambda^6-(u+u^{-1})\lambda^5+2\lambda^2-1\right], \tag{2}
\]

\[
\det(\lambda I-T_F(u))=
\lambda^2[\lambda-(u+u^{-1})]
[\lambda^3+\lambda-(u+u^{-1})]. \tag{3}
\]

八态无00图强连通，因为 A_s→D_{−s}→C_{−s}→B_{−s}→A_{−s} 可以翻转符号；C_s→C_s 是自环。其非负矩阵 T_C(1) 原始且 Perron 根为 φ。一个正右 Perron 向量，在每个符号的 A,B,C,D 类上取 (1,φ^{-1},1,φ^{-1})；相应正左向量取 (1,φ,φ²,φ^{-1})。全八态左/右内积恰为10，因此从 A_+ 出发的每个终点的谱投影权为

\[
p_{A_s}=\frac1{10},\quad
p_{B_s}=\frac{\varphi}{10},\quad
p_{C_s}=\frac{\varphi^2}{10},\quad
p_{D_s}=\frac{\varphi^{-1}}{10}. \tag{4}
\]

令 u=e^z，式(2)的 φ 邻域单根解析分支只依赖 u+u^{-1}=2cosh z，故对数根在 z=0 的一阶导数为0。隐函数微分给出

\[
\frac{d^2}{dz^2}\log \lambda_C(e^z)\big|_{z=0}
=\frac{2\varphi^4}{6\varphi^5-10\varphi^4+4\varphi}
=\frac32+\frac{7\sqrt5}{10}=\sigma^2>0. \tag{5}
\]

六态 full 图也强连通且 (2,s) 有自环。T_F(u) 的**每一行**权和等于 u+u^{-1}，故在 u=1 附近的主根是 λ_F(e^z)=2cosh z，漂移0、方差斜率1。T_F(1) 的右 Perron 向量全1，归一化左向量恰为

\[
\pi_{q,s}=1/8\ (q=0,1),\qquad
\pi_{2,s}=1/4,\quad s=\pm1. \tag{6}
\]

式(2)(3)、正特征向量、归一化和(5)均在本轮以 Python/SymPy **精确**验证；这只是无限分析证明的代数输入，不把数值有限检查当极限定理。

## 4. Fourier 谱峰唯一性与全效果一致的局部极限定理

考虑 θ∈[−π,π]，M_X(θ)=T_X(e^{iθ})，X=C,F。每条边的 Laurent 指数均为±1，故 |M_X(θ)|≤T_X(1)。若一个复杂加权矩阵达到非负原始矩阵 T_X(1) 的 Perron 谱半径，则 Perron 谱半径等号定理要求所有边相位具有同一个全局相位与起终点规范相位之比。在 clean 的 C_+、C_- 自环（full 的 (2,+)、(2,-) 自环）上，两端的规范相位抵消，自环的 Δt 分别为−1与+1，因此同时要求

\[
e^{-i\theta}=e^{i\alpha}=e^{i\theta}
\quad\Longrightarrow\quad
\theta=0\ \text{或}\ \pi\pmod{2\pi}. \tag{7}
\]

反之 T_X(−u)=−T_X(u)（所有增量都是奇数），所以 θ=0、π 确实是唯一两个外围谱峰。离开这两个峰的闭集具有统一严格谱隙。峰附近的简单特征值解析延拓（取与正实主根相连的分支）满足

\[
\log[\lambda_C(e^{i\theta})/\varphi]
=-\sigma^2\theta^2/2+O(\theta^4),\quad
\log[\lambda_F(e^{i\theta})/2]
=-\theta^2/2+O(\theta^4). \tag{8}
\]

对每个有限矩阵幂系数进行 Fourier–Laurent 反演：

\[
[u^t](T_X(u)^n)_{ij}
=\frac1{2\pi}\int_{-\pi}^{\pi}
e^{-it\theta}(M_X(\theta)^n)_{ij}\,d\theta.
\]

将积分分解为 θ=0、π 的短邻域及补集。补集由统一谱隙指数压低；邻域用单根谱投影、θ=x/√n 和式(8)的严格负二次曲率，高斯支配收敛给出主项。由于 Fourier 因子模恒为1，误差可以在所有整数 t 和有限末态上**一致地**取为 o(ρ^n/√n)。又因为 T_X(−u)=−T_X(u)，两个峰在 t≡n (mod2) 时恰好相加并产生因子2，在另一奇偶类严格为零。因此，对于 t≡n (mod2)，有以下一致局部极限式：

\[
[u^t](T_C(u)^n)_{A_+,x}
=\frac{2\varphi^np_x}{\sqrt{2\pi\sigma^2n}}
\exp(-t^2/(2\sigma^2n))
+o(\varphi^n/\sqrt n),\tag{9}
\]

\[
[u^t](T_F(u)^n)_{(0,+),(q,s)}
=\frac{2\,2^n\pi_{q,s}}{\sqrt{2\pi n}}
\exp(-t^2/(2n))
+o(2^n/\sqrt n). \tag{10}
\]

这些是无限尺度的解析推论；它们需要第3节和本节已给出的原始性、谱峰排除、零漂移、正曲率和正谱投影，不能从有限枚举直接猜测。

## 5. 证明重置峰值精确常数及共同纤维最终相等

由式(4)(9)，对任一允许奇偶的 g=(s,st)，重置纤维有**全 t 一致误差**：

\[
P_n(g)=C_*\frac{\varphi^n}{\sqrt n}
e^{-t^2/(2\sigma^2n)}
+o(\varphi^n/\sqrt n). \tag{11}
\]

选 s=+、偶 n 的 t=0、奇 n 的 t=1，给出 (1+o(1))C_*φ^n/√n 的下界；由高斯因子≤1得到同一上界，故

\[
\Lambda_n\sim C_*\varphi^n/\sqrt n. \tag{12}
\]

任选真实最大效果 g_n=(s_n,k_n)，t_n=s_n k_n。如果 |t_n|≥δ√n 的子列存在，则式(11)的高斯因子至多 e^{−δ²/(2σ²)}<1，与式(12)和中心奇偶可达点的下界矛盾。因此

\[
t_n=o(\sqrt n). \tag{13}
\]

于是固定**同一个峰值 g_n**，式(1)(4)(9)(13)给出三个 clean 通道的比值：

\[
H_n((0,0),g_n)=\Lambda_n,\quad
\frac{H_n((1,0),g_n)}{\Lambda_n}\to\varphi>1,\quad
\frac{H_n((2,0),g_n)}{\Lambda_n}\to
\varphi^2+\varphi^{-1}=2\varphi>1. \tag{14}
\]

三个 dirty 通道则由式(1)(9)(10)(13)满足

\[
H_n((q,1),g_n)=
\frac{2\,2^n\pi_{q,s_n}}{\sqrt{2\pi n}}(1+o(1))
-O(\varphi^n/\sqrt n),\quad \pi_{q,s_n}>0.
\]

所以每个 dirty 通道数与 Λ_n 之比均趋于正无穷。只有有限六通道，两种可能的符号已在统一公式里覆盖，因而存在共同有限阈值 N，使所有 n≥N 时峰值效果 g_n 的其他五种通道都严格多于重置通道，最小值恰为 Λ_n。由 B_n≤Λ_n 与对该 g_n 取最小值，得

\[
\boxed{B_n=\Lambda_n\text{ 对一切充分大的 }n},\qquad
\boxed{B_n\sim C_*\varphi^n/\sqrt n}.
\]

这是 **最终精确整数相等**，而非只是渐近比值1；仍**未得到有效数值 N**。

## 6. 已执行验证与证据范围

随附 R273_verify_publish.py 是本轮实际执行过的纯 Python/SymPy 精确程序：从原始边重建 T_C、T_F，验算两个特征多项式、特征向量归一化与方差式(5)；用无界整数计算全部来源直方图至深度400；对深度0..12的8191条原始词独立枚举交叉核对；验证深度12..400的389个 **有限** 整数等式 B_n=Λ_n。深度7..11精确不等对为 (1,2),(2,3),(2,4),(2,5),(5,6)。深度400峰值效果 (+1,−4)，重置路径数为 901002236823778700360329067399515119908453804139015642975169095731380963473764507。完整扩展版程序与长格式证据同时保留在本地研究包。

**不可混淆：**上述计算不验证全部 n；无限定理由第2–5节的解析推导承担。本轮未执行原版 enterprise_math 包，未建立 R193/P000 保真映射。原生控制 em_control_tasks 报 CONTROL_QUOTA；em_session_start 被 STATIC_READONLY_SCOPE_DENIED 阻断且 operation_sent=false。未权威核实活跃 Owner、未取得正式 CLAIM、Source Result 或独立 Driver 接纳。

## 7. 下一问题、精确来源和方法复用

首先尝试把存在性 N 证明加强成 **所有 n≥12** 的明确阈值（寻找同效果组合单射、有限状态系数非负证明或有效的谱误差上界）；其次研究峰值效果偏移序列和 1/n 修正；D(6) 正权效果条件化六控制态聚合及 R193/P000 原生映射仍开放。不能因为统一局部极限而擅自宣布任何一种原生物理主张成立。

固定 GLOBAL_KNOWLEDGE_V1 main@ad082b1ef072ce8fc4d748964b7fdfe293d84d73；P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc。研究时 EM main@9eb552f86709355b6fecaef69bf4cbc4b5f202ec。模型输入 R271 be4d5bb132f99fd932be70201161faab7a8f334d、R272 39c4801a51850d58f75ef71c9d4721e9ed8c6316；谱传输复用 R262 be6b89f3b2b9a477f747d68919625dcd0d025a95、R264 6498dfa6289b9e909a8666979f278f08d41592fa（均是其自身的原始作者证明等级）。BRC 使用决议：**COMPOSE_APPLIED / REUSE_APPLIED**；本文新贡献在保留完整正权效果的统一局部极限、峰值集中的证明及最终六通道相等。作者侧活动登记 RA-EMR3-20261025-0433-R273RESETLLT 不构成任务 CLAIM。
