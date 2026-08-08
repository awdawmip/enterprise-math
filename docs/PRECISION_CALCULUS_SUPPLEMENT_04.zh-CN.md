# P018 —— 有限精度证明演算：补充 04

状态：`ACTIVE RESEARCH NOTE`  
范围：抽象有限精度系统、ambiguity multiplicity、first-decision shell，以及 precision 与 time 在 partition order 上的关系  
依赖：P018 第一到第四阶段与 P010/T012  
纪律：inverse/projective system、等价关系与 partition refinement 都是成熟数学；P018 不把这些一般结构据为原创。

## 1. 为什么 scale coordinate 已经不再是最基础对象

P018 现在已经拥有两条真正不同的 precision axis：

- **scale precision**：观测值是 Euclidean coarse state；
- **factor precision**：观测值是当前可见的 divisor witness。

它们的算术 detail 完全不同，但证明结构却相同。

这个共同结构比任意一条具体 precision coordinate 更基础。

设 `X` 为一个有限 terminal state set。一个 precision level `lambda` 由观测映射

\[
O_\lambda:X\to Y_\lambda
\]

表示。

两个 terminal state 在 precision `lambda` 下不可区分，当且仅当它们拥有相同观测值。

对 `x in X`，定义 precision fiber：

\[
[x]_\lambda
=
\{y\in X:O_\lambda(y)=O_\lambda(x)\}.
\]

每个 observation 因此在 `X` 上诱导一个 partition。

这里不需要 inverse limit、无限 terminal precision、metric 或隐藏连续体。

## 2. P018-T35 —— 抽象 refinement 判据与 projection map

状态：`PROVED`

若 fine level 上相等必然推出 coarse level 上相等：

\[
O_\mu(x)=O_\mu(y)
\Longrightarrow
O_\lambda(x)=O_\lambda(y),
\]

则称 `mu` 比 `lambda` 更细。

对有限 observation，这与存在唯一映射

\[
p_{\mu\to\lambda}:\operatorname{im}(O_\mu)\to\operatorname{im}(O_\lambda)
\]

满足

\[
\boxed{
O_\lambda
=
p_{\mu\to\lambda}\circ O_\mu
}
\]

等价。

证明：若多个 terminal state 共享一个 fine observation value，refinement 条件保证它们的 coarse observation value 相同，因此 projection 定义良好；因为 `im(O_mu)` 中每一个值都来自至少一个 terminal state，projection 又是唯一的。反向由复合式立即得到。∎

这就是 inverse/projective system 中相容 transition map 的有限 observation 版本。P018 刻意只保留当前问题实际出现的有限层。

## 3. P018-T36 —— Precision fiber 嵌套

状态：`PROVED`

若 `mu` refine `lambda`，则对任意 `x in X`：

\[
\boxed{
[x]_\mu\subseteq[x]_\lambda.
}
\]

因为若 `y` 位于 fine fiber，则 `O_mu(y)=O_mu(x)`；refinement 随即推出 `O_lambda(y)=O_lambda(x)`。∎

所以 precision refinement 本质上就是 observation partition 的 refinement。

## 4. P018-T37 —— Ambiguity multiplicity 单调不增

状态：`PROVED`

定义 precision `lambda` 下的 **ambiguity multiplicity**：

\[
A_\lambda(x)=|[x]_\lambda|.
\]

若 `mu` 比 `lambda` 更细，则

\[
\boxed{
A_\mu(x)\le A_\lambda(x).
}
\]

这是 T36 的基数形式。

它有直接有限含义：当前 observation 后，仍有多少 terminal state 与真实状态 `x` 相容。

不需要对数，也不需要概率。

## 5. P018-T38 —— 严格精化的充要条件

状态：`PROVED`

当 `mu` refine `lambda` 时，下列条件等价：

1. `A_mu(x) < A_lambda(x)`；
2. `[x]_mu` 是 `[x]_lambda` 的真子集；
3. 存在 `y in X`，使

\[
O_\lambda(y)=O_\lambda(x),
\]

但

\[
O_\mu(y)\ne O_\mu(x).
\]

因此 ambiguity 严格下降，当且仅当下一 precision observation **真的劈开了当前包含 x 的 coarse fiber**。

如果新增 detail 只发生在状态空间其他位置，而没有劈开 `x` 所在 fiber，那么对 `x` 来说这一级 precision 没有新增证明信息。

这正是 P010 中“严格历史合流需要当前可达 fiber 真正发生碰撞”的 precision-direction 对应物。

