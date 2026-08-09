# P019 补充 14 —— Tree-Independent Relation Field 与紧整数 Flow Charts

状态：`RESEARCH WIP / EXACT INTEGER IDENTITIES PROVED`

## 1. 问题

Contraction Atlas 已说明不同 binary trees 可以作为同一 current fine state 的不同 `z` 坐标图。

但还可以继续追问：

> tree 之前是否存在一个完全 tree-independent 的关系对象？

答案是肯定的。最直接的对象不是连续坐标，而是所有 unit slots 之间的整数差关系。

## 2. 定义完整 pair relation field

对整数 slots

\[
x=(x_1,\ldots,x_N),
\]

定义

\[
\boxed{d_{ij}=x_i-x_j.}
\]

记完整关系场为

\[
D(x)=(d_{ij})_{1\le i,j\le N}.
\]

它具有：

\[
\boxed{d_{ii}=0,}
\]

\[
\boxed{d_{ij}=-d_{ji},}
\]

以及三点闭合：

\[
\boxed{d_{ij}+d_{jk}=d_{ik}.}
\]

这些都是纯整数关系。

## 3. P019-X37 —— closed pair field + total 唯一恢复 fine state

设一个整数 matrix `D=(d_ij)` 满足上述 diagonal/antisymmetry/three-cycle closure。

对每个 `i`：

\[
\sum_j d_{ij}
=
Nx_i-\sum_jx_j.
\]

若 root total 为

\[
c=\sum_jx_j,
\]

则

