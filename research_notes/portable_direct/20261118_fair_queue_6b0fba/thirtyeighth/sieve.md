# 同余筛选何时保留 ζ 分布的幂分解独立性

取正奇整数 $K$，赋以概率 $\Pr(K=n)=n^{-\sigma}/Z_o(\sigma)$，其中 $\sigma>1,\ Z_o(\sigma)=(1-2^{-\sigma})\zeta(\sigma)$。固定 $m\ge2$，唯一地写 $K=ST^m$，$S$ 不含任何素数的 $m$ 次方。给定 $K$ 的一个模 $q$ 剩余类后，描述 $(S,T)$ 的条件分布最少需要多少个独立乘积分布？下文给出全部模数与全部单剩余的精确答案。例 $m=2$ 时，知道 $K\equiv0\bmod9$ 或 $K\equiv3\bmod9$ 都保留独立性，知道 $K\equiv0\bmod3$ 则将二者耦合。对 $K\equiv3\bmod105$，最少需要十二个乘积项。

原始 #1162 笔记 §1、4、5 给出奇整数分布、正的 ζ 倾斜及无条件独立性；未经重新赋权的原始别名分布是 $\sigma=2$。具体地，奇素数 $p$ 处 $\rho=p^{-\sigma}$，两边的指数 $R=v_p(S)$ 与 $J=v_p(T)$ 独立，其他素数也独立，而且
$$
\Pr(R=i)=\frac{(1-\rho)\rho^i}{1-\rho^m}\quad(0\le i<m),\qquad
\Pr(J=j)=(1-\rho^m)\rho^{mj}\quad(j\ge0).
$$
因此 $S$ 在所有正奇 $m$ 次幂自由整数上按 $s^{-\sigma}$ 赋权，$T$ 在正奇整数上按 $t^{-m\sigma}$ 赋权。后续交接和相邻的实特征估计处理了不同读数。本文沿原稿 §9 的同余方向研究正概率条件律，作为未编号数论分叉。[原始幂分解](https://github.com/awdawmip/enterprise-math/blob/67eef66c62ec0f085d7313fa895a6a8ead964a03/research_notes/1162_alias_prime_valuation_thickness_semigroup_20260908.md) · [#1162 交接目录](https://github.com/awdawmip/enterprise-math/blob/1acc7f08521a2fb922c46511c0a3ba17d6bfd350/research_notes/1162_research_handoff_index_20260909.md) · [相邻特征估计](https://github.com/awdawmip/enterprise-math/blob/67eef66c62ec0f085d7313fa895a6a8ead964a03/research_notes/1162_rough_observer_neutrality_character_estimator_20260908.md)

## 1. 单位剩余集合：独立性与共享信息

先给定 $(K,q)=1$。这等价于分别要求 $(S,q)=(T,q)=1$，故 $S,T$ 仍独立。写 $G=(\mathbb Z/q)^\times$，$G^m=\{g^m:g\in G\}$，约定 $q=1$ 时群平凡。$S,T$ 的单位剩余支撑均为整个 $G$。例如把所需单位提升为模 $\operatorname{lcm}(2,q)$ 的奇单位，该同余类中有素数，即可同时满足奇与幂自由要求。

再筛非空集合 $A\subseteq G$，事件为 $E_A=\{ST^m\bmod q\in A\}$。则
$$
S\perp T\mid E_A\quad\Longleftrightarrow\quad A\,G^m=A. \tag{1}
$$
这里及以下凡 $A\subseteq G$，$E_A$ 已蕴含互素条件。证明：在限定 $T=t$ 的列上，$S$ 允许的行恰为 $At^{-m}$，每列非空。原联合质量是两份正权的乘积，筛后独立等价于许可支撑为一个矩形。因此所有列必等于 $T=1$ 的列 $A$，这也充分。

若 $A=gJ$ 是子群 $J\le G$ 的一个陪集，则在事件上 $Y=T^mJ$ 由 $SJ$ 唯一决定，反之亦然。给定 $Y$ 后，筛选重新分成 $S,T$ 各自的独立条件，因而
$$
I(S;T\mid E_A)=H(Y\mid E_A),\qquad
\Pr(Y=y\mid E_A)\ \propto\ \Pr(T^mJ=y)\Pr(SJ=gy^{-1}). \tag{2}
$$
右侧先验都取在相应互素条件下。$H$ 用自然对数，条件互信息指给定事件后的整对随机变量的互信息。这里无需假设单位剩余等概率。

## 2. 全部单剩余的最小乘积分解定理

现只给定 $E_r=\{K\equiv r\bmod q\}$。若 $q$ 为偶数且 $r$ 为偶数，事件概率为零；其余剩余类均可实现。对 $p^e\parallel q$，令 $v=\min(v_p(r),e)$，对 $r=0$ 取 $v=e$。定义
$$
M=\prod_{v<e}p^{e-v},\qquad
b=\#\{p^e\parallel q:\ p\text{ 奇},\ v=e,\ m\nmid e\},\qquad
L=|((\mathbb Z/M)^\times)^m|\,2^b. \tag{3}
$$
空乘积取 $1$。则模 $q$ 条件联合概率矩阵的实秩与非负秩均为 $L$；覆盖许可支撑所需的最少矩形数、将原整数对的条件分布写成独立乘积分布的最少混合项数，也都恰为 $L$。特别地，独立性等价于 $L=1$。即每个 $v<e$ 的素数幂都满足 Carmichael 指数 $\lambda(p^{e-v})\mid m$，每个奇的 $v=e$ 素数幂都满足 $m\mid e$。

**局部条件。** 若 $v<e$，则 $R=i=v\bmod m$、$J=j=\lfloor v/m\rfloor$ 分别固定。除此以外恰须
$$
(S/p^i)\,(T/p^j)^m\equiv r/p^v\pmod{p^{e-v}} .
$$
许可矩阵分成 $|((\mathbb Z/p^{e-v})^\times)^m|$ 个互不相连的满矩形，每块由第二因子的幂值标记。偶素数的可行情况 $v=0$ 同理。若 $v=e$ 且 $p$ 奇，写 $e=mk+d,\ 0\le d<m$。$d=0$ 时只须 $J\ge k$。$d>0$ 时先须 $J\ge k$，其余精确条件为
$$
[R\ge d]\ \text{或}\ [J\ge k+1].
$$
将两侧分别压缩成低、高两类，得到子矩阵 $\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)$，其秩为 2，支撑连通。注意即使 $e<m$，$S\equiv0\bmod p^e$ 也可能，因为 $v_p(S)$ 只需小于 $m$。

