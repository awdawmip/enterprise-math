# 有限 Dirichlet 原始谱矩的首个非整阶与联合最小公分母

对原路径矩阵 $L_M=\operatorname{tridiag}(-1,2,-1)$（阶数 $M-1$），固定约分后的分母 $d\ge2$，取全部具名模态一次，定义
$$
 u_{k,d}=2-2\cos(\pi k/d),\qquad
 P_n(d)=\sum_{\substack{1\le k<d\\(k,d)=1}}u_{k,d}^{-n},\qquad n\ge1.
$$
若 $d$ 有至少两个不同素因子，每一阶 $P_n(d)$ 都是整数。若 $d=p^a$，第一项非整数的分母恰是 $p$，其阶数由实分圆域的不同指数决定。更整体地，对任意 $H\ge1$，所有 $d$ 和 $1\le n\le H$ 的**最小**公分母为
$$
 D_H=2^H\prod_{\substack{3\le p\le 2H+1\\p\ \mathrm{prime}}}
                 p^{\lfloor 2H/(p-1)\rfloor}.                               \tag{1}
$$
例如 $D_1,D_2,D_3,D_4,D_5$ 依次为 $6,180,7560,226800,14968800$。以下还给出固定一阶可能有额外消去时的模 $p$ 判据。

原任务第4、6项要求厘清真正分母分层所保留的算术。第3轮与第107轮给出了 Jordan 系数及其 Dirichlet 级数中的极点；第15轮识别了互补谱片与整数环。这里取同一个 $P_n(d)$ 的有理数分母。所用局部域的迹对偶、分圆整数环及不同理想都是经典结果。[冻结任务](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/EMW59A_1159_SPECTRAL_ZETA_JORDAN_20260909.md) · [原始分母读数](https://github.com/awdawmip/enterprise-math/blob/6bbb4454f9f2ba3cb23409846ebf414ed1dc4028/research_notes/PRIMITIVE_SPECTRAL_DIRICHLET_SERIES_AND_RH_READOUT_20260905.md) · [第3轮](../third/jordan.md) · [第15轮](../fifteenth/cyclotomic.md) · [第107轮](../hundredseventh/jordan.md)

## 一、素幂层何时首次出现分母

对 $d=p^a$ 记
$$
(e,\delta)=
\begin{cases}
\big(p^{a-1}(p-1)/2,\,[p^{a-1}(ap-a-1)-1]/2\big),&p\text{ 奇},\\
\big(2^{a-1},\,a2^{a-1}-1\big),& p=2.
\end{cases}
$$
以 $v_p(p)=1$ 归一化，则 $P_n(p^a)\in\mathbb Z[1/p]$，且
$$
 v_p(P_n(p^a))\ge\left\lfloor\frac{\delta-n}{e}\right\rfloor,\qquad
 v_p(P_{\delta+1+te}(p^a))=-1-t\quad(t=0,1,2,\ldots).                \tag{2}
$$
因此首次非整阶恰为 $\delta+1$。给定未知的素幂壳，这一项的分母给出 $p$，阶数又随 $a$ 严格增加，故两项读数即可唯一识别 $d$。这里“阶数”是该项在整个顺序矩列中的位置。

**从原模态到迹。** 对 $l\ge3$，令 $\zeta_l$ 为本原 $l$ 次单位根，$u=2-\zeta_l-\zeta_l^{-1}$，$f_l$ 为其首一最小多项式，度数 $\varphi(l)/2$。偶 $d$ 时所有具名特征值恰为 $l=2d$ 的一套实共轭。奇 $d$ 时偶 $k$ 给 $l=d$ 的一套，另外的 $d-k$ 给互补值 $4-u$ 的一套，即 $l=2d$；两套都要保留。其谱乘积分别为 $\Phi_l(1)$。由分圆分解，在 $l$ 为素幂时此乘积等于相应素数，否则为 $1$。于是非素幂 $d$ 的全部谱值都是代数单位，而每套共轭的和为有理数，倒数矩也为整数。对奇素幂 $d$，只有 $l=d$ 的一套有非单位值；$4-u$ 为单位且位于同一实分圆域。偶素幂 $d=2^a$ 只需 $l=2^{a+1}$。

**不同指数。** 现在 $l$ 是上一段的素幂，在 $p$ 处 $K=\mathbb Q_p(u)$ 全分歧，$\mathcal O_K=\mathbb Z_p[u]$，$u$ 是均匀元，$\mathfrak p=(u)$，$[K:\mathbb Q_p]=e$。这是因为全分圆域由 $\pi=\zeta_l-1$ 的 Eisenstein 方程生成，且 $u=-\pi^2/\zeta_l$；全域在 $K$ 之上次数二，整环由 $1,\zeta_l$ 生成。奇素数时全域不同指数为 $p^{a-1}(ap-a-1)$，实域之上的二次层不同指数为 $1$。后者可由 $\zeta_l-\zeta_l^{-1}$ 的全域赋值直接算出。对 $l=2^{a+1}$，这两个指数分别为 $a2^a$ 和 $2$。不同理想塔公式给出的实域不同指数正是上述 $\delta$。全域指数也可由 $\Phi_l'(\zeta_l)=l\zeta_l^{-1}/(\zeta_l^{l/p}-1)$ 取赋值得到。[局部迹对偶与不同理想](https://doi.org/10.1007/978-1-4757-5673-9)

**锐边界。** 迹对偶为 $\mathfrak p^{-\delta}$，因此任意整数 $k$ 满足
$$
 \operatorname{Tr}_{K/\mathbb Q_p}(\mathfrak p^k)=p^{\lfloor(k+\delta)/e\rfloor}\mathbb Z_p.
$$
事实上其包含在 $p^h\mathbb Z_p$ 中当且仅当 $\mathfrak p^{k-eh}\subseteq\mathfrak p^{-\delta}$，取最大整数 $h$ 即可。用 $k=-n$ 得 (2) 的下界，奇素幂的另一套单位迹也满足它，因为它来自 $\mathcal O_K\subseteq\mathfrak p^{-n}$。当 $n=\delta+1+te$，$\mathfrak p^{-n}$ 与 $\mathfrak p^{1-n}$ 的迹像恰差一级；两边相邻商都是一维 $\mathbb F_p$，故非零代表 $u^{-n}$ 的迹确实达到该赋值。另一套单位迹是整数，不能消去负赋值。

对 $a=1$ 的奇素数，$\delta=e-1$，在 $n=e,2e,3e,\ldots$ 逐级取到等号。所有 $a$ 均有 $\delta\ge e-1$、$e\ge(p-1)/2$。因此对每个奇 $p$，任一 $n\le H$ 的分母指数至多 $\lfloor2H/(p-1)\rfloor$，且取 $d=p$、$n=e\lfloor H/e\rfloor$ 可达到每个正指数。对 $p=2$，$d=2$ 的 $P_H(2)=2^{-H}$ 达到最大指数 $H$。这证明 (1)，亦即经典阶 $2H$ 的 Todd 数除以 $2^H$。由 $Z_n(M)=\operatorname{Tr}L_M^{-n}=\sum_{d\mid M,d>1}P_n(d)$ 与其整数 Möbius 逆式，原矩阵的全部 $Z_n(M)$ 也有同一最小公分母。式 (1) 允许不同素数在不同阶达到最大值。

## 二、每个中间阶的首位检验

固定 $d=p^a$，在有非单位谱的那一套简写 $f=f_l$。在 $\mathcal O_K/p\simeq\mathbb F_p[X]/(X^e)$ 中，以下两单位用度数小于 $e$ 的多项式代表：
$$
 W(X)=p/u^e\bmod p,\qquad V(X)=f'(u)/u^\delta\bmod p .
$$
对任一 $n=\delta+1+te+s$，其中 $t\ge0$、$0\le s<e$，有
$$
 p^{t+1} P_n(d)\equiv [X^s]V(X)W(X)^{t+1}\pmod p.                    \tag{3}
$$
右侧非零恰表示 $v_p(P_n(d))=-t-1$。右侧为零时估值至少 $-t$。证明用共轭上的 Lagrange 插值：$\deg g<e$ 时 $\operatorname{Tr}(g(u)/f'(u))=[X^{e-1}]g(X)$。一般整多项式先对 $f$ 取余。将 $p^{t+1}f'(u)u^{-n}=u^{e-1-s}(f'(u)/u^\delta)(p/u^e)^{t+1}$ 代入，由 $f\bmod p=X^e$ 即得 (3)；奇素幂的单位迹乘以 $p^{t+1}$ 自动消失。对固定 $s$，除以 $W(0)^{t+1}$ 后，(3) 的读数按 $t$ 的周期整除最小的 $p$ 幂 $p^b\ge s+1$。这是因为 $(W/W(0))^{p^b}\equiv1\pmod{X^{s+1}}$。这样在每一素幂层用有限张表就能判定全部达到下界的阶数。

端点 $s=0$ 特别简单。对奇 $p$，
$$
 W(0)=(-1)^{e+1},\qquad V(0)=(-1)^{e+a+1-\delta}/2 \quad\text{于 }\mathbb F_p;          \tag{4}
$$
$p=2$ 时二者均为 $1$。故 (2) 中的无穷等号序列还有具名首位 $W(0)^{t+1}V(0)$。为核符号，将 $p=\prod_{r\in(\mathbb Z/l)^\times}(1-\zeta_l^r)$ 除以 $\pi^{2e}$，模 $\pi$ 得 $-1$，因为每一非零模 $p$ 余数重复 $p^{a-1}$ 次。又 $u=-\pi^2/\zeta_l$。在形式恒等式 $f(2-Z-Z^{-1})=(-1)^e Z^{-e}\Phi_l(Z)$ 两边求导后取 $Z=\zeta_l$，使用 $1-\zeta_l^{-2}\equiv2\pi\pmod{\pi^2}$。二项式展开还给 $(\zeta_l^{p^{a-1}}-1)/\pi^{p^{a-1}}\equiv1\pmod\pi$，因为中间二项式系数均含 $p$ 且 $v_\pi(p)=2e\ge p^{a-1}$。结合 $2\delta=2ea-p^{a-1}-1$ 即为 (4)。

## 三、奇素数壳有多少阶会消掉首位

当 $d=p\ge5$，$e=(p-1)/2$，令 $T=t+1$，$w=W/W(0)$。把 (3) 除以 $W(0)^T$，对给定 $0\le s<e$ 得到 $T\bmod p$ 的一个**恰 $s$ 次多项式**。所以每个完整周期至少 $p-s$ 个余类取到 (2) 的分母界。对 $s>0$，其中有一个确定的抵消余类 $eT+s\equiv0\pmod p$。前两个非端点的全表是
$$
\begin{array}{c|c|c}
s& \text{归一化的首位}&\text{首位消失的全部 }T\bmod p\\\hline
1& -(eT+1)/24 & 2 \\
2& (eT+2)(5T-22)/5760 & 4,\ 22/5
\end{array}
$$
第二行要求 $p\ge7$，两个余类相异。例如 $p=5$ 的第4阶有分母 $25$，第5阶首位消去，对应联合公分母与单阶之间的区别。

推导时写 $f=X^e+p h$，在原点用形式幂级数 $\widehat W=-1/h$ 表示 $W$，$w=\widehat W/\widehat W(0)$。因 $\delta=e-1$，在 $\mathcal O_K/p$ 中 $V=e+Xw'/w$。为算 $h$ 的初项，取 $X=4\sin^2 y$、$F_e(X)=\sin((2e+1)y)/\sin y$，则 $f=(-1)^eF_e$，而 $\sum_{e\ge0}F_e(X)z^e=(1+z)/((1-z)^2+Xz)$。因此对 $j<e$，
$$
 \frac{[X^j]h}{h(0)}
 =(-1)^j\frac{\binom{e+j}{2j}}{2j+1}
 \equiv \frac{\binom{2j}{j}}{16^j(2j+1)} \pmod p.
$$
在允许这些项的精度上，$w^{-1}=1+X/24+3X^2/640+\cdots$。由于 $s!$ 在 $\mathbb F_p$ 可逆，$[X^s]w^T$ 关于 $T$ 的次数为 $s$，首系数为 $(-1/24)^s/s!$。当 $s>0$，该多项式还含因子 $T$。由形式求导得到 $(eT+s)[X^s]w^T/T$ 为归一化首位；这里先作多项式整除，再代入 $T=0$ 仍有效。展开 $s=1,2$ 得表内结论。$s=0$ 直接给 $V(0)=e\bmod p$。

## 四、从原路径矩阵独立复算

| $d$ | $e$ | $\delta$ | 首次非整阶 | 该阶完整 $P_n(d)$ | 随后每隔 $e$ 阶的前四个归一首位（含首次） |
|---:|---:|---:|---:|---:|---|
| 2 | 1 | 0 | 1 | $1/2$ | $1,1,1,1$ |
| 3 | 1 | 0 | 1 | $4/3$ | $1,1,1,1$ |
| 4 | 2 | 3 | 4 | $17/2$ | $1,1,1,1$ |
| 5 | 2 | 1 | 2 | $38/5$ | $3,2,3,2$ |
| 7 | 3 | 2 | 3 | $920/7$ | $3,3,3,3$ |
| 9 | 3 | 4 | 5 | $117656/3$ | $2,2,2,2$ |

程序从原三对角矩阵的首一续行列式 $Q_1=1,Q_2=X-2,Q_{M+1}=(X-2)Q_M-Q_{M-1}$ 逐个整除真因子，得到 $d=2,\ldots,128$ 的全部 $127$ 个原始特征多项式。独立一路由 $Z^l-1$ 提取分圆多项式并用 $Z^i+Z^{-i}$ 递推回到 $X$，两路逐系数完全一致。原多项式的 Newton 和供给 $9593$ 个精确有理矩；其中 $44$ 个素幂层的 $5887$ 个首位另由 (3) 重算。在 $5\le p\le31$ 的每个素数上检满全部 $T\bmod p$ 与全部 $s$。$1\le H\le20$ 的实际联合最小公分母另行逐项求 lcm，均与 (1) 相同。复算只依赖 Python 标准库，所有算术均为整数或分数。[程序](cyclotrace_check.py) · [逐层读数与摘要](cyclotrace_checked.json)

~~~sh
python3 -I cyclotrace_check.py | cmp - cyclotrace_checked.json
~~~
