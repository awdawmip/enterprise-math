# P019 —— Causal Local Isotropy：Primitive Direction Link、FCC/HCP 与高维候选竞争

状态：`ACTIVE CROSS-ROUTE RESEARCH / EXACT DISCRETE THEOREMS + CANDIDATE AXIOMS`

本文件不占用并发中的顺序 Supplement 编号。它记录 minimum-precision geometry 路线上一组独立结果，并与 P019 Supplement 10–13 保持并行，等待 canonical semantic replay。

## 1. 研究纠偏

此前“若 1 是最小空间精度，simple cubic 可能无法忠实表达相对方向，FCC/HCP 更自然”的直觉不能靠 packing density 或 hidden Euclidean angle 落地。

当前更严格的问题是：

\[
\boxed{
\text{primitive directions 在最小 adjacency language 内本身形成什么 finite relation structure？}
}
\]

因此比较对象从“球堆积”改成：

- primitive-neighbor set；
- primitive-direction link；
- primitive-edge common-neighbor context；
- higher-shell stabilizer orbit profile；
- graph-ball growth；
- relation boundary；
- graded future-resolution behavior。

## 2. A_p primitive-direction link

对

\[
A_p=\{x\in\mathbb Z^{p+1}:\sum_i x_i=0\},
\]

primitive moves 为

\[
e_i-e_j,\quad i\ne j.
\]

以 ordered pair `(i,j)` 表示一个 direction。两个 first-shell endpoints 之间仍有 primitive edge，当且仅当

\[
\boxed{(i,j)\sim(k,l)\iff i=k\ \text{或}\ j=l.}
\]

所以：

\[
\boxed{N_1=p(p+1)},
\]

\[
\boxed{\deg L_p=2(p-1)},
\]

\[
\boxed{|E(L_p)|=p(p+1)(p-1)}.
\]

`p>=2` 时 first-direction link 连通，diameter 3。

### A2

6 directions、degree 2，direction link 是 6-cycle。

### A3

12 directions、degree 4、24 link edges；组合上有 8 triangles 与 6 chordless row/column rectangles。

这与 cuboctahedral local link 的有限图数据一致。成熟 lattice 文献中 A3 与 FCC 是同一三维 root-lattice/FCC 结构的不同表示；该对应不属项目原创。

## 3. A_p primitive-edge context theorem

固定 primitive edge

\[
0\leftrightarrow e_i-e_j.
\]

其 common primitive neighbors 分成

\[
\{e_i-e_k:k\ne i,j\}
\]

与

\[
\{e_k-e_j:k\ne i,j\}.
\]

两组分别为 clique `K_(p-1)`，组间无 primitive edge，因此：

\[
\boxed{
\operatorname{CN}_{A_p}(e_i-e_j)
\cong
K_{p-1}\sqcup K_{p-1}.
}
\]

所有 primitive edges 完全同型。

整数 signature：

\[
\boxed{
\left(
2(p-1),
2\binom{p-1}{2},
(p-1,p-1)
\right).
}
\]

对 A3：

\[
\boxed{(4,2,(2,2))}.
\]

这就是 graph-theoretic 421 common-neighbor pattern。

外部成熟 common-neighbor analysis 对 ideal close-packed structures 的标准识别是：FCC 12×421，HCP 6×421 + 6×422。因此 FCC/HCP 虽然 first coordination number 都为 12，却在 nearest-neighbor relation context 上已经分裂。

## 4. Simple cubic pressure test

standard-axis `Z^p` 的 primitive directions 为

\[
\pm e_i,
\]

共有 `2p` 个。

任意两个不同 first-shell endpoints 的 L1 difference 都不是 primitive step，因此 direction link 没有任何 edge：

\[
\boxed{|E(L_{Z^p})|=0.}
\]

所以 simple cubic 虽然 coordinate symmetries 能令 first directions 同 orbit，但在 minimum adjacency layer 内，direction 与 direction 之间没有 primitive triangular relation。

这提供一个不借 Euclidean angle 的结构差异。

## 5. Higher-shell orbit-count 单指标被否决

不能把

\[
a_\Lambda(r)=|S_\Lambda(r)/\operatorname{Stab}(0)|
\]

简单规定为“越小越 isotropic”。

在 radius 2：

### Z3

orbit types：

\[
(2,0,0),\qquad(1,1,0),
\]

所以

\[
\boxed{a_{Z^3}(2)=2},
\]

orbit sizes `6,12`，shell size 18。

### A3

orbit types：

\[
(2,-2,0,0),
\]

\[
(2,-1,-1,0)\text{ 及反号},
\]

\[
(1,1,-1,-1),
\]

所以

\[
\boxed{a_{A_3}(2)=3},
\]

orbit sizes `12,24,6`，shell size 42。

若只最小化 orbit count，反而会把 Z3 判得优于 A3。因此该单指标规则明确被拒绝。

## 6. Candidate local-isotropy axioms

以下只处于 `HYPOTHESIS / PRESSURE-TEST`。

### CLI-1 primitive-direction transitivity

所有 primitive directions 在 origin stabilizer 下结构等价。

### CLI-2 direction-link connectedness

对于 dimension>=2，primitive directions 在最小 adjacency layer 内应有一个连通 relation link，而不是互不相干的标签集合。

### CLI-3 primitive-edge context uniformity

每条 primitive edge 的 finite common-neighbor induced graph 应同构。

A_p 满足 CLI-1/2/3；simple cubic 失败 CLI-2；ideal HCP 的成熟 CNA 结果显示 nearest-neighbor bonds 有两种 context，因此若 CLI-3 最终保留，则 HCP 不满足 single-context primitive-lattice 版本。

