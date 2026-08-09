# Causal LEGO Fiber Composition —— 同一个 Fiber 分解生成 Sum-Product、Min-Plus 与 Boolean Shadows

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE LEGO THEOREMS`

## 1. 核心纠偏

不能因为传统动态规划、半环、卷积工具成熟，就先把某个 algebra 当作底层。

真正先发生的是 LEGO coarse block 的 fine-lift 分解。

对 `m` 个 nonnegative fine slots 与 coarse total `c`，定义：

\[
\mathcal F_m(c)=\{(a_1,\ldots,a_m)\in\mathbb N^m:\sum_i a_i=c\}.
\]

`1` 仍然是一个 unit；`m` 只是它可处于多少 fine relation slots 的结构信息。

## 2. FC-01 —— fiber composition law

把 `m+n` 个 slots 分成左 `m` 个与右 `n` 个。

每一个 full fine lift 唯一决定左总量：

\[
a\in\{0,\ldots,c\}.
\]

反之，给：

- 一个 `a`；
- 一个左 lift `u in F_m(a)`；
- 一个右 lift `v in F_n(c-a)`；

可以唯一拼成一个 `(m+n)`-slot lift。

因此存在 exact disjoint decomposition：

\[
\boxed{
\mathcal F_{m+n}(c)
\cong
\bigsqcup_{a=0}^{c}
\mathcal F_m(a)\times\mathcal F_n(c-a).
}
\]

这条 set/fiber identity 才是本体。

## 3. FC-02 —— counting observation 生成 sum-product convolution

定义 fine-lift multiplicity：

\[
H_m(c)=|\mathcal F_m(c)|.
\]

对 FC-01 取 cardinality：

\[
\boxed{
H_{m+n}(c)
=
\sum_{a=0}^{c}
H_m(a)H_n(c-a).
}
\]

传统 convolution 不是先验操作；它来自：

- alternative coarse splits `a` 之间做加法；
- 左右独立 fine choices 之间做乘法。

闭式：

\[
\boxed{H_m(c)=\binom{c+m-1}{m-1}.}
\]

传统 stars-and-bars / Vandermonde 只是该 fiber law 的 counting shadow/proof tool。

## 4. FC-03 —— minimum additive cost 生成 min-plus convolution

若每个 fine lift 有 additive block cost，且我们问的不是“多少种”而是“最低 cost”，则同一个 FC-01 自动给：

\[
\boxed{
\Psi_{m+n,s}(c)
=
\min_a
\left[
\Psi_{m,s}(a)+\Psi_{n,s}(c-a)
\right].
}
\]

因此 min-plus 不是新的 geometry ontology，而是：

> 对同一个 LEGO fiber composition，选择“minimum additive cost”这个 observation 后产生的 algebra shadow。

A3 `dimension_contraction.py` 已实现该 family。

## 5. FC-04 —— existence observation 生成 Boolean composition

若只问某个 constrained fiber 是否存在 fine lift，则：

\[
\boxed{
E_{m+n}(c)
=
\bigvee_a
\big(E_m(a)\wedge E_n(c-a)\big).
}
\]

因此 Boolean OR/AND convolution 同样不是 foundation；它是 existence/support observation 的 shadow。

对 unconstrained nonnegative allocation，当然所有 `c>=0` 都存在；该式在 support constraint、guard、capacity、forbidden-state 问题中才有非平凡作用。

## 6. FC-05 —— observation algebra principle

当前候选原则：

\[
\boxed{
\text{同一个 causal fiber composition}
+\text{不同 observation question}
\to
\text{不同传统 algebra shadow}.
}
\]

已严格出现：

- counting -> `sum/product`；
- minimum additive cost -> `min/+`；
- existence -> `OR/AND`。

因此未来遇到 max-plus、tropical、generating function 等工具时，优先问：它是否只是同一个 fiber composition 在另一种 observation aggregator 下的 shadow，而不是另加数学本体。

## 7. FC-06 —— exact dimension-lowering difference law

counting shadow 还有：

\[
\boxed{
H_m(c+1)-H_m(c)=H_{m-1}(c+1),\qquad m\ge2.
}
\]

纯 LEGO 证明：

1. 从 `F_m(c)` 到 `F_m(c+1)`，给一个指定 slot 加 1，得到 injection；
2. injection 没覆盖的 states 恰好是该 slot 为 0 的 `(c+1)`-unit lifts；
3. 删除该空 slot，正好得到 `F_(m-1)(c+1)`。

所以 difference 不是“近似 derivative”，而是精确剥掉一个 hidden slot freedom。

反复得到：

\[
\boxed{
\Delta^rH_m(c)=H_{m-r}(c+r)
}
\]

以及：

\[
\boxed{
\Delta^{m-1}H_m(c)=1,
\qquad
\Delta^mH_m(c)=0.
}
\]

因此：

\[
\boxed{
m-1=\text{fiber multiplicity 的 exact difference depth}.}
\]

这与 relation-rank dimension、contraction depth、ball-growth difference dimension 给出同一个整数。

## 8. FC-07 —— `1` 不变，但 relation possibilities 增加

对一个 unit：

\[
H_m(1)=m.
\]

这不是说 unit value 变成 `m`。

含义是：

- coarse total 仍然是 `1`；
- fine level 有 `m` 个可能 placements。

所以：

\[
\boxed{
1\text{ remains }1;
\quad
\text{dimension increases the ways the same unit can relate/place}.
}
\]

## 9. FC-08 —— 同一个 `(m,c)` 生成 fiber multiplicity 与 collision extremum

A3 tagged contraction 中的 `(block capacity m, total c)` 现在有更本体化解释。

它同时确定：

### 全部 fine lifts 数量

\[
H_m(c)=\binom{c+m-1}{m-1}.
\]

### minimum power/collision cost

\[
\Psi_{m,s}(c)=\min_{\sum a_i=c}\sum_i|a_i|^s.
\]

### balanced minimizer 数

若 `c=mq+r`：

\[
\boxed{N_{min}(m,c)=\binom mr.}
\]

因此 capacity tag 不是“数值外加 precision 声明”。它是 coarse fiber 的结构参数：决定可能性总数、minimum collision behavior 与 minimum-state multiplicity。

## 10. 与 P011 collapse spectrum 的关系

一个 coarse partition 的每个 coarse state 都有 fiber multiplicity `H`。因此在有限总 unit count 下，可以直接把这些 multiplicities 送入 P011：

\[
J_k=\sum_{coarse\ states}\binom{H(coarse)}k.
\]

于是 dimension contraction 也成为 Causal Collapse Spectrum 的一个具体 role。

## 11. 传统数学的 status

- stars-and-bars：`COORDINATE/COUNTING TOOL`；
- Vandermonde convolution：`SHADOW_FORMULA`；
- sum-product convolution：`CAUSAL_DERIVED SHADOW`；
- min-plus convolution：`CAUSAL_DERIVED SHADOW`；
- Boolean convolution：`CAUSAL_DERIVED SHADOW`；
- generic semiring ontology：尚未作为 foundation 接纳。

## 12. 可执行资产

- `src/enterprise_math/lego_partition_fiber.py`
- `tests/test_lego_partition_fiber.py`
- `src/enterprise_math/dimension_contraction.py`

## 13. 下一步

1. 定义一般 “fiber question / aggregator” 接口，但避免把 abstract semiring 先升级成 ontology；
2. 研究 P011 collision spectrum 是否也由 FC-01 递归生成；
3. 把 graph-ball / radial-ball 的高维递推重新解释成特定 fiber questions；
4. 检查材料碰撞/回弹中的 threshold、min/max、carry 是否能统一为同一 fiber composition 的 observation shadows；
5. 研究 interaction coupling 后，FC-01 的 direct product 是否被怎样修改。
