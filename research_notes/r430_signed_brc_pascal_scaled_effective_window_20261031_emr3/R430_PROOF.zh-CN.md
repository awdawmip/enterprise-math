# R430 — signed BRC 右边界的阶数敏感有效阈值（作者侧证明）

日期：2026-10-31。状态：AUTHOR_SIDE_ANALYTIC / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED。

固定 GLOBAL_KNOWLEDGE_V1 为 main@970b5c00edacde19d0a8c5b6a6660e77d9877f57，Enterprise Math 规范为 main@d93aeaece6d8d0916680c5de40ad66a7fbeaa18b。输入数学前沿是 R429 commit 163246e2bbdfe14ec6bd5d7f52dfc95456fab5f7 的逐系数误差引理。适用对象仅是 signed BRC 辅助组合标量读出，不声称原生 X6 保真。

## 精确定义

设 r≥2、0≤h≤r−2 为整数，定义

\[
\delta_{r,r-h}=[t^r](1-t)(1+t)^{2(r-h)}(1+t^2)^h,\qquad
H_{r,r-h}=\binom{2r-h}{h}\delta_{r,r-h},
\]
\[
C_r=\binom{2r}{r}/(r+1),\qquad c_{r,h}=H_{r,r-h}/(C_r r^h).
\]

h<0 或 h>r−2 时零延拓 c。对任意 K≥1，从索引集 {0,...,K} 各选严格递增的行 u_1<...<u_k 与列 v_1<...<v_k，研究 A=[c_{r,v_j-u_i}]。

## 新定理：阶数 p 独立选择

对任意整数 K≥1、1≤p≤K+1，设置

\[
\boxed{T(K,p)=64 K^3 p!\,p\,2^{(K+1)p}.}\tag{1}
\]

若 r≥T(K,p)，则任意上述 1≤k≤p 的子式满足：

* 若存在 i 使 v_i<u_i，则 det A=0（支撑零）。
* 若所有 v_i≥u_i，则

\[
\boxed{\det A\ge \frac34\frac{\prod_{i=1}^k u_i!}{\prod_{j=1}^k v_j!}>0.}\tag{2}
\]

取 p=K+1 即得到全阶有效阈值

\[
\boxed{\widehat R(K)=64K^3(K+1)!(K+1)2^{(K+1)^2},\quad \log \widehat R(K)=O(K^2).}\tag{3}
\]

R429 的旧充分阈值为 2^{K+6} K^3 (K+1)! (K+1) (K!)^{K+1}，其对数为 Θ(K² log K)。K≥4 时式 (3) 严格更小；K=1,2,3 保留旧阈值更紧。可统一取两者最小值。固定阶 p 的有效阈值仅为 exp(O_p(K))。以上均为保守充分条件。

## 证明：保留 signed 支路，复用 R429 精确系数引理

R429 已从原始有符号二项卷积证明：若 r≥16K²，则

\[
\left|c_{r,h}-1/h!\right|\le\eta/h!,\qquad
\eta=32K^3/r,\qquad 0\le h\le K.\tag{4}
\]

原支路恒等式为：置 s=r−h、d=h−2\ell，

\[
\delta_{r,r-h}=\sum_{\ell=0}^h\binom h\ell
\left[\binom{2s}{s+d}-\binom{2s}{s+d-1}\right].\tag{5}
\]

R429 是在逐条 signed 支路做精确有理估计后，才用
2^{-h}\sum_\ell\binom h\ell(1−2d)=1 做相消；此处不把有符号振幅解释成正权重。本轮的全新步骤是以下 Pascal 缩放与阶数敏感扰动估计。

令

\[
M_{ij}=\frac{v_j!}{u_i!}c_{r,v_j-u_i},
\quad P_{ij}=\binom{v_j}{u_i}\quad
(\binom vu=0\ \text{当}\ u>v).\tag{6}
\]

对 v_j≥u_i，由 (4) 有 |M_ij−P_ij|≤η P_ij；对负偏移二者均为0。由于 v_j≤K，0≤P_ij≤2^K。条件 (1) 保证 r≥16K²，且

