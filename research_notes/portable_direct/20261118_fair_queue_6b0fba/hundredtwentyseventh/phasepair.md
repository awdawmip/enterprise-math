# 两个整数起点的 Ramanujan 和能量何时翻号

在同一条整数道路取一个均匀起点 $B$，另一个起点定为 $B+H$。分母 $p$ 为大素数时，两处锚定能量的协方差在间距约 $p/\log p$ 时翻号。分母改为 $3p$ 后，即使 $H$ 在模 $p$ 下不变，只加上一个 $p$，仍能把正相关变为负相关。例如 $p=101$ 时，间距 $14$ 与 $115$ 的协方差分别落在 $[28.781,28.796]p^2$ 与 $[-45.596,-45.583]p^2$。以下给出算术系数、第二阶过渡以及有限例子的整数复算。[原研究任务](https://github.com/awdawmip/enterprise-math/blob/169284c1bb7b2365abcf27d019513261656c281a/research_tasks/RH-ROAD-KERNEL-20260909.md) · [单起点能量与平移均值](../hundredsixth/road.md)

令 $c_q(v)=\sum_{(a,q)=1}e^{2\pi iav/q}$，其中求和遍历模 $q$ 的可逆剩余类。写
$$
 E_q(b)=\sum_{N\ge1}N^{-2}\left|\sum_{n=1}^N c_q(n-b)\right|^2,\qquad
 V_{m,p}(H)=p^{-2}\operatorname{Cov}_{B\bmod mp}(E_{mp}(B),E_{mp}(B+H)).
$$
这里 $m$ 固定、平方自由，素数 $p\nmid m$ 趋于无穷。两个读数共享同一个均匀相位 $B$，每个读数都包含无限多个整数截止点。取 $H=rp+h$，$0\le r<m$、$0<h<p$；记 $L=\log p$、$x=h/p$、$A=\varphi(m)$，并约定 $A=1$ 当 $m=1$。

## 主尺度与可计算的边界

**定理一。** 若 $h\sim \lambda p/L$，$0<\lambda<\infty$，则
$$
 \frac{V_{m,p}(rp+h)}{L^2}\longrightarrow\frac{M_r}{\lambda}-A^2,\qquad
 M_r=\prod_{\ell\mid m}
 \begin{cases}
 (\ell-1)(\ell^2-3\ell+3),&\ell\mid r,\\
 2\ell-3,&\ell\nmid r .
 \end{cases} \tag{1}
$$
乘积取素因子，空积取 $1$。特别地 $m=3$ 时 $A^2=4$，$(M_0,M_1,M_2)=(6,3,3)$。在 $h\sim p/L$，同一模 $p$ 间距的头两种提升，归一化协方差分别趋于 $2$ 与 $-1$。

**定理二。** 设 $\mu=M_r/A^2$，$\sigma=2$ 当 $m=1$，$\sigma=0$ 当 $m>1$。对固定实数 $v$，取最近整数间距
$$
 h=\frac{\mu p}{L}\left[1-\frac{(1+\sigma/A^2)\log L+v}{L}\right]+O(1).
$$
则
$$
 \frac{V_{m,p}(rp+h)}L\ \longrightarrow\
 A^2v+(A^2+\sigma)\log\mu+A^2(\gamma+1-2d_m)+D_r,\quad
 d_m=\log m+\gamma+1-\log(2\pi)+\sum_{\ell\mid m}\frac{\log\ell}{\ell-1}. \tag{2}
$$
素分母的右端为 $v+4\log(2\pi)-\gamma-3$。因而素分母的次阶位移含 $3\log L$，固定 $m>1$ 时只含 $\log L$。后者的系数源于背景部分的周期原函数有界，素分母的背景为常数序列，其原函数随长度增长。

### 离散相位的端点展开

用 $b\in\{1,\ldots,p\}$ 表示 $B\bmod p$，$j=(b-B)/p\bmod m$；$b,j$ 独立均匀。平移 $rp+h$ 后的表示为 $(b+h,j-r)$ 当 $b+h\le p$，以及 $(b+h-p,j-r-1)$ 当 $b+h>p$。记 $t_b=\psi_1(b)=\sum_{n\ge b}n^{-2}$、$u_b=pt_b$。存在分解
$$
 E_{mp}(B)/p = a_j u_b +J_j(b/p)+O_m(1/b). \tag{3}
$$
对 $m>1$，写 $a_j=c_m(j)^2$、$C_j(k)=\sum_{i=0}^k c_m(j+i)$，定义
$$
 L_j(z)=\sum_{k\ge0} C_j(k)^2\left(\frac1{k+z}-\frac1{k+z+1}\right),\qquad
 J_j(z)=L_j(z)-a_j/z .
$$
$J_j$ 在 $[0,1]$ 上光滑。确实，第 $k$ 个脉冲后的原始累积值为 $pC_j(k)-\sum_{n\le N}c_m(n-B)$，第二项一致有界。将能量除以 $p$，背景平方与交叉项合计 $O_m(1/p+1/b)$。首脉冲块给 $a_jp(t_b-t_{b+p})$，首项恰是 (3) 的离散奇部。剩余块的递减平方权以首末矩形夹住，求和与相应积分之差 $O_m(1/p)$，同理 $pt_{b+p}=1/(1+b/p)+O(1/p)$。

对 $m=1$，令 $a_0=1$，
$$
 J(z)=F(z)-1/z,\qquad
 F(z)=\log(2\pi)-(1-2z)\psi(z)-2\log\Gamma(z).
$$
在[精确逐余类式](../hundredsixth/road.md)的后段 $(1-z)^2\psi_1(z)$ 中剥去 $z^{-2}-2z^{-1}$，前段及两处正则余项均有一致的一阶导数界。对余项用矩形求积，对调和和用积分界，给 (3)。特别地
$$
 J(z)=2\log z+d_0+O(z),\quad d_0=\log(2\pi)+\gamma-2,\qquad
 J(1)=\log(2\pi)-\gamma-1 .
$$
相同的均值公式给 $\mathbb E_B(E_{mp}(B)/p)=A(L+d_m)+O_m(1/p)$。

### 四项乘积与回卷的贡献

设 $h$ 与 $p/L$ 的比值处在 $(0,\infty)$ 的某个紧子集。定义
$$
 D_r=\frac1m\sum_{j\bmod m}\big[a_jJ_{j-r}(0)+a_{j-r-1}L_j(1)\big]\quad(m>1),
 \qquad D_0=2\log(2\pi)-2\quad(m=1).
$$
此处素分母的 $d_0$ 是 $J(z)-2\log z$ 在零端的值，与均值常数 $d_m$ 分别计算。可统一写成
$$
 V_{m,p}(rp+h)=\frac{M_r}{x}(\log h+\gamma+1)-A^2 L^2+
 [\sigma\log x+D_r-2A^2 d_m]L+O_m((1+\log L)^2). \tag{4}
$$
余项常数容许依赖上述紧集。给出求和细节以保留进入下阶的相位信息。

1. 对于没有回卷的 $b$，两个 $u$ 的乘积平均给
   $p\sum_{b\le p-h}t_bt_{b+h}=x^{-1}(\log h+\gamma+1)+O(1)$。先以 $1/b$ 代 $t_b$，所得为 $x^{-1}(H_h+H_{p-h}-H_p)$，$H_n$ 为调和数。差 $t_b-1/b=O(b^{-2})$ 的总和恰为 $1$，因为 $\sum_{b\le n}t_b=H_n+nt_{n+1}$。把它乘 $p/(b+h)$ 再换成 $p/h$，误差 $O(p\log h/h^2+p/(h(p-h)))$；第二因子用 $1/(b+h)$ 代换的误差亦为 $O(p(1+\log h)/h^2)$。回卷部分 $p\sum_{k=1}^h t_k t_{p-h+k}=L+O(1+\log L)$。两段分别乘 $M_r$ 与 $M_{r+1}$，其中 $M_s=m^{-1}\sum_j a_ja_{j-s}$。中国剩余定理使它分解为 (1)，在每个素因子上只需乘开 $c_\ell(j)^2=1+\ell(\ell-2)\mathbf1_{\ell\mid j}$。
2. 对于第一个 $u$ 与第二个 $J$ 的乘积，主项从 $b\le h$ 给出，因 $\sum_{b\le h}t_b=\log h+\gamma+1+O(1/h)$。复合分母的贡献为 $L\,m^{-1}\sum_j a_jJ_{j-r}(0)$。素分母给 $L(2\log x+d_0)$。在首段以 $J(x)$ 代 $J(x+b/p)$ 的总损失 $O(1)$，源于 $|J'(z)|\ll1+1/z$。其后的未回卷段由 $\sum_{h<b\le p}(1+\log(p/b))/b\ll(1+\log L)^2$ 控制。回卷段在零端的对数可积。将 $\log h$ 换成 $L$ 同样落在该误差内。
3. 反向乘积 $J$ 与 $u$ 的主项来自回卷的 $k=1,\ldots,h$，这时原相位 $b/p$ 距 $1$ 至多 $x$。所给系数为 $m^{-1}\sum_j a_{j-r-1}J_j(1)$ 或 $J(1)$。未回卷段由 $\sum_{b\le p-h}(1+|\log(b/p)|)/(b+h)\ll(1+\log L)^2$ 控制。两个 $J$ 的平均乘积用均方有界性控制为 $O_m(1)$，(3) 中 $1/b$ 误差与另一奇部相乘的平均亦有界，由 $\sum1/(bb')\le\sum1/b^2$ 得到，其中 $b'$ 是移后的相位。

合并第 1 项回卷与第 3 项，$a_j+J_j(1)=L_j(1)$。素分母相应的常数为 $1+d_0+J(1)$。减去均值平方得到 (4)，代入指定间距即得 (1)、(2)。

对 $m=3$ 还可完全消去端点积分。三个 $a_j$ 为 $(4,1,1)$，而 $C_j(k)^2$ 按 $k\bmod3$ 依次为 $(a_j,a_{j-1},0)$。设 $U=\sum_{k\ge1,\,k\equiv1(3)}(1/k-1/(k+1))=\pi/(3\sqrt3)$，另两个余类的权和为 $1-U$。将三项在 $J_j(0),L_j(1)$ 的式子中循环一次，得到 $D_r=U(2M_{r+1}-M_r)$；$U$ 的值也可由 digamma 反射公式取得。因此即使两个提升的 $L^2$ 项相同，也有
$$
 \frac{V_{3,p}(2p+h)-V_{3,p}(p+h)}{\log p}\longrightarrow\frac{2\pi}{\sqrt3}
 \qquad(h\asymp p/\log p).
$$

## 固定步长与素分母过零点

当 $h\ge0$ 固定，(3) 给 $V_{m,p}(rp+h)/p\longrightarrow M_r S_h$，其中 $S_h=\sum_{b\ge1}t_b t_{b+h}$。逐项主值由可和上界 $O_m(b^{-2})$ 控制；回卷仅有 $h$ 项，其乘积在此尺度趋于零。常数无需截断无穷级数，
$$
 S_0=3\zeta(3),\quad S_1=3\zeta(3)-7\zeta(4)/4,\quad
 S_{h+1}-2S_h+S_{h-1}=\frac{2H_h}{h^3}-\frac{\zeta(2)-H_h^{(2)}}{h^2}\quad(h\ge1).
$$
的确 $D(h)=S_h-S_{h+1}=\sum_{b\ge1}t_b/(b+h)^2$。在 $h=0$ 时三角和为 $(\zeta(2)^2+\zeta(4))/2$；相邻两式错位相减，得 $\zeta(2)/h^2-\sum_{b\ge1}1/[b^2(b+h)^2]$，部分分式给所示递推。$S_0$ 用 Euler 的 $\zeta(2,1)=\zeta(3)$。故固定步长在首阶上始终正相关。[定差为零的原方差计算](../hundredsixth/road.md)

这组常数还给出 $(0,1)$ 上正密度的全部整数矩。用 $\sum_{b\ge1}t_b y^{b-1}=(\zeta(2)-\operatorname{Li}_2(y))/(1-y)$ 以及 $t_{b+h}=\int_0^1 y^{b+h-1}(-\log y)/(1-y)\,dy$，得到
$$
 S_h=\int_0^1 y^h\frac{(-\log y)(\zeta(2)-\operatorname{Li}_2(y))}{(1-y)^2}\,dy .
$$
密度在开区间严格为正。因此对每一阶差分 $(-1)^k\Delta^k S_h>0$，任意有限 Hankel 矩阵 $(S_{i+j})_{i,j=0}^{n}$ 都正定。

素分母在整个半周期 $0\le h\le p/2$ 内，充分大的 $p$ 只有一次符号过渡。写 $e_b=E_p(b)/p=u_b+w_b$。由原能量差分，对 $1\le b<p$ 有
$$
 w_{b+1}-w_b=2/b-(1-2b/p)\psi_1(1+b/p)/p .
$$
因此 $w$ 的最大绝对值、圆周总变差均为 $O(L)$，缝边单差亦为 $O(L)$。对两 $u$ 项的圆周乘积作 $h$ 的一阶差，未回卷的主差为 $-pD(h)$，截尾与边界共 $O(1/p)$，回卷差为 $O(1/h+L/p)$。对混合项把差分落在 $w$ 上；除缝边外用 $\sum t_b/b'\ll L/h+L/(p-h)$ 或反向对应式，缝边贡献同阶。两个 $w$ 的差用最大值乘总变差再除以 $p$。于是
$$
 V_{1,p}(h+1)-V_{1,p}(h)=-pD(h)+O(L^2/p)<0 .
$$
$D(h)\sim(\log h)/h^2$ 可由 $b\le h$ 上以 $1/h^2$ 代 $1/(b+h)^2$、余尾 $O(1/h^2)$ 直接得到。以上差分的负号先在 $h\asymp p/L$ 成立，并可延伸到 $1\le h\le 2p/L$：保留混合项误差 $O(L/h+L/(p-h))$ 及 $O(L^2/p)$，即一致小于 $pD(h)\gg p\log(2h)/h^2$。零间距到第一步严格下降也可直接由非恒定序列的平方差得到。对 $2p/L\le h\le p/2$，(3) 给 $w_b$ 一致有上界且均方有界；两奇部的未回卷平均至多 $pS_h$，回卷贡献 $O(L)$。因而 $V_{1,p}(h)\le pS_h-L^2+O(L)<0$，其中用 $S_h$ 递减及 $S_{\lceil 2p/L\rceil}\sim L^2/(2p)$；后一渐近由 (4) 的乘积估计或 $t_b=1/b+O(b^{-2})$ 得到。另一半周期由 $V_{1,p}(h)=V_{1,p}(p-h)$ 决定。结合 (4)，首个非正整数间距为
$$
 \frac{p}{L}\left[1+\frac{-3\log L+4\log(2\pi)-\gamma-3}{L}\right]
       +O\!\left(\frac{p(1+\log L)^2}{L^3}\right).
$$
这里按跨过零的相邻整数定位，允许某个整数恰为零。整条道路上不同分母与实际系数之间的抵消仍是另一个问题。

## 整数复算

对每个余类 $k$，数值证书把 $\sum_{j\ge0}(k+jq)^{-2}$ 的头 40 项以 $2^{-62}$ 为单位向外取整，余尾用递减函数的积分及首项夹住。对原始整数前缀逐项平方，再以乘积下界减去均值平方上界（及反向界）得到协方差区间。这个实现与用周期原函数、两次圆周相关重建全体能量的浮点程序彼此独立。附件还核了九个固定步长的递推、五个平方自由小因子的 CRT 系数，以及 $p$ 到 $100003$ 的浮点样例。极限常数由上述推导给出。[程序](phasepair_check.py) · [整数区间与数值输出](phasepair_checked.json)
