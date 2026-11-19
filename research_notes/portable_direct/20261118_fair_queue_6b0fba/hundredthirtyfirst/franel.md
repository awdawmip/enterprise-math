# Franel 数的两个中点数位与等深问题的复合下标读数

记 $F_j=\sum_{i=0}^j\binom ji^3$。对每个素数 $p\equiv5,7\pmod8$ 和每个整数 $c\ge0$，有
$$
\boxed{\quad F_{p^2c+(p^2-1)/2}\equiv p^2 F_c\pmod{p^3}.\quad} \tag{1}
$$
所以，当 $p\nmid F_c$ 时，附加两个中点数位后的赋值恰为二。当 $p\mid F_c$ 时，(1) 给出赋值至少为三。取 $c=0$ 即得到 Z.-H. Sun 在 2015 年明确提出的猜想 2.2 的首式。这个结论不要求单中点 $F_{(p-1)/2}$ 恰有一次 $p$ 因子。

同一计算给出原 P022 两个首商的乘积。设 $p\equiv5,23\pmod{24}$、$n=(p-2)/3$、$m=(p-1)/2$，且 $p\mid F_n$。则在 $\mathbf F_p$ 中
$$
\boxed{\quad 3\,\frac{F_n}{p}\frac{F_m}{p}
  =16\,\frac{F_{n-1}}{F_{m-1}}-9\,\frac{F_{pn+m}}{p^2}.\quad}       \tag{2}
