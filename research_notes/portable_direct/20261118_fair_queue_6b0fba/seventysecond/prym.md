# P46 的二进局部幺正群、四阶几何自同构与有限域扭曲

在特征 7 的实际 Prym 上，R106 所问非分歧二进因子的 Hermitian 格在整换基下唯一，Gram 矩阵可取 $\operatorname{diag}(1,2)$。其局部等距群在三个主极化方向上传递。实际保极化几何自同构群恰为 $C_4$，逐点固定这三个方向；每个三线商自身的保极化几何自同构群也是 $C_4$。两群的生成元和作用可以分别核验。

记 $E:y^2=x^3-6x^2+36$，$C:w^2=y(x^2-12)$，$P=\operatorname{Prym}(C/E)$，$\lambda$ 为诱导极化。第 13 轮已证三条 $\mathbb F_2$ 直线的主极化商 $A_l=P/l$ 两两几何不同构、均非 Jacobian，第 19 轮已证真实 Rosati 陪集的范数 24 壳为空及三阶元排除。原 R106 交接还给出在假定格受整个非分歧系数环作用时，中心 $\mu_3$ 对三条线的作用。本文从钉住的 $R$ 作用确定格，并求整个局部群、它的可提升有限像和真实几何群。[R106 原任务](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/EMF6D046_R106_TWO_ADIC_HERMITIAN_UNITARY_GEN2_20260909.md) · [原交接及条件结果](https://github.com/awdawmip/enterprise-math/blob/6884dfbce402ece5aee316a0b08a6696ed77dc1d/research_artifacts/mcp/RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY/MCP-c618a61189764f23846a391a08518a1a/105106d60df17cc1b9f3/_checkpoint.json) · [三商及余切表示](../thirteenth/theta.md) · [实际空壳](../nineteenth/hermitian.md)

## 一、从 Frobenius 整作用恢复非分歧格

设 $J$ 为七次 Frobenius，$\alpha=J^2$。冻结结果给出 $\operatorname{End}^0_{\rm geom}(P)=M_2(F)$，其中 $F=\mathbb Q(\alpha)$ 为本原非 Galois 四次 CM 域，唯一二次子域是 $F^+=\mathbb Q(\sqrt{417})$。中心整序 $R=\mathbb Z[J^2,V^2]$ 作用于 $P$，且
$$
 R\otimes\mathbb Z_2=R_r\times O,\qquad K=\mathbb Q_2(\sqrt5),\quad O=\mathcal O_K=\mathbb Z_2[\omega],\quad \omega^2+\omega+1=0 .
$$
$R_r$ 在另一处分歧因子的极大序中指数为 2。$\ker\lambda$ 全部落在非分歧因子，同构于 $O/2O$。令 $e$ 为这个因子的幂等元；其 Rosati 共轭为自身（Rosati 在 CM 中心是共轭，固定两处下方各自的实二次局部因子）。于是 $L=eT_2P$ 是真实 Tate 格的整直和项，受整个 $O$ 作用。它在 $K$ 上满秩二，且在离散赋值环 $O$ 上有限无挠，故为自由秩二。[R105 的整序及极化核 §§2–3](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_TWO_ADIC_INTEGRAL_KERNEL_ORDER_20260904.md) · [Honda–Tate 和几何端同态代数](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_HONDA_TATE_20260904.md)

在几何 Tate 模中选定 $\mathbb Z_2(1)$ 的基，设 $\psi$ 为极化交错式。两个幂等分量彼此正交。在 $L_K$ 上以迹配对写
$$
 \psi(x,y)=\operatorname{Tr}_{K/\mathbb Q_2}(\eta h(x,y)),\qquad \eta=1+2\omega,\quad\bar\eta=-\eta .
$$
具体地，要求同式对所有 $\psi(x,a y)$ 成立，右端在迹内乘 $a\in K$。迹对偶给出唯一 $h$；$\psi(ax,y)=\psi(x,\bar a y)$ 和交错性使 $h$ 为 Hermitian 式，第二变量线性。因 $K$ 非分歧、$\eta$ 为单位、$OL=L$，$\psi$ 的整对偶正是 $h$ 的 $O$ 对偶。极化诱导的 Tate 同态的余核同型于其二初等极化核，故 $L^\#/L\simeq O/2O$。因此 $h$ 在 $L$ 上整、行列式估值 1，模 2 的 Hermitian 形秩为 1。在剩余域 $\mathbb F_4$ 上，去掉根基得到非退化一维 Hermitian 形，故存在范数非零的向量。提升它，得到一个单位范数的整向量，可正交分裂。第二个对角条目的估值必为 1。所有奇二进单位都是 $O^\times$ 的范数：对任一奇数 $u$，$N(x+\omega)=x^2-x+1=u$ 在 $x=0\bmod2$ 由奇导数唯一提升。这允许分别重标，终于
$$
 (L,h)\simeq (O^2,H),\qquad H=\operatorname{diag}(1,2),\qquad
 L^\#=Oe_1\oplus\tfrac12 Oe_2 .
$$
以上恢复的是唯一定出的局部整等距类；原曲线全局整序的一组带名基以及伴随分歧格的实际 Gram 仍未由此给出。

## 二、全部局部等距、模精度和生成元

记 $N(x)=x\bar x$。非零的 $N(x),2N(y)$ 估值奇偶不同，故 $h(v,v)\in\mathbb Z_2$ 恰等价于 $v\in L$。每个有理等距都保持此格。其完整矩阵集合为
$$
 U(L)=\left\{\begin{pmatrix}a&-2u\bar c\\ c&u\bar a\end{pmatrix}:
       a,c,u\in O,\quad N(a)+2N(c)=1,\quad N(u)=1\right\}. \tag{1}
$$
首列强制 $a$ 为单位，它的正交补由 $(-2\bar c,\bar a)^t$ 生成，第二列的范数条件强制 $N(u)=1$。行列式为 $u$。在 $D=L^\#/L$ 上，$e_2/2$ 映成 $u\bar a\,e_2/2$，作用由 $u\bar a\bmod2$ 确定。$\operatorname{diag}(1,\omega)$ 给出 $1\to\omega\to\omega^2\to1$ 的三循环。每条 $\mathbb F_2$ 线的稳定子就是作用核，在 $U(L)$ 中指数为 3。

**有限层的提升判据。** 取 $n\ge1$，在 $O/2^n$ 上所有可逆的 Gram 同余解中，一个矩阵能从式 (1) 提升，当且仅当 $N(\det g)\equiv1\pmod{2^n}$。事实上首列与正交条件仍迫使同式 (1) 的参数表示；但第二列的范数只要求 $2(N(u)-1)=0\bmod2^n$。固定 $c$ 的任一整提升时可保持 $a\bmod2^n$ 解出 $N(a)=1-2N(c)$，同样可保持 $u\bmod2^n$ 解出 $N(u)=1$，因为对任何单位的范数多项式 $x^2-xy+y^2$ 至少一个偏导为奇数。由模范数满射，其单位范数核阶为 $3\cdot2^{n-1}$。因此可提升像的阶为
$$
 4^n(3\cdot2^{n-1})^2=9\cdot2^{4n-2}.
$$
模 2 所有同余解都可提升；从模 4 起，每层同余解恰有一半可提升。例如 $\operatorname{diag}(1,1+2^{n-1}\omega)$ 对 $n\ge2$ 是同余等距，行列式范数模 $2^n$ 却是 $1+2^{n-1}$。

复算给出一组有限**拓扑生成元**。在模 8 依次取第一、第二对角的单位矩阵变体，以及非对角变体；确切九张矩阵按行和 $1,\omega$ 基列在证书的 `generators_mod8`。逐一加入时生成子群阶为 $2,4,12,48,192,384,768,2304,9216$。对每一张取上述 Hensel 整提升即可。若 $U_n=\ker(U(L)\to\mathrm{GL}_2(O/2^n))$，则 $|U_n/U_{n+1}|=16$ 对 $n\ge1$ 成立。当 $n\ge2$ 时，平方把 $1+2^n Z$ 送至 $1+2^{n+1}Z\bmod2^{n+2}$，因而在相邻两商间给出双射。从模 8 满射及模 4 至 8 的核出发，依次平方填满所有更高层，再取闭包。这是具体的有限生成证书，未假定生成元数最小。

## 三、实际四阶几何群与三个商

令 $\Gamma=\operatorname{Aut}_{\bar{\mathbb F}_7}(P,\lambda)$，保持群原点。原曲线给出 $\sigma(x,y,w)=(x,-y,iw)$，$i^2=-1$，其在 $P$ 上满足 $\sigma^2=-I$。余切基 $\nu,x\nu,y\nu,x^2\nu$，$\nu=dx/(yw)$，上面的特征值为 $i,i,-i,i$；故 $\sigma$ 与 $-\sigma$ 在特征 7 的余切迹分别为 $2i,-2i$，不能共轭。[实际覆盖及正则形式](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_LINE_BUNDLE_HODGE_MODEL_20260904.md)

保极化群有限且嵌入 $\mathrm{GL}_2(F)$。若 $g$ 有阶 3，因 $F$ 不含 $\zeta_3$，它的最小多项式是 $X^2+X+1$。此恒等式在整同态环也成立；若它逐点固定非零 $D$，限制后左边等于 $3I_D=I_D\ne0$。所以既有三线平凡作用确实排除全部三阶元，包括假设落在作用核内的元素。若 $g$ 有素阶 $\ell\ge5$，本原 $\ell$ 次根在 $F$ 上的次数必须至多 2。$F$ 和分圆域的交至多二次（$F$ 非 Galois）；对 $\ell\ge7$ 仍至少为 3，对 $\ell=5$ 的唯一二次交候选 $\mathbb Q(\sqrt5)$ 也不是 $F^+$。同理 $\mathbb Q(\zeta_8)$ 的三个二次子域均非 $F^+$，排除阶 8。故 $\Gamma$ 是所有元素阶至多 4 的 2 群。

行列式落入 $\mu(F)=\{\pm1\}$。令 $H_0=\Gamma\cap\mathrm{SL}_2(F)$。$\sigma$ 的最小多项式为 $X^2+1$，故 $\det\sigma=1$，即 $\sigma\in H_0$。其中对合只有 $-I$，所有阶四元的平方均为 $-I$（$i\notin F$）。因此 $H_0/\{\pm I\}$ 的每个元素平方为 1，群是阿贝尔的，$H_0$ 共轭 $\sigma$ 只能得到 $\pm\sigma$。余切迹排除负号，故 $H_0$ 位于其中心化域 $F[\sigma]\simeq F(i)$，其中满足四次方为 1 的元素恰为 $\langle\sigma\rangle$。整个 $\Gamma$ 亦正规化 $H_0=\langle\sigma\rangle$，同样不能反转 $\sigma$，再次落入同一域，于是
$$
 \Gamma=\langle\sigma\rangle\simeq C_4 .
$$

记 $q_l:P\to A_l$，$M_l=(T_2q_l)^{-1}T_2A_l$，$T=T_2P$。先前已证 $T=M_l\cap\alpha^{-1}M_l$。任一 $A_l$ 的极化自同构 $f$ 给出 $q_l^{-1}f q_l$，它与中心 $\alpha$ 对易，因而保 $T$，且它与逆元的两倍均为整同态。两倍整同态消去 $P[2]$，故经 $[2]$ 分解，得到 $P$ 的整极化自同构。反向所有 $\Gamma$ 逐点固定 $l$，都经 $q_l$ 下降，两次构造互逆。故每个无标记商的几何保极化群正好也是 $C_4$。[三个商的格恢复与整提升 §3](../thirteenth/theta.md)

## 四、有限域上的扭曲、点数与同源类

$P$ 的原模型定义于 $\mathbb F_7$，各 $A_l$ 的原模型在 $\mathbb F_{7^n}$ 的存在条件为 $3\mid n$。以下对 $A_l$ 都限于这些 $n$。由于 $i^7=-i$，七次 Frobenius 对几何群由 $\sigma\mapsto\sigma^{-1}$ 作用。商上的作用经原同源传递。对 $\mathbb F_{7^n}$，原模型的保极化扭曲由 $H^1(\widehat{\mathbb Z},C_4)$ 给出，即 $C_4/(\mathrm{Frob}^n-1)C_4$；有限群中的每个指定生成元值都给连续余循环。奇数 $n$ 有两类，以指数 $k=0,1$ 表示，原模型的有理自同构群为 $C_2$。偶数 $n$ 有四类 $k=0,1,2,3$，有理自同构群为 $C_4$。几何群阿贝尔，扭曲后的有理自同构群同阶。

令 $h(T)=T^4+5T^3+245T+2401$，$h_m(T)=\prod_{h(\alpha_i)=0}(T-\alpha_i^m)$。冻结 Honda–Tate 检验给出不同 $\alpha_i$ 的比不是单位根，故 $h_m$ 始终不可约四次、$\mathbb Q(\alpha^m)=F$。在扭曲的 Tate 表示上，Frobenius 可取为 $\sigma^k J^n$（反向余循环约定会交换 $k=1,3$）。由 $J^2=\alpha I$、$J\sigma J^{-1}=\sigma^{-1}$，取 $2\times2$ 特征多项式的域范数，得到

|扩域次数|扭曲|八次 Weil 多项式|
|---|---|---|
|$n$ 奇|$k=0,1$|$h_n(T^2)$|
|$n=2m$|$k=0$|$h_m(T)^2$|
|$n=2m$|$k=2$|$h_m(-T)^2$|
|$n=2m$|$k=1,3$|$h_{2m}(-T^2)$|

奇数 $n$ 时两种 Frobenius 都反交换于 $\sigma$，平方为 $\alpha^n I$；在冻结的二次剩余度七进素处 $v(\alpha)=1$，故 $\alpha^n$ 不是 $F$ 中平方，所列八次式不可约。偶数 $n$ 时前两个四次因子彼此不同：相同将迫使两不同根之比是单位根。最后一式不可约，因为 $\mathbb Q(i\alpha^m)$ 经平方包含 $\mathbb Q(\alpha^{2m})=F$，再包含 $i$，次数为 8。因此奇数 $n$ 的两类极化扭曲同源；偶数 $n$ 恰为三个同源类，$k=1,3$ 合并。原三个主极化商之间的几何不同构在扭曲后保持，且它们在相同 $k$ 下有同一 Weil 多项式。特别地，$\mathbb F_{7^3}$ 上有六个这样的主极化形式，同属一个同源类；$\mathbb F_{7^6}$ 上十二个，三个同源类各含 3、3、6 个。这里计数保持极化与群原点的形式，仅限指定的三个几何模点。[真实 Weil 数据及根比值、七进估值](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_HONDA_TATE_20260904.md)

直接枚举 $E,C$，前三个扩域及四次扩域的 Prym 迹 $\#E-\#C$ 为 $0,-10,0,50$。在 $n=3$ 两种扭曲的有理点数均为 $13942826352$；在 $n=6$ 时按 $k=0,1,2,3$ 分别为 $194402406682025627904$、$191581498500773609104$、$188800470532313595904$、$191581498500773609104$。脚本逐层核验模 2、4 的所有候选矩阵，在模 8 上重建并逐个生成全部 9216 个可提升矩阵；并由扭曲幂迹与原四次的 Newton 恒等式两路核对 $n=1,\ldots,12$ 的全部多项式。标准库命令 `python prym_check.py --out prym_checked.json` 可重建输出。[复算器](prym_check.py) · [有限矩阵与点数证书](prym_checked.json)
