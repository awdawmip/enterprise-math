# P025 补充 155 —— Static state support 与 executable action support 是两种不同 repair

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-state-support-stage155`

## 1. 修复 nonclosed action family 的两条路

Stage 152 已证明任意 visible helper-action set

\[
Q\subseteq P_{gate}
\]

可能依赖 hidden predecessors。Stage 153 通过把**可执行 action subsystem**扩展到 predecessor-closed support `down(Q)` 来修复。

但这不是唯一 possible future contract。

现在假设：

- helper-only phase 中全部 raw antecedents 固定；
- 只有原始 set `Q` 中的 actions 可以 firing；
- `Q` 外 hidden helper statuses 保持静态，除非该 helper 本身也属于 `Q`。

此时 hidden dependencies 可以作为 state inputs 保留，而不必升级成 executable actions。

## 2. 精确 Q-only state support

令 `Pred(q)` 表示 compiler DAG 中 action `q` 的 direct helper predecessors。定义

\[
\boxed{
R_Q
=
Q\cup\bigcup_{q\in Q}\operatorname{Pred}(q).
}
\]

对 global ideal `I`，declared action `q` enabled 当且仅当

\[
q\notin I
\quad\text{且}\quad
\operatorname{Pred}(q)\subseteq I.
\]

这个判断涉及的 helper coordinates 全部属于 `R_Q`。所以每个 `q in Q` 的当前 legality 只依赖

\[
I\cap R_Q.
\]

当 `q` firing 时，唯一改变的 helper coordinate 就是 `q` 自身，它也属于 `R_Q`。declared operation language 又保证 `Q` 外 hidden predecessor statuses 保持不变。

所以每个有限 Q-only action word，包括 prefix legality 与 projected results，都通过

\[
\boxed{I\mapsto I\cap R_Q}
\]

因子化。

由于所有 declared word 带来的 state changes 都留在 `Q subseteq R_Q` 内，一步 factorization 对 word length 归纳即可。

## 3. Hidden direct predecessors 确实必要

在 balanced helper tree 中，每个不属于 Q 的 direct predecessor 都存在 exact finite witness：在保持 `R_Q` 其他坐标相同的合法 ideals 上，只改变该 predecessor 的完成状态，就能翻转对应 declared action 的 enabledness。

所以这些 direct predecessor coordinates 不只是方便的 sufficient set；在当前 label-projection representation 中，它们具有精确 necessity witness。

## 4. Static state support 可以远小于 action closure

对 perfect `k=2^d` compiler，选择一个最高 pre-output helper action。

Stage154 的 autonomous executable action closure 包含整个 helper subtree：

\[
|\downarrow\{q\}|
=
\frac{k}{2}-1.
\]

但 Q-only static state support 只含：

- action `q` 自身；
- 它的两个 direct helper predecessors。

因此对 `k>=8`，

\[
\boxed{
|R_{\{q\}}|=3,
\qquad
|\downarrow\{q\}|=\frac{k}{2}-1.
}
\]

精确例：

\[
\begin{array}{c|c|c}
k & \text{Q-only state support} & \text{autonomous action support}\\
\hline
8 & 3 & 3\\
16 & 3 & 7\\
32 & 3 & 15
\end{array}
\]

perfect 16-way compiler 中若同时声明两个 top actions，static support 只需六个 helper coordinates，而 autonomous executable support 包含全部十四个 pre-output helpers。

## 5. 架构后果

hidden dependency 至少可以用两种不等价方式 repair：

1. **state repair** —— 暴露/保存 prerequisite status，但让它 operationally frozen；
2. **action repair** —— 把 prerequisite actions 也纳入 executable language，并递归关闭 subsystem。

因此

\[
\boxed{
\text{required state support}
\neq
\text{required action support}.
}
\]

哪种 repair 正确，由 future operation envelope 决定，而不是 dependency graph 单独决定。

## 6. 下一阶段边界

小 support `R_Q` 只有在 non-Q helper statuses 静态时才 sufficient。若 environment 可以异步更新 hidden predecessors，contract 会再次变化。Stage 156 应测试 interference 是否会把 support 强迫回 `down(Q)`。

## 7. 前人工作边界

static inputs 与 executable subsystem closure 属于标准 systems/modular-verification reasoning。这里不主张 generic novelty。P025 提供 helper-tree exact separation 与 precision-accounting boundary。
