# 勒让德压力测试 — 补充 11

状态：`ACTIVE RESEARCH NOTE`  
范围：通过精确大模数命中状态并集，对高带 three-prime 资源做盆地级汇总  
依赖：P017 L035、L039–L041  
纪律：**本文不证明勒让德猜想。** 本文不引入新的筛法形式。规范 L041 处理 anchor-surviving support closure；这里的 L042 则对不同 least-factor shells 中已经知道的大模数命中进行汇总。

## 1. 在规范 L041 之后的位置

规范 L041 解决的是：一个 transverse support product 命中平方盆地后，何时得到精确 support。这里的问题不同。

L036 和 L040 都在每个 least-factor shell 内分别控制 three-prime states。如果只把各 shell 上界相加，同一个 cofactor resource prime 仍可能在另一个 shell 中再次被计数。

L039 已经提供了比 shell 计数更多的信息：只要模数 `d>=2k` 命中盆地，命中状态就是唯一且显式的。因此跨 shell 汇总应当对**已经实现的 hit states**去重，而不是只数合格模数。

---

## 2. 可产生 triple 的高带最小素因子

令

\[
U=(k+1)^2-1.
\]

一个高带 three-prime state 写成

\[
n=p\ell s,
\qquad
p\le \ell\le s,
\qquad
p^2\ge2k.
\]

必有

\[
p^3\le n\le U.
\]

定义有限 least-prime 集合

\[
\mathcal P_H(k)
=
\{p\le k:p\text{ 为素数},\ p^2\ge2k,\ p^3\le U\}.
\]

只有这个集合中的素数可能成为高带 three-prime state 的最小素因子。

---

## 3. 一个资源素数的精确命中状态容量

固定一个作为 triple state 两个 cofactor primes 之一的素数 `r`。

如果状态

\[
n=p\ell s
\]

使用 `r`，则

\[
p\le r.
\]

另一个 cofactor prime 至少为 `p`，所以

\[
n\ge p^2r.
\]

因此定义合格 least-prime 集合

\[
\mathcal E_r(k)
=
\{p\in\mathcal P_H(k):p\le r,\ p^2r\le U\}.
\]

对其中每个 `p`，

\[
pr\ge p^2\ge2k.
\]

因此 L039 保证 `pr` 在开平方盆地中至多命中一个状态。若命中存在，记其唯一状态为

\[
x_{p,r}(k).
\]

定义已实现 hit-state union

\[
X_r(k)
=
\{x_{p,r}(k):p\in\mathcal E_r(k),\ H_{pr}(k)=1\},
\]

不同模数若产生同一个状态，只计一次，并定义

\[
c_r(k)=|X_r(k)|.
\]

这是一个精确的有限整数容量。

它自动满足

\[
c_r(k)
\le
\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\]

以及

\[
c_r(k)\le H_r(k),
\]

因为每个已实现状态本身都是盆地中的 `r` 倍数。并集可以严格小于这两个较粗上界，因为不同模数 `pr` 可能实现为同一个状态。

---

## 4. 精确平方 cofactor 修正

令 `E_H(k)` 表示高带 three-prime states 中 cofactor 为素数平方 `r^2` 的状态数。

对一个 least prime `p`，高带 cofactor window 的长度至多为 `p`，所以跨度至多为 `p-1`。根至少为 `p` 的两个不同平方之间的距离大于这个跨度，因此窗口中至多有一个素数平方。

而且，只要素数 `r>=p` 满足

\[
r^2\in W_p(k),
\]

则 `r^2` 自动是 `p`-rough。所以

\[
p r^2
\]

确实就是 least-factor-`p` shell 中的 three-prime state。

因此 `E_H(k)` 恰好等于满足下列条件的有限 `(p,r)` 对数量：

\[
p\in\mathcal P_H(k),
\qquad
r\text{ 为素数},
\qquad
p\le r,
\qquad
r^2\in W_p(k).
\]

它不是未知误差项。

---

## 5. L042 — 全局命中并集资源上界

状态：`PROVED`。

