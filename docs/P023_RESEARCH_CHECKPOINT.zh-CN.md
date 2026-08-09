# P023 研究检查点 —— 可复合安全坍缩

状态：`CHECKPOINT / ACTIVE RESEARCH`  
日期：2026-08-09

## 当前保留核心

本研究线保留以下一般基础对象：

1. 有限细状态空间；
2. 显式粗商 / 观测分区；
3. 粗状态在声明的未来语言中必须支持的运算与观测；
4. fiber 常值 / congruence 作为安全判据；
5. 判据失败时的最小 partition refinement；
6. safe-precision selector 作为有限等价关系格上的单调、向下、幂等映射。

核心定理不需要误差度量、概率、熵、连续极限或物理解读。

## 当前规范定理栈

- T01：fiber 常值当且仅当观测可通过商下沉；
- T02：`(旧粗标签, 失败的未来观测)` 构成最粗一步修复；
- T03–T07：有限确定性未来细化有限稳定到最粗转移兼容细化；
- T08：精确 quotient 与任意 floor-precision quotient 兼容；
- T09：同空间 multiple collapse 通过 floor precision 下沉，当且仅当两个整数参数在整除序下可比；
- T10–T14：有限闭包推广到有限确定性运算族，并具有 operation-word 未来语义；
- Stage 2：safe-precision interior 是给定精度关系下方最大的兼容关系；均匀 divisibility scale 并不对最小修复封闭，因此 localized bounded detail 是合法精度对象；
- Stage 3 / Supplement 07：固定 safe-selector word 反复执行会稳定到各运算要求并集对应的 joint safe precision；一次执行顺序可以影响瞬态，但稳定精度与顺序无关。

## 独立有界检查

在仓库 CI 之外，重新独立实现核心数学定义并做穷举：

- 至多四状态、一个确定性运算、二值初始观测共 4330 个系统，检查稳定兼容、未来深度语义、最粗兼容细化；
- 三状态、两个生成算子、二值初始观测共 5832 个系统，检查共同兼容、operation-word 语义、最粗共同细化。

上述有界域内未发现反例。

这些检查只是证明的支持证据，不替代普通证明或仓库 CI。

## P024 建立后的职责分界

P023 继续保留为**一般理论**，不再把每一个 future-safe quotient 的算术特化都吸收进来。

P024（`docs/P024_ACTION_LANGUAGE_PRECISION.zh-CN.md`）负责一维加法/有序阈值特化：

- 整数平移动作幺半群；
- 可达边界轨道 `B-M`；
- 单向 numerical-semigroup holes；
- gcd 过细缺陷的精确计数；
- conductor 局域非均匀边界层；
- 真正双向动作的群完备化；
- 有限循环周期化后的自动子群完备化。

因此职责边界是：

```text
P023：哪个等价关系对未来安全 / 最粗？
P024：在“整数平移 + 有序阈值观测”下，
      这个关系具体具有怎样的算术几何？
```

E001 Boolean-contact 与 E002 actuation 可以把 P024 当作算术母层，但它们仍分别拥有自己的工程/物理语义。

## 当前下一定理目标

P023 一般路线应越过已经拆给 P024 的加法阈值特例。优先方向：

1. state-dependent operation family，其安全关系不能归约为状态无关的加法幺半群；
2. 非均匀 / localized safe precision 的高效规范表示，避免退化成任意 database-like 标签；
3. 抽象 P019 collapse-word stabilization 与 P023 selector-word stabilization 的共同母定理；
4. 多组独立 safe-precision 要求的相互作用，特别是各自最小修复位于不同结构化状态族时。
