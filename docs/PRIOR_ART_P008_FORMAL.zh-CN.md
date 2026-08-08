# 前人工作附录 —— P008/P014 的 Mathlib 形式化基础

状态：`CANONICAL PRIOR-ART APPENDIX`

## 1. Nat.nthRoot 是成熟的形式化库成果

当前固定版本的进取数论 Lean 层直接复用 mathlib 的 `Nat.nthRoot`。Mathlib 源码已经证明正自然数幂与自然数 nth root 之间的关键序刻画和 Galois connection。 [SRC-MATHLIB-NTHROOT]

因此，进取数论**不**把 integer nth root、本身的 floor 不等式、完全幂精确恢复或相应 Lean API 宣称为自己的发明。

这里必须区分形式结构与内部语义。Mathlib 可以使用普通成熟数学来刻画或实现 `Nat.nthRoot`，其中包括 real-root/floor 视角。进取数论导入的是已经证明的整数/序结构性质，但不会把一个隐藏的无限精度实数根作为自身状态运算的内部第一性含义。

## 2. Galois connection 是成熟序理论

Mathlib 的 GaloisConnection 库已经提供成熟的伴随语言、insertion/coinsertion、单调性结果、复合律以及 commuting-adjoint 工具；P008/P014 的形式化层直接复用了这些结构。 [SRC-MATHLIB-GALOIS-CONNECTION]

因此，P008 得出“当前 v0.1 运算自然落在偏序与伴随结构中”，并不意味着项目发明了 Galois connection。项目特有工作是：在进取数论显式有限状态语义下提出最弱结构问题，并把这些成熟工具组织成一套可复用基础层。

## 3. 与已登记来源的关系

向下整数除法作为右伴随已经登记在 [SRC-MATHLIB-FLOORDIV]；closure/interior 型幂等算子已经登记在 [SRC-MATHLIB-CLOSURE]。

这些成熟组成共同支撑 `EM-COMP-014`：

- 幂构造 / 整数根构成伴随；
- 乘法 / 向下整数除法构成伴随；
- order embedding / coinsertion 给出精确恢复；
- 诱导出向下、幂等的坍缩；
- 左伴随交换方块被传递成 P014 使用的 root/division interchange。

## 4. 项目特有的综合

进取数论当前项目级综合是：

1. 把整数状态及其显式分辨率/尺度作为被表示状态，而不是默认视为某个必须存在的隐藏实数完成体的近似；
2. 要求显式状态的相等语义忠实，因此使用偏序，或先对 preorder 做 posetal quotient，而不是把不同但 preorder-equivalent 的状态静默混同；
3. 把 principal sublevel 存在最大元识别为当前运算所需右伴随存在的字面条件；
4. 直接复用 mathlib，而不是另造一套平行 root/order framework；
5. 把 root/division/scale compatibility 统一解释为同一 order-adjoint 模式。

这一综合的历史创新性继续标记为 `NOVELTY_UNVERIFIED`。
