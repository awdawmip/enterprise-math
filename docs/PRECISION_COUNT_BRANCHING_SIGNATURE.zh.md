# Count-Sensitive Branching Signature

状态：`RESEARCH BRIDGE / NONCANONICAL`

Support branching 只保留 successor behavioural types 的**集合**。如果 future theory 会读取 branch multiplicity，就需要更丰富的 aggregator：每一种 behavioural type 到底有多少个 raw successors。

这形成了 Boolean support 与 full witness provenance 之间的一层自然数 branching precision。

## 1. 递归 count branching signature

对 observation O 与 labelled finite relations R_a，定义：

`μ_0(x)=O(x)`。

下一层对每个 action a，统计 raw target states 中每一种 previous-depth signature 出现多少次：

`μ_(h+1)(x)`

`=(O(x), ( Counter( μ_h(y) : x R_a y ) )_a )`。

这个 counter 就是 successor behavioural types 上的有限 multiset / natural-valued measure。

因此 `μ_h` equality 给出 h-round **count-stable / equitable** relation partition：同一 class 内的 states 对每个 action、每个 current behavioural class 都拥有相同 successor count。

在有限 state set 上，partition 同样会在有限 block splits 后到达 fixed point。

## 2. Natural count -> Boolean support 是精确的 branching coefficient quotient

在每个 successor behavioural type 上递归应用：

`N -> B`, `n |-> [n>0]`。

每个 positive multiplicity 被压成 presence / absence；如果多个 count-types 擦除后变成同一个 support-type，再进行 set collapse。

得到的结果精确等于 parent 的 support branching signature `σ_h`。

所以：

`count branching precision`

一定 refine

`support branching precision`。

这就是已有 relation path-count route 中 path-count -> path-existence quotient 在 branching-operation interface 上的版本。

## 3. Sharp multiplicity gap

取四个 states `x,y,u,v`，observation constant，只有一个 relation a：

`x -> {u,v}`，

`y -> {u}`，

且 u/v 此后 behavioural type 完全相同。

Support branching 从 x/y 都只看到：

`{one successor type}`，

所以会合并 x/y。

Count branching 则看到：

`2 * that type`

versus

`1 * that type`，

在 depth1 就把 x/y 拆开。

因此，即使 target behavioural support 完全相同，successor multiplicity 仍然是一个独立 semantic precision coordinate。

## 4. Terminal natural path count 是第二个 projection

给定 count branching signature 与一个 literal word，terminal observed path counts 可以纯递归计算：

- empty word 对 current observation 贡献 count1；
- action a 下，对每一种 successor type 递归执行 suffix，并乘上该 type 的 successor multiplicity；
- 把所有 child count vectors 相加。

结果精确等于 ordinary natural path counts 按 terminal observation 分组后的值。

因此：

`count branching signature -> terminal path-count trace`

是一个 deterministic projection。

但这个 projection 同样可能不 injective。

## 5. Sharp count-correlation gap

取八个 states：

`p,q,r1,r2,s,t,z1,z2`，

observation constant。

Relation a：

`p -> {r1,r2}`，

`q -> {s,t}`。

两个 r-states 的 future count type 都是：

`b-count=1, c-count=1`。

State s 的 type 是：

`b-count=2, c-count=0`；

state t 的 type 是：

`b-count=0, c-count=2`。

但是 p/q 对每个 literal word 的 terminal natural path counts 完全相同：

- a：2 paths；
- `ab`：2 paths；
- `ac`：2 paths；
- acyclic fixture 中其余更长 / 不匹配 words 都有同样的 zero counts。

然而在 branching depth2：

p 的 successor-type multiset 是

`2 * (1,1)`；

q 的 successor-type multiset 是

`1 * (2,0) + 1 * (0,2)`。

因此 count branching 会拆开 p/q，而所有 terminal path-count traces 仍然合并它们。

这里丢掉的是：**在求和以前，future count behaviours 分别属于哪些 successor branches。**

## 6. 两种独立 aggregation quotient

当前 relation 路线已经明确出现两种不同的 coarse operation。

### Coefficient erasure

`N -> B`

擦掉同一个 behavioural type 的 multiplicity。

### Trace summation

`successor count-types 的 multiset -> summed terminal word counts`

擦掉每个 future count vector 属于哪个 successor type 的 grouping。

两者都可能丢失 task-relevant information。

所以 exact path counts 虽然在 numeric coefficient 上比 support 丰富，但如果 future language 要在 behavioural classes 上直接执行 count-valued relation，它仍可能在 structure 上太粗。

## 7. Deterministic / partial collapse

若每个 action/source 只有 0 或 1 个 successor，那么所有 successor multiplicity 天然只有 0/1。

此时 natural count 与 Boolean support branching signatures 在每个 depth 完全相同。

因此新 count 轴只由 genuine branching multiplicity 产生。

## 8. 与 #380 path-count precision 的关系

现有 path-count route 询问：每个 literal word 最终产生什么 terminal count vector。

本 generation 询问更强的 operation-interface question：

> 在 terminal summation 以前，这个 quotient state 对每一种**future behavioural count type**分别拥有多少 successors？

前者属于 linear-time count trace semantics；后者属于 branching-time count semantics / weighted-bisimulation-style precision。

它们之间的 strict gap，正是 Boolean support 下 trace-vs-bisimulation gap 的 count analogue。

## 9. Raw relation boundary

Raw relation 是 source-target ordered pairs 的 set，所以同一个 ordered pair 本身没有 duplicate parallel edge。

这里统计的 multiplicity 是：有多少个**不同 raw target states**落入同一个 behavioural class。

如果 literal parallel witnesses / edges 自身带 multiplicity，那么必须先让 A4 暴露更丰富的 multigraph / witness object，再应用本 compiler。

## 10. Precision hierarchy

对 declared relation futures，目前至少可以区分：

`terminal Boolean support trace`

`<= support branching / successor types 的 set`

`<= count branching / successor types 的 multiset`

并且独立地：

`terminal natural path-count trace <= count branching`，

两个比较都有 strict witnesses。

Full witness identity / provenance 仍然可能需要比 count branching 更丰富的 state。

## 11. Prior-art boundary

Multiset、equitable partition、weighted bisimulation、path counting 与 semiring quotient 都是标准既有数学 / CS。A4 保留 raw witness / correspondence ownership；P023/A2 保留 declared future-signature precision ownership。

这里的项目价值是明确 factorization：

> **multiplicity precision 与 branching-correlation precision 是两条独立轴；terminal path count 可以保住前者，却仍然丢掉后者。**