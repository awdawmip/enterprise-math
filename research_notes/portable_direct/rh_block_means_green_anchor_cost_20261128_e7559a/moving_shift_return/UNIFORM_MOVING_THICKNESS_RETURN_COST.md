# 随窗口变化的大正厚度校准族：参数一致尾界、幂窗口转移与必需的系数增长

第9轮，统一作者 **EM-DIRECT-E7559A / TASK_RESEARCH**，Activity **RA-D2F111EA1C0D4B1DBEFBC1B4**。直接前驱 Source `28665c59f04df2b7edcbdae5a1e967f587305cde`。本稿是作者研究和严格有限核验，不是 independent Review 或 formal Result。

保持 P000 / Heartbeat X6 固定原生轴上的辅助标量观察；源保留全部整数及合数、`D(1)=0`、真实 `1/n`、完整背景、前史和闭整数端点。这里的厚度族可以随窗口变化，节点数也可以变化。没有把第7轮的固定道路误称为同一条随窗道路。

## 1. 新结论及使用范围

固定

\[
\frac12<\alpha\le1,\qquad \lambda>1,\qquad
\delta=\alpha-\frac12.
\]

对每个窗口起点 A，可以重新选择任意有限个厚度及实权，只要求全部厚度 `a_j≥α`，且三项完整校准准确成立。无需厚度上界，也无需统一限制节点数。自然系数成本为

\[
M_F=\sum_j\frac{|w_j|}{a_j},\qquad W_F=\sum_j|w_j|,
\qquad M_F\le W_F/\alpha.
\tag{1.1}
\]

本稿首先证明参数一致的全道路估计

\[
\boxed{|q_F(y)|\le H_\alpha M_Fy^{1-\alpha}\quad(y\ge1),}
\tag{1.2}
\]

\[
H_\alpha=\frac52+2^\alpha
\left(\frac{1+\log2-\gamma}{\alpha}+\frac1{\alpha^2}\right).
\tag{1.3}
\]

特别地，**全部厚度 `a_j≥1`，包含等于 1 的节点，也已经给出完整道路有界**：

\[
\boxed{|q_F(y)|\le H_1M_F<7M_F,\quad
H_1=\frac{13}{2}+2\log2-2\gamma.}
\tag{1.4}
\]

这改善了第7轮在 `a=1` 使用的 `O(log y)` 初等充分界。改进来自准确的 Möbius 部分和，未使用 RH 或素数定理。

对移动族 `F_A`，在完整幂窗口

\[
[A,B_A],\qquad B_A=\lfloor A^\lambda\rfloor,
\qquad e_A=q_{F_A}-q^*,
\tag{1.5}
\]

若

\[
M_A=o\!\left(A^\delta\sqrt{\log A}\right),
\tag{1.6}
\]

则它的完整返回误差保持第8轮的对数能量成本：RH 下，每个这样的窗口具有准确正、负和绝对对数系数；非 RH 下，每一侧在这些窗口上的归一化上极限均为无穷。无条件有显式正下界。因此固定正间隔 `a_j≥α>1/2` 加上 `W_{B}=B^{o(1)}`，不能实现完整窗口返回误差趋零。

更定量地，如果完整返回根能量甚至只是 `o(sqrt(log A))`，那么必需

\[
\boxed{
\limsup_{A\to\infty}
\frac{M_A}{A^\delta\sqrt{\log A}}
\ge\frac{\sqrt{(2\alpha-1)(\lambda-1)V}}{H_\alpha}>0.}
\tag{1.7}
\]

RH 下可把这里的 limsup 加强为 liminf，并把 `V` 换成准确谱常数 `\mathcal A`；非 RH 下左边为无穷。只要求某一固定方向的返回正能量小，也有同型必需成本，把 `V` 换成第8轮的单侧常数 `P`。

以下结论对全部整数起点成立，也对仅选择 dyadic 起点 `A=2^k` 成立。更一般地，它们对任何相邻起点之比有统一上界的无界整数网格成立。对于任意稀疏、间距不受控的起点子列，本稿没有作同样断言。

## 2. 定义、校准与前驱输入

单厚度源及完整道路沿用

\[
D_a(1)=0,\qquad
D_a(n)=\frac1a\prod_{p\mid n}(1-p^{-a})\quad(n\ge2),
\]

