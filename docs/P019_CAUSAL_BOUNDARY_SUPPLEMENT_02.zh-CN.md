# P019 —— 因果边界补充 02：从径向公式到 primitive graph cut

状态：`ACTIVE RESEARCH NOTE`  
依赖：P012 primitive graph geometry、P018 finite precision、P019 Schwarzschild/RN stages  
范围：不使用半径坐标的有限图 horizon skeleton  
纪律：本补充抽象的是“边界结构”，还没有从 Einstein dynamics 推导 expansion 场。

## 1. 输入不再包含半径

令

\[
G=(V,E)
\]

为一个有限 primitive undirected graph。边 `E` 是基本相邻关系，不由隐藏欧氏距离生成。

再给定一个整数值 outgoing-expansion 场

\[
\boxed{\xi:V\to\mathbb Z.}
\]

只保留其符号：

\[
\phi(v)=\operatorname{sgn}(\xi(v))\in\{-1,0,+1\}.
\]

解释层面可把：

- `+1` 视为 outgoing expansion；
- `0` 视为 marginal/zero expansion；
- `-1` 视为 outgoing contraction。

但本文的定理只依赖整数符号，不依赖这个物理解读。

## 2. 定义：causal boundary complex

定义零顶点集合

\[
\boxed{V_0=\{v\in V:\xi(v)=0\}.}
\]

定义变号边集合

\[
\boxed{
E_{\pm}
=
\{\{u,v\}\in E:\xi(u)\xi(v)<0\}.
}
\]

称

\[
\boxed{\partial_\xi G=(V_0,E_{\pm})}
\]

为 `xi` 的 **causal boundary complex**。

它故意同时保留两种离散 horizon：

1. **primal boundary**：零 expansion 顶点；
2. **dual boundary**：两个相反 phase 之间的 crossing edge。

这正是 RN 压力测试要求的最小统一对象。

## 3. P019-G-T01 —— 离散因果介值定理

状态：`PROVED`

设

\[
v_0,v_1,\ldots,v_m
\]

是一条 graph path，并且两个端点具有相反的非零 phase：

\[
\xi(v_0)\xi(v_m)<0.
\]

则该路径必然满足至少一种：

1. 存在 `i` 使

\[
\xi(v_i)=0;
\]

2. 存在相邻 `i,i+1` 使

\[
\xi(v_i)\xi(v_{i+1})<0.
\]

即：

\[
\boxed{
\text{每条从 expansion region 到 contraction region 的路径都与 }\partial_\xi G\text{ 相交。}
}
\]

### 证明

若路径中已有零顶点，结论成立。

否则每个 `xi(v_i)` 都严格正或严格负。首点与末点符号不同，因此沿有限序列从首项走到末项时，存在第一次符号改变。对应的相邻两项乘积为负，即形成 `E_pm` 中的一条 crossing edge。∎

这是一条完全有限的离散 intermediate-value statement；不需要连续函数、实数区间或极限。

## 4. P019-G-T02 —— 删除 boundary 后每个连通分量 phase 单一

状态：`PROVED`

从 `G` 中：

- 删除所有 `V_0` 顶点；
- 删除所有 `E_pm` crossing edges。

得到剩余图 `G\partial`。

则其每一个连通分量中的所有顶点 phase 必相同。

否则同一连通分量中存在一正一负两个顶点，它们之间存在一条仍留在剩余图中的 path；由 T01，该 path 必须穿过已删除的零顶点或 crossing edge，矛盾。∎

所以 `partial_xi G` 确实把正/负因果相分开，而不是只给出一组局部标记。

## 5. P019-G-T03 —— Extremal boundary 解释了为什么不能只用 sign-change edge

状态：`PROVED BY EXAMPLE / STRUCTURAL NECESSITY`

考虑 path

\[
+\;--\;0\;--\;+.
\]

没有任何相邻顶点乘积为负，因此

\[
E_{\pm}=\varnothing.
\]

但中心顶点属于

\[
V_0.
\]

这正对应 RN extremal `Delta=0` 的结构：零 expansion boundary 存在，但两侧 phase 相同。

因此任何只定义

\[
\text{horizon}=\text{positive/negative sign-change cut}
\]

的离散方案都会漏掉 extremal boundary。

最小统一对象必须保留：

\[
\boxed{V_0+E_{\pm}.}
\]

## 6. P019-G-T04 —— Boundary construction 对 primitive graph automorphism 自然协变

状态：`PROVED`

设

\[
\alpha:V\to V
\]

是 graph automorphism。

把 expansion 场同步搬运为

\[
\xi'(\alpha(v))=\xi(v).
\]

则

