# Stage131 — Binary AND Tree 中的 Rooted-Circuit Table Explosion

状态：`RESEARCH BRIDGE / NONCANONICAL`

unary chain 只暴露了 transitive redundancy。multi-premise Horn closure 出现更强现象：即使 compositional basis 只是一个 tree，完整 one-round rooted-circuit premise table 也会因为枚举所有 inclusion-minimal root premises，而对 leaf count 呈 exponential growth。

## 1. Local basis

取 height h 的 balanced binary AND tree，leaves 数：

`L=2^h`。

每个 internal node 只有一条 local Horn rule，由两个 children 推出。

整个 compositional basis 只有：

`L-1=2^h-1`

条 rules。

从全部 leaves 出发，需要 h 个 synchronous rounds derive root。

## 2. 这里的 rooted-circuit premise 是什么

对一个 internal node r，rooted-circuit premise 是一个 inclusion-minimal seed set P，满足：

`r in Cl(P)`

且 `r notin P`。

所以 circuit table 列出的，是“哪些 minimal seed patterns 可以让 r 被直接视为一轮可得”。

这些 premises 不要求位于同一个 tree level。

## 3. Availability recurrence

令 `A_h(z)` 统计让 height-h node available 的 minimal ways，**允许 node 自己直接作为 seed**。`z^m` coefficient 表示 width-m minimal availability sets 数量。

对 leaf：

`A_0(z)=z`。

对 internal node，只有两类互不包含的 minimal way：

1. 直接 seed node：贡献 z；
2. 左右 children 各自以某种 minimal way available：贡献 `A_(h-1)(z)^2`。

因此：

`A_h(z)=z+A_(h-1)(z)^2`。

## 4. Rooted-circuit width polynomial

对 root 本身，直接 seed root 不算 rooted-circuit premise，所以：

`P_h(z)=A_(h-1)(z)^2=A_h(z)-z`。

`[z^m]P_h` 精确等于 width-m inclusion-minimal root premises 的数量。

branch 对 height4 以内的全部 minimal premise sets 做 explicit enumeration，并与 polynomial 完全对照。

## 5. Exact count recurrence

记：

`M_h=P_h(1)`

为 height-h root 的 rooted-circuit premise 数。

则：

`M_1=1`，

而 `A_(h-1)(1)=1+M_(h-1)`，所以：

`M_h=(1+M_(h-1))^2`。

前几项：

`1, 4, 25, 676, 458329, 210066388900, ...`。

这不是 implementation explosion，而是 root 的 inclusion-minimal premise sets 的 exact combinatorial count。

## 6. Small examples

### Height1

只有一个 circuit：

`{left leaf,right leaf}`。

所以：

`P_1(z)=z^2`。

### Height2

root 有四个 circuits：

- 两个 child nodes；
- left child + right subtree 两 leaves；
- left subtree 两 leaves + right child；
- 全部四 leaves。

所以：

`P_2(z)=z^2+2z^3+z^4`。

### Height3

`P_3(z)` 为：

`z^2+2z^3+3z^4+4z^5+5z^6+6z^7+4z^8`，

coefficients 总和25。

## 7. 每一种 premise width 都会出现

归纳假设 `A_(h-1)` 在全部 degrees

`1,...,2^(h-1)`

上 coefficient 都为正。

平方以后，所有 sums

`2,...,2^h`

都会出现。

因此：

`P_h(z)`

在 width2 到全部 `2^h` leaves 的**每一个 width**上都有 rooted circuits。

所以 root 不是只拥有 level-frontier 那几种 `2,4,8,...` widths，而是一个 dense minimal-premise width spectrum。

## 8. 对 leaf count 的 exponential growth

对 h>=2：

`M_h >= M_(h-1)^2`，

且 `M_2=4`，因此：

`M_h >= 2^(2^(h-1))`。

写 `L=2^h`，即：

`M_h >= 2^(L/2)`。

