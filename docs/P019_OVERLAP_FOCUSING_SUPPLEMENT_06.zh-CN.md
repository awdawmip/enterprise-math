# P019 —— 重叠谱聚焦补充 06：多体 future overlap 与 expansion 次模性

状态：`ACTIVE RESEARCH NOTE`  
依赖：P011 collision spectrum、P019 Directed Expansion Supplement 03、P019 Integer Focusing Supplement 05  
范围：把 future collision/focusing excess `C` 精确拆成二路、三路、四路…… successor overlap；建立边际 expansion 与次模结构  
纪律：本文得到的是有限集合与有限图上的精确组合结构；不得把某一阶 overlap 未经进一步推导直接命名为 Ricci curvature、shear 或物质能量项。

## 1. 为什么继续拆 `C`

前一阶段得到

\[
\Xi(A)=B(A)-C(A),
\]

其中

\[
C(A)=\sum_{w\in F(A)}(m_A(w)-1).
\]

这个总量已经能表达 future-state focusing，但它把“两路合流”和“三路、四路……更高重数聚焦”全部压成一个整数。

P011 已经告诉我们：有限函数的 fiber multiplicity 可以用完整 collision spectrum

\[
J_k=\sum_w\binom{m(w)}k
\]

精确展开。

P019 的下一步因此不是发明新的曲率标量，而是问：**`C` 在现有 `J_k` 中究竟是什么？**

答案是一个精确交替投影。

## 2. 定义：k 路 successor overlap

对当前截面

\[
A\subseteq V
\]

以及每个 source vertex `v` 的 successor set

\[
S(v)=\{w:(v,w)\in E^+\},
\]

定义第 `k` 阶 successor overlap：

\[
\boxed{
O_k(A)
=
\sum_{\substack{T\subseteq A\\|T|=k}}
\left|\bigcap_{v\in T}S(v)\right|.
}
\]

它直接数：任取 `k` 个当前 source，它们共同拥有多少 future target，并对所有 `k` 元 source 子集求和。

## 3. P019-OF-T01 —— k 路 overlap 与 P011 local collision spectrum 完全相同

状态：`PROVED`

对每个 future target `w`，令

\[
m_A(w)=|\{v\in A:w\in S(v)\}|.
\]

交换求和顺序：一个固定的 `w` 会被多少个 `k` 元 source 子集共同包含？恰好是

\[
\binom{m_A(w)}k.
\]

所以

\[
\boxed{
O_k(A)
=
\sum_{w\in F(A)}\binom{m_A(w)}k
=J_k^{\rm out}(A).
}
\]

因此 successor-overlap spectrum 不是另一套新 invariant；它就是 P011 collision spectrum 在 causal incidence target map 上的集合论表达。

这给 P011 与 P019 一个更强接口：

- P011 的 `J_k`：从 fiber multiplicity 看 k 重碰撞；
- P019 的 `O_k`：从多个 source 的共同 future reachability 看 k 路聚焦。

二者是同一个整数。

## 4. P019-OF-T02 —— Focusing excess 是完整 overlap spectrum 的交替投影

状态：`PROVED`

对任意整数 `m>=1`，二项式恒等式

\[
(1-1)^m=0
\]

给出

\[
1-m+\binom m2-\binom m3+\cdots+(-1)^m=0.
\]

因此

\[
\boxed{
m-1
=
\binom m2-inom m3+inom m4-\cdots.}
\]

对所有 future target 的 multiplicity 求和：

\[
C(A)
=
\sum_w(m_A(w)-1).
\]

所以

\[
\boxed{
C(A)
=J_2^{\rm out}(A)-J_3^{\rm out}(A)+J_4^{\rm out}(A)-\cdots.
}
\]

等价地：

\[
\boxed{
C(A)=O_2(A)-O_3(A)+O_4(A)-\cdots.}
\]

于是中心 expansion 恒等式得到完整谱版本：

\[
\boxed{
\Xi(A)
=
B(A)-J_2+J_3-J_4+J_5-\cdots.
}
\]