**从局部到整体。** 将所需的局部 $S$ 赋值 $i_p<m$ 逐一固定，写 $D=\prod_{p\mid q,\ p\text{ 奇}}p^{i_p}$。各处指定的单位部分经除去其他素因子后成为一个单位同余类。中国剩余定理和算术级数中素数的存在性允许取一个不整除 $2q$ 的素数 $\ell$，使得 $S=D\ell$ 满足全部指定。$T$ 同理可同时实现所有模板，甚至可以自由固定各有限赋值本身。因此，各局部许可矩阵的张量积准确描述了支撑，概率权重无需在 CRT 坐标间分解。

每个非空角度块（即各 $v<e$ 处幂值的组合）中，按 $b$ 个阈值的行指标向量分别取固定高低，共有 $2^b$ 个不交矩形。原先 $S,T$ 独立，这些矩形各自给一个乘积项。每种行、列模板都实现，抽取各一种代表得到与单位阵和上述 $2\times2$ 矩阵的张量积等价的满秩 $L$ 阶子矩阵。乘正的行、列权重并重新归一化不改秩，给出混合下界。即使允许矩形重叠也不会变少：在每个角度块对每个二进向量 $u$ 取一对互补的行列 $(u,1-u)$。不同 $u,w$ 的两个交叉位置不可能同时合法，否则 $u\ge w$ 且 $w\ge u$。不同角度块间则两边的交叉位置都不合法。因此每个全许可矩形至多覆盖所选 $L$ 个位置中的一个。

若只问能从 $S$ 与 $T$ **分别确定的同一标签**，最细标签只有式 (3) 中的幂值组合，恰为 $|((\mathbb Z/M)^\times)^m|$ 类。这是因为群角度不同就断开；在同一块，所有阈值均高的行和列将每个允许顶点连成一片。确定性共同比特要求在每条有正质量的边上取相同值，因而在连通分量内必定常值。例如 $m=2,q=105,r=3$ 时有六个角度值、一个独立的阈值条件，故有六个确定性标签，却需要十二个混合项。$q=105,r=0$ 时只有一个标签，仍需八个混合项。

## 3. 零剩余的互信息：不同素数精确相加

