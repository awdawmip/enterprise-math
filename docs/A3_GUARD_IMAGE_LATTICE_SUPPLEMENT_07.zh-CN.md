# A3 Guard-Image Lattice 补充 07 —— Canonical Hidden-Subgroup Refinement 与 Rank-Two Complete Task Solver

状态：`RESEARCH WIP / GENERAL SUBGROUP-REFINEMENT THEOREM + COMPLETE RANK-TWO STATE-LOCAL SOLVER`

## 1. rank-one modulus 的真正一般形式

Supplement 06 中：

\[
L_{parent}=\mathbb Z h
\]

的 refinement 由子群：

\[
q\mathbb Z h
\]

控制；按 hidden labels modulo `q` 分组得到 canonical coarsest refinement。

这不是 rank-one 特例，而是一般 hidden lattice 的 subgroup/coset 结构。

设 parent hidden guard image：

\[
L=W(K_P)
\subseteq\mathbb Z^r
\]

rank 为：

\[
d.
\]

取 exact `Z`-basis：

\[
H:\mathbb Z^d\xrightarrow{\cong}L.
\]

## 2. A3-G26 —— Hidden Coordinate Labels

在每个 parent block `B` 内固定 anchor `a`。

对任意 `i in B`：

\[
W_i-W_a\in L.
\]

由于 `H` 是 `Z`-basis，存在唯一：

\[
\boxed{\lambda_i\in\mathbb Z^d}
\]

使：

\[
\boxed{W_i-W_a=H\lambda_i.}
\]

anchor label 取 `0`。

换 anchor 只对该 parent block 全体 `lambda_i` 做同一个平移，因此 pair differences 与 subgroup cosets 不变。

## 3. A3-G27 —— Canonical Hidden-Subgroup Refinement Theorem

任取 integer subgroup：

\[
M\le\mathbb Z^d.
\]

在每个 parent block 内定义：

\[
\boxed{
i\sim_M j
\iff
\lambda_i-\lambda_j\in M.
}
\]

由于 `M` 是 subgroup，`~_M` 是等价关系。

其等价类组成 partition：

\[
\boxed{R_M.}
\]

### 3.1 containment

若 `i,j` 位于同一 `R_M` block：

\[
\lambda_i-\lambda_j\in M.
\]

于是：

\[
W_i-W_j=H(\lambda_i-\lambda_j)\in H(M).
\]

所以：

\[
\boxed{W(K_{R_M})\subseteq H(M).}
\]

### 3.2 coarsest property

若任意 refinement `R` 满足：

\[
W(K_R)\subseteq H(M),
\]

则同一 `R` block 内任意 `i,j`：

\[
H(\lambda_i-\lambda_j)=W_i-W_j\in H(M).
\]

`H` injective，因此：

\[
\lambda_i-\lambda_j\in M.
\]

故：

\[
\boxed{R\preceq R_M.}
\]

所以 `R_M` 是唯一最粗使 child hidden image contained in `H(M)` 的 partition refinement。

## 4. A3-G28 —— Exact-Image Preservation

进一步，若某 actual refinement `R` 的 hidden image **恰好**是：

\[
\boxed{W(K_R)=H(M),}
\]

则由 G27：

\[
R\preceq R_M,
\]

所以：

\[
H(M)=W(K_R)
\subseteq
W(K_{R_M}).
\]

而 containment 已给：

\[
W(K_{R_M})\subseteq H(M).
\]

因此：

\[
\boxed{W(K_{R_M})=H(M).}
\]

这意味着：

> 任意 refinement 若实现某一个具体 hidden subgroup，canonical coset partition 会以更粗或相同的 partition 实现**完全相同**的 hidden score lattice。

对固定当前 fine state，它们的 guard-score coset也相同：

\[
g+H(M).
\]

所以任何只依赖当前 reachable coarse effects 的 state-local task，在 `R` 与 `R_M` 上具有相同 branch ambiguity。

## 5. A3-G29 —— Partition-Realizable Hidden Subgroups 是有限的

