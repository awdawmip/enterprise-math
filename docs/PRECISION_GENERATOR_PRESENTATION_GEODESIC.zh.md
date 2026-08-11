# Minimum Precision Design 作为 Generator-Presentation Geodesic

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Design / execution separation 有一个直接的 algebraic 形式：generator presentation 会给 semantic operation algebra 赋予 word-length / weighted-cost geometry。Minimum precision design 因而可以被解释成某个 target semantic effect 的 shortest expression。

对 Set-Cover OR semilattice，这个 target geodesic **精确就是** Minimum Set Cover。

## 1. Presented OR semilattice

把 semantic effect state 表示成 m-bit universe mask。

每个 primitive action i 有 mask `a_i`，并作用于 semantic effect：

`x -> x OR a_i`。

Identity 是 mask0。Full precision target 是 full mask：

`Omega=2^m-1`。

Literal word `i_1...i_h` 的 forward evaluation 是：

`a_i1 OR ... OR a_ih`。

这个 forward execution formula 极其简单。

## 2. Generator presentation 诱导 Cayley geometry

在 semantic masks 上建立 directed right Cayley graph：

`x --i--> x OR a_i`。

每个 generator unit cost。对 reachable effect t，presentation-induced distance 是生成 t 的 shortest word length。

因为 OR generators idempotent 且 commute，word 中的 repeated occurrence 可以删除、order 不重要。因此 shortest words 精确对应 generator subsets。

## 3. Full-precision design 就是 target distance

对于 target `Omega`，generator subset 到达 Omega，当且仅当对应 candidate sets cover whole universe。

因此：

`d_A(0,Omega)=minimum Set Cover cardinality`。

本 branch 对全部 3-element / 3-generator incidence families 逐一验证。

所以 minimum precision-preserving capability design 就是：**在 generator presentation 确定以后，semantic algebra 中的一个 geodesic problem。**

## 4. Weighted design 是 weighted geodesic synthesis

给 primitive generator 非负 cost `c_i`。

同一 Cayley graph 把 edge cost 设为 `c_i`，从0到 target 的 shortest path cost 就是：

`min sum c_i`

其中 generator subset 的 union 到达 target。

对 full mask，这精确就是 weighted Set Cover。

Owner 用 bounded brute-force weighted-cover oracle 对照 Dijkstra 结果。

## 5. Same abstract monoid，不同 word metric

Abstract semantic algebra 本身不能决定这个 distance。

固定 universe size m，比对两个 `m+1`-generator presentations，它们都生成完整 Boolean semilattice `2^[m]`：

- singleton generators + 一个 duplicate singleton；
- singleton generators + 一个 full-universe generator。

两边 semantic effects 都是相同的 `2^m` masks，composition law 都是 OR。

但：

`d_A(0,Omega)=m`，

而

`d_B(0,Omega)=1`。

Distance gap 是 `m-1`。

因此 presentation-induced word metric 不是 abstract generated monoid invariant。

## 6. Forward execution 与 inverse synthesis

两个方向结构不同。

### Forward

输入：一个 generator word。

输出：它的 semantic effect。

在 OR semilattice 中：

`effect = generator masks 的 bitwise OR`。

Work 对 input length 线性，parallel depth logarithmic。

### Inverse

输入：target effect Omega。

输出：达到 Omega 的 minimum-cost generator word / subset。

同一个 family 中这就是 Set Cover。

所以简单 forward homomorphism 可以拥有困难的 minimum-preimage problem。

## 7. 为什么 explicit-state shortest path 不与 NP-hardness 冲突

若把完整 semantic monoid 显式展开，它有 `2^m` 个 mask states。Standard BFS 可以在这个**expanded graph size**上 polynomial 地求 unit-cost target geodesic。

但 Set Cover input 是 compact 的：m 个 universe coordinates 与 k 个 generator masks 可按 O(mk) incidence bits 存储。

显式 semantic state space 对 m 指数增长。

所以 NP-hardness 与 easy explicit BFS 完全兼容：

`compact generator presentation -> exponentially large semantic Cayley state space`。

难点是 succinct inverse synthesis，而不是 local transition evaluation。

## 8. Presentation size 与 semantic state-space size

若 m=k，generator catalogue 只含 singletons：

- dense incidence proxy：`m*k=m^2` bits；
- explicit semantic effect states：`2^m`。

m=20 时，explicit OR monoid 已超过一百万 states，而简单 generator incidence proxy 只有400 bits。

所以“直接 search semantic monoid”并不是 compact algorithmic representation。

## 9. Target-specific design

Geodesic viewpoint 还说明 design 是 semantic-target relative，而不是只由 generator algebra 决定。

Partial target mask 可能比 full precision target 有短得多的 geodesic。不同 future tasks 因而可以在同一个 presented algebra 内产生不同 design cost。

这又是一种 task-relative precision effect。

## 10. Geodesic synthesis 与 generated-algebra closure 不同

生成整个 semantic algebra，与到达一个 required target effect，不是同一个 optimization problem。

Set-Cover precision target 只要求一个 distinguished full-coverage effect。一个 generator subset 可以对这个 target optimal，却不是整个 monoid 的 minimum generating set。

因此从 classical generator-rank theory 借用术语时必须保持这个区别。

## 11. General architectural form

Set-Cover semilattice 暗示一个更一般的结构：

`free syntax / primitive actions`

`--forward semantic homomorphism-->`

`exact operation algebra`。

Forward execution 是计算这个 homomorphism。

Inverse design 是在 declared semantic target / target region 中寻找 minimum-resource preimage。

没有 generic 理由要求 inverse synthesis complexity 与 forward evaluation complexity 相同。

## 12. Stage131 consequence

Stage131 resource analysis 还应加入 **presentation geodesic cost** 这一 upstream resource，它与 runtime law representation 分开。

一个完整 pipeline 可以同时出现：

- primitive catalogue 中 hard target synthesis；
- synthesis 完成后的 easy formulaic execution；
- chosen execution law 内部继续存在 storage / depth Pareto。

这些成本属于不同 phase，不应合成一个 scalar “rule complexity”。

## Owner-local assets

- `src/enterprise_math/generator_geodesic_synthesis.py`；
- `tests/test_generator_geodesic_synthesis.py`；
- 本双语 theorem note。

## Prior-art / status

Cayley graph、word metric、shortest path、succinct state space 与 Set Cover 都是标准既有数学 / CS。P023/A2 保留 precision / future-signature ownership。本文只拥有 minimum semantic design 的 target-geodesic interpretation。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
