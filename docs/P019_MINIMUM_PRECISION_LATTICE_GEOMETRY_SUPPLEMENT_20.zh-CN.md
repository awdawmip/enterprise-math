# P019 补充 20 —— Refinement Forest 的合法整数格 Index 与自适应 Tree 选择

状态：`RESEARCH WIP / EXACT INTEGER DETERMINANT THEOREM PROVED`

## 1. 问题

Supplement 19 证明：一个 coarse block 含 `r` 个 fine child blocks 时，保存任意 spanning tree 上的 `r-1` 条 weighted relations，再加 coarse total 与 capacities，就足以精确恢复所有 child totals。

但这些 `r-1` 个 edge relations 并不是 ambient `Z^(r-1)` 中的任意整数 tuple。合法 relation-tree coordinates 仍满足由 capacities 导致的整除约束。

本补充计算其精确 lattice index，并回答：

> 若 spanning tree 只是 current-state refinement chart，怎样选 tree 才使合法 relation coordinates 最稠密？

## 2. augmented relation-tree chart

有 `r` 个 fine blocks：

\[
(m_i,c_i),\qquad i=1,\ldots,r.
\]

选一棵 spanning tree `T`，任意定向其 `r-1` 条 edges。

坐标输出为：

1. grand total
   \[
   C=\sum_i c_i;
   \]
2. 每条 tree edge `u->v` 的 weighted relation
   \[
   Z_{uv}=m_vc_u-m_uc_v.
   \]

这给一个 `r x r` 整数线性 map：

\[
\mathcal A_T:\mathbb Z^r\to\mathbb Z^r.
\]

第一行全为 1；edge `u->v` 对应一行只在 columns `u,v` 有非零系数 `m_v,-m_u`。

## 3. P019-X67 —— relation-tree chart determinant

记：

\[
M=\sum_i m_i,
\]

以及 tree 中 vertex `i` 的 undirected degree 为 `deg_T(i)`。

当 `r>=2`：

\[
\boxed{
|\det\mathcal A_T|
=
M\prod_{i=1}^r m_i^{\deg_T(i)-1}.
}
\]

`r=1` 时 determinant/index 定义为 1。

### 证明

令 `B_T` 是任意 orientation 的 tree incidence matrix，每个 edge row 为 `e_u-e_v`。

把 `A_T` 的每个 column `i` 乘以 `m_i`。第一行变成：

\[
(m_1,\ldots,m_r).
\]

edge `u->v` 行变成：

\[
m_um_v(e_u-e_v).
\]

因此：

\[
\det(\mathcal A_T)\prod_i m_i
=
\left(\prod_{uv\in E(T)}m_um_v\right)
\det\begin{pmatrix}m^T\\B_T\end{pmatrix}.
\]

对 tree incidence matrix，删去任意一列得到 determinant `±1` 的 reduced incidence matrix。沿第一行展开可得：

\[
\left|\det\begin{pmatrix}m^T\\B_T\end{pmatrix}\right|
=\sum_i m_i=M.
\]

另一方面：

\[
\prod_{uv\in E(T)}m_um_v
=
\prod_i m_i^{\deg_T(i)}.
\]

除以 `prod_i m_i`，即得：

\[
|\det\mathcal A_T|
=M\prod_i m_i^{\deg_T(i)-1}.
\]

全程只使用有限整数 determinant。∎

## 4. P019-X68 —— fixed-total edge-relation chart 有相同 index

由于 grand-total map

\[
(c_i)\mapsto C=\sum_i c_i
\]

对 `Z` 是满射，固定任意 `C` 后，tree-edge relation coordinates 的合法 affine lattice 在 ambient `Z^(r-1)` 中具有相同 index：

\[
\boxed{
I_{rel}(T)
=M\prod_i m_i^{\deg_T(i)-1}.
}
\]

所以 Supplement 19 的 Refinement Forest 不仅在 rank 上恰好使用 `r-1` 个 relation coordinates；X68 还精确刻画了它们的整除密度。

## 5. unit capacities 的特殊简化

若所有 fine children 都是 unit blocks：

\[
m_i=1,
\]

则无论 tree shape：

\[
\boxed{I_{rel}(T)=r.}
\]

因此在最原始 unit refinement 层：

> 任选哪一棵 spanning tree 都不会改变 relation-coordinate lattice density。

这与 binary Contraction Atlas 的 imbalance-chart index

\[
\prod_v|v|
\]

明显不同。后者强烈依赖 hierarchical tree shape。