每个 child hidden image 都由 child blocks 内的 coefficient differences生成。

在 parent hidden coordinates 中，这些 generators 全部来自有限集合：

\[
\boxed{
D=\{\lambda_i-\lambda_j:
 i,j\text{ 在同一 parent block}\}.
}
\]

所以任意 partition refinement `R` 的 coordinate subgroup：

\[
M_R=H^{-1}(W(K_R))
\]

必由 `D` 的某个 subset 生成。

反过来，若：

\[
M=\langle D_0\rangle,
\qquad D_0\subseteq D,
\]

则 `R_M` 会把 `D_0` 中每条 difference 的两个 endpoints 放在同一 equivalence class，所以 child image包含 `D_0` 生成的 `M`；G27 又给 child image包含于 `M`。

因此：

\[
\boxed{W(K_{R_M})=H(M).}
\]

故：

\[
\boxed{
\{\text{partition-realizable hidden images}\}
=
\{\langle D_0\rangle:D_0\subseteq D\}
\text{ 去重后的有限 subgroup family}.
}
\]

这把 infinite state / Bell partition 问题进一步压成 finite hidden-subgroup closure 问题。

最坏仍可能指数增长；本 theorem 不主张 general polynomial enumeration。

## 6. Rank-two executable specialization

当 parent hidden rank：

\[
d=2,
\]

用 Supplement 02 的 exact `Z^2` basis 后：

- rank-0 subgroup：`()；`
- rank-1 subgroup：canonical step；
- rank-2 subgroup：canonical HNF-style pair。

membership 也全部 integer-exact。

新增：

- `canonical_z2_subgroup`；
- `z2_subgroup_contains`；
- `rank_two_guard_labels`；
- `rank_two_canonical_sublattice_refinement`；
- `rank_two_label_differences`；
- `rank_two_realizable_image_subgroups`。

实现不是枚举 all set partitions，而是从：

\[
\{0\}
\]

开始，逐个加入有限 label differences，并在每一步 canonicalize subgroup basis，去掉重复 closures。

## 7. A3-G30 —— Complete Rank-Two State-Local Minimum Task Precision

固定：

- rank-two parent partition `P`；
- 当前 fine state 的 base guard scores `g`；
- fixed parent-level branch-effect map：
  \[
  E:\{F,T\}^r\to\mathcal Y.
  \]

枚举全部 distinct realizable coordinate subgroups：

\[
M_1,\ldots,M_s.
\]

对每一个：

1. 构造唯一最粗 canonical partition `R_(M_a)`；
2. 其 child hidden rank 只能是 `0,1,2`；
3. rank 0：当前 pattern 唯一；
4. rank 1：使用 rank-one switch sweep / branch-erasure；
5. rank 2：使用 Supplement 02 exact 2D integer solver / branch-erasure；
6. 记录：
   \[
   \Delta d_a=|R_(M_a)|-|P|.
   \]

所有 safe candidates 中最小：

\[
\boxed{
\Delta d_{min}
=
\min_a\Delta d_a
}
\]

就是**全部 partition refinements 中**该 state / fixed effect language 的 minimum task-exact relation-rank gain。

证明：任意 safe refinement `R` 有实际 image `H(M_R)`；由 G28，canonical `R_(M_R)` 不比 `R` 更细、具有完全相同当前 hidden score coset，因此同样 safe。∎

minimum frontier 同样可能含多个 incomparable canonical partitions。

## 8. 四槽 rank-two strict precision-separation 例子

取两个 guards：

\[
w^{(1)}=(0,1,2,0),
\]

\[
w^{(2)}=(0,1,2,1).
\]

parent single block 的 hidden labels，在标准 `Z^2` basis 下：

\[
\boxed{
(0,0),\ (1,1),\ (2,2),\ (0,1).
}
\]

这些 differences 生成完整：

\[
\boxed{L_{parent}=\mathbb Z^2.}
\]

取 current fine state `c=(0,1,0,0)`：

\[
g=(1,1).
\]

