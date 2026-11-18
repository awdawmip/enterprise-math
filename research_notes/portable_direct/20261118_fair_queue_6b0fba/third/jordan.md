# 原始谱矩的 Jordan 系数与高阶 Dirichlet 分子的不消零高度

任务 `RS-EMW59A-1159-SPECTRAL-ZETA-JORDAN`，不可变发布 `TP2-739DEFE26506D2C975C8`。冻结笔记给出了低阶谱矩、主系数递推和一阶谱矩的 RH 等价命题，并指出高阶分子可能消去分母零点。下面给出每个固定阶的显式高度界，将可能消去的非平凡零点限制在一个有界区域。有限代数、内部相位极限与经典解析延拓分别给出所需的输入。结果为作者推导，待独立审阅。

## 有限矩、正系数与原始分母

取 $(M-1)$ 阶 Dirichlet 三对角阵 $L_M=\operatorname{tridiag}(-1,2,-1)$，设其谱为 $u_{k,M}$，$Z_n(M)=\operatorname{Tr}(L_M^{-n})$。令 $X=M^2$，$H_M(u)=\det(L_M-uI)/M$。冻结行列式给出 $[u^j]H_M=(-1)^je_j(X)$，其中
$$
e_j(X)=\frac{\prod_{a=1}^j(X-a^2)}{(2j+1)!}.
$$
在 $M$ 为整数时，$j\ge M$ 的项自动为零。由 $-uH'_M/H_M=\sum_{n\ge1}Z_n(M)u^n$ 比较形式系数，
$$
Z_n(M)=\sum_{j=1}^{n-1}(-1)^{j-1}e_j Z_{n-j}+(-1)^{n-1}n e_n.
$$
因此每一个 $Z_n$ 都是 $X$ 的至多 $n$ 次有理多项式，$X=1$ 时为零。

