# 因果吞并计划 —— 让传统数学成为进取数论的派生影子

状态：`ACTIVE RESEARCH CORRECTION / CROSS-ROUTE PROGRAM`

本文件纠正当前研究中出现的一个结构性滑移：

> **不能把传统数学对象保持为本体，只在外面增加 `precision / quotient / scale` 声明。**

进取数论若要形成自己的理论，顺序必须反过来。

## 1. 新的基础顺序

基础链统一改写为：

\[
\boxed{
\text{state}
\to
\text{causal operations}
\to
\text{future distinguishability}
\to
\text{collapse}
\to
\text{derived observable / precision / geometry}.
}
\]

因此：

- precision 是因果坍缩后的结果，不是先验标签；
- dimension 是剩余可区分自由度的结构量，不是先声明坐标数；
- distance 必须来自 primitive operation / causal program cost / distinguishability depth，而不是先验范数；
- topology 必须来自因果可区分 filtration / reachability stability，而不是先给 open sets；
- matrix、rank、kernel、Smith/Hermite、ILP 等首先只是计算语言，只有在被因果结构严格推出后才允许进入 core ontology。

## 2. 因果吞并测试

任何传统工具 `T` 进入 Enterprise Math core 前，必须明确属于以下哪一类。

### A. CAUSAL_DERIVED

`T` 能从显式 state + operation language + future observations 精确推出。

这是真正被“吞掉”。

### B. SHADOW_FORMULA

进取数论对象先存在；`T` 只是某个特殊 regime 下的闭式或传统命名。

例如标准 unit-step integer geometry 中，`L1` 是最短 primitive program length 的闭式，不是基础范数。

### C. COORDINATE_TOOL

`T` 只是为了计算、压缩、证明或换坐标。

例如 HNF/SNF/矩阵表示可以保留，但不得因为计算方便就升级为本体。

### D. EXTERNAL_COMPARISON

若 `T` 需要隐藏实数完成、连续极限、外加 epsilon/precision 公理或其他进取数论没有自行产生的结构，则只作为比较工具。

## 3. 第一阶段已经被吞并的对象

### 3.1 Quotient / congruence

一般 set quotient 不再是基础。

真正 primitive 的问题是：

> 哪些差异在所有允许未来中永远不能被区分？

未来等价先由 operation language 产生；传统 quotient 只是把该 equivalence class 编码成状态。

P023/A2 是这一方向的现有母理论。

### 3.2 Kernel / rank / observability

在 integer-linear future language 中：

\[
K_*=\{\eta:WB_\omega\eta=0\text{ for all finite future words }\omega\}
\]

先由因果不可区分性定义。

随后：

- `kernel` = 永久不可见 integer motion；
- `rank` = 未来能独立区分的自由度数；
- observability rows/matrix = 把未来实验拉回当前后的计算表。

所以传统线性代数被降为 causal distinguishability 的计算 shadow。

### 3.3 Basis

basis 不再首先是“空间的一组坐标基”。

定义 **causal probe basis**：最少一组具体未来实验，使两个状态只要在这些实验上结果相同，就自动在所有允许有限未来上不可区分。

其大小等于 causal visible rank。

因此：

\[
\boxed{
\text{basis size}
=
\text{minimal number of independent future distinguishability generators}.
}
\]

### 3.4 Ultrametric-like structure

不先定义实值 ultrametric。

定义：

\[
s(x,y)=\text{first future depth that distinguishes }x,y.
\]

则：

\[
\boxed{s(x,z)\ge\min(s(x,y),s(y,z)).}
\]

这是纯整数 causal agreement law。

传统 ultrametric 如需使用，只是 `s` 的单调数值重编码。

### 3.5 Topology

每个深度 `t` 的不可区分 class：

\[
U_t(x)=[x]_{\sim_t}
\]

自动构成 clopen basis。

所以 neighborhood 的因果定义是：

> 在某个有限未来深度仍无法与 `x` 区分的所有状态。

该拓扑的 T0 quotient 恰好就是 stable future-equivalence quotient。

因此 topology 在该 regime 中由因果过滤层派生。

### 3.6 Metric / norm

P012 已经提供第一类成功吞并：

