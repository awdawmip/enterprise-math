# Causal Transfer Dimension Core —— 守恒搬运几何中的统一维数链

状态：`ACTIVE CROSS-ROUTE RESEARCH CORE / EXACT CONDITIONAL THEOREMS`

归属：A5/P022 几何与 A0 foundation 应消费；本文件在当前 research branch 作为跨线恢复入口。

## 1. 目的

本文件不把“维数”定义成坐标数量。

研究对象是一个 conservative slot-transfer system：

- `N` 个 integer relation slots；
- primitive relation由 transfer graph `G` 的 edges给出；
- edge `{i,j}` 表示允许一个不可分 unit在 `i,j` 间直接搬运；
- 每个 connected component 的 total charge严格守恒。

问：这个系统内部能用多少种彼此独立的方法测到同一个 relation dimension？

## 2. relation rank

若 `G` 有 `c(G)` 个 connected components，则允许 displacement满足每个 component total为 0。

所以：

\[
\boxed{
p_G=N-c(G).
}
\]

这是 incidence lattice 的 integer rank。

connected case：

\[
p_G=N-1.
\]

## 3. contraction independence

primitive relation edge `e` 被 contract，表示把两个 slots识别为一个 coarse slot。

一组 edges `F` 若逐条 contraction时每一步都真正令 relation rank降 1，则称其 contraction-independent。

严格等价：

\[
\boxed{
F\text{ independent}
\iff
F\text{ is a forest}.
}
\]

因此 maximal independent relation sets就是 spanning forests。

其大小恒为：

\[
\boxed{|F_{max}|=N-c(G)=p_G.}
\]

traditional graphic matroid 在这里是“哪些 primitive relations代表独立 dimension losses”的组合 shadow。

## 4. tree basis 与 simple-cubic chart

connected spanning tree恰有 `N-1` edges，形成 zero-sum lattice 的一个 integer basis。

以这些 edge flows作为 coordinates，primitive moves为：

\[
\pm e_1,\ldots,\pm e_{N-1}.
\]

所以每一棵 spanning tree都是一个：

\[
\boxed{\mathbb Z^{p_G}/L^1}
\]

basis-only chart。

这解释了 simple-cubic type geometry为什么可以作为 coordinate chart，而不必成为底层唯一 primitive law。

## 5. general transfer metric 是全部 basis charts 的 lower envelope

对 connected `G`：

\[
\boxed{
d_G(x,y)
=
\min_{T\in ST(G)}d_T(x,y).
}
\]

任意 minimum integer flow都可去掉 circulation cycle，得到 forest-supported optimum，再扩成 spanning tree。

因此 geometry不是“选一个 basis”；它是所有 independent relation bases在 primitive future language下共同留下的 minimum operation cost。

complete anonymous transfer `K_N` 是所有 slot-pair shortcuts都 primitive的特例。

## 6. word ball 与 symmetric edge polytope

令 oriented incidence matrix columns为 primitive displacements `b_e`。

word norm：

\[
\|x\|_G
=
\min_{Bz=x,\,z\in\mathbb Z^E}
\sum_e|z_e|.
\]

令：

\[
P_G=\operatorname{conv}\{\pm b_e\}.
\]

incidence matrix totally unimodular，因此对 integer RHS，real `l1` flow relaxation有 integer optimum。

所以：

\[
\boxed{
B_G(r)
=
L_G\cap rP_G.
}
\]

即 primitive operation radius-r ball恰为 symmetric edge polytope dilation 的 lattice points。

因此 traditional Ehrhart count：

\[
|rP_G\cap L_G|
\]

就是 causal word-ball count。

Ehrhart degree等于 polytope dimension，而这里 dimension恰为 incidence rank：

\[
\boxed{
\deg |B_G(r)|
=
p_G=N-c(G).
}
\]

所以 ball-growth degree不是单独引入的维数定义；它被同一个 charge/transfer structure强迫与 relation rank一致。

## 7. directional relation boundary exact 降一维

固定 oriented primitive edge `e`：

\[
C_{G,e}(r)
=
\{x\in B_G(r):x+b_e\notin B_G(r)\}.
\]

contract edge endpoints：

\[
G\to G/e.
\]

slot-merge projection严格给：

\[
\boxed{
C_{G,e}(r)
\cong
B_{G/e}(r).
}
\]

只要 `e` 不是 loop，edge contraction令 relation rank降 1：

\[
p_{G/e}=p_G-1.
\]

所以一个 primitive directional relation boundary本身就是低一 relation-rank complete ball。

全部 directed relation boundary：

\[
\boxed{
|\partial_{rel}B_G(r)|
=
2\sum_{e\in E(G)}|B_{G/e}(r)|.
}
\]

因此 relation boundary growth degree严格为 `p_G-1`。

## 8. 与 state shell 的区别

