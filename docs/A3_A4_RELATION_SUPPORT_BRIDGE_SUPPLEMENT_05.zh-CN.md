# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 05

状态：`ACTIVE RESEARCH NOTE`  
范围：完整 two-stage budget language 在 coarse partition 上的精确 MAY/MUST 坐标

## 1. 设置

Stage 05 已经为每个 fine endpoint pair `x,z` 定义了有限 Pareto frontier

\[
F_{xz}\subset\mathbb N^2,
\]

其 upward closure 精确等于

\[
(x,z)\in R_r;R_s
\]

的全部 truth region。

令 `P={A,B,...}` 为 A3 zero-relation quotient `X0` 的一个 partition。

对 coarse blocks `A,B` 定义 staged modalities：

- `MAY_(r,s)(A,B)`：至少存在一个 fine endpoint pair `x in A, z in B`，在预算 `(r,s)` 内有 two-stage witness；
- `MUST_(r,s)(A,B)`：每一个 fine endpoint pair `x in A, z in B` 都分别存在某个 intermediate witness，并且都能在同一预算 `(r,s)` 内完成。

MUST 中不同 endpoint pairs 可以使用不同的 intermediate `y`；它要求 budget 对所有 endpoint pairs 都有效，而不是要求一个共同 `y` 同时服务所有 endpoints。

## 2. Upward-closed budget sets 的 frontier algebra

对有限 frontier `F`，记

\[
\uparrow F
=
\{(r,s):\exists(a,b)\in F,\ a\le r,\ b\le s\}.
\]

### Union

对有限多个 frontiers `F_i`，

\[
\bigcup_i\uparrow F_i
=
\uparrow\operatorname{ParetoMin}\left(\bigcup_iF_i\right).
\]

### Intersection

对两个 frontiers `F,G`，定义 coordinatewise join

\[
(a,b)\vee(c,d)=(\max(a,c),\max(b,d)).
\]

则

\[
\boxed{
(\uparrow F)\cap(\uparrow G)
=
\uparrow\operatorname{ParetoMin}\{p\vee q:p\in F,q\in G\}.
}
\]

证明：一个 budget 同时支配 `F` 中某个 `p` 与 `G` 中某个 `q`，当且仅当它支配 `p vee q`。迭代该公式即可得到任意有限 family 的精确 intersection frontier。

## 3. B17 — coarse staged MAY frontier

定义

\[
\boxed{
F^-_{AB}
=
\operatorname{ParetoMin}
\bigcup_{x\in A,z\in B}F_{xz}.
}
\]

则

\[
\boxed{
MAY_{(r,s)}(A,B)
\iff
\exists p\in F^-_{AB}:p\preceq(r,s).
}
\]

因此 `F^-` 就是完整 all-budget staged-MAY coordinate。

## 4. B18 — coarse staged MUST frontier

对每个 fine endpoint pair `(x,z) in A×B`，选择一个 frontier point

\[
p_{xz}\in F_{xz}.
\]

取所有这些 points 的 coordinatewise join：

\[
\bigvee_{x,z}p_{xz}
=
\left(
\max_{x,z}p^{(1)}_{xz},
\max_{x,z}p^{(2)}_{xz}
\right).
\]

定义

\[
\boxed{
F^+_{AB}
=
\operatorname{ParetoMin}
\left\{
\bigvee_{x\in A,z\in B}p_{xz}
:
p_{xz}\in F_{xz}
\right\}.
}
\]

则

\[
\boxed{
MUST_{(r,s)}(A,B)
\iff
\exists p\in F^+_{AB}:p\preceq(r,s).
}
\]

所以 `F^+` 是完整 all-budget staged-MUST coordinate。

直接枚举所有组合可能具有较高组合复杂度。这里给出的是 exact reference specification，而不是最终优化算法；实际计算可以逐个做 frontier intersection，并在每一步后立刻 Pareto prune。

## 5. B19 — P023 task-minimality

完整 MAY truth function 在 `N^2` 上唯一确定 `F^-_AB`：它就是 MAY 第一次为 true 的 coordinatewise-minimal budgets。同理，完整 MUST truth function 唯一确定 `F^+_AB`。

