# Legendre 压力测试：平方盆地、进位与 Möbius 消去

状态：`ACTIVE RESEARCH NOTE`  
结论纪律：本文**没有证明 Legendre 猜想**。本文只记录已经普通数学证明、有限计算反例、以及由此留下的明确开放障碍。

## 1. 为什么选择 Legendre 猜想

Legendre 猜想要求对每个整数 `k>=1`，开区间

\[
(k^2,(k+1)^2)
\]

至少含一个素数。

这与进取数论的平方坍缩盆地直接重合：`C_2(n)=k^2` 的盆地是

\[
[k^2,(k+1)^2-1].
\]

因此该公开难题可以不改变对象地改写为：每个平方坍缩盆地的内部状态中至少有一个素数。

外部基准：截至本笔记形成时，该猜想仍未解决。Campbell 2026 给出所有相邻平方之间必有一个至多含 3 个素因子的整数；Sorenson–Webster 已把 Oppermann/Legendre 的直接计算验证推进到 `k<=7.05*10^13`。见 `SRC-CAMPBELL-2026-SQUARES`、`SRC-SORENSON-WEBSTER-2025`。

## 2. 记号

定义平方盆地内部

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\qquad |I_k|=2k.
\]

对正整数 `d` 定义命中数

\[
H_d(k)
=
\#\{n\in I_k:d\mid n\}
=
\left\lfloor\frac{k^2+2k}{d}\right\rfloor
-
\left\lfloor\frac{k^2}{d}\right\rfloor.
\]

更一般地，对整数幂 `p>=1` 定义

\[
H_{p,d}(k)
=
\left\lfloor\frac{(k+1)^p-1}{d}\right\rfloor
-
\left\lfloor\frac{k^p}{d}\right\rfloor,
\]

以及幂间隔

\[
W_p(k)=(k+1)^p-k^p.
\]

## 3. 定理 L001 —— 根—因子视界

状态：`PROVED`

若 `n>1` 至少含有 `m` 个素因子（重数计入），则至少有一个素因子满足

\[
p\le R_m(n).
\]

证明：若这 `m` 个素因子都大于 `R_m(n)`，则它们都至少为 `R_m(n)+1`，从而

\[
n\ge(R_m(n)+1)^m>n,
\]

矛盾。

因此在平方盆地内部 `n\in I_k` 时，`R_2(n)=k`，于是

\[
n\text{ 合数}
\iff
\exists\text{ 素数 }p\le k,\ p\mid n.
\]

这给出了 Legendre 问题的有限筛截断：只需考虑 `p<=k`。

## 4. 定理 L002 —— 欧几里得盆地下降

状态：`PROVED`

令

\[
k=qd+t,
\qquad 0\le t<d.
\]

则对所有 `p>=1`，

\[
\boxed{
H_{p,d}(k)
=
\frac{W_p(k)-W_p(t)}{d}
+
H_{p,d}(t)
}.
\]

证明：因为 `k congruent t (mod d)`，所以

\[
k^p-t^p
\]

和

\[
(k+1)^p-(t+1)^p
\]

都被 `d` 整除。把两个端点分别减去对应的局部端点后再取整数商，整除部分直接提出，余下正是 `H_{p,d}(t)`。

平方情形 `p=2` 特别简化为

\[
\boxed{H_d(k)=2q+H_d(t)}.
\]

这是一个严格的尺度下降：全局命中数被拆成确定的宏观主体与一个 `t<d` 的局部盆地命中。

## 5. 定义 L003 —— 平方进位

定义

\[
\kappa_d(k)=H_d(k\bmod d).
\]

于是 L002 给出

\[
\boxed{H_d(k)=2\left\lfloor\frac{k}{d}\right\rfloor+\kappa_d(k)}.
\]

若 `t=k mod d`，则

\[
\kappa_d(k)
=
\left\lfloor
\frac{(t^2\bmod d)+2t}{d}
\right\rfloor.
\]

因为 `0<=t<d`，有

\[
0\le (t^2\bmod d)+2t<3d,
\]

所以得到平方情形特有的三值性：

\[
\boxed{\kappa_d(k)\in\{0,1,2\}}.
\]

对更高次幂，局部盆地宽度通常不再小于固定倍数的 `d`，因此这种三值压缩是平方层的特殊性质。

## 6. 定理 L004 —— Möbius 进位恒等式

状态：`PROVED`

令

\[
P_k=\prod_{p\le k}p
\]

