# 因果吞并 02 —— 从坍缩 multiplicity 导出有限测度，概率只做后表示

状态：`CROSS-ROUTE RESEARCH WIP / EXACT FINITE COUNTING THEOREMS + EXECUTABLE REFERENCE`

归属建议：一般 fiber multiplicity / collision mathematics 归 A1/P010/P011；本文件在 A3 branch 作为 cross-route 实验来源，稳定母定理应通过 Relay 回流 A1，而不是长期复制在 A3。

## 1. 目标

传统有限概率论通常先给一个 probability space / measure，再讨论映射后的分布。

这里反过来。

进取数论已有有限确定性坍缩：

\[
F:X\to Y,
\qquad |X|=N.
\]

fine states 是显式的一个个离散状态。每个 fine state 本身只贡献一个 unit count：

\[
1.
\]

不先引入概率。

## 2. CM-01 —— coarse weight 由 unit-1 multiplicity 自动产生

对 reachable coarse state：

\[
m_F(y)=|F^{-1}(\{y\})|.
\]

对 coarse event：

\[
A\subseteq \operatorname{im}(F),
\]

定义：

\[
\boxed{
\mu_F(A)
:=
|F^{-1}(A)|
=
\sum_{y\in A}m_F(y).
}
\]

这个量不是先验 measure；它只是：

> **有多少个 fine unit-1 被当前坍缩送入该 coarse event。**

所以 singleton 权重：

\[
\mu_F(\{y\})=m_F(y).
\]

总权重：

\[
\boxed{\mu_F(\operatorname{im}(F))=N.}
\]

## 3. CM-02 —— 有限可加性不是公理，而是 fiber 分拆定理

若：

\[
A\cap B=\varnothing,
\]

则：

\[
F^{-1}(A\cup B)
=
F^{-1}(A)\sqcup F^{-1}(B).
\]

因此：

\[
\boxed{
\mu_F(A\cup B)
=
\mu_F(A)+\mu_F(B).
}
\]

所以在有限确定坍缩上，counting measure 的有限可加性来自 disjoint fiber union，而不是另加 measure axiom。

## 4. CM-03 —— 后续坍缩 = integer pushforward

再给：

\[
G:Y\to Z.
\]

P011 已有：

\[
\boxed{
m_{G\circ F}(z)
=
\sum_{G(y)=z}m_F(y).}
\]

因此 coarse weight 的更新只做整数求和。

对：

\[
B\subseteq Z,
\]

有：

\[
\boxed{
\mu_{G\circ F}(B)
=
\mu_F(G^{-1}(B)).
}
\]

传统 pushforward measure 在这个有限 regime 中只是 collapse multiplicity 的重写。

## 5. CM-04 —— probability 不再是 primitive

若某外部任务确实要输出传统有限概率，可以再定义 exact count pair：

\[
\boxed{
P^\#_F(A)
=
(\mu_F(A),N).
}
\]

例如传统：

\[
2/5
\]

在 core 中先保留为：

\[
(2,5).
\]

比较：

\[
(a,b)\ ?\ (c,d)
\]

只需比较：

\[
\boxed{ad\ ?\ cb.}
\]

不需要 float，也不需要 true division。

只有在 API/外部解释层明确要求时，才把 exact count pair 渲染成 rational/decimal probability。

## 6. CM-05 —— 条件概率先退回条件计数

给 fine-state event：

\[
A,B\subseteq X,
\qquad B\neq\varnothing.
\]

primitive object 先定义成：

\[
\boxed{
C^\#(A\mid B)
=
(|A\cap B|,|B|).
}
\]

仍然是两个整数。

传统条件概率：

\[
P(A\mid B)=|A\cap B|/|B|
\]

只是当额外采用“`B` 中所有 fine states 使用相同 unit sampling weight”的解释后，对该整数对做的后表示。

因此：

> **conditional count 是因果/组合对象；conditional probability 还需要额外 stochastic semantics。**

## 7. 与“1 是 LEGO unit”的关系

这条路线和当前项目最底层直觉直接一致。

fine states 中每一个基本状态只贡献：

\[
1.
\]

坍缩不会把这个 `1` 改成别的数；它只把多个不同 fine states 合并到同一个 coarse state。

于是 coarse weight 自然是：

\[
\boxed{1+1+\cdots+1=m_F(y).}
\]

所以 measure-like weight 并不是从连续长度/面积/概率密度中引入，而是 unit identity 在 many-to-one collapse 下的纯整数累积。

## 8. 与 P011 collision spectrum 的关系

`m_F(y)` 给出 coarse state 吞掉多少 unit histories。

P011：

\[
J_k(F)=\sum_y\binom{m_F(y)}k
\]

进一步读取这些 coarse weights 内部有多少 `k` 元历史子集已经合流。

因此当前层级更像：

\[
\boxed{
\text{unit count}
\to
\text{fiber multiplicity}
\to
\text{collision spectrum}
\to
\text{optional normalized probability/entropy rendering}.
}
\]

而不是：

\[
\text{probability measure}
\to
\text{再解释 collapse}.
\]

## 9. 吞并边界

当前只能说**有限 counting measure** 被第一阶段吞并。

不能未经证明扩大为：

- 任意 non-uniform probability measure；
- 连续 probability density；
- Lebesgue measure；
- stochastic dynamics；
- quantum probability amplitude。

这些结构都包含额外信息，不是单靠 finite collapse multiplicity 自动产生。

因此当前状态：

- finite counting measure：`CAUSAL_DERIVED`；
- uniform finite probability representation：`SHADOW_FORMULA + extra sampling interpretation`；
- general probability：尚未吞并；
- continuous measure：尚未吞并。

## 10. 可执行参考

新增：

- `src/enterprise_math/causal_count_measure.py`；
- `tests/test_causal_count_measure.py`。

覆盖：

- fiber multiplicity；
- event count；
- postcomposition integer pushforward；
- exact count ratio；
- fraction-free ratio comparison；
- conditional count pair。

## 11. 下一步

1. 检验 P011 `J_k` 是否能“吞并”有限概率中的 higher moments / collision probability，而不先除以 `N^k`；
2. 将 product-map multiplicity law 与传统 independence product rule 比较，区分结构独立与统计独立；
3. 研究一般 integer weights 是否可由 repeated unit collapse 生成，还是需要真正额外 measure data；
4. 如果需要额外权重，明确这正是 probability 无法被纯 collapse 完全吞并的边界；
5. Relay 到 A1/P010/P011 owner。
