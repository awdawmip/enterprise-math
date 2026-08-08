# P023 —— Reductive Borrow 补充 04

状态：`ACTIVE RESEARCH NOTE`  
范围：任意 reductive 整数运算的通用粗精度 borrow 公式

## 1. 设置

令

\[
T:\mathbb N\to\mathbb N
\]

满足

\[
T(n)\le n.
\]

固定正精度比 `r`，写成

\[
n=qr+t,
\qquad
q=Q_r(n),
\qquad
0\le t<r.
\]

定义 reductive gap

\[
\boxed{
G_T(n)=n-T(n).
}
\]

下面恒等式不要求 `T` 单调、幂等或具有特殊算术形式；仅 reductive 即可。

## 2. P023-T17 —— 通用 reductive precision-borrow 恒等式

定义

\[
\boxed{
B_{T,r}(n)
=
\left(G_T(n)-t+r-1\right)//r.
}
\]

则

\[
\boxed{
Q_r(T(n))=Q_r(n)-B_{T,r}(n).
}
\]

等价地，

\[
\boxed{
B_{T,r}(n)=Q_r(n)-Q_r(T(n)).
}
\]

因此 `B_(T,r)` 精确等于 reductive 运算跨过的粗 `r`-fiber 数量。

### 证明

由于

\[
T(n)=n-G_T(n)=qr+t-G_T(n),
\]

所以

\[
Q_r(T(n))
=
q+\left(t-G_T(n)\right)//r.
\]

又因 `0<=t<r` 且 `G_T(n)>=0`，

\[
-\left(t-G_T(n)\right)//r
\]

正是 `(G_T(n)-t)/r` 的上取整，而不用真除法可以写成

\[
\left(G_T(n)-t+r-1\right)//r.
\]

故得证。

## 3. P023-T18 —— gap-borrow 状态就是最粗一步修复

对未来粗观测

\[
h(n)=Q_r(T(n)),
\]

定义修复状态

\[
\boxed{
\widetilde q_T(n)=\left(Q_r(n),B_{T,r}(n)\right).
}
\]

因为

\[
h(n)=Q_r(n)-B_{T,r}(n),
\]

反过来又有

\[
B_{T,r}(n)=Q_r(n)-h(n),
\]

所以 `(Q_r,B_(T,r))` 与 `(Q_r,h)` 诱导完全相同的分区。

由 P023-T02，

\[
\boxed{
\widetilde q_T
\text{ 是 }Q_r\text{ 针对 }Q_rT\text{ 的最粗兼容细化。}
}
\]

因此这不是任意类编号，而是一般性的规范 repair coordinate。

## 4. 与 P018 subtraction borrow 的关系

P018-T05 证明了

\[
x-y
\]

的一层 subtraction borrow。

P023-T17 是更一般的结论：任意 reductive transformation 都有精确的**粗 fiber 借位层数**，而且这个层数可以大于 1。

当细粒度减法至多跨过一个当前精度边界时，就退化回 P018 的 `0/1` borrow。

因此 carry/borrow 并不只属于基础 `+/-` 运算，它可以作为描述 reductive 运算如何跨越有限精度 fiber 的一般语言。

## 5. P007 multiple-collapse 特例

若

\[
T=D_d,
\qquad
G_T(n)=n-D_d(n)=n\bmod d,
\]

则

\[
\boxed{
B_{D_d,r}(n)
=
\bigl((n\bmod d)-(n\bmod r)+r-1\bigr)//r.
}
\]

补充 03 已进一步证明：固定一个 `Q_r` fiber 后，这个 borrow count 最多只有两种值，因此最粗修复还能继续压成一个 boundary-crossing bit。

## 6. P002 完全幂 collapse 特例

若

\[
T=C_p,
\]

记 P002 collapse gap 为

\[
G_p(n)=n-C_p(n).
\]

则

\[
\boxed{
B_{p,r}(n)
=
\bigl(G_p(n)-(n\bmod r)+r-1\bigr)//r,
}
\]

并且

\[
\boxed{
Q_r(C_p(n))=Q_r(n)-B_{p,r}(n).
}
\]

所以 P002 basin gap 获得了一个精确的 P023/P018 解释：

> 先扣除当前 precision fiber 内本来就知道的 detail `n mod r`，剩余 gap 精确决定完全幂 collapse 跨过了多少个粗精度 fiber。

这不是替代 P002 gap，而是把 gap 运送到了 precision dynamics 里。

## 7. 为什么重要

此前，“collapse gap 很大”和“发生 precision borrow”看起来像两套不同语言。

T17 表明，对任意 reductive 整数运算，它们由一个统一分解连接：

\[
\boxed{
\text{reductive gap}
=
\text{fiber 内 detail 消耗}
+
\text{跨 coarse fiber 的 borrow 贡献}
}
\]

粗层贡献由 `B_(T,r)` 精确计量。

这让 P023 第一次直接贯通 P002/P007/P018 的现有算术核心，并为后续 collapse/collision 动力学提供可复用接口。

## 8. 可执行审计

- `src/enterprise_math/p023_reductive_borrow.py`
- `tests/test_p023_reductive_borrow.py`

有界参考测试覆盖所有 `0<=T(n)<=n<120`、正精度比小于 15 的组合，并额外检查 P007 multiple-collapse 与完全幂 collapse 实例。
