# Causal Block Precision Bridge —— P018 固定尺度作为完整 LEGO Block 的派生特例

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT INTEGER SPECIALIZATION`

归属：P018 bridge。本文不取代 P018 declared resolution calculus，而说明其何时可由实际 causal block construction 生成。

## 1. 完整块生成固定尺度

假设系统中真实存在 capacity 为 `d` 的完整 LEGO block。完整 levels：

\[
\boxed{V_d(k)=kd.}
\]

P008 自动给：

\[
R_d(n)=\left\lfloor\frac nd\right\rfloor,
\]

\[
C_d(n)=d\left\lfloor\frac nd\right\rfloor,
\]

以及 exact basin detail：

\[
\boxed{\delta_d(n)=n\bmod d.}
\]

所以 P018 的：

\[
n=dq+r
\]

在这个 regime 中可重写为：

\[
\boxed{
\text{实际 }d\text{-unit complete block}
\to
\text{P008 root/collapse}
\to
(q,r).
}
\]

Euclidean division 是结果，不是 ontology。

## 2. 嵌套 block 生成 divisibility scale chain

若：

\[
e=md
\]

并且 `e`-block 的物理/因果语义确实是 `m` 个 `d`-blocks 组成一个 superblock，则：

\[
\boxed{C_e(C_d(n))=C_e(n).}
\]

因此：

\[
d\mid e
\]

不只是抽象 scale order，而是可解释成真实 nested assembly。

这给 P018 scale chain 一个充分的 causal derivation regime。

## 3. carry 由 detail basin 合并产生

两个同尺度 states：

\[
x=dq_x+r_x,
\qquad
y=dq_y+r_y.
\]

相加时：

\[
r_x+r_y=dc+r,
\qquad0\le r<d.
\]

于是：

\[
\boxed{
c=\left\lfloor\frac{r_x+r_y}{d}\right\rfloor}
\]

正是 detail reservoirs 新完成了多少个 `d`-blocks。

这与 `causal_grade_coherence.py` 中 base-`d` coherent carry 是同一个整数机制。

## 4. quotient-only state 什么时候真的足够？

只保留：

\[
q_d(n)=\left\lfloor\frac nd\right\rfloor.
\]

允许 additive future：

\[
n\mapsto n+u.
\]

则 quotient-only state 对所有 basin members future-safe，当且仅当：

\[
\boxed{d\mid u.}
\]

### 必要性

若：

\[
u=md+r,\qquad0<r<d,
\]

取：

\[
n=0,\qquad n'=d-r.
\]

二者当前 quotient 都是 `0`，但：

\[
q_d(n+u)=m,
\qquad
q_d(n'+u)=m+1.
\]

所以任何 sub-block additive action 都会重新读取 remainder。

### 充分性

若：

\[
u=md,
\]

则：

\[
q_d(n+u)=q_d(n)+m
\]

与 detail 无关。

因此：

\[
\boxed{
\text{detail 是否必要}
=
\text{未来语言是否包含 sub-block 操作}.
}
\]

## 5. 这与“precision 声明”不同

如果当前层所有未来操作都严格以完整 `d`-blocks 发生，那么 remainder 对任何未来都不可见，应当真实坍缩。

如果未来允许 finer units，则 remainder 是 continuation state 的必要部分。

所以：

\[
\boxed{
\text{scale }d
\text{ 不是因为被声明为 precision 就自然成立；}
\text{它必须与实际 complete blocks 和 future operation language 对齐。}
}

## 6. 与 variable basin 的关系

固定 `d` 只是：

\[
V(k)=dk
\]

的 constant-width special case。

一般 causally generated complete growth：

\[
V(k)
\]

产生 state-dependent basin capacity：

\[
\Delta V(k).
\]

若 growth degree ≥2，basin widths 通常无界，此时任何固定正 additive increment 都无法在 level-only quotient 上全局 future-safe；detail/continuation state 变成内生必要结构。

## 7. 可执行资产

- `causal_block_precision.py`
- `causal_basin_state.py`
- `causal_basin_translation.py`
- tests
