# 图拓扑事件作为精度转移

状态：`RESEARCH BRIDGE / NONCANONICAL`

本文件是 `PRECISION_GRAPH_EXACT_SEQUENCE.zh.md` 的架构伴随说明，只提炼标准图论结论的 precision 解释，不新增图论 theorem，也不与 E001 topology-removal owner 竞争。

对固定顶点数 `V` 的有限图，记 edge 数为 `E`、connected component 数为 `c`、cycle rank 为

`beta=E-V+c`。

标准 graph homology 给出

`rank H_0=c`，
`rank H_1=beta`，

因此

`rank H_0-rank H_1=V-E`。

当同一张图既被用于 edge-history fiber，又被用于 vertex-ledger redistribution 时，这个恒等式可以读成一条精确的 topology/precision ledger。

## 1. 增加一条 edge

只有两种情况。

### 1.1 连接两个原本不同的 components

`c -> c-1`，`beta` 不变。

precision 解释：

- vertex-ledger 侧：两个原本独立的 component totals 可以经新 transfer path 相互混合，因此独立 H0 invariant 少一个；
- edge-history 侧：没有产生新的 cycle，所以 hidden H1 history 不增加。

### 1.2 edge 加在同一个 component 内

`c` 不变，`beta -> beta+1`。

precision 解释：

- vertex-ledger 侧：component-total invariant rank 不变；
- edge-history 侧：新增一条 independent cycle-history direction，在 incidence 投影到 vertices 后不可见。

## 2. 删除一条 edge

两种情况完全反向。

### 2.1 删除 bridge

`c -> c+1`，`beta` 不变。

新增一个独立 vertex-component total；cycle-history rank 不变。

### 2.2 删除 non-bridge cycle edge

`c` 不变，`beta -> beta-1`。

消掉一个 hidden cycle-history direction，而 vertex component-total invariant rank 不变。

## 3. 架构结论

拓扑事件不能只概括为“更连通 / 更不连通”。它具体改变哪一种 precision resource，取决于 edge event 发生在 component 之间还是 component 内部：

```text
bridge addition / removal
    <-> 改变 H0 / conserved component-ledger precision

cycle-edge addition / removal
    <-> 改变 H1 / hidden edge-history precision
```

这也把两条已有研究线统一到同一 boundary operator 上：

- contact cycle break 会减少 edge-history 侧的 H1 hidden fiber；
- transfer graph split 会增加 vertex-ledger 侧的 H0 conserved coarse coordinates。

如果 future law 还观察 transfer path 自身的历史，那么 transfer graph 的 H1 也会成为隐藏 policy-history；这时应在 exact-sequence 框架内增加对应 witness，而不能把它混成 vertex component totals。

上述恒等式都是标准 Euler-characteristic / graph homology 事实。项目价值仅在 precision-first 解释与跨路线 routing。
