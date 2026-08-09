# A3 Guard-Image Lattice 补充 08 —— Finite-Workload Common Precision 与局部最优不可直接拼接

状态：`RESEARCH WIP / COMPLETE RANK-ONE/TWO FINITE-WORKLOAD SOLVER + STRICT LOCAL/GLOBAL GAP`

## 1. 从单 state 到统一 coarse program

Supplements 06/07 已分别对 rank-one/rank-two hidden guard 给出 **state-local** minimum task precision：固定一个 parent coarse fiber / 一个当前 fine state，只求该 state 的 declared branch-effect language exact 所需最低 refinement。

但实际 coarse program 往往需要服务多个 states。

设有限 workload：

\[
\mathcal Y=\{y_1,\ldots,y_N\},
\]

每个 state 在 parent hidden basis 中有 base guard-score vector：

\[
g^{(1)},\ldots,g^{(N)}.
\]

要求选择**同一个 partition refinement** `R`，使 workload 中每一个 state 都对同一个 parent-level branch-effect language `E` exact。

## 2. A3-G31 —— Finite-Workload Safe Refinement

给定 candidate refinement `R`，其 child hidden image为 `L_R`。

对 workload state `a`，当前 child score coset：

\[
g^{(a)}+L_R.
\]

令实际 reachable pattern set：

\[
R_a(R).
\]

则 `R` 对整个 workload safe 当且仅当：

\[
\boxed{
E|_{R_a(R)}\text{ 对所有 }a=1,\ldots,N\text{ 都为常值。}
}
\]

等价：

\[
\boxed{
\max_a a_E(y_a;R)=1.
}
\]

这是 state-local reachable-effect criterion 的有限 conjunction。

## 3. A3-G32 —— Canonical Replacement 对 workload 同时成立

Supplements 06/07 已证明：任意 refinement `R` 的实际 hidden image `L_R`，存在唯一不更细的 canonical refinement `R_can(L_R)`，并且：

\[
W(K_{R_{can}})=L_R.
\]

对 workload 中每一个固定 fine state，其 base score `g^(a)` 不变，所以：

\[
g^{(a)}+W(K_R)
=
g^{(a)}+W(K_{R_{can}}).
\]

因此所有 states 的 reachable pattern/effect ambiguity逐个相同。

所以：

\[
\boxed{
R\text{ 对整个 workload safe}
\Longrightarrow
R_{can}(L_R)\text{ 同样 safe 且不更细。}
}
\]

这说明 finite-workload minimum solver 仍只需搜索 canonical hidden-image family，而不需要恢复 Bell-number partition 枚举。

## 4. rank-one complete workload solver

parent hidden image：

\[
\mathbb Z h.
\]

所有 canonical candidates 是 Supplement 06 的有限 modulus partitions：

\[
R_1,\ldots,R_D.
\]

对每个 `R_q`，逐 workload state 运行 rank-one reachable-effect checker；全部 safe 才保留。

取：

\[
\boxed{
\Delta d_{work}
=
\min_{q:\,R_q\text{ safe for all states}}
(|R_q|-|P|).
}
\]

返回所有达到该 cost 的 partitions，形成 finite-workload minimum frontier。

## 5. rank-two complete workload solver

parent hidden rank为 2。

枚举 Supplement 07 的全部 partition-realizable subgroups：

\[
M_1,\ldots,M_s\le\mathbb Z^2.
\]

对每个 canonical `R_(M_i)`，逐 state：

- hidden rank 0：当前 pattern 唯一；
- hidden rank 1：rank-one sweep；
- hidden rank 2：rank-two exact integer halfplane solver。

全部 states safe 才保留。

minimum relation-rank gain：

\[
\boxed{
\Delta d_{work}
=
\min_{i:\,R_{M_i}\text{ workload-safe}}
(|R_{M_i}|-|P|).
}
\]

由 G32，这对所有 partition refinements 完备。

## 6. A3-G33 —— Workload Precision Lower Bound 与 strict gap

显然任何 common-safe refinement 必须对每个单 state 都 safe，所以：

\[
\boxed{
\Delta d_{work}
\ge
\max_{y\in\mathcal Y}\Delta d_{min}(y).
}
\]

但等号不必成立。

### rank-one strict example

取 hidden labels：

\[
(0,1,3),
\]

parent direction：

\[
h=(1,-1),
\]

