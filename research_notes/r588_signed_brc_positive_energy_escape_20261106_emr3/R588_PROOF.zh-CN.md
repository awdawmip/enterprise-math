# R588｜辅助逆谱正型能量的固定窗口逃逸定理

日期：2026-11-06。等级：AUTHOR_SIDE_ANALYTIC_DERIVATION；独立数学 Driver 待审。

## 研究对象与冻结来源

母问题为 R462 signed BRC 联合十二支路的结构保真性；科学输入固定于 R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f。这里仅研究 R576–R587 的 Toeplitz–Hessenberg 辅助标量谱。其联合支路、相位、标签、来源保留为独立的原生数据，不用标量复谱代替。

整数 k≥2，d=2k−1。令 Q_k 的非零复根为 λ_{k,i}，逆根 μ_{k,i}=1/λ_{k,i}，定义 V_k=d^{-1}∑_{i=1}^d(Im μ_{k,i})²。沿 R579 冻结系数 A_0=1，A_j=H_k(j+2)/H_k(2)：
\[
Q_k(\lambda)=\sum_{j=0}^d(-1)^j A_j\lambda^{d-j},\quad
F_k(z)=\sum_{j=0}^d(-1)^j A_j(z/k^2)^j=(z/k^2)^dQ_k(k^2/z).
\]
故 F_k 的零点 z 与 Q_k 的根一一对应：z=k²/λ=k²μ，均计重数。R576 已给出复紧集一致收敛
\[
F_k(z)\to F(z)=\sum_{j=0}^{\infty}(-1)^j\frac{24\,8^j}{(2j+4)!}z^j
=\frac{24}{t^4}(\cos t-1+t^2/2),\qquad t^2=8z,\quad F(0)=1.
\]

## 定理 R588-A：固定零点窗口能量的精确极限

记 Z_k 为 F_k 零点多重集。任意固定 R>0 满足 F 在 |z|=R 上无零点，定义
\[
V_k^{(<R)}=\frac1{dk^4}\sum_{z\in Z_k,\ |z|<R}(\operatorname{Im}z)^2.
\]
则
\[
\boxed{\lim_{k\to\infty}k^5V_k^{(<R)}
=\frac12\sum_{F(\zeta)=0,\ |\zeta|<R}(\operatorname{Im}\zeta)^2.}\tag{R588.1}
\]
右侧按多重零点求和，是有限数。

证明：缩放 z=k²μ 给出对全部 k 的严格代数恒等式
\[
\boxed{k^5V_k=\frac{k}{2k-1}\sum_{z\in Z_k}(\operatorname{Im}z)^2.}\tag{R588.2}
\]
F_k→F 在闭盘一致，且 F 在边界无零点。Rouché 定理及围绕内部有限零点的两两不交小圆盘表明：F_k 的内部零点（计重数）与 F 的内部零点多重集逐个匹配并收敛。按根取虚部平方求和并使用 k/(2k−1)→1/2，得到 (R588.1)。证毕。

依 R577 的精确有理绕数证书，|z|<14 只含最近共轭零点 ζ、共轭ζ，其中 Im ζ≈9.4809517165，故
\[
\lim_{k\to\infty}k^5V_k^{(<14)}=(\operatorname{Im}\zeta)^2\approx89.88844545.\tag{R588.3}
\]
十进制只是历史零点近似的显示值，精确结论为原式。

## 引理 R588-B：F 有无限多个零点且其虚部无界

F 每阶幂级数系数非零，因而不是多项式。令 r=|z|≥1、u=√(8r)，直接对绝对系数求和：
\[
|F(z)|\le24\sum_{j\ge0}\frac{u^{2j}}{(2j+4)!}\le24u^{-4}e^u.
\]
故 F 为整函数且增长阶 ≤1/2<1。Hadamard 因子分解：有限阶小于1的整函数若只有有限零点，则其指数因子为常数，从而自身必为多项式。故 F 有无限多个不同零点。

对 x>0，取 t=√(8x)>0，cos t>1−t²/2；对 x<0，取 t=iy（y>0），cosh y>1+y²/2；且 F(0)=1。故 F 在实轴严格为正，所有零点非实。

进一步，对任一 F 零点 ζ，选 t=a+ib 满足 t²=8ζ，T=|t|。零点方程为 cos t=1−t²/2，使用
\[
|\cos(a+ib)|^2=\cos^2 a+\sinh^2 b
\]
及三角不等式，得到
\[
T^2/2-1\le|\cos t|\le\cosh|b|,\qquad
|\sinh b|\le|\cos t|\le 1+T^2/2.
\]
T→∞ 时，第一式推出 |b|≥2log T−log4，第二式推出 |b|=O(log T)，所以 |a|=√(T²−b²)≥T/2（T 足够大）。故
\[
|\operatorname{Im}\zeta|=|ab|/4
\ge T(2\log T-\log4)/8\to+\infty.
\]
整函数的无限零点集在每个紧盘内只有有限个点，因此存在任意大的零点模长 T，且对应虚部无界。证毕。

Hadamard 因子分解外部来源：Wolfram MathWorld, Hadamard Factorization Theorem, https://mathworld.wolfram.com/HadamardFactorizationTheorem.html；Conway, Functions of One Complex Variable I, XI §3。这里是辅助整函数的解析定理而非原生心跳演化计算。

## 定理 R588-C：全谱正型能量的严格逃逸

\[
\boxed{\lim_{k\to\infty}k^5V_k=+\infty.}\tag{R588.4}
\]
而对每个 F 在 |z|=R 无零点的固定 R，均有
\[
\boxed{\lim_{k\to\infty}V_k^{(<R)}/V_k=0.}\tag{R588.5}
\]

证明：任意 M>0，由引理选一个 F 的零点 ζ 使 (Im ζ)²>4M。紧集一致收敛和 Rouché/Hurwitz 定理保证全部足够大的 k 有一个 F_k 零点 z_k→ζ。由 (R588.2) 各项非负，
\[
\liminf_{k\to\infty}k^5V_k\ge\frac12(\operatorname{Im}\zeta)^2>2M.
\]
M 任意，故全序列 k^5V_k→+∞。固定 R 下 (R588.1) 使分子 k^5V_k^{(<R)} 收敛到有限值，再除以发散的 k^5V_k，得到 (R588.5)。证毕。

结构结论：在缩放坐标 z=k²μ 下，任何固定整函数零点窗口只能保留虚部平方正型能量中渐近消失的份额。主份额来自越过所有固定窗口的谱尾，给出一种新的谱观测信息损失/尾部保真研究单元。这一 k^{-5} 的严格下尺度与 R586 的 V_k=O(k^{-1/2}) 候选兼容。

## 复核及接续

R588_VERIFY.py 已执行：k=2..48 精确检查2350个 Fraction 倒数系数；k=2..24 再独立检查69个有理多项式值；k=2..7 对辅助复谱能量关系进行数值一致性检查。全部通过，终止标记 R588_SPECTRAL_LEAKAGE_FINITE_CROSSCHECK_PASS，原始 stdout 在 R588_EVIDENCE.txt。有限计算只交叉检查系数定义及转换；全阶结果承重于本证明和 R576 的作者侧紧集一致定理，独立 Driver 尚未审阅。

下一研究问题：用随 k 增长的窗口 R(k) 及谱尾二阶能量证书对 V_k 建立有效上界，验证或证伪 V_k=O(k^{-1/2})；原生 signed BRC 联合支路保真桥接仍待单独建立。
