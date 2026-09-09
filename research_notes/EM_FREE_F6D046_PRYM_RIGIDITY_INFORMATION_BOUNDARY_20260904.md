# Gaussian Prym 的刚性分界：type (2,0) 被迫分裂，而 type (3,1) 需要新的算术信息

Status: `FREE_RESEARCH / DERIVED_INFORMATION_BOUNDARY / POSITIVE_DIMENSIONAL_MODULI_NO_GO / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R12-PRYM-RIGIDITY-INFORMATION-BOUNDARY`

## 0. 结论

R11 给出两个带 `Q(i)` action 的 Prym：

- `P6`：dimension 2，Hodge signature `(2,0)`；
- `P46`：dimension 4，Hodge signature `(3,1)`。

对带虚二次乘法、signature `(r,s)` 的极化阿贝尔簇，相应 Hermitian deformation domain 的复维数是

\[
\boxed{rs.}
\]

因此：

\[
(2,0):\quad rs=0,
\]

与 R11 的 lattice 论证一致，`P6` 是刚性的 Gaussian CM product，作为不指定极化的复阿贝尔簇为 `E_i^2`。

而

\[
(3,1):\quad rs=3.
\]

所以 `P46` 所携带的现有信息——dimension、`Q(i)` action、Hodge multiplicities、branch count、polarization type——落在正三维的 PEL/Hermitian 变形空间中。它们不能唯一决定 `P46` 的 isogeny class，也不能单独强迫“几何简单”或“分裂”。

## 1. 精确 no-go

设一个判定器只读取：

- `Q(i)` action；
- Hodge signature `(3,1)`；
- polarization 的离散类型；
- R10/R11 的 deck-character multiplicities。

这些数据在同一个正维模空间上局部常值。因此该判定器不可能从这些输入唯一重构 endomorphism algebra 或 isogeny decomposition。任何“由 signature `(3,1)` 直接推出 simple/split”的论证都缺少信息。

这与 `(2,0)` 情形的区别不是计算量，而是 deformation dimension 从 `0` 变成 `3`。

## 2. 下一阶段所需的新数据

要判定当前特定 `P46`，至少需要加入下列一种真正变化的信息：

1. 若干好素数处的 Frobenius characteristic polynomials；
2. 一个经认证的 period matrix 与 endomorphism search；
3. 显式 correspondence／quotient map；
4. 与已知 genus-2/abelian-surface factors 的 Hom-space 证书。

其中有限域路线最适合先行：若取得足够多好素数的完整 degree-8 Prym Frobenius polynomials，可测试共同因子、CM pattern 和绝对简单性候选；单独的点数第一矩不够。

## 3. 对研究链的意义

R12 不是停止研究，而是关闭一条已经无新增信息的纯对称性路线：

\[
\text{CURRENT CHARACTER/HODGE DATA}
\not\Rightarrow
\text{P46 ISOGENY DECOMPOSITION}.
\]

后继工作必须切换到算术证据层，而不能继续把 Wronskian、Clausen parity 或中心 character 当作新的分裂证据。

## 4. 审计

该结论是标准 Hermitian/PEL deformation-dimension 机制对 R11 的应用。它构成精确 information-boundary，不是新公理，也不修改 P000。

分类：`DERIVED_INFORMATION_BOUNDARY / POSITIVE_DIMENSIONAL_MODULI_NO_GO / NOT_NEW_AXIOM / NOT_FOUNDATION`。
