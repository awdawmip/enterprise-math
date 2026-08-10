# P025 补充 144 —— Scheduler freedom 把 helper progress 升级成 ideal lattice

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. 同一个 compiler，不同 scheduler language

固定 Stage 137 的 balanced binary helper compiler，并假设全部 raw antecedents 已经存在，而所有 helpers 与 output `z` 初始 absent。

在 `z` 触发以前，比较两种 internal operation languages：

1. **synchronous parallel** —— 每轮触发全部当前 enabled helper gates；
2. **asynchronous** —— 每一步可以任选一个当前 enabled helper gate 触发，然后继续。

semantic raw input 与 implication graph 完全相同，只改变 scheduler freedom。

## 2. Gate-dependency poset

令 `P_gate` 为 helper gates 上的有限 poset，并定义

\[
u\le v
\]

当 helper `u` 是 compiler DAG 中 helper `v` 的 ancestor prerequisite。

若 helper `v` 已经完成，那么它的所有 helper ancestors 必然已经完成。因此任意 asynchronously reachable completed-helper set 都是 `P_gate` 的 order ideal。

## 3. 反方向 reachability

任取 `P_gate` 的 order ideal `I`。选择一个与 dependency order 一致的 `I` 的 linear extension，并按这个顺序逐个触发 helpers。

所有 raw leaf prerequisites 已经存在；而每次轮到某个 helper 时，它的所有 helper predecessors 都已经在 completed set 中，所以该步 enabled。

因此任意 ideal 都可达。

从而得到精确等式

\[
\boxed{
\{\text{asynchronously reachable helper-progress states}\}
=
J(P_{gate}).
}
\]

这不是上界，而是 exact equality。

## 4. Antichain-boundary precision 再次出现

每个 ideal 都由其 maximal antichain boundary 唯一表示。因此 worst-case boundary generator 数为

\[
\boxed{\operatorname{width}(P_{gate}).}
\]

所以 Stage113 的 `rank -> antichain boundary` 转变，在这里以**runtime scheduling effect** 的形式重新出现，而不是来自外部给定的 observation geometry。

## 5. 精确样本

### 四元 balanced conjunction

有两个彼此独立的第一层 helpers。helper poset 是二元素 antichain：

\[
\operatorname{width}=2,
\qquad
|J(P_{gate})|=4.
\]

而 synchronous pre-output execution 只访问两个 helper states：空集，然后同时出现两个 helpers。

### 八元 balanced conjunction

六个 helpers 构成两个彼此独立的 `V` 型子树。helper-poset width 为四，并且

\[
\boxed{|J(P_{gate})|=25.}
\]

synchronous pre-output execution 只访问三个 helper states，而 asynchronous scheduling 允许全部 25 个 ideals。

## 6. 架构后果

scheduler freedom 本身就是 state-precision generator。

在 raw state、implication rules、helper coordinates 与 endpoint semantics 全部相同的情况下：

- deterministic synchronous scheduling 产生一条 progress path；
- asynchronous scheduling 产生一个合法 progress states 的 ideal lattice。

因此 runtime state type 不能由 compiler graph 单独推出，它依赖 declared internal operation language。

这是 P025 helper-state program 与此前 A2/A4/Stage113 poset-boundary precision program 的直接桥。

## 7. 前人工作边界

dependency posets、asynchronous event structures、order ideals 与 topological firing orders 都是经典 concurrency/order theory。这里不主张 generic novelty。P025 提供 exact compiler-level specialization 与 precision-architecture connection。