## 6. P018-T39 —— Ambiguity gain 望远镜分解

状态：`PROVED`

设有限 refinement chain 为

\[
\lambda_0\preceq\lambda_1\preceq\cdots\preceq\lambda_m.
\]

定义

\[
g_i(x)=A_{\lambda_{i-1}}(x)-A_{\lambda_i}(x).
\]

则

\[
\boxed{g_i(x)\ge0}
\]

并且

\[
\boxed{
\sum_{i=1}^m g_i(x)
=A_{\lambda_0}(x)-A_{\lambda_m}(x).
}
\]

所以 ambiguity reduction 本身也拥有一个有限 precision-shell 分解。

`g_i=0` 表示新层对当前状态没有新增区分能力；`g_i>0` 则精确记录这一级排除了多少原本相容的候选状态。

## 7. P018-T40 —— 任意 Boolean predicate 的 certificate 持久性

状态：`PROVED`

令

\[
P:X\to\{\text{true},\text{false}\}
\]

为任意 Boolean predicate。

在 precision `lambda` 下，用整个 fiber 上的 predicate value 定义证书：

- `[x]_lambda` 中所有状态都满足 `P`：`TRUE`；
- `[x]_lambda` 中所有状态都不满足 `P`：`FALSE`；
- 否则：`UNRESOLVED`。

若 `mu` refine `lambda`，则 `lambda` 上已经得到的 TRUE 或 FALSE 在 `mu` 上仍保持相同。

证明：T36 给出 fine fiber 是 coarse fiber 的子集，所以在 coarse fiber 上已经常值的 predicate，在其任何子 fiber 上仍保持同一值。∎

这就是 Stage 3 的抽象形式。它已经不要求序、单调性、interval 或 homogeneous operation。

唯一需要的结构就是：**有限 fiber 嵌套。**

## 8. P018-T41 —— First-decision precision shell 分割 terminal set

状态：`PROVED`

固定一条有限 refinement chain 与 Boolean predicate `P`。

对每个 terminal state `x`，定义

\[
d_P(x)
\]

为 predicate certificate 第一次从 UNRESOLVED 变成 TRUE/FALSE 的 precision index；若始终未决定，则未定义。

于是

\[
D_j(P)=\{x:d_P(x)=j\}
\]

以及必要时的 terminal unresolved set

\[
D_\infty(P)=\{x:d_P(x)\text{ 未定义}\}
\]

共同构成 `X` 的不交分割。

它们就是 **first-decision precision shells**。

T33 的 least-prime-factor shell 是一个算术实例：合数第一次出现 compositeness witness 的 precision 就是其最小素因子；terminal prime 则在有限完备 horizon 才决定。

## 9. P018-T42 —— 有限 injective terminal precision 给出普遍完备性

状态：`PROVED`

若最终 observation `O_*` 在 `X` 上单射，则每个 terminal fiber 都是 singleton：

\[
\boxed{[x]_* = \{x\}.}
\]

所以

\[
\boxed{A_*(x)=1}
\]

对所有 `x` 成立。

因此对**任意 Boolean predicate** `P`，terminal certificate 必为 TRUE 或 FALSE，而不可能仍是 UNRESOLVED。

所以，只要一个有限 precision system 存在有限 injective terminal observation，它就在这个有限问题上拥有 universal decision horizon。

这给出 P018 一个重要基础边界：

> 有限问题上的 proof completeness 不需要无限精度极限；它只需要一个能够区分本问题所有 relevant terminal states 的有限 precision level。

更弱地，对某一个具体 predicate，只需要 predicate-complete observation，而不必要求 state-injective。平方盆地 factor precision 对 primality 就是这种情况。

## 10. P018-T43 —— Product precision fiber 等于轴 fiber 的交

状态：`PROVED`

设同一个有限 terminal state set 上有两个 precision observation：

\[
O_1:X\to Y_1,
\qquad
O_2:X\to Y_2.
\]

定义 product observation：

\[
O_{1\times2}(x)=(O_1(x),O_2(x)).
\]

则

\[
\boxed{
[x]_{1\times2}
=[x]_1\cap[x]_2.
}
\]

因此

\[
\boxed{
A_{1\times2}(x)
\le
\min\{A_1(x),A_2(x)\}.
}
\]

这给出了组合不同 precision axis 的精确代数。

特别地，scale precision 与 factor precision 可以同时施加，而无需假装它们拥有同一种 detail。联合信息就是两个 terminal-state fiber 的交集。

