# 少于 log B 的匹配阶：有理厚度族与全窗口误差

日期：2026-11-24，Asia/Hong_Kong。作者研究：EM-DIRECT-E7808F / TASK_RESEARCH；Activity RA-0B92AAF774CA466C1C1BC38B。继承 EM-DIRECT-B5750A 的完整道路与直接厚度插值定理。本文件是辅助标量估计，不变更 Heartbeat X6 原生状态、P000 或研究接纳状态。

## 1. 使用的完整道路和本轮接口

厚度 a_j>0 的端点 Lagrange 权为

\[
v_j=\prod_{i\ne j}\frac{a_i}{a_i-a_j},\qquad
\sum_jv_j=1,\quad\sum_jv_ja_j^r=0\quad(1\le r<m).
\]

保留全整数厚度源 D、单位 D_1=0、原背景 κ、完整前缀及同一 γ。令辅助道路 q* 只把 D 替换为 Λ。前置直接插值定理给

\[
|D_n-\Lambda(n)|\le A_m(\log n)^{m+1},\qquad
A_m=\frac{\prod_ja_j}{(m+1)!}.
\]

本轮 matching_transfer 分支证明：对任意固定 0<c≤1，若 k=m+1≥c log B，置 η_B=A_m(log B)^k，则

\[
\boxed{\|q-q^*\|_{w,[A,B]}
\le\frac{\eta_B\sqrt{B-A+1}}{c(c+1)}.}\tag{1}
\]

同一界适用于任意包含真实 A、B 的节点插值。这里 w_n=n^{-2}，闭窗口包含两端。用到的初等核界可独立复核：令 ρ=c，则

\[
\left(\frac{\log n}{\log y}\right)^k\le(n/y)^c,
\quad
\sum_{n=2}^y(y/n-1)(n/y)^c
\le y\int_0^1t^{c-1}(1-t)dt=\frac y{c(c+1)}.
\]

最后一步因为 0<c≤1 时 t^{c-1}(1-t) 单调递减，右端点和受积分控制。完整精确前缀差仍是 Σ(y/n−1)(D_n−Λ(n))。

## 2. Chebyshev 根的乘积与权重

固定有理 0<θ≤1。用多项式递推 T_0=1、T_1=z、T_{r+1}=2zT_r−T_{r-1} 定义 T_m；取其 m 个根 z_j∈(−1,1)，并令 b_j=θ(1+z_j)/2。节点可完全以有理多项式根隔离描述；不需要以三角函数数值作为算法输入。

由 T_m 的首项系数 2^{m−1} 和 T_m(−1)=(−1)^m，精确有

\[
\boxed{\prod_jb_j=2(\theta/4)^m.}\tag{2}
\]

这些是经典 Chebyshev 恒等式；参考 NIST DLMF §18.3（首项系数、式18.3.1–2离散正交）及 §3.11(ii)（多项式递推）。本轮的新部分是将它们接到 (1) 及下述显式有理扰动、匹配阶预算。

设 ℓ_j(z) 为这些根上的基 Lagrange 多项式。离散正交直接给

\[
\ell_j(-1)=\frac1m+\frac2m\sum_{r=1}^{m-1}(-1)^rT_r(z_j).
\]

因为 |T_r(z)|≤1（−1≤z≤1），

\[
\sum_j|\ell_j(-1)|\le2m-1.\tag{3}
\]

式 (3) 采用一个足够的粗界，不声称优化端点 Lebesgue 常数。

## 3. 可以采用精确有理节点，无需把近似根冒充真根

按递增顺序排列 b_j，选择任意有理 a_j 满足

\[
|a_j-b_j|\le\frac{\theta}{128m^3}.\tag{4}
\]

Chebyshev 根的标准位置及 sin t≥2t/π（0≤t≤π/2）给出

\[
\min(b_1,\theta-b_m)\ge\frac{\theta}{4m^2},
\qquad b_{j+1}-b_j\ge\frac{2\theta}{m^2}\quad(m\ge2).
\]

所以这些有理节点仍严格位于 (0,θ)、保持次序。每个分子因子的相对变化≤1/(32m)，每个差分母因子的相对变化≤1/(128m)。由

\[
(1+u)^r\le\frac1{1-ru},\quad
(1-u)^r\ge1-ru\quad(ru<1),
\]

