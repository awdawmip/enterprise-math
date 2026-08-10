# P025 补充 67 —— Projective Capacity State 的稀疏激活盆地

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 47、64  
Hard block：`NONE`

## 1. 一个远粗于完整 projective value 的 future query

完整 projective observable 为

\[
\sigma_{\rm proj}=\max\{\rho_a,\rho_b,\rho_c\}.
\]

许多 future task 首先只需要回答 Boolean 问题

\[
\boxed{A_{\rm proj}=\mathbf1_{\{\sigma_{\rm proj}\ge1\}}.}
\]

把 `A_proj=1` 称为 **activated projective state**，`A_proj=0` 称为 **subunit basin**。

这个 bit 是 projective scalar 的严格 quotient。例如

\[
1+2=3
\]

与

\[
1+3=4
\]

都处在 activated state，但 exact projective values 分别为 `1` 与 `2`。

## 2. P025-T134 —— exact subunit-basin 判据

因为 `sigma_proj` 是三个 cyclic terms 的最大值，

\[
\boxed{
\sigma_{\rm proj}<1
\iff
\rho_a<1,\ \rho_b<1,\ \rho_c<1.
}
\]

等价地，在 Stage 47 的 residual/capacity 坐标中，

\[
\boxed{
\begin{aligned}
m(a)&<K_{bc},\\
m(b)&<K_{ac},\\
m(c)&<K_{ab}.
\end{aligned}}
}
\]

所以 activation bit 是 exact 的，并且完全不需要 witness search。

## 3. P025-T135 —— activated states 在 de Bruijn 意义下稀疏

Stage 64 在导入经典 de Bruijn radical-counting theorem 后证明，在 dyadic height 区间

\[
X/2<c\le X
\]

有

\[
N_X(\sigma_{\rm proj}\ge T)
\ll_\varepsilon
\frac{X^{1+\varepsilon}}T,
\qquad1\le T\le X.
\]

取 `T=1`，得到

\[
\boxed{N_X(A_{\rm proj}=1)\ll_\varepsilon X^{1+\varepsilon}.}
\]

同一区间内正整数 additive triples 的 ambient 数量为 `Theta(X^2)`，故

\[
\boxed{
\frac{N_X(A_{\rm proj}=1)}{X^2}
\ll_\varepsilon X^{-1+\varepsilon}.
}
\]

因此 activated projective state 的密度趋于零，并在当前导入的 de Bruijn 层面拥有接近完整 `X^-1` 的相对 saving。

等价地，几乎所有 additive states 都落在 exact subunit basin

\[
\boxed{\sigma_{\rm proj}<1.}
\]

这是一条关于项目自定义 observable 的 theorem，不是 pointwise abc theorem。

## 4. 为什么这比“PCC failures 稀疏”更强

任意固定正指数 `eta` 下，`PCC_eta` 只问

\[
\sigma_{\rm proj}<c^\eta,
\]

其阈值会随 height 增长。

P025-T135 把 threshold 固定在绝对整数尺度 `1`，仍然得到稀疏 exceptional layer。

所以 projective observable 不只是“通常低于任何正幂”；它通常甚至低于第一个非平凡整数阈值。

由此自然形成 precision basin：

\[
\boxed{
\text{subunit bulk }(\sigma<1)
\quad\cup\quad
\text{sparse activated layer }(\sigma\ge1).
}
\]

## 5. 精度解释

完整 projective value 比 activation bit 丰富得多，但对 future language

> “projective resource 是否越过第一个整数阈值？”

而言，所有低于 1 的数值都 exact-equivalent。

外部计数 theorem 又说明这个 coarse quotient 极端不平衡：随规模增大，一个 fiber 几乎吞掉整个有限宇宙。

因此需要区分：

- **state complexity**：quotient 只有两个标签；
- **incidence complexity**：其中一个标签按 power law 稀疏；
- **exact value precision**：只有进入 activated layer 后才真正需要。

## 6. Prior-art 边界

De Bruijn theorem 及其 radical-counting 后果属于外部前人数学。P025-T135 只是 Stage 64 projective compiler 在 `T=1` 的 specialization 再接该 prior theorem。

项目侧价值是识别 explicit projective precision state 中的 sparse activation basin，不对计数 theorem 主张优先权。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_projective_activation.py`；
- `tests/test_abc_projective_activation.py`。

代码只保存 exact finite activation classification，不实现外部渐近计数 theorem。

## 8. 下一前沿

Hard block 不存在。继续：

1. 研究 sparse activated layer **内部**的 `sigma_proj` 条件分布；
2. 使用 Stage 65 将 activated states 分成 c-oriented 与 side-oriented；
3. 检查 activated layer 是否能针对有用 downstream queries 再压成小于完整 weighted-radical tuple 的 exact state；
4. 把 `state cardinality / incidence sparsity / value precision` 的区分 Relay 给 A2/P023。
