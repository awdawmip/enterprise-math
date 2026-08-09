# Causal Collapse Spectrum Core —— P011 从“不可逆性指标”提升为通用有限坍缩谱

状态：`CROSS-ROUTE RESEARCH WIP / REINTERPRETATION OF PROVED P011 FINITE THEOREMS`

归属建议：母理论应回流 A1/P011；本文件只记录 causal absorption 推导。

## 1. 纠偏

P011 最初从不可逆前向映射出发：多个 fine histories 合流成一个 coarse state。

但后续研究发现，同一个 fiber mathematics 反复出现于：

- temporal history merge；
- cross-future forgetting；
- task-signature reduction；
- finite precision/coarse observation；
- finite dimension contraction；
- measurement collapse。

因此 `J_k` 更底层的语义不是“某种熵”，甚至不必先叫不可逆性。

## 2. CC-01 —— 任意有限 causal collapse

设 `X` 是当前理论已经能区分的有限 states，任何声明的 abstraction / forgetting / observation：

\[
q:X\to Q.
\]

只要 `q` 把多个 fine distinctions 合成一个 coarse state，它就是 finite causal collapse。

fiber size：

\[
m_q(z)=|q^{-1}(z)|.
\]

定义：

\[
\boxed{J_k(q)=\sum_{z\in\operatorname{im}q}\binom{m_q(z)}k.}
\]

## 3. CC-02 —— universal distinction-loss meaning

`J_k(q)` 精确统计：

> 有多少个 `k` 元 fine-state 子集，其成员在 collapse 前彼此是 distinct states，但经过 `q` 后全部拥有同一个 coarse label。

因此：

- `J_1=|X|`：fine distinctions 总数；
- `J_2`：被识别到一起的 fine-state pairs；
- 高阶 `J_k`：更高阶 simultaneous collapse groups。

P011 已证明完整 spectrum 经整数二项反演精确恢复 fiber-size multiset。

## 4. CC-03 —— 不同领域只是同一 collapse 的不同 causal role

### 时间不可逆

`q` 是 history/current-state forward map。

### Signature coupling

`q=\rho:Q_AB->R` 忘掉 cross-future information。此时 `J_k(q)` 就是 coupling split spectrum。

### Task precision

`q` 把 full future signature 映到 task-restricted signature。

### Measurement

`q` 把 fine causal states 映到实际 observation labels。

### Dimension contraction

在有限截面/有限球中，`q` 把 fine relation states 映到 coarse partition states。

因此：

\[
\boxed{
\text{irreversibility / coupling loss / precision loss / contraction loss}
=
\text{finite causal collapse 的不同角色解释}.
}
\]

## 5. CC-04 —— staged collapse 已由 P011 给出完整链式增量

若：

\[
X\xrightarrow{F}Y\xrightarrow{G}Z,
\]

则 P011 已证明：

\[
J_k(G\circ F)\ge J_k(F),
\]

并且增量：

\[
\Delta J_k
\]

精确计数这一步新产生的 cross-old-fiber `k`-history groups。

所以不同层 abstraction 的“新丢了多少 distinction”不需要另造 entropy chain rule；P011 已经有 exact integer chain accounting。

## 6. CC-05 —— spectrum 不是完整 causal state

完整 `J_k` 虽然恢复 fiber-size multiset，却不恢复：

- 哪些具体 states 被合并；
- fiber identity；
- incidence relation；
- 后续操作是否依赖具体 witness identity。

因此：

\[
\boxed{\text{collapse relation / witness} > \text{collision spectrum} > \text{scalar shadows}.}
\]

这与 P021 的结论一致：cardinality/spectrum 可以作为 anonymous statistics，但未来复合若仍读取 witness identity，就不能只留 `J_k`。

## 7. CC-06 —— traditional entropy / information 的位置

在 finite collapse 中，任何只依赖 fiber-size multiset 的 symmetric scalar 都是完整 `J_k` spectrum 的后处理。

因此这类 entropy/moment/probability scalar 不含超过完整 spectrum 的 fiber-size information。

但这不意味着：

- thermodynamic entropy 已被推导；
- Shannon operational coding theorem 被替代；
- continuous information theory 已被吞并。

这里只建立：

> finite causal distinction loss 有一个比很多传统 scalar 更底层、完全整数、可组合追踪的母对象。

## 8. CC-07 —— 与 support 的正交关系

collapse spectrum 只描述“已有 fine states 怎样被认成同一个 coarse state”。

它不描述哪些理论组合根本不存在。

因此 signature coupling 的 typed decomposition：

\[
(M,S)
\]

应理解成：

- `M`：support/reachability defect；
- `S` 与 `C_k`：cross-future forgetting collapse defect。

这两类机制不可压成一个 scalar。

## 9. 当前工具状态

不新增新的计算 primitive；复用：

- `causal_count_measure.py::collision_count`；
- `collision_interaction_basis.py`；
- P011 canonical theorem/test assets；
- `causal_signature_coupling.py`。

## 10. 下一步

1. 研究 infinite integer relation systems 中，rank/kernel/Smith 是否是 finite collapse spectrum 的结构对应物；
2. 把 A3 dimension contraction 的 lost relation rank 与有限球上的 `J_k` collapse profile 连接；
3. 判定什么 operation languages 下 anonymous spectrum 已经 future-safe；
4. 把 P021 witness necessity 写成 collapse-core 的 composability gate。
