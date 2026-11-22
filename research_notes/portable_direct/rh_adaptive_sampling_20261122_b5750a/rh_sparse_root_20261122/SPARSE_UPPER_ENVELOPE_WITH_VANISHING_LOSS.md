# 稀疏真实样本的直接上包络：算术损失趋零与有理能量求和

Researcher-ID: `EM-DIRECT-B5750A / TASK_RESEARCH`  
Research-Activity-ID: `RA-60C6D083A81B19084A74C5BA`  
Batch started: 2026-11-22 (Asia/Hong_Kong)  
Status: 作者组合证明；相关分支负载论证已交叉核对。

科学基础冻结于 `enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`。沿用完整整数道路、单位、合数、全部厚度标签、真实端点与前史。所有标量序列以选定原生 X6 Cell 锚点上的 `c_*+nE_1` 索引；已观察数据和有界未观察残差均保留其类型，辅助上界不取代完整原状态。

本稿组合两份新结果：`rh_partial_frontier_20261122/SPARSE_SOURCE_ENVELOPES_AND_MONOTONE_QUERIES.md` 的样本源界包络，以及 `rh_arithmetic_next_20261122/ARITHMETIC_FINE_REMAINDER_BOUNDS.md` 的算术 Green 界。它把可计算上界直接接到完整 q 的正能量，无需把真实细余项能量作为预算输入。

## 1. 同一完整道路与统一匹配界

对终点 B 选择一组既定稳定厚度节点及精确权，所有 n≤B 共用该组参数。实际道路为

\[
q(y)=\sum_{2\le n\le y}D_n(y/n-1)
-y\log y+(1+\gamma)y,
\qquad D_1=0.
\]

在整数处

\[
f_n=-\Delta^2q_n=(\kappa_n-D_n)/n,
\quad \kappa_n=n\Delta^2(n\log n).
\]

取一个对整个前缀共同有效的认证上界

\[
|D_n-\Lambda(n)|\le\varepsilon_B,
\quad n\le B.
\tag{1}
\]

该界来自已有直接厚度插值余项，与逆卷积误差 `c-c*=mu I` 的论证分别保留。稳定族可取 `epsilon_B=O(B^(-beta)/log B)`，`beta=log 8-1>1`。构造有理实现时可以用更大的认证有理上界，只需保持所声明的渐近界或有界性。

记 `H_n=sum_{j=1}^n 1/j`、`H_0=0`，则

\[
\Delta^2(nH_n)=1/n.
\tag{2}
\]

令 `Pi` 包含全部真实块端点，`I_Pi` 表示使用真实样本值的分段仿射插值，`G_Pi` 是逐细单元零端点 Green 算子。闭窗口权为 `w_n=n^(-2)`。

## 2. 精确已知势与直接正上包络

先取

\[
g_n=n\log n+\varepsilon_B nH_n.
\]

由式 (1)—(2)，

\[
\Delta^2(q+g)_n=(D_n+\varepsilon_B)/n\ge0.
\]

所以 `q+g` 在全部窗口整数上离散凸，其任意真实样本割线均在它上方。定义

\[
\boxed{U_\Pi=I_\Pi(q+g)-g\ge q.}
\tag{3}
\]

在所有已观察节点上 `U=q`，包括真端点。在每个细单元内，二者之差的端点为零，且其负二阶差分为 `(D+epsilon_B)/n`，故

\[
\boxed{
U_\Pi-q=G_\Pi((D+\varepsilon_B)/n),
\qquad
0\le U_\Pi-q
\le G_\Pi(\Lambda/n)+2\varepsilon_BG_\Pi(1/n).
}
\tag{4}
\]

这一误差是非负 Green 像。它不含旧粗骨架的独立覆盖项，也不需要取得真实细余项 `P=q-I_Pi q` 的能量才能计算 `U`。

配套样本定理还证明了：固定精确样本和同一单侧内部源界时，式 (3) 是相应信息类的逐点最大成员。新增真实样本 x 时，包络恰减去一个非负三角帽，因而逐点单调下降。附加双侧源界或其他算术信息会缩小信息类；这里不把单侧最优性扩大到更多信息的情形。

## 3. 全有理已知势版本

从已有背景展开可得，对全部 n≥1，

\[
1\le\kappa_n\le1+\frac1{2n^2}.
\tag{5}
\]

固定 A≥2，选有理认证上界 epsilon_B，置

\[
C=1+\frac1{2A^2}+\varepsilon_B,
\qquad g_n=CnH_n,
\]

\[
\boxed{U_\Pi=I_\Pi(q+CnH_n)-CnH_n.}
\tag{6}
\]

此时 `Delta^2(q+g)=(D-kappa+C)/n>=0`，故仍有 `U>=q`，并且