$$
等号右边只读一个复合指标的二阶商，以及两个较小指标的普通剩余。两个邻项都是单位。右边非零，当且仅当原两个指标同为深度一；若读到零，则至少一者深度达到二，还须分别检测。原登记另外要求此前缺陷全部逃逸，才可把这一局部等深用于整行判断。第 120 轮找到的两个双单位点都有更早的可见缺陷。[登记任务](https://github.com/awdawmip/enterprise-math/blob/3f0e163bff5c259d19cec7f6ffd6680cece295c0/research_tasks/P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_20260827.md) · [冻结首阶返回](https://github.com/awdawmip/enterprise-math/blob/5d95eab7697a7fdd45259138f357519a2451f033/research_returns/P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_RETURN_20260827.md) · [原行的两个精确实例](../hundredtwentieth/franel.md)

## 两个坏位的三次模数公式

在本节取任意素数 $p\ge5$。若 $0\le d<p$ 且 $p\mid F_d$，称 $d$ 为坏位，记 $u_d=F_d/p\bmod p$。设
$$ L_b=3\sum_{j=0}^b\binom bj^3(H_b-H_j),\qquad H_j^{(s)}=\sum_{h=1}^j h^{-s},\qquad H_j=H_j^{(1)}.$$
$G_b$ 是 Franel 同一三项递推的第二个解，取 $G_0=0,G_1=1$。对任意坏位 $a,b$（不要求不同）、任意整数 $c\ge0$，
$$
 \frac{F_{p^2c+pa+b}}{p^2}
 \equiv F_c\left[(u_a+cL_a)(u_b+aL_b)+8a^2 F_{a-1}G_b\right]\pmod p.       \tag{3}
$$
两坏位保证左边可整除；即使前缀 $c$ 内部含坏位，也可原样使用。特别在不加前缀时，两个坏位的二阶商矩阵按 $a,b$ 分别取行列，其秩至多三：三项分别为 $u_a u_b$、$(a u_a)L_b$、$(8a^2F_{a-1})G_b$。上界可达：$p=29$ 的全部坏位按 $12,14,16$ 排序，矩阵是 $[(16,14,11),(9,1,9),(15,25,21)]$，行列式模 29 等于 1。

**二项式展开。** 先令一般高位整数 $A\ge1$ 满足 $p\mid F_A$，低位 $b$ 为坏位。把原立方和按 $pi+j$ 分组。$j>b$ 的项因进位被 $p^3$ 整除。$j\le b$ 时，$\binom{pA}{pi}\equiv\binom Ai\bmod p^3$，因为每个完整单位块 $\prod_{h=1}^{p-1}(vp+h)\equiv(p-1)!\bmod p^3$。这里用 $H_{p-1}^{(2)}\equiv0\bmod p$ 以及配对 $h,p-h$ 得 $H_{p-1}\equiv0\bmod p^2$。余下的三个短块相除。写
$$
 X=A H_b-iH_j-(A-i)H_{b-j},\qquad
 Y=A^2 H_b^{(2)}-i^2H_j^{(2)}-(A-i)^2H_{b-j}^{(2)}.
$$
于是立方被加数模 $p^3$ 等于
$$
 \binom Ai^3\binom bj^3\left[1+3pX+\tfrac12p^2(9X^2-3Y)\right].
$$
常数与一次项求和给 $F_AF_b+pA F_A L_b$，也给任意 $A,b$ 的一阶规律（无须坏位）。对二次项令 $z=2i-A$。关于 $z$ 的一次部分因 $i\leftrightarrow A-i$ 求和为零，常数部分乘 $p^2F_A$ 消失。$z^2$ 的系数求和为
$$
 \sum_{j=0}^b\binom bj^3\left[\tfrac98(H_{b-j}-H_j)^2+
                 \tfrac38(H_j^{(2)}+H_{b-j}^{(2)})\right]=3G_b.
$$
这是二项式变形 $\sum (b!/[(1+t)_j(1-t)_{b-j}])^3$ 的 $t^2$ 系数的四分之一；该系数为 $12G_b$，有同递推和初值的望远镜验证。另由 $i^3\binom Ai^3=A^3\binom{A-1}{i-1}^3$ 及对称性，
$$
 \sum_{i=0}^A(2i-A)^2\binom Ai^3=\frac{A^2}{3}(8F_{A-1}-F_A).
$$
整理后有 $F_{pA+b}/p^2=(F_A/p)(u_b+AL_b)+8A^2F_{A-1}G_b\bmod p$。代 $A=pc+a$，前一阶展开给 $F_A/p=F_c(u_a+cL_a)$，Lucas 给 $F_{A-1}=F_cF_{a-1}\bmod p$。因坏位必有 $a\ge1$，这里减一不会跨位，得 (3)。[一阶数位公式](../fiftysecond/franel.md) · [伴解系数与望远镜证书](../thirtieth/franel_jet.md) · [Straub–Zudilin 的二项变形](https://doi.org/10.1093/imrn/rnac125)

**中点及等深乘积。** $p\equiv5,7\bmod8$ 时 $m$ 为坏位。中点关系为
$$ L_m=2u_m,\qquad F_{m-1}G_m=\tfrac12\pmod p.$$
第一式也可直接由已知的单个截断和 $\sum_{j=0}^m\binom{-1/2}j^3\equiv0\bmod p^2$ 看出。因 $pm+m\equiv-1/2\bmod p^2$，该和模 $p^2$ 是上述分组 $A=m,i=0$ 的整个短块，等于 $F_m+pm L_m$。第二式来自 Casoratian
$$ F_{d-1}G_d-F_dG_{d-1}=(-8)^{d-1}/d^2 $$
及 $(-8)^m=-1\bmod p$。取 $a=b=m$，(3) 中 $u_m+mL_m=0$，余项 $8m^2F_{m-1}G_m=1$，得 (1)。取 $a=n,b=m,c=0$，代 $n=-2/3\bmod p$，得 (2)。[Ji–Sun，Lemma 6 与 Theorem 8](https://cs.uwaterloo.ca/journals/JIS/VOL19/Ji/ji6.pdf) · [中点参数导数](../nineteenth/franel.md)

也可消去 (2) 的两个邻项。定义 $T_{ab}(c)=F_{p^2c+pa+b}/p^2\bmod p$，$S_{ab}=T_{ab}(1)/2-T_{ab}(0)$。由 (3)，$S_{ab}=L_a(u_b+aL_b)$。因此
$$
 2(1+2n)u_nu_m=(1+2n)S_{mn}-2m S_{nm}\pmod p.
$$
四个复合指标的归一化差可独立恢复同一读数；这里 $F_1=2$、$1+2n=-1/3$ 均可逆。

## 一位很深，重复后为何可以恰为二

令 $a=b=d$ 为任意坏位。Casoratian 给 $8d^2 F_{d-1}G_d=-(-8)^d\bmod p$。故对好前缀 $p\nmid F_c$，三个数位所得二阶商除以 $F_c$ 后即为
$$ (u_d+cL_d)(u_d+dL_d)-(-8)^d.                           \tag{4}$$
这给出完整的提升判据。若 $u_d+dL_d=0$，所有好前缀都恰有二层。若 $L_d(u_d+dL_d)\ne0$，只容许一个 $c\bmod p$ 再提升；该剩余本身须是好位，才能由好前缀实现。若 $L_d=0$，则所有好前缀都取同一个值 $u_d^2-(-8)^d$。特别地，对每个 $p^2\mid F_d$ 的单数位，$v_p(F_{(p+1)d})=2$。此处第二位带来的贡献来自伴解。

例如 $p=67,d=23$，有 $u_d=0,L_d=23$。不带前缀时，$F_{1564}/67^2\equiv8\bmod67$，而添上好前缀 $c=40$ 后，$F_{181124}/67^3\equiv33\bmod67$。另在 $p=29,d=12$，前缀 0 与 1 分别给出深度 2 和 3。两例都由保留进位和单位部的原始逐项二项立方和直接复算到模 $p^5$。这里的 $d=12$ 是 $p=29$ 的非对角坏位；该素数的原 $n$ 是 9。

## 先例与精确算例

Z.-H. Sun 的猜想 2.2、3.3 分别对 $A=F,S$ 提出 $A_{(p^2-1)/2}\equiv p^2\bmod p^3$，以及 $p^r\mid A_{(p^r-1)/2}$ 对每个 $r\ge1$ 成立，其中 $p\equiv5,7\bmod8$。第二条的下标由 $r$ 个中点数位组成。Delaygue 定理 1 及 §1.6 的 A000172、A081085 两行分别适用于 $F,S$，给出坏位数的赋值下界；由 $F_m\equiv0$ 及 $S_m\equiv(-1)^m F_m\bmod p$，便已包括两条猜想的全 $r$ 整除部分。Ji–Sun 在 Theorem 8 对 $c=0$ 证明 $F_{(p^2-1)/2}\equiv0\bmod p^2$，并证明该数与其 Catalan–Larcombe–French 归一化 $S_{(p^2-1)/2}$ 模 $p^3$ 相等。结合 (1) 可把他们的 $S$ 的该剩余也定为 $p^2$，从而得到两条猜想的固定第三位。Osburn–Straub 的序列 A 正是这里的 $F$；其 §2.2 式 (12)、(13) 确定单中点对模形式的模 $p$ 剩余。本文从二阶分块得到的是任意前缀下的首个可能非零数码，以及不同坏位次序的修正；对于更多个重复中点，本文沿用上述整除下界。[Z.-H. Sun，猜想 2.2、3.3](https://arxiv.org/pdf/1502.02499v3) · [Delaygue](https://arxiv.org/abs/1310.4131) · [Ji–Sun, *Two Properties of Catalan–Larcombe–French Numbers*](https://cs.uwaterloo.ca/journals/JIS/VOL19/Ji/ji6.pdf) · [Osburn–Straub, §2.2](https://arminstraub.com/downloads/pub/zagier-apery-lvalues.pdf)

| $p$ | $pn+m$ | $F_{pn+m}/p^2$ | $F_{pm+n}/p^2$ | $F_{n-1}/F_{m-1}$ | $u_nu_m$ |
|---:|---:|---:|---:|---:|---:|
| 536111 | 95804912088 | 362052 | 377671 | 95414 | 316237 |
| 663983 | 146957697432 | 544421 | 641303 | 198964 | 313189 |

后四列均取模 $p$。用前缀 1 重新算两个次序，首例得 $T_{nm}(1)=91630,T_{mn}(1)=122868$，次例得 $462464,656228$；都给出表中同一个首商乘积。两例还恰有 $S_{mn}=S_{nm}$。一般在这两个指标上，其差等于 $(2/3)u_m(3u_n-L_n)$。当 $u_m\ne0$ 时，两差相等恰需 $\sum_{j=0}^{p-1}\binom{-2/3}j^3\equiv0\bmod p^2$：用 $n=-2/3+p/3$ 在每个 $j\le n$ 处的一次 Taylor 展开得该和为 $F_n-pL_n/3\bmod p^2$，$j>n$ 的整除项立方后消失。这是两个实例提示的另一个超几何问题；这里仅证明等价式。

程序计算大指标时直接保留低位的全部二项式。具体在高位 $a$、低位 $b$、外和下标 $i$ 时，去掉公因子 $\binom{pa}{pi}^3$ 的低位块和记为 $H(i)$。前述三个短乘积使 $H(i)\bmod p^3$ 为次数至多二的多项式，且 $H(a-i)=H(i)$。取真实乘积算出 $H(0),H(1)$，便得到
$$ F_{pa+b}\equiv H(0)F_a+
 \frac{H(1)-H(0)}{3(a-1)}a^2(F_a-2F_{a-1})\pmod{p^3},$$
这里仅需 $a-1$ 可逆；两组大指标都符合。此算法按乘积和二次插值直接求值，不以中点恒等式或 (2) 生成证据。整个有限核检查 $5\le p\le71$ 的 67 个有序坏位对、134 个额外前缀和 66 次中点读数。执行标准库命令即可重建结果。[复算程序](franel_check.py) · [精确结果](franel_checked.json)

~~~sh
python3 franel_check.py > /tmp/franel-131.json
cmp /tmp/franel-131.json franel_checked.json
~~~
