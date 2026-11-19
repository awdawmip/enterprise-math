# 理想类怎样限制同时发生的平面重合旋转

虚二次整数环 $\mathcal O_K\subset\mathbb C$ 可以有非主理想。一个局部看似可行的旋转指标，在整个格上未必由任何旋转实现。本篇研究 $k$ 个**有序、具名、可重复**的保向重合旋转，按它们与原格的共同交格指标截断。每个旋转以单位倍数为同一行。第 32 轮处理了 Eisenstein 整数的类数一情形；这里得到一般虚二次极大环的类约束、各组类的极限比例，以及真旋转所占比例趋向极限的首个非零偏差。[第 32 轮](../thirtysecond/eisenstein.md)

取类群 $G=\mathrm{Cl}(K)$，置 $H=G/G[2]$，$h=|H|$。把所有满足局部格条件的候选行列为一个总体，计数时每个候选元组只算一次。记 $B(X)$ 为交格指标不超过 $X$ 的候选元组总数，$B_0(X)$ 为其中真正能由 $k$ 个旋转实现的个数。如果 $h>1$ 且 $k\ge2$，则存在可用 Euler 乘积求出的 $c_{K,k}>0$，使
$$
 \frac{B_0(X)}{B(X)}
 = \frac{1}{h^k}+\frac{c_{K,k}}{(\log X)^{2^{k-1}}}
      +o\!\left((\log X)^{-2^{k-1}}\right).                         \tag{1}