\[
\boxed{
0\le U_\Pi-q
=G_\Pi((D-\kappa+C)/n)
\le G_\Pi(\Lambda/n)+\rho_BG_\Pi(1/n),
\quad \rho_B=2\varepsilon_B+\frac1{2A^2}.
}
\tag{7}
\]

原 q 的真实样本仍可能含非有理量；式 (6) 中的已知势和几何为有理。使用认证有理样本时的完整误差在第 5 节支付。

## 4. 算术损失可以随窗口远移趋零

外部算术输入为 Montgomery–Vaughan (1973), *The large sieve*, Theorem 2, printed p.121, 式 (1.12)：

\[
\pi(M+N)-\pi(M)\le2N/\log N,
\quad M>0,\ N>1.
\]

原作者 [PDF](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf) 已实际核读；配套算术稿给出使用范围、初等 Chebyshev 界和全部 Green 计算。

将辅助 `Lambda` 分为素数与高次素数幂。对一块 `[X,Y]`、`Y<=2X`，细单元长度 h，正 Green 列平方范数至多 `h^3/32`。因此素数部分满足

\[
\|G_\Pi(\Lambda\mathbf1_{\rm prime}/n)\|_{w,[X,Y]}^2
\le\frac{(\log Y)^2}{8X^4}
\sum_{h\ge2}\frac{h^5}{(\log h)^2}.
\tag{8}
\]

式 (8) 按本块全部细单元求和，h 是各单元长度，重复长度分别计数。

高次素数幂的总质量至多 `12 sqrt Y`，给出在最大步长 `delta_X<=X^(3/4)` 时

\[
\|G_\Pi(\Lambda\mathbf1_{\rm higher\ power}/n)\|_{w,[X,Y]}^2
\le9X^{-3/4}.
\tag{9}
\]

此外

\[
\|G_\Pi(1/n)\|_w^2
\le T_\Pi:=
\sum_{[X,Y]}\frac1{120X^4}\sum_{[L,R]\subset[X,Y]}(h^5-h).
\tag{10}
\]

所以式 (7) 在任意允许网格上都有显式总误差界

\[
\boxed{\|U_\Pi-q\|_w
\le\|G_\Pi(\Lambda\mathbf1_{\rm prime}/n)\|_w
+\|G_\Pi(\Lambda\mathbf1_{\rm higher\ power}/n)\|_w
+\rho_B\sqrt{T_\Pi}.}
\tag{11}
\]

固定幂窗口 `B=floor(A^lambda)`、`lambda>1`，按倍增块分解并保留真实尾端。选

\[
h_X\le H_X:=\frac{X^{3/4}}{(\log X)^\alpha},
\qquad \alpha\ge0.
\tag{12}
\]

函数 `h^4/(log h)^2` 在 h≥2 递增；对充分大的 X，`log H_X>=(log X)/2`。因此式 (8) 每块为 `O((log X)^(-4alpha))`，式 (10) 亦如此。块数为 `O_lambda(log A)`；式 (9) 在倍增块上的和为 `O(A^(-3/4))`。对稳定匹配族，rho_B 有界，得到

\[
\boxed{
\|U_\Pi-q\|_w^2
=O_{\lambda,\alpha}((\log A)^{1-4\alpha})
+O(A^{-3/4}).
}
\tag{13}
\]

由逐点 `q<=U` 和正部的 1-Lipschitz 性，

\[
\boxed{
\|q_+\|_w\le\|U_+\|_w
\le\|q_+\|_w+\|U-q\|_w.
}
\tag{14}
\]

故 **alpha>1/4 时，只由真实点样本与已知势计算的上包络，其正能量根与完整道路正能量根之差趋零**。alpha=1/2 时误差根为 `O(1/sqrt(log A))`。

取规则整数步长 `floor H_X`，H_X≥2 后每块节点数至多 `2(Y-X)/H_X+2`。沿倍增块求和，

