# P025 补充 135 —— Direct premise arity 可以用 derivation depth 交换

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. 可扩展 synergy family

固定彼此独立的 raw antecedents

\[
a_1,\ldots,a_k,
\qquad k\ge2,
\]

最终 root `z`，以及 helper labels

\[
e_2,\ldots,e_{k-1}.
\]

使用 binary implication chain

\[
a_1a_2\Rightarrow e_2,
\]

\[
e_{j-1}a_j\Rightarrow e_j
\qquad(3\le j\le k-1),
\]

以及

\[
e_{k-1}a_k\Rightarrow z.
\]

当 `k=2` 时，唯一规则就是 `a_1 a_2 -> z`。

记这些规则生成的 closure 为 `cl_k`。

## 2. k-ary rooted direct circuit 仍然存在

raw antecedent set

\[
A_k=\{a_1,\ldots,a_k\}
\]

能够强迫 `z`。并且删掉任意一个 raw antecedent，helper chain 都会在到达 final root 以前断裂。因此

\[
\boxed{A_k\Rightarrow z}
\]

本身就是一个 premise arity 为 `k` 的 rooted minimal implication。

所以 Stage 130 的 direct circuit horizon 满足

\[
\boxed{h_{\rm circ}(cl_k)\ge k.}
\]

再由 Stage 133，任意 depth-one sound complete single-head representation 都必须包含这条 direct `k`-ary rule。

## 3. Binary iterative compilation

上面的 helper basis 恰有

\[
\boxed{k-1}
\]

条规则，每条 premise arity 都等于二；从 raw seed `A_k` 出发，helper states 每轮生成一层，final root 精确在

\[
\boxed{k-1}
\]

轮后出现。

因此同一 closure 拥有 iterative presentation

\[
\boxed{
(\text{max premise arity},\text{rule count},\text{raw-seed depth})
=(2,k-1,k-1).
}
\]

而它的 direct one-round law 中仍存在不可约 arity-`k` circuit。

## 4. 无界 arity/depth 交换

随着 `k` 增大，direct one-round semantics 所需要面对的最大 premise arity 无界增长；而 iterative basis 的 premise arity 始终固定为二。

所以

\[
\boxed{
\text{一旦允许 iterative helper computation，direct relation-law arity 就不是 semantic closure 的静态不变量。}
}
\]

可以通过更深的 future computation 换取更低的 stored rule arity。

## 5. 下一阶段必须保留的边界

从 arity `k` 降到 arity 二，使用了**额外 helper labels**。因此内部 law/state alphabet 实际发生了扩展，虽然目标 raw conjunction consequence 被保留。

Stage 136 必须进一步拆开：

- derivation depth；
- rule premise arity；
- auxiliary/helper-state dimension。

否则本补充会被误读成“只增加 depth 就总能降低 arity”。

## 6. 前人工作边界

用 binary helper gates 编译 multi-input conjunction 属于经典 circuit/Horn logic。这里不主张 generic novelty。P025 的价值是精确拆分这些 precision resources，并指出 direct circuit arity 与 iterative rule arity 位于不同 runtime/state contracts 下。