parent full-rank fiber 命中全部四个 Boolean patterns。

设 `(T,F)` 的 branch effect 与其余三个不同。

### diagonal subgroup

取：

\[
M=\mathbb Z(1,1).
\]

canonical coset partition 是：

\[
\boxed{
R_M=\{\{0,1,2\},\{3\}\}.
}
\]

child hidden image：

\[
\mathbb Z(1,1).
\]

current score coset：

\[
(1,1)+t(1,1).
\]

只命中：

\[
(F,F),\quad(T,T).
\]

所以 `(T,F)` 不可达，task exact。

relation rank gain：

\[
\boxed{\Delta d_{task}=1.}
\]

### guard-visible precision

四个 hidden labels 全不同，所以 exact guard identity 需要 singleton partition：

\[
\boxed{\Delta d_{guard}=3.}
\]

因此：

\[
\boxed{
\Delta d_{task}=1<3=\Delta d_{guard}.
}
\]

rank-two 同样严格证明 task precision 可以远低于 guard-visible precision。

## 9. 两层 completeness oracle

对上述 4-coordinate example，测试做了两层独立全 partition 审计。

### subgroup-level oracle

枚举全部 15 个 set partitions；对每个 partition：

1. 直接求其实际 child guard-image generators；
2. 映回 parent `Z^2` basis；
3. canonicalize subgroup。

得到的 distinct subgroup set 与：

`rank_two_realizable_image_subgroups(...)`

完全一致。

所以 subgroup enumeration 没有漏掉任何 partition-realizable hidden image。

### minimum-frontier oracle

再逐一测试全部 15 partitions 的真实 branch reachability/effect ambiguity。

minimum safe relation rank 与 subgroup solver 完全一致；minimum partition frontier 也逐项相等。

这同时验证：

- search space completeness；
- final optimizer completeness。

## 10. 实现

新增：

- `src/enterprise_math/rank_two_guard_refinement.py`；
- `tests/test_rank_two_task_precision.py` 中 subgroup-level oracle；
- `src/enterprise_math/rank_two_task_precision.py`；
- `tests/test_rank_two_task_precision.py`。

`minimum_rank_two_task_precision(...)` 返回：

- minimum relation-rank gain；
- 全部 minimum safe canonical candidates；
- realizable subgroup count。

## 11. 一般 rank-d 含义

G26–G29 本身不依赖 `d=2`。

对任意 hidden rank `d`：

\[
\boxed{
\text{partition refinement}
\longleftrightarrow
\text{finite-label-generated hidden subgroup }M\le\mathbb Z^d
\longrightarrow
\text{canonical coset partition }R_M.
}
\]

真正缺少的是一般 `d` 的高效 subgroup canonicalization / membership 与 branch reachability实现，而不是结构定理。

结合 Supplement 03：fixed `d` reachability 可交给成熟 fixed-dimension ILP；因此未来 general solver 可以：

1. 用 HNF/SNF 表示 candidate subgroups；
2. 用 canonical coset refinement 取代 raw partition enumeration；
3. 用 fixed-dimension ILP 检查当前 branch effects；
4. 输出 minimum relation-rank frontier。

A3 不应自己复制一般 lattice/ILP library。

## 12. 当前边界

该 complete solver仍是：

- state-local；
- fixed parent-level branch-effect language；
- finite fine coordinate set。

它尚未解决多个 parent coarse states 的统一 global program synthesis。

subgroup enumeration 最坏仍可指数增长；当前只证明语义搜索空间比 Bell partition 更直接，不主张 universal complexity improvement。

## 13. 下一步

1. 把 general `R_M` theorem Relay 到 A2/P023/P018；
2. 研究多个 coarse states 的 common-safe subgroup frontier；
3. 用 A4 staged-support / P021 witness predicates构造真实多-state effect language；
4. 分析 minimum subgroup frontier 是否可用 antichain dominance 剪枝；
5. 将 relation rank、relation quantum、hidden subgroup index/orientation 统一成 typed precision certificate。