\[
q_a(y)=y(1+\gamma-\log y)
+\sum_{2\le n\le y}(y/n-1)D_a(n).
\tag{2.1}
\]

令

\[
g(a)=1/\zeta(1+a),\quad d(a)=g(a)/a,
\]

\[
C(a)=1+\gamma+(\gamma-1)d(a)+(g'(a)-1)/a.
\tag{2.2}
\]

每个有限族准确满足

\[
\boxed{\sum_jw_j=1,\qquad
\sum_jw_jd(a_j)=1,\qquad
\sum_jw_jC(a_j)=0.}
\tag{2.3}
\]

于是混合完整道路确实是 `q_F=Σ_jw_jq_{a_j}`。第7轮已证明：任意非空正厚度开区间中均存在三个有理厚度和准确实权满足 (2.3)。这里不需要重新选取或数值拟合节点。

本稿用到两项前驱解析输入：

1. 第7轮 `shifted_roads/FIXED_SHIFTED_ROADS_AND_RETURN_COST.md` 的完整 Möbius–谐和表示及其实数 floor 相位估计。
2. 第8轮 `return_energy/LOGARITHMIC_RETURN_ENERGY.md` 的参考道路对数均值、逐侧 RH 判据和严格正常数。

第6轮 `coherent_tail/UNIFORM_CALIBRATED_MOBIUS_TAIL.md` 研究的是厚度趋零的相干校准族。本稿固定厚度与 `1/2` 的正间隔，结论与该小厚度机制适用范围不同。

参考道路始终是

\[
q^*(y)=y(1+\gamma-\log y)
+\sum_{n\le y}(y/n-1)\Lambda(n).
\tag{2.4}
\]

对任意完整道路 v 定义闭整数根能量

\[
\|v\|_{[A,B]}^2=\sum_{n=A}^{B}\frac{v(n)^2}{n^2},
\quad
\|v_\pm\|_{[A,B]}^2=\sum_{n=A}^{B}\frac{v(n)_\pm^2}{n^2}.
\tag{2.5}
\]

## 3. 一个初等 Möbius 部分和消去 `a=1` 的伪对数损失

对任意整数 `N≥1`，卷积恒等式给

\[
\sum_{d\le N}\mu(d)\lfloor N/d\rfloor=1.
\]

所以

\[
N\sum_{d\le N}\frac{\mu(d)}d
=1+\sum_{d\le N}\mu(d)\{N/d\}.
\]

`d=1` 的分数部分为零，其余每项绝对值小于 1。因此

\[
\boxed{\left|\sum_{d\le N}\frac{\mu(d)}d\right|\le1.}
\tag{3.1}
\]

这仅用 `μ*1=ε`；没有用到 Mertens 和的渐近消去。

记 `S_a(y)=Σ_{d≤y}μ(d)d^{-a}`、`N=floor y`。对 (3.1) 作有限 Abel 求和，乘子为 `d^{1-a}`。若 `a≥1`，乘子递减，端值与总变差之和为 1；若 `0<a<1`，该和为 `2N^{1-a}−1`。于是

\[
|S_a(y)|\le
\begin{cases}
2N^{1-a}-1,&0<a<1,\\
1,&a\ge1.
\end{cases}
\tag{3.2}
\]

特别对全部 `a≥α`、`0<α≤1`，统一有

\[
\boxed{|S_a(y)|\le2y^{1-\alpha}-1.}
\tag{3.3}
\]

这是本轮参数一致估计的关键；若先把 `Σμ(d)d^{-a}` 换成 `Σd^{-a}`，会重新引入 `a=1` 附近的额外对数或 `1/|a-1|`。

## 4. 完整道路的参数一致尾：单位项和所有旧源均在式中

令

\[
\mathcal K(z)=zH_{\lfloor z\rfloor}-\lfloor z\rfloor.
\]

把源中的因子乘积展开为 Möbius 除数和，完整单位扣除给准确式

\[
q_a(y)=y(1+\gamma-\log y)
+\frac1a\sum_{d\le y}\mu(d)d^{-a}\mathcal K(y/d)
-\frac{y-1}{a}.
\tag{4.1}
\]

第7轮对全部实 `z≥1` 已证明

\[
\mathcal K(z)=z(\log z+\gamma-1)+\frac12+E(z),
\qquad |E(z)|\le1/z.
\tag{4.2}
\]

该式包括 `z` 的 floor 相位，不只在整数 z 成立。令

\[
R_a(y)=q_a(y)-(d(a)-1)y\log y-C(a)y.
\]

将 (4.2) 代入 (4.1)，再用绝对收敛的
`Σμ(d)d^{-1-a}=g(a)` 和 `−Σμ(d)log d·d^{-1-a}=g'(a)`，得到

\[
\boxed{\begin{aligned}
R_a(y)={}&\frac1a+\frac{S_a(y)}{2a}
+\frac1a\sum_{d\le y}\mu(d)d^{-a}E(y/d)\\
&+\frac ya\sum_{d>y}\frac{\mu(d)}{d^{1+a}}
\left(\log(d/y)+1-\gamma\right).
\end{aligned}}
\tag{4.3}
\]

第一项 `1/a` 是完整单位扣除返回。最后一项含全部 `d>y`，不是把旧源截掉。

### 4.1 单位及半个部分和

由 (3.3) 和 `y^{1-α}≥1`，

\[
\frac1a+\frac{|S_a(y)|}{2a}
\le\frac{y^{1-\alpha}+1/2}{a}
\le\frac{3}{2a}y^{1-\alpha}.
\tag{4.4}
\]

### 4.2 完整谐和核余量

由 `a≥α`、`α≤1` 及 (4.2)，

\[
\frac1a\sum_{d\le y}d^{-a}|E(y/d)|
\le\frac1{ay}\sum_{d\le y}d^{1-a}
\le\frac1a y^{1-\alpha}.
\tag{4.5}
\]

这里对 `a>1` 没有使用会随 a 放大的 `2^a`。

### 4.3 无限尾

设 `N=floor y≥y/2`。对整数 `d>y` 及 `t∈[d−1,d]`，有 `d≤2t`，并且

\[
\frac{\log(d/y)+1-\gamma}{d^{1+a}}
\le\frac{\log(t/y)+\log2+1-\gamma}{t^{1+\alpha}}.
\]

右边非负，因为 `t≥N≥y/2` 和 `γ<1`。逐区间积分得到

\[
\begin{aligned}
\sum_{d>y}\frac{\log(d/y)+1-\gamma}{d^{1+a}}
&\le N^{-\alpha}
\left(\frac{\log(N/y)+\log2+1-\gamma}{\alpha}
+\frac1{\alpha^2}\right)\\
&\le2^\alpha y^{-\alpha}
\left(\frac{1+\log2-\gamma}{\alpha}+\frac1{\alpha^2}\right).
\end{aligned}
\tag{4.6}
\]

合并 (4.3)—(4.6)，对所有 `a≥α`、`y≥1` 得

\[
\boxed{|R_a(y)|\le\frac{H_\alpha}{a}y^{1-\alpha}.}
\tag{4.7}
\]

三项准确校准使 `Σw_jR_{a_j}=q_F`，所以 (1.2) 得证。由于 `γ>1/2`、`log2<3/4`，有 `H_1<7`，故 (1.4) 也得证。对于 `α=3/4` 另有方便的有理充分常数

\[
H_{3/4}<\frac52+2\left(\frac{5/4}{3/4}+\frac1{(3/4)^2}\right)
=\frac{169}{18}.
\tag{4.8}
\]

`a=1` 的有界结论不自动声称 `R_1(y)` 有极限；本稿只需要且只证明显示的统一上界。

## 5. 参数一致的完整闭窗口根界

对整数 `B≥A≥1`，由 (1.2) 及递减积分比较，

\[
\boxed{\begin{aligned}
\|q_F\|_{[A,B]}
&\le H_\alpha M_F
\left(A^{-2\alpha}
+\frac{A^{1-2\alpha}-B^{1-2\alpha}}{2\alpha-1}\right)^{1/2}\\
&\le H_\alpha M_FA^{-\delta}
\left(A^{-1}+\frac1{2\alpha-1}\right)^{1/2}.
\end{aligned}}
\tag{5.1}
\]

第一行仍支付两个闭整数端点；`A=B` 时第二项为零，准确保留单点。第二行控制任意 `B`，甚至整个无界尾。取 `α=1`，得到

\[
\|q_F\|_{[A,B]}<7M_F\sqrt{A^{-2}+A^{-1}}.
\tag{5.2}
\]

所有界均针对真正的完整道路，而不是局部三点算子。若实际厚度下界 `a_0>1`，仍可取 `α=1`；当前三项校准没有消除单位返回的常数项，所以本稿不据 `a_0>1` 再提高 (5.2) 的幂次。

## 6. 从前缀上极限到幂窗口上极限：量词完整的转移引理

### 6.1 引理

设 `b_n≥0`，`S(N)=Σ_{n≤N}b_n`。固定 `λ>1`。令 `𝒢⊂{2,3,…}` 为一个无界整数网格，并假设存在固定 `K≥1`，使每个充分大的实数 x 都存在 `A∈𝒢` 满足

\[
x\le A\le Kx.
\tag{6.1}
\]

全部整数可取 `K=2`，dyadic 起点同样可取 `K=2`。定义

\[
T_\lambda(A)=\sum_{n=A}^{\lfloor A^\lambda\rfloor}b_n.
\]

则包括无穷值在内，

\[
\boxed{
\limsup_{\substack{A\to\infty\\A\in\mathcal G}}
\frac{T_\lambda(A)}{\log A}
\ge(\lambda-1)
\limsup_{N\to\infty}\frac{S(N)}{\log N}.}
\tag{6.2}
\]

### 6.2 证明

若左边为无穷，结论成立。否则记它为 L。任取 `ε>0`，充分大的网格点都有 `Tλ(A)≤(L+ε)log A`。对大整数 N，用 (6.1) 选

\[
N^{1/\lambda}\le A\le KN^{1/\lambda}.
\]

于是 `floor A^λ≥N`，非负性给

\[
S(N)\le S(A-1)+(L+\varepsilon)\log A.
\tag{6.3}
\]

从 `N_0=N` 反复置 `N_{i+1}=A_i−1`，直到低于某个固定阈值；选阈值足够大可保证严格下降。写 `t_i=log N_i`，有

\[
t_{i+1}\le t_i/\lambda+\log K,
\quad \log A_i\le t_i/\lambda+\log K.
\]

设 `c=λ log K/(λ−1)`。递推给

\[
t_i\le c+\lambda^{-i}(\log N-c).
\]

迭代次数 `m=O(log log N)`，并且

\[
\sum_{i<m}\log A_i
\le\frac{\log N}{\lambda-1}+O(\log\log N).
\]

对 (6.3) 迭代，因此

\[
S(N)\le\frac{L+\varepsilon}{\lambda-1}\log N
+O(\log\log N)+O(1).
\]

取前缀 limsup 再令 `ε↓0`，即得 (6.2)。有限 L 会强制右边有限，故也覆盖右边无穷的情形。

### 6.3 不能未经证明改成每个窗口的下界

即使 `limsup S(N)/log N=∞`，也可能有无穷多个幂窗口完全为空。例如固定 `λ>1`，取整数 `c>λ`，在位置 `n_k=2^{c^k}` 放质量 `b_{n_k}=c^{2k}`，其余为零。前缀归一化上极限无穷；但 `A_k=2n_k` 是 dyadic 起点，且充分大时 `A_k^λ<n_{k+1}`，所以 `Tλ(A_k)=0`。这个一般非负序列例子说明了本引理的 limsup 边界；它不是对实际 `q*` 的振荡分布作新的断言。

## 7. 参考道路在幂窗口上的准确转移

复用第8轮常数

\[
C_*=2+\gamma-\log(4\pi),
\]

\[
V=6+2\gamma+4\gamma_1+2\gamma^2-2\log(4\pi)-\pi^2/4>0,
\quad P=V^2/(4C_*^2)>0.
\tag{7.1}
\]

保存的严格数值区间为

\[
0.00007420127287492974302501086782655
\le V\le
0.00007420127287492974302501086782656,
\]

\[
0.00000064511944366753062832059956463
\le P\le
0.00000064511944366753062832059956464.
\tag{7.2}
\]

Stieltjes 约定与第8轮相同：`ζ(1+z)=1/z+γ−γ₁z+O(z²)`。

在 RH 下，令不同非平凡零点 `ρ=1/2+iγ_ρ` 的重数为 `m_ρ`，并记

\[
F(t)=\sum_{\rho\ \mathrm{distinct}}
\frac{m_\rho e^{i\gamma_\rho t}}{\gamma_\rho^2+1/4},
\quad
\mathcal A=\sum_{\rho\ \mathrm{distinct}}
\frac{m_\rho^2}{(\gamma_\rho^2+1/4)^2},
\]

\[
\mathcal A_\pm=M(F_\pm^2),\quad
\mathcal A_++\mathcal A_-=\mathcal A,\quad
\mathcal A\ge V,\quad\mathcal A_\pm\ge P.
\tag{7.3}
\]

第8轮已经证明，全部闭整数前缀有

\[
S(q^*;N)=\mathcal A\log N+o(\log N),
\quad S_\pm(q^*;N)=\mathcal A_\pm\log N+o(\log N).
\]

在 `B_A=floor A^λ` 与 `A−1` 处相减，得到每个幂窗口的准确渐近

\[
\boxed{
\|q^*\|_{[A,B_A]}^2=(\lambda-1)\mathcal A\log A+o(\log A),}
\]

\[
\boxed{
\|q^*_\pm\|_{[A,B_A]}^2=(\lambda-1)\mathcal A_\pm\log A+o(\log A).}
\tag{7.4}
\]

两个余项各自都是 `o(log A)`；闭端点由 `S(B_A)−S(A−1)` 准确处理。

若 RH 不成立，第8轮的逐侧判据给

\[
\limsup_N S_\pm(q^*;N)/\log N=\infty.
\]

把 (6.2) 分别用于 `b_n=q^*(n)_\pm²/n²`，得到任一满足 (6.1) 的网格上

\[
\boxed{
\limsup_{\substack{A\to\infty\\A\in\mathcal G}}
\frac{\|q^*_\pm\|_{[A,B_A]}^2}{\log A}=\infty.}
\tag{7.5}
\]

于是无条件有

\[
\boxed{
\limsup_{A\in\mathcal G}\frac{\|q^*\|_{[A,B_A]}^2}{\log A}
\ge(\lambda-1)V,
\quad
\limsup_{A\in\mathcal G}\frac{\|q^*_\pm\|_{[A,B_A]}^2}{\log A}
\ge(\lambda-1)P.}
\tag{7.6}
\]

这里无条件结论保留 limsup。每个窗口的准确渐近 (7.4) 明确使用 RH。

## 8. 移动校准族的完整返回成本

现在对每个 `A∈𝒢` 允许选择不同族 `F_A`。它们只须满足 (2.3)、`a_{j,A}≥α`。置

\[
r_A=\frac{M_A}{A^\delta\sqrt{\log A}},
\quad
h_A=H_\alpha\left(A^{-1}+\frac1{2\alpha-1}\right)^{1/2}.
\]

由 (5.1)，

\[
\frac{\|q_{F_A}\|_{[A,B_A]}}{\sqrt{\log A}}
\le h_Ar_A,
\qquad h_A\longrightarrow\frac{H_\alpha}{\sqrt{2\alpha-1}}.
\tag{8.1}
\]

本式每次使用的是与同一个窗口相对应的真正道路，不把某一族的全局尾界交换为另一族的固定常数。

### 8.1 小系数族保留准确对数成本

若 `r_A→0`，则 `||q_F_A||=o(sqrt(log A))`。对同一闭窗口，绝对值和正部的 1-Lipschitz 性给

\[
\big|\|e_A\|-\|q^*\|\big|\le\|q_{F_A}\|,
\]

\[
\big|\|(e_A)_+\|-\|q^*_-\|\big|\le\|q_{F_A}\|,
\quad
\big|\|(e_A)_-\|-\|q^*_+\|\big|\le\|q_{F_A}\|.
\tag{8.2}
\]

RH 下结合 (7.4) 得

\[
\boxed{\begin{aligned}
\frac{\|e_A\|^2}{\log A}&\longrightarrow(\lambda-1)\mathcal A,\\
\frac{\|(e_A)_+\|^2}{\log A}&\longrightarrow(\lambda-1)\mathcal A_-,\\
\frac{\|(e_A)_-\|^2}{\log A}&\longrightarrow(\lambda-1)\mathcal A_+.
\end{aligned}}
\tag{8.3}
\]

非 RH 下，这三项归一化量的 limsup 均为无穷。无条件则

\[
\boxed{
\limsup\frac{\|e_A\|^2}{\log A}\ge(\lambda-1)V,
\quad
\limsup\frac{\|(e_A)_\pm\|^2}{\log A}\ge(\lambda-1)P.}
\tag{8.4}
\]

因此仅靠随窗重选大正厚度，而系数满足 (1.6)，不能使完整返回误差趋零。

### 8.2 返回误差小所必需的定量系数成本

反过来，假定

\[
\|e_A\|_{[A,B_A]}=o(\sqrt{\log A}).
\tag{8.5}
\]

由 (8.1)—(8.2)，

\[
\frac{\|q^*\|_{[A,B_A]}}{\sqrt{\log A}}
\le o(1)+h_Ar_A.
\]

再用 (7.6)，即得 (1.7)。如果 RH 成立，左边趋于
`sqrt((λ−1)\mathcal A)`，所以更准确有

\[
\boxed{
\liminf_{A\in\mathcal G}r_A
\ge\frac{\sqrt{(2\alpha-1)(\lambda-1)\mathcal A}}{H_\alpha}.}
\tag{8.6}
\]

如果 RH 不成立，则由 (7.5) 必有 `limsup r_A=∞`。

若只假定一个固定符号的 `||(e_A)_±||=o(sqrt(log A))`，相同论证给无条件必要成本

\[
\boxed{
\limsup r_A\ge
\frac{\sqrt{(2\alpha-1)(\lambda-1)P}}{H_\alpha};}
\tag{8.7}
\]

RH 下对应的 liminf 常数分别用 `\mathcal A_-`、`\mathcal A_+` 代替 P。方向交换来自 `e_A=q_F_A−q*`，没有把两侧准确常数默认相等。

这些是必要条件，不是达到该系数增长就足以构造匹配族的充分条件。

### 8.3 换成总权和 B 尺度

由 `M_A≤W_A/α`，(1.7) 的总权必要成本为

\[
\boxed{
\limsup\frac{W_A}{A^\delta\sqrt{\log A}}
\ge\frac{\alpha\sqrt{(2\alpha-1)(\lambda-1)V}}{H_\alpha}.}
\tag{8.8}
\]

把归一化分母换成 `B_A^{\delta/\lambda}\sqrt{\log B_A}`，右边再除以 `sqrt λ`。特别若 `W_{B_A}=B_A^{o(1)}`，由于 `δ>0` 固定，必有 `r_A→0`，从而适用 (8.3)—(8.4)。

若只知道厚度与 `1/2` 的距离随 A 缩小，本稿没有固定正 δ，不能沿用该子多项式总权排除结论。第6轮的小厚度族也不满足这里的厚度假设。

## 9. 本轮有限核验及边界

`verify_uniform_moving_return.py` 只读取前驱保存的正规常数和区间运算模块；不重跑前驱证书，不新增 ζ 零点求值，不重新筛选旧真实道路。

新增核验包含：

- `μ*1=ε`、`|Σ_{d≤N}μ(d)/d|≤1` 的准确有理检查；
- 整数及分数厚度的 Abel 部分和边界，分数幂用向外整数平方根区间；
- 非整数参数上完整谐和核 (4.2) 的 floor 相位检查；
- 原 `D_a` 的因子乘积、Möbius–谐和完整道路和单位扣除的准确有理恒等检查；
- `H_1<7`、`H_{3/4}<169/18` 及 `λ=2` 时必要系数常数的向外区间；
- 稀疏非负序列的有限见证，核对有正前缀能量而某些完整幂窗口为空的量词边界。

所有无界量词、无限尾和必要增长率由上文解析证明承担。有限核验检查公式、方向、单位项、floor 相位和显示常数，不据此证明 RH，也不充当独立 Review。

复算命令：

```bash
python moving_shift_return/verify_uniform_moving_return.py \
  --previous previous/riemann_directed_dyadic_integer_return_20261128 \
  --output moving_shift_return/uniform_moving_return_certificate.json
```

相对路径以最终第9轮包根目录为准；脚本也接受任意准确的前驱包目录。精确有限检查数及依赖 SHA-256 写入本轮证书。
