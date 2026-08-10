# Causal Conservation–Transfer Geometry —— 从守恒、primitive operation 与 future relation 生成离散几何

状态：`ACTIVE CROSS-ROUTE RESEARCH CORE / CONDITIONAL FOUNDATIONAL THEOREMS + EXECUTABLE REFERENCES`

归属：基础 primitive 应由 A0/A5/P022 评估；P019 几何结果可作为实例消费。本文件暂存在 relation-quotient research branch，原因是其核心 bridge 使用 future/context quotient，但不把几何 theorem-home 永久移到 A3。

## 1. 目的

本文件纠正一种继续滑回传统数学的风险：

> 先选 `Z^p / A_p / D_p / E_8 / FCC / HCP`，再给它们添加 precision / causal 标签。

新的顺序是：

\[
\boxed{
\text{conservation law}
\to
\text{allowed displacement kernel}
\to
\text{primitive operation law}
\to
\text{word geometry}
\to
\text{future continuation}
\to
\text{traditional shadow}.
}
\]

因此“哪个格”不再是第一问。

## 2. exact conserved unit 与 A 系

有 `N` 个整数 relation slots。若基础 displacement 严格保持一个 exact additive charge：

\[
Q(x)=\sum_i x_i,
\]

则 allowed relation difference 是：

\[
\boxed{
L_A=\ker Q
=\{x\in\mathbb Z^N:\sum_i x_i=0\}.
}
\]

它有整数 rank：

\[
\boxed{N-1.}
\]

这一步还没有选传统 root system。

## 3. primitive one-unit transfer

若一个 primitive operation：

1. 不改变 exact total；
2. 一次只搬一个不可分 unit `1`；
3. 只作用于一个 donor 与一个 receiver；

则 displacement 唯一是：

\[
\boxed{e_i-e_j.}
\]

如果 slots 在 primitive law 下完全匿名，即 law 对整个 `S_N` slot permutation group 不变，那么只要存在一条非平凡 pair transfer，整个 ordered-pair orbit 都必须存在。

所以 primitive set 被强迫为所有：

\[
\boxed{
\{e_i-e_j:i\ne j\}.
}
\]

传统 `A_(N-1)` root set 因此只是该 causal transfer law 的坐标 shadow。

## 4. 一个更强的 minimal-ontology 唯一性

设目标 relation rank 为 `p`。

若要求：

- 至少一个 nontrivial exact additive conserved charge；
- 只有一个 primitive exact charge；
- charge 对所有 slot permutations 不变；
- ambient slot 数最少；

则任意 `S_N`-invariant integer linear charge

\[
Q(x)=\sum_i a_i x_i
\]

在交换任意两个 slots 后不变，只能有：

\[
a_1=\cdots=a_N.
\]

primitive normalization 后就是 total charge。

一个 independent exact charge令 relation rank为：

\[
N-1.
\]

因此 rank `p` 的最小 ambient slots：

\[
\boxed{N=p+1.}
\]

从而：

\[
\boxed{
\text{anonymous single exact charge}
+\text{minimal ambient slots}
\Rightarrow A_p.
}
\]

这是条件唯一性，不是“宇宙已经证明采用 A_p”。

## 5. transfer graph：同一个 state lattice 可以有不同 geometry

更一般地，不要求所有 slot pairs 都能直接 primitive transfer。

给 slots 一个无向 transfer graph `G`：

\[
\{i,j\}\in E(G)
\]

表示允许 `i<->j` 的 one-unit direct transfer。

若 `G` 有 `c` 个 connected components，则 incidence moves 生成的 relation rank 是：

\[
\boxed{N-c.}
\]

每个 component 的 total 分别守恒。

特别地，任何 connected `G` 都生成同一个：

\[
\{x:\sum x_i=0\}
\]

state lattice。

但 word metric 由 `G` 决定。

所以：

\[
\boxed{
\text{state lattice}\ne\text{primitive geometry}.
}
\]

## 6. tree geometry = simple-cubic type

connected tree 只有 `N-1` 个 undirected edges。

这些 incidence vectors 已生成 rank `N-1` 的 relation lattice，数量又恰好等于 rank，所以构成一个整数 basis。

在 edge-flow coordinates 中 primitive moves就是：

\[
\pm e_1,\ldots,\pm e_{N-1}.
\]

因此 tree transfer law 的 abstract word geometry严格是：

\[
\boxed{\mathbb Z^{N-1}\text{ with }L^1\text{ primitive metric}.}
\]

这就是 simple-cubic / standard-axis 几何的 transfer-law来源。

star `K_(1,p)` 只是其中最直观的“显式 reservoir slot”坐标图。

## 7. complete graph = symmetry completion

若 slots 完全匿名，而 primitive transfer relation是 nonempty simple pair relation，则 `S_N` 对 unordered slot pairs transitive。

