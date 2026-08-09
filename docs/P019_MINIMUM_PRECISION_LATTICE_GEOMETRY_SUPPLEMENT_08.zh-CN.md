# P019 补充 08 —— Future-Composition 等价与安全 Trace 消去

状态：`RESEARCH WIP / ABSTRACT FINITE THEOREMS PROVED`

## 1. 为什么不存在无条件的“最小 trace”

Supplement 07 表明：

- minimum value 可以强烈压缩；
- minimum provenance 也可以结合地压缩；
- one-step full fiber relation 可以压成 `[L,U]`；
- selected multi-step boundary witness 却对 oriented contraction history 敏感。

因此“最小需要保留多少历史”没有脱离任务的唯一答案。

正确问题必须是：

> 给定未来允许执行的运算与允许读取的观测，两个 fine states 在未来是否仍可能被区分？

只有未来永远无法区分的 states 才能安全合并。

## 2. future program family

设有限 fine state space 为 `X`。

给定有限个 deterministic integer/discrete operations：

\[
\mathcal A=\{T_a:X\to X\}_{a\in A},
\]

以及当前允许读取的 observation

\[
O:X\to Z.
\]

对有限 operation word

\[
w=a_1a_2\cdots a_k
\]

记

\[
T_w=T_{a_k}\circ\cdots\circ T_{a_1}.
\]

`w` 可以为空，此时 `T_w=id`。

## 3. P019-X13 —— future-composition equivalence

定义

\[
\boxed{
x\equiv_{\mathcal A,O}y}
\]

当且仅当对所有有限 operation words `w` 都有

\[
\boxed{
O(T_w(x))=O(T_w(y)).
}
\]

这是等价关系。

其含义不是“x,y 本体相同”，而是：在已经声明的未来操作/观测语言内，没有任何有限 future program 能把二者区分。

## 4. P019-X14 —— coarsest safe quotient

设一个候选 summary / collapse 为

\[
q:X\to Y.
\]

称 `q` 对 `(A,O)` **future-safe**，若

\[
q(x)=q(y)
\Longrightarrow
x\equiv_{\mathcal A,O}y.
\]

也就是说，同一个 coarse state 内部的所有 fine states 对未来程序完全等价。

定义 canonical behavioral quotient

\[
\pi_*:X\to X/{\equiv_{\mathcal A,O}}.
\]

则：

\[
\boxed{
\pi_*\text{ 是最粗的 future-safe quotient。}
}
\]

更精确地：若 `q` future-safe，则存在唯一良定义映射

\[
h:q(X)\to X/{\equiv}
\]

使

\[
\boxed{
\pi_*=h\circ q.
}
\]

所以任何 future-safe summary 都只能比 canonical quotient 更细，不能更粗。

### 证明

若 `q(x)=q(y)`，future-safe 性给出 `x equiv y`，因此把 `q(x)` 映到 `[x]` 不依赖 representative，`h` 良定义。∎

这把“最小充分 trace”从经验设计变成一个 quotient universal property。

## 5. 有限 future horizon

实际研究常常只要求未来 `L` 步内 composition exact。

定义

\[
x\equiv_L y
\]

当且仅当对所有长度 `|w|<=L` 的 operation words：

\[
O(T_w(x))=O(T_w(y)).
\]

于是

\[
\equiv_0
\supseteq
\equiv_1
\supseteq
\equiv_2
\supseteq\cdots
\]

随着 lookahead 增加，partition 只能细化，不能重新合并。

定义整数 future-resolution count

\[
Q_L=|X/{\equiv_L}|.
\]

则

\[
\boxed{Q_{L+1}\ge Q_L.}
\]

对单个 state 定义 residual ambiguity multiplicity

\[
A_L(x)=|[x]_L|.
\]

则

\[
\boxed{A_{L+1}(x)\le A_L(x).}
\]

这里不需要 log/entropy；future resolution 本身就是整数 partition refinement。

## 6. P019-X15 —— 一旦 finite refinement 停止，就永久稳定

若对某个 `L`：

\[
\equiv_{L+1}=\equiv_L,
\]

则

\[
\boxed{
\equiv_k=\equiv_L
\quad\forall k\ge L.
}
\]

### 证明

若 `x equiv_L y`，由 `equiv_(L+1)=equiv_L`，对每个 generator `T_a` 和任意长度至多 `L` 的 word `v`：

\[
O(T_v(T_a(x)))
=
O(T_v(T_a(y))),
\]

因为 `av` 总长度至多 `L+1`。

所以

\[
T_a(x)\equiv_L T_a(y).
\]

