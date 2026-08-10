# P025 补充 140 —— 单一 raw-state fiber 内的精确 progress precision

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. 固定 raw projection

使用 sequential `k`-way helper compiler，并选择 raw seed

\[
S_{k-1}=\{a_1,\ldots,a_{k-1}\},
\]

令最后一个 antecedent `a_k` absent。

raw output 永远无法触发，所以整个执行过程中 raw projection 始终精确等于 `S_(k-1)`。但 internal helper chain 会依次推进：

\[
\varnothing,
\quad e_2,
\quad e_2,e_3,
\quad\ldots\quad,
 e_2,\ldots,e_{k-1}.
\]

`e_(k-1)` 生成后，由于 `a_k` absent，状态稳定。

## 2. 精确 fiber cardinality

这条 execution trace 中精确有

\[
\boxed{k-1}
\]

个合法 internal states，并且全部满足

\[
\boxed{\pi(T)=S_{k-1}.}
\]

所以一个 raw-projection fiber 内可以包含任意长的合法 runtime-memory chain。

## 3. Remaining-round future 分离全部状态

把 trace states 记为 `t=0,...,k-2`。从状态 `t` 出发，到稳定以前剩余的 helper-update rounds 精确为

\[
\boxed{k-2-t.}
\]

这些值两两不同。因此，对 declared future language

> 返回到 internal stability 还剩多少轮，

全部 `k-1` 个 states 都必须保持语义可区分。

一个自然的 exact repair coordinate 就是 progress index `t`，等价地也可保存 remaining rounds。

## 4. Endpoint/runtime collapse gap

同一个 fiber 因此呈现最大反差。

### Raw saturated endpoint language

全部 `k-1` 个 transient states 拥有同一个 raw endpoint，可以 collapse 成一个 class。

### Internal runtime-progress language

全部 `k-1` 个 states 必须保持不同。

所以在同一个 raw semantic fiber 内，

\[
\boxed{
\text{endpoint helper precision}=0,
\qquad
\text{runtime progress precision}=k-1\text{ 个离散层级}.
}
\]

## 5. 架构后果

internal state 对 precision 的贡献不由 storage dimension 本身决定。同样一批 helper coordinates，在一个 future 下可以全部 quotient，在另一个 future 下却全部分离。

这是此前 operation-language 原理的一个 state-level 精确版本：

\[
\boxed{
\text{future language 可以在 raw observable state 完全不变化时，在一个 fiber 内生成新的 precision。}
}
\]

## 6. 前人工作边界

progress counters、remaining-time sufficient state 与 deterministic execution traces 都是经典对象。这里不主张 generic novelty。项目侧贡献是一个 exact finite family：同一 endpoint cache 在更强 runtime future 下变成 `k-1` 层级的 runtime memory coordinate。
