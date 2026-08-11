# Semantic Word Normalization 的第二层 Storage/Depth Pareto

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Literal block-cache theorem 把 precomputed consequences 按 action words 建表。当很多 words 实际诱导同一个 exact operation 时，semantic normal form 可以进一步压缩这些 consequences。

但这种压缩不是免费的：runtime 仍然必须把输入 word 计算成正确的 semantic effect。对 finite deterministic state spaces，这会在 Stage131 内部再生成一条 storage / depth Pareto。

## 1. Finite transformation monoid

设 finite state set X 有 n 个 states，k 个 total deterministic generators 作用于 X。

每个 action word 都诱导一个 transformation：

`F_w:X->X`。

Identity 与所有 generated transformations 组成 finite transformation monoid M。

记：

`m=|M|`。

因为 X 上 total endomap 总数只有 `n^n`：

`m<=n^n`。

所以 semantic word effects 最终会 saturation，即使 literal words 随 horizon 继续指数增长。

## 2. Exact monoid compiler

Owner 通过右乘 generators 做 closure，构造 generated transformation monoid，并生成：

- canonical effect IDs；
- generator effect IDs；
- 完整 Cayley multiplication table；
- 每个 effect 对 fine states 的 exact action。

Sequential 与 balanced-parallel word normalizers 都会对照 literal word execution 做 exact cross-check。

## 3. Resource point A — direct generator execution

只存 k 个 generator state maps。

Storage scale：

`k*n` state-table cells。

长度 H 的 word 需要 H 次 state updates。

这是当前比较中最小的 direct execution representation。

## 4. Resource point B — full literal word index

把 horizon H 内每个 literal word 都作为 key，指向其 semantic effect ID。

Auxiliary index entries：

`S(k,H)=sum_(i=1)^H k^i`。

m 个 semantic effects 则只需在共享的 `m*n` action table 中各存一次。

已知 whole word 时，runtime 做一次 word lookup，再 apply effect；在当前 round abstraction 下等价于1次最终 application round。

当 k>1 时，index 对 H 指数增长。

## 5. Resource point C — sequential semantic effect automaton

不再给每个 word 建 key，只存 right-generator transition table：

`current effect ID x next generator -> next effect ID`。

Auxiliary storage：

`m*k` entries。

对非空长度 H 的 word，可直接以第一个 generator effect ID 初始化，再做 H-1 次 right-generator transitions，最后 apply 一次 state effect。

所以当前 abstraction 下 total depth=H。

这一路线虽然不降低相对 direct generator execution 的 asymptotic depth，但它推进的是 compact semantic effect state，而不是不断更新 fine physical state。

## 6. Resource point D — full Cayley parallel normalizer

存任意 effect×effect product：

`m*m` entries。

Associativity 允许在不要求 commutativity 的前提下，把 H 个 generator effect IDs 用 balanced binary tree reduce。

Normalization depth：

`ceil(log2 H)`。

再加一次 state application：

`total depth = ceil(log2 H)+1`。

因此更大的 algebra table 可以换 logarithmic compile depth。

## 7. Exact Cayley/literal break-even horizon

Literal-index 与 Cayley route 都可共享同一份 `m*n` semantic effect action table。

所以它们 auxiliary storage 的比较精确就是：

`m^2` vs `S(k,H)`。

第一次 Cayley auxiliary storage 小于 full literal word index 的 horizon，是最小满足：

`S(k,H)>m^2`

的 H。

这是当前 cell model 中的 exact phase boundary。

## 8. Sharp two-state identity/flip example

取 two states，generators 为 identity 与 flip。

此时：

`m=2`, `k=2`。

H=20 时：

### Generator maps

- generator state cells：4；
- execution depth：20。

### Literal word index

- word entries：`2^21-2 = 2,097,150`；
- shared semantic effect cells：4；
- execution depth：1。

### Sequential semantic automaton

- auxiliary entries：`m*k=4`；
- total depth：20。

### Cayley parallel normalizer

- auxiliary entries：`m^2=4`；
- shared effect cells：4；
- 当前 cell model 下 total storage：8；
- normalization depth：5；
- total depth：6。

这里 Cayley normalization 的 storage 几乎与 generators 同量级，却把 depth 从20降到6，同时避开 exponential literal table。

## 9. Short horizon 会反转比较

同一个 m=2,k=2 系统在 H=1 时：

- literal index 只有2 entries；
- Cayley table 固定要4 entries。

因此 literal representation 更小。

Exact break-even 是 H=2，因为：

`S(2,1)=2<=4`，

而

`S(2,2)=6>4`。

所以 semantic normalization 不是 universally superior compression。

## 10. Large monoid 会重新打开 storage/depth tradeoff

取 parent free-prefix fixture，k=2、cache depth3。它生成 transformation monoid：

`m=16`。

于是：

- right-generator automaton：`m*k=32` entries；
- full Cayley table：`m^2=256` entries。

在 H=8：

- sequential semantic route total depth8；
- Cayley route total depth4；
- literal word index 有510 entries。

因此三个 points 都 materially distinct。

该 fixture 的 Cayley/literal auxiliary-storage break-even 精确出现在 H=8。

## 11. Literal table、semantic store 与 compiler 是三个独立资源

“只有 m 个 semantic effects”本身并不能定义一个 operationally useful representation。

完整实现还必须说明：输入 word 怎样映射到这 m 个 effects 中的正确一个。

所以资源对象至少是：

`semantic effect store + normalization mechanism + state action`。

不同 normalizers 可以在完全相同的 exact effect quotient 上实现不同 storage / execution depth。

## 12. Algebraic normal form 还可以继续压 Cayley table

Generic finite monoid table 要 `m^2` storage。但具体 operation language 可能存在更紧凑的 exact multiplication formula。

P024 的 guarded word profile `(T,H)` 就是例子：normal form 有 closed max-plus-style product，不必为所有 reachable profiles 显式存 Cayley table。

所以 Cayley table 只是 universal finite-state construction，不是每个 structured action language 的最终 optimal representation。

下一条改进轴是：

**formulaic normal-form algebra vs tabulated monoid algebra**。

## 13. Stage131 hierarchy

当前 future-law representation hierarchy 已形成：

1. sparse generators —— stored syntax 最少，runtime composition 最大；
2. semantic right-generator automaton —— compact effect state，sequential normalization；
3. semantic Cayley algebra —— algebra storage 更大，logarithmic parallel normalization；
4. literal block/full-word tables —— precomputation 最大，lookup execution 最浅。

它们都可以表示同一个 exact future law。

这就是原 Stage131 “relation-law precision 本身具有 storage/execution-depth Pareto” 的直接一般化。

## 14. Scope boundary

当前 executable theorem 假设 finite total deterministic transformations。

对 partial actions，semantic effect object 必须保留 DOMAIN。对 multivalued relations，则必须保留 declared support/count/witness interface。对 infinite 但 finitely parameterized 的 normal-form monoid，table enumeration 可能不可能，但 formulaic algebra 仍可能存在。

所以 finite transformation monoid 是一个干净的 positive owner，不替代 richer operation semantics。

## Owner-local assets

- `src/enterprise_math/semantic_word_normalizer.py`；
- `src/enterprise_math/semantic_word_normalizer_resources.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

Finite transformation monoid、Cayley table、automata normalization 与 parallel associative reduction 都是标准既有 algebra / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 semantic-normalizer storage/depth resource specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
