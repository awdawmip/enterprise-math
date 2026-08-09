# Causal Polynomial Collapse No-Go —— 非线性完整增长不能闭合固定正向 Level-Only 加法

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT THEOREM`

范围：P008 strictly increasing integer-valued polynomial complete-growth law 与 level-only quotient 的 additive future safety。

## 1. 设定

给：

\[
V:\mathbb N_0\to\mathbb N_0
\]

为严格增长、无界的 integer-valued polynomial complete-growth law。

P008 level quotient：

\[
q_V(n)=R_V(n)=\max\{k:V(k)\le n\}.
\]

第 `k` 个 basin width：

\[
\boxed{w_k=V(k+1)-V(k)=\Delta V(k).}
\]

研究固定 additive future：

\[
T_t(n)=n+t,
\qquad t>0.
\]

问题：何时 `T_t` 可以完全通过 `q_V` 下沉，即：

\[
q_V(x)=q_V(y)
\Longrightarrow
q_V(x+t)=q_V(y+t)
\]

对所有 `x,y` 成立？

## 2. NG-01 —— 任意过宽 basin 都破坏 +t future safety

若：

\[
w_k>t,
\]

取 same-level states：

\[
x=V(k),
\qquad
y=V(k+1)-1.
\]

二者当前都在 level `k`。

因为 `t<w_k`：

\[
x+t<V(k+1),
\]

故：

\[
q_V(x+t)=k.
\]

但：

\[
y+t\ge V(k+1),
\]

所以：

\[
q_V(y+t)\ge k+1.
\]

因此：

\[
\boxed{w_k>t\Rightarrow +t\text{ 不能在 level-only quotient 上 exact}.}
\]

## 3. NG-02 —— unbounded basin width 排除所有固定正 translation

若：

\[
\sup_k w_k=\infty,
\]

则对任意固定：

\[
t>0
\]

总能找到 `k` 使 `w_k>t`。

于是：

\[
\boxed{
\mathcal S_V=\{0\}
}
\]

对于 fixed positive additive translations。

这里 `S_V` 是该 collapse level quotient 自己生成的 safe-translation monoid。

## 4. NG-03 —— polynomial classification

若：

\[
\deg V=p.
\]

finite difference：

\[
\Delta V(k)
\]

是 degree：

\[
p-1.
\]

### p >= 2

`Delta V` 是正次数 polynomial。由于 `V` 严格增长且 leading growth 为正，`Delta V(k)` 最终正且无界。

所以：

\[
\boxed{
p\ge2
\Longrightarrow
\mathcal S_V=\{0\}
}

对于 fixed positive additive futures。

### p = 1

写：

\[
V(k)=ak+b,
\qquad a>0.
\]

所有 basin width 恒为：

\[
a.
\]

translation `t` future-safe 当且仅当：

\[
\boxed{a\mid t.}
\]

所以：

\[
\boxed{
\mathcal S_V=a\mathbb N_0.
}
\]

因此在 strictly increasing polynomial complete-growth 类中：

\[
\boxed{
\exists t>0\text{ globally safe}
\iff
\deg V=1.
}
\]

## 5. 对维度路线的直接含义

### free LEGO allocation

\[
H_m(c)=\binom{c+m-1}{m-1}
\]

degree：

\[
m-1.
\]

当：

\[
m\ge3
\]

即 hidden relation rank 至少 2 时，任何固定正 additive amount 都不能只靠 complete configuration level exact 演化。

### A_p graph-ball growth

现有：

\[
V_p(r)=|B_r^{A_p}|
\]

具有 degree `p`。

所以：

\[
\boxed{
p\ge2
\Longrightarrow
\text{radius / complete-ball-level alone cannot support any fixed positive additive count update globally}.}
\]

这不表示几何本身错误；它表示 radius state 不足以作为该 future language 的完整 causal state。

## 6. 为什么 detail 是因果必要而不是“高精度可选项”

在 degree ≥2 growth 中，basin width 随 level 增长。

同一个 complete level 内越来越多 exact amounts 被合并。

普通固定 `+t` 最终一定能读取“当前 amount 究竟位于 basin 的哪里”。

所以 detail：

\[
\delta=n-V(R_V(n))
\]

不是外部 precision annotation，而是保持 additive future exact 所必需的 continuation state。

## 7. 与 periodic basin 的区别

periodic nonconstant basin width 不属于 polynomial degree ≥2 regime。

若 widths 周期化，仍可能产生 natural period capacity `T`，使 `+T` safe。

所以真正的分界不是“nonlinear 看起来复杂”，而是：

\[
\boxed{
\text{collapse boundary pattern 是否允许非零 safe operation monoid}.}
\]

## 8. 与传统数学的关系

“polynomial finite difference 降 degree 一阶”是成熟离散代数事实，不是本项目原创。

项目性的组合是：

\[
\text{causal complete growth}
\to
\text{P008 basins}
\to
\text{future-safe operation monoid}
\to
\text{detail necessity no-go}.
\]

这给“精度是否可删”一个 operation-relative causal theorem，而不是误差估计。
