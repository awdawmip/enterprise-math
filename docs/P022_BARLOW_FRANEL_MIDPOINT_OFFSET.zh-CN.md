# P022 — Franel 零位几何的通用中点偏移伴随序列

状态：`ACTIVE RESEARCH NOTE / EXACT UNIVERSAL REDUCTION / PRIOR-ART SENSITIVE`  
Owner：`program/p022-geometry-v2`  
依赖：Franel recurrence；Jarvis--Verrill 强制中点零；p-Lucas zero-digit geometry  
跨路线相关：P011 collision identifiability；P018 defect/holonomy；P023 task-relative repair

## 1. 问题

对奇素数

\[
p\equiv5,7\pmod8,
\]

令

\[
m=\frac{p-1}{2}.
\]

半指标定理给出

\[
F_m\equiv0\pmod p.
\]

此前完整 zero-digit set

\[
Z_p=\{1\le j\le p-1:p\mid F_j\}
\]

由镜像对称、p-Lucas 与 Franel recurrence 描述，但这些描述表面上仍需对每个 prime 单独计算。

本笔记把 prime 从中点附近的递推中完全消掉：**一个固定的有理伴随序列同时编码所有强制中点 prime 的 zero geometry。**

---

## 2. 在强制中点重新中心化 Franel recurrence

Franel recurrence 为

\[
(n+1)^2F_{n+1}
=(7n^2+7n+2)F_n+8n^2F_{n-1}.
\]

在强制中点模 `p` 有

\[
m\equiv-\frac12.
\]

取 offset `d>=0`，令

\[
n=m-d.
\]

则

\[
n\equiv-\frac{2d+1}{2},
\qquad
n+1\equiv-\frac{2d-1}{2}
\pmod p,
\]

并且

\[
7n^2+7n+2
\equiv\frac{28d^2+1}{4}\pmod p.
\]

由于相邻 Franel zeros 不可能同时出现，而 `F_m=0`，所以

\[
F_{m-1}\not\equiv0\pmod p.
\]

用这个单位归一化：

\[
R_d^{(p)}
:=
\frac{F_{m-d}}{F_{m-1}}\pmod p.
\]

于是

\[
R_0^{(p)}=0,
\qquad
R_1^{(p)}=1.
\]

代入中心化后的系数得到

\[
\boxed{
8(2d+1)^2R_{d+1}^{(p)}
=
(2d-1)^2R_{d-1}^{(p)}
-(28d^2+1)R_d^{(p)}.
}
\]

注意：递推系数中已经不再出现 `p`。

---

## 3. P022-LI27 — 通用中点伴随定理

定义有理序列

\[
G_0=0,
\qquad
G_1=1,
\]

对 `d>=1`，

\[
\boxed{
8(2d+1)^2G_{d+1}
=
(2d-1)^2G_{d-1}
-(28d^2+1)G_d.
}
\]

对 `0<=d<m`，递推中出现的所有奇数 denominator factor 都严格小于 `p`，因此在模 `p` 下均可逆。

`R_d^(p)` 与 `G_d` 具有相同初值并满足同一个二阶递推，所以

\[
\boxed{
F_{m-d}
\equiv
G_dF_{m-1}
\pmod p
\qquad(0\le d<m).}
\]

这就是通用 midpoint-companion theorem。

换言之，经典 Franel recurrence 在强制中点做半整数中心化后，得到一个固定的有理解；它的模 `p` 约化控制所有强制中点素数的局部乃至整个左半 zero geometry。

---

## 4. P022-LI28 — 全部 zero digits 变成一个通用整数分子序列的素因子问题

把 `G_d` 约成最简分数：

\[
G_d=\frac{N_d}{Q_d},
\qquad
\gcd(N_d,Q_d)=1.
\]

当 `1<=d<m` 时，`p` 不整除 `Q_d`。又因 `F_(m-1)` 模 `p` 可逆，所以 LI27 给出

\[
\boxed{
p\mid F_{m-d}
\iff
p\mid N_d.}
\]

因此整个左半 zero geometry 都由固定整数序列

\[
N_1,N_2,N_3,\ldots
\]

的素因子结构控制，而不再需要为每个 `p` 单独重新生成 Franel table。

前几项为

\[
\begin{array}{c|r}
d&N_d\\
\hline
1&1\\
2&-29\\
3&157\\
4&-929\\
5&53185\\
6&-42700613\\
7&291801013\\
8&-2037217865
\end{array}
\]

例如

\[
53185=5\cdot11\cdot967.
\]

