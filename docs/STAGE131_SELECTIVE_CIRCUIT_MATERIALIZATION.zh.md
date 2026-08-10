# Stage131 — Selective Rooted-Circuit Materialization

状态：`RESEARCH BRIDGE / NONCANONICAL`

完整 rooted-circuit table 是指数级巨大的。修正后的 width/depth value spectrum 让下一问题变成 operational：

> 在有限 storage / fan-in / workload budget 下，究竟应该 materialize 哪些 one-round minimal-premise rules？

对于一个重要且可精确求解的 task contract——workload 只查询 root 的 inclusion-minimal premise sets——选择问题可以在聚合的 `(premise width, base depth)` 类型空间中 exact 求解，而无需枚举指数多个 premise sets。

## 1. Minimal root premises 构成 antichain

同一个 root 的两个不同 inclusion-minimal premise sets P,Q 不可能满足 `P proper_subset Q` 或 `Q proper_subset P`。

否则较大的那个就不是 inclusion-minimal。

因此当 workload queries 本身就是 rooted-circuit minimal premises 时，materialize `P=>root` 不会让另一个不同 minimal query Q 因包含 P 而提前触发。

owner 对 small AND tree 的 explicit circuits 做 antichain 检查。

## 2. Additive circuit benefit

记：

- `d(P)`：local basis 从 P derive root 的 base depth；
- `f(P)`：exact query P 的 workload frequency/weight。

不存 macro 时 query P 需要 d(P) 轮；materialize exact rule `P=>root` 后变成1轮。

所以 gross weighted saving：

`v(P)=f(P)*(d(P)-1)`。

由于 minimal queries 构成 antichain，在该 task contract 下 selected macro set 的总收益就是各 candidate benefit 之和。

## 3. Type aggregation 避免指数枚举

balanced AND tree 中，修正后的 value spectrum 已按：

`(width,base_depth)`

给出每类 circuits 的 multiplicity。

若 workload 在同一 type 内对每条 circuit 的 frequency 相同，那么同 type candidates 拥有相同 storage/value data。

compiler 因而只在小型 type table 上优化，而不是枚举完整 premise antichain。

## 4. Unit-rule storage budget

若每条 materialized circuit 都只按1条 rule 计 storage，exact optimizer 是：

1. 计算每个 type 的 per-circuit benefit；
2. 按 benefit 降序；
3. 从最高 benefit 类型开始选，直到 rule budget 用完。

benefit tie 时可优先选更窄 premise，不改变 weighted objective。

uniform frequency 下，benefit 只等于 `d-1`，所以 deepest circuits 优先。

## 5. Premise-literal storage budget

若存 `P=>root` 的成本按 `|P|` premise literals 计，则变成 bounded 0/1 knapsack：

- item cost = premise width；
- item benefit = `f(P)*(d(P)-1)`；
- multiplicity = 该 `(width,depth)` type 的 circuit 数。

executable planner 对 type multiplicity 做 binary decomposition，因此数十万 multiplicity 不会变成数十万 DP items。

## 6. Fan-in cap 给出 exact speedup ceiling

value-spectrum theorem 已知 exact depth-d circuits 的 minimum width 是 `d+1`。

因此最大 allowed fan-in W 时：

`d_max(W)=min(h,W-1)`

（W>=2）。

可 materialize 的最大 one-round saving 是：

`max(0,d_max(W)-1)`。

所以 rule language 或 hardware fan-in limit 会直接转化为 proof-depth shortcut ceiling。

## 7. Narrow deepest circuits 仍然有指数 multiplicity

exact depth d 的 minimum-width circuits 宽度为 `d+1`。

这种最窄 circuit 恰有：

`2^(d-1)`

条。

原因：要保持 minimum width，一个 child side 必须采用 minimum-width depth-(d-1) configuration，另一侧直接使用 child atom；左右有2种选择，因此 `C_d=2C_(d-1)`，`C_1=1`。

所以即使 fan-in cap 很紧，也通常存在多个 high-speedup candidates。

例如 depth5 有16条 width6 circuits；每一条若命中 exact premise query，都能省4轮。

## 8. Uniform workload 下每 premise literal 的最高效率

exact depth-d circuit 满足：

`benefit <= d-1`，

`width >= d+1`。

所以 per-premise-literal efficiency 至多：

`(d-1)/(d+1)`。

minimum-width depth-d circuits 达到该 bound。

而：

`(d-1)/(d+1)`

随 d 严格增加。

因此 uniform per-circuit workload 下，**最深 depth class 中最窄的 circuits 拥有全局最高的直接 round-saving / premise-literal 效率**。

这只是 ranking theorem，不等于完整 knapsack theorem：integer budget leftovers 与 multiplicity 仍可能让 mixed selection 最优。

## 9. Height-5 unit-rule example

height5 root 的 depth counts：

`1,3,21,651,457653`。

uniform frequency、budget=10 circuit rules 时，compiler 选择10条 depth5 circuits；tie 时先选 width6 candidates。

资源：

- 10 stored circuit rules；
- 60 premise literals；
- max fan-in6；
- gross weighted round saving40。

只 materialize 完整 table 的极小比例，却全部来自最高 value depth class。

## 10. Height-5 premise-literal example

premise-literal budget=60、uniform frequency 时，exact bounded-knapsack planner 也选择10条 width6/depth5 circuits：

- total premise storage60；
- gross saving40。

type-level DP 不需要枚举458329条 root circuits。

## 11. Workload 可以反转 depth priority

depth 只是潜在 saving，actual benefit 是 frequency × saving。

一个高频 depth2 circuit 完全可能支配一个极低频 depth4 circuit。

compiler 支持 type-level workload frequencies，因此按 weighted benefit 选择，而不是机械按结构 depth 排序。

## 12. Additive theorem 的 scope

antichain 使收益可加，只对 declared workload——**exact minimal-premise root queries**——成立。

若 query seed set 是任意 superset，一个 selected circuit 可以帮助许多 queries；若 materialized macros 还能参与更深 reusable derivation，不同 macros 之间还会 interaction。此时 global value function 不再是 candidate benefit 的简单和。

更强 continuation-state optimization 属于下一层 proof-DAG / Horn macro compilation。

## 13. Stage131 interpretation

完整 rooted-circuit table 是“把全部 minimal premise alternatives 都缓存成 one-round rule”的 maximal cache。

selective compiler 把它变成 budgeted execution layer：

`semantic basis`

`-> exponential circuit opportunity spectrum`

`-> workload/storage/fan-in filter`

`-> selected execution macros`。

这就是 rooted-circuit minimality boundary 的正面用途：不能把完整 table 当 minimal law，也不能盲目删除其中全部 shortcuts。

## Owner-local assets

- `stage131_selective_circuit_materialization.py`；
- unit-rule / fan-in / knapsack / antichain tests；
- `STAGE131_SELECTIVE_CIRCUIT_MATERIALIZATION.{en,zh}.md`。

## Prior art / status

Knapsack、antichain 与 workload-weighted caching 都是标准既有数学/CS。Enterprise Math 的项目价值是基于 rooted-circuit width/depth opportunity spectrum 的 Stage131 selective materialization compiler。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。