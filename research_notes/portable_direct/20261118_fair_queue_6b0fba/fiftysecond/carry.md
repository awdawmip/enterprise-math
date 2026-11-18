# 原计数中心进位能量的二进平均与零点重数

原任务的真实能量记为
\[
 W(N)=\sum_{N\le n<2N}\frac{J(n)^2}{n^2},\qquad
 M_K=\frac1K\sum_{k=0}^{K-1}W(2^k).
\]
**\(M_K\) 在扩展实数中必有极限。** RH 成立时，每块 \(W(2^k)=O(1)\)，平均极限为一个绝对收敛的正谱和。RH 不成立时，\(M_K\to+\infty\)。有限分支有显式下界 \(M_0^*=0.09694746724955\ldots\)，并且
\[
 \lim_{K\to\infty}M_K=M_0^*\quad\Longleftrightarrow\quad
 \text{RH 成立且每个非平凡零点都是单零点。}
 \tag{1}
\]
此处给出等价刻画；无条件证明原任务所求的一致多对数上界仍是开放问题。

冻结交接已记载有界块能量与 RH 等价，以及固定多对数界向 RH 的逆推。Cramér 的经典条件均方估计已足以证明有界这一方向。第七轮处理的是截断大素数窗的缺失中心和纯几何压缩。这里提取原 \(J\) 的平均、实际重复零点的权重和可观测的滞后相关。[任务书](https://github.com/awdawmip/enterprise-math/blob/3f4d3f20031f51803d897914aa9bea28a4fadbf9/research_tasks/RH_BRC_COUNT_CENTERED_CARRY_CLOSURE_20260909.md) · [V11–V17 交接](https://github.com/awdawmip/enterprise-math/blob/3f4d3f20031f51803d897914aa9bea28a4fadbf9/research_notes/RH_BRC_COUNT_CENTERED_CARRY_STATE_MACHINE_HANDOFF_20260909.md#L79) · [第七轮](https://github.com/awdawmip/enterprise-math/blob/3f4d3f20031f51803d897914aa9bea28a4fadbf9/research_notes/portable_direct/20261118_fair_queue_6b0fba/seventh/carry.md)

## 一、从整数进位到连续平方范数

置 \(c_m(n)=\lfloor2n/m\rfloor-2\lfloor n/m\rfloor\)，\(A_n=\sum_{m\le n}c_m(n)\)，\(\alpha_n=A_n/n\)。使用自然对数和原 von Mangoldt 权重，
\[
 J(n)=\sum_{m\le n}(c_m(n)-\alpha_n)\Lambda(m)
     =\log {2n\choose n}-\psi(2n)+(1-\alpha_n)\psi(n).
\]
阶乘恒等式给出第二式；全范围含 \(n<m\le2n\) 的进位恰为一。设 \(D(x)=\sum_{m\le x}\lfloor x/m\rfloor\)，\(L=\log2\)，\(a=2-2L\)。有 \(n\alpha_n=D(2n)-2D(n)-n\)。经典 Dirichlet 除数问题余项可取 \(O(x^{2/5})\)，足以得 \(1-\alpha_n=a+O(n^{-3/5})\)。Stirling 公式、\(\psi(n)\ll n\) 及 \(E(x)=\psi(x)-x\) 给出
\[
 J(\lfloor x\rfloor)=aE(x)-E(2x)+O(x^{2/5}),\qquad x\ge2.
 \tag{2}
\]
在 \(x\in[n,n+1)\) 内，\(\psi(2x)\) 可能经过 \(2n+1\)，其跳跃至多 \(\log(2n+1)\)。降低除数余项指数到 \(1/2\) 以下，使 (2) 的归一化误差趋于零。[Huxley 的更强除数余项](https://doi.org/10.1112/S0024611503014485) · [冻结计数中心实现](https://github.com/awdawmip/enterprise-math/blob/437d4d595f1495d3a0486b3c06e9e2b14567db82/src/enterprise_math/brc_count_centered_carry.py)

令 \(F(t)=e^{-t/2}E(e^t)\)，\(H(t)=aF(t)-\sqrt2 F(t+L)\)。对 \(x=e^t\)、\(n=\lfloor x\rfloor\) 取 \(V_*(t)=J(n)\sqrt{x}/n\)。则对每个 \(N=2^k\)
\[
 \int_{kL}^{(k+1)L}|V_*(t)|^2dt=W(2^k),\qquad
 |V_*(t)-H(t)|\ll e^{-t/10}\quad(t\ge L).
 \tag{3}
\]
第一式由逐个整数格积分精确得到，第二式中额外因子 \(x/n-1=O(1/n)\)，且无条件 \(J(n)=O(n)\)。因此在整半线上两者之差的 \(L^2\) 范数有限。所有零点谱以下都从 (3) 转回原始能量。

## 二、条件显式公式与移动窗的一致性

本节假设 RH。按互异的实纵坐标 \(\gamma\) 取 \(\rho=1/2+i\gamma\)，正负纵坐标都取，令 \(m_\gamma\) 为重数。经典 von Mangoldt 显式公式在每个远离 \(t=0\) 的紧区间内给出
\[
 H(t)=\sum_{\gamma\ \mathrm{distinct}}c_\gamma e^{i\gamma t}
         +O(e^{-t/2}),\qquad
 c_\gamma=\frac{m_\gamma(2^\rho-a)}{\rho}\quad(t\ge L)
 \tag{4}
\]
的局部 \(L^2\) 等式。常数项和负偶数零点产生这里的指数小余项。\(\psi\) 的跳点可取半权，积分不受影响。

为核对 (4) 在长度 \(L\) 的所有移动窗上都能截断，将 \(\gamma\) 按 \([j,j+1)\) 分箱。Riemann–von Mangoldt 的单位箱计数给出 \(b_j=\sum_{\gamma\in[j,j+1)}|c_\gamma|\ll\log(2+|j|)/(1+|j|)\)，其中已计重数。用一个非负高斯放大后平移覆盖任一窗，展开高斯平方积分。第 \(i,j\) 箱的绝对 Gram 权至多 \(C_L e^{-c_L(|i-j|-1)_+^2}\)，每行和有界。故对所有截断尾 \(T<|\gamma|\le U\)，积分平方范数一致为 \(O(\log^2(2T)/T)\)，无须零点间的最小间距。对称截断的经典显式公式在非跳点趋于原函数，因而这个局部 \(L^2\) 极限与 (4) 相同。此论证给出逐块 \(W(2^k)=O(1)\)，也可直接用 Cramér 在 RH 下的 \(\int_X^{2X}E(x)^2dx\ll X^2\) 与 (3) 交叉核对。[Brent–Platt–Trudgian 引言公式 (1)、定理 1 与参考文献 3、7](https://arxiv.org/abs/2008.06140)

原矩形窗定义 \(K_L(u)=\int_0^L e^{iut}dt\)。于是
\[
 W(2^k)=\sum_{\gamma,\lambda}c_\gamma\overline{c_\lambda}
       K_L(\gamma-\lambda)e^{ikL(\gamma-\lambda)}+O(2^{-k/10}) .
 \tag{5}
\]
这一次双和绝对且对 \(k\) 一致收敛。因为 \(|K_L(\gamma-\lambda)|\ll_L(1+|i-j|)^{-1}\)，当 \(|i|=n\ge2\)，将 \(|j|\le n/2\)、\(n/2<|j|\le2n\)、\(|j|>2n\) 分开，得 \(\sum_j b_j/(1+|i-j|)\ll\log^2(2n)/n\)。再乘 \(b_i\) 求和，\(\max(|\gamma|,|\lambda|)>T\) 的绝对贡献是 \(O(\log^3(2T)/T)\)。这还说明原 \(W(2^k)\) 是一个一致几乎周期序列加上趋零误差。它有极限分布，可表为圆周相位 \((e^{ikL\gamma})_\gamma\) 的闭包上的 Haar 测度经 (5) 的连续实值函数推前；闭包依实际零点关系确定。

## 三、平均为什么没有频率混叠

固定 \(\delta=\gamma-\lambda\)。若 \(\delta L\notin2\pi\mathbf Z\)，则 \(e^{ikL\delta}\) 的均值为零。若 \(\delta L\in2\pi\mathbf Z\setminus\{0\}\)，则单块积分 \(K_L(\delta)=0\)。唯一保留的是 \(\delta=0\)，同一零点的 \(m_\gamma\) 个拷贝已相干叠加。于是
\[
 M:=\lim_K M_K
 = L\sum_{\gamma\ \mathrm{distinct}}m_\gamma^2
           \frac{|2^{1/2+i\gamma}-a|^2}{1/4+\gamma^2}>0 .
 \tag{6}
\]
转移因子 \(|2^\rho-a|\ge\sqrt2-a>0\)。因此不需要猜测任何两零点的差是否为 \(2\pi/L\) 的倍数，也不需要零点单重。

对从任意 \(k_0\ge0\) 开始的 \(K\) 个相邻块，均值同样一致趋于 \(M\)。一个可带入有限零点表的误差上界为
\[
 O\left(K^{-1}+\frac{\log^3(2T)}{T}\right)
 +\sum_{\substack{|\gamma|,|\lambda|\le T\\\gamma\ne\lambda}}
 |c_\gamma c_\lambda|\min\left(L,\frac{2}{K|\gamma-\lambda|}\right).
 \tag{7}
\]
因为 \(K\) 个矩形窗积分拼成单个连续区间，只有真实纵坐标差出现在分母。先取足够大但固定的 \(T\)，再令 \(K\to\infty\) 即证。若只取窗起点的场值，这个消除整数倍差频的机制会消失。

## 四、闭式常数与重数剩余

记 \(S(x)=\sum_\rho x^\rho/[\rho(1-\rho)]\)，此处每个零点按重数逐次求和。在 RH 下 \(\rho(1-\rho)=|\rho|^2\)，该和在 \([1,2]\) 一致绝对收敛。完成函数 \(\xi\) 的对数导数配合函数方程给出 \(S(1)=2+\gamma_E-\log(4\pi)\)。在 \(1<x<2\) 对称显式公式以分布意义给出
\[
 S(x)-xS'(x)=\sum_\rho\frac{x^\rho}{\rho}
       =x-\log(2\pi)-\tfrac12\log(1-x^{-2}),
\]
因为该区间 \(\psi(x)=0\)。左端的一阶微分使上式与连续的 \(S\) 相容，且在 \(x\downarrow1\) 仅有可积对数奇性。将 \((S/x)'\) 积分至 2，
\[
 S(2)=2S(1)+\log(4\pi)-1-\tfrac32\log3.
\]
具体地，积分中的 \(\tfrac12\int_{1/2}^1\log(1-u^2)du=(3\log2-1-\tfrac32\log3)/2\)，端点 \(2\) 的素数跳跃不改变积分。展开 (6) 并配对正负零点得到
\[
 \begin{split}
 M_0^*&=L\big((2+a^2)S(1)-2aS(2)\big)
       =0.096947467249549\ldots,\\
 M-M_0^*&=L\sum_{\gamma\ \mathrm{distinct}}m_\gamma(m_\gamma-1)
             \frac{|2^\rho-a|^2}{|\rho|^2}.
 \end{split}
 \tag{8}
\]
每个因子都有确定的正下界或符号，故有限分支中的等号精确检测所有非平凡零点是否单重。

## 五、RH 假时平均发散

Brent–Platt–Trudgian §4 首段援引 Stechkin–Popov 定理 7。若 RH 假，\(I(X)/X^2\to+\infty\)，其中 \(I(X)=\int_X^{2X}E(x)^2dx\)。由 \(x\le2X\) 得 \(\int_{\log X}^{\log(2X)}F(t)^2dt\ge I(X)/(4X^2)\)，故 \(\|F\|_{[0,KL]}/\sqrt K\to\infty\)。缩写 \(\|\cdot\|_K=\|\cdot\|_{L^2[0,KL]}\)。由 \(\|F(\cdot+L)\|_K\ge\|F\|_K-\|F\|_{L^2[0,L]}\)、\(a<\sqrt2\) 以及 (3)，
\[
 \Big(\sum_{k<K}W(2^k)\Big)^{1/2}
 \ge (\sqrt2-a)\|F\|_K-O(1).
\]
这证明 \(M_K\to+\infty\)，从而完成 (1)。结论针对累计平均，单个 \(W(2^k)\) 在此分支的下极限未由这条不等式确定。[Brent–Platt–Trudgian §4](https://arxiv.org/abs/2008.06140) · [Stechkin–Popov 原文](https://doi.org/10.1070/RM1996v051n06ABEH003000)

## 六、从有符号的滞后观测读回零点

RH 下取任意固定实数 \(h\)，令 \(V(n)=J(n)/\sqrt n\)，跳过 \(\lfloor e^hn\rfloor=0\) 的有限起始项。则
\[
 \lim_{K\to\infty}\frac1{KL}\sum_{1\le n<2^K}
 \frac{V(n)V(\lfloor e^h n\rfloor)}n
 = R(h):=\sum_{\gamma\ \mathrm{distinct}}|c_\gamma|^2 e^{i\gamma h}.
 \tag{9}
\]
在单位格内用 (2) 连续化时，固定 \(h\) 的有界位移最多跨 \(O_h(1)\) 个整数，每次 \(\psi\) 的跳跃 \(O_h(\log(2n))\)。\(1/n\) 与 \(\int_n^{n+1}dx/x\) 的差为 \(O(n^{-2})\)，RH 下 \(V(n)\ll\log^2(2n)\)。由一致局部 \(L^2\) 界和 Cauchy–Schwarz，替换误差除以 \(KL\) 后趋零；(4) 的有限截断相乘再取时间均值，只留同一纵坐标。式右绝对收敛。若给出所有实滞后的极限，则在任意频率 \(\omega\) 取 \((2H)^{-1}\int_{-H}^H R(h)e^{-i\omega h}dh\) 的极限，就得到其原子质量。由 \(c_\gamma\ne0\) 和 (4)，能恢复每个纵坐标及其重数。只给 \(h\in L\mathbf Z\) 时，傅里叶变换只恢复频率对 \(2\pi/L\) 取模后的推前质量。有限数值观测的分辨率另需误差估计。

## 七、复算证据

程序在 \(1\le n\le192\) 上，把 \(nJ(n)\) 的原始进位与阶乘恒等式按每个 \(\log p\) 的整数系数逐项比较，共 8080 项。其后用除数筛和素数幂筛计算真实 \(k=0,\ldots,16\) 的能量，\(W(65536)=0.071599269\)，前 17 块均值为 0.081065439。有限初段允许低于渐近标尺。另设有精确整倍谐振的四个频率和 \(1,2,2,1\) 的重数，单取窗起点得平均 34，连续窗能量得 26，与合并重数再平方完全相符。这组人为频率用于检验混叠代数。小数均为数值复核；(1)–(9) 的断言来自相应推导。[复算程序](carry_check.py) · [确定性结果](carry_checked.json)
