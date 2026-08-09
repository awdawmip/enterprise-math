# A3 Guard-Image Lattice 补充 05 —— Rank-One Residue Refinement 与低于 Guard-Visible 的 Task Precision

状态：`RESEARCH WIP / EXACT SUBLATTICE REFINEMENT LAW + STRICT PRECISION-SEPARATION EXAMPLE`

## 1. 问题

前面已经证明：若当前 coarse fiber 的实际可达 branch effects 不唯一，则当前 quotient 对该 future language 不 exact。

一个最直接但可能过度的修复是：把所有 guards 完全暴露，使每个 guard score 都能从 refined coarse state 精确读取。

但这是否必要？

答案是否定的。

rank-one hidden lattice 下，partition refinement 可以在**不降低 hidden rank**的情况下缩小 hidden lattice 的指数，从而只保留 parent arithmetic-line 参数的某个 residue class。某些导致 effect ambiguity 的 branch pattern 会因此消失。

## 2. A3-G19 —— Rank-One Guard Image 的 Refinement Subgroup Law

设 parent partition 为 `P`，refinement 为 `R`：

\[
R\preceq P.
\]

则：

\[
K_R\subseteq K_P.
\]

施加 guard map `W`：

\[
W(K_R)\subseteq W(K_P).
\]

若 parent hidden image rank 为 1，写 canonical step：

\[
W(K_P)=\mathbb Z h.
\]

child image 的 rank 不可能增加，只可能：

### 情形 A —— rank 降到 0

\[
W(K_R)=0.
\]

此时 guards 对该 refined partition 完全可见。

### 情形 B —— rank 仍为 1

任意 `Z h` 的 rank-one subgroup 都具有形式：

\[
\boxed{
W(K_R)=q\mathbb Z h,
\qquad q\in\mathbb N_{>0}.
}
\]

用 canonical first-nonzero-positive steps：

\[
\boxed{h_R=q h_P.}
\]

`q` 正是 subgroup index：

\[
\boxed{q=[W(K_P):W(K_R)].}
\]

所以 refinement 即使不让 guard rank 下降，也可以让 hidden variation lattice 变得更稀。

## 3. A3-G20 —— Refinement Fiber = Parent Parameter 的 Residue Class

parent coarse fiber 的 scores：

\[
g+t h,
\qquad t\in\mathbb Z.
\]

若 child image：

\[
q\mathbb Z h,
\]

则每个具体 child fiber 对应 parent 参数的一个剩余类：

\[
\boxed{t\equiv a\pmod q.}
\]

写：

\[
t=a+qn,
\qquad n\in\mathbb Z.
\]

child scores 就是：

\[
\boxed{
(g+a h)+n(qh).
}
\]

所以 child branch reachability 仍然是 Supplement 01 的 rank-one sweep，只是：

- base 从 `g` 变成 `g+a h`；
- step 从 `h` 变成 `q h`。

因此 residue-refined branch reachability 有 exact closed solver，不需要 fine-state enumeration。

## 4. 关键三槽例子

取 3 个 fine coordinates，两个 guards：

\[
w^{(1)}=(0,1,2),
\]

\[
w^{(2)}=(0,-1,-2).
\]

### Parent partition

\[
P=\{\{0,1,2\}\}.
\]

其 kernel generators 可取：

\[
e_1-e_0,
\qquad
e_2-e_0.
\]

guard images：

\[
(1,-1),
\qquad
(2,-2).
\]

所以：

\[
\boxed{W(K_P)=\mathbb Z(1,-1).}
\]

取 fine state：

\[
c=(0,1,0).
\]

base scores：

\[
g=(1,-1).
\]

parent score line：

\[
(1+t,-1-t).
\]

可达 patterns：

\[
\boxed{
(F,T),\quad(T,T),\quad(T,F).
}
\]

其中 `(T,T)` 在：

\[
t=-1
\]

出现，因为 scores 恰为 `(0,0)`。

## 5. 一个中间 refinement 就能删除 `(T,T)`

取：

\[
R=\{\{0,2\},\{1\}\}.
\]

此时唯一 hidden within-block direction 是：

\[
e_2-e_0,
\]

其 guard image：

\[
(2,-2).
\]

所以：

\[
\boxed{
W(K_R)=2\mathbb Z(1,-1).
}
\]

hidden rank **仍为 1**；guards 并没有变成可见。

但包含当前 fine state `c=(0,1,0)` 的 child fiber 对应 parent 参数：

\[
\boxed{t\equiv0\pmod2.}
\]

scores 只可能：

\[
(1+2n,-1-2n).
\]

于是：

\[
\boxed{
R_y=\{(F,T),(T,F)\},
}
\]