令 $q$ 奇，筛选 $q\mid K$，含 $q=1$ 的平凡情形。对 $p^e\parallel q$ 置 $d=e\bmod m,\ \rho=p^{-\sigma}$，取 $h_2(z)=-z\log z-(1-z)\log(1-z)$ 并连续延拓端点。互信息为
$$
I(S;T\mid q\mid K)=
\sum_{\substack{p^e\parallel q\\d>0}}
\left[h_2(\rho^{m-d})-
\frac{1-\rho^{m-d}}{1-\rho^m}h_2(\rho^m)\right].                \tag{4}
$$
每项严格正；它只看局部指数 $e$ 对 $m$ 的余数。对 $d>0$，在 $J\ge k$ 后，$B=[R\ge d]$ 与 $C=[J>k]$ 独立，其先验概率为 $(\rho^d-\rho^m)/(1-\rho^m)$ 和 $\rho^m$；剩余筛选是 $B\lor C$，其概率为 $\rho^d$。筛后 $\Pr(C)=\rho^{m-d}$、$\Pr(B)=(1-\rho^{m-d})/(1-\rho^m)$。$B=0$ 时 $C=1$，$B=1$ 时 $C$ 保持原始分布。这给出 $H(C)-H(C\mid B)$ 的上式，而给定各指示量以后各自的超额指数不再传递信息。零条件可独立加在各素数上，故各项直接相加。特别地在原生 $\sigma=2$、$m=2$ 时，$3\mid K$ 的条件表为
$$
\begin{pmatrix}0&1/10\\8/9&1/90\end{pmatrix}
$$
（行列依次按照 $B,C$ 的 0、1 排列）。同一 $m$ 下 $9\mid K$ 无损保留独立性。固定 $m,d,\sigma$ 令 $p\to\infty$ 时，写 $\delta=\rho^{m-d}$，该素点的互信息等于 $\delta\log(1/\delta)+\delta+O_m(\delta^2+\rho^m\log(1/\rho))$。

## 4. 计算一般剩余类与临界边界

**全模数概率表。** 对任意 $A\subseteq\mathbb Z/q$，只要事件概率为正，就可用有限个特殊函数值求整张条件表。置 $Q=\operatorname{lcm}(2,q)$，通过奇数条件把每个可行剩余提升为唯一的奇类 $b\bmod Q$，取 $1\le b\le Q$。$T$ 的概率为 $Q^{-m\sigma}\zeta(m\sigma,b/Q)/Z_o(m\sigma)$。$S$ 的未归一化权重可如下计算：
$$
\sum_D D^{-\sigma}
\sum_{\substack{u\in U_Q\\Du\equiv b\bmod Q}}
\frac1{\varphi(Q)}\sum_{\chi\bmod Q}
\overline{\chi(u)}\,\frac{L(\sigma,\chi)}{L(m\sigma,\chi^m)} .       \tag{5}
$$
$D$ 遍历 $\prod_{p\mid Q,\ p\ne2}p^{i_p}$，各 $0\le i_p<m$，$U_Q=(\mathbb Z/Q)^\times$。除以 $Z_o(\sigma)/Z_o(m\sigma)$ 即为概率。证明是剥离 $Q$ 的素因子后使用单位剩余类的特征正交，Euler 因子为 $1+z+\cdots+z^{m-1},\,z=\chi(p)p^{-\sigma}$；式中特征皆按模 $Q$ 延拓为非单位上取零。将两份概率表相乘，保留 $st^m\in A$ 的格子、重新归一化，即得结果。整数对的互信息等于该有限表的互信息，因为在已给定的两个余数内，原始两边的细分仍条件独立。

**$\sigma\downarrow1$ 的差异。** 固定 $q,m$ 且先给定 $(K,q)=1$。$S$ 的单位剩余趋于均匀：由 (5)，非主特征的权为 $O_{q,m}(\sigma-1)$，因为分子在 $1$ 有限、归一化主项有简单极点，而 $L(m\sigma,\chi^m)$ 在 $\sigma=1$ 非零。$T$ 的极限仍按 $t^{-m}$ 在与 $2q$ 互素的正整数上赋权。对任意单位集 $A$，令 $U_A$ 在 $A$ 上均匀、$Y=T^m\bmod q$ 取这一极限分布且与 $U_A$ 独立。则
$$
\lim_{\sigma\downarrow1} I(S;T\mid E_A)=H(U_A Y^{-1})-\log |A|.
$$
这是因为此时每列的允许行数同为 $|A|$，条件 $E_A$ 不再改变列分布。特别对陪集 $A=gJ$，极限为 $H(T^mJ)$。对 $q=5,m=2,A=\{1\}$，两个标签的极限概率恰为 $(1\pm\sqrt5/3)/2$。事实上 $\chi=\left(\frac{\cdot}{5}\right)$ 区分 $T^2=1,4$，且 $L(2,\chi)=\pi^2[\csc^2(\pi/5)-\csc^2(2\pi/5)]/25=4\pi^2/(25\sqrt5)$。去除 $2$ 的 Euler 因子后除以 $(1-2^{-2})(1-5^{-2})\zeta(2)$，得 $\mathbb E\chi(T)=\sqrt5/3$。这一区别在接近 $\sigma=1$ 时仍存在。

