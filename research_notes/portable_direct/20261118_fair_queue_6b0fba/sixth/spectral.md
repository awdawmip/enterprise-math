# 有限谱的整系数分解：从结式到全部 Smith 不变量

问题来自 1159 的谱算术任务。冻结稿已确定原始分母因子的两两结式，并在两组互素因子上建立了整系数中国剩余定理。若同一素数的不同层同时出现，分解在有理数上仍成立，在整数上却有有限余核。下面给出其全部循环因子，并纠正将两张互补谱图之间的坐标替换理解为同一数域自同构的说法。[任务书](https://github.com/awdawmip/enterprise-math/blob/b3a25442cd5ee1fafb037d2c2052f8fbb1da3ec1/research_tasks/EMW59A_1159_SPECTRAL_ARITHMETIC_20260909.md) · [冻结结式](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/SPECTRAL_CYCLOTOMIC_NATIVE_RESULTANT_LAW_20260904.md) · [已有整系数 CRT](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/SPECTRAL_GCD_CRT_UNIT_RESULTANT_20260905.md)

## 分解映射的余核

置 $t=u-2$，令 $Q_1=1,Q_2=t,Q_{m+1}=tQ_m-Q_{m-1}$。以冻结的实谱量子化编号，第 $m$ 层第 $k$ 个根的原始分母为 $m/\gcd(k,m)$。用 $\Psi_d$ 表示原始分母 $d$ 的首一因子。于是 $Q_M=\prod_{1<d\mid M}\Psi_d$、$\deg\Psi_d=\varphi(d)$；按分母归纳作首一除法即得整系数。

取任意有限非空、无重复的指标集 $I\subset\{2,3,\ldots\}$。记 $A_d=\mathbb Z[t]/(\Psi_d)$。考察同时取余映射

$$
\mathbb Z[t]\big/\big(\prod_{d\in I}\Psi_d\big)\ \longrightarrow\ \prod_{d\in I}A_d .
$$

此映射单射，源和靶是同秩的自由阿贝尔群。固定一个素数 $p$，将 $I$ 按去掉所有 $p$ 因子的部分分组。在每一组内从小到大排列指标 $d_1<\cdots<d_b$。则余核的 $p$ 主部分恰为对各组取直和的

$$
\bigoplus_{i=1}^{b-1}(\mathbb Z/p^{\,b-i}\mathbb Z)^{\varphi(d_i)}.
$$

这一公式只数每个指标之后实际选取的层。即使选择 $d$ 和 $dp^7$ 而省去中间六层，这一对仍只产生指数为 $p$ 的循环因子。

**完整长度的闭式。** 若 $I$ 为 $M$ 的全部大于 1 的约数，写 $M=p^a m$，$p\nmid m$。对 $1\le h\le a$，循环因子 $\mathbb Z/p^h\mathbb Z$ 的个数为

$$m\varphi(p^{a-h})-\mathbf1_{h=a}.$$

把 $M-1$ 个 Smith 因子从大到小列为 $D_1,\ldots,D_{M-1}$，并令 $L(n)=\operatorname{lcm}(1,\ldots,n)$。则所有素数可合并成一条整式：

$$\boxed{D_k=\gcd\!\left(M,L\!\left(\left\lfloor\frac M{k+1}\right\rfloor\right)\right)},\qquad 1\le k<M.$$

事实上当 $1\le h\le a$ 时，指数至少为 $h$ 的循环因子有 $m\sum_{j=0}^{a-h}\varphi(p^j)-1=M/p^h-1$ 个。因此 $p^h\mid D_k$ 当且仅当 $p^h\mid M$ 且 $(k+1)p^h\le M$。两整格的指数为 $\prod_{p^a\parallel M}p^{(M/p^a)(p^a-1)/(p-1)-a}$。例 $M=12$ 的非平凡 Smith 因子按降序为 $12,12,6,2,2$，其积为 3456。不存在任何素因子时取空积，$M=1$ 的余核为零。

## 首一递推和结式的独立核对

在自由二次代数中以可逆符号 $z$ 写 $x=z+z^{-1}$。由于 $z$ 在此为不定元，整系数多项式可在 Laurent 环中逐系数检验。迹递推 $C_0=2,C_1=x,C_{n+1}=xC_n-C_{n-1}$ 给 $C_n(x)=z^n+z^{-n}$。故 $R_n(u)=2-C_n(2-u)$ 满足 $R_{mn}=R_m\circ R_n$；同样的差式 $U_{n-1}(x/2)=(z^n-z^{-n})/(z-z^{-1})$ 给出 $H_{mn}(u)=H_m(u)H_n(R_m(u))$，其中 $H_m=U_{m-1}((2-u)/2)/m$。这里没有使用分圆结式或单位根分解。

记 $P_n$ 为原始根的乘积，使用未平移的正谱变量 $u$。在零点处取全谱行列式的绝对值得 $m=\prod_{1<d\mid m}P_d$，故 $P_n=p$ 当 $n$ 为 $p$ 的正整数次幂，否则 $P_n=1$。每层 $p^j$ 恰有 $\varphi(p^j)$ 个原始根，互补 $u\mapsto4-u$ 保持该层。用冻结的内部正弦 $S$ 及其第一个正零点 $\tau$，倍角关系和互补置换给
$\prod_{(k,n)=1,\ 1\le k<n}S(k\tau/n)=P_n/2^{\varphi(n)}$。

**一次 Möbius 反演即可覆盖整除与不整除两种情形。** 总取较大的指标 $n$ 固定，$1<m<n$。对每个 $d\mid m$ 都有 $n\nmid d$，故 $|\operatorname{Res}(\Psi_n,Q_d)|$ 永远非零。令 $v=n/\gcd(n,d)$。由行列式在第 $k$ 模态的绝对值为 $|S(dk\tau/n)|/S(k\tau/n)$，将互素剩余类均匀投到模 $v$ 的单位群，得

$$|\operatorname{Res}(\Psi_n,Q_d)|=P_v^{\varphi(n)/\varphi(v)}/P_n.$$

取各 $d\mid m$ 的 $\mu(m/d)$ 次幂之积。分母完全消去。若要产生素数 $p$ 的赋值，写 $n=p^ac$、$p\nmid c$，必要条件为 $c\mid d$ 且 $n/\gcd(n,d)$ 是 $p$ 的正次幂。若 $c\nmid m$ 无贡献；若 $m$ 在某个非 $p$ 素位比 $c$ 多一幂或更多，该素位的两个 Möbius 项大小相同、符号相反。剩余只可能 $m=cp^j,\ 0\le j<a$。两个可能的 $p$ 位权重给出 $\varphi(c)(p^j-\mathbf1_{j>0}p^{j-1})=\varphi(m)$。综上，若 $n/m=p^k$ 为正次素幂，则两因子结式的绝对值为 $p^{\varphi(m)}$；其余均为 1。整个计算始终使用 $d<n$ 的有限乘积。

判别式也可从同一份资料独立读出。在全体原始 $m$ 模态上，导数绝对值为 $m/(2S(k\tau/m)^2)$。全谱的导数积给出 $|\operatorname{disc} Q_m|=2^{m-1}m^{m-3}$。原始模态的导数积为 $(2m)^{\varphi(m)}/P_m^2$，再除去所有真约数原始因子的交叉结式，即得

$$|\operatorname{disc}\Psi_m|
=\frac{(2m)^{\varphi(m)}}{P_m\prod_{p\mid m}p^{\varphi(m)/(p-1)}}.$$

其中对每个 $p^a\parallel m$，真约数 $m/p^j>1$ 贡献的总指数为 $\varphi(m)/(p-1)-\mathbf1_{m=p^a}$。

## 为什么整系数余核只取决于同素数链

在特征 $p$ 令 $t=z+z^{-1}$，将 $z^m-z^{-m}$ 取 $p$ 次幂并约去 $z-z^{-1}$，得到 $Q_{mp}=E_p Q_m^p$，其中 $E_2=t$，对奇数 $p$ 有 $E_p=(t^2-4)^{(p-1)/2}$。对 $c>1,\ p\nmid c$ 在 $c$ 的约数上作乘法 Möbius 反演。与 $c$ 无关的 $E_p$ 因子消去，故

$$\overline{\Psi}_{cp^a}=\overline{\Psi}_c^{\,\varphi(p^a)},\qquad
\overline{\Psi}_{p^a}=E_p^{p^{a-1}}\quad(a\ge1).$$

因此在同一条链上，$i<j$ 时 $\Psi_{d_j}$ 模 $\Psi_{d_i}$ 的每个系数都能被 $p$ 整除。在 $A_{d_i}$ 中写这个元素为 $p v_{ij}$。上节的结式等于乘法行列式的绝对值，给出 $|\det(v_{ij})|=1$，故 $v_{ij}$ 是整系数商环中的单位，即使该商环有零因子也成立。

局部化到 $\mathbb Z_{(p)}$ 后，不同链之间的结式均为单位，故可逐链运算。每链从大到小写作 $f_0,\ldots,f_{b-1}$。源的 Newton 基为 $\{\prod_{j<i}f_j\,t^k:0\le k<\deg f_i\}$，它逐度首一。取余矩阵在第 $i$ 个块列的上方为零，块列内所有项都是 $p^i$ 的倍数，除去 $p^i$ 后对角块为若干单位的乘法。由块下三角性，逐列除后的矩阵在本地环上可逆。于是每块恰贡献 $\deg f_i$ 个 $p^i$。完整长度时按 $p$ 自由部分枚举 $m$ 的约数，用 $\sum_{c\mid m}\varphi(c)=m$，再排除指标 1，便得到闭式。

## 射影谱图的域与坐标

设 $d>2$，$\Omega_d$ 的根是 $v_{k,d}=2-2C(2k\tau/d)$，其中 $C$ 在此表示内部余弦函数，$k$ 取模 $d$ 的单位、按 $\pm1$ 配对。奇数 $d=2b+1$ 的全部半谱由 $U_b((2-u)/2)+U_{b-1}((2-u)/2)$ 给出（统一首项符号）；和角公式给出其根，再按约数归纳即得 $\Omega_d$ 整系数。对奇 $d>1$ 有 $\Psi_d=\Omega_d\Omega_{2d}$，两因子经 $v\mapsto4-v$ 互换。对偶 $m$ 有 $\Omega_{2m}=\Psi_m$。奇 $d>1$ 时，倍角作用保持模 $d$ 的单位群；将全部 $S(2k\tau/d)^2/S(k\tau/d)^2$ 相乘并按 $\pm k$ 配对，可得 $|\Omega_d(4)|=1$。

这些恒等式和上面的判别式说明，$\Omega_d$ 在任何 $p\nmid 2d$ 处模 $p$ 可分。若 $\alpha$ 和 $R_p(\alpha)$ 分属不同首一不可约因子 $f,g$，则 $f$ 整除 $g(R_p)$。但模 $p$ 时 $R_p(v)\equiv v^p$，故 $\bar f\mid\bar g^p$，与可分性矛盾。每个模 $d$ 的单位都有一个与 $2d$ 互素的正奇数代表，其各素因子都满足上述条件。因此一个根所属的不可约因子已包含所有根。全部共轭 $R_j(\alpha)$ 均在 $\mathbf Q(\alpha)$ 内，由组合律和 $\pm$ 配对即得伽罗瓦群 $(\mathbb Z/d)^\times/\{\pm1\}$。对任意整数 $h$，有限旋转矩阵的几何和给出全体剩余类的余弦和在 $d\mid h$ 时为 $d$，否则为 0。按约数反演得到互素类的和 $\sum_{e\mid(d,h)}e\mu(d/e)$；特别地 $\mathrm{Tr}(v_{1,d})=\varphi(d)-\mu(d)$。

**两处边界。** 奇 $d$ 的相等 $K_d=K_{2d}$ 是生成元变换；对这里的每个奇数 $d>1$，在同一数域内都没有把 $\alpha$ 送到 $4-\alpha$ 的有理域自同构。事实上两者分别属于不同的最小多项式。最小例 $d=3$ 时是有理数 3 和 1。相同数域也可能出现在不由该条倍增关系连接的标签间：$K_3=K_4=\mathbf Q$，而三个有理生成元分别见于 $\Omega_3=u-3,\Omega_4=u-2,\Omega_6=u-1$。这些例子不影响原稿的互补多项式恒等式；仅靠倍增关系和次数比较，无法推出所有数域相等情形都已分类。[冻结的谱图与导子稿](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md)

复算从普通整系数幂基直接构造取余矩阵，用 Smith 标准形核对非连续指标集和完整长度。所有 378 个指标对另经独立结式验证。群结构的推导适用于任意有限指标集。[复算程序，需 SymPy](spectral_check.py)
