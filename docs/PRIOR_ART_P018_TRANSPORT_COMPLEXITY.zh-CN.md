# 前人工作边界 —— P018 Transport Complexity

状态：`PRIOR-ART NOTE`  
范围：deterministic one-message function computation、communication complexity、coding for computing、decoder side information，以及 P018 transport branching capacity 的边界

## 成熟邻域

Yao 1979 年关于 distributed computing 的论文是 communication-complexity 模型的奠基来源之一：计算一个函数所需的信息交换量本身可以成为复杂度对象。[SRC-YAO-1979-DISTRIBUTIVE]

Orlitsky 与 Roche 的 *Coding for Computing* 研究了 decoder 拥有相关 side information 时，为计算目标函数进行编码的问题。[SRC-ORLITSKY-ROCHE-2001-CODING]

因此 P018 **不主张发明**：

- communication complexity 这一领域或模型；
- 为计算函数而最小化通信量；
- 带 side information 的 zero-error / exact function computation；
- 只为目标函数编码而不重建全部 hidden inputs 的一般思想；
- decoder side information 可以减少 message alphabet / rate 的一般事实；
- 通过 operation tree 逐节点拼接消息得到 generic product protocol 的方法。

## 进取数论的专门化问题

P018 在 contextual congruence closure 已经解决 exact state sufficiency 之后，提出一个更窄的有限状态问题：

> 已知原 coarse input classes，在最坏 coarse input cell 内，一个 operation 仍可能产生多少个不同 coarse output classes？若 decoder 已知 coarse inputs，为了精确确定 coarse output，deterministic correction token 的最小 alphabet 到底多大？

项目把这个有限基数记为 `B_E(mu)`，称为 **transport branching capacity**。它对应的最小 token 定理只是初等有限计数，不声称是新的 communication-complexity 结果。项目专门价值在于把它与以下结构精确接起来：

- P018-T169–T181 的 precision equivalence / congruence；
- P018-T176/T178 的 minimum persistent detail；
- 更早 precision calculus 的 carry/defect transport；
- operation-tree composition bound；
- 完全整数的 fixed-length bit cost；
- radix addition 只需要二元 token、而 radix multiplication 可以达到完整 residue-pair information bound 的显式算术例子。

## 关键区分

`B_E(mu)` 衡量的是：**在 coarse input classes 已知时，一步 deterministic transport 还剩多少 output ambiguity**。它不是 minimal exact contextual quotient 的 state 数量。

两类量回答不同问题：

1. persistent state complexity：每个 operand 至少必须长期保留什么 detail，才能让声明的 operations 都 well-defined？
2. transport complexity：decoder 已知 coarse input cells 后，还至少需要多少 operation-specific message 才能确定 exact coarse output？

radix addition 是最清楚的分离例子：full remainder 是 unavoidable persistent detail，但一步 coarse-output transport 只需要一个 carry bit。

## Claim discipline

Supplement 24 的 minimum-cardinality token 结果应当被理解为项目中的 finite coordinate / contract，而不是 communication complexity 或 functional compression 的历史首次发现。

项目真正仍开放的更强问题是：什么时候 minimal 或 near-minimal token 能够形成**结构化、可组合的 transport law**（carry/cocycle-like 或其他结构），而不是任意 cell-dependent codebook？不预设所有高效 transport structure 都属于 cohomology。