为不超过 `k` 的素数之积，`mu` 为经典 Möbius 函数。Möbius 反演本身属于既有数学，项目采用该工具而不主张其新颖性，见 `SRC-ROTA-1964-MOBIUS`。

由 L001，`I_k` 中与 `P_k` 互素的状态恰好就是素数，因此若

\[
\Pi(k)=\#\{p:k^2<p<(k+1)^2,\ p\text{ 为素数}\},
\]

则

\[
\Pi(k)=\sum_{d\mid P_k}\mu(d)H_d(k).
\]

代入 L003：

\[
\Pi(k)
=
2\sum_{d\mid P_k}\mu(d)\left\lfloor\frac{k}{d}\right\rfloor
+
\sum_{d\mid P_k}\mu(d)\kappa_d(k).
\]

第一项中的和恰好计算 `1..k` 中与 `P_k` 互素的整数个数，而唯一这样的整数是 `1`。因此

\[
\boxed{
\Pi(k)
=
2+
\sum_{d\mid P_k}\mu(d)\kappa_d(k)
}.
\]

所以 Legendre 猜想严格等价于

\[
\boxed{
\sum_{d\mid P_k}\mu(d)\kappa_d(k)\ge-1
}.
\]

这不是证明；它把难题压成了一个有符号局部进位平衡问题。

## 7. 定理 L005 —— 二进制奇偶压缩

状态：`PROVED`

对奇数 `d` 定义

\[
\delta_d(k)=\kappa_d(k)-\kappa_{2d}(k).
\]

令

\[
q=\left\lfloor\frac{k}{d}\right\rfloor.
\]

则

\[
\boxed{
\delta_d(k)\in\{0,(-1)^q\}
}.
\]

因此存在二值变量

\[
\varepsilon_d(k)\in\{0,1\}
\]

使

\[
\delta_d(k)=(-1)^q\varepsilon_d(k).
\]

证明要点：`H_d(k)` 对应一个连续的整数商区间，而 `H_{2d}(k)` 正好数其中的偶数商。长度为偶数的连续整数块中奇偶数数量完全平衡；唯一可能的不平衡来自平方进位产生的最多两个边界商。当 `q` 为偶数时差只能为 `0` 或 `+1`，当 `q` 为奇数时差只能为 `0` 或 `-1`。

将 L004 中的 divisor 按 `d <-> 2d` 配对，得到

\[
\boxed{
\Pi(k)
=
2+
\sum_{\substack{d\mid P_k\\d\text{ 奇}}}
\mu(d)
(-1)^{\lfloor k/d\rfloor}
\varepsilon_d(k)
}.
\]

因此三值局部进位可以进一步压成**二值边界事件 + 商层奇偶符号**。

## 8. 中心锚点与定理 L006 —— 锚点面消去

把平方区间改写到中心锚点

\[
M=k(k+1).
\]

则

\[
I_k=M+\{1-k,\ldots,k\}.
\]

若 `p|M`，则

\[
p\mid(M+s)\iff p\mid s.
\]

这说明 `k(k+1)` 的素因子在中心坐标中全部对齐到零余数类。

令

\[
A_k=\prod_{\substack{p\le k\\p\mid k(k+1)}}p.
\]

则对任何 `d|A_k`，令 `t=k mod d`。因为

\[
t(t+1)\equiv0\pmod d,
\]

有：

- 若 `d|k`，则 `t=0`，从而 `kappa_d(k)=0`；
- 否则 `0<t<d` 且 `t^2 congruent -t (mod d)`，故 `t^2 mod d=d-t`，从而 `kappa_d(k)=1`。

因此得到：

\[
\boxed{
\sum_{d\mid A_k}\mu(d)\kappa_d(k)=0
\qquad(k\ge2)
}.
\]

证明也可以按 `k` 与 `k+1` 的互素素因子集合拆开：只含 `k` 一侧素因子的项全部为零；一旦含 `k+1` 一侧的素因子，`kappa=1`，而对 `k` 一侧所有子集的 Möbius 和为零。

含义：**所有只生活在中心锚点素因子 Boolean 面上的进位贡献完全消去。真正困难的 Möbius 项必须至少包含一个不整除 `k(k+1)` 的“横向素数”。**

## 9. 锚点 Möbius 转移

把不超过 `k` 的素数分成

\[
A_k=\prod_{p\mid k(k+1)}p,
\qquad
B_k=\prod_{\substack{p\le k\\p\nmid k(k+1)}}p.
\]

对 `b|B_k` 定义

\[
\Lambda_b(k)
=
\sum_{a\mid A_k}\mu(a)\kappa_{ab}(k).
\]

