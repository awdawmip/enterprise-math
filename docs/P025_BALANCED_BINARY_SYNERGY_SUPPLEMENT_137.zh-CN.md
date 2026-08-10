# P025 补充 137 —— Pure k-way conjunction 的最优 binary-helper compilation

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. 问题

Stage 136 已证明 pure raw law

\[
a_1\wedge\cdots\wedge a_k\Rightarrow z
\]

在固定 raw alphabet 上无法把 premise arity 从 `k` 降低；引入 auxiliary labels 后才可以 binary compilation。Stage 135 使用的是 depth `k-1` 的顺序 helper chain，但这个 depth 不是最优。

现在允许：sound positive single-head rules、最大 premise arity 二、fresh helper labels 与 distinguished output `z`。compiler 必须对每个 raw-only initial seed 保持 pure raw closure。

## 2. Helper 下界

考虑从完整 raw seed `A={a_1,...,a_k}` 推导 `z`。由于 compiler 对 pure conjunction sound，每个 raw antecedent 都必须真正必要：若某个 `a_i` 没有 dependency path 到 `z`，删掉它以后同一推导仍成立，就会违反 raw semantics。

取一次成功推导 `z` 的 ancestor DAG。它有

- `k` 个必要 raw source vertices；
- `m` 个 derived/gate vertices，其中一个是 `z`；
- 每个 derived vertex indegree 至多二。

底层 ancestor graph 连通，因此至少有

\[
k+m-1
\]

条 edges；而 indegree bound 给出进入 derived vertices 的 edges 至多 `2m`。所以

\[
2m\ge k+m-1,
\]

从而

\[
\boxed{m\ge k-1.}
\]

其中一个 derived vertex 是 `z`，因此至少需要

\[
\boxed{k-2}
\]

个 auxiliary helper labels。

## 3. Depth 下界

parallel derivation depth 零时，每个 raw label 只依赖一个 raw source。使用 binary rules 后，depth `t` 新生成的一个 label 最多依赖

\[
2^t
\]

个 raw sources。

soundness 要求 `z` 真正依赖全部 `k` 个 antecedents，因此

\[
2^d\ge k,
\]

所以

\[
\boxed{d\ge\lceil\log_2k\rceil.}
\]

## 4. Balanced construction

每一轮尽可能成对组合当前 live signals。每一对生成一个 fresh helper，若有一个落单 signal 则直接带到下一轮。一直进行到只剩两个 live signals，再直接组合成 `z`。

每次 pairing 让 live signal 数减少一。把 `k` 个 raw signals 降到一个 output 因而精确使用

\[
\boxed{k-1}
\]

个 binary rules/gates，其中

\[
\boxed{k-2}
\]

个是 helpers，最后一个 gate 输出 `z`。

最大化并行 pairing 后，depth 精确为

\[
\boxed{\lceil\log_2k\rceil.}
\]

executable compiler 已逐个 raw-only seed 检查：在扩展系统中 forward chaining 后投影回 raw alphabet，精确等于 pure k-way closure。

## 5. 精确最优值

在这个 positive binary-helper compiler model 中，balanced construction 同时达到两个下界：

\[
\boxed{
(\max\text{ premise arity},\#\text{helpers},\#\text{rules},d)
=
\left(2,k-2,k-1,\lceil\log_2k\rceil\right).
}
\]

因此 Stage 135 的 sequential compiler 数学上正确，但 depth 不是最优；balanced tree 在保持 minimum helper count 与 rule count 不变的同时，把 depth 从 `k-1` 降到 logarithmic。

## 6. 架构后果

一旦 auxiliary state 被允许，relation-law compilation 本身就是一个多资源优化问题。即使 premise arity 固定为二，execution depth 仍不由它决定；内部 topology 继续产生差异。

raw semantic closure 因此不足以规定 implementation precision。至少还要声明：

- 允许的 auxiliary-state dimension；
- rule fan-in / premise arity；
- rule count / storage；
- parallel derivation depth。

## 7. 前人工作边界

fan-in-two circuit size/depth 下界与 balanced AND tree 属于经典 circuit theory。这里不主张 generic novelty。项目侧价值是把这些经典资源精确放入 future-relative relation-law precision accounting。