因此，在有限重新编码意义下，

\[
\boxed{F^-_{AB}}
\]

是完整 staged-MAY budget language 的 P023 coarsest repair coordinate；

\[
\boxed{F^+_{AB}}
\]

则是 staged-MUST 的对应 coarsest coordinate。

如果未来同时需要两种 modality，则保留 `(F^-_AB,F^+_AB)`。

这正是 Stage 04 的二维升级：

\[
d^-_{AB},d^+_{AB}
\quad\longrightarrow\quad
F^-_{AB},F^+_{AB}.
\]

## 6. MUST 蕴含 MAY，但两个 frontiers 不必相同

对任何 budget pair 都有

\[
MUST_{(r,s)}(A,B)\Longrightarrow MAY_{(r,s)}(A,B),
\]

因此

\[
\uparrow F^+_{AB}\subseteq\uparrow F^-_{AB}.
\]

这并不要求两个 frontier points 之间存在一一对应。

两个 upward-closed regions 之间的差，就是 Stage-04 uncertainty interval 的 staged analogue：在这些 budgets 下，有些 fine endpoint pairs 可以完成 staged support，但并非全部都可以。

## 7. 例子：coarse block `{0,1}` 对 `{2}`

使用 unit states `{0,1,2}` 及 geodesic metric。

fine endpoint frontiers 为

\[
F_{0,2}=\{(0,2),(1,1),(2,0)\},
\]

\[
F_{1,2}=\{(0,1),(1,0)\}.
\]

取 coarse blocks

\[
A=\{0,1\},\qquad B=\{2\}.
\]

MAY 由更容易的 fine pair 控制：

\[
\boxed{F^-_{AB}=\{(0,1),(1,0)\}.}
\]

MUST 必须同时满足两组 endpoint pairs，因此

\[
\boxed{F^+_{AB}=\{(0,2),(1,1),(2,0)\}.}
\]

这正是 one-step thresholds `d^-=1`、`d^+=2` 的 staged counterpart。

## 8. B20 — one-step endpoint thresholds 无法决定 staged semantics

考虑两个 systems，它们声明的 endpoints direct distance 都是 `rho=2`：

1. represented states `{0,1,2}`；
2. represented states `{0,2}`。

在两个系统里，对 singleton coarse endpoint blocks 都有

\[
d^-=d^+=2.
\]

所以全部 one-step all-radius MAY/MUST queries 完全相同。

但 two-stage frontiers 不同：

\[
\{0,1,2\}:\quad F=\{(0,2),(1,1),(2,0)\},
\]

\[
\{0,2\}:\quad F=\{(0,2),(2,0)\}.
\]

因此

\[
\boxed{
(d^-,d^+)\text{ 对 staged/common-target semantics 不充分。}
}
\]

这是一个信息分离定理，不只是某个实现不佳的例子。

## 9. 跨路线后果

### A2/P023

最小 repair 随 future-language depth 改变。一个对 endpoint queries 闭合的 quotient，完全可能在所有 one-step thresholds 都保留的情况下，对 staged queries 仍然不闭合。

### P018

precision 不能只按“保存了多少个坐标”排序。两个大小相近的 summaries 可能支持不同的 future languages；semantic closure 才是门槛。

### A4/E001

在 A3-generated subclass 中，一个 coarse object pair 的 staged MAY/MUST semantics 有规范有限 antichain representation。

### A5/P022

geometry 可以比较的不只是 direct distance，还可以比较 coarse staged frontier 的复杂度与形状，从而暴露相同 endpoint distance 下不同的 interpolation structure。

## 10. Prior-art discipline

upward-closed sets 的 antichain representation、Pareto frontier 的 union/intersection 都是成熟工具。当前项目特有的结果，是把它们精确放到 A3、A4 与 P023 之间，作为 task-relative repair coordinates。

## 11. Executable reference

新增 reference module 实现：

- upward-closed frontier union；
- 用 coordinatewise joins + Pareto pruning 精确求 intersection；
- coarse staged MAY frontier；
- coarse staged MUST frontier；
- exact query evaluation。
