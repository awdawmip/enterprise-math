# P019 补充 22 —— Partition Kernel、状态—运动同核与任意维球 Quotient

状态：`RESEARCH WIP / EXACT INTEGER QUOTIENT THEOREMS PROVED`

## 1. 目标

前面已经分别研究：

- state relation quotient；
- invisible updates；
- binary directional excavation；
- arbitrary partition coarsening。

本补充证明它们实际上共享同一个整数 kernel，并把一次 binary 挖球推广到任意 partition 的球 quotient。

## 2. partition matrix 与 kernel lattice

设当前有 `k` 个 blocks，coarse partition 有 `ell` 个 groups，对应 0-1 partition matrix：

\[
A:\mathbb Z^k\to\mathbb Z^\ell.
\]

定义：

\[
\boxed{
K_A=\{\eta\in\mathbb Z^k:A\eta=0\}.
}
\]

因为每个 fine block 恰属于一个 coarse group，`A eta=0` 等价于：

> 每个 coarse group 内的 integer changes 总和都为零。

因此：

\[
\boxed{
\operatorname{rank}K_A=k-\ell.
}
\]

## 3. P019-X75 —— coarse state fiber 是 `c+K_A`

固定 capacities `m` 与一个 fine total vector `c`。

所有具有相同 coarse totals 的 fine lifts 满足：

\[
Ac'=Ac.
\]

等价于：

\[
c'-c\in K_A.
\]

所以：

\[
\boxed{
Q_A^{-1}(Q_A(c))
=c+K_A
}
\]

（这里只写 totals fiber；weighted relation quotient 与 coarse totals/capacities 等价）。

因此被降维擦掉的 state distinctions 构成一个 affine integer kernel lattice。

## 4. P019-X76 —— coarse-invisible dynamics 就是同一个 `K_A`

所有保持 coarse totals 不变的 additive integer update `delta` 满足：

\[
A\delta=0.
\]

所以：

\[
\boxed{
\text{coarse-invisible update lattice}
=K_A.
}
\]

因此不是两个“rank 都是 `k-ell`”的巧合，而是同一个对象：

\[
\boxed{
\text{state fiber direction}
=
\text{invisible motion direction}.
}
\]

fine state 在同一 coarse fiber 内的所有移动，正是 coarse quotient 看不见的 internal dynamics。

## 5. primitive transfers 在 quotient 下的像

fine primitive update：

\[
\delta=e_i-e_j.
\]

若 `i,j` 属于同一个 coarse group：

\[
\boxed{A\delta=0.}
\]

若它们分别属于 coarse groups `alpha,beta`：

\[
\boxed{
A\delta=e_\alpha-e_\beta.
}
\]

所以 primitive relation move 在降维时只有两种命运：

1. 变成 coarse identity（纯内部运动）；
2. 仍然是一个 coarse primitive transfer。

这给 P012 primitive adjacency 一个直接 partition quotient law。

## 6. P019-X77 —— weighted relation dynamics 与 partition quotient 自然交换

weighted relation matrix：

\[
Z=cm^T-mc^T.
\]

对任意 zero-total integer update `delta`：

\[
c'=c+\delta.
\]

因此：

\[
\boxed{
Z'=Z+\delta m^T-m\delta^T.
}
\]

coarsen by `A`：

\[
AZ'A^T
=
AZA^T
+(A\delta)(Am)^T
-(Am)(A\delta)^T.
\]

即：

\[
\boxed{
Q_A\circ T_\delta
=
T_{A\delta}\circ Q_A.
}
\]

所以所有预先指定的 additive integer updates 都与 relation coarsening 严格交换。

若 operation 的 update vector 本身由 coarse quotient 决定，则仍可 descend；若 update selection 偷读 hidden relation，则可能违反 Supplement 18 的 quotient-compatible criterion。

## 7. update lattice 的 rank quotient

总量保持 update lattice：

\[
U_k=\{\delta\in\mathbb Z^k:\sum_i\delta_i=0\}
\]

有 rank：

\[
k-1.
\]

coarse update lattice `U_ell` rank：

\[
\ell-1.
\]

partition aggregation：

\[
A:U_k\to U_\ell
\]

是满射；其 kernel 正是 `K_A`。

因此：

\[
\boxed{
0\to K_A\to U_k\to U_\ell\to0
}
\]

是一个纯整数 exact sequence。

不需要把 category/homological language 当作基础；该式仅表示：

- 每个 coarse update 都有 fine lift；
- 两个 fine lifts 的差是 internal update；
- internal update rank = `k-ell`。

## 8. arbitrary partition 下的 collision-power fiber minimum

定义：

\[
E_{\mathbf m}^{(s)}(c)
=
\sum_i\Psi_{m_i,s}(c_i).
\]

对 partition `A`，coarse capacity：

\[
\mathbf M=A\mathbf m.
\]

固定 coarse totals：

\[
y=Ac.
\]

则 fine fiber minimum：

\[
\boxed{
\min_{Ac=y}E_{\mathbf m}^{(s)}(c)
=
E_{A\mathbf m}^{(s)}(y).
}
\]

### 证明

每个 coarse group 的约束只固定该 group 内 child totals 的总和。

由 `Psi` 的 min-plus block-addition law，该 group 内所有 fine blocks 的最小总 cost 等于：

\[
\Psi_{\sum m_i,s}(y_\alpha).
\]

