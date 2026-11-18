# Franel 数模素数平方：一个坏数字何时升阶，单位余数怎样分布

令 $F_n=\sum_{j=0}^n\binom nj^3$。对任意奇素数 $p$，$F_n\bmod p^2$ 是相邻两位数码各贡献一个因子的乘积。模 $p$ 为零的数字称为坏数字。若恰有一个坏位，是否升至 $p^2$ 只由它及紧邻高位决定。特别地，$p=29$ 的坏数字为 $12,14,16$，即使其余位全好，邻接数位 $17|12$ 和 $11|16$ 也能造成额外一个因子 29。

这还给出两个抽样结论。固定 $p\ge5$，只在全部数位都好的 $m$ 位串中均匀抽样，朴素单数位乘积与其模 $p^2$ 所需的修正量渐近独立，朴素乘积正确的概率趋于 **$1/p$**。若改在全部整数 $0\le n<p^m$ 中等概率抽样，而该素数存在坏数字，朴素公式正确的概率却趋于 **1**。后一个极限由两侧同时变成零造成。这里是独立的经典整数序列研究；第 30 轮分析了同一递推的端点反射与伴解，P022 的登记前置另行管理。[以前的 Franel 端点研究](https://github.com/awdawmip/enterprise-math/blob/3f4d3f20031f51803d897914aa9bea28a4fadbf9/research_notes/portable_direct/20261118_fair_queue_6b0fba/thirtieth/franel_jet.md)

## 1. 相邻数位的乘积公式

在 $\mathbb F_p$ 记 $H_0=0,\ H_j=\sum_{k=1}^j1/k$（此处 $j<p$），并令

$$
L_b=3\sum_{j=0}^b\binom bj^3(H_b-H_j),\qquad 0\le b<p.
$$

**定理 1。** 对任何整数 $a\ge0$、任何 $0\le b<p$，
$$
F_{pa+b}\equiv F_a(F_b+paL_b)\pmod{p^2}.
\tag{1}
$$
所以若 $n=\sum_{j=0}^{m-1}b_jp^j$（允许前导零），约定 $b_m=0$，便有
$$
F_n\equiv\prod_{j=0}^{m-1}(F_{b_j}+p b_{j+1}L_{b_j})\pmod{p^2}.
\tag{2}
$$

证明直接在原和中按 $k=pi+j$ 分组。若 $j>b$，Lucas 同余使该项有因子 $p$，立方后消失。若 $j\le b$，在 $\mathbb Z_{(p)}$ 中消去整块的 $p$ 倍数，得
$$
\binom{pa+b}{pi+j}\equiv
\binom ai\binom bj\{1+p[aH_b-iH_j-(a-i)H_{b-j}]\}\pmod{p^2}.
$$
这里 $\binom{pa}{pi}\equiv\binom ai\bmod p^2$ 对任意 $a$ 成立，因为每块 $\prod_{t=1}^{p-1}(pq+t)\equiv(p-1)!(1+pqH_{p-1})\equiv(p-1)!\bmod p^2$，$H_{p-1}=0$ 在 $\mathbb F_p$ 中成立。额外的首尾短块分别贡献上式三个调和和。立方后求和，用 $\sum_i i\binom ai^3=(a/2)F_a$ 与 $j\leftrightarrow b-j$ 得 (1)，从低到高迭代得 (2)。无须高位前缀小于 $p$。逐数字无修正律 $F_{pa+b}\equiv F_a F_b\bmod p^2$ 对所有 $a$ 成立，当且仅当 $L_b=0$，必要性只须取 $a=1$。

同一证明适用于 $F_n^{(r)}=\sum_j\binom nj^r$、任意整数 $r\ge2$，只须把 $L_b$ 改为 $r\sum_j\binom bj^r(H_b-H_j)$。因此 $p\mid r$ 时，朴素逐数位公式对所有数都在模 $p^2$ 成立。这也解释原三次问题的 $p=3$ 边界。

**先行结果。** Lucas 二项式同余已经导出 Franel 数的模 $p$ 数位律。Gessel 对 Apéry 数 $A_n=\sum_k\binom nk^2\binom{n+k}k^2$ 给过与 (1) 形式相同的模 $p^2$ 一阶提升；Rowland、Yassawi、Krattenthaler 的式 (4) 与定理 2 进一步给相应反射判据。Mellit–Vlasenko 定理 1 处理 Newton 多面体只有原点为内整点的 Laurent 多项式幂之常数项；此处可取 $\Lambda=(1+x)(1+y)(1+(xy)^{-1})$，直接展开即得 $F_n=\operatorname{CT}\Lambda^n$，其六边形只含这一个内整点。Delaygue 定理 1 和 §1.6 的 A000172 条目已经给出 $v_p(F_n)\ge\#\{\text{坏位出现次数}\}$。下面精算一个坏位何时超过这条下界以及随机数位的单位分布，不把该一般下界或 Lucas 方法列为新定理。[Gessel](https://doi.org/10.1016/0022-314X(82)90071-3) · [Rowland–Yassawi–Krattenthaler](https://ericrowland.github.io/papers/Lucas_congruences_for_the_Apery_numbers_modulo_p%5E2.pdf) · [Mellit–Vlasenko](https://arxiv.org/abs/1306.5811) · [Delaygue](https://arxiv.org/abs/1310.4131)

## 2. 估值精确到第二层

记 $G=\{b:p\nmid F_b\}$、$B=\{0,\ldots,p-1\}\setminus G$，$g=|G|$。对 $b\in B$ 记 $e_b=F_b/p\bmod p$，$T_{a,b}=e_b+aL_b$。由 (2) 逐个检查因子，得到三个互斥条件。

- $v_p(F_n)=0$ 当且仅当全部数位在 $G$。
- $v_p(F_n)=1$ 当且仅当恰有一个坏数字 $b$，且其紧邻高位 $a$ 满足 $T_{a,b}\ne0$。最高位若坏，取 $a=0$。
- 其余情形恰为 $v_p(F_n)\ge2$。若 $L_b\ne0$，额外升阶的高邻只能是 $-e_b/L_b$；若 $L_b=0$，则该坏位的局部因子是否升阶与邻位无关。

记 $A_0=\#\{b\in B:e_b\ne0\}$、$A_1=\#\{(a,b)\in G\times B:T_{a,b}\ne0\}$。区间 $[0,p^m)$ 中三个类的基数为
$$
N_0=g^m,\qquad N_1=A_0 g^{m-1}+(m-1)A_1 g^{m-2},\qquad N_{\ge2}=p^m-N_0-N_1 .
\tag{3}
$$
$m=1$ 时省略第二项。首项数坏位恰是最高位的词；其余 $m-1$ 个位置均须同时固定该位和高邻。$p=29$ 的数据如下。

| $b$ | $e_b$ | $L_b$ | 造成额外升阶的好高邻 |
|---:|---:|---:|---|
| 12 | 7 | 3 | 17 |
| 14 | 2 | 4 | 无；唯一解 14 本身是坏位 |
| 16 | 5 | 18 | 11 |

故 $g=26,\ A_0=3,\ A_1=76$，$m=2$ 的三类数为 $(676,154,11)$，$m=3$ 为 $(17576,5980,833)$。整数递推独立给出 $F_{335}\equiv3\cdot29^2$、$F_{505}\equiv6\cdot29^2\bmod29^3$，两数均恰有一个坏位且估值恰为二。$418=14\cdot29+12$ 属于另一种情况，有两个坏位而同样具有精确估值二。

**估值一时，除掉 $p$ 后还剩什么？** 记 $f_a=F_a\bmod p$、$\mu=\sum_{a\in G}\delta_{f_a}$，在 $\mathbb F_p^\times$ 上用乘法卷积，$\delta_x$ 表示单位点质量。按整数个数计的精确分布为
$$
\operatorname{hist}_{v_p=1}(F_n/p)=
\sum_{\substack{b\in B\\e_b\ne0}}\delta_{e_b}*\mu^{*(m-1)}
+(m-1)\sum_{\substack{a\in G,\ b\in B\\T_{a,b}\ne0}}
                 \delta_{f_a T_{a,b}}*\mu^{*(m-2)} .
\tag{4}
$$
$m=1$ 时仍省略第二项。这由 (2) 除去唯一的 $p$ 得到；高邻既参与修正也贡献自身的 $f_a$。设 $H=\langle f_a:a\in G\rangle\le\mathbb F_p^\times$。$\mu/g$ 含单位元且生成 $H$，其卷积幂在 $H$ 上指数趋均匀。式 (4) 因此给出对每个可能陪集的**确切总质量**和陪集内部的渐近均匀性。若 $A_1>0$ 且 $m\to\infty$，内部类别权重极限只须在 $A_1$ 个许可 $(a,b)$ 等权统计相应 $T_{a,b}H$；若仅有最高位项，则使用相应 $e_bH$。$N_1=0$ 时不作条件化。

## 3. 单数字乘积与相邻数字修正渐近独立

在全好数字上独立均匀取 $m$ 位。令 $U_b=F_b\bmod p^2$、$\ell_b=L_b/f_b\bmod p$，并记
$$
D_m=\prod_j U_{b_j},\qquad E_m=\sum_j b_{j+1}\ell_{b_j}\pmod p,\qquad
F_n\equiv D_m(1+pE_m)\pmod{p^2}.
$$
令 $K=\langle U_b:b\in G\rangle\le(\mathbb Z/p^2)^\times$。

**定理 2。** 对 $p\ge5$，$(D_m,E_m)$ 在 $K\times\mathbb F_p$ 上指数趋于均匀分布，因此两个分量渐近独立；$F_n$ 在 $H$ 模 $p^2$ 的整逆像上指数趋于均匀。这些结论不假定 $H=\mathbb F_p^\times$。$p=3$ 时 $G=\{0,1,2\}$，$E_m=0$ 恒成立，$U_1=2$ 生成 $(\mathbb Z/9)^\times$，所以 $F_n=D_m$ 仍渐近均匀于全部单位。

从高位向低位读，初始前缀的相邻数字为 0。从 $a$ 至 $b$ 的边附带 $(U_b,a\ell_b)$，而至 0 的边附带 $(1,0)$。以 0 为基点的环 $0,b,0$ 产生 $(U_b,0)$；以 $0,a,b,0$ 的因子除以两个单环，产生 $(1,a\ell_b)$。有限群中环的逆同样可由重复环实现。又 $0,1\in G$，$f_1=2,L_1=3$，故 $p\ge5$ 时 $a=b=1$ 生成全部加法主因子。任一状态可移到数字 0、补成任一所需群坐标、再前往目的数字。零处自环令周期为一。固定当前、下一数字后，群坐标的变化是平移，故“数字均匀 × 群均匀”平稳。这证明联合结论。实际 $F_n$ 的群是 $(D,E)\mapsto D(1+pE)$ 的像，恰为所述整逆像。

**一个显式谱界。** 对 $K$ 的角色 $\chi$ 与 $t\in\mathbb F_p$，写 $e_p(x)=\exp(2\pi i x/p)$；作用于好数字的矩阵为
$$
M_{\chi,t}(a,b)=g^{-1}\chi(U_b)e_p(t a\ell_b).
$$
$(D_m,E_m)$ 的该傅里叶系数为 $\mathbf e_0^{\mathsf T}M_{\chi,t}^m\mathbf1$。当 $t=0$，系数恰为 $(g^{-1}\sum_b\chi(U_b))^m$。若 $\chi$ 非平凡，其模小于一，因 $U_0=1$ 且 $U_b$ 生成 $K$。若 $t\ne0,p\ge5$，每项绝对值为 $1/g$，全体奇异值平方和为 1。第 $0,1$ 行列构成的二阶子式绝对值为 $|e_p(t\,3/2)-1|/g^2\ge 2\sin(\pi/p)/g^2$，其中 $3/2$ 取模 $p$。所有二阶子式模平方和等于所有两两奇异值平方乘积之和；若最大奇异值平方为 $1-\delta$，此和至多 $(1-\delta)\delta+\delta^2/2\le\delta$。因此
$$
\|M_{\chi,t}\|_2\le r_1=\sqrt{1-4\sin^2(\pi/p)/g^4}<1.
$$
特别地，上述“野”傅里叶系数的模至多 $\sqrt g\,r_1^m$。固定 $p$，由有限傅里叶反演即可得到指数收敛；该界没有宣称对 $p\to\infty$ 有一致正谱隙。同一联合群证明也适用于前述 $r$ 次幂和的 $p\nmid r$ 情形，此时 $L_1=r$。

**两种抽样的区别。** 全好时，朴素等式 $F_n\equiv D_m\bmod p^2$ 成立恰当 $E_m=0$，概率趋 $1/p$。若在全部 $[0,p^m)$ 中抽取而 $B\ne\varnothing$，凡有至少两个坏位，朴素等式两边都为零，因此失败概率至多 $(g^m+m|B|g^{m-1})/p^m\to0$。有限实算中，$p=29,m=4$ 的 456,976 个全好词已有 23,548 个联合支持值，等于 $|K|p$，但朴素等式仅 16,533 次成立；满支持并不要求此时已经均匀。

## 4. 证据范围

同目录的 franel_check.py 仅用 Python 标准库。先由整数递推 $(n+1)^2F_{n+1}=(7n^2+7n+2)F_n+8n^2F_{n-1}$ 求至 $n=4100$，前 151 项与原二项式定义直接比较。对全部奇素数 $p\le41$ 和全部 $0\le n\le4100$，程序将 (2) 与该独立递推核对；模 $p^2$ 的逐数字状态计数又对照了 (3)、(4)，在 $m=1,2,3,5,8$ 验证每个估值一的单位部。其他幂次用 $p=3,5,7,11,\ 2\le r\le7,\ n<p^2$ 另从原二项式和检验。167 个奇素数 $p\le997$ 的单数字模 $p$ 单位群直接计算都等于 $\mathbb F_p^\times$；所有素数的一般命题在此仍未证明。可重跑结果保存在 franel_checked.json 中。
