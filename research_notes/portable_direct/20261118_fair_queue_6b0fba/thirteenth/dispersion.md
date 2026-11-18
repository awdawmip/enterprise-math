# 三次高斯和校正平方的三个系数与粗糙性障碍

任务 RS-OAI7-023-B-20261007-6F2A81，审计对象是指定外稿命题 prop:dispersion 的第二项。主项确实以相同常数、相同算术总和闭合。三项来自三个不同计算：正平方作 Poisson 求和，交叉项作 Type I 比较，模型项可直接求值。下面还给出固定小素理想的反例，且写出不施加粗糙性时局部互素约束的 Gram 核。原稿的其他解析估计作为明确输入列在表中。[任务书](https://github.com/awdawmip/enterprise-math/blob/a71f6c994705dba12addf03fd76826f5ffa947ab/research_tasks/RS-OAI7-023-B-20261007-6F2A81.md) · [外稿命题及推导](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dispersion.tex) · [复算程序](dispersion_check.py) · [结果](dispersion_checked.json)

## 一、精确平方与求和域

记 $\mathcal O=\mathbb Z[\omega]$，$\omega^3=1,\ \omega\ne1$，$\lambda=\sqrt{-3}$，$N z=|z|^2$。理想均取与 $3$ 互素、模 $3$ 同余于 $1$ 的唯一主生成元。归一化三次 Gauss 和满足 $|G(a)|=\mu^2(a)$，$G(ab)=G(a)G(b)\overline{\chi_b(a)}$，非互素时乘法式两侧同为零。设 $AB\asymp X$，$X^{.32}\le B\ll X^{1/2}$，$H=B^2/A$，$\mathcal Q=ABH^{1/3}=A^{2/3}B^{5/3}$，$L=\log X$。令
\[
 b_u=\beta_b(Nb)^{iu},\quad w_b=b_u(Nb)^{-1/6},\quad S=\sum_b w_b,\quad
 F(a)=\sum_b b_uG(b)\overline{\chi_b(a)},\qquad c_*=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)}.
