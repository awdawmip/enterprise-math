# A3 Guard-Image Lattice 补充 06 —— Canonical Modulus Refinement 与 Rank-One Minimum Task-Precision Frontier

状态：`RESEARCH WIP / EXACT COARSEST MODULUS REFINEMENT + COMPLETE STATE-LOCAL MINIMUM-RANK SOLVER`

## 1. 目标

Supplement 05 证明：rank-one hidden guard 可以通过有限-index residue refinement 消除危险 branch，而不必让 guards 完全可见。

现在进一步解决：

> 给定一个 parent partition、当前 coarse fiber 的 base guard scores，以及固定的 parent-level branch-effect language，在**全部 partition refinements** 中，最少需要增加多少 relation rank 才能让当前 task exact？

不是只在手选候选中优化，而是要得到一个 complete minimum solver。

## 2. A3-G22 —— Fine coordinate 的 hidden integer labels

假设 parent guard image：

\[
W(K_P)=\mathbb Z h.
\]

在每一个 parent block `B` 中固定一个 anchor `a`。

对任意 `i in B`：

\[
W_i-W_a\in\mathbb Z h.
\]

由于 `h` 是 parent image 的 canonical subgroup generator，存在唯一整数：

\[
\boxed{\lambda_i\in\mathbb Z}
\]

使：

\[
\boxed{W_i-W_a=\lambda_i h.}
\]

取：

\[
\lambda_a=0.
\]

这些 `lambda_i` 是 parent block 内的 hidden integer labels。

换 anchor 只会给该 block 全部 labels 加同一个常数，因此所有：

- label differences；
- modulo-`q` equality classes；

都与 anchor choice 无关。

## 3. A3-G23 —— Canonical Modulus Refinement Theorem

给定正整数：

\[
q\ge1.
\]

在每一个 parent block 内，按：

\[
\boxed{\lambda_i\bmod q}
\]

分组，得到 refinement：

\[
\boxed{R_q.}
\]

### 性质 1 —— `R_q` 保证 hidden image 被 `q` 整除

若 `i,j` 仍在同一 child block：

\[
\lambda_i\equiv\lambda_j\pmod q,
\]

所以：

\[
W_i-W_j
=(\lambda_i-\lambda_j)h
\in q\mathbb Z h.
\]

因此：

\[
\boxed{W(K_{R_q})\subseteq q\mathbb Z h.}
\]

### 性质 2 —— `R_q` 是满足该条件的最粗 refinement

设任意 refinement `R` 满足：

\[
W(K_R)\subseteq q\mathbb Z h.
\]

若 `i,j` 位于同一个 `R` block，则：

\[
W_i-W_j\in W(K_R)\subseteq q\mathbb Z h.
\]

所以：

\[
q\mid(\lambda_i-\lambda_j),
\]

即：

\[
\lambda_i\equiv\lambda_j\pmod q.
\]

因此每个 `R` block 必须完全落入某个 `R_q` residue block：

\[
\boxed{R\preceq R_q.}
\]

所以 `R_q` 是**唯一最粗**使 child hidden image contained in `q*parent image` 的 partition refinement。

## 4. 若某 refinement 的实际 image index 为 q，则 R_q 也恰好是 q

设某 refinement `R` 的 child hidden rank 仍为 1，且：

\[
\boxed{W(K_R)=q\mathbb Z h.}
\]

由上节：

\[
R\preceq R_q,
\]

所以 kernel inclusion 给：

\[
q\mathbb Z h
=W(K_R)
\subseteq
W(K_{R_q}).
\]

另一方面 canonical modulus construction 给：

\[
W(K_{R_q})\subseteq q\mathbb Z h.
\]

因此：

\[
\boxed{W(K_{R_q})=q\mathbb Z h.}
\]

这一步非常关键：任何 arbitrary refinement 如果实现某个 rank-one image index `q`，canonical `R_q` 会以**更粗或相同**的 partition 实现完全相同的 hidden guard lattice。

## 5. A3-G24 —— 有限 Modulus Visibility Bound

在每个 parent block 中取 label span：

\[
D_B=\max_{i\in B}\lambda_i-
\min_{i\in B}\lambda_i.
\]

定义：

\[
\boxed{D=1+\max_B D_B.}
\]

若：

\[
q\ge D,
\]

则任意 unequal labels 满足：

\[
|\lambda_i-\lambda_j|<q,
\]

不可能 modulo `q` 相等。

因此所有 `q>=D` 的 residue refinement 都稳定到同一个 **label-equality partition**：

\[
\boxed{R_q=R_{vis}}.
\]

`R_vis` 使所有 within-child guard coefficient differences 为零，所以：

\[
\boxed{W(K_{R_{vis}})=0.}
\]

即 guard-hidden rank 降到 0。

所以全部非零 rank-one child image indices 一定出现在有限范围：

\[
\boxed{1\le q<D.}
\]

## 6. A3-G25 —— Minimum State-Local Rank-One Task Precision Theorem

固定：

- parent partition `P`，且 `rank W(K_P)=1`；
- 当前 fine state / 当前 parent fiber 的 base guard scores `g`；
- 一个固定的 **parent-level future effect language**：
  \[
  E:\{F,T\}^r\to\mathcal Y.
  \]

我们允许 refinement 只作为内部 precision，提高后最终仍问同一个 parent-level effect `E`。

对任意 candidate refinement `R`：

