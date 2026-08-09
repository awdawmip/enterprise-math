# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 06

状态：`ACTIVE RESEARCH NOTE`  
范围：任意有限 stage-depth 的 budget frontier 与 future-depth collapse theorem

## 1. 从 two-stage 推广到 `k` stages

Stage 05 处理了两段 support。该构造对任意有限 future depth 都有精确推广。

固定整数 `k>=1`、endpoints `x,z`，以及 budget vector

\[
\mathbf r=(r_1,\ldots,r_k)\in\mathbb N^k.
\]

一个 represented `k`-stage chain 为

\[
x=x_0,x_1,\ldots,x_{k-1},x_k=z.
\]

它的精确 cost vector 是

\[
\boxed{
\mathbf c(x_0,\ldots,x_k)
=(\rho(x_0,x_1),\ldots,\rho(x_{k-1},x_k)).
}
\]

当且仅当 cost vector 在 coordinatewise order 下不超过 `r` 时，该 chain 才能放入预算。

## 2. B21 — `k`-stage Pareto frontier

令 `C^(k)_xz` 为从 `x` 到 `z` 的所有 represented `k`-stage chains 的有限 cost-vector set，并定义

\[
\boxed{
F^{(k)}_{xz}
=\operatorname{Min}_{\preceq} C^{(k)}_{xz}
\subset\mathbb N^k.
}
\]

则

\[
\boxed{
(x,z)\in R_{r_1};\cdots;R_{r_k}
\iff
\exists\mathbf a\in F^{(k)}_{xz}:\mathbf a\preceq\mathbf r.
}
\]

证明与 B13 相同：dominated chain-cost vectors 永远不会改变任何 budget query，因此只保留 Pareto-minimal antichain 即可。

`k=1` 时，frontier 是 singleton：

\[
F^{(1)}_{xz}=\{(\rho(x,z))\}.
\]

`k=2` 时，B21 就是 Stage-05 的 `F_xz`。

## 3. B22 — 固定 future depth 下的 task-minimality

完整 truth function

\[
H^{(k)}_{xz}(\mathbf r)
=1[(x,z)\in R_{r_1};\cdots;R_{r_k}]
\]

唯一确定 `F^(k)_xz`：frontier 正是全部 coordinatewise-minimal true budgets；反过来 frontier 也能重建完整 truth function。

所以，在有限重新编码意义下，

\[
\boxed{F^{(k)}_{xz}}
\]

就是该 endpoint pair 的完整 `k`-stage integer-budget language 的 P023 task-minimal coordinate。

这形成精确的 **future-language depth filtration**：

\[
F^{(1)},F^{(2)},F^{(3)},\ldots
\]

它是 semantic filtration，而不是单纯数值精度层级：depth-one 足够的状态，未必支持 depth-two。

## 4. Triangle simplex boundary

任意 chain cost vector

\[
\mathbf a=(a_1,\ldots,a_k)\in C^{(k)}_{xz}
\]

由重复使用 triangle inequality 得到

\[
\boxed{
\sum_{t=1}^k a_t\ge\rho(x,z).
}
\]

令 `n=rho(x,z)`，定义 weak compositions 构成的 integer simplex layer：

\[
\boxed{
\Sigma_k(n)
=\left\{
(a_1,\ldots,a_k)\in\mathbb N^k:
\sum_t a_t=n
\right\}.
}
\]

`Sigma_k(n)` 中任意两个不同向量在 coordinatewise order 下都互不可比。

## 5. B23 — geodesic future-depth collapse theorem

假设 Stage 03 的 global geodesic condition 成立：

\[
d_{G1}=\rho,
\]

等价地，A4 对所有 two-stage integer budget splits 都 split-complete。

那么对任意 `k>=1`、任意 endpoints `x,z` 与任意 budget vector `r`，

\[
\boxed{
R_{r_1};\cdots;R_{r_k}
=R_{r_1+\cdots+r_k}.
}
\]

等价地，

\[
\boxed{
F^{(k)}_{xz}=\Sigma_k(\rho(x,z)).
}
\]

### 证明

令 `n=rho(x,z)`，选择长度为 `n` 的 unit geodesic。

对任意 weak composition

\[
n=a_1+\cdots+a_k,
\]

在 unit geodesic 上按照累计长度

\[
a_1,\ a_1+a_2,\ldots
\]

