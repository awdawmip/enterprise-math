# P019 —— 有向因果扩张补充 03：未来截面、分支与合流

状态：`ACTIVE RESEARCH NOTE`  
依赖：P010/P011 forward merging、P012 primitive graph、P019 causal boundary supplement 02  
范围：从 directed one-step reachability 直接生成整数 expansion，而不是手工赋值 `xi`  
纪律：这是有限图上的候选 null-cross-section calculus，不是 Einstein/Raychaudhuri 方程的离散证明。

## 1. 从点的 phase 转向未来截面的 cardinality

令

\[
G=(V,E^+)
\]

为有限 directed primitive graph。

对一个非空有限截面

\[
A\subseteq V,
\]

定义一步未来可达集

\[
\boxed{
F(A)
=
\{w\in V:\exists v\in A,(v,w)\in E^+\}.
}
\]

这里 `F(A)` 只保留**不同的未来状态**；多条边到达同一个 `w` 时，`w` 只计一次。

定义整数 future-section expansion：

\[
\boxed{
\Xi(A)=|F(A)|-|A|.
}
\]

于是：

- `Xi(A)>0`：下一截面拥有更多可区分 future states；
- `Xi(A)=0`：marginal cardinality；
- `Xi(A)<0`：未来截面收缩。

这给 Supplement 02 中手工输入的 `xi` 一个第一候选来源：把**截面本身**视作状态，以 `Xi(A)` 作为其 expansion field。

## 2. P019-D-T01 —— Future 运算保持并集

状态：`PROVED`

对任意两个截面 `A,B`：

\[
\boxed{F(A\cup B)=F(A)\cup F(B).}
\]

这是存在量词定义的直接结果：一个顶点从 `A union B` 一步可达，当且仅当它从 `A` 或 `B` 中至少一个截面可达。∎

## 3. P019-D-T02 —— Expansion 的精确 overlap defect

状态：`PROVED`

由有限集合容斥：

\[
|F(A\cup B)|
=|F(A)|+|F(B)|-|F(A)\cap F(B)|,
\]

\[
|A\cup B|
=|A|+|B|-|A\cap B|.
\]

因此

\[
\boxed{
\Xi(A\cup B)
=
\Xi(A)+\Xi(B)
+|A\cap B|
-|F(A)\cap F(B)|.
}
\]

特别地若

\[
A\cap B=\varnothing,
\]

则

\[
\boxed{
\Xi(A\cup B)
=
\Xi(A)+\Xi(B)
-|F(A)\cap F(B)|.
}
\]

也就是说：两个原本分开的截面如果未来开始共享状态，**未来 overlap 会精确扣减总 expansion**。

这是第一个不需要连续曲率就能把“聚焦/合流”直接写进空间截面变化的公式。

## 4. P019-D-T03 —— 分支—碰撞精确分解

状态：`PROVED`

定义从 `A` 发出的 directed edge incidence 数：

\[
E_A
=
|\{(v,w)\in E^+:v\in A\}|.
\]

定义 **branching surplus**：

\[
\boxed{
B(A)=E_A-|A|.
}
\]

对每个未来状态 `w` 定义入射 multiplicity：

\[
m_A(w)
=
|\{v\in A:(v,w)\in E^+\}|.
\]

定义 **collision/focusing excess**：

\[
\boxed{
C(A)
=
\sum_{w\in F(A)}(m_A(w)-1).
}
\]

因为

\[
\sum_{w\in F(A)}m_A(w)=E_A,
\]

有

\[
C(A)=E_A-|F(A)|.
\]

于是：

\[
\Xi(A)
=|F(A)|-|A|
\]

可以精确改写为

\[
\boxed{
\Xi(A)=B(A)-C(A).
}
\]

这是本阶段最关键的公式。

它把截面变化拆成两个完全整数的机制：

\[
\boxed{
\text{future expansion}
=
\text{branching surplus}
-
\text{collision/focusing excess}.
}
\]

因此“空间收敛”不再需要被写成一个神秘的连续压缩量：在这个候选模型里，它首先意味着**未来可达分支产生的新状态，被多路径合流消耗得更多**。

## 5. P019-D-T04 —— Marginal boundary 是 branch 与 collision 的整数平衡

状态：`PROVED`

由 T03：

\[
\Xi(A)=0
\iff
B(A)=C(A).
\]

所以一个 marginal cross-section 的整数候选条件是

\[
\boxed{
\text{新增 future branching}
=
\text{future collision/focusing}.
}
\]

同理：

\[
\Xi(A)>0
\iff
B(A)>C(A),
\]

\[
\Xi(A)<0
\iff
B(A)<C(A).
\]

这给“扩张—视界—收敛”三相一个统一离散机制，而不仅是三个符号标签。

## 6. P019-D-T05 —— Local collision spectrum 与 P011 的精确接口

状态：`PROVED FINITE-MAP INTERFACE`

把所有从 `A` 发出的 edge incidences 组成有限集合

\[
I_A
=
\{(v,w)\in E^+:v\in A\}.
\]

定义 target map

\[
\tau_A:I_A\to F(A),
\qquad
\tau_A(v,w)=w.
\]

它是一个真正的有限函数，其 fiber size 恰好是

\[
m_A(w).
\]

所以可以直接使用 P011 collision spectrum：

\[
\boxed{
J_k^{\mathrm{out}}(A)
=
\sum_{w\in F(A)}\binom{m_A(w)}k.
}
\]

其中：

