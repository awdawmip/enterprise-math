# Stage131 — Workload-Weighted Shortcut Presentation

状态：`RESEARCH BRIDGE / NONCANONICAL`

worst-case inference diameter 只是一个 execution contract。若 Stage131 系统面对的是 nonuniform premise/target query distribution，那么最优 exact shortcut presentation 应该随 workload 改变。

本代保持 semantic closure law 完全不变，只改变 operational objective。

## 1. Weighted query language

对 chain：

`0<1<...<n`，

给每个 comparable pair `i<j` 一个 nonnegative query weight：

`mu(i,j)`。

对 exact stored presentation E，定义 weighted execution cost：

`C_mu(E)=sum_(i<j) mu(i,j) dist_E(i,j)`。

再除以 total query mass，得到 expected inference depth。

这与 worst-case directed diameter 是不同 task contract。

## 2. One-shortcut exact gain theorem

从 adjacent edges 出发，加一条 shortcut：

`a->b`, `b-a>=2`。

query `i->j` 能使用该 shortcut，当且仅当：

`i<=a` 且 `b<=j`。

一旦能使用，原 adjacent path length `j-i` 变成：

`(a-i)+1+(j-b)`。

所以每个 spanning query 都恰好节省：

`b-a-1`

轮，与具体 i/j 无关。

因此 total weighted gain：

`Gain_mu(a,b)`

`=(b-a-1) * sum_(i<=a,j>=b) mu(i,j)`。

所以最优 one-shortcut presentation 就是在最大化：

`shortcut saving length x query rectangle mass`。

这是 exact closed objective，不是 simulation heuristic。

## 3. Query locality 会改变哪个 derived implication 值得存

公式直接给出 Stage131 caching rule：

- long shortcut 每次命中时节省更多 rounds；
- 但只有很多高权重 queries 跨过它时才真正有价值。

因此不能只按 semantic redundancy 给 transitive implications 排序；其 operational value 是 workload-sensitive 的。

## 4. Single-query extreme

若全部 workload mass 都集中在一个 nonadjacent query：

`i->j`，

则最大 saving 的 shortcut 唯一就是：

`i->j`。

它把 declared query 从 `j-i` 轮直接降成1轮。

chain 其他区域仍可能几乎和原来一样慢。

例如 endpoint-only workload `0->n`：存 direct edge `0->n` 后 expected depth=1，但 global worst-case diameter 仍是 `n-1`。

这对 declared workload 是最优的，对 all-pairs continuation contract 却很差。

## 5. Uniform all-pairs workload

给所有 comparable pair unit weight。

对 shortcut a->b，定义 positive segment lengths：

`x=a+1`，

`y=b-a-1`，

`z=n-b+1`。

于是：

`x+y+z=n+1`。

恰有：

`x*z`

个 queries 会跨过 shortcut，每个节省 y 轮，所以 total gain 精确为：

`xyz`。

## 6. Uniform closed optimum

对 fixed positive integer sum，product xyz 最大，当且仅当三部分尽可能均衡，即 pairwise difference 至多1。

所以 uniform one-shortcut optimum 可以直接把 `n+1` 分成三个尽量相等的正整数，再映射回 shortcut coordinates。

不需要 O(n^2) 枚举全部 shortcuts；branch 提供 closed constructor。

## 7. Uniform expected-depth formula

adjacent chain 的 all-pairs total distance：

`n(n+1)(n+2)/6`，

query pair count：

`n(n+1)/2`。

所以 adjacent expected depth：

`(n+2)/3`。

记 `P_3(n+1)` 为三个正整数、总和 `n+1` 时的最大 product，则最优 one-shortcut expected depth：

`(n+2)/3 - P_3(n+1)/(n(n+1)/2)`。

balanced product closed form：

- `3q`: `q^3`；
- `3q+1`: `(q+1)q^2`；
- `3q+2`: `(q+1)^2 q`。

## 8. Uniform optimum 同时达到 worst-case one-shortcut optimum

用同一组 segment variables，one-shortcut worst-case diameter：

`max{x+y-1, y+z-1, x+z-1}`

`= n - min{x,y,z}`。

balanced triple 同时最大化最小 segment，因此也达到 exact one-shortcut worst-case optimum：

`floor((2n+1)/3)`。

所以每个 uniform expected-depth optimum 都是 worst-case optimal。

反方向不一定成立：worst-case 只要求最小 segment 尽量大，而 product optimum 还要求其余 segments 继续尽量平衡。

## 9. n=1024 uniform example

Adjacent presentation：

- 1024 rules；
- uniform expected depth342；
- worst-case diameter1024。

加一条 balanced shortcut：

- 1025 rules；
- expected depth `34899219/131200`，约266.0；
- worst-case diameter683。

所以只存一条 derived implication，就能在 uniform workload 下同时显著改善 average 与 worst-case execution。

## 10. Nonuniform workload 可以主动牺牲 worst-case depth

对同一 long chain 的 endpoint-only query，direct `0->1024` 用同样一条额外 rule 就能把 expected workload depth 降到1。

但 global diameter 仍是1023。

因此两个同样 n+1-rule 的 exact presentations 可以在：

`expected workload depth x worst-case continuation depth`

上占据完全不同位置。

在 task contract 未声明 objective 前，不存在唯一“best shortcut”。

## 11. 多 shortcut 时 gains 不再可加

多条 shortcuts 可以在一条 shortest path 中组合使用，所以总收益不再是各 one-shortcut rectangle score 的简单和。

branch 因此提供 small-n exact budget optimizer：

- adjacent edges 强制保留；
- 在 rule budget 内选 optional shortcut subset；
- literal 计算 shortest paths；
- 最小化 weighted query cost；
- tie-break by worst-case diameter，再考虑 storage。

该枚举只作为 small-chain pressure-test oracle，不主张 scalable optimizer。

## 12. 三轴 operational frontier

nonuniform presentation 至少需要按：

`stored rules`

`x expected workload inference depth`

`x worst-case continuation diameter`

评价。

这些 axes 可以独立变化。

一个 workload curve 可能先把 expected depth 降到理论最小1，之后继续增加 storage，只用于降低 global worst-case continuation depth。

所以即使 workload queries 已经全部一次命中，continuation capability 仍可能是独立资源。

## 13. 与 semantic precision 的关系

整个过程中 closure law 不变。query weights 不改变哪些 implications 为真。

它们只改变哪些 semantic-redundant implications 值得缓存。

所以 workload 属于 **presentation optimization**，不是 semantic closure truth。

这又是一种 future-language relativity：

- same exact world；
- same exact closure；
- different declared usage/query distribution；
- different optimal stored presentation。

## 14. 与 TC-spanner prior art 的关系

worst-case bounded-hop shortcut 与 TC-spanner / shortcut graph objective 对齐。

workload-weighted 版本把 operational criterion 从 maximum reachable-pair distance 改成 weighted / expected shortest-path cost。

generic shortest-path optimization 属于已有 graph/algorithmic territory；项目特有作用是把 query workload 显式提升为 Stage131 presentation resource。

## Owner-local assets

- `src/enterprise_math/stage131_chain_workload_shortcuts.py`；
- `src/enterprise_math/stage131_uniform_workload_shortcut.py`；
- `tests/test_stage131_chain_workload_shortcuts.py`；
- `docs/STAGE131_CHAIN_WORKLOAD_SHORTCUTS.{en,zh}.md`。

## Prior art / status

Shortest-path shortcutting、weighted query optimization 与 graph design 都是标准既有数学/CS。Enterprise Math 的项目价值是 Stage131 rule-caching 解释与 exact one-shortcut workload theorem。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。