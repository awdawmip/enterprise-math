# 勒让德压力测试 — 补充 10

状态：`ACTIVE RESEARCH NOTE`  
范围：通过精确大模数命中并集，对高带 three-prime 资源做盆地级汇总  
依赖：P017 L034–L041，尤其是 L039–L040  
纪律：本补充不证明勒让德猜想，也不引入新的筛法形式。目的只是把已经 canonical 的二值命中事件转化为真正的跨 shell 不等式。

## 1. 为什么下一步必须是全局的

L036 与 L040 都是在每个 least-factor shell 内分别控制 three-prime states。这是有效的，但把各 shell 上界直接相加，仍允许同一个 cofactor resource prime 在另一个 shell 中再次被计数。

第一版修正思路，是同时用下面两个量控制资源素数 `r` 的使用次数：

- `r` 可以出现的 least-factor shells 数量；
- 整个平方盆地中的命中数 `H_r(k)`。

这个上界成立，但仍然丢失信息。L039 已经给了更强的事实：对每个合格的 least prime `p`，模数 `p r` 本身就至少为 `2k`，所以它在盆地中的命中是二值的，并且命中状态可以精确写出。

因此正确的下一对象不是平均密度，而是**这些精确命中状态的集合并集**。

---

## 2. 高带 three-prime 可行的最小素因子

令

\[
U=(k+1)^2-1.
\]

一个高带 three-prime state 写成

\[
n=p\ell s,
\qquad
p\le\ell\le s,
\]

并满足

\[
p^2\ge2k.
\]

又必有

\[
p^3\le n\le U.
\]

因此定义

\[
\mathcal P_H(k)
=
\{p\le k:p\text{ 为素数},\ p^2\ge2k,\ p^3\le U\}.
\]

不在这个有限集合中的素数，不可能成为高带 three-prime state 的最小素因子。

---

## 3. 一个资源素数的合格使用条件

固定一个作为 triple state 两个 cofactor primes 之一的素数 `r`。

若

\[
n=p\ell s
\]

使用资源 `r`，则必有

\[
p\le r.
\]

另一个 cofactor prime 至少为 `p`，因此

\[
n\ge p^2r.
\]

故必要条件为

\[
p^2r\le U.
\]

定义

\[
\mathcal E_r(k)
=
\{p\in\mathcal P_H(k):p\le r,\ p^2r\le U\}.
\]

对其中任意 `p`，

\[
pr\ge p^2\ge2k.
\]

开平方盆地共有 `2k` 个连续状态，其跨度只有 `2k-1`，所以其中至多存在一个 `pr` 的倍数。

若该倍数存在，记为

\[
x_{p,r}(k),
\]

若

\[
H_{pr}(k)=0,
\]

则保持未定义。

根据 L039，它是否存在，恰好由

\[
k(k+1)\bmod(pr)
\]

的共同中心 residue event 决定。

---

## 4. 资源命中并集

定义

\[
X_r(k)
=
\{x_{p,r}(k):p\in\mathcal E_r(k),\ H_{pr}(k)=1\},
\]

这里的大括号是**状态集合**：如果不同模数命中了同一个状态，只计一次。

令

\[
c_r(k)=|X_r(k)|.
\]

这是一个精确的有限整数容量。

它自动满足较弱的两个上界

\[
c_r(k)
\le
\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\]

以及

\[
c_r(k)\le H_r(k),
\]

因为 `X_r(k)` 中每个状态都是盆地中的 `r` 倍数。

采用并集的意义在于：上面两个不等式都可能严格成立，因为不同合格模数 `pr` 可以命中同一个盆地状态。

---

## 5. 精确平方 cofactor 修正项

令 `E_H(k)` 表示高带 three-prime states 中 cofactor 为平方的状态数量：

\[
q=r^2.
\]

固定 least prime `p`，cofactor window 的跨度至多为 `p-1`，因此其中至多存在一个平方根不小于 `p` 的素数平方。

而且，只要素数 `r>=p` 满足

\[
r^2\in W_p(k),
\]

则 `r^2` 自动是 `p`-rough，于是

\[
p r^2
\]

确实就是该 shell 中一个 three-prime state。

因此 `E_H(k)` 不是未知误差项，而是满足下列条件的有限 `(p,r)` 对的精确数量：

\[
p\in\mathcal P_H(k),
\quad
r\text{ 为素数},
\quad
p\le r,
\quad
r^2\in W_p(k).
\]

---

## 6. L041 — 全局命中并集资源上界

状态：`PROVED`。

令 `T_H(k)` 表示**所有** least-factor shells 中高带 three-prime states 的总数。

则

\[
\boxed{
2T_H(k)-E_H(k)
\le
\sum_r c_r(k).
}
\]

从而

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{E_H(k)+\sum_r c_r(k)}{2}
\right\rfloor.
}
\]

资源素数只有有限多个：对每个合格 least prime `p`，任意 cofactor resource 都满足

\[
r\le\left\lfloor\frac{U}{p^2}\right\rfloor.
\]

### 证明

对每个高带 three-prime state

\[
n=p\ell s,
\]

记它的 cofactor prime support 为

\[
S(n)=\{\ell,s\}.
\]

若 `ell<s`，则 `|S(n)|=2`；若 `ell=s`，则 `|S(n)|=1`。因此

\[
\sum_n |S(n)|
=
2T_H(k)-E_H(k).
\]

现在固定资源素数 `r`，令 `u_r(k)` 为 cofactor support 中包含 `r` 的实际高带 three-prime states 数量。

任取其中一个状态。它的 least prime `p` 属于 `P_H(k)`。因为 `r` 是 cofactor prime，

\[
p\le r,
\qquad
p^2r\le n\le U,
\]

故 `p` 属于 `E_r(k)`。

该状态又被 `pr` 整除。由于 `pr>=2k`，模数 `pr` 在盆地中至多有一个 hit，而这个实际状态必然就是唯一 hit `x_(p,r)(k)`。所以 `u_r(k)` 计数的每个实际状态都属于集合 `X_r(k)`。

因此

\[
u_r(k)\le c_r(k).
\]

对所有资源素数求和：

\[
2T_H(k)-E_H(k)
=
\sum_r u_r(k)
\le
\sum_r c_r(k).
\]

结论即得。∎

---

## 7. 为什么它强于简单相加二值模数

可以使用更弱的容量

\[
\sum_{p\in\mathcal E_r(k)}H_{pr}(k).
\]

L041 则直接对**命中状态本身**取并集。

例如在

\[
k=110,
\qquad
r=19
\]

时，两个模数

\[
17\cdot19
\qquad\text{和}\qquad
19^2
\]

都命中了同一个盆地状态

\[
12274.
\]

因此两个二值模数 hit 实际只消耗一个 resource-19 state slot：

\[
X_{19}(110)=\{12274\},
\qquad
c_{19}(110)=1.
\]

这就是经过反例筛选后真正保留下来的“共同中心相关性”：不是宣称 hit bits 在统计上普遍稀疏，而是利用它们实现状态之间的精确碰撞。

---

## 8. 已核验的有限容量

可执行回归层会在有限 `k` 范围内，将该定理与真实 high-band triple states 直接对照。

保留两个固定 checkpoint：

### `k=110`

\[
\sum_r c_r(110)=7,
\qquad
E_H(110)=1.
\]

因此

\[
T_H(110)\le4.
\]

已经组合过的逐 shell L036/L040 上界之和为 `5`，所以 L041 在这个 checkpoint 上严格更强。

### `k=500`

\[
\sum_r c_r(500)=33,
\qquad
E_H(500)=1,
\]

故

\[
T_H(500)\le17.
\]

这些只是回归 witness，不是渐近结论。

---

## 9. 研究诊断发生了什么变化

此前有限实验已经否定了下面这句话：

> 共同平方中心会让二值 hit bits 普遍变得稀疏。

L041 **没有**恢复这个说法。

它利用的是另一个事实：

> 即使很多合格模数都发生 hit，它们的唯一 hit states 仍可能碰撞；实际资源使用次数由实现后的 hit-state union 基数控制。

这是确定性的、精确的、盆地级的。

它也把更早的 P017 工作继续合并起来：

\[
H_d(k)
\longrightarrow
\text{大模数唯一状态}
\longrightarrow
\text{跨 shell 资源并集}.
\]

不需要再新增 modular invariant。

---

## 10. 剩余阻碍

L041 只控制高带的 **three-prime** 部分。

现在主要未解部分被更清楚地分开：

1. prime cofactor `q` 对应的 semiprime states `p q`；
2. `p^2<2k` 的较低 least-factor shells；
3. 如何把精确有限的 hit-union sum 转化成足够强的统一解析上界，并与前两部分耦合。

所以下一步不应再创造同一 hit 的另一种表示。应直接检验

\[
\sum_r c_r(k)
\]

是否存在有用的统一上包络，或者高带收益能否和 semiprime / lower-band 计数发生耦合。若两者都不能产生新不等式，这条路线就应停在 L041。
