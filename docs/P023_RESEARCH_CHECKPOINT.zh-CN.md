# P023 研究检查点 —— 可复合安全坍缩

状态：`CHECKPOINT / ACTIVE RESEARCH`  
日期：2026-08-09

## 当前保留核心

本研究线目前只保留以下基础对象：

1. 有限细状态空间；
2. 显式粗商 / 观测分区；
3. 粗状态必须支持的运算；
4. fiber 常值 / congruence 作为安全判据；
5. 判据失败时的最小 partition refinement。

核心定理不需要误差度量、概率、熵、连续极限或物理解读。

## 当前定理栈

- T01：fiber 常值当且仅当观测可通过商下沉；
- T02：`(旧粗标签, 失败的未来观测)` 构成最粗一步修复；
- T03–T07：有限确定性未来细化有限稳定到最粗转移兼容细化；
- T08：精确 quotient 与任意 floor-precision quotient 兼容；
- T09：同空间 multiple collapse 通过 floor precision 下沉，当且仅当两个整数参数在整除序下可比；
- T10–T14：有限闭包推广到有限确定性运算族，并具有 operation-word 未来语义。

## 独立有界检查

在仓库 CI 之外，重新独立实现核心数学定义并做穷举：

- 至多四状态、一个确定性运算、二值初始观测共 4330 个系统，检查稳定兼容、未来深度语义、最粗兼容细化；
- 三状态、两个生成算子、二值初始观测共 5832 个系统，检查共同兼容、operation-word 语义、最粗共同细化。

上述有界域内未发现反例。

这些检查只是证明的支持证据，不替代普通证明或仓库 CI。

## 当前阻断 / 下一定理目标

下一步攻算术最小修复：

> 当 P018 floor-precision quotient 与某个进取数论运算不兼容时，最粗修复能否由已有有界 detail 坐标（Euclidean remainder、basin position、carry、collision spectrum 等）规范表达，而不是任意重新编号分区？

如果答案为正，通用 quotient compatibility 将直接接入项目的整数精度演算；若为负，应找出最小反例并定位缺失的 detail 类型。
