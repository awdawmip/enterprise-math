# 特征七的 Prym 对应到指定二属曲线，源侧最小次数是二

取 $k=\mathbf F_{49}=\mathbf F_7(i)$，$i^2=-1$。记 $X=C_{46,7}$、$Y=C_7$、$A=J(Y)$。在 R108 指定的两个模型之间，**几何上不存在非常值态射 $X\to Y$。但存在定义于 $k$、几何整的有效对应 $\Gamma\subset X\times Y$，其到 $X$ 的投影可分且次数恰为二。** 对任意非零整同态 $u:J(X)\to A$，这样的对应可以诱导指定的 $u$。给定 $u$ 的极化高度 $H(u)$，可以把另一投影的次数 $d$ 控制在 $2\le d\le H(u)-3$。此外 $H(u)\ge6$；这里没有确定最小高度或最小的另一投影次数。

R108 要求把 $\mathbf F_{49}$ 上的同源分裂接回两条指定曲线，允许以一个精确的次数障碍交付。第 4、5 轮的有理对应和小整数分子位于 $X\times X$，第 59 轮判定 Frobenius 交换的极化正交对；第 13、19、72、95 轮研究主极化商、局部整格和 theta 数据。这里的次数按 $X\times Y$ 中一条几何整曲线的两个投影计。[R108 任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/EMF6D046_R108_HONDA_TATE_CORRESPONDENCE_REDUCTION_GEN2_20260909.md) · [R105 交接](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md) · [第 4 轮](../fourth/honda.md) · [第 5 轮](../fifth/honda_small.md) · [第 59 轮](../fiftyninth/honda.md)

## 1. 两个有限域模型与几何同态的定义域

以下方程均取光滑射影模型。$X$ 的属为五。$z$ 为二重覆盖 $X\to E$ 的对合 $w\mapsto-w$，$O$ 为无穷处唯一的点。属二曲线 $Y$ 有超椭圆对合 $\iota$ 及有理 Weierstrass 点 $W=\infty$。

$$
\begin{aligned}
E&:\ y^2=x^3+x^2+1,\qquad X:\ w^2=y(x^2-5),\\
Y&:\ v^2=F(t)=t^5+(5+6i)t^4+(1+3i)t^3+3it^2+4t+2+4i .
\end{aligned}
$$

源材料给出 $J(X)\sim_k E\times A^2$，$A$ 绝对单纯，且
$\operatorname{End}^0_{\bar k}(A)=\operatorname{End}^0_k(A)=F_0=\mathbf Q(\alpha)$，其中 $h(\alpha)=0$，
$h(T)=T^4+5T^3+245T+2401$。这里 $F_0$ 是四次 CM 域，实子域是 $K=\mathbf Q(\sqrt{417})$。这项几何端代数的稳定性用到了 $h$ 不同根之比不是单位根；仅比较一个有限域上的点数不能单独给出稳定性。[原二属模型与同源证明，§§2–3](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_B_GENUS2_WEIL_RESTRICTION_20260904.md) · [Honda–Tate、绝对单纯及几何端代数，§§4–6](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_HONDA_TATE_20260904.md)

这里也独立核对跨扩域稳定性。置 $y=\alpha+49/\alpha$，则 $y^2+5y-98=0$，两个实根均在 $(-14,14)$；因此 $\alpha^2-y\alpha+49=0$ 在实二次域上不可约。若两个不同的根之比为 $m$ 次本原单位根，其合成域次数至多 $16$，故 $\varphi(m)\le16$。由 $\varphi(m)^2\ge m/2$ 只需枚举 $m\le512$，除 $1$ 外共 $31$ 项。复算为每一项给出一个辅助素数，使 $1,\alpha^m,\alpha^{2m},\alpha^{3m}$ 在模该素数的 $h$ 幂基中满秩。这证明每个幂仍区分四个根；因而任意有限扩域的 Frobenius 在四维 Tate 模上仍有四个互异特征值，中心化子维数保持为四。配合有限域 Tate 定理，这就从同一个 $h$ 复核了所用的几何端同态结论。

因此 $\operatorname{Hom}_{\bar k}(E,A)=0$。在上述 $k$-同源坐标中，$\operatorname{Hom}^0_{\bar k}(JX,A)$ 是 $F_0$ 上的二元行向量空间，已全部在 $k$ 上有定义。整同态群无挠，故 Galois 若固定整同态的有理类，就固定整同态本身。以下所有非零 $u:JX\to A$ 都是 $k$-同态，且因 $A$ 单纯均为满射。

## 2. 五个源点迫使图分支为空

$X\to E$ 的几何支点为无穷点、$y=0$ 的三点及 $x^2=5$ 的四点。函数 $y(x^2-5)$ 的七个有限零皆简单，在无穷点的极阶为七。三次式 $x^3+x^2+1$ 在 $k$ 上无根；$x=3i,4i$ 两种情形各有两个 $k$-有理 $y$ 值。因此八个固定点的 $49$ 次 Frobenius 轨长为 $(1,1,1,1,1,3)$。另一方面，
$$
F(t)=(t^2+(6+6i)t+6+6i)
      (t^3+6t^2+(1+3i)t+4+6i)
