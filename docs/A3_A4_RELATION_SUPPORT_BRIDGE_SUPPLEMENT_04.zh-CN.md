# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 04

状态：`ACTIVE RESEARCH NOTE`  
范围：完整 two-stage/common-target budget language 的 task-minimal 精确坐标

## 1. 为什么 endpoint thresholds 不够

Stage 04 证明，一步 all-radius MAY/MUST 语义可由标量阈值 `d^-` 和 `d^+` 精确表达。Stage 02/03 同时证明，两阶段 support 还依赖 intermediate states 是否真实存在。

因此，完整 staged query language 需要更丰富、但仍然有限的坐标。

继续在 A3 zero-relation quotient `X0` 上使用整数 metric

\[
\rho(x,z)=\min\{r:xR_rz\}.
\]

固定 ordered endpoints `x,z`。每一个可能的 intermediate state `y` 都对应一个 two-stage budget cost

\[
\boxed{c_y(x,z)=(\rho(x,y),\rho(y,z))\in\mathbb N^2.}
\]

## 2. B13 — staged budget Pareto frontier

定义

\[
C_{xz}=\{c_y(x,z):y\in X_0\}.
\]

在 `N^2` 上使用 coordinatewise order：

\[
(a,b)\preceq(r,s)\iff a\le r\text{ 且 }b\le s.
\]

定义有限 Pareto-minimal antichain

\[
\boxed{F_{xz}=\operatorname{Min}_{\preceq}(C_{xz}).}
\]

则对所有整数预算 `(r,s)`，

\[
\boxed{
(x,z)\in R_r;R_s
\iff
\exists(a,b)\in F_{xz}:a\le r,\ b\le s.
}
\]

### 证明

按照定义，`(x,z) in R_r;R_s` 当且仅当存在 represented intermediate `y` 使

\[
\rho(x,y)\le r,
\qquad
\rho(y,z)\le s.
\]

这正是 `C_xz` 中某个 cost point 位于 `(r,s)` 下方。有限 cost set 中，每个 point 的下方总能找到一个 Pareto-minimal point，因此删除 dominated costs 不会改变任何 query 的答案。

所以 `F_xz` 的 upward closure 与所有 two-stage budget queries 的完整 truth set 完全相同。

## 3. B14 — frontier 是完整 two-stage language 的 task-minimal 坐标

定义

\[
H_{xz}(r,s)=1[(x,z)\in R_r;R_s].
\]

完整 truth function `H_xz` 可以唯一恢复 `F_xz`：`F_xz` 恰好是 `H_xz` 第一次变为 true 的 coordinatewise-minimal budget pairs。

反过来，B13 证明 `F_xz` 可以重建任意 `(r,s)` 上的 `H_xz`。

因此，在编码等价意义下，

\[
\boxed{F_{xz}}
\]

就是 endpoint pair 的**完整 two-stage integer-budget query language** 的 P023 coarsest repair coordinate。

这把 Stage 04 的 repair hierarchy 继续向前推进：

- 一个固定 `(r,s)` query：一个 truth bit；
- 全部 one-step radii：一个 scalar threshold（根据 modality 为 `d^-` 或 `d^+`）；
- 全部 two-stage budget pairs：一个有限 Pareto antichain `F_xz`；
- unrestricted future operation words：进入一般 P023 compatible-quotient closure。

所需状态随声明的 future language 增长，而不是因为抽象地要求“保存全部 fine detail”而增长。

## 4. B15 — triangle lower boundary

对任意 `(a,b) in F_xz`，metric 三角不等式都给出

\[
\boxed{a+b\ge\rho(x,z).}
\]

令 `n=rho(x,z)`。选择 `y=x` 与 `y=z` 分别得到

\[
(0,n),\qquad(n,0).
\]

二者都是 Pareto-minimal。因此任何 frontier 都包含两个 endpoint costs；内部 frontier point 则表示真正有用的 represented intermediate state。

定义 exact anti-diagonal

\[
G_n=\{(k,n-k):0\le k\le n\}.
\]

## 5. B16 — geodesic/split-complete frontier theorem

固定 endpoint pair `x,z`，令 `n=rho(x,z)`。以下条件等价：

