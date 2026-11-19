# 1159 内部首模的最优矩区间：精确渐近常数与一对矩的预算差

设 $a_q$ 为冻结 Dirichlet 问题的最小正特征根，$q\ge2$，$z=a_q/4\in(0,1/2]$。令 $G_n(z),L_n(z)$ 为只知矩 $m_0,\ldots,m_{2n-1}$ 和支撑 $[0,1]$ 时归一化相位 $F(z)$ 的最小、最大可行值。置
$$
 t=\frac{1-\sqrt{1-z}}{1+\sqrt{1-z}},\qquad
 x=\frac{\arccos\sqrt z}{2\pi},\qquad
 C(z)=2\pi^2(1+t)^2
 \frac{\Gamma(1-x)\Gamma(1/2+x)}
      {\Gamma(x)\Gamma(1/2-x)} .
$$
则在**整个** $0<z\le1/2$ 上一致地有
$$
 L_n-G_n\sim C(z)t^{2n},\qquad
 F-G_n\sim L_n-F\sim\tfrac12 C(z)t^{2n}\qquad(n\longrightarrow\infty).
 \tag{1}
$$
此处每个比值的误差对 $z$ 取上确界后仍趋零，允许分辨率 $q$ 随 $n$ 任意增长。在原生首模处 $x=(q-1)/(4q)$，常数只涉及有理点的 Gamma 值与代数因子。对全部有限阶，式 (6) 还给出一个可直接使用的保证：指定绝对精度后，能排除的最少矩对预算与保证充分的预算最多相差一对。第12轮已有最优端点的有限有理表达式、Chebyshev 上界和逐例舍入结果。[冻结任务](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/EMW59A_1159_HIGH_ORDER_PRECISION_RG_20260909.md) · [相位归一与原生特征根](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md) · [第12轮最优有限矩区间](../twelfth/wallis.md)

## 一、实际测度与两侧误差

内部相位系数 $c_j=2/(j^2\binom{2j}j)$，$m_j=4^jc_{j+1}$，且 $F(z)=\ell(4z)/(4z)=\int_0^1(1-zu)^{-1} d\nu(u)$，$\tau^2=q^2a_q F(z)$。由第12轮的乘积模型，$\nu$ 是均匀变量与独立 $\operatorname{Beta}(1,1/2)$ 变量的乘积分布，故其真实密度为
$$
 w(u)=\int_u^1\frac{dv}{2v\sqrt{1-v}}
 =\operatorname{atanh}\sqrt{1-u},\qquad 0<u<1.
$$
$w$ 在左端为对数奇性，在右端渐近于 $\sqrt{1-u}$，且积分为一。原系数也给 $F(z)=(\arcsin\sqrt z)^2/z$（展开后系数相同），经典三角表达用于最后的独立数值核对。原生有限问题的 $a_q=4\sin^2(\pi/(2q))$；二进 $q$ 时验证器还从 $a_2=2,\ a_{2q}=2-\sqrt{4-a_q}$ 作根式夹逼。有限证书的上下端由已知矩构造，无须先输入待估目标 $\tau$。

记 $P_n$、$S_{n-1}$ 分别是 $w$ 和 $w_1(u)=u(1-u)w(u)$ 的首一正交多项式，$Q^*(z)=z^{\deg Q}Q(1/z)$。正交除法或节点插值给
$$
 \begin{aligned}
 F-G_n&=\frac{z^{2n}}{P_n^*(z)^2}\int_0^1
              \frac{P_n(u)^2w(u)}{1-zu}\,du,\\
 L_n-F&=\frac{z^{2n}}{(1-z)S_{n-1}^*(z)^2}\int_0^1
              \frac{S_{n-1}(u)^2w_1(u)}{1-zu}\,du .
 \end{aligned}\tag{2}
$$
例如第一式中，将核减去平方多项式余项，所得为次数 $\le2n-1$ 的插值多项式；在 $P_n$ 的 $n$ 个零点，余项为零。上式另一行用两端点及 $S_{n-1}$ 的零点，得 Gauss–Lobatto 式。两种求积的正权原子测度都实现给定矩，故其差是仅有这些矩与支撑约束时真正的最优宽度。实际全支撑测度位于开区间；额外已知的解析微分方程属于更强的输入。

## 二、强渐近及全窗一致性

为维持归一，写 $u_\theta=(1+\cos\theta)/2$，$d\alpha(\theta)=d\theta/(2\pi)$，$P_t(\theta)=(1-t^2)/(1-2t\cos\theta+t^2)$。下文 $v$ 取 $w$ 或 $w_1$，令 $g_v=\exp\int\log v(u_\theta)d\alpha$，$D_v$ 为圆周权 $W_v=(\pi/2)v(u_\theta)|\sin\theta|$ 的外函数，正规化为 $D_v(0)>0$。两种密度的对数均可积，Szegő 强外部渐近适用。若 $Q_j$ 是 $v$ 的首一正交多项式，$h_j=\int Q_j^2v$，则
$$
 h_j\sim (\pi/2)g_v16^{-j},\qquad
 (4t)^j Q_j((2+t+t^{-1})/4)\longrightarrow D_v(0)/D_v(t).
 \tag{3}
