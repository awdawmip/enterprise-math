# Relation-Valued Operations 的 Branching Future Signature

状态：`RESEARCH BRIDGE / NONCANONICAL`

只要 future language 允许观察**每个 branch successor 的 behavioural type set**，而不是只把 literal word 的 terminal supports union 起来，那么 relation-support stable quotient 就能重新写成普通的 future-signature kernel。

## 1. 递归 branching signature

设 `O:X->Y` 是 current observation，`{R_a}` 是有限 labelled relation family。

定义：

`σ_0(x)=O(x)`。

递归定义：

`σ_(h+1)(x)`

等于 current observation，再加上对每个 named action a 的 successor signature set：

`{ σ_h(y) : x R_a y }`。

空集合必须精确保留。

它就是 depth-h labelled branching tree 在“相同 successor type 去重”后的表示：保 support，不保 multiplicity。

## 2. 与 relation-support refinement stages 精确相同

令 `E_h` 表示 `σ_h` equality。

h=0 时，`E_0` 就是 current observation partition。

给定 `E_h`，两个 states 的 `σ_(h+1)` 相等，当且仅当：

- current observation 相同；
- 对每个 action，它们到达同一组 `E_h` successor classes。

而 `σ_h` equality 已经自动包含所有更浅 depth 的 equality，所以这恰好就是一轮 support-stability refinement。

因此：

`kernel(σ_h) = 第 h 轮 relation-support refinement partition`。

Executable branch 会直接比较完整 partition sequence 与 fixed-point compiler。

## 3. 有限 branching depth 足以认证 infinite quotient

若总共有 n 个 finite states，initial observation 有 `c_0` 个 blocks，则每次 strict branching refinement 至少增加一个 block。

因此 stable relation-support quotient 最多经过

`n-c_0`

次 strict branching-depth refinement 就会到达。

若某一层 horizon 没有产生新的 partition split，那么 relation support 已经 stable，任何更深 branching signature 都不会再细化 state partition。

所以 infinite support-bisimulation quotient 拥有一个 exact finite-depth certificate。

## 4. Literal terminal support 是 branching signature 的 deterministic projection

给定 `σ_h(x)` 与 word

`w=a_1...a_k`, `k<=h`，

可以纯递归计算 terminal observed support：

- empty word -> `{O(x)}`；
- 对第一个 action a，取 a-successor signatures，对每个 child 递归执行剩余 word，再把结果 union。

得到的结果精确等于：

`{ O(y) : x R_w y }`。

因此所有 word-indexed terminal observed-support signatures 都 factor through branching signature：

`branching signature -> terminal support traces`。

所以同一 horizon 下，branching partition 一定 refine terminal trace partition。

## 5. 为什么只有 genuine branching 才会让 projection 丢信息

若每个 action/source 最多只有一个 successor，则 action support 只有：

- empty；或
- 一个 child signature。

此时 terminal word language 可以递归恢复“这个 child 是否存在”以及它的全部 future trace type。

因此对 deterministic partial relation family：

`horizon h 的 branching partition`

精确等于

`horizon h 的 legality / terminal-support word partition`。

这完整恢复 total deterministic 与 FQ-006 情形。

branching / trace gap 只有在一个 action 同时拥有多个 sibling successor types 时才会出现。

## 6. Choice-timing witness

对经典结构：

`p = a.(b+c)`

与

`q = a.b + a.c`，

terminal traces 相同，但 branching signatures 不同。

Depth1 时 p/q 仍然等价，因为它们的 a-successors 尚处于同一个 observation class。

Depth1 同时已经拆开 middle states：

- r 同时支持 b、c；
- s 只支持 b；
- t 只支持 c。

到了 depth2：

`σ_2(p)` 的 a-support 只有一个 child type `[r]`；

而

`σ_2(q)` 的 a-support 有两个 child types `[s],[t]`。

所以 branching depth2 能看见 nondeterministic choice 的 timing，而任何 literal terminal word 都看不见。

## 7. Terminal union 丢掉的到底是什么

Word trace 分别询问每个选定 action sequence 最后能发生什么。

它不保留下面这个 joint question：

> 哪一组 future behaviours 属于同一个 successor branch？

Branching signature 先按 successor behavioural type 分组，再做后续运算，因此保留这种 correlation。

这就是 branching-time semantics 可以区分 linear-time trace-equivalent processes 的原因。

## 8. 仍然只是 support precision

Set constructor 会把相同 successor signature 的重复项去掉。

因此 `σ_h` 仍然忘记：

- 同一 behavioural type 有多少个 raw successors；
- 到同一 state 的多条 parallel witness；
- path identity / provenance；
- branch-local history / cost。

若 future language 读取 count 或 witness，就必须把 successor aggregator 从 `set` 升级成更丰富的对象。

由此自然得到下一条 precision axis：

`terminal union`

`< successor behavioural types 的 set`

`< successor behavioural types 的 multiset/count`

`< explicit witness/provenance state`，

其中每个 strictness 都取决于 declared future semantics。

## 9. Semantic-preorder interpretation

同一个 raw A4 relation 因此可以对应多个合法的 precision object：

- future 只问 terminal reachable support -> trace quotient；
- relation 必须作为 behavioural-class 上的 set-valued operation 直接 descend -> support-bisimulation quotient；
- multiplicity / provenance 会被 future 重新读取 -> 更丰富 witness quotient。

若不先声明 interface，就不存在一个 scalar “relation precision” 可以自动排序全部情形。

## 10. Prior-art boundary

Tree unfolding、bisimulation approximants、modal transition semantics 与 trace projection 都是标准既有数学 / CS。A4 保留 correspondence / witness ownership；P023/A2 保留 future-signature / kernel ownership。

这里的项目价值是明确 factorization：

> **direct multivalued-operation precision 是 recursive branching future signature 的 kernel，而 terminal support traces 一般只是它的严格 coarse projection。**