得到

\[
\prod_ja_j\le\frac{32}{31}\prod_jb_j
<4(\theta/4)^m,
\]

\[
|v_j|\le\frac{32}{31}\frac{128}{127}|\ell_j(-1)|
<2|\ell_j(-1)|,
\qquad \boxed{\sum_j|v_j|<4m.}\tag{5}
\]

m=1 时直接用 b_1=θ/2，权重为1；同样满足上述结论。

对有理 θ，用 T_m 的有理根隔离把每个 b_j 包在宽度≤θ/(512m³) 的区间内，再将中点取到步长≤θ/(512m³) 的二进制网格，即可保证 (4)。所得 v_j 根据真实有理 a_j 重新精确计算，所有匹配矩精确为零；没有沿用理想根的权重。

对固定 θ，二进制节点仅需 O(log m) 位，单个权重的显式分子分母至多 O(m log m) 位，全部权重的直接表示为 O(m²log m) 位。这里不声称构造、求根、厚度计算或验证是免费的；这只是显式输入表示长度和权重总变差的上界。

## 4. 无界窗口上的阶数与误差

令 B≥2，L=log B，取

\[
m=\lceil c\log B\rceil,\qquad 0<c\le1,
\qquad \beta(c,\theta):=c\log\frac{4c}{e\theta}.
\]

如果 β(c,θ)>1/2，则 eθ/(4c)<1。对满足 (4) 的有理节点，由 m!≥(m/e)^m、(5) 和 m≥cL 有

\[
\begin{aligned}
\eta_B
&\le\frac{4(\theta/4)^mL^{m+1}}{(m+1)!}\\
&\le\frac{4L}{m+1}\left(\frac{e\theta L}{4m}\right)^m
\le\frac4c B^{-\beta(c,\theta)}.
\end{aligned}\tag{6}
\]

将 (6) 代入 (1)，对任意 1≤A≤B 及任意节点网格都有

\[
\boxed{\|q-q^*\|_{w,[A,B]}
\le\frac{4}{c^2(c+1)}B^{1/2-\beta(c,\theta)}\longrightarrow0.}\tag{7}
\]

因此，去掉 k≥log B 的旧限制后，可以在仍具有多对数权重总变差和精确有理输入的族上降低匹配阶。

特别取 θ=1/2、c=7/10，则

\[
\beta=\frac7{10}\log\frac{28}{5e}
=0.5059366184\ldots>\frac12.
\]

故 m=⌈0.7 log B⌉ 已给全窗口误差 O(B^{-0.0059366184…})。也可取 c=3/4，得到 β=0.5938196019…，以稍多节点换取更快衰减。

临界方程 c log(8c/e)=1/2 的唯一相关根约为0.6965490747。它是本显式上界保证衰减的阈值，并非所有匹配构造的最优阶数下界。严密性由有理 log 区间确认 β(0.7)>1/2；小数只作阅读辅助。

## 5. 对完整道路目标的作用

本族证明匹配误差可以在整个增长窗口上消失，包括真实骨架端点的误差支付；并保留全部整数 D 的含义。它让两条道路的正部根能量之差≤(7)，不提供 q* 自身的统一算术能量估计。

本轮1270个旧采样点的改进仍使用旧11个固定有理厚度。本节是另一个可构造的无界匹配族，两个计算对象保持区分。节点数少约30%是相对 m≈log B 的充分条件比较，不是端到端运行时间加速声明。

## 6. 可复核证据与来源

- `certify_matching_order.py`：用有理多项式根隔离取得有理节点；逐个有理端点检查多项式符号及所有隔离区间的互不相交；精确核对产品上界、权重总变差与每个匹配矩；有理级数认证 β(0.7)>1/2。
- `matching_order_certificate.json`：固定 m=1,…,16 的节点、权重、根区间与验证结果。有限计算用于核对构造实现；全m结论由上面的解析证明承担。
- NIST DLMF §18.3: https://dlmf.nist.gov/18.3 。§3.11(ii): https://dlmf.nist.gov/3.11#ii 。
- 前置实际厚度误差：上一轮复算包 `dependencies/ARITHMETIC_FINE_REMAINDER_BOUNDS.md` §1；本轮全k核：`matching_transfer/ALL_ORDER_MATCHING_KERNEL.md`。