但这些还不能定义唯一格。

## 7. D_n 反压：CLI 条件不会把 A_p 偷偷写死

对 root lattice `D_n`，primitive roots：

\[
\pm e_i\pm e_j,
\qquad i\ne j.
\]

纯整数 root-difference adjacency 给：

\[
\boxed{N_1=2n(n-1)},
\]

\[
\boxed{\deg L_{D_n}=4(n-2)}.
\]

`n>=3` direction link 连通且 primitive-edge context uniform。

### D3

12 directions、degree 4、24 link edges，edge common-neighbor signature：

\[
(4,2,(2,2)),
\]

与 A3/FCC 局部数据一致；这与 D3/A3 的低维同构相容。

### D4

\[
\boxed{N_1=24},
\]

\[
\boxed{\deg L=8}.
\]

每条 primitive edge 有 8 common neighbors，其 induced graph 已连通并有 12 internal edges：

\[
\boxed{(8,12,(8))}.
\]

而 A4 只有 20 primitive directions、link degree 6，edge context `K3 sqcup K3`。

因此 CLI-1/2/3 在 4D 同时允许 A4 与 D4，甚至 D4 的局部 relation 更丰富。结论是：

\[
\boxed{
\text{三维 FCC/A3 的成功不能外推成“所有维度固定选 A_p”。}
}
\]

每个维度应让 A/D/E 等候选在同一 causal diagnostics 下重新竞争。

实现：

- `causal_lattice_direction_link.py`
- `causal_d_lattice_direction_link.py`
- 对应 tests。

## 8. FCC/HCP 不应先作为两套本体：close-packed continuation law

close-packed layer registries 记为

\[
s_n\in\mathbb Z/3\mathbb Z,
\]

相邻 layer 不能使用同一 registry。定义相对一步：

\[
\delta_n=s_{n+1}-s_n\in\{+1,-1\}\pmod3.
\]

给定两层以后，下一层只有两种 close-packed choice：

\[
\boxed{F:\delta\mapsto\delta},
\]

即继续到第三 registry；以及

\[
\boxed{H:\delta\mapsto-\delta},
\]

即回到两层之前的 registry。

固定前两层以后：

\[
\boxed{
\{F,H\}^{N-2}
\longleftrightarrow
\text{length-N close-packed stacking sequences}
}
\]

为一一对应。

- `FFFF...` 生成 `ABCABC...`：FCC stacking；
- `HHHH...` 生成 `ABAB...`：HCP stacking；
- 一般 F/H word 生成 stacking fault / polytype support sequence。

所以在本体顺序上更自然的是：

\[
\boxed{
\text{one local close-packed support law}
+\text{continuation trajectory}
\to
\text{FCC/HCP/polytype}.
}
\]

而不是先把 FCC/HCP 当两个 unrelated spaces。

绝对 registry phase 在 global `+1 mod 3` relabel 下改变，但 `delta` 与 F/H word 不变，所以 phase 是 coordinate/gauge-like label，不属于最小 relative continuation state。

实现：

- `causal_close_packed_stacking.py`
- `tests/test_causal_close_packed_stacking.py`

## 9. support law 与 physical grade 必须继续分离

close-packed support 只需要 2-state relative continuation，并不意味着真实材料的 grade/energy/entropy 只依赖两层。

如果 higher-order physical observation 读取更多 stacking context，`CAUSAL_OPERATION_CLOSURE_CORE` 会自动把 continuation state 细化。此前 finite-range grade theorem、weighted future quotient、semantic grade 都可直接复用。

因此：

\[
\boxed{
\text{support complexity}
\ne
\text{physical observation complexity}.
}
\]

## 10. 当前 comparison vector

暂不压成单一 scalar：

\[
\boxed{
\mathcal I(\Lambda)=
(N_1,
\mathrm{orbit}_1,
\mathrm{LinkConnectivity},
\mathrm{EdgeContextTypes},
\mathrm{ShellOrbitProfile},
\mathrm{BallGrowth},
\mathrm{RelationBoundary},
\mathrm{FutureStateComplexity}).
}
\]

这比 packing density 单指标更符合 Enterprise Math 的 causal/discrete discipline。

## 11. 当前结论等级

### 已证内部结果

- A_p direction-link closed formulas；
- A_p edge common-neighbor context `K_(p-1) sqcup K_(p-1)`；
- Z^p first-direction link edgeless；
- A3 radius-2 orbit count 3 vs Z3 orbit count 2；
- D_n local-link pressure-test formulas；
- close-packed F/H continuation bijection。

### 成熟外部事实

- A3/FCC correspondence；
- CNA local-structure method；
- ideal FCC 12×421 与 ideal HCP 6×421+6×422。

### 仍是候选

- CLI-1/2/3 是否真应成为 minimum-precision axioms；
- 每个 dimension 最优 candidate family；
- primitive direction link 与 Voronoi precision domain 的最终 bridge；
- local isotropy 与实际物理 measurement 的 falsification contract。

## 12. 下一步

1. 对 E8 与其它高对称候选计算同一 local comparison vector；
2. 构造满足 CLI-1/2/3 却明显物理不合理的反例，压力测试 axioms；
3. 将 close-packed continuation 的 higher-order observation state 用一般 operation-language quotient 自动最小化；
4. 研究 local direction-link 是否能从 finite Voronoi/Delaunay incidence 纯组合地恢复；
5. 仅在这些压力测试通过后，才考虑把 FCC/A3 从 candidate 升格为 3D minimum-precision model。
