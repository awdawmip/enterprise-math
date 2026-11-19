# Dirichlet 路径谱的整闭包、全部 Smith 因子与最小投影分母

取 $M-1$ 个内点的 Dirichlet 路径矩阵 $H_M$，对角元为 2，相邻元为 $-1$。下文 $\lambda$ 就是冻结原稿的正谱坐标 $u$；平移变量是 $t=\lambda-2$。置 $N=2M$，$S_M=\mathbb Z[H_M]$，在其有理代数中取整闭包 $\widetilde S_M$。对 $M\ge2$，将 $\widetilde S_M/S_M$ 的 $M-1$ 个 Smith 因子按从大到小排列，包含 1。则
$$
 \boxed{D_k=\gcd\!\left(N,\operatorname{lcm}\left(1,\ldots,
 \left\lfloor\frac N{2k+1}\right\rfloor\right)\right)},\qquad 1\le k<M . \tag{1}
$$
对每个 $e\mid N,\ e>2$，令 $P_e$ 是投影到精确阶 $e$ 谱分量的有理矩阵。使 $b_eP_e$ 逐项为整数的最小正数为
$$
 \boxed{b_e=\frac Ne\prod_{\substack{p\mid e\ \mathrm{prime}\\e/p>2}}p.} \tag{2}
$$
例如 $M=6$ 的非平凡因子为 $12,2$，四个分量 $e=3,4,6,12$ 的最小投影分母分别为 $4,3,4,6$。$M=1$ 是零维空谱，两个列表均空；$M=2$ 只有整数分量 $e=4$，Smith 因子和投影分母都为 1。