不同 coarse groups 相互独立，因此对 groups 求和即得。∎

这对所有整数 `s>=1` 成立。

## 9. P019-X78 —— 任意 partition 的球像严格等于低维 tagged 球

定义 fine ball：

\[
B_{\mathbf m}^{(s)}(T)
=\{c:E_{\mathbf m}^{(s)}(c)\le T,\ \sum c_i=C\}.
\]

coarse tagged ball：

\[
B_{A\mathbf m}^{(s)}(T).
\]

则：

\[
\boxed{
Q_A\bigl(B_{\mathbf m}^{(s)}(T)\bigr)
=
B_{A\mathbf m}^{(s)}(T).
}
\]

### 证明

若 fine state 在 ball 内，coarse fiber-minimum不大于该 fine cost，所以其 coarse image 在 coarse ball 内。

反过来，若 coarse state在 coarse ball 内，X77 的 fiber-minimum（本节 X77 此处应读 X77 之后的 X78 前置公式）保证存在一个 fine minimizer，其 cost 正好等于 coarse cost，因此也在 fine ball 内。∎

所以任何维度降到任何更低 partition 后，得到的不是近似球，而是同一 family 的精确 tagged ball。

## 10. P019-X79 —— oriented binary contraction flag 给出球 quotient 的 boundary section

把一个 coarse partition `A` 分解为一串 oriented binary merges：

\[
\mathcal F:
\Pi_0\to\Pi_1\to\cdots\to\Pi_r=A.
\]

每一步 Supplement 16 X53 都给一个 directional-boundary bijection，其逆向 lift：

\[
L_t:B_{\Pi_{t+1}}\to B_{\Pi_t}
\]

选中对应 binary fiber 的唯一方向 endpoint。

复合：

\[
\boxed{
L_{\mathcal F}
=L_0\circ L_1\circ\cdots\circ L_{r-1}
}
\]

得到：

\[
\boxed{
Q_A\circ L_{\mathcal F}=\operatorname{id}.
}
\]

所以任意 oriented contraction flag 都给 coarse ball quotient 的一个 exact boundary section。

其像是一组嵌套 directional boundaries 上的 fine witnesses。

## 11. P019-X80 —— quotient 唯一，但 boundary section 可以依赖 flag

Supplement 06 已有最小反例：不同 contraction trees/flags 可从同一个最终 coarse state 选出不同 fine boundary witness。

所以：

\[
\boxed{
Q_A\text{ tree-independent},
}
\]

但：

\[
\boxed{
L_{\mathcal F}\text{ generally flag-dependent}.
}
\]

这不矛盾：

- coarse current relation state 不保存 contraction history；
- 一个 boundary section 是额外的 representative-selection rule；
- 若 future language 关心 representative/witness provenance，必须保存相应 flag/detail。

## 12. 高 codimension “表面”

当 `r` 次 binary merges 把 relation dimension 从 `p` 降到 `p-r`，`L_F` 把一个低 `p-r` 维 tagged ball 嵌回原球中的 nested boundary flag。

因此“表面的表面继续降维”可以写成有限组合：

\[
\boxed{
B_p
\xleftarrow{L_0}
B_{p-1}
\xleftarrow{L_1}
\cdots
\xleftarrow{}
B_0.
}
\]

每一步都是同一个 binary directional endpoint theorem，不需要新增高维公式。

## 13. 实现与验证

新增：

- `src/enterprise_math/relation_dynamics.py`
  - weighted relation update；
  - primitive transfer；
  - partition-aggregated update；
  - coarsening/update naturality check；
- `src/enterprise_math/partition_dynamics.py`
  - update lattice dimension；
  - internal update basis；
  - coarse update exact lift；
  - primitive transfer quotient image；
- tests：
  - `tests/test_relation_dynamics.py`；
  - `tests/test_partition_dynamics.py`。

回归验证：

- direct total update 与 relation update 一致；
- 多组 zero-sum updates 下 coarsening 与 dynamics 严格交换；
- within-block primitive transfer 映到 zero；
- cross-block primitive transfer 映到 coarse primitive transfer；
- kernel basis 数量严格为 `k-ell`；
- 任意小 coarse update 都存在整数 fine lift。

## 14. 当前统一结论

现在一次 finite dimension quotient 同时作用于：

### state

\[
c\mapsto Ac,
\qquad
Z\mapsto AZA^T;
\]

### motion

\[
\delta\mapsto A\delta;
\]

### ball / observation

\[
B_{\mathbf m}^{(s)}\mapsto B_{A\mathbf m}^{(s)};
\]

### hidden detail

\[
K_A=\ker A.
\]

所以：

\[
\boxed{
\text{state fiber}
=
\text{invisible motion lattice}
=
\text{dimension-loss kernel}.
}
\]

这可能是目前“乐高式维度代数”最紧的一版。

## 15. 下一步

1. 把 `K_A` 与 Refinement Forest 直接做整数 basis 对偶/坐标映射；
2. 对 higher-rank fiber `K_A` 研究 collision-power sublevel 的 discrete-convex exchange structure；
3. 研究 boundary sections 的 flag-dependence 能否由最小 witness quotient 分类；
4. 将 X77–X80 形式化到 Lean；
5. 用相同 partition-kernel language 重写 P018 precision refinement 与 P021 witness composition。