$$
的两因子均在 $k$ 上不可约，故 $Y$ 的六个 Weierstrass 点轨长为 $(1,2,3)$。特别是 $W$ 为唯一 $k$-有理 Weierstrass 点。

对任一几何非常值态射 $f:X\to Y$，用 $j_X(x)=[x-O]$、$j_Y(y)=[y-W]$ 作 Abel 嵌入，写
$$
j_Y f=u j_X+t,\qquad u=f_*,\quad t=j_Y(f(O)).
$$
$\Theta=j_Y(Y)$ 给出主极化，任何保持这个除子的平移都属于 $\ker\lambda_\Theta=0$。因 $u$ 已在 $k$ 定义，对每个 $\sigma\in\mathrm{Gal}(\bar k/k)$，$\sigma(t)-t$ 平移 $\Theta$ 至自身（$f$ 满到 $Y$），故 $t$ 以至 $f$ 本身都在 $k$ 定义。

又因 $1+z_*$ 在 $JX$ 上经椭圆商 $E$ 分解，$u(1+z_*)=0$；$z(O)=O$。超椭圆对合在 $j_Y$ 坐标中为负号。于是 $j_Y f z=-j_Y f+2t$，同样由 $\Theta$ 的平移稳定子为零得 $2t=0$ 和 $fz=\iota f$。这迫使五个不同的 $k$-有理 $z$-固定点全映到 $W$。若 $f$ 可分，则
$$
5\le\deg f\le \frac{2g(X)-2}{2g(Y)-2}=4 .
$$
右界来自 Riemann–Hurwitz，允许分歧。若 $f$ 含不可分部分，先从源剥去 $7^a$ 次相对 Frobenius，剩下可分态射 $X^{(7^a)}\to Y$。$X$ 来自 $\mathbf F_7$，每个源 twist 都同构于 $X$，可分情形的矛盾仍成立。反向 $Y\to X$ 的可分部分直接由属排除。因此任一几何整且两个投影均占优的 $\Gamma\subset X\times Y$，**两个投影的可分度都至少为二**。确实，若一个投影纯不可分，正规化曲线就是相应因子的逆 Frobenius twist：一维函数域 $K'$ 满足 $[K':K'^{\,7^a}]=7^a$，而 $7^a$ 次纯不可分子扩张必含 $K'^{\,7^a}$。若该因子为 $Y$，其任意 twist 仍只有属二。

这个障碍逐曲线取决于 Weierstrass 点的轨道，而非单靠 Weil 多项式。对任意同一 $k$-同源类中的属二 Jacobian，六点置换模去两个平凡组成因子后才给 $J[2]$，故六点置换的模二特征多项式为 $(T+1)^2 h(T)\bmod 2$。列举六的分拆，相容轨型有 $(1,2,3)$ 和 $(1,1,1,3)$ 两种。本文对前一种的同源模型同样排除图；后一种单凭五个源点不能排除，其实际出现也不由分拆计算保证。对指定 $Y$，$\mathbf F_{49^n}$ 上的两侧固定点数分别为 $5+3\,\mathbf1_{3\mid n}$ 与 $1+2\,\mathbf1_{2\mid n}+3\,\mathbf1_{3\mid n}$。裸计数的矛盾恰在 $(n,6)=1$ 出现，几何全域的否定借助了前述下降。

## 3. 源侧次数二可达，另一侧能省下三个交点