\[
\boxed{\#\Pi=O_{\lambda,\alpha}(B^{1/4}(\log B)^\alpha).}
\tag{15}
\]

误差界允许更密的不规则网格；式 (15) 的节点数上界针对上述规则构造。式 (14) 是根能量差，不将它未经其他增长界转换为平方能量绝对差趋零。它也没有证明真实 q 的正能量本身趋零或次幂增长；该算术问题继续保留。

## 5. 最终 q 样本可采用固定绝对精度

若每个样本取认证有理上端 r_i，满足

\[
0\le r_i-q(x_i)\le\delta_A,
\]

使用同一有理势构造

\[
\widehat U=I_\Pi(r+CnH_n)-CnH_n.
\]

仿射插值是非负重心组合，所以

\[
0\le\widehat U-U\le\delta_A.
\]

而 `sum_{n=A}^B n^(-2)<=1/(A-1)`，因此

\[
\boxed{
0\le\|\widehat U_+\|_w-\|q_+\|_w
\le\|U-q\|_w+\frac{\delta_A}{\sqrt{A-1}}.
}
\tag{16}
\]

所以固定绝对样本误差就足够；更一般地，只需 `delta_A=o(sqrt A)`。例如若 q 的认证区间宽度≤1，取其上端的向上整数舍入，可令 `delta_A<=2`，仍得到渐近准确的正能量根上界。精确样本的 U 在节点等于 q；上舍入后的 Uhat 在节点等于 r，端点舍入成本已由式 (16) 计入。

这是对**最终 q 观察值**的精度结论。由于 q 含两项完整前缀矩及中心项，内部计算必须控制相消误差以取得该最终绝对精度；本结论没有给中间量任意降精度的许可，也不把取样数减少当成完整道路生成成本同比减少。

## 6. 用六个谐和矩精确汇总全部整数能量

式 (6) 在一个细单元内部可写成

\[
U(n)=a n+b-CnH_n,
\qquad U(n)/n=a+b/n-CH_n.
\tag{17}
\]

其中 a,b 由两端样本和已知势确定。若端点样本及 C 为有理，则 a,b 有理。由于 `Delta^2U=-C/n<0`，该单元中 U>0 的整数支撑至多为一个连续段；可先定位离散峰，再定位两侧符号边界。所需判断只涉及式 (17)，不读取任何新 q 值。

置 `H_N^(2)=sum_{n=1}^N n^(-2)`，N=0 时以下各量均为零。六个前缀矩为

\[
\begin{aligned}
S_0(N)&=N,& S_1(N)&=H_N,&S_2(N)&=H_N^{(2)},\\
T_0(N)&=(N+1)H_N-N,\\
T_1(N)&=\tfrac12(H_N^2+H_N^{(2)}),\\
T_2(N)&=(N+1)H_N^2-(2N+1)H_N+2N.
\end{aligned}
\tag{18}
\]

它们分别等于 `sum 1`、`sum 1/n`、`sum 1/n^2`、`sum H_n`、`sum H_n/n`、`sum H_n^2`。后三个等式可直接用 H_N=H_(N-1)+1/N 作一阶差分并核验 N=0；因此不是连续积分近似。

令 `Delta Z=Z(v)-Z(u-1)`。在已定位的正值整数段 `[u,v]` 上，全部正能量精确为

\[
\boxed{
\sum_{n=u}^v\frac{U(n)^2}{n^2}
=a^2\Delta S_0+b^2\Delta S_2+C^2\Delta T_2
+2ab\Delta S_1-2aC\Delta T_0-2bC\Delta T_1.
}
\tag{19}
\]

每个细单元只对严格内部求和，再把所有已观察节点的 `(q(x_i))_+^2/x_i^2` 加一次，得到完整闭窗口能量；上舍入版本使用 r_i。零值点对能量无贡献。这样可以按有限个谐和矩汇总全整数人口，没有抽样替代求和。

精确谐和数的分母位数会增长；式 (19) 减少显式求和和新 q 读取，不自动建立低位复杂度或整体运行提速。实际有理区间实现还应为这些矩及大项相消分配误差。

## 7. 与骨架优化、查询障碍的关系

自适应骨架稿已经证明：在同一细网格内，提升足够多的真实节点可使最优正包络等于 F_+，骨架覆盖损失转由细余项支付。本稿给出另一条直接入口：从点值和已知势构造 U，本身就包含可证明趋零的余项支付，不必输入真实细余项能量。

`rh_sampling_lower_20261122/POINT_SAMPLE_ENERGY_LOWER_BOUND.md` 在一般双侧源类中证明：全零样本仍可隐藏平方能量至少 `M^2/161280*(X/k^4-X^(-3))`。因此四分之一次幂尺度具有明确的信息下界解释。它不把一般源类的困难转写为实际算术道路的必要样本数。

本轮稀疏有限证书使用 1270 个旧道路样本，直接夹住原完整正能量；该诊断与本文无界误差定理分别成立。整体仍需估计实际 q 的正能量规模；上包络及采样结构现在有了明确、可计算且渐近消失的附加成本。

## 8. 复算与作者核对

`verify_harmonic_energy_formula.py` 以精确 Fraction 检查式 (2)、六矩一阶差分恒等式，并在多组有理系数、不同窗口和空/满/内部正支撑下验证式 (19) 与直接完整求和一致。它只验证新的求和实现，没有重算原算术道路。

算术分支逐式核对了式 (4)、(7) 的源和端点、式 (11)—(16) 的量词及采样误差。所用经典筛定理的原文已由根作者再次打开；作者交叉核对不作为独立 Project Review。
