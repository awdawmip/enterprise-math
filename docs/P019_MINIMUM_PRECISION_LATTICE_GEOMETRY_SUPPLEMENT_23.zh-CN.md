# P019 补充 23 —— 高阶 Collision Power 的共同 Minimum Relation Geometry

状态：`RESEARCH WIP / EXACT INTEGER MINIMIZER THEOREM PROVED`

## 1. 问题

Supplement 10 证明：当 `s>2` 时，单个 block 的 scaled power defect 一般随 bulk quotient 增长，不能像平方层 `s=2` 那样完全压成 bounded residue correction。

这容易让人误以为：高阶 power 的最优 relation coordinates 也必然随大数增长。

本补充证明相反结论：

> **对所有 `s>=2`，global fiber minimum 选择的 relation geometry 完全相同，并且只依赖 total residue allocation，不依赖 bulk quotient。**

## 2. 全部 unit slots 的平衡定理

总 capacity：

\[
M=\sum_i m_i.
\]

固定 grand total：

\[
C\in\mathbb Z.
\]

作 Euclidean division：

\[
\boxed{
C=Mq+r,
\qquad
0\le r<M.
}
\]

对：

\[
\sum_{u=1}^M|x_u|^s,
\qquad
\sum_u x_u=C,
\]

当 `s>=2` 时，任意 global minimizer 的 unit values 都只能取：

\[
\boxed{q\text{ 或 }q+1.}
\]

并且恰有 `r` 个 slots 取 `q+1`。

### 纯整数交换证明

若存在两个 slots：

\[
x_a\ge x_b+2,
\]

则做：

\[
(x_a,x_b)\to(x_a-1,x_b+1)
\]

保持总和不变。

由于整数函数 `|t|^s` 的 forward difference

\[
|t+1|^s-|t|^s
\]

随 `t` 单调严格增加（`s>=2`），上述交换严格降低总 cost。

所以 minimum 时任意两个 slots 相差至多 1。给定总和 `Mq+r`，只能是 `q/q+1` 分布。∎

这不使用实数导数。

## 3. coarse blocks 的 residue allocation

把 `M` 个 unit slots 按 capacities `m_i` 分成 coarse blocks。

定义：

\[
h_i
=
\text{block }i\text{ 中取 }q+1\text{ 的 unit 数}.
\]

则：

\[
\boxed{
0\le h_i\le m_i,
}
\]

\[
\boxed{
\sum_i h_i=r.
}
\]

coarse block total：

\[
\boxed{
c_i=m_iq+h_i.}
\]

反过来，任何满足上述 bounds/sum 的 `h_i` 都可以通过选择 block 内 `h_i` 个 slots 取 `q+1` 构造一个 global minimizer。

因此 global coarse minimizer set 与 `s` 无关，只由：

\[
(m_i),\quad C\bmod M
\]

决定。

## 4. P019-X81 —— minimum weighted relation field 中 bulk quotient 完全消去

对任意两个 coarse blocks：

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

代入：

\[
c_i=m_iq+h_i,
\qquad
c_j=m_jq+h_j.
\]

得到：

\[
Z_{ij}
=m_j(m_iq+h_i)-m_i(m_jq+h_j).
\]

`q` 项严格相消：

\[
\boxed{
Z_{ij}=m_jh_i-m_ih_j.
}
\]

所以 minimum relation geometry 与 bulk quotient `q` 无关。

## 5. P019-X82 —— minimum relation field 有 capacity-only bound

因为：

\[
0\le h_i\le m_i,
\qquad
0\le h_j\le m_j,
\]

所以：

\[
-m_im_j
\le
m_jh_i-m_ih_j
\le
m_im_j.
\]

因此：

\[
\boxed{
|Z_{ij}|\le m_im_j.
}
\]

该 bound 不依赖：

- grand-total bulk `|q|`；
- power `s>=2`；
- absolute scale of current state。

所以高阶 value defect 可以增长，而 minimum relation field 仍然处在一个 capacity-bounded integer box 内。