切分，即可得到 intermediate vertices，并精确实现 segment costs `(a_1,...,a_k)`。所以 `Sigma_k(n)` 中所有 points 都被 represented。

反过来，任何 represented chain cost 的坐标总和都至少为 `n`。对任意 non-negative vector `c`，只要 `sum c>=n`，都可以在每个 coordinate 的可用容量内分配 `n` 个单位，得到一个 weak composition `a`，满足 `a_t<=c_t`。对应的 exact geodesic cost 会支配掉所有 simplex 上方的 cost，因此 frontier 恰好是 `Sigma_k(n)`。

对于 budget vector `r`，存在一个 `n` 的 weak composition 位于 `r` 下方，当且仅当

\[
n\le\sum_t r_t.
\]

所以 `k`-fold relation product 精确等于 `R_(sum r)`。

## 6. Converse 与精确压缩含义

B23 的 `k=2` 情形就是 Stage-03 split-completeness。因此以下三件事等价：

1. radius-one graph 本征地实现 `rho`；
2. 每个 two-stage budget language 都坍缩为 total budget；
3. 每个有限 stage-depth budget language 都坍缩为 total budget。

所以 geodesicity 不只是一个几何性质，而是一个精确的 **future-depth compression theorem**：

> 一旦证明 geodesicity，支持关系在任意有限复合深度下都只需要 endpoint `rho` 与 future budgets 的总和；无需继续保留 intermediate witness identity 或高维 frontier。

一旦 geodesicity 失败，问题已经会在 depth two 暴露，并且为了精确 staged semantics 必须保留更丰富的 antichain state。

## 7. Canonical frontier size 与 information size 不相同

geodesic frontier 的显式 antichain 大小为

\[
|\Sigma_k(n)|=\binom{n+k-1}{k-1}.
\]

但这**不意味着**最小信息状态必须存储全部这些 points。因为在已证明 geodesic law 后，整个 simplex 可以由单一 scalar `n=rho(x,z)` 生成。

必须严格区分：

- canonical explicit truth-boundary representation 可能很大；
- structural theorem 可以把它大幅压缩。

这正是进取数论希望研究的压缩方式：只有在证明了能够重建全部所需未来行为的规律后，才删除细节。

## 8. 负例

对 represented unit states `{0,2}`，`rho(0,2)=2`，但 midpoint 不存在。

在 depth `k=3`，完整 simplex layer 为

\[
\Sigma_3(2)=
\{(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)\}.
\]

实际 Pareto-minimal 的只有三个 endpoint-stuttering costs：

\[
(2,0,0),\quad(0,2,0),\quad(0,0,2).
\]

包含两个 unit stages 的三种 costs 都因没有 midpoint 而缺失。

所以若没有 geodesic/split-complete theorem，仅知道 `rho=2` 不能重建 depth-three semantics。

## 9. 与 A3 piecewise non-monotonicity 的关系

future-depth collapse theorem 针对的是一个明确声明的 operation language：带 additive integer budgets 的 generated support relations 的复合。

它绝不能被泛化为“精度越高越安全”。A3 piecewise affine 研究已经独立证明：任意 refinement 可能在 selector 仍隐藏时先暴露 branch effects，从而使原本 exact 的 quotient 变得 non-exact。

所以项目级正确原则仍然是：

\[
\boxed{
\text{按照声明的 future semantics 做 refinement，并重新证明 factorization。}
}
\]

## 10. 跨路线后果

### A2/P023

B23 是一个明确例子：structural compatibility theorem 可以把无限族 finite-depth future queries 压缩回一个 scalar state coordinate。

### A4

split-completeness 现在可以理解为对任意有限 support-word composition 的闭合，而不只是一次 two-stage equality。

### A5/P022

满足 `Gamma=0` 的 geometry 自动获得任意有限 stage 下的精确 additive support composition；存在 holes 的 geometry 则需要更丰富的 future state。

### P018

这里给出一个干净例子：“闭合定理成立后，精度细节可以消失”。higher-stage antichain 的需求是一种 semantic defect，而不是本体上必须保存所有 paths。

## 11. Prior-art discipline

relation powers、path metrics、weak compositions 与 Pareto antichains 都是已有数学。当前项目特有的研究目标，是把它们纳入 A3→A4→P023 legal-collapse 链，并把 geodesicity 解释为 finite-future state-compression certificate。

## 12. Executable reference

reference layer 增加 generic `k`-stage Pareto frontier，并在有限例子上检查 simplex-collapse theorem。
