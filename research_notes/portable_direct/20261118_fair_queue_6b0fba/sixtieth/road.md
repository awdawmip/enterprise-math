# 哪些素数尺度在固定起点的道路能量中可以一致区分

固定平方自由整数 $m\ge1$ 和实数 $\lambda>1$。对每个充分大的 $P$，取 $p_j$ 为不小于 $P\lambda^j$ 的首个素数，$j=0,1,\ldots$。记 $A_q(N)=\sum_{n=1}^N c_q(n)$，其中 $c_q$ 是完整 Ramanujan 和。**存在只依赖 $m,\lambda$ 的 $0<a<b<\infty$，使任意有限复系数列均满足**
$$
 a\sum_j|z_j|^2\le
 \sum_{N\ge1}\frac1{N^2}\left|\sum_j z_j\frac{A_{mp_j}(N)}{\sqrt{p_j}}\right|^2
 \le b\sum_j|z_j|^2 . \tag{1}
$$
这一估计同时适用于任意长的有限素数列表。只观察 $1\le N\le H$ 时，来自 $p_j>H$ 的所有通道却只有一个可辨方向。本文还给出从离散核到连续极限的带符号误差、近合流尺度和多素因子远距相关变号的实例。证明无条件，$N$ 遍历全部正整数。关于完整道路在参数变化时的算术尾能量，仍须另控制实际系数。[原任务书](https://github.com/awdawmip/enterprise-math/blob/169284c1bb7b2365abcf27d019513261656c281a/research_tasks/RH-ROAD-KERNEL-20260909.md) · [冻结 Ramanujan 展开](https://github.com/awdawmip/enterprise-math/blob/169284c1bb7b2365abcf27d019513261656c281a/research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md) · [审计](../twelfth/road.md) · [原频率核与分母块](../nineteenth/road_blocks.md)

## 1. 从整数能量到平移核

设 $a_1(x)=-\{x\}$，$a_m(x)=A_m(\lfloor x\rfloor)$（$m>1$），$F_m(u)=e^{-u/2}a_m(e^u)$，$T_vF(u)=F(u-v)$，定义 $K_m(v)=\langle F_m,T_vF_m\rangle$。写 $D_m(p,q)=\langle A_{mp}/\sqrt p,A_{mq}/\sqrt q\rangle$，内积用 (1) 的固定起点权。下文 $p,q$ 为不整除 $m$ 的素数，可相同。正尺度 $R=q/p$ 的连续核是
$$
 K_m(\log R)=\sqrt{pq}\int_0^\infty a_m(x/p)a_m(x/q)\,\frac{dx}{x^2}.
$$
当 $m>1$ 时，$a_m$ 有界且 $m$ 周期，记 $M_m=\max|a_m|$。**对全部尺度比**，
$$
 |D_m(p,q)-K_m(\log R)|\le8M_m^2/\sqrt{pq}. \tag{2}
$$
事实上 $A_{mp}(N)=p a_m(N/p)-A_m(N)$。展开内积，含一个小项的两项各用 $\sum_{N\ge p}N^{-2}\le2/p$ 或对 $q$ 的同式，总计至多 $4M_m^2/\sqrt{pq}$；余下的小项乘积至多 $2M_m^2/\sqrt{pq}$。主因子在每个整数格 $[N,N+1)$ 上常值，且须 $N\ge J=\max(p,q)$ 才能非零。其积分权与左端点权之差为 $1/[N^2(N+1)]$，总差至多 $2\sqrt{pq}M_m^2/J^2$。这也给出任何固定有限批 $p_i/P\to r_i>0$ 的极限 Gram，即 $[K_m(\log(r_i/r_j))]$。

对裸素数 $m=1$，$A_p(N)=-(N\bmod p)$。设 $p\le q$。其整数修正具有确定符号及对数主项，
$$
 \tfrac16\le \sqrt{pq}\,[K_1(\log R)-D_1(p,q)]-\tfrac12\log R\le\tfrac{13}4. \tag{3}
$$
记 $x=N+u$，$e_p=N\bmod p$。连续被积函数乘 $\sqrt{pq}$ 后为 $[(e_p+u)/(N+u)][(e_q+u)/(N+u)]$，在每格单调不减。首格贡献 1，$1\le N<p$ 格差为零。$p\le N<q$ 格的差恰为 $(N-e_p)(N^{-1}-\log(1+N^{-1}))$，介于 $1/(2N)-[(p-1)/2+1/3]/N^2$ 和 $1/(2N)$；用对数交错级数即可。$N\ge q$ 的格差介于零与 $(p+q)/(2N^2)$，由乘积对 $u$ 求导、积分获得。求和用 $0\le\sum_{p\le N<q}1/N-\log R\le1/p$ 和 $\sum_{N\ge p}N^{-2}\le1/(p-1)$，得到 (3)。当 $q/p$ 无界，(2) 的无对数形式无法沿用到 $m=1$。

## 2. 所有共同素因子都是可逆的平移算子

以下以 $\ell$ 为指标的乘积均遍历 $m$ 的素因子。Ramanujan 的除数展开给出统一式
$$
 a_m(x)=-\sum_{d\mid m}d\mu(m/d)\{x/d\},\qquad
 F_m=\mathcal D_mF_1,\quad \mathcal D_m=\prod_{\ell\mid m}(\sqrt\ell\,T_{\log\ell}-I). \tag{4}
$$
$m>1$ 时线性项因 $\sum_{d|m}\mu(d)=0$ 消失。每个因子的逆是算子范数收敛的 $\sum_{k\ge1}\ell^{-k/2}T_{-k\log\ell}$。若第 $\ell$ 项截于 $k=L_\ell$，从 $F_m$ 恢复 $F_1$ 的误差不超过 $\|F_1\|[\prod_{\ell|m}(1+\ell^{-L_\ell/2})-1]$，对任意同样的有限平移线性组合也成立，把右侧 $\|F_1\|$ 换成对应组合范数即可。

采用 Fourier 核 $e^{-itu}$，令 $s=1/2+it$。Mellin 恒等式 $-\int_0^\infty\{x\}x^{-s-1}dx=\zeta(s)/s$ 成立于 $0<\Re s<1$。把积分拆在 1，用普通 Dirichlet 级数的分部求和延拓到该条带即可。故 $K_m$ 的双侧谱密度为
$$
 \frac{|\zeta(1/2+it)|^2}{2\pi(1/4+t^2)}\prod_{\ell|m}|\sqrt\ell\,e^{-it\log\ell}-1|^2.
$$
$F_1$ 在两端指数衰减。该密度几乎处处正，临界线上的离散零点不影响这一性质。对有限互异实平移，非零指数多项式几乎处处非零，Gram 严格正定。$F_1$ 的全体实平移的线性张成稠密于 $L^2(\mathbf R)$：若 $g$ 与所有平移正交，$\widehat g\,\overline{\widehat F_1}$ 是 Fourier 逆变换恒零的 $L^1$ 函数，故 $g=0$。从而对同一实尺度组的 Gram 有尖锐比较
$$
 \prod_{\ell|m}(\sqrt\ell-1)^2G_1\preceq G_m\preceq\prod_{\ell|m}(\sqrt\ell+1)^2G_1 . \tag{5}
$$
尖锐性指遍历所有有限实尺度和所有系数。下端在零频附近，上端可由 Kronecker 逼近使所有素数相位趋于 $-1$，因为不同素数的对数在 $\mathbf Q$ 上线性无关。稠密性使两端均可由有限组合逼近。固定某一离散网格的最优常数可以更好。连续分数部分自相关的源流见 Báez-Duarte、Balazard、Landreau、Saias。[经典连续核](https://doi.org/10.1007/s11139-005-0834-4)

## 3. 固定任意几何比的统一下界

设 $h=\log\lambda>0$。对 $0\le u<h$ 作 Zak 和 $Z_\theta(u)=\sum_{j\in\mathbf Z}F_1(u+jh)e^{ij\theta}$。因为 $|F_1(u)|\le e^{-|u|/2}$，在 $u$ 的紧集上对 $\theta$ 一致绝对收敛。Gram 卷积的 Fourier 符号为
$$
 S_h(\theta)=\int_0^h |Z_\theta(u)|^2du=\sum_{n\in\mathbf Z}K_1(nh)e^{in\theta}.
$$
$|K_1(v)|\le(2+|v|)e^{-|v|/2}$，故符号连续且有界。观察 $Z_\theta$ 在 $u=0$ 的跳。基波在 $\log n$ 的跳等于 $1/\sqrt n$。若 $\lambda$ 没有正整数次幂为整数，只剩 $n=1$，跳为 1。否则取最小的 $d>0$ 使 $Q=\lambda^d$ 为整数，所有这样的指数恰为 $d$ 的倍数。理由是两次整数幂的最大公因数次幂为有理数（Bézout），且该有理数有一正幂为整数，故本身为整数。总跳为 $1/(1-Q^{-1/2}e^{id\theta})$。两种情形每个 $\theta$ 的跳都非零。一致收敛保证两边极限存在，至少一侧有正测度的非零值，因此 $S_h(\theta)>0$。在圆上取极值得 $0<a_h\le S_h\le b_h<\infty$，即整个双向格上的 Riesz 不等式。由 (5) 立刻推到各 $m$。

**一项可手检的下界。** $\lambda=2$ 时 $a_h>2^{-20}$。取 $0<t<\delta=2^{-16}$ 并写 $H_\theta(x)=\sqrt x\,Z_\theta(\log x)$。比较 $H_\theta(1+t)-H_\theta(1-t)$ 与上述跳。对 $j\le16$，负指标只贡献斜率，非负指标跳后两边剩余斜率误差合计至多 $2t\sum_{j\le16}2^{j/2}<1/32$。较高指标的误差至多 $2\sum_{j>16}2^{-j/2}<1/32$。跳的绝对值至少 $1/(1+2^{-1/2})$，故两值之差模大于 $1/2$。对 $t$ 积分，因 $\log[(1+\delta)/(1-\delta)]<h$ 且 $|Z|$ 按 $h$ 周期，
$S_h\ge\delta/[8(1+\delta)^2]>2^{-20}$。

**回到真正的素数通道。** 设 $p_j$ 如开头所选，$\eta_P=\sup_{j\ge0}|\log(p_j/(P\lambda^j))|$。普通素数定理给出 $\eta_P=o(1)$，因为对任意固定 $\epsilon>0$，所有充分大的 $x$ 在 $[x,(1+\epsilon)x]$ 中有素数。因此这些素数最终互异并与 $m$ 互素。对 $m>1$ 也有 $|F_m(u)|\le M_m e^{-|u|/2}$。连续平移 Gram 在对数坐标的错位 $\le\eta_P$ 下按算子范数趋于原格：当 $|j-k|\le L$，各项之差由 $K_m$ 的连续性一致趋零；其余的绝对行和统一受 $O_{m,h}(\sum_{r>L}(1+r)e^{-hr/2})$ 控制。先取 $L$ 再取 $P$，由 Schur 检验得证。由 (2)、(3) 叠加的离散误差绝对值逐元为 $O_{m,h}(P^{-1}(1+|j-k|)\lambda^{-(j+k)/2})$，其算子范数为 $O_{m,h}(P^{-1})$。于是 (1) 成立，并保留所有复系数相位。这只需普通素数定理，不需给首素数距离加入假设。

## 4. 近合流和有限采样的不同限制

令 $v\to0$。第十九轮给 $\|A_{mp}-A_{mq}\|^2=\varphi(m)(q-p)\log[p/(q-p)]+O_m(q-p)$ 于 $0<q-p<p/2$。固定小 $v>0$，选 $p\to\infty,q/p\to e^v$ 后用 (2)、(3) 传到连续核；除以 $p$ 后左侧趋 $C_m(1+e^v)-2e^{v/2}K_m(v)$，其中 $C_m=K_m(0)>0$。利用偶性得
$$
 2(C_m-K_m(v))=\varphi(m)|v|\log(1/|v|)+O_m(|v|). \tag{6}
$$
因此格比趋 1 时 (1) 的下界不能对所有格比保持同一正数。还可以求整簇退化率。固定 $x_0<\cdots<x_k$，记 $G_\epsilon=[K_m(\epsilon(x_i-x_j))]$，$\beta=\varphi(m)\epsilon\log(1/\epsilon)$。用第一列波形和其余各相邻增量代替原波形，换基行列式为 1。增量平方范数是 $\beta(x_i-x_{i-1})+O(\epsilon)$；不重叠区间的两增量内积为 $O(\epsilon)$，由 (6) 的四项距离极化，绝对值线性项在不重叠区间上相消。首波形与各增量内积为 $O(\beta)$。将增量各除以 $\sqrt\beta$，便得
$$
 \det G_\epsilon\sim C_m\beta^k\prod_{i=1}^k(x_i-x_{i-1}).
$$
在区间 $(x_i,x_{i+1})$ 加一点 $x$ 后，新增波形到所有原点张成空间的平方距离是两个 Gram 行列式的比，渐近为 $\beta(x-x_i)(x_{i+1}-x)/(x_{i+1}-x_i)$。该结论限固定点数和给定互异尺度。

**整数前缀的精确秩。** 给 $k$ 个不同素数 $p_1<\cdots<p_k$，观察 $1\le N\le H$，$H\ge1$。此有限矩阵秩恰为
$$
 \min\{k,1+\#\{i:p_i\le H\}\}. \tag{7}
$$
对未归一化列，$N=1$ 读出总系数乘 $-A_m(1)=-\mu(m)\ne0$，这里约定 $A_1(N)=N$。再依次用 $N=p_i\le H$，扣掉已知的较小素数项，剩余新主元为 $p_i A_m(1)$。未越过的所有素数给同一列 $-A_m(N)$，只影响它们的系数总和。归一化列将未越过的系数改按 $1/\sqrt{p_i}$ 加权。$k\ge2$ 时首次满列秩为 $H=p_{k-1}$。故全无限能量有统一下界，与每个固定前缀能被两条远素数通道精确抵消同时成立。式 (7) 只谈无噪精确辨识。

## 5. 远尺度的符号在第二项留下算术周期

$m>1$，$R\to\infty$。记 $B_2(x)=x^2-x+1/6$，$H_m(x)=-\frac12\sum_{d\mid m}d^2\mu(m/d)B_2(\{x/d\})$。这是 $a_m-\bar a_m$ 的连续周期原函数，均值为零，$\bar a_m=-\varphi(m)/2$。则
$$
 K_m(\log R)=\frac{\varphi(m)\Lambda(m)}{2\sqrt R}
       +\frac{B_m(R)}{R^{3/2}}+O_m(R^{-5/2}),\qquad
 B_m(R)=-\sum_{n\ge1}\frac{c_m(n)H_m(Rn)}{n^2}. \tag{8}
$$
$\Lambda$ 为 von Mangoldt 函数。将积分写为 $R^{-1/2}\int a_m(Ry)a_m(y)dy/y^2$。$\int a_m(y)dy/y^2=-\Lambda(m)$ 由除数和或 (4) 的 Mellin 变换在 $s=1$ 消极点得到。就其余项分部积分，$d(a_m(y)/y^2)$ 在各整数 $n\ge1$ 有跳 $c_m(n)/n^2$，其连续部分为 $-2a_m(y)dy/y^3$。后者乘 $H_m(Ry)$ 的积分为 $O_m(1/R)$，因为 $H_m$ 有有界原函数且 $a_m(y)/y^3$ 的全变差有限。由此得 (8)。

$B_m$ 连续、$m$ 周期且均值为零。$H_m(0)=-\prod_{\ell|m}(\ell^2-1)/12$ 和 $\sum c_m(n)/n^2=\zeta(2)\prod_{\ell|m}(\ell^{-1}-1)$ 给出 $B_m(0)\ne0$。因此单素公共因子有正的远距主项；含两个或更多素因子的 $m$ 则 $\Lambda(m)=0$，正定核在任意远处都取到两种符号。例 $m=6$ 时 $H_6(0)=-2,H_6(3)=2$，$B_6(0)=2\zeta(2)/3$、$B_6(3)=-4\zeta(2)/3$。实际的不同素数之比通常不落在指定整数余类。依 (2)，当 $R=q/p=o(p)$ 且 $R\bmod m$ 保持在 $B_m$ 有严格符号下界的邻域时，离散误差是 $o(R^{-3/2})$，符号随之保留。这类素数对也可先逐个固定大的目标比值，再用普通素数定理选足够大的 $p,q$ 逼近构造。

## 6. 复算

运行 `python road_check.py`，仅需 Python 标准库。用 2640 个分数点检查 (4)，分别以完整分母除数式、共同因子阶梯式及带余项的连续积分比对 (2)、(3)。例如 $(p,q)=(11,101)$ 时，$\sqrt{pq}(K_m-D_m)$ 对 $m=1$ 处于 $(2.088,2.238)$，对 $m=6$ 处于 $(-2.505,-2.249)$。程序为每格作有向整数舍入并加入无穷尾界，用有理消元对照 225 个前缀秩，另以除数展开核验 $m=6$ 的两个远距周期系数。这些有限检查各有明确截断，(1) 的无限素数族结论依赖第 3 节的证明。[复算程序](road_check.py) · [有理区间与精确结果](road_checked.json)
