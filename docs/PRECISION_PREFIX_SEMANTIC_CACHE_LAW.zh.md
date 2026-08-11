# Prefix Semantic Quotient 下的 Horizon Cache Growth

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

把 horizon H 内所有 literal future words 全部 cache，storage 可能指数增长。如果在 cache materialization **之前**先做 exact semantic quotient，cache growth law 可以发生质变。

对 terminal / discovery / timing prefix ladder，distinct-operation cache size 都能写成 closed form。

## 1. Literal syntax cache

包括 empty word，长度<=H 的 literal words 数：

`C_lit(k,H)=1+sum_(h=1)^H k^h`。

k>1 时：

`C_lit=(k^(H+1)-1)/(k-1)`。

对 H 指数增长。

## 2. Terminal semantic cache

Terminal effect 是 size<=H 的 generator subset。

所以：

`C_terminal(k,H)=1+sum_(s=1)^min(k,H) C(k,s)`。

H>=k 后：

`C_terminal=2^k`。

Future horizon 再增长，cache 完全停止增长。

## 3. Discovery-order semantic cache

Discovery effect 是长度<=H 的 distinct-generator ordered list。

因此：

`C_discovery(k,H)=1+sum_(s=1)^min(k,H) P(k,s)`。

H>=k 后 saturation 到 finite discovery monoid size：

`1+sum_(s=1)^k P(k,s)`。

同样不再产生 horizon growth。

## 4. Full-timing semantic cache

Exact word length h 下，s-phase timing forms 数量：

`P(k,s) C(h-1,s-1)`。

对所有 `h<=H` 求和：

`1 + sum_s P(k,s) sum_(h=s)^H C(h-1,s-1)`。

利用 hockey-stick identity：

`sum_(h=s)^H C(h-1,s-1)=C(H,s)`。

因此 full-timing cache exact size：

`C_timing(k,H)=1+sum_(s=1)^min(k,H) P(k,s) C(H,s)`。

这就是 total length<=H 的全部 RLE prefix-semantic operations 数量。

## 5. Fixed-k timing cache 从 exponential 降成 polynomial

H>=k 时：

`C_timing(k,H)=1+sum_(s=1)^k P(k,s) C(H,s)`。

它是 H 的 degree-k polynomial。

最高次项：

`k! C(H,k)`，

leading coefficient=1。

所以 fixed k 下：

`C_timing(k,H)=Theta(H^k)`。

Branch 机械验证 H>=k 后 k 阶 forward difference 恒等于 `k!`。

## 6. 四种 cache-growth regime

Fixed k：

### Literal provenance

`Theta(k^H)`。

### Full prefix timing

`Theta(H^k)`。

### Discovery order

Finite saturation：`1+sum P(k,s)`。

### Terminal set

Finite saturation：`2^k`。

所以仅仅改变 declared semantic observation layer，就可以让 horizon-cache growth 从 exponential 变 polynomial，再变 constant。

先是 semantic change，之后才是 representation-resource change。

## 7. Sharp k=5,H=5

Through horizon5：

- literal words：3906；
- full timing semantic operations：1546；
- discovery operations：326；
- terminal operations：32。

即使 horizon 很短，各 quotient layers 也已经显著改变 table size。

## 8. Sharp k=5,H=20

Through horizon20：

- literal words：`119,209,289,550,781`；
- full timing semantic operations：`2,514,181`；
- discovery operations：326；
- terminal operations：32。

Literal / timing entry-count ratio 已超过一千万。

Timing cache 仍远大于 discovery cache，因为 exact durations 仍被 future language 观察。

## 9. k=1 boundary

只有一个 generator 时：

- literal words through H：H+1（含 identity）；
- full timing operations：H+1；
- discovery operations：H>=1 后为2；
- terminal operations：H>=1 后为2。

Timing 层没有 literal redundancy 可删，因为 word length 本身就是完整 prefix semantic state。

Polynomial formula 正确退化为 degree1。

## 10. Cache after quotient，而不是 materialize literal cache 后再 quotient

以上 formulas 计算的是 **distinct semantic cache entries**。

理论上可以：

1. 先 materialize 每个 literal word，再 deduplicate；
2. 直接 normalize 到 semantic quotient，只存每个 semantic form 一次。

最终 semantic key set 相同，但第一条路径可能 transiently 支付完整 exponential literal storage/work。

所以当 semantic quotient 已经属于 declared future semantics 时，normalizer 应优先放在 cache materialization 之前。

## 11. Exact-length class count 与 horizon total cache count degree 不同

单个 exact length H 上，full timing semantic classes 增长：

`Theta(H^(k-1))`。

把 **所有 lengths <=H** 都 cache，会再累计一个 degree：

`Theta(H^k)`。

这是 sizing bounded-horizon future table 时必须区分的两种量。

## 12. Timing cache 内部还存在 fiber heterogeneity

Prefix-fiber generation 已证明 timing classes 的 literal fibers 不均匀。

所以 semantic entry count 相同，并不意味着 nonuniform workload 下 expected dedup benefit 相同。

当前 closed form 是 exact worst-case **distinct-entry count**，不是 average cache-hit theorem。

## 13. Stage131 consequence

“cache future through H”的成本，在 semantic cache key 未声明之前根本没有唯一含义。

合法 exact keys 可以是：

- literal word；
- full timing RLE；
- discovery order；
- terminal effect。

它们的 horizon growth laws 完全不同。

所以 Stage131 在 storage / depth comparison 之前必须同时声明：

`一个 cache entry 用什么 semantic quotient 定义？`

以及

`cache 的 horizon / reuse interface 是什么？`

## Owner-local assets

- `src/enterprise_math/prefix_semantic_cache_law.py`；
- `tests/test_prefix_semantic_cache_law.py`；
- 本双语 theorem note。

## Prior-art / status

Hockey-stick identity、falling factorial 与 memoized semantic-state table 都是标准既有 combinatorics / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 prefix-semantic horizon-cache growth specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
