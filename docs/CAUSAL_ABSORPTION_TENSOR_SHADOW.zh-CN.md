# 因果吞并 06 —— Tensor-like 结构作为 LEGO 多边可加 Interaction 的 Shadow

状态：`CROSS-ROUTE RESEARCH WIP / EXACT FREE-INTEGER DERIVATION + NEGATIVE BOUNDARY`

## 1. 不先假设 tensor

此前已经得到：

- 单系统 operation 若尊重 LEGO composition，则 integer matrix 只是 unit effects 的坐标表；
- local interaction 与 causal coupling 不是同一个对象。

下一问是：传统 bilinear / tensor 为什么有时会自然出现？

本文件不把 tensor product 当 ontology，而从 cross interaction 对 LEGO 拼接的响应规律出发。

## 2. TS-01 —— pair interaction 的 separate LEGO additivity

设左系统 state `x`、右系统 state `y`，额外 cross effect：

\[
B(x,y).
\]

要求：

\[
B(x_1\oplus x_2,y)=B(x_1,y)\oplus B(x_2,y),
\]

\[
B(x,y_1\oplus y_2)=B(x,y_1)\oplus B(x,y_2),
\]

并要求空 multiplicity 不制造 cross effect。

在 signed free integer slot state 上，这就是对两个参数分别保持 LEGO composition。

## 3. TS-02 —— unit-pair effects 精确生成全部 response

设左边 unit generators 为 `e_i`，右边为 `f_j`。

定义 primitive pair effect：

\[
\boxed{b_{ij}=B(e_i,f_j).}
\]

若：

\[
x=\sum_i x_i e_i,
\qquad
y=\sum_j y_j f_j,
\]

则 repeated separate additivity 强制：

\[
\boxed{B(x,y)=\sum_{i,j}x_i y_j b_{ij}.}
\]

因此真正 primitive 的不是 tensor，而是：

> 每一种左 unit 与每一种右 unit 相遇时产生什么 effect。

传统 bilinear matrix / rank-2 tensor 是把 `b_ij` 排成坐标表的 shadow。

## 4. TS-03 —— converse

任意有限 unit-pair effect table `b_ij` 都通过：

\[
B(x,y)=\sum_{i,j}x_i y_jb_{ij}
\]

定义一个对两边分别 LEGO-additive 的 exact integer interaction。

所以在 free integer regime：

\[
\boxed{
\text{separate LEGO additivity}
\iff
\text{unit-pair effect table representation}.
}
\]

这才是传统 bilinear/tensor shadow 获得进入资格的因果条件。

## 5. TS-04 —— 多体推广

对 `r` 个 subsystem 的 cross effect：

\[
B(x^{(1)},\ldots,x^{(r)}),
\]

若它对每个 argument 都分别保持 LEGO composition，则由 unit-tuples 完全决定：

\[
\boxed{
B(x^{(1)},\ldots,x^{(r)})
=
\sum_{i_1,\ldots,i_r}
\left(\prod_{a=1}^{r}x^{(a)}_{i_a}\right)
B(e^{(1)}_{i_1},\ldots,e^{(r)}_{i_r}).
}
\]

传统 rank-`r` multilinear array / tensor 只是这些 unit-tuple effects 的坐标 shadow。

因此 tensor order 在这一 regime 下可以解释成：

> 一个不可约 effect 同时需要多少个 independently composable LEGO subsystems 才被触发，并且对每边 multiplicity 保持可加。

## 6. TS-C01 —— 非可加 interaction 不能被固定 pair table 吞掉

取单一 unit type：

\[
B(n,m)=\min(n,m).
\]

若固定 pair effect `b=B(1,1)=1` 能重建，则 bilinear shadow 会给：

\[
B(2,1)=2\cdot1\cdot1=2.
\]

但真实定义给：

\[
B(2,1)=1.
\]

矛盾。

所以 threshold、saturation、competition、capacity limit、winner-take-all 等 interaction 一般不能被 fixed tensor table 表示。

这类对象必须回到 LEGO interaction spectrum、causal signature 或其他 finite relation law，不允许为了传统 tensor 方便而硬线性化。

## 7. Tensor interaction 不等于 causal coupling

即使 `B(x,y)` 有非零 pair effects，只要 marginal signatures 已经足够重建 `x,y`，那么 `B(x,y)` 也可由 marginals 唯一计算，不增加 signature split。

所以：

\[
\boxed{
\text{tensor-like cross response}\not\Rightarrow\text{causal coupling}.
}
\]

反向也不成立：parity reachability constraint 可以制造高阶 causal coupling，而没有任何指定 bilinear cross response。

真正桥接仍是 fiber-descent：joint response 只有在同一个 marginal-signature fiber 内取不同值时，才新增 causal distinction。

## 8. 传统 tensor product 的位置

本阶段只因果导出：

- unit-pair effect table；
- separate-additive bilinear shadow；
- multi-additive unit-tuple shadow。

尚未因果导出：

- abstract tensor product 的全部 universal-property ontology；
- Hilbert tensor product；
- topological tensor completion；
- quantum tensor ontology。

如果未来这些传统结构只是方便统一表示 multi-additive maps，可列为 `COORDINATE_TOOL / SHADOW_FORMULA`；若需要额外 completion ontology，则仍留外部。

## 9. 可执行资产

- `src/enterprise_math/lego_pair_interaction.py`
- `tests/test_lego_pair_interaction.py`

## 10. 下一步

1. 把 unit-tuple multiadditivity 与 causal independence complex 的 minimal nonfaces 比较；
2. 判定什么条件下 irreducible coupling group 同时具有 exact multilinear shadow；
3. 对 saturation / threshold / carry interaction 寻找非 tensor 的原生 LEGO 合成律；
4. 若出现必须同时保留 pair-unit table 与 signature coupling spectrum 的情形，研究二者的最小联合状态，而不是直接升级为传统 tensor ontology。