对原有的任一非零整同态 $u$，记 $\psi_0=u j_X$。取 $t\in A(k)$ 并以 $2W$ 将 $\mathrm{Pic}^2(Y)$ 与 $A$ 认同，令 $\psi=\psi_0+t$。属二 Riemann–Roch 给每个二次线丛一个唯一的有效代表，唯一例外为典范类 $K_Y=2W$，其线性系为 $\mathbf P^1$。故 $\psi$ 在稠密开集上给出映到 $\mathrm{Sym}^2(Y)$ 的提升；$\psi$ 非常值且 $X$ 光滑，该提升在每个点由适当性唯一延拓，记为 $\widetilde\psi$。拉回对称平方上的万能次数二除子，得到 $\Gamma_t\subset X\times Y$，在 $k$ 上定义并对 $X$ 有限平坦、次数二。对两个源点作纤维之差，其 Abel 类等于 $u([x-x'])$；故对应确实诱导指定的整同态。

在 $\bar k(X)$ 上，若该二点除子分裂或非约化，就由两个有理点组成（可重合，特征为七）。这两点各延成 $X\to Y$ 的态射，上一节迫使它们都常值，与 $\psi$ 非常值矛盾。因此几何泛纤维是可分二次域。由有限平坦性，整张对应几何整，另一个投影亦占优。这个构造证明第一投影次数的确切最小值，只依赖任一已存在的 $u$。对实际 Frobenius 分裂的秩一分量，可先选从该像至 $A$ 的同源，复合有理投影后清分母得到此类 $u$。从 $u$ 也可回得自伴秩一有理投影 $u^\dagger(uu^\dagger)^{-1}u$。此处没有选定那条同源的方程，也没有给出最优双次数的一组显式定义式。

定义 $H(u)=\deg\psi_0^*\mathcal O_A(\Theta)$。属二 Abel 映射 $\alpha:\mathrm{Sym}^2(Y)\to A$ 是在 $0=[K_Y-2W]$ 的吹起，记例外曲线为 $D$。一个直接理由是 $\alpha$ 在 $0$ 以外为同构，唯一收缩的光滑曲线 $|K_Y|\simeq\mathbf P^1$ 自交数为 $-1$：在 $Y\times Y$ 的二重商上，其逆像为超椭圆对合的图像，泛点处重数一，图像自交数为 $2-2g(Y)=-2$。由光滑曲面的 $(-1)$ 曲线收缩即得。对每个 $y\in Y$，固定一个坐标为 $y$ 的除子 $X_y\subset\mathrm{Sym}^2(Y)$ 是 $\Theta$ 的一个平移的严格变换；这条平移在 $0$ 光滑、重数一。因而投影至 $Y$ 的次数为
$$
d_t=\deg\widetilde\psi^*\mathcal O(X_y)
    =H(u)-\deg\widetilde\psi^*D. \tag{1}
$$
任一平移不改变曲线上拉回的线丛次数。对每个满足 $\psi(x)=0$ 的几何点，末项至少贡献一，可按重数更大。

因 $u(1+z_*)=0$ 且 $O$ 为固定点，五个有理固定点在 $\psi_0$ 下落入 $A[2](k)$。由六个 Weierstrass 点的偶子集模去补集可得此群的阶恰为二：固定点 $W$ 使稳定的子集不可能送到自身的补集，而 $(1,2,3)$ 的稳定偶子集仅四个，再除以补集配对。故可选 $k$-有理二挠平移 $t$ 把至少三点同时送到中心。结合 (1) 及第 2 节，两侧次数达到
$$
(\deg_X,\deg_Y)=(2,d_t),\qquad 2\le d_t\le H(u)-3 .
$$

## 4. 由实际 Weil 实子域再限制极化高度

所有伴随以两个 Jacobian 的典范主极化定义。$v=uu^\dagger$ 是 $A$ 上的整自同态。CM 域上 Rosati 为复共轭，$v\in\mathcal O_K$ 且在两个实位全正：$u$ 满射，$v$ 对应对偶同态从 $JX$ 拉回的 ample 极化，是正自伴同源。对 $\ell\ne7$，Abel 曲线类的 Poincaré 公式以及阿贝尔簇 Riemann–Roch 给
$$
H(u)=\tfrac12\operatorname{Tr}_{V_\ell JX}(u^\dagger u)
    =\tfrac12\operatorname{Tr}_{V_\ell A}(v)
    =\operatorname{Tr}_{K/\mathbf Q}(v). \tag{2}
$$
具体地，$\chi(t\Theta_X+u^*\Theta)$ 的次首系数是 $\Theta_X^{4}\cdot u^*\Theta/4!=H(u)$，而它的平方为 $\det(tI+u^\dagger u\mid V_\ell JX)$。再用矩形乘积迹的循环不变性以及 $V_\ell A$ 在 $F_0\otimes\mathbf Q_\ell$ 上秩一即得 (2)。

$417$ 无平方因子且 $\equiv1\bmod4$。写 $v=(H+b\sqrt{417})/2$，$b\equiv H\bmod2$。若 $b\ne0$，全正性给 $H>|b|\sqrt{417}$；若 $b=0$，则 $H$ 是偶数。第 3 节已迫使 $H\ge5$，现在得到
$$
H(u)\ge6,\qquad H(u)\le20\ \Longrightarrow\
u u^\dagger=[H(u)/2]\text{ 且 } H(u)\text{ 为偶数}.
$$
这里的界适用于指定曲线间每一个非零整同态；二次整对应的第二投影最优值仍取决于实际同态与撞到吹起中心的重数。

## 5. 复算

运行 `python3 weil_check.py`（Python 3.10 以上，仅标准库）。程序逐点计数，直接求五次式与 $T^{49^j}-T$ 的最大公因式；再从实际六点置换枚举 $16$ 个二挠类，独立从两层点数恢复 Weil 多项式。有限核验的数据为

| 域大小 | $\#X$ | $\#E$ | $\#Y$ | 源有理固定点 | 靶有理 Weierstrass 点 |
|---:|---:|---:|---:|---:|---:|
| $49$ | 65 | 55 | 55 | 5 | 1 |
| $2401$ | 2425 | 2475 | 2377 | 5 | 3 |

几何同态下降、不可分分解、整对应的存在与高度界由上述论证给出。[复算程序](weil_check.py) · [整域输出](weil_checked.json)
