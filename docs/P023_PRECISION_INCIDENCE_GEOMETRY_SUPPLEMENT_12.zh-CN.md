# P023 —— Precision Incidence Geometry，补充 12

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并桥接 P012 intrinsic discrete geometry  
依赖：P023-S9/S10/S11、P012 metric discipline  
纪律：bipartite block-incidence graphs、set partitions、directed/quasi-metric 思想与 integer coding depth 都属于成熟数学。本文记录的是它们在 finite precision 中的精确综合，不主张通用结构的历史优先权。

## 1. 两个 precision states 天然定义一张二部图

令 `E,F` 为同一个有限非空状态集 `X` 上的两个 equivalence relations。

构造 **precision incidence graph**：

- 左侧 vertices：`X/E`；
- 右侧 vertices：`X/F`；
- 当且仅当
  \[
  B\cap C\ne\varnothing
  \]
  时，在 `B in X/E` 与 `C in X/F` 之间连边。

记 edge set 为

\[
\boxed{
\Gamma(E,F)
=
\{(B,C):B\cap C\ne\varnothing\}.
}
\]

这张图与 block label 的命名无关，只取决于两个 precision relations 本身。

## 2. P023-S12-T01 —— Realized product classes 就是图的 edges

状态：`PROVED`。

common refinement `E cap F` 的每个 block，恰好对应一个非空 block intersection。因此

\[
\boxed{
|X/(E\cap F)|
=|\Gamma(E,F)|.
}
\]

formal Cartesian candidate count 是

\[
|X/E|\,|X/F|,
\]

所以未被任何真实 state 实现的 product-class tuples 数正好是

\[
\boxed{
U(E,F)
=|X/E|\,|X/F|-|\Gamma(E,F)|.
}
\]

因此 P023-S9 的“数 realized tuples，不数 formal product”原则，精确等价于 sparse bipartite graph 与 complete bipartite graph 的区别。

## 3. P023-S12-T02 —— Directed repair factor 就是最大 incidence degree

状态：`PROVED`。

假设当前已经知道 precision `E`，现在新增 task `F`。目标 precision 是 common refinement `E cap F`。

对一个 `E` block `B`，其中目标 blocks 的数量，恰好等于与它相交的 `F` blocks 数，也就是 incidence degree

\[
\deg_F(B).
\]

所以精确最小 repair alphabet 为

\[
\boxed{
\rho(E,F)
=
R(E\to E\cap F)
=
\max_{B\in X/E}\deg_F(B).
}
\]

这个量一般不对称：

\[
\rho(E,F)\ne\rho(F,E).
\]

这种不对称有真实任务含义：已经知道 `E` 时再补 `F`，与已经知道 `F` 时再补 `E`，成本不必相同。

## 4. P023-S12-T03 —— Directed repair spectrum 就是 degree spectrum

状态：`PROVED`。

把 `F` 加到 `E` 上的完整 relative repair spectrum 为

\[
\boxed{
\mathcal R_k(E\leftarrow E\cap F)
=
\sum_{B\in X/E}
\binom{\deg_F(B)}k.
}
\]

所以 S11 quotient-projection spectrum 正是 incidence graph 一侧 degree 的 binomial spectrum。

反方向任务使用另一侧 degrees：

\[
\mathcal R_k(F\leftarrow E\cap F)
=
\sum_{C\in X/F}
\binom{\deg_E(C)}k.
\]

两个方向共享同一批 edges，但局部 repair profile 可以非常不同。

## 5. 两个极端

### 当前精度已经充分

\[
\boxed{
\rho(E,F)=1
\iff
E\subseteq F.
}
\]

因为每个 `E` block 恰好只接触一个 `F` block，当且仅当每个 `E` block 都落在一个 `F` block 内。

因此 directed repair factor 为 1 的含义就是：当前保留的 precision `E` 已经能够决定 task `F`。

### Complete incidence

若每个 `E` block 都与每个 `F` block 相交，则 incidence graph 为 complete bipartite graph，并且

\[
\boxed{
\rho(E,F)=|X/F|,
\qquad
\rho(F,E)=|X/E|.
}
\]

这是 formal product 完全被实现的极端。若没有额外概率结构，不应把它直接称为 probabilistic independence；这里只是 complete combinatorial incidence。

## 6. P023-S12-T04 —— Multiplicative triangle inequality

状态：`PROVED`。

对任意三个 finite precision relations `E,F,G`，

\[
\boxed{
\rho(E,G)
\le
\rho(E,F)\rho(F,G).
}
\]

### 证明

固定一个 `E` block `B`。任意与 `B` 相交的 `G` block `D` 中，都存在某个 `x in B cap D`。该 `x` 同时属于某个 `F` block `C`，所以 `C` 同时与 `B,D` 相交。

`B` 至多接触 `rho(E,F)` 个不同 `F` blocks；每个这样的 `F` block 又至多接触 `rho(F,G)` 个不同 `G` blocks。因此 `B` 最多接触二者乘积这么多个 `G` blocks。

对所有 `E` blocks 取最大值得证。∎