并令只有 `(T,T)` branch effect 与 `(F,T)/(T,F)` 不同。

取两个 states：

\[
g^{(1)}=(-3,3),
\qquad
g^{(2)}=(-2,2).
\]

#### state 1

危险 `(T,T)` 发生在 parent parameter：

\[
t=3.
\]

mod 2 refinement只允许一个 mod-2 residue class，删除 `t=3`；mod 3 保留 `t=3`。

所以 state 1 有 rank-gain-1 minimum：mod 2 partition

\[
\{\{0\},\{1,2\}\}.
\]

#### state 2

危险 `(T,T)` 发生在：

\[
t=2.
\]

mod 3 删除它，而 mod 2 保留它。

所以 state 2 也有 rank-gain-1 minimum，但偏好另一个 partition：

\[
\{\{0,2\},\{1\}\}.
\]

两个 minimum partitions 互不兼容为一个共同 rank-1 refinement。

共同 workload 只有 label-visible singleton 能同时安全：

\[
\boxed{
\Delta d_{min}(y_1)=1,
\quad
\Delta d_{min}(y_2)=1,
\quad
\Delta d_{work}=2.
}
\]

因此：

\[
\boxed{
\Delta d_{work}
>
\max_y\Delta d_{min}(y).
}
\]

这证明“逐 state 各自最优后任选一个”不是合法 global precision strategy。

## 7. rank-two strict workload example

沿 Supplement 07 的 four-slot guards：

\[
w^{(1)}=(0,1,2,0),
\qquad
w^{(2)}=(0,1,2,1),
\]

并令 `(T,F)` effect 与其他 patterns 不同。

state 1：

\[
g^{(1)}=(1,1).
\]

diagonal subgroup：

\[
\mathbb Z(1,1)
\]

已能删除 `(T,F)`，只需 rank gain `1`。

state 2：

\[
g^{(2)}=(2,0).
\]

同一 diagonal coset 仍能命中 `(T,F)`，因此该 rank-gain-1 refinement 不 safe。

共同 workload 可使用 horizontal rank-one subgroup：

\[
\mathbb Z(1,0),
\]

对应 canonical partition：

\[
\boxed{
\{\{0\},\{1,3\},\{2\}\},
}
\]

relation rank gain：

\[
\boxed{2.}
\]

所以 rank-two 中同样出现：

\[
\boxed{
\text{one-state cost }1
<
\text{two-state common cost }2.
}
\]

## 8. 两组 full partition oracle

测试分别对：

- rank-one 3-coordinate；
- rank-two 4-coordinate；

枚举全部 parent refinements，逐 workload state直接计算 hidden rank、reachable patterns 与 effects。

两组中：

- common solver 的 minimum cost；
- complete minimum partition frontier；

都与 Bell-partition oracle完全相等。

因此有限-workload solver 的 completeness不仅继承自 theorem，也有独立小规模穷举回归。

## 9. 实现

新增：

- `src/enterprise_math/guard_workload_precision.py`；
- `tests/test_guard_workload_precision.py`。

接口：

- `minimum_rank_one_workload_precision`；
- `minimum_rank_two_workload_precision`；
- `WorkloadPrecisionCandidate`；
- `WorkloadPrecisionResult`。

结果返回：

- common minimum relation-rank gain；
- 全部 minimum common-safe candidates；
- workload size；
- canonical search-state count。

## 10. 三层 precision 必须区分

当前已经明确出现：

\[
\boxed{
\text{state-local minimum}
\neq
\text{finite-workload minimum}
\neq
\text{global all-state program minimum}.
}
\]

前两层已在 rank-one/rank-two 得到 complete solver。

第三层不能通过“workload 再多取几个 sample”偷换，需要对无限 coarse-state lattice 做符号化证明。

## 11. 下一步

1. 研究一个固定 refinement 是否能在**全部 coarse states**上产生唯一 coarse effect，从而编译为 global exact program；
2. 将 base-score variation 分解为 coarse-readable score lattice + hidden image lattice，避免枚举无限 states；
3. rank-one 优先寻找全局 periodic/residue coarse program 的闭式；
4. 将 finite-workload strict gap Relay 到 P018/P023，提醒 adaptive precision 区分 per-state 与 shared-model cost；
5. 对实际 A4 staged-support / P021 predicate workload做首个跨路线实例。
