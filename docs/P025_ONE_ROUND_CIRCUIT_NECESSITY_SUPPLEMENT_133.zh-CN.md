# P025 补充 133 —— Derivation depth 为一时 rooted circuits 全部强制存在

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`

## 1. 设置

设 `cl=cl_Omega` 为 Stage 127 的有限 conjunction closure。sound single-head implication basis `B` 由规则

\[
C\Rightarrow b
\]

组成，其中 `b in cl(C)`；若 iterative forward chaining 对任意 seed `S` 都恢复 `cl(S)`，则称其 complete。

Stage 131 已说明：若允许额外 derivation rounds，一些 rooted circuits 可以删除。本补充固定另一个端点：**只允许一轮并行触发**。

## 2. 必要性定理

假设 `B` sound，并且对任意 seed `S`，一次并行 firing 就已经得到 `cl(S)`。

那么

\[
\boxed{
B\text{ 必须包含每一条 rooted closure circuit。}
}
\]

### 证明

任取 rooted circuit

\[
A\Rightarrow b,
\qquad b\notin A.
\]

从 seed `A` 出发，one-round completeness 要求 `b` 在这一轮内被加入。因此 `B` 中存在某条

\[
C\Rightarrow b
\]

在初始 seed 上已经 enabled，所以 `C subseteq A`。

由 soundness，

\[
b\in cl(C).
\]

但 `A` 已是所有强迫 `b` 的 premises 中 inclusion-minimal 的一个，因此只能有 `C=A`。

所以 exact circuit rule `A -> b` 必须属于 `B`。由于 circuit 任意，所有 rooted circuits 都强制存在。证毕。

空 premise circuits（mandatory labels）同样包含在论证内。

## 3. 反方向

Stage 130 已证明完整 rooted-circuit table 对任意 seed 一轮即可恢复 closure。因此在 sound single-head implication representations 中，

\[
\boxed{
\text{完整 rooted-circuit table}
=
\text{唯一 inclusion-minimal one-round complete basis}.
}
\]

任何 one-round complete basis 都必须包含它；额外规则对 one-round completeness 语义上没有必要。

## 4. 为什么 Stage 131 的冗余不构成矛盾

对

\[
a\Rightarrow c\Rightarrow b,
\]

完整 rooted-circuit table 包含

\[
a\Rightarrow c,
\qquad c\Rightarrow b,
\qquad a\Rightarrow b.
\]

删掉 `a -> b` 后 eventual closure 不变，但 required depth 从一轮增加到两轮。所以该规则在不同 future runtime 下具有不同地位：

- depth-one semantics 下强制；
- unrestricted iterative semantics 下冗余。

因此 rule redundancy 本身也是 **future-runtime-relative** 的。

## 5. 精确资源端点

给定允许的最大 derivation depth `D`，令 `s_D(cl)` 表示 worst-case parallel depth 至多 `D` 的 sound complete single-head basis 的最小 rule count。

本补充精确确定 depth-one 端点：

\[
\boxed{
s_1(cl)=\#\{\text{rooted circuits of }cl\}.
}
\]

Stage 131 已给出 `D>1` 时可以严格减小 `s_D` 的样本。

## 6. 架构后果

relation-law compression 无法脱离 declared future execution language 单独评价。同一条 implication 是否可删除，可以仅仅因为允许的 derivation depth 改变而翻转。

因此至少必须分开：

1. semantic closure；
2. rooted/direct relation-law content；
3. 被存储的 iterative basis size；
4. 允许/需要的 derivation depth。

## 7. 前人工作边界

Horn implication bases、forward chaining 与 transitive redundancy 都是经典对象。这里不主张 generic novelty。项目侧价值是精确的 future-runtime-relative precision boundary，以及它对 A2/A4/Foundation layering 的压力测试。