- 若 child hidden rank 0，则当前 child fiber 只有一个 guard pattern，自动 branch-deterministic；
- 若 child hidden rank 1，设实际 image index：
  \[
  W(K_R)=q\mathbb Z h.
  \]
  当前 child fiber 的 score coset 恰为：
  \[
  g+q\mathbb Z h.
  \]
  exactness 只依赖这个 coset 上实际可达 patterns 的 `E` 是否常值。

由 G23/G24：

> 任意 safe refinement `R`，都存在一个 canonical `R_q`（或 guard-visible `R_vis`），其 partition 不比 `R` 更细，并且对当前 state 具有相同 hidden score lattice/coset，因此同样 safe。

所以只需有限检查：

\[
\boxed{q=1,2,\ldots,D.}
\]

对每个 `R_q`：

1. 计算实际 child guard-image rank / step；
2. 用 rank-one exact sweep 求当前 fiber reachable patterns；
3. 用 Supplement 04 判断 reachable effects 是否唯一；
4. 记录 relation rank gain：
   \[
   \Delta d_q=|R_q|-|P|.
   \]

取所有 safe candidates 中最小：

\[
\boxed{
\Delta d_{min}
=
\min_{q:\,R_q\text{ safe}}
(|R_q|-|P|).
}
\]

则：

\[
\boxed{
\Delta d_{min}
=
\text{全部 partition refinements 中的最小 state-local task-exact relation-rank gain}.
}
\]

这不是候选族内局部最优，而是利用 rank-one subgroup structure 得到的 complete solver。

## 7. 最低 cost 可以唯一，但最低 partition 不一定唯一

定义 minimum frontier：

\[
\mathcal F_{min}
=
\{R_q:
R_q\text{ safe},\ |R_q|-|P|=\Delta d_{min}\}.
\]

该集合可以包含多个互不 refinement 的 partitions。

### 最小例子

hidden labels：

\[
(0,1,3).
\]

对 parent single block：

### mod 2

residues：

\[
(0,1,1),
\]

得到：

\[
R_2=\{\{0\},\{1,2\}\}.
\]

### mod 3

residues：

\[
(0,1,0),
\]

得到：

\[
R_3=\{\{0,2\},\{1\}\}.
\]

二者互不 refine，但 relation rank gain 都为 1。

取 base scores `(1,-1)`，parent direction `(1,-1)`，并令只有 `(T,T)` branch effect 与 `(F,T)/(T,F)` 不同，则：

- mod 2 child step 为 `2h`；
- mod 3 child step 为 `3h`；
- 两个 child fiber 都不再命中 `(T,T)`；
- 两个 partition 都 task exact。

全三槽 partition oracle 验证：

\[
\boxed{
\mathcal F_{min}=\{R_2,R_3\}.
}
\]

因此应区分：

\[
\boxed{
\text{minimum precision cost}
}
\]

与：

\[
\boxed{
\text{minimum precision frontier}.
}
\]

cost 可以唯一，representation choice 可以形成 antichain。

## 8. 与 A2/P023 / A4 frontier 思想的关系

一般“所有最低 future-compatible states 的 frontier”属于 A2/P023 的 behavioral/minimal-state 母问题。

A3 在这里给出一个非常具体的 arithmetic specialization：

- minimum cost 是 integer relation-rank gain；
- minimum states 是 canonical modulus partitions 的 antichain；
- hidden lattice subgroup / residue 决定哪些 branch behaviors 被删除。

这与 Relay 中 A4/support 路线近期出现的 Pareto/frontier/antichain 结构是 `COMPOSABLE_INDEPENDENT`，不能因术语相似直接合并；可在未来寻找共同的 finite-antichain母工具。

## 9. 实现

新增：

- `src/enterprise_math/rank_one_guard_modulus.py`；
- `tests/test_rank_one_guard_modulus.py`；
- `src/enterprise_math/rank_one_task_precision.py`；
- `tests/test_rank_one_task_precision.py`。

关键接口：

- `rank_one_guard_labels`；
- `rank_one_modulus_refinement`；
- `rank_one_modulus_visibility_bound`；
- `minimum_rank_one_task_precision`。

测试包括：

1. hidden integer labels 重建；
2. canonical modulus theorem 的小规模全 partition oracle；
3. modulus visibility stabilization；
4. 三槽 `Delta d_task=1 < Delta d_guard=2` 例子；
5. solver minimum rank 与全 partition brute oracle 完全一致；
6. `(0,1,3)` 的两个 incomparable minimum partitions，oracle 确认 frontier 完整。

## 10. 当前边界

本 theorem 是**state-local + fixed parent-level effect language**。

它不自动解决：

- refinement 后 future output language 本身也变细的情形；
- 多个 coarse states 共同要求一个 global coarse program 的情形；
- rank-two/higher hidden image 的 minimum partition synthesis。

这些必须另行证明，不能把 state-local solver 偷换成 global theorem。

## 11. 下一步

1. 把 minimum frontier 与 relation quantum / guard-image index 一起形成 typed precision certificate；
2. rank-two 研究 finite-index sublattice refinement 的 canonical form，判断是否存在类似 modulus refinement 的 coarsest lattice constraints；
3. 对多个 parent coarse states 求共同 safe refinement，检查 minimum frontier 是否仍有限可生成；
4. 将该 strict precision-separation result Relay 到 P018/A2；
5. 尝试把 A3 minimum partition antichain 与 P023/A4 的 finite frontier 工具做 theorem-level bridge，而不是复制实现。