\]
$\beta$ 有固定除数型界，支撑为 $Nb\asymp B$ 的平方自由理想。外稿低高度强校正要求 $|u|\le L^{O(1)}$、带排除条件的三次 Hecke 特征 Siegel–Walfisz 性质、所有支撑素因子范数大于 $L^{C_r}$ 以及 $H\ge L^{C_g}$。$B>X^{.40}$ 时还有光滑素数卷积条件。$W_A(a)=W(a/\sqrt A)$ 为固定非负光滑径向环带权。以下记 $T=\sum_a\mu^2(a)W_A(a)(Na)^{-1/3}$，$M=c_*^2|S|^2T$。[定义与乘法](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/background-type1.tex#L25-L55)

直接展开，三个**精确**贡献为
\[
 P=\sum_a\mu^2(a)W_A(a)|F(a)|^2,\quad
 -2\Re\left[c_*\bar S\sum_{a,b} b_u W_A(a)(Na)^{-1/6}G(ab)\right],\quad +M. \tag{1}
\]
第二个和可写全体主生成元，因为 $G(ab)$ 已编码平方自由和互素性。$P$ 仅有上界 $M+O(\mathcal Q L^{-K})$ 就够用。外稿的筛替换为 $\mu^2(a)\le(\sum_{c^2|a,Nc\le L^{D_0}}\mu(c))^2=\sum_{d^2|a}\lambda_d$，只需对非负的 $W_A|F|^2$ 施行。各个 $\lambda_d$ 可以为负。模型与交叉项保留真实平方自由权；若始终显式保留 $G(a)$，两项在非平方自由处已经是零。移除该因子后，仅凭筛权的逐点大小无法处理有符号的实部。

**正平方的立方频率。** $b_1,b_2$ 的对角单列。对非对角项按 $f=(b_1,b_2), b_i=fp_i$ 分解，$m\mid f$ 去除 $(a,f)=1$，$l$ 来自对 $(p_1,p_2)=1$ 作 Möbius 反演。原始 Poisson 恒等式针对互素 $p_1,p_2$；先延拓所显示的表达式再施行 $l$ 反演，人工加入的重复对在反演中抵消。用下表的估计去除非单位 $f,l$ 后 $f=l=m=1$，$d$ 平方自由、$Nd\le L^{2D_0}$。保留 $h\ne0$ 且 $dh$ 为立方的非零频率，即 $h=d^2j^3,\ j\in\mathcal O\setminus\{0\}$，还需 $(j,b_1b_2)=1$。每个 $h$ 正好三重计数；$d\equiv1\bmod3$、立方模 $3$ 同余有理整数，故 $e(\operatorname{Tr}(h/(3\lambda)))=1$。Poisson 前因子为 $A\lambda_d/(9(Nd)^2\sqrt{Nb_1Nb_2})$ 乘 $b_{1,u}\bar b_{2,u}$，此处 $b_{i,u}=\beta_{b_i}(Nb_i)^{iu}$。除去互素条件的格点体积为
\[
 \frac13\left(\frac{27N(b_1b_2)}A\right)^{1/3}
 \int\widehat W(z^3)\,d\mathfrak m(z),\qquad
 d\mathfrak m=\tfrac2{\sqrt3}\,d\Re z\,d\Im z.
\]
乘积的代数因子恰为 $A^{2/3}\lambda_d w_{b_1}\bar w_{b_2}/(9(Nd)^2)$。迹配对按实二维变换使用两倍频率；立方换元给 Jacobian 因子 $1/3$。Riesz 积分 $\int\widehat W(z^3)d\mathfrak m=c_*^2\int W(y)|y|^{-2/3}d\mathfrak m(y)$，可用二维高斯积分与 $\Gamma(1/3)\Gamma(2/3)=2\pi/\sqrt3$ 复核。$\sum\lambda_d/(Nd)^2$ 换为 $\sum\mu(d)/(Nd)^2$ 后乘主生成元的密度 $1/9$，正好产生 $M$。[Poisson 规范化](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dispersion.tex#L160-L216) · [立方计数与常数](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dispersion.tex#L499-L590)

**交叉项。** 外稿 Type I 命题取 $R=B,U=A$，将 (1) 内层双和替为
\[
 c_*\sum_b w_b\,T_A(b)+O(A^{-1/6}X^{5/6-\eta}),\qquad
 T_A(b)=\sum_{(a,b)=1}\mu^2(a) W_A(a)(Na)^{-1/3}.
 \tag{2}
\]
$(Na)^{-1/6}$ 在光滑权中提走 $A^{-1/6}$。由于 $S\ll B^{5/6}L^{O(1)}$，该解析余项乘上 $\bar S$ 的成本为 $O(\mathcal Q X^{-\eta}L^{O(1)})$。粗糙支撑允许 $T_A(b)$ 换为 $T$，于是交叉项为 $-2M+O(\mathcal Q L^{-K})$，模型平方恰为 $M$。三项从而在相同规范化下以 $1,-2,1$ 相消。交叉项没有按 $h$ 逐点进行 Poisson 对消。[Type I 命题](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/background-type1.tex#L499-L513)

| 剩余项 | 条件、量级与所用来源 |
|---|---|
| 筛后对角与筛系数截断 | 对角 $O(AB L^{O(1)})$ 相对 $\mathcal Q$ 节省 $H^{-1/3}$，需 $C_g$ 大。因 $Nd\le L^{D_0}$ 时 $\lambda_d=\mu(d)$，密度误差为 $O(L^{-D_0/2})$。 |
| 大公因子和大/中导子非立方频率 | 外稿用三次大筛、普通大筛与例外构型的对偶估计；在 $B$ 接近 $X^{1/2}$ 用到素数卷积假设。仅审计如何调用与归一化。 |
| 非平凡 $f,l$ 及小导子 | 支撑粗糙性使其范数超过 $L^{C_r}$，对相应尾部取任意对数节省。余下小导子非立方使用带互素排除的 (SW)，高 Mellin 平移用快速衰减。 |
| 非零 $j$ 的格点数 | 外稿误差 $O(H^{1/6}+1)$，主量为 $H^{1/3}$；恢复 $(j,b_1b_2)=1$ 的粗估成本 $O(H^{1/3}\sum_{\pi|b_1b_2}1/N\pi)$。下文给出保留局部密度的独立写法。 |
| 平方自由格点与 (2) | 原稿平方自由未加权计数的绝对误差 $O_\epsilon(A^{1/2+\epsilon})$，当前权乘 $A^{-1/3}$。Type I 的幂次节省与交叉项归一化如 (2)。取 $D_0$ 后取 $C_r>2D_0$ 足够大，最后取 $C_g$。 |
| 较短过渡区 | $1\ll H<L^{C_g}$ 使用原稿的未校正式；以上三项抵消所得的任意对数节省仅用于长区间。 |

## 二、把小素理想留在系数里

写 $\rho_b=\prod_{\pi|b}(1+1/N\pi)^{-1}$。对任意固定非零非负 $W$ 及 $Nb\le X^{O(1)}$ 有
\[
 T_A(b)=C_W A^{2/3}\rho_b+O\!\left(A^{1/6}\log(2A)\tau(b)\right),\quad
 C_W=\frac19\prod_{\pi\nmid3}(1-(N\pi)^{-2})
        \int W(y)|y|^{-2/3}\,d\mathfrak m(y)>0 . \tag{3}
\]
证明：对平方自由和互素性分别反演，得 $(d,b)=1,\ e|\operatorname{rad}(b)$，写 $a=d^2e v$，$v$ 取主生成元。每一格点和的未归权主量为常数乘 $A/[(Nd)^2Ne]$，误差为 $O(1+\sqrt{A/Ne}/Nd)$，来自基本平行四边形上的一阶光滑余项。由于支撑截断，$Nd\ll\sqrt{A/Ne}$；每个 $e$ 的误差和及主项补尾不超过 $O(\sqrt{A/Ne}\log(2A))$，对 $Ne\gg A$ 仅有同样可控的主项尾。加回权的 $A^{-1/3}$ 后即得。指定 $\pi|b$ 将局部因子从 $1-q^{-2}$ 改为 $1-q^{-1}$，比值正是 $q/(q+1)$。这也给 (2) 中混合项的精确首系数 $\sum_b w_b\rho_b$。在粗糙集合内 $0\le1-\rho_b\le\sum_{\pi|b}1/N\pi\ll\log B/L^{C_r}$。

由此还可确定最佳单个校正系数。令 $m(a)=c_*\overline{G(a)}(Na)^{-1/6}$，在权 $\mu^2(a)W_A(a)$ 下对 $F$ 作到 $m$ 的正交投影，得到 $s_{\rm opt}=\langle F,m\rangle/(c_*^2T)$（内积对第一变量线性）。(2) 和 (3) 给出
\[
 s_{\rm opt}=\sum_b w_b\rho_b+
 O\!\left(\frac{A^{-1/6}X^{5/6-\eta}
 +A^{1/6}\log(2A)\sum_b|w_b|\tau(b)}{A^{2/3}}\right).
\]
这里只使用明确标注的 Type I 比较与光滑格点计数，允许小素因子。对任意 $s\in\mathbb C$，实际加权误差精确分解为最小误差加上 $c_*^2T|s-s_{\rm opt}|^2$。最佳系数也不能单独控制与 $m$ 正交的其余能量。

**局部互素约束的方差分解。** 只考察模型中的算术筛选 $Y(a)=\sum_{(a,b)=1} w_b$。在平方自由主理想的极限分布中，有限个素理想是否整除 $a$ 是独立 Bernoulli 变量，命中 $\pi$ 的概率为 $1/(N\pi+1)$。这由 (3) 对有限集合容斥得到。对平方自由 $b,c$，两列的 Gram 核及整个模型的方差精确为
\[
 K(b,c)=\rho_{[b,c]}=\rho_b\rho_c\sum_{d|(b,c)}(Nd)^{-1},\qquad
 {\rm Var}(Y)=\sum_{d\ne(1)}\frac1{Nd}
     \left|\sum_{d|b}\rho_b w_b\right|^2. \tag{4}
\]
这里 $d$ 遍历非单位理想。将中间 Euler 乘积按共同素因子展开得第一式；对有限复系数二次型求和，$d=1$ 的项恰为 $|\mathbb E Y|^2$。有限 $A$ 的单项核误差经 (3) 控制；若支撑随 $X$ 增长，可以用各对系数绝对值加权相加。式 (4) 描述的是局部互素模型。实际高斯和的其他相位与非单位 $f,l$ 在低粗糙度下仍需单独估计。

同一个局部信息也可保留到非零立方的格点计数中。令 $g(z)=\widehat W(z^3)$，对任意 $R>0$ 有 $\sum_{j\ne0}g(j/R)=R^2\int g\,d\mathfrak m+O_g(1)$。$R\ge1$ 时对 Schwartz 函数用全格点 Poisson 再去原点，$R<1$ 时直接用衰减。径向性排除了复旋转的影响。故
\[
 \sum_{\substack{j\ne0\\(j,t)=1}}g(j/R)
 =R^2\prod_{\pi|t}(1-1/N\pi)\int g\,d\mathfrak m+O_g(2^{\omega(t)}).
\]
此处是全部 $j$ 的自然密度 $1-1/q$；(3) 的 $q/(q+1)$ 则来自平方自由 $a$，两个因子须分别保留。

## 三、去掉粗糙性会实际失败

固定 $\pi\nmid3$，$q=N\pi$，取 $B=X^{3/8}, A=X^{5/8},u=0$ 及
$\beta_b=\mu^2(b)\mathbf1_{\pi|b}V(Nb/B)$，其中 $V$ 为固定、非负、非零的光滑环带函数。$B<X^{.40}$ 且 $H=X^{1/8}$。当 $\pi|a$ 时，每一项 $\chi_b(a)=0$，故 $F(a)=0$。由 (3) 的同一格点估计（换用指数 $-1/6$ 或 $-1/3$），有 $S\sim C_V B^{5/6}/(q+1)$，并且
\[
 \sum_{\pi|a}\mu^2(a)W_A(a)(Na)^{-1/3}
 \sim C_W A^{2/3}/(q+1).
\]
此处 $C_V>0$ 是无 $\pi$ 限制时的光滑平方自由密度常数。仅这一片就让原校正平方的左侧至少达到
\[
 (c_*^2 C_V^2 C_W+o_\pi(1))\,\frac{\mathcal Q}{(q+1)^3}.
\]
占该组系数自身模型能量的份额是 $1/(q+1)$。这一障碍不依赖 Type I 或三次大筛。

该例保留外稿所需的 (SW)。若指定排除或特征模包含 $\pi$，相应和为零；否则写 $b=\pi v$ 并施加 $(v,\pi m)=1$。对平方自由与排除条件作 (3) 的两次反演。有限阶非主射线特征在主生成元的完整剩余周期内和为零。对一个平滑环带范数尺度 $Y$，按模理想的平行四边形分格，含高度不超过对数幂的范数扭曲后，每个剩余类的误差由 $L^{O(1)}(\sqrt Y+1)$ 统控；剩余类数也是对数幂。对各 $d,e$ 求和，成本 $\ll \tau(m\pi)L^{O(1)}\sqrt B=B^{1/2+o(1)}$，其中 $Nm\le X^{O(1)}$。因此仅有特征等分布和宽区间仍不足以恢复原稿的常系数模型。若要扩大适用支撑，(4) 给出了可直接检验的局部条件；非立方频率与共享素因子的其余贡献仍是开放部分。这里的计算均在经典艾森斯坦整数及有限复数和上进行。
