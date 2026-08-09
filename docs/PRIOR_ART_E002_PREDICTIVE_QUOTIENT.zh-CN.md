# 前人工作 — E002 预测商编译器

状态：`ACTIVE PRIOR-ART NOTE`

## 1. 范围

E002 第六阶段把一个有限确定状态系统编译成：在未来动作 word 下保持已声明观测语言的最粗 partition。这个最小化思想本身并不存在历史新颖性。

## 2. 序贯机器

Edward F. Moore 1956 年的章节研究确定性有限序贯机器：当前状态由此前状态/输入决定，输出依赖状态。它是通过实验和未来输入输出行为区分状态的直接前人工作。 [SRC-MOORE-1956-SEQUENTIAL-MACHINES]

E002 采用这一有限行为视角，但不把 Moore machine、有限状态可观测性或行为等价声称为 Enterprise Math 的发明。

## 3. 自动机最小化与 partition refinement

Hopcroft 1971 年的报告研究有限自动机最小化，并给出通过不断细分状态类别实现高效状态最小化的算法。 [SRC-HOPCROFT-1971-AUTOMATON-MINIMIZATION]

E002 的通用编译器有意采用这一成熟的有限 partition-refinement 路线，而不是把它包装成新的最小化算法。

## 4. E002 真正增加的内容

本项目的特定问题更窄：

- fine state 是显式有限精度世界状态；
- action 是已声明的未来物理/控制操作；
- observation 是已声明的未来问题；
- 有限 horizon 本身也是语言的一部分；
- 得到的最小有限状态商，被解释为：对于该已声明未来语言，可以安全替代更细世界状态的精度状态；
- 编译器被当作通用证伪 oracle，独立检验 E002 手工算术闭式与 P023 future-compatible quotient 路线。

这里不声称该解释已经取得历史优先权。状态继续保持 `NOVELTY_UNVERIFIED`。