\[
\boxed{
\partial_{\xi'}G
=
\alpha(\partial_\xi G).
}
\]

原因是：

- `xi(v)=0` iff `xi'(alpha(v))=0`；
- `xi(u)xi(v)<0` iff `xi'(alpha(u))xi'(alpha(v))<0`；
- automorphism 精确保持 primitive adjacency。

所以 boundary 不依赖顶点命名或某个外部坐标标签。

这比径向 `n=h` 表述更接近 P012 所要求的 intrinsic geometry。

但它仍只保证**相对于已经选定的 primitive graph 与 expansion 场**的内禀性；并没有证明真实时空应该选哪个图或哪个 `xi`。

## 7. P019-G-T05 —— Schwarzschild/RN 是 graph boundary 的一维实例

状态：`PROVED BY SPECIALIZATION`

取 radial line graph

\[
0-1-2-3-\cdots
\]

并令

\[
\xi(n)=P(n)=n^2-an+b.
\]

则 `partial_xi G` 恰好退化为 RN 补充 01 的 vertex-edge boundary complex：

- `P(n)=0` 给出零顶点；
- `P(n)P(n+1)<0` 给出双视界 non-grid-aligned crossing edges。

再令 `b=0,a=h`：

\[
P(n)=n(n-h),
\]

正半径 boundary 恢复 Schwarzschild horizon `h`。

因此三阶段形成严格嵌套：

\[
\boxed{
\text{Schwarzschild}
\subset
\text{quadratic charged radial model}
\subset
\text{coordinate-free graph boundary skeleton}.
}
\]

## 8. P019-G-T06 —— Precision refinement 使 causal-phase ambiguity 单调不增

状态：`PROVED FROM P018`

固定有限 terminal vertex set `V`，令 precision observation 为

\[
O_\lambda:V\to Y_\lambda.
\]

对状态 `v` 的 observation fiber：

\[
[v]_\lambda
=
\{u:O_\lambda(u)=O_\lambda(v)\}.
\]

定义当前仍可能的 phase 集合

\[
\boxed{
\Phi_\lambda(v)
=
\{\phi(u):u\in[v]_\lambda\}.
}
\]

以及 phase ambiguity

\[
\boxed{
A^\phi_\lambda(v)=|\Phi_\lambda(v)|
\in\{1,2,3\}.
}
\]

若 `mu` 在 P018 意义下 refine `lambda`，则

\[
[v]_\mu\subseteq[v]_\lambda,
\]

所以

\[
\Phi_\mu(v)\subseteq\Phi_\lambda(v)
\]

并得到

\[
\boxed{
A^\phi_\mu(v)
\le
A^\phi_\lambda(v).
}
\]

这给 P019 一个比“径向位置 ambiguity”更直接的物理候选量：随着 precision 增加，一个 observation 对“我是 expansion / marginal / contraction 哪一相”的不确定类型数只能减少。

同样必须强调：这仍是 precision ambiguity，不是 thermodynamic entropy。

## 9. P019-G-T07 —— Boundary certificate 可以比完整状态恢复更早完成

状态：`DIRECT P018 CONSEQUENCE`

为了判断一个状态是否已经确定处于正相或负相，不必把 terminal vertex 唯一恢复出来。

只要 observation fiber 上 `phi` 已经恒为 `+1`，就得到稳定 OUTSIDE/EXPANDING certificate；恒为 `-1` 就得到稳定 INSIDE/CONTRACTING certificate。

由 P018 predicate certificate persistence，进一步 refinement 不会推翻已经常值的 phase certificate。

所以 horizon detection 更适合被表述为 **predicate-complete precision** 问题，而不是 state-complete precision 问题。

这与 P018 的主方向完全一致：自然问题往往不要求无限精度重建全部状态，只需要有限 precision 足以决定目标结构。

## 10. 当前得到的 coordinate-free 核心

到这里，P019 已经不再需要用

\[
r=r_s
\]

作为 horizon 的定义。

当前最小数学候选是：

\[
\boxed{
\text{primitive graph}
+
\text{integer outgoing-expansion field}
+
\text{zero vertices / crossing edges}
+
\text{finite precision fibers}.
}
\]

其中 horizon/boundary 是

\[
\boxed{\partial_\xi G=(V_0,E_{\pm}).}
\]

它有四个目前已经证明的优点：

1. 不需要 radial coordinate；
2. 不需要隐藏 Euclidean distance；
3. 同时容纳普通和 extremal boundary；
4. 在 primitive graph automorphism 下自然搬运。

## 11. 仍然没有解决的问题

这个抽象只是把问题推进到真正困难的位置，并没有完成黑洞理论。

### 11.1 `xi` 从哪里来？

我们目前把 integer outgoing-expansion field 当作输入。真正的物理理论必须由局部状态、能量/物质与演化律产生 `xi`，而不是手工标注。

### 11.2 directed causality

P012 当前第一阶段以 undirected primitive adjacency 建立 metric。真实 causal structure 更自然是 directed graph / relation。P019 下一步要研究 directed refinement，而不能把无向 skeleton 当最终因果本体。

### 11.3 locality

`xi(v)` 应当由多大的局部 neighborhood 决定？如果需要全图扫描，就失去局部物理意义。

### 11.4 dynamics

静态 boundary 只是切片。黑洞形成、蒸发、并合要求

\[
G_t,\xi_t,\partial_{\xi_t}G_t
\]

随 time 演化。

### 11.5 与连续 GR 的 invariant 对应

必须比较 trapped surface、null expansion、event horizon/apparent horizon 等不同外部概念，不能把它们都压成一个词 “horizon”。

## 12. 本阶段 ledger

- `P019-G-T01`：discrete causal intermediate-value theorem —— `PROVED`
- `P019-G-T02`：boundary removal makes each connected component phase-homogeneous —— `PROVED`
- `P019-G-T03`：zero vertices are necessary for extremal boundaries —— `PROVED STRUCTURAL NECESSITY`
- `P019-G-T04`：graph-automorphism equivariance —— `PROVED`
- `P019-G-T05`：RN/Schwarzschild specialization —— `PROVED`
- `P019-G-T06`：phase ambiguity is nonincreasing under P018 refinement —— `PROVED`
- `P019-G-T07`：phase predicate completeness can precede state completeness —— `P018 CONSEQUENCE`

Executable checks：

- `src/enterprise_math/causal_boundary.py`
- `tests/test_causal_boundary.py`

## 13. 下一步

1. 把 `G` 升级成 directed primitive causal graph；
2. 从 one-step future reachability 定义一个不依赖手工输入的 integer expansion candidate；
3. 研究该 expansion 在图 refinement / scale projection 下是否相容；
4. 对动态 `G_t` 建立 boundary creation/merge/split 的整数事件分类；
5. 再用 Kerr 作为旋转压力测试，判断 boundary complex 是否必须从 vertex/edge 升级到 higher cells。
