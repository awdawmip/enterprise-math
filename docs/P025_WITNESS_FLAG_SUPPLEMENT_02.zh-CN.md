# P025 补充 02 —— Witness Flag 的规范外积签名

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 Supplement 01；P023 quotient/minimal repair  
数学背景：有理线性代数、整数饱和格、外代数/Plücker 坐标均为既有数学  
创新状态：`ARCHITECTURE NOVELTY_UNVERIFIED`

## 1. 问题

P025 Supplement 01 得到 relation-conditioned witness flag

\[
T^\circ\subsetneq T\subset\mathbb Z^S,
\]

其中

\[
T=\ker_{\mathbb Z}\alpha,
\qquad
T^\circ=\ker_{\mathbb Z}\alpha\cap\ker_{\mathbb Z}\beta.
\]

`alpha` 可 primitive + sign normalization 后成为 `T` 的规范法向量。

但原始 pair `(alpha,beta)` 不是 flag 的规范状态，因为对任意 `lambda neq 0` 与 `mu`，

\[
\beta'=\lambda\beta+\mu\alpha
\]

在 `T=ker(alpha)` 上与 `beta` 具有相同零集合，因此定义相同的 `T^circ`。

所以真正要找的是：

> 什么有限整数对象精确表示这个 nested witness flag，而不保留无意义的 `beta` shear/scaling 自由度？

## 2. 外积消除 shear

考虑

\[
\alpha\wedge\beta\in\bigwedge^2\mathbb Z^S.
\]

若

\[
\beta'=\lambda\beta+\mu\alpha,
\]

则

\[
\alpha\wedge\beta'
=\lambda(\alpha\wedge\beta),
\]

因为

\[
\alpha\wedge\alpha=0.
\]

所以把 `alpha wedge beta` 的全部 Plücker 坐标除去 gcd，并固定整体符号后，其 primitive projective class 自动同时消除了：

- `beta -> beta + mu alpha` 的 shear；
- `beta -> lambda beta` 的非零整体缩放。

记这个规范二形式为

\[
\widehat\Pi(\alpha,\beta).
\]

## 3. P025-T07 —— saturated witness flag 的完备有限签名

固定同一个带标签有限坐标集 `S`。设 `alpha,beta` 与 `alpha',beta'` 都满足：

- `alpha,alpha'` primitive nonzero；
- `beta` 不在 `Q alpha` 中；
- `beta'` 不在 `Q alpha'` 中。

定义两个 saturated flags：

\[
F(\alpha,\beta):
\ker_{\mathbb Z}\alpha\cap\ker_{\mathbb Z}\beta
\subset
\ker_{\mathbb Z}\alpha
\subset
\mathbb Z^S.
\]

则

\[
\boxed{
F(\alpha,\beta)=F(\alpha',\beta')
}
\]

当且仅当

\[
\boxed{
\widehat\alpha=\widehat\alpha'
\quad\text{且}\quad
\widehat\Pi(\alpha,\beta)
=
\widehat\Pi(\alpha',\beta').
}
\]

### 证明

第一层整数核相同，由 P025-T06 等价于 primitive normal 相同，所以

\[
\widehat\alpha=\widehat\alpha'.
\]

固定该第一行以后，第二层 `T^circ` 是 `ker alpha` 内的 codimension-one rational hyperplane 与 `Z^S` 的交。

两个这样的第二层整数饱和格相同，当且仅当相应有理子空间相同；等价地，两个 rank-two row spaces

\[
\operatorname{span}_{\mathbb Q}\{\alpha,\beta\}
\]

与

\[
\operatorname{span}_{\mathbb Q}\{\alpha,\beta'\}
\]

相同。

而一个 rank-two row space 的 projective Plücker 坐标正由非零外积

\[
[\alpha\wedge\beta]
\]

决定。primitive + sign normalization 给出同一 rational ray 的唯一整数代表。因此第二层相同恰好等价于

\[
\widehat\Pi(\alpha,\beta)
=
\widehat\Pi(\alpha,\beta').
\]

证毕。

## 4. 规范 witness-flag state

因此，对 P025 的 abc witness，可定义

\[
\boxed{
\Sigma_{\rm flag}(a,b,c)
=
\left(
S,
\widehat\alpha,
\widehat\Pi(\alpha,\beta)
\right).
}
\]

其中：

- `S=supp(abc)` 保留 prime 坐标标签；
- `hat alpha` 决定 additive witness lattice `T`；
- `hat Pi` 决定 `T` 内的 Wronskian-degenerate sublattice `T^circ`；
- `L_infinity` norm 由同一个带标签 ambient coordinate system 继承。

于是 `Sigma_flag` 精确决定完整 normed flag

\[
T^\circ\subset T\subset\mathbb Z^S
\]

以及由它产生的全部有限 witness balls

\[
\mathcal W_k=(T\setminus T^\circ)\cap[-k,k]^S
\]

和临界 witness precision `mu`。

## 5. P023 分层最小修复

这给 P025/P023 交叉处一个清楚的层级：

### 只恢复 additive witness lattice

未来观察：

\[
h_1(x)=T(x).
\]

最粗规范签名是

\[
\Sigma_{\rm add}=(S,\widehat\alpha).
\]

### 恢复完整非退化 witness flag

未来观察：

\[
h_2(x)=\bigl(T^\circ(x)\subset T(x)\bigr).
\]

最粗规范签名提升为

\[
\Sigma_{\rm flag}
=(S,\widehat\alpha,\widehat\Pi).
\]

### 只判断小 witness 是否存在

未来观察：

\[
h_{3,K}(x)=1_{\mu(x)\le K}.
\]

这里 `Sigma_flag` 足够，但通常未必最粗。真正的 P023-minimal repair 仍需按具体 `K` 求 quotient。

因此已经出现一个严格的“任务越弱，所需签名可以继续坍缩”的研究阶梯。

## 6. 与 A4 的接口

A4 关心 multivalued admissible support。P025 现在给出一个不应单值化的自然例子：

\[
x\mapsto\mathcal W_k(x).
\]

但 `Sigma_flag` 说明，多值 witness family 的生成数据可以比枚举全部 witnesses 紧凑得多：一个 rank-one normal 加一个 primitive projective two-form 就足以重建整个 flag，再按半径生成有限 witness family。

所以一个可能的通用方向不是“把所有 support 都存下来”，而是：

\[
\boxed{
\text{generator signature}
\to
\text{admissible relation family}
\to
\text{task-relative finite slice}.
}
\]

这个方向是否超出现有 relation/lattice/automata 理论，仍需 prior-art 审计。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_witness_flag.py`
  - exterior two-form；
  - primitive projective normalization；
  - canonical witness-flag signature；
  - `beta -> lambda beta + mu alpha` shear invariance；
  - saturated flag equality checker。
- `tests/test_abc_witness_flag.py`
  - 外积坐标；
  - shear/scaling invariance；
  - 不同 additive normal 的 flag 分离；
  - `5+27=32` 的规范签名样本；
  - dependent-row rejection。

## 8. 当前结论

P025 已经从一个 ABC 应用问题压缩出一个更通用的有限状态候选：

\[
\boxed{
\text{relation-state}
\to
\text{primitive normal / exterior signature}
\to
\text{normed saturated witness flag}
\to
\text{finite witness precision}.
}
\]

最重要的是，它没有把被遗忘的 fine state 全部补回来，而是只补回**生成当前任务证书空间所必需的不变量**。

这正是后续应继续拿去压力测试 P023 “最少补回多少信息”的地方；但在完成一般定理和 prior-art 搜索前，仍保持 `NOVELTY_UNVERIFIED`，不进入 Foundation canonical。