`(T,T)` 永远不可达。

## 6. A3-G21 —— Task-Exact Precision 可严格低于 Guard-Visible Precision

定义 branch effects：

- `(F,T)` 与 `(T,F)` 产生相同 coarse effect `E`；
- `(T,T)` 产生不同 coarse effect `E'`；
- `(F,F)` 不可达，其 effect 任意。

### Parent

parent 可达 `(T,T)`，所以：

\[
a_E(P)>1.
\]

当前 quotient 不 exact。

### Intermediate refinement `R`

`(T,T)` 因 mod-2 hidden residue 消失，只剩两个 effect 都为 `E` 的 patterns：

\[
\boxed{a_E(R)=1.}
\]

所以 future task 已 exact，尽管 guards 仍 hidden。

### Guard-visible refinement

两个 guard 的 fine coefficient signatures 分别为：

\[
(0,0),\quad(1,-1),\quad(2,-2).
\]

三者全部不同。

若要求两个 guards 本身 exact observable，则 observation-aware solver 必须 refinement 到：

\[
\boxed{
S=\{\{0\},\{1\},\{2\}\}.
}
\]

即 singleton precision。

因此：

\[
\boxed{
\text{minimum precision for this declared branch-output task}
<
\text{minimum precision for exact guard identity}.
}
\]

这是严格例子，不是启发式比较。

## 7. relation-rank precision cost

fine capacities 全为 1。

### Parent `P`

block count `1`：

\[
\operatorname{rank}_{rel}=0.
\]

### Task-exact `R`

block count `2`：

\[
\operatorname{rank}_{rel}=1.
\]

从 parent 只需：

\[
\boxed{\Delta d_{task}=1.}
\]

### Guard-visible singleton `S`

block count `3`：

\[
\operatorname{rank}_{rel}=2.
\]

需：

\[
\boxed{\Delta d_{guard}=2.}
\]

所以：

\[
\boxed{
\Delta d_{task}=1<2=\Delta d_{guard}.
}
\]

这直接展示“future language 决定最低精度”的非平凡收益。

## 8. 与 relation quantum 的二维 precision profile

该例也说明只看 relation rank 不够，而只看 relation quantum 也不够。

unit capacities `(1,1,1)` 下：

- parent capacities `(3)`：relation quantum `g=3`；
- intermediate capacities `(2,1)`：`g=1`；
- singleton capacities `(1,1,1)`：`g=1`。

所以 intermediate refinement 已经把 structural relation quantum 从 `3` 细化到 `1`，与 singleton 相同，但保留的 relation rank 只有 `1` 而不是 `2`。

任务此时已经 exact。

因此：

\[
\boxed{
\text{precision 至少需要 rank 与 quantum 两个方向，
但 branch reachability 还可能进一步依赖 lattice coset/orientation。}
}
\]

不能把精度压成一个单标量。

## 9. 实现

新增：

- `src/enterprise_math/rank_one_guard_refinement.py`；
- `tests/test_rank_one_guard_refinement.py`。

接口：

- `rank_one_step_index`；
- `analyze_rank_one_guard_refinement`；
- `rank_one_residue_reachable_patterns`；
- `rank_one_residue_branch_erasure_report`。

测试直接保存本文三槽例子，并验证：

- parent step `(1,-1)`；
- child step `(2,-2)`；
- image index `2`；
- parent 不 exact；
- child hidden rank 仍为 1，但 task exact；
- exact guard observation 必须 singleton；
- task relation rank gain `1`，guard-visible rank gain `2`。

## 10. 对 P018 / A2 的含义

该结果给出一个强约束：

> **precision refinement 不应被简化成“把未来读取的 predicate 全部显式保存”。**

有时更少的 retained relation detail 只需把 hidden fiber 缩成更稀的 residue class，就足以消除未来 coarse-output ambiguity。

对 A2/P023：这是 general future-compatible quotient 的 A3 arithmetic specialization。

对 P018：这是“任务所需 precision 小于 observables 全量可见 precision”的明确 integer example，应作为 adaptive precision selection 的压力测试。

## 11. 下一步

1. 对 rank-one parent lattice，分类哪些 partition refinements 能产生哪些 image index `q`；
2. 给定 branch effect classes，求使 `a_E=1` 的最小 image-index / relation-rank refinement；
3. 推广到 rank-two：refinement 对 `L_G` 产生 finite-index sublattice / rank drop，分析 arrangement cells 如何因 lattice residue 被删除；
4. 把 `(relation rank, relation quantum, guard-image index/coset)` 形成 task-precision certificate，而不是人为加权成一个分数；
5. Relay 给 P018/P023，避免下游把“guard fully visible”当作最低精度的默认要求。
