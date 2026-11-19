# 两条秩五选择子坐标分离所有带水平二标记的 CM 点

取 Legendre 族的纯对称四次，沿用零第三奇周期扩张的归一化。令 $x=\lambda(\tau),\ W=\vartheta_3(\tau)^4,\ y=\operatorname{Im}\tau, e=(E_2(\tau)-3/(\pi y))/W$。冻结 CP19 定义的坐标为
$$
 b=\frac{1-3x-e}{1-x},\qquad
 \alpha=\frac{e^2+(4x-2)e+7x^2-7x+1}{3(1-x)^2}.                 \tag{1}
$$
在上半平面的所有 CM 点（任选水平二标记）上，映射 $x\mapsto(\alpha,b)$ 是单射，包括不同判别式之间的比较。因此对每一带标记点都有
$$
                    \mathbb Q(\alpha,b)=\mathbb Q(x).
                                                                    \tag{2}
$$
第 56 轮在正虚轴得到式 (2)。此处处理了其余标记、全部奇判别式，以及两种对数归一化在复参数下产生的差别。证明对 $|D|\ge41$ 给出统一估计，剩余 20 个判别式附严格区间计算。[原登记与 CP17–19](https://github.com/awdawmip/enterprise-math/blob/9819f394e8d77dbaa2e38aa6c938b60fc535b646/research_tasks/1195_RANK5_SELECTOR_GALOIS_CLASSFIELD_GEN2_20260909.md) · [第 5 轮的模族与导数](../fifth/selector.md) · [第 56 轮的矩形情形](../fiftysixth/classfield.md)

## 一、哪两条奇行给出原读数

采用 $q=e^{\pi i\tau},\ z=x/16,\ \ell=\log|q|=-\pi y,\ \delta=(1-x)W,\ L=W^3/(1-x)$。本族的 Yukawa 耦合为 1，瞬子级数和第三扩张常数为零，故 CP19 的 $U=\ell^2/3,\ V=-\ell$。把它们代回原比率，以 Jacobi 导数将 $E_2/W+3/(W\ell)$ 合并就得到 (1)。在镜面局部级数域外，使用这套指定模族的模函数和导数延拓。[CP19 原式](https://github.com/awdawmip/enterprise-math/issues/1195#issuecomment-5576426514)

CP18 的奇行还要指定对数相位。在给定 $\tau_0$ 的局部令 $t_c=\pi i(\tau-c)$，其中 $c$ 是冻结的实常量。取 $u=W^2t_c,\ v=W^2t_c^3/6$，用 $\theta=z\,d/dz$ 对两行取二阶射流。因 $q\,dt_c/dq=1$，在 $\tau_0$ 的最高系数可归一成 1，有
$$
 b_c=-\frac{3}{\delta t_c}-\theta\log L,\qquad
 b_c-b=-\frac{3}{(1-x)W}(t_c^{-1}-\ell^{-1}).                    \tag{3}
$$
同一链式法则给 $\alpha_c=3/(\delta t_c)^2-b_c\theta\log W^2-\theta^2(W^2)/W^2$。因此选 $c=\operatorname{Re}\tau_0$ 的两个真正奇行在该点给出 (1)。其余**实代数** $c$ 在 CM 点给超越的 $b_c$：右边差值是 $1/(\pi W)$ 的非零代数倍。Masser 给 $e$ 代数，且 $E_4\in\overline{\mathbb Q}W^2,E_6\in\overline{\mathbb Q}W^3,E_2=eW+3/(\pi y)$。Nesterenko 的超越次数下界遂使 $e^{2\pi i\tau_0},\pi,W$ 代数独立。常量 $c$ 仅在取导时冻结；沿不同 CM 点它可不同。特别是沿用未经平移的 $t=\pi i\tau$ 得到代数奇行比率，恰当所取代表在正虚轴。这给出了把实际奇行从矩形向其它标记移动时的确切障碍。[CP18 的奇行与最大子式](https://github.com/awdawmip/enterprise-math/issues/1195#issuecomment-5576406515) · [Nesterenko 定理](https://doi.org/10.1070/SM1996v187n09ABEH000158)

## 二、错误逆根与一个复邻域

复乘点上 $x,e$ 代数。更精确地，$e\in\mathbb Q(x)$，并随嵌入搬运到对应 CM 标记的同一伴随值。理由是 $j=256(1-x+x^2)^3/[x^2(1-x)^2]$，而 $\chi^*=E_2^*E_4 E_6/\Delta\in\mathbb Q(j)$ 随任意奇模共轭正确搬运。在 $j\ne0,1728$ 时用第 56 轮 (3) 将 $e$ 写成 $x,\chi^*$ 的有理式。两椭点及其全部模像有 $E_2^*=0$。Spence 的结果含 Masser 对 $|D|=3k^2, k$ 奇的特殊分支。[Spence 命题 5.1–5.2](https://arxiv.org/abs/1607.03769)

令 $t=(1-x)^{-1}$。消去 (1) 的 $e$ 得
$$
 t^2+(2b-5)t+b^2-2b+4-3\alpha=0 .
$$
故若另一有限标记有相同读数且 $x'\ne x$，它只能是
$$
 J(x,e)=\left(\frac{1+2x+2e}{2+x+2e},-\frac{2+2x+3e}{2+x+2e}\right).    \tag{4}
$$
分母为零时另一 $t$ 为零，不对应有限标记。水平二标记的基本变换为
$S(x,e)=(1-x,-e),\ T(x,e)=(x/(x-1),e/(1-x))$，来自 theta 变换。$I=STS:(x,e)\mapsto(1/x,e/x)$ 与 $J$ 交换。因此在主形的六种标记上，只须独查恒等、$T,S$ 三种；其余三种再施 $I$。

**邻域估计。** 对上半平面上任意点，若 $|x|<2/5$，则 $|e|<1$。证明可直接用 nome 级数。对 $|q|=r=1/25$，
$$
 |\lambda(q)|\ge 16r
 \left(\frac{1-r^2/(1-r^2)}{1+2r/(1-r^3)}\right)^4>2/5 .
$$
这是 $\vartheta_2/(2q^{1/4})=1+\sum_{n\ge1}q^{n(n+1)}$ 与 $\vartheta_3=1+2\sum_{n\ge1}q^{n^2}$ 的直接界。圆内 $\lambda(q)$ 只有 $q=0$ 一个单零，Rouché 定理给出 $|x|<2/5$ 的小 nome 代表。$e$ 对 $\Gamma(2)$ 单值，故可在该代表估计。写 $r=|q|\le1/25,\ L_0=-\log r>3$，则
$$
 |e|\le\frac{1-3/L_0+24r^2/(1-r^2)^3}{(1-2r/(1-r^3))^4}<1 .
$$
最后一步用 $L_0(8.01r+25r^2)<3$，左侧处处不超过在 $r=1/25$ 的值。这一估计覆盖复标记，不要求 $q$ 实。[Jacobi theta 级数](https://dlmf.nist.gov/20.2) · [模变换](https://dlmf.nist.gov/20.7)

## 三、全判别式单射

先取一个 CM 点到主形的共轭，主形代表为 $\tau_0=(-B+i\sqrt{|D|})/2, B=0$ 或 (1)。当 $|D|\ge41$ 时 $L_0=\pi\sqrt{|D|}/2>10$。令 $s=|q|=e^{-L_0},\ u=3/L_0, (z,v)=(\lambda(\tau_0),e(\tau_0))$，从前述级数有
$$
 |z|\le17s,\quad |v-(1-u)|\le12s,\quad 0<u<0.3 .
$$
例如 $ |\vartheta_3^{-4}-1|\le(1-2s/(1-s^3))^{-4}-1<9s$，而 $|E_2-1|<25s^2$。对恒等或 $T$ 得到的 $(x,e)$，因 $T$ 的分母为 $1-z$，有 $|x|+|e-(1-u)|\le49s<u/50$（用 $L_0e^{-L_0}\le10e^{-10}$）。

若 (4) 是真实伴随值，$SJ(x,e)=(a,d)$ 也应真实。恒等或 $T$ 两种情形给
$$
 a=(1-x)/(2+x+2e),\qquad d=1+(x+e)/(2+x+2e).
$$
上述误差给 $|a|<0.31$，且最后的分数距离正实数 $ (1-u)/(4-2u)$ 小于 $0.01$，从而 $\operatorname{Re} d>1$。取 $S$ 后则
$$
 a=z/(3-2v-z),\qquad d=1+(1-v-z)/(3-2v-z).
$$
写 $v=1-u+E$，分数是 $(u-E-z)/(1+2u-2E-z)$。因 $|E|+|z|<u/50$，其分子乘分母共轭的实部严格正，且 $|a|<0.01$。三种均与邻域估计冲突。因 $I$ 的相容性，主形的六种标记都排除错误根。

如有两个标记 $x_1,x_2$ 读数相同，且其一判别式 $|D_1|\ge41$，用同一绝对 Galois 自同构将 $j(x_1)$ 搬到其主形。两个标记的读数仍相同；第一个成为刚排除错误根的六个点之一，第二个仍是带标记 CM 点。因此原本只能 $x_1=x_2$。此处无须 $D_1=D_2$。

剩下 $-40\le D\le-3$ 的 20 个判别式，用本原约化二次型逐一取 $\tau=(-B+i\sqrt{|D|})/(2A)$。在每一形上计算全部六个标记，椭点按阶三或二稳定子只取不同标记。Arb 在 192 位区间上由 theta 和 80 项 Lambert 级数取值，后者在 $r=|q|^2$ 时的绝对余量至多 $24\cdot81r^{81}/(1-r)^3$。得到 197 个不同 $x$。逐一比较 19,306 个无序对，均有
$$
 \max(|\alpha_1-\alpha_2|,|b_1-b_2|)>1/346 .
$$
这是有限部分的严格区间证明；其覆盖边界来自上一段的统一估计。在这 197 个点上，仅 $b$ 已足以区分所有点，一坐标性质只由该有限证书支持。合并两部分得到全体单射。最后任意固定两读数的数域嵌入也固定其唯一的 $x$，配合 $\alpha,b\in\mathbb Q(x)$ 即得 (2)。[可复算程序](classfield_check.py) · [有理下界和有限清单](classfield_checked.json)

## 四、生成域、理想类与有限素位

令 $D=f^2D_K$，$K$ 为虚二次域，$H=H_{2f}$ 为导子 $2f$ 的环类域，$A=\operatorname{Pic}(\mathcal O_{2f})$。完整水平二标记的 CM 互反律给 $K(x)=H$。在 2 处标记的稳定子是 $1+2\mathcal O_{f,2}=\mathcal O_{2f,2}^{\times}$，奇素位稳定子是 $\mathcal O_{f,\ell}^{\times}$，再乘全局 $K^\times$。这也解释了为何即使 $2\mid f$ 仍应写序导子 $2f$。Bourdon–Clark 的结果还给出 $\mathbb Q(x)$ 对奇偶判别式的区别，而 (2) 表明在各情形原两读数均生成此域。[Clark，Theorem 1.1 与 Remark 1.1](https://arxiv.org/abs/2212.13316) · [Streng，Theorem 2.2](https://pub.math.leidenuniv.nl/~strengtc/reciprocity.pdf)

* **奇 $D$。** $\mathbb Q(\alpha,b)=H$，已经包含 $K$。可从主形直接理解：$\tau_0=(-1+\sqrt D)/2$ 满足 $-\overline{\tau_0}=\tau_0+1$，故复共轭在标记上是换位 $T$。固定主形 $j$ 的 $K$ 上 Artin 作用来自 $(\mathcal O_f/2)^\times$，在 $D\equiv1\bmod8$ 时平凡，在 $D\equiv5\bmod8$ 时为三循环的子群。$D<-4$ 时六标记的 $S_3$ 作用自由，故没有任何反射固定这样的标记。类数比为 $h(4D)/h(D)=2-(D/2)$；从而两个模 8 类的 $6h(D)$ 个标记分别分成三个、一个绝对 Galois 轨道。$D=-3$ 的两标记满足 $x^2-x+1=0,e=0$，式 (1) 给 $\alpha=2-2x,\ b=3-2x$，各自的最小多项式是 $Z^2-2Z+4$、$Z^2-4Z+7$，两值总配成 $b=\alpha+1$。它们已生成 $K=H_2$。
* **偶 $D$。** 主形是纯虚的，其六种标记都是 $\lambda(\tau_0)$ 的有理变换，生成同一个实嵌入下的 $H^{\langle c\rangle}$，$c$ 为复共轭。其它标记的场是此域在 $H/\mathbb Q$ 中的共轭，次数 $h(4D)$。某个给定复嵌入的值可以非实。$D<-4$ 时 $h(4D)=2h(D)$，故共有三个轨道。$D=-4$ 的三个不同 $x=-1,1/2,2$ 全为有理数，$e=0$。

这些式子可直接预测选择子域中未分歧素数的剩余次数。写 $\operatorname{Gal}(H/\mathbb Q)=A\rtimes\langle c\rangle$，$c$ 取逆。若有理素数 $\ell$ 在 $K$ 分裂，令 $n$ 为其一侧在 $A$ 中的 Frobenius 阶，则选择子域中各处的剩余次数皆为 $n$，处的个数是该域次数除以 $n$。若 $\ell$ 在 $K$ 惰性，奇 $D$ 时所有剩余次数均为 2。偶 $D$ 时，设该点的固定反射是 $vc$，选 $\ell$ 的一个 Frobenius 代表 $uc$。在按 $a\in A$ 标记的陪集上，固定点方程为 $a^2=u/v$。因此恰有
$$
 \begin{cases}
 |A[2]|,& u/v\in A^2,\\[1mm]
 0,& u/v\notin A^2
 \end{cases}
$$
个一次素位，余下的标记两两结成二次素位。该判据不依赖 Frobenius 代表的共轭选择。它计数抽象数域的素位；若要从整系数模型中直接约化两比率、区分各个读数，还要剔除分母和不同标记约化相撞的有限个素数。例如 $\tau=i\sqrt5$ 给 $D=-20$。判别式 $-80$ 的四个本原约化型是 $[1,0,20],[3,\pm2,7],[4,0,5]$，中间两型互逆而不等，故 $A=C_4$。将经典 $H_{-20}(j)=j^2-1264000j-681472000$ 与 $j(x)$ 消元，三个整系数四次因子中，$\lambda(i\sqrt5)$ 唯一落在 $16X^4-32X^3+88X^2-72X+1$ 的根上。当 $\ell=11,13$ 时均在 $K$ 惰性，该四次式分别分为 $(X+1)(X+9)(X^2+10X+1)$ 与 $(X^2+4X+9)(X^2+7X+1)$（略去首项单位）。两个反射分裂型均实际出现，因子无重根，足以读出这些素位。

本文解决的是一个确有五维周期系统的分裂对称四次模族，Galois 协变使用指定的水平二标记和 CP19 的实部对数。其它秩五族的 Yukawa 耦合、非零扩张常数及奇行正规化仍要在各自的模族上重新确定。有限证书用 Python 与 python-flint 0.9.0，命令为 `python classfield_check.py --out classfield_checked.json`。
