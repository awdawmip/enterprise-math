# 因果吞并 04 —— 用 LEGO interaction spectrum 取代“先验非线性/泰勒”视角

状态：`CROSS-ROUTE RESEARCH WIP / EXACT FINITE INTERACTION DECOMPOSITION`

## 1. 目标

如果线性已经被重新定义为：

\[
T(x\oplus y)=T(x)\oplus T(y),
\]

那么“非线性”也不应该继续默认由 polynomial degree、导数、Jacobian 或 Taylor expansion 来定义。

对有限 LEGO unit system，更直接的问题是：

> 多个 unit 同时存在时，是否出现任何无法由较低阶 unit effects 相加解释的新 effect？

## 2. unit subset response

取一组带标签 unit blocks：

\[
S=\{1,\ldots,n\}.
\]

对任意 subset：

\[
A\subseteq S,
\]

观测 operation response：

\[
T(A)\in\mathbb Z^m.
\]

这里 `A` 本身就是“哪些 unit 当前共同存在”。

## 3. CI-01 —— pair interaction

两个 unit `i,j` 的 pair interaction 定义为：

\[
\boxed{
I(\{i,j\})
=
T(\{i,j\})
-T(\{i\})
-T(\{j\})
+T(\varnothing).
}
\]

若：

\[
I(\{i,j\})=0,
\]

则这两个 unit 的 joint response 完全由 baseline + 两个单 unit response 决定。

若不为零，则出现真实 pair interaction。

## 4. CI-02 —— 任意阶 exact interaction

对任意 finite subset `A`：

\[
\boxed{
I(A)
=
\sum_{B\subseteq A}
(-1)^{|A|-|B|}T(B).
}
\]

这只是有限整数加减。

`I(A)` 的解释：

> **只有当 `A` 中这些 units 共同存在时才无法被所有更低阶 subset effects 完全解释的剩余 effect。**

因此 interaction order 直接由 LEGO coexistence 产生。

## 5. CI-03 —— exact reconstruction

Boolean subset lattice 上的有限 Möbius inversion 给出：

\[
\boxed{
T(A)=\sum_{B\subseteq A}I(B).
}
\]

所以 interaction spectrum：

\[
\{I(B):B\subseteq S\}
\]

不是近似 expansion，而是 operation response 的 exact finite decomposition。

没有：

- 极限；
- epsilon；
- 导数；
- Taylor remainder；
- 连续变量。

## 6. CI-04 —— LEGO-linearity 是 interaction spectrum 的退化情形

若：

\[
T(\varnothing)=0,
\]

且所有：

\[
|A|\ge2
\]

的 interaction 都为零，那么：

\[
T(A)=\sum_{i\in A}I(\{i\}).
\]

也就是 unit effects 完全独立相加。

因此：

\[
\boxed{
\text{LEGO additive operation}
=
\text{higher interaction spectrum identically zero}.
}
\]

这使“线性”成为 interaction-free regime，而不是预先给定向量空间后再定义的性质。

## 7. CI-05 —— operation order 的新定义

定义：

\[
\boxed{
\operatorname{ord}_{interaction}(T)
=
\max\{|A|:I(A)\neq0\}.
}
\]

于是：

- order 0：只有 baseline；
- order 1：independent-unit additive response；
- order 2：存在 pair interactions，但无更高 interaction；
- order 3：存在 genuine three-body effects；
- 以此类推。

这不是传统 polynomial degree 的直接重命名，因为 primitive variable 不是连续 scalar，而是 unit coexistence relation。

## 8. CI-06 —— 为什么这可能比“离散微分”更适合进取数论

我们可以把 inclusion–exclusion 公式叫 finite difference，但这样会再次让研究语言滑回“微积分的离散版”。

更符合当前 ontology 的解释是：

\[
\boxed{
\text{interaction}
=
\text{联合存在所新增的 causal effect}.
}
\]

Möbius inversion只是 exact accounting tool。

因此工具与本体分离：

- Möbius inversion：传统 `COORDINATE_TOOL / proof tool`；
- LEGO interaction：因果对象；
- Taylor/derivative：当前不需要。

## 9. 与 P010/P011 的潜在连接

P010/P011 已研究 many-to-one collapse、fiber merge 与 collision spectra。

这与当前 interaction spectrum 很可能有一条深连接：

- `J_k` 统计已有多少 `k` 元 histories 发生 collapse collision；
- `I(A)` 统计一个具体 `k` 元 unit set 同时存在时产生多少不可约 joint effect。

二者并不相同：

\[
\boxed{
\text{collision count}
\neq
\text{interaction value}.
}
\]

但它们都把传统“高阶统计/非线性”重新解释成 finite unit relations。

下一阶段应研究是否存在 operation-specific bridge：例如 collision engine 的 pair interaction 是否精确由 P011 `J_2` 增量控制。

## 10. 与传统 polynomial/Taylor 的关系

如果某个传统多项式函数限制在 binary unit cube：

\[
\{0,1\}^n,
\]

那么它当然也有 Boolean Möbius expansion。

因此不能把 inclusion–exclusion 本身当作项目原创。

真正研究问题是反方向：

> Enterprise Math 是否可以把 finite interaction spectrum 作为 primitive nonlinear description，而把 polynomial/Taylor representation 降为只有在额外连续/代数结构存在时才使用的 shadow？

当前状态：`NOVELTY_UNVERIFIED`。

## 11. 吞并边界

当前 exact result 只覆盖：

- finite labeled unit subsets；
- integer-vector responses；
- complete/downward-closed subset observations。

尚未解决：

- repeated indistinguishable units 的 multiset interaction；
- large-count state 上如何避免 `2^n` subset explosion；
- interaction 与 capacity-weighted A3 relation 的最小充分编码；
- causal time ordering；
- irreversible interaction history；
- continuous variables。

因此目前不能声称已取代所有 nonlinear analysis。

## 12. 可执行参考

新增：

- `src/enterprise_math/lego_interaction_spectrum.py`；
- `tests/test_lego_interaction_spectrum.py`。

回归覆盖：

- additive response 的所有 pair/higher interactions 精确为 0；
- pure pair interaction；
- pure three-body interaction；
- nonzero baseline；
- full exact reconstruction。

## 13. 下一步

1. 推广到 multiset / repeated unit counts，避免把相同 `1` 人为标签化；
2. 寻找从 P011 collision spectrum 到 interaction spectrum 的 operation-specific bridge；
3. 判断 `interaction order` 是否可以成为 nonlinear causal complexity 的一部分；
4. 研究 interaction 在 dimension contraction / partition quotient 下如何聚合；
5. 优先寻找递推或局部闭式，避免 exponential subset enumeration 成为底层算法。
