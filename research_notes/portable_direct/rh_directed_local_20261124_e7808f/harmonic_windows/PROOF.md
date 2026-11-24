# 三角亏缺是嵌套调和区间亏缺的精确平均

日期：2026-11-24。EM-DIRECT-E7808F / TASK_RESEARCH；同轮作者推导。
依赖 `directed_arithmetic/LOCAL_PRIME_DEFICIT_TRANSFER.md` 的局部普通素数亏缺定义，使用同一原生 X6 整数轴上的辅助标量观察。

## 1. 超水平区间的精确形状

令整数 L<x<R，a=x−L、b=R−x，φ 为峰高1的帽函数；w(n)=φ(n)/n。左段 w(n)=(1−L/n)/a 单调增加，右段 w(n)=(R/n−1)/b 单调减少，峰值为1/x。对0<z<1，定义

\[
u_p(z)=\frac{L}{1-az/x},\qquad
v_p(z)=\frac{R}{1+bz/x}.
\]

分母严格为正，u≤x≤v。直接解两个不等式得到

\[
\boxed{w(n)>z/x\iff u_p(z)<n<v_p(z).}\tag{1}
\]

两端从(L,R)同时向x收缩，在倒数坐标中边界是仿射变化，因此称为调和收缩区间。它保留真实偏斜参数a、b，不用1/n≈1/x。

## 2. 完整整数背景下的单侧亏缺

记 θ(v;u)=Σ_{u<p<v}log p（p为普通素数），并定义

\[
\Delta_p(z)=\#\{n\in\mathbb Z:u_p(z)<n<v_p(z)\}-\theta(v_p(z);u_p(z)).
\]

所有区间都位于原包内，整数计数包括合数。由有限求和与层蛋糕恒等式，

\[
\begin{aligned}
\tau_p&=\sum_n w(n)\bigl(1-\mathbf1_{n\ {\rm prime}}\log n\bigr)\\
&=\frac1x\int_0^1\Delta_p(z)\,dz.
\end{aligned}\tag{2}
\]

积分在这里只是一个有限阶梯函数的精确有理线性组合记法：变化点是有理数 z_n=xφ(n)/n。边界采用严格不等号；有限多个阈值处的值不改变积分。没有连续算术假设或缺失整数。

更一般地，(2) 对任意给定有符号序列g_n成立：把Δ改为上述区间内Σg_n，右侧即Σw(n)g_n。

## 3. 定向层预算的准确目标与可用充分条件

对同一层包，原普通素数归约目标准确等于

\[
\boxed{\mathcal N_X(\tau)^2
=\frac1{X^2}\sum_p\frac{h_p^3}{x_p^2}
\left(\int_0^1\Delta_p(z)dz\right)_+^2.}\tag{3}
\]

正化发生在同一包的完整平均之后，保留不同收缩程度之间的抵消。由正部凸性和Cauchy–Schwarz，

\[
\mathcal N_X(\tau)^2
\le\frac1{X^2}\int_0^1\sum_p\frac{h_p^3}{x_p^2}
(\Delta_p(z))_+^2\,dz.\tag{4}
\]

式(4)是更强的充分条件；式(3)才是精确等价目标。它不需要控制窗口上全部可能区间，只涉及实际包所决定的这些嵌套区间。

如果有逐包非负界 d_p 使所有z满足Δ_p(z)≤d_p，则

\[
\mathcal N_X(\tau)\le\frac1X\left(\sum_p h_p^3d_p^2/x_p^2\right)^{1/2}.
\]

这些是待用的可验证输入形式。本稿没有给出无界真实素数亏缺的所需统一上界。

## 4. 与既有文献的关系

Coppola–Laporta 的 weighted Selberg integral 研究长区间上短区间加权和的平方平均，其中 modified Selberg integral 使用Cesàro三角权：*Symmetry and short interval mean-squares*, arXiv:1312.5701v3 (2016), https://arxiv.org/abs/1312.5701 。Coppola 的作者讲义给出该权的公式：https://giovannicoppola.name/files/articoli/9_ja28copp.pdf ，第2页。

这里的标量核保留实际1/n、非对称包、亏缺方向和固定层位置。文献中的全中心或无符号平方估计不能仅凭“三角权”名称直接替换(3)。本文公式由有限求和独立证明，未把上述文献作为新的无界算术估计。

## 5. 复算

`verify_harmonic_windows.py` 对680个整数包及确定的有理有符号源，逐阈值精确核对超水平集合、积分恒等式及定向Jensen界，共7380个阈值段。解析证明覆盖任意合法整数包和任意有限有符号源；有限核验只检查实现及端点处理。