符号对 zero criterion 没有影响。

---

## 5. P022-LI29 — 完整 zero alphabet 与 rank of apparition

Jarvis--Verrill 镜像给出

\[
j\in Z_p
\iff
p-1-j\in Z_p.
\]

定义

\[
H_p
=
\{1\le d<m:p\mid N_d\}.
\]

则

\[
\boxed{
Z_p
=
\{m\}
\cup
\{m-d,m+d:d\in H_p\}.}
\]

因此

\[
\boxed{z_p=1+2|H_p|.}
\]

最早 zero 对应最远的左偏移，所以

\[
\boxed{r_p=m-\max(H_p\cup\{0\}).}
\]

此前“中点 primitive”的判据也可重新写成

\[
\boxed{
p\text{ 在 }F_m\text{ 首次出现}
\iff
p\nmid N_d\text{ 对全部 }1\le d<m.}
\]

于是 midpoint primitivity 已经变成对一个**通用 companion numerator sequence** 的 prime-avoidance 条件，而不是每个 prime 独立的问题。

---

## 6. 精确例子

### `p=29`

\[
m=14,
\qquad
29\mid N_2.
\]

`m` 以内没有其他 companion hit，所以

\[
Z_{29}=\{12,14,16\},
\qquad
r_{29}=12.
\]

这直接由

\[
N_2=-29
\]

解释最早的非 primitive 强制 midpoint。

### `p=157`

\[
m=78.
\]

companion hits 为

\[
d=3,62.
\]

所以

\[
\boxed{
Z_{157}=\{16,75,78,81,140\},
\qquad
r_{157}=16.}
\]

靠近中点的 `75,81` 来自 `N_3=157`；远离中点的 zero `16` 则来自更后的 numerator `N_62`。

### `p=173`

\[
m=86,
\]

唯一左侧 hit 为

\[
d=82.
\]

因此

\[
\boxed{Z_{173}=\{4,86,168\},\qquad r_{173}=4.}
\]

这说明 companion theorem 不只是“中点附近的小邻域近似”：zero 可以离中点极远，但仍由同一个通用序列编码。

---

## 7. 对 p-Lucas basin 的直接含义

对强制中点 prime，不再需要直接计算

\[
F_1,\ldots,F_{p-1}
\]

才能获得 zero alphabet。

只需判断

\[
N_1,\ldots,N_{m-1}
\]

中哪些被 `p` 整除。

因此完整 `p^L` block 中非零项数量可直接写成

\[
\boxed{
\left(
 p-1-2\#\{1\le d<m:p\mid N_d\}
\right)^L.}
\]

Franel p-Lucas basin 被降成了一个通用 companion sequence 的 prime-divisor statistic。

---

## 8. 对 half-defect support 问题的直接含义

设 midpoint 的 canonical central-binomial elimination 使用更早指标集合

\[
S_p\subset\{1,\ldots,m-1\}.
\]

对 `j in S_p` 定义 offset

\[
d=m-j.
\]

由 LI28，support avoidance 精确等价于

\[
\boxed{
S_p\cap Z_p=\varnothing
\iff
p\nmid N_{m-j}
\quad\text{对所有 }j\in S_p.}
\]

所以原来经验性的 support-avoidance 问题现在被改写为一个纯整数序列问题：

> 通用 companion numerators 的 prime divisors，是否避开 canonical A-elimination support 的 offset image？

这还没有证明 `p=5,23 mod24` 的目标 family 永远 avoidance，但已经把 Franel table 本身从未知量中移除。

---

## 9. Prior-art 边界

这里使用的已有数学包括：

- 经典 Franel recurrence；
- Jarvis--Verrill reflection；
- 二阶递推唯一性；
- Franel recurrence 二维解空间的一般研究。

2026 年已有工作还显式研究了整数指标 Franel recurrence solution space 与 Casoratian / continued-fraction basis；这些均属于 prior art。

P022 当前的特定结果，是**强制中点的半整数重中心化**，以及利用所得通用有理伴随序列的分子来统一编码 `Z_p`、`r_p` 与 support-avoidance 问题。

目前定向检索尚未找到完全相同的 midpoint-offset numerator formulation；这不能证明历史新颖性，状态仍为

`NOVELTY_UNVERIFIED`。

---

## 10. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_franel_midpoint_offset.py`；
- `tests/test_p022_barlow_franel_midpoint_offset.py`。

测试核验有理递推、前若干精确 numerators、多组强制 prime 的完整 zero-alphabet 重建，以及 `p=29,157,173` 的 rank 示例。