这说明：仅看 pair collision `J_2` 会系统性重复计算三路及以上聚焦；高阶项以 inclusion-exclusion 方式逐层修正。

例如三个 source 全部只到达同一个 future target：

\[
(J_1,J_2,J_3)=(3,3,1).
\]

真实 focusing loss 是

\[
C=3-1=2,
\]

而不是 `J_2=3`；三路项 `J_3=1` 正好修正 pair overcount：

\[
C=J_2-J_3=2.
\]

## 5. P019-OF-T03 —— Pair collision 是 `C` 的上界，并受最大 multiplicity 控制

状态：`PROVED`

令

\[
\mu(A)=\max_{w\in F(A)}m_A(w).
\]

对每个 `m>=1`：

\[
m-1\le\binom m2.
\]

所以

\[
\boxed{C(A)\le J_2^{\rm out}(A).}
\]

若 `C(A)>0`，又因为

\[
2\binom m2=m(m-1)\le\mu(A)(m-1),
\]

求和得到

\[
\boxed{
2J_2^{\rm out}(A)
\le
\mu(A)C(A).
}
\]

因此

\[
\boxed{
\frac{2J_2}{\mu}
\le C\le J_2
}
\]

只是外部简写；整数核心使用交叉乘法版本，不把分数作为基本状态。

这给 pair-collision load 一个可解释边界：若没有非常深的高 multiplicity target，`J_2` 不可能无限夸大真实 focusing excess。

## 6. P019-OF-T04 —— 增加一个 source 的边际 expansion 有精确局部公式

状态：`PROVED`

取

\[
v\notin A.
\]

定义边际 expansion：

\[
\Delta_v\Xi(A)
=
\Xi(A\cup\{v\})-\Xi(A).
\]

新 source 的 successor set 是 `S(v)`。

它新增的 future states 恰好是

\[
S(v)\setminus F(A),
\]

所以

\[
|F(A\cup\{v\})|-|F(A)|
=|S(v)|-|S(v)\cap F(A)|.
\]

同时 current section cardinality 增加 1。

因此：

\[
\boxed{
\Delta_v\Xi(A)
=
(|S(v)|-1)
-|S(v)\cap F(A)|.
}
\]

右侧恰好是：

\[
\boxed{
\text{new-source branch increment}
-
\text{existing-future overlap load}.
}
\]

这是一条真正局部的 focusing source formula：要判断增加一个 source 对 expansion 的净贡献，只需要它自己的 successor set 与当前 future union 的重叠，不需要扫描一个隐藏连续空间。

## 7. P019-OF-T05 —— Expansion 具有 diminishing returns

状态：`PROVED`

若

\[
A\subseteq B,
\qquad
v\notin B,
\]

则

\[
F(A)\subseteq F(B).
\]

因此

\[
|S(v)\cap F(A)|
\le
|S(v)\cap F(B)|.
\]

代入 T04：

\[
\boxed{
\Delta_v\Xi(A)
\ge
\Delta_v\Xi(B).
}
\]

也就是说：

> **同一个新 source，在一个更大的既有截面上，其净 future expansion 贡献不会更大。**

原因不是人为加入“阻尼”，而是更大的截面已经覆盖更多 future targets，所以新 source 更容易与既有 future structure 重叠。

这是一种纯组合的 focusing/diminishing-return 机制。

## 8. P019-OF-T06 —— Future-section expansion 是次模 set function

状态：`PROVED`

把空集自然延伸为

\[
F(\varnothing)=\varnothing,
\qquad
\Xi(\varnothing)=0.
\]

`|F(A)|` 是 successor-set union 的 coverage function，因此次模；`|A|` 是 modular function。

所以

\[
\Xi(A)=|F(A)|-|A|
\]

仍然次模：

\[
\boxed{
\Xi(A)+\Xi(B)
\ge
\Xi(A\cup B)+\Xi(A\cap B).
}
\]

其 defect 可以直接化简为 future-overlap 的集合恒等式。

T05 的 diminishing returns 与 T06 的 submodularity 是等价的有限集合视角。