$$
右式在单位圆盘的任一紧子集一致，在 $t=0$ 左侧取多项式延拓值一。常数可用圆周变换直接校准：$W_v d\alpha$ 经 $u_\theta$ 推送即为 $v(u)du$。若 $\Phi_{2j}$ 为圆周首一正交多项式，$\Phi_{2j}^*$ 为圆周反射多项式，则 (3) 左侧恰为 $(\Phi_{2j}(t)+\Phi_{2j}^*(t))/(1+\Phi_{2j}(0))$，由对称化、首项和正交性可验。对应 $h_j=2\|\Phi_{2j}\|^2/[16^j(1+\Phi_{2j}(0))]$。圆周 Szegő 定理给 $\|\Phi_{2j}\|^2\to D_v(0)^2=\pi g_v/4$、$\Phi_{2j}^*\to D_v(0)/D_v$、$\Phi_{2j}\to0$，正合 (3)。[Szegő 类及强渐近定理出处，DLMF §18.2(xi)](https://dlmf.nist.gov/18.2#xi) · [Simon，圆周正交多项式综述](https://doi.org/10.1090/S0273-0979-05-01075-X)

相应概率测度 $Q_j^2 v\,du/h_j$ 弱收敛到 $[0,1]$ 的反正弦测度。为见此，由范数比得首一三项递推的次对角系数 $h_j/h_{j-1}\to1/16$。从 (3) 在 $t=0$ 的一次系数收敛，得相邻阶的对角递推系数趋于 $1/2$（该一次系数是 $2j-4\sum\text{根}$）。对任意固定幂次，Jacobi 矩阵相应对角元只涉及有限个邻项，极限因此是双边常系数算子的矩。其 Fourier 符号为 $(1+\cos\theta)/2$，即所称反正弦测度。核 $(1-zu)^{-1}$ 的积分随之趋于 $(1-z)^{-1/2}$，且在 $0\le z\le1/2$ 一致，因为该核的几何级数可在全窗以同一尾界截断。

在 (3) 取 $t=t(z)$，有 $1/z=(2+t+t^{-1})/4$、$z/(4t)=1/(1+t)^2$。令
$$
 J(t)=\int P_t(\theta)\log w(u_\theta)\,d\alpha(\theta).
$$
由 $|1-e^{2i\theta}|=2|\sin\theta|$ 的 Poisson 延拓，
$[D_w(t)/D_w(0)]^2=(1-t^2)\exp(J(t))/g_w$。代回 (2) 第一式即得
$$
 (F-G_n)/t^{2n}\longrightarrow (\pi/2)(1+t)^2\exp J(t).
$$
对第二式同算，$g_{w_1}/g_w=1/16$，且 $D_{w_1}(t)/D_w(t)=(1-t^2)/4$；故两侧首常数相同。这里 $t$ 的全域包含于紧区间 $[0,3-2\sqrt2]$。消去显式的 $t^{2n}$ 后，(3) 及核积分都是延拓过 $0$ 的紧集一致收敛，极限各处严格为正，由此得到 (1) 的**相对**一致性。在 $z=0$ 实际区间宽度为零，相对公式只对 $z>0$ 解读；归一化后的极限常数延拓到零。

## 三、Poisson 平均化成有理点 Gamma 常数

取 $\theta\in[0,\pi]$，换元 $v=\operatorname{atanh}\sin(\theta/2)$，则 $d\theta=2\operatorname{sech}v\,dv$。置 $\varphi=\arccos\sqrt z=2\pi x$，直接通分给
$$
 P_t(\theta)\operatorname{sech}v
 =\frac{\sin\varphi\,\cosh v}{\cosh^2v-\cos^2\varphi}
 =2\sum_{j\ge0}\sin((2j+1)\varphi)e^{-(2j+1)v}. \tag{4}
$$
最后一步分别展开 $1/(\cosh v\pm\cos\varphi)$ 的几何级数。若 $S(s,x)=\sum_{n\ge1}\sin(2\pi nx)/n^s$，积分 Mellin 变换并求导给
$$
 J(t)=\frac4\pi\left.\frac d{ds}
 \{\Gamma(s)[S(s,x)-2^{-s}S(s,2x)]\}\right|_{s=1}.
$$
在 $\Re s>1$ 可绝对交换级数和积分。左侧 Mellin 核在零附近有界、无穷处指数衰减，解析至 $\Re s>0$；右侧正弦级数的部分和有界，也延拓于同一半平面。因此导数操作无需在临界直线上绝对求和。

Hurwitz 函数方程给
$4\Gamma(s)(2\pi)^{-s}\sin(\pi s/2)S(s,x)=\zeta(1-s,x)-\zeta(1-s,1-x)$。用 $\zeta(0,x)=1/2-x$ 和 Lerch 的 $\zeta'(0,x)=\log\Gamma(x)-\tfrac12\log(2\pi)$ 后，可对 $x$ 和 $2x$ 分别求导，得到
$$
 e^{J(t)}
 =2\pi\, 2^{1-4x}\!
    \left(\frac{\Gamma(1-x)}{\Gamma(x)}\right)^2
    \frac{\Gamma(2x)}{\Gamma(1-2x)}
 =2\pi\frac{\Gamma(1-x)\Gamma(1/2+x)}
             {\Gamma(x)\Gamma(1/2-x)} . \tag{5}
$$
最后一步是倍乘公式。此处 $1/8\le x\le1/4$，没有 Gamma 极点。在深分辨率端 $z\downarrow0$，$C(0)=4\pi^4/\Gamma(1/4)^4$。原生 $q=2$ 对应 $x=1/8$。[Hurwitz 函数方程](https://dlmf.nist.gov/25.11.E9) · [零点导数](https://dlmf.nist.gov/25.11.E18) · [Gamma 倍乘](https://dlmf.nist.gov/5.5.E5)

## 四、任何有限矩数都能使用的上下界

置 $A(z)=\pi(1-t^2)^2/(8\sqrt{1-z})$、$B(z)=4/[(1-t)\sqrt{1-z}]$。对 $n\ge1$，有
$$
 \frac{A(z)t^{2n}}{1-t^{2n+2}}
 \le L_n(z)-G_n(z)\le B(z)t^{2n}.\tag{6}
$$
上端是第12轮已有的 Chebyshev 尾界。左端来自正测度的变分比较。Gaussian 误差等于
$$
 \min_{\deg h\le n,\ h(1/z)=1}\int_0^1 \frac{h(u)^2 w(u)}{1-zu}\,du .
$$
最优多项式为 $P_n(u)/P_n(1/z)$，因为任何可行差都含因子 $u-1/z$，交叉项由正交性消失。$w(u)\ge\sqrt{1-u}\ge\sqrt{u(1-u)}$。换成末项半圆权，最优多项式改为归一化的 $U_n(2u-1)$。在 $u=u_\theta$ 扩展 Poisson 核，使用 $\sin^2((n+1)\theta)=(1-\cos((2n+2)\theta))/2$，半圆权下分子积分为 $\pi(1-t^{2n+2})/(8\sqrt{1-z})$。再用 $U_n(2/z-1)=t^{-n}(1-t^{2n+2})/(1-t^2)$ 便得 (6)。

目标宽度取 $\eta>0$。若用函数 $N(c)=\max(1,\lceil\log(c/\eta)/(2\log(1/t))\rceil)$，则对归一化 $F$ 的最少矩对数 $n_*$ 有 $N(A)\le n_*\le N(B)$。因为 $t\le3-2\sqrt2<1/5$，
$B/A=32/[\pi(1-t)(1-t^2)^2]<16<t^{-2}$，故两整数端点相差至多一；若需精确决策，只须用原生有理区间核此相邻预算。每对消耗两个已知矩，其中含 $m_0=1$。对于 $\tau^2$，两常数同乘 $q^2a_q$。对 $\tau$，用 $1\le G_n\le L_n\le1/(1-z)$，所以上下常数分别乘 $q\sqrt{a_q}\sqrt{1-z}/2$ 和 $q\sqrt{a_q}/2$；其比至多再增 $\sqrt2$，仍小于 $t^{-2}$。给定矩与支撑时这约束真实可保证区间宽度。若利用实际 $F$ 的额外解析知识，(1) 说明真实值与两端之差各渐近为半宽；中点在有限阶的有符号误差不能直接用该等价式充当保证。

## 五、独立核对

程序按 SHA-256 校验第12轮 T5 实现并调用其真实 Gauss/Lobatto 构造与二进根式入口。用闭合的中心二项式核对 $98$ 个矩；在 $t=1/100,1/10,1/6$ 与六个阶上以有理运算验证全部 $18$ 组 (6)，左端甚至用较大的 $22/7$ 替换 $\pi$。另在四个真实分辨率的六个阶上用高精度有限比值核验两侧方向、总宽度与已证的单项式分子式；Poisson 实积分与独立 Gamma 求值比对至 $44$ 位十进小数。下表为 $n=48$ 的数值校准；其渐近误差随阶数的严格速率未在本文求出。

|$q$|$C(z)$|实际宽度除以 $C(z)t^{96}$|真下侧误差占总宽度|
|---:|---:|---:|---:|
|2|2.371439567|1.016093|0.491262|
|4|2.296683261|1.012981|0.492519|
|16|2.257728749|1.012295|0.492770|
|64|2.255115871|1.012256|0.492784|

使用标准库与 mpmath 1.3.0，运行 `python quadrature_check.py --out quadrature_checked.json`。精确有理比较负责有限界核验，高精度小数用于校准渐近等价式。Szegő、Hurwitz 和 Gauss 型求积均为经典工具；此处的求值与预算针对 1159 的实际相位测度及已声明的有限矩信息。[复算程序](quadrature_check.py) · [数值与精确检验结果](quadrature_checked.json)
