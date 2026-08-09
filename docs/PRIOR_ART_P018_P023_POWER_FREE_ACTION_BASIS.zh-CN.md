# 前人工作说明 — P018/P023 幂自由未来动作基

状态：`研究谱系说明 / NOVELTY_UNVERIFIED`  
范围：有界 quotient-root 状态识别、最小区分动作族与幂自由算术

## 1. 保守的新颖性立场

P018/P023 bridge 不应把以下一般思想表述为 Enterprise Math 的原创：

- 选择最小的一组测试/观测，使任意两个状态都能被至少一个测试区分；
- 有限状态系统中的状态识别与 distinguishing-sequence 问题；
- 一般 Test Cover 最优化问题及其计算复杂性理论；
- power-free / k-free 整数、其分解思想以及经典计数渐近。

这些都是已有的数学与算法结构。

本项目当前可能具有项目特异性的部分更窄：对结构化观测

`O_a(q) = R_r(floor(q/a))`,

在有界精确状态域 `0,...,N` 上，一般的区分测试最优化会坍缩成一个精确的强制动作基，即 `N` 以内所有正的 `r`-power-free 整数。

这一精确特例的历史优先性**尚未得到验证**。

## 2. Minimum Test Cover 属于前人工作

Crowston、Gutin、Jones、Saurabh 与 Yeo 研究参数化 Test Cover 问题，其目标正是选择一组测试，使任意两个对象都至少被其中一个测试区分。[SRC-CROWSTON-TEST-COVER-2012]

Gutin、Muciaccia 与 Yeo 进一步研究同一一般 Test Cover 问题的 kernelization 与复杂性边界。[SRC-GUTIN-TEST-COVER-KERNELS-2012]

因此，#233 不对“最小测试 / 两两区分”这一问题表述本身主张新颖性。其特殊性在于：quotient-root 动作族允许把每一个被迫测试/动作写成闭式算术条件，而不需要求解一般组合优化问题。

## 3. 幂自由算术属于前人工作

幂自由整数及其计数理论是经典数论。Mossinghoff、Oliveira e Silva 与 Trudgian 对 `k`-free 数的分布给出现代的第一手研究，并使用标准主尺度 `x/zeta(k)`。[SRC-MOSSINGHOFF-KFREE-2019]

因此，#233 不主张发明 `r`-power-free 整数、剥离 `r` 次幂因子的解释，或其经典渐近密度。

Lean 证明中只使用有限强下降来证明存在分解

`q = b * t^r`,

其中 `b` 为 `r`-power-free；它不依赖任何新的唯一分解定理。

## 4. Enterprise Math 的精确特例

该分支已经用 warning-fatal Lean 证明局部定律

`O_a(q-1) != O_a(q)  iff  q = a * t^r`

其中 `t` 为正整数。

因此，对一个 `r`-power-free 边界 `b-1 | b`，能够区分它的动作只能是 `a=b`。反过来，每个正边界都可以通过有限下降分解为 `q=b*t^r`，其中 `b` 幂自由，所以这些被强制的动作又足以区分全部边界。

于是，对任意动作集合 `A`，

`A 能区分 0,...,N 中全部精确状态`

当且仅当

`A 包含所有满足 1<=b<=N 的正 r-power-free 整数 b`。

因此，幂自由集合是在包含关系下唯一的最小区分动作族。

## 5. 新颖性边界

当前最稳妥的分类是：

- **ADOPT** 一般 Test Cover / distinguishing-family 的问题语言；
- **ADOPT / COMBINE** 经典幂自由整数结构与计数；
- 对 quotient-root 的精确闭式动作基定理，以及把它作为 P023 future-action-language 特例的做法，保持 **NOVELTY_UNVERIFIED**。

本轮检索没有在已检查文献中找到完全相同的 quotient-root / power-free action-basis 陈述，但“没有检索到”不等于历史新颖性证据。任何优先性主张都仍需要更广泛的专项文献检索或外部专家复核。

## 6. 来源登记

本说明使用的第一手来源登记在 `sources_p018_p023_power_free_action_basis.json`；项目侧谱系关系登记在 `lineage_p018_p023_power_free_action_basis.json`。