\[
\boxed{
x_i=(c+\sum_jd_{ij})//N.}
\]

因此只要所有 numerator 可被 `N` 整除，`D+c` 唯一恢复一个整数 fine state。

对 `A_{N-1}` 零和状态，`c=0`，所以合法 closed field 本身即可恢复状态。

## 4. P019-X38 —— contraction imbalance 是 relation-field cut sum

取两个不交的 slot sets `A,B`。

定义原 contraction imbalance：

\[
z(A,B)
=
|B|\sum_{i\in A}x_i
-|A|\sum_{j\in B}x_j.
\]

则

\[
\boxed{
z(A,B)
=
\sum_{i\in A}\sum_{j\in B}d_{ij}.}
\]

证明直接展开右侧：

\[
\sum_{i\in A,j\in B}(x_i-x_j)
=|B|\sum_{i\in A}x_i-|A|\sum_{j\in B}x_j.
\]

因此 Contraction Atlas 中每个 internal `z` 都只是同一个 tree-independent relation field 在某个 directed block cut 上的整数求和。

这解释了：

- 为什么换 tree 只是换 cut basis；
- 为什么 local reassociation 可以只搬运 `z`；
- 为什么 pentagon coherence 自动成立于合法 states；
- 为什么 `z^2` 能进入 pair-dispersion merge law。

## 5. P019-X39 —— pair dispersion 就是 relation-field square sum

Supplement 11 定义

\[
P(x)=\sum_{i<j}(x_i-x_j)^2.
\]

因此立即有

\[
\boxed{P(x)=\sum_{i<j}d_{ij}^2.}
\]

对零和 `A_{N-1}`：

\[
\boxed{P=2Nq.}
\]

所以 P019 的 square-radial observation 可以完全从 tree-independent pair relation field 重建。

## 6. primitive unit 在关系场中的维度不变性

取 primitive root state

\[
x=e_i-e_j.
\]

有

\[
\sum_kx_k^2=2,
\qquad
q=1.
\]

由 X39：

\[
\boxed{P=2N.}
\]

也就是说，随着 slots/维度增加，primitive unit 关联到的 raw pair relations 数量会增加，但 exact scale projection

\[
\boxed{q=P//(2N)=1}
\]

始终保持 1。

这给“1 在任意有限维仍为 1”一个新的关系层解释：

> 高维增加的是该 unit 与更多 slots 的关系数量，不是 unit value 本身。

## 7. P019-X40 —— relation dimension = `N-1`

完整 field 有 `N(N-1)/2` 个无向 pair differences，但 three-cycle closure 使它们高度相关。

固定一个参考 slot `r` 后，只要保存

\[
\delta_i=x_i-x_r,
\qquad i\ne r,
\]

就有

\[
\boxed{d_{ij}=\delta_i-\delta_j}
\]

（约定 `delta_r=0`）。

所以完整 closed pair field 只含 `N-1` 个自由整数关系度。

对 `A_p`，`N=p+1`：

\[
\boxed{
\dim_{relation}=N-1=p.
}
\]

结合此前：

\[
\boxed{
\dim_{growth}
=
\dim_{contract}
=
\dim_{relation}
=p.
}
\]

这是三个不同离散操作得到的相同维数。

## 8. anchor-difference chart：`N-1` 个数但有一个模 `N` 合法条件

给定

\[
\delta_i=x_i-x_r,
\]

和 total `c`：

\[
c=Nx_r+\sum_{i\ne r}\delta_i.
\]

所以：

\[
\boxed{
x_r=(c-\sum\delta_i)//N.}
\]

合法性仅为

\[
\boxed{
\sum\delta_i\equiv c\pmod N.
}
\]

因此固定 total 的 anchor-difference coordinates 在 ambient `Z^(N-1)` 中形成 index `N` 的 affine sublattice。

这已经比 binary contraction `z` chart 的

\[
I(T)=\prod_v|v|
\]

更稠密，但它仍然选择一个 anchor，且 pair differences 本身不是 fixed-total lattice 的 unimodular coordinates。

## 9. P019-X41 —— spanning-tree subtree-flow chart 是 index 1

再取任意连接全部 slots 的 rooted spanning tree `S`。

对每个非 root vertex `v`，删去 parent edge 后，令 `Sub(v)` 是 `v` 下方的 rooted subtree。

定义 flow coordinate：

\[
\boxed{
f_v=\sum_{i\in Sub(v)}x_i.}
\]

共有 `N-1` 个整数。

### 反解

若 `children(v)` 为 children：

非 root：

\[
\boxed{
x_v=f_v-\sum_{w\in children(v)}f_w.}
\]

root：

\[
\boxed{
x_r=c-\sum_{w\in children(r)}f_w.}
\]

因此任意

\[
(f_v)\in\mathbb Z^{N-1}
\]

都唯一给出一个 total 为 `c` 的整数 state。

所以：

\[
\boxed{
\{x\in\mathbb Z^N:\sum x_i=c\}
\cong
\mathbb Z^{N-1}
}
\]

由纯整数 tree-flow chart 实现，chart index 为

\[
\boxed{1.}
\]

对零和 `A_{N-1}`，这就是一个真正的 unimodular integer chart。

## 10. path chart 与 `A` 型简单根坐标

若 spanning tree 取一条 path，则 flows 是 successive subtree/prefix sums。

例如取合适方向：

\[
f_1=x_1,
\qquad
f_2=x_1+x_2,
\quad\ldots\quad,
 f_{N-1}=x_1+\cdots+x_{N-1}.
\]

反解：

\[
x_1=f_1,
\qquad
x_i=f_i-f_{i-1},
\qquad
x_N=c-f_{N-1}.
\]

在 `c=0` 时，这正是 `A_{N-1}` 零和整数格的标准 rank-`N-1` 整数坐标邻域；`A_n` root lattice 与 simple-root bases 属于成熟数学，本项目不作原创声明。

## 11. 四种 current-state 表示的层级

现在至少有四种等价但用途不同的表示：

### A. slot values

`x_1,...,x_N` + fixed total constraint。

### B. complete pair relation field

`d_ij`。

优点：tree-independent、pair/permutation relation 明确；缺点：`O(N^2)` 冗余。

### C. spanning-tree flow chart

`N-1` 个 `f_e`。

优点：index 1、最紧整数 state coordinates；缺点：选择 spanning tree/chart。

### D. contraction imbalance chart

`N-1` 个 `z_v`。

优点：与 block merge、fiber minimum、pair dispersion、boundary witness 高度局部；缺点：合法 lattice index

\[
\prod_v|v|
\]

较稀疏。

因此 contraction tree 的价值不再是“压到最少整数个数”，而是：

\[
\boxed{
\text{用坐标格密度换取层级局部性与 dimension-contraction locality。}
}
\]

## 12. P019-X42 —— binary split-flow chart 到 imbalance chart 的三角缩放

对 binary contraction tree 的每个 internal node `v`：

- parent total `c_v`；
- left child size `m_v`；
- total size `|v|`；
- left child total 记作 split flow

\[
f_v=a_v.
\]

则

\[
\boxed{
z_v=|v|f_v-m_vc_v.}
\]

给定 root total 与所有 `f_v`，整棵叶子 state 可递归恢复，而且任意整数 `f_v` 都合法。

若按 root-to-leaf 顺序排列 internal nodes，则 `c_v` 只依赖 root total 与 ancestor split flows。

所以从 `f` 到 `z` 的整数线性/仿射变换是 triangular，主对角线恰为

\[
|v|.
\]

因此

\[
\boxed{
|\det(f\to z)|
=
\prod_v|v|
=I(T).
}
\]

这给 Supplement 13 的 chart-index theorem 一个更直接解释：

> imbalance chart 的 lattice sparsity 正是把 unimodular bulk split-flow 改写成 proportional-deviation coordinates 所产生的逐层整数缩放。

## 13. 前人工作边界

本补充邻接多个成熟工具：

- `A_n` root lattice / simple roots；
- graph incidence / spanning-tree integer coordinates；
- complete-graph Laplacian quadratic form；
- cut/flow spaces。

这些一般理论不属于 Enterprise Math 原创。

P019 当前新增研究接口在于：

1. 把 pair relation field 与 finite-precision `q`、unit invariance 连接；
2. 证明所有 contraction imbalance 都是同一个 field 的 cut sums；
3. 对比 index-1 flow chart 与 high-index imbalance chart，解释后者的 locality tradeoff；
4. 把 growth/contract/relation 三种内部维数读法统一到 `p`。

正式 promotion 前必须登记 primary sources / lineage。

## 14. 实现与验证

`src/enterprise_math/relation_field.py`：

- complete pair field；
- closure check；
- field + total recovery；
- anchor difference chart / modulo-N legality；
- spanning-tree subtree-flow chart / exact recovery；
- block cut sum；
- pair dispersion from field。

`tests/test_relation_field.py` 验证：

- 完整 field closure 与恢复；
- 所有 anchors 的 round-trip；
- anchor chart index `N`；
- path/star/arbitrary rooted-tree flow chart 的 index-1 round-trip；
- 任意 block imbalance = relation-field cut sum；
- zero-sum pair dispersion / quadratic state。

## 15. 下一步

1. 把 spanning-tree flow chart 与 contraction split-flow chart 明确同构，并实现 chart routing；
2. 研究哪种 chart 对给定 future operation family 最低成本，而不是静态追求最小 index；
3. 用 Supplement 08 future-safe quotient 判断何时 complete field / flow chart / imbalance chart 可以互相安全替换；
4. 把 intrinsic automorphism direction 作用直接提升到 pair relation field，而不是绑定某一 contraction tree；
5. 继续研究“挖球”边界是否可以直接表达成 relation-field cut condition，从而完全移除外部几何坐标解释。
