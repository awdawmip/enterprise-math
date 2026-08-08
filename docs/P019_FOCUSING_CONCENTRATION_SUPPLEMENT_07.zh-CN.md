# P019 —— 聚焦集中度补充 07：总收缩相同，不代表微观聚焦相同

状态：`ACTIVE RESEARCH NOTE`  
依赖：P011 collision spectrum、P019 Overlap-Spectrum Focusing Supplement 06  
范围：证明总 focusing excess `C` 从三 source 开始不再完整，并构造高阶集中度整数观察量  
纪律：这些量描述 future-target multiplicity 的集中程度；当前不赋予 Ricci/shear/energy 的物理名称。

## 1. 问题

前两阶段已经得到

\[
\Xi=B-C
\]

以及

\[
C=J_2-J_3+J_4-\cdots.
\]

因此自然出现一个问题：

> 如果两个局部 causal structures 具有同样的当前截面大小 `N`、同样 branching surplus `B`、同样 total focusing `C` 和同样 expansion `Xi`，它们的微观聚焦结构是否必然相同？

答案是否定的，而且最早在三个 source 就发生。

## 2. P019-FC-T01 —— 至多两个 source 时，粗量已经恢复 multiplicity profile

状态：`PROVED`

若

\[
|A|\le2,
\]

则任意 future target 的 multiplicity 只能是

\[
m_w\in\{1,2\}.
\]

此时

\[
C=\sum_w(m_w-1)
\]

恰好就是 multiplicity-2 targets 的数量。

又因为总 outgoing incidence 数

\[
E=N+B,
\]

而 future target 数

\[
F=E-C=N+B-C,
\]

所以：

\[
\boxed{
\#\{m=2\}=C,
}
\]

\[
\boxed{
\#\{m=1\}=F-C=N+B-2C.
}
\]

因此在 `N<=2` 的 regime，给定 `N,B,C` 已经完全确定 future-target multiplicity multiset。

换言之，在两个 source 以内，还不存在“总聚焦相同但高阶结构不同”的自由度。

## 3. P019-FC-T02 —— 三个 source 是总量失去完整性的最小门槛

状态：`PROVED BY T01 + EXPLICIT COUNTEREXAMPLE`

取当前截面

\[
A=\{a,b,c\}
\]

和两个 future targets `x,y`。

### 结构 D：分散 pair focusing

取 edges：

\[
a\to x,
\quad b\to x,
\quad a\to y,
\quad c\to y.
\]

future multiplicities 是

\[
(2,2).
\]

于是：

\[
N=3,
\quad E=4,
\quad B=1,
\quad F=2,
\quad C=2,
\quad\Xi=-1.
\]

collision spectrum：

\[
(J_1,J_2,J_3)=(4,2,0).
\]

### 结构 H：集中 triple focusing

取 edges：

\[
a\to x,
\quad b\to x,
\quad c\to x,
\quad a\to y.
\]

future multiplicities 是

\[
(3,1).
\]

同样有：

\[
N=3,
\quad E=4,
\quad B=1,
\quad F=2,
\quad C=2,
\quad\Xi=-1.
\]

但 collision spectrum 为

\[
(J_1,J_2,J_3)=(4,3,1).
\]

所以：

\[
\boxed{
(N,B,C,\Xi)_{D}
=(N,B,C,\Xi)_{H}
}
\]

而

\[
\boxed{
(J_2,J_3)_{D}\ne(J_2,J_3)_{H}.
}
\]

由 T01，`N<=2` 不可能出现这种差异；因此

\[
\boxed{
N=3
}
\]

是 coarse focusing data 首次不足以恢复微观 multiplicity structure 的最小 source cardinality。

若要求当前层与 future layer 顶点互不重合，上述 witness 只需要 3 个 current vertices + 2 个 future vertices，共 5 个图顶点。

## 4. P019-FC-T03 —— 高阶集中度 `H=J_2-C`

状态：`PROVED`

定义

\[
\boxed{
H(A)=J_2^{\rm out}(A)-C(A).
}
\]

对单个 multiplicity `m`：

\[
\binom m2-(m-1)
=
\frac{(m-1)(m-2)}2
=
\binom{m-1}2.
\]

因此：

\[
\boxed{
H(A)
=
\sum_w\binom{m_A(w)-1}{2}.
}
\]

所以

\[
H(A)\ge0.
\]

而且

\[
\boxed{
H(A)=0
\iff
m_A(w)\le2\text{ for every future target }w.
}
\]

因此 `H>0` 是一个精确的 **higher-order focusing witness**：它当且仅当至少一个 future target 被三路或更多 current incidences 共同命中时出现。

