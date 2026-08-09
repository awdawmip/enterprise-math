# P019 补充 13 —— Contraction Chart 的合法整数子格与 Index

状态：`RESEARCH WIP / EXACT INTEGER INDEX THEOREM PROVED`

## 1. 问题

Supplement 12 的 local reassociation 公式含有诸如 `//(m+n)` 的精确整数除法。

这必须解释清楚：

- 为什么合法 relation states 一定可整除？
- 不同 tree charts 的 `z` 坐标究竟落在 `Z^(N-1)` 的什么子集？
- tree rotation 为什么可以有非 `±1` 的 ambient rational determinant，却仍是合法整数 state 之间的双射？

本补充把这些问题统一为一个 chart-lattice index 定理。

## 2. 固定 root total 的 chart map

取一棵 rooted ordered binary tree `T`，有 `N` 个 labeled unit leaves。

固定 root total：

\[
\sum_{i=1}^N x_i=c.
\]

所以 fine state lattice 有 `N-1` 个自由整数坐标。

对每个 internal node `v`：

- left child size `m_v`，total `a_v`；
- right child size `n_v`，total `b_v`；
- `|v|=m_v+n_v`。

定义该 node 的 imbalance coordinate：

\[
\boxed{
z_v=n_v a_v-m_v b_v.}
\]

全部 internal nodes 恰有 `N-1` 个，所以得到 chart map：

\[
\Phi_T:\{x\in\mathbb Z^N:\sum x_i=c\}
\to\mathbb Z^{N-1}.
\]

## 3. 单步合法同余条件

在一个 internal node 上，parent total 为

\[
c_v=a_v+b_v.
\]

由

\[
z_v=(m_v+n_v)a_v-m_vc_v
\]

可得

\[
\boxed{
z_v\equiv -m_vc_v\pmod{|v|}.}
\]

反过来，只要该同余成立，就有唯一整数 child totals：

\[
a_v=(m_vc_v+z_v)//|v|,
\qquad
b_v=c_v-a_v.
\]

因此整棵 tree 的合法性是一个递归 triangular congruence system：从 root total 开始，每个 node 检查一次自己的 modulus `|v|`，即可决定 children totals 并继续向下。

## 4. P019-X33 —— 合法 imbalance states 构成 affine sublattice

固定 `T` 与 root total `c`。

所有合法 `z_T=(z_v)` 构成 `Z^(N-1)` 中一个 affine lattice coset，记为

\[
L_T(c).
\]

不同 `c` 可以平移该 coset，但 lattice index 与 `c` 无关。

## 5. P019-X34 —— chart index 等于 internal block-size 乘积

定义

\[
\boxed{
I(T)=
[\mathbb Z^{N-1}:L_T(c)].
}
\]

则

\[
\boxed{
I(T)=
\prod_{v\in\operatorname{Internal}(T)}|v|.
}
\]

### 递归证明

若 `T` 只有一个 leaf，则没有自由坐标，index 为 1。

设 root 左右 subtrees 为 `T_L,T_R`，sizes 为 `m,n`，`N=m+n`。

固定 root total `c` 后，左 subtree total `a` 每改变 1，root imbalance

\[
z=Na-mc
\]

改变恰好 `N`。

所以 root congruence 对 ambient `z` 坐标贡献 index `N`。

在固定 child totals 后，左右内部 chart 分别贡献

\[
I(T_L),\qquad I(T_R).
\]

因此

\[
I(T)=N I(T_L)I(T_R).
\]

归纳即得所有 internal subtree sizes 的乘积。∎

## 6. 低维例子

### 四槽链式 tree

\[
T=(((1,1),1),1).
\]

internal sizes：

\[
2,3,4.
\]

所以

\[
\boxed{I(T)=24.}
\]

### 四槽平衡 tree

\[
T=((1,1),(1,1)).
\]

internal sizes：

\[
2,2,4.
\]

所以

\[
\boxed{I(T)=16.}
\]

直接构造固定 root-total 的 imbalance chart matrix，整数 determinant 绝对值分别正好为 `24,16`。

## 7. P019-X35 —— local rotation determinant 正好匹配 chart-index 比值

Supplement 12 的 rotation：

\[
((A_m,B_n),C_k)
\longleftrightarrow
(A_m,(B_n,C_k))
\]

在两维 local tag plane 上的线性变换为

