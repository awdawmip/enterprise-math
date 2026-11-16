# R429｜signed BRC 右边界窗口全阶正性的有效阈值

2026-10-31 · AUTHOR_SIDE_ANALYTIC / EXACT_FINITE_CHECKED / DRIVER_UNREVIEWED / NOT_ADMITTED

## 问题、原始来源与结论

接续 R428 (Git commit 07bac45d000d8083252b2bedffc874ef94fa6606) 的固定窗口渐近全阶正性定理，解决其明确留下的“给出可计算窗口阈值 R(K)”问题。所有结论限于原始带符号 BRC 辅助组合模型，不宣称到原生 X6 的保真映射。

令 δ_{r,s}=[t^r](1−t)(1+t)^{2s}(1+t²)^{r−s}，
H_{r,s}=binom(r+s,2s)δ_{r,s}，C_r=binom(2r,r)/(r+1)。
对 0≤h≤r−2 令 B_{r,h}=H_{r,r−h}，c_{r,h}=B_{r,h}/(C_r r^h)；
对 h<0 或 h>r−2 的下标零延拓。

**新定理（有效、保守）。** 对任意整数 K≥1，设置

\[
\boxed{R(K)=2^{K+6}K^3(K+1)!(K+1)(K!)^{K+1}.} \tag{A}
\]

若 r≥R(K)，则对任意 1≤k≤K+1，以及 0≤u_1<⋯<u_k≤K、
0≤v_1<⋯<v_k≤K 且逐项 v_i≥u_i，有严格定量下界

\[
\boxed{\det[c_{r,v_j-u_i}]_{i,j=1}^k\ge \frac{1}{2(K!)^{K+1}}>0.} \tag{B}
\]

若某个 v_i<u_i，行列式因支撑结构恒为零。因此右端窗口
(c_{r,j−i})_{0≤i,j≤K} 的全部阶子式非负；所有结构上可能非零的子式严格正。
K=0 时 c_{r,0}=1，结论平凡。
正比例 C_r 与 r^{-h} 仅提供 Toeplitz 正行列缩放，未归一化 B_{r,h} 子式符号相同。

## 引理：统一、显式、逐系数有理误差

对 K≥1、r≥16K²、0≤h≤K，

\[
\boxed{\left|c_{r,h}-1/h!\right|\le 32K^3/(r h!).}\tag{1}
\]

证明：令 q=r−h，d=h−2ℓ，ℓ=0,…,h。保留原 signed 卷积每条支路：

\[
\delta_{r,r-h}=
\sum_{\ell=0}^h\binom h\ell
\left[\binom{2q}{q+d}-\binom{2q}{q+d-1}\right].\tag{2}
\]

逐支路使用精确整数恒等式
binom(2q,q+d)−binom(2q,q+d−1)=binom(2q,q+d)(1−2d)/(q−d+1)。
置

\[
P=\prod_{j=q+1}^{r}\frac{2j}{2j-1},\quad
Q=\frac{\binom{2q}{q+d}}{\binom{2q}{q}},\quad
E=\frac{r+1}{q-d+1}.
\]

从 binom(2q,q)/binom(2r,r)=4^{-h}P，得到**未丢弃符号的**恒等式

\[
\frac{\delta_{r,r-h}}{C_r}
=4^{-h}\sum_{\ell=0}^h\binom h\ell(1-2d)PEQ.\tag{3}
\]

下列均对 r≥16K²、|d|≤h≤K 成立：
log P ≤ h/(2q+1)≤K/r≤1/16，故 1≤P≤1+2K/r≤9/8；
E−1=(h+d)/(r−h−d+1)，故 1≤E≤1+3K/r≤19/16，PE<2。
由二项对称性和有限乘积

\[
Q=\prod_{i=1}^{|d|}\left(1-\frac{2i-1}{q+i}\right)
\]

得 0≤1−Q≤Σ_{i=1}^{|d|}(2i−1)/(q+i)≤K²/(q+1)≤2K²/r。
于是

\[
|PEQ-1|\le(P-1)+P(E-1)+PE(1-Q)
\le(2K+27K/8+4K²)/r\le10K²/r.\tag{4}
\]

保留 signed 支路，**只在这一步**应用完整相消恒等式

\[
2^{-h}\sum_{\ell=0}^h\binom h\ell(1−2h+4\ell)=1.
\]

由 (3),(4) 和 |1−2d|≤1+2K≤3K 得

\[
\left|2^h\delta_{r,r-h}/C_r-1\right|\le30K^3/r.\tag{5}
\]

