# P019 补充 25 —— 整数线性 Dynamics 的最小 Exact Partition Solver

状态：`RESEARCH WIP / EXACT INTEGER QUOTIENT THEOREM + FINITE PARTITION ALGORITHM`

## 1. 主问题的第一个大类解

Relation LEGO Core 把下一阶段主问题收敛为：

> 给定 future operation language，求最小 exact relation state。

本补充对一个重要无限状态大类给出完整答案：

\[
\boxed{
c' = Bc+u,\qquad B\in\mathbb Z^{k\times k},\ u\in\mathbb Z^k.}
\]

状态空间仍是整个整数格，不枚举有限 state box。

我们只求：给定一个初始 partition，哪些 fine coordinates 真的还必须分开，才能让未来所有这些 integer affine operations 在 coarse state 上精确运行？

## 2. partition matrix

设 partition `Pi` 把 `k` 个 fine coordinates 分成 `ell` 个 coarse blocks。

其 0-1 aggregation matrix：

\[
A\in\{0,1\}^{\ell\times k},
\]

每个 fine coordinate column 恰有一个 1。

coarse state：

\[
y=Ac.
\]

## 3. P019-X90 —— 线性 dynamics exact descend 的矩阵条件

对：

\[
T_B(c)=Bc,
\]

存在一个 integer coarse dynamics：

\[
\bar T(y)=\bar By
\]

使：

\[
\boxed{
A B = \bar B A
}
\]

当且仅当该 partition 对 `B` 是 exact。

### 为什么 `bar B` 自动是整数

partition matrix `A` 对 `Z^k -> Z^ell` 是满射：每个 coarse basis vector 都可由该 block 内任一 fine basis vector映到。

如果 `AB` 在同一 source block 的 columns 相同，那么这些 common integer columns 直接组成 `bar B`。

所以不需要有理/实数 quotient matrix。

## 4. P019-X91 —— column-effect signature 判据

`AB` 的第 `j` 个 column 表示：fine coordinate `j` 的一个 unit 对每个 coarse target block 的总影响。

因此 X90 等价于：

> 对每一个 current source block `S`，任意 `i,j in S`，`AB` 的 columns `i,j` 必须完全相同。

写成 target coarse block `R` 的有限整数求和：

\[
\boxed{
\sum_{r\in R}B_{ri}
=
\sum_{r\in R}B_{rj}
}
\]

对所有 source-same `i,j` 与所有 target blocks `R` 成立。

这就是一个完全静态的 integer signature test。

## 5. P019-X92 —— 与 dimension-loss kernel invariance 等价

当前 partition kernel：

\[
K_A=\ker_{\mathbb Z}A.
\]

则：

\[
\boxed{
AB=\bar BA
\iff
B(K_A)\subseteq K_A.
}
\]

### `=>`

若 `eta in K_A`：

\[
A(B\eta)
=\bar B(A\eta)=0.
\]

所以 `B eta in K_A`。

### `<=`

若 `B` 保持 `K_A`，定义 coarse map：

\[
\bar B(Ac)=ABc.
\]

若 `Ac=Ac'`，则：

\[
c-c'\in K_A.
\]

由 invariance：

\[
B(c-c')\in K_A,
\]

所以：

\[
ABc=ABc'.
\]

因此 `bar B` well-defined。A 满射，故得到 integer matrix `bar B`。∎

这把 Supplement 22 的：

`state fiber = invisible motion lattice = K_A`

进一步升级为：

> 一个 dynamics 是否安全 coarse-grain，恰好问它是否把 invisible motion lattice 映回自身。

## 6. P019-X93 —— affine offset 不增加 distinguishability 条件

对：

\[
T(c)=Bc+u,
\]

若 linear part 已满足：

\[
AB=\bar BA,
\]

则：

\[
A(Bc+u)
=\bar B(Ac)+Au.
\]

所以 coarse affine dynamics：

\[
\boxed{
\bar T(y)=\bar By+Au.
}
\]

因此固定 offset `u` 总能投影成 `Au`；partition refinement 只由 linear part 的 hidden-to-coarse coupling 决定。

## 7. 多 operation family

设 future language 有有限个 integer linear generators：

\[
\mathcal B=\{B_1,\ldots,B_m\}.
\]

partition exact 当且仅当：

\[
\boxed{
B_a(K_A)\subseteq K_A
\quad\forall a.
}
\]

等价于每一个 `B_a` 都满足其 coarse column-effect signature condition。

只要 generators 全部 descend，任意有限 composition 自动 descend，这正是 Supplement 18 future-safe criterion 在无限整数线性 state space 上的直接实现。

## 8. P019-X94 —— signature refinement algorithm

给定初始 partition：

\[
\Pi_0.
\]

在当前 partition `Pi_t` 下，对每个 fine source coordinate `j` 构造 signature：

1. 它当前属于哪个 coarse block；
2. 对每个 operation matrix `B_a`；
3. 对每个 current target block `R`；
4. 记录：
   \[
   \sum_{r\in R}(B_a)_{rj}.
   \]

然后只在每个 current block 内按 signature 相同/不同拆分，得到：

\[
\Pi_{t+1}.
\]

重复直到：

\[
\Pi_{t+1}=\Pi_t.
\]

由于 fine coordinate 数有限，每次非稳定迭代至少增加一个 block，最多 `k-1` 次 split rounds 后终止。

## 9. P019-X95 —— stable partition 是最粗 exact refinement

设算法输出：

\[
\Pi_*.
\]

### exact

稳定意味着同一 block 内所有 coordinates 对所有 matrices / current target blocks 的 aggregate column effects 相同，因此所有 `B_a` descend。

### coarsest

设 `R` 是 `Pi_0` 的任意另一个 exact refinement。

归纳证明：

\[
R\preceq\Pi_t
\]

对所有 `t` 成立。

初始显然。

若 `R` refine `Pi_t`，取同一个 `R`-block 内两个 coordinates `i,j`。因为每个 `B_a` 在 `R` 上 exact，它们对每个 `R` target block 的 aggregate effect 相同。每个 `Pi_t` target block 是若干 `R` blocks 的并，因此对该 `Pi_t` target block 的总 effect 也相同。

所以 `i,j` 在本轮 signature 下不能被拆开，仍落在同一个 `Pi_(t+1)` block。

故 `R` refine `Pi_(t+1)`。

终止时：

\[
\boxed{
R\preceq\Pi_*.
}
\]

即所有 exact refinements 都比 `Pi_*` 更细或相同。

所以：

\[
\boxed{
\Pi_*=
\text{coarsest / minimum-state exact refinement of }\Pi_0.
}
\]

## 10. relation state 的最小 exact 表示

一旦得到 `Pi_*`，就不需要再把 fine totals 当运行 state。

直接运行：

\[
\boxed{
(m_*,C,Z_*)
=
(A_*m,C,A_*ZA_*^T),
}

并为每个 generator 计算对应 coarse `bar B_a`。

因此对于这一 operation family：

> `Pi_*` 上的 weighted relation state 是由 partition distinguishability 角度得到的最粗 exact relation state。

若 future language 不要求 refinement/history provenance，`K_(A_*)` 内的 distinctions 都可以安全删除。

## 11. 与“表面拟合/归因简化”的研究方法相容

该算法不会先假设某些 fine coordinates “应该相同”。

它从一个候选 coarse attribution 开始，然后只在 future operations 能实际把某个 hidden distinction 反馈到 coarse layer 时拆开。

所以 coarse state 的复杂度由 operation dependency 自动决定，而不是由人为坐标直觉决定。

## 12. 与成熟前人工作的边界

该结构与成熟的：

- equitable partitions；
- exact aggregation / lumpability；
- congruence / bisimulation；
- partition refinement / automata minimization；
- invariant subspace / quotient dynamics

高度相邻。

一般的 `AB=B_bar A` factorization、stable/equitable partition refinement 不是 Enterprise Math 原创。

P019 当前贡献候选是把该安全工具嵌入：

`weighted relation state + partition kernel + dimension contraction + precision/refinement memory`

这一具体 finite-precision framework。正式 promotion 前必须补 sources/lineage。

## 13. 实现与验证

新增：

- `src/enterprise_math/linear_relation_quotient.py`
  - partition matrix；
  - `descended_linear_matrix`；
  - `linear_matrix_descends`；
  - family descend；
  - iterative minimum refinement；
  - kernel-invariance checker。
- `tests/test_linear_relation_quotient.py`
  - exact intertwining `AB=B_bar A`；
  - hidden-feedback failure；
  - automatic split；
  - multi-operation joint refinement；
  - 4-coordinate candidate partitions brute-force coarsest check；
  - 3x3 binary matrices exhaustive `descend <=> kernel invariance`；
  - affine offset exact descent。

## 14. 当前意义

Relation LEGO Core 的主问题第一次有一个大类的自动解：

\[
\boxed{
\text{integer affine future language}
\Longrightarrow
\text{finite partition refinement solver}
\Longrightarrow
\text{minimum exact relation partition}.
}
\]

而 state space 本身仍然可以是无限的 `Z^k`。

这说明“future-safe 精度/降维选择”不必总靠状态枚举；在有代数结构的 operation family 中，可以直接对 operations 本身做 quotient synthesis。

## 15. 下一步

1. 扩展到 piecewise-linear / predicate-controlled integer operations：先让 branch predicates 在 quotient fibers 上可决定，再检查每个 branch matrix descend；
2. 把 weighted-relation additive dynamics registry 自动转成 `B` matrices，求实际 P019 最小 exact partition；
3. 将 P018 precision predicates / observation costs 接到这个 partition solver；
4. 研究 nonlinear polynomial maps 的 finite generator/signature closure；
5. Lean 形式化 X90–X95 的 finite partition / integer matrix版本。
