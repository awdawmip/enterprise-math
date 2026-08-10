# P025 补充 114 —— Poset Boundary Width

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-poset-observable-stage113`  
依赖：P025 补充 113  
硬阻断：`NONE`

## 1. 从失效边界到精确替代成本

补充 113 已证明：对 full membership future，scalar ideal cardinality 只有在 observation poset 为 chain 时才完备。精确 replacement state 是 maximal antichain boundary：

\[
\partial I=\operatorname{Max}(I).
\]

Stage 114 进一步问：worst case 下这个 boundary 必须有多大？

## 2. P025-T255 —— exact width law

令 \(P\) 为有限 poset，\(w(P)\) 表示它的 width，即最大 antichain 大小。

则

\[
\boxed{
\max_{I\in J(P)}|\partial I|
=
w(P).
}
\]

### 证明

每个 \(\partial I\) 都是 antichain，所以

\[
|\partial I|\le w(P).
\]

反过来，取一个 maximum antichain \(A\)。其 down-closure

\[
I_A:=\downarrow A
\]

是 order ideal；又因为 \(A\) 是 antichain，

\[
\operatorname{Max}(I_A)=A.
\]

故上界可以达到。

因此，对 full ideal-membership semantics，worst-case 所需的 labelled boundary generators 数量精确等于 poset width。

## 3. Total-order recovery

有限 poset 的 width 等于 1 当且仅当它是一条 chain。因此

\[
\boxed{
w(P)=1
\iff
\text{Stage109 scalar prefix/rank geometry 全局成立}.
}
\]

此前的一坐标 merged-rank path，正是 width-one boundary calculus。

## 4. P025-T256 —— monotone ideal path 等价于 dominance-monotone antichain path

若

\[
I_0\subseteq I_1\subseteq\cdots\subseteq I_h
\]

是一条 monotone order-ideal path，并定义

\[
A_j:=\partial I_j,
\]

则

\[
\boxed{
A_0\preceq A_1\preceq\cdots\preceq A_h,
}
\]

其中

\[
A\preceq B
\iff
\downarrow A\subseteq\downarrow B.
\]

反之，任意这样的 dominance-monotone antichain path，都通过 down-closure 唯一恢复 monotone ideal path。

所以 full ideal history 可以存成 boundary path，每个 node 最多保存 \(w(P)\) 个 boundary labels，而不必保存整张 incidence matrix。

## 5. Boundary labels 是语义信息

boundary 的**大小**仍然不够。二元素 antichain 上

\[
\{a\}
\quad\text{与}\quad
\{b\}
\]

boundary size 都是 1，却对 labelled membership query 给出不同答案。

所以 scalar rank 的正确替代物不是另一个 scalar（例如 `used boundary width`），而是一个 labelled antichain state；\(w(P)\) 只控制它的 worst-case support size。

## 6. 与 A4 support 的关系

A4 拥有 finite multivalued support / correspondence algebra。Stage 114 不把 A4 relation 约化成 poset antichain。

这里可复用的 pressure test 只有：

- chain observation family → 一个 prefix boundary coordinate；
- width-\(w\) partial observation family → 最多可能需要 \(w\) 个 incomparable labelled boundary generators；
- 对 full membership future，support/cardinality 不能代替 labels。

这为底层提供一条重要区分：

\[
\boxed{
\text{precision amount}
\neq
\text{precision support geometry}.
}
\]

## 7. Prior-art 边界

poset width、antichains、order ideals 与 ideal–antichain correspondence 都是经典数学。这里不主张一般理论新颖。

项目侧结果是：它们给出了 P025 merged-rank future-state compiler 的精确 failure/replacement calculus。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_boundary_width.py`；
- `tests/test_poset_boundary_width.py`。

executable layer 检查 width identity、tight witness、total-order recovery、boundary-path round trip，以及 equal boundary cardinality 不是 semantic equality 的负边界。

## 9. 下一前沿

下一问题转为 task-relative：full membership query 需要完整 ideal boundary，但 declared future language 可能只读取 poset elements 的某个子集或 quotient。因此后续应寻找 declared query family 的 **coarsest sufficient boundary projection**，而不是默认总保存完整 antichain。
