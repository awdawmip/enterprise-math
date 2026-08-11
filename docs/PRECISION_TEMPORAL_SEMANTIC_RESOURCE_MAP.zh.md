# Temporal Semantic Precision 与 Representation Resources

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Stage131 这条线已经给出一个 sharp warning：不能把“future horizon”或“rule count”直接当作 precision scalar。即使只看一个很小的 commuting-idempotent OR action family，只要改变 **future language 到底观察哪些 temporal information**，在任何 implementation tradeoff 之前 exact operation algebra 就已经改变。

本文不新增 Foundation Question，只把 prefix generations 暴露出的 semantic / resource routing 汇总回 Foundation。

## 1. 先声明 temporal observation semantics，再优化 representation

一个 literal action word 至少可以按以下 exact semantic levels 观察。

### Terminal effect

只观察 final transformation / state effect。

k 个 OR generators 下，algebra 是 finite Boolean semilattice，共 `2^k` 个 masks。

### Discovery-event order

观察新的 state distinctions / generator effects 第一次出现的顺序，但不观察 discoveries 之间 state 保持不变多久。

Exact algebra finite，可用 first-occurrence normal form 表示。

### Full prefix timing

观察每一个 cumulative prefix state，包括每个 level 持续多少 steps。

Unbounded horizon 下 exact algebra infinite，但可用最多 k 个 structural phases + integer durations 的 run-length normal form 表示。

### Literal provenance

即使 represented state 没有变化，也观察到底执行了哪个 named action。

这可以把 semantics 一直恢复到 full literal word language。

这些是不同 future theories，不是同一个 theory 的不同 implementations。

## 2. Exact quotient maps 构成 temporal semantic ladder

OR pressure family 中：

`literal provenance`

`-> full prefix timing`

`-> discovery order`

`-> terminal set`。

每个 arrow 都是 deterministic semantic quotient。

向下分别删除：

- stutter action identity；
- stutter duration；
- first-discovery order。

Declared semantic quotient 一旦删除某 distinction，后续 representation optimization 不可能把它恢复回来。

## 3. 不同 temporal layers 的 semantic cardinality growth type 不同

Exact word length H、fixed k：

- literal words：`k^H`，对 H exponential；
- full timing semantics：`Theta(H^(k-1))`，polynomial；
- discovery order：H>=k 后 finite saturation；
- terminal effect：H>=k 后 finite saturation。

所以“多一个 future step”可以同时意味着：新增 exponentially many syntax strings、polynomially many timing semantics，或完全不新增 terminal semantic effects。

## 4. Infinite semantic algebra 仍可 finite-parameter exact present

Full timing semantics infinite，因为 durations unbounded。

但 exact run-length form 最多只有 k 个 phases：

`((g_1,r_1),...,(g_s,r_s)), s<=k`。

Composition 最多扫描 k 个 phases，并组合 integer durations。

因此：

`infinite number of semantic operations`

不推出

`unbounded structural parameter dimension`。

Finite algebra cardinality 与 compact law presentation 必须分开。

## 5. Materialized history 与 compositional operation state 是不同 interface

Fixed k 下，compact run-length form 可以用 O(k log H) 量级简单 fields 表示 H-step prefix operation。

但若 consumer 真正要求观察全部 H 个 prefix states，这 H 个 outputs 仍必须 emit / materialize。

所以：

`compact exact future state`

不推出

`zero-cost observable history`。

这又是 answer / state / interface distinction 的一个实例。

## 6. Cache growth 取决于 semantic key

若 cache horizon H 内全部 operations：

### Literal cache

`1+sum_(h=1)^H k^h`，exponential。

### Full timing cache

`1+sum_s P(k,s) C(H,s)`，fixed k 下是 degree-k polynomial。

### Discovery cache

Finite saturation。

### Terminal cache

Finite saturation 到 `2^k`。

所以 “cache all future rules through H” 在 semantic cache entry 未声明前没有唯一 storage law。

## 7. Class count 与 workload information 是不同 resources

Worst-case semantic state count 不依赖 distribution。

Shannon entropy 必须声明 workload。

Uniform literal-word workload 下 exact quotient fibers 给出：

`H_literal`

`=H_terminal`

`+first-discovery-order information`

`+discovery-duration information`

`+stutter-action provenance information`。

这些是 semantic quotient ladder 诱导出的 exact information increments。

## 8. Cardinality 可以增长，而 entropy 反而收敛

Fixed k、H→∞、uniform random actions：

- terminal entropy ->0；
- discovery entropy ->`log2(k!)`；
- full timing entropy -> finite coupon-collector constant；
- literal entropy=`H log2 k` 线性增长。

与此同时 full timing **class count** 仍然 polynomial 增长。

所以 worst-case indexing/storage capacity 与 average workload information 可以朝完全不同的方向变化。

没有声明 optimization objective 时，两者不能互相替代。

## 9. Work、batch depth、streaming latency 与 reuse 也不同

Prefix semantics 固定后：

- sequential scan 使用 minimum OR work 与 O(1) streaming state，但 batch dependency depth 对 H 线性；
- parallel prefix scan 可以用额外 work/storage 把 batch depth 压到 logarithmic；
- terminal-only balanced reduction 资源很漂亮，但对 full-prefix observation semantic invalid。

同样，materialize reusable terminal normal form 在 reuse 下可节省 duplicated work，却可能在 one-shot execution 多出一层 avoidable pipeline depth。

所以“execution depth”本身也必须声明 execution model。

## 10. Expanded Stage131 resource vector

一个 precision-preserving compiler/executor 至少可能需要报告：

`semantic observation layer`

`x semantic class cardinality`

`x exact normal-form parameter dimension`

`x parameter bit width`

`x bounded-horizon cache entries`

`x workload Shannon information`

`x output materialization volume`

`x preprocessing/design cost`

`x execution work`

`x batch critical-path depth`

`x online latency`

`x live working storage`

`x reuse/amortization profile`。

这些不是一个 scalar precision coordinate。

## 11. Foundation routing order

对 temporal future language，安全顺序是：

1. 声明哪些 temporal distinctions semantic observable；
2. 求 exact semantic quotient / operation algebra；
3. 找 exact normal form 或 compiler state；
4. 声明 workload 与 execution model；
5. 只在同一 semantic-equivalence fiber 内比较 storage / work / depth / coding / cache implementations。

跳过 step1，会让 resource-optimal implementation semantic 错误。

跳过 step3，会把 finite/infinite cardinality statement 错当成 implementation lower bound，即使其实存在 compact formulaic presentation。

## 12. 与现有 Foundation layers 的关系

本文 refine 而不替代 earlier distinctions：

- state detail vs semantic capability；
- semantic law vs generator presentation；
- semantics vs execution representation；
- sufficient answer vs executable continuation state。

Temporal observation 再增加一条 routing axis：**future path 的哪些部分本身属于必须保留的 law semantics**。

## 13. Prior-art boundary

Trace semantics、left regular band、run-length encoding、parallel prefix scan、coupon collector asymptotic 与 Shannon entropy 都是标准既有 mathematics / CS。

Enterprise Math 在这里得到的是 consolidated precision-first routing：必须先固定 semantic temporal observation，再比较 representation resources。

无 canonical-main、无 `EXECUTABLE_CHECKED` claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
