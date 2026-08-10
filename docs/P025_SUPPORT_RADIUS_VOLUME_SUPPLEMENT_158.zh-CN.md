# P025 补充 158 —— Dependency-support radius 与 volume 是两个独立资源

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-state-support-stage155`

## 1. 设置

考虑 acyclic helper dependency graph 中一个 declared helper action `q`，并假设每个 helper gate 至多有两个 helper predecessors。

令

\[
h=H_{supp}(\{q\})
\]

为 Stage157 的 reverse dependency horizon，令

\[
V=|\downarrow q|
\]

为 full dependency support 中的 helper coordinate 数。

相同 radius `h` 可以对应非常不同的 support volume。

## 2. 通用下界

由 horizon `h` 的定义，必存在某个 helper 到 `q` 的 reverse dependency distance 精确为 `h`。从该 helper 到 `q` 的一条最短路径包含

\[
h+1
\]

个不同 helper vertices。

因此

\[
\boxed{V\ge h+1.}
\]

sequential helper chain 取得等号。

## 3. Binary-fan-in 上界

reverse distance 零处只有 action `q`。因为每个 helper 至多有两个 helper predecessors，distance `t` 的 reverse shell 至多有

\[
2^t
\]

个 helpers。

所以

\[
V
\le
\sum_{t=0}^{h}2^t
=
2^{h+1}-1.
\]

即

\[
\boxed{
h+1
\le
V
\le
2^{h+1}-1.
}
\]

perfect binary helper subtree 取得上界。

## 4. 每个 horizon 上两端都 sharp

任意 `h>=0`：

### Lower extreme

取 reverse distance horizon 为 `h` 的 sequential helper chain。support 就是这条 chain 上的 `h+1` 个 helpers：

\[
\boxed{V_{chain}=h+1.}
\]

### Upper extreme

取 raw antecedent 数

\[
k=2^{h+2}
\]

的 perfect balanced compiler 的最高 helper。其 support 是 shell size 为 `1,2,...,2^h` 的 perfect helper tree，所以

\[
\boxed{V_{tree}=2^{h+1}-1.}
\]

两者 radius 完全相同。

## 5. 精确分离样本

当

\[
h=4
\]

时，chain support 只有

\[
V=5,
\]

而 perfect binary support 有

\[
V=31.
\]

随着 `h` 增大，两个 sharp extremes 的比值以指数/线性的速度分离。

## 6. Precision 后果

relation/support horizon 衡量的是**必须跨越多少 dependency layers**；support volume 衡量的是**这些 layers 中有多少 labelled coordinates**。

因此它们是两个不同资源：

\[
\boxed{
\text{support radius}
\neq
\text{support volume}.
}
\]

只保存 dependency depth 的 precision cost model 会严重低估 branching support。

## 7. 前人工作边界

tree branching bounds 与 radius/volume growth 都属于经典 graph/combinatorial facts。这里不主张 generic novelty。P025 提供它们作为不同 future-operation support resources 的 exact interpretation。
