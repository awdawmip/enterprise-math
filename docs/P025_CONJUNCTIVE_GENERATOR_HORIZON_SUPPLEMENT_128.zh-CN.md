# P025 补充 128 —— Exact Conjunctive Generator Horizon

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonideal-boundary-stage125`  
依赖：P025 补充 126–127  
硬阻断：`NONE`

## 1. Closed query classes 仍需要 generators

补充 127 已把 closure classes 确定为 conjunction query 的 exact semantic states。Stage 128 进一步问 operation 问题：

> 每个 closure class 最少需要几个 raw labels 才能命名？

## 2. P025-D51 —— minimum generator size

对 closed set

\[
C\in\operatorname{Fix}(\operatorname{cl}_\Omega),
\]

定义

\[
\boxed{g_\Omega(C):=\min\{|S|:\operatorname{cl}_\Omega(S)=C\}.}
\]

定义 global conjunctive generator horizon

\[
\boxed{g(\Omega):=\max_{C\in\operatorname{Fix}(\operatorname{cl}_\Omega)}g_\Omega(C).}
\]

它就是表示全部 semantic conjunction-future classes 所需的 exact worst-case minimum arity。

## 3. P025-T280 —— exact arity meaning

每个 raw conjunction query 都等价于某个大小不超过

\[
g(\Omega)
\]

的 generator。

反过来，按定义至少有一个 closure class 精确需要

\[
g(\Omega)
\]

个 labels；任何更小的统一 arity cap 都无法表示全部 query classes。

因此

\[
\boxed{g(\Omega)\text{ 是 exact conjunction-operation arity horizon}.}
\]

它直接由 actual future equivalence relation 定义，而不是 ambient label count 或 structural width 的粗上界。

## 4. P025-T281 —— semantic width 只是 upper bound

令

\[
P_\Omega
\]

为补充 126 的 semantic implication quotient poset。

minimum-cardinality generator 不可能包含两个 semantically equivalent labels，否则其中一个冗余。

它也不能包含两个 distinct unary-comparable classes。若

\[
x\preceq_\Omega y
\]

且二者同时进入 generator，则任何包含 \(y\) 的 exact state 已自动包含 \(x\)，删除 \(x\) 不改变 query extent / closure。

因此 every minimum generator 投影成 \(P_\Omega\) 中 antichain，从而

\[
\boxed{g(\Omega)\le\operatorname{width}(P_\Omega).}
\]

## 5. P025-C43 —— strict higher-order gap

取

\[
\Omega=\{\{a\},\{b\},\{a,b,c\}\}.
\]

补充 127 给出 semantic implication width

\[
\operatorname{width}(P_\Omega)=2.
\]

但四个 closure classes 为

\[
\varnothing,
\{a\},
\{b\},
\{a,b,c\},
\]

分别有 generators

\[
\varnothing,
\{a\},
\{b\},
\{c\}.
\]

所以

\[
\boxed{g(\Omega)=1<2=\operatorname{width}(P_\Omega).}
\]

因此 unary width 可以严格高估 true conjunction precision。

## 6. All-ideal scope 恢复 poset-width theorem

令 \(P\) 为有限 poset，并取

\[
\Omega=J(P)
\]

即**全部** order ideals。

此时 raw query 的 closure 正是包含它的最小 ideal：

\[
\boxed{\operatorname{cl}_{J(P)}(S)=\downarrow S.}
\]

因为任何包含 \(S\) 的 ideal 都包含 \(\downarrow S\)，而 \(\downarrow S\) 自己就是被 intersection 的 exact states 之一。

ideal \(I\) 的 minimum generator 就是 maximal antichain boundary \(\partial I\)。因此

\[
\boxed{g(J(P))=\operatorname{width}(P).}
\]

这在原 all-ideal scope 下精确恢复补充 114 与 120。

## 7. Degenerate mandatory-state boundary

若唯一 exact state 是 full universe \(P\)，则

\[
\operatorname{cl}(\varnothing)=P
\]

每个 query 都等价于 empty query。所以

\[
\boxed{g(\Omega)=0}
\]

尽管 semantic implication quotient 仍有一个 always-active equivalence class，width 为 1。

所以即使 unary width 为 1，更强 semantic certainty 仍能把 operation arity 压到 0。

## 8. 架构结论

precision parameters 现在形成：

\[
\boxed{
\text{ambient width}
\to
\text{semantic implication width}
\to
\text{closure generator horizon }g(\Omega).
}
\]

每一步都可能严格下降或改变 relevant geometry。

最后一个量对 conjunction future 是 task-relative 且 exact，不只是 structural upper bound。

## 9. 与 A2/A4 的关系

A2 拥有 generic future equivalence；A4 拥有 arbitrary admissible correspondences。Stage 128 给出 finite Boolean specialization，其中 coarsest operation arity 可以直接从 closure generators 计算。

不主张 arbitrary A4 relations 存在 poset-width formula。

## 10. Prior-art 边界

finite closure systems 的 minimum generators 与 implication bases 属于标准 closure/FCA 数学。这里不主张 generic novelty。

项目侧结果是 exact P025 pressure-test hierarchy，以及 unary width 与 full conjunction generator precision 之间的 strict boundary。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/conjunctive_generator_horizon.py`；
- `tests/test_conjunctive_generator_horizon.py`。

executable layer 枚举 minimum generators、验证 semantic-width upper bound、恢复 chain/diamond all-ideal width horizons、检查 strict `2 -> 1` higher-order gap，以及 zero-generator mandatory-state boundary。

## 12. 下一前沿

Stage 129 应精确刻画何时 unary semantic implication relation 已经足够表达全部 conjunctions。候选条件是 closure 完全由 singleton consequences（加 always-active core）生成，等价于不存在 irreducible higher-order implication。