即 `equiv_L` 已对所有 generators 稳定，是 operation congruence。归纳即可得到任意未来长度。∎

若 `X` 有限，则严格 refinement 每次至少增加一个 equivalence class，而 class 总数不超过 `|X|`，所以过程有限终止。

定义第一次稳定的层级

\[
\boxed{H_{comp}}
\]

为 **composition horizon**。

它表示：再看更远的未来，已经不会迫使状态表示继续细分。

## 7. 与 P018 的直接关系

P018 把 precision refinement 本身提升为数学操作。

这里得到另一类纯 partition refinement：

\[
\text{更长 future obligation}
\Rightarrow
\text{更细 state distinction}.
\]

所以 trace precision 可以被理解为：

`当前 observables 所需 precision + future composability 所需 precision`。

这不是围绕隐藏实数增加位数，而是在有限状态 partition 上增加可区分关系。

## 8. 与 P010/P011 的对偶方向

P010 的 forward many-to-one evolution 中，历史 fiber multiplicity 随时间可增加：

\[
M_{t+1}(x)\ge M_t(x).
\]

本补充的 future-lookahead partition 中，要求未来可组合性越长，ambiguity fiber 只会缩小：

\[
A_{L+1}(x)\le A_L(x).
\]

因此出现一个结构对偶：

- **真实 forward collapse**：history classes 合并；
- **研究者增加 future obligations**：summary classes 被迫拆开。

这两者不能混成同一个“信息量”。

## 9. 对 contraction trace 的具体分类

### 9.1 只问 minimum energy / ball membership

未来 operations 若只依赖

\[
E_{\mathbf m}^{(s)}(c),
\]

则

`visible totals + block sizes + power`

已经 future-safe。

完整 contraction history 是多余的。

### 9.2 只问 minimum-witness multiplicity

对 `s>1`，binomial remainder profile / provenance polynomial 可从当前 tagged state 重建。

history 仍可删除。

### 9.3 问 one-step full fiber relation

`[L,U]` 是 composition query 的最小候选局部 summary；它同时给出 endpoint 与 multiplicity。

### 9.4 问 selected multi-step boundary witness

Supplement 06/07 的反例说明最终 partition 不 future-safe。

当前已知充分 summary 是完整 oriented contraction flag。

### 9.5 问 exact historical identity

若 observation family 本身包含 fine witness identity，则

\[
x\equiv y\iff x=y
\]

在被观察的部分成立。

此时任何非平凡 history collapse 都不 future-safe。

## 10. full relation vs selected representative

这里得到一个关键纠偏。

对给定 coarse state、threshold 与 cost law，若未来问题只问：

> 哪些 fine witnesses 仍然可能？

则不需要保存真实 contraction tree；完整 relation 可以直接定义为当前 coarse fiber 的全部可行 preimages。

selected right-boundary representative 的非结合性来自**每层都做一次 canonical selection**，而不是 full relation 本身失去结合性。

这与 P021 的结论一致：

- witness relation 是 composition-complete primitive；
- cardinality 或单一 representative 是 relation 的 shadow；
- 只有证明 shadow 对未来 query safe，才允许删除 witness identity。

## 11. automorphism-safe quotient

P012/P019 已使用 graph automorphism orbit 作为 intrinsic relation/direction language。

若 future operation family 与 observation 都对某个 automorphism group `G` 协变/不变，则同一个 `G`-orbit 内的 fine witnesses 是候选可合并类。

但 orbit quotient 只有在完整 future language 下验证 safe 后才能使用。

`one orbit` 仍不等于“物理完全各向同性”；这里只讨论操作不可区分性。

## 12. 外部工具边界

future behavioral equivalence、automata state minimization、bisimulation/coarsest relational partition 与 partition refinement 均有成熟前人工作。

P019 不声称发明这些一般工具。项目要研究的是：

1. 把它们接到 finite-precision collapse / fiber / block-size tags；
2. 用它们精确定义“历史什么时候可以安全删除”；
3. 与 P010/P011/P018/P021 的 history、collision、precision、witness composition 统一。

合并前必须完成正式 source/lineage 登记。

## 13. 下一步

下一步优先：

1. 对 finite contraction toy systems 实现 partition-refinement reference algorithm；
2. 测量 `Q_L`, `A_L`, `H_comp`；
3. 找出 P019 boundary operations 下哪些 trace 部分最早失去 future distinguishability；
4. 研究 exact relation 可否用 interval / multiplicity / provenance polynomial 的组合压缩，而不退回整棵 witness tree；
5. 把结果与 P021 witness join 统一成一个 shared safe-collapse criterion。