这个结果很重要，因为它说明 causal focusing 不只存在于某个特制的 radial black-hole 例子里，而是**任何由 successor-union 产生的 future-section expansion 都天然带有次模结构**。

## 9. 对“局部曲率源”的含义

到这里，我们已经能够把 focusing 拆成：

\[
\boxed{
C
=
O_2-O_3+O_4-\cdots
}
\]

并把一个 source 的边际效应写成：

\[
\boxed{
\Delta_v\Xi
=
\text{branch increment}
-
\text{future overlap load}.
}
\]

这比单一 `C` 更接近“local source decomposition”。

但是现在仍然**不能**说：

- `O_2` 就是 Ricci focusing；
- `O_3` 就是 shear；
- 某个固定阶数就是物质能量。

传统 Raychaudhuri 中不同几何源具有明确 tensor/geodesic 意义。P019 的 `O_k` 当前只记录 k 路 future overlap multiplicity。

正确下一问是：不同微观 causal graphs 是否会在相同 `N,B,C` 下拥有不同 `O_k` spectrum，而这些差异是否对应不同的横向变形/方向性结构。

若答案是肯定的，完整 overlap spectrum 才可能成为区分 shear-like 与 isotropic-focusing-like 行为的候选输入。

## 10. 一个新的可检验区分：同样的总 focusing，可以有不同高阶谱

考虑两个局部结构都具有相同的

\[
C=2.
\]

它可以来自：

- 两个独立的 pair collisions：`J_2=2,J_3=0`；
- 一个三重 target collision：`J_2=3,J_3=1`。

两者的总 `C` 相同，但高阶谱不同。

因此：

\[
\boxed{
C\text{ alone is not a complete local focusing invariant.}
}
\]

P011 已证明完整 collision spectrum 能恢复 fiber-size multiset；P019 现在把这个结论解释为：完整 `O_k` 能恢复“future targets 被多少路 source 共同命中”的 multiplicity profile。

这为下一阶段比较“各向同性压缩”与“非均匀聚焦”提供了比一个总标量更丰富的整数数据。

## 11. 与外部成熟数学的关系

T06 的 submodularity/coverage-function 结构本身属于成熟组合优化/集合函数数学，不应作为 Enterprise Math 独创性质宣称。

P019 当前可研究的组合点在于：

- 把 successor coverage 的次模性；
- P011 collision spectrum；
- finite-precision fibers；
- causal boundary / future-section dynamics；

放进同一整数研究链中，并检验它是否能够承担黑洞/聚焦物理的可证伪建模任务。

因此 novelty discipline 继续保持：数学工具分别承认前人工作，项目只对特定组合与解释承担新颖性审查。

## 12. 本阶段 ledger

- `P019-OF-T01`：k-way successor overlap equals local P011 collision spectrum —— `PROVED`
- `P019-OF-T02`：`C=J2-J3+J4-...` and `Xi=B-J2+J3-...` —— `PROVED`
- `P019-OF-T03`：pair-collision bounds using maximum target multiplicity —— `PROVED`
- `P019-OF-T04`：exact marginal expansion formula for adding one source —— `PROVED`
- `P019-OF-T05`：diminishing returns under section inclusion —— `PROVED`
- `P019-OF-T06`：future-section expansion is submodular —— `PROVED`

Executable checks：

- `src/enterprise_math/overlap_focusing.py`
- `tests/test_overlap_focusing.py`

## 13. 下一阶段门槛

现在 local focusing source 已经从单个总量 `C` 展开成完整 overlap spectrum。

下一阶段最有价值的问题不是继续增加公式，而是构造**同 `N,B,C`、不同 `O_k` spectrum** 的最小图对，并研究哪些更细的整数观察量能够识别：

1. 聚焦是否集中在少数高 multiplicity future targets；
2. 聚焦是否分散为大量 pairwise overlaps；
3. 不同方向/局部子截面上的 overlap spectrum 是否不对称；
4. 这些结构在 graph automorphism 与 P018 refinement 下哪些保持、哪些消失。

只有完成这一层，才有资格讨论 shear-like / curvature-like source decomposition。