则 L004 可重写为

\[
\Pi(k)=2+
\sum_{b\mid B_k}\mu(b)\Lambda_b(k),
\]

而 L006 给出

\[
\Lambda_1(k)=0.
\]

所以

\[
\boxed{
\Pi(k)=2+
\sum_{\substack{b\mid B_k\\b>1}}
\mu(b)\Lambda_b(k)
}.
\]

这把问题的支撑从全部小素数缩到“横向素数与锚点素数的交互”。

一个曾经很诱人的更强猜测是

\[
|\Lambda_b(k)|\le\omega(A_k).
\]

有限搜索已经给出反例：

\[
k=456,
\quad A_k=2\cdot3\cdot19,
\quad b=5,
\quad \Lambda_5(456)=-4,
\]

而 `omega(A_k)=3`。因此该线不再作为候选定理。

## 10. 失败路线：仅有平方剩余/公共根仍然不够

另一个候选想法是：也许禁余数类全部来自同一个平方根，就足以阻止长度 `2k` 的完全覆盖。

这也不成立。

存在

\[
y=73,
\]

以及

\[
x=33641709557196602631265058865,
\]

令

\[
P_{73}=\prod_{p\le73}p
=40729680599249024150621323470,
\]

则直接整数验证得到

\[
\gcd(x^2+r,P_{73})>1
\qquad(1\le r\le146).
\]

所以从 `x^2+1` 到 `x^2+146` 的全部状态都被 `p<=73` 的素数覆盖。这里各模素数下的平方根不仅局部存在，而且确实来自同一个整数 `x`。

关键区别是：

\[
x\gg73.
\]

因此真正的 Legendre 约束不是“公共平方根”，而是更强的

\[
\boxed{x=y=k}.
\]

也就是**根本身同时等于筛选截断尺度**。本项目把尚未被排除的特殊结构称为：

**Bounded Common-Root Coherence / 有界公共根相干性**，更精确地说是 **Root–Cutoff Coupling / 根—截断耦合**。

这与传统 Jacobsthal/覆盖问题有明显邻接关系，因此当前一律标记为 `NOVELTY_UNVERIFIED`，不能把新术语当成历史新颖性证明。

## 11. 当前真正的障碍

L004–L006 并没有绕过经典筛法的 parity barrier。Campbell 的 2026 结果也明确说明其加权筛框架在继续把 `Omega<=3` 推向更低素因子数时存在自然限制（`SRC-CAMPBELL-2026-SQUARES`）。

进取数论压力测试现在把需要的新工具定位得更窄：

1. 不能只控制总删除量；
2. 不能只利用“是平方剩余”；
3. 不能只利用“来自一个公共根”；
4. 必须利用 `root = cutoff = k` 的自洽约束；
5. 必须控制奇偶 Möbius 层之间的**有符号**相消，而不是只有非负前像计数。

一个值得继续攻击的形式是寻找对

\[
\mu(d)(-1)^{\lfloor k/d\rfloor}\varepsilon_d(k)
\]

的符号反转配对、商层递推或横向素数分层，使绝大多数项成对消去，并把未配对边界项压到总和 `>=-1`。

## 12. 对 P008 的反馈

这个压力测试说明，P008“最小代数结构”至少需要认真比较以下成熟结构：

- 交换幂等坍缩/半格；
- Boolean divisor lattice；
- incidence algebra；
- Möbius inversion；
- 有符号边界/进位观察量；
- 欧几里得下降形成的多尺度递推。

现有“前像数量单调”只提供非负信息，而公开素数难题立刻要求处理有符号相消。因此 P008 不应只问“怎样表达坍缩”，还应问“怎样在坍缩格上表达交叠层级与符号反演”。

## 13. 当前状态

- `L001` 根—因子视界：`PROVED`
- `L002` 欧几里得盆地下降：`PROVED`
- `L003` 平方三值进位：`PROVED`
- `L004` Möbius 进位恒等式：`PROVED`
- `L005` 二进制奇偶压缩：`PROVED`
- `L006` 锚点面消去：`PROVED`
- `|Lambda_b|<=omega(A_k)`：`DISPROVED_BY_COUNTEREXAMPLE`
- “任意公共平方根即可阻止完全覆盖”：`DISPROVED_BY_EXPLICIT_WITNESS`
- “有界公共根相干性足以推出 Legendre”：`OPEN`
- Legendre 猜想：`OPEN / NOT PROVED HERE`

可执行验证见 `src/enterprise_math/legendre.py` 与 `tests/test_legendre_pressure.py`。
