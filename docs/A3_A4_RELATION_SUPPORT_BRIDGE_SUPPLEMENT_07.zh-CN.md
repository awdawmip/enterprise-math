# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 07

状态：`ACTIVE RESEARCH NOTE`  
范围：整个 generated-support language 通过整数 metric 的精确 factorization，以及它相对于更丰富 A3 operations 的边界

## 1. 压缩问题

前面各阶段一直使用整数 metric

\[
\rho(x,y)=\min\{r:xR_ry\}
\]

作为 A3→A4 的 derived object。现在提出更强的 P023 问题：

> 对哪一整类 future operation language，`rho` 本身已经是 complete coarse state？

对 generated support language，可以给出精确答案。

## 2. 定义 support language

令 `L_supp` 为从 primitive radius relations

\[
R_r=\{(x,y):\rho(x,y)\le r\},
\qquad r\in\mathbb N
\]

出发，通过有限次 relational composition 生成的 expression language。即使再允许有限 union、intersection 与 converse，下面定理仍然成立，因为这些都只是对由 primitive `R_r` 已经确定的有限 relations 做操作。

labeled quotient-state set `X0` 是状态的一部分，因为该 language 允许询问具体 endpoint classes。

## 3. B24 — metric factorization theorem

任何 `L_supp` expression 都由

\[
\boxed{(X_0,\rho)}
\]

唯一决定。

### 证明

任意 radius `r` 下，`R_r` 可直接通过 threshold rule 恢复：

\[
(x,y)\in R_r\iff\rho(x,y)\le r.
\]

有限 relation composition / union / intersection / converse 完全可以由这些有限 relations 本身计算。因此，对任意 support-language expression 做结构归纳，只使用 `(X0,rho)` 就能重建其精确结果。

所以映射

\[
(m,c,Z)
\longmapsto
(X_0,\rho)
\]

对整个 generated-support language 是 future-safe quotient。

一旦 future-language boundary 已经明确声明，就不再需要 exact `Z_ij`、capacity、total、rational density 或 hidden real completion。

## 4. B25 — full primitive support language 的 information equivalence

反过来，完整 primitive support truth family 可以精确恢复 `rho`：

\[
\boxed{
\rho(x,y)=\min\{r:(x,y)\in R_r\}.
}
\]

所以 `(X0,rho)` 与完整 labeled primitive support family `{R_r}` 在有限重新编码意义下包含相同信息。

因此，如果 future language 包含所有 labeled primitive radius queries，`rho` 不只是 sufficient，而是该 language 的规范 information-complete coordinate。

这是 P023 层面的 semantic information-content 陈述，不是关于最少 machine bits 或最优 serialization 的声明。

## 5. B26 — nested legal-collapse hierarchy

现在得到一条明确的逐级 task-specific state 链：

\[
\boxed{
(m,c,Z)
\longrightarrow
(X_0,\rho)
\longrightarrow
\text{task-specific thresholds/frontiers}
}
\]

每个箭头都有不同 proof obligation。

### Full A3 relation-state language

如果未来 operations 需要 exact signed weighted relations、capacities、partition aggregation 或 reconstruction，则继续保留 `(m,c,Z)`，或另一个已证明能重建它的 representation。

### Full generated-support language

由 B24，`(X0,rho)` 已经 exact。

### Restricted endpoint/staged query language

Stage 04–06 允许进一步压缩为：

- scalar thresholds；
- coarse MAY/MUST intervals；
- two-stage Pareto frontiers；
- fixed-depth Pareto antichains；
- 若 geodesic，则任意 finite support depth 再重新坍缩为 endpoint `rho`。

因此 legal compression 是一条由 declared future language 索引的 ladder。

## 6. B27 — 负边界：`rho` 不是 full A3 quotient state

metric 丢失 sign 与 sub-unit normalized relation detail，而这些区别会影响 A3 partition aggregation。

取相同 capacities：

\[
m=(2,2,2,2)
\]

以及两个 total vectors：

\[
c=(-3,-2,-1,2),
\]

\[
\tilde c=(-3,-1,-2,2).
\]

它们产生完全相同的 labeled integer relation metric：

\[
\rho=
\begin{pmatrix}
0&1&1&3\\
1&0&1&2\\
1&1&0&2\\
3&2&2&0
\end{pmatrix}.
\]

现在对二者使用同一个 A3 partition：

\[
A=\{0,1\},\qquad B=\{2,3\}.
\]

第一个 fine state 的 direct aggregated coarse threshold 为

\[
\bar\rho_{AB}=2,
\]

第二个则为

\[
\tilde{\bar\rho}_{AB}=1.
\]

所以两个 A3 states 即使 `(X0,rho)` 完全相同，也会在 future operation “按照该 partition aggregation，再读取 coarse relation threshold”下产生不同结果。

因此

\[
\boxed{
(X_0,\rho)\text{ 对 }L_{supp}\text{ future-safe，
但对 full A3 partition-operation language 不 future-safe。}
}
\]

这正是 P023 要求我们在删除 detail 之前必须明确写出的边界。

## 7. 与 A3 piecewise non-monotonicity 的关系

B24 并没有说把 `(m,c,Z)` 换成 `rho` 是普遍意义上的“更高效精度”。它只证明该替换对一个明确声明的 language exact。

如果后来 program 增加 partition aggregation、signed response、piecewise guards 或其他读取 `rho` 已删除区别的 A3 operations，就必须重新审计并修复该 quotient。A3 piecewise 结果已经独立证明，即使 arbitrary refinement 也未必保持 exactness，除非新 representation 恰好暴露 future semantics 所需区别。

## 8. 一个闭合的 support-language state machine

给定 `(X0,rho)`：

1. threshold `rho` 生成任意 primitive `R_r`；
2. relational composition 计算任意 finite support word；
3. 计算 common-target relations；
4. 计算任意 fixed-depth Pareto frontiers；
5. 检验 geodesicity / split-completeness；
6. 若 geodesic，则所有 finite support words 进一步坍缩为 total budget。

所以在完成 A3→metric quotient 以后，support-language subsystem 已经闭合。

## 9. 跨路线后果

### A2/P023

B24/B27 构成一个非常干净的 task-relative quotient legality 实例：同一个 state reduction 对一个 operation algebra 完全 exact，对更丰富 language 却明确非法。

### A4

在 generated subclass 中，`(X0,rho)` 可以作为 complete finite support-state representation。arbitrary A4 relations 仍然不属于该生成子类。

### A3

不能用 `rho` 替代 A3 weighted relation core。`rho` 只应作为 support-language quotient/interface。

### P018

这是一个明确的 precision projection，其 legal future scope 由数学证明声明，而不是凭直觉推断。

## 10. Prior-art discipline

metric 决定其 radius relations，而这些 finite relations 上的 relational algebra 是标准数学。当前项目特有的研究目标，是把这一 quotient 明确放入 A3→A4→P023 架构，并用精确反例标出它停止合法的 operation-language 边界。

## 11. Executable reference

reference layer 新增：

- 直接从 metric matrix 生成 support relations；
- finite support-word evaluation；
- 从完整 primitive radius family 重建 metric；
- B27 same-metric / different-A3-aggregation regression counterexample。
