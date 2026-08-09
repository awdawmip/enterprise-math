# P019 补充 19 —— Weighted Relation 的矩阵压缩律与 Refinement Forest

状态：`RESEARCH WIP / EXACT INTEGER RECONSTRUCTION PROVED`

## 1. 目标

Supplement 15–18 已经得到：

- weighted relation field 是 tree-independent current relation object；
- partition coarsening 可严格复合；
- 每次 binary merge 删除一个 internal relation；
- coarsening-only quotient 可永久删除这些 relations；
- 一旦允许 exact refinement，就需要重新提供足够的 relation memory。

本补充解决两个结构问题：

1. arbitrary partition quotient 是否有一个更紧的统一矩阵式？
2. exact refinement 到底需要保存多少条 internal relations？

## 2. P019-X61 —— weighted relation matrix 是一个整数 wedge form

把 current block totals / capacities 写成列向量：

\[
c=(c_1,\ldots,c_k)^T,
\qquad
m=(m_1,\ldots,m_k)^T.
\]

weighted relation matrix：

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

整体可写成：

\[
\boxed{
Z=cm^T-mc^T.
}
\]

所以 `Z` 自动 skew-symmetric。

一般 exterior/wedge algebra 属于成熟线性代数工具；P019 只使用这个整数表示，不作原创声明。

注意：ordinary matrix rank 与 P019 relation dimension 不是同一个概念。`Z` 作为 decomposable skew matrix 的线性代数 rank 很低，但生成它的 fixed-total integer state 仍有 `k-1` 个独立自由度。

## 3. P019-X62 —— arbitrary partition quotient 是 `AZA^T`

设当前有 `k` 个 blocks，coarse partition 有 `ell` 个 blocks。

定义 partition incidence matrix：

\[
A\in\{0,1\}^{\ell\times k},
\]

其中每个 fine block column 恰在所属 coarse block row 上取 1。

则 coarse totals/capacities：

\[
\boxed{c'=Ac,}
\qquad
\boxed{m'=Am.}
\]

于是：

\[
Z'
=c'{m'}^T-m'{c'}^T.
\]

代入：

\[
\boxed{
Z'=A Z A^T.
}
\]

这是 Supplement 16 双重 cut-sum 公式的矩阵版本。

## 4. partition composition 一行得到

若：

\[
A_1:k\to\ell,
\qquad
A_2:\ell\to r,
\]

则总 coarsening matrix：

\[
A=A_2A_1.
\]

所以：

\[
A_2(A_1ZA_1^T)A_2^T
=(A_2A_1)Z(A_2A_1)^T.
\]

即：

\[
\boxed{
Q_{A_2}\circ Q_{A_1}=Q_{A_2A_1}.
}
\]

这再次说明 binary tree 不是 current coarse state 的必要本体。

## 5. P019-X63 —— coarsening kernel 的 relation dimension loss 为 `k-ell`

fine totals fixed grand total 后有：

\[
k-1
\]

个自由整数度。

coarse partition 有 `ell` 个 totals，固定相同 grand total 后有：

\[
\ell-1
\]

个自由度。

因此 quotient fiber 的 rank：

\[
\boxed{
(k-1)-(\ell-1)=k-\ell.
}
\]

等价地，每个 coarse block `A_alpha` 内含 `r_alpha` 个 fine blocks，内部可重新分配的 rank 为：

\[
r_\alpha-1.
\]

求和：

\[
\sum_\alpha(r_\alpha-1)
=k-\ell.
\]

## 6. P019-X64 —— 一个 coarse block 内的 spanning-tree relations 足以 exact refinement

考虑一个 coarse block 内有 `r` 个 fine child blocks：

- capacities `m_i`；
- unknown totals `c_i`；
- 已知 coarse total：
  \[
  C=\sum_i c_i.
  \]

在这 `r` 个 child blocks 上任选一棵 spanning tree。

对每条 tree edge `(i,j)` 保存：

\[
\boxed{Z_{ij}=m_jc_i-m_ic_j.}
\]

共：

\[
\boxed{r-1}
\]

条 relation coordinates。

则 `C + capacities + tree-edge relations` 唯一恢复所有 `c_i`。

### 唯一性证明

假设 `c_i` 与 `c_i'` 有相同 tree-edge relations 与相同 total。

令：

\[
\delta_i=c_i-c_i'.
\]

每条 tree edge `(i,j)` 给：

\[
m_j\delta_i-m_i\delta_j=0.
\]

由于 tree 连通，沿路径得到所有：

\[
\frac{\delta_i}{m_i}
\]

相同（这里仅作为等比例陈述，可全程用交叉乘法表达）。

所以存在公共比例 `lambda` 使：

\[
\delta_i=\lambda m_i.
\]