## 6. P019-X83 —— 所有 `s>=2` 共享同一个 argmin relation set

定义：

\[
\mathcal M_s(C,\mathbf m)
=
\arg\min_{\sum c_i=C}
\sum_i\Psi_{m_i,s}(c_i).
\]

由 unit balancing / min-plus associativity：

\[
\boxed{
\mathcal M_s(C,\mathbf m)
=
\left\{
(m_iq+h_i)_i:
0\le h_i\le m_i,\ \sum h_i=r
\right\}
}
\]

对所有：

\[
\boxed{s>=2}
\]

相同。

所以：

\[
\boxed{
\text{power order changes minimum value,
not minimum relation geometry.}
}
\]

## 7. `s=1` 为什么不同

当：

\[
s=1,
\]

cost 为：

\[
\sum|x_u|.
\]

只要所有非零 unit values 与 grand total 同号，很多不平衡分配也能达到相同 minimum `|C|`。

所以 `s=1` 的 argmin set 更大，不再强制 `q/q+1` balancing。

这解释一个重要结构差别：

- `s=1` graph layer 对 capacity/内部拥挤不敏感；
- `s>=2` collision-sensitive layers 共享严格的 balanced relation geometry。

## 8. 与 Supplement 10 的负结论不冲突

Supplement 10 研究的是：

\[
D_{m,s}(c)
=m^{s-1}\Psi_{m,s}(c)-|c|^s.
\]

固定一个 block 的 `(m,c)`，当 `s>2` 时其 defect 一般随 `q` 增长。

本补充研究的是：

> 给定总 capacity / total，允许 block totals 在 fiber 内重新分配时，global minimum 的 relation field。

两个问题不同。

所以：

\[
\boxed{
\text{value defect bulk-sensitive}
}
\]

可以同时与：

\[
\boxed{
\text{argmin relation geometry bulk-invariant}
}
\]

成立。

## 9. 与有限精度的意义

这给一个可能非常有用的层次：

### relation minimum state

只需：

- capacities；
- total residue `r=C mod M`；
- residue allocation `h_i`。

weighted relations 自动 bounded。

### value channel

不同 `s` 再对同一 balanced arrangement 赋予不同 collision penalty。

所以 high-order observation 可能不需要重新求几何 minimizer，只需要重新计算 value。

## 10. 与 P011 collision spectrum

`Psi_(m,s)` 本身是 occupancy multiplicity 的 power sum，而 power sum 可由完整 `J_k` collision spectrum 线性组合。

X83 表明：当优化目标是任意 `s>=2` 单一 power sum 时，最优 occupancy geometry一致。

下一步值得研究：

> 对任意非负 superadditive / convex collision-spectrum 组合，是否仍由同一个 balanced relation geometry 最小化？

若成立，minimum relation geometry 将不依赖具体 irreversibility observable，而只依赖“碰撞惩罚严格凸”这一结构。

## 11. 实现接口

`src/enterprise_math/discrete_fiber_convexity.py` 已实现：

- exact forward slope：
  \[
  \Psi(c+1)-\Psi(c)=|q+1|^s-|q|^s;
  \]
- transfer cost change；
- pure integer exchange descent；
- no-decreasing-exchange minimum check。

`tests/test_discrete_fiber_convexity.py` 验证 powers `1..5`、signed totals 与多个 capacities 下：

- slope 公式；
- slope monotonicity；
- exchange increment exactness；
- exchange descent 到达 closed global min-plus minimum。

## 12. 下一步

1. 把 X83 推广到一般 discrete-convex collision penalty，而不仅是 powers；
2. 对 residue allocation polytope/finite lattice 研究 relation-field orbit structure；
3. 用 bounded `Z` minimum field 设计比 full fine state 更紧的 minimizer witness；
4. 判断 black-hole/focusing 等 dynamics 中 observable order 变化是否只改变 value 而不改变 preferred relation geometry；
5. 与成熟 discrete-convex/M-convex resource-allocation 理论做正式 prior-art 映射，避免重复证明已有一般结果。