1. exact total distance 的每一种整数 budget split 都可以实现；
2. 每个 `k=0,...,n` 都存在 represented state `y_k`，满足
   \[
   \rho(x,y_k)=k,
   \qquad
   \rho(y_k,z)=n-k;
   \]
3. staged Pareto frontier 精确等于
   \[
   \boxed{F_{xz}=G_n.}
   \]

如果对所有 endpoint pairs 都成立，就等价于 B08 的 global split-completeness/geodesic condition。

### 为什么 geodesic 情形不会留下额外 Pareto points

任取 intermediate cost `(a,b)`。三角不等式给出 `a+b>=n`。可选择整数

\[
k\in[\max(0,n-b),\min(a,n)].
\]

若 endpoint pair 是 geodesic，则 `(k,n-k)` 被真实表示，并满足

\[
(k,n-k)\preceq(a,b).
\]

所以 anti-diagonal 上方的任何 cost 都会被支配；唯一 Pareto-minimal costs 就是 exact geodesic splits。

## 6. Stage-05 defect language

frontier 比标量 geodesic defect `Gamma` 暴露更丰富的结构。

### Missing exact splits

定义

\[
\boxed{M_{xz}=G_{\rho(x,z)}\setminus F_{xz}.}
\]

`M_xz` 精确记录哪些 zero-slack budget split 缺少 represented intermediate witness。

### Detour frontier points

任何满足

\[
a+b>\rho(x,z)
\]

的 frontier point 都是 nondominated **detour witness**：它对某些 staged query 有用，但必须付出正的 total slack。

所以 `F_xz` 同时区分：

- exact geodesic interpolation；
- missing exact splits；
- 仍有价值但需要额外预算的 detours。

`Gamma` 回答 global unit-path question；`F_xz` 回答每一个 two-stage budget query。

## 7. 例子

### `{0,1,2}`

对 endpoints `0,2`，`rho=2`，三个 represented intermediate choices 给出

\[
F_{0,2}=\{(0,2),(1,1),(2,0)\}=G_2.
\]

### `{0,2}`

只有 endpoint witnesses：

\[
F_{0,2}=\{(0,2),(2,0)\}.
\]

因此 missing split set 为

\[
M_{0,2}=\{(1,1)\}.
\]

### 连通但 non-geodesic 的例子

取相同 capacity `10`，totals 为 `(0,7,14,20)`。它们对应 normalized positions `0,0.7,1.4,2`，但所有表示与运算仍是整数。

对 endpoints `0,2`，direct integer relation distance 是 `rho=2`，而 radius-one graph path 需要三条边。两个内部 states 的 costs 分别为 `(1,2)` 与 `(2,1)`，都被 endpoint costs 支配，因此

\[
F_{0,2}=\{(0,2),(2,0)\}.
\]

exact `(1,1)` split 仍然缺失，虽然 unit graph 是连通的。

这区分了 finite detour 与 complete disconnection。

## 8. 跨路线后果

### A2 / P023

这是一个具体的 task-minimal repair hierarchy。完整 two-stage support budgets 的规范状态并不一定需要完整 witness set，而是 witness costs 的 Pareto frontier。任何更粗编码只有在每个 quotient fiber 上保留相同 frontier/truth function 时才合法。

### A4

common-target composition 在 A3-generated metric subclass 中得到一个紧凑、精确的 budget signature。

### A5 / P022

geometry-specific holes 现在可以通过 missing anti-diagonal splits 与 detour frontiers 分类，而不只是看 graph connectivity 或 shell counts。

### A3

bridge 当前形成三个逐渐更丰富的 observables：

\[
\rho
\quad\to\quad
(d^-,d^+)
\quad\to\quad
F_{xz}.
\]

它们分别适用于不同的 declared future language。

## 9. Prior-art discipline

Pareto frontier、`N^2` 的 upward-closed sets、multiobjective shortest-path costs、antichain representation 都属于已有数学。本项目不主张这些一般工具本身的新颖性。

当前项目特有的贡献候选，是从 A3-generated A4 support family 精确推导这一 antichain repair coordinate，并把它放入 P023 的 task-relative legal-collapse hierarchy。

## 10. Executable reference

新增 reference module 计算：

- Pareto-minimal budget antichains；
- 所有 endpoint pairs 的 `F_xz`；
- 从 frontier 精确回答 staged queries；
- missing exact splits `M_xz`；
- geodesic anti-diagonal criterion。
