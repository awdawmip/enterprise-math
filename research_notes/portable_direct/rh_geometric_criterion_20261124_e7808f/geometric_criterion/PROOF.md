# 固定 9:12:16 三角族的单侧 RH 判据

日期：2026-11-24。研究身份：`EM-DIRECT-E7808F / TASK_RESEARCH`；Activity：`RA-0B92AAF774CA466C1C1BC38B`。本文件为同轮共同作者推导与有限复核，不是独立 Review，也不是 RH 的证明。沿用科学基础 `9fc068244e4f1117f1e75df5eb0285c6697d21d7` 和前轮已保存研究源 `42e7aa4dbd01a6eb66e2f881c7cddcba72a3d775`。

研究仍限于指定 Heartbeat X6 原生轴上的辅助标量观察。完整整数、厚度、单位、背景和前史保持原义。本文使用经典复分析研究这个观察量，不改变 P000 或原生对象的定义。

## 1. 固定对象、主结论和量词

使用同一个、与窗口无关的参考道路

\[
Q(x):=q^*(x)=x(1+\gamma-\log x)
 +\sum_{k\le x}(x/k-1)\Lambda(k),\qquad x\ge1.
\tag{1}
\]

在整数上，它就是前轮保留完整背景、同一 \(\gamma\) 和完整前缀、仅将 \(D\) 替为 \(\Lambda\) 的辅助道路。实际道路仍满足

\[
D_1=0,\qquad \kappa_n=n\Delta^2(n\log n),\qquad
c=\mu_{\rm Mob}*(D-\kappa),\qquad c(1)=-2\log2.
\tag{2}
\]

不把 (2) 改成 \(\mu_{\rm Mob}*D\)。

对**每个正整数** \(n\)，采用同一个形状的三角包

\[
p_n=(9n,12n,16n),\quad a=3n,\quad b=4n,\quad h=7n,
\]

并定义

\[
t_n=\frac{Q(12n)-Q(9n)}{3n}
       -\frac{Q(16n)-Q(12n)}{4n},
\qquad G(x)=7Q(12x)-4Q(9x)-3Q(16x).
\tag{3}
\]

因此 \(G(n)=12n\,t_n\)。这里的“固定几何族”指所有整数伸缩参数 \(n\)，不是只采样一个稀疏几何子序列。

### 定理 A：单侧有界判据

以下条件等价：

1. 黎曼假设 RH。
2. \(\sup_{n\ge1}\sqrt n\,(t_n)_+<\infty\)。
3. 对每个 \(\epsilon>0\)，存在 \(C_\epsilon<\infty\)，使所有 \(n\ge1\) 都满足 \((t_n)_+\le C_\epsilon n^{-1/2+\epsilon}\)。
4. 单包归一化预算

   \[
   \mathcal B(n):=\frac{(7n)^3}{(9n)^2}(t_n)_+^2
   =\frac{343}{81}n(t_n)_+^2
   =\frac{343}{11664}\frac{G(n)_+^2}{n}
   \tag{4}
   \]

   一致有界。
5. 对每个 \(\epsilon>0\)，\(\mathcal B(n)=O_\epsilon(n^\epsilon)\)。

这些是同一个固定参考道路的单侧判据。它们未断言上述未知上界已经成立。

### 定理 B：判据还精确记录最右零点的上确界

令