因此唯一 nonempty `S_N`-invariant transfer graph是：

\[
\boxed{K_N.}
\]

所以：

- tree：basis-only primitive law；
- complete graph：full slot-exchange symmetry completion。

它们生成同一个 state lattice，但不同 primitive metric。

额外 direct relation 的 independent 数量是 graph cycle rank：

\[
\beta_1(G)=|E|-|V|+1.
\]

对 `K_N`：

\[
\boxed{
\beta_1(K_N)=\frac{(N-1)(N-2)}2.
}
\]

它们是相对于 tree basis 新加入的直接 relation shortcuts。

## 8. 相对距离正确性：one-unit pair distance theorem

固定 slots `i,j`。

relation displacement：

\[
e_i-e_j.
\]

其 primitive word distance严格等于 slot graph shortest-path：

\[
\boxed{
 d_{rel}(0,e_i-e_j)
=\operatorname{dist}_G(i,j).
}
\]

路径给上界；任何 unit transfer sequence若净 effect 是 `j->i`，至少必须沿 transfer graph 把一单位 flow 从 `j` 连到 `i`，所以不能短于 graph distance。

因此若所有不同 slots 在基础层不可区分，并要求任意 pair 的 one-unit redistribution属于同一个最小 relation class，则：

\[
\operatorname{dist}_G(i,j)=1\quad\forall i\ne j.
\]

唯一可能：

\[
\boxed{G=K_N.}
\]

这给 simple cubic 的 axis bias 一个纯整数来源：tree graph人为让某些 anonymous slot pairs 必须绕 intermediate slots。

## 9. 三维：A3 到 FCC 的纯整数 bridge

rank 3 的 minimal one-charge ontology需要 4 个 slots：

\[
(a,b,c,d),\qquad a+b+c+d=0.
\]

定义：

\[
\boxed{
\Phi(a,b,c,d)=(a+b,a+c,b+c).
}
\]

其像恰为：

\[
D_3=\{(u,v,w)\in\mathbb Z^3:u+v+w\equiv0\pmod2\}.
\]

逆映射：

\[
a=(u+v-w)/2,
\quad
b=(u+w-v)/2,
\quad
c=(v+w-u)/2,
\]

由 parity condition 保证 exact integer division。

12 个 A3 primitive transfers一一映到 12 个 D3 nearest moves `±e_i±e_j`。

因此：

\[
\boxed{
\text{3D complete conservative transfer graph}
\cong
\text{traditional FCC nearest-neighbor graph}.
}
\]

这里没有使用“FCC 是 densest packing”作为选择理由。

### 条件物理解读

只有在另一个 bridge theorem 证明“physical spatial dimension = 当前 relation rank”之后，才能进一步说该结果直接选择 physical FCC adjacency。

目前它是严格的 rank-3 causal-relation theorem，不是实验物理定论。

## 10. D 系：conservation law 已经改变

`D_n` roots：

\[
\pm e_i\pm e_j.
\]

其中 `e_i+e_j` 改变 exact total `+2`。

所以 D 系不属于 exact-unit-total conservation ontology。

它保持的是：

\[
\boxed{
\sum_i x_i\pmod2.
}
\]

而：

\[
\boxed{
D_n=\{x\in\mathbb Z^n:\sum_i x_i\equiv0\pmod2\}.
}
\]

finite parity charge只限制 residue sector，不降低 integer rank：

\[
\operatorname{rank}D_n=n.
\]

所以 A/D 的差别可以解释成：

\[
\boxed{
A:\text{exact free charge conservation};
\qquad
D:\text{finite parity conservation}.
}
\]

## 11. E 系：更强 finite charge code + higher collective events

scaled `E8` 可写成 integer subgroup：

1. 八个 coordinates 同 parity；
2. coordinate sum 被 4 整除。

它是 full-rank finite-index constraint，不减少 rank 8。

对这个 kernel 看二阶 integer grade：

\[
Q_2(v)=\sum_i v_i^2.
\]

最小 nonzero grade为 8。

grade-8 events 恰好：

- 112 个两坐标 `±2` events；
- 128 个八坐标全 `±1` events、负号数偶数。

传统 scaled E8 roots由此出现。

E7再加 exact charge：

\[
\sum_i x_i=0,
\]

得到 rank 7；E6再加第二个 exact linear charge，得到 rank 6。

因此 E family也可以被解释为不同 charge architecture 的 minimum-second-order events，而不是先把 exceptional root system放进本体。

## 12. 一个重要的 grade 边界

`Q_2` equal grade不等于 equal unit-transfer cost。

对 exact-total E7 roots：

- 56 个 event 的实际 conserved transfer mass为 2；
- 70 个 event 的 transfer mass为 4；
- 但全部传统 root `Q_2=8`。

