# P025 补充 123 —— Task-Relative Witness-Count Pushforward

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-witness-count-stage121`  
依赖：P025 补充 115、121–122  
硬阻断：`NONE`

## 1. Full ambient inversion 并不会自动获得许可

补充 121 已证明：`J(P)` 上 full ideal-count table 可以精确恢复 ambient witness multiplicity function。但 declared future 可能只读取 queried subposet

\[
Q\subseteq P
\]

中的 labels。

这种 future 不应恢复任何在 restriction 到 \(Q\) 后已经消失的 ambient distinction。

## 2. P025-D48 —— multiplicity pushforward

令

\[
w:J(P)\to\mathbf N
\]

为 ambient witness multiplicity。对每个 query ideal \(K\in J(Q)\)，定义 pushforward multiplicity

\[
\boxed{
\bar w_Q(K)
:=
\sum_{I\in J(P):\ I\cap Q=K}w(I).
}
\]

它把所有具有相同 declared-query state 的 ambient exact witnesses 合并。

总 multiplicity 守恒：

\[
\boxed{
\sum_{I\in J(P)}w(I)
=
\sum_{K\in J(Q)}\bar w_Q(K).
}
\]

## 3. P025-T271 —— query counts 是 pushforward 的 zeta transform

令 \(S\subseteq Q\) 为 raw query，则

\[
\begin{aligned}
c_P(S)
&=\sum_{I\supseteq S}w(I)\\
&=\sum_{K\in J(Q):K\supseteq S}\bar w_Q(K).
\end{aligned}
\]

把 \(S\) 规范成 induced-query ideal / maximal-antichain normal form 后，这正是 `J(Q)` 上的 upper zeta transform。

因此

\[
\boxed{
\text{全部 essential }Q\text{-count queries}
\Longleftrightarrow
\bar w_Q.
}
\]

Möbius inversion 恢复的是 **projected multiplicity distribution**，而不是 ambient multiplicity state。

## 4. Exact ambient collision

取二元素 antichain

\[
P=\{a,b\},
\qquad Q=\{a\}.
\]

比较两个 exact witness assignments：

- 唯一 witness 位于 \(\{a\}\)；
- 唯一 witness 位于 \(\{a,b\}\)。

二者 ambient state 不同，但 restriction 到 \(Q\) 后都等于 query ideal \(\{a\}\)。因此

\[
\boxed{\bar w_Q^{(1)}=\bar w_Q^{(2)}}
\]

所有只使用 \(a\) 的 count queries 都完全相同。

所以 count observable 不能越过 declared-future visibility boundary。

## 5. P025-T272 —— task-relative count horizon

只要 count queries 覆盖 induced query poset 中每个 ideal 的 boundary，完整 projected multiplicity \(\bar w_Q\) 就能恢复。因此 exact recovery horizon 是

\[
\boxed{\operatorname{width}(Q),}
\]

而不是 \(\operatorname{width}(P)\)。

worst-case sharpness 直接取 `P=Q` 为 antichain，并使用补充 122 的 even/odd construction 即得。

所以 task restriction 同时改变：

1. **能恢复哪一个 state** —— ambient `w` 还是 projected `bar w_Q`；
2. **需要多少 essential query arity** —— ambient width 还是 query width。

## 6. Branching ambient poset 中的 chain query

在 diamond

\[
a<b<d,
\qquad a<c<d,
\qquad b\parallel c
\]

中，ambient width 是 2。但对

\[
Q=\{a,d\},
\]

induced query poset 是 width-one chain。

singleton query counts 加上 empty total count 已能恢复三个 query ideals

\[
\varnothing,
\{a\},
\{a,d\}
\]

上的完整 multiplicity distribution。

但它仍无法辨认 query state \(\{a\}\) 的 multiplicity 在 ambient branches \(b,c\) 之间如何分布。

## 7. 架构结论

task-relative precision 包含两个不同 quotient operations：

\[
\boxed{
\text{ambient exact state}
\xrightarrow{\text{query restriction}}
\text{projected state}
\xrightarrow{\text{chosen observable}}
\text{count response}.
}
\]

一个强 observable 可以 invert 第二个 map，却不能因此 invert 第一个 map。

所以

\[
\boxed{\text{observable invertibility}\neq\text{ambient-state recoverability}.}
\]

这是 A2/A4 future-signature language 的重要边界。

## 8. Prior-art 边界

measure/count pushforward、induced-subposet restriction 与 Möbius inversion 都是经典数学。这里不主张 generic novelty。

项目侧结果是 P025 precision hierarchy 中的 exact task-relative placement 与 counterexample。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/poset_query_count_pushforward.py`；
- `tests/test_poset_query_count_pushforward.py`。

executable layer 验证 pushforward conservation、query ideal lattice 上的 zeta inversion、具有 identical query multiplicity 的 ambient collision、branching ambient poset 内 width-one recovery，以及 `Q=P` 时 identity recovery。

## 10. 下一前沿

即使 witness support family 本身固定不变，counts 也会严格比 existential support 更细。Stage 124 应把这层 value precision 显式化：MAY/MUST 由 counts 在 `0` 与 total count 两个阈值上退化得到，而 exact integer counts 保留这些 truth values 丢掉的 witness multiplicity。