\[
\Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

经典零点对称性给 \(1/2\le\Theta\le1\)。将 \(\log0\) 解释为 \(-\infty\)，有

\[
\boxed{\limsup_{n\to\infty}\frac{\log G(n)_+}{\log n}=\Theta,}
\tag{5}
\]

\[
\boxed{\limsup_{n\to\infty}\frac{\log(t_n)_+}{\log n}=\Theta-1,
\qquad
\limsup_{n\to\infty}\frac{\log\mathcal B(n)}{\log n}=2\Theta-1.}
\tag{6}
\]

不假设存在一个实部恰好等于 \(\Theta\) 的零点。不将衰减量的对数改成 \(\log(1+(t_n)_+)\)，否则会丢掉 (6) 中的负指数。

下面先证明这些结论，再将它们付费转到普通素数及实际全整数厚度族。

## 2. 精确的局部算术式与完整背景

令 \(\phi_n(k)\) 为 \(p_n\) 上的帽函数：

\[
\phi_n(k)=
\begin{cases}
(k-9n)/(3n),&9n<k\le12n,\\
(16n-k)/(4n),&12n<k<16n,\\
0,&\text{其余整数 }k.
\end{cases}
\tag{7}
\]

前轮已经证明的完整源三角恒等式，在本几何上给出

\[
\boxed{t_n=\log(4/3)
-\sum_{9n<k<16n}\frac{\phi_n(k)}k\Lambda(k).}
\tag{8}
\]

这里常数 \(\log(4/3)\) 是完整 \(\kappa\) 的精确贡献。直接计算为

\[
\begin{aligned}
\sum_k\frac{\phi_n(k)}k\kappa_k
&=\frac{16n\log(16n)-12n\log(12n)}{4n}
 -\frac{12n\log(12n)-9n\log(9n)}{3n}\\
&=4\log(16n)-7\log(12n)+3\log(9n)
=\log(4/3).
\end{aligned}
\tag{9}
\]

所有 \(k\le9n\) 的源贡献在三个真实点上都仿射，因此被指定三点算子精确消去。\(\gamma\) 项同样被精确消去。这是局部观察的代数性质，不能据此删除完整道路、累计场或真实骨架中的前史、背景和锚点。包端点处 \(\phi_n=0\)，所以端点恰好为素数幂时无需另加半权。

另外

\[
\sum_k\phi_n(k)=\frac{7n}{2},\qquad
\sum_k\frac{\phi_n(k)}k\le\frac7{18}.
\tag{10}
\]

### 为什么整数观察足够

\(Q\) 连续且在每个有限闭区间上绝对连续；每个新源项在加入的时刻 \(x=k\) 恰为零。几乎处处有

\[
Q'(x)=\gamma-\log x+\sum_{k\le x}\Lambda(k)/k.
\]

合成三个导数后，所有 \(k\le9x\) 的前缀再次精确消去，得到

\[
\boxed{G'(x)=12\log(4/3)
+36\sum_{9x<k\le12x}\frac{\Lambda(k)}k
-48\sum_{12x<k\le16x}\frac{\Lambda(k)}k.}
\tag{11}
\]

注意第一个局部和的系数是 **36**。利用 \(0\le\Lambda(k)\le\log k\)，对 \(x\ge1\) 有

\[
|G'(x)|\le12\log(4/3)+(28+8/x)\log(16x)
\le12\log(4/3)+36\log(16x).
\tag{12}
\]

因此 \(n\le x\le n+1\) 时

\[
|G(x)-G(n)|\le12\log(4/3)+36\log(16(n+1)).
\tag{13}
\]

对任意固定 \(\alpha>0\)，整数上的 \(G(n)_+=O(n^\alpha)\) 因而推出整个连续半轴上的 \(G(x)_+=O(x^\alpha)\)。所付误差只有 \(O(\log x)\)，不使用素数定理、RH 或新的局部抵消。

## 3. Mellin 变换：三角算子不遮掉临界带零点

对 \(\Re s>1\)，绝对收敛与逐项积分给

\[
\mathcal Q(s):=\int_1^\infty Q(x)x^{-s-1}\,dx
=\frac{1+\gamma}{s-1}-\frac1{(s-1)^2}
-\frac{\zeta'(s)}{\zeta(s)s(s-1)}.
\tag{14}
\]

其中每个源项的积分为

\[
\int_k^\infty(x/k-1)x^{-s-1}\,dx
=\frac{k^{-s}}{s(s-1)},
\]

再用 Euler 乘积在 \(\Re s>1\) 的绝对收敛对数导数
\(\sum\Lambda(k)k^{-s}=-\zeta'(s)/\zeta(s)\)。粗界 \(Q(x)=O(x(\log x)^2)\) 已足以给出本初始半平面，不需先用任何零点估计。

令

\[
M(s)=7\,12^s-4\,9^s-3\,16^s.
\]

通过变量代换，有

\[
\mathcal G(s):=\int_1^\infty G(x)x^{-s-1}\,dx
=M(s)\mathcal Q(s)-H(s),
\tag{15}
\]

其中完整的有限下端修正是

\[
H(s)=7\,12^s\int_1^{12}Q(u)u^{-s-1}\,du
-4\,9^s\int_1^9Q(u)u^{-s-1}\,du
-3\,16^s\int_1^{16}Q(u)u^{-s-1}\,du.
\tag{16}
\]

\(H\) 是整函数；没有将它丢弃为零。

最关键的精确因式分解是

\[
\boxed{M(s)=-3\,9^s\big((4/3)^s-1\big)
                         \big((4/3)^s-4/3\big).}
\tag{17}
\]

如果 \(M(s)=0\)，则 \(\Re s=0\) 或 \(\Re s=1\)。所以

\[
M(s)\ne0\qquad(0<\Re s<1).
\tag{18}
\]

更定量地，令 \(r=4/3\)，反三角不等式给

\[
|M(\sigma+it)|\ge
3\,9^\sigma(r^\sigma-1)(r-r^\sigma)>0
\qquad(0<\sigma<1,\ t\in\mathbb R).
\tag{18a}
\]

这是对整条竖线的统一不退化，不是有限零点检查。

每个重数为 \(m_\rho\) 的非平凡零点 \(\rho\)，都在 (15) 的亚纯延拓中产生真实的简单极点，留数为

\[
\operatorname {Res}_{s=\rho}\mathcal G(s)
=\frac{m_\rho M(\rho)}{\rho(1-\rho)}\ne0.
\tag{19}
\]

整函数 \(H\) 不能抵消这个极点；同一个零点的重数已经保留在系数中。

另一方面，(15) 在每个正实数处局部全纯。对 \(0<s<1\)，交错级数
\(\eta(s)=\sum_{k\ge1}(-1)^{k-1}k^{-s}>0\)，而
\(\zeta(s)=\eta(s)/(1-2^{1-s})<0\)，所以没有实零点。对 \(s>1\) 用 Euler 乘积。\(s=1\) 处，Laurent 展开

\[
-\zeta'(s)/\zeta(s)=1/(s-1)-\gamma+O(s-1)
\]

使 (14) 中的二重及一重主部完全相消。这个正则性陈述针对完整 \(Q\) 的 Mellin 变换。几何量 \(G\) 本身对 \(Q(x)\mapsto Q(x)+cx\) 不变；\(M(1)=0\) 与有限下端修正也会一起消去该线性平移。因而几何判据本身不能读出 \(\gamma\) 的校准。返回完整道路的单侧能量与真实骨架时，原 \(\gamma\)、背景和锚点仍须保留，不能由此删除。

## 4. 单侧 Landau 步骤与 RH 方向

这里复用并列分支 `../one_sided_mellin/PROOF.md` 的单侧 Mellin 引理。为使逻辑闭合，列出所需形式及证明。

**单侧引理。** 设实函数 \(f\) 局部可积且具有多项式增长，初始 Mellin 变换在某个右半平面定义。假设它亚纯延拓到 \(\Re s>\alpha\)，且在该域的每个实数点附近全纯。如果对每个实 \(\sigma>\alpha\)，

\[
\int_1^\infty f_+(x)x^{-\sigma-1}\,dx<\infty,
\]

则原 Mellin 变换在整个 \(\Re s>\alpha\) 全纯。

**证明。** \(f_+\) 的 Mellin 变换已在该域全纯。若 \(f_-\) 的收敛横坐标 \(\sigma_c>\alpha\)，则利用二者之差及假设的延拓，它的 Mellin 变换可跨实点 \(\sigma_c\) 全纯延拓。非负函数的 Landau 奇点原理排除这一点。该原理可以直接证明：若非负 \(h\) 的 Mellin 变换跨实收敛横坐标全纯，在略右的 \(s_0\) 处取一个 Taylor 圆，其半径跨到收敛横坐标左侧。系数满足

\[
(-1)^jL^{(j)}(s_0)
=\int_1^\infty h(x)(\log x)^j x^{-s_0-1}\,dx\ge0.
\]

在 \(s_0-r<\sigma_c\) 处对 Taylor 级数应用单调收敛，得到
\(\int h(x)x^{-(s_0-r)-1}dx<\infty\)，与横坐标的定义矛盾。这样的 Taylor 圆存在：延拓包含 \(\sigma_c\) 的一个小圆盘，和原右半平面合起来包含以足够近的 \(s_0>\sigma_c\) 为中心、越过 \(\sigma_c\) 的圆盘。故 \(\sigma_c\le\alpha\)，正负两部的 Mellin 变换都在目标半平面全纯。证毕。

将其用于 \(f=G\)：

- 若条件 2 成立，由 (13) 有 \(G(x)_+=O(\sqrt x)\)，所以正部 Mellin 积分对所有 \(\sigma>1/2\) 收敛。
- 若只有条件 3，对给定 \(\sigma>1/2\)，选 \(0<\epsilon<\sigma-1/2\)，仍得到同样的积分收敛。

因此 (15) 在整个 \(\Re s>1/2\) 全纯。(19) 随即排除所有 \(\Re\rho>1/2\) 的非平凡零点；零点关于临界线的对称性再给 RH。

这一步只有正部假设。没有用无符号平方能量替代定向目标，也没有假设负部已经满足同样的界。

## 5. RH 反向与平滑带来的无对数上界

并列分支 `../one_sided_mellin/PROOF.md` 从经典 \(\xi\) 乘积、对数导数和 Mellin 唯一性完整推得

\[
\boxed{Q(x)=\sum_\rho\frac{x^\rho}{\rho(1-\rho)}
+\log(2\pi)-\sum_{j\ge1}\frac{x^{-2j}}{2j(2j+1)},\qquad x\ge1.}
\tag{20}
\]

零点按重数计数。这里

\[
\sum_\rho\frac1{|\rho(1-\rho)|}<\infty,
\qquad
\sum_\rho\frac1{\rho(1-\rho)}
=C_0:=2+\gamma-\log(4\pi).
\tag{21}
\]

所以零点和在每个紧 \(x\) 区间上绝对一致收敛；不需要以截断后未经支付的形式使用它。在 \(x=1\) 处，利用
\(\sum_{j\ge1}1/[2j(2j+1)]=1-\log2\)，(20) 正好给 \(Q(1)=1+\gamma\)，核对了单位端点。

在 RH 下，\(\rho(1-\rho)=1/4+(\Im\rho)^2>0\)。将 (20) 代入 (3)，常数 \(\log(2\pi)\) 因 \(7-4-3=0\) 精确消去，得到

\[
G(x)=\sum_\rho\frac{M(\rho)x^\rho}{\rho(1-\rho)}
+T(x),\qquad
T(x):=-\sum_{j\ge1}\frac{M(-2j)x^{-2j}}{2j(2j+1)}.
\tag{22}
\]

由 (17)，\(M(-2j)<0\)，且 \(-M(-2j)\le4\,9^{-2j}\)。因此

\[
0<T(x)\le\frac2{3(81x^2-1)}\qquad(x\ge1).
\tag{23}
\]

在临界线上

\[
|M(\rho)|\le7\sqrt{12}+4\sqrt9+3\sqrt{16}
=24+14\sqrt3.
\]

结合 (21)—(23) 可取明确的 RH 条件常数

\[
\boxed{|t_n|\le
\left[C_0\left(2+\frac{7\sqrt3}{6}\right)+\frac1{1440}\right]n^{-1/2}.}
\tag{24}
\]

说明：\(T(n)/(12n)\le1/[18n(81n^2-1)]\le1/(1440n^3)\)。所以平滑的三角观察在 RH 下不需要额外的 \(\log n\) 或 \((\log n)^2\)。 (24) 推出条件 2；条件 2⇒3，且 (4) 直接给 2⇔4、3⇔5。至此定理 A 全部成立。

### 更锐的 RH 常数：直接求零点系数的绝对质量

可以保留固定几何带来的相位关系，避免在 (24) 中逐项使用同一个最大乘子界。RH 下令 \(\rho=1/2+i\tau\)、\(r=4/3\)，有

\[
M(\rho)=\sqrt{12}\,e^{i\tau\log12}
\bigl(7-4\sqrt3\cos(\tau\log r)\bigr).
\]

括号始终严格为正，因为 \(7>4\sqrt3\)。于是

\[
\sum_\rho\frac{|M(\rho)|}{\rho(1-\rho)}
=3\sqrt{12}\,A_r,
\quad
A_r:=(r+1)C_0-2\bigl(Q(r)-\log(2\pi)+T_0(r)\bigr),
\tag{24a}
\]

这里 \(T_0(r)=\sum_{j\ge1}r^{-2j}/[2j(2j+1)]\)。等式来自 (20)、共轭配对及绝对收敛：
\(Q(r)-\log(2\pi)+T_0(r)=\sqrt r\sum_\rho\cos(\tau\log r)/[\rho(1-\rho)]\)。

因为 \(1<r<2\)，\(Q(r)=r(1+\gamma-\log r)\)；两个几何级数原函数给出

\[
T_0(r)=1+\log r-\frac12\bigl((r+1)\log(r+1)-(r-1)\log(r-1)\bigr).
\]

在 \(r=4/3\) 处精确整理为

\[
A_{4/3}=\frac{7\log7-4\log2-8\log3-\gamma-\log\pi}{3}.
\tag{24b}
\]

因此比 (24) 更锐的条件性上界为

\[
\boxed{|t_n|\le C_{\rm geo}\,n^{-1/2}+\frac1{1440n^3},\qquad
C_{\rm geo}=\frac{\sqrt3}{6}
\bigl(7\log7-4\log2-8\log3-\gamma-\log\pi\bigr).}
\tag{24c}
\]

这不是从有限零点样本估计出来的常数。其值仅需固定 \(\gamma\) 输入和初等常数的严格区间；脚本用 Machin 恒等式 \(\pi=16\arctan(1/5)-4\arctan(1/239)\) 的交错有理余项认证 \(\pi\)，再用前轮对数区间模块计算。该 Machin 恒等式本身可由正切加法有理运算和角所在区间验证。这里的绝对零点质量解释及 (24c) 都仍以 RH 为条件，常数的有限认证不是对 RH 的认证。

## 6. 最右零点上确界的精确增长指数

由绝对收敛的 (20)，对所有 \(x\ge1\) 有

\[
Q(x)=O(x^\Theta),\qquad G(x)=O(x^\Theta).
\tag{25}
\]

常数来自 \(\sum_\rho1/|\rho(1-\rho)|\) 和固定几何；不依赖存在最右零点。这先给 (5) 的上界。

若 (5) 左侧严格小于 \(\Theta\)，取一个

\[
0<\alpha<\Theta
\]

严格大于该上极限。便有 \(G(n)_+=O(n^\alpha)\)。由 (13) 将其延拓为连续界，再用第 4 节单侧引理，(15) 必在 \(\Re s>\alpha\) 全纯。但 \(\alpha<\Theta\) 的定义保证存在某个非平凡零点 \(\Re\rho>\alpha\)，其非零留数 (19) 导致矛盾。因此 (5) 成立。(3)、(4) 随即给 (6)。这也证明 \(G(n)>0\) 对无穷多个整数成立。

由于 \(\Theta\ge1/2\)，(6) 中的预算指数非负；它为零当且仅当 RH。这里是指数的精确识别；在 RH 方向，一致有界的加强结论另外由平滑公式 (24) 提供。

## 7. 普通素数版本：保留同一个精确背景

定义仅对普通素数求和的亏缺

\[
\delta_n:=\log(4/3)
-\sum_{9n<p<16n\atop p\ {\rm prime}}
\frac{\phi_n(p)}p\log p.
\tag{26}
\]

由于完整背景没有改变，准确地有

\[
\delta_n=t_n+P_n,\qquad
P_n=\sum_{9n<p^j<16n\atop j\ge2}\frac{\phi_n(p^j)}{p^j}\log p\ge0.
\tag{27}
\]

前轮的初等 Chebyshev 支付是

\[
\sum_{p^j\le y,\ j\ge2}\log p<12\sqrt y\quad(y\ge2).
\]

其证明只用 \(\psi(u)\le4(\log2)u\) 及
\(4\log2+24/e<12\)，不含 RH。由此

\[
\boxed{0\le P_n\le\frac{16}{3\sqrt n}.}
\tag{28}
\]

故

\[
(t_n)_+\le(\delta_n)_+\le(t_n)_++16/(3\sqrt n).
\tag{29}
\]

定理 A 中全部条件都可以把 \(t_n\) 换成 \(\delta_n\)。相应的三点放大量 \(G_\delta(n)=12n\delta_n\) 及预算 \(\mathcal B_\delta(n)=(343/81)n(\delta_n)_+^2\) 也保留精确指数

\[
\limsup\frac{\log G_\delta(n)_+}{\log n}=\Theta,
\qquad
\limsup\frac{\log\mathcal B_\delta(n)}{\log n}=2\Theta-1.
\tag{30}
\]

下界由 \(\delta_n\ge t_n\) 得到；上界用 (25)、(28) 和 \(\Theta\ge1/2\)。素数幂项具有确定方向，所以在临界指数处不会取消 \(t_n\) 的正峰。

## 8. 转回真实全整数厚度族：必须明确窗口随 n 改变

现在对每个 \(n\) 分别选取一个整数 \(B_n\ge16n\)。沿用前轮 `../prior/riemann_directed_local_20261124/matching_order/PROOF.md` 的真实有理厚度构造：

\[
\theta=\frac12,\qquad m_n=\lceil(7/10)\log B_n\rceil,
\qquad k_n=m_n+1.
\]

节点是 Chebyshev 根附近的精确有理数；权重根据这些真实有理节点重新精确计算。将相应的**全整数**源记为 \(D^{(n)}\)，完整道路记为 \(q^{(n)}\)，并用同一个 \(p_n\) 定义 \(t_n^D\)。每个成员仍保留 (2) 的背景、单位和卷积约定。源的直接解析余项为

\[
|D^{(n)}_k-\Lambda(k)|\le a_{m_n}(\log k)^{k_n},
\qquad
\eta_y^{(n)}:=a_{m_n}(\log y)^{k_n}.
\tag{31}
\]

前轮有理构造已经证明

\[
\eta_{B_n}^{(n)}\le\frac{40}{7}B_n^{-\beta},
\qquad
\beta=\frac7{10}\log\frac{28}{5e}>rac12.
\tag{32}
\]

局部帽核、(10) 和 \(\eta_y^{(n)}\) 的单调性直接给

\[
\boxed{|t_n^D-t_n|
\le\frac7{18}\eta_{16n}^{(n)}
\le\frac7{18}\eta_{B_n}^{(n)}
\le\frac{20}{9}B_n^{-\beta}.}
\tag{33}
\]

本式适用于任意匹配阶，不附加 \(k_n\ge\log B_n\) 的旧条件。所有合数和非素数幂的实际厚度来源都通过 (31) 支付，未将其直接丢弃。

因为 \(B_n\ge16n\)、\(\beta>1/2\)，(33) 是 \(o(n^{-1/2})\)，且

\[
|12n t_n^D-G(n)|=O(n^{1-\beta}),\qquad 1-\beta<1/2\le\Theta.
\tag{34}
\]

因此定理 A 的全部等价条件仍可将 \(t_n\) 换成 \(t_n^D\)。预算及放大量也仍具有定理 B 的精确指数：上界由 (34) 给出；若实际量的正部指数低于 \(\Theta\)，取一个严格位于两者之间、同时大于 \(1-\beta\) 的指数，(34) 会迫使 \(G(n)_+\) 具有同样过小的指数，矛盾。

本陈述包括两种明确场景：

- 最小前缀 \(B_n=16n\)，误差为 \(O(n^{-\beta})\)。
- 用户母窗口 \(A_n=9n\)、\(B_n=\lceil A_n^\lambda\rceil\)，固定 \(\lambda>1\)。充分大 \(n\) 时 \(B_n\ge16n\)，误差为 \(O(n^{-\lambda\beta})\)。有限个早期项可另取 \(B_n\ge16n\)，不影响判据或指数。

在这里 \(D^{(n)}\) 是明确随窗口变化的一族源。不能把它冒充一个与 \(n\) 无关的固定厚度道路，不能把 Mellin 变换直接施加给它；Mellin 论证始终用于固定的 \(Q\)，最后才通过 (33) 转移。本结论也不自动适用于前轮固定的 11 个厚度输入。

## 9. 与原目标的关系和保留的开放边界

三角累计场恒等式仍给

\[
t_n=\frac{\bar E_{9n,12n}-\bar E_{12n,16n}}{12n},
\quad
V_{p_n}^+=\frac{12n}{7}(t_n)_+^2,
\]

其中参考道路使用完整参考场 \(E_k^*=\sum_{j\le k}(\Lambda(j)-\kappa_j)\)；实际道路分别使用自己的完整 \(E^{(n)}\)。因此 (4) 正是这个确定包在尺度 \(X=9n\) 的原定向预算，而不是另造无符号目标。

\(16n<2(9n)\)，所以每个包都具有原块范围内允许的几何比例。**但“该包在几何上合法”不等于“已有的每棵自适应树都包含它”。** 本文没有证明原实际节点集合、同层集合或深度优化程序必然产生所有 \(p_n\)。若要由某个实际树预算推出本判据，必须另证这些包被覆盖，或给出保留方向和尺度的比较成本。反向也不能仅由一个固定形状族的判据，直接宣称任意树的全部层、骨架和相位成本都已控制。

本研究得到的是可检验条件与 RH 的严格逻辑等价，以及该条件对零点实部上确界的精确敏感性；没有证明条件成立。有限复算不能证明所有 \(n\) 的界。原无界算术目标因此仍未解决。

作为几何说明，任意整数 \(v>u>0\) 的族 \((u^2n,uvn,v^2n)\) 都有

\[
(u+v)(uv)^s-v(u^2)^s-u(v^2)^s
=-u(u^2)^s\big((v/u)^s-1\big)\big((v/u)^s-v/u\big).
\]

本稿选用 \((u,v)=(3,4)\)，以便包全部位于一个 \(Y\le2X\) 的块内，同时保持较小的整数系数。本文只完整记录并复算 9:12:16 的版本。

## 10. 复算范围、依赖与来源

`certify_geometric_criterion.py` 与 `fixed_input.json` 只做明确的有限复核：三点源核的有理恒等式、背景的对数系数恒等式、乘子因式分解、局部导数系数、固定整数参数上的严格 \(\Lambda\) 与普通素数矩区间，以及素数幂支付。数值使用前轮已固定的 80 位向外整数区间和有理余项；不查询零点、不使用 RH 作为程序断言、不读取或生成完整厚度道路缓存。

解析依赖：

1. `../one_sided_mellin/PROOF.md`：自足的单侧 Landau 引理及平滑公式 (20)—(21)。
2. `../prior/riemann_directed_local_20261124/directed_arithmetic/LOCAL_PRIME_DEFICIT_TRANSFER.md`：完整帽核、全阶局部支付、初等高次素数幂成本。
3. `../prior/riemann_directed_local_20261124/matching_order/PROOF.md`：真实有理匹配族、全窗口 \(\eta_B\) 界与 \(\beta>1/2\) 的有理认证。
4. 冻结前轮的完整道路、累计场与方向恒等式。

经典事实的主来源入口：NIST DLMF [§25.2](https://dlmf.nist.gov/25.2)（解析延拓、Laurent 展开及交错表达）、[§25.10](https://dlmf.nist.gov/25.10)（零点带与对称性）、[§27.4](https://dlmf.nist.gov/27.4)（绝对收敛 Euler 乘积）。本稿的局部三角因式分解、端点修正、单侧移植和付费厚度推论均在上文推导，而非从这些页面直接引用成定理。

已对本地前轮依赖与已保存报告做关键词和公式接口比较，未发现本固定 9:12:16 的 Mellin 单侧判据。这个有限的依赖比较不是全面文献优先权调查；本稿不声称它在经典数论文献中首次出现。