另一方面，对 `1+M_h` 做简单上界可得：

`M_h < 2^(2^h-1)=2^(L-1)`。

所以 root circuit table 对 leaf count 是 exponential：

`2^(L/2) <= M_h < 2^(L-1)`。

local basis 仍然只有 `L-1` rules。

## 9. 全部 internal-node rooted circuits

height-h tree 中，height t 的 nodes 有 `2^(h-t)` 个。

所以全部 internal nodes 的 rooted-circuit rule count：

`C_h=sum_(t=1)^h 2^(h-t) M_t`。

exact examples：

- h=3：37 rooted-circuit rules vs 7 local basis rules；
- h=4：750 vs 15；
- h=5：459829 vs 31；
- h=6：210067308558 vs 63。

很快由 root term 主导。

## 10. Premise-literal storage 更大

生成多项式还直接记录 premise storage。

全部 root circuits 的 total premise literals 是：

`P_h'(1)`。

例如 h=5：

- root circuits：458329；
- total root premise literals：7048360；
- average premise width 约15.38；
- maximum width32。

所以即使只数 circuit rule 数，也仍然低估了 premise representation cost。

## 11. Explosion 的根源

对每个 internal node，每个 child 有两种结构性选择：

- 直接把 child atom 放进 premise；
- 用该 child 自己的任意 rooted-circuit premise 来 derive child。

左右 subtree choices 独立组合，于是产生 squaring recurrence。

rooted-circuit enumeration 会把 compositional subtree 中每一种 minimal alternative 全部展开成 separate one-round premise rule。

## 12. Minimal premise table 与 compositional basis 是不同 contract

local Horn basis 存的是**如何递归构造** conclusions。

rooted-circuit table 存的是**每一种 minimal premise set，若已经同时拥有，就能一轮得到 root**。

二者不是同一个 representation contract。

AND tree 中：

- basis storage 对 leaf count 线性；
- rooted-circuit table storage 对 leaf count exponential。

但两者表示完全相同的 closure law。

## 13. Stage131 interpretation

这给 unary transitive redundancy 更强的 negative boundary：

> rooted circuits 不只是稍微多存一些 transitive rules；在 multi-premise closure 中，它们可能因为枚举 minimal premise alternatives 而比 compositional basis 指数级更大。

同一个 explosion 同时也是 execution resource：每个 stored circuit 都提供 exact premise set 下的一轮 access。

因此正确问题不是“把所有 redundant circuits 删除”，而是：

> 在 declared storage / depth / workload contract 下，哪些 one-round premise macros 值得 materialize？

## 14. 与 Horn macro presentation 的关系

parent Horn generation 只缓存 selected derived macros，例如固定 span 的 subtree frontiers。

complete rooted-circuit table 则相当于 materialize **所有** minimal premise alternatives。

所以 selected macro caching 位于：

- local compositional basis；
- complete rooted-circuit table

之间。

这正是 multi-premise 版本的 adjacent basis / sparse shortcuts / full transitive table spectrum。

## 15. Presentation resources 现在还必须包括 premise antichain size

multi-premise system 的 presentation cost 至少来自：

- stored rule 数；
- total premise literals；
- maximum premise width；
- 每个 root 的 alternative minimal premise 数；
- declared seed/workload language 下的 execution depth。

因此 rooted-circuit count 只是一个 presentation-complexity coordinate，不是 universal semantic-size measure。

## Owner-local assets

- `stage131_rooted_circuit_table_explosion.py`；
- recurrence / width spectrum / explicit enumeration / exponential-bound tests；
- `STAGE131_ROOTED_CIRCUIT_TABLE_EXPLOSION.{en,zh}.md`。

## Prior art / status

Horn closure、minimal generators、antichains 与 generating functions 都是标准既有数学/CS。Enterprise Math 的项目价值是 Stage131 解释，以及 binary AND-tree 对 rooted-circuit storage semantics 的 exact pressure test。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。