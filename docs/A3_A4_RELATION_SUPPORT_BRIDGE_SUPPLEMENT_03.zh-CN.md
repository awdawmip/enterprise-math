# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 03

状态：`ACTIVE RESEARCH NOTE`  
范围：fine-support 阈值坐标，以及 A3 partition quotient 面向 A4 MAY/MUST support query 的 task-minimal repair

## 1. 动机

Stage 01 已证明 A3 partition quotient 会因为 signed cancellation 隐藏 fine support；Stage 02/03 又证明 staged support 还可能依赖 intermediate witnesses。

P023 接下来的精确问题是：

> 如果未来 query 需要 fine support 信息，最少必须保留什么？

本文件对 A4 的 **MAY/MUST radius-query language** 给出精确答案。

在 A3 zero-relation quotient `X0` 上使用整数 metric

\[
\rho(x,y)=\min\{r:xR_ry\}.
\]

令 `P={A,B,...}` 为 `X0` 的任意 coarse partition。

## 2. B10 — pairwise MAY/MUST threshold interval

对两个 coarse blocks `A,B`，定义

\[
\boxed{
d^-_{AB}=\min_{x\in A,y\in B}\rho(x,y),
\qquad
d^+_{AB}=\max_{x\in A,y\in B}\rho(x,y).
}
\]

它们都是有限非负整数。

对 radius `r` 定义：

- `MAY_r(A,B)`：`A,B` 之间至少存在一个 fine pair 被 radius-`r` support；
- `MUST_r(A,B)`：`A,B` 之间所有 fine pair 都被 radius-`r` support。

则

\[
\boxed{MAY_r(A,B)\iff d^-_{AB}\le r,}
\]

以及

\[
\boxed{MUST_r(A,B)\iff d^+_{AB}\le r.}
\]

因此，全部 radius 下的 MAY/MUST 行为可以由整数区间

\[
\boxed{I_{AB}=[d^-_{AB},d^+_{AB}]}
\]

完整编码。

该区间具有精确三段语义：

1. `r<d^-`：没有 fine witness；
2. `d^-<=r<d^+`：MAY 为真、MUST 为假；
3. `r>=d^+`：所有 fine pair 都 supported。

定义 **support uncertainty width**

\[
\boxed{W_{AB}=d^+_{AB}-d^-_{AB}.}
\]

它测量 coarse block pair 在多大 radius 区间内存在混合 fine support 行为。

## 3. B11 — task-minimal P023 repair coordinates

令 `q_P` 为 A3 coarse partition state map，固定一个 coarse block pair `A,B` 作为未来 query language 的组成部分。

### 只需要 MUST

真值序列

\[
(MUST_0,MUST_1,MUST_2,\ldots)
\]

完全由 `d^+` 决定；反过来，也能从 MUST 第一次变为 true 的 radius 唯一恢复 `d^+`。

因此，在 quotient partition 等价意义下，

\[
\boxed{(q_P,d^+_{AB})}
\]

就是该 pair 的 all-radius MUST query 的 P023 coarsest one-step repair。

### 只需要 MAY

同理，

\[
\boxed{(q_P,d^-_{AB})}
\]

是 all-radius MAY query 的 coarsest repair。

### 同时需要 MAY/MUST

整数 pair

\[
\boxed{(d^-_{AB},d^+_{AB})}
\]

就是完整 MAY/MUST radius language 的 complete 且 task-minimal coordinate。对整个 coarse partition，则使用相应的有限 threshold matrices。

如果未来只问一个预先固定的 radius，P023-T02 还能继续把 repair 降到那一个 truth bit。这里说的整数 thresholds，是针对**整个 radius family**的最小坐标，而不是单个固定 query。

### 精确 future-safety 条件

原始 quotient `q_P` 对这些 query language 已经 future-safe，当且仅当它所需要的 threshold coordinate 在每个 `q_P` fiber 上恒定。B03 已经证明这种恒定性一般并不成立。

## 4. Coarse A3 support threshold

A3 partition quotient 本身生成 aggregated capacities 和 relation：

\[
m'_A=\sum_{i\in A}m_i,
\qquad
Z'_{AB}=\sum_{i\in A,j\in B}Z_{ij}.
\]

定义其 direct coarse threshold

