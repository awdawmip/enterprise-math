# Ramanujan 喷流协向量的坐标协变、回路全纯阻碍与 P000 切片粘合

Status: `FREE_RESEARCH / DERIVED_GLUING_THEOREM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`

Author/program signature: `YUAN X / Enterprise Math`

## 1. 目的

前一阶段已经证明，Ramanujan 型系数对 `(A,B)` 是守恒周期辛面积在 Clausen 一阶喷流 `(F,Theta F)` 上的坐标。现在进一步解决：不同局部坐标、不同截面规范以及不同 P000 二维切片之间，系数对如何粘合；何时存在一个全局一致的公式。

## 2. 一阶喷流变换矩阵

设局部坐标由 `z=z(w)` 重参数化，并作非零截面规范变换

\[
F(z(w))=g(w)\widetilde F(w).
\]

记

\[
\Theta_z=z\frac d{dz},\qquad
\Theta_w=w\frac d{dw},\qquad
\kappa(w)=\frac{z(w)}{wz'(w)}.
\]

则

\[
\Theta_z=\kappa\Theta_w.
\]

在固定点 `w0`，定义喷流列向量

\[
j_z(F)=\binom{F}{\Theta_zF},\qquad
j_w(\widetilde F)=\binom{\widetilde F}{\Theta_w\widetilde F}.
\]

直接求导得到

\[
\boxed{
j_z(F)=T(g,\kappa)j_w(\widetilde F),
\qquad
T(g,\kappa)=
\begin{pmatrix}
g&0\\
\kappa\Theta_wg&\kappa g
\end{pmatrix}_{w=w_0}.}
\]

所以允许的坐标/规范变换作用在一阶喷流上形成可逆下三角群。

## 3. 系数协向量的逆变规则

令局部标量公式写为

\[
\mathcal J=c_zj_z(F),\qquad c_z=(A_z,B_z).
\]

为保持同一个抽象标量 `mathcal J`，新坐标中的协向量必须满足

\[
\boxed{c_w=c_zT(g,\kappa).}
\]

即

\[
\boxed{
A_w=gA_z+B_z\kappa\Theta_wg,
\qquad
B_w=B_z\kappa g.}
\]

这精确解释了为什么单独的 `A`、`B`、`A/B` 不是不变量。真正不变的是评价配对

\[
\boxed{\mathcal J=\langle c,j\rangle.}
\]

特别地，当坐标不变且 `g=w^{-lambda}` 时，该公式退化为前一阶段得到的规范平移规律。

## 4. 喷流群胚粘合定理

设一组局部切片/图册以指标 `i` 标记，在交叠上有喷流变换

\[
j_i=T_{ij}j_j.
\]

假设它们满足群胚余循环条件

\[
T_{ij}T_{jk}=T_{ik},\qquad T_{ii}=I.
\]

### 定理 4.1 — 全局 Ramanujan 协向量判据

一族局部公式

\[
\mathcal J=c_i j_i
\]

定义同一个全局标量，当且仅当

\[
\boxed{c_j=c_iT_{ij}}
\]

在每个交叠上成立。

证明只是把 `j_i=T_ij j_j` 代入 `c_i j_i`；反向亦然。

### 定理 4.2 — 回路全纯判据

固定图册 `i0`。沿闭合回路 `gamma` 的喷流全纯记为

\[
H_\gamma=T_{i_0i_1}T_{i_1i_2}\cdots T_{i_ri_0}.
\]

给定起点协向量 `c_i0` 可全局延拓，当且仅当

\[
\boxed{c_{i_0}H_\gamma=c_{i_0}}
\]

对所有闭合回路成立。

因此非零全局 Ramanujan 公式存在，当且仅当全部喷流全纯在对偶表示中有共同不动协向量。这个条件比“每个局部切片各自有一个 `1/pi` 公式”严格得多。

## 5. 两级阻碍分解

由定理 4.2 与前一阶段的维数阻碍，可把 P000 全局化问题分成两个逻辑独立的层级：

### 一级：秩二喷流全纯阻碍

即使每个二维周期平面局部满足 Ramanujan 型公式，若回路全纯不固定其协向量，局部系数对也不能拼成一个全局公式。

### 二级：四维补空间欠定性

即使秩二协向量全局平坦，二维传输仍不能决定六维传输的四维补空间部分。任取补空间表示 `R_ij`，只要其自身满足余循环，就得到不同的六维扩张

\[
T_{ij}\oplus R_{ij}.
\]

所以“全局公式存在”与“存在规范的 P000 六维提升”不是同一个命题：前者只要求对偶喷流不动向量，后者还要求补空间及其耦合被额外结构唯一选定。

## 6. 对 degree-29 系数的含义

标准 Ramanujan–Clausen 图册中的

\[
(1103,26390)
\]

只是一个局部协向量的整数化坐标。进入另一图册后，它一般按 `c_j=c_iT_ij` 混合，不应期待两个整数分别保持不变。可比较的对象有三层：

1. 标量值 `1/pi` 或 `sin(pi a)/pi`；
2. 协向量作为对偶喷流束的抽象截面；
3. 给定图册和归一化后的具体整数坐标。

文献中的整数公式主要属于第三层；本研究给出的几何桥位于第二层。

## 7. 公理审计

本粘合定理是线性代数、链式法则和余循环条件的直接推论，分类为

`DERIVED_GLUING_THEOREM / NOT_NEW_AXIOM / NOT_FOUNDATION`。

它补强了之前的负结论：缺少 P000 图册交叠矩阵时，问题不是“尚未猜到正确的六维公式”，而是输入数据不足，连秩二协向量的全局化都未被定义；即使补足秩二交叠，四维补空间仍然欠定。

## 8. 下一可执行研究单元

选择至少两条不同 degree 或 level 的 Ramanujan–Sato 公式，构造各自标准喷流协向量，并检验是否存在自然模对应诱导的 `T_ij`，使它们落在同一对偶喷流群胚轨道。只有在这个轨道被明确后，才有资格讨论 P000 粘合数据是否能选择统一提升。