两者不是同一个 chart optimization problem。

## 6. P019-X69 —— 最小 index tree 是最小-capacity star

对 `r>=2`，tree degrees 满足：

\[
\deg_i\ge1,
\qquad
\sum_i(\deg_i-1)=r-2.
\]

所以：

\[
I_{rel}(T)
=M\prod_i m_i^{\deg_i-1}.
\]

要最小化 product，只需把全部 `r-2` 个 excess degree 放到最小 capacity 的 vertex。

存在对应 tree：以该 vertex 为 center 的 star。

因此：

\[
\boxed{
I_{rel}^{min}
=M\,m_{min}^{\,r-2}.
}
\]

若最小 capacity 有多个，可选任一最小 vertex 为 star center。

同理：

\[
\boxed{
I_{rel}^{max}
=M\,m_{max}^{\,r-2},
}
\]

由最大-capacity star 达到。

这里使用的事实“正整数 degree sequence 满足 tree degree sum 时可由某棵 labeled tree 实现”可通过 Prüfer sequence 直接构造，属于成熟 tree combinatorics。

## 7. 为什么 star 最优并不意味着所有 chart 都应选 star

`I_rel` 只衡量：

> fixed-total edge-relation coordinates 在 ambient integer lattice 中的合法密度。

它不直接衡量：

- future operation locality；
- tag bit length；
- direction-orbit locality；
- partial refinement cost；
- historical interpretability。

所以 star 是 **index objective** 的最优 tree，不是所有 future languages 下的 universal chart。

这与 Supplement 18 的 operation-dependent quotient 原则一致。

## 8. 与 Contraction Atlas tree-index 的对照

### Contraction imbalance chart

index：

\[
I_{contraction}(T)=\prod_{v\in Internal(T)}|v|.
\]

其外部 tree-shape statistic 与已有 tree-factorial / Q-shape 研究相邻；complete/greedy-from-bottom 树倾向最小化，chain/caterpillar 最大化。

### Refinement relation-tree chart

index：

\[
I_{rel}(T)=M\prod_i m_i^{\deg_i-1}.
\]

unit capacities 时 shape-independent；unequal capacities 时按 vertex capacities 分配 degree，最小-capacity star 最小化。

因此两个 atlas 分别优化：

- hierarchical proportional-deviation coordinates；
- present-state weighted edge-relation coordinates。

不能机械共用“balanced tree 最优”结论。

## 9. P019-X70 —— relation-tree index 只依赖 degree sequence

X68 中 tree shape 只通过：

\[
(\deg_1,\ldots,\deg_r)
\]

进入。

所以两棵 labeled spanning trees 若具有相同 vertex degree sequence，则：

\[
\boxed{I_{rel}(T_1)=I_{rel}(T_2).}
\]

这比 Contraction Atlas 的 subtree-size product 更粗：Refinement Forest 的 lattice density 不读取完整 tree topology。

## 10. 实现与验证

新增：

- `src/enterprise_math/refinement_forest.py`
  - `relation_tree_degrees`
  - `refinement_tree_index_formula`
  - `augmented_relation_tree_matrix`
  - exact Bareiss determinant
  - `refinement_tree_chart_determinant`
  - `star_parents`
  - min/max index helpers
  - Prüfer degree enumeration helpers
- `tests/test_refinement_forest.py`

回归包括：

- 多组 unequal capacities 下 direct determinant = X67 formula；
- unit capacities 下 path/star 均为 index `r`；
- star closed form；
- 小规模全部 Prüfer degree sequences 上 min/max 等于最小/最大-capacity star；
- capacities `1..3` 的 5-block 组合上直接验证 extrema。

## 11. 前人工作边界

本补充使用的：

- tree incidence matrix；
- matrix-tree / reduced-incidence unimodularity；
- Prüfer sequence 与 tree degree sequences；

均属于成熟组合图论。

P019 当前新增候选接口是它们与 capacity-weighted relation refinement chart 的组合及 index 解释，不作一般图论原创声明。

## 12. 下一步

1. 研究 `I_rel` 与实际 relation-tag bit length 的关系；
2. 给 partial refinement operation family 优化 tree，而不是只优化 global index；
3. 研究 relation-tree basis change 的 determinant/index ratio与 local tree exchange；
4. 对 coarse block 内 capacities 动态变化时设计 adaptive forest rerouting；
5. 将 `k-ell` rank cost + `I_rel` lattice density 同时纳入 P018 precision-selection cost。