\[
0\le\eta\le[2p!p\,2^{(K+1)p}]^{-1}<1.\tag{7}
\]

逐项排列展开 det，并用一项乘积替换至多 k 个因子的望远镜估计：

\[
\begin{aligned}
|\det M-\det P|
&\le k!\,k\,\eta(1+\eta)^{k-1}2^{Kk}\\
&\le k!k\eta\,2^{(K+1)k-1}\\
&\le p!p\eta\,2^{(K+1)p-1}\le\tfrac14.
\end{aligned}\tag{8}
\]

关键差别是：在应用行列式扰动前，就将指数核的阶乘因子化为整数 Pascal 子式，而不是在未缩放的指数核上取极小下界 (K!)^{-(K+1)}。

Pascal 子式的正性可由 Lindström–Gessel–Viennot 不交路径引理直接证明。源点 A_i=(u_i,−u_i)，终点 B_j=(v_j,0)，向右/向上格路径数是 binom(v_j,u_i)；因此 det P 为非负整数。若逐项 v_i≥u_i，则从 A_i 先水平到 (v_i,−u_i)、再竖直到 B_i 的 k 条路径因 u、v 均严格递增而两两不交，故 det P≥1。若某个 v_i<u_i，有序支撑不容许完全匹配，任何排列项都含零因子，故 det P=det M=det A=0。

于是对结构非零子式，det M≥3/4，并由行列正缩放

\[
\det A=\frac{\prod_i u_i!}{\prod_j v_j!}\det M
\]

推出 (2)。证毕。

## 次要推论：基于同一相对误差的二阶多项式界

若 r≥256K^4，则 η≤1/(8K)。任意结构非零二阶子式，令 a=v_1−u_1≥0、e=v_2−v_1≥1、d=u_2−u_1≥1；主对角指数核积 X=1/[a!(a+e−d)!]。副对角与主对角之比在 a≥d 时为

\[
\rho=\frac{a!(a+e-d)!}{(a+e)!(a-d)!}\le \frac a{a+e}\le\frac{K-1}{K};
\]

在 a<d 时副对角为0。故

\[
\det A\ge X[(1-\eta)^2-(1-1/K)(1+\eta)^2]
\ge X/(2K)>0.\tag{9}
\]

这是误差引理的另一个自足推论，但并非最佳 PF₂ 界：合并 R425 全行 Turán 符号与正系数性的已给范围，还可以获得线性 r≥K+2 的右边界二阶正性。本轮创新点是 (1)–(3) 对更高阶及全阶的量化改进。

## 精确计算与证明边界

R430_VERIFY.py 使用 Python 整数、Fraction 与精确行列式复核，输出 R430_EVIDENCE.json，实际返回：

R430_EXACT_PASS 40 40 2534 1234 1300 25 515591

其中 K=1..5、r∈{16K²,32K²} 的40组原始 signed 卷积以求和与多项式 DP 两路核验、40个系数误差核验；2,534个完整有限窗口子式中1,234个严格正、1,300个结构性零；25组阈值代数界以及 K=2..30 的515,591项二阶相对间隙检查。JSON 证据 SHA256 为 83467abd2d6e477f7a6cecd6da9ca62806c75dbaa82da335c34756b4226a182d。有限计算没有在巨大阈值逐项展开子式；无限定理由 (4)、(8)、LGV 解析推导承担。

文献背景：I. M. Gessel & G. Viennot, Binomial Determinants, Paths, and Hook Length Formulae, Advances in Mathematics 58(3) (1985), 300–321, DOI: 10.1016/0001-8708(85)90121-5。

权限：GitHub 作者侧研究与保存，原生 DIRECTED_RESEARCH authority_granted=false，原生 control_tasks 查询返回 CONTROL_QUOTA。无 Source CLAIM/Result、独立 Driver Review、正式数学接纳。P000 和 ACTIVE 世界观未修改。

下一问题：以加权不交路径相对灵敏度替换 (8) 中粗糙的 2^{Kk}，争取固定阶 p≥3 的多项式阈值；全阶继续降低 exp(O(K²))，或构造随窗口增长的首个高阶负子式。