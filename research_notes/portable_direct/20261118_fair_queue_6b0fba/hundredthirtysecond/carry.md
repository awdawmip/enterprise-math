# 普通素数进位窗的逼近误差能读出零点最右实部

固定 $C>6$。在每个整数块 $N\le n<2N$ 上，对 $y\le N/(\log N)^C$ 的普通素数半剩余类进位求和，再减去同一窗口的连续积分。**在所有二幂块上，这个差的最大块范数有多对数上界，当且仅当黎曼猜想成立。** 在 RH 下该范数趋于零。无条件地说，其对数增长上极限精确等于非平凡零点的实部上确界减去 $1/2$。离散读数可以反推素数计数，原因是两个截点之间存在正比例的一组整数，让所有中间素数同时处于同一进位半区。另一组整数使它们同时处于相反半区。

给定整数 $2\le y\le N$，采用原读数
$$
 c_p(n)=\lfloor2n/p\rfloor-2\lfloor n/p\rfloor,\quad
 a_p=\lfloor p/2\rfloor/p,\quad w(v)=\mathbf1_{\{v\}\ge1/2}-1/2,
$$
$$L_y(n)=\sum_{p\le y}[c_p(n)-a_p]\log p,\qquad I_y(n)=\int_0^y w(n/x)\,dx,\qquad
 B(N,y)^2=\sum_{N\le n<2N}\frac{|L_y(n)-I_y(n)|^2}{n^2}.$$
奇素数精确满足 $c_p(n)-a_p=w(n/p)+1/(2p)$。$p=2$ 的偏移为零。每个 $y$ 在求整块能量时固定，再对 $y$ 取最大值。记 $\Theta=\sup\{\Re\rho:\zeta(\rho)=0,\;0<\Re\rho<1\}$，$1/2\le\Theta\le1$。

