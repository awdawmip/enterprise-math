# 同一 Ramanujan 和的整数起点能把锚定能量改变多少

在完整道路的每个整数截止点 $N$ 观察累积，用权 $N^{-2}$ 计能量。对素数分母 $p$，所有整平移的逐频功率都相同。最小锚定能量却渐近于 $p\log2$，最大值渐近于 $p^2\pi^2/6$。在 $p$ 个具名相位里均匀抽一个，能量除以 $p$ 的极限中位数约为 $0.9766745$；平移平均本身则按 $p\log p$ 增长。以下把相位的每一步变化，以及所有分母的平均误差，落实到原道路的同一范数中。[原登记](https://github.com/awdawmip/enterprise-math/blob/169284c1bb7b2365abcf27d019513261656c281a/research_tasks/RH-ROAD-KERNEL-20260909.md) · [冻结道路展开](https://github.com/awdawmip/enterprise-math/blob/169284c1bb7b2365abcf27d019513261656c281a/research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md) · [研究核审计](../twelfth/road.md)

写
$$
 c_q(v)=\sum_{\substack{a\bmod q\\(a,q)=1}} e^{2\pi iav/q},\quad
 A_{q,b}(N)=\sum_{n=1}^N c_q(n-b),\quad
 E_q(b)=\sum_{N\ge1}\frac{|A_{q,b}(N)|^2}{N^2}.
$$
求和取模 $q$ 的所有可逆剩余类，$b=1,\ldots,q$，$b=q$ 是未平移原块。下文 $q\ge2$；周期和为零，所以各 $E_q(b)$ 有限。$q=1$ 的原块为常数一，其能量发散。固定起点仍为 1；移动的是整块的整数相位。有限平移平均只作为丢掉相位后的单一统计量。第 19 轮与第 60 轮研究原相位的不同分母及其相关性，第 92 轮分析了逃逸尾场的零读数。[分母替换](../nineteenth/road_blocks.md) · [几何尺度的分母族](../sixtieth/road.md) · [逃逸尾](../ninetysecond/zeros.md)

## 首个脉冲的位置与完整能量分布

素数情形 $c_p(n-b)=p\mathbf1_{n\equiv b\ (p)}-1$，首个脉冲恰在 $n=b$。令 $\psi=(\log\Gamma)'$、$\psi_1=\psi'$。写 $k=N\bmod p$，则
$$
 A_{p,b}(N)=-k+p\mathbf1_{k\ge b},\qquad
 E_p(b)=\sum_{1\le k<b}(k/p)^2\psi_1(k/p)
       +\sum_{b\le k<p}(1-k/p)^2\psi_1(k/p).
 \tag{1}
$$
余类零的贡献为零。由同一余类上 $\sum_{j\ge0}(jp+k)^{-2}=p^{-2}\psi_1(k/p)$，在 $1\le b<p$ 上有精确差分
$$
 E_p(b)-E_p(b+1)=(1-2b/p)\psi_1(b/p).
 \tag{2}
$$
对每个奇素数 $p$，能量随 $b$ 先严格下降、再严格上升，唯一最小相位是 $(p+1)/2$。最大只能位于两端；在 (2) 中成对取 $b,p-b$，因 $\psi_1$ 严格下降，每个差分对相加均为正，故唯一最大相位是 1。$p=2$ 两个相位确实并列，能量都是 $\pi^2/8$。

对任何 $b/p\to x\in(0,1]$，(1) 作为黎曼和给出
$$
 \frac{E_p(b)}p\ \longrightarrow\
 F(x)=\log(2\pi)-(1-2x)\psi(x)-2\log\Gamma(x).
 \tag{3}
$$
该收敛在 $b/p\in[\epsilon,1]$ 一致。直接积分首先给 $F(1)=\int_0^1 u^2\psi_1(u)\,du=\log(2\pi)-\gamma$，利用两次分部积分和 $\int_0^1\log\Gamma(u)\,du=\tfrac12\log(2\pi)$。后者由 Gamma 反射式与 $\int_0^1\log\sin(\pi u)\,du=-\log2$ 得到。其余部分为 $\int_x^1(1-2u)\psi_1(u)\,du$，产生 (3)。特别 $F(1/2)=\log2$。在另一端 $x\downarrow0$，有 $F(x)=1/x+2\log x+O(1)$。当 $b=o(p)$，相应的整数端点公式为
$$
 E_p(b)=p^2\sum_{k\ge b}k^{-2}
          +O\!\left(p[1+\log(p/b)]\right)
       \sim p^2\psi_1(b).
 \tag{4}
$$
事实上在 $0<u\le1$，$u^2\psi_1(u)=O(1)$，$(1-u)^2\psi_1(u)=u^{-2}-2u^{-1}+O(1)$，代回 (1) 并补上 $k\ge p$ 的尾项即证。$b=1$ 给出最大值系数；$b=p$ 则属于 (3) 的右端点。[三伽马函数的级数](https://dlmf.nist.gov/5.15) · [Gamma 反射公式](https://dlmf.nist.gov/5.5)

取 $b$ 均匀，(3) 联合长度至多 $\epsilon p$ 的首段界给出 $E_p(b)/p\Rightarrow F(U)$，$U$ 在 $(0,1)$ 均匀。由 $F'(x)=-(1-2x)\psi_1(x)$，左、右分支在 $1/2$ 两侧严格单调。对充分大的 $v$ 只有左分支能超出 $v$，于是 $\Pr(F(U)>v)\sim1/v$。中位数 $c$ 位于 $\log2$ 与 $F(1)$ 之间：在 $c=F(1)$ 下整个右半区和一段左半区都已计入。因而 $c$ 由唯一的 $0<x_-<1/2$ 满足 $F(x_-)=F(x_-+1/2)=c$ 给出，数值约为 $x_-=0.3157192,x_+=0.8157192,c=0.9766745$。中位能量对应左右两种起点；概率极限的无穷均值也提示不能把 (3) 逐点取平均。

## 所有分母的平移平均及统一误差

**定理。** 令 $\overline E_q=q^{-1}\sum_{b=1}^q E_q(b)$，$c=\gamma+1-\log(2\pi)$。对每个整数 $q\ge2$，
$$
 \left|\overline E_q-\varphi(q)\left(\log q+c+
                    \sum_{p\mid q}\frac{\log p}{p-1}\right)\right|
 \le \frac2q\prod_{p\mid q}(1+p).
 \tag{5}
$$
乘积、求和均只计不同素因子。该式同时适用于原道路采用的平方自由分母以及单独定义的非平方自由 Ramanujan 和；无须限制素因子个数或最小素因子。

令 $h_N(\theta)=\sum_{n=1}^Ne^{in\theta}$。在全部平移上平均，正交性恰好消去不同具名频率间的项。对单频 $\theta=2\pi x,\ 0<x<1$，有
$$
 \sum_{N\ge1}|h_N(2\pi x)|^2/N^2
 =G(x)=\frac{\pi^2x(1-x)}{2\sin^2(\pi x)} .
$$
这是由 $\sum_{N\ge1}(1-\cos(2\pi N x))/N^2=\pi^2x(1-x)$ 与有限几何和得到。因此 $\overline E_q=\sum_{1\le a<q,\,(a,q)=1}G(a/q)$。固定 $b$ 时，这些复相位在跨频项中仍起作用，见 (1) 的不同能量。

设 $B_m=\sum_{1\le a<m}G(a/m)$，$B_1=0$，则 $\overline E_q=\sum_{d\mid q}\mu(d)B_{q/d}$。由 $\psi_1(x)+\psi_1(1-x)=\pi^2/\sin^2(\pi x)$ 及配对，$B_m=\sum_{a=1}^{m-1}x(1-x)\psi_1(x)$，$x=a/m$。在两个端点都可正则延拓的函数为
$$
 H(x)=x(1-x)\psi_1(x)-1/x
     =-1+x(1-x)\sum_{\ell\ge1}(\ell+x)^{-2}.
$$
它满足 $H(0)=H(1)=-1$、$\|H''\|_\infty\le2\zeta(2)+4\zeta(3)+\tfrac32\zeta(4)<12$。将积分先从 $\epsilon$ 起算，$[x(1-x)\psi-(1-2x)\log\Gamma]_{\epsilon}^1-2\int_{\epsilon}^1\log\Gamma$ 再加 $\log\epsilon$，取极限得 $\int_0^1H=1-\log(2\pi)$。复合梯形公式的总余项在求和量级至多 $\|H''\|_\infty/(12m)$；调和数满足 $|m H_{m-1}^{\rm harm}-m(\log m+\gamma)+1/2|\le1/(12m)$。合并可取对所有 $m\ge1$ 的绝对界
$$
 |B_m-m(\log m+c)-1/2|\le2/m .
$$
在 $\mu(d)$ 求和中常数项 $1/2$ 对 $q>1$ 完全消失。由 $\sum_{d\mid q}\mu(d)q/d=\varphi(q)$，每个 $p\mid q$ 在 $\log(q/d)$ 的额外系数为 $\varphi(q)/(p-1)$。各误差绝对相加给 $\sum_{d\mid q}2|\mu(d)|d/q$，正是 (5) 的右端。特别素数分母的平均为 $p(\log p+c)+O(1)$。

## 复合分母的尾常数与矩的分界

固定平方自由 $m>1$，取 $p\nmid m$ 的素数趋于无穷。要在 $q=mp$ 上保留原整数频率，令 $B$ 是均匀的整相位，$1\le b\le p$ 为 $B\bmod p$ 的正代表，$j=(b-B)/p\bmod m$。这给全部 $p m$ 个相位与 $(b,j)$ 的双射，所以 $b,j$ 独立均匀。令 $C_j(k)=\sum_{\ell=0}^kc_m(j+\ell)$。$c_{mp}(n-B)=(p\mathbf1_{n\equiv b\,(p)}-1)c_m(n-B)$，而 $c_m(pv)=c_m(v)$。因此在 $b+kp\le N<b+(k+1)p$ 上，累积值恰为 $pC_j(k)-A_{m,B}(N)$；在首脉冲前只有后一项。$C_j$ 与 $A_{m,B}$ 都有界，只依赖 $m$。

于是若 $b/p\to x>0$ 且 $j$ 固定，能量除以 $p$ 趋于
$$
 L_j(x)=\sum_{k\ge0} C_j(k)^2
            \big[(k+x)^{-1}-(k+x+1)^{-1}\big] .
$$
对每块把 $N^{-2}$ 之和乘 $p$ 取黎曼积分，剩余高块以有界 $C_j$ 和收敛的望远镜差控制；背景平方总贡献为 $O_m(1)$，混合项为 $O_m(p/b)$。故均匀相位的分布极限为 $L_J(U)$，其中 $J$ 在模 $m$ 余类上均匀且与 $U$ 独立。由 $L_j(x)=c_m(j)^2/x+O_m(1)$，
$$
 \lim_{v\to\infty}v\,\Pr(L_J(U)>v)
     =\frac1m\sum_{j\bmod m}c_m(j)^2=\varphi(m).
$$
$F$ 的素数情形须独立处理：$m=1$ 时背景原函数为 $N$，不满足这里使用的有界性。

对任意固定 $s>1$，均匀相位的高矩还可直接算出：
$$
 \lim_{p\to\infty}\frac{\mathbb E_B E_{mp}(B)^s}{p^{2s-1}}
 =\left[\prod_{\ell\mid m}\frac{(\ell-1)^{2s}+\ell-1}{\ell}\right]
        \sum_{b\ge1}\psi_1(b)^s ,
 \tag{6}
$$
乘积取素因子。固定 $b,j$，从 $b$ 到下一脉冲的能量为 $p^2c_m(j)^2\psi_1(b)+O_m(p+p/b)$，这里已将下一脉冲以后的平方权尾和补回。所有后续脉冲所在的实际余尾同样至多 $O_m(p)$。对全部 $b\le p$ 均有 $E_{mp}(B)/p^2\ll_m1/b$，因此按 $b$ 作支配收敛便得 (6)。CRT 下 $c_m$ 的 $2s$ 次绝对矩分解为上述局部乘积。若 $0<s<1$，同一界使 $(E_{mp}/p)^s$ 在 $b/p<\epsilon$ 上的平均至多 $O_{m,s}(\epsilon^{1-s})$，所以该归一化的矩趋于 $\mathbb E L_J(U)^s$。$s=1$ 的临界增长由 (5) 给出。

特别地 $\sum_{b\ge1}\psi_1(b)^2=\sum_{a,k\ge1}\min(a,k)/(a^2k^2)=\zeta(3)+2\zeta(2,1)=3\zeta(3)$，用的是 Euler 的 $\zeta(2,1)=\zeta(3)$。以 (5) 控制均值平方便有
$$
 \operatorname{Var}_B E_{mp}(B)
 \sim 3\zeta(3)\,p^3\prod_{\ell\mid m}(\ell-1)(\ell^2-3\ell+3).
$$
这些平均都对平移的有限相位取值，$N$ 仍遍历全部正整数。[Euler 双重和恒等式](https://mathworld.wolfram.com/MultipleZetaFunction.html)

## 复算

在 $m=2,3,6,10$ 的四个复合样例中，还对 9,797 个具名相位与截止点组合逐项核对脉冲分解及局部四次矩。在 54 个分母的 2,104 个实际整数平移上，程序由 $c_q(n)=\sum_{d\mid(q,n)}d\mu(q/d)$ 生成整数前缀，逐个周期余类核验二阶均值与非本原网格的 Möbius 消去完全一致。无限尾的区间用 $\psi_1(z)$ 的交错 Euler–Maclaurin 余项：将前十项精确相加，在 $z\ge10$ 处余尾用 $1/z+1/(2z^2)+1/(6z^3)-1/(30z^5)$ 及该式加 $1/(42z^7)$ 夹住。此界也可由 $\psi_1$ 的 Laplace 积分及双曲余切部分分式，逐项使用几何级数的交错余项得到。所有原能量区间按整数向外取整；中位数的小数是独立数值读数。[复算程序](road_check.py) · [整数区间](road_checked.json) · [部分分式](https://dlmf.nist.gov/4.36)

| $q$ | 全部平移的平均能量 | $E_q(1)$ | $E_q((q+1)/2)$ | $E_q(q)$ |
|---:|---:|---:|---:|---:|
| 5 | 7.18947 | 20.10402 | 2.88852 | 4.99545 |
| 31 | 98.86426 | 1343.64777 | 20.97432 | 37.76042 |
| 101 | 440.29766 | 15771.72710 | 69.50379 | 126.00507 |
| 210 | 338.63196 | | | |

文中的概率来自额外声明的均匀平移实验。给定道路系数和固定相位产生的尾部抵消，还需要控制这些实际相位之间的联合关系。