- `J_2` 计算成对 future-incidence collisions；
- 更高 `J_k` 记录多重聚焦；
- 完整 spectrum 重建 target-fiber multiplicity multiset。

而 T03 的

\[
C(A)=\sum_w(m_A(w)-1)
\]

是比完整 collision spectrum 更粗的一阶 focusing loss。

因此 P019 不需要发明另一套“黑洞合流熵”；现有 P011 的整数 fiber 工具可以直接作用于 causal incidence target map。

必须注意：这里 P011 作用的是**outgoing incidence 到 future target 的局部函数**，不是自动等同于整个宇宙的时间演化函数。

## 7. P019-D-T06 —— 单值 successor dynamics 不能产生正的 cardinal expansion

状态：`PROVED`

若 `A` 中每个顶点恰有一个 outgoing successor，则

\[
E_A=|A|,
\]

因此

\[
B(A)=0.
\]

T03 给出

\[
\boxed{
\Xi(A)=-C(A)\le0.
}
\]

并且

\[
\Xi(A)=0
\]

当且仅当 successor map 在 `A` 上单射。

所以：

> **如果把 bare spatial vertex 的未来演化限制成单值函数，那么 distinct future-state cardinality 只能保持或减少，不能正扩张。**

这与 P010 的 deterministic postcomposition / merging 结构一致。

因此要表示真正的空间 light-front expansion，primitive causal geometry 不能简单等同于“每个空间点只有一个 successor 的状态函数”。至少需要：

- branching reachability relation；或
- 更丰富的 ray/direction state；或
- time-layered cells，其中一个空间截面可以到达多个未来 cells。

这是一条架构约束，而不是物理结论。

## 8. P019-D-T07 —— Expansion 沿未来截面演化严格望远镜

状态：`PROVED`

令

\[
A_{t+1}=F(A_t).
\]

则按定义

\[
\Xi(A_t)=|A_{t+1}|-|A_t|.
\]

所以对任意有限 `T`：

\[
\boxed{
\sum_{t=0}^{T-1}\Xi(A_t)
=|A_T|-|A_0|.
}
\]

这是一条完全整数的 cumulative expansion law。

它不需要导数、积分或连续 affine parameter。

如果要与传统 null expansion 比较，后续可以研究“每一步 cardinal difference”在 typed scale 下怎样对应连续 limit，但那个 limit 不是本定义的前提。

## 9. P019-D-C01 —— Expansion 不是 entropy，也不要求单调

状态：`COUNTEREXAMPLE / SCOPE BOUNDARY`

有限 directed graph 可以产生 expansion sequence：

\[
+1,-3,-1.
\]

所以 `Xi_t` 本身不单调。

它只是相邻 future cross-sections 的 cardinal difference。

因此禁止把

\[
\Xi
\]

直接命名为 entropy 或不可逆性单调量。

真正的 P010/P011 单调性仍然属于特定 forward-function fiber/collision observables；P019 的 `Xi` 是几何/因果截面量，二者通过 T03/T05 接口联系，但不能混为一物。

## 10. 从用户最初直觉得到的更精确表达

最初问题是：

> 黑洞会不会是时间变慢，导致的空间收敛？

经过 Schwarzschild、RN、graph boundary、directed future-section 四层重算，目前能够严格表达的候选机制已经变成：

\[
\boxed{
\text{future reachability}
\to
\text{branching}
+
\text{collision/focusing}
\to
\Xi=B-C.
}
\]

当

\[
C>B,
\]

未来截面 cardinality 收缩；当

\[
C=B,
\]

得到 marginal boundary 候选。

“时间变慢”本身还没有被证明为 `C` 增大的原因。但第一阶段 clock observation 与这一图结构现在有了一个清楚的待接接口：

\[
\boxed{
\text{clock precision state}
\stackrel{?}{\longrightarrow}
\text{allowed future incidence structure}
\longrightarrow
B,C,\Xi.
}
\]

下一阶段真正应该攻的是这个箭头，而不是继续重复离散 Schwarzschild 公式。

## 11. 本阶段 ledger

- `P019-D-T01`：future preserves unions —— `PROVED`
- `P019-D-T02`：exact union-overlap expansion defect —— `PROVED`
- `P019-D-T03`：`Xi=B-C` branching/collision decomposition —— `PROVED`
- `P019-D-T04`：marginal iff branching equals collision —— `PROVED`
- `P019-D-T05`：local outgoing collision spectrum interfaces exactly with P011 —— `PROVED`
- `P019-D-T06`：single-successor maps cannot create positive distinct-state expansion —— `PROVED`
- `P019-D-T07`：future-section expansion telescopes —— `PROVED`
- `P019-D-C01`：`Xi` need not be monotone and is not entropy —— `COUNTEREXAMPLE / BOUNDARY`

Executable checks：

- `src/enterprise_math/directed_expansion.py`
- `tests/test_directed_expansion.py`

## 12. 下一步：把 clock 和 causal incidence 真正耦合

当前最优先问题变成：

1. 给每个 finite clock state `K` 定义允许的 future-incidence budget，而不是手工指定 graph；
2. 检验更慢的 clock state 是否必然减少 branching、增加 collision，或者二者都不是——必须允许反例；
3. 找出 `K=0` 时产生 marginal `B=C` 的最小附加公理；
4. 区分 observer-coordinate clock slowdown 与 invariant causal-incidence restriction；
5. 若该耦合无法自然建立，就应否定“时间变慢导致空间收敛”的强因果方向，只保留二者由同一底层结构共同产生的较弱解释。