另有完全精确的比率
binom(2r−h,h)/r^h=(2^h/h!)T，
T=∏_{i=0}^{h-1}(1−(h+i)/(2r))。
每个因子属于 [0,1]，所以 0≤T≤1，并且
1−T≤Σ_{i=0}^{h−1}(h+i)/(2r)=(3h²−h)/(4r)≤K³/r。
令 U=2^h δ/C_r，则 c_{r,h}=TU/h!，结合 (5)：

\[
|c_{r,h}-1/h!|\le\{T|U−1|+(1−T)\}/h!
\le31K³/(r h!)\le32K³/(r h!).
\]

h=0 时 c_{r,0}=1。引理证毕。

## 主定理证明：Pascal 的整数正下界 + 有限扰动

对选定 u,v，定义 A=[c_{r,v_j−u_i}]，
F=[1_{v_j≥u_i}/(v_j−u_i)!]，ε=32K³/r。
引理给出每个位置 |A_{ij}−F_{ij}|≤ε；负偏移二者都是零。
并且 |F_{ij}|≤1，|A_{ij}|≤1+ε。由行列式排列展开逐项望远镜化乘积（k! 项，每项 k 因子），

\[
|\det A−\det F|
\le k!\,k\,ε(1+ε)^{k−1}
\le(K+1)!(K+1)2^K ε.\tag{6}
\]

这里 ε≤1 由 (A) 保证。通过 binom(v,u)=v!/[u!(v−u)!] 得

\[
\det F=
\frac{\prod_i u_i!}{\prod_j v_j!}
\det[\binom{v_j}{u_i}].\tag{7}
\]

在 v_i≥u_i 条件下，Pascal 子式是一个至少为 1 的非负整数：
由平面不交路径 LGV 消去引理，det[binom(v_j,u_i)] 是不交路径族的数目。
非空性直接由路径 A_i=(u_i,−u_i) 先向右到 (v_i,−u_i)，再向上到
(v_i,0) 构成：u_i 和 v_i 都严格递增，路径互不相交。
故 det F≥1/(K!)^k≥1/(K!)^{K+1}。

把 (A) 代入 (6)：

\[
|\det A-\det F|\le1/[2(K!)^{K+1}],
\]

于是 det A≥1/[2(K!)^{K+1}]，即 (B)。
若 v_i<u_i，对应顺序下不存在任何仅由允许位置 v_j≥u_i 构成的
完全匹配；每一个行列式排列积都含有零因子，故行列式恒为零。证毕。

## 精确有限交叉核验

同目录 R429_VERIFY.py 使用纯 Python 标准库整数、Fraction 和
Bareiss 行列式，复核 690 组原始 signed BRC 卷积/反向支路恒等式、
220 组误差式 (1)，以及 4914 个结构上可非零的有限窗口子式；
全部严格为正或符合不等式，返回 R429_EXACT_PASS 690 220 4914。
研究覆盖 K=3..6 的十组 (K,r)，详见 R429_EVIDENCE.json。
该程序**没有在所有理论阈值进行逐行检查**；
例如 R(1)=512，R(2)=294912，R(3)=1719926784。
无限双参数命题由上述解析证明承担。

## 边界、BRC 应用与下一问题

这是一条 *effective threshold*，不是最佳阈值；它的巨大超阶乘增长来自
对所有排列积逐项粗估，以及 Pascal 子式下界。R426 已证明完整行 r≥4 非 PF∞，
本结果仅断言每个固定右端窗口的 eventual 严格正性，两者不矛盾。

BRC 接口：复用精确 signed convolution 及每条 ℓ 支路，在 (3) 保持支路、
符号和二项组合，只有完成支路有理误差控制后才施加 (5) 的精确相消。
这只证明声明的辅助 scalar observer；未证明对原生 X6 的未来操作/联合关系
保真，未做不可逆的信息消去正当化。

下一单元：运用 Pascal 非交路径组合与 signed BRC 支路相关性，
把 R(K) 降为 exp(O(K log K)) 或多项式，或找出随 r 增长的窗口中第一
PF∞ 破坏位置。独立 Driver 审核/正式 Source Result 仍待当前 owner 和
权限路径，P000 与 ACTIVE 世界观未修改。

固定来源：GLOBAL_KNOWLEDGE_V1 main@7043f52faf40cf50cdb808d77a51e7dbbf769c1f；
Enterprise Math main@a8a17b9449cd61aa9ab13cc56894f6cf953247ff；
R428 immutable 07bac45d000d8083252b2bedffc874ef94fa6606。
