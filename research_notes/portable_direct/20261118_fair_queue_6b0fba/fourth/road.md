# 合数道路在移动窗口上的能量

两份 9 月 9 日任务书使用相同的全整数权重、固定起点与中心化常数。第一个任务研究中点能量的逃逸尾，同时依赖 audit 和 kernel。第二个任务依赖本线 baseline audit，另要求原始 Green 能量及误差核算。以下给出一份共用的算术推导、三个不同的数学主张和第二份任务专属的有理区间算例。来源 S5 给出有限 Green 恒等式，S6 给出固定窗的 $O_M(a^2)$，更早的正变形笔记引用了切向场的壳下界。本次推导把切向估计转移到有限厚度且随 $a$ 逃逸的窗口。两条任务各自的调度依赖由原任务书决定。[中点尾任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RH-ROAD-TAIL-20260909.md) · [Green 尾任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RS-RH-COMPOSITE-ROAD-ESCAPING-TAIL_20260909.md) · [S5](https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md) · [S6](https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md) · [早期切向下界](https://github.com/awdawmip/enterprise-math/blob/9d7c4c6eafc5479a6795a128fc0288fc893bed3c/research_notes/COMPOSITE_ROAD_RH_FUTURE_PORT_POSITIVE_DEFORMATION_20260906.md)

取 $0<a<1$，$R_a(n)=\prod_{p\mid n}(1-p^{-a})$，$R_a(1)=1$，$c_a=1/\zeta(1+a)$，$S_a(x)=\sum_{n\le x}R_a(n)$。记 $U_a(x)=S_a(x)-1-c_ax$（$x\ge1$），在 $0<x<1$ 取 $U_a(x)=-c_ax$。原始能量为 $Q_a[L,H]=\int_L^H U_a(x)^2\,dx/x^2$。以 $B_{a,N}=S_a(N)-1-c_a(N+1/2)$ 定义 $D_a[L,H)=\sum_{L\le N<H} B_{a,N}^2/N^2$。

## 一、无条件的可增长前缀

对 $x\ge1$，设 $J(x)=1+\tfrac12\log^2x$。对所有 $a,x$ 同时成立

$$
|U_a(x)-a(\psi(x)-x)|\le a^2xJ(x).
\tag{1}
$$

在素数幂 $p^e$ 上用 $0\le t-(1-e^{-t})\le t^2/2$，$t=a\log p$。其余 $n>1$ 选任意两个不同素因子 $p,q$，全乘积介于 0 与 $a^2\log p\log q\le a^2\log^2(n)/4$ 之间。故每个整数 $n\ge2$ 都满足 $|R_a(n)-a\Lambda(n)|\le a^2\log^2(n)/2$。由积分判别 $1/a\le\zeta(1+a)\le1+1/a$，从而 $0\le a-c_a\le a^2/(1+a)$。求和即得 (1)。特别地，在 $[L,H]$ 上两场按 $dx/x^2$ 的范数差最多为 $a^2\sqrt{H-L}\,J(H)$。

写 $e(1)=e(2)=1$，$e(x)=9.22022(\log x)^{3/2}\exp(-b\sqrt{\log x})$（$x>2$），$b=0.8476836$。Fiori–Kadiri–Swidinsky 推论 1.4 无条件给出 $|\psi(N)-N|/N\le e(N)$。每个正整数 $H$ 均有可逐项核算的界

$$
D_a[1,H+1)\le 3a^2\sum_{N=1}^H
 \left(e(N)^2+\frac1{4N^2}+a^2J(N)^2\right).
\tag{2}
$$

这是 (1) 及 $B_{a,N}=U_a(N)-c_a/2$ 的平方界。令 $t=\log(1/a)$，取 $0\le\lambda<1.6953672$，则

$$
M_\lambda(a)=\left\lfloor a^{-1}\exp(\lambda\sqrt{t})\right\rfloor,
\qquad D_a[1,M_\lambda+1)=o(a),\qquad Q_a[0,M_\lambda]=o(a).
\tag{3}
$$

取 $(\lambda/(2b))^2<\theta<1$。将 (2) 的素数定理误差项在 $M^\theta$ 处分段。小段中 $e$ 有界且 $aM^\theta\to0$。大段除去因子 $a$ 后，上界为 $3(9.22022)^2aM(\log M)^3\exp(-2b\sqrt{\theta\log M})\to0$。非线性项除以 $a$ 后最多 $3a^3MJ(M)^2\to0$。原始能量前缀由单元比较 (4) 和首格 $c_a^2$ 得出。[Fiori–Kadiri–Swidinsky，推论 1.4](https://arxiv.org/abs/2204.02588)

## 二、无条件的逃逸尾下界

对整数 $2\le L<H$，记 $V_{L,H}=\tfrac{c_a^2}{12}\sum_{N=L}^{H-1}N^{-2}$。每一格 $[N,N+1]$ 内 $U_a(N+u)=B_{a,N}+c_a(1/2-u)$，故

$$
\left(\frac L{L+1}\right)^2(D_a[L,H)+V_{L,H})
\le Q_a[L,H]\le D_a[L,H)+V_{L,H}.
\tag{4}
$$

右侧上界对 $L=1$ 也成立。对每个充分大整数 $X$，Brent–Platt–Trudgian 给出 $\int_X^{2X}(\psi(x)-x)^2dx\ge X^2/5374$。其定理 1 同时陈述上下界；无条件下界还须合读 §4 开头，RH 为假时 Stechkin–Popov 给出该二矩除以 $X^2$ 趋向无穷大。这样两个情形都满足下界。引言公式 (3) 的 $L^1$ 界经 Cauchy–Schwarz 另给常数 $1/40000$；具体起始 $X$ 只取文献的「充分大」。结合 (1)、(4)、$V_{X,2X}\le a^2/(12X)$ 得到显式的有限厚度壳界

$$
D_a[X,2X)\ge
a^2\left(\frac1{2\sqrt{5374}}-a\sqrt X\,J(2X)\right)_+^2-\frac{a^2}{12X}.
\tag{5}
$$

固定 $0<\delta<\eta<2$。在 $a^{-\delta}\le X$、$2X\le a^{-\eta}$ 的所有二倍壳，(5) 中两个损失一致趋零（按 $a^2$ 归一化）。互不相交的整二倍壳有 $(\eta-\delta)t/\log2+O(1)$ 个。最后令 $\eta\uparrow2$，所得无条件估计为

$$
\liminf_{a\downarrow0}\frac{D_a[\lceil a^{-\delta}\rceil,\infty)}
 {a^2\log(1/a)}\ge \frac{2-\delta}{4\cdot5374\log2}.
\tag{6}
$$

它排除了在这些截断位置一致给出 $O(a^2)$ 余尾的设想。目标量级 $O(a)$ 仍有余地。[Brent–Platt–Trudgian，摘要、定理 1、§4](https://arxiv.org/abs/2008.06140)

## 三、有限移动环带的判别式

令 $L=\lceil a^{-\delta}\rceil$、$H=\lceil a^{-\eta}\rceil$、$W_a=D_a[L,H)$，其中 $0<\delta<\eta<2$ 固定。按不同非平凡零点定义 $c_1=\sum_\rho m_\rho^2/|\rho|^2$。则

$$
\frac{W_a}{a^2\log(1/a)}\longrightarrow
\begin{cases}
(\eta-\delta)c_1,&\text{RH 成立},\\
+\infty,&\text{RH 不成立}.
\end{cases}
\tag{7}
$$

在 RH 成立的情形，Brent–Platt–Trudgian §5 定理 5 的证明使用 $\int_1^Y(\psi(x)-x)^2\,dx/x^2\sim c_1\log Y$。该文公式 (18) 的求和本身按重数计数，故改用不同零点求和时分子为 $m_\rho^2$。以 $Y=H,L$ 作差，得到切向场在环带上的首项。根据 (1)，环带上的范数误差最多 $a^2\sqrt H\,J(H)=o(a)$。再用 (4)，其中 $V_{L,H}\le a^2/(12(L-1))$，得到第一式。若 RH 不成立，§4 的壳二矩除以 $X^2$ 趋向无穷大，故 (5) 中的 $1/(2\sqrt{5374})$ 可换成任意固定正数，只要 $X$ 充分大。在环带内求和即得第二式。

因而对任意这样一个固定环带，归一能量沿某一 $a\downarrow0$ 子列有界就等价于 RH。这是单独的条件刻画。它也加强了无条件下界 (6)。在 RH 情形由 $\xi$ 的对数导数与函数方程给出的经典求和 $\sum_{\rho\ {\rm distinct}}m_\rho/|\rho|^2=2+\gamma-\log(4\pi)$，可知 $c_1\ge2+\gamma-\log(4\pi)$。在另一情形有限环带的归一能量已趋向无穷大。因此 (6) 右边还可换成 $(2-\delta)(2+\gamma-\log(4\pi))$。这一推导不预设哪一个情形成真。[Brent–Platt–Trudgian，§4、§5.1 与定理 5 证明](https://arxiv.org/abs/2008.06140)

## 四、原始 Green 能量的区间算例

取 $H=128$，在全体 $2\le n\le128$ 上计算 $R_{1/k}(n)$。下表给出 $D_{1/k}[1,128)$ 及 $Q_{1/k}[0,128]$ 的向外舍入。

| $k$ | $c_{1/k}$ | $D_{1/k}[1,128)$ | $Q_{1/k}[0,128]$ |
|---:|---|---|---|
| 4 | [0.2176218376, 0.2176232827] | [0.2024812297, 0.2024879220] | [0.1678160444, 0.1679712191] |
| 8 | [0.1164648114, 0.1164659822] | [0.0591276901, 0.0591306577] | [0.0490081987, 0.0490754432] |
| 16 | [0.0603070101, 0.0603075381] | [0.0160409584, 0.0160416629] | [0.0133022620, 0.0133179602] |

标准库脚本 road_check.py 对 $k=4,8,16$ 用整数开方将每个 $n^{-1/k}$ 夹入 $2^{-80}$ 网格，三个算例中每个全乘积的区间宽度至多 $2\cdot2^{-80}$。对 $\zeta(1+1/k)$ 的前 $T=4096$ 项作有理外包，剩余正项夹在 $k(T+1)^{-1/k}$ 与 $kT^{-1/k}$ 之间，再取倒数。以 $A_n=S_a(n)-1$ 记道路质量；每格原始能量按 $A_n^2/[n(n+1)]-2c_a A_n\log(1+1/n)+c_a^2$ 计算，并与双和 Green 核及连续背景交叉项的独立分组比较。对数用 $2\operatorname{atanh}(1/(2n+1))$ 展开至 47 次，余项至多 $2z^{49}/(49(1-z^2))$。所有带减号运算均按有理端点向外舍入；两种区间交集给出表值。

可分别核算输入误差。若道路质量各自取区间中点，最大半宽为 $\Delta_w$，密度半宽为 $\Delta_c$，则原始能量的输入误差至多 $2H\Delta_w+2H\Delta_c$，因为 $A(x)/x,c_a\in[0,1]$，且 $A(x)/x$ 的扰动至多 $\Delta_w$。脚本保留区间直到最后一次符号相减，计算直接针对 raw $Q$，不调用 completed Schur 能量。表内没有用无限能量外推来填有限算例的右端。两书共同剩下的无条件上界是 $D_a[M_\lambda(a)+1,\infty)=O(a)$；本次给出了相应前缀的 $o(a)$ 和尾部的独立下界。RH 仍开放。
