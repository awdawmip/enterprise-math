# P025 补充 141 —— 跨任务 helper cache 必须 invalidation

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. 合法 cache 也会变 stale

在一次合法初始化的 computation 内，Stage 139 已证明 saturated helper coordinates 是确定性 derived cache。但这并不意味着 raw input 被替换成新任务后，同一 cache 可以直接保留。

对 sequential k-way compiler，helper `e_j` 表示已经计算完成的 raw prefix

\[
a_1\wedge\cdots\wedge a_j.
\]

固定任意

\[
2\le j\le k-1.
\]

## 2. 精确 stale-helper 反例

选择前一 raw job

\[
S_{old}=\{a_1,\ldots,a_j\}.
\]

合法 saturation 会生成 `e_j`。

然后启动一个新的 raw job，只包含 suffix

\[
S_{new}=\{a_{j+1},\ldots,a_k\},
\]

但保留上一任务留下的 stale helper `e_j`。

此时 internal seed 为

\[
T=\{e_j\}\cup S_{new}.
\]

sequential helper chain 会从 `e_j` 继续运行，最终推出

\[
z.
\]

然而新 raw job 缺少全部 prefix antecedents `a_1,...,a_j`，所以 pure raw conjunction 不应触发：

\[
cl_{raw}(S_{new})=S_{new}.
\]

因此

\[
\boxed{
\pi(F_{ext}^*(T))\ne cl_{raw}(S_{new}).
}
\]

每一个 helper 都存在这样的 witness。

## 3. 精确 fixed-reset 下界

设跨任意 jobs 的 lifecycle policy 只能采用一个固定 helper deletion set，并且没有 version tag 或 revalidation mechanism。

若某个 helper `e_j` 没有被清除，就可以用上面的构造：前一任务令它合法变 true，后一任务提供恰好的 suffix，使 stale value 生成错误 output。

所以每一个 helper 都必须属于 reset set：

\[
\boxed{
\text{minimum fixed helper-clear count}=k-2.
}
\]

清除全部 helpers 又由 Stage 138 的 raw-initialization simulation theorem 保证 sufficient。

## 4. Initialization legality 还不够

Stage 138 要求 raw computation 开始时 helpers absent。Stage 141 说明这不是一次性的 startup convention，而是一个**lifecycle invariant**。

每当 raw inputs 被替换时，implementation 必须至少做以下之一：

1. 清除失效 helper state；
2. 针对新 raw inputs 重新验证/重算；
3. 保存额外 provenance/version information，阻止 stale helpers 被消费。

所以合法 hidden state 还需要 maintenance operation language。

## 5. Precision 后果

完整 auxiliary-state contract 现在至少有三层：

- **initialization precision** —— 哪些 internal states 被允许作为初态；
- **runtime progress precision** —— 一次 computation 中哪些 transient helper states 必须保持不同；
- **lifecycle validity precision** —— 外部/raw state 改变后，哪些 retained helpers 仍然有效。

一个在某个 saturated endpoint 上语义冗余的 cache，仍可能对未来 reset/invalidation operations 施加义务。

## 6. 前人工作边界

cache invalidation、stale-state hazards、versioning 与 lifecycle invariants 都是经典 systems 思想。这里不主张 generic novelty。P025 提供 exact finite counterexample family，并把 cache invalidation 放进与 state/operation legality 相同的 future-relative precision framework。
