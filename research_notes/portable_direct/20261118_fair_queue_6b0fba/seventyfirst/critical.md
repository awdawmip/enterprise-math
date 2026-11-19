# 锚定道路在临界窗中的非零频谱和真实能量尾

登记 RS-RH-COMPOSITE-ROAD-ANCHORED-COHERENCE 的第15轮研究给出了固定分母截断的锚定核及真实序列的无条件尾下界。其式 (2) 包含一个相干的常数频率通道，以下只从其中抽取非零频率，并独立返回真实序列。原研究的定理2只陈述到 $a=1/2$，其证明不能原样提供临界窗两侧的一致常数。[原任务书](https://github.com/awdawmip/enterprise-math/blob/6f9abc50893bb8fde31627f5580af7ab92a6835b/research_tasks/RS-RH-COMPOSITE-ROAD-ANCHORED-COHERENCE_20260909.md) · [原路分解](https://github.com/awdawmip/enterprise-math/blob/bf181bfa6c4f1fdbe4ddf6352385c5f4b819cc53/research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md)

## 1. 分母谱的统一二项式

设 $R_a(n)=\sum_{d\mid n}\mu(d)d^{-a}$，$c_a=1/\zeta(1+a)$，$B_n=\sum_{k\le n}(R_a(k)-c_a)-1-c_a/2$。对 $q\ge2$ 写 $b_q=c_a\mu(q)/\prod_{p\mid q}(p^{1+a}-1)$，$J_2(q)=q^2\prod_{p\mid q}(1-p^{-2})$。原非零频谱正好为
\[
 E_a(Q)=\frac1{12}\sum_{2\le q\le Q}|b_q|^2J_2(q)
 =\frac{c_a^2}{12}\left[\sum_{q\le Q}h_a(q)q^{-2a}-1\right],\quad
 h_a(q)=\mu(q)^2\prod_{p\mid q}\frac{1-p^{-2}}{(1-p^{-1-a})^2}.
\]
其中 $-1$ 排去 $q=1$。

记 $H_p=h_a(p)$，$g_a=h_a*\mu$，$G_a(z)=\sum_d g_a(d)d^{-z}$。$g_a(p)=H_p-1=O(p^{-1-a}+p^{-2})$，$g_a(p^2)=-H_p$，更高次幂为零。故 $G_a$ 的级数和 Euler 积在 $\Re z>1/2$ 绝对收敛，紧子集上一致，包括在 $a$ 的任意固定紧正区间对 $a,z$ 取任意固定阶导数。这里并不要求无权 $\sum_d|g_a(d)|$ 收敛。交换约数求和即得
\[
 \sum_{n\le x}h_a(n)=G_a(1)x+O(x^{3/4}).
\]
尾误差与取整误差都由 $\sum_d |g_a(d)|d^{-3/4}$ 控制。记 $s=2a$。对任意固定临界邻域 $|s-1|<1/8$，部分求和给出
\[
 \sum_{q\le Q}h_a(q)q^{-s}
 = \zeta(s)G_a(s)-G_a(1)\frac{Q^{1-s}}{s-1}
       +O(Q^{3/4-s}).
\]
此式先于 $s>1$ 成立。将计数余项自 $Q$ 积至无穷的积分在 $\Re s>3/4$ 绝对收敛，右侧差的奇点可去，因而无需对截尾误差分别乘上可能无界的 $1/|s-1|$。

令 $L=\log Q$，$\eta=(2a-1)L$，$\Phi(u)=(1-e^{-u})/u$ 且 $\Phi(0)=1$。星号表示 $a_*=1/2$。定义
\[
 A(a)=c_a^2G_a(1)/12,\qquad B_* = c_*^2\{\gamma_{\rm E}G_*(1)+\partial_zG_*(1)-1\}/12.
\]
则对 $|\eta|\le K$ 一致有
\[
 E_a(Q)=A_*L\Phi(\eta)+B_* +\tfrac12 A'(1/2)(1-e^{-\eta})+O_K(L^{-1}).
\]
这是 $\zeta(1+v)=v^{-1}+\gamma_{\rm E}+O(v)$ 的直接展开。使用 $A(a)$ 来写主项时无须最后的漂移补项。$G$ 线性项取对 $z$ 的导数，$A'$ 取对 $a$ 的导数。各常数均为可直接求值的收敛 Euler 表达式：
\[
 A(a)=\frac1{12}\prod_p(1-p^{-1})[(1-p^{-1-a})^2+p^{-1}(1-p^{-2})],\qquad
 A_*=\frac1{12}\prod_p(1-p^{-1})(1+p^{-1}-2p^{-3/2})>0.
\]
$A'(a)/A(a)$ 是各因子对数导数之和，每项分子为 $2(\log p)p^{-1-a}(1-p^{-1-a})$、分母为上述方括号。$G_a(z)=\prod_p(1-p^{-z})(1+H_pp^{-z})$。临界点本身特别给出 $E_{1/2}(Q)=A_*\log Q+B_*+O(Q^{-1/4})$。

## 2. 除去扭和估计中的对数

下文可固定 $2/5\le a\le3/5$ 并取临界子窗。对任一本原 $z=e^{2\pi i r/q}$ 和 $Y\ge X$，$2\le q\le X^{1/3}$，有一致绝对误差
\[
 \sum_{n\le Y}(R_a(n)-c_a)\bar z^n =Y b_q+O(Y^{1-a}).
 \tag{1}
\]
这里前和原点固定，$Y$ 为实数也只影响整部。把约数 $d\le Y$ 提出。$q\mid d$ 的项和 $Y\sum_{q\mid d}\mu(d)d^{-1-a}=Yb_q$ 之差由取整和 $d>Y$ 尾共同给 $O(Y^{1-a})$，包括非平方自由 $q$。常数项 $c_a$ 的非零频率和为 $O(q)$。$q\nmid d$ 的几何和绝对值同时受
\[
 \min(Y/d, |\sin(\pi rd/q)|^{-1})
\]
控制。$d$ 在一个周期内跑遍非零余数，给 $T\ge1$ 时的截断周期界
\[
 \sum_{j=1}^{q-1}\min(T,|\sin(\pi j/q)|^{-1})\le q(1+\log T).
\]
证明用 $1/|\sin(\pi j/q)|\le q/(2\min(j,q-j))$；在半周取单调函数 $\min(T,1/(2x))$ 的右端点和，至多为其积分的 $2q$ 倍。先收去 $d\le2q$，其贡献 $O(q\log(2q))=O(Y^{1-a})$。其余在 $D<d\le2D$, $D\ge q$ 分组，单个余数至多 $2D/q$ 次，块界为
\[
 O\big(D^{1-a}(1+\log(Y/D))\big).
\]
从 $Y$ 向下作二分，以 $\sum_{k\ge0}(k+1)2^{-k(1-a)}=O(1)$ 回收全体块，余数段落始终可取至 $2q$。这一步利用大 $d$ 时可用的真实几何和长度，消去了第15轮下面式 (7) 的对数损失。对固定 $0<a<1/2$ 也可用 $q\le C_a X^{a/(1+a)}$，因 $a/(1+a)<1-a$ 且 $a/(1+a)<1/2$。

## 3. 真均方与带权尾，保留谱截断首常数

设 $\xi=(2a-1)\log X$，$|\xi|\le K$，$Q=\lfloor X^{1/3}\rfloor$。记原尾 $T_a(X)=\sum_{n>X}|B_n|^2/n^2$ 与 $s_X=\sum_{n>X}n^{-2}$。取两种概率权重
\[
 \nu_n=X^{-1}{\bf1}_{X<n\le2X},\qquad
 \text{或}\qquad\nu_n=s_X^{-1}n^{-2}{\bf1}_{n>X}
\]
（$X$ 为正整数）。对前者用式 (1) 两端相减；对后者从 $X$ 对该式 Abel 求和。均得到 $\sum\nu_n(R_a(n)-c_a)\bar z^n=b_q+O_K(X^{-a})$。注意 $Y$ 可延至无穷，但在该积分中 $a$ 固定于所选 $X$。由 $B_n\ll n^{1-a}$（从约数取整即得），把一次差分移到频率上后，
\[
 \left|(1-\bar z)\widehat B_\nu(z)-b_q\right|\ll_K X^{-a}.
 \tag{2}
\]
尾情形的新边界取决于 $\nu_{X+1}|B_X|+\sum_{n>X}(\nu_n-\nu_{n+1})|B_n|=O_K(X^{-a})$，频率的相位只贡献单位模。有限窗有两个端点，误差同阶。

有限既约频率的间距至少 $Q^{-2}$。两种权重下互异频率的归一 Gram 元都 $\ll X^{-1}/|1-z\bar w|$；尾权用 Abel 与 $\nu_{X+1}\asymp X^{-1}$ 即得。沿左右半圆依距离逐项求和，Gram 算子范数 $\le1+O(Q^2\log(2Q)/X)$。其频率系数的平方和至多为这个常数乘真实均方，真实尾若无限下界自动成立。另一方面，由 $|b+e|^2\ge |b|^2-2|b||e|$、$\sum_{(r,q)=1}|1-e(r/q)|^{-2}=J_2(q)/12$ ($q>1$) 及 $|b_q|\le q^{-1-a}$，得到
\[
 \sum_z |\widehat B_\nu(z)|^2\ge E_a(Q)-O\left(X^{-a}\sum_{q\le Q}|b_q|J_2(q)\right)
 \ge E_a(Q)-O_K(X^{-a}Q^{2-a})=E_a(Q)-O_K(1).
\]
非零 $q$ 的比较在平方后再按分母合并。逐个要求相对误差趋零会损失 $\log\log X$。临界窗 $E_a(Q)=O_K(\log X)$，故 Gram 的剩余乘法损失为 $o(1)$。由此
\[
 \min\left(\frac1X\sum_{X<n\le2X}|B_n|^2,~\frac{T_a(X)}{s_X}\right)
 \ge E_a(\lfloor X^{1/3}\rfloor)-O_K(1)
 \ge A_*\log X\,\frac{1-e^{-\xi/3}}{\xi}-O_K(1).
\]
在 $\xi=0$ 比值取 $1/3$。这给固定锚点的真实下界；尚无相匹配的上界，不能把截断谱当成真实均方恒等式。

对固定 $0<a<1/2$，取 $Q=\lfloor c'_a X^{a/(1+a)}\rfloor$ 并使 $c'_a>0$ 足够小。各平方自由 $q\le Q$ 有 $|b_q|\ge c_a q^{-1-a}$，式 (2) 的误差遂逐项至多是原值的一半。Gram 余项趋零，平方自由数密度给出
\[
 T_a(X)\gg_a X^{-1+a(1-2a)/(1+a)}.
\]
与原第15轮式 (7) 相比，这里去掉了分母中的对数幂。临界窗结果同时适用于 $a$ 略大于 $1/2$，但不构成 RH、未截能量或零点的推断。


## 4. 临界下界还可增加任意固定倍的 $\log\log X$

记 $L=\log X$，$\mathcal M_a(X)$ 为第 3 节两种真实均方的较小者。对每个**固定** $b>0$，取 $Q_b=\lfloor X^{1/3}L^b\rfloor$。当 $|\xi|=|(2a-1)L|\le K$ 时，一致有
\[
 \mathcal M_a(X)\ge E_a(Q_b)-o_{b,K}(1)
 \ge A_* L\,\frac{1-e^{-\xi/3}}{\xi}
       + b A_* e^{-\xi/3}\log L-O_{b,K}(1). \tag{3}
\]
特别地，从真实均方中减去右侧的首项后，所得差除以 $\log\log X$ 一致趋于正无穷。这里只逐个固定 $b$ 后令 $X$ 增长，所用渐近阈值一般无有效数值。

所需的经典输入是 Davenport 对 Möbius 函数的加性扭和估计。写 $e(t)=e^{2\pi it}$，则对每个 $M>0$ 和 $u\ge2$，
\[
 \sup_{\theta\in\mathbb R}\left|\sum_{d\le u}\mu(d)e(d\theta)\right|
 \ll_M u(\log(2u))^{-M}.
\]
这一形式包括 $\theta=0$，隐常数与相位的分母无关。[Davenport，1937，313–320 页](https://doi.org/10.1093/qmath/os-8.1.313) · [Green–Tao，引言式 (1.1) 及非有效常数的说明](https://arxiv.org/pdf/0807.1736)

**扭和与端点。** 取 $2/5\le a\le3/5$，固定 $b,H>0$，$Y\ge X$，$q\le X^{1/3}(\log X)^b$。取 $D=Y/(\log Y)^E$，其中 $E$ 为稍后选定的常数，因此当 $X$ 充分大时有 $2q\le D$、$\log D\asymp\log Y$。对本原相位 $r/q$ 考察
\[
 \sum_{d\le Y}\mu(d)d^{-a}\sum_{h\le Y/d} e(-rdh/q)
       -Y\sum_{q\mid d}\frac{\mu(d)}{d^{1+a}}.
\]
第二个和遍历全部正整数 $d$。按下列三段估计。

1. $d\le D$ 时，共振项 $q\mid d$ 的取整误差之和为 $O(D^{1-a})$。其余项先取 $d\le2q$，再按第 2 节的截短几何和从 $D$ 向下二分，合计
\[
 O\big(q\log(2q)+D^{1-a}(1+\log(Y/D))\big).
\]
其中 $q\log(2q)\ll_{b,H}Y^{1-a}(\log Y)^{-H}$，因为 $1-a-1/3\ge1/15$。
2. 原双和的 $d>D$ 部分先固定 $h\le Y/D$。对 $\theta=-rh/q$ 部分求和，Davenport 界给 $|\sum_{D<d\le U}\mu(d)d^{-a}e(d\theta)|\ll_M U^{1-a}(\log D)^{-M}$，$D\le U\le Y$。取 $U=Y/h$ 再求和，得 $O_M(Y^{1-a}(Y/D)^a(\log D)^{-M})$。
3. 剩余共振主项是 $Y\sum_{d>D,\,q\mid d}\mu(d)d^{-1-a}$。用 $\mathbf1_{q\mid d}=q^{-1}\sum_{v=0}^{q-1}e(vd/q)$。每个相位对这个无限尾部分求和，均得 $O_M(D^{-a}(\log D)^{-M})$；$q$ 项的平均仍为同一界。乘 $Y$ 后与上一段同阶。

例如取 $E=4(H+2)$、$M>H+E+2$ 即可令上述各段都为 $O_{b,H}(Y^{1-a}(\log Y)^{-H})$。减去 $c_a$ 的非零频率和再花 $O(q)$。这就把式 (1) 的误差改成了该带任意对数节省的界。令 $q=1$ 时同一分解直接估计 $\sum_{n\le Y}R_a(n)-c_aY$，第一段仅有共振取整，故 $B_{\lfloor Y\rfloor}\ll_H Y^{1-a}(\log Y)^{-H}$。回到第 3 节，两种窗的差分端点都保留此节省。无限尾的 Abel 积分中用 $\log Y\ge\log X$，得到
\[
 |(1-\bar z)\widehat B_\nu(z)-b_q|\ll_{b,H}X^{-a}L^{-H}.
\]

**合并全部频率。** 到 $Q_b$ 的加权交叉误差至多为 $O_{b,H}(X^{-a}Q_b^{2-a}L^{-H})$，因为仍按 $|b_q|J_2(q)$ 求和。在临界窗 $X^{-a}Q_b^{2-a}\ll_K L^{(2-a)b}$，取 $H>2b+2$ 即为 $o(1)$。Gram 的相对误差 $O(Q_b^2\log Q_b/X)$ 乘 $E_a(Q_b)=O_K(L)$ 后也趋零（固定 $b,K$）。最后，令 $v=2a-1$，将谱主项写作 $A_*\int_0^{\log Q}e^{-vu}\,du$。把积分上限从 $L/3$ 推到 $\log Q_b=L/3+b\log L+o(1)$，增加量为 $b A_* e^{-\xi/3}\log L+O_{b,K}((\log L)^2/L)+o(1)$。第 1 节的其余项一致有界，式 (3) 即得。因 $e^{-\xi/3}\ge e^{-K/3}$ 且 $A_*>0$，逐个取任意大的固定 $b$ 就给出所述一致发散。

## 5. 原数列的区间复算

取 $X=4096,Q=16,a=1/2$，直接按约数构造每个 $R_a(n)$，以 160 位 Arb 区间算术求真实锚定量。二倍窗口均方位于 $[0.51945121475670, 0.51945121475671]$，选定频率的算术谱和位于 $[0.03389563246571, 0.03389563246572]$。用相同方法另核 $a=7/16,9/16$，覆盖临界参数两侧。对加权尾，数值表只给到 $4X$ 的有限段。第 3、4 节的解析不等式作用于整个无限尾。

[原锚定量复算程序](critical_check.py) · [有限谱与能量核验](critical_checked.json) · [临界常数区间程序](critical_constant.py) · [有向舍入结果](critical_constant_checked.txt) · [原数列 Arb 区间复算](critical_arb.py) · [三组有理包围](critical_arb_checked.json)
