# Semantic Precision 与 Representation Resources 的分层

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

本文不新增 Foundation Question。它是在 semantic-preorder、continuation、coefficient-factorization 与 future-law compilation 结果之后，对“precision”一词做一次更严格的架构澄清。

核心修正是：

> **semantic precision 与承载这份 precision 的 representation resource cost 是不同层。**

两个 representations 可以实现完全相同的 declared future theory，却在 storage、arithmetic width、channel count、work 与 execution depth 上相差巨大。

## 1. 先确定 semantic precision

相对于 declared future theory T，representation 首先必须回答项目已经建立的 semantic questions：

- 哪些 fine states 仍然 equivalent？
- 哪些 operations 真正 descend？
- DOMAIN / definedness 是否保留？
- 哪些 RELATION / witness distinctions 仍可见？
- 哪些 coefficient laws 与 reflection guarantees 有效？
- representation 是 recursively executable state，还是只够回答一次 terminal query？

这些共同决定 task-relative semantic capability profile。

若 representation 丢掉 required capability，那不是 implementation tradeoff，而是 semantic 上真的太粗。

## 2. Resource comparison 只发生在同一 semantic-equivalence fiber 内

假设两个 representations 都实现同一个 exact T-semantics，可以恢复相同的 declared state / output / operation interface。

则对该 task，它们位于同一个 semantic-equivalence class 中。

只有**在这个 class 内**，才应该比较：

- state storage；
- rule / effect table storage；
- coefficient bit width；
- parallel channel count；
- preprocessing / cache construction；
- normalization work；
- execution depth；
- reconstruction / synchronization cost。

这些 exact implementations 的 nondominated 集合形成 representation Pareto frontier。

## 3. 更多 stored rules 不等于更高 semantic precision

Stage131 的 chain example 已经说明这一点。

Sparse adjacent / Hasse basis 与 full transitive implication table 可以生成同一个 closure law。

Full table 之所以更快，是因为它预计算了更多 consequences。它并不自动表示一个更细的 semantic world。

所以：

`more rules`

有时真正意味着：

`more cached execution structure`，

而不是：

`more semantic precision`。

只要 rule table 是从同一个 exact law 派生出来，就应坚持这一分层。

## 4. CRT coefficient factorization：相同 arithmetic semantics，不同 resources

固定一个 exact modular arithmetic content L。

CRT 允许多种 exact representation：

- 一个宽 mod-L channel；
- 多个较窄 coprime channels；
- fully split prime channels。

它们拥有完全相同的 integer-equality / reflection semantics。

变化的是：

- channel count；
- peak arithmetic width；
- rounded storage width；
- optional CRT reconstruction depth；
- parallel execution opportunity。

例如 `L=210` 时，exact nondominated `(channels,peak bits)` points 是：

`(1,8),(2,4),(3,3)`。

第四条 fully split channel 已不再降低 peak width，因此被支配。

这证明 arithmetic precision 自己可以拥有多种 semantically identical operational factorizations。

## 5. Literal future-word caching：同一 operation language，不同 runtime depth

对 k 个 action generators，把长度不超过 block depth d 的所有 literal word effects 预存下来。

Storage：

`sum_(i=1)^d k^i`。

长度 H 的 word 需要：

`ceil(H/d)`

个 cached rounds。

两个 endpoints：

- 只存 generators：storage 小、H rounds；
- 存 full horizon table：storage 指数级、1 round。

所有中间 nondominated caches 都在执行**同一个 exact literal future law**。

所以它们的区别是 representation cost，而不是 semantic refinement。

## 6. Semantic word quotient：literal syntax 数量与 exact operation 数量不同

许多 literal words 可以诱导同一个 exact operation。

按 exact transformation equality quotient literal words，可得到 semantic operation monoid。

这可能极大降低 effect 数量，但新的 representation 必须提供 word-to-effect normalizer。

因此：

`number of literal rules / words`

与

`number of exact semantic operations`

是不同 complexity coordinates。

两者任何一个都不能单独决定 runtime cost。

## 7. Tabulated semantic algebra 与 formulaic semantic algebra

即使知道 semantic operations 有多少个，也不能推出 law storage 有多大。

Commuting-idempotent mask family 有：

`m=2^k`

个 exact operations。

Generic Cayley table 与 effect-action table 都有 `4^k` entries。

但每个 operation 只是一个 k-bit mask，composition 是 bitwise OR，state action 也是同一个 OR formula。

因此一个很大的 exact semantic algebra 仍然可以有非常紧凑的 exact presentation。

这证明：

`semantic algebra cardinality`

与

`semantic algebra presentation complexity`

是不同资源。

## 8. Work / depth 也由 representation 决定

同一个 formulaic OR normalizer 用 runtime circuit work 替代 exponential table：

