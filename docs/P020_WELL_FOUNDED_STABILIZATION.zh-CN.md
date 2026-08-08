# P020 —— Lean 验证的良基有限稳定化

状态：`PROVED / LEAN-CHECKED`  
问题：`P020`  
范围：普通序论与形式化

## 1. 结论

设 `(X, ≤)` 是偏序集，并且严格序 `<` 良基。设

\[
F:X\to X
\]

单调且向下收缩：

\[
x\le y\Rightarrow F(x)\le F(y),
\qquad F(x)\le x.
\]

P020 在 Lean 中直接形式化 P019 的序论母定理。

### P020-T01 —— 有限次普通迭代到达初态下方最大不动点

对每个 `x`，存在 `n : ℕ`，使

\[
F^{[n]}(x)
\]

恰好是满足

\[
F(z)=z,
\qquad z\le x
\]

的最大状态 `z`。

该结论在 `EnterpriseMath/Order/WellFoundedStabilization.lean` 中形式化为 `exists_iterate_isGreatest`。

证明使用良基归纳。若 `F x = x`，零次迭代即可；否则，由向下收缩与不等式得到 `F x < x`，归纳假设可以作用在 `x` 下方。单调性又保证任何不动点 `y≤x` 都已经满足 `y≤F x`，所以递归情形找到的最大不动点同时也是原初态下方的最大不动点。

## 2. 规范有限稳定化

Lean 层从 P020-T01 给出的有限迭代次数中选择一个 `stabilizationSteps`，并定义

\[
\operatorname{stabilize}_F(x)
=F^{[\operatorname{stabilizationSteps}(x)]}(x).
\]

该定义明确是**有限次普通迭代**，不使用 `n→∞` 极限、实数完备化或隐藏连续状态。

Lean 已检查 `stabilize_F(x)`：

- 是 `F` 的不动点；
- 不超过 `x`；
- 支配所有不超过 `x` 的 `F`-不动点。

因此

\[
\boxed{
\operatorname{stabilize}_F(x)
=
\max\{y:F(y)=y,\ y\le x\}.
}
\]

## 3. 完成为 interior-like 算子

### P020-T02 —— 稳定化完成定理

Lean 证明映射

\[
x\mapsto\operatorname{stabilize}_F(x)
\]

具有：

1. 单调；
2. 向下；
3. 幂等；
4. 与原映射 `F` 完全相同的不动点集合。

特别地，

\[
\operatorname{stabilize}_F(
\operatorname{stabilize}_F(x))
=
\operatorname{stabilize}_F(x).
\]

所以，在良基偏序上，任意单调向下自映射都可以仅通过有限迭代，被完成成一个具有相同不动点集合的 interior/coreflection-like 幂等投影。

这直接连接 P008：P008 从已经幂等的 `C_p` 一类 coreflection 出发；P020 则说明，即使一步映射本身不幂等，良基有限动力学仍可生成相应的幂等稳定化算子。

## 4. 与 P019 的关系

P019 已在普通数学层证明固定坍缩词

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}
\]

最终稳定到

\[
C_L(n_0),
\qquad
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

P020 形式化了这一论证背后的通用序论发动机。把“最大不动点”进一步识别成 `C_L(n_0)`，仍由 P004/P019 的完全幂算术特化提供。

## 5. 最小结构边界

P020 **不需要**：

- 格或完备格；
- 度量或拓扑；
- 实数；
- 无限迭代极限；
- 紧致性或连续性。

当前 Lean 定理实际使用的假设就是：

- `PartialOrder X`；
- `WellFoundedLT X`；
- `Monotone F`；
- `∀ x, F x ≤ x`。

这些假设是否还能进一步削弱，同时保留同一结论，属于后续独立研究问题。

## 6. 形式化验证

根模块 `EnterpriseMath.lean` 显式导入

`EnterpriseMath.Order.WellFoundedStabilization`。

固定版本、warnings-fatal 的 Lean CI 已在仓库固定的 Lean/mathlib revision 上实际编译该模块。形式化直接复用成熟的 mathlib 良基归纳与有限函数迭代 API。[SRC-MATHLIB-WELLFOUNDED] [SRC-MATHLIB-FUNCTION-ITERATE]

这些工具属于成熟前人工作；项目组合及创新边界登记于 `EM-COMP-016`。与 P008 序伴随/interior 框架的连接继续复用成熟 Galois connection 理论。[SRC-MATHLIB-GALOIS-CONNECTION]

P008/P019/P020 这一精确组合的历史创新性仍保持未核验。
