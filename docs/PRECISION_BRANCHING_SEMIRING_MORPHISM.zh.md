# Branching Semiring Morphism 与 Structural Trace Fold

状态：`RESEARCH BRIDGE / NONCANONICAL`

Support、exact multiplicity 与 modular multiplicity 可以放进同一个 recursive branching framework；差别只在于每一种 successor behavioural type 携带什么 coefficient semiring。

同一个 framework 还暴露出一个新的负边界：coefficient product 确实是两个 views 的 common refinement，但它可能额外保留跨 view 的 successor correlation，因此不一定是两个 task views 的最粗 semantic join。

## 1. K-valued branching signature

选择一个 commutative semiring K。

Raw relation 的每个不同 source-target pair 都贡献一个 unit。到了 branching depth h，把 target states 按 depth-h K-behavioural type 分组，并对落入同一 type 的 raw targets 在 K 中累加 `1_K`。

因此每个 action 保存的是 child behavioural types 上一个 finitely supported K-valued function。

重要 coefficient worlds 包括：

- `K=N`：每种 behavioural type 的 exact successor multiplicity；
- `K=B`：每种 type 是否出现；
- `K=Z/MZ`：successor multiplicity modulo M；
- product semiring：同时保留多个 coefficient capabilities。

## 2. Semiring morphism 递归诱导 coarse map

设

`phi:K->L`

是 semiring homomorphism。

把一个 K-branching signature 映到 L 时：

1. 递归映射每个 child K-signature；
2. 每个 coefficient 经过 phi；
3. 若多个 richer child types 在 L 中 collapse 成同一个 child type，则在 L 中把 coefficients 相加；
4. 删除最终 coefficient 为 zero 的项。

这个 recursive map 与从 raw relation 直接构造 L-branching signature **精确交换**。

因此：

`beta^K_h(x)=beta^K_h(y)`

必然推出

`beta^L_h(x)=beta^L_h(y)`。

所以 K-branching partition 一定 refine 它在 coefficient morphism 下的 L-image。

## 3. Concrete quotient：N -> Boolean

Positivity：

`n |-> [n>0]`

是 natural count semiring 到 Boolean OR/AND semiring 的 homomorphism。

递归作用后，得到的正是 parent generation 的 support branching signature。

因此此前 count→support 不是一个孤立的 recursion 技巧，而是 generic coefficient-morphism theorem 的实例。

## 4. Concrete quotient：N -> Z/MZ

Reduction：

`n |-> n mod M`

同样是 semiring homomorphism。

它生成 modular branching world：每一种 successor behavioural type 的 multiplicity 只保留 modulo M。

它与 Boolean support 的语义不同。比如 mod2：

- zero successors -> coefficient0；
- two equivalent successors -> coefficient0。

所以一个真正 nonempty 的 successor class 可以被 modular count 完全 annihilate。

## 5. Branching coefficient quotient 与 terminal trace fold 是两种不同操作

给定 K-branching signature 和 literal word w，可以递归得到 terminal K-valued trace：

- empty word 对 current observation 贡献 `1_K`；
- 对第一个 action a，把每个 child 的 suffix trace 乘以该 child-type coefficient；
- 再把所有 child contributions 在 K 中相加。

这精确重构 raw K-semiring path execution。

因此存在一个 horizontal structural map：

`K-branching -> K-terminal-word trace`。

它**不是 coefficient quotient**，而是在 word composition 下把 successor grouping 经乘法 / 加法 fold 掉。

## 6. Coefficient / trace commuting square

对 semiring morphism `phi:K->L`，两个路径精确交换：

`K branching --trace--> K word traces`

`    | phi_*                 | phi`

`    v                       v`

`L branching --trace--> L word traces`。

原因正是 phi 同时保 zero、one、addition、multiplication。

所以当前可以严格区分两种信息损失：

1. **vertical coefficient loss**：K -> L；
2. **horizontal structural loss**：branching grouping -> terminal trace aggregation。

它们是两条独立 precision axis。

## 7. Boolean support 与 parity count 是不可比 views

比较 natural count 的两个 quotient：

`N -> B`

和

`N -> Z/2Z`。

二者互不 factor。