- 长度 H word 的 total bit work：`kH`；
- parallel normalization depth：`ceil(log2 H)`；
- 再做一次 state application。

所以 compact law formula 可以降低 memory，同时增加 runtime work，而 semantic law 完全不变。

正确的 resource vector 必须包含 **work**，不能只看 storage 与 depth。

## 9. Sufficient answer 与 sufficient state 仍是 semantic boundary

Representation Pareto 不能用来掩盖 semantic mismatch。

Terminal trace answer 可能足以回答某个 query，却太粗，不能作为下一轮 future executable state。Continuation-closure theorem 正是测量恢复 operation stability 需要增加哪些 distinctions。

这种 repair 改变的是 semantic capability，必须发生在 resource optimization **之前**。

只有 required executable state 已经确定后，才能把不同 encodings / caches / factorizations 当作 resource-equivalent implementations 比较。

## 10. Nonrealizable semantic join 仍然必须 lift representation

同理，如果 joined future theory 要求的 capabilities 在当前 representation family 中无法同时实现，那么再怎么调 cache、table 或 factorization 都无法解决问题。

必须先 lift state / representation type，使 semantic join 可实现。

Resource Pareto 从 semantic realizability 之后才开始。

## 11. 建议采用 two-level precision architecture

对 declared task T，把 precision questions 分成两层。

### Level A — semantic precision / capability

先确定 T 所需的 minimum exact state/interface：

- observation kernel；
- DOMAIN / RELATION / witness channels；
- coefficient reflection requirements；
- safe operation language；
- continuation / executable-state closure。

这一层由 task-relative semantic precision preorder 排序。

### Level B — representation resources

在实现该 semantic object 的所有 exact representations 中，优化资源向量：

`rho(R)=(state bits, law storage, coefficient width, channel count, preprocessing, work, depth, reconstruction cost)`。

这里不必存在一个 least representation；保留 Pareto frontier。

## 12. Exact-law compiler 才是 operational resource object

做资源分析时，一个 law 不应只被看成 extensional rule set，而应视为一个 **exact compiler / executor package**，至少要能：

1. identify / decode represented state；
2. normalize 或 locate declared future operation；
3. 在 represented state 上 exact execute；
4. expose declared outputs / witness channels。

不同 packages 可以实现相同 semantic law，但 resource vectors 完全不同。

Stage131 应比较的是这些 compiler packages，而不是只比较“有多少条规则”。

## 13. Compression claim 必须把 compiler cost 算进去

Semantic effect store 可能远小于 literal word table，但若 effect ID 的计算仍然要 replay whole word，execution depth 会回来。

Formulaic normal form 可以消掉 Cayley table，但会引入 arithmetic / circuit work。

Split CRT 可以降低 peak arithmetic width，但 scalar consumer 可能要支付 reconstruction depth。

因此每一个 compression claim 都必须说明它假设了什么 decoder / normalizer / executor。

## 14. Stage131 原表述应进一步 sharpen

更安全的说法是：

> 同一个 exact relation / future law 可以拥有多种 operational representations，它们在 storage、work、execution depth 上成本不同。若 declared future semantics 完全相同，这些差异属于 representation-resource Pareto，而不是 semantic precision difference。

只有 representation 真正增加或丢失了 task-relevant distinctions / capabilities，semantic precision 才发生变化。

## 15. Foundation routing rule

今后比较两个 candidate precisions 时，按以下顺序：

1. 它们是否实现同一个 declared future semantics？
2. 若否，用 semantic capability preorder 比较；
3. 若是，不要因为 table/state 更大就自动叫“更精确”；
4. 比较 operational resource vectors，找 nondominated Pareto points；
5. decoder / normalizer / reconstruction cost 必须一起进入比较，不能只算 stored payload。

## 16. Evidence routes

支持本文 synthesis 的近期 executable research 包括：

- task-relative semantic precision preorder；
- coarsest operation-safe / partial / relation-support state repair；
- continuation debt from terminal answer to executable state；
- bounded local-law reflection 与 contextual decoding；
- constrained modular sensor Set Cover；
- CRT sensor factorization Pareto；
- literal future-word block-cache Pareto；
- finite semantic transformation-monoid normalizers；
- formulaic commuting-idempotent word algebra。

这些仍然是 research / Draft evidence；本文不会自动把它们 promote 为 canonical Foundation。

## Prior-art / status

Time-memory tradeoff、CRT、automata / monoid、circuit representation 与 Pareto optimization 都是标准既有数学 / CS。Enterprise Math 在这里的价值是 precision-first routing：把 **保留了什么 semantic world** 与 **怎样 operationally 表示同一个 exact world law** 严格分开。

No new FQ。无 canonical-main 或 `EXECUTABLE_CHECKED` claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
