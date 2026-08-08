# 前人工作说明 —— P023 可复合安全坍缩

状态：`RESEARCH PROVENANCE NOTE`  
范围：与 P023 相关的商映射因子化、未来可区分性与 partition refinement

## 1. 保守的新颖性立场

P023 不得把以下一般思想描述为进取数论原创：

- 一个映射能否通过商下沉，取决于它是否在商 fiber 上常值；
- 与 congruence 兼容的商可以承载诱导动力学；
- 未来可区分性可以决定有限状态类的规范细化；
- 反复 partition refinement 可以求最粗稳定分区；
- 自动机最小化 / Myhill–Nerode 型等价与 bisimulation 已提供成熟邻近理论。

P023 把这些成熟结构作为数学基础设施使用。

## 2. Paige–Tarjan partition refinement

Robert Paige 与 Robert E. Tarjan 的 “Three Partition Refinement Algorithms”，发表于 *SIAM Journal on Computing* 16(6), 973–989 (1987)，DOI `10.1137/0216062`，研究了包括最粗分区问题在内的高效 partition-refinement 算法。

P023 当前可执行实现故意保持为有限、直接的参考版本，不主张 Paige–Tarjan 层面的算法新颖性或复杂度优势。

## 3. Myhill–Nerode / 有限状态可区分性

“两个状态是否应该继续保持不同，取决于是否存在未来输入/延续能区分它们的可观测行为”是自动机理论中的经典思想。P023 的 operation-word signature 在结构上属于这一类。

进取数论的项目特有解释更窄：把得到的 future-compatible quotient 视为**合法信息丢失 / 合法降低精度必须满足的证明义务**；粗状态被当作第一类有限状态，而不是隐藏连续值的近似。

## 4. 与 P023 各结论的关系

因此：

- P023-T01/T02 属于基本 quotient/factorization 结构，不做优先权主张；
- P023-T03–T07 属于有限 partition refinement / congruence 结果，不做优先权主张；
- 真正需要继续检验的是：这些成熟工具与 P010/P011 不可逆历史观测、P018 有限精度状态分解、P021 witness transport 结合后，能否产生新的算术分类和统一的精度丢失演算。

## 5. source registration 门禁

P023 从 Draft 研究提升到 canonical main 之前，应在 `sources.json` / `lineage.json` 为最终正文涉及的 partition-refinement 与 automata/congruence 前人工作登记稳定 source ID。本说明只固定归因目标，不绕过机器可读 provenance 门禁。