A roots则全部：

\[
\boxed{M_{transfer}=1.}
\]

所以若“1 是 primitive transfer quantum”，transfer count比 quadratic equal-length 更基础。

E roots可以作为 second-order/collision grade 的 emergent primitive shell，但不能只因 traditional equal root length 就自动和 one-unit A move处在同一 ontology 层。

## 13. primitive-direction causal profile

几何候选还需比较：

- primitive direction capacity；
- direction link connectivity；
- rooted edge context；
- compatible flag continuation signature；
- anisotropy split frontier `(relation arity, future depth)`。

已验证：

- FCC/A3 在 full compatible flag language 内不 split；
- HCP coarse coordination同为 12/degree4，但最小 split frontier含：
  \[
  (1,2),(2,1);
  \]
- D5 首 split `(3,1)`；
- E7 首 split `(5,1)`；
- E8 targeted result首 split `(7,1)`。

因此不采用单一“neighbor count/isotropy score”。

## 14. 挖球：一般 transfer-graph boundary contraction theorem

对 transfer graph `G` 的 word ball `B_G(r)`，固定 oriented primitive edge `e`，定义 directional relation cut：

\[
C_{G,e}(r)
=\{x\in B_G(r):x+b_e\notin B_G(r)\}.
\]

contract `e` 两端 slots：

\[
G\to G/e.
\]

则 coordinate merge projection在：

\[
\boxed{
C_{G,e}(r)
\leftrightarrow
B_{G/e}(r)
}
\]

之间给出 exact bijection。

所以：

\[
\boxed{
|\partial_{rel}B_G(r)|
=2\sum_{e\in E(G)}|B_{G/e}(r)|.
}
\]

这已经对全部 38 个 connected labeled four-slot simple graphs、每条 edge、多个小 radius 做 exhaustive integer oracle。

证明工具可用 integer min-cost flow / total unimodularity：word norm fiber在 `e` 方向形成 discrete convex interval，每个 nonempty fiber有唯一正向 endpoint。这里传统 optimization 是证明工具，不是 geometry ontology。

### A / SC 都被统一

`K_(p+1)/e=K_p`：

\[
E_{A_p,e}(r)=V_{A_{p-1}}(r).
\]

star/tree coordinate下也得到 standard-axis dimension lowering。

因此“relation boundary exact 降一维”是 transfer-graph contraction 的统一定理，而不是 FCC 特例。

## 15. graph Laplacian 作为二阶 shadow

对 primitive transfer graph：

\[
\boxed{
P_G(x)=\sum_{\{i,j\}\in E(G)}(x_i-x_j)^2.
}
\]

传统写法 `x^T L_G x` 中的 graph Laplacian，只是 primitive edge relation 的 second-moment summary。

对 complete graph：

\[
P_{K_N}(x)
=N\sum_i x_i^2-(\sum_i x_i)^2.
\]

在 exact total kernel：

\[
\boxed{
P_{K_N}(x)=N\sum_i x_i^2.
}
\]

这正好回收 P019 pair-dispersion identity，并给 quadratic `q` 一个 relation-first解释。

star/tree marked geometry则不具有该 full-pair identity；相同 slot quadratic grade的 states可产生不同 edge dispersion。

## 16. 当前核心分层

当前最小几何 ontology candidate 是：

\[
\boxed{
\text{charge kernel}
+
\text{primitive transfer graph/law}
+
\text{future continuation type}
+
\text{optional higher observation grade}.
}
\]

分别控制：

1. relation rank / dimension candidate；
2. primitive metric / local direction geometry；
3. material/stacking/history-dependent behavior；
4. quadratic/collision/radial 等 observation shadow。

这比“传统 lattice + precision tag”更接近当前 Enterprise Math 路线。

## 17. 尚未证明

不得越界声称：

- physical space 已证明等于 relation rank；
- vacuum 必定采用 exact total charge ontology；
- full slot-exchange symmetry 是自然界实测对称性；
- FCC 已被物理实验唯一选出；
- HCP/D/E 不能作为其它物理 regime 的基础结构。

这些必须进入 P016 physical falsification / bridge program。

## 18. 可执行资产

- `causal_conserved_transfer_geometry.py`
- `causal_transfer_graph_geometry.py`
- `causal_transfer_boundary_contraction.py`
- `causal_charge_kernel_geometry.py`
- `causal_charge_grade_roots.py`
- `causal_primitive_link_profile.py`
- `causal_geometry_selection.py`
- `causal_transfer_quadratic_shadow.py`
- 对应 `tests/test_causal_*.py`

当前 full local repository CI 尚未因环境 DNS 限制运行；小规模 exhaustive integer oracles 与 connector-authored regression 已持续维护。该门禁滚动处理，不阻断数学研究。
