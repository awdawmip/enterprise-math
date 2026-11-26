# 准确规范反模型的整函数实现与Gamma函数方程补全

2026-11-26（Asia/Hong_Kong）。共同作者 **EM-DIRECT-E7559A / TASK_RESEARCH**；Activity **RA-D2F111EA1C0D4B1DBEFBC1B4**。本稿为同一作者研究及交叉核对，**不是独立 Review 或 formal Result**。不远端写入，不重跑旧点表、旧窗口或旧证书。

直接前驱为本轮同级目录中的：

- `canonical_sampling/EXACT_CANONICAL_ALIAS_COUNTERMODEL.md`：准确规范别名包、完整正能量指数；
- `canonical_sampling/SPACED_CANONICAL_SPECTRUM_AND_PRECISE_COUNT.md`：高度避让、有效删除规则和精细计数；
- 第2轮 `anchors/ONE_SIDED_ENERGY_MELLIN_AND_MACRO_BIAS.md` §5：完整参考展开及准确常数 \(C_*=2+\gamma-\log(4\pi)>0\)。

本稿只追加一个独立的解析实现，不修改这些前驱文件。P000、Heartbeat X6、真实算术道路、全部整数和合数来源、完整前史及真实端点均保持原义。

## 1. 结论：可以补全到哪些解析结构

可以有效选择前驱中的质量缩放、基准临界高度和一个额外临界共轭对，使最终抽象谱 \(\mathscr R\) 同时满足：

\[
0<\Re\rho<1,\quad \Im\rho\ne0,
\quad m_{\bar\rho}=m_{1-\rho}=m_\rho\in\mathbb Z_{>0},
\]

