# P023 —— Borrow 复合补充 05

状态：`ACTIVE RESEARCH NOTE`  
范围：reductive 轨迹上粗精度 borrow 的精确可加性与望远镜性质

## 1. 定义

对满足 `T(n)<=n` 的 reductive 运算和正精度比 `r`，定义

\[
\boxed{
B_r^T(n)=Q_r(n)-Q_r(T(n)).
}
\]

由 P023-T17，它也可以完全由 reductive gap 与当前 fiber 内 detail 算出。

## 2. P023-T19 —— 两步 borrow 复合

设 `T`、`S` 在实际访问状态上均 reductive：

\[
T(n)\le n,
\qquad
S(T(n))\le T(n).
\]

则

\[
\boxed{
B_r^{S\circ T}(n)
=
B_r^T(n)+B_r^S(T(n)).
}
\]

### 证明

直接使用精确望远镜恒等式：

\[
Q_r(n)-Q_r(S(T(n)))
=
\bigl(Q_r(n)-Q_r(T(n))\bigr)
+
\bigl(Q_r(T(n))-Q_r(S(T(n)))\bigr).
\]

没有近似，也没有渐近过程。

## 3. P023-T20 —— 有限轨迹望远镜

对有限 reductive 轨迹

\[
n_0\ge n_1\ge\cdots\ge n_m,
\]

定义局部 borrow

\[
b_i=Q_r(n_{i-1})-Q_r(n_i).
\]

则

\[
\boxed{
\sum_{i=1}^{m} b_i
=
Q_r(n_0)-Q_r(n_m).
}
\]

因此总 coarse precision loss 只取决于首尾，而局部 borrow profile 记录这份损失沿路线如何分布。

## 4. 与 P019 collapse-word 稳定化的关系

P019 已证明，固定完全幂 collapse 词会稳定到最大不动点；若指数 lcm 为 `L`，最终状态为 `C_L(n0)`。

因此，从 `n0` 到同一稳定终点的任意 reductive 瞬态路线，都有相同的总 `r`-borrow：

\[
\boxed{
B_{\mathrm{total}}
=
Q_r(n_0)-Q_r(C_L(n_0)).
}
\]

但局部 borrow 分布可以随词序和瞬态状态而改变。

### 最小例子

取 `n0=8`、`r=2`。

一种 collapse-word 路线是

\[
8\xrightarrow{C_2}4\xrightarrow{C_3}1,
\]

若把 `C_3 C_2` 当成一次词映射，则是

\[
8\to1
\]

其 borrow profile 为

\[
(4).
\]

相反词序作为固定词重复时给出

\[
8\to4\to1
\]

其 borrow profile 为

\[
(2,2).
\]

两条路线总 borrow 都是 `4`，因为首尾粗状态均从 `Q_2(8)=4` 降到 `Q_2(1)=0`。

所以需要区分：

- **total borrow** —— 首尾不变量；
- **borrow profile** —— 瞬态 / 路径信息。

## 5. 与 P010/P011 的联系

P010/P011 强调：同一个最终状态并不保留中间历史。P023-T20 给出一个精度版本：

\[
\text{同终点}
\Longrightarrow
\text{同总 coarse borrow},
\]

但不保证局部 borrow 序列相同。

因此 total borrow 是粗粒度可加不变量，而 borrow profile 是更细的历史 witness；后者可能在 stable-equivalence quotient 中丢失。

这正是 P023 要控制的区别：一个商可以完整保留目标不变量，同时破坏路径级可恢复信息。

## 6. 可执行审计

- `src/enterprise_math/p023_borrow_cocycle.py`
- `tests/test_p023_borrow_cocycle.py`

参考测试穷举 `n>=mid>=end` 且 `n<80` 的两步有限链、正精度比小于 10 的组合，并检查一般有限轨迹望远镜，以及显式保留 `8->1` 与 `8->4->1` 的 collapse-word witness。