而：

\[
\sum_i\delta_i=0
\]

以及所有 `m_i>0`，迫使：

\[
\lambda=0.
\]

所以所有 `delta_i=0`。唯一。∎

存在性/整数合法性由实际 fine state 产生的 edge relations 保证；任意外部给定 tags 仍需通过 exact divisibility checks。

## 7. P019-X65 —— Refinement Forest 的 relation count 精确等于丢失维数

对整个 coarse partition，每个 coarse block `A_alpha` 内各选一棵 spanning tree。

所有这些 trees 构成一个 forest。

需要保存的 internal relations 总数：

\[
\sum_\alpha(|A_\alpha|-1).
\]

由于：

\[
\sum_\alpha|A_\alpha|=k,
\]

且 coarse block 数为 `ell`：

\[
\boxed{
|E_{forest}|=k-\ell.
}
\]

而 X63 的 relation rank loss 也是：

\[
\boxed{k-\ell.}
\]

所以 Refinement Forest 在**独立 relation-coordinate 数 / rank**意义下恰好补回所有被降掉的自由度。

这不声称“任意编码理论中绝对最少的整数个数”；一个整数可以人为编码很多数据。这里的 minimality 指自然线性/关系自由度计数。

## 8. binary merge 是最小特例

若一个 coarse block 只合并两个 children：

\[
r=2,
\]

spanning tree 只有一条 edge。

Refinement Forest 只需保存：

\[
\boxed{Z_{12}=z.}
\]

这正好退化到 Supplement 15 X47。

## 9. P019-X66 —— full history 不是 current-state exact refinement 的必要条件

若目标只是：

> 从 current coarse state 恢复某个已知 fine partition 的 current totals，

那么：

\[
\boxed{
\text{coarse weighted quotient}
+
\text{Refinement Forest}
}
\]

已经足够。

不需要知道：

- 哪两个 blocks 最先 merge；
- independent merges 的真实先后顺序；
- binary contraction tree；
- selected boundary witness 的实际 process path。

这些额外信息属于 process provenance，只有 future language 查询它们时才需要保存。

## 10. relation-tree recovery 的整数算法

实现使用一棵 rooted internal relation tree。

已知 edge：

\[
Z_{parent,child}.
\]

先沿 tree 用 weighted three-block closure，把每个 vertex 与 root 的 weighted relation恢复出来。

如果当前已知：

\[
Z_{u,r}
\]

以及 edge：

\[
Z_{u,v},
\]

则由 weighted closure：

\[
\boxed{
m_u Z_{v,r}
=-m_r Z_{u,v}+m_v Z_{u,r}.}
\]

合法 fine state 保证右侧可被 `m_u` 整除。

得到所有 `Z_{v,r}` 后，利用 coarse grand total：

\[
M c_r
=m_r C-\sum_{v\ne r}Z_{v,r}
\]

恢复 root total，再逐个恢复其他 totals。

全部是 exact integer divisions。

## 11. relation memory 的三个层级

### 0. Pure coarsening state

只保留 coarse quotient。

适用于 quotient-closed future language。

### 1. Exact current refinement state

coarse quotient + Refinement Forest。

可恢复指定 fine partition 的 current totals，但不保留实际 merge chronology。

### 2. Process provenance state

再加入真实 historical witness / contraction order / boundary selections。

适用于 history-sensitive future language。

这三个层级不应混同。

## 12. 实现与验证

`src/enterprise_math/weighted_relation_field.py` 新增：

- `tree_internal_relations`；
- `recover_totals_from_relation_tree`。

`tests/test_weighted_relation_field.py` 新增：

- 多种 capacities/totals 下，`k-1` 条 spanning-tree weighted relations + grand total 精确 round-trip；
- 不同 relation-tree 选择恢复相同 present state。

## 13. 前人工作边界

spanning tree bases、incidence matrices、cut/flow coordinates、exterior products 等属于成熟图论/线性代数。

P019 不主张这些一般工具原创。

当前研究贡献候选在于把它们组合到 finite-precision dimension contraction 中，形成：

- weighted relation quotient；
- deleted relation rank；
- exact refinement forest；
- future-safe deletion hierarchy。

## 14. 下一步

1. 对 Refinement Forest 建立 tree-change/local basis transform，类似 Contraction Atlas rotation；
2. 研究哪些 partial refinements 只需 forest 的子集，可做 demand-driven relation memory；
3. 将 `k-ell` relation memory 与 P018 precision refinement cost 连接；
4. 用 P021 witness join 检查：exact current-state forest 是否也足够未来 causal composition，还是需要额外 provenance；
5. 对 weighted relation quotient 研究 Smith normal form / integer lattice invariants，判断合法 relation tags 的最紧标准形。