\[
\begin{pmatrix}u'\\v'\end{pmatrix}
=
\frac1{m+n}
\begin{pmatrix}
-k & n\\
m+n+k & m
\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
\]

其 ambient rational determinant 为

\[
\boxed{
-\frac{n+k}{m+n}.
}
\]

而 rotation 前后只有一个 internal block size 改变：

- old local product 含 `m+n`；
- new local product 含 `n+k`。

因此

\[
\boxed{
|\det R|
=
\frac{I(T')}{I(T)}.
}
\]

所以该变换不是要求整个 ambient `Z^2` 被保持，而是恰好把 index 为 `I(T)` 的合法 lattice 双射到 index 为 `I(T')` 的合法 lattice。

这解释了 X29 中所有“自动整除”。

## 8. 与已知 tree factorial 工具的边界

“rooted tree 上所有 subtree sizes 的乘积”在现有组合数学 / B-series 文献中已有 tree-factorial 类概念。

因此

\[
\prod_v|v|
\]

本身不属于 P019 可声称原创的对象。

P019 当前研究的是它在**固定 root-total imbalance chart 的合法子格 index** 中出现的作用，以及它与 local reassociation denominator / determinant 的匹配。

正式合并前必须把 tree-factorial 前人工作登记到 `sources.json/lineage.json`。

## 9. P019-X36 —— 链式 chart 的 index 为 `N!`

完全 chain/comb tree 的 internal sizes 依次为

\[
2,3,\ldots,N.
\]

所以

\[
\boxed{I(T_{chain})=N!.}
\]

更强地，在所有 `N`-leaf binary trees 中：

\[
\boxed{I(T)\le N!.}
\]

### 证明

归纳。root split 为 `m+n=N`：

\[
I(T)=N I(T_L)I(T_R)
\le N m!n!.
\]

对正整数 `m,n` 且 `m+n=N`：

\[
m!n!\le(N-1)!.
\]

因此

\[
I(T)\le N!.
\]

chain split `1+(N-1)` 逐层达到等号。∎

## 10. 平衡 chart 的 index 可显著更小

当

\[
N=2^h
\]

且 tree 完全平衡时，size `2^j` 的 internal blocks 有 `N/2^j` 个。

所以

\[
I(T_{balanced})
=
\prod_{j=1}^h(2^j)^{N/2^j}.
\]

指数求和为

\[
\sum_{j=1}^h\frac{jN}{2^j}
=2N-h-2.
\]

因此

\[
\boxed{
I(T_{balanced})
=2^{2N-h-2}.
}
\]

例如：

- `N=4`：`16`；
- `N=8`：`2048`；
- `N=16`：`2^26`。

相比 chain 的 `N!`，chart congruence density 可以因 tree choice 相差巨大。

当前不在本文声称完全平衡 tree 对所有 `N` 都是 global minimizer；这是后续独立优化问题。

## 11. 计算含义

如果 tree 只是 current-state representation chart，而非真实 history，则可以选择更适合计算的 chart。

候选目标包括：

- 较小 chart index；
- 较小 imbalance tag range；
- 更局部的 future operations；
- 更容易进行 automorphism quotient。

这意味着 Contraction Atlas 不只是理论等价类，也可能允许**自适应整数坐标选择**。

## 12. 实现与验证

新增：

- `src/enterprise_math/contraction_atlas.py`
  - `tree_leaves`
  - `tree_size`
  - `internal_block_sizes`
  - `chart_index_product`
  - `imbalance_tags`
  - `chart_matrix`
  - `chart_determinant`
  - `chart_index_identity`
- `tests/test_contraction_atlas.py`

对保持 leaf order 的所有 ordered binary tree shapes 枚举到 `N=6`，直接验证：

\[
|\det(\Phi_T)|
=
\prod_{v\in Internal(T)}|v|.
\]

## 13. 下一步

1. 对 chart-index 最小化问题做严格分类，而不是只看 balanced candidate；
2. 研究 chart index 与实际 `z` bit-length / future quotient 复杂度是否相关；
3. 把 local rotation 变成 atlas routing algorithm：自动选择更低成本 chart；
4. 在不保存 historical process 的任务中，检验动态 chart change 是否能显著压缩 trace；
5. 继续完成 tree-factorial / B-series 前人工作映射，明确已有概念与 P019 chart-lattice 应用的边界。