精确的次数及系数可由第二种表示读出。采用冻结的内部形式相位 $S,C$，$F(t)=S(\sqrt t)/\sqrt t$，$U(t)=2-2C(\sqrt t)$。定义 $-tF'/F=\sum_{r\ge1}\beta_rt^r$，$T(u)=U^{-1}(u)$ 表示形式复合逆。有限续行列式的倍角关系给出 $H_M(U(t))=F(M^2t)/F(t)$。消去三角命名后的精确系数公式为
$$
Z_n(M)=\sum_{r=1}^n A_{n,r}(X^r-1),\qquad
A_{n,r}=\frac nr\,\beta_r [u^n]T(u)^r>0.
$$
这里 $F(t)=\sum_{j\ge0}(-1)^jt^j/(2j+1)!$ 满足 $4tF''+6F'+F=0$。比较其形式对数导数给出
$$
\beta_1=\tfrac16,\qquad
\beta_n=\frac2{2n+1}\sum_{j=1}^{n-1}\beta_j\beta_{n-j}.
$$
由 $C^2+S^2=1$ 得 $u(4-u)(T')^2=4T$，再从系数等式或形式求导得到 $u(4-u)T''+(2-u)T'=2$。所以 $T(u)=\sum_{j\ge1}c_j u^j$，$c_1=1$ 且 $c_{j+1}=j^2 c_j/[(j+1)(4j+2)]>0$。这些是形式系数运算，直接给出 $A_{n,n}=\beta_n>0$，因而次数恰为 $n$。若使用 Bernoulli 记号 $v/(e^v-1)=\sum B_jv^j/j!$，在形式复数扩张中令 $v=2ix$。由 $xC(x)/S(x)=v/(e^v-1)+v/2$ 及 $-x^2 F'(x^2)/F(x^2)=(1-xC(x)/S(x))/2$ 得
$$
\beta_n=(-1)^{n+1}2^{2n-1}B_{2n}/(2n)!.
$$
这个推导只用形式幂级数，未从已知偶 ζ 值反推系数。[冻结有限行列式](https://github.com/awdawmip/enterprise-math/blob/269b1cafac209e42d6770b0aae4a4d8d0a981f8a/research_notes/WALLIS_SINE_DISCRETE_ROTATION_SPECTRAL_PRECISION_THEOREMS_20260903.md) · [原主系数递推](https://github.com/awdawmip/enterprise-math/blob/ad6fbb0a1ac98d63ff99354569ca04c0f601ee50/research_notes/SPECTRAL_RICCATI_RECURRENCE_FOR_EVEN_ZETA_COEFFICIENTS_20260905.md)

对 $d>1$，$P_n(d)=\sum_{1\le k<d,(k,d)=1}u_{k,d}^{-n}$。按 $k/M$ 的真正分母分拆，$Z_n(M)=\sum_{d\mid M}P_n(d)$，约定 $P_n(1)=0$；这里使用下一节冻结量子化给出的 $u_{ak,ad}=u_{k,d}$。Möbius 反演精确给出 $P_n(d)=\sum_{r=1}^n A_{n,r}J_{2r}(d)$，其中 $J_b=\mu*(m\mapsto m^b)$。前三阶多项式依次为 $(X-1)/6$、$(2X^2+5X-7)/180$、$(8X^3+21X^2+42X-71)/7560$。后三阶可逐项使用上式转换成 Jordan 系数：
$$
\begin{aligned}
Z_4&=(24X^4+80X^3+147X^2+270X-521)/226800,\\
Z_5&=(32X^5+132X^4+286X^3+451X^2+792X-1693)/2993760,\\
Z_6&=(44224X^6+218400X^5+558558X^4+993850X^3+1438437X^2+2457000X-5710469)/40864824000.
\end{aligned}
$$

## 有限尾界与偶 ζ

内部相位来源以 $S$ 的第一个正零点定义 $\tau$。其续行列式恒等式及 $S$ 的半周期弦界给出 $\rho_{k,M}=M\sqrt{u_{k,M}}=2M S(k\tau/(2M))\ge 2k$，对每个固定 $k$ 有 $\rho_{k,M}\to k\tau$。具体地，$S''=-S\le0$ 及 $S(0)=0,S(\tau/2)=1$ 给出 $S(y)\ge2y/\tau$；$S(y)/y\to1$ 给出逐模态收敛。因此 $K\ge1$ 时
$$
\sum_{K<k<M}\rho_{k,M}^{-2n}\le\frac{K^{1-2n}}{2^{2n}(2n-1)}.
$$
先对有限前缀取极限，再令 $K$ 增大，得 $\lim_{M\to\infty} M^{-2n}Z_n(M)=\tau^{-2n}\zeta(2n)=\beta_n$。此处没有使用 Euler 乘积。[内部相位量子化与半周期界](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md)

## 高阶分子的不消零高度定理

令 $D_n(z)=\sum_{d\ge2}P_n(d)d^{-z}$，$N_n(z)=\sum_{r=1}^n A_{n,r}\zeta(z-2r)$。绝对收敛横坐标恰为 $2n+1$：Jordan 多项式给出 $P_n(d)=O_n(d^{2n})$；$k=1$ 总与 $d$ 互素，且 $d\sqrt{u_{1,d}}\le\tau$，故 $P_n(d)\ge d^{2n}/\tau^{2n}$。在绝对收敛域，由各个 Jordan 函数的 Dirichlet 卷积有
$$
D_n(z)=N_n(z)/\zeta(z)-\sum_{r=1}^n A_{n,r}.
$$
每个 $\zeta(z-2r)/\zeta(z)$ 有 Euler 乘积。和式是有限线性组合，毋须假定它本身可乘。

**高度证书。** 对 $n\ge2$，若 $T>0$ 满足下式，则 $N_n(z)$ 在 $0<\Re z<1$、$|\Im z|\ge T$ 上处处非零：
$$
 \frac{11}{6}\sum_{r=1}^{n-1}\frac{A_{n,r}}{A_{n,n}}(40/T^2)^{n-r}<1.
$$
因此在此高度以上，每个非平凡 ζ 零点在 $D_n$ 中产生一个同重数极点。每个固定阶最多只须另行检查有限多个低处零点。对 $n=2,3,4,5,6,7,8$，使这份充分证书成立的最小正整数高度依次为 $14,16,18,20,22,24,25$；此处没有声称这些高度是分子实际零点的最优界。

证明使用经典 ζ 函数方程，仅作用于解析延拓后的 Dirichlet 变换。在上述带内，$\zeta(z-2n)\ne0$。对 $r<n$ 取两式的比，
$$
\frac{\zeta(z-2r)}{\zeta(z-2n)}
=\frac{(-1)^{n-r}(2\pi)^{2(n-r)}}{\prod_{j=2r+1}^{2n}(j-z)}
 \frac{\zeta(1-z+2r)}{\zeta(1-z+2n)} .
$$
最后一个比由两个绝对收敛级数（ζ 与 $1/\zeta$）的绝对值界控制为 $\zeta(2r)\zeta(2n)\le\zeta(2)\zeta(4)<(5/3)(11/10)=11/6$。这两个有理上界可分别取前五项、前三项并用积分估尾。用 $|j-z|\ge|\Im z|$ 和 $(2\pi)^2<40$ 即得余下各项的绝对值总和严格小于主项，证明分子不为零。一阶本来就有 $D_1=(\zeta(z-2)/\zeta(z)-1)/6$，且整个临界带内分子无零，故 RH 等价于其带内所有极点实部为 $1/2$。上面的新证书控制高阶读数的分子消去，却没有限定任何极点的实部。[冻结 Dirichlet 读数及原待查范围](https://github.com/awdawmip/enterprise-math/blob/6bbb4454f9f2ba3cb23409846ebf414ed1dc4028/research_notes/PRIMITIVE_SPECTRAL_DIRICHLET_SERIES_AND_RH_READOUT_20260905.md) · [经典 ζ 函数方程](https://dlmf.nist.gov/25.4)

## 已发表低高度零点计数与整体 RH 判据

Platt 计算的已验证零点表给出前三个正虚部 $14.1347251417\ldots,\ 21.0220396387\ldots,\ 25.0108575801\ldots$；其数据说明记录了 $2^{-102}$ 的绝对精度和检验列表完备性的严格 Turing 方法。故 $0<|\Im z|\le14$ 内没有非平凡零点，截止高度 25 的正虚部零点恰有前两个。Platt 和 Trudgian 的定理 1 另证 $0<\Im z\le 3\,000\,175\,332\,800$ 的全部 ζ 零点实部均为 $1/2$；共轭对称给出负半平面。开区间 $0<z<1$ 上的交错 eta 级数严格为正且 $1-2^{1-z}<0$，故实轴上也没有遗漏的非平凡零点。这里只调用已验证的低高度结果。[Platt 的零点表](https://www.lmfdb.org/L/download_zeros/1-1-1.1-r0-0-0) · [数据来源、误差和完备性](https://www.lmfdb.org/zeros/zeta/Source) · [Platt–Trudgian，定理 1](https://doi.org/10.1112/blms.12460)

**二阶推论。** 临界开带内 $D_2$ 的全部极点与全部非平凡 ζ 零点逐点、逐重数一致。每个零点均高于二阶的不消零高度 14；反向地，带内 $N_2$ 全纯，极点只可能来自分母。因此 RH 等价于 $D_2$ 在临界开带内的每个极点都位于临界线上。

**三至八阶推论。** 对每一个固定的 $3\le n\le8$，同样有
$$
\mathrm{RH}\quad\Longleftrightarrow\quad
\text{$D_n$ 在 $0<\Re z<1$ 的每个极点均有 $\Re z=1/2$}.
$$
若 RH 成立，极点只能落在分母零点所在的线上。若有离线零点，它的绝对高度必大于 25；上述高度证书在这个范围对每一阶均已适用，所以它在每个 $D_n$ 中均显为同重离线极点。此推论容许低处临界线上的分母零点在个别高阶读数中被约去，并未作逐点约消的数值判断。更一般地，对任何固定阶，只要其不消零高度落入已有严密的临界线验证范围，同一论证即给出相应等价判据。这些等价式不决定离线零点是否存在。

**精确核验。** 同目录 `jordan_check.py` 先由有限行列式生成多项式，再独立以形式相位逆级数核对一至八阶全部 Jordan 系数与 Bernoulli 主项；以 $M=2,\ldots,14$ 逐阶直接计算三对角逆矩阵幂迹，104 项相符；以 $d=2,\ldots,42$ 独立按约数反演与 Jordan 展开比较，328 项相符。所有高度仅用有理不等式逐个复算，没有用有限零点表替代解析证明。