在 T02 的两个结构中：

- 分散 `(2,2)`：`H=0`；
- 集中 `(3,1)`：`H=1`。

## 5. P019-FC-T04 —— 二次聚焦集中度 `Q=2J_2-C`

状态：`PROVED`

定义

\[
\boxed{
Q(A)=2J_2^{\rm out}(A)-C(A).
}
\]

因为

\[
2\binom m2-(m-1)
=m(m-1)-(m-1)
=(m-1)^2,
\]

得到

\[
\boxed{
Q(A)
=
\sum_w(m_A(w)-1)^2.
}
\]

`C` 是 excess multiplicity 的一次总量：

\[
C=\sum_w(m_w-1),
\]

而 `Q` 是同一 excess 的平方和。

因此在固定 `C` 时，`Q` 对聚焦是否集中到少数高 multiplicity targets 更敏感。

T02 中：

- `(2,2)`：excess `(1,1)`，所以 `Q=2`；
- `(3,1)`：excess `(2,0)`，所以 `Q=4`。

两者拥有相同总 focusing `C=2`，但 `Q` 明确区分 diffuse 与 concentrated focusing。

这仍只是整数 multiplicity concentration，不自动等于物理 shear 或 curvature。

## 6. P019-FC-T05 —— `C` 不是完整局部聚焦 invariant

状态：`PROVED`

由 T02 的明确图对，存在两个 finite causal sections 满足相同：

\[
N,
\quad B,
\quad C,
\quad\Xi,
\]

但具有不同：

\[
J_2,J_3,\ldots,
\quad H,
\quad Q,
\quad\mu=\max_w m_w.
\]

所以

\[
\boxed{
C\text{ alone is not a complete local focusing invariant.}
}
\]

同样，`Xi=B-C` 虽足以决定截面 cardinality 的净变化，也不足以恢复造成该变化的微观 overlap structure。

这与 P011 的完整性结果一致：要恢复 fiber-size multiset，需要完整 collision spectrum，而不是一个低阶汇总量。

## 7. 对“shear-like / curvature-like”研究的约束

这一步给下一阶段建立了一个必要条件：如果两个局部图具有相同 `N,B,C,Xi`，但 `J_k` spectrum 不同，那么任何只依赖 `C` 或 `Xi` 的候选“离散曲率”都无法区分它们。

但我们仍不能反过来武断指定：

- `H` 就是 shear；
- `Q` 就是 curvature；
- 高 `J_3` 就是某种特定物质源。

真正需要的是再加入**方向/局部子截面结构**，研究同样 multiplicity concentration 是否沿不同方向分布不同。

因此下一步应该构造 directional refinement，而不是继续增加无方向标量。

## 8. 与现有 P011 的关系

P011 已证明完整 collision spectrum

\[
(J_2,\ldots,J_N)
\]

加上 domain size 可以恢复 fiber-size multiset。

P019-FC 只是把该已有结果在 causal incidence map 上解释成：

> 完整 spectrum 恢复每个 future target 被多少条 current causal incidences 共同命中的 multiplicity distribution。

因此本阶段的数学新内容必须谨慎区分：

- collision-spectrum 完整性来自 P011；
- 最小 3-source witness、`H/Q` 在 P019 causal focusing 中的用途、以及后续 directional source decomposition 是当前研究组合。

## 9. 本阶段 ledger

- `P019-FC-T01`：for at most two sources, `N,B,C` reconstruct the multiplicity profile —— `PROVED`
- `P019-FC-T02`：three sources are the minimal cardinality for equal coarse focusing with different higher-order spectra —— `PROVED`
- `P019-FC-T03`：`H=J2-C=sum binom(m-1,2)`, with `H=0` iff all multiplicities are at most 2 —— `PROVED`
- `P019-FC-T04`：`Q=2J2-C=sum(m-1)^2` —— `PROVED`
- `P019-FC-T05`：total focusing `C` is not a complete local focusing invariant —— `PROVED`

Executable checks：

- `src/enterprise_math/focusing_concentration.py`
- `tests/test_focusing_concentration.py`

## 10. 下一阶段

到这里，“总聚焦量”已经被拆到足够细，继续增加标量收益会迅速下降。

下一步优先研究 **directional overlap spectrum**：

1. 为 primitive outgoing incidences 增加不依赖连续角度的方向/邻接类别；
2. 比较不同方向子截面的 `J_k,H,Q`；
3. 定义纯整数 anisotropy witness；
4. 检查 graph automorphism 下该 witness 如何变换；
5. 再与 continuum shear 的结构性质比较。

只有这一层建立以后，才值得讨论某个整数项是否真正具有 shear-like 含义。