所以 `rho` 是 finite precision states 上一个 multiplicative directed distance-like quantity。

## 7. Integer symbol-depth

固定整数 alphabet base

\[
B\ge2.
\]

定义 integer symbol depth：

\[
L_B(n)
=
\min\{\ell\in\mathbb N_0:n\le B^\ell\}.
\]

这是项目已有的自然 integer information-level 构造，不需要 logarithm。

定义 directed precision depth：

\[
\boxed{
d_B(E,F)=L_B(\rho(E,F)).
}
\]

它表示：从已知 `E` 增加 task `F` 时，在最坏局部 `E` fiber 中至少需要多少个 base-`B` repair digits/symbols 才足够。

## 8. P023-S12-T05 —— Directed integer triangle inequality

状态：`PROVED`。

对任意 `E,F,G`，

\[
\boxed{
d_B(E,G)
\le
d_B(E,F)+d_B(F,G).}
\]

### 证明

令

\[
a=d_B(E,F),
\qquad
b=d_B(F,G).
\]

则

\[
\rho(E,F)\le B^a,
\qquad
\rho(F,G)\le B^b.
\]

由 T04，

\[
\rho(E,G)
\le B^{a+b},
\]

再由 `L_B` 的最小性，得到

\[
d_B(E,G)\le a+b.
\]

∎

另外，

\[
\boxed{
d_B(E,F)=0\iff E\subseteq F.}
\]

因此 directed distance 为零的含义是“从 `E` 出发回答 `F` 不需要增加额外 precision”，而不要求两个 precision states 完全相等。

这正符合 directed task-upgrade cost 的 preorder 行为。

## 9. P023-S12-T06 —— Precision relations 上的 symmetric integer metric

状态：`PROVED`。

定义

\[
\boxed{
D_B(E,F)
=
d_B(E,F)+d_B(F,E).
}
\]

则 `D_B` 是固定 finite state set `X` 上 equivalence relations 的一个 metric：

1. `D_B(E,F)>=0`；
2. `D_B(E,F)=D_B(F,E)`；
3. `D_B(E,F)=0` 当且仅当 `E=F`；
4. triangle inequality：
   \[
   \boxed{
   D_B(E,G)
   \le
   D_B(E,F)+D_B(F,G).
   }
   \]

### 证明

只需说明 definiteness 与 triangle。

若 `D_B(E,F)=0`，则两个 directed depths 都为 0，所以 `E subseteq F` 且 `F subseteq E`，于是 `E=F`。

对 triangle，分别对 `E -> F -> G` 和 `G -> F -> E` 应用 T05，再把两个不等式相加即可。∎

所以 finite precision states 获得了一种由 exact repair requirements 自然诱导的 integer-valued intrinsic geometry，而不是外加的 Euclidean coordinate。

## 10. 与 P012 的关系

P012 要求 geometry 来自显式声明的离散结构，而不是 hidden rounded Euclidean distance。

S12 提供了一种新的 derived geometry，其 primitive data 是：

- 一个 finite underlying state set；
- 两个 precision equivalence relations；
- nonempty block intersection；
- exact minimum repair multiplicity。

因此它应被理解为**precision-state geometry**，不是 physical-space geometry。

但它可以作为 proof/observation state spaces 上一种可复用的 P012-style graph metric。

## 11. 与 P023-S8/S9/S10/S11 的关系

incidence graph 把前四层结果压成同一结构的不同读数：

- S8 label recovery：相关最大 degree 等于 1；
- S9 minimum task repair：最大 block degree；
- S10 admissible-relation ambiguity：observation-side degree；
- S11 higher repair spectrum：binomial degree spectrum。

所以 “image separation”、“minimal repair”、“incidence repair”、“relative repair spectrum” 不是四套独立机制，而是同一个 finite incidence structure 的越来越丰富的 observables。

## 12. 研究工具含义

面对两个候选 precision descriptions，可以统一做以下 preflight：

1. 构造它们的 block-incidence graph；
2. 数实际 edges，而不是 formal Cartesian tuples；
3. 查看两侧 degrees，得到 exact directed repair factors；
4. 若 worst-case repair 不够，再用 degree binomial spectrum；
5. 若需要紧凑 integer transition/geometry cost，再使用 `d_B` 或 `D_B`。

这为 task addition、state compression 与 precision comparison 提供了统一有限语言。

## 13. 可执行规格

- `src/enterprise_math/precision_incidence_geometry.py`
- `tests/test_precision_incidence_geometry.py`

回归枚举四状态集合的全部 15 个 partitions，并对所有 `15^3=3375` 个 triples 检查 multiplicative repair triangle、directed integer triangle 与 symmetric metric triangle；同时把 incidence degree spectrum 与 S11 quotient-projection repair spectrum 交叉验证。

## 14. Foundation 边界

`D_B` 是 mathematical precision relations 上的 metric，不自动成为 physical spatial distance 或 ontological information metric。它的含义是 operational 且 exact 的：在声明的 finite observation/task states 之间转换时，需要多少离散 repair capacity。