**二次标签的二进极限与锐利损失率。** 顺序固定为先令 $\sigma\downarrow1$，再取 $m=2,\ q=2^e,\ e\to\infty$，筛一个奇单位剩余类。写 $Y_e=T^2\bmod 2^e$，$T$ 为奇整数 ζ 分布 $\mu_2$。上面的互信息极限为 $H(Y_e)$，而
$$
H(T)-H(Y_e)\sim \frac{8}{2^e}\qquad\text{（自然对数）}.               \tag{6}
$$
特别地，奇整数完整的熵上界在此族中可逼近。若先取其他模数的互素条件，$T$ 的极限是删掉相应素数的独立赋值坐标所得的条件律，故其熵不超过 $H(T)$。

证明令 $M=2^{e-1}$，$e\ge3$。对奇数 $t,t'$，$t^2\equiv t'^2\bmod2^e$ 当且仅当 $t\equiv\pm t'\bmod M$：除等值情形，$t-t',\,t+t'$ 的两个赋值中有一个为 $1$。因而每个标签用一个奇数 $0<a<M/2$ 代表。令 $x=a/M$，将该纤维中的正整数除以 $M$ 后，得到
$$
{\cal R}_x=\{j+x,\ j+1-x:\ j=0,1,\ldots\},\qquad
V(x)=\sum_{y\in{\cal R}_x}y^{-2}=\pi^2\csc^2(\pi x).
$$
因此标签概率恰为 $8M^{-2}\csc^2(\pi a/M)$。取 $Z=\pi^2/8$，定义
$$
F(x)=V(x)\log V(x)-\sum_{y\in{\cal R}_x}y^{-2}\log(y^{-2}).
$$
按纤维展开离散熵，得 $H(T)-H(Y_e)=(ZM^2)^{-1}\sum_{a\ \rm odd}F(a/M)$，其中仍限 $0<a<M/2$。首项 $x^{-2}\log(x^{-2})$ 在 $F$ 中消去，剩余 $O(1+|\log x|)$。在远离零的区间作中点 Riemann 和并用该对数界控制近零部分，即得该和等价于 $\frac M2\int_0^{1/2}F(x)\,dx$。

为算积分，先截到 $[\epsilon,1/2]$。以 $t=\cot(\pi x)$ 代换，
$$
\int_\epsilon^{1/2}V\log V\,dx
=\pi\,[t\log(\pi^2(1+t^2))-2t+2\arctan t]_{0}^{\cot(\pi\epsilon)}
=-2(\log\epsilon+1)/\epsilon+\pi^2+o(1).
$$
另一项折叠各个纤维后，是 $\int_\epsilon^\infty -2\log y\,dy/y^2$ 加上 $O(\epsilon)$：遗漏的是正整数周围宽 $2\epsilon$ 的小段，离零后被积函数在这些段上的上界可和。该积分为 $-2(\log\epsilon+1)/\epsilon$。相减得到 $\int_0^{1/2}F=\pi^2$，代入 $Z,M$ 即得 (6)。

运行 <code>python sieve_check.py</code> 可逐字生成 <code>sieve_checked.json</code>（Python 3.8+ 标准库）。脚本穷举 15,216 个单剩余的实支撑模板，用二进消元核对秩、用连通分量核对共享标签；另穷举 3,636 个非空单位集和 15,000 个实际正奇整数分解。240 组素数幂阈值概率使用有理数核对。直接截断 $q=5$ 的极限分布至 10,000 并向外估计尾项，所得概率区间也包含上述根式。另用二进标签的三角函数精确质量复算了 $e=6,8,10$ 的熵损失。一般单位剩余的先验依概率而异，实秩与支撑虽可按 CRT 相乘，不能由此假设每个单位标签等概率。
