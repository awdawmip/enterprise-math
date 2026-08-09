# 勒让德压力测试 — 补充 13

状态：`ACTIVE RESEARCH NOTE`  
范围：通过精确大模数命中状态并集，对高带 three-prime 资源做盆地级汇总  
依赖：P017 L035、L039–L048  
纪律：**本文不证明勒让德猜想。** 本文不引入新的筛法形式。L041 处理 support closure，L042–L045 处理 centered mirror separation，L046–L048 处理有界 CRT sign-pattern capacity；这里的 L049 则把规范的大模数命中跨 least-factor shells 汇总。

## 1. 为什么仍需要另一条跨状态不等式

L042–L045 关联同一个 centered mirror pair 的两侧状态；L046–L048 编码 mirror-side sign pattern 并控制其有限 lift；L036 与 L040 则在单个 least-factor shell 内控制 three-prime states。它们都没有阻止同一个 cofactor resource prime 在另一个 least-factor shell 中再次被计数。

L039 给出了缺失的精确对象：每个模数 `d>=2k` 在开平方盆地中至多命中一次，而且命中状态由共同中心显式确定。因此跨 shell 汇总应当对**已经实现的 hit states**去重，而不只是数合格模数。

---

## 2. 可产生 triple 的高带最小素因子

令

\[
U=(k+1)^2-1.
\]

一个高带 three-prime state 写成

\[
n=p\ell s,\qquad p\le\ell\le s,\qquad p^2\ge2k.
\]

必有 `p^3<=n<=U`。定义

\[
\mathcal P_H(k)
=
\{p\le k:p\text{ 为素数},\ p^2\ge2k,\ p^3\le U\}.
\]

只有这个有限集合中的素数可能成为高带 three-prime state 的最小素因子。

---

## 3. 一个 cofactor resource 的精确状态容量

固定一个作为高带 triple state 两个 cofactor primes 之一的素数 `r`。若 `n=p\ell s` 使用 `r`，则 `p<=r`；另一个 cofactor prime 至少为 `p`，所以

\[
n\ge p^2r.
\]

定义

\[
\mathcal E_r(k)
=
\{p\in\mathcal P_H(k):p\le r,\ p^2r\le U\}.
\]

对其中每个 `p`，

\[
pr\ge p^2\ge2k.
\]

因此 L039 保证模数 `pr` 在盆地中至多命中一个状态。若命中存在，记唯一状态为 `x_{p,r}(k)`。

定义已经实现的 hit-state union

\[
X_r(k)
=
\{x_{p,r}(k):p\in\mathcal E_r(k),\ H_{pr}(k)=1\}
\]

以及精确容量

\[
c_r(k)=|X_r(k)|.
\]

不同模数若产生相同状态，只计一次。自动有

\[
c_r(k)\le\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\qquad\text{和}\qquad
c_r(k)\le H_r(k),
\]

因为并集中的每个状态本身都被 `r` 整除。

---

## 4. 精确平方 cofactor 修正

令 `E_H(k)` 为高带 three-prime states 中 cofactor 为素数平方 `r^2` 的状态数。

对一个 least prime `p`，高带 cofactor window 的长度至多为 `p`，因此跨度至多为 `p-1`；而根至少为 `p` 的两个不同平方之间距离更大。所以窗口中至多存在一个素数平方。

若素数 `r>=p` 满足

\[
r^2\in W_p(k),
\]

则 `r^2` 自动是 `p`-rough，所以 `p r^2` 确实是 least-factor-`p` shell 中的 three-prime state。因此 `E_H(k)` 恰好等于满足下列条件的有限 `(p,r)` 对数量：

\[
p\in\mathcal P_H(k),\qquad r\text{ 为素数},\qquad p\le r,\qquad r^2\in W_p(k).
\]

---

## 5. L049 — 全局命中并集资源上界

状态：`PROVED`。

令 `T_H(k)` 为所有 least-factor shells 中高带 three-prime states 的总数。则

\[
\boxed{2T_H(k)-E_H(k)\le\sum_r c_r(k).}
\]

因此

\[
\boxed{
T_H(k)
\le
\left\lfloor\frac{E_H(k)+\sum_r c_r(k)}{2}\right\rfloor.
}
\]

资源素数只有有限多个：在 least-factor-`p` triple 中，

\[
r\le\left\lfloor\frac{U}{p^2}\right\rfloor.
\]

### 证明

对每个高带 triple state `n=p\ell s`，令

\[
S(n)=\{\ell,s\}
\]

为其 cofactor-prime resource 集。非平方 cofactor 贡献两个资源，平方 cofactor 贡献一个资源。因此

\[
\sum_n|S(n)|=2T_H(k)-E_H(k).
\]

固定资源素数 `r`，令 `u_r(k)` 计数 cofactor support 中包含 `r` 的实际高带 triple states。任取其中一个状态。其 least prime `p` 属于 `P_H(k)`。由于另一个 cofactor prime 至少为 `p`，

\[
p\le r,\qquad p^2r\le n\le U,
\]

故 `p` 属于 `E_r(k)`。该状态被 `pr` 整除，而 `pr>=2k`；根据 L039，该模数在盆地中至多有一个 hit。因此实际状态必然恰好是 `x_{p,r}(k)`，从而属于 `X_r(k)`。

所以

\[
u_r(k)\le c_r(k).
\]

对所有资源素数求和得到

\[
2T_H(k)-E_H(k)=\sum_r u_r(k)\le\sum_r c_r(k),
\]

L049 得证。∎

---

## 6. 精确跨 shell 碰撞 witness

在

\[
k=110,\qquad r=19
\]

时，两个合格模数

\[
17\cdot19\qquad\text{和}\qquad19^2
\]

都命中了同一个盆地状态

\[
12274.
\]

因此

\[
X_{19}(110)=\{12274\},\qquad c_{19}(110)=1.
\]

两个二值 modulus hits 实际只占一个 resource-19 state slot。L049 **不**宣称 hit bits 在统计上普遍稀疏，只利用它们实现状态之间的精确碰撞。

---

## 7. 回归 checkpoint

可执行测试会在有限 `k` 范围内，把 L049 与真实 high-band triple states 直接对照。

在 `k=110` 时，

\[
\sum_r c_r(110)=7,\qquad E_H(110)=1,
\]

所以

\[
T_H(110)\le4.
\]

已经组合的逐 shell L036/L040 上界之和为 `5`，因此 L049 在这个 checkpoint 上严格更强。

在 `k=500` 时，

\[
\sum_r c_r(500)=33,\qquad E_H(500)=1,
\]

故

\[
T_H(500)\le17.
\]

这些数值只是实现回归，不是渐近结论。

---

## 8. 与 L041–L048 的关系及下一目标

当前几条跨状态工具各有明确职责：

- L041：large transverse-support hit 后，判断 anchor-surviving exact-support closure；
- L042–L045：关联 centered mirror 两侧状态，并得到 mirror-incidence 必要条件；
- L046–L048：CRT/idempotent sign-pattern 编码与 bounded lift capacity；
- L049：用精确大模数 hit-state union，跨 least-factor shells 汇总高带 cofactor-resource 占用。

目前未解部分清楚分为：

1. prime cofactor `q` 对应的 semiprime states `p q`；
2. 满足 `p^2<2k` 的 lower least-factor shells；
3. 精确有限量
   \[
   \sum_r c_r(k)
   \]
   的有用统一解析上包络。

下一步应直接攻击这些部分之一，或把 L049 与 mirror-incidence 约束真正连接起来；不应再为同一组二值 hits 引入另一套等价编码。