这也直接指向 adaptive multi-axis proof：选择最能减少当前 relevant ambiguity 的那条 precision axis 进行 refinement。

## 11. P018-T44 —— Time 与 precision 在同一个 partition order 上反向运动

状态：`PROVED ORDER-THEORETIC RELATION`，**不是 categorical duality 主张**。

任意映射

\[
f:X\to Y
\]

都会在 `X` 上诱导 kernel equivalence relation，从而得到 partition

\[
\Pi(f).
\]

按 refinement 排序 partition：`P <= Q` 表示 `P` 的每个 block 都包含于 `Q` 的某个 block。

### Precision direction

如果 `O_mu` refine `O_lambda`，则

\[
\boxed{
\Pi(O_\mu)\le\Pi(O_\lambda).
}
\]

precision 沿着 **更细 partition** 的方向移动；ambiguity fiber 被分裂，cardinality 单调不增。

### Time direction

令

\[
F_{t+1}=T_{t+1}\circ F_t.
\]

若两条 history 在 `F_t` 下已经相等，postcomposition 后必继续相等。所以

\[
\boxed{
\Pi(F_t)\le\Pi(F_{t+1}).
}
\]

time 沿着 **更粗 partition** 的方向移动；history fiber 被合并，cardinality 单调不减，这正是 T012 与 P010 的内容。

因此，precision refinement 与 deterministic forward time 是同一种数学对象——有限状态集合 partition lattice——上的两种反向单调运动。

这比之前的语言类比更强，但仍弱于 categorical duality。我们没有证明 inverse functor、adjunction 或 category equivalence。

当前严格结论只是：

\[
\boxed{
\text{precision：partition refinement / ambiguity loss},
\qquad
\text{time：partition coarsening / history merging}.
}
\]

## 12. 两个规范实例

### 12.1 Scale precision

固定一个有限 terminal scale `D`。对每个 `d|D`，定义

\[
O_d(x)=x//(D/d).
\]

若 `d|e|D`，则 `O_e` refine `O_d`，这就是第一至第三阶段的 Euclidean precision cell。

当 `d=D` 时 observation 就是 identity，因此单射。T42 随即给出：在选定有限 terminal domain 上存在 universal finite completeness。

### 12.2 Factor precision

固定一个平方盆地，令

\[
O_y(n)=D_y(n).
\]

随着 cutoff 增大，observation 通过新增 visible divisor witness 被精化。终点 `y=k` 的 factor observation 不必单射，但 Root-Factor Horizon 已保证它对特定 predicate“是否为素数”完备。

所以必须区分：

- **state completeness**：observation 单射；
- **predicate completeness**：observation 只需要分开某一 predicate 的 true/false classes。

P018 的 proof design 应优先寻找后者，因为它往往需要远少于完整状态重建的 precision。

## 13. 前人边界

inverse/projective system 中的相容 transition map 是成熟 category-theoretic 语言；等价关系、函数 kernel 与 partition refinement 都是成熟的基本数学。P018 不声称这些对象或 partition lattice ordering 是新发明。

当前要检验的是如下有限组合：

\[
\boxed{
\text{finite terminal state set}
+
\text{precision observations}
+
\text{compatible forgetting maps}
+
\text{ambiguity multiplicity}
+
\text{persistent predicate certificates}
+
\text{first-decision shells}
+
\text{multi-axis product precision}
+
\text{time 下的 opposite partition motion}.
}
\]

最重要的是，这一理论**不要求**进入 inverse limit。有限 terminal observation，或者仅对目标 predicate 已经完备的有限 horizon，就足够支持上述所有定理。

这一组合的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 14. 第五阶段状态

- P018-T35 abstract refinement / projection criterion：`PROVED`
- P018-T36 fiber nesting：`PROVED`
- P018-T37 ambiguity multiplicity monotonicity：`PROVED`
- P018-T38 strict ambiguity-drop criterion：`PROVED`
- P018-T39 telescoping ambiguity gains：`PROVED`
- P018-T40 arbitrary-predicate certificate persistence：`PROVED`
- P018-T41 first-decision shells：`PROVED`
- P018-T42 finite injective terminal completeness：`PROVED`
- P018-T43 product precision fiber intersection：`PROVED`
- P018-T44 precision/time opposite monotonicity on partition order：`PROVED`
- categorical time/precision duality：`NOT CLAIMED / OPEN`
- adaptive optimal precision selection：`NEXT`
- nonmonotone multi-axis proof search：`OPEN`

可执行检查位于 `src/enterprise_math/precision_system.py` 与 `tests/test_precision_system.py`。
