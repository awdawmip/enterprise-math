# R589｜signed BRC 辅助极限整函数的单零点定理、远零点几何及局部稳定性

日期：2026-11-07（Asia/Shanghai）；地位：AUTHOR_SIDE_ANALYTIC_PROOF，INDEPENDENT_REVIEW_PENDING。

## 科学对象与来源

冻结科学输入：R462，awdawmip/enterprise-math@18783e01e3646c72b7aab3b16d3f565e83e6446f。接续 R576–R588 辅助 Toeplitz–Hessenberg 标量特征谱。本证明仅涉及复辅助观察变量，并不对原生 X6 联合十二支路实施演化或残差计算。支路、符号、相位、multiplicity 和来源保留于其原始载体。

R576/R588 的已知作者侧前沿为 F_k 在每个复紧集上收敛于

\[
F(z)=\sum_{j=0}^{\infty}(-1)^j\frac{24\,8^j}{(2j+4)!}z^j
=\frac{24}{t^4}\bigl(\cos t-1+t^2/2\bigr),\quad t^2=8z,\quad F(0)=1.
\]

R588 已证明 F 有无穷多个非实零点。上述 F 是本轮准确的辅助对象，而非心跳世界原生 BRC 演化算子。

## 定理 A：所有零点简单

对所有复数 ζ，若 F(ζ)=0，则 F'(ζ)≠0。

证明：取 t²=8ζ 并记 f(t)=cos(t)−1+t²/2。由于 F(0)=1，零点处 t≠0 且 f(t)=0。链式法则给出

\[
F'(\zeta)=96(t-\sin t)/t^5. \tag{A}
\]

如果导数也为零，那么 sin(t)=t，cos(t)=1−t²/2。复变量恒等式 sin²(t)+cos²(t)=1 于是要求
t²+(1−t²/2)²−1=t⁴/4=0，矛盾于 t≠0。故每个零点均为单零点。式 (A) 在 t 换为 −t 时保持不变。

## 定理 B：所有远零点的同一渐近轨迹

令 ζ 遍历 F 的全部零点，r=|ζ|→∞，则一致成立

\[
\operatorname{Re}\zeta
=r-\tfrac14\log^2(8r)+O(\log r/r), \tag{B1}
\]
\[
|\operatorname{Im}\zeta|
=\frac{\sqrt{8r}}4\log(8r)
+O((\log r)^3/\sqrt r). \tag{B2}
\]

因此

\[
\lim_{F(\zeta)=0,\ |\zeta|\to\infty}
\frac{|\operatorname{Im}\zeta|}{\sqrt{|\zeta|}\log|\zeta|}
=\frac1{\sqrt2},\quad \arg\zeta\to0
\]

（辐角用主值）。这说明零点的虚部无界，但零点方向靠近正实轴。

证明：写 t=a+ib，T=|t|，B=|b|，r=T²/8。由 cos(t)=1−t²/2，

\[
|\cos t|=|1-t^2/2|=T^2/2+O(1).
\]

利用复三角函数恒等式
|\cos(a+ib)|²=cos²(a)+sinh²(B) 及 0≤cos²(a)≤1，得到

\[
\sinh B=T^2/2+O(1),\qquad
B=\operatorname{arsinh}(T^2/2+O(1))
=2\log T+O(T^{-2}). \tag{B3}
\]

因 a²=T²−B²，故 |a|=T[1+O((log T)²/T²)]。
又 ζ=t²/8，满足 Re ζ=(a²−B²)/8=r−B²/4，|Im ζ|=|a|B/4。
将 B3 与 T²=8r 代入即得 B1、B2。两式同时给出 Re ζ/r→1、Im ζ/r→0 以及充分远零点的 Re ζ>0。证毕。

## 定理 C：远零点导数及固定窗口根稳定

所有远零点满足

\[
|F'(\zeta)|=\frac{48}{(8r)^{3/2}}(1+O(r^{-1/2})),
\qquad
\lim r^{3/2}|F'(\zeta)|=3/\sqrt2. \tag{C1}
\]

证明：|sin(a+ib)|²=sin²(a)+sinh²(b)，配合 B3 得
|sin(t)|=T²/2+O(1)。由三角不等式 |t−sin(t)|=T²/2+O(T)；代入 (A) 即
|F'(ζ)|=48/T³(1+O(1/T))，再以 T²=8r 化简。

另取任意固定零点 ζ。由定理 A，可选 δ>0，使闭盘 Dbar(ζ,δ) 中仅有 ζ 且为单零点。定义
h(z)=F(z)/(z−ζ)，并在 z=ζ 处设 h(ζ)=F'(ζ)。它在该闭盘内不为零，记
m_δ=min_{|z−ζ|≤δ}|h(z)|>0。
若 ε_k=sup_{|z−ζ|≤δ}|F_k(z)−F(z)|<δ m_δ，则 Rouché 定理在边界上保证 F_k 在盘内恰有一个（按重数）零点 ζ_k。由 F_k(ζ_k)=0：

\[
|\zeta_k-\zeta|\,|h(\zeta_k)|=|F(\zeta_k)|\le \varepsilon_k
\quad\Longrightarrow\quad
|\zeta_k-\zeta|\le\varepsilon_k/m_\delta. \tag{C2}
\]

此结论把 R588 的固定窗口多重集收敛精化为逐个简单零点的线性误差控制。C1 显示远零点的导数规模为 r^{-3/2}；移动窗口 R(k) 的零点验证需要同时估计 F_k−F、零点间距和 m_δ，不能直接将固定窗口常数视为统一常数。

## 精确核验与证明范围

R589_VERIFY.py 实际使用 SymPy 精确 Groebner 消元，对关系
C=1−u²/2、S=u、S²+C²=1、u·inv=1 的理想得到单位元 1，从而代数验证定理 A 的矛盾环节；还核对 (A) 的 t→−t 不变性及 B2/C1 的渐近系数。原始 stdout 见 R589_EVIDENCE.txt。渐近误差及 C2 的复分析论证由上述手工证明建立，不依赖有限计算或复根浮点拟合；本轮未获得独立数学 Driver 审阅。

## 下一科研问题

读取 R576 原始系数界，建立 k 与增长盘 R(k) 联合控制的 sup_{|z|≤R(k)}|F_k−F|；结合 C1/C2 与增长区域的零点分离，推进移动窗口零点计数和 V_k 的正型谱尾定量界，判定 R586 的 V_k=O(k^{-1/2}) 候选。P000/原生联合十二支路的保真桥接继续独立保留。

来源：R588_PROOF.zh-CN.md@0395d0169a57594054a40a893ca0345ee8fd2f2f；
冻结 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；
R576 紧集一致极限经 R588 已载明。