令 `T_H(k)` 为所有 least-factor shells 中高带 three-prime states 的总数。则

\[
\boxed{
2T_H(k)-E_H(k)
\le
\sum_r c_r(k).
}
\]

因此

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{E_H(k)+\sum_r c_r(k)}{2}
\right\rfloor.
}
\]

资源素数只有有限多个，因为 least-factor-`p` triple 中任意资源都满足

\[
r\le\left\lfloor\frac{U}{p^2}\right\rfloor.
\]

### 证明

对每个高带 triple state

\[
n=p\ell s,
\]

定义其 cofactor prime resource 集合

\[
S(n)=\{\ell,s\}.
\]

非平方 cofactor 满足 `|S(n)|=2`，平方 cofactor 满足 `|S(n)|=1`。故

\[
\sum_n |S(n)|=2T_H(k)-E_H(k).
\]

固定资源素数 `r`，令 `u_r(k)` 为 cofactor support 包含 `r` 的实际高带 triple states 数量。

任取其中一个状态。其 least prime `p` 属于 `P_H(k)`。由于 `r` 是 cofactor prime，而另一个 cofactor prime 至少为 `p`，所以

\[
p\le r,
\qquad
p^2r\le n\le U.
\]

因此 `p` 属于 `E_r(k)`。该状态被 `pr` 整除；因为 `pr>=2k`，L039 说明该模数在盆地中至多有一个 hit。于是这个实际状态必然就是 `x_(p,r)(k)`，从而属于 `X_r(k)`。

因此

\[
u_r(k)\le c_r(k).
\]

对所有资源素数求和得到

\[
2T_H(k)-E_H(k)
=
\sum_r u_r(k)
\le
\sum_r c_r(k),
\]

定理得证。∎

---

## 6. 精确跨 shell 碰撞 witness

在

\[
k=110,
\qquad
r=19
\]

时，两个合格模数

\[
17\cdot19
\qquad\text{与}\qquad
19^2
\]

都命中了同一个盆地状态

\[
12274.
\]

所以两个二值 modulus hits 实际只占一个 resource-19 state slot：

\[
X_{19}(110)=\{12274\},
\qquad
c_{19}(110)=1.
\]

这是此前反例筛选后真正保留下来的共同中心现象。L042 **不**宣称 hit bits 在统计上普遍稀疏，它只使用它们实现出的状态之间的精确碰撞。

---

## 7. 回归 checkpoint

可执行测试会在有限 `k` 范围内，把 L042 与真实 high-band triple states 直接对照。

在 `k=110` 时，

\[
\sum_r c_r(110)=7,
\qquad
E_H(110)=1,
\]

所以

\[
T_H(110)\le4.
\]

已经组合的逐 shell L036/L040 上界之和为 `5`，因此跨 shell 并集在这个 checkpoint 上严格更强。

在 `k=500` 时，

\[
\sum_r c_r(500)=33,
\qquad
E_H(500)=1,
\]

故

\[
T_H(500)\le17.
\]

这些数值只作为实现回归，不是渐近结论。

---

## 8. 研究后果

L042 是这条路线中第一个不依赖平均筛密度、而真正跨不同 least-factor shells 汇总高带 three-prime 资源的结果。

它也进一步压缩了 P017 的语言：

\[
H_d(k)
\longrightarrow
\text{L039 唯一命中状态}
\longrightarrow
\text{L042 跨 shell 状态并集}.
\]

规范 L041 与此正交：它判断 large-support hit 之后的精确 transverse-support closure；L042 则计数一个 cofactor resource 跨 least-factor shells 最多能占据多少状态槽位。

目前未解部分被清楚地分为：

1. prime cofactor `q` 对应的 semiprime states `p q`；
2. 满足 `p^2<2k` 的 lower least-factor shells；
3. 精确有限量
   \[
   \sum_r c_r(k)
   \]
   的统一解析上包络。

下一步应直接攻击这三部分之一或建立它们之间的联系，不应再为同一组二值 hits 引入另一套等价编码。