第7轮给出真整数半剩余类的中心，第78轮处理原计数中心全素幂 $J$ 的增长指数，第120轮把 $L_y$ 无条件逼近至 $N^{2/3}$ 乘任意固定对数幂，并在 RH 下得到第一临界截断 $N^{3/4}$ 的三角波。本篇求误差 $L_y-I_y$ 的双向判据及全部固定阶的后续波形。前向使用经典加性大筛、von Mangoldt 显式公式和短区间二次均值方法，逆向使用整数符号读数和经典 von Koch 判据。原始未经校正的平方函数是否无条件多对数有界，仍由原任务的开放范围约束。[原任务书](https://github.com/awdawmip/enterprise-math/blob/29840e4bcf6fc68a07e3be7677913535b57749e7/research_tasks/RH_BRC_COUNT_CENTERED_CARRY_CLOSURE_20260909.md) · [原进位函数](https://github.com/awdawmip/enterprise-math/blob/437d4d595f1495d3a0486b3c06e9e2b14567db82/src/enterprise_math/brc_count_centered_carry.py) · [第7轮](../seventh/carry.md) · [第78轮](../seventyeighth/edge.md) · [第120轮](../hundredtwentieth/aperture.md)

## 1. 用加性大筛同时抑制系数误差

设 $\ell=\log(2N)$。以下渐近量均以 $N\to\infty$ 为准，$y$ 在 $[2,Y]$ 内取整数。对任意 $Y=Y(N)=o(N/\ell^6)$，在 RH 下有 $\sup_{2\le y\le Y}B(N,y)=o(1)$。更一般地，对同一个范围，无条件有
$$\sup_{2\le y\le Y}B(N,y)\ll o(1)+Y^{\Theta}\ell^3/\sqrt N.$$
第一项可一致取 $O(\ell^{-1/2}+N^{-1/10}\ell^{O(1)})$。

沿用原大筛，$p\le N^{3/5}$ 范数为 $O(N^{-1/10}\sqrt\ell)$。该处积分范数 $O(N^{-3/10})$。其余用 $X\asymp2^jN^{3/5}$ 的 $(X,b],b\le2X$ 分段。取 $K=\lceil\ell^4\max(1,X^3/N^2)\rceil$。$K=o(X)$，故 $h/p$ 的正负频率彼此不合并，整圈间隔 $\gg X^{-2}$。在约定 $e(x)=\exp(2\pi i x)$ 下，非零连续系数为 $\widehat w(h)=((-1)^h-1)/(2\pi i h)$。对应离散系数为 $[e(-h\lceil p/2\rceil/p)-1]/[p(1-e(-h/p))]$。在 $0<|h|\le K$ 二者相差 $O(1/p)$，在 $0<|h|\le(p-1)/2$ 离散系数为 $O(1/|h|)$，两条都是有限几何和。所有低频系数差的平方权至多 $O(K\sum_{X<p\le 2X}(\log p)^2/p^2)=O(K\log(2X)/X)$。因此整段替换的平方范数由加性大筛给出
$$\ll (N+X^2)K\log(2X)/(N^2 X).$$
低 $X$ 时它为 $O(N^{-4/3}\ell^5)$（$X\le N^{2/3}$），高 $X$ 时为 $O((X/N)^4\ell^5)$。高段范数的 $X^2$ 因子沿各段作几何求和。离散频尾单段平方范数 $\ll(N+X^2)X\log(2X)/(N^2K)\ll \ell^{-3}$，全部段的范数和 $O(\ell^{-1/2})$。连续频尾每段 $O(X^2/(N^{3/2}K))=O(N^{-1/6})$。连续频尾用 $|\int_X^b e(hn/x)dx|\ll X^2/(N|h|)$ 求和。先取 Fejér 平均即可绕开跳点的逐点级数约定。这些估计允许末段在任意整数处截断。[Montgomery–Vaughan，《The large sieve》](https://doi.org/10.1112/S0025579300004708)

## 2. 不同实部零点的短窗均方

现在每个 $1\le h\le K$ 都只需比较同一谐波上的 $d\vartheta-dx$，其中 $\vartheta(x)=\sum_{p\le x}\log p$。将它在 $(X,b]$ 上用 $x\mapsto h/x$ 推到圆上，记为 $\mu_h$。取弧长 $\delta=1/(8N)$。区间指示的第 $n$ 个 Fourier 系数在整块内模长 $\gg N^{-1}$。Parseval 给 $N^{-2}\sum_{N\le n<2N}|\widehat\mu_h(n)|^2\ll\int|\mu_h([v,v+\delta])|^2dv$。对该小弧换元 $x=h/(v+\delta)$，$|dv|\asymp h\,dx/X^2$。弧原像若被截点切开，两端仍落在 $[x,x+H]$，端点差的平方至多为最大增量平方的四倍。因此
$$B_h^2\ll\frac h{X^2}\int_{X/2}^{3X}
  \sup_{0\le v\le H}|\vartheta(x+v)-\vartheta(x)-v|^2 dx,$$
这里 $B_h$ 表示该段该谐波的块范数。取固定大常数 $C_0$，则 $H=C_0X^2/(Nh)$ 对 $1\le h\le K$ 统一满足 $1\ll H=o(X)$。较小的 $X$ 有 $H\gg N^{1/5}/\ell^4$，较大的 $X$ 有 $H\gg N/(Y\ell^4)$。$h/x$ 离周期切口的距离大于弧长，截段后的两端均在同一个长 $H$ 的短窗内。

令 $\psi(v)=\sum_{p^j\le v}\log p$，$Q(v)=\psi(v)-v$。固定 $1/X\ll s\ll H/X$，写 $\log x=\log X+u$。第120轮显式公式的非平凡零点对 $Q(e^s x)-Q(x)$ 的贡献在除以 $X^\Theta$ 后是
$$-X^{\rho-\Theta}\,(e^{\rho s}-1)\rho^{-1} e^{\beta u}e^{i\gamma u},\qquad \rho=\beta+i\gamma.$$
系数模 $\ll\min(s,(1+|\gamma|)^{-1})$。在有界 $u$ 窗取光滑紧支上包络，乘积核对 $\beta,\beta'\in[0,1]$ 一致为 $O_A((1+|\gamma-\gamma'|)^{-A})$，这是分部积分的直接结果。将零点按虚部的单位箱分组，计入重数时各箱仍有 $O(\log(2+|\gamma|))$ 个零点。箱间衰减矩阵行和有界。将 $\sum_{k\ge1}\log^2(2+k)\min(s^2,k^{-2})$ 在 $1/s$ 处分开，得到固定步归一均方 $\ll s\log^2(2/s)$。可先截零点再取局部二次均值极限，固定 $s$ 的上述箱估计尾趋零。跳点是积分零测集。常数消去，平凡零点项在 $x\asymp X$ 上更小。固定步长的平方积分乘回 $dx\asymp Xdu$ 与 $X^{2\Theta}$ 后为 $O(X^{1+2\Theta}s\ell^2)$。对数坐标二进拆分，一层有 $O(H/(Xs))$ 个长度 $s$ 的候选增量，最后每个余段在 $x$ 变量长度 $O(1)$。各层共 $O(\log X)$，Cauchy–Schwarz 再付一次对数，得到
$$\int_{X/2}^{3X}\sup_{0\le v\le H}|Q(x+v)-Q(x)|^2 dx\ll X^{2\Theta}H\ell^4.$$
替换回 $\vartheta$ 时，$p^j$、$j\ge2$ 的短窗总数加权不超过 $O((1+H/\sqrt X)\ell^2)$，平方积分被 $O(XH\ell^4)$ 控制。故每个 $h$ 的原归一范数 $\ll X^\Theta\ell^2/\sqrt N$。乘 $O(1/h)$ 后求和，再沿 $X^\Theta$ 几何求和，即得所给上界。特别在 RH 下取 $Y=o(N/\ell^6)$ 即得趋零。该估计按重数使用单位箱计数，允许 $\Theta$ 不在任何一个零点取到。这里使用的短区间界已在上面直接推出，不假设未经证明的零点密度加强。经典 Selberg 积分文献与本项目此前使用的范围可对照下列来源。[Languasco–Zaccagnini，式 (5) 与引理 2](https://arxiv.org/abs/1206.0252) · [第52轮显式公式和分箱](../fiftysecond/carry.md) · [第78轮混合实部的局部二次收敛](../seventyeighth/edge.md)

## 3. 从两次整数读数恢复素数区间余项

固定 $C>6$，$B_N=\sup_{2\le y\le N/(\log N)^C} B(N,y)$。**只观察二的幂 $N$，RH 等价于后两种增长条件，分别为 $B_N=o(1)$、$B_N=O((\log N)^A)$ 对某个固定 $A\ge0$。** 还有无条件指数
$$\limsup_{N=2^j\to\infty}\frac{\log(1+B_N)}{\log N}=\Theta-1/2.$$

对每个大 $Y$ 取二幂 $N\asymp_C Y(\log Y)^C$ 使 $N/(\log N)^C\ge 2Y$。把任一 $[Y,Y']\subset[Y,2Y]$ 的整数区间切成至多 $O(N/Y)$ 段 $(x,z]$，段长至多 $Y^2/(16N)$，允许最后的短段。$\{n/x\}\in[1/8,3/8]$ 在 $N\le n<2N$ 占正比例，因为 $x$ 为整数，$N/x\to\infty$。同时 $0\le n/x-n/t\le1/8$ 对所有 $x\le t\le z$。故这些 $n$ 上 $w(n/t)$ 恒为 $-1/2$，两个窗口误差之差严格等于
$$-\tfrac12[\vartheta(z)-\vartheta(x)-(z-x)]+\tfrac12\sum_{x<p\le z}\log p/p.$$
还可同时取 $\{n/x\}\in[5/8,7/8]$ 的另一批整数，其窗口差值恰为 $+[\vartheta(z)-\vartheta(x)-(z-x)]/2$ 加同一加权中心。任选各批一件，取正批读值减负批读值即精确给出素数计数余项，中心逐项消去。仅用负批时，最后的和 $O(1)$ 由 Chebyshev 界给出。两个误差的原范数之和至多 $2B_N$，该常数值须为 $O(\sqrt N B_N)$。所有子段相加，再把此前的几何尺度加上，可知，$B_N\ll N^{b+\epsilon}$ 对每个 $\epsilon>0$ 最终成立，蕴涵 $\vartheta(Y)-Y=O_\epsilon(Y^{1/2+b+\epsilon})$。用 $\psi-\vartheta=O(\sqrt Y\log^2Y)$ 及 $-\zeta'/\zeta$ 的 Mellin 表达，得到 $\Theta\le1/2+b$。上节无条件正向界给相反方向的指数不等式，故得所示等号。若 $B_N\ll(\log N)^A$，更得到 $O(\sqrt Y(\log Y)^{3C/2+A})$ 的素数计数余项。当 $Y=N^\theta$、$3/4<\theta<1$，同一推理给“该范围内一致多对数逼近”蕴涵 $\Theta\le3/(2\theta)-1$。

如果允许**全部整数起点**，可以把 $B_N$ 换成单一确定日程 $B(N,y(N))$，$y(N)=\lfloor N/(\log N)^C\rfloor$。函数最终每步增零或一。为每个截点取首次做到 $y(N_x)=x$ 的 $N_x$。若 $z-x\le Y^2/(100N_x)$ 则 $|N_z-N_x|\ll_C(Y+\log^C Y)=o(N_x)$，从导数 $\asymp(\log N)^{-C}$ 即得。所以在两个原块的交叠上仍有正比例同号相位，可在共同整数上取误差之差。上述指数和 RH 等价式逐字成立。这种只验单日程的加强并不覆盖同时稀疏化到二幂起点的情形。

**一个截点配稀疏起点。** 更强地，对任意固定实数 $d\ge1$，仅用 $N_j=\lfloor j^d\rfloor$ 和 $y_j=\lfloor N_j/(\log N_j)^C\rfloor$，同样有
$$\limsup_{j\to\infty}\frac{\log(1+B(N_j,y_j))}{\log N_j}=\Theta-1/2.$$
在这个单日程上，某固定多对数上界、范数趋零、RH 三者等价。证明要控制已采截点之间没有直接读数的部分。

在所有 $y_j\asymp Y$ 中，起点满足 $N_j\asymp_C Y(\log Y)^C$。由中值定理，相邻截点的最大空隙 $G\ll_{C,d}1+Y^{1-1/d}(\log Y)^{O(1)}$。取 $H_0=c_C Y/(\log Y)^C$，其中 $c_C>0$ 足够小以令 $H_0\le Y^2/(100N_j)$。有 $G=o(H_0)$。从一个已采点贪心跳到距离不超过 $H_0$ 的最后一个已采点，尾段外每次至少推进 $H_0/2$。每个倍增尺度只需 $O_C((\log Y)^C)$ 段。段的两端起点 $N_j,N_k$ 相差 $O_C((H_0+1)(\log Y)^C)=O_C(Y)=o(N_j)$，这一步对真实日程 $N/(\log N)^C$ 求导即得，不需要在相邻 $N_j$ 之间额外作测量。故公共整数块保持正比例的两批冻结相位。若观测的上极限为 $b$，则加总各尺度后，每个已采端点 $z\asymp Y$ 上的 $|\vartheta(z)-z|\ll_\epsilon Y^{1/2+b+\epsilon}$。这里各尺度可依次取其第一个已采点为分界，相邻尺度直接从上一尺度的末端继续。

置 $E(x)=\vartheta(x)-x$，对于 $x\in[Y,2Y]$ 取第一个已采 $z\ge x$，$z-x\le G$（必要时把统计空隙的尺度放宽至 $3Y$）。把第二节无条件短区间最大均方用于 $H=\max(1,G)$，再用 Cauchy–Schwarz，得到
$$\frac1Y\int_Y^{2Y}|E(x)|dx
  \ll_\epsilon Y^{1/2+b+\epsilon}+Y^{\Theta-1/(2d)+\epsilon}.$$
在 $\Re s>\max(1/2+b,\Theta-1/(2d))$，$\int_1^\infty E(x)x^{-s-1}dx$ 于是按倍增块绝对收敛。高次素幂的 Mellin 贡献在 $\Re s>1/2$ 全纯。故 $-\zeta'/\zeta$ 的非平凡零点必须满足 $\Theta\le\max(1/2+b,\Theta-1/(2d))$。固定有限 $d$ 给第二项严格小于 $\Theta$，必有 $\Theta\le1/2+b$。正向估计给反不等式，RH 下对该日程给趋零。平方数采样还可直接用单调性夹住两采样间的计数，因为这时 $G=O(\sqrt Y)$。对一般固定次幂，上面的短窗均方保住全指数。单取二幂起点且只给一个截点时，相邻截点相距与 $Y$ 同阶，两种补点论证都不适用。

## 4. 固定阶的临界点与相邻截窗

取 $V_0=w$，$V_j'=V_{j-1}$ 且 $V_j$ 一周期均值零。傅里叶系数对 $h\ne0$ 为 $\widehat V_j(h)=((-1)^h-1)/(2\pi i h)^{j+1}$。端点值以实际进位为准。积分中有限跳点无影响，所有 $j\ge1$ 的 $V_j$ 连续。重复分部积分于 $I_y=n\int_{n/y}^\infty w(s)s^{-2}ds$ 得
$$I_y(n)=-\sum_{i=1}^j i!\,y^{i+1}n^{-i}V_i(n/y)+O_j(y^{j+2}n^{-j-1}).$$
故在 RH 下 $\theta_j=(2j+1)/(2j+2)$、$y/N^{\theta_j}\to c>0$ 时，去掉前 $j-1$ 阶后，平方范数趋于
$$c^{2j+2}(j!)^2\frac{8(1-2^{-2j-2})\zeta(2j+2)}{(2\pi)^{2j+2}}\frac{1-2^{-2j-1}}{2j+1}.$$
常数在 $j=1,2$ 分别为 $7/4608,31/307200$。余项范数 $O(y^{j+2}N^{-j-3/2})=o(1)$，仍取块内固定整数的格点均值。若 $y/N^{\theta_j}\to0$，去前 $j-1$ 项的残差趋零。固定 $j$ 时若该比值趋于无穷而 $y=o(N/\log^6 N)$，则残差范数与 $y^{j+1}/N^{j+1/2}$ 之比趋于上式取 $c=1$ 后的平方根。后一结论用下一项相对量 $O(y/N)$。

对同一 $n$ 叠加不同固定临界阶的窗口，相位与慢变量 $n/N$ 联合趋于各圆的 Haar 测度与均匀 $dt$ 的乘积。确有非零频率的固定整数向量中最小的 $y_i$ 主导 $\sum h_i/y_i$，几何级数除以 $N$ 后为 $O(y_i/N)$，Abel 求和允许连续慢权，故各波形内积消失。同阶邻窗有保留相位相关。若 $y'-y\sim s y^2/N$（更一般 $N(y'-y)/y^2\to s$），则 $n/y'-n/y\to-s(n/N)$ 一致。两个临界残差的内积趋于
$$(j!)^2c^{2j+2}\int_1^2 t^{-2j-2}\int_0^1 V_j(u)V_j(u-st)\,du\,dt.$$
$s=0$ 恢复能量常数。相关函数由奇谐波的平方傅里叶系数完全决定。明确地，记 $B_k(u)$ 为 Bernoulli 多项式。由其 Fourier 级数，内层相位协方差在位移 $v$ 的值为
$$\frac{2(-1)^{j+1}}{(2j+2)!}\left[B_{2j+2}(\{v+1/2\})-B_{2j+2}(\{v\})\right].$$
计算两窗口的内积之前，各自已扣去其对应相位的全部较低阶校正。[NIST DLMF，Bernoulli 多项式的 Fourier 级数](https://dlmf.nist.gov/24.8)

对 $y'-y=o(y)$、$N|y'-y|/y^2\to\infty$，两相位也联合均匀。若两个整数频率和非零则原 $1/y$ 主导，若相消则频率为 $\asymp|y'-y|/y^2$，两者在整数块内都绕过无穷多周期。

## 5. 原整数端点和独立有限复算

取 $N=32768,Y=2048$，从 $[Y,2Y]$ 中选67个整数小区间，含一个截短末段。对两组相位的每个整数，程序先用 $\lfloor2n/x\rfloor=\lfloor2n/z\rfloor$ 检查整个实区间上的进位符号，再逐个调用区间内的素数进位。负批为548,975个具名位置、554,759次素数进位，正批为548,813个位置、558,222次素数进位。在 $(2079,2087]$ 上，$n=33524$ 与 $32768$ 分属两批，差读数精确给出 $\log2081+\log2083+\log2087-8$，包括右端素数。这里在形式基 $1,\log p$ 上逐个核验系数，全程使用整数和分数。

在 $C=7$ 的单截点日程上另取 $d=1,2,3,4,8$，从 $j=10^{32}+7$ 出发，逐例精确找出贪心最远下标，核两端块的交叠和两种相位代表。每个截点的取整均由对数的上下有理包围确定。

对波形另取 $j=1,\ldots,8$，由 $V_j(u)=[B_{j+1}(\{u\})-B_{j+1}(\{u+1/2\})]/(j+1)!$ 在分界点 $0,1/2,v,v+1/2\pmod1$ 切开，再把两个多项式乘积逐项积分。六个有理位移的相关都与 Fourier 公式精确相等。前三个临界均方常数分别为 $7/4608,31/307200,2159/128450560$。

还从原地板函数独立取初值、按各素数跳点推进全部整数，考察第二临界 $y=\lfloor N^{5/6}\rfloor$ 下扣除第一波后的原始能量。下面的两列在同一块、同一截点求和，采用36位十进制算术后保留12位小数。最大块处普通素数能量仍有明显的有限尺寸差异。

| $N$ | $y$ | $\|L_y+y^2V_1(n/y)/n\|_N^2$ | 单取第二波的平方范数 |
|---:|---:|---:|---:|
| 4096 | 1024 | 0.058711870550 | 0.000099782490 |
| 16384 | 3250 | 0.073725852345 | 0.000103963673 |
| 65536 | 10321 | 0.053877148830 | 0.000095418595 |

标准库命令为 `python3 carry_check.py | cmp - carry_checked.json`。也可运行 `python3 carry_check.py --native-dir /path/to/frozen/src/enterprise_math | cmp - carry_checked.json`。第二种方式先核对冻结源码摘要，然后用原函数 `carry_bit`、`primes_up_to` 执行同一组检查。两种方式已实际运行，所得 JSON 逐字节相同。素数表、单步进位与半区相位均为公开的普通数论计算。[冻结原码](https://github.com/awdawmip/enterprise-math/blob/437d4d595f1495d3a0486b3c06e9e2b14567db82/src/enterprise_math/brc_count_centered_carry.py) · [复算程序](carry_check.py) · [精确结果及有限数值](carry_checked.json)
