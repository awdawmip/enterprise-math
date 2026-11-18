# 惰性负号分支在奇异系数处的两位展开

设 $p>7$ 为素数，$p\equiv5\pmod6$，写
$$
L=(p+1)/6,\quad H=(p-1)/2=3L-1,\quad s=H-1,\quad
r=(p-2)/3=2L-1,\quad M=(2p-1)/3=H+L.
$$
奇异方程右端 $pT_H-R_s$ 的 $p^0$ 位恒为零。本节给出除以 $p$ 后模 $p^2$ 的值，涉及两个可能为零的系数与一个只在 $\mathbb F_p$ 中计算的短和。与实际系数 $108s a_s$ 比较时，必须保留满 $p^3$ 精度的原始加权前缀可从 $s-1$ 再缩短到 $r$；余下的长度为 $L-2$ 的部分只用模 $p^2$ 的显式展开。上述系数公式适用于所列全部 $p$。与原惰性负号目标的等价在已冻结的 $p\equiv17,23\pmod{24}$ 两类使用。

## 任务及返回式

记 $b_k=216^{-k}\binom{2k}{k}^2\binom{3k}{k}$、$f_k=(6k+1)b_k$。PR 814 的返回定义
$$
a_n=\frac{216^{n-1}\sum_{k<n} f_k}{n(2n+1)\binom{2n}n},
\quad R_n=(6n+1)\binom{2n-1}n\binom{3n}n/(2n+1),
\quad (2n+3)a_{n+1}=108n a_n+R_n .
$$
在 $T_p=-216^{p-1}/((2p+1)\binom{2p}p)$ 模 $p^2$ 起始，把同一递推倒推至 $T_H$。唯一奇异步的残差为 $B_p=108s a_s+R_s-pT_H\bmod p^3$。设 $C_p=2\sum_{k=0}^{M}f_k-E_p$。下文将对这里全部 $p$ 直接推导两个残差间的单位比例。Swisher 的 $E_p\equiv-2p\bmod p^3$ 精确对应其 Theorem 1.1 取 $a=1/3,b=2$，亦见论文式 (1)。PR 814 是开放的来源。其 Driver 对严格归约的代数作了复核，因旧结果 RR-D082EB0CD630968536FB 的输出清单所指 Git blob 与其声明提交不一致，要求以新结果号重交来源封装；该旧返回未验收。本节只使用可核对的有限定义和上述父接口。[V2 任务书](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_FINITE_CLAUSEN_SWISHER_BRIDGE_V2_20260828.md) · [PR 814 冻结返回](https://github.com/awdawmip/enterprise-math/blob/fcde513e7e6305545c8fd646c8dc0afb39d52e16/research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_FINITE_CLAUSEN_SWISHER_BRIDGE_RETURN_20260829.md) · [Driver 修订决定](https://github.com/awdawmip/enterprise-math/pull/814#pullrequestreview-5055907675) · [Swisher 原文](https://doi.org/10.1186/s40687-015-0037-6)

Sun 的 *Open Conjectures on Congruences* 中，Conjecture A14(i) 已列出 $a_n$ 及其一阶递推。Conjecture A14(ii) 的加权部分取 $a=1$，预言 $W_p=\sum_{k=0}^{p-1} f_k\equiv p(p/3)\pmod{p^3}$，其中 $(p/3)$ 是 Legendre 符号。在这里 $p\equiv2\bmod3$，右侧成为 $-p$。这是猜想的历史定位，式 (1)–(5) 的推导没有调用该猜想。[Sun，arXiv:0911.5665v41，第 13 页 Conjecture A14](https://arxiv.org/pdf/0911.5665v41#page=13)

## 奇异系数公式

设 $\tau=(-1)^H$、$\chi=(6/p)$ 为 Legendre 符号，$q_p(d)=(d^{p-1}-1)/p\bmod p$，写 $D=1-2q_p(2)+3q_p(6)/2\in\mathbb F_p$。在 $\mathbb F_p$ 定义
$$
\Xi_p=\sum_{j=1}^{L}\frac{3j-1}{j}(-32)^j
\frac{\binom Lj\binom{L+j-1}j}{\binom{2j}j^3}.
\tag{1}
$$
因 $2L<p$，各分母均可逆。**上端目标与奇异源项满足**
$$
T_H\equiv\frac{\tau}{108}
\big[\chi+4+p(\chi D+10-2\Xi_p)\big]\pmod{p^2},
\qquad
\frac{R_s}{p}\equiv\frac{\tau}{54}
\left(-\frac{72}{35}-p\frac{5427}{1225}\right)\pmod{p^2}.
\tag{2}
$$
因而原未决条件恰为
$$
\boxed{\quad
108s a_s\equiv\frac{\tau p}{108}
\left[\chi+\frac{284}{35}
 +p\left(\chi D+\frac{23104}{1225}-2\Xi_p\right)\right]\pmod{p^3}.
\quad}
\tag{3}
$$
特别是，$p^1$ 位目标为 $108s a_s\equiv \tau p(\chi+284/35)/108\bmod p^2$。目标两类的 $(\tau,\chi)$ 分别为 $(1,-1)$ 与 $(-1,1)$。因而 $p^1$ 位由相应类选定的有理常数在 $\mathbb F_p$ 中的像给出。一般适用域内，$p=29$ 和 $83$ 的这一位都为零，两个素数均在原目标两类之外。式 (3) 确定模 $p^3$ 的数值，对 $p^2$ 位不设非零条件；若要写标准 $p$ 进数字，还要计入首项有理数代表的进位。式 (3) 给出应与 $a_s$ 比较的确定值；左边依然有算术内容。

**推导。** 令 $U=216^{H-1}/(H\binom{p-1}H)$。由归一化定义，$p a_H=U\sum_{k<H}f_k$、$R_s=Uf_s$。同一递推从 $p$ 倒推时对应把全和的目标值设置为 $-p$，所以
$$
T_H\equiv-U\left(1+\sum_{k=H}^{M} f_k/p\right)\pmod{p^2}.
\tag{4}
$$
这里 $k>M$ 的项被 $p^3$ 整除。亦可把 $S_n^*=216^{n-1}(-p-\sum_{k=n}^{p-1} f_k)$ 除以 $n(2n+1)\binom{2n}n$，这给出以 $T_p$ 为末值的精确有理数解，直接推出 (4)。

将 (4)、$108s a_s=U\sum_{k<s}f_k$ 与 $R_s=Uf_s$ 相加，得到所有 $p>7$、$p\equiv5\bmod6$ 都适用的单位恒等式
$$
 B_p\equiv U\left(\sum_{k=0}^{M}f_k+p\right)
 \equiv (U/2)C_p\pmod{p^3}.
$$
第二步只用上述 Swisher 定理；$U/2$ 在此范围是单位。所以 $B_p\equiv0\Leftrightarrow C_p\equiv0$ 在整个范围成立。从 $C_p$ 返回项目最初惰性负号两个条件的冻结等价只在 $p\equiv17,23\bmod24$ 使用。这些单位等式本身不要求任何一个残差已经消失。

相邻项之比为
$$
b_{k+1}/b_k=\frac{(k+1/2)(k+1/3)(k+2/3)}{2(k+1)^3}.
$$
$k=H$ 时第一个因子为 $p/2$。拔去这个因子后，对 $1\le j\le L$ 有
$$
\frac{b_{H+j}}{p b_H}\equiv
\frac{(j-1)!(-1/6)_j(1/6)_j}{2^{j+1}(1/2)_j^3}\pmod p .
$$
此处 $(a)_j$ 为升阶乘。用 $1/6\equiv L\bmod p$、$6(H+j)+1\equiv6j-2$ 及 $(1/2)_j/j!=4^{-j}\binom{2j}j$，就得到 $\sum_{j=1}^L f_{H+j}\equiv p b_H\Xi_p\bmod p^3$。$b_H$ 恰含一个 $p$ 因子，故 (1) 只需首位。

现计算两项单位。$\binom{p-1}{H}=\tau\prod_{i=1}^H(1-p/i)$ 且 $\binom{p+H-1}{H}=p H^{-1}\prod_{i=1}^{H-1}(1+p/i)$。于是出现精确乘积消去
$$
U\frac{b_H}{p}=\frac{\tau}{216H^2}(1-p/H)
\prod_{i=1}^{H-1}(1-p^2/i^2)
\equiv \frac{\tau}{54}(1+4p)\pmod{p^2}.
$$
另一方面 $\sum_{i=1}^H i^{-1}\equiv-2q_p(2)\bmod p$，可由 $2^p-2=\sum_{k=1}^{p-1}\binom pk$ 除 $p$ 后分奇偶项得到。由 $(6^H)^2=1+p q_p(6)\bmod p^2$、$6^H\equiv\chi\bmod p$ 得 $216^H\equiv\chi(1+3p q_p(6)/2)\bmod p^2$。进而 $U\equiv-\tau\chi(1+pD)/108\bmod p^2$。将这些值连同 $f_H=(3p-2)b_H$ 代入 (4) 即得 $T_H$。

最后由 $s=H-1$ 和相邻项之比，得到
$$
\frac{f_s}{b_H}=\frac{18(p-1)^3(3p-8)}{(p-2)(3p-7)(3p-5)}
\equiv -\frac{72}{35}+p\frac{4653}{1225}\pmod{p^2}.
$$
同 $Ub_H/p$ 相乘给出 (2) 的第二式，作差给出 (3)。常数 $23104/1225$ 来自 $10+2\cdot5427/1225$。

## 实际 $a_s$ 的满精度前缀

在 (3) 的另一侧，记 $P_r=\sum_{k=0}^r f_k$，其中 $r=(p-2)/3$。下述展开把 $s-1-r=L-2$ 个原始模 $p^3$ 项换成模 $p^2$ 的系数。对 $1\le j\le L-2$ 定义
$$
d_j=\frac{(j-1)!(-1/6)_j(-1/3)_j}{3\cdot2^j(1/3)_j^3},\qquad
h_j=\sum_{i=0}^{j-1}\left(\frac1{i-1/6}+\frac1{i-1/3}-\frac3{i+1/3}\right)+\sum_{i=1}^{j-1}\frac1i.
$$
有独立于 (3) 右端的恒等同余
$$
108s a_s\equiv U\left[P_r+p b_r\sum_{j=1}^{L-2}
 (6r+6j+1)d_j(1+p h_j/3)\right]\pmod{p^3}.
\tag{5}
$$
$U$ 在此可直接用原分数取模 $p^3$。为证明 (5)，对 $r+j$ 使用上面的相邻项比。参数 $r+2/3=p/3$ 的首次出现提供外侧的 $p$。其余因子的中心值为 $-1/6,-1/3,1/3$ 与正整数，并共同平移 $p/3$。把有限乘积在此平移下展开到一阶正给 $b_{r+j}/(p b_r)\equiv d_j(1+p h_j/3)\bmod p^2$。在 $j\le L-2$ 时分母及各展开中心值均为单位，因为 $1/6\equiv L$、$1/3\equiv2L\bmod p$。再用 $108s a_s=U\sum_{k<s} f_k$ 即得。

式 (3) 与 (5) 两边所需的最高精度前缀现在是 $k\le r$。还须证明这两个独立表达式对两个目标类恒相等；(5) 对中间带降了一位精度，(1) 对上带降了两位。本文保留 $\Xi_p$ 的有限和，并未得到使两边一致的求值公式。

## 可手核的边界与复算

$p=17$ 时 $L=3$，式 (1) 的三项在 $\mathbb F_{17}$ 中依次为 $13,15,10$，合计 $4$。$a_s=464709144$，$T_H=43$、$R_s/p=214\bmod289$，故奇异方程要求 $108s a_s/p\equiv118\bmod289$；实值符合。若删除 $\Xi_p$，残差变为 $2890\bmod4913$。另一个目标类 $p=23$ 也有 $\Xi_p=4$，删除后残差为 $6348\bmod12167$。因此两类都已有反例排除「只取单位因子、忽略上带」的简化。

同目录 `python3 clausen_check.py` 输出 `clausen_checked.json`。程序逐项对照冻结的整系数回推、模 $p^3$ 的原始二项式和、显式互逆二项式尾和及式 (5) 的逐项展开。在 $7<p\le600$、$p\equiv5\bmod6$ 的全部 56 个素数上相符，其中 28 个属目标类。另逐素数重建 $E_p$ 及单位恒等式；将目标从 $-p$ 移至 $-2p$ 时，残差增量须为非零的 $pU\bmod p^3$，独立倒推也逐项相符。另对 $p=17,23$ 独立使用有理数升阶乘计算 $E_p$、$\widetilde W_p$ 和 $a_s$。样本中 56 个 $\Xi_p$ 都非零，全部 $B_p$ 恰为零模 $p^3$；对任意大素数的恒等式仍开。