\[
N_+(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+\frac78+O(1),
\quad
\sum_\rho m_\rho|\rho(1-\rho)|^{-1}<\infty,
\]

\[
\boxed{\sum_\rho\frac{m_\rho}{\rho(1-\rho)}=C_* .}
\tag{1.1}
\]

它是一个实型、关于 \(s\mapsto1-s\) 对称的**恰为1阶的整函数** \(\Xi\) 的准确零点多重集，且

\[
\Xi(\bar s)=\overline{\Xi(s)},\qquad
\Xi(1-s)=\Xi(s),\qquad
\Xi(0)=\Xi(1)=\tfrac12.
\tag{1.2}
\]

定义

\[
\boxed{
Z(s)=\frac{2\Xi(s)\pi^{s/2}}
{s(s-1)\Gamma(s/2)}.
}
\tag{1.3}
\]

则Z在复平面亚纯，唯一极点为s=1的简单极点；其留数为1，Laurent常数为Euler常数γ。它具有与ζ相同的Gamma函数方程、负偶整数简单平凡零点，以及

\[
\boxed{
Z(s)=\frac1{s-1}+\gamma+O(s-1),
\quad Z(0)=-\tfrac12,
\quad Z'(0)=-\tfrac12\log(2\pi).
}
\tag{1.4}
\]

这个谱的最右实部仍为未取得的
\(\Theta_0=\log_2(7/4)>1/2\)。其完整闭整数正能量仍有指数 \(2\Theta_0-1\)，而dyadic两端点插值的正能量一致有界。

**范围。** 这是一个辅助解析函数与谱采样反模型。本稿没有为Z构造Dirichlet级数系数、整数支撑的原算术源或Euler乘积，也没有把Z认作实际ζ。下文所有新增结论都由乘积及归一化直接证明，不是实际ζ零点结论。

## 2. 同时把未补准的总规范权做小

用γ专指Euler常数，谱高度另记v。先取一个有效的正有理数

\[
0<\ell<C_*.
\]

这可复用前驱的严格正界；本稿不重新计算C_*的数值。另有粗界 \(C_*<1<8\)：由 \(\gamma<1\) 和 \(\log(4\pi)>2\) 即得。

### 2.1 临界线基准尾的明确可计算界

记

\[
F(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+\frac78,
\qquad \tau_k=F^{-1}(k)
\]

并只在 \(T>2\pi\) 的严格递增支上反演。若 \(T=\tau_K>2\pi\)，单调积分比较给

\[
\begin{aligned}
2\sum_{k\ge K}\frac1{1/4+\tau_k^2}
&\le 2\sum_{k\ge K}\frac1{\tau_k^2}\\
&\le\frac2{T^2}
+2\int_K^\infty\frac{dv}{\{F^{-1}(v)\}^2}\\
&=\frac2{T^2}
+\frac{\log(T/(2\pi))+1}{\pi T}
=:\mathcal B(T).
\end{aligned}
\tag{2.1}
\]

\(\mathcal B(T)\to0\)，并在 \(T>2\pi\) 单调下降。故可以有效提高基准起始索引k_0，使

\[
\mathcal B(\tau_{k_0})<\ell/4.
\tag{2.2}
\]

选择时只需认证严格不等式；不需判断F(T)是否恰好等于整数。前驱从基准谱删除临界点，只会减小这个非负权和。此处不再补回前驱提及的有限起始计数偏移；任意固定起始偏移本来就在 \(F(T)+O(1)\) 的范围内。

### 2.2 离临界线规范谱的准确总权

前驱正原子测度μ具有可计算总质量M和有效上界 \(\bar M\)。准确规范化不是仅保持正整数采样矩：每个原子包的全部规范系数和也准确等于该原子的目标质量。因此离临界线部分的总规范权为

\[
\boxed{
S_{\rm off}:=\sum_{\rho\ {\mathrm{off}}}\frac{m_\rho}{\rho(1-\rho)}=tM>0,
\qquad
\sum_{\rho\ {\mathrm{off}}}\frac{m_\rho}{|\rho(1-\rho)|}\le2tM.
}
\tag{2.3}
\]

它虽逐项为复数，总和是明确的正实数。先选k_0，再扩大前驱高度阈值G_*，使其超过 \(\tau_{k_0}+2\)、满足全部避让与密度条件。最后选有理t>0同时满足

\[
t\bar M<\ell/4,
\qquad
t\bar M\le\min\{1/2,K^2/G_*^2\}.
\tag{2.4}
\]

这与前驱的所有要求相容。缩小t把所有新别名包的初始允许高度进一步提高，不破坏精细计数构造。

令S_crit为实际保留临界线基准点的双侧规范权。由(2.1)—(2.4)，尚未补准时

\[
\boxed{
0<S_0=tM+S_{\rm crit}<\ell/2<C_*/2.
}
\tag{2.5}
\]

S_0不仅存在，而且是可计算实数。M有前驱的有效质量尾；每个基准整数索引是否被删除，前驱§5.2已给有限判定程序；保留临界系数和的尾由(2.1)控制。因此可以把S_0认证到任意预定精度。

## 3. 一个临界共轭对准确补齐总权

置

\[
\Delta=C_*-S_0.
\]

由(2.5)，\(C_*/2<\Delta<C_*<8\)。所以

\[
\boxed{
v_c=\sqrt{\frac2\Delta-\frac14}>0
}
\tag{3.1}
\]

是可计算的正实数。添加重数均为1的临界共轭对

\[
\rho_c^\pm=\tfrac12\pm iv_c
\]

后，新增的准确总权为

\[
\frac1{\rho_c^+(1-\rho_c^+)}
+\frac1{\rho_c^-(1-\rho_c^-)}
=\frac2{1/4+v_c^2}=\Delta.
\tag{3.2}
\]

于是(1.1)成立。若它恰好与已有临界点重合，只需合并整数重数，不产生新的证明问题；也可在第2节先要求 \(\tau_{k_0}>2/\sqrt\ell+2\)，使它严格位于全部旧谱高度之前，因为 \(v_c<2/\sqrt{C_*}<2/\sqrt\ell\)。

有限添点只给 \(N_+(T)\) 加一个最终常数，不改变 \(F(T)+O(1)\)。这对临界项的系数可和且场幅度为 \(O(\sqrt y)\)，也不改变前驱完整正能量指数或dyadic采样的有界根支付。

## 4. 中心配对乘积：全部零点准确实现

令 \(z=s-1/2\)。对每个离临界线完整轨道选代表

\[
\rho=\beta+iv,\qquad\beta>1/2,\quad v>0,
\qquad\alpha=\rho-1/2.
\]

其共同重数为m。临界点取正高度v及共同重数m_v。定义

\[
\boxed{
P(z)=
\prod_{\text{off轨道}}
\left(1-\frac{z^2}{\alpha^2}\right)^m
\left(1-\frac{z^2}{\bar\alpha^2}\right)^m
\prod_{v\ {\mathrm{critical}}>0}
\left(1+\frac{z^2}{v^2}\right)^{m_v}.
}
\tag{4.1}
\]

离临界线两因子分别给出四点 \(\rho,1-\rho,\bar\rho,1-\bar\rho\)，每点重数准确为m；一个临界因子给出一对临界共轭点，没有四倍计数。

### 4.1 局部一致收敛与可计算性

精细计数给 \(N_+(T)=O(T\log(2+T))\)，所以

\[
\sum_{v>0}\frac{\text{正高度处的总重数}}{v^2}<\infty.
\tag{4.2}
\]

离临界线因子的 \(|\alpha|\ge v\)。因此(4.1)按 \(z^2\) 配对后局部绝对一致收敛，是整函数；它不需另乘未知的指数因子。避开其已列零点，尾因子的对数绝对收敛，因此没有额外零点。

这个收敛还有有效尾。用前驱的明确计数上界，可计算常数C_0,C_1，使

\[
N_+(T)\le C_0+C_1T\log(2+T).
\]

Stieltjes分部积分给

\[
\sum_{v>T}\frac{\text{正侧重数}}{v^2}
\ll\frac{\log(2+T)+1}{T}+\frac1{T^2},
\tag{4.3}
\]

隐常数可从C_0,C_1明确取得。对 \(|z|\le R\)、\(T>\sqrt2R\)，尾对数绝对值至多 \(2R^2\) 乘(4.3)左侧。前驱有限高度段的有效截止保证可以完成全部可能低于T的谱项；不必判定某个超越高度是否恰好等于T。故P及其导数可在紧集上有效逼近。

### 4.2 实型、对称及归一化

各离临界线轨道的因子为实系数偶多项式，临界因子也如此。因此

\[
P(-z)=P(z),\qquad P(\bar z)=\overline{P(z)}.
\]

对实z，离临界线因子为 \(|1-z^2/\alpha^2|^{2m}>0\)，临界因子也为正；局部绝对收敛使 \(P(z)>0\)。尤其 \(P(1/2)>0\)。定义

\[
\boxed{\Xi(s)=\frac{P(s-1/2)}{2P(1/2)}.}
\tag{4.4}
\]

便得到(1.2)，而且 \(\Xi(s)>0\) 对每个实s成立。

还有一个准确等价、归一化更直接的写法。每个反射对
\(\{\rho,1-\rho\}\) 只取其正虚部代表，则

\[
\boxed{
\Xi(s)=\frac12\prod_{\Im\rho>0}
\left(1-\frac{s(1-s)}{\rho(1-\rho)}\right)^{m_\rho}.
}
\tag{4.5}
\]

这是因为
\((1-z^2/\alpha^2)/(1-1/(4\alpha^2))
=1-s(1-s)/[\rho(1-\rho)]\)。其局部绝对收敛也直接来自规范系数绝对可和。离临界线正虚部代表必须同时保留两个不同实部，不能只取每个四元轨道的一点；临界共轭对则只有一个代表。

## 5. 整函数阶恰为1；不是有限型声明

对 \(|z|\le R\)，逐因子上界为

\[
\log|P(z)|
\le\sum_{v>0}(\text{正侧重数})\log(1+R^2/v^2).
\]

分部积分后右侧等于

\[
\int_0^\infty
\frac{2R^2N_+(t)}{t(t^2+R^2)}\,dt.
\tag{5.1}
\]

谱离高度0有正距离。用 \(N_+(t)=O(t\log(2+t))\)，再令t=Ru，可得

\[
\log M_P(R)=O(R\log(2+R)).
\tag{5.2}
\]

所以阶至多1。另一方面，全部零点的实部偏离中心不超过1/2，半径R内的零点数至少为

\[
2N_+\!\left(\sqrt{R^2-1/4}\right)
\sim\frac R\pi\log R.
\]

由P(0)=1及Jensen公式，半径2R的最大模对数至少为这个数乘log2。因此阶至少1，且

\[
\boxed{\operatorname{ord}\Xi=1.}
\tag{5.3}
\]

该计数还使 \(\log M_\Xi(R)/R\) 无界，所以这里是1阶的无限型；不能将“1阶”改写成“1阶有限型”。

## 6. 总规范权决定端点对数导数

先对一个配对因子作准确代数。若 \(\alpha=\rho-1/2\)，则

\[
\left.\frac d{ds}\log\left(1-\frac{(s-1/2)^2}{\alpha^2}\right)\right|_{s=1}
=\frac1{1/4-\alpha^2}
=\frac1{\rho(1-\rho)}.
\tag{6.1}
\]

这个因子产生 \(\rho\) 和 \(1-\rho\) 两个零点，两点的规范系数相同；故(6.1)是这个二点总规范权的一半。离临界线另一共轭因子和临界因子具有同样关系。

端点附近的导数级数绝对一致收敛，归一化常数不影响对数导数。因此

\[
\boxed{
\frac{\Xi'}\Xi(1)
=\frac12\sum_\rho\frac{m_\rho}{\rho(1-\rho)}
=\frac{C_*}{2},
\qquad
\frac{\Xi'}\Xi(0)=-\frac{C_*}{2}.
}
\tag{6.2}
\]

这里是已构造乘积的导数恒等式；不能只从 \(\Xi(0)=\Xi(1)=1/2\) 两个函数值就推断它。

## 7. Gamma函数方程、极点、平凡零点和两端展开

本节所用经典Gamma事实是：\(1/\Gamma\) 为整函数，在非正整数有简单零点；\(\Gamma(1/2)=\sqrt\pi\)；\(\psi(1/2)=-\gamma-2\log2\)；\(\Gamma(w)=1/w-\gamma+O(w)\)。这些公式已对照NIST DLMF §§5.2、5.4和5.7，完整ζ因子的标准约定见§25.4。外部公式只用于此处的标准归一化；谱与乘积构造来自本稿证明。

### 7.1 同一Gamma函数方程

由(1.3)、\(\Xi(s)=\Xi(1-s)\) 及 \((1-s)(-s)=s(s-1)\)，有亚纯恒等式

\[
\boxed{
\pi^{-s/2}\Gamma(s/2)Z(s)
=\pi^{-(1-s)/2}\Gamma((1-s)/2)Z(1-s).
}
\tag{7.1}
\]

这是与ζ相同的Gamma完成和反射方程。

### 7.2 唯一极点与准确Laurent常数

把 \(Z(s)=H(s)/(s-1)\)，其中

\[
H(s)=\frac{2\Xi(s)\pi^{s/2}}{s\Gamma(s/2)}.
\]

H在s=1邻域全纯，\(H(1)=1\)。由(6.2)，

\[
\begin{aligned}
H'(1)
&=\frac{\Xi'}\Xi(1)+\frac12\log\pi-1-\frac12\psi(1/2)\\
&=\frac{C_*}{2}-1+\frac\gamma2+\frac12\log(4\pi)
=\gamma.
\end{aligned}
\tag{7.2}
\]

因此s=1是留数1的简单极点，Laurent常数准确为γ。Z的唯一其他候选极点为s=0，但它可去；其余Gamma倒数与Ξ均为整函数，所以没有其他极点。

### 7.3 s=0的值与导数

利用

\[
\frac1{\Gamma(s/2)}=\frac s2+\frac\gamma4s^2+O(s^3),
\qquad
\Xi(s)=\frac12\left(1-\frac{C_*}{2}s+O(s^2)\right),
\]

直接相乘给

\[
\begin{aligned}
Z(s)
&=-\frac12\left[1+
\left(-\frac{C_*}{2}+\frac12\log\pi+1+\frac\gamma2\right)s+O(s^2)\right]\\
&=-\frac12-\frac12\log(2\pi)s+O(s^2).
\end{aligned}
\tag{7.3}
\]

这证明(1.4)中s=0的两项，符号与系数均固定。

### 7.4 平凡和非平凡零点准确位置

对n≥1，\(1/\Gamma(s/2)\) 在s=−2n有简单零点；\(\Xi(-2n)>0\)，其余因子非零。因此每个负偶整数是Z的简单零点。除这些点外，Z的全部零点准确等于 \(\mathscr R\)，重数不变；s=0不是零点，s=1是上述极点。Z也保持实型。

## 8. 原采样分离以及参考背景仍保留

把离临界线场记为

\[
f_{\rm off}(y)=\sum_{\rho\ {\mathrm{off}}}\frac{m_\rho y^\rho}{\rho(1-\rho)},
\]

把保留临界线及补准共轭对的场记为g(y)。准确规范化仍给

\[
f_{\rm off}(2^j)=0\quad(j=1,2,\ldots),
\]

而全部临界系数为正实数，其双侧系数和是 \(C_*-tM\)。所以

\[
\boxed{|g(y)|\le(C_*-tM)\sqrt y<C_*\sqrt y.}
\tag{8.1}
\]

设完整零点场为f=f_off+g。在闭dyadic整数窗口 \([X,2X]\)，g的加权根能量至多 \(C_*\sqrt{\sum_{n=X}^{2X}1/n}=O(1)\)。由正部映射的1-Lipschitz性质，添加g不改变f_off已有的正能量上极限指数，因此

\[
\boxed{
\limsup_{X=2^k\to\infty}
\frac{\log(1+\sum_{n=X}^{2X}f(n)_+^2/n^2)}{\log X}
=2\Theta_0-1>0.
}
\tag{8.2}
\]

在dyadic两个真端点，f=f_off+g=g。平方根函数的凹性表明，这两个端点的真实割线J满足

\[
|J(y)|\le C_*\sqrt y,
\quad
\sum_{n=X}^{2X}\frac{J(n)_+^2}{n^2}
\le C_*^2\sum_{n=X}^{2X}\frac1n=O(1).
\tag{8.3}
\]

还可恢复原参考展开的固定背景，定义辅助函数

\[
\widetilde q(y)=\log(2\pi)+f(y)
-\sum_{k\ge1}\frac{y^{-2k}}{2k(2k+1)}.
\tag{8.4}
\]

因 \(f(1)=C_*\) 和 \(\sum_{k\ge1}[2k(2k+1)]^{-1}=1-\log2\)，准确有

\[
\boxed{\widetilde q(1)=1+\gamma.}
\tag{8.5}
\]

新增背景在闭dyadic窗口只付 \(O(X^{-1/2})\) 根能量，故(8.2)仍适用于 \(\widetilde q\)，其dyadic两端点割线正能量仍为O(1)。但(8.4)只是这个辅助Z的规范零点场及固定背景；没有由此证明它等于原定义中带 \(\Lambda(n)\) 或厚度源 \(D_n\) 的完整道路。

### 8.1 辅助观察与Z的完整Mellin接口

这个辅助观察不仅使用Z的同一零点标签；它的完整Mellin变换也准确接到Z的对数导数。记

\[
J_Z(s)=\frac{\Xi'}{\Xi}(s),
\qquad
\mathcal R_Z(s)=
\sum_\rho\frac{m_\rho}{\rho(1-\rho)(s-\rho)}.
\]

由反射对 \(\{\rho,1-\rho\}\) 的两个分式直接相加，并对(4.5)取对数导数，得到

\[
\boxed{
\mathcal R_Z(s)=
\frac{(2s-1)C_*/2-J_Z(s)}{s(s-1)}.
}
\tag{8.6}
\]

两边在避开谱点的紧集上按反射对绝对一致收敛；s=0、1的表面分母由(6.2)消去。没有省略一个未知线性指数因子。

当 \(\Re s>1\)，(8.4)可以逐项作绝对收敛的Mellin积分：

\[
\widehat{\widetilde q}(s)
=\frac{\log(2\pi)}s+\mathcal R_Z(s)
-\sum_{k\ge1}\frac1{2k(2k+1)(s+2k)}.
\tag{8.7}
\]

这里 \(\psi_\Gamma=\Gamma'/\Gamma\)。为直接检查全部背景常数，部分分式恒等式

\[
\frac{s(s-1)}{t(t+1)(t+s)}
=\frac{s-1}{t}-\frac{s}{t+1}+\frac1{t+s}
\]

配合Gamma对数导数级数，给

\[
s(s-1)\sum_{k\ge1}
\frac1{2k(2k+1)(s+2k)}
=s(1-\log2)-\frac\gamma2
-\frac12\psi_\Gamma(s/2)-\frac1s.
\tag{8.8}
\]

由

\[
\frac{Z'}Z
=J_Z+\frac12\log\pi-\frac1s-\frac1{s-1}
-\frac12\psi_\Gamma(s/2)
\]

以及 \(C_*=2+\gamma-\log(4\pi)\)，(8.6)—(8.8)化为

\[
\boxed{
\int_1^\infty\widetilde q(y)y^{-s-1}\,dy
=\frac{1+\gamma}{s-1}-\frac1{(s-1)^2}
-\frac{Z'(s)/Z(s)}{s(s-1)},
\qquad \Re s>1.
}
\tag{8.9}
\]

这与原完整道路的Mellin形式相同，前史与固定背景都在其中。与实际参考道路 \(q^*\) 相减时，亦准确得到

\[
\boxed{
\int_1^\infty(\widetilde q(y)-q^*(y))y^{-s-1}\,dy
=-\frac{Z'(s)/Z(s)-\zeta'(s)/\zeta(s)}{s(s-1)}.
}
\tag{8.10}
\]

但(8.9)本身没有把 \(-Z'/Z\) 变成整数支撑的Dirichlet级数。因此这一完整解析接口仍不能冒充原来的真实算术源。

## 9. 新增意义与证明边界

本补充排除了一个更强的抽象充分条件：准确规范系数、正整数重数、两种谱对称、精细 \(F(T)+O(1)\) 计数、1阶整完成、与ζ相同的Gamma函数方程、唯一极点留数、两端首项归一化以及完整观察的Mellin接口，一起仍能与几何锚点遗漏完整正能量并存。

这个结论没有把原素数亏缺估计转成无条件上界，也没有证明实际ζ的几何锚点结论失败。若要从上述解析结构进一步回到实际ζ，还需要实际Dirichlet级数、Euler乘积或能排除本构造的真实算术约束。本稿没有擅自给辅助Z附加这些性质，也不声称已经证明它不可能有任何其他意义下的Dirichlet表示。

新增步骤均为解析证明，没有新增数值证书。第6、7节的配对导数、Laurent系数及补准共轭对已由另一共同作者独立推算交叉核对；这是作者核对，不是独立Review。

### 已核对的标准公式来源

- NIST DLMF [§25.4，特别(25.4.3)—(25.4.4)](https://dlmf.nist.gov/25.4)：ζ的Gamma完成约定与反射方程。
- NIST DLMF [§5.2](https://dlmf.nist.gov/5.2)：Gamma的极点、无零性及倒数的简单零点。
- NIST DLMF [§5.4，特别(5.4.6)、(5.4.13)](https://dlmf.nist.gov/5.4)：\(\Gamma(1/2)\) 与 \(\psi(1/2)\)。
- NIST DLMF [§5.7，特别(5.7.1)、(5.7.6)](https://dlmf.nist.gov/5.7)：Gamma的原点级数及对数导数的部分分式。

以上来源只支持标准特殊函数事实；本稿的规范谱实现、有效总权补准、完整Mellin接口和保留采样分离由 §§2–8 的证明承担。