state shell：

\[
S_G(r)=B_G(r)\setminus B_G(r-1)
\]

是 radius growth 的 first integer difference，因此其计数degree也降 1。

但一般：

\[
|S_G(r)|
\neq
|B_H(r)|
\]

对任何固定低一维 family `H`。

relation boundary则有 exact contraction target `G/e`。

所以：

\[
\boxed{
\text{state shell: degree lowering};
\qquad
\text{relation boundary: exact structure lowering}.
}
\]

## 9. 多次 contraction

沿一个 independent forest逐条 contract，每一步 relation rank降 1。

最大长度：

\[
\boxed{p_G.}
\]

到 spanning forest全部 contract后，每个 connected component只剩一个 coarse slot，relation rank为 0。

因此：

\[
\boxed{
\text{dimension}
=
\text{maximum exact primitive-relation contraction depth}.
}
\]

这与 relation rank / ball-growth degree独立得到同一个整数。

## 10. connected anonymous case

若基础 slots完全匿名且 primitive pair law对整个 `S_N` invariant，唯一 nonempty simple transfer graph是：

\[
K_N.
\]

所以其 rank：

\[
p=N-1.
\]

三维 `p=3`需要 `N=4` slots，complete transfer graph `K_4` 经纯 integer A3↔D3 map给 traditional FCC nearest-neighbor graph。

这不是因为先使用 sphere-packing density，而是 conservation + anonymity + primitive transfer law的结果。

## 11. spanning-tree charts 的有限 shadow

complete `K_N` 的 spanning-tree basis 数由 Cayley theorem：

\[
N^{N-2}.
\]

每棵 tree都是一个 basis-only/L1 chart。

full complete metric：

\[
d_{K_N}=\min_T d_T.
\]

而二阶 edge dispersion在所有 tree charts上的 finite sum满足：

\[
\boxed{
\sum_T P_T(x)
=
2N^{N-3}P_{K_N}(x).
}
\]

因为每条 complete-graph edge恰在 `2N^(N-3)` 棵 spanning trees中出现。

所以传统 min-plus 与 quadratic averaging可以同时作为同一 basis-chart family的不同 observation shadows。

## 12. 二阶 symmetric shadow

complete primitive relation field：

\[
P_{K_N}(x)
=
\sum_{i<j}(x_i-x_j)^2.
\]

严格恒等：

\[
P_{K_N}(x)
=N\sum_i x_i^2-(\sum_i x_i)^2.
\]

exact total kernel中：

\[
\boxed{
P_{K_N}(x)=N\sum_i x_i^2.
}
\]

若 pair-local quadratic observation要求 full slot anonymity，则所有 pair weights必须相同，因此该 quadratic shadow在这一 observation class中唯一到一个整数尺度。

traditional graph Laplacian / inner product因此可作为 primitive relation field 的 second-order shadow。

## 13. 统一 dimension certificate

在 conservative transfer class中，同一个整数：

\[
\boxed{p_G=N-c(G)}
\]

同时是：

1. charge-kernel relation rank；
2. maximal independent relation set size；
3. maximum primitive contraction depth；
4. word-ball/Ehrhart growth degree；
5. relation boundary target rank + 1；
6. spanning-forest basis size。

这是当前最强的内部 dimension agreement theorem之一。

## 14. 与 P008

任何 word-ball count：

\[
V_G(r)=|B_G(r)|
\]

都是因果 primitive operation law生成的 complete-growth candidate。

只要作为 `r -> V_G(r)` order embedding使用，P008 自动生成：

\[
R_{V_G},\qquad C_{V_G}.
\]

这样完整链是：

\[
\boxed{
\text{conservation}
\to
\text{primitive transfer}
\to
\text{word ball growth}
\to
\text{P008 root/collapse}.
}
\]

P008 不再需要先由外部选一个 `k^p` growth。

## 15. prior art 边界

以下均是成熟数学工具/对象，不作原创声明：

- graphic matroid / spanning-tree basis exchange；
- Cayley tree count；
- network incidence total unimodularity；
- earth mover / min-cost flow；
- symmetric edge polytopes；
- Ehrhart polynomial degree = lattice-polytope dimension。

项目当前的研究内容是它们在同一 causal LEGO ordering 下的统一解释，以及与 P008/P011/P012/P018/P019/P023 的 bridge。

## 16. 仍未证明

这套 dimension theorem是 **conditional transfer-geometry theorem**。

仍需独立证明：

- physical spatial dimension为何应等于这种 relation rank；
- physical vacuum为什么采用 exact unit-total conservation；
- slots为何应 full anonymous；
- primitive operation成本为何对应空间最小位移；
- 真实测量怎样从 relation boundary/graded future tower读出宏观长度与时间。

这些属于 P016 physical bridge/falsification，而不是本文件可以偷渡的前提。