冻结的谱算术任务从连分行列式和实谱量子化出发。第 6 轮求得按照原始分母 $d\mid M$ 分块的整系数余核；奇数 $d>1$ 的每个块仍有两片。第 15 轮求得单个奇数块分片后的 2 导子。本篇求由**原矩阵直接同时投影到全部实分量**的余核、各分量导子以及这两步能否分裂。先用整数递推与有限多项式运算证明取余矩阵的因子，随后识别极大整数环。[任务书](https://github.com/awdawmip/enterprise-math/blob/b3a25442cd5ee1fafb037d2c2052f8fbb1da3ec1/research_tasks/EMW59A_1159_SPECTRAL_ARITHMETIC_20260909.md) · [原结式研究](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/SPECTRAL_CYCLOTOMIC_NATIVE_RESULTANT_LAW_20260904.md) · [第 6 轮](../sixth/spectral.md) · [第 15 轮](../fifteenth/cyclotomic.md)

## 一、正谱坐标与最终分量

$Q_1=1$，$Q_2=\lambda-2$，$Q_{M+1}=(\lambda-2)Q_M-Q_{M-1}$，所以 $Q_M=\det(\lambda I-H_M)$。$e_1,H_Me_1,\ldots,H_M^{M-2}e_1$ 逐列组成整基，因第 $j+1$ 列支撑在前 $j+1$ 项且末项是 $(-1)^j$。特别地，$S_M=\mathbb Z[\lambda]/Q_M$。任何与 $H_M$ 交换的有理矩阵 $T$ 若 $Te_1$ 整，则由该基可知 $T$ 是 $H_M$ 的某个整系数多项式。这使 (2) 同时刻画多项式分量与原始矩阵的最小整倍。

在 Laurent 变量中写 $\lambda=2-z-z^{-1}$。连分递推乘 $z-z^{-1}$ 后给 $(-1)^{M-1}(z^M-z^{-M})$。因此 $z^N=1$ 中仅去掉 $z=\pm1$ 两个端点，每一其余根与其倒数合并。令 $F_e(z)$ 为 $z^e-1$ 按约数递除所得的恰阶首一因子。按全部复根的精确阶分组和首一长除，得到 $F_e\in\mathbb Z[z]$。$e>2$ 时它互反，$h_e=\varphi(e)/2$，于是
$$
 F_e(z)=(-1)^{h_e}z^{h_e}\Omega_e(2-z-z^{-1}),\qquad
 Q_M(\lambda)=\prod_{\substack{e\mid N\\e>2}}\Omega_e(\lambda). \tag{3}
$$
确实 $z^{-h_e}F_e(z)$ 是 $z+z^{-1}$ 的整系数多项式，由 $z^k+z^{-k}$ 的二阶递推即得。符号 $(-1)^{h_e}$ 确保 $\Omega_e$ 在正谱坐标中首一。这些恰阶因子也是不可约的。若 $F_e$ 的两个不同首一不可约因子 $P,Q$ 分别含根 $z,z^\ell$，其中 $\ell\nmid e$ 为素数，则 $P(X)\mid Q(X^\ell)$。模 $\ell$ 后 $\bar P\mid\bar Q^\ell$，与 $X^e-1$ 可分矛盾。任一与 $e$ 互素的正整数均是此类素数的积，故 $P$ 已含全部恰阶根；(3) 随即给出实因子的不可约性。

原始分母 $d\mid M$ 若为偶数，$\Psi_d=\Omega_{2d}$；若 $d>1$ 为奇数，$\Psi_d=\Omega_d\Omega_{2d}$。例如 $\Omega_3=\lambda-3,\ \Omega_4=\lambda-2,\ \Omega_6=\lambda-1$，即便三者均给有理数域，也保留三个不同谱分量。

## 二、同一素数链中每个后层给一个 $p$

令 $O_i=\mathbb Z[\lambda]/(\Omega_i)$。固定素数 $p$，写指标为 $cp^a$，$p\nmid c$。对 $b\ge1$，
$$
 F_{cp^b}(z)=\frac{F_c(z^{p^b})}{F_c(z^{p^{b-1}})},\qquad
 \overline F_{cp^b}=\overline F_c^{\,\varphi(p^b)}\ \text{于 }\mathbb F_p[z]. \tag{4}
$$
首式由精确阶分组，次式由 Frobenius 和整域消去。$a=0$ 的因子直接是 $F_c$。$F_c$ 模 $p$ 的根均有精确阶 $c$，因为 $z^c-1$ 在该处可分。若两个去 $p$ 因子的指标不同，则它们的实余式模 $p$ 也互素：同一 $\lambda$ 只给二次方程 $z^2-(2-\lambda)z+1=0$ 的一对互逆根，它们阶数相同。此论证容许特征二中的重根。

**局部乘法引理。** 若 $i=cp^a>2,\ j=cp^b>i$，则 $\Omega_j(\lambda_i)=p\times O_i^\times$，其中 $\lambda_i$ 是 $\lambda$ 的剩余类。先证真的有 $p$ 整除。把 $O_i$ 放入
$$
 O_i[z]/(z^2-(2-\lambda_i)z+1)\simeq\mathbb Z[z]/(F_i).
$$
两边由 (3) 及 $z^{-1}=2-\lambda_i-z$ 互相给出。左边在 $O_i$ 上有自由基 $1,z$，所以模 $p$ 后 $O_i/pO_i$ 仍单射。由 (4)，$\overline F_i\mid\overline F_j$，而 $z$ 是单位，故实余式已在 $O_i/pO_i$ 中为零。这里没有除以 2，$p=2$ 与去 $p$ 因子后 $c=1,2$ 的边界均适用。

再求商元素的单位性。在任意恰阶 $i$ 的根 $z$ 处，(4) 首式的分子、分母都有单零。求导取商得到
$$
 F_j(z)=p z^{p^b-p^{b-1}}
 \frac{F_c'(z^{p^b})}{F_c'(z^{p^{b-1}})} .
$$
当 $z$ 遍历恰阶 $i$ 全部根时，分子和分母的导数自变量按相同重数遍历恰阶 $c$ 的根。故 $\left|\prod F_j(z)\right|=p^{\varphi(i)}$。合并互逆配对，得到 $\Omega_j(\lambda_i)$ 的乘法行列式绝对值 $p^{h_i}$。先前的整除性允许将该元素除以 $p$，所得乘法行列式为 $\pm1$，故为单位。只知道两个块的结式并不足以完成第一步。

## 三、整基消元与 Smith 层

局部化到 $\mathbb Z_{(p)}$，不同 $c$ 的链由互素取余拆开。同一链按指标由大到小排列 $f_0,f_1,\ldots,f_{s-1}$。在源取首一、度数连续的 Newton 基
$$
 \left(\prod_{j<l} f_j\right)\lambda^h,\qquad
       0\le h<\deg f_l,\quad 0\le l<s.
$$
第 $l$ 个块列在上方为零，其余各行的 $l$ 个后层因子各贡献一个 $p$，故整块列可提出 $p^l$。在对角的第 $l$ 个商环中，提出该幂后得到单位乘法矩阵。逐块列提出 $p^l$ 后成为可逆块下三角矩阵。因此第 $l$ 块准确贡献 $\deg f_l$ 个指数 $l$。这是对整格的基变换，给出了各层而不仅是它们的总和。

完整约数集下，第 $e$ 块有至少 $h$ 个更高层正好等价于 $ep^h\mid N$。对 $p^h\mid N$，指数至少为 $h$ 的个数为
$$
 \tfrac12\sum_{\substack{e\mid N/p^h\\e>2}}\varphi(e)
  =\left\lfloor\frac{N/p^h-1}{2}\right\rfloor, \tag{5}
$$
而 $p^h\nmid N$ 时为零。奇数 $N/p^h$ 只减去指标 1；偶数还要减去指标 2。因此 $p^h\mid D_k$ 等价于 $p^h\mid N$ 且 $(2k+1)p^h\le N$，即 (1)。

**与前两次分块的关系。** 令 $M=2^a m$，$m$ 奇，在 $S_M\subseteq B=\prod_{1<d\mid M}\mathbb Z[\lambda]/\Psi_d\subseteq\widetilde S_M$ 之间有自然阿贝尔群短正合列。由奇分母的两片粘合，$\widetilde S_M/B=(\mathbb Z/2)^{(m-1)/2}$。奇素数处 $B/S_M$ 与总余核相同。$a\ge1$ 时，$B/S_M$ 的 2 主部在 $1\le h\le a$ 有 $M/2^h-1$ 个长度至少 $h$ 的因子，由 (5) 这一部分在总余核中计数不动，但总余核另有 $(m-1)/2$ 个长度达到 $a+1$。故在不变量的多重集里恰有这么多个最高 $2^a$ 伸长为 $2^{a+1}$。当且仅当 $a=0$ 或 $m=1$ 时，这个阿贝尔群扩张分裂；前者两端阶互素，后者末项为零。在 $M=6$，旧余核为 $(6,2)$，单独归一化的商为 $(2)$，合起来是 $(12,2)$。这些不变量无需选定某个规范的循环生成元。

## 四、分量导子及最小整数投影

对每个 $e$ 定义 $G_e=Q_M/\Omega_e$。仅支撑在第 $e$ 分量、且来自原序的所有坐标组成理想
$$
 I_e=(G_e(\lambda_e))\ \subseteq O_e .
$$
一个整多项式若在其余全部分量为零，就在 $\mathbb Q[\lambda]$ 中被这些互素因子的乘积整除；首一长除把商降回整数。反向任意倍数都能如此实现。因此总导子为 $\prod_e I_e$，且 $b_e$ 是 $I_e\cap\mathbb Z$ 的正生成元。

更细地，将 $v$ 取为任一位于 $p$ 上的赋值，归一成 $v(p)=1$。记 $a=v_p(e)$，则
$$
 v(I_e)=v_p(N/e)+
 \sum_{\substack{1\le j\le a\\e/p^j>2}}
     \frac{\varphi(e/p^j)}{\varphi(e)}. \tag{6}
$$
同链后层各贡献一，不同链贡献零。要计算前层，置 $e=cp^a$、$i=cp^b>2$、$b<a$，在恰阶 $e$ 根 $z$ 处将 $F_i(z)$ 写成 $\prod_w(z-w)$。非零贡献要求 $z,w$ 的阶数与 $p$ 互素的分量相同，因为阶数与 $p$ 互素的单位根约化单射（$X^c-1$ 的根模 $p$ 可分）。恰有 $\varphi(p^b)$ 个 $w$ 符合，每个 $z/w$ 是恰阶 $p^a$ 的根 $\eta$。$\prod_{(r,p)=1,\,1\le r\le p^a}(1-\eta^r)=p$，而 $(1-\eta^r)/(1-\eta)$ 模极大理想为非零的 $r$，故 $v(1-\eta)=1/\varphi(p^a)$。据 (3) 移回实分量即得 (6)，每个位于 $p$ 上的素理想有相同的归一化值。

(6) 中前层和不超过 $1/(p-1)$，且其为正的充要条件是 $p\mid e$ 且 $e/p>2$。向上取整即得 (2)。还可只用整除性证明这一步：全部前层 $F_{e/p^j}(z)$ 的乘积整除 $z^{e/p}-1$，而 $1-z^{e/p}$ 整除 $p$。依 (3) 差去单位因子，实层的乘积也整除 $p$，实性可沿前述自由二次基下降。有真正前层时其范数是大于 1 的 $p$ 幂，所以恰需再添一个 $p$。最后 $\operatorname{lcm}_e b_e=D_1$（$M\ge2$），因为当各分量单位的统一整倍都可孤立时，乘以原序中任意多项式便能逐分量得到同一整倍的全部分量。

原路径坐标还给出完全整数的独立检验。写 $c_e(n)=\sum_{l\mid\gcd(e,n)}l\mu(e/l)$。相应特征向量坐标为 $\sqrt{2/M}\sin(\pi ka/M)$，$1\le k<M$。将投影和中的 $k$ 按 $N/\gcd(k,N)=e$ 分组。积化和差后，补上 $-k$ 正好遍历全部恰阶指标，而 Möbius 反演将相应指数和化为 $c_e$。因此
$$
 (P_e)_{ab}=\frac{c_e(a-b)-c_e(a+b)}N,\qquad
 b_e=\frac{N}{\gcd\bigl(N,\ c_e(j-1)-c_e(j+1)\ (1\le j<M)\bigr)}. \tag{7}
$$
第二式只需看首列，因为第一节的整循环基把首列整性传到整个投影矩阵。(6) 与 (7) 分别从局部理想和路径节点读取同一分母。

## 五、与全整数环的对应和直接复算

以上取余计算从有限 Dirichlet 递推开始，仅用精确阶、形式多项式、Frobenius、导数以及整基消元。现在识别靶环。对恰阶 $e$ 的复根 $z$，经典分圆整数环为 $\mathbb Z[z]$，其复共轭不变子环是 $\mathbb Z[2-z-z^{-1}]$。后一事实直接由自由基 $1,z$ 可见：$A+Bz=A+Bz^{-1}$ 强制 $B=0$。因此 $O_e$ 是极大实子域的全整数环，$\prod_{e\mid N,e>2}O_e$ 确为全谱环的整闭包。相同抽象数域保留各自的谱坐标，公式 (2) 对指标 $3,4,6$ 也按原标签分别计算。此步的经典识别没有被用作前面原生结式或各层消元的预设理由。[原实谱标签与互补坐标](https://github.com/awdawmip/enterprise-math/blob/9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c/research_notes/PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md)

标准库程序在 $M=1,\ldots,22,24,27,30,32,36,42,45$ 上，先以原路径坐标产生所有分量取余列，并在每一列核对与 $H_M$ 的交织式。它用 Bareiss 行列式确定须检验的素数，再在模素数幂上逐个消去单位主元求全部 Smith 层。各 $b_e$ 则由原坐标解有理线性方程、逐列取分母最小公倍数独立算出。上述 29 个 $M$ 的全部投影首列还与 (7) 逐项相同。另在 $2\le M\le512$ 的全部 4070 个 $(M,e)$ 上，程序用 Möbius 整数和比较了 (7) 与 (2)。$M=12$ 的非单位因子为 $(24,12,6,2,2)$，$M=30$ 为五个 $60$、两个 $12$、两个 $6$、五个 $2$。运行 `python smith_check.py` 即重建证书。[复算代码](smith_check.py) · [精确结果](smith_checked.json)
