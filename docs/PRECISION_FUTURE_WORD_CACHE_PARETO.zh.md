# Future-Law Word Cache：Storage 与 Execution Depth Pareto

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Stage131 最初从 unary chain 中发现：同一个 closure law 可以用较小 generator basis 换较多 inference rounds，也可以用更大的 explicit rule table 换较浅 execution depth。

同一 resource law 可以通过 future word effect 的 block caching 推广到任意 finite action language。

## 1. Literal block-cache model

设 declared action alphabet 有 k 个 named generators，最大 future word horizon 为 H。

选 cache depth d，满足 `1<=d<=H`。

预存**所有长度1到d的非空 literal words** 的 exact effects。

Literal cache entry 数是：

`S(k,d)=sum_(i=1)^d k^i`。

当 k>1：

`S(k,d)=k*(k^d-1)/(k-1)`。

当 k=1：

`S(1,d)=d`。

## 2. Exact execution depth

任意长度 h 的 word 都能拆成 consecutive blocks，每块长度至多 d。

因此 execution rounds 为：

`R(h,d)=ceil(h/d)`。

在当前 block-cache model 中，这个 bound 是最优的：一个 cached primitive 最多覆盖 d 个 input action symbols，所以长度 h 的 word 不可能用少于 `ceil(h/d)` 个 cached primitives 表达。

## 3. Exact round-budget design

给定 horizon H 与 worst-case runtime budget r，最小可行 cache depth 精确为：

`d_min=ceil(H/r)`，

当 r>=H 时 d_min=1。

Literal storage 随 d 严格上升，因此这个 d 同时给出满足 round budget 的 minimum literal-cache storage：

`S(k,ceil(H/r))`。

## 4. 两个 endpoint resource laws

### Generator-only execution

取 d=1。

- storage：k 个 generator effects；
- worst-case runtime：H rounds。

### Full word table through H

取 d=H。

- storage：`sum_(i=1)^H k^i`；
- worst-case runtime：1 次 lookup/application round。

### Intermediate block caches

任何 `1<d<H` 只要真正降低 `ceil(H/d)`，就提供 strict time-memory compromise。

对 noncommuting / free word language，storage 会随 d 指数增长。

## 5. Sharp free-word storage witness

Owner 构造 finite prefix-append transition system：

- states 是所有长度<=d 的 action words，再加一个 absorbing overflow state；
- action a 在未超过 depth 时 append symbol a。

任意两个不同 words `w`（长度<=d）都会把 empty state 送到不同 prefix state。

因此所有 cached word transformations 都不同：

`#unique effects through d = S(k,d)`。

所以 literal exponential storage bound 即使在 finite deterministic state system 中也可以 worst-case sharp。

## 6. Discrete Pareto frontier

由于 storage 随 d 严格增加，一个 cache depth nondominated，当且仅当它是某个 distinct runtime round count 的**最小**可行 depth。

Pareto cache depths 精确等于：

`{ceil(H/r): r=1,...,H}`

去重后的集合。

因此 frontier 的 depth locations 只由 H 决定，与 action count k 无关。k 只决定每个 point 的 storage 有多贵，通常会极大改变成本数量级。

## 7. Frontier 只有 O(sqrt(H)) 个 points

利用：

`ceil(H/r)=floor((H-1)/r)+1`，

经典 quotient-value decomposition 给出只有 O(sqrt H) 个 distinct values。

本 branch 使用简单上界：

`#Pareto points <= 2*ceil(sqrt H)`。

所以虽然 cache depth 有 H 个候选，真正 nondominated 的 points 是稀疏的。

## 8. Sharp binary H=8 example

k=2、H=8 时，nondominated cache depths 是：

`d=1,2,3,4,8`。

对应 exact resource pairs `(literal entries, worst-case rounds)`：

- `(2,8)`；
- `(6,4)`；
- `(14,3)`；
- `(30,2)`；
- `(510,1)`。

Depth5、6、7 都被支配：storage 更大，但 runtime 仍然是2 rounds。

## 9. Literal storage 与 semantic effect storage 是两回事

Literal table 每个 word block 都存一个 key。但不同 words 可能诱导同一个 exact operation。

定义：

`N_d=# distinct transformations induced by words of length<=d`。

总有：

`N_d <= S(k,d)`。

差距可以极大。

例如：

- 两个不同 generator names 都实现 identity：任意 d 下 `N_d=1`，而 literal storage 仍指数增长；
- identity + two-state flip：`N_d=2`，但 literal words 数是 `2^(d+1)-2`。

## 10. Semantic compression 不是免费的 O(1) lookup

只知道 unique effects 只有 `N_d` 个，并不能自动把一个 arbitrary literal block O(1) 映射到正确 effect。

还必须提供一个 **word-to-effect / exact normal-form compiler**。

若 compiler 只是把 d 个 generators 重新 replay 一遍，block cache 的 runtime 优势就消失。若 compiler 利用 compact algebraic normal form，它自己的 storage / computation cost 必须被计入。

因此下一层 resource problem 不是简单：

`literal storage -> unique effect storage`，

而是：

`literal table storage`

versus

`semantic effect store + normalization compiler cost`。

P024 的 guarded `(T,H)` exact operational normal form 正是这类结构的具体实例。

## 11. 与 rooted circuits / chain basis 的关系

Stage131 原始 chain example 比较：

- sparse Hasse / adjacent basis：derivation depth 较长；
- dense transitive / circuit table：execution 较浅。

Word-cache theorem 的 combinatorial table 不完全相同，但暴露的是同一 structural principle：

> exact law semantics 固定以后，可以在 precomputed consequence storage 与 future composition depth 之间交换。

对 multi-action free language，storage side 可以比 unary-chain 情况更剧烈地增长到 exponential。

## 12. 与 CRT factorization Pareto 的关系

前一代 CRT generation 在同一个 coefficient law 内交换 arithmetic width、channel count 与 optional reconstruction depth。

本 generation 在同一个 operation language 内交换 cached future-law storage 与 action-composition depth。

因此至少已有两个独立 representation axes：

- factorize **coefficient state**；
- precompute / factorize **future operation language**。

完整 precision compiler 可能必须同时优化两条轴。

## 13. Scope boundary

本文假设：

- finite total deterministic operations；
- literal word effects exact；
- cache lookup/application 计作一个 operation round；
- storage 计 table entries，不细算 byte-level key encoding；
- cached effects 本身能放进所选 state representation。

Partial operations 需要 DOMAIN-aware word semantics；multivalued relations 需要对应 branching / witness interface。选择正确 operation normal form 后，同一 cache principle 可能继续成立，但不能因此擦掉这些 semantic channels。

## Owner-local assets

- `src/enterprise_math/future_word_cache_pareto.py`；
- `src/enterprise_math/future_word_cache_frontier.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

Time-memory tradeoff、block caching、transformation semigroup 与 quotient-value arithmetic 都是标准既有数学 / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 Stage131 future-law block-cache Pareto specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