$$
所以每一行的类条件最终各花一个因子 $h$，但足够大的有限截断中，全部可实现的比例严格偏高。若 $G$ 的每个元素都是 2 阶或单位元，所有候选均能实现，即使类数大于一。已有平面重合理论通过理想分解研究单个或多个重合子格；此处计数的对象是带锚的有序生成元组。此文为从旧文分叉的独立算术，登记计数为零。[Pleasants、Baake、Roth](https://doi.org/10.1063/1.531424) · [Baake、Grimm](https://doi.org/10.1524/zkri.2006.221.8.571)

## 真旋转的精确判据

保向旋转写为复数乘法 $\alpha$，其中 $|\alpha|=1$。它让 $\mathcal O_K$ 与 $\alpha\mathcal O_K$ 有限指数重合，当且仅当 $\alpha\in K$，这是因为两格的有理张成必须相等。对每个分裂有理素数 $p$ 选择一侧 $\mathfrak p$，另一侧记为 $\bar{\mathfrak p}$。候选行由有限支撑的整数 $t_p$ 给出分式理想
$$
      I(t)=\prod_{p\ {\rm split}}
                    (\mathfrak p/\bar{\mathfrak p})^{t_p}.
$$
惰性和分歧处在共轭下固定，$\alpha\bar\alpha=1$ 强制这些赋值为零。反之 $I(t)$ 的绝对理想范数为 1，一旦是主理想，任一生成元的复绝对值即为 1。因 $[\bar{\mathfrak p}]=[\mathfrak p]^{-1}$，准确的条件是
$$
       \sum_p t_p c_p=0\quad\hbox{于 }H,\qquad
       c_p=[\mathfrak p]\pmod{G[2]}.                                \tag{2}
$$
同一候选的全部生成元相差 $\mathcal O_K^\times$。交换某个素数两侧时 $t_p,c_p$ 同时变号。

令 $\mathbf t_p=(t_{1,p},\ldots,t_{k,p})$，加入零行锚点。记 $d(\mathbf t)=\max(0,t_1,\ldots,t_k)-\min(0,t_1,\ldots,t_k)$。理想交逐素位取最大赋值，故候选元组的交指标恰为 $m=\prod_p p^{d(\mathbf t_p)}$。对 $\mathbf b\in H^k$，令 $B_{\mathbf b}(X)$ 计 $m\le X$ 且 $\sum_p c_p\mathbf t_p=\mathbf b$ 的元组。式 (2) 说明 $B_0$ 就是实际旋转数。单个交指标可以由多个不同的有序元组给出。

## 一个局部恒等式同时处理所有类

取有限特征 $\boldsymbol\chi=(\chi_1,\ldots,\chi_k)\in\widehat H^k$，暂固定一个分裂素数，记 $z_i=\chi_i(c_p)$，并补 $z_0=(z_1\cdots z_k)^{-1}$。置 $D_j(z)=1+z+\cdots+z^j$。局部级数有恒等式
$$
 F_p(x)=\sum_{\mathbf t\in\mathbb Z^k}x^{d(\mathbf t)}
               \prod_{i=1}^k z_i^{t_i}
       =(1-x)^2\sum_{j\ge0}x^j\prod_{i=0}^kD_j(z_i).               \tag{3}
$$
对每个包含所有 $t_i$ 和 0 的整数区间 $[-b,a]$，赋权 $x^{a+b}$。固定 $\mathbf t$ 所得权重和为 $x^{d(\mathbf t)}/(1-x)^2$。反过来先固定 $a+b=j$，再对 $b=0,\ldots,j$ 求和，产生第零个几何和。尤其所有 $z_i=1$ 时，$x^e$ 系数为 $(e+1)^{k+1}-2e^{k+1}+(e-1)^{k+1}$（$e\ge1$）。

把 $F_p(p^{-s})$ 对分裂素数相乘，记所得特征级数为 $D_{\boldsymbol\chi}(s)$。对每个非空 $S\subseteq\{1,\ldots,k\}$ 置 $\chi_S=\prod_{i\in S}\chi_i$，视为 $G$ 上的非分歧 Hecke 类特征。直径恰为 1 的列，正好是在某个非空子集上统一为 $+1$ 或 $-1$ 的列。因此
$$
   D_{\boldsymbol\chi}(s)
   =G_{\boldsymbol\chi}(s)\!
       \prod_{\varnothing\ne S\subseteq[k]}L_K(s,\chi_S).            \tag{4}
$$
在分裂处一级系数 $\sum_S(\chi_S(c_p)+\overline{\chi_S(c_p)})$ 完全相消后，修正乘积的局部因子为 $1+O_{k,\sigma}(p^{-2\sigma})$。惰性素理想的范数是 $p^2$，分歧素数只有有限个。由 (3) 的系数界，$G_{\boldsymbol\chi}$ 在 $\Re s>1/2$ 正规收敛、全纯，且在每个闭右半带 $\Re s\ge\sigma>1/2$ 有界。这个全纯因子在一般特征处允许有零点。

置 $r(\boldsymbol\chi)=\#\{S\ne\varnothing:\chi_S=1\}$。式 (4) 在 $s=1$ 的极阶至多是 $r$。这里用到有限类特征的标准 Hecke 延拓、固定竖带多项式增长与 $L_K(1,\psi)\ne0$（$\psi\ne1$）。最后一条也可由 $H$ 对应的 Hilbert 类域子扩张的 Dedekind ζ 分解得出：两端的 ζ 都在 1 有简单极点，其余有限多个 Hecke 因子在 1 全纯，因而都非零。非平凡因子的实轴极限为正，共轭素理想配成正实局部因子，分歧理想的类在 $H$ 中为零。[Neukirch，《Algebraic Number Theory》](https://doi.org/10.1007/978-3-662-03983-0)

为把极阶用于硬截断，记 $A_{\boldsymbol\chi}(X)$ 为相同指标截断下的加权和。对某个固定 $\delta>0$ 有
$$
 A_{\boldsymbol\chi}(X)
   =\operatorname*{Res}_{s=1}D_{\boldsymbol\chi}(s)\frac{X^s}{s}
                   +O_{K,k}(X^{1-\delta}).                          \tag{5}
$$
简述误差。无权局部系数是 $e$ 的固定次多项式，且 $e=1$ 的系数有界，因此总系数逐项 $\ll_{k,\epsilon}m^\epsilon$，可将小素数单独吸收入常数。取一个在 $[1,1+\eta]$ 光滑下降的截止，并在 $3/4\le\Re s\le2$ 对其 Mellin 变换分部积分。在 $|t|\ge1$ 时得到 $O_A(|t|^{-1}(1+\eta|t|)^{-A})$；移到 $3/4$ 线成本至多 $O(X^{3/4}\eta^{-C})$。在 1 附近平滑变换与 $1/s$ 的各固定阶导数相差 $O(\eta)$，改变留数至多 $O(X\eta(1+\log X)^{2^k})$；首尾去平滑成本至多 $O((1+\eta X)X^\epsilon)$。取 $\eta=X^{-b}$，其中 $b>0$ 足够小，再取 $\epsilon<b/2$ 即得 (5)。有限群只有有限多种特征。

## 最慢消失的类偏差

平凡元组有 $r_0=2^k-1$。非平凡元组至多有 $r_*=2^{k-1}-1$。选一个 $\chi_j=a\ne1$，把所有子集按是否加入 $j$ 配对，每对至多一个子集积为 1，再扣掉空集即可。取到上界的**全部**元组为

- 恰有一项非平凡；
- 恰有两项非平凡，且互逆；
- 每一非平凡项均为同一个二阶特征。

以上条件可能重叠。确实，等号要求其余指标的任意子集积在 $\{1,a^{-1}\}$ 中。若有两个非平凡的其余项，则二者都等于 $a^{-1}$，而 $a^{-2}\in\{1,a^{-1}\}$ 迫使 $a^2=1$。反方向逐对检查。

对平凡元组及取到上界的元组，式 (4) 中 $G_{\boldsymbol\chi}(1)>0$。前两类在添加锚后，每个素数处最多留下一对互逆的非平凡相位。因此式 (3) 右边每项是非负的 $(j+1)^{k-1}|D_j(z)|^2$，或全部相位为一。第三类在添加锚后有偶数个 $-1$，乘积同样非负。每次 $j=0$ 均给 1。故 $F_p(1/p)>0$，归一化局部因子也为正，且它们与 1 的差绝对可和。结合正的 ζ 留数与其余 $L$ 值，得到
$$
 g_{\boldsymbol\chi}=\lim_{s\to1^+}(s-1)^{r(\boldsymbol\chi)}
 D_{\boldsymbol\chi}(s)>0
$$
对上述元组成立。因而在这些极大阶处没有局部零点抵消主项。

由有限群 Fourier 反演，$B_{\mathbf b}=h^{-k}\sum_{\boldsymbol\chi}
\overline{\boldsymbol\chi(\mathbf b)}A_{\boldsymbol\chi}$。平凡项就是 $h^{-k}B(X)$，$B(X)\sim Xg_{\bf1}(\log X)^{r_0-1}/(r_0-1)!$。当 $k\ge2$ 时，各极大非平凡项的首项为 $Xg_{\boldsymbol\chi}(\log X)^{r_*-1}/(r_*-1)!$。所以对每个 $\mathbf b$ 都有式 (1) 的展开，将偏差系数换成
$$
 c(\mathbf b)=\frac{(r_0-1)!}{h^k(r_*-1)!\,g_{\bf1}}
       \sum_{\substack{\boldsymbol\chi\ne\bf1\\r(\boldsymbol\chi)=r_*}}
         \overline{\boldsymbol\chi(\mathbf b)}g_{\boldsymbol\chi}.    \tag{6}
$$
同一元组和其逆配对，故此数是实数。对 $\mathbf b=0$，如果 $h>1$ 则可以选取仅一个坐标非平凡的特征元组，每项为正，给出 (1) 的严格正系数。这也给出均匀分布与截断后类分布之间总变差的准确对数阶。$k=1$ 时所有非平凡元组的 $r$ 都为零，(5) 给出 $B_b(X)=B(X)/h+O(X^{1-\delta})$；这一情形没有上述对数偏差。

## 用真正格交检验类条件

取 $K=\mathbb Q(\sqrt{-23})$，$\theta=(1+\sqrt{-23})/2$，整数范数为 $N(a+b\theta)=a^2+ab+6b^2$。Minkowski 界 $(2/\pi)\sqrt{23}<4$ 表明只需范数 2、3 的理想生成类群。两素数都分裂，选 $\mathfrak p_2=(2,\theta),\ \mathfrak p_3=(3,\theta)$，则 $(\theta)=\mathfrak p_2\mathfrak p_3$，$(1+\theta)=\bar{\mathfrak p}_2^3$。范数方程没有解 2，故 $G=H=C_3$。仅在这两个素数上有支撑的行，条件恰是 $t_2-t_3=0\bmod3$。指标 2、3 均无单行旋转，6、8 却各有两行。两个有序行的共同指标恰为 6 时，36 个局部候选只有 6 个真正可实现。

在三元类群内每个非主素类可任选一侧为 $+1$。程序对此作统一选择；若与上例的 $c_3=-1$ 相反，将整个局部列 $\mathbf t_3$ 变号即得保持直径和类残差的双射。复算独立枚举 $(a+b\theta)/n$，要求 $N(a+b\theta)=n^2,\ \gcd(a,b,n)=1$，并去掉共同单位符号。这个最小分母等于单行指标：对每个分裂素数，分母指数是 $|t_p|$。对每组实际旋转，以公共分母把各个旋转逆矩阵的转置格与整数格相加，由所有二阶子式的 gcd 求出对偶格的余体积，再取倒数得到交指标。单行至 180、两行至 90、三行至 36 的逐指标计数均与独立的理想类计数相等。另核 600 个四行以内的局部字符系数（三次单位根在有限域中取值，确切组数见回执）及若干循环群上的极阶等号条件。交指标至 3000 时，两行共有 110,731 个候选，其中 12,511 个来自实际旋转。这些有限计数核验了代数接口，渐近式及偏差符号来自 (3)–(6)。[复算程序](classes_check.py) · [逐指标数据](classes_checked.json)