- count 0 与2：Boolean 能区分 absent / present，parity 不能；
- count 1 与2：parity 能区分，Boolean 只看到 nonzero。

所以在 unbounded natural multiplicity 上，任何一边都不能从另一边恢复。

这再次证明 coefficient precision 本身也不是一个 scalar total order。

## 8. Product semiring 给出 common refinement

Coefficient world

`B x Z/2Z`

会同时保存每一种 successor behavioural type 的 presence 与 parity。

投影到任一 coordinate 都是 semiring homomorphism，因此 product branching 同时 refine Boolean-support branching 与 parity branching。

对 raw successor count 0,1,2,3：

- 0 -> `(0,0)`；
- 1 -> `(1,1)`；
- 2 -> `(1,0)`；
- 3 -> `(1,1)`。

所以 product 保住两个 coefficient capabilities，但仍然比 exact N-count 粗，例如1与3仍合并。

## 9. Direct product branching 会额外保留 cross-capability correlation

在更深 branching horizon 上出现一个新的 subtle boundary。

假设 child behavioural types 分别按两套 interface 分类：

- Boolean-support future behaviour；
- parity-count future behaviour。

一个 direct `B x Z/2Z` child type 不只是保存两边各自的信息，它还记录：

> **哪一个 Boolean type 与哪一个 parity type 属于同一个 successor。**

但如果 declared task 只要求两个完整 interfaces 并行可用，那么真正需要的只是：

- full Boolean branching signature；
- full parity branching signature。

并不必然需要保留它们在 raw successors 上的逐项 pairing。

### Sharp witness

构造三种 child product-types：

- A = `(Boolean-empty, parity-zero)`；
- C = `(Boolean-present, parity-zero)`；
- D = `(Boolean-present, parity-one)`。

Source p 的 raw child counts 为：

`A=1, C=0, D=1`。

Source q 为：

`A=2, C=1, D=1`。

它们 separate Boolean views 相同：

- A-type 出现；
- 某个 Boolean-present type 出现。

Separate parity views 也相同：

- parity-zero child 总数在两者中都为 odd；
- parity-one child 总数也都为 odd。

所以 p/q 在两个完整 coefficient interfaces 中分别都等价，在这两个 state partitions 的普通 joint refinement 中也继续等价。

但 direct product branching signature 不同，因为它保留 A/C/D 的具体 pairing 与 multiplicity pattern。

Executable branch 用一个 eight-state depth-two relation fixture 实现这个 strict witness。

因此：

`direct coefficient product branching`

可能严格细于

`同时保留两个 separate branching interfaces 的最粗 state partition`。

## 10. Representation product 不是自动的 semantic join

这再次出现 Enterprise Math 已多次看到的架构警告：

> 把两个 sufficient representations 直接做 raw product，可能偷偷保留两项 declared tasks 都没有要求的 correlation。

Product 是安全 upper bound，但不能自动当作 minimal joined precision。

如果 task 确实需要“同一个 successor 同时具有哪两种 capability”的 correlation，那么 product detail 有意义。

如果 task 只要求两个 interfaces 独立可恢复，那么保留这种 pairing 就属于 overprecision。

因此必须区分：

`semantic requirement join`

与

`representation product`。

## 11. Generic factorization principle

当前 relation precision 最好理解成两个彼此交换、但相互独立的选择：

### Branching coefficient world

选择 K，以及 K-world 之间的 coefficient morphisms。

### Structural observation interface

选择 future 是保留 branching structure，还是把它 fold 成 word traces。

任意一个选择变化，都可能改变 state kernel。

一个 scalar “relation precision” 无法同时概括这两条轴。

## 12. Prior-art boundary

Semiring-weighted automata、weighted bisimulation、coalgebra morphism、product semiring 与 trace semantics 都是标准既有数学 / CS。A4 保留 relation / witness ownership；P023/A2 保留 future-signature / precision ownership。

这里的项目价值是给出明确的 precision diagram：

> **coefficient morphism 与 trace fold 是不同的 coarse maps；它们在 semiring homomorphism 下形成 commuting square；即使 categorical coefficient product，也可能额外保存 task-irrelevant successor correlation。**