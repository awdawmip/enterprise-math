# P025 补充 145 —— Perfect binary compiler 的精确 asynchronous progress state count

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. Perfect binary family

设

\[
k=2^d,
\qquad d\ge2,
\]

并使用 Stage 137 的 perfect balanced binary conjunction compiler。在 output root `z` 触发以前，helper dependency poset 由两个互不相交、高度为 `d-1` 的 perfect binary gate subtrees 构成。

Stage 144 已证明 asynchronous helper-progress states 精确等于该 poset 的 order ideals。

## 2. 单个 gate subtree 的 ideal-count recurrence

设 `F_h` 表示高度 `h` 的 perfect binary subtree 的 internal-gate poset 的 ideal 数，其中包含该 subtree 的 root gate。

当 `h=1`，subtree 只有一个 gate，所以

\[
\boxed{F_1=2.}
\]

当 `h>=2`，按 subtree root 是否出现分类。

### Root absent

左右两个 child gate subtrees 相互独立，因此有

\[
F_{h-1}^2
\]

种选择。

### Root present

若 ideal 包含 root，就必须包含它下面的全部 gate ancestors，也就是整个 subtree。只有一种。

因此

\[
\boxed{
F_h=F_{h-1}^2+1.
}
\]

前几项为

\[
2,\ 5,\ 26,\ 677,\ldots
\]

## 3. 完整 pre-output asynchronous state count

对完整 `k=2^d` compiler 去掉 output root `z`，剩余 helper poset 是两个高度 `d-1` gate subtrees 的 disjoint union，所以

\[
\boxed{
N_{async}(2^d)=F_{d-1}^2.
}
\]

精确值包括

\[
\boxed{
N_{async}(4)=4,
\quad
N_{async}(8)=25,
\quad
N_{async}(16)=676,
\quad
N_{async}(32)=458329.
}
\]

## 4. Width 与 synchronous 对照

最宽 antichain 是第一层 helper gates，每一对 raw inputs 对应一个 gate。因此

\[
\boxed{
\operatorname{width}(P_{gate})=\frac{k}{2}.
}
\]

相反，deterministic synchronous pre-output execution 每个 parallel level 只有一个 helper state，包括初始空 helper 集：

\[
\boxed{
N_{sync}(2^d)=d=\log_2 k.
}
\]

所以 synchronous path states 与 asynchronous ideal states 的精确比较为

\[
\boxed{
\log_2 k
\quad\text{versus}\quad
F_{\log_2 k-1}^2.
}
\]

## 5. 架构后果

巨大的 state-count gap 完全由 scheduler freedom 生成。raw input、compiler DAG、helper count、rule set 与 saturated endpoint 全部固定不变。

因此 runtime implementation 不能只从 circuit size/depth 推出所需 state precision；还必须包含 concurrency/scheduling language。

同一个 compiler 在 deterministic schedule 下可以是 low-state，在 permissive asynchronous schedule 下则成为 high-state。

## 6. 前人工作边界

rooted tree 的 ideal counting 与 asynchronous configurations 属于经典 enumerative order/concurrency theory。这里不主张 generic novelty。P025 提供 perfect-compiler specialization 及其 precision interpretation。
