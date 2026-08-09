# Causal Signature Product Law —— 独立 LEGO 子系统的签名组合与因果维数可加性

状态：`CROSS-ROUTE RESEARCH WIP / EXACT INDEPENDENT-PRODUCT THEOREM + INTEGER SPECIALIZATION`

## 1. 目标

Causal Signature Core 若真能替代“先给高维 Cartesian space”，必须证明独立子系统可以直接从各自 signature 生成 joint state，而不是每升一维都重新定义一套数学。

## 2. 独立 causal systems

系统 `A`：

- state `X`；
- operation language `Omega_A`；
- observations `O_A`；
- signature `Sigma_A`。

系统 `B` 同理。

独立组合要求：

1. operation 只在各自 subsystem 内作用；
2. observation 可以分别读取两个 subsystem；
3. 不额外加入 cross interaction observation。

记独立组合为：

\[
A\boxtimes B.
\]

## 3. CP-01 —— signature factorization

对 joint state：

\[
(x,y)\in X\times Y,
\]

以及独立 operation/observation pair，joint experiment result 只是两个 component results 的有序对。

因此：

\[
\boxed{
\Sigma_{A\boxtimes B}(x,y)
=
(\Sigma_A(x),\Sigma_B(y)).
}
\]

这里右边表示带完整 operation/observation labels 的 signature product。

## 4. CP-02 —— future equivalence factorization

由 CP-01：

\[
\boxed{
(x,y)\equiv_{A\boxtimes B}(x',y')
\iff
x\equiv_Ax'
\text{ 且 }
y\equiv_By'.
}
\]

所以独立系统里没有额外 hidden cross distinction。

## 5. CP-03 —— quotient product 是 signature law 的 shadow

于是：

\[
\boxed{
(X\times Y)/\equiv_{A\boxtimes B}
\cong
(X/\equiv_A)\times(Y/\equiv_B).
}
\]

这条公式不再被当作“product quotient 的抽象代数事实”放在最前面。

因果顺序是：

\[
\boxed{
\text{independent signature factorization}
\to
\text{future equivalence factorization}
\to
\text{traditional quotient product shadow}.
}
\]

## 6. CP-04 —— 因果维数可加

在 integer-linear special case 中，两个 subsystem 的 future-visible row spaces 位于不同 LEGO slot blocks。

因此 joint visible space 是 direct block sum，得到：

\[
\boxed{
\dim_{causal}(A\boxtimes B)
=
\dim_{causal}(A)
+
\dim_{causal}(B).
}
\]

这给“维数相加”一个新的解释：

> **独立 subsystem 增加了多少新的 future-distinguishable freedom。**

不是：

> 先声明多了几个 Cartesian coordinates。

## 7. 与“1 在任意维仍是 1”的关系

组合两个 subsystem 并不会改变任何 unit 的 value。

unit 仍然是：

\[
1.
\]

变化的是：

- relation slots 增加；
- operation language 形成 product；
- future signature 增加独立 component；
- causal dimension 因新增独立 distinction 而增加。

因此：

\[
\boxed{
\text{dimension addition}
=
\text{independent distinguishability addition},
\quad
1\text{ itself unchanged}.
}
\]

## 8. CP-05 —— counting weight 同时可乘

若 subsystem collapse fibers 大小分别为：

\[
m_A(a),
\qquad
m_B(b),
\]

独立 product state `(a,b)` 的 fine history fiber 是 Cartesian product：

\[
F_A^{-1}(a)\times F_B^{-1}(b).
\]

所以：

\[
\boxed{
m_{A\boxtimes B}(a,b)=m_A(a)m_B(b).}
\]

这不是额外 probability independence axiom；它来自 independent fine-state composition。

传统 product measure/probability rule 只有在进一步 normalization/sampling interpretation 后才出现。

## 9. CP-06 —— interaction 是 product law 的 failure

如果 joint system 出现：

- cross operation；
- cross observation；
- one subsystem 的 operation 依赖另一个 subsystem state；
- joint response 不能由 component signatures 重建；

那么：

\[
\Sigma_{AB}\neq(\Sigma_A,\Sigma_B).
\]

这时 product factorization 失败。

所以：

\[
\boxed{
\text{interaction}
=
\text{independent signature factorization 的失败}.
}
\]

这给 LEGO interaction spectrum 又一个更高层的因果定义候选：具体 `I(S)` 应解释为 signature product law 的局部 defect，而不只是 inclusion–exclusion coefficient。

## 10. 传统 direct product / tensor 的位置

当前能被吞并的是**独立 product**。

不能因为传统数学常用，就自动引入：

- tensor product；
- Hilbert-space tensor product；
- Kronecker product 作为 ontology；
- entanglement；
- multilinear completion。

Kronecker/block matrix 可以作为 independent operation 的 `COORDINATE_TOOL`，但不是底层 composition 本体。

## 11. 可执行参考

新增：

- `src/enterprise_math/causal_product_system.py`；
- `tests/test_causal_product_system.py`。

integer-linear tests 验证：

- block-independent operation；
- observation 无 cross terms；
- causal visible rank 精确可加。

## 12. 下一步

1. 定义 signature coupling defect，衡量 product law 失败时最少需要补多少 cross relation；
2. 连接 LEGO interaction spectrum，证明 pair interaction 是否等价于某类 signature factorization defect；
3. 研究 dimension contraction 是否是 product signature 的 causal quotient，而非坐标删除；
4. 检验 P019/A3 tagged contraction 是否能重新解释为 independent/coupled signature coarse-graining；
5. 只有证明必要时才引入 tensor-like traditional machinery。