\[
d(x,y)=\text{从 }x\text{ 到 }y\text{ 的最短 primitive operation length}.
\]

标准 `L1` 只是特定 generator family 下的 closed form。

今后一般 norm 只有在能证明是某个 causal word-cost 的闭式时，才能进入 core。

## 4. 当前仍未被吞并的传统工具

以下工具暂时只允许作为 `COORDINATE_TOOL / EXTERNAL_COMPARISON`：

- 一般 Euclidean norm；
- 任意实值 inner product；
- 连续 manifold；
- calculus/derivative/integral 作为基础操作；
- Hilbert/Banach completion；
- 先验 probability measure；
- 未从 causal operations 推出的拓扑；
- 仅因为传统数学常用而引入的 field/vector-space completion。

这不是永久禁止，而是要求先给出 causal derivation。

## 5. 对当前 A3 Future Precision 路线的纠偏

`A3_FUTURE_PRECISION_CORE` 中已有很多有效结果，但以后解释顺序必须改写：

旧倾向：

\[
\text{traditional quotient/module}
+\text{precision declaration}.
\]

新解释：

\[
\boxed{
K_A
\xrightarrow{\text{future language }W}
L_A=W(K_A)
\to
\text{future indistinguishability}
\to
\text{minimal exact collapse}.
}
\]

只有最后才读取：

- rank；
- Smith factors；
- torsion residue；
- relation quantum；
- minimum precision cost。

这些都是 causal collapse 的 **diagnostics / coordinates**，不是本体。

## 6. 研究纪律变化

从本文件生效后，在该研究线上：

1. 不再因为找到一个传统 invariant 就增加一个“precision coordinate”；
2. 先写明它对应什么 future distinction / operation obligation；
3. 若无法写出 causal meaning，则不得进入 core，只能放 tooling/prior-art；
4. 每次使用传统定理，必须区分：
   - 我们在借它证明自己的因果对象；还是
   - 我们偷偷把传统对象重新设成基础；
5. 优先寻找“传统定理成为进取数论特殊情形”的方向，而不是“进取数论兼容传统定理”。

## 7. 第一批吞并路线

### Route 1 — Linear algebra → causal future module

目标：完成

`kernel / rank / basis / observability / quotient module`

的因果重解释。

当前已得到：

- infinite `Z^k` 上 future-visible closure；
- strict refinement 次数 <= `k`；
- causal visible rank；
- causal probe basis。

### Route 2 — topology / ultrametric → future-depth filtration

目标：以 nested future-equivalence classes 为 primitive，传统 topology/ultrametric 只作为 shadow。

### Route 3 — norm / metric → causal program cost

目标：把 P012 graph metric 提升为一般 operation-language word cost，并判断哪些传统 norms 能成为 exact closed form。

### Route 4 — probability → collapse multiplicity（候选）

不预设概率测度。

优先检查 P010/P011 fiber multiplicity / collision spectrum 是否能先生成整数 weight，再在额外归一化选择下才出现传统 probability。

该路线尚未证明，不得提前宣称完成。

## 8. 当前代码/证明来源

- `src/enterprise_math/causal_future_module.py`
- `tests/test_causal_future_module.py`
- `src/enterprise_math/causal_probe_basis.py`
- `tests/test_causal_probe_basis.py`
- `docs/CAUSAL_ABSORPTION_LINEAR_FUTURE_MODULE.*`

## 9. 架构归属

本计划是 cross-route correction，不创建新的 canonical problem 编号。

当前建议 ownership：

- general future distinguishability / causal quotient：A2/P023；
- capacity-weighted integer specialization：A3；
- causal word metric / geometry：A5/P012/P022；
- multiplicity / collision-generated weight：A1/P010/P011。

新的 reusable mother theorem 必须 Relay 到真正 owner；不能因为发现于 A3 branch 就长期留成 A3 重复母理论。

## 10. 当前研究问题

真正值得继续攻的不是“还有哪些传统 invariant 可以加 precision”。

而是：

\[
\boxed{
\text{给定一个传统数学结构，
能否证明它只是某种有限因果演算的影子？}
}
\]

如果答案是能，进取数论就把它吞掉。

如果答案是否，则它目前仍是外部工具，不应成为进取数论底层。