\[
\boxed{
\bar\rho_{AB}
=
\left\lceil\frac{|Z'_{AB}|}{m'_A m'_B}\right\rceil.
}
\]

由 B02 可得

\[
\boxed{\bar\rho_{AB}\le d^+_{AB}.}
\]

因此定义 **hidden MUST defect**

\[
\boxed{H^+_{AB}=d^+_{AB}-\bar\rho_{AB}\ge0.}
\]

`H^+` 测量 direct coarse support radius 可能把“要保证全部 fine pairs”所需 radius 低估了多少。

## 5. B12 — coarse threshold 与 MAY threshold 不存在一般序关系

`bar rho` 与 `d^-` 之间不存在 universal inequality。

### Coarse threshold 可以小于 MAY threshold

取 unit fine values：

- coarse block `A={0,10}`；
- coarse block `B={5,5}`。

所有 fine cross distance 都是 `5`，所以

\[
d^-_{AB}=d^+_{AB}=5.
\]

但两个 coarse averages 都是 `5`，因此

\[
\bar\rho_{AB}=0.
\]

所以 `bar rho < d^-`。

### Coarse threshold 也可以大于 MAY threshold

取

- `A={0,100}`；
- `B={0}`。

fine 层存在 zero-distance witness，因此 `d^-_{AB}=0`；而 `A` 的 aggregate normalized value 是 `50`，所以

\[
\bar\rho_{AB}=50.
\]

因此 `bar rho > d^-`。

所以 coarse A3 support predicate 既不是 MAY summary，也不是 MUST summary，而是另一个 aggregate observable。

## 6. 精确 sufficiency 陈述

固定一个 coarse pair `A,B`：

- coarse support alone 要精确回答 all-radius MUST，至少必须有 `bar rho=d^+`，并且这个值在相关 coarse-state fiber 上保持不变；
- coarse support alone 要精确回答 all-radius MAY，则至少需要 `bar rho=d^-`，同样还必须满足 fiber-invariance；
- 要同时精确回答 MAY/MUST，则必须在整个 quotient fiber 中保持
  \[
  \bar\rho=d^-=d^+.
  \]

在某一个具体 fine state 上数值恰好相等，只是 observation；P023 的 future safety 始终是“所有被同一个 coarse quotient 表示的 fine states”上的 fiber-level 条件。

这避免一个常见错误：单个例子恰好吻合，不等于 quotient representation 已经对未来 query 闭合。

## 7. 与 A4 MAY/MUST semantics 的关系

A4 已经区分 possible support 与 guaranteed support。B10 证明，在 A3-generated metric subclass 中，这两个逻辑 modality 各自有一个规范有限整数坐标：

\[
MAY\leftrightarrow d^-,
\qquad
MUST\leftrightarrow d^+.
\]

因此 `[d^-,d^+]` 是一个非常紧凑的 bridge object，连接：

- A3 structured relation state；
- A4 modal support semantics；
- A2/P023 task-relative precision repair。

## 8. 与 staged/common-target query 的关系

threshold interval 足够回答一步 MAY/MUST radius questions，但一般不足以回答 staged/common-target queries。Stage 02/03 已经证明 intermediate-state availability 是额外信息。

所以现在 repair hierarchy 可以明确写成：

\[
\text{endpoint MAY/MUST}
\quad\Rightarrow\quad
(d^-,d^+),
\]

而

\[
\text{staged/common-target composition}
\quad\Rightarrow\quad
\text{还需要 interpolation/geodesic witness data（按任务决定）}.
\]

这正是 P023 原则的一个具体实例：合法最小状态由声明好的 future operation language 决定。

## 9. Prior-art discipline

set 间 min/max distance、existential/universal relation lifting、abstract interpretation 的 MAY/MUST semantics、quotient repair 都有成熟前人工作。

当前项目特有的研究目标，是把它们与 A3 weighted relation quotient、Stage 01 生成的 A4 support family，以及 P023 的 task-relative legal-collapse discipline 精确地组合成纯整数有限状态接口。

## 10. Executable reference

bridge reference implementation 新增：

- coarse-partition MAY/MUST threshold matrices `(d^-,d^+)`；
- direct coarse A3 threshold matrix `bar rho`；
- support uncertainty width `W`；
- hidden MUST defect `H^+`；
- B12 两个方向的 regression examples